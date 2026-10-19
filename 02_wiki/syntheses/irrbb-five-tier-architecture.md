---
title: "IRRBB — Kiến trúc Toàn diện 5 Tầng: Từ Bản chất Lãi suất đến Thực thi ALM Treasury"
aliases: [IRRBB Five Tier Architecture, Kiến trúc 5 tầng IRRBB, Khung phân rã IRRBB toàn diện, Master IRRBB Architecture, Bản thiết kế kiến trúc IRRBB]
type: synthesis
domains: [alm, basel]
status: active
maturity: canonical
origin: research
question: "Làm thế nào để hệ thống hóa toàn bộ các cấu phần của IRRBB từ bản chất lãi suất, hai lăng kính đo lường vốn-thu nhập, các mô hình toán học định lượng, công cụ tài chính phòng ngừa đến cơ chế điều chuyển giá vốn nội bộ FTP thành một kiến trúc 5 tầng khép kín trong quản trị ALM ngân hàng?"
sources: ["[[src-bcbs-irrbb-2016]]"]
relations: []
tags: [irrbb, 5-tier-architecture, alm-blueprint, eve-vs-nii, quantitative-models, hedging-instruments, ftp, basel]
updated: 2026-10-17
reviewed:
---

## Tóm tắt Cấp cao (Executive Summary)

Rủi ro lãi suất trên sổ ngân hàng (Interest Rate Risk in the Banking Book - IRRBB) là rủi ro hiện tại hoặc tiềm tàng đối với nguồn vốn và thu nhập của ngân hàng phát sinh từ các biến động bất lợi của lãi suất thị trường tác động lên các vị thế trên sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u02-1]].

Thay vì tiếp cận IRRBB như một danh sách các công thức tính toán rời rạc hay một bộ quy định tuân thủ Trụ cột 2 đơn thuần của [[bcbs-irrbb]], nghiên cứu này thiết lập **Bản thiết kế Kiến trúc Toàn diện 5 Tầng (The 5-Tier Master Architecture)** xâu chuỗi logic khép kín:
$$\text{Bản chất Rủi ro (T1)} \longrightarrow \text{Mục tiêu \& Đánh đổi (T2)} \longrightarrow \text{Lượng hóa Mô hình (T3)} \longrightarrow \text{Thực thi Phòng ngừa (T4)} \longrightarrow \text{Truyền dẫn Kỷ luật (T5)}$$

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 BẢN THIẾT KẾ KIẾN TRÚC 5 TẦNG IRRBB                             │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TẦNG 1: BẢN CHẤT LÃI SUẤT & 3 PHÂN LOẠI RỦI RO CỐT LÕI (CORE RISK SUB-TYPES & CSRBB)           │
│  ├── Phân rã 5 thành phần lý thuyết lãi suất & Ranh giới IRRBB vs CSRBB                         │
│  ├── Gap Risk (Rủi ro tái định giá): Dịch chuyển song song & Phi song song (Steepener/Flattener)│
│  ├── Basis Risk (Rủi ro cơ sở): Tenor Basis, Benchmark Index Basis, Currency Basis             │
│  └── Option Risk: Automatic Options (Black-76, KAO) vs Behavioural Options (NMD, CPR, TDRR)    │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TẦNG 2: HAI LĂNG KÍNH ĐO LƯỜNG & MÂU THUẪN QUẢN TRỊ KINH ĐIỂN (DUAL-LENS & THE TRADE-OFF)       │
│  ├── Lăng kính Vốn: ΔEVE (Run-off horizon, Chiết khấu phi rủi ro, Outlier Test 15% Tier 1)     │
│  ├── Lăng kính Thu nhập: ΔNII / EaR (12M–3Y, Constant/Dynamic Balance Sheet)                   │
│  └── The Fundamental ALM Trade-off: Cố định hóa lợi suất bảo vệ NII ⮂ Kéo dài thời lượng hại EVE│
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TẦNG 3: CÁC MÔ HÌNH ĐỊNH LƯỢNG CẤU PHẦN (QUANTITATIVE MODELS)                                  │
│  ├── Duration Gap Model (DGAP): Macaulay, Modified, Effective Duration, Miễn nhiễm, Tính lồi (C)│
│  ├── Key Rate Duration (KRD): Phân rã 19 dải kỳ hạn Basel, Hàm suy giảm mũ e^(-t_k/4)           │
│  ├── Replicating Portfolio Model: Moving-Average Tranches, Cointegration, Tối ưu hóa NIM & T2   │
│  └── Value at Risk Sổ Ngân hàng: EVaR & EaR (Delta-Normal, Historical, Monte Carlo, Rủi ro đuôi)│
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TẦNG 4: CÔNG CỤ TÀI CHÍNH PHÒNG NGỪA & TÁI CẤU TRÚC THỜI LƯỢNG (HEDGING INSTRUMENTS)           │
│  ├── Interest Rate Swap (IRS): Payer Swap (giảm duration), Receiver Swap (tăng duration), OIS │
│  ├── Interest Rate Caps & Floors: Phòng ngừa rủi ro phi tuyến, Bóc tách quyền chọn bán ngầm định│
│  └── Swaptions: Payer/Receiver (Bermudan), Triệt tiêu tính lồi âm (Negative Convexity)          │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ TẦNG 5: KIẾN TRÚC ĐIỀU CHUYỂN GIÁ VỐN NỘI BỘ (IRRBB FUNDS TRANSFER PRICING - FTP)              │
│  ├── Cơ chế Chuyển giao Kỳ hạn Khớp (Matched-Maturity Marginal Funding Rate) về ALM Treasury    │
│  └── Phân rã 4 thành phần: Base Rate + Liquidity Spread + Behavioral Option Charge + Commercial │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## TẦNG 1: Bản chất Lãi suất & Ba Phân loại Rủi ro Lãi suất Cốt lõi

