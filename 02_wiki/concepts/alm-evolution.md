---
title: "Tiến hoá các khái niệm ALM"
aliases: [ALM Evolution, Tiến hoá ALM, Lịch sử ALM, ALM Concepts Evolution, Evolution of ALM]
type: concept
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bardaeva-alm]]"]
relations:
  - {type: input-to, to: "[[strategic-alm]]", cite: "[[src-bardaeva-alm#^ch7-6]]"}
tags: [alm, history, regulation, evolution]
updated: 2026-10-20
reviewed:
---

## Ý chính
Quản trị Tài sản — Nợ (ALM) trong hệ thống ngân hàng thương mại không phải là một mô hình tĩnh tại mà đã trải qua **6 giai đoạn tiến hoá lớn** từ sau Chiến tranh Thế giới thứ hai đến nay, được định hình bởi những biến động kinh tế vĩ mô và sự phát triển của khung giám sát an toàn [[src-bardaeva-alm#^ch7-1]] [[src-bardaeva-alm#^ch7-6]]:
1. **1950–1973**: Can thiệp tối thiểu (*Minimal intervention*) — Bối cảnh Bretton Woods ổn định; ALM thụ động.
2. **1973–1986**: Rủi ro tối thiểu (*Minimum risk*) — Khủng hoảng dầu mỏ và lạm phát; ra đời phân tích khe hở ([[repricing-gap-analysis]]).
3. **1986–1998**: Công cụ ngoại bảng (*Off-balance-sheet instruments*) — Phái sinh lãi suất ([[interest-rate-swap]]), đệm trái phiếu Repo và mô hình [[duration-gap-model]].
4. **1998–2008**: Rào cản bảng cân đối (*Balance sheet restrictions*) — Basel II, [[icaap]], FTP và phân bổ vốn kinh tế.
5. **2009–2020**: Thời kỳ biên sinh lời thấp (*Low margin times*) — Basel III, chuẩn định lượng thanh khoản ([[lcr]], [[nsfr]]) và vốn lai ghép ([[contingent-convertible-bond]]).
6. **2020–2030s**: Vượt qua các điểm nghẽn (*Overcoming bottlenecks*) — Basel IV/Banking Package, liên kết toàn diện đa tham số giữa Vốn, Thanh khoản, [[irrbb-management]] và MREL.

## Sáu kỷ nguyên tiến hoá của ALM

### 1. 1950–1973: Khái niệm can thiệp tối thiểu (Minimal Intervention)
- **Bối cảnh vĩ mô**: Hệ thống tiền tệ Bretton Woods duy trì tỷ giá hối đoái và mặt bằng lãi suất cố định hoặc biến động cực thấp. Hoạt động ngân hàng vận hành chủ yếu theo mô hình truyền thống (huy động tiền gửi ngắn hạn cho vay dài hạn với biên lãi ổn định).
- **Mô hình ALM**: Quản lý tài sản và nguồn vốn diễn ra rời rạc, độc lập. Bộ phận ALM (nếu có) chỉ đảm nhận chức năng kế toán ghi nhận, theo dõi dòng tiền thanh toán ngắn hạn hàng ngày và chuyển nhượng vốn thụ động khi phát sinh thiếu hụt [[src-bardaeva-alm#^ch1-1]] [[src-bardaeva-alm#^ch1-2]]. Không có nhu cầu đo lường hay phòng ngừa rủi ro lãi suất phức tạp.

### 2. 1973–1986: Khái niệm rủi ro tối thiểu (Minimum Risk)
- **Bối cảnh vĩ mô**: Sự sụp đổ của hệ thống Bretton Woods (1971–1973) cùng hai cuộc khủng hoảng năng lượng (1973 và 1979) đẩy lạm phát toàn cầu tăng vọt. Các ngân hàng trung ương (điển hình là Fed dưới thời Paul Volcker) thả nổi lãi suất điều hành, khiến chi phí vốn ngân hàng biến động dữ dội.
- **Mô hình ALM**: Ngân hàng chuyển từ thế bị động sang chủ động kiểm soát rủi ro với mục tiêu giảm thiểu tối đa tổn thất (*minimum risk concept*) [[src-bardaeva-alm#^ch2-1]].
- **Công cụ chủ đạo**: Phân tích khe hở (Gap Analysis):
  - Phân tích sự chênh lệch kỳ hạn định giá lại giữa tài sản sinh lời và nợ chịu lãi ([[repricing-gap-analysis]]).
  - *Nguyên tắc vận hành (Box 2.1)*: Trong khi khe hở thanh khoản (*Liquidity Gap*) luôn được ưu tiên duy trì ở mức dương tại mọi thời điểm để đảm bảo khả năng thanh toán, khe hở lãi suất (*Interest Rate Gap*) lý tưởng nhất nên giữ quanh mức 0 hoặc nằm trong các giới hạn khẩu vị rủi ro (*RAS limits*) đã thiết lập [[src-bardaeva-alm#^ch2-2]].

### 3. 1986–1998: Khái niệm công cụ ngoại bảng (Off-Balance-Sheet Instruments)
- **Bối cảnh vĩ mô**: Làn sóng bãi bỏ quy chế tài chính (*deregulation*), thị trường vốn mở rộng và xuất hiện các sản phẩm tài chính cấu trúc.
- **Mô hình ALM**: Ngân hàng nhận ra việc điều chỉnh cấu trúc bảng cân đối vật lý (bán bớt tài sản, huy động thêm nợ) tốn nhiều chi phí giao dịch và chậm chạp. Sự xuất hiện của các công cụ phái sinh ngoại bảng (IRS, Swaptions, Caps/Floors) cho phép ALM tách rời quyết định quản lý rủi ro lãi suất khỏi bảng cân đối kế toán [[src-bardaeva-alm#^ch3-1]].
- **Công cụ chủ đạo**:
  - Hợp đồng hoán đổi lãi suất ([[interest-rate-swap]]): Hoán đổi dòng tiền cố định sang thả nổi và ngược lại để điều tiết khe hở mà không làm phình to tổng tài sản.
  - Mô hình [[duration-gap-model]]: Đo lường độ nhạy của giá trị kinh tế vốn chủ sở hữu (EVE) trước các cú sốc lãi suất.
  - Quản trị thanh khoản bằng danh mục trái phiếu: Ngân hàng bắt đầu xây dựng danh mục trái phiếu thanh khoản cao chuyên biệt để làm tài sản bảo đảm trong các giao dịch Repo ngắn hạn trên thị trường liên ngân hàng [[src-bardaeva-alm#^ch3-2]].

### 4. 1998–2008: Khái niệm rào cản bảng cân đối (Balance Sheet Restrictions)
- **Bối cảnh vĩ mô**: Ban hành Hiệp ước Vốn Basel II (2004), yêu cầu vốn theo rủi ro (RWA), sự hình thành các tập đoàn tài chính đa quốc gia.
- **Mô hình ALM**: Quản lý bảng cân đối không còn chỉ là cân đối thanh khoản và lãi suất mà phải đối mặt với hàng loạt rào cản quy định về an toàn vốn (*balance sheet restrictions*) [[src-bardaeva-alm#^ch4-1]].
- **Công cụ chủ đạo**:
  - Quy trình Đánh giá Mức đủ Vốn Nội bộ ([[icaap]]) dưới Pillar 2.
  - Cơ chế Định giá Điều chuyển Vốn Nội bộ ([[funds-transfer-pricing]]): Tách bạch lãi suất thị trường, chi phí vốn và phí thanh khoản nhằm điều hướng hành vi kinh doanh của các khối nghiệp vụ.
  - Mô hình Vốn Kinh tế (*Economic Capital*) và RAROC (*Risk-Adjusted Return on Capital*).

### 5. 2009–2020: Khái niệm thời kỳ biên sinh lời thấp (Low Margin Times)
- **Bối cảnh vĩ mô**: Hậu quả của Khủng hoảng Tài chính Toàn cầu 2008 (GFC). Các ngân hàng trung ương áp dụng chính sách nới lỏng định lượng (QE) kéo dài, đưa lãi suất danh nghĩa về mức cận 0 hoặc âm (ZIRP/NIRP). Biên lãi thuần (NIM) của các ngân hàng bị thu hẹp kỷ lục.
- **Mô hình ALM**:
  - Basel III ra đời, lần đầu tiên thiết lập các tỷ lệ an toàn thanh khoản định lượng bắt buộc trên toàn cầu: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn 30 ngày ([[lcr]]) và Tỷ lệ nguồn vốn ổn định ròng dài hạn 1 năm ([[nsfr]]) [[src-bardaeva-alm#^ch5-1]] [[src-bardaeva-alm#^ch7-5]].
  - Tính toán đệm thanh khoản LCR được chuẩn hóa: duy trì HQLA vượt tối thiểu 100% (hoặc mục tiêu 110%) dòng tiền ra ròng chịu stress 30 ngày, áp dụng trần dòng vào tối đa 75% dòng ra [[src-bardaeva-alm#^ch5-2]].
  - Cấu trúc vốn thay đổi: Xuất hiện các công cụ nợ lai ghép có khả năng hấp thụ tổn thất như trái phiếu chuyển đổi dự phòng ([[contingent-convertible-bond]] / AT1) với cơ chế kích hoạt tự động khi CET1 giảm xuống 5,125% theo CRR; các ngân hàng lớn châu Âu đã phát hành hơn 91 tỷ EUR giai đoạn 2013–2016 [[src-bardaeva-alm#^ch5-3]] [[src-bardaeva-alm#^ch5-4]].

### 6. 2020–2030s: Khái niệm vượt qua các điểm nghẽn (Overcoming Bottlenecks)
- **Bối cảnh vĩ mô**: Triển khai gói cải cách ngân hàng hoàn tất (*Banking Package*: Basel IV, CRR II, CRD V, BRRD II), lạm phát hậu đại dịch Covid-19 và chu kỳ tăng lãi suất quyết liệt nhất trong 4 thập kỷ của các ngân hàng trung ương lớn [[src-bardaeva-alm#^ch6-1]].
- **Mô hình ALM**:
  - **Liên kết toàn diện (*Complete Interrelation*)**: Các phân hệ Vốn (CET1, Total Capital, Output Floor), Thanh khoản (LCR, NSFR, phòng ngừa cliff effect), [[irrbb-management]] (kép NII & EVE) và Khả năng xử lý khi đổ vỡ (MREL/TLAC) không thể quản trị độc lập mà ràng buộc lẫn nhau [[src-bardaeva-alm#^ch6-2]].
  - **Tối ưu hoá đa tham số (*Multi-parametric optimization*)**: ALM trở thành cơ quan đầu não điều phối bảng cân đối, phân tích để xác định chính xác "điểm nghẽn" (*bottleneck*) — rào cản thắt chặt nhất đối với từng ngân hàng cụ thể (ví dụ: thiếu vốn CET1 hay thiếu HQLA, vướng trần đòn bẩy hay thiếu trái phiếu đủ chuẩn MREL) — từ đó thiết kế công cụ chuyên biệt để vượt qua điểm nghẽn mà không làm tổn hại đến hiệu quả kinh doanh [[src-bardaeva-alm#^ch6-3]] [[src-bardaeva-alm#^ch6-4]] [[src-bardaeva-alm#^ch7-6]].

## Bảng so sánh tổng hợp 6 giai đoạn tiến hoá ALM

| Giai đoạn | Tên khái niệm | Động lực vĩ mô / Pháp lý chính | Trọng tâm ALM | Công cụ / Kỹ thuật chủ đạo |
|---|---|---|---|---|
| **1950–1973** | Minimal intervention | Bretton Woods, lãi suất ổn định | Thụ động, theo dõi dòng tiền thanh toán ngắn | Sổ sách kế toán, hạn mức thanh toán cơ bản |
| **1973–1986** | Minimum risk | Khủng hoảng dầu mỏ, lạm phát phi mã, thả nổi lãi suất | Khép kín khoảng trống kỳ hạn (closing gaps) | [[repricing-gap-analysis]], đối ứng kỳ hạn tiền gửi — cho vay |
| **1986–1998** | Off-balance-sheet instruments | Deregulation, phái sinh phát triển | Tách rời quản lý rủi ro khỏi cấu trúc bảng cân đối | [[interest-rate-swap]], [[duration-gap-model]], danh mục trái phiếu Repo |
| **1998–2008** | Balance sheet restrictions | Basel II, Pillar 2 ICAAP, toàn cầu hóa | Điều phối bảng cân đối dưới nhiều ràng buộc vốn | [[icaap]], [[funds-transfer-pricing]], Economic Capital, RAROC |
| **2009–2020** | Low margin times | Khủng hoảng 2008, QE, lãi suất âm/0, Basel III | Đáp ứng các chỉ số thanh khoản và vốn định lượng ngặt nghèo | [[lcr]], [[nsfr]], [[contingent-convertible-bond]] (AT1), HQLA buffer |
| **2020–2030s** | Overcoming bottlenecks | Banking Package (Basel IV, CRR II, BRRD II), lạm phát mới | Giải bài toán tối ưu hoá đa biến, xử lý rào cản thắt chặt nhất | Tối ưu hoá đa tham số, RAF 3 vùng đèn tín hiệu, giải tỏa điểm nghẽn Vốn — Thanh khoản — IRRBB — MREL |
