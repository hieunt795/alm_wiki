---
title: "Cơ chế truyền dẫn FTP đến các risk factors"
aliases: [src-ftp-transmission-analysis, FTP Transmission Analysis, Co che truyen dan FTP]
type: source
source_id: src-ftp-transmission-analysis
domains: [alm]
status: active
maturity: draft
tier: T5
doc_status: draft
issuer: Không rõ
published: 2026-10-15
raw: 01_sources/alm/ftp_transmission_analysis.md
units_done: [u01]
updated: 2026-10-22
---

## Thông tin nguồn
- Tiêu đề: *Cơ chế truyền dẫn FTP đến các risk factors — Nghiên cứu chi tiết về vai trò của Funds Transfer Pricing trong Quản trị Rủi ro Ngân hàng*.
- Cơ sở lý thuyết: Dựa trên framework lý thuyết từ chuyên khảo *Asset Liability Management Optimisation: A Practitioner's Guide to Balance Sheet Management and Remodelling* của Beata Lubinska (Wiley Finance 2020) kết hợp với thực tiễn hệ thống ngân hàng Việt Nam.
- Tier: T5 (tài liệu phân tích chuyên sâu tổng hợp; chưa xác định rõ danh tính tác giả xuất bản chính thức).
- File raw: `01_sources/alm/ftp_transmission_analysis.md` (189 dòng).
- Unit ingest: `u01` (lines 1–189).

## Tóm tắt Nội dung và Khẳng định Then chốt

### 1. Vai trò Hệ thống Điều khiển Trung tâm (Unified Control Mechanism)
- FTP không chỉ là một cơ chế kỹ thuật để hạch toán lợi nhuận nội bộ giữa các phòng ban mà đóng vai trò là một hệ thống điều khiển trung tâm trong quản trị bảng cân đối kế toán ngân hàng.
  > "Funds Transfer Pricing (FTP) không chỉ đơn thuần là công cụ định giá nội bộ mà đóng vai trò như một hệ thống điều khiển trung tâm (unified control mechanism) trong quản trị bảng cân đối ngân hàng."
  > — u01 ^ftp-trans-1

- FTP liên kết đồng thời và điều phối ba loại rủi ro trọng yếu nhất của bảng cân đối:
  > "FTP tác động đồng thời đến ba loại rủi ro chính thông qua các kênh truyền dẫn riêng biệt nhưng có tương tác lẫn nhau: Rủi ro Thanh khoản (RRTK), Rủi ro Lãi suất (RRLS), và Rủi ro Tín dụng (RRTD)."
  > — u01 ^ftp-trans-2

### 2. Cấu trúc Lãi suất FTP Tổng quát
- Lãi suất FTP được phân rã thành bốn cấu phần rủi ro riêng biệt:
  > "FTP Rate = Base Rate + Liquidity Spread + Credit Spread + Optionality Cost"
  > — u01 ^ftp-trans-3

Chi tiết từng thành phần:
- Base Rate là lãi suất tham chiếu phi rủi ro phản ánh chi phí cơ hội của vốn và chính sách tiền tệ.
  > "Base Rate là lãi suất tham chiếu phi rủi ro (VNIBOR, lãi suất SBV), phản ánh chi phí cơ hội của vốn và chính sách tiền tệ."
  > — u01 ^ftp-trans-4
- Liquidity Spread là phần bù thanh khoản theo kỳ hạn, phản ánh chi phí huy động vốn biên tế và tuân thủ LCR/NSFR.
  > "Liquidity Spread là phần bù thanh khoản theo kỳ hạn (term liquidity premium), phản ánh chi phí huy động vốn biên tế (marginal cost of funding) và yêu cầu tuân thủ LCR/NSFR."
  > — u01 ^ftp-trans-5
- Credit Spread bao gồm chi phí rủi ro tín dụng và chi phí vốn kinh tế, phản ánh xếp hạng tín dụng của chính ngân hàng và đối tác.
  > "Credit Spread bao gồm chi phí rủi ro tín dụng (expected loss charge) và chi phí vốn kinh tế (economic capital cost), phản ánh xếp hạng tín dụng của chính ngân hàng và đối tác."
  > — u01 ^ftp-trans-6
- Optionality Cost là chi phí của các quyền chọn ngầm như rủi ro trả nợ trước hạn và rút tiền sớm, tác động đến rủi ro hành vi.
  > "Optionality Cost là chi phí của các quyền chọn ngầm (embedded options) như rủi ro trả nợ trước hạn (prepayment risk) và rút tiền sớm (early redemption), tác động đến rủi ro hành vi (behavioral risk)."
  > — u01 ^ftp-trans-7

