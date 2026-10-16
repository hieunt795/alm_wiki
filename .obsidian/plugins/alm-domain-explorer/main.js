"use strict";
// ALM Domain Explorer — xem node 02_wiki theo domain: danh sách theo type, hoặc graph dạng layer.
// Chỉ đọc frontmatter qua metadataCache; không ghi file nào trong vault.
const { Plugin, ItemView, Keymap, TFile, debounce, parseYaml, setIcon } = require("obsidian");

const VIEW_TYPE = "alm-domain-explorer";
const WIKI_ROOT = "02_wiki/";
const TAXONOMY_PATH = "03_meta/taxonomy.md";
const UNASSIGNED = "__none__";

// Dùng khi không đọc được khối ```yaml taxonomy
const FALLBACK_DOMAINS = {
  macro: "Macroeconomic",
  product: "Financial Product",
  alm: "ALM",
  basel: "Basel",
  "vn-reg": "VN Regulator",
};

// Thứ tự nhóm theo cây chọn node type trong CLAUDE.md
const TYPES = [
  ["regulation", "Regulation"],
  ["entity", "Entity"],
  ["instrument", "Instrument"],
  ["metric", "Metric"],
  ["model", "Model"],
  ["concept", "Concept"],
  ["synthesis", "Synthesis"],
  ["source", "Source note"],
];
const TYPE_LABEL = Object.fromEntries(TYPES);
const TYPE_RANK = Object.fromEntries(TYPES.map(([t], i) => [t, i]));
const MATURITIES = ["draft", "reviewed", "canonical"];

// Thứ tự cột của graph chế độ "type": chọn để phần lớn cạnh relation (chủ thể → đối tượng)
// đi từ trái sang phải trên dữ liệu wiki tháng 10/2026 (vd. concept→metric, synthesis→metric).
const TYPE_FLOW = ["source", "synthesis", "regulation", "instrument", "model", "concept", "metric", "entity"];

// Nhóm relation theo 3 nhóm trong 03_meta/taxonomy.md; quyết định màu và kiểu nét của cạnh
const REL_GROUPS = {
  "part-of": "component",
  measures: "control", governs: "control", limits: "control",
  drives: "impact", "input-to": "impact",
};
const GROUP_LABEL = {
  component: "Thành phần: part-of",
  control: "Đo lường / quản trị / giới hạn: measures, governs, limits",
  impact: "Tác động / đầu vào: drives, input-to",
  other: "Khác: hedges, priced-by, exposed-to, implements, supersedes, amends",
};

// Kích thước layout graph (đơn vị SVG)
const COL_GAP = 260;
const ROW_GAP = 26;
const LABEL_MAX = 30;

// Chế độ cụm: màu từng cụm, khoá cho node không có citation, số nhãn hiện mặc định
const CLUSTER_COLORS = ["blue", "cyan", "green", "yellow", "orange", "red", "pink", "purple"];
const NO_SOURCE = "__nocite__";
const LABEL_TOP = 15;

const DEFAULT_SETTINGS = {
  domain: "alm",
  scope: "any", // any | primary (domains[0])
  maturity: "",
  showSources: false,
  showInactive: true,
  relation: "",
  layerMode: "cluster", // cluster | type | depth
  showLabels: false,
  crossOnly: false,
  collapsed: {},
};

function asList(v) {
  if (v == null || v === "") return [];
  return (Array.isArray(v) ? v : [v]).map((x) => String(x).trim()).filter(Boolean);
}

function linkpath(v) {
  return String(v || "").replace(/^\s*\[\[/, "").replace(/\]\]\s*$/, "").split("|")[0].split("#")[0].trim();
}

function shorten(s) {
  return s.length > LABEL_MAX ? s.slice(0, LABEL_MAX - 1) + "…" : s;
}

// createSvg của Obsidian thêm class bằng classList.add(chuỗi), nên chuỗi nhiều class (có dấu cách) sẽ ném lỗi.
// Mọi phần tử SVG trong plugin tạo qua hàm này để tách class thành mảng.
function svgEl(parent, tag, o) {
  if (o && typeof o.cls === "string") o = Object.assign({}, o, { cls: o.cls.split(/\s+/).filter(Boolean) });
  return parent.createSvg(tag, o);
}

// Gán cột theo độ sâu relation: phá chu trình bằng DFS (đánh dấu back edge, đảo chiều khi xếp tầng),
// xếp tầng theo longest path; node không có cạnh nằm ở cột cuối.
function depthColumns(paths, edges, deg) {
  const out = new Map(paths.map((p) => [p, []]));
  const indeg = new Map(paths.map((p) => [p, 0]));
  for (const e of edges) {
    out.get(e.from).push(e);
    indeg.set(e.to, indeg.get(e.to) + 1);
  }

  const state = new Map();
  const visit = (p) => {
    state.set(p, 1);
    for (const e of out.get(p)) {
      const s = state.get(e.to) || 0;
      if (s === 1) e.back = true;
      else if (s === 0) visit(e.to);
    }
    state.set(p, 2);
  };
  for (const p of [...paths].sort((a, b) => indeg.get(a) - indeg.get(b))) {
    if (!state.get(p)) visit(p);
  }

  const succ = new Map(paths.map((p) => [p, []]));
  const dagIn = new Map(paths.map((p) => [p, 0]));
  for (const e of edges) {
    const [u, v] = e.back ? [e.to, e.from] : [e.from, e.to];
    succ.get(u).push(v);
    dagIn.set(v, dagIn.get(v) + 1);
  }

  const layer = new Map(paths.map((p) => [p, 0]));
  const queue = paths.filter((p) => dagIn.get(p) === 0);
  while (queue.length) {
    const u = queue.shift();
    for (const v of succ.get(u)) {
      layer.set(v, Math.max(layer.get(v), layer.get(u) + 1));
      dagIn.set(v, dagIn.get(v) - 1);
      if (dagIn.get(v) === 0) queue.push(v);
    }
  }

  const connected = paths.filter((p) => deg.get(p) > 0);
  const isolated = paths.filter((p) => deg.get(p) === 0);
  const nLayers = connected.length ? Math.max(...connected.map((p) => layer.get(p))) + 1 : 0;
  const cols = Array.from({ length: nLayers }, () => []);
  for (const p of connected) cols[layer.get(p)].push(p);
  const headers = cols.map((_, i) => `Tầng ${i + 1}`);
  if (isolated.length) {
    cols.push(isolated);
    headers.push("Không liên kết");
  }
  return { cols, headers };
}

