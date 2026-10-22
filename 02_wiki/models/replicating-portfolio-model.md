---
title: "Replicating Portfolio Model (Mô hình danh mục tái lập)"
aliases: [Replicating Portfolio Model, Mô hình danh mục tái lập, NMD Replication Model, Moving Average Portfolio, Mô hình tái lập tiền gửi không kỳ hạn]
type: model
domains: [alm, basel]
status: active
maturity: draft
sources: ["[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: measures, to: "[[non-maturity-deposits]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-6]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-6]]"}
  - {type: drives, to: "[[economic-value-of-equity]]", direction: "-", regime: rising_rate, cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-6]]"}
  - {type: hedges, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-6]]"}
tags: [irrbb, model, replicating-portfolio, nmd, moving-average, cointegration, margin-stability]
updated: 2026-10-20
reviewed:
---

## Khái niệm và Mục tiêu
Mô hình Danh mục Tái lập (Replicating Portfolio Model) là kỹ thuật kinh tế lượng và tối ưu hóa tài chính được các ngân hàng thương mại quốc tế sử dụng rộng rãi nhằm gán kỳ hạn hành vi (behavioural maturity) và cấu trúc lãi suất cho các nguồn vốn không có kỳ hạn theo hợp đồng — chủ yếu là **Tiền gửi không kỳ hạn ([[non-maturity-deposits|NMDs]])** và **Vốn chủ sở hữu (Equity Capital)** [[src-bcbs-irrbb-2016#^irrbb-u06-6]].

Do khách hàng có quyền rút NMDs bất kỳ lúc nào nhưng trên thực tế số dư tiền gửi lõi (core deposits) lại có tính bám dính cao và chi phí trả lãi rất thấp, việc coi NMDs là vốn qua đêm sẽ làm sai lệch bản chất kinh tế. Mô hình Danh mục Tái lập xây dựng một danh mục tài sản đầu tư cố định giả định (hoặc danh mục các hợp đồng hoán đổi lãi suất [[interest-rate-swap|Receiver IRS]]) có cấu trúc dòng tiền và lợi suất mô phỏng hoàn hảo hành vi sinh lời và chi phí của NMDs [[src-bcbs-irrbb-2016#^irrbb-u06-6]].

## Cấu trúc Phương pháp Luận

### 1. Phân tách Quy mô: Lõi (Core) vs Phi lõi (Non-core)
Theo Nguyên tắc 5 và Annex 1 Basel d368, ngân hàng trước hết phải phân rã tổng số dư NMDs thành hai phần [[src-bcbs-irrbb-2016#^irrbb-p05-2]] [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:
- **Phần phi lõi (Non-core deposits / Volatile tranche)**: Phần số dư biến động thường xuyên do nhu cầu thanh toán ngắn hạn hoặc mùa vụ. Phần này bắt buộc phải được mô hình hoá với kỳ hạn qua đêm (overnight / time bucket 1) [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
- **Phần lõi (Core deposits / Stable tranche)**: Phần số dư ổn định duy trì dài hạn ngay cả khi lãi suất thị trường biến động mạnh. Chỉ phần này mới được phép đưa vào danh mục tái lập dài hạn [[src-bcbs-irrbb-2016#^irrbb-u05-4]].

### 2. Kỹ thuật Lát cắt Bình quân Trượt (Moving Average Tranches)
Phương pháp phổ biến nhất trong thực tế quản trị ALM là chia số dư tiền gửi lõi thành $M$ lát cắt bằng nhau (tranches), mỗi lát cắt được tái đầu tư định kỳ vào các công cụ có kỳ hạn cố định $T$ năm [[src-bcbs-irrbb-2016#^irrbb-u06-6]]:
- **Ví dụ chuẩn của Basel (Footnote 38)**: Một danh mục tái lập NMDs kỳ hạn 5 năm được chia thành 60 lát cắt (tái đầu tư $1/60$ tổng số dư vào kỳ hạn 5 năm mỗi tháng). Cấu trúc này sẽ tạo ra:
  - Thời lượng bình quân gia quyền (Weighted Average Maturity - WAM): $\approx 2.5$ năm [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
  - Lợi suất danh mục mang lại: Đường trung bình động 60 tháng (60-month moving average) của lãi suất thị trường kỳ hạn 5 năm.

### 3. Mô hình Kinh tế lượng Tối ưu hóa (Econometric Optimization)
Thay vì chia tỷ lệ cơ học, các ngân hàng tiên tiến sử dụng bài toán tối ưu hóa danh mục:
- **Ước lượng Hệ số Truyền dẫn Lãi suất (Deposit Beta $\beta$)**:
  $$\Delta r_{\text{dep}, t} = \alpha + \beta \cdot \Delta R_{\text{market}, t} + \epsilon_t$$
  Với $0 \le \beta < 1$. $\beta$ đo lường mức độ ngân hàng phải tăng lãi suất tiền gửi khi lãi suất thị trường tăng.
- **Mô hình Đồng tích hợp (Cointegration & Error Correction Model - ECM)**: Xác định mối quan hệ cân bằng dài hạn giữa lãi suất tiền gửi và đường cong lợi suất TPCP.
- **Hàm Mục tiêu Tối ưu hóa**:
  Tìm vector tỷ trọng đầu tư $\vec{w} = [w_1, w_2, \dots, w_K]^T$ trên các kỳ hạn $1, 2, \dots, K$ năm nhằm **tối đa hóa tính ổn định của Biên lãi ròng (NIM)** hoặc **tối đa hóa Sharpe Ratio của biên thu nhập NII**:
  $$\min_{\vec{w}} \text{Var}\left( \sum_{k=1}^K w_k R_k(t) - r_{\text{dep}}(t) \right)$$
  Thỏa mãn các ràng buộc:
  $$\sum_{k=1}^K w_k = 1, \quad w_k \ge 0, \quad \sum_{k=1}^K w_k \cdot k \le \text{Maturity Cap}$$

## Ràng buộc của Khuôn khổ Chuẩn hoá Basel d368

Để ngăn chặn các ngân hàng kéo dài kỳ hạn danh mục tái lập một cách thái quá nhằm thổi phồng thu nhập kỳ vọng, Basel d368 (Table 2) áp đặt các mức trần nghiêm ngặt đối với tỷ lệ tiền gửi lõi và kỳ hạn bình quân tối đa [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:

| Phân khúc Khách hàng | Loại Tài khoản | Trần Tiền gửi Lõi (Core Cap) | Trần Kỳ hạn Bình quân (Average Maturity Cap) | Nguồn |
|---|---|---|---|---|
| **Bán lẻ (Retail)** | Tài khoản giao dịch (Transactional accounts) | **90%** | **5.0 năm** | [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| **Bán lẻ (Retail)** | Tài khoản phi giao dịch (Non-transactional) | **70%** | **4.5 năm** | [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| **Bán buôn (Wholesale)** | Tất cả các khoản tiền gửi doanh nghiệp | **50%** | **4.0 năm** | [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |

## Sự Đánh đổi Chiến lược: Ổn định Thu nhập ($\Delta\text{NII}$) vs Rủi ro Vốn ($\Delta\text{EVE}$)

Mô hình Danh mục Tái lập là hiện thân rõ nét nhất của mâu thuẫn quản trị kinh điển trong ALM [[src-bcbs-irrbb-2016#^irrbb-u02-4]] [[src-bcbs-irrbb-2016#^irrbb-u06-6]]:
- **Nếu kéo dài kỳ hạn tái lập (ví dụ WAM = 4–5 năm)**:
  - *Lợi ích*: Thu nhập lãi từ tài sản mô phỏng cực kỳ ổn định, bảo vệ vững chắc biên thu nhập lãi thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]] không bị suy sụp khi lãi suất thị trường giảm [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
  - *Rủi ro*: Danh mục tài sản cố định dài hạn này mang thời lượng lớn. Khi lãi suất thị trường tăng sốc, giá trị thị trường của danh mục sụt giảm mạnh, dẫn tới sự suy giảm nghiêm trọng của Giá trị kinh tế của vốn [[economic-value-of-equity|$\Delta\text{EVE}$]], dễ khiến ngân hàng vi phạm ngưỡng cảnh báo [[outlier-bank-test|15% Vốn cấp 1]] [[src-bcbs-irrbb-2016#^irrbb-u06-6]] [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
- **Nếu rút ngắn kỳ hạn tái lập (ví dụ WAM = 3–6 tháng)**:
  - *Lợi ích*: Giảm thiểu rủi ro $\Delta\text{EVE}$ về mức gần như bằng 0.
  - *Rủi ro*: Thu nhập của ngân hàng trôi nổi hoàn toàn theo chu kỳ lãi suất ngắn hạn, biên lợi nhuận bị xói mòn nghiêm trọng khi lãi suất rơi vào chu kỳ giảm.
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM.

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