### 3. Kênh Truyền dẫn đến Rủi ro Thanh khoản (RRTK)
- FTP điều tiết thanh khoản bằng cách gán chi phí / lợi ích biên tế của thanh khoản trực tiếp vào biểu giá điều chuyển vốn:
  > "Nếu LCR thấp (thiếu thanh khoản ngắn hạn), tăng spread cho các tenor ngắn (O/N đến 30 ngày). Nếu NSFR thấp (thiếu nguồn vốn ổn định), tăng spread cho các tenor dài (6M đến 2Y trở lên)."
  > — u01 ^ftp-trans-8

Cơ chế này khuyến khích Liability Center tích cực huy động nguồn vốn kỳ hạn dài và hạn chế Asset Center giải ngân các khoản vay dài hạn làm tiêu hao nguồn vốn ổn định.

### 4. Kênh Truyền dẫn đến Rủi ro Lãi suất (IRRBB)
- Điểm cốt lõi của FTP hiện đại là cô lập hoàn toàn rủi ro lãi suất khỏi các đơn vị kinh doanh và chuyển giao tập trung về ALM / Treasury:
  > "Điểm mấu chốt là FTP tự động tách biệt IRRBB từ Business Units và chuyển giao toàn bộ về ALM để quản lý tập trung."
  > — u01 ^ftp-trans-9

- Business Units chỉ thấy fixed margin, ALM kế thừa toàn bộ mismatch giữa asset repricing và liability repricing:
  > "Business Units không còn exposure với repricing risk vì họ chỉ thấy fixed margin (customer rate - FTP rate). ALM kế thừa toàn bộ mismatch giữa asset repricing và liability repricing."
  > — u01 ^ftp-trans-10

Thông qua cơ chế định giá phù hợp kỳ hạn, ALM chịu trách nhiệm quản lý khe hở định giá lại, độ nhạy NII và EVE.

### 5. Kênh Truyền dẫn đến Rủi ro Tín dụng & Chi phí Vốn (RAROC)
- FTP tích hợp chi phí tổn thất kỳ vọng (Expected Loss) để cover expected loss của danh mục:
  > "Expected Loss (EL) Charge: FTP bao gồm một khoản charge để cover expected loss của danh mục. EL = PD × LGD × EAD"
  > — u01 ^ftp-trans-11

- Capital Charge là chi phí vốn cho Unexpected Loss:
  > "Capital Charge: Ngoài EL, FTP còn bao gồm chi phí vốn cho Unexpected Loss. Capital Charge = RWA × Capital Ratio × Cost of Equity."
  > — u01 ^ftp-trans-12

Nhờ vậy, mỗi khoản tín dụng tại từng đơn vị kinh doanh đều được đánh giá hiệu quả trên cơ sở lợi nhuận điều chỉnh theo rủi ro (RAROC deal-level):
$$\text{RAROC} = \frac{\text{Doanh thu} - \text{Chi phí vốn (FTP)} - \text{EL} - \text{Chi phí hoạt động}}{\text{Vốn kinh tế (Economic Capital)}}$$

### 6. Hệ Thống Phản Hồi Tích Hợp và Tối Ưu Hóa Bảng Cân Đối
- Quản trị bảng cân đối ALM vận hành như một vòng lặp kín:
  > "Basel III Signals (LCR, NSFR, ΔNII, ΔEVE, CAR) → FTP Engine Calibration → Business Unit Behavior Change → Balance Sheet Reshape → Risk Metrics Improve → Re-monitor → Re-calibration"
  > — u01 ^ftp-trans-13

- Công thức định giá tổng hợp cho tài sản:
  > "FTP_Asset(t,T) = BaseRate(t,T) + LiqSpread(T) × LCR_adj × NSFR_adj + CreditSpread(rating) × PD × LGD + OptionCost(prepay) + CapitalCharge(RWA × CoE)"
  > — u01 ^ftp-trans-14

### 7. Bổ sung 2026-10-22 — công thức điều chỉnh, ví dụ, steering và cân bằng
- Công thức điều chỉnh Liquidity Spread: kỳ ngắn tăng theo α nhân khoảng cách LCR dưới target, kỳ dài tăng theo β nhân khoảng cách NSFR dưới target; α do ALCO quyết định. Nguồn nêu target 110% (LCR) và 105% (NSFR) làm ví dụ.
  > "ΔSpread\_short = α × (LCR\_target - LCR\_actual), trong đó α là hệ số nhạy cảm do ALCO quyết định."
  > "ΔSpread\_long = β × (NSFR\_target - NSFR\_actual)."
  > — u01 §2.2 ^ftp-trans-15