// Layout kiểu neural network: mỗi cột là một tầng (theo type hoặc theo độ sâu relation),
// thứ tự node trong cột sắp bằng barycenter của láng giềng để giảm cạnh cắt nhau.
function layoutGraph(nodes, edges, mode) {
  const paths = nodes.map((n) => n.file.path);
  const byPath = new Map(nodes.map((n) => [n.file.path, n]));
  const nbrs = new Map(paths.map((p) => [p, []]));
  const deg = new Map(paths.map((p) => [p, 0]));
  for (const e of edges) {
    nbrs.get(e.from).push(e.to);
    nbrs.get(e.to).push(e.from);
    deg.set(e.from, deg.get(e.from) + 1);
    deg.set(e.to, deg.get(e.to) + 1);
  }

  let cols, headers;
  if (mode === "depth") {
    ({ cols, headers } = depthColumns(paths, edges, deg));
  } else {
    const present = [...new Set(nodes.map((n) => n.type))].sort((a, b) => {
      const ia = TYPE_FLOW.indexOf(a), ib = TYPE_FLOW.indexOf(b);
      return (ia < 0 ? 99 : ia) - (ib < 0 ? 99 : ib) || a.localeCompare(b);
    });
    cols = present.map((t) => paths.filter((p) => byPath.get(p).type === t));
    headers = present.map((t) => TYPE_LABEL[t] || t);
  }

  const byTypeTitle = (a, b) => {
    const na = byPath.get(a), nb = byPath.get(b);
    return ((TYPE_RANK[na.type] ?? 99) - (TYPE_RANK[nb.type] ?? 99)) || na.title.localeCompare(nb.title, "vi");
  };
  cols.forEach((c) => c.sort(byTypeTitle));

  const pos = new Map();
  const index = () => cols.forEach((c) => c.forEach((p, i) => pos.set(p, i - (c.length - 1) / 2)));
  index();
  const reorder = (c) => {
    const key = new Map(c.map((p) => {
      const ns = nbrs.get(p);
      return [p, ns.length ? ns.reduce((s, q) => s + pos.get(q), 0) / ns.length : pos.get(p)];
    }));
    c.sort((a, b) => key.get(a) - key.get(b));
  };
  for (let iter = 0; iter < 4; iter++) {
    for (let i = 0; i < cols.length; i++) reorder(cols[i]);
    index();
    for (let i = cols.length - 1; i >= 0; i--) reorder(cols[i]);
    index();
  }

  const coords = new Map();
  cols.forEach((c, li) => c.forEach((p) => coords.set(p, { x: li * COL_GAP, y: pos.get(p) * ROW_GAP })));
  const maxRows = Math.max(1, ...cols.map((c) => c.length));
  return { cols, headers, coords, deg, height: (maxRows - 1) * ROW_GAP };
}

