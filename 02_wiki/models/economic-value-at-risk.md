---
title: "Economic Value at Risk (EVaR — Giá trị kinh tế chịu rủi ro)"
aliases: [EVaR, Banking Book VaR, EaR vs EVaR, Value at Risk sổ ngân hàng, Rủi ro giá trị kinh tế phân phối xác suất]
type: model
domains: [alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: measures, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-7]]"}
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-7]]"}
tags: [irrbb, model, evar, ear, value-at-risk, monte-carlo, historical-simulation, tail-risk]
updated: 2026-10-18
reviewed:
---

## Khái niệm và Định nghĩa
Giá trị kinh tế chịu rủi ro (Economic Value at Risk - EVaR) là mô hình đo lường rủi ro thống kê - xác suất, xác định mức suy giảm giá trị kinh tế tối đa kỳ vọng của toàn bộ sổ ngân hàng (hoặc của Vốn chủ sở hữu [[economic-value-of-equity|$\Delta\text{EVE}$]]) trong một khoảng thời gian nắm giữ xác định (holding period, ví dụ 10 ngày, 1 tháng hoặc 1 năm) dưới điều kiện thị trường bình thường tại một mức độ tin cậy định trước (confidence level, ví dụ 95%, 99% hoặc 99.9%) [[src-bcbs-irrbb-2016#^irrbb-u06-7]].

Bên cạnh EVaR (tập trung vào giá trị vốn dài hạn), các ngân hàng thường vận hành song song thước đo **Earnings at Risk (EaR)** để lượng hóa mức sụt giảm tối đa của Thu nhập lãi thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]] trong chu kỳ 12 tháng kế tiếp ở cùng mức độ tin cậy [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

## Ba Phương pháp Luận Tính toán EVaR

Theo hướng dẫn của Ủy ban Basel d368 (Annex 1, par 4.2), EVaR cho sổ ngân hàng được định lượng qua 3 phương pháp chính [[src-bcbs-irrbb-2016#^irrbb-u06-7]]:

### 1. Phương pháp Tham số / Ma trận Phương sai - Hiệp phương sai (Delta-Normal VaR)
- **Cơ chế**: Dựa trên xấp xỉ tuyến tính thông qua vector độ nhạy thời lượng hoặc PV01 của các dải kỳ hạn ([[key-rate-duration|KRD]]) kết hợp với ma trận hiệp phương sai biến động lãi suất $\mathbf{\Sigma}$:
  $$\Delta E \approx -\mathbf{S}^T \Delta\mathbf{y}$$
  Trong đó $\mathbf{S}$ là vector PV01 ròng của 19 dải kỳ hạn, $\Delta\mathbf{y} \sim \mathcal{N}(0, \mathbf{\Sigma})$ là vector biến động lãi suất đa biến.
- **Công thức EVaR**:
  $$\text{EVaR}_{\alpha} = Z_{\alpha} \cdot \sqrt{\mathbf{S}^T \mathbf{\Sigma} \mathbf{S}}$$
  Trong đó $Z_{\alpha}$ là giá trị phân vị chuẩn (ví dụ $Z_{0.99} = 2.33$).
- **Ưu/Nhược điểm**: Tính toán nhanh, trực quan, nhưng **thất bại hoàn toàn trước các công cụ có tính phi tuyến tính mạnh** (quyền chọn Caps, Floors, Swaptions hoặc rủi ro trả nợ trước hạn) và giả định phân phối chuẩn làm đánh giá thấp rủi ro đuôi béo (fat tails) [[src-bcbs-irrbb-2016#^irrbb-u06-7]].

### 2. Mô phỏng Lịch sử (Historical Simulation VaR)
- **Cơ chế**: Sử dụng chuỗi biến động thực tế của đường cong lợi suất trong quá khứ (ví dụ 500 đến 1.000 ngày giao dịch gần nhất). Áp dụng từng vector biến động lịch sử vào đường cong lợi suất hiện tại để tái định giá toàn bộ bảng cân đối kế toán:
  $$\Delta E_k = E(\mathbf{y}_0 + \Delta\mathbf{y}_k^{\text{hist}}) - E(\mathbf{y}_0)$$
  Sắp xếp các giá trị $\Delta E_k$ theo thứ tự từ lỗ nặng nhất đến lãi nhiều nhất; $\text{EVaR}_{\alpha}$ là giá trị phân vị tại ngưỡng $(1-\alpha)\%$.
- **Ưu/Nhược điểm**: Không cần giả định phân phối chuẩn, ghi nhận được các tương quan phi tuyến thực tế, nhưng mang tính nhìn về quá khứ (backward-looking), hoàn toàn có thể bỏ lỡ các sự kiện thiên nga đen chưa từng xuất hiện trong giai đoạn mẫu [[src-bcbs-irrbb-2016#^irrbb-u06-7]].

### 3. Mô phỏng Monte Carlo (Monte Carlo Simulation)
- **Cơ chế**: Sử dụng các mô hình cấu trúc kỳ hạn lãi suất ngẫu nhiên (Stochastic Term Structure Models như Hull-White, Black-Karasinski, Libor Market Model / LMM) để sinh ra hàng chục nghìn kịch bản đường cong lợi suất tương lai. Tái định giá toàn phần (full revaluation) từng tài sản, khoản nợ và phái sinh trên bảng cân đối dưới mỗi kịch bản [[src-bcbs-irrbb-2016#^irrbb-u06-7]].
- **Ưu/Nhược điểm**: Phương pháp hoàn thiện và chính xác nhất, xử lý hoàn hảo các quyền chọn phức tạp (path-dependent options) và các hành vi khách hàng động, nhưng đòi hỏi năng lực tính toán và công nghệ cực kỳ lớn [[src-bcbs-irrbb-2016#^irrbb-u06-7]].

## Hạn chế Cốt tử của EVaR và Sự Cần thiết của Stress Testing

Ủy ban Basel nhấn mạnh rằng **EVaR không thể được sử dụng làm căn cứ duy nhất để xác định an toàn vốn cho IRRBB** vì 3 lý do kỹ thuật cốt yếu [[src-bcbs-irrbb-2016#^irrbb-u06-7]]:
1. **Thiết kế cho Điều kiện Thị trường Bình thường**: EVaR được xây dựng trên giả định thị trường vận hành bình thường, do đó **không đánh giá đầy đủ rủi ro đuôi (tail risk)** và các cú sốc thanh khoản cực đoan [[src-bcbs-irrbb-2016#^irrbb-u06-7]].
2. **Hiện tượng Vỡ gãy Tương quan (Correlation Breakdown)**: Trong khủng hoảng, các tương quan lịch sử giữa các kỳ hạn hoặc giữa các chỉ số tham chiếu (basis) thường bị đổ vỡ, khiến các giả định phân tán rủi ro của VaR trở nên vô hiệu.
3. **Tính phi thanh khoản của Sổ Ngân hàng**: Khác với sổ kinh doanh (Trading Book) có thể thanh lý vị thế trong vài ngày, các tài sản và nợ trên sổ ngân hàng mang tính dài hạn và phi thanh khoản. Việc sử dụng chân trời 10 ngày của VaR thông thường là không thực tế với chu kỳ quản trị của ALM [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

Basel d368 quy định ngân hàng nên (should) áp dụng 6 kịch bản sốc lãi suất chuẩn hoá cho EVE [[src-bcbs-irrbb-2016#^irrbb-u07-1]], và cơ quan giám sát nên áp dụng ít nhất một phép thử ngoại lai so sánh $\Delta\text{EVE}$ cực đại dưới 6 kịch bản đó với 15% Tier 1 capital [[src-bcbs-irrbb-2016#^irrbb-p12-1]]. *Diễn giải:* (ngoài wiki, chưa có nguồn) các kịch bản quy định sẵn bổ sung cho những hạn chế của EVaR nêu trên; nguồn đã ingest không nói d368 thay thế mô hình EVaR nội bộ.

## Đề xuất cập nhật

- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 52 "… làm chuẩn mực quy định bắt buộc thay vì dựa vào các mô hình EVaR nội bộ": 6 kịch bản là "Banks should apply" ([[src-bcbs-irrbb-2016#^irrbb-u07-1]]), phép thử ngoại lai là "should implement" ([[src-bcbs-irrbb-2016#^irrbb-p12-1]]); vế "thay vì EVaR nội bộ" không có trong claim được cite (par 69 còn ghi ngân hàng dùng IMS của mình để tính số công bố, [[src-bcbs-irrbb-2016#^irrbb-p08-1]] chỉ trích một phần). Đề xuất viết lại theo should và chuyển vế so sánh với EVaR sang `*Diễn giải:*`. → đã áp [2026-10-18]