- Ví dụ minh hoạ của nguồn: ngân hàng X có LCR 105% (target 115%), NSFR 102% (target 108%); ALM tăng Liquidity Spread kỳ 1W-1M thêm 30-50 bps và kỳ 6M-2Y thêm 50-80 bps; sau 3-6 tháng LCR lên 118%, NSFR lên 108%.
  > "Giả sử ngân hàng X có LCR = 105% (target 115%) và NSFR = 102% (target 108%)."
  > "Tăng Liquidity Spread cho tenor 1W-1M thêm 30-50 bps"
  > "Tăng Liquidity Spread cho tenor 6M-2Y thêm 50-80 bps"
  > "Kết quả sau 3-6 tháng: LCR tăng lên 118%, NSFR tăng lên 108%, đạt target."
  > — u01 §2.3 ^ftp-trans-16

- Tín hiệu kênh thanh khoản: ALM theo dõi LCR, NSFR, Survival Horizon và Structural Ratio; chỉ số tiến gần hoặc vi phạm ngưỡng cảnh báo thì kích hoạt điều chỉnh.
  > "ALM theo dõi liên tục các chỉ số thanh khoản bao gồm LCR (Liquidity Coverage Ratio), NSFR (Net Stable Funding Ratio), Survival Horizon, và Structural Ratio."
  > "Khi các chỉ số này tiến gần hoặc vi phạm ngưỡng cảnh báo, tín hiệu điều chỉnh được kích hoạt."
  > — u01 §2.1 ^ftp-trans-17

- Phản ứng của Business Units ở kênh thanh khoản: Liability Center tăng huy động ở kỳ hạn được khuyến khích; Asset Center giảm cho vay ở kỳ hạn có chi phí vốn cao; cấu trúc tài sản-nợ cải thiện LCR và NSFR.
  > "Liability Center phản ứng với FTP cao hơn bằng cách tăng cường huy động vốn ở các kỳ hạn được khuyến khích"
  > "Asset Center phản ứng bằng cách giảm cho vay ở các kỳ hạn có chi phí vốn cao (vì margin bị thu hẹp)."
  > "Kết quả là cấu trúc tài sản-nợ thay đổi theo hướng cải thiện LCR và NSFR."
  > — u01 §2.1 ^ftp-trans-18

- Cơ chế chuyển giao rủi ro lãi suất: Asset Center cho vay cố định 5 năm nhận vốn từ ALM theo FTP rate cố định 5 năm; Liability Center huy động 3 tháng bán vốn cho ALM theo FTP rate 3 tháng.
  > "Khi Asset Center cho vay một khoản vay cố định 5 năm, họ nhận vốn từ ALM với FTP rate cố định 5 năm. Khi Liability Center huy động tiền gửi 3 tháng, họ bán vốn cho ALM với FTP rate 3 tháng."
  > — u01 §3.1 ^ftp-trans-19

- Steering kênh lãi suất: ALM có thể điều chỉnh FTP curve theo hướng penalize mismatch (tăng spread cho tenor có gap lớn, giảm spread hoặc thêm reward cho matched funding) khi ΔNII hoặc ΔEVE tiến gần hoặc vi phạm limit.
  > "tăng spread cho các tenor có gap lớn, giảm spread (hoặc thêm reward) cho matched funding."
  > "Khi ΔNII hoặc ΔEVE tiến gần hoặc vi phạm limit, ALM có thể điều chỉnh FTP curve để steering hành vi của BUs."
  > — u01 §3.1–3.2 ^ftp-trans-20

- Basis risk: phát sinh khi assets và liabilities repriced theo benchmark khác nhau (ví dụ VNIBOR 1M so với VNIBOR 3M, hoặc VNIBOR so với lãi suất điều hành SBV); FTP curve riêng cho từng benchmark giúp theo dõi, và chi phí hedge có thể đưa vào FTP.
  > "Basis risk phát sinh khi assets và liabilities được repriced theo các benchmark khác nhau"
  > "Bằng cách thiết lập FTP curve riêng cho từng benchmark và áp dụng cross-currency/cross-index adjustment, ALM có thể theo dõi và kiểm soát basis risk exposure."
  > "Chi phí hedge basis risk có thể được incorporate vào FTP để pass through cho BUs."
  > — u01 §3.3 ^ftp-trans-21