// Layout cụm kiểu radial: mỗi cụm (theo node.source) là một vòng tròn trên vành quanh tâm,
// diện tích tỉ lệ số node; cụm liên kết nhiều với nhau được xếp cạnh nhau.
// Trong cụm: khởi tạo hình hoa hướng dương (node nhiều cạnh ở giữa) rồi chạy Fruchterman–Reingold
// giới hạn trong vòng tròn, có lực kéo nhẹ về phía các cụm mà node liên kết tới.
function layoutClusters(nodes, edges) {
  const paths = nodes.map((n) => n.file.path);
  const byPath = new Map(nodes.map((n) => [n.file.path, n]));
  const keyOf = new Map(nodes.map((n) => [n.file.path, n.source || NO_SOURCE]));
  const deg = new Map(paths.map((p) => [p, 0]));
  for (const e of edges) {
    deg.set(e.from, deg.get(e.from) + 1);
    deg.set(e.to, deg.get(e.to) + 1);
  }
  const radius = (p) => 4 + Math.min(6, Math.sqrt(deg.get(p)) * 1.2);

  const groups = new Map();
  for (const p of paths) {
    const k = keyOf.get(p);
    if (!groups.has(k)) groups.set(k, { key: k, members: [] });
    groups.get(k).members.push(p);
  }

  const cross = new Map();
  const pairKey = (a, b) => (a < b ? a + "\u0000" + b : b + "\u0000" + a);
  for (const e of edges) {
    const a = keyOf.get(e.from), b = keyOf.get(e.to);
    if (a !== b) cross.set(pairKey(a, b), (cross.get(pairKey(a, b)) || 0) + 1);
  }
  const weight = (a, b) => cross.get(pairKey(a, b)) || 0;
  const bySize = (a, b) => b.members.length - a.members.length || a.key.localeCompare(b.key);
  const rest = [...groups.values()].sort(bySize);
  const order = [rest.shift()];
  while (rest.length) {
    const last = order[order.length - 1].key;
    rest.sort((a, b) => weight(last, b.key) - weight(last, a.key) || bySize(a, b));
    order.push(rest.shift());
  }

  order.forEach((g, i) => {
    g.r = 40 + 19 * Math.sqrt(g.members.length);
    g.color = i;
  });
  const gap = 50, hub = 90;
  const maxR = Math.max(...order.map((g) => g.r));
  const sumD = order.reduce((s, g) => s + 2 * g.r + gap, 0);
  const R = Math.max(hub + maxR + 80, sumD / (2 * Math.PI));
  let acc = 0;
  for (const g of order) {
    const span = ((2 * g.r + gap) / sumD) * 2 * Math.PI;
    g.angle = -Math.PI / 2 + acc + span / 2;
    acc += span;
    g.cx = R * Math.cos(g.angle);
    g.cy = R * Math.sin(g.angle);
  }
  const groupOf = new Map(order.map((g) => [g.key, g]));

  const coords = new Map();
  for (const g of order) {
    const m = g.members.length, inner = Math.max(1, g.r - 14);
    g.members.sort((a, b) => deg.get(b) - deg.get(a) || byPath.get(a).title.localeCompare(byPath.get(b).title, "vi"));
    const idx = new Map(g.members.map((p, i) => [p, i]));
    const x = [], y = [];
    g.members.forEach((_, i) => {
      const rr = m === 1 ? 0 : inner * Math.sqrt((i + 0.5) / m), th = i * 2.399963;
      x.push(rr * Math.cos(th));
      y.push(rr * Math.sin(th));
    });

    const local = [], pull = g.members.map(() => [0, 0]);
    for (const e of edges) {
      const a = keyOf.get(e.from), b = keyOf.get(e.to);
      if (a === g.key && b === g.key) {
        local.push([idx.get(e.from), idx.get(e.to)]);
      } else if (a === g.key || b === g.key) {
        const [mine, other] = a === g.key ? [e.from, b] : [e.to, a];
        const o = groupOf.get(other);
        const vx = o.cx - g.cx, vy = o.cy - g.cy, d = Math.hypot(vx, vy) || 1;
        const pv = pull[idx.get(mine)];
        pv[0] += vx / d;
        pv[1] += vy / d;
      }
    }

    if (m > 1) {
      const K = Math.sqrt((Math.PI * inner * inner) / m) * 0.8;
      let t = inner * 0.2;
      for (let it = 0; it < 150; it++) {
        const dx = new Array(m).fill(0), dy = new Array(m).fill(0);
        for (let i = 0; i < m; i++) {
          for (let j = i + 1; j < m; j++) {
            const vx = x[i] - x[j], vy = y[i] - y[j];
            const d = Math.max(0.01, Math.hypot(vx, vy)), f = (K * K) / (d * d);
            dx[i] += vx * f; dy[i] += vy * f;
            dx[j] -= vx * f; dy[j] -= vy * f;
          }
        }
        for (const [a, b] of local) {
          const vx = x[a] - x[b], vy = y[a] - y[b];
          const f = Math.max(0.01, Math.hypot(vx, vy)) / K;
          dx[a] -= vx * f; dy[a] -= vy * f;
          dx[b] += vx * f; dy[b] += vy * f;
        }
        for (let i = 0; i < m; i++) {
          dx[i] += pull[i][0] * K * 0.3;
          dy[i] += pull[i][1] * K * 0.3;
          const len = Math.hypot(dx[i], dy[i]);
          if (len > 0) {
            const k = Math.min(len, t) / len;
            x[i] += dx[i] * k;
            y[i] += dy[i] * k;
          }
          const rr = Math.hypot(x[i], y[i]);
          if (rr > inner) {
            x[i] *= inner / rr;
            y[i] *= inner / rr;
          }
        }
        t *= 0.97;
      }

      // Tách các cặp node còn đè nhau, vẫn giữ trong vòng tròn
      const rad = g.members.map(radius);
      for (let it = 0; it < 60; it++) {
        let moved = false;
        for (let i = 0; i < m; i++) {
          for (let j = i + 1; j < m; j++) {
            const vx = x[i] - x[j], vy = y[i] - y[j], d = Math.hypot(vx, vy) || 0.01;
            const need = rad[i] + rad[j] + 3;
            if (d >= need) continue;
            const k = (need - d) / 2 / d;
            x[i] += vx * k; y[i] += vy * k;
            x[j] -= vx * k; y[j] -= vy * k;
            moved = true;
          }
        }
        for (let i = 0; i < m; i++) {
          const rr = Math.hypot(x[i], y[i]);
          if (rr > inner) {
            x[i] *= inner / rr;
            y[i] *= inner / rr;
          }
        }
        if (!moved) break;
      }
    }
    g.members.forEach((p, i) => coords.set(p, { x: g.cx + x[i], y: g.cy + y[i] }));
  }

  const hubRing = Math.max(70, (R - maxR) * 0.55);
  return { clusters: order, coords, deg, radius, keyOf, hubRing, extent: R + maxR + 60 };
}

class DomainExplorerView extends ItemView {
  constructor(leaf, plugin) {
    super(leaf);
    this.plugin = plugin;
    this.query = "";
    this.mode = "list";
    this.hoverPopover = null;
    this.uid = Math.random().toString(36).slice(2, 8);
    this.transform = null;
    this.graphKey = "";
    this.focusCluster = null;
  }

  getViewType() { return VIEW_TYPE; }
  getDisplayText() { return this.mode === "graph" ? "Domain graph" : "Domain explorer"; }
  getIcon() { return this.mode === "graph" ? "network" : "layers"; }

  getState() {
    return { ...super.getState(), mode: this.mode };
  }

  async setState(state, result) {
    if (state && (state.mode === "list" || state.mode === "graph")) this.mode = state.mode;
    this.applyMode();
    await super.setState(state, result);
  }

  async onOpen() {
    const root = this.contentEl;
    root.empty();
    root.addClass("alm-dx");

    const modeBar = root.createDiv("alm-dx-modes");
    this.modeBtns = {};
    for (const [mode, text] of [["list", "Danh sách"], ["graph", "Graph"]]) {
      const btn = modeBar.createEl("button", { text });
      btn.addEventListener("click", () => this.setMode(mode));
      this.modeBtns[mode] = btn;
    }
    const tabBtn = modeBar.createEl("button", { cls: "clickable-icon alm-dx-tab-btn", attr: { "aria-label": "Mở graph ở tab mới" } });
    setIcon(tabBtn, "maximize-2");
    tabBtn.addEventListener("click", () => this.plugin.openGraphTab());

    this.chipsEl = root.createDiv("alm-dx-chips");

    const controls = root.createDiv("alm-dx-controls");
    const search = controls.createEl("input", {
      type: "search",
      cls: "alm-dx-search",
      attr: { placeholder: "Lọc theo title, alias, id…" },
    });
    search.addEventListener("input", () => {
      this.query = search.value.trim().toLowerCase();
      this.refresh();
    });

    const row = controls.createDiv("alm-dx-row");
    this.addSelect(row, "scope", [["any", "Mọi vị trí"], ["primary", "Chỉ primary"]],
      "Mọi vị trí: domain xuất hiện bất kỳ đâu trong domains. Chỉ primary: domain là phần tử đầu.");
    this.addSelect(row, "maturity", [["", "Mọi maturity"], ...MATURITIES.map((m) => [m, m])]);

    const row2 = controls.createDiv("alm-dx-row");
    this.addToggle(row2, "showSources", "Source notes");
    this.addToggle(row2, "showInactive", "Superseded/retired");

    this.descEl = root.createDiv("alm-dx-desc");
    this.listEl = root.createDiv("alm-dx-list");

    this.graphEl = root.createDiv("alm-dx-graph");
    const toolbar = this.graphEl.createDiv("alm-dx-row alm-dx-graph-toolbar");
    this.addSelect(toolbar, "layerMode",
      [["cluster", "Cụm theo nguồn"], ["type", "Tầng theo type"], ["depth", "Tầng theo độ sâu relation"]],
      "Cụm: node gom theo source note được cite nhiều nhất. Type: mỗi cột là một node type. " +
      "Độ sâu: xếp tầng theo chuỗi relation dài nhất (có thể ra nhiều tầng).");
    this.relSelect = toolbar.createEl("select", { cls: "dropdown" });
    this.relSelect.addEventListener("change", () => this.plugin.update({ relation: this.relSelect.value }));
    const fitBtn = toolbar.createEl("button", { text: "Fit" });
    fitBtn.addEventListener("click", () => this.fitGraph());
    this.clusterOpts = this.graphEl.createDiv("alm-dx-row");
    this.addToggle(this.clusterOpts, "showLabels", "Mọi nhãn");
    this.addToggle(this.clusterOpts, "crossOnly", "Chỉ cạnh liên cụm");
    this.renderLegend(this.graphEl.createEl("details", { cls: "alm-dx-legend" }));
    this.svgWrap = this.graphEl.createDiv("alm-dx-svg-wrap");

    this.applyMode();
  }

