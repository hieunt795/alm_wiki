const { Plugin, ItemView, Component, MarkdownRenderer } = require("obsidian");

const VIEW_TYPE = "alm-neural-link-graph";
const DOMAIN_LABELS = {
  alm: "ALM",
  basel: "BCBS / Basel",
  macro: "Macroeconomics",
  product: "Financial products",
  "vn-reg": "Vietnam regulation",
};
const DOMAIN_COLORS = {
  alm: "#65a9ff",
  basel: "#ff9e64",
  macro: "#b28dff",
  product: "#5bd6b0",
  "vn-reg": "#f27aa5",
  other: "#9aa4b2",
};
const MIN_NODE_DIAMETER = 3;
const MAX_NODE_DIAMETER = 18;
const DOMAIN_NODE_MIN_DIAMETER = 26;

class NeuralLinkGraphView extends ItemView {
  constructor(leaf) {
    super(leaf);
    this.nodes = [];
    this.edges = [];
    this.positions = new Map();
    this.zoom = 1;
    this.pan = { x: 0, y: 0 };
    this.filterDomain = "alm";
    this.searchText = "";
    this.selectedId = "";
    this.dragging = null;
  }

  getViewType() { return VIEW_TYPE; }
  getDisplayText() { return "ALM Neural Link Graph"; }
  getIcon() { return "network"; }

  async onOpen() {
    this.containerEl.addClass("alm-topic-graph");
    this.renderShell();
    await this.refreshGraph();
    this.registerEvent(this.app.metadataCache.on("changed", () => this.scheduleRefresh()));
    this.registerEvent(this.app.vault.on("create", () => this.scheduleRefresh()));
    this.registerEvent(this.app.vault.on("delete", () => this.scheduleRefresh()));
    this.registerEvent(this.app.vault.on("rename", () => this.scheduleRefresh()));
  }

  async onClose() {
    window.clearTimeout(this.refreshTimer);
    this.previewComponent?.unload();
    this.containerEl.empty();
  }

  scheduleRefresh() {
    window.clearTimeout(this.refreshTimer);
    this.refreshTimer = window.setTimeout(() => this.refreshGraph(), 300);
  }

  renderShell() {
    this.containerEl.empty();
    const root = this.containerEl.createDiv({ cls: "alm-tg-root" });
    const toolbar = root.createDiv({ cls: "alm-tg-toolbar" });
    const select = toolbar.createEl("select", { cls: "alm-tg-domain", attr: { "aria-label": "Lọc theo domain" } });
    for (const [domain, label] of Object.entries(DOMAIN_LABELS)) {
      select.createEl("option", { text: label, value: domain });
    }
    select.value = this.filterDomain;
    select.addEventListener("change", () => {
      this.filterDomain = select.value;
      this.selectedId = "";
      this.refreshGraph();
    });

    const search = toolbar.createEl("input", {
      cls: "alm-tg-search",
      attr: { type: "search", placeholder: "Tìm node…", "aria-label": "Tìm node" },
    });
    search.addEventListener("input", () => { this.searchText = search.value.trim().toLowerCase(); this.draw(); });
    const fit = toolbar.createEl("button", { text: "Căn khung", cls: "alm-tg-fit" });
    fit.addEventListener("click", () => this.fitGraph());

    const workspace = root.createDiv({ cls: "alm-tg-workspace" });
    const graphPane = workspace.createDiv({ cls: "alm-tg-graph-pane" });
    this.canvas = graphPane.createEl("canvas", { cls: "alm-tg-canvas", attr: { "aria-label": "Đồ thị liên kết tri thức" } });
    this.context = this.canvas.getContext("2d");
    this.status = graphPane.createDiv({ cls: "alm-tg-status" });
    this.preview = workspace.createDiv({ cls: "alm-tg-preview" });
    this.renderEmptyPreview("Chọn một node để xem nội dung.");
    this.bindCanvas();
    this.resizeObserver = new ResizeObserver(() => this.resize());
    this.resizeObserver.observe(graphPane);
    this.register(() => this.resizeObserver.disconnect());
    this.resize();
  }

  resize() {
    if (!this.canvas) return;
    const rect = this.canvas.getBoundingClientRect();
    const ratio = window.devicePixelRatio || 1;
    this.canvas.width = Math.max(1, Math.floor(rect.width * ratio));
    this.canvas.height = Math.max(1, Math.floor(rect.height * ratio));
    this.context.setTransform(ratio, 0, 0, ratio, 0, 0);
    this.width = rect.width;
    this.height = rect.height;
    if (this.nodes.length && !this.positions.size) this.seedAndRelax();
    this.draw();
  }