- Rating-based pricing grid: rating cao (AAA-A) có credit spread thấp, rating thấp (BB trở xuống) có credit spread cao.
  > "Khách hàng có rating cao (AAA-A) có credit spread thấp, trong khi khách hàng có rating thấp (BB trở xuống) có credit spread cao."
  > — u01 §4.2 ^ftp-trans-22

- Khi CAR tiến gần regulatory minimum, ALM có thể tăng Capital Charge trong FTP để hạn chế tăng trưởng tài sản và khuyến khích deal có RWA density thấp hơn.
  > "Khi CAR (Capital Adequacy Ratio) của ngân hàng tiến gần regulatory minimum, ALM có thể tăng Capital Charge component trong FTP"
  > — u01 §4.2 ^ftp-trans-23

- RAROC cấp deal = (Revenue - Funding Cost - EL - Operating Cost) / Economic Capital; deal có RAROC dưới hurdle rate không được chấp thuận hoặc phải reprice. FTP là công cụ để operationalize RAROC.
  > "FTP là công cụ quan trọng để operationalize RAROC (Risk-Adjusted Return on Capital) framework."
  > "RAROC tại deal level = (Revenue - Funding Cost - EL - Operating Cost) / Economic Capital"
  > "deal không được chấp thuận hoặc phải reprice."
  > — u01 §4.3 ^ftp-trans-24

- CoE trong công thức FTP là hurdle rate của cổ đông, thường 12-15%.
  > "Cost of Equity hurdle rate (thường 12-15%)"
  > — u01 §6.1 ^ftp-trans-25

- Tương tác chéo giữa các kênh: tăng liquidity spread dài hạn để cải thiện NSFR làm duration tài sản ngắn lại, ΔEVE giảm; tăng capital charge để cải thiện CAR đẩy BU sang tài sản RWA thấp (ví dụ HQLA), LCR cải thiện.
  > "Tăng liquidity spread dài hạn để cải thiện NSFR → Asset Center giảm cho vay dài hạn → Duration của asset portfolio ngắn lại → ΔEVE giảm → RRLS cải thiện."
  > "Tăng capital charge để cải thiện CAR → BUs tập trung vào low-RWA assets (ví dụ HQLA) → Liquidity buffer tăng → LCR cải thiện."
  > — u01 §5.3 ^ftp-trans-26

- Trạng thái cân bằng của ba kênh: LCR/NSFR đạt target thì ALM giảm liquidity spread về mức bình thường; Gap trong limit và ΔNII/ΔEVE ổn định thì FTP curve không cần điều chỉnh; CAR đủ buffer thì credit spread phản ánh rủi ro từng rating bucket.
  > "Khi LCR/NSFR đạt target, ALM giảm liquidity spread về mức"
  > "Khi Gap trong limit và ΔNII/ΔEVE ổn định, FTP curve không cần điều chỉnh."
  > "Khi CAR có đủ buffer, credit spread reflect true risk của từng rating bucket."
  > — u01 §5.2 ^ftp-trans-27

- Chu kỳ phản hồi diễn ra liên tục, thường hằng tháng hoặc hằng quý tuỳ biến động của thị trường và bảng cân đối.
  > "Chu kỳ này diễn ra liên tục, thường là hàng tháng hoặc hàng quý tùy theo mức độ biến động của thị trường và bảng cân đối."
  > — u01 §5.1 ^ftp-trans-28

- Khuyến nghị triển khai của nguồn: thiết lập FTP governance framework với vai trò của ALCO trong việc approve FTP curve và steering adjustments; định kỳ review và back-test để calibrate các hệ số α, β, γ, δ, ε, ζ.
  > "thiết lập FTP governance framework rõ ràng với vai trò của ALCO trong việc approve FTP curve và steering adjustments."
  > "định kỳ review và back-test effectiveness của FTP steering để calibrate các hệ số α, β, γ, δ, ε, ζ"
  > — u01 §7.2 ^ftp-trans-29

## Khái niệm và Liên kết
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản tổng quát.
- [[ftp-transmission-mechanism]]: Chi tiết phân tích các kênh truyền dẫn FTP đến rủi ro thanh khoản, lãi suất, tín dụng và vốn.
- [[ftp-pricing-methodology]]: Phương pháp định giá chi tiết các cấu phần VOF, COF, phụ phí pháp định và quyền chọn ẩn.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn Basel III.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn Basel III.
- [[bcbs-irrbb]]: Rủi ro lãi suất trên sổ ngân hàng theo tiêu chuẩn Basel.
