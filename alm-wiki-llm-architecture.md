# ALM Wiki LLM — Kiến trúc sơ bộ

## 1. Mục tiêu hệ thống

ALM Wiki LLM là một hệ thống tri thức tài chính persistent, được tổ chức theo tinh thần LLM Wiki của Karpathy:

- Raw source là nguồn tham chiếu bất biến.
- Markdown source là nguồn machine-readable canonical cho LLM.
- Evidence là lớp claim có provenance.
- Wiki là lớp tri thức đã được tổng hợp, liên kết và duy trì theo thời gian.
- Query và synthesis có thể tạo ra tri thức mới và quay lại làm giàu Wiki sau khi được review/promotion phù hợp.
- LLM đóng vai trò knowledge compiler và knowledge maintainer, không phải source of truth.

Các domain chính:

- Macroeconomic
- Financial Product
- ALM
- Basel
- VN Regulator

Một Wiki Node có thể thuộc nhiều domain. Mỗi node có một `primary_domain` và có thể có nhiều `secondary_domains`.

Ví dụ:

```yaml
primary_domain: ALM
secondary_domains:
  - Basel
  - Macroeconomic
```

Filesystem của Wiki được tổ chức theo `node_type`, không tổ chức theo domain. Domain là metadata many-to-many.

---

# 2. Cấu trúc Project

```text
alm-wiki/
│
├── CLAUDE.md
├── README.md
├── INDEX.md
├── CHANGELOG.md
│
├── .claude/
│   ├── agents/
│   │   ├── source-normalizer.md
│   │   ├── source-ingestor.md
│   │   ├── knowledge-compiler.md
│   │   ├── query-router.md
│   │   ├── domain-researcher.md
│   │   ├── contradiction-resolver.md
│   │   ├── wiki-linter.md
│   │   ├── knowledge-promoter.md
│   │   └── regulatory-reviewer.md
│   │
│   ├── skills/
│   │   ├── normalize-source/
│   │   ├── ingest-source/
│   │   ├── compile-wiki/
│   │   ├── query-wiki/
│   │   ├── synthesize/
│   │   ├── reconcile/
│   │   ├── lint-wiki/
│   │   ├── promote-node/
│   │   ├── retire-node/
│   │   └── trace-source/
│   │
│   ├── rules/
│   │   ├── source-integrity.md
│   │   ├── provenance.md
│   │   ├── temporal-validity.md
│   │   ├── regulation-governance.md
│   │   ├── node-governance.md
│   │   ├── cross-domain-linking.md
│   │   └── write-policy.md
│   │
│   ├── commands/
│   │   ├── normalize.md
│   │   ├── ingest.md
│   │   ├── query.md
│   │   ├── lint.md
│   │   ├── reconcile.md
│   │   └── promote.md
│   │
│   ├── templates/
│   │   ├── source.md
│   │   ├── evidence-claim.md
│   │   ├── definition-node.md
│   │   ├── concept-node.md
│   │   ├── entity-node.md
│   │   ├── instrument-node.md
│   │   ├── regulation-node.md
│   │   ├── metric-node.md
│   │   ├── model-node.md
│   │   ├── relationship-node.md
│   │   └── synthesis-node.md
│   │
│   ├── schemas/
│   │   ├── node.schema.yaml
│   │   ├── source.schema.yaml
│   │   ├── evidence.schema.yaml
│   │   ├── relationship.schema.yaml
│   │   └── lifecycle.schema.yaml
│   │
│   └── context/
│       ├── taxonomy.md
│       ├── domains.md
│       ├── source-authority.md
│       └── glossary.md
│
├── config/
│   ├── taxonomy.yaml
│   ├── source-authority.yaml
│   ├── node-schema.yaml
│   ├── lifecycle.yaml
│   ├── domain-routing.yaml
│   └── citation-policy.yaml
│
├── source-original/
│   ├── macro/
│   ├── products/
│   ├── alm/
│   ├── basel/
│   └── regulator-vn/
│
├── source-md/
│   ├── macro/
│   ├── products/
│   ├── alm/
│   ├── basel/
│   └── regulator-vn/
│
├── evidence/
│   ├── claims/
│   ├── source-index/
│   ├── tables/
│   └── conflicts/
│
├── wiki/
│   ├── definitions/
│   ├── concepts/
│   ├── entities/
│   ├── instruments/
│   ├── regulations/
│   ├── metrics/
│   ├── models/
│   ├── relationships/
│   ├── synthesis/
│   └── analysis/
│
├── logs/
│   ├── ingestion.md
│   ├── query.md
│   ├── lint.md
│   └── decisions.md
│
└── archive/
```