  async onClose() {
    this.contentEl.empty();
  }

  onResize() {
    if (this.mode === "graph" && !this.transform) this.fitGraph();
  }

  setMode(mode) {
    this.mode = mode;
    this.applyMode();
    this.app.workspace.requestSaveLayout();
  }

  applyMode() {
    if (!this.listEl) return;
    const graph = this.mode === "graph";
    this.contentEl.toggleClass("is-graph", graph);
    this.listEl.toggle(!graph);
    this.graphEl.toggle(graph);
    for (const [m, btn] of Object.entries(this.modeBtns)) btn.toggleClass("mod-cta", m === this.mode);
    this.leaf.updateHeader?.();
    this.refresh();
  }

  addSelect(parent, key, options, title) {
    const sel = parent.createEl("select", { cls: "dropdown" });
    if (title) sel.title = title;
    for (const [value, text] of options) sel.createEl("option", { value, text });
    sel.value = this.plugin.settings[key];
    sel.addEventListener("change", () => this.plugin.update({ [key]: sel.value }));
  }

  addToggle(parent, key, label) {
    const lab = parent.createEl("label", { cls: "alm-dx-check" });
    const cb = lab.createEl("input", { type: "checkbox" });
    cb.checked = !!this.plugin.settings[key];
    lab.appendText(" " + label);
    cb.addEventListener("change", () => this.plugin.update({ [key]: cb.checked }));
  }

  renderLegend(det) {
    det.createEl("summary", { text: "Chú giải" });
    const types = det.createDiv("alm-dx-legend-row");
    for (const [t, label] of TYPES) {
      const item = types.createSpan("alm-dx-legend-item");
      item.createSpan({ cls: `alm-dx-dot t-${t}` });
      item.appendText(label);
    }
    const groups = det.createDiv("alm-dx-legend-col");
    for (const [g, label] of Object.entries(GROUP_LABEL)) {
      const item = groups.createDiv("alm-dx-legend-item");
      item.createSpan({ cls: `alm-dx-line g-${g}` });
      item.appendText(label);
    }
    det.createDiv({
      cls: "alm-dx-desc",
      text: "Mũi tên đi từ chủ thể sang đối tượng của relation. " +
        "Chế độ cụm: node gom theo source note được cite nhiều nhất trong thân bài, màu theo cụm; " +
        "click số hoặc tên cụm để focus (click lại để bỏ). " +
        "Chế độ tầng: màu theo type; cung bên trái cột là relation giữa hai node cùng tầng. " +
        "Chế độ độ sâu: nét đứt là cạnh nằm trong chu trình, vẽ ngược chiều layout; cột cuối là node không có cạnh trong phạm vi đang lọc. " +
        "Viền đậm: node canonical. Kéo để di chuyển, cuộn để zoom, Ctrl+hover để xem trước.",
    });
  }

  matches(node, domain) {
    const known = this.plugin.domains;
    if (domain === UNASSIGNED) return !node.domains.some((d) => d in known);
    if (this.plugin.settings.scope === "primary") return node.domains[0] === domain;
    return node.domains.includes(domain);
  }

  // Mọi bộ lọc trừ domain; số đếm trên chip dùng chung kết quả này
  filtered() {
    const s = this.plugin.settings;
    return this.plugin.collectNodes().filter((n) => {
      if (!s.showSources && n.type === "source") return false;
      if (!s.showInactive && n.status !== "active") return false;
      if (s.maturity && n.maturity !== s.maturity) return false;
      if (this.query && !n.search.includes(this.query)) return false;
      return true;
    });
  }

  refresh() {
    if (!this.listEl) return;
    const s = this.plugin.settings;
    const domains = this.plugin.domains;
    const nodes = this.filtered();

    const keys = Object.keys(domains);
    if (nodes.some((n) => this.matches(n, UNASSIGNED))) keys.push(UNASSIGNED);
    const current = keys.includes(s.domain) ? s.domain : keys[0];

    this.chipsEl.empty();
    for (const key of keys) {
      const chip = this.chipsEl.createEl("button", { cls: "alm-dx-chip" });
      if (key === current) chip.addClass("is-active");
      if (key === UNASSIGNED) chip.addClass("is-warning");
      chip.createSpan({ text: key === UNASSIGNED ? "Chưa gán" : this.plugin.domainLabel(key) });
      chip.createSpan({ cls: "alm-dx-count", text: String(nodes.filter((n) => this.matches(n, key)).length) });
      chip.title = key === UNASSIGNED ? "Node thiếu domains hoặc domain không có trong taxonomy" : domains[key];
      chip.addEventListener("click", () => this.plugin.update({ domain: key }));
    }

    this.descEl.setText(current === UNASSIGNED
      ? `Node thiếu domains hoặc domain không có trong ${TAXONOMY_PATH}.`
      : (domains[current] || ""));

    const visible = nodes.filter((n) => this.matches(n, current));
    if (this.mode === "graph") this.renderGraph(visible, current);
    else this.renderList(visible, current);
  }

