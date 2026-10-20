const { Plugin, ItemView } = require("obsidian");

const VIEW_TYPE = "alm-topic-graph-view";
const DOMAIN_LABELS = {
  alm: "ALM",
  basel: "BCBS / Basel",
  macro: "Macroeconomics",
  product: "Financial products",
  "vn-reg": "Vietnam regulation",
};
const DOMAIN_COLORS = {
  alm: "#65a9ff", basel: "#ff9e64", macro: "#b28dff",
  product: "#5bd6b0", "vn-reg": "#f27aa5", other: "#9aa4b2",
};

class TopicGraphView extends ItemView {
  constructor(leaf, plugin) {
    super(leaf);
    this.plugin = plugin;
    this.nodes = [];
    this.edges = [];
    this.positions = new Map();
    this.dragging = null;
    this.pan = { x: 0, y: 0 };
    this.zoom = 1;
    this.frame = 0;
    this.filterDomain = "alm";
    this.searchText = "";
    this.showRelations = true;
  }

  getViewType() { return VIEW_TYPE; }
  getDisplayText() { return "ALM Topic Graph"; }
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
    if (this.frame) cancelAnimationFrame(this.frame);
    this.frame = 0;
    this.containerEl.empty();
  }

  scheduleRefresh() {
    window.clearTimeout(this.refreshTimer);
    this.refreshTimer = window.setTimeout(() => this.refreshGraph(), 350);
  }

  renderShell() {
    const root = this.containerEl;
    root.empty();
    const toolbar = root.createDiv({ cls: "alm-tg-toolbar" });
    const select = toolbar.createEl("select", { cls: "alm-tg-domain", attr: { "aria-label": "Domain filter" } });
    for (const [domain, label] of Object.entries(DOMAIN_LABELS)) {
      select.createEl("option", { text: label, value: domain });
    }
    select.value = this.filterDomain;
    select.addEventListener("change", () => { this.filterDomain = select.value; this.refreshGraph(); });

    const search = toolbar.createEl("input", { cls: "alm-tg-search", attr: { type: "search", placeholder: "Tìm node hoặc chủ đề…", "aria-label": "Search graph" } });
    search.addEventListener("input", () => { this.searchText = search.value.trim().toLowerCase(); this.draw(); });
    const relationLabel = toolbar.createEl("label", { cls: "alm-tg-toggle" });
    const relationCheck = relationLabel.createEl("input", { attr: { type: "checkbox", checked: "checked" } });
    relationLabel.createSpan({ text: "Quan hệ" });
    relationCheck.addEventListener("change", () => { this.showRelations = relationCheck.checked; this.refreshGraph(); });
    const fit = toolbar.createEl("button", { text: "Căn khung", cls: "alm-tg-fit" });
    fit.addEventListener("click", () => {
      this.zoom = 1; this.pan = { x: 0, y: 0 };
      this.stage.scrollTop = 0; this.stage.scrollLeft = 0;
      this.draw();
    });

    this.stage = root.createDiv({ cls: "alm-tg-stage" });
    this.canvas = this.stage.createEl("canvas", { cls: "alm-tg-canvas" });
    this.context = this.canvas.getContext("2d");
    this.status = root.createDiv({ cls: "alm-tg-status" });
    this.legend = root.createDiv({ cls: "alm-tg-legend" });
    this.bindCanvas();
    this.resizeObserver = new ResizeObserver(() => this.resize());
    this.resizeObserver.observe(this.stage);
    this.register(() => this.resizeObserver.disconnect());
    this.resize();
  }

  resize() {
    if (!this.canvas) return;
    const canvasWidth = Math.max(1020, this.stage.clientWidth);
    const canvasHeight = Math.max(this.stage.clientHeight, this.contentHeight || 480);
    this.canvas.style.width = `${canvasWidth}px`;
    this.canvas.style.height = `${canvasHeight}px`;
    const rect = this.canvas.getBoundingClientRect();
    const ratio = window.devicePixelRatio || 1;
    this.canvas.width = Math.max(1, Math.floor(rect.width * ratio));
    this.canvas.height = Math.max(1, Math.floor(rect.height * ratio));
    this.context.setTransform(ratio, 0, 0, ratio, 0, 0);
    this.width = rect.width;
    this.height = rect.height;
    if (this.nodes?.length) this.seedPositions();
    this.draw();
  }

  async refreshGraph() {
    const files = this.app.vault.getMarkdownFiles();
    const noteById = new Map();
    const notes = [];
    for (const file of files) {
      if (!file.path.startsWith("02_wiki/")) continue;
      const cache = this.app.metadataCache.getFileCache(file);
      const fm = cache?.frontmatter;
      if (!fm || !fm.type || fm.type === "source" || fm.type === "nav") continue;
      const id = file.basename.toLowerCase();
      const note = {
        id, file, title: String(fm.title || file.basename), type: String(fm.type),
        domains: Array.isArray(fm.domains) ? fm.domains.map(String) : [],
        status: String(fm.status || ""), maturity: String(fm.maturity || ""),
        relations: Array.isArray(fm.relations) ? fm.relations : [],
      };
      notes.push(note);
      noteById.set(id, note);
    }

    const clusterMap = new Map();
    for (const domain of Object.keys(DOMAIN_LABELS)) {
      const nav = this.app.vault.getAbstractFileByPath(`02_wiki/domains/domain-${domain}.md`);
      if (!nav) continue;
      const raw = await this.app.vault.cachedRead(nav);
      const clusters = this.extractClusters(raw, noteById);
      const assigned = new Set();
      for (const [label, ids] of clusters) {
        const uniqueIds = ids.filter(id => !assigned.has(id));
        if (!uniqueIds.length) continue;
        const key = `${domain}:${label}`;
        clusterMap.set(key, { key, label, domain, ids: uniqueIds });
        for (const id of uniqueIds) assigned.add(id);
      }
      for (const note of notes) {
        if (!note.domains.includes(domain) || assigned.has(note.id)) continue;
        const label = "Other / chưa phân cụm";
        const key = `${domain}:${label}`;
        if (!clusterMap.has(key)) clusterMap.set(key, { key, label, domain, ids: [] });
        clusterMap.get(key).ids.push(note.id);
      }
    }

    const selected = this.filterDomain;
    const visibleNotes = notes.filter(n => n.domains.includes(selected));
    const visibleIds = new Set(visibleNotes.map(n => n.id));
    const graphNodes = [];
    const graphEdges = [];
    const addNode = node => { if (!graphNodes.some(n => n.id === node.id)) graphNodes.push(node); };
    const domain = selected;
    const domainClusters = [...clusterMap.values()].filter(c => c.domain === domain && c.ids.some(id => visibleIds.has(id)));
    if (domainClusters.length) {
      const rootId = `domain:${domain}`;
      addNode({ id: rootId, kind: "domain", label: DOMAIN_LABELS[domain], domain });
      for (const cluster of domainClusters) {
        const clusterId = `cluster:${cluster.key}`;
        addNode({ id: clusterId, kind: "cluster", label: cluster.label, domain });
        graphEdges.push({ source: rootId, target: clusterId, kind: "topic" });
        for (const id of cluster.ids) {
          if (!visibleIds.has(id)) continue;
          const note = noteById.get(id);
          if (!note) continue;
          addNode({ id: note.id, kind: "note", label: note.title, type: note.type, domain: note.domains[0] || domain, file: note.file, maturity: note.maturity });
          graphEdges.push({ source: clusterId, target: note.id, kind: "membership" });
        }
      }
    }
    if (this.showRelations) {
      for (const note of visibleNotes) {
        for (const relation of note.relations) {
          const targetId = this.wikilinkId(relation?.to);
          if (!targetId || !visibleIds.has(targetId) || !noteById.has(targetId)) continue;
          const kind = String(relation.type || "related");
          graphEdges.push({ source: note.id, target: targetId, kind: "relation", label: kind });
        }
      }
      const clustersByNote = new Map();
      for (const edge of graphEdges) {
        if (edge.kind !== "membership") continue;
        if (!clustersByNote.has(edge.target)) clustersByNote.set(edge.target, []);
        clustersByNote.get(edge.target).push(edge.source);
      }
      const topicRelations = new Map();
      for (const edge of graphEdges.filter(item => item.kind === "relation")) {
        for (const from of clustersByNote.get(edge.source) || []) {
          for (const to of clustersByNote.get(edge.target) || []) {
            if (from === to) continue;
            const key = `${from}\u0000${to}`;
            if (!topicRelations.has(key)) topicRelations.set(key, { source: from, target: to, kind: "topic-relation", labels: new Set() });
            topicRelations.get(key).labels.add(edge.label);
          }
        }
      }
      for (const edge of topicRelations.values()) graphEdges.push({ ...edge, label: [...edge.labels].join(" · ") });
    }
    this.nodes = graphNodes;
    this.edges = graphEdges;
    const topicCount = graphEdges.filter(edge => edge.kind === "topic").length;
    this.contentHeight = Math.max(480, visibleNotes.length * 31 + topicCount * 34 + 70);
    this.positions.clear();
    this.resize();
    this.status.setText(`${DOMAIN_LABELS[selected]} · ${visibleNotes.length} node · ${new Set(graphEdges.filter(e => e.kind === "relation").map(e => `${e.source}:${e.target}`)).size} quan hệ · ${topicCount} chủ đề`);
    this.renderLegend([selected]);
    this.draw();
  }

  extractClusters(markdown, noteById) {
    const lines = markdown.split(/\r?\n/);
    const result = [];
    let active = false;
    let current = null;
    for (const line of lines) {
      if (/^##\s+Cụm chủ đề/i.test(line)) { active = true; continue; }
      if (active && /^##\s+/.test(line)) break;
      if (!active) continue;
      const heading = line.match(/^###\s+(.+)$/);
      if (heading) {
        current = { label: heading[1].replace(/\s+#+\s*$/, "").trim(), ids: [] };
        result.push(current);
        continue;
      }
      if (!current) continue;
      for (const match of line.matchAll(/\[\[([^\]#|]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]/g)) {
        const id = match[1].split("/").pop().trim().toLowerCase();
        if (noteById.has(id) && !current.ids.includes(id)) current.ids.push(id);
      }
    }
    return result.filter(cluster => cluster.ids.length).map(cluster => [cluster.label, cluster.ids]);
  }

  wikilinkId(value) {
    if (typeof value !== "string") return "";
    const match = value.match(/\[\[([^\]#|]+)/);
    return (match ? match[1] : value).split("/").pop().trim().toLowerCase();
  }

  seedPositions() {
    this.positions.clear();
    const width = this.width;
    const height = this.height;
    const xDomain = 74 - width / 2;
    const xTopic = Math.max(330, width * 0.36) - width / 2;
    const xNote = Math.min(width - 260, Math.max(700, width * 0.68)) - width / 2;
    let cursorY = 38;
    const clusters = this.nodes.filter(node => node.kind === "cluster");

    for (const cluster of clusters) {
      const members = this.edges
        .filter(edge => edge.kind === "membership" && edge.source === cluster.id)
        .map(edge => this.nodes.find(node => node.id === edge.target))
        .filter(Boolean)
        .sort((a, b) => a.label.localeCompare(b.label));
      const rowGap = 31;
      const centerY = cursorY + Math.max(0, (members.length - 1) * rowGap / 2);
      this.positions.set(cluster.id, { x: xTopic, y: centerY - height / 2, vx: 0, vy: 0 });
      members.forEach((member, index) => {
        const y = cursorY + index * rowGap;
        this.positions.set(member.id, { x: xNote, y: y - height / 2, vx: 0, vy: 0 });
      });
      cursorY += Math.max(rowGap, members.length * rowGap) + 34;
    }

    const root = this.nodes.find(node => node.kind === "domain");
    if (root) {
      const rootY = 38;
      this.positions.set(root.id, { x: xDomain, y: rootY - height / 2, vx: 0, vy: 0 });
    }
  }

  bindCanvas() {
    this.canvas.addEventListener("pointerdown", event => {
      const p = this.localPoint(event);
      const hit = this.hitTest(p.x, p.y);
      if (hit) {
        this.dragging = hit.id;
        this.canvas.setPointerCapture(event.pointerId);
      } else {
        this.dragging = "pan";
        this.lastPointer = p;
        this.canvas.setPointerCapture(event.pointerId);
      }
    });
    this.canvas.addEventListener("pointermove", event => {
      if (!this.dragging) return;
      const p = this.localPoint(event);
      if (this.dragging === "pan") {
        this.pan.x += p.x - this.lastPointer.x;
        this.pan.y += p.y - this.lastPointer.y;
        this.lastPointer = p;
      } else {
        const pos = this.positions.get(this.dragging);
        if (pos) { pos.x = (p.x - this.width / 2 - this.pan.x) / this.zoom; pos.y = (p.y - this.height / 2 - this.pan.y) / this.zoom; pos.vx = 0; pos.vy = 0; }
      }
      this.draw();
    });
    this.canvas.addEventListener("pointerup", event => {
      if (this.dragging && this.dragging !== "pan") {
        const p = this.localPoint(event);
        const hit = this.hitTest(p.x, p.y);
        if (hit?.kind === "note" && hit.id === this.dragging && Math.abs(p.x - this.downX) < 4 && Math.abs(p.y - this.downY) < 4) this.app.workspace.openLinkText(hit.file.path, "", false);
      }
      this.dragging = null;
    });
    this.canvas.addEventListener("pointerdown", event => { const p = this.localPoint(event); this.downX = p.x; this.downY = p.y; });
    this.canvas.addEventListener("wheel", event => {
      if (!event.ctrlKey && !event.metaKey) return;
      event.preventDefault();
      const before = this.localPoint(event);
      const factor = event.deltaY < 0 ? 1.1 : 0.9;
      const oldZoom = this.zoom;
      this.zoom = Math.max(0.25, Math.min(3, this.zoom * factor));
      this.pan.x = before.x - this.width / 2 - (before.x - this.width / 2 - this.pan.x) * (this.zoom / oldZoom);
      this.pan.y = before.y - this.height / 2 - (before.y - this.height / 2 - this.pan.y) * (this.zoom / oldZoom);
      this.draw();
    }, { passive: false });
    this.canvas.addEventListener("dblclick", event => {
      const p = this.localPoint(event), hit = this.hitTest(p.x, p.y);
      if (hit?.kind === "note") this.app.workspace.openLinkText(hit.file.path, "", false);
    });
  }

  localPoint(event) { const r = this.canvas.getBoundingClientRect(); return { x: event.clientX - r.left, y: event.clientY - r.top }; }
  worldPoint(pos) { return { x: this.width / 2 + this.pan.x + pos.x * this.zoom, y: this.height / 2 + this.pan.y + pos.y * this.zoom }; }
  hitTest(x, y) {
    for (let i = this.nodes.length - 1; i >= 0; i--) {
      const node = this.nodes[i], pos = this.positions.get(node.id); if (!pos) continue;
      const p = this.worldPoint(pos), radius = (node.kind === "domain" ? 14 : node.kind === "cluster" ? 10 : 7) * this.zoom;
      if (Math.hypot(p.x - x, p.y - y) <= radius + 4) return node;
    }
    return null;
  }

  renderLegend(domains) {
    this.legend.empty();
    for (const domain of domains) {
      const item = this.legend.createSpan({ cls: "alm-tg-legend-item" });
      item.createSpan({ cls: "alm-tg-dot", attr: { style: `background:${DOMAIN_COLORS[domain] || DOMAIN_COLORS.other}` } });
      item.appendText(DOMAIN_LABELS[domain]);
    }
    this.legend.createSpan({ cls: "alm-tg-legend-hint", text: "Cuộn để xem · Ctrl+lăn để zoom · bấm node để mở" });
  }

  draw() {
    if (!this.context || !this.width || !this.height) return;
    const ctx = this.context;
    ctx.clearRect(0, 0, this.width, this.height);
    const query = this.searchText;
    const matches = node => !query || node.label.toLowerCase().includes(query) || String(node.type || "").toLowerCase().includes(query);
    const focused = this.nodes.filter(n => n.kind === "note" && matches(n));
    const focusIds = new Set(focused.map(n => n.id));
    const connected = new Set(focusIds);
    if (query) for (const edge of this.edges) if (focusIds.has(edge.target) || focusIds.has(edge.source)) { connected.add(edge.target); connected.add(edge.source); }
    const visible = () => true;
    const edgeAlpha = query ? 0.15 : 0.55;
    const styles = getComputedStyle(this.containerEl);
    const normalText = styles.getPropertyValue("--text-normal").trim();
    const mutedText = styles.getPropertyValue("--text-muted").trim();
    for (const edge of this.edges) {
      if ((edge.kind === "relation" || edge.kind === "topic-relation") && !this.showRelations) continue;
      const a = this.positions.get(edge.source), b = this.positions.get(edge.target);
      const na = this.nodes.find(n => n.id === edge.source), nb = this.nodes.find(n => n.id === edge.target);
      if (!a || !b || !na || !nb || !visible(na) || !visible(nb)) continue;
      const pa = this.worldPoint(a), pb = this.worldPoint(b);
      const dx = pb.x - pa.x, dy = pb.y - pa.y;
      const length = Math.max(1, Math.hypot(dx, dy));
      const endRadius = (nb.kind === "note" ? 8 : 12) * this.zoom;
      const ex = pb.x - (dx / length) * endRadius, ey = pb.y - (dy / length) * endRadius;
      ctx.beginPath(); ctx.moveTo(pa.x, pa.y); ctx.lineTo(ex, ey);
      const isRelation = edge.kind === "relation" || edge.kind === "topic-relation";
      ctx.strokeStyle = isRelation ? `rgba(220,225,235,${edge.kind === "topic-relation" ? 0.62 : query ? 0.38 : 0.32})` : `rgba(145,160,180,${edgeAlpha})`;
      ctx.lineWidth = edge.kind === "topic-relation" ? 2 : edge.kind === "relation" ? 1.4 : 1;
      ctx.setLineDash(edge.kind === "topic-relation" ? [7, 4] : edge.kind === "relation" ? [] : [4, 5]); ctx.stroke(); ctx.setLineDash([]);
      if (isRelation) {
        const angle = Math.atan2(dy, dx), head = 5 * this.zoom;
        ctx.beginPath(); ctx.moveTo(ex, ey);
        ctx.lineTo(ex - head * Math.cos(angle - Math.PI / 6), ey - head * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(ex - head * Math.cos(angle + Math.PI / 6), ey - head * Math.sin(angle + Math.PI / 6));
        ctx.closePath(); ctx.fillStyle = "rgba(220,225,235,.48)"; ctx.fill();
      }
      if (isRelation && this.zoom > 0.65 && edge.label) {
        ctx.font = "10px sans-serif"; ctx.fillStyle = "rgba(190,198,211,.68)";
        ctx.fillText(edge.label, (pa.x + pb.x) / 2, (pa.y + pb.y) / 2);
      }
    }
    for (const node of this.nodes) {
      if (!visible(node)) continue;
      const pos = this.positions.get(node.id); if (!pos) continue;
      const p = this.worldPoint(pos), r = (node.kind === "domain" ? 14 : node.kind === "cluster" ? 10 : 6.5) * this.zoom;
      const color = DOMAIN_COLORS[node.domain] || DOMAIN_COLORS.other;
      const highlighted = !query || matches(node) || focusIds.has(node.id);
      ctx.beginPath(); ctx.arc(p.x, p.y, r, 0, Math.PI * 2);
      ctx.fillStyle = node.kind === "cluster" ? `${color}aa` : color;
      ctx.globalAlpha = highlighted ? 1 : 0.2; ctx.fill(); ctx.globalAlpha = 1;
      ctx.font = `${node.kind === "domain" ? "bold 14px" : node.kind === "cluster" ? "12px" : "11px"} sans-serif`;
      ctx.fillStyle = highlighted ? normalText : mutedText;
      ctx.globalAlpha = highlighted ? 0.92 : 0.2;
      const label = node.kind === "note" ? this.shortLabel(node.label, 34) : node.label;
      ctx.fillText(label, p.x + r + 5, p.y + 4);
      ctx.globalAlpha = 1;
    }
  }

  shortLabel(text, max) { return text.length > max ? `${text.slice(0, max - 1)}…` : text; }
}

module.exports = class AlmTopicGraphPlugin extends Plugin {
  async onload() {
    this.registerView(VIEW_TYPE, leaf => new TopicGraphView(leaf, this));
    this.addRibbonIcon("network", "Open ALM Topic Graph", () => this.activateView());
    this.addCommand({ id: "open-topic-graph", name: "Open ALM Topic Graph", callback: () => this.activateView() });
  }

  async activateView() {
    let leaf = this.app.workspace.getLeavesOfType(VIEW_TYPE)[0];
    if (!leaf) leaf = this.app.workspace.getRightLeaf(false);
    await leaf.setViewState({ type: VIEW_TYPE, active: true });
    this.app.workspace.revealLeaf(leaf);
  }
};