---

# 3. Cấu trúc vận hành

## 3.1. Luồng tổng thể

```text
Source Original
      │
      │ audit / reference
      ▼
Source Markdown Canonical
      │
      ▼
Evidence / Claims
      │
      ▼
Knowledge Compiler
      │
      ▼
Wiki Nodes
      │
      ├── Query
      ├── Synthesis
      ├── Reconcile
      └── Lint
      │
      ▼
Promotion / Review
      │
      └──────────────► Wiki
```

Nguyên tắc vận hành:

```text
Source → Evidence → Knowledge → Synthesis / Analysis
```

Các lớp này không được trộn lẫn.

---

## 3.2. Các operation chính

### OP01 — Normalize Source

Mục tiêu: bảo đảm bản Markdown phản ánh đúng source gốc.

Luồng:

```text
source-original
      ↓
source-md
      ↓
structural validation
      ↓
canonical markdown
```

Các điểm kiểm tra đã xác định:

- heading structure
- paragraph continuity
- page references
- tables
- equations
- footnotes
- lists
- article / section numbering
- missing figures
- encoding errors

`source-original` chỉ dùng để đối chiếu khi bản Markdown có khả năng sai lệch do quá trình chuyển đổi.

---

### OP02 — Ingest Source

Luồng:

```text
source-md
   ↓
validate normalization
   ↓
classify source
   ↓
create / update source metadata
   ↓
extract atomic claims
   ↓
identify affected nodes
   ↓
create impact map
   ↓
invoke knowledge compiler
```

Output chính:

```yaml
source_id: SRC-...
new_nodes: []
updated_nodes: []
conflicts: []
candidate_relationships: []
```

---

### OP03 — Compile Wiki

Đây là operation cốt lõi theo tinh thần Karpathy.

Luồng:

```text
Evidence
   ↓
map to existing nodes
   ↓
create missing nodes
   ↓
update concepts / models / metrics / regulations
   ↓
update relationships
   ↓
update synthesis
   ↓
update index
```

Một source có thể tác động đến nhiều Wiki Node thuộc nhiều domain khác nhau.

---

### OP04 — Query Wiki

Nguyên tắc:

```text
wiki first
raw second
```

Luồng:

```text
User Question
   ↓
Intent Classification
   ↓
Domain Routing
   ↓
Temporal Resolution
   ↓
Wiki Retrieval
   ↓
Evidence Verification
   ↓
Synthesis
   ↓
Answer
```

Raw/source-original chỉ được dùng khi cần verify hoặc đối chiếu source.

---

### OP05 — Synthesize

Một query hoặc analysis có giá trị có thể được lưu lại dưới dạng `synthesis` hoặc `analysis` node.

Luồng:

```text
question
   ↓
analysis
   ↓
review
   ↓
persisted synthesis / analysis node
```

Mục tiêu là để tri thức từ query tiếp tục compound thay vì biến mất trong chat history.

---

### OP06 — Reconcile

Mục tiêu: xử lý contradiction, không overwrite âm thầm.

Khi hai claim khác nhau, hệ thống phải kiểm tra ít nhất các chiều đã xác định:

- có cùng entity hay không
- có cùng loại sản phẩm / loại tiền gửi hay không
- có cùng period hay không
- có cùng methodology hay không
- có cùng rate cycle / regime hay không
- authority của source
- effective date
- scope
- jurisdiction
- specificity

Conflict phải được ghi nhận và xử lý rõ ràng.

---

### OP07 — Lint Wiki

Các kiểm tra chính:

- broken links
- orphan nodes
- missing citations
- unsupported claims
- stale facts
- expired regulations
- missing `valid_to`
- conflicting definitions
- duplicate concepts
- missing relationships
- outdated synthesis

Đối với regulator:

- amendment
- supersession
- expiry

Đối với macro:

- stale period

Đối với Basel:

- phân biệt consultative paper và final standard

---

### OP08 — Promote Node

Node có maturity lifecycle:

```text
M0 Draft
M1 Extracted
M2 Synthesized
M3 Reviewed
M4 Validated
M5 Canonical
```

LLM có thể tạo và cập nhật các mức thấp hơn.

Các mức cao hơn, đặc biệt đối với regulatory interpretation, model methodology và approved assumptions, cần human review / validation.