  renderList(nodes, domain) {
    const s = this.plugin.settings;
    this.listEl.empty();
    if (!nodes.length) {
      this.listEl.createDiv({ cls: "alm-dx-empty", text: "Không có node nào khớp bộ lọc." });
      return;
    }

    const groups = new Map();
    for (const n of nodes) {
      if (!groups.has(n.type)) groups.set(n.type, []);
      groups.get(n.type).push(n);
    }
    const order = TYPES.map((t) => t[0]).concat([...groups.keys()].filter((t) => !TYPE_LABEL[t]).sort());

    for (const type of order) {
      const items = groups.get(type);
      if (!items) continue;
      items.sort((a, b) => a.title.localeCompare(b.title, "vi"));

      const det = this.listEl.createEl("details", { cls: "alm-dx-group" });
      det.open = !s.collapsed[type];
      det.addEventListener("toggle", () => {
        if (!!s.collapsed[type] === !det.open) return;
        s.collapsed[type] = !det.open;
        this.plugin.saveSettings();
      });
      const sum = det.createEl("summary");
      sum.createSpan({ text: TYPE_LABEL[type] || type });
      sum.createSpan({ cls: "alm-dx-count", text: String(items.length) });

      const ul = det.createEl("ul");
      for (const n of items) this.renderItem(ul, n, domain);
    }
  }

  renderItem(ul, n, domain) {
    const li = ul.createEl("li", { cls: "alm-dx-item" });
    if (n.status !== "active") li.addClass("is-inactive");

    const a = li.createEl("a", { cls: "alm-dx-link", text: n.title, href: "#" });
    a.title = n.file.path + (n.status !== "active" ? ` (${n.status})` : "");
    this.bindOpen(a, n);

    const meta = li.createDiv("alm-dx-meta");
    if (n.maturity) meta.createSpan({ cls: `alm-dx-badge mat-${n.maturity}`, text: n.maturity });
    n.domains.forEach((d, i) => {
      if (d === domain) return;
      const tag = meta.createSpan({ cls: "alm-dx-tag", text: d });
      if (i === 0) {
        tag.addClass("is-primary");
        tag.title = "Primary domain";
      }
    });
  }

  bindOpen(el, n) {
    el.addEventListener("click", (evt) => {
      evt.preventDefault();
      this.app.workspace.getLeaf(Keymap.isModEvent(evt)).openFile(n.file);
    });
    el.addEventListener("mouseover", (evt) => {
      this.app.workspace.trigger("hover-link", {
        event: evt, source: VIEW_TYPE, hoverParent: this, targetEl: el, linktext: n.file.path,
      });
    });
  }

  renderGraph(nodes, domain) {
    const s = this.plugin.settings;
    this.clusterOpts.toggle(s.layerMode === "cluster");

    // Danh sách relation lấy từ taxonomy; giữ lựa chọn hiện tại
    this.relSelect.empty();
    this.relSelect.createEl("option", { value: "", text: "Mọi relation" });
    for (const r of this.plugin.relationTypes) this.relSelect.createEl("option", { value: r, text: r });
    this.relSelect.value = s.relation;

    const byPath = new Map(nodes.map((n) => [n.file.path, n]));
    const edgeMap = new Map();
    for (const n of nodes) {
      for (const r of n.relations) {
        if (s.relation && r.type !== s.relation) continue;
        if (!r.target || r.target === n.file.path || !byPath.has(r.target)) continue;
        const key = n.file.path + "\u0000" + r.target;
        if (!edgeMap.has(key)) edgeMap.set(key, { from: n.file.path, to: r.target, types: [] });
        const e = edgeMap.get(key);
        if (!e.types.includes(r.type)) e.types.push(r.type);
      }
    }
    const edges = [...edgeMap.values()];

    // Giữ vị trí pan/zoom khi chỉ có nội dung node thay đổi; fit lại khi đổi domain/bộ lọc/bố cục
    const key = [domain, s.scope, s.maturity, s.showSources, s.showInactive, s.relation, s.layerMode, this.query].join("|");
    if (key !== this.graphKey) this.transform = null;
    this.graphKey = key;

    this.svgWrap.empty();
    if (!nodes.length) {
      this.svgWrap.createDiv({ cls: "alm-dx-empty", text: "Không có node nào khớp bộ lọc." });
      return;
    }

    const svg = svgEl(this.svgWrap, "svg", { cls: "alm-dx-svg" });
    const defs = svgEl(svg, "defs");
    for (const g of Object.keys(GROUP_LABEL)) {
      const m = svgEl(defs, "marker", {
        attr: {
          id: `alm-dx-arrow-${g}-${this.uid}`, viewBox: "0 0 10 10", refX: "9", refY: "5",
          markerWidth: "6", markerHeight: "6", orient: "auto-start-reverse",
        },
      });
      svgEl(m, "path", { cls: `alm-dx-arrow g-${g}`, attr: { d: "M0,0 L10,5 L0,10 z" } });
    }
    const vp = svgEl(svg, "g");
    this.viewport = vp;

    const ctx = { svg, vp, byPath, nodeEls: new Map(), incident: new Map(nodes.map((n) => [n.file.path, []])) };
    if (s.layerMode === "cluster") this.drawClusters(ctx, nodes, edges, domain);
    else this.drawLayers(ctx, nodes, edges);

    // Hover: làm nổi node, láng giềng và cạnh liên quan
    for (const [p, g] of ctx.nodeEls) {
      g.addEventListener("mouseenter", () => {
        svg.addClass("has-focus");
        g.addClass("is-hl");
        for (const { el, other } of ctx.incident.get(p)) {
          el.addClass("is-hl");
          ctx.nodeEls.get(other).addClass("is-hl");
        }
      });
      g.addEventListener("mouseleave", () => {
        svg.removeClass("has-focus");
        svg.querySelectorAll(".is-hl").forEach((el) => el.removeClass("is-hl"));
      });
    }

    this.bindPanZoom(svg);
    if (this.transform) this.applyTransform();
    else requestAnimationFrame(() => this.fitGraph());
  }

