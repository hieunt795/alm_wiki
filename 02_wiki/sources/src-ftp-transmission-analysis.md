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
updated: 2026-10-16
---

## Thông tin nguồn
- Tiêu đề: *Cơ chế truyền dẫn FTP đến các risk factors — Nghiên cứu chi tiết về vai trò của Funds Transfer Pricing trong Quản trị Rủi ro Ngân hàng*.
- Cơ sở lý thuyết: Dựa trên framework lý thuyết từ chuyên khảo *Asset Liability Management Optimisation: A Practitioner's Guide to Balance Sheet Management and Remodelling* của Beata Lubinska (Wiley Finance 2020) kết hợp với thực tiễn hệ thống ngân hàng Việt Nam.
- Tier: T5 (tài liệu phân tích chuyên sâu tổng hợp; chưa xác định rõ danh tính tác giả xuất bản chính thức).
- File raw: `01_sources/alm/ftp_transmission_analysis.md` (189 dòng).
- Unit ingest: `u01` (lines 1–189).

## Tóm tắt Nội dung và Khẳng định Then chốt

### 1. Vai trò Hệ thống Điều khiển Trung tâm (Unified Control Mechanism)
FTP không chỉ là một cơ chế kỹ thuật để hạch toán lợi nhuận nội bộ giữa các phòng ban mà đóng vai trò là một **hệ thống điều khiển trung tâm** (unified control mechanism) trong quản trị bảng cân đối kế toán ngân hàng.

> "Funds Transfer Pricing (FTP) không chỉ đơn thuần là công cụ định giá nội bộ mà đóng vai trò như một hệ thống điều khiển trung tâm (unified control mechanism) trong quản trị bảng cân đối ngân hàng." ^ftp-trans-1

FTP liên kết đồng thời và điều phối ba loại rủi ro trọng yếu nhất của bảng cân đối:

> "FTP tác động đồng thời đến ba loại rủi ro chính thông qua các kênh truyền dẫn riêng biệt nhưng có tương tác lẫn nhau: Rủi ro Thanh khoản (RRTK), Rủi ro Lãi suất (RRLS), và Rủi ro Tín dụng (RRTD)." ^ftp-trans-2

### 2. Cấu trúc Lãi suất FTP Tổng quát
Lãi suất FTP được phân rã thành bốn cấu phần rủi ro riêng biệt:

> "FTP Rate = Base Rate + Liquidity Spread + Credit Spread + Optionality Cost" ^ftp-trans-3

Chi tiết từng thành phần:
- **Base Rate (Lãi suất cơ sở phi rủi ro)**:
  > "Base Rate là lãi suất tham chiếu phi rủi ro (VNIBOR, lãi suất SBV), phản ánh chi phí cơ hội của vốn và chính sách tiền tệ." ^ftp-trans-4
- **Liquidity Spread (Phần bù thanh khoản kỳ hạn)**:
  > "Liquidity Spread là phần bù thanh khoản theo kỳ hạn (term liquidity premium), phản ánh chi phí huy động vốn biên tế (marginal cost of funding) và yêu cầu tuân thủ LCR/NSFR." ^ftp-trans-5
- **Credit Spread & Capital Charge**:
  > "Credit Spread bao gồm chi phí rủi ro tín dụng (expected loss charge) và chi phí vốn kinh tế (economic capital cost), phản ánh xếp hạng tín dụng của chính ngân hàng và đối tác." ^ftp-trans-6
- **Optionality Cost (Chi phí quyền chọn ngầm)**:
  > "Optionality Cost là chi phí của các quyền chọn ngầm (embedded options) như rủi ro trả nợ trước hạn (prepayment risk) và rút tiền sớm (early redemption), tác động đến rủi ro hành vi (behavioral risk)." ^ftp-trans-7

### 3. Kênh Truyền dẫn đến Rủi ro Thanh khoản (RRTK)
FTP điều tiết thanh khoản bằng cách gán chi phí / lợi ích biên tế của thanh khoản trực tiếp vào biểu giá điều chuyển vốn:
- Khi ngân hàng đối mặt với áp lực thanh khoản ngắn hạn hoặc chỉ số [[lcr|LCR]] tiệm cận ngưỡng tối thiểu: ALM tăng spread ở các kỳ hạn ngắn.
- Khi ngân hàng thiếu hụt nguồn vốn trung dài hạn ổn định để thỏa mãn [[nsfr|NSFR]]: ALM tăng spread ở các kỳ hạn dài.

