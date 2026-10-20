# ALM Topic Graph

Local Obsidian view for exploring wiki notes as `domain → topic cluster → note`.

## Open

- Select the network icon in the left ribbon, or run **Open ALM Topic Graph** from the command palette.
- Choose one domain: **ALM**, **BCBS / Basel**, **Macroeconomics**, **Financial products**, or **Vietnam regulation**. Only notes assigned to that domain are shown.
- Search by topic or note title. Click a note to open it; drag nodes to arrange the view; use the wheel to zoom.
- Toggle **Relations** to show or hide directional, typed edges from note frontmatter.

## Data sources

- Domain membership: `domains` in each note's frontmatter.
- Topic labels and cluster membership: headings and wikilinks beneath `## Cụm chủ đề` in `02_wiki/domains/domain-<domain>.md`.
- Typed and directed edges: `relations` in note frontmatter.
- Cross-topic arrows: derived when a typed relation connects notes in different topic clusters.
- Each note appears once under the first matching topic cluster in that domain's navigation page. Notes not listed there appear in `Other / chưa phân cụm`.

Sources are excluded. Synthesis notes remain visible when they have a domain and appear in a cluster.