  drawNode(ctx, n, x, y, r, showLabel, extraCls, color) {
    const p = n.file.path;
    const g = svgEl(ctx.nodeLayer, "g", {
      cls: `alm-dx-node t-${n.type}` + (n.status !== "active" ? " is-inactive" : "") +
        (n.maturity ? ` mat-${n.maturity}` : "") + (extraCls ? ` ${extraCls}` : ""),
      attr: { transform: `translate(${x},${y})` },
    });
    if (color) g.style.setProperty("--alm-dx-cl", color);
    svgEl(g, "circle", { attr: { r } });
    if (showLabel) {
      svgEl(g, "text", { attr: { x: r + 4, dy: "0.32em" } }).textContent = shorten(n.title);
    }
    svgEl(g, "title").textContent =
      `${n.title}\n${n.type} · ${n.maturity || "—"} · ${n.domains.join(", ")}\n${p}`;
    this.bindOpen(g, n);
    ctx.nodeEls.set(p, g);
  }

  drawEdge(ctx, e, d, forward) {
    const group = REL_GROUPS[e.types[0]] || "other";
    const path = svgEl(ctx.edgeLayer, "path", {
      cls: `alm-dx-edge g-${group}` + (e.back ? " is-back" : ""),
      attr: { d },
    });
    path.setAttr(forward ? "marker-end" : "marker-start", `url(#alm-dx-arrow-${group}-${this.uid})`);
    svgEl(path, "title").textContent =
      `${ctx.byPath.get(e.from).title} —${e.types.join(", ")}→ ${ctx.byPath.get(e.to).title}` +
      (e.back ? "\n(cạnh trong chu trình, vẽ ngược chiều layout)" : "");
    ctx.incident.get(e.from).push({ el: path, other: e.to });
    ctx.incident.get(e.to).push({ el: path, other: e.from });
  }

  drawLayers(ctx, nodes, edges) {
    const L = layoutGraph(nodes, edges, this.plugin.settings.layerMode);
    const radius = (p) => 5 + Math.min(5, Math.sqrt(L.deg.get(p)));
    // Độ lồi của cung nối hai node cùng cột, tăng theo khoảng cách dọc
    const bulge = (dy) => 24 + Math.abs(dy) * 0.3;
    let maxBulge = 0;
    for (const e of edges) {
      const a = L.coords.get(e.from), b = L.coords.get(e.to);
      if (a.x === b.x) maxBulge = Math.max(maxBulge, bulge(b.y - a.y));
    }
    this.layoutBox = {
      minX: -20 - maxBulge * 0.75,
      maxX: (L.cols.length - 1) * COL_GAP + 200,
      minY: -L.height / 2 - 40,
      maxY: L.height / 2 + 20,
    };

    const headers = svgEl(ctx.vp, "g", { cls: "alm-dx-headers" });
    L.headers.forEach((h, i) => {
      const t = svgEl(headers, "text", {
        attr: { x: i * COL_GAP, y: -L.height / 2 - 24, "text-anchor": "middle" },
      });
      t.textContent = `${h} (${L.cols[i].length})`;
    });

    ctx.edgeLayer = svgEl(ctx.vp, "g", { cls: "alm-dx-edges" });
    for (const e of edges) {
      const a = L.coords.get(e.from), b = L.coords.get(e.to);
      let d, forward = true;
      if (a.x === b.x) {
        // Cùng cột: cung lồi sang trái, mũi tên ở node đích
        const k = bulge(b.y - a.y), x1 = a.x - radius(e.from), x2 = b.x - radius(e.to);
        d = `M${x1},${a.y} C${a.x - k},${a.y} ${b.x - k},${b.y} ${x2},${b.y}`;
      } else {
        forward = a.x < b.x;
        const [p, q] = forward ? [a, b] : [b, a];
        const [pp, qp] = forward ? [e.from, e.to] : [e.to, e.from];
        const x1 = p.x + radius(pp), x2 = q.x - radius(qp), dx = (x2 - x1) / 2;
        d = `M${x1},${p.y} C${x1 + dx},${p.y} ${x2 - dx},${q.y} ${x2},${q.y}`;
      }
      this.drawEdge(ctx, e, d, forward);
    }

    ctx.nodeLayer = svgEl(ctx.vp, "g", { cls: "alm-dx-nodes" });
    for (const n of nodes) {
      const p = n.file.path, c = L.coords.get(p);
      this.drawNode(ctx, n, c.x, c.y, radius(p), true, "", null);
    }
  }