---

### OP09 — Retire Node

Knowledge hết hiệu lực không bị xóa.

Ví dụ:

```yaml
status: retired
valid_to: YYYY-MM-DD
superseded_by: NODE-ID
```

Node lịch sử vẫn phải tồn tại để phục vụ truy vấn historical/as-of.

---

### OP10 — Trace Source

Mục tiêu: truy ngược từ Wiki Node / claim về:

```text
Wiki Node
   ↓
Evidence Claim
   ↓
Source Markdown
   ↓
Source Original
```

---

# 4. Vai trò của `.claude`

`.claude` là control plane của hệ thống.

## 4.1. Rule

Rule là constraint luôn đúng.

Ví dụ:

- Không sửa `source-original`.
- Không tạo regulatory claim nếu không có provenance.
- Không overwrite conflict âm thầm.
- Không coi LLM interpretation là source evidence.
- Phải giữ historical version.
- Phải tôn trọng temporal validity.
- Phải tôn trọng regulatory hierarchy.

---

## 4.2. Skill

Skill là procedure có input/output rõ ràng.

Các skill chính:

- normalize-source
- ingest-source
- compile-wiki
- query-wiki
- synthesize
- reconcile
- lint-wiki
- promote-node
- retire-node
- trace-source

---

## 4.3. Agent

Agent là role có reasoning responsibility.

Các agent chính:

- source-normalizer
- source-ingestor
- knowledge-compiler
- query-router
- domain-researcher
- contradiction-resolver
- wiki-linter
- knowledge-promoter
- regulatory-reviewer

Agent có thể sử dụng nhiều skill khác nhau.

---

# 5. Yêu cầu đối với Source

## 5.1. Source Original

Vị trí:

```text
source-original/
```

Yêu cầu:

- là tài liệu gốc PDF, Word hoặc định dạng ban đầu
- immutable / read-only
- dùng làm source of truth để audit và kiểm tra lỗi markdown hóa
- không bị overwrite khi có phiên bản mới
- phiên bản cũ vẫn được giữ lại

Ví dụ:

```text
source-original/basel/BCBS_IRRBB_2016.pdf
```

---

## 5.2. Source Markdown

Vị trí:

```text
source-md/
```

Vai trò:

- machine-readable canonical source cho LLM
- là input chính của ingestion
- được phép sửa chỉ trong quá trình `normalize-source`

Frontmatter tối thiểu đã xác định:

```yaml
source_id: SRC-BCBS-IRRBB-2016

title: Interest rate risk in the banking book

source_type: regulatory_standard

issuer: BCBS

primary_domain: Basel
secondary_domains:
  - ALM

published_at: 2016-04-01

original_file:
  path: source-original/basel/BCBS_IRRBB_2016.pdf

conversion:
  method: pdf-to-markdown
  status: verified
  verified_at: YYYY-MM-DD
```

Nếu conversion có vấn đề:

```yaml
normalization:
  status: partial
  issues:
    - page: 37
      type: table_conversion
      note: "Column structure differs from original PDF"
```

---

# 6. Yêu cầu đối với Evidence

Evidence là lớp trung gian giữa source và wiki.

Vai trò:

```text
Source says X
```

khác với:

```text
Wiki interprets X as Y
```

Evidence nên atomic, traceable và có provenance.

Ví dụ:

```yaml
claim_id: CLM-001229
source_id: SRC-BCBS-IRRBB
claim: "..."
primary_domain: Basel
secondary_domains:
  - ALM

target_nodes:
  - CONCEPT-IRRBB
  - METRIC-EVE
```

Evidence có thể chứa các metadata đã xác định:

- source
- page / article / section khi có
- effective date
- authority
- confidence / verification status
- target nodes

Evidence không phải Wiki knowledge và không phải LLM opinion.

---

# 7. Yêu cầu đối với Wiki

## 7.1. Nguyên tắc chung

Wiki là lớp compiled knowledge.

Wiki được tổ chức theo `node_type`:

```text
wiki/
├── definitions/
├── concepts/
├── entities/
├── instruments/
├── regulations/
├── metrics/
├── models/
├── relationships/
├── synthesis/
└── analysis/
```

Không tổ chức filesystem theo domain.

Không duplicate cùng một node theo nhiều domain.

Ví dụ không nên có:

```text
macro/yield-curve.md
products/yield-curve.md
alm/yield-curve.md
```

Nên có một node duy nhất:

```text
wiki/concepts/yield-curve.md
```