> "Nếu LCR thấp (thiếu thanh khoản ngắn hạn), tăng spread cho các tenor ngắn (O/N đến 30 ngày). Nếu NSFR thấp (thiếu nguồn vốn ổn định), tăng spread cho các tenor dài (6M đến 2Y trở lên)." ^ftp-trans-8

Cơ chế này khuyến khích Liability Center tích cực huy động nguồn vốn kỳ hạn dài (nhận được giá bán vốn VOF cao từ ALM) và hạn chế Asset Center giải ngân các khoản vay dài hạn làm tiêu hao nguồn vốn ổn định (do bị charge giá mua vốn COF cao).

### 4. Kênh Truyền dẫn đến Rủi ro Lãi suất (IRRBB)
Điểm cốt lõi của FTP hiện đại là **cô lập hoàn toàn rủi ro lãi suất khỏi các đơn vị kinh doanh (Business Units)** và chuyển giao tập trung về ALM / Treasury:

> "Điểm mấu chốt là FTP tự động tách biệt IRRBB từ Business Units và chuyển giao toàn bộ về ALM để quản lý tập trung." ^ftp-trans-9

> "Business Units không còn exposure với repricing risk vì họ chỉ thấy fixed margin (customer rate - FTP rate). ALM kế thừa toàn bộ mismatch giữa asset repricing và liability repricing." ^ftp-trans-10

Thông qua cơ chế định giá phù hợp kỳ hạn (matched-maturity pricing), ALM chịu trách nhiệm quản lý khe hở định giá lại ([[gap-risk]]), độ nhạy thu nhập lãi thuần ([[net-interest-income-sensitivity|ΔNII]]), và giá trị kinh tế của vốn chủ sở hữu ([[economic-value-of-equity|ΔEVE]]). Khi khe hở kỳ hạn vượt hạn mức rủi ro, ALM dùng FTP để khuyến khích hoặc phạt các kỳ hạn cụ thể nhằm tái lập cân bằng.

### 5. Kênh Truyền dẫn đến Rủi ro Tín dụng & Chi phí Vốn (RAROC)
FTP tích hợp chi phí tổn thất kỳ vọng (Expected Loss) và tổn thất ngoài kỳ vọng (Unexpected Loss / Chi phí vốn kinh tế):

> "Expected Loss (EL) Charge: FTP bao gồm một khoản charge để cover expected loss của danh mục. EL = PD × LGD × EAD" ^ftp-trans-11

> "Capital Charge: Ngoài EL, FTP còn bao gồm chi phí vốn cho Unexpected Loss. Capital Charge = RWA × Capital Ratio × Cost of Equity." ^ftp-trans-12

Nhờ vậy, mỗi khoản tín dụng tại từng đơn vị kinh doanh đều được đánh giá hiệu quả trên cơ sở lợi nhuận điều chỉnh theo rủi ro (RAROC deal-level):
$$\text{RAROC} = \frac{\text{Doanh thu} - \text{Chi phí vốn (FTP)} - \text{EL} - \text{Chi phí hoạt động}}{\text{Vốn kinh tế (Economic Capital)}}$$

### 6. Hệ Thống Phản Hồi Tích Hợp và Tối Ưu Hóa Bảng Cân Đối
Quản trị bảng cân đối ALM vận hành như một vòng lặp kín (closed feedback loop):

> "Basel III Signals (LCR, NSFR, ΔNII, ΔEVE, CAR) → FTP Engine Calibration → Business Unit Behavior Change → Balance Sheet Reshape → Risk Metrics Improve → Re-monitor → Re-calibration" ^ftp-trans-13

Công thức định giá tổng hợp cho tài sản:

> "FTP_Asset(t,T) = BaseRate(t,T) + LiqSpread(T) × LCR_adj × NSFR_adj + CreditSpread(rating) × PD × LGD + OptionCost(prepay) + CapitalCharge(RWA × CoE)" ^ftp-trans-14

## Khái niệm và Liên kết
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản tổng quát.
- [[ftp-transmission-mechanism]]: Chi tiết phân tích các kênh truyền dẫn FTP đến rủi ro thanh khoản, lãi suất, tín dụng và vốn.
- [[ftp-pricing-methodology]]: Phương pháp định giá chi tiết các cấu phần VOF, COF, phụ phí pháp định và quyền chọn ẩn.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa bảng cân đối ngân hàng thông qua hệ thống điều khiển FTP.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn Basel III.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn Basel III.
- [[bcbs-irrbb]]: Rủi ro lãi suất trên sổ ngân hàng theo tiêu chuẩn Basel.