  drawClusters(ctx, nodes, edges, domain) {
    const s = this.plugin.settings;
    const C = layoutClusters(nodes, edges);
    if (this.focusCluster && !C.clusters.some((g) => g.key === this.focusCluster)) this.focusCluster = null;
    const focus = this.focusCluster;
    const colorOf = (g) => `var(--color-${CLUSTER_COLORS[g.color % CLUSTER_COLORS.length]})`;
    const clusterOf = new Map(C.clusters.map((g) => [g.key, g]));
    const radius = C.radius;
    this.layoutBox = { minX: -C.extent, maxX: C.extent, minY: -C.extent, maxY: C.extent };

    // Node thuộc cụm khác nhưng có cạnh tới cụm đang focus: không làm mờ, hiện nhãn
    const focusNbrs = new Set();
    if (focus) {
      for (const e of edges) {
        const ka = C.keyOf.get(e.from), kb = C.keyOf.get(e.to);
        if (ka === focus && kb !== focus) focusNbrs.add(e.to);
        if (kb === focus && ka !== focus) focusNbrs.add(e.from);
      }
    }

    // Tâm: hub domain, vòng badge đánh số cụm, nan hoa nối tới từng cụm
    const bg = svgEl(ctx.vp, "g", { cls: "alm-dx-bg" });
    svgEl(bg, "circle", { cls: "alm-dx-hub-ring", attr: { r: C.hubRing } });
    for (const g of C.clusters) {
      svgEl(bg, "line", {
        cls: "alm-dx-spoke",
        attr: { x1: 0, y1: 0, x2: g.cx - g.r * Math.cos(g.angle), y2: g.cy - g.r * Math.sin(g.angle) },
      });
    }
    svgEl(bg, "circle", { cls: "alm-dx-hub", attr: { r: Math.max(34, C.hubRing * 0.45) } });
    svgEl(bg, "text", { cls: "alm-dx-hub-label", attr: { "text-anchor": "middle", dy: "0.32em" } })
      .textContent = domain === UNASSIGNED ? "Chưa gán" : this.plugin.domainLabel(domain);

    C.clusters.forEach((g, i) => {
      const info = this.plugin.sourceInfo(g.key);
      const color = colorOf(g);
      const toggleFocus = () => {
        this.focusCluster = this.focusCluster === g.key ? null : g.key;
        this.refresh();
      };

      const cg = svgEl(bg, "g", { cls: "alm-dx-cluster" + (focus ? (g.key === focus ? " is-focus" : " is-dim") : "") });
      cg.style.setProperty("--alm-dx-cl", color);
      svgEl(cg, "circle", { attr: { cx: g.cx, cy: g.cy, r: g.r } });
      const below = Math.sin(g.angle) > 0.3;
      const ly = below ? g.cy + g.r + 18 : g.cy - g.r - 26;
      const label = svgEl(cg, "text", {
        cls: "alm-dx-cluster-label alm-dx-clickable",
        attr: { x: g.cx, y: ly, "text-anchor": "middle" },
      });
      label.textContent = `${i + 1}  ${shorten(info.label)}`;
      svgEl(label, "title").textContent = `${info.label}\nClick để focus cụm này`;
      label.addEventListener("click", toggleFocus);
      svgEl(cg, "text", { cls: "alm-dx-cluster-sub", attr: { x: g.cx, y: ly + 14, "text-anchor": "middle" } })
        .textContent = `${info.sub} · ${g.members.length} node`;

      const badge = svgEl(bg, "g", {
        cls: "alm-dx-cluster-badge alm-dx-clickable" + (focus === g.key ? " is-focus" : ""),
        attr: { transform: `translate(${C.hubRing * Math.cos(g.angle)},${C.hubRing * Math.sin(g.angle)})` },
      });
      badge.style.setProperty("--alm-dx-cl", color);
      svgEl(badge, "circle", { attr: { r: 13 } });
      svgEl(badge, "text", { attr: { "text-anchor": "middle", dy: "0.35em" } }).textContent = String(i + 1);
      svgEl(badge, "title").textContent = `${info.label}\nClick để focus cụm này`;
      badge.addEventListener("click", toggleFocus);
    });

    // Cạnh: trong cụm là đường thẳng; liên cụm là đường cong kéo về phía tâm
    const trim = (from, to, r) => {
      const vx = to.x - from.x, vy = to.y - from.y, d = Math.hypot(vx, vy) || 1;
      return { x: to.x - (vx / d) * r, y: to.y - (vy / d) * r };
    };
    ctx.edgeLayer = svgEl(ctx.vp, "g", { cls: "alm-dx-edges" });
    for (const e of edges) {
      const ka = C.keyOf.get(e.from), kb = C.keyOf.get(e.to);
      if (s.crossOnly && ka === kb) continue;
      if (focus && ka !== focus && kb !== focus) continue;
      const a = C.coords.get(e.from), b = C.coords.get(e.to);
      let d;
      if (ka === kb) {
        const p = trim(b, a, radius(e.from)), q = trim(a, b, radius(e.to));
        d = `M${p.x},${p.y} L${q.x},${q.y}`;
      } else {
        const c = { x: ((a.x + b.x) / 2) * 0.35, y: ((a.y + b.y) / 2) * 0.35 };
        const p = trim(c, a, radius(e.from)), q = trim(c, b, radius(e.to));
        d = `M${p.x},${p.y} Q${c.x},${c.y} ${q.x},${q.y}`;
      }
      this.drawEdge(ctx, e, d, true);
    }

    // Nhãn mặc định: các node nhiều cạnh nhất; khi focus: node trong cụm và láng giềng liên cụm
    const degs = nodes.map((n) => C.deg.get(n.file.path)).sort((a, b) => b - a);
    const thr = Math.max(1, degs[Math.min(LABEL_TOP, degs.length) - 1] || 0);
    ctx.nodeLayer = svgEl(ctx.vp, "g", { cls: "alm-dx-nodes" });
    for (const n of nodes) {
      const p = n.file.path, c = C.coords.get(p), g = clusterOf.get(C.keyOf.get(p));
      const inFocus = !focus || g.key === focus || focusNbrs.has(p);
      const showLabel = s.showLabels || (focus ? inFocus : C.deg.get(p) >= thr);
      this.drawNode(ctx, n, c.x, c.y, radius(p), showLabel, "in-cluster" + (inFocus ? "" : " is-dim"), colorOf(g));
    }
  }

  bindPanZoom(svg) {
    let drag = null;
    svg.addEventListener("wheel", (evt) => {
      if (!this.transform) return;
      evt.preventDefault();
      const t = this.transform;
      const rect = svg.getBoundingClientRect();
      const mx = evt.clientX - rect.left, my = evt.clientY - rect.top;
      const k = Math.min(4, Math.max(0.1, t.k * Math.exp(-evt.deltaY * 0.0015)));
      t.x = mx - (mx - t.x) * (k / t.k);
      t.y = my - (my - t.y) * (k / t.k);
      t.k = k;
      this.applyTransform();
    }, { passive: false });
    svg.addEventListener("pointerdown", (evt) => {
      if (evt.button !== 0 || !this.transform || evt.target.closest(".alm-dx-node, .alm-dx-clickable")) return;
      drag = { x: evt.clientX - this.transform.x, y: evt.clientY - this.transform.y };
      svg.setPointerCapture(evt.pointerId);
      svg.addClass("is-panning");
    });
    svg.addEventListener("pointermove", (evt) => {
      if (!drag) return;
      this.transform.x = evt.clientX - drag.x;
      this.transform.y = evt.clientY - drag.y;
      this.applyTransform();
    });
    const end = () => {
      drag = null;
      svg.removeClass("is-panning");
    };
    svg.addEventListener("pointerup", end);
    svg.addEventListener("pointercancel", end);
  }

  fitGraph() {
    if (!this.viewport || !this.layoutBox || !this.viewport.isConnected) return;
    const w = this.svgWrap.clientWidth, h = this.svgWrap.clientHeight;
    if (!w || !h) return;
    const b = this.layoutBox;
    const bw = b.maxX - b.minX, bh = b.maxY - b.minY;
    const k = Math.min(1.5, (w / bw) * 0.95, (h / bh) * 0.95);
    this.transform = {
      k,
      x: (w - bw * k) / 2 - b.minX * k,
      y: (h - bh * k) / 2 - b.minY * k,
    };
    this.applyTransform();
  }