với metadata:

```yaml
primary_domain: Macroeconomic
secondary_domains:
  - Financial-Product
  - ALM
```

---

## 7.2. Wiki Node Schema cơ sở

```yaml
id: CONCEPT-ALM-DEPOSIT-BETA
title: Deposit Beta

node_type: concept

primary_domain: ALM
secondary_domains:
  - Macroeconomic

status: synthesized
maturity: M2

created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD

validity:
  valid_from:
  valid_to:

authority:
  level: derived

sources:
  - SRC-001
  - SRC-014

related_nodes:
  - CONCEPT-NMD
  - METRIC-NII
  - MODEL-DEPOSIT-BETA

tags:
  - deposit
  - pricing
  - repricing
```

---

# 8. Các loại Wiki Node

## 8.1. Definition Node

Dùng cho định nghĩa chuẩn.

Ví dụ:

- Duration
- Modified Duration
- DV01
- EVE
- NII
- Deposit Beta
- NMD
- Liquidity Premium
- FTP
- Basis Risk
- Optionality Risk

Nội dung chính:

```text
Definition
Formula
Interpretation
Typical Usage
Common Confusion
Related Concepts
```

Definition không phải nơi chứa opinion hoặc synthesis rộng.

---

## 8.2. Concept Node

Dùng để mô tả cách một khái niệm hoạt động, drivers, mechanisms và implications.

Ví dụ:

- Deposit Beta
- NMD Behaviour
- Structural Liquidity
- IRRBB
- Funding Stability
- Liquidity Transformation
- Term Premium
- Yield Curve
- Basis Risk

Nội dung chính:

```text
Core Idea
Drivers
Mechanisms
Empirical Observations
Regime Dependency
Regulatory Interpretation
ALM Implications
Open Questions
Related Nodes
Evidence
```

---

## 8.3. Entity Node

Ví dụ:

- State Bank of Vietnam
- Federal Reserve
- ECB
- BIS
- BCBS
- Banks
- currencies
- indices

Nội dung chính:

```text
Overview
Role
Relevant Policies
Relevant Instruments
Relevant Regulations
ALM Relevance
Timeline
Related Nodes
```

---

## 8.4. Instrument Node

Ví dụ:

- Government Bond
- Corporate Bond
- Interest Rate Swap
- Cross Currency Swap
- OIS
- FRA
- Repo
- FX Swap
- Cap/Floor
- Swaption
- Callable Bond
- Floating Rate Note

Nội dung chính:

```text
Definition
Cashflow Structure
Pricing
Risk Factors
Greeks / Sensitivities
Accounting Treatment
Liquidity Characteristics
ALM Usage
Hedging Usage
Basel Treatment
Vietnam Regulatory Considerations
Key Relationships
```

---

## 8.5. Regulation Node

Dùng cho regulation document và regulatory requirement.

Metadata chính:

```yaml
issuer:
jurisdiction:
published:
effective_from:
effective_to:
status:
supersedes:
superseded_by:
authority_level:
```

Nội dung chính:

```text
Purpose
Scope
Definitions
Requirements
Thresholds
Reporting Obligations
Exceptions
Effective Dates
Amendments
Superseded Provisions
ALM Impacts
Linked Evidence
```

Không overwrite regulation cũ; phải giữ timeline.

---

## 8.6. Metric Node

Ví dụ:

- LCR
- NSFR
- EVE
- ΔEVE
- NII Sensitivity
- Duration Gap
- Liquidity Gap
- Deposit Beta
- Loan Beta
- FTP Curve
- Survival Horizon
- LCR Runoff Rate
- NSFR ASF
- NSFR RSF

---

## 8.7. Model Node

Ví dụ:

- NMD behavioural model
- Deposit decay model
- Prepayment model
- Early redemption model
- EVE model
- NII simulation model
- Liquidity stress model
- FTP model

Nội dung chính:

```text
Objective
Definition
Mathematical Formulation
Inputs
Assumptions
Calibration
Outputs
Regulatory Usage
Management Usage
Limitations
Validation Considerations
```

---

## 8.8. Relationship Node

Mục tiêu là mô hình hóa quan hệ giữa các node.

Các relation đã xác định:

```text
CAUSES
AFFECTS
HEDGES
CONSTRAINS
MEASURED_BY
REQUIRED_BY
SUPERSEDES
CORRELATES_WITH
PRICED_BY
EXPOSED_TO
```

Ví dụ:

