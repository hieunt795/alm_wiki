---
title: "Gap Risk (Rủi ro chênh lệch kỳ hạn)"
aliases: [Gap Risk, Rủi ro tái định giá, Repricing Risk, Yield Curve Risk]
type: concept
domains: [alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: drives, to: "[[economic-value-of-equity]]", direction: "-", regime: rising_rate, cite: "[[src-bcbs-irrbb-2016#^irrbb-u07-1]]"}
tags: [irrbb, gap-risk, repricing-mismatch, yield-curve, parallel, non-parallel]
updated: 2026-10-16
reviewed:
---

## Định nghĩa
Rủi ro chênh lệch kỳ hạn (Gap risk, hay rủi ro tái định giá - Repricing risk) phát sinh từ cấu trúc kỳ hạn của các công cụ trên sổ ngân hàng, miêu tả rủi ro xuất hiện do sự lệch pha về mặt thời điểm giữa các lần thay đổi lãi suất của tài sản sinh lời và các khoản nợ phải trả [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

Khi các tài sản và khoản nợ tái định giá tại các thời điểm khác nhau, ngân hàng đối mặt với rủi ro:
- Lãi suất phải trả trên nợ tài trợ tăng lên trước khi lãi suất thu được từ tài sản kịp điều chỉnh tăng (ép biên thu nhập lãi thuần $\Delta\text{NII}$ co hẹp hoặc âm) [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- Lãi suất thu được từ tài sản giảm trước khi lãi suất trả cho các khoản nợ giảm theo [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- Giá trị hiện tại thuần của các tài sản có thời lượng dài sụt giảm mạnh hơn nhiều so với mức tăng giá trị của các khoản nợ ngắn hạn khi lãi suất thị trường tăng, dẫn tới suy giảm nghiêm trọng giá trị kinh tế của vốn chủ sở hữu [[economic-value-of-equity|$\Delta\text{EVE}$]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

## Hai hình thái chính của Gap Risk

Theo Ủy ban Basel d368, mức độ nghiêm trọng của Gap risk phụ thuộc vào hình thái biến động của đường cong lợi suất [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]]:

### 1. Rủi ro dịch chuyển song song (Parallel Risk)
- Xảy ra khi toàn bộ đường cong lợi suất dịch chuyển lên hoặc xuống cùng một biên độ tại tất cả các kỳ hạn tái định giá [[src-bcbs-irrbb-2016#^irrbb-u07-1]].
- Dạng rủi ro này tác động trực tiếp đến khoảng cách tái định giá gộp (cumulative repricing gap) và thời lượng hiệu chỉnh (modified duration) tổng thể của ngân hàng.
- Thường được đo lường qua kỹ thuật $PV01$ (giá trị hiện tại của một điểm cơ bản lãi suất) hoặc thời lượng dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u06-7]].

### 2. Rủi ro phi song song / Xoay trục đường cong (Non-parallel Risk / Rotation Risk)
- Xảy ra khi mức thay đổi lãi suất phân hoá giữa các kỳ hạn khác nhau dọc theo đường cong lợi suất (thường gọi là *Yield Curve Risk* hay *Twist Risk*) [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- Basel d368 chuẩn hoá 2 dạng xoay trục chính [[src-bcbs-irrbb-2016#^irrbb-u07-1]] [[src-bcbs-irrbb-2016#^irrbb-u07-3]]:
  - **Kịch bản dốc lên (Steepener shock)**: Lãi suất ngắn hạn giảm và lãi suất dài hạn tăng. Khiến đường cong dốc hơn, tác động bất lợi đến các ngân hàng có vị thế tài sản ngắn hạn tài trợ cho nợ dài hạn hoặc các danh mục phái sinh nhận cố định dài hạn.
  - **Kịch bản phẳng đi (Flattener shock)**: Lãi suất ngắn hạn tăng và lãi suất dài hạn giảm. Đây là kịch bản "chết người" đối với mô hình kinh doanh truyền thống của các NHTM (huy động ngắn hạn tài trợ cho vay dài hạn): chi phí huy động vốn ngắn hạn tăng vọt trong khi lợi suất đầu tư dài hạn bị nén lại.
  - **Kịch bản sốc lãi suất ngắn hạn (Short rate shock up/down)**: Chỉ tác động lên đoạn đầu của đường cong lợi suất với mức độ suy giảm dần theo hàm mũ $e^{-t_k / 4}$ về phía các kỳ hạn dài [[src-bcbs-irrbb-2016#^irrbb-u07-3]].

## Phương pháp luận Đo lường Gap Risk

### 1. Phân tích khoảng cách tái định giá (Repricing Gap Analysis)
- Phân bổ toàn bộ tài sản, nợ và ngoại bảng nhạy cảm lãi suất vào $K$ dải kỳ hạn chuẩn hoá ($K=19$ dải theo Khuôn khổ chuẩn hoá Basel, từ qua đêm đến trên 20 năm) dựa trên ngày tái định giá tiếp theo [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
- Tại mỗi dải kỳ hạn $k$, xác định khoảng cách chênh lệch:
  $$\text{Gap}_k = \text{Assets}_k - \text{Liabilities}_k$$
- **Trạng thái nhạy cảm tài sản (Asset-sensitive) và nhạy cảm nợ (Liability-sensitive) theo Moorad Choudhry**:
  - Khi $\text{Gap}_k > 0$ (tài sản nhiều hơn nợ): ngân hàng ở trạng thái *asset sensitive*, hưởng lợi khi lãi suất tăng do tài sản tái định giá lên nhanh hơn nợ [[src-choudhry-principles-banking#^choudhry-irrbb-5]].
  - Khi $\text{Gap}_k < 0$ (nợ nhiều hơn tài sản): ngân hàng ở trạng thái *liability sensitive*, hưởng lợi khi lãi suất giảm nhưng chịu tổn thất khi lãi suất tăng do nợ tái định giá tăng nhanh hơn tài sản [[src-choudhry-principles-banking#^choudhry-irrbb-5]].
  - Do cấu trúc chuyển đổi kỳ hạn truyền thống (huy động ngắn hạn tài trợ cho vay dài hạn), đa số các ngân hàng thương mại rơi vào trạng thái *liability sensitive* ở các dải kỳ hạn ngắn dưới 1 năm, khiến NIM và NII chịu sức ép nặng nề khi lãi suất điều hành tăng [[src-choudhry-principles-banking#^choudhry-irrbb-1]] [[src-choudhry-principles-banking#^choudhry-irrbb-5]].
- **Hạn chế**: Giả định mọi dòng tiền trong cùng một dải kỳ hạn tái định giá đồng thời tại điểm giữa (bỏ qua intra-bucket mismatch) và không đo lường được rủi ro cơ sở bên trong dải kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u06-7]].

### 2. Độ nhạy giá trị kinh tế (Duration Profile / EVE)
- Phân tích độ nhạy thông qua [[duration-gap-model|Mô hình chênh lệch thời lượng (Duration Gap Model)]] và [[key-rate-duration|Thời lượng lãi suất từng kỳ hạn (Key Rate Duration - KRD)]]. Mỗi khoản chênh lệch $\text{Gap}_k$ được nhân với thời lượng và hệ số chiết khấu sau sốc:
  $$\Delta\text{EVE} \approx \sum_{k=1}^{19} \text{Gap}_k \times \text{Duration}_k \times \Delta R(t_k)$$
- Cho phép nhận diện chính xác các tổn thương về vốn tự có trước các cú sốc đường cong lợi suất phức tạp [[src-bcbs-irrbb-2016#^irrbb-u05-8]]. Để tái cân bằng khoảng cách thời lượng, Treasury sử dụng các công cụ phái sinh như [[interest-rate-swap|Hợp đồng hoán đổi lãi suất (IRS)]].

## Mối liên hệ với Thanh khoản và NSFR
- **Bản chất của hoạt động trung gian ngân hàng**: Ngân hàng thực hiện chức năng chuyển đổi kỳ hạn (maturity transformation) — thu hút tiền gửi ngắn hạn để cung cấp tín dụng dài hạn cho nền kinh tế. Chức năng này tạo ra chênh lệch kỳ hạn cơ cấu vốn, vốn là tâm điểm kiểm soát của chỉ số [[nsfr]] (yêu cầu nguồn vốn ổn định sẵn có ASF $\ge$ nguồn vốn ổn định cần thiết RSF).
- **Sự đánh đổi kép**: Một ngân hàng nỗ lực cải thiện NSFR bằng cách kéo dài kỳ hạn nợ phải trả (tăng nợ kỳ hạn $\ge 1$ năm với ASF 100%) sẽ làm giảm Gap risk âm. Ngược lại, nếu ngân hàng tài trợ các khoản vay thế chấp nhà ở kỳ hạn 20–30 năm bằng tiền gửi không kỳ hạn hoặc ngắn hạn, ngân hàng không chỉ chịu áp lực về tỷ lệ RSF cao (RSF 65%–85%) mà còn tạo ra một mức Gap risk khổng lồ, khiến $\Delta\text{EVE}$ dễ dàng vượt ngưỡng cảnh báo [[outlier-bank-test|15% Tier 1 Capital]] khi lãi suất tăng.
- Xem chi tiết tại [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[duration-gap-model]], [[key-rate-duration]], [[interest-rate-swap]], [[integrated-alm-liquidity-strategy]].