  applyTransform() {
    const t = this.transform;
    if (this.viewport && t) this.viewport.setAttr("transform", `translate(${t.x},${t.y}) scale(${t.k})`);
  }
}

module.exports = class AlmDomainExplorer extends Plugin {
  async onload() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
    this.settings.collapsed = Object.assign({}, this.settings.collapsed);
    this.domains = { ...FALLBACK_DOMAINS };
    this.relationTypes = Object.keys(REL_GROUPS);

    this.registerView(VIEW_TYPE, (leaf) => new DomainExplorerView(leaf, this));
    this.registerHoverLinkSource(VIEW_TYPE, { display: "ALM domain explorer", defaultMod: true });
    this.addRibbonIcon("layers", "ALM domain explorer", () => this.activateView());
    this.addCommand({ id: "open", name: "Open domain explorer", callback: () => this.activateView() });
    this.addCommand({ id: "open-graph", name: "Open domain graph", callback: () => this.openGraphTab() });

    const refresh = debounce(() => this.refreshViews(), 300, true);
    this.registerEvent(this.app.metadataCache.on("changed", (file) => {
      if (file.path === TAXONOMY_PATH) this.loadTaxonomy();
      else if (file.path.startsWith(WIKI_ROOT)) refresh();
    }));
    this.registerEvent(this.app.metadataCache.on("resolved", refresh));
    this.registerEvent(this.app.vault.on("delete", refresh));
    this.registerEvent(this.app.vault.on("rename", refresh));

    this.app.workspace.onLayoutReady(() => this.loadTaxonomy());
  }

  async loadTaxonomy() {
    const file = this.app.vault.getAbstractFileByPath(TAXONOMY_PATH);
    if (file instanceof TFile) {
      try {
        const text = await this.app.vault.cachedRead(file);
        const m = text.match(/```yaml taxonomy\r?\n([\s\S]*?)\r?\n```/);
        const tax = m ? parseYaml(m[1]) : null;
        if (tax && tax.domains && typeof tax.domains === "object") {
          this.domains = Object.fromEntries(
            Object.entries(tax.domains).map(([k, v]) => [k, String(v == null ? "" : v)]));
        }
        if (tax && tax.relations && typeof tax.relations === "object") {
          this.relationTypes = Object.keys(tax.relations);
        }
      } catch (e) {
        console.warn("[alm-domain-explorer] Không đọc được taxonomy, dùng giá trị mặc định", e);
      }
    }
    this.refreshViews();
  }

  sourceInfo(key) {
    if (!key || key === NO_SOURCE) return { label: "Chưa có citation", sub: "—" };
    const file = this.app.vault.getAbstractFileByPath(key);
    const fm = file instanceof TFile ? this.app.metadataCache.getFileCache(file)?.frontmatter : null;
    const base = key.split("/").pop().replace(/\.md$/, "");
    return { label: String(fm?.title || base), sub: String(fm?.source_id || base) };
  }

  domainLabel(key) {
    const desc = this.domains[key] || "";
    return desc.split(" — ")[0].trim() || key;
  }

  collectNodes() {
    const out = [];
    for (const file of this.app.vault.getMarkdownFiles()) {
      // Bỏ index/log/overview nằm ngay ở gốc 02_wiki/
      if (!file.path.startsWith(WIKI_ROOT) || file.path.split("/").length < 3) continue;
      const cache = this.app.metadataCache.getFileCache(file);
      const fm = cache?.frontmatter;
      if (!fm) continue;
      const title = String(fm.title || file.basename);
      const resolve = (v) => this.app.metadataCache.getFirstLinkpathDest(linkpath(v), file.path);

      // Nguồn chính = source note được cite nhiều nhất trong thân bài; hoà thì theo thứ tự trong `sources`
      const listed = asList(fm.sources).map((v) => resolve(v)?.path).filter(Boolean);
      const rank = (p) => (listed.includes(p) ? listed.indexOf(p) : listed.length);
      const counts = new Map();
      for (const l of cache.links || []) {
        const dest = resolve(l.link);
        if (dest && dest.basename.startsWith("src-")) counts.set(dest.path, (counts.get(dest.path) || 0) + 1);
      }
      let source = null, best = 0;
      for (const [p, c] of counts) {
        if (c > best || (c === best && rank(p) < rank(source))) {
          source = p;
          best = c;
        }
      }
      if (!source) source = listed[0] || null;
      if (fm.type === "source") source = file.path;

      const relations = [];
      for (const r of Array.isArray(fm.relations) ? fm.relations : []) {
        if (!r || typeof r !== "object") continue;
        const dest = this.app.metadataCache.getFirstLinkpathDest(linkpath(r.to), file.path);
        relations.push({ type: String(r.type || ""), target: dest ? dest.path : null });
      }
      out.push({
        file,
        title,
        type: String(fm.type || "unknown"),
        domains: asList(fm.domains),
        maturity: String(fm.maturity || ""),
        status: String(fm.status || "active"),
        source,
        relations,
        search: [title, file.basename, ...asList(fm.aliases)].join(" ").toLowerCase(),
      });
    }
    return out;
  }

  async update(patch) {
    Object.assign(this.settings, patch);
    this.refreshViews();
    await this.saveSettings();
  }

  async saveSettings() {
    await this.saveData(this.settings);
  }

  refreshViews() {
    for (const leaf of this.app.workspace.getLeavesOfType(VIEW_TYPE)) {
      if (leaf.view instanceof DomainExplorerView) leaf.view.refresh();
    }
  }

  async activateView() {
    const { workspace } = this.app;
    let leaf = workspace.getLeavesOfType(VIEW_TYPE)[0];
    if (!leaf) {
      leaf = workspace.getLeftLeaf(false) || workspace.getLeaf(true);
      await leaf.setViewState({ type: VIEW_TYPE, active: true, state: { mode: "list" } });
    }
    workspace.revealLeaf(leaf);
  }

  async openGraphTab() {
    const leaf = this.app.workspace.getLeaf("tab");
    await leaf.setViewState({ type: VIEW_TYPE, active: true, state: { mode: "graph" } });
    this.app.workspace.revealLeaf(leaf);
  }
};
