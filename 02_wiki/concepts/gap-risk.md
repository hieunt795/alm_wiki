---
title: "Gap Risk (Rủi ro chênh lệch kỳ hạn)"
aliases: [Gap Risk, Rủi ro tái định giá, Repricing Risk, Yield Curve Risk]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: drives, to: "[[economic-value-of-equity]]", direction: "-", regime: rising_rate, cite: "[[src-bcbs-irrbb-2016#^irrbb-u07-1]]"}
tags: [irrbb, gap-risk, repricing-mismatch, yield-curve, parallel, non-parallel]
updated: 2026-10-19
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
- Dòng tiền được xếp dải theo repricing date, tức ngày của mỗi khoản hoàn trả gốc, tái định giá gốc hoặc thanh toán lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Công cụ lãi suất thả nổi được giả định tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
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

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Chỉ số repricing gap | [cần nguồn] | Chiến lược IRRBB tối thiểu gồm nguyên tắc quản lý theo trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile) [[src-tt83-2025-nhnn#^d53-1a1]] | TT83 Đ53.1.a(i) | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Báo cáo nội bộ | [cần nguồn] | Tối thiểu hằng quý, gồm trạng thái chênh lệch kỳ định lại lãi suất [[src-tt83-2025-nhnn#^d55-1]] | TT83 Đ55 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |

Khác biệt: [[tt83-2025]] đặt repricing gap profile thành chỉ số bắt buộc trong chiến lược IRRBB.

## Đề xuất cập nhật
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đề xuất bổ sung vào câu phân bổ dải kỳ hạn (dòng 46) rằng dòng tiền được xếp theo repricing date, tức ngày hoàn trả gốc, tái định giá gốc hoặc thanh toán lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]]; công cụ thả nổi tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7 — user duyệt [2026-10-19]: thêm dòng VN. TT83/2025 yêu cầu chiến lược IRRBB tối thiểu gồm nguyên tắc quản lý theo trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile) [[src-tt83-2025-nhnn#^d53-1a1]]; báo cáo nội bộ tối thiểu hằng quý gồm trạng thái này [[src-tt83-2025-nhnn#^d55-1]]; link [[tt83-2025]]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: thêm dòng `## Basel vs VN` "Định nghĩa": VN — rủi ro chênh lệch phát sinh từ sự không khớp thời điểm định giá lại lãi suất hoặc kỳ hạn giữa tài sản và nợ phải trả (kể cả ngoại bảng) trên sổ ngân hàng [[src-tt83-2025-nhnn#^d3-22]]; tương đương d368 [[src-bcbs-irrbb-2016#^irrbb-u02-2]].
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm nguồn T4 thứ hai: gap risk đo bằng repricing gap và chênh lệch ròng theo dải và đồng tiền trọng yếu, phụ thuộc dịch chuyển song song hay không [[src-lubinska-alm-optimisation#^lubinska-u02-30]]; dấu GAP và rủi ro tái đầu tư/tái cấp vốn [[src-lubinska-alm-optimisation#^lubinska-u02-26]]. Link [[repricing-gap-analysis]].
- [2026-10-19] ingest src-choudhry-principles-banking u25 — chờ user duyệt: thêm cách phân loại năm nguồn IRRBB của Choudhry (gap, yield curve, basis, run-off, option; gap risk nhiều khi là lỗ cơ hội khi lãi suất cố định) [[src-choudhry-principles-banking#^choudhry-cs-12]]; IRRBB là sản phẩm phụ do khách hàng tạo ra, kèm sáu nguyên nhân [[src-choudhry-principles-banking#^choudhry-cs-13]]. Link [[structural-hedging]].
- [2026-10-19] ingest src-choudhry-principles-banking u10 — chờ user duyệt: thêm funding short/funding long: đường cong dương thì huy động ngắn, cho vay dài, 'tail' là interest-rate gap, lãi suất ngắn tăng làm thu hẹp biên [[src-choudhry-principles-banking#^choudhry-hedge-1]]; đường cong đảo ngược thì funding long [[src-choudhry-principles-banking#^choudhry-hedge-2]]. Công cụ phòng ngừa gap: đã có node [[forward-rate-agreement]] [[src-choudhry-principles-banking#^choudhry-hedge-8]] và [[interest-rate-futures]] [[src-choudhry-principles-banking#^choudhry-hedge-4]]. Gap risk trong [[securitisation]] phải được phòng ngừa [[src-choudhry-principles-banking#^choudhry-sec-4]].
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: thêm cách phân loại của Choudhry: IRR = investment (price) risk + income risk; income risk do lãi suất huy động và funding thay đổi không đồng bộ, chính là gap risk [[src-choudhry-principles-banking#^choudhry-irr-2]]; gap risk còn gọi là mismatch risk, nhạy với dịch chuyển song song hoặc pivotal; yield curve risk tách riêng [[src-choudhry-principles-banking#^choudhry-irr-4]]. Underfunded gap ngụ ý kỳ vọng lãi suất giảm, over-funded gap ngụ ý kỳ vọng lãi suất tăng [[src-choudhry-principles-banking#^choudhry-lgap-9]].
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM.
- [2026-10-19] ingest src-bardaeva-alm u03 — chờ user duyệt: thêm cách phân loại của Bardaeva: gap risk, basis risk và yield curve risk là chung cho mọi ngân hàng, optionality risk có thể nhỏ hoặc đặc thù [[src-bardaeva-alm#^ch11-15]]; Risk lập báo cáo gap analysis cho ALM [[src-bardaeva-alm#^ch11-22]]. Link [[irrbb-management]] ở lần nhắc quy trình quản trị.