```yaml
from: Deposit Beta
relation: AFFECTS
to: NII
direction: negative
regime: rising_rate
confidence: high
```

---

## 8.9. Synthesis Node

Dùng để tổng hợp tri thức cross-source và cross-domain.

Nội dung chính:

```text
Question
Executive Conclusion
Mechanism
Supporting Evidence
Conflicting Evidence
Regime Dependency
Regulatory Implications
ALM Implications
Uncertainties
Source Map
```

---

## 8.10. Analysis Node

Dùng cho phân tích được sinh từ query/research và có giá trị lưu lại.

Analysis chỉ nên được coi là tri thức bền vững sau review/promotion phù hợp.

---

# 9. Domain Model

Các domain chính:

```text
D01 Macroeconomic
D02 Financial Product
D03 ALM
D04 Basel
D05 VN Regulation
```

Có thể có cross-domain interpretation, nhưng không cần duplicate node.

Ví dụ:

### Yield Curve

```yaml
primary_domain: Macroeconomic
secondary_domains:
  - Financial-Product
  - ALM
```

### Interest Rate Swap

```yaml
primary_domain: Financial-Product
secondary_domains:
  - ALM
  - Basel
```

### IRRBB

```yaml
primary_domain: ALM
secondary_domains:
  - Basel
  - VN-Regulator
```

---

# 10. Temporal Validity

Financial knowledge phụ thuộc thời gian.

Các node / claim cần hỗ trợ các field đã xác định:

```yaml
observed_at:
published_at:
valid_from:
valid_to:
as_of:
```

Historical knowledge không bị xóa khi hết hiệu lực.

---

# 11. Source Authority

Hierarchy đã xác định:

```text
A1 Primary Law / Regulation
A2 Official Regulator Guidance
A3 Basel / BIS Publication
A4 Central Bank Publication
A5 Audited Financial Report
A6 Academic / Industry Paper
A7 Sell-side Research
A8 News
A9 Commentary
A10 LLM-derived
```

Khi có conflict, không áp dụng nguyên tắc "newer wins" một cách tự động.

Phải xem xét:

```text
authority
+ effective date
+ scope
+ jurisdiction
+ specificity
```

---

# 12. Write Policy

## 12.1. LLM được phép tự động

- create source notes
- create draft nodes
- add cross-links
- suggest relationships
- detect conflicts
- generate synthesis drafts

## 12.2. LLM cần review trước khi thay đổi

- canonical definition
- regulatory interpretation
- model methodology
- approved assumptions
- regulation supersession status

## 12.3. LLM không được phép

- edit `source-original`
- delete history
- erase conflicting evidence
- invent missing source

---

# 13. Vai trò của `CLAUDE.md`

`CLAUDE.md` là root constitution của hệ thống, không phải nơi chứa toàn bộ logic operation.

Nó nên định nghĩa tối thiểu:

```text
Mission
Source hierarchy
Core rules
Domain model
Node model
Reference tới rules / schemas / skills / agents
```

Các nguyên tắc cốt lõi đã thống nhất:

1. Raw / original source là immutable.
2. `source-md` là canonical machine-readable source.
3. Evidence và Wiki phải tách biệt.
4. Mọi factual claim trong Wiki phải traceable.
5. Không coi LLM interpretation là source evidence.
6. Không overwrite historical regulation.
7. Mọi fact phụ thuộc thời gian phải có temporal context.
8. Conflict phải reconcile, không silently overwrite.
9. Một node có thể thuộc nhiều domain.
10. Filesystem của Wiki tổ chức theo node type; domain là metadata.
11. Query ưu tiên Wiki; raw source được dùng cho verification.
12. Analysis có giá trị có thể quay lại Wiki thông qua review/promotion.

---

# 14. Tóm tắt kiến trúc

```text
CLAUDE.md
      │
      ▼
.claude/
 rules + agents + skills + schemas
      │
      ▼
source-original
      │ audit / reference
      ▼
source-md
      │
      ▼
evidence
      │
      ▼
wiki
      │
      ├── query
      ├── synthesis
      ├── reconcile
      └── lint
      │
      ▼
review / promotion
      │
      └──────────────► wiki
```

Kiến trúc này giữ nguyên các nguyên tắc đã thống nhất từ LLM Wiki của Karpathy, đồng thời áp dụng các lớp source, evidence, wiki, provenance, temporal validity và governance cần thiết cho các domain Macroeconomic, Financial Product, ALM, Basel và VN Regulator.