### 1. Phân rã 5 Thành phần Lý thuyết & Ranh giới IRRBB vs CSRBB
Theo chuẩn mực Basel d368 (Annex 1, par 1.3), mọi mức lãi suất thu được từ tài sản hoặc chi trả cho nợ đều cấu thành từ 5 thành phần lý thuyết [[src-bcbs-irrbb-2016#^irrbb-u06-2]]:

$$\text{All-in Interest Rate} = r_{\text{risk-free}} + s_{\text{duration}} + s_{\text{mkt-liq}} + s_{\text{gen-credit}} + s_{\text{idio-credit}}$$

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   CẤU TRÚC 5 THÀNH PHẦN LÃI SUẤT                                │
├──────────────────────────────────────────┬───────────────────┬──────────────────────────────────┤
│                PHẠM VI IRRBB             │   PHẠM VI CSRBB   │         CREDIT RISK              │
├─────────────────────┬────────────────────┼─────────────┬─────┴──────────────────┬───────────────┤
│ 1. Risk-Free Rate   │ 2. Market Duration │ 3. Market   │ 4. General Market      │ 5. Idiosyncratic
│    (Lãi suất phi    │    Spread          │    Liquidity│    Credit Spread       │    Credit Spread
│     rủi ro chuẩn:   │    (Phần bù biến   │    Spread   │    (Phần bù rủi ro     │    (Rủi ro vỡ nợ
│     OIS / RFR)      │     động kỳ hạn)   │    (Thanh   │     nhóm xếp hạng tín  │     đặc thù của
│                     │                    │     khoản)  │     nhiệm AA, BBB)     │     khách hàng)
└─────────────────────┴────────────────────┴─────────────┴────────────────────────┴───────────────┘
```

- **Ranh giới IRRBB**: Bao gồm các biến động của *Lãi suất phi rủi ro ($r_{\text{risk-free}}$)*, *Spread thời lượng thị trường ($s_{\text{duration}}$)*, *Lãi suất tham chiếu (Reference rate)* và *Biên tài trợ (Funding margin)* [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- **Ranh giới [CSRBB (Credit Spread Risk in the Banking Book)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/concepts/csrbb.md)**: Là rủi ro biến động của *Spread thanh khoản thị trường ($s_{\text{mkt-liq}}$)* và *Spread tín dụng thị trường chung ($s_{\text{gen-credit}}$)* đối với các công cụ chịu rủi ro tín dụng trên sổ ngân hàng mà **không giải thích được bởi IRRBB hay rủi ro vỡ nợ đột ngột (jump-to-default risk)** [[src-bcbs-irrbb-2016#^irrbb-u02-3]]. Các tài sản ghi nhận theo Giá trị Hợp lý (Fair Value / Mark-to-Market như trái phiếu doanh nghiệp, TPCP ngoại tệ trong đệm [[hqla]]) sẽ bị trừ trực tiếp vào Vốn tự có khi credit spread giãn rộng [[src-bcbs-irrbb-2016#^irrbb-u06-1]].
- **Danh mục Bảng Cân đối Phơi nhiễm**: Toàn bộ tài sản nhạy cảm lãi suất, nợ và ngoại bảng trên sổ ngân hàng được cấu trúc thành 3 nhóm vị thế theo mức độ chuẩn hoá (xem chi tiết tại [[irrbb-balance-sheet-portfolios]]).

---

### 2. Ba Phân loại Rủi ro Lãi suất Trực tiếp

#### A. [Gap Risk (Rủi ro chênh lệch kỳ hạn tái định giá)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/concepts/gap-risk.md)
Phát sinh từ sự không trùng khớp về thời điểm tái định giá lãi suất của tài sản và nợ [[src-bcbs-irrbb-2016#^irrbb-u02-2]]:
- **Parallel Shift (Dịch chuyển song song)**: Toàn bộ đường cong lợi suất tăng hoặc giảm cùng biên độ tại tất cả các kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u07-1]].
- **Non-parallel / Yield Curve Risk (Rủi ro xoay trục đường cong)**:
  - *Steepener Shock*: Lãi suất dài hạn tăng, ngắn hạn giảm (hoặc ngắn hạn tăng ít hơn dài hạn).
  - *Flattener Shock*: Lãi suất ngắn hạn tăng vọt trong khi dài hạn đi ngang hoặc giảm (Bear Flattener là kịch bản nguy hiểm nhất đối với các NHTM huy động ngắn hạn cho vay dài hạn).
  - *Curvature / Butterfly Twists*: Điểm bụng (Belly 2Y–5Y) biến động lệch pha so với hai cánh (Wings 3M và 10Y–30Y).
  - *Phân tích thành phần chính (PCA)*: Theo Alexander During & Moorad Choudhry, biến động đường cong được chi phối bởi 3 nhân tố độc lập: **Level (~80–90%)**, **Slope (~8–12%)**, và **Curvature (~2–4%)**.

#### B. [Basis Risk (Rủi ro cơ sở)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/concepts/basis-risk.md)
Phát sinh do sự tương quan không hoàn hảo giữa các chỉ số lãi suất tham chiếu khác nhau áp dụng cho các công cụ có cùng kỳ hạn tái định giá [[src-bcbs-irrbb-2016#^irrbb-u02-2]]:
- **Tenor Basis**: Lệch pha giữa các kỳ hạn của cùng một họ chỉ số (SOFR 1M vs SOFR 3M).
- **Benchmark / Index Basis**: Tài sản cho vay neo theo lãi suất cho vay cơ sở (Prime Rate), nợ tài trợ neo theo SOFR hoặc VNIBOR; hoặc phân kỳ giữa lợi suất TPCP và lãi suất hoán đổi (Treasury-Swap spread).
- **Currency Basis**: Chênh lệch giá vốn khi tài trợ tài sản ngoại tệ bằng nguồn nội tệ qua hợp đồng Cross-Currency Basis Swap (CCBS).

#### C. [Option Risk (Rủi ro quyền chọn)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/concepts/option-risk.md)
- **Quyền chọn Tự động (*Automatic Options*)**: Người nắm giữ chắc chắn thực hiện quyền khi có lợi ích tài chính (hành vi duy lý). Gồm: [Caps, Floors](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/interest-rate-cap-floor.md), [Swaptions](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/swaption.md), hoặc trái phiếu có quyền mua/bán lại (callable/puttable bonds) [[src-bcbs-irrbb-2016#^irrbb-u06-4]]. Khi ngân hàng cam kết trần lãi suất cho vay hoặc sàn lãi suất tiền gửi, ngân hàng đã bán khống quyền chọn (Short Option) [[src-bcbs-irrbb-2016#^irrbb-u05-3]].
- **[Quyền chọn Hành vi (*Behavioural Options*)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/concepts/behavioural-options.md)**: Khách hàng thực hiện quyền chịu tác động của yếu tố tâm lý, chi phí giao dịch, nhân khẩu học:
  1. *[Non-Maturity Deposits (NMDs)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/concepts/non-maturity-deposits.md)*: Khách hàng có quyền rút tiền bất kỳ lúc nào, nhưng số dư tiền gửi lõi lại duy trì ổn định dài hạn với lãi suất thấp [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
  2. *Rủi ro Trả nợ Trước hạn (Prepayment CPR)*: Người vay trả nợ trước hạn ồ ạt khi lãi suất giảm, gây ra **tính lồi âm (Negative Convexity)** và co cụm thời lượng [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
  3. *Rủi ro Rút tiền gửi Có kỳ hạn Sớm (Early Redemption TDRR)*: Rút tiền gửi kỳ hạn trước hạn để gửi sang nơi có lãi suất cao hơn [[src-bcbs-irrbb-2016#^irrbb-u05-6]].

---

## TẦNG 2: Hai Lăng kính Đo lường & Mâu thuẫn Quản trị Kinh điển

### 1. So sánh Chuyên sâu Hai Lăng kính Đo lường

| Đặc tính | [Giá trị Kinh tế của Vốn ($\Delta\text{EVE}$)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/economic-value-of-equity.md) | [Độ nhạy Thu nhập Lãi thuần ($\Delta\text{NII}$)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/net-interest-income-sensitivity.md) |
|---|---|---|
| **Bản chất đo lường** | Biến động giá trị hiện tại thuần (NPV) của toàn bộ dòng tiền sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u06-5]]. | Biến động thu nhập thuần từ lãi trong kỳ kế toán [[src-bcbs-irrbb-2016#^irrbb-u06-5]]. |
| **Đường chân trời** | **Dài hạn — Run-off horizon** cho đến khi vị thế cuối cùng đáo hạn [[src-bcbs-irrbb-2016#^irrbb-p04-2]]. | **Ngắn/Trung hạn — 12 tháng** (công bố) hoặc 1–3 năm [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. |
| **Bảng cân đối** | **Run-off Balance Sheet** (không tái đầu tư) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. | **Constant Balance Sheet** (thay thế tương đương) hoặc Dynamic [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. |
| **Vốn chủ sở hữu** | **Loại trừ hoàn toàn** khỏi dòng tiền chiết khấu [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. | Vốn tự có tạo ra lợi suất nền (*endowment return*) [[src-bcbs-irrbb-2016#^irrbb-u06-6]]. |
| **Cơ chế chiết khấu** | Chiết khấu theo đường cong phi rủi ro (RFR / OIS) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. | Không chiết khấu (tính toán số học thu nhập lãi) [[src-bcbs-irrbb-2016#^irrbb-u06-5]]. |
| **Trọng tâm giám sát** | Cơ quan giám sát: **[[outlier-bank-test\|Outlier Bank Test]] $\Delta\text{EVE} > 15\%$ Tier 1** [[src-bcbs-irrbb-2016#^irrbb-p12-1]]. | Ban điều hành & ALCO: Bảo toàn biên lãi ròng NIM, lợi nhuận P&L và cổ tức [[src-bcbs-irrbb-2016#^irrbb-u02-4]]. |

### 2. Mâu thuẫn Quản trị Kinh điển (The Fundamental EVE vs NII Trade-off)
Một ngân hàng **không thể triệt tiêu đồng thời cả biến động EVE và biến động NII**:
- **Nếu triệt tiêu rủi ro EVE ($\text{DGAP} \approx 0$)**: Bằng cách đưa tài sản về thả nổi ngắn hạn hoặc khớp kỳ hạn ngắn với tiền gửi. Khi lãi suất thị trường giảm sâu, thu nhập từ tài sản giảm ngay lập tức trong khi chi phí tiền gửi có sàn không thể giảm tiếp $\rightarrow$ **Thu nhập lãi thuần $\Delta\text{NII}$ bốc hơi dữ dội**.
- **Nếu triệt tiêu rủi ro NII**: Để bảo vệ thu nhập ổn định cho nguồn vốn tự có và NMDs, ngân hàng đầu tư nguồn vốn này vào một danh mục trái phiếu cố định dài hạn 10 năm. Khi lãi suất thị trường tăng vọt, giá trị thị trường của trái phiếu lao dốc $\rightarrow$ **$\Delta\text{EVE}$ sụt giảm nghiêm trọng, kích hoạt vi phạm ngưỡng ngoại lai 15% Vốn cấp 1**.
- *Bài học Silicon Valley Bank (SVB - 2023)*: Ưu tiên tối đa hóa NII bằng cách gom mua TPCP và MBS dài hạn. Khi lãi suất tăng 500 bps, tổn thất thị trường đã xóa sạch toàn bộ vốn chủ sở hữu ($\Delta\text{EVE} < -\text{Capital}$).

---

## TẦNG 3: Các Mô hình Định lượng Cấu phần (Quantitative Models)

### 1. [Duration Gap Model (Mô hình Chênh lệch Thời lượng - DGAP)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/models/duration-gap-model.md)
Xác định sự thay đổi giá trị kinh tế của vốn chủ sở hữu ($\Delta E$) trước cú sốc lãi suất song song $\Delta y$:

$$\Delta E \approx -\left( D_A - \frac{L}{A} D_L \right) \cdot A \cdot \Delta y + \frac{1}{2} \left( C_A - \frac{L}{A} C_L \right) \cdot A \cdot (\Delta y)^2$$

- **Chỉ số Chênh lệch Thời lượng**: $\text{DGAP} = D_A - k \cdot D_L$ (với $k = L/A$ là đòn bẩy nợ).
- **Hệ số đòn bẩy $k$**: Do ngân hàng hoạt động với đòn bẩy cao ($L/A \approx 90\%$), một chênh lệch thời lượng nhỏ cũng bị khuếch đại gấp 10 lần lên vốn chủ sở hữu.
- **Điều kiện miễn nhiễm hoàn toàn (Redington / Fisher-Weil Immunization)**:
  $$\text{DGAP} = 0 \iff D_A = \left(\frac{L}{A}\right) D_L \quad \text{và} \quad C_A > \left(\frac{L}{A}\right) C_L$$

### 2. [Key Rate Duration (Thời lượng Lãi suất Từng Kỳ hạn - KRD)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/models/key-rate-duration.md)
Khắc phục nhược điểm của Duration tổng thể bằng cách phân rã độ nhạy trên từng điểm kỳ hạn then chốt $k$:

$$\text{KRD}_k = -\frac{1}{P} \frac{\partial P}{\partial y_k}, \quad \sum_{k=1}^{19} \text{KRD}_k = D_{\text{Mod}}$$

- **19 Dải Kỳ hạn Chuẩn hoá Basel d368**: Notional repricing cash flow được phân bổ theo khả năng chuẩn hoá của vị thế [[src-bcbs-irrbb-2016#^irrbb-u05-16]] vào 19 dải kỳ hạn hoặc điểm giữa $t_k$ [[src-bcbs-irrbb-2016#^irrbb-u05-2]], từ Overnight (0.0028 năm) đến trên 20 năm (25 năm) [[src-bcbs-irrbb-2016#^irrbb-u05-25]]; trong mỗi dải, dòng tiền dương và âm được bù trừ thành một vị thế ròng $CF_{i,c}(k)$ [[src-bcbs-irrbb-2016#^irrbb-u05-17]].
- **Công thức giải tích của các cú sốc xoay trục đường cong (Annex 2)**:
  $$\Delta R_{\text{steepener},c}(t_k) = -0.65 \cdot |\Delta R_{\text{short},c}| \cdot e^{-t_k / 4} + 0.9 \cdot |\Delta R_{\text{long},c}| \cdot (1 - e^{-t_k / 4})$$
  $$\Delta R_{\text{flattener},c}(t_k) = +0.8 \cdot |\Delta R_{\text{short},c}| \cdot e^{-t_k / 4} - 0.6 \cdot |\Delta R_{\text{long},c}| \cdot (1 - e^{-t_k / 4})$$
  Hàm suy giảm mũ $e^{-t_k / 4}$ nắm bắt chính xác độ lồi của đường cong mà DGAP tổng thể bỏ qua [[src-bcbs-irrbb-2016#^irrbb-u07-3]].

### 3. [Replicating Portfolio Model (Mô hình Danh mục Tái lập cho NMDs)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/models/replicating-portfolio-model.md)
Mô hình hóa hành vi tiền gửi không kỳ hạn thông qua bài toán tối ưu hóa kinh tế lượng [[src-bcbs-irrbb-2016#^irrbb-u06-6]]:
1. **Phân đoạn**: Tách số dư NMDs thành phần Phi lõi (Non-core, bắt buộc xếp dải qua đêm $T=0$) và phần Lõi (Core deposits) [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
2. **Kỹ thuật Lát cắt Bình quân Trượt (Moving-Average Tranches - Footnote 38)**: Chia tiền gửi lõi thành $M=60$ lát cắt, mỗi tháng tái đầu tư $1/60$ vào tài sản cố định kỳ hạn 5 năm $\rightarrow$ tạo ra kỳ hạn bình quân gia quyền $\text{WAM} = 2.5$ năm và lợi suất bằng đường MA 60 tháng của lãi suất 5 năm.
3. **Quy hoạch Tối ưu hóa**:
   $$\min_{\vec{w}} \text{Var}\left( \sum_{k=1}^K w_k R_k(t) - r_{\text{dep}}(t) \right) \quad \text{hoặc} \quad \max_{\vec{w}} \frac{\mathbb{E}[\text{NIM}] - r_f}{\sigma(\text{NIM})}$$
   Thỏa mãn các trần khống chế nghiêm ngặt tại **Table 2 Basel d368**:
   - Bán lẻ giao dịch: Tiền gửi lõi $\le 90\%$, WAM $\le 5.0$ năm.
   - Bán lẻ phi giao dịch: Tiền gửi lõi $\le 70\%$, WAM $\le 4.5$ năm.
   - Bán buôn: Tiền gửi lõi $\le 50\%$, WAM $\le 4.0$ năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]].

### 4. [Economic Value at Risk (EVaR — Giá trị Kinh tế Chịu Rủi ro)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/models/economic-value-at-risk.md)
- **Ba phương pháp**: (1) *Delta-Normal VaR* dựa trên ma trận hiệp phương sai $\mathbf{\Sigma}$; (2) *Mô phỏng Lịch sử*; (3) *Mô phỏng Monte Carlo* qua mô hình Hull-White.
- **Hạn chế rủi ro đuôi (Tail Risk)**: EVaR thất bại khi các tương quan bị đổ vỡ (Correlation breakdown). Đây là lý do Basel bắt buộc áp dụng **Phép thử Căng thẳng Kịch bản Chuẩn hoá (6 Standardised Shock Scenarios)** và **[[outlier-bank-test|Outlier Bank Test]]** làm căn cứ giám sát Trụ cột 2 thay vì mô hình nội bộ của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u06-7]].

---

## TẦNG 4: Công cụ Tài chính Phòng ngừa & Tái cấu trúc Thời lượng

### 1. [Interest Rate Swap (Hợp đồng Hoán đổi Lãi suất - IRS)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/interest-rate-swap.md)
IRS là công cụ điều tiết thời lượng thanh khoản cao và chi phí thấp nhất của ALM Treasury:
- **Payer Swap (Trả cố định, nhận thả nổi)**: Thời lượng âm ($\text{Duration} < 0$). Rút ngắn thời lượng tài sản, phòng ngừa rủi ro cho danh mục trái phiếu cố định dài hạn khi dự báo lãi suất tăng [[src-bcbs-irrbb-2016#^irrbb-p12-3]].
- **Receiver Swap (Nhận cố định, trả thả nổi)**: Thời lượng dương ($\text{Duration} > 0$). Kéo dài thời lượng, khóa chặt lợi suất tài sản khi bước vào chu kỳ hạ lãi suất.
- **Công thức Khớp DV01**:
  $$\text{Notional}_{\text{IRS}} = \frac{\Delta\text{EVE}_{\text{Balance Sheet}}}{\text{DV01}_{\text{IRS, unit}}}$$

### 2. [Interest Rate Caps, Floors và Collars](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/interest-rate-cap-floor.md)
- **Cap**: Mua Cap để giới hạn trần chi phí huy động vốn thả nổi.
- **Floor**: Mua Floor để bảo vệ lợi suất sàn cho các khoản cho vay lãi suất thả nổi khi thị trường nới lỏng tiền tệ.
- **Chiến lược Zero-Cost Collar**: Mua Cap và đồng thời bán Floor sao cho phí mua bằng đúng phí bán ($\text{Premium}_{\text{cap}} = \text{Premium}_{\text{floor}}$), thiết lập hành lang chi phí vốn mà không tốn dòng tiền ban đầu.
- **Phụ trội vốn $\text{KAO}_{i,c}$ của Basel**: Toàn bộ vị thế quyền chọn tự động đã bán (sold options) phải được định giá lại dưới mức tăng **25% độ biến động ngầm định ($\Delta\sigma / \sigma = +25\%$)** kết hợp với 6 kịch bản sốc lãi suất để tính phần bù rủi ro vốn quy định [[src-bcbs-irrbb-2016#^irrbb-u05-7]].

### 3. [Swaptions (Quyền chọn Hoán đổi Lãi suất)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/swaption.md)
- **Receiver Swaption (Quyền nhận cố định, trả thả nổi)**: Công cụ phòng ngừa hoàn hảo cho rủi ro trả nợ trước hạn (Prepayment). Khi lãi suất giảm sâu, người vay đảo nợ làm sụt giảm thu nhập lãi, nhưng giá trị hợp đồng Receiver Swaption tăng vọt, bù đắp chính xác tổn thất dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- **Bermudan Style Swaption**: Cho phép thực thi quyền tại nhiều ngày thanh toán định kỳ trong tương lai, khớp hoàn toàn với bản chất quyền trả nợ trước hạn linh hoạt của khách hàng cá nhân.

---

## TẦNG 5: Kiến trúc Điều chuyển Giá vốn Nội bộ (IRRBB FTP Architecture)

Cơ chế Định giá Điều chuyển Vốn Nội bộ (Funds Transfer Pricing - FTP) là "hệ thần kinh trung ương" giúp ngân hàng thương mại phân tách và quản trị rủi ro lãi suất một cách tập trung:

$$\text{Customer Lending Rate} = \text{Base Benchmark Rate} + \text{Liquidity Spread} + \text{Behavioral Option Charge} + \text{Commercial Margin}$$

1. **Base Benchmark Rate (Lãi suất Tham chiếu Kỳ hạn Khớp)**: Lãi suất phi rủi ro trên đường cong chuẩn (RFR/OIS) tương ứng với kỳ hạn tái định giá của hợp đồng. Toàn bộ phần này được chuyển về ALM Treasury để tập trung trạng thái [Gap Risk](file:///d:/AI/202610%20ALM%20wiki/02_wiki/concepts/gap-risk.md).
2. **Liquidity Spread (Phần bù Thanh khoản Kỳ hạn)**: Chi phí bù đắp thời gian nắm giữ thanh khoản theo chuẩn [LCR](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/lcr.md) và [NSFR](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/nsfr.md) (tài sản kỳ hạn càng dài thì chịu chi phí [RSF](file:///d:/AI/202610%20ALM%20wiki/02_wiki/metrics/required-stable-funding.md) càng lớn).
3. **Behavioral Option Charge (Phí Bù trừ Quyền chọn Hành vi)**:
   - Các khoản vay thế chấp cho phép trả nợ trước hạn không phạt bắt buộc phải chịu một khoản phụ phí (ví dụ $+25$ bps).
   - Khoản phí thu từ khách hàng này được chuyển về Treasury làm **ngân sách phòng hộ (Hedging Budget)** để Treasury mua các hợp đồng [Swaptions](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/swaption.md) trên thị trường phái sinh nhằm trung hòa tính lồi âm.
4. **Commercial Margin (Biên độ Lợi nhuận Thương mại)**: Phần chênh lệch lợi nhuận thuần túy phản ánh công sức tìm kiếm khách hàng và quản lý rủi ro tín dụng của chi nhánh.

---

## Bốn Thách thức Thực chiến & Vùng Ranh giới Phức tạp

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    4 THÁCH THỨC THỰC CHIẾN CỦA KIẾN TRÚC 5 TẦNG                         │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. RỦI RO MÔ HÌNH HÀNH VI (TẦNG 3 LÀ GÓT CHÂN ACHILLES):                                │
│    • Giả định CASA "bám dính" có thể sụp đổ trong vài ngày (Bài học SVB 2023).          │
│    • Nếu Tầng 3 mô hình hóa sai, Tầng 4 sẽ phòng hộ ngược (Over-hedging tai hại).       │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. XUNG ĐỘT KẾ TOÁN IFRS 9 (RÀO CẢN GIỮA TẦNG 4 VÀ P&L):                                │
│    • Phòng ngừa kinh tế hoàn hảo (T4) có thể gây biến động dữ dội trên báo cáo P&L      │
│      nếu không đáp ứng các điều kiện khắt khe của Fair Value Hedge Accounting.          │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. SỰ CÔ LẬP CỦA IRRBB VỚI THANH KHOẢN (LCR/NSFR) VÀ VỐN (LEVERAGE RATIO):             │
│    • IRRBB không đứng một mình. Tối ưu hóa IRRBB có thể phá vỡ LCR hoặc NSFR:           │
│      - Mua phái sinh (T4) làm phình to phơi lượng ngoại bảng và tiêu hao thế chấp.      │
│      - Đệm TPCP Level 1 của LCR chính là "quả bom thời lượng" của EVE trong IRRBB.      │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. SỰ TRỖI DẬY CỦA CSRBB (TẦNG 1):                                                      │
│    • Basel d368 chỉ coi CSRBB là rủi ro liên đới, nhưng EBA (Châu Âu) đã bắt buộc lượng │
│      hóa CSRBB độc lập. Spread dãn rộng có thể xóa sạch vốn trước khi IRRBB kịp phát tác.│
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

1. **Rủi ro Mô hình Hành vi (Gót chân Achilles của Tầng 3)**: Tất cả tính toán tinh vi ở Tầng 4 và Tầng 5 đều dựa trên giả định NMDs bám dính. Trong kỷ nguyên ngân hàng số, khi dòng tiền rút chạy chỉ trong vài cú chạm ứng dụng di động, giả định CASA sụp đổ sẽ đẩy ngân hàng vào trạng thái phòng hộ ngược (*over-hedged*) đầy tai họa.
2. **Xung đột Kế toán Phòng ngừa Rủi ro IFRS 9**: Phái sinh ở Tầng 4 hạch toán theo Giá trị Hợp lý (Fair Value through P&L), trong khi tài sản sổ ngân hàng thường ghi nhận theo Giá gốc Phân bổ (Amortised Cost). Nếu không đủ điều kiện áp dụng Fair Value Hedge Accounting, việc phòng hộ kinh tế hoàn hảo lại gây biến động lợi nhuận P&L giả tạo.
3. **Cạm bẫy Tương tác Liên chỉ số (LCR $\times$ NSFR $\times$ IRRBB $\times$ Leverage)**: Đệm trái phiếu chính phủ Level 1 dồi dào để đáp ứng [[lcr]] và [[nsfr]] chính là nguồn cơn tạo ra rủi ro thời lượng EVE lớn nhất; việc phòng hộ bằng IRS lại làm tăng tài sản tiềm tàng ngoại bảng và tiêu hao hạn mức đòn bẩy Leverage Ratio.
4. **Sự trỗi dậy của CSRBB**: Cơ quan Ngân hàng Châu Âu (EBA Guidelines 2022/14) đã bắt buộc tách biệt và lượng hóa độc lập CSRBB. Đây là xu hướng tất yếu mà các ngân hàng hiện đại phải tích hợp vào Tầng 1.

---

## Ma trận Tương tác 5 Tầng trong Điều hành ALCO

| Tầng | Câu hỏi Chiến lược của ALCO | Mô hình Định lượng Cốt lõi | Công cụ Thực thi / Cơ chế Điều hành |
|:---:|---|---|---|
| **Tầng 1** | Ngân hàng đang chịu những loại rủi ro lãi suất cụ thể nào? | Phân tích 5 thành phần lãi suất & PCA | Bóc tách sổ ngân hàng, nhận diện các quyền chọn nhúng |
| **Tầng 2** | Sự đánh đổi giữa an toàn Vốn (EVE) và Thu nhập (NII) nằm ở đâu? | Mô phỏng Run-off vs Constant Balance Sheet | Thiết lập hệ thống hạn mức ALCO 4 tầng & [[outlier-bank-test\|Outlier Test]] (15% Tier 1) |
| **Tầng 3** | Mức độ tổn thất định lượng chính xác là bao nhiêu bps/triệu USD? | [DGAP](file:///d:/AI/202610%20ALM%20wiki/02_wiki/models/duration-gap-model.md), [KRD](file:///d:/AI/202610%20ALM%20wiki/02_wiki/models/key-rate-duration.md), [Replicating Portfolio](file:///d:/AI/202610%20ALM%20wiki/02_wiki/models/replicating-portfolio-model.md), [EVaR](file:///d:/AI/202610%20ALM%20wiki/02_wiki/models/economic-value-at-risk.md) | Chạy 6 kịch bản sốc Basel Annex 2 & Stress Testing |
| **Tầng 4** | Cần sử dụng công cụ phái sinh nào để trung hòa trạng thái rủi ro? | Định giá No-Arbitrage, Black-76, DV01 Matching | [IRS (Payer/Receiver)](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/interest-rate-swap.md), [Caps/Floors](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/interest-rate-cap-floor.md), [Swaptions](file:///d:/AI/202610%20ALM%20wiki/02_wiki/instruments/swaption.md) |
| **Tầng 5** | Làm thế nào để truyền dẫn kỷ luật rủi ro xuống toàn bộ mạng lưới? | Khung Matched-Maturity FTP 4 cấu phần | Biểu giá FTP nội bộ, Phí bù quyền chọn hành vi |

## Đề xuất cập nhật
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại mục "19 Dải Kỳ hạn Chuẩn hoá Basel d368" (dòng 149). → đã rà [2026-10-18]
- [2026-10-18] research (rà sau U05 bổ sung) — đề xuất cho dòng 149 "19 Dải Kỳ hạn Chuẩn hoá Basel d368", chờ user duyệt: → đã áp [2026-10-19]
  - Việc bù trừ dòng tiền dương và âm trong mỗi dải thành một vị thế ròng là bước 1 của par 132, nên cite thêm [[src-bcbs-irrbb-2016#^irrbb-u05-17]]; việc phân bổ theo khả năng chuẩn hoá của vị thế cite [[src-bcbs-irrbb-2016#^irrbb-u05-16]] (par 105). Giữ [[src-bcbs-irrbb-2016#^irrbb-u05-2]] cho 19 dải và điểm giữa dải.
  - Hai mốc "0.0028 năm" và "22.5 năm" không có trong claim u05-2 (claim chỉ nêu "Table 1"); cần `/ingest src-bcbs-irrbb-2016 u05` bổ sung claim Table 1 hoặc bỏ hai mốc.
  - Đề xuất viết lại: "Notional repricing cash flow được slot vào 19 dải kỳ hạn hoặc điểm giữa $t_k$ [[src-bcbs-irrbb-2016#^irrbb-u05-2]]; trong mỗi dải, dòng tiền dương và âm được bù trừ thành một vị thế ròng $CF_{i,c}(k)$ [[src-bcbs-irrbb-2016#^irrbb-u05-17]]."