  async refreshGraph() {
    const files = this.app.vault.getMarkdownFiles().filter(file => file.path.startsWith("02_wiki/"));
    const allById = new Map();
    const notes = [];
    for (const file of files) {
      const fm = this.app.metadataCache.getFileCache(file)?.frontmatter;
      if (!fm?.type || ["source", "nav"].includes(String(fm.type))) continue;
      const note = {
        id: file.basename.toLowerCase(), file,
        title: String(fm.title || file.basename), type: String(fm.type),
        domains: Array.isArray(fm.domains) ? fm.domains.map(String) : [],
        status: String(fm.status || ""), maturity: String(fm.maturity || ""),
        relations: Array.isArray(fm.relations) ? fm.relations : [],
      };
      notes.push(note);
      allById.set(note.id, note);
    }

    const visibleNotes = notes.filter(note => note.domains.includes(this.filterDomain));
    const visibleIds = new Set(visibleNotes.map(note => note.id));
    const edgesByKey = new Map();
    const addEdge = (source, target, kind, label = "") => {
      if (!source || !target || source === target || !visibleIds.has(source) || !visibleIds.has(target)) return;
      const key = kind === "relation" ? `${source}\0${target}\0${kind}\0${label}` : [source, target].sort().join("\0") + "\0link";
      if (!edgesByKey.has(key)) edgesByKey.set(key, { source, target, kind, label });
    };

    for (const note of visibleNotes) {
      for (const relation of note.relations) {
        const targetId = this.wikilinkId(relation?.to);
        addEdge(note.id, targetId, "relation", String(relation?.type || "related"));
      }
      const raw = await this.app.vault.cachedRead(note.file);
      const body = raw.replace(/^---\s*\r?\n[\s\S]*?\r?\n---\s*(?:\r?\n)?/, "");
      for (const match of body.matchAll(/\[\[([^\]#|]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]/g)) {
        const targetId = match[1].split("/").pop().trim().toLowerCase();
        addEdge(note.id, targetId, "link");
      }
    }

    const domainNode = {
      id: `domain:${this.filterDomain}`,
      kind: "domain",
      title: DOMAIN_LABELS[this.filterDomain],
      type: "domain",
      domains: [this.filterDomain],
      noteCount: visibleNotes.length,
    };
    for (const note of visibleNotes) edgesByKey.set(`membership:${note.id}`, {
      source: domainNode.id, target: note.id, kind: "membership", label: "",
    });
    this.nodes = [domainNode, ...visibleNotes];
    this.edges = [...edgesByKey.values()];
    this.degree = new Map(this.nodes.map(node => [node.id, { in: 0, out: 0 }]));
    for (const edge of this.edges) {
      if (edge.kind === "membership") continue;
      const sourceDegree = this.degree.get(edge.source);
      const targetDegree = this.degree.get(edge.target);
      if (sourceDegree) sourceDegree.out++;
      if (targetDegree) targetDegree.in++;
    }
    const maxNoteDiameter = Math.max(MIN_NODE_DIAMETER, ...visibleNotes.map(note => this.nodeDiameter(note)));
    domainNode.diameter = Math.max(DOMAIN_NODE_MIN_DIAMETER, maxNoteDiameter + 6);
    const selectedStillExists = visibleIds.has(this.selectedId);
    if (!selectedStillExists) {
      this.selectedId = "";
      this.renderEmptyPreview("Chọn một node để xem nội dung.");
    } else {
      this.renderPreview(allById.get(this.selectedId));
    }
    this.seedAndRelax();
    this.status.setText(`${DOMAIN_LABELS[this.filterDomain]} · ${visibleNotes.length} node · ${this.edges.length - visibleNotes.length} liên kết`);
    this.draw();
  }

  wikilinkId(value) {
    if (typeof value !== "string") return "";
    const match = value.match(/\[\[([^\]#|]+)/);
    return (match ? match[1] : value).split("/").pop().trim().toLowerCase();
  }

  nodeDiameter(node) {
    if (node.kind === "domain") return node.diameter || DOMAIN_NODE_MIN_DIAMETER;
    const degree = this.degree?.get(node.id);
    const count = degree ? degree.in + degree.out : 0;
    return Math.min(MAX_NODE_DIAMETER, MIN_NODE_DIAMETER + 2.5 * Math.sqrt(count));
  }

  seedAndRelax() {
    if (!this.width || !this.height) return;
    this.positions.clear();
    const count = this.nodes.length;
    const radius = Math.max(80, Math.min(this.width, this.height) * 0.36);
    const sorted = [...this.nodes].sort((a, b) => a.id.localeCompare(b.id));
    sorted.forEach((node, index) => {
      const angle = index * 2.399963229728653;
      const r = radius * Math.sqrt((index + 0.5) / Math.max(1, count));
      this.positions.set(node.id, {
        x: Math.cos(angle) * r, y: Math.sin(angle) * r,
        vx: 0, vy: 0,
      });
    });

    const nodeCount = this.nodes.length;
    const iterations = nodeCount > 450 ? 45 : 100;
    const ideal = Math.max(30, Math.min(85, 850 / Math.sqrt(Math.max(nodeCount, 1))));
    const edgePairs = this.edges.map(edge => [this.positions.get(edge.source), this.positions.get(edge.target)]).filter(pair => pair[0] && pair[1]);
    for (let step = 0; step < iterations; step++) {
      const cooling = 1 - step / iterations;
      for (let i = 0; i < sorted.length; i++) {
        const a = this.positions.get(sorted[i].id);
        for (let j = i + 1; j < sorted.length; j++) {
          const b = this.positions.get(sorted[j].id);
          let dx = a.x - b.x, dy = a.y - b.y;
          const d2 = Math.max(36, dx * dx + dy * dy);
          const d = Math.sqrt(d2);
          const force = Math.min(1.4, (ideal * ideal * 0.8) / d2);
          dx = dx / d * force; dy = dy / d * force;
          a.vx += dx; a.vy += dy; b.vx -= dx; b.vy -= dy;
        }
      }
      for (const [a, b] of edgePairs) {
        const dx = b.x - a.x, dy = b.y - a.y;
        const distance = Math.max(1, Math.hypot(dx, dy));
        const force = (distance - ideal) * 0.008;
        const fx = dx / distance * force, fy = dy / distance * force;
        a.vx += fx; a.vy += fy; b.vx -= fx; b.vy -= fy;
      }
      for (const node of sorted) {
        const p = this.positions.get(node.id);
        p.vx += -p.x * 0.0015;
        p.vy += -p.y * 0.0015;
        p.vx *= 0.78; p.vy *= 0.78;
        const maxStep = 7 * cooling + 0.15;
        const speed = Math.hypot(p.vx, p.vy);
        if (speed > maxStep) { p.vx *= maxStep / speed; p.vy *= maxStep / speed; }
        p.x += p.vx; p.y += p.vy;
      }
    }
    this.pan = { x: 0, y: 0 };
    this.zoom = 1;
    this.draw();
  }

  fitGraph() {
    if (!this.nodes.length) return;
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    for (const p of this.positions.values()) {
      minX = Math.min(minX, p.x); minY = Math.min(minY, p.y);
      maxX = Math.max(maxX, p.x); maxY = Math.max(maxY, p.y);
    }
    const contentW = Math.max(1, maxX - minX), contentH = Math.max(1, maxY - minY);
    this.zoom = Math.max(0.2, Math.min(2, Math.min((this.width - 56) / contentW, (this.height - 56) / contentH)));
    this.pan = { x: -(minX + maxX) / 2 * this.zoom, y: -(minY + maxY) / 2 * this.zoom };
    this.draw();
  }

  bindCanvas() {
    this.canvas.addEventListener("pointerdown", event => {
      const point = this.localPoint(event);
      const node = this.hitTest(point.x, point.y);
      this.downPoint = point;
      this.dragging = node ? node.id : "pan";
      this.lastPoint = point;
      this.canvas.setPointerCapture(event.pointerId);
    });
    this.canvas.addEventListener("pointermove", event => {
      if (!this.dragging) return;
      const point = this.localPoint(event);
      if (this.dragging === "pan") {
        this.pan.x += point.x - this.lastPoint.x;
        this.pan.y += point.y - this.lastPoint.y;
      } else {
        const pos = this.positions.get(this.dragging);
        if (pos) {
          pos.x = (point.x - this.width / 2 - this.pan.x) / this.zoom;
          pos.y = (point.y - this.height / 2 - this.pan.y) / this.zoom;
          pos.vx = 0; pos.vy = 0;
        }
      }
      this.lastPoint = point;
      this.draw();
    });
    this.canvas.addEventListener("pointerup", event => {
      if (this.dragging && this.dragging !== "pan") {
        const point = this.localPoint(event);
        if (Math.hypot(point.x - this.downPoint.x, point.y - this.downPoint.y) < 5) this.selectNode(this.dragging);
      }
      this.dragging = null;
    });
    this.canvas.addEventListener("dblclick", event => {
      const point = this.localPoint(event), node = this.hitTest(point.x, point.y);
      if (node && node.kind !== "domain") this.app.workspace.openLinkText(node.file.path, "", false);
    });
    this.canvas.addEventListener("wheel", event => {
      event.preventDefault();
      const point = this.localPoint(event), oldZoom = this.zoom;
      this.zoom = Math.max(0.2, Math.min(4, this.zoom * (event.deltaY < 0 ? 1.1 : 0.9)));
      this.pan.x = point.x - this.width / 2 - (point.x - this.width / 2 - this.pan.x) * this.zoom / oldZoom;
      this.pan.y = point.y - this.height / 2 - (point.y - this.height / 2 - this.pan.y) * this.zoom / oldZoom;
      this.draw();
    }, { passive: false });
  }

  localPoint(event) {
    const rect = this.canvas.getBoundingClientRect();
    return { x: event.clientX - rect.left, y: event.clientY - rect.top };
  }

  screenPoint(pos) {
    return { x: this.width / 2 + this.pan.x + pos.x * this.zoom, y: this.height / 2 + this.pan.y + pos.y * this.zoom };
  }

  hitTest(x, y) {
    for (let i = this.nodes.length - 1; i >= 0; i--) {
      const node = this.nodes[i], pos = this.positions.get(node.id);
      if (!pos) continue;
      const point = this.screenPoint(pos);
      if (Math.hypot(point.x - x, point.y - y) <= Math.max(9, this.nodeDiameter(node) * this.zoom / 2 + 5)) return node;
    }
    return null;
  }

  selectNode(id) {
    const node = this.nodes.find(item => item.id === id);
    if (!node) return;
    this.selectedId = id;
    if (node.kind === "domain") this.renderDomainPreview(node);
    else this.renderPreview(node);
    this.draw();
  }

  renderDomainPreview(node) {
    this.previewComponent?.unload();
    this.previewComponent = null;
    this.preview.empty();
    const head = this.preview.createDiv({ cls: "alm-tg-preview-head" });
    head.createEl("h3", { cls: "alm-tg-preview-title", text: node.title });
    head.createDiv({ cls: "alm-tg-preview-meta", text: "Domain" });
    this.preview.createDiv({ cls: "alm-tg-empty", text: `${node.noteCount} node thuộc domain này.` });
  }

  renderEmptyPreview(message) {
    this.previewComponent?.unload();
    this.previewComponent = null;
    this.preview.empty();
    this.preview.createDiv({ cls: "alm-tg-empty", text: message });
  }

  async renderPreview(node) {
    if (!node) return this.renderEmptyPreview("Chọn một node để xem nội dung.");
    this.previewComponent?.unload();
    const component = new Component();
    this.previewComponent = component;
    this.preview.empty();
    const head = this.preview.createDiv({ cls: "alm-tg-preview-head" });
    head.createEl("h3", { cls: "alm-tg-preview-title", text: node.title });
    head.createDiv({ cls: "alm-tg-preview-meta", text: [node.type, DOMAIN_LABELS[node.domains[0]] || node.domains[0], node.status, node.maturity].filter(Boolean).join(" · ") });
    const bodyEl = this.preview.createDiv({ cls: "alm-tg-preview-body" });
    const raw = await this.app.vault.cachedRead(node.file);
    if (this.selectedId !== node.id || this.previewComponent !== component) return;
    const body = raw.replace(/^---\s*\r?\n[\s\S]*?\r?\n---\s*(?:\r?\n)?/, "");
    component.load();
    await MarkdownRenderer.render(this.app, body, bodyEl, node.file.path, component);
  }

  draw() {
    if (!this.context || !this.width || !this.height) return;
    const ctx = this.context;
    ctx.clearRect(0, 0, this.width, this.height);
    const query = this.searchText;
    const matches = node => !query || node.title.toLowerCase().includes(query) || node.type.toLowerCase().includes(query);
    const matched = this.nodes.filter(matches);
    const matchIds = new Set(matched.map(node => node.id));
    const connected = new Set(matchIds);
    if (query) for (const edge of this.edges) {
      if (edge.kind === "membership") continue;
      if (matchIds.has(edge.source) || matchIds.has(edge.target)) { connected.add(edge.source); connected.add(edge.target); }
    }

    for (const edge of this.edges) {
      const source = this.positions.get(edge.source), target = this.positions.get(edge.target);
      if (!source || !target) continue;
      const a = this.screenPoint(source), b = this.screenPoint(target);
      const dim = query && edge.kind !== "membership" && !connected.has(edge.source) && !connected.has(edge.target);
      ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y);
      ctx.strokeStyle = edge.kind === "relation" ? "rgba(220,230,244,.56)" : edge.kind === "membership" ? "rgba(130,155,185,.16)" : "rgba(150,170,195,.22)";
      ctx.globalAlpha = dim ? 0.12 : 1;
      ctx.lineWidth = edge.kind === "relation" ? 1.1 : edge.kind === "membership" ? 0.7 : 0.8;
      ctx.setLineDash(edge.kind === "membership" ? [1, 6] : edge.kind === "link" ? [2, 4] : []);
      ctx.stroke(); ctx.setLineDash([]);
      if (edge.kind === "relation") {
        const angle = Math.atan2(b.y - a.y, b.x - a.x), head = 5;
        ctx.beginPath(); ctx.moveTo(b.x, b.y);
        ctx.lineTo(b.x - head * Math.cos(angle - Math.PI / 6), b.y - head * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(b.x - head * Math.cos(angle + Math.PI / 6), b.y - head * Math.sin(angle + Math.PI / 6));
        ctx.closePath(); ctx.fillStyle = "rgba(220,230,244,.6)"; ctx.fill();
      }
      ctx.globalAlpha = 1;
    }

    for (const node of this.nodes) {
      const pos = this.positions.get(node.id);
      if (!pos) continue;
      const point = this.screenPoint(pos), color = DOMAIN_COLORS[node.domains[0]] || DOMAIN_COLORS.other;
      const active = node.kind === "domain" || !query || connected.has(node.id), selected = node.id === this.selectedId;
      const diameter = this.nodeDiameter(node);
      ctx.globalAlpha = active ? 1 : 0.2;
      if (selected) {
        ctx.beginPath(); ctx.arc(point.x, point.y, Math.max(diameter / 2 + 4, this.zoom * 5), 0, Math.PI * 2);
        ctx.strokeStyle = color; ctx.lineWidth = 1.2; ctx.stroke();
      }
      ctx.beginPath(); ctx.arc(point.x, point.y, diameter / 2, 0, Math.PI * 2);
      ctx.fillStyle = color; ctx.fill();
      const focused = selected || (query && matchIds.has(node.id));
      const fadeStart = this.nodes.length >= 220 ? 0.55 : 0.2;
      const fadeEnd = this.nodes.length >= 220 ? 1.4 : 1.15;
      const progress = Math.max(0, Math.min(1, (this.zoom - fadeStart) / (fadeEnd - fadeStart)));
      const easedProgress = progress * progress * (3 - 2 * progress);
      const labelAlpha = focused ? 1 : node.kind === "domain" ? Math.max(0.25, easedProgress) : easedProgress;
      if (labelAlpha > 0.01) {
        ctx.font = node.kind === "domain" ? "bold 12px sans-serif" : selected || matchIds.has(node.id) ? "11px sans-serif" : "10px sans-serif";
        ctx.fillStyle = getComputedStyle(this.containerEl).getPropertyValue("--text-normal").trim() || "#ddd";
        ctx.globalAlpha = labelAlpha * (active ? 1 : 0.2);
        ctx.fillText(node.title, point.x + diameter / 2 + 5, point.y - 5);
      }
      ctx.globalAlpha = 1;
    }
  }
}

module.exports = class AlmNeuralLinkGraphPlugin extends Plugin {
  async onload() {
    this.registerView(VIEW_TYPE, leaf => new NeuralLinkGraphView(leaf));
    this.addRibbonIcon("network", "Open ALM Neural Link Graph", () => this.activateView());
    this.addCommand({ id: "open-neural-link-graph", name: "Open ALM Neural Link Graph", callback: () => this.activateView() });
  }

  async activateView() {
    const leaf = this.app.workspace.getRightLeaf(false);
    await leaf.setViewState({ type: VIEW_TYPE, active: true });
    this.app.workspace.revealLeaf(leaf);
  }
};
