---
title: "Thông tư 50/2026/TT-NHNN — Các giới hạn, tỷ lệ bảo đảm an toàn trong hoạt động của NHTM, CN NHNNg"
aliases: []
type: source
source_id: src-tt50-2026-nhnn
domains: [vn-reg, alm, basel]
status: active
maturity: draft
tier: T1
doc_status: final
issuer: SBV
published: 2026-09-30
effective: 2026-10-01
raw: 01_sources/alm/TT50_2026_SBV/TT50_2026_SBV.md
units_done: [C1, C2-M2, C2-M4, C2-M5, PL1, PL2, PL4]
updated: 2026-10-20
---

## Thông tin nguồn
- Issuer: Ngân hàng Nhà nước Việt Nam (NHNN); số 50/2026/TT-NHNN.
- Tier T1, `doc_status: final`.
- Hiệu lực: 01/10/2026, trừ trường hợp tại Đ37.2 (Đ37.1). TT50 thay thế TT22/2019 đối với NHTM và chi nhánh NHNNg: Đ37.3.a thu hẹp đối tượng của TT22 còn ngân hàng hợp tác xã và NHTM đang thực hiện Đ23.3 TT41/2016. Văn bản dùng kỹ thuật sửa đổi, không có điều khoản bãi bỏ TT22.
- Raw: `01_sources/alm/TT50_2026_SBV/TT50_2026_SBV.md` (2.310 dòng); bản gốc pdf và docx cùng thư mục.
- Conversion: ok (xem `03_meta/sources.yaml`).
- Node regulation tương ứng: [[tt50-2026]].
- Đã ingest: C2-M2 (Đ8), C2-M4 (Đ12), C2-M5 (Đ13–Đ27), PL1 (HQLA, dòng tiền ra, dòng tiền vào), PL2 (bảng ASF, RSF). Đ37.1–37.2 (unit C3) được đọc để lấy hiệu lực; C3 chưa ingest trọn.

## Tóm tắt
- Mục 5 Chương II (Đ13–Đ27) đưa tỷ lệ khả năng chi trả (LCR) và tỷ lệ nguồn vốn ổn định ròng (NSFR) vào khung NHNN, với công thức, HQLA, dòng tiền ra ròng, ASF/RSF theo cấu trúc Basel III.
- Từ 01/10/2028 ngân hàng phải áp dụng cả LCR và NSFR theo lộ trình: LCR quy VNĐ riêng lẻ 50% năm thứ nhất, tăng 10 điểm mỗi năm tới 100% từ 01/10/2033; NSFR 90%, 95%, 100% từ 01/10/2030. Ngân hàng được đăng ký áp dụng sớm.
- TT50 thay thế TT22/2019 đối với NHTM và chi nhánh NHNNg. Trong giai đoạn chuyển tiếp trước khi áp dụng LCR/NSFR, Đ13.4 TT50 dẫn chiếu các tỷ lệ tính theo TT22 (dự trữ thanh khoản, khả năng chi trả 30 ngày, nguồn ngắn hạn cho vay trung dài hạn, LDR).
- Đ14 bổ sung yêu cầu quản lý rủi ro thanh khoản ngoài TT83/2025: thanh khoản trong ngày, quản lý tài sản bảo đảm, quản lý HQLA, kiểm tra sức chịu đựng với dữ liệu tối thiểu 10 năm và báo cáo NHNN trong 30 ngày sau quý.
- PL1 (HQLA, hệ số rút tiền, thu tiền) và PL2 (hệ số ASF/RSF) đã ingest.

## Key claims

### C1 — Quy định chung

- TT50 quy định các giới hạn, tỷ lệ bảo đảm an toàn mà NHTM và chi nhánh NHNNg phải thường xuyên duy trì: hạn chế, giới hạn cấp tín dụng; LCR; NSFR; tỷ lệ mua, nắm giữ TPCP; giới hạn góp vốn, mua cổ phần; LDR; LEV.
  > "Thông tư này quy định về các giới hạn, tỷ lệ bảo đảm an toàn trong hoạt động mà các ngân hàng thương mại, chi nhánh ngân hàng nước ngoài (sau đây gọi là ngân hàng) phải thường xuyên duy trì, bao gồm:"
  > "Tỷ lệ khả năng chi trả (sau đây gọi là tỷ lệ LCR);"
  > "Tỷ lệ nguồn vốn ổn định ròng (sau đây gọi là tỷ lệ NSFR);"
  > "Tỷ lệ dư nợ cho vay so với tổng tiền gửi (sau đây gọi là tỷ lệ LDR);"
  > "Tỷ lệ đòn bẩy (sau đây gọi là tỷ lệ LEV)."
  > — Đ1.1 ^d1-1

- Trong thời gian kiểm soát đặc biệt, ngân hàng không phải tuân thủ Điều 136, 137, 138 và khoản 3 Điều 144 Luật Các TCTD và các quy định liên quan tại TT50.
  > "Trong thời gian kiểm soát đặc biệt, ngân hàng không phải tuân thủ quy định tại các Điều 136, 137, 138 và khoản 3 Điều 144 Luật Các tổ chức tín dụng số 32/2024/QH15"
  > — Đ1.2 ^d1-2

- Căn cứ thanh tra, giám sát, NHNN có quyền yêu cầu ngân hàng áp hệ số thanh khoản, hệ số thu tiền, rút tiền, ASF, RSF chặt chẽ hơn TT50 cho từng phần số dư hoặc cấu phần khi tính LCR, NSFR, hoặc áp giới hạn, tỷ lệ chặt chẽ hơn.
  > "Ngân hàng thực hiện áp dụng hệ số thanh khoản, hệ số thu tiền, hệ số rút tiền, hệ số nguồn vốn ổn định sẵn có (sau đây gọi là hệ số ASF), hệ số nguồn vốn ổn định yêu cầu (sau đây gọi là hệ số RSF) chặt chẽ hơn so với quy định tại Thông tư này đối với từng phần số dư hoặc từng cấu phần cụ thể khi tính tỷ lệ LCR và tỷ lệ NSFR;"
  > "Ngân hàng thực hiện một hoặc một số giới hạn, tỷ lệ bảo đảm an toàn chặt chẽ hơn so với các mức quy định tại Thông tư này;"
  > — Đ1.5.a, 1.5.c ^d1-5

- Ba mức huỷ ngang: không thể huỷ ngang (không huỷ, đổi được sau khi ký; hoặc khách hàng trả phí và huỷ ngang dẫn đến ngân hàng phải bồi thường); huỷ ngang có điều kiện (khả năng trả nợ suy giảm, vi phạm thoả thuận, hoặc thực hiện nghĩa vụ làm ngân hàng vi phạm giới hạn, tỷ lệ); huỷ ngang vô điều kiện (không cần điều kiện, không gây rủi ro cho ngân hàng).
  > "Các thỏa thuận mà không thể hủy bỏ hoặc thay đổi dưới bất kỳ hình thức nào khi thỏa thuận này đã được ký kết;"
  > "Khả năng trả nợ của khách hàng suy giảm theo thỏa thuận hoặc khi khách hàng vi phạm thỏa thuận đã được ký kết;"
  > "Hủy ngang vô điều kiện là thỏa thuận có thể hủy ngang không cần bất kỳ điều kiện, thỏa thuận nào với khách hàng và việc hủy ngang không gây ra các rủi ro cho ngân hàng."
  > — Đ3.5–3.7 ^d3-5

- Quyền thế chấp lại (rehypothecation): quyền của ngân hàng, theo thoả thuận và khi pháp luật cho phép, dùng tài sản bảo đảm của khách hàng làm tài sản bảo đảm cho nghĩa vụ tài chính của ngân hàng với tổ chức khác; tài sản dùng trong phái sinh với bên thứ ba để phòng ngừa rủi ro cho giao dịch với chính khách hàng đó, bên thứ ba không được thế chấp lại tiếp.
  > "Quyền thế chấp lại (rehypothecation) phải có đầy đủ các đặc điểm sau:"
  > "bên thứ ba không được tiếp tục thế chấp lại tài sản này."
  > — Đ3.15 ^d3-15

- Bị ràng buộc: tài sản không thể thanh lý, bán, chuyển nhượng, sử dụng theo pháp luật hoặc thoả thuận; không bị ràng buộc là trường hợp còn lại.
  > "Bị ràng buộc là việc tài sản của ngân hàng, khách hàng không thể thanh lý, bán, chuyển nhượng, sử dụng theo quy định của pháp luật hoặc thỏa thuận giữa các bên liên quan."
  > "Không bị ràng buộc là việc tài sản của ngân hàng, khách hàng không thuộc trường hợp bị ràng buộc."
  > — Đ3.17 ^d3-17

- Rủi ro thanh khoản, rủi ro danh tiếng và kiểm tra sức chịu đựng dùng định nghĩa của TT83/2025.
  > "Rủi ro thanh khoản, rủi ro danh tiếng và kiểm tra sức chịu đựng được định nghĩa theo quy định tại Thông tư số 83/2025/TT-NHNN"
  > — Đ3.18 ^d3-18

- Ngân hàng phải ban hành quy định nội bộ về quản lý rủi ro thanh khoản theo Đ14; quy định nội bộ được rà soát ít nhất một năm một lần và gửi NHNN trong 10 ngày kể từ ngày ban hành, sửa đổi.
  > "Ngân hàng phải ban hành quy định nội bộ về quản lý rủi ro thanh khoản theo quy định tại Điều 14 Thông tư này."
  > "Nội dung quy định nội bộ quy định tại khoản 1 và khoản 3 Điều này phải được rà soát, đánh giá lại định kỳ ít nhất một năm một lần và sửa đổi, bổ sung nếu cần thiết. Trong thời hạn 10 ngày kể từ ngày ban hành, sửa đổi, bổ sung quy định nội bộ, ngân hàng phải gửi Ngân hàng Nhà nước"
  > — Đ4.3–4.4 ^d4-3

- Ngân hàng phải có hệ thống thông tin kết nối toàn hệ thống để thống kê, theo dõi, quản lý dòng tiền, các khoản mục vốn, tài sản, nợ phải trả và tính toán, giám sát các giới hạn, tỷ lệ.
  > "Ngân hàng phải có hệ thống thông tin được kết nối toàn hệ thống để thực hiện các quy định tại Thông tư này, đảm bảo các yêu cầu tối thiểu sau:"
  > "Thống kê, theo dõi, quản lý dòng tiền, các khoản mục vốn, tài sản, nợ phải trả; tính toán, quản lý, giám sát các giới hạn, tỷ lệ bảo đảm an toàn trong hoạt động."
  > — Đ5 ^d5-1

*Không trích:* Đ1.3–1.4 (NHTM hỗ trợ, chương trình Chính phủ), Đ3.1–3.4, 3.8–3.14, 3.16, 3.19 (định nghĩa tín dụng, tỷ giá), Đ4.1–4.2 (quy định nội bộ về cấp tín dụng và vốn), Đ4.5 (hình thức gửi).

### C2-M2 — Tỷ lệ đòn bẩy

- Thống đốc NHNN quyết định, khi cần thiết trong từng thời kỳ, việc áp dụng tỷ lệ LEV, gồm ngưỡng tối thiểu và chế độ báo cáo. LEV = Vốn cấp 1 / Tổng trạng thái rủi ro (EM, Phụ lục III) × 100%. Ngoài thời gian áp dụng, ngân hàng quản lý LEV theo quy định nội bộ.
  > "Trong từng thời kỳ, trường hợp cần thiết, Thống đốc Ngân hàng Nhà nước quyết định việc áp dụng tỷ lệ LEV bao gồm ngưỡng áp dụng tối thiểu; tần suất, thời gian, phương thức báo cáo cho Ngân hàng Nhà nước và nội dung khác (nếu có)."
  > "T1: Vốn cấp 1 được xác định theo quy định của Thống đốc Ngân hàng Nhà nước về tỷ lệ an toàn vốn mà ngân hàng đang áp dụng;"
  > "EM (Exposure measure): Tổng trạng thái rủi ro được xác định theo Phụ lục III kèm theo Thông tư này."
  > "Ngoài khoảng thời gian áp dụng tỷ lệ LEV quy định tại khoản 1 Điều này, ngân hàng được thực hiện quản lý đối với tỷ lệ LEV theo quy định nội bộ của ngân hàng."
  > — Đ8.1–3 ^d8-1

### C2-M4 — Tỷ lệ dư nợ cho vay so với tổng tiền gửi

- LDR = L / D × 100%, tính theo VNĐ (gồm ngoại tệ quy đổi). L là tổng dư nợ cho vay (gồm dư nợ từ nhận uỷ thác) trừ cho vay TCTD khác tại VN và vay tái cấp vốn NHNN không nhằm hỗ trợ thanh khoản.
  > "Ngân hàng xác định tỷ lệ dư nợ cho vay so với tổng tiền gửi theo VNĐ, bao gồm VNĐ và các loại ngoại tệ được quy đổi sang VNĐ (theo tỷ giá quy định tại khoản 14 Điều 3 Thông tư này) theo công thức sau đây:"
  > "Số dư nợ cho vay đối với tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác tại Việt Nam;"
  > "Số dư vay tái cấp vốn của Ngân hàng Nhà nước không nhằm mục đích hỗ trợ thanh khoản."
  > — Đ12.1–3 ^d12-1

- D (tổng tiền gửi) gồm tiền gửi tổ chức (trừ tiền gửi TCTD, ký quỹ, tiền gửi không kỳ hạn của KBNN và 80% tiền gửi có kỳ hạn của KBNN), tiền gửi cá nhân, trái phiếu đủ điều kiện Vốn cấp 2, vốn uỷ thác, chênh lệch dương liên ngân hàng, vay nước ngoài, vốn chủ sở hữu (sau các khoản trừ) và lợi nhuận chưa phân phối; trừ đi cấp tín dụng khác không phải cho vay và đầu tư trái phiếu doanh nghiệp.
  > "(iv) 80% số dư tiền gửi có kỳ hạn của Kho bạc Nhà nước hoặc một tỷ lệ khác do Thống đốc Ngân hàng Nhà nước quyết định trong từng thời kỳ;"
  > "Số dư trái phiếu do ngân hàng phát hành trong nước đủ điều kiện tính vào Vốn cấp 2 theo quy định của Thống đốc Ngân hàng Nhà nước về tỷ lệ an toàn vốn mà ngân hàng đang áp dụng;"
  > "Chênh lệch dương giữa số dư được cấp tín dụng, nhận tiền gửi từ tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác trừ đi số dư cấp tín dụng, gửi tiền tại tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác;"
  > "Nguồn vay nước ngoài (bao gồm cả trái phiếu phát hành ra thị trường quốc tế) của ngân hàng."
  > "Số dư đầu tư trái phiếu doanh nghiệp (không bao gồm trái phiếu do tổ chức tín dụng khác tại Việt Nam phát hành, trái phiếu đặc biệt của Công ty Quản lý tài sản của các tổ chức tín dụng Việt Nam);"
  > — Đ12.4–5 ^d12-4

- Ngân hàng phải duy trì LDR tối đa 95%; thời điểm áp dụng theo Đ13.5 (từ khi áp dụng LCR/NSFR); từ đó phải báo cáo NHNN.
  > "Ngân hàng phải duy trì tỷ lệ LDR tối đa là 95%."
  > "Thời điểm áp dụng tỷ lệ LDR tại khoản 1 Điều này thực hiện theo quy định tại khoản 5 Điều 13 Thông tư này."
  > — Đ12.6–7 ^d12-6

### C2-M5 — Tỷ lệ khả năng chi trả và tỷ lệ nguồn vốn ổn định ròng

#### Điều 13. Áp dụng

- Từ 01/10/2028 ngân hàng phải áp dụng cả LCR và NSFR theo lộ trình tại Đ16.1.c và Đ22.2.
  > "Kể từ ngày 01 tháng 10 năm 2028, ngân hàng phải áp dụng cả 02 tỷ lệ LCR, tỷ lệ NSFR theo lộ trình quy định tại điểm c khoản 1 Điều 16, khoản 2 Điều 22 Thông tư này và các quy định khác tại Mục này."
  > — Đ13.1 ^d13-1

- Ngân hàng được đăng ký áp dụng sớm: trước 01/01/2028 để áp dụng LCR/NSFR theo lộ trình; trước 01/01/2033 để tuân thủ ngưỡng tối thiểu 100% cho cả hai tỷ lệ. Hồ sơ đăng ký phải kèm báo cáo đánh giá của HĐQT/HĐTV và của tổ chức kiểm toán độc lập; áp dụng từ ngày đầu tháng tiếp theo tháng đăng ký.
  > "Kể từ ngày Thông tư này có hiệu lực thi hành đến trước ngày 01 tháng 01 năm 2028, ngân hàng được gửi văn bản đăng ký đến Ngân hàng Nhà nước"
  > "Kể từ ngày Thông tư này có hiệu lực thi hành đến trước ngày 01 tháng 01 năm 2033, ngân hàng được gửi văn bản đăng ký đến Ngân hàng Nhà nước (Cục Quản lý, giám sát tổ chức tín dụng hoặc Ngân hàng Nhà nước Khu vực theo đối tượng giám sát an toàn vi mô) để đăng ký thực hiện tuân thủ ngưỡng tối thiểu 100% đối với cả 02 tỷ lệ LCR và NSFR;"
  > "Ngân hàng phải có báo cáo đánh giá của Hội đồng quản trị, Hội đồng thành viên của ngân hàng thương mại, Tổng Giám đốc (Giám đốc) của chi nhánh ngân hàng nước ngoài và báo cáo đánh giá của tổ chức kiểm toán độc lập về việc đã tuân thủ đầy đủ các quy định tại Mục này"
  > "Kể từ ngày đầu tiên của tháng tiếp theo tháng có văn bản đăng ký theo quy định tại điểm a hoặc điểm b khoản này, ngân hàng phải áp dụng quy định về tỷ lệ LCR, tỷ lệ NSFR theo ngưỡng đăng ký và các quy định khác tại Mục này."
  > — Đ13.2 ^d13-2

- Ngân hàng được chấp thuận dùng phương pháp xếp hạng nội bộ theo TT14/2025 trước 01/07/2033 phải tuân thủ ngưỡng 100% cho cả LCR và NSFR trong tối đa 90 ngày kể từ ngày được chấp thuận.
  > "Trường hợp được Ngân hàng Nhà nước chấp thuận áp dụng phương pháp xếp hạng nội bộ theo quy định tại Thông tư số 14/2025/TT-NHNN trước ngày 01 tháng 07 năm 2033, ngân hàng phải tuân thủ ngưỡng tối thiểu là 100% đối với cả 2 tỷ lệ LCR, tỷ lệ NSFR và các quy định khác tại Mục này trong thời hạn tối đa 90 ngày kể từ ngày được Ngân hàng Nhà nước chấp thuận."
  > — Đ13.3 ^d13-3

- Trước khi áp dụng LCR/NSFR, ngân hàng phải tuân thủ và báo cáo tỷ lệ dự trữ thanh khoản, tỷ lệ khả năng chi trả trong 30 ngày, tỷ lệ tối đa nguồn vốn ngắn hạn cho vay trung dài hạn và LDR theo TT22/2019 (đã sửa đổi bởi TT26/2022, TT09/2024, TT25/2026).
  > "Kể từ ngày Thông tư này có hiệu lực thi hành đến trước ngày ngân hàng áp dụng quy định về tỷ lệ LCR, tỷ lệ NSFR theo quy định tại khoản 1, 2, 3 Điều này, ngân hàng phải tuân thủ và báo cáo về tỷ lệ dự trữ thanh khoản, tỷ lệ khả năng chi trả trong 30 ngày, tỷ lệ tối đa của nguồn vốn ngắn hạn được sử dụng để cho vay trung hạn và dài hạn, tỷ lệ dư nợ cho vay so với tổng tiền gửi theo quy định tại Thông tư số 22/2019/TT-NHNN"
  > — Đ13.4 ^d13-4

- Từ khi áp dụng LCR/NSFR: không tuân thủ LDR theo TT22 mà tuân thủ LDR theo Đ12 TT50; các tỷ lệ cũ của TT22 chỉ phải báo cáo. Khi áp dụng ngưỡng 100% cho cả hai tỷ lệ: không phải tuân thủ, không phải báo cáo các tỷ lệ cũ; LDR không phải tuân thủ nhưng vẫn phải báo cáo.
  > "Ngân hàng không phải tuân thủ và không phải báo cáo tỷ lệ LDR theo quy định tại Thông tư số 22/2019/TT-NHNN;"
  > "Ngân hàng phải tuân thủ và báo cáo về tỷ lệ LDR theo quy định tại Điều 12 Thông tư này, trừ trường hợp quy định tại điểm d khoản này;"
  > "Ngân hàng không phải tuân thủ nhưng phải báo cáo tỷ lệ dự trữ thanh khoản, tỷ lệ khả năng chi trả trong 30 ngày, tỷ lệ tối đa của nguồn vốn ngắn hạn được sử dụng để cho vay trung hạn và dài hạn theo quy định tại Thông tư số 22/2019/TT-NHNN, trừ trường hợp quy định tại điểm d khoản này;"
  > "(i) Không phải tuân thủ và không phải báo cáo các tỷ lệ quy định tại điểm c khoản này;"
  > "(ii) Không phải tuân thủ nhưng vẫn phải báo cáo tỷ lệ quy định tại điểm b khoản này."
  > — Đ13.5 ^d13-5

#### Điều 14. Quản lý rủi ro thanh khoản

- Quản lý rủi ro thanh khoản theo TT83/2025; riêng quản lý theo loại tiền tệ trong LCR theo loại tiền tệ mà pháp luật về LCR yêu cầu từng thời kỳ.
  > "Ngân hàng thực hiện quản lý rủi ro thanh khoản theo quy định tại Thông tư số 83/2025/TT-NHNN. Riêng đối với quy định quản lý rủi ro thanh khoản theo loại tiền tệ trong tỷ lệ LCR, ngân hàng thực hiện quản lý thanh khoản theo loại tiền tệ mà ngân hàng phải áp dụng trong từng thời kỳ theo quy định pháp luật về tính tỷ lệ LCR."
  > — Đ14.1 ^d14-1

- Ngân hàng có giả định phù hợp về thanh khoản tài sản và khả năng tiếp cận nguồn vốn khi căng thẳng; trong căng thẳng, kiểm soát, hạn mức và quy mô HQLA không bị chi phối bởi áp lực cạnh tranh hay kết quả kinh doanh.
  > "Khi thực hiện quản lý rủi ro thanh khoản, ngân hàng có các giả định phù hợp về tính thanh khoản của tài sản và khả năng tiếp cận nguồn vốn trong giai đoạn căng thẳng."
  > "Trong giai đoạn căng thẳng của ngân hàng, các yêu cầu về hiệu quả quản lý rủi ro thanh khoản, các chức năng kiểm soát, hệ thống hạn mức, quy mô tài sản có tính thanh khoản cao (sau đây gọi là HQLA) không bị ảnh hưởng, chi phối bởi áp lực cạnh tranh, kết quả hoạt động kinh doanh để đáp ứng nhu cầu thanh khoản."
  > — Đ14.2 ^d14-2

- Ngân hàng xây dựng kế hoạch truyền thông, kế hoạch tài trợ dự phòng về thanh khoản, dự trữ thanh khoản và đa dạng hoá nguồn tài trợ để giảm lan truyền do rủi ro danh tiếng.
  > "Ngân hàng xây dựng kế hoạch và thực hiện việc truyền thông đến các đối tượng cần thiết theo quy định nội bộ; xây dựng các kế hoạch tài trợ dự phòng về thanh khoản cho ngân hàng, các khoản dự trữ thanh khoản và đa dạng hóa nguồn tài trợ khi xảy ra vấn đề thanh khoản để giảm thiểu khả năng lan truyền do rủi ro danh tiếng."
  > — Đ14.3 ^d14-3

- Với đồng tiền trọng yếu (VNĐ và ngoại tệ trọng yếu theo quy định nội bộ), ngân hàng phải xét đặc điểm thị trường và khả năng hoán đổi tiền tệ trong căng thẳng.
  > "Ngân hàng phải xem xét đặc điểm thị trường và đánh giá khả năng hoán đổi tiền tệ trong điều kiện căng thẳng khi quản lý thanh khoản đối với đồng tiền trọng yếu (VNĐ và ngoại tệ trọng yếu xác định theo quy định nội bộ của ngân hàng)."
  > — Đ14.4 ^d14-4

- Ngân hàng phải quản lý thanh khoản nội và ngoại bảng, chênh lệch kỳ hạn huy động – sử dụng vốn; đặt hạn mức tăng dự trữ thanh khoản cho giai đoạn nhu cầu cao (cuối năm, lễ tết, quyết toán thuế); xây dựng phương pháp xác định số dư vượt mức của tiền gửi hoạt động.
  > "Quản lý thanh khoản các hoạt động trong và ngoài bảng cân đối tài khoản kế toán, tính thanh khoản của tài sản và nợ phải trả, mức độ chênh lệch kỳ hạn giữa huy động và sử dụng vốn, sự đa dạng trong mô hình kinh doanh và chiến lược huy động vốn;"
  > "Xây dựng kế hoạch, thiết lập các hạn mức cần thiết trong hoạt động kiểm soát nội bộ nhằm tăng dự trữ thanh khoản để đảm bảo ngân hàng ứng phó với những giai đoạn có nhu cầu thanh khoản tăng cao (bao gồm cả các khoảng thời gian cuối năm, dịp nghỉ lễ, tết, khoảng thời gian quyết toán thuế);"
  > "Xây dựng nội dung về phương pháp xác định số dư vượt mức theo yêu cầu trong chính sách sản phẩm đối với tiền gửi hoạt động dựa trên dữ liệu, nhu cầu thanh toán của khách hàng hoặc nhóm khách hàng trong quy định nội bộ của ngân hàng."
  > — Đ14.5 ^d14-5

- Ngân hàng phải quản lý thanh khoản trong ngày: mục tiêu đáp ứng nghĩa vụ thanh toán đúng hạn trong điều kiện bình thường và căng thẳng; đo tổng dòng vào, dòng ra dự kiến trong ngày và mức thiếu hụt tiềm năng; có tài sản bảo đảm và phương án tiếp cận nguồn thanh khoản trong ngày; hằng năm thống kê, phân tích các sự kiện thanh khoản trong ngày.
  > "Ngân hàng phải thực hiện quản lý thanh khoản trong ngày (intraday liquidity management) theo các nguyên tắc sau:"
  > "(i) Đáp ứng nghĩa vụ thanh toán và quyết toán đúng hạn trong cả điều kiện bình thường và căng thẳng;"
  > "(ii) Ngân hàng phải đo lường tổng dòng tiền vào, tổng dòng tiền ra dự kiến trong ngày (expected daily gross liquidity inflows and outflows) và dự kiến mức độ thiếu hụt thanh khoản (range of potential net funding shortfalls) có thể phát sinh tại các thời điểm khác nhau trong ngày;"
  > "(iv) Ngân hàng phải có phương án tiếp cận các nguồn thanh khoản để đáp ứng nhu cầu thanh khoản trong ngày;"
  > "(v) Ngân hàng phải có tài sản bảo đảm có thể sử dụng được để tiếp cận nguồn thanh khoản, thực hiện quản lý và có cơ chế sử dụng tài sản bảo đảm này khi cần thiết để đáp ứng đủ nhu cầu thanh khoản trong ngày;"
  > "Hằng năm, ngân hàng phải thực hiện tổng hợp, thống kê, phân tích các sự kiện đã diễn ra khi thực hiện quản lý thanh khoản trong ngày của các ngày trong năm nhằm đánh giá sự phù hợp của các quy định về quản lý rủi ro thanh khoản"
  > — Đ14.6 ^d14-6

- Quản lý trạng thái tài sản bảo đảm: lập danh sách, theo dõi tài sản đang dùng làm bảo đảm và tài sản có thể dùng để huy động vốn dài hạn, ngắn hạn, trong ngày; với phái sinh, phải tính khả năng phát sinh yêu cầu bổ sung tài sản bảo đảm.
  > "Ngân hàng phải lập danh sách, xây dựng tiêu chí, theo dõi trạng thái của tài sản đang được sử dụng làm tài sản bảo đảm theo thỏa thuận, tài sản có thể sử dụng làm tài sản bảo đảm để huy động vốn trong dài hạn, ngắn hạn và trong ngày"
  > "Khi sử dụng công cụ phái sinh, ngân hàng phải tính đến khả năng phát sinh yêu cầu bổ sung tài sản bảo đảm theo thỏa thuận do biến động thị trường, thay đổi xếp hạng tín nhiệm, biến động tình hình tài chính của ngân hàng đó và các sự kiện kích hoạt khác."
  > — Đ14.7 ^d14-7

- Ngân hàng phải duy trì quy mô HQLA đủ tiêu chuẩn đáp ứng dòng tiền ra ròng theo kịch bản kiểm tra sức chịu đựng và ngưỡng LCR; quy mô HQLA phù hợp khẩu vị rủi ro; đánh giá khả năng thanh lý từng loại tài sản theo từng kịch bản.
  > "Ngân hàng phải duy trì quy mô HQLA đủ tiêu chuẩn để đáp ứng nhu cầu dòng tiền ra ròng phù hợp các kịch bản kiểm tra sức chịu đựng và ngưỡng yêu cầu tối thiểu của tỷ lệ LCR"
  > "(ii) Quy mô HQLA phù hợp với khẩu vị rủi ro của ngân hàng."
  > "Ngân hàng phải đánh giá khả năng thanh lý, bán, chuyển nhượng, sử dụng của từng loại tài sản phù hợp với từng kịch bản kiểm tra sức chịu đựng."
  > — Đ14.8 ^d14-8

- Kiểm tra sức chịu đựng về thanh khoản theo TT83/2025, kèm: gửi báo cáo kết quả cho NHNN trong 30 ngày sau khi kết thúc quý; kết quả phải đánh giá dòng tiền ra ròng, số ngày tồn tại (days of survival), cấu trúc nguồn vốn và tài sản, LCR, NSFR trong các kịch bản; dữ liệu lịch sử quan sát tối thiểu 10 năm; với kịch bản đặc thù và hỗn hợp, hệ số rút tiền do ngân hàng tự xác định nhưng tối thiểu bằng hệ số của Thông tư.
  > "Trong thời hạn 30 ngày kể từ ngày kết thúc Quý thực hiện kiểm tra sức chịu đựng về rủi ro thanh khoản, ngân hàng phải gửi báo cáo kết quả kiểm tra sức chịu đựng về rủi ro thanh khoản cho Ngân hàng Nhà nước"
  > "kết quả kiểm tra sức chịu đựng phải đánh giá được dòng tiền ra ròng, số ngày tồn tại (days of survival), cấu trúc nguồn vốn và tài sản của ngân hàng, tỷ lệ LCR, tỷ lệ NSFR trong các kịch bản kiểm tra sức chịu đựng của ngân hàng"
  > "(i) Xác định khoảng thời gian quan sát dữ liệu lịch sử (bao gồm dữ liệu nội bộ, dữ liệu thị trường) phục vụ xây dựng kịch bản kiểm tra sức chịu đựng tối thiểu là 10 năm liền kề trước thời điểm thực hiện kiểm tra sức chịu đựng;"
  > "Đối với kịch bản đặc thù của ngân hàng và kịch bản hỗn hợp, hệ số rút tiền của các loại tiền gửi do ngân hàng tự xác định nhưng tối thiểu phải bằng hệ số rút tiền quy định tại Thông tư này."
  > — Đ14.9 ^d14-9

#### Điều 15. Hành động khắc phục

- Căn cứ thanh tra, kiểm tra, giám sát, NHNN được yêu cầu biện pháp khắc phục về quản lý rủi ro thanh khoản, gồm hoàn thiện kế hoạch dự phòng thanh khoản, giảm rủi ro (như duy trì HQLA cao hơn), hạn chế cấp tín dụng hoặc mở rộng kinh doanh, áp tỷ lệ an toàn vốn cao hơn.
  > "Đánh giá, hoàn thiện kế hoạch dự phòng thanh khoản;"
  > "Các biện pháp giảm mức độ rủi ro thanh khoản (như hạn chế chênh lệch quy mô, kỳ hạn giữa huy động và sử dụng vốn, duy trì quy mô HQLA đủ tiêu chuẩn cao hơn);"
  > "Hạn chế thực hiện hoạt động cấp tín dụng, góp vốn, mua cổ phần hoặc mở rộng hoạt động kinh doanh;"
  > "Yêu cầu áp dụng tỷ lệ an toàn vốn cao hơn so với quy định về tỷ lệ an toàn vốn của Ngân hàng Nhà nước;"
  > — Đ15.2 ^d15-2

#### Điều 16–18. Tỷ lệ LCR

- Ba loại LCR: LCR quy VNĐ (VNĐ và ngoại tệ quy đổi), LCR VNĐ, LCR ngoại tệ trọng yếu. LCR = Giá trị HQLA đủ điều kiện / Dòng tiền ra ròng trong 30 ngày tiếp theo × 100%.
  > "(i) Tỷ lệ LCR quy VNĐ (bao gồm VNĐ và các ngoại tệ khác được quy đổi sang VNĐ theo tỷ giá quy định tại khoản 14 Điều 3 Thông tư này);"
  > "(ii) Tỷ lệ LCR đối với VNĐ (sau đây gọi tắt là tỷ lệ LCR VNĐ);"
  > "(iii) Tỷ lệ LCR đối với một đồng tiền ngoại tệ trọng yếu (sau đây gọi tắt là tỷ lệ LCR ngoại tệ trọng yếu);"
  > "Giá trị HQLA đủ điều kiện: Phần giá trị HQLA đủ tiêu chuẩn được quy định tại Điều 20 Thông tư này và Phần A Phụ lục I kèm theo Thông tư này;"
  > "Dòng tiền ra ròng trong 30 ngày tiếp theo kể từ ngày chốt số liệu báo cáo tính tỷ lệ LCR được xác định theo quy định tại Điều 21 Thông tư này."
  > — Đ16.1.a–b ^d16-1

- Lộ trình ngưỡng tối thiểu LCR quy VNĐ riêng lẻ: 50% (năm thứ nhất, từ 01/10/2028 với ngân hàng thuộc Đ13.1), tăng 10 điểm mỗi năm, 100% từ năm thứ sáu (01/10/2033).
  > "Ngân hàng thực hiện lộ trình áp dụng các ngưỡng tối thiểu của tỷ lệ LCR quy VNĐ riêng lẻ như sau:"
  > — Đ16.1.c, Bảng 1 ^d16-1c

  | Năm áp dụng | Năm thứ nhất | Năm thứ hai | Năm thứ ba | Năm thứ tư | Năm thứ năm | Năm thứ sáu trở đi |
  |---|---|---|---|---|---|---|
  | (i) Thuộc khoản 1 Điều 13 | 01/10/2028 | 01/10/2029 | 01/10/2030 | 01/10/2031 | 01/10/2032 | 01/10/2033 |
  | (ii) Thuộc điểm a khoản 2 Điều 13 | Ngày đầu tiên của tháng tiếp theo tháng có văn bản đăng ký | +1 năm | +2 năm | +3 năm | +4 năm | +5 năm |
  | Tỷ lệ LCR quy VNĐ áp dụng | 50% | 60% | 70% | 80% | 90% | 100% |

- LCR hợp nhất và LCR ngoại tệ trọng yếu do ngân hàng quản lý theo quy định nội bộ; LCR VNĐ riêng lẻ ngân hàng phải quản lý. Ngân hàng phải báo cáo NHNN LCR riêng lẻ (LCR quy VNĐ và LCR VNĐ).
  > "Ngân hàng được thực hiện quản lý đối với tỷ lệ LCR hợp nhất, tỷ lệ LCR ngoại tệ trọng yếu theo quy định nội bộ của ngân hàng;"
  > "Ngân hàng phải quản lý tỷ lệ LCR VNĐ riêng lẻ."
  > "Ngân hàng phải báo cáo Ngân hàng Nhà nước tỷ lệ LCR riêng lẻ (bao gồm tỷ lệ LCR quy VNĐ và tỷ lệ LCR VNĐ) theo quy định về chế độ báo cáo thống kê đối với các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài."
  > — Đ16.1.d–đ, Đ16.2 ^d16-2

- Ngân hàng phải có bộ phận tại trụ sở chính theo dõi, quản lý LCR hằng ngày, do Tổng giám đốc hoặc Phó Tổng giám đốc được uỷ quyền phụ trách.
  > "Ngân hàng phải có bộ phận tại trụ sở chính để theo dõi, quản lý tỷ lệ LCR quy định tại điểm c khoản 1 Điều 16 Thông tư này hằng ngày, do Tổng giám đốc (Giám đốc) hoặc Phó Tổng giám đốc (Phó Giám đốc) được ủy quyền phụ trách."
  > — Đ17.1 ^d17-1

- Khi vi phạm LCR quy VNĐ riêng lẻ: ngân hàng phải ngay lập tức dùng biện pháp tự xử lý (vay TCTD khác, cam kết không thể huỷ ngang…); dùng biện pháp tự xử lý từ 10% giá trị HQLA đủ điều kiện trở lên thì NHNN giám sát tăng cường; báo cáo hằng ngày trước 12 giờ sáng hôm sau, ngày đầu báo cáo bổ sung trước 17 giờ.
  > "Áp dụng một hoặc một số biện pháp tự xử lý khi vi phạm tỷ lệ LCR, bao gồm: Vay của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác, vay của tổ chức tài chính ở nước ngoài"
  > "Trường hợp ngân hàng phải sử dụng các biện pháp tự xử lý quy định tại điểm b(i) khoản này ở mức từ 10% trở lên của giá trị HQLA đủ điều kiện, Ngân hàng Nhà nước giám sát tăng cường và thực hiện các biện pháp xử lý theo quy định của pháp luật;"
  > "Thời hạn báo cáo số liệu của từng ngày là trước 12 giờ sáng hôm sau. Riêng trong ngày báo cáo lần đầu tiên kể từ thời điểm tỷ lệ LCR vi phạm, trước 17 giờ, ngân hàng phải báo cáo bổ sung các nội dung tối thiểu như sau:"
  > — Đ17.2 ^d17-2

- Ngân hàng chỉ được cho vay, ký cam kết không thể huỷ ngang với TCTD khác để bù đắp thiếu hụt khả năng chi trả nếu sau đó vẫn đảm bảo LCR.
  > "Ngân hàng chỉ được cho vay, ký các cam kết gửi tiền có kỳ hạn không thể hủy ngang, cam kết cho vay không thể hủy ngang với tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác để bù đắp thiếu hụt khả năng chi trả nếu sau khi thực hiện các hoạt động này vẫn đảm bảo tỷ lệ LCR quy định tại Điều 16 Thông tư này."
  > — Đ17.3 ^d17-3

- Nguy cơ mất khả năng chi trả: giá trị HQLA đủ điều kiện thấp hơn 90% mức phải đáp ứng trong 30 ngày liên tục. Mất khả năng chi trả: không thanh toán được nghĩa vụ nợ trong 30 ngày kể từ ngày đến hạn.
  > "Ngân hàng có nguy cơ mất khả năng chi trả khi giá trị HQLA đủ điều kiện tại thời điểm tính tỷ lệ LCR thấp hơn mức 90% giá trị HQLA đủ điều kiện mà ngân hàng phải đáp ứng để tuân thủ quy định về tỷ lệ LCR tại Thông tư này trong thời gian 30 ngày liên tục."
  > "Ngân hàng mất khả năng chi trả khi không có khả năng thực hiện thanh toán nghĩa vụ nợ trong thời gian 30 ngày kể từ ngày đến hạn thanh toán."
  > — Đ18.1–2 ^d18-1

#### Điều 19–21. HQLA và dòng tiền ra ròng

- HQLA gồm tài sản cấp 1 và cấp 2 (2A, 2B), xác định theo Phụ lục I.
  > "Tài sản có tính thanh khoản cao gồm tài sản cấp 1, tài sản cấp 2. Tài sản cấp 2 bao gồm tài sản cấp 2A và tài sản cấp 2B. Tài sản cấp 1, tài sản cấp 2A, tài sản cấp 2B được xác định theo quy định tại Phụ lục I kèm theo Thông tư này."
  > — Đ19.1 ^d19-1

- HQLA đủ tiêu chuẩn là HQLA đáp ứng yêu cầu vận hành tại Đ20.2 và được dùng để tính LCR.
  > "Tài sản có tính thanh khoản cao đủ tiêu chuẩn là HQLA đáp ứng đầy đủ các yêu cầu vận hành quy định tại khoản 2 Điều này. HQLA đủ tiêu chuẩn được sử dụng để tính tỷ lệ LCR."
  > — Đ20.1 ^d20-1

- Yêu cầu vận hành: chuyển đổi được thành tiền (bán trực tiếp, repo, giao dịch với NHNN) trong căng thẳng 30 ngày; không bị ràng buộc (tài sản ràng buộc một phần coi là bị ràng buộc); do bộ phận quản lý thanh khoản kiểm soát; xác định danh mục hằng ngày; HQLA không còn đủ tiêu chuẩn được giữ thêm 30 ngày.
  > "HQLA phải có sẵn để ngân hàng có thể chuyển đổi thành tiền mặt thông qua các hình thức như bán trực tiếp (outright sale) hoặc giao dịch repo hoặc các giao dịch với Ngân hàng Nhà nước, nhằm bù đắp thiếu hụt trong giai đoạn căng thẳng 30 ngày mà không bị hạn chế đối với việc sử dụng số tiền thu được;"
  > "Trường hợp một tài sản tài chính (trừ tiền mặt) bị ràng buộc một phần giá trị cũng được xác định là bị ràng buộc;"
  > "Danh mục HQLA phải được kiểm soát bởi bộ phận chịu trách nhiệm quản lý thanh khoản của ngân hàng"
  > "Ngân hàng phải thực hiện xác định danh mục HQLA hằng ngày đảm bảo phù hợp với sự thay đổi của quy định pháp luật, thị trường và các biến động khác;"
  > "Trường hợp HQLA đủ tiêu chuẩn trở thành không đủ tiêu chuẩn, ngân hàng được phép tiếp tục giữ tài sản đó trong danh mục HQLA đủ tiêu chuẩn trong 30 ngày kể từ ngày HQLA đủ tiêu chuẩn đó trở thành không đủ tiêu chuẩn."
  > — Đ20.2 ^d20-2

- Tổng dòng tiền ra ròng = Tổng dòng tiền ra − Min(Tổng dòng tiền vào, 75% Tổng dòng tiền ra). Dòng tiền ra = số dư nghĩa vụ nợ và cam kết ngoại bảng × hệ số rút tiền (Phần B PL I); dòng tiền vào = số dư tài sản và cam kết ngoại bảng × hệ số thu tiền (Phần C PL I).
  > "Tổng dòng tiền ra ròng = Tổng dòng tiền ra – Min (Tổng dòng tiền vào, 75% Tổng dòng tiền ra)"
  > "Tổng dòng tiền ra bằng số dư của các nghĩa vụ nợ và cam kết ngoại bảng nhân với hệ số rút tiền. Tổng dòng tiền ra được xác định theo Phần B Phụ lục I kèm theo Thông tư này;"
  > "Tổng dòng tiền vào bằng số dư của các loại tài sản và cam kết ngoại bảng nhân với hệ số thu tiền, nhưng không vượt quá 75% tổng dòng tiền ra."
  > — Đ21.2 ^d21-2

- Nguyên tắc: chỉ tính dòng tiền trong 30 ngày; dòng vào từ tài sản đã tính vào HQLA không được tính là dòng vào; khoản mục thuộc nhiều nhóm dòng ra thì dùng hệ số rút tiền cao nhất.
  > "Chỉ tính các dòng tiền có khả năng phát sinh trong vòng 30 ngày tiếp theo kể từ ngày chốt số liệu báo cáo tính tỷ lệ LCR;"
  > "Các tài sản thuộc danh mục HQLA đủ tiêu chuẩn và đã tính vào HQLA đủ điều kiện thì dòng tiền vào phát sinh từ tài sản đó không được tính là dòng tiền vào;"
  > "Trường hợp một khoản mục có thể được ghi nhận đồng thời vào nhiều nhóm dòng tiền ra có hệ số rút tiền khác nhau, ngân hàng tính dòng tiền ra tương ứng với hệ số rút tiền cao nhất cho khoản mục đó."
  > — Đ21.3 ^d21-3

#### Điều 22–26. Tỷ lệ NSFR

- NSFR = ASF / RSF × 100%; ASF theo Đ23 và Phụ lục II, RSF theo Đ24 và Phụ lục II.
  > "Nguồn vốn ổn định sẵn có (ASF) là giá trị danh mục ASF được quy định tại Điều 23 Thông tư này và Phụ lục II kèm theo Thông tư này;"
  > "Nguồn vốn ổn định yêu cầu (RSF) là giá trị danh mục RSF được quy định tại Điều 24 Thông tư này và Phụ lục II kèm theo Thông tư này."
  > — Đ22.1 ^d22-1

- Lộ trình ngưỡng tối thiểu NSFR riêng lẻ (VNĐ và ngoại tệ quy đổi): 90% (01/10/2028), 95% (01/10/2029), 100% từ 01/10/2030 với ngân hàng thuộc Đ13.1.
  > "Ngân hàng thực hiện lộ trình áp dụng các ngưỡng tối thiểu của tỷ lệ NSFR riêng lẻ (bao gồm các khoản mục bằng VNĐ và ngoại tệ khác được quy đổi sang VNĐ theo tỷ giá quy định tại khoản 14 Điều 3 Thông tư này) như sau:"
  > — Đ22.2, Bảng 2 ^d22-2

  | Năm áp dụng | Năm thứ nhất | Năm thứ hai | Năm thứ ba trở đi |
  |---|---|---|---|
  | a) Thuộc khoản 1 Điều 13 | 01/10/2028 | 01/10/2029 | 01/10/2030 |
  | b) Thuộc điểm a khoản 2 Điều 13 | Ngày đầu tiên của tháng tiếp theo tháng có văn bản đăng ký | +1 năm | +2 năm |
  | Tỷ lệ NSFR áp dụng | 90% | 95% | 100% |

- NSFR hợp nhất do ngân hàng quản lý theo quy định nội bộ; NSFR riêng lẻ phải báo cáo NHNN.
  > "Ngân hàng được thực hiện quản lý đối với tỷ lệ NSFR hợp nhất theo quy định nội bộ của ngân hàng."
  > "Ngân hàng phải báo cáo Ngân hàng Nhà nước tỷ lệ NSFR riêng lẻ theo quy định về chế độ báo cáo thống kê đối với các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài."
  > — Đ22.3–4 ^d22-3

- Khi tính NSFR dùng định nghĩa thống nhất với LCR; áp quy định về cấu phần vốn, hệ số rủi ro theo văn bản tỷ lệ an toàn vốn ngân hàng đang áp dụng (TT41/2016 hoặc phương pháp tiêu chuẩn TT14/2025). Khoản phải đòi và phải trả repo/reverse repo tính tách biệt: phải đòi vào RSF, phải trả vào ASF.
  > "Sử dụng định nghĩa, thuật ngữ thống nhất với định nghĩa, thuật ngữ quy định khi tính tỷ lệ LCR;"
  > "(ii) Phương pháp tiêu chuẩn quy định tại Thông tư số 14/2025/TT-NHNN, kể cả trường hợp ngân hàng tính tỷ lệ an toàn vốn theo phương pháp xếp hạng nội bộ."
  > "Các khoản phải đòi, khoản phải trả trong giao dịch repo, reverse repo phải được tính trên cơ sở tách biệt tổng giá trị khoản phải đòi, tổng giá trị khoản phải trả. Tổng giá trị khoản phải đòi sẽ được tính vào RSF, tổng giá trị khoản phải trả sẽ được tính vào ASF."
  > — Đ22.5–6 ^d22-5

- ASF = Σ giá trị thành phần danh mục ASF × hệ số ASF (Phần A PL II). Kỳ hạn ASF tính tới thời điểm sớm nhất phải thực hiện nghĩa vụ; khách hàng có quyền rút trước hạn thì lấy thời điểm sớm nhất khách hàng được thực hiện quyền; quyền gia hạn giả định không thực hiện; vi phạm thanh toán sớm theo kết luận thanh tra thì ASF 0%.
  > "Ngân hàng thực hiện xác định danh mục ASF và hệ số ASF theo quy định tại Phần A Phụ lục II kèm theo Thông tư này."
  > "Danh mục ASF phải được phân loại vào các nhóm kỳ hạn (maturity buckets) và kỳ hạn là khoảng thời gian kể từ thời điểm tính tỷ lệ NSFR đến thời điểm sớm nhất phải thực hiện nghĩa vụ theo thỏa thuận phù hợp với quy định pháp luật của công cụ vốn chủ sở hữu hoặc nợ phải trả."
  > "Trường hợp ngân hàng không có quyền mua lại, thanh toán sớm và khách hàng có quyền bán lại, rút trước hạn theo thỏa thuận phù hợp với quy định pháp luật, kỳ hạn được xác định trên cơ sở thời điểm sớm nhất khách hàng được thực hiện quyền theo thỏa thuận đó;"
  > "Trường hợp vi phạm việc thực hiện thanh toán sớm theo kết luận thanh tra, kiểm tra, ngân hàng phải áp dụng hệ số ASF là 0% đối với toàn bộ số dư phải thực hiện thanh toán sớm còn lại đến thời điểm tính tỷ lệ NSFR;"
  > — Đ23.1–3 ^d23-1

- RSF = Σ giá trị thành phần danh mục RSF × hệ số RSF (PL II). Kỳ hạn RSF tính tới thời điểm muộn nhất phải thực hiện nghĩa vụ; tài sản bị ràng buộc từ 1 năm trở lên nhận RSF 100%; từ 6 tháng đến dưới 1 năm nhận tối thiểu 50%; dưới 6 tháng như khi không bị ràng buộc.
  > "Ngân hàng thực hiện xác định danh mục RSF và hệ số RSF theo quy định tại Phụ lục II kèm theo Thông tư này."
  > "Danh mục RSF phải được phân loại vào các nhóm kỳ hạn (maturity buckets) và kỳ hạn là khoảng thời gian kể từ thời điểm tính tỷ lệ NSFR đến thời điểm muộn nhất phải thực hiện nghĩa vụ theo thỏa thuận phù hợp với quy định pháp luật của tài sản."
  > "Thời gian bị ràng buộc còn lại từ một năm trở lên phải nhận hệ số RSF 100%;"
  > "(i) Trong trường hợp không bị ràng buộc mà tài sản nhận hệ số RSF bằng hoặc thấp hơn 50% thì tài sản đó khi bị ràng buộc phải nhận hệ số RSF 50%;"
  > "Thời gian bị ràng buộc còn lại dưới 06 tháng nhận hệ số RSF như tài sản đó khi không bị ràng buộc."
  > — Đ24.1–4 ^d24-1

- Phái sinh: nợ phái sinh NSFR = nợ phái sinh − ký quỹ biến động bằng tài sản tài chính; tài sản phái sinh NSFR = tài sản phái sinh − ký quỹ biến động bằng tiền mặt đủ điều kiện. Chênh lệch dương nợ − tài sản nhận ASF 0%; chênh lệch dương tài sản − nợ nhận RSF 100%.
  > "Nợ phái sinh NSFR = Nợ phái sinh – Giá trị ký quỹ biến động (variation margin) bằng tài sản tài chính"
  > "ASF = 0% x Max ((Nợ phái sinh NSFR – Tài sản phái sinh NSFR), 0);"
  > "RSF = 100% x Max ((Tài sản phái sinh NSFR – Nợ phái sinh NSFR), 0)."
  > — Đ25.2, 25.5 ^d25-5

- Cặp tài sản – nợ phải trả phụ thuộc lẫn nhau (nguồn vốn chỉ dùng cho tài sản cụ thể, kỳ hạn và số tiền khớp hoàn toàn, không phải phái sinh, ngân hàng chỉ là trung gian pass-through) được áp RSF và ASF 0%; NHNN có quyền yêu cầu ngừng áp dụng.
  > "Nguồn vốn huy động để sử dụng cho một tài sản cụ thể và không thể sử dụng để tài trợ cho tài sản khác;"
  > "Kỳ hạn, thời hạn, số tiền thanh toán gốc từ tài sản và nợ phải trả phải trùng khớp hoàn toàn với nhau;"
  > "Ngân hàng chỉ đóng vai trò trung gian (pass-through), chuyển toàn bộ nguồn vốn nhận được sang tài trợ cho tài sản tương ứng và không chịu rủi ro trong quá trình cung cấp sản phẩm, dịch vụ."
  > "Được áp dụng hệ số RSF và ASF bằng 0% đối với từng cặp tài sản và nợ phải trả phụ thuộc đáp ứng đầy đủ các điều kiện tại khoản 1 Điều này."
  > — Đ26.1–2 ^d26-1

#### Điều 27. Công bố thông tin

- Ngân hàng phải công bố thông tin về các tỷ lệ thanh khoản theo Phụ lục IV tối thiểu 6 tháng một lần (bán niên chậm nhất 75 ngày, năm chậm nhất 120 ngày); ngân hàng chưa đạt ngưỡng 100% không được tuyên bố đã tuân thủ toàn bộ Mục 5.
  > "Ngân hàng phải thực hiện công bố thông tin về các tỷ lệ thanh khoản theo nội dung quy định tại Phụ lục IV kèm theo Thông tư này tối thiểu định kỳ 06 tháng một lần theo thời hạn như sau:"
  > "Thời hạn công bố thông tin bán niên chậm nhất 75 ngày kể từ ngày kết thúc 06 tháng đầu năm tài chính;"
  > "Thời hạn công bố thông tin năm chậm nhất 120 ngày kể từ ngày kết thúc năm tài chính."
  > "ngân hàng chỉ được công bố thông tin theo nguyên tắc phản ánh đúng thực trạng ngân hàng đang triển khai thực hiện theo Thông tư này, không được tuyên bố đã tuân thủ toàn bộ quy định tại Mục này."
  > — Đ27.1, 27.4 ^d27-1

### PL1 — Hướng dẫn xác định tỷ lệ khả năng chi trả

#### Phần A. HQLA đủ điều kiện

- Giá trị HQLA đủ điều kiện = Level 1 + Level 2A + Level 2B + hạn mức (khoản 4, 5) − KĐC15% − KĐC40%. KĐC15% và KĐC40% là phần điều chỉnh trần, tính trên giá trị sau khi đảo ngược (unwinding) các giao dịch có bảo đảm, repo, reverse repo đáo hạn trong 30 ngày; hệ số 15/85, 15/60 và 2/3 như trong công thức.
  > "Level 1, Level 2A, Level 2B: Giá trị HQLA đủ tiêu chuẩn cấp 1, cấp 2A, cấp 2B không điều chỉnh sau khi nhân với hệ số thanh khoản tương ứng với tài sản liên quan;"
  > "Giá trị điều chỉnh của tài sản cấp 1, cấp 2A, cấp 2B là giá trị HQLA đủ tiêu chuẩn thu được sau khi hoàn tất việc đảo ngược (unwinding) các giao dịch có bảo đảm bằng tài sản tài chính hoặc giao dịch repo, reverse repo có ngày đáo hạn trong 30 ngày"
  > "Giá trị HQLA đủ điều kiện = Level 1 + Level 2A + Level 2B + Hạn mức (Mục 5 Bảng này) – KĐC15% (Mục 3 Bảng này) – KĐC40% (Mục 4 Bảng này)"
  > — PL1.A.I.1–3 ^pl1-a1

  *Công thức trong raw (PL1.A.I.2–3):* $\text{KĐC15\%}=\max[(\text{KĐC.L2B}-\tfrac{15}{85}(\text{KĐC.L1}+\text{KĐC.L2A})),(\text{KĐC.L2B}-\tfrac{15}{60}\text{KĐC.L1}),0]$; $\text{KĐC40\%}=\max[(\text{KĐC.L2A}+\text{KĐC.L2B}-\text{KĐC15\%}-\tfrac{2}{3}\text{KĐC.L1}),0]$.

- Hạn mức chưa sử dụng bảo đảm bằng HQLA cấp 1 trong giao dịch với NHNN được tính vào HQLA đủ điều kiện như tài sản cấp 1. Chi nhánh NHNNg được tính hạn mức cam kết của ngân hàng mẹ, tối đa 50% (có danh mục HQLA cấp 1 đối ứng) hoặc 40% (không đối ứng) giá trị HQLA đủ điều kiện phải đáp ứng.
  > "Hạn mức chưa sử dụng được thiết lập trên cơ sở bảo đảm bởi HQLA cấp 1 trong giao dịch với Ngân hàng Nhà nước được đưa vào giá trị HQLA đủ điều kiện và được coi là tài sản cấp 1."
  > "hạn mức cam kết chưa sử dụng từ ngân hàng mẹ được tính vào giá trị HQLA đủ điều kiện nhưng không vượt quá 50% giá trị HQLA đủ điều kiện mà chi nhánh ngân hàng nước ngoài phải đáp ứng"
  > "chi nhánh ngân hàng nước ngoài được tính vào giá trị HQLA đủ điều kiện nhưng không vượt quá 40% giá trị HQLA đủ điều kiện"
  > — PL1.A.I.4–5 ^pl1-a1-4

- Tài sản cấp 1: hệ số thanh khoản 100%, không bị giới hạn; gồm tiền mặt, tiền gửi tại NHNN (cả DTBB), công cụ nợ Chính phủ VN và tín phiếu NHNN bằng VNĐ và ngoại tệ, trái phiếu Chính phủ bảo lãnh 100%, trái phiếu chính quyền địa phương dùng trong giao dịch NHNN theo quyết định của Thống đốc, chứng khoán Chính phủ/NHTW/PSE nước ngoài và tổ chức quốc tế có hệ số rủi ro 0%, niêm yết, giảm giá tối đa 5% trong 30 ngày căng thẳng (lịch sử 10 năm). NHNN có quyền yêu cầu hệ số thấp hơn.
  > "HQLA đủ tiêu chuẩn cấp 1 không bị giới hạn khi tính giá trị HQLA đủ điều kiện và được áp dụng hệ số thanh khoản là 100%, trừ trường hợp quy định tại khoản 2 Mục này."
  > "Tiền gửi (bao gồm cả tiền gửi dự trữ bắt buộc) tại Ngân hàng Nhà nước;"
  > "Có lịch sử thị trường trong 10 năm (hoặc thời gian tối đa mà thị trường có dữ liệu nếu dữ liệu dưới 10 năm) với mức giảm giá tối đa không vượt quá 5% hoặc mức tăng của chiết khấu không vượt quá 5% trong khoảng thời gian 30 ngày căng thẳng của thị trường đó;"
  > "Công cụ nợ của Chính phủ Việt Nam (bao gồm cả trái phiếu Chính phủ Việt Nam, tín phiếu Kho bạc Nhà nước), tín phiếu Ngân hàng Nhà nước được phát hành bằng VNĐ;"
  > "Công cụ nợ của Chính phủ Việt Nam, tín phiếu Ngân hàng Nhà nước được phát hành bằng ngoại tệ;"
  > "Trái phiếu được Chính phủ bảo lãnh thanh toán 100% giá trị gốc, lãi khi đến hạn; trái phiếu chính quyền địa phương được sử dụng trong các giao dịch của Ngân hàng Nhà nước theo quyết định của Thống đốc Ngân hàng Nhà nước trong từng thời kỳ;"
  > — PL1.A.II.1–3 ^pl1-a2

- Tài sản cấp 2A: hệ số thanh khoản 85%; gồm chứng khoán Chính phủ/NHTW/PSE nước ngoài, tổ chức tài chính quốc tế có hệ số rủi ro tối đa 20%, và chứng khoán nợ doanh nghiệp phi tài chính xếp hạng từ AA- trở lên; đều phải niêm yết, giảm giá tối đa 10% trong 30 ngày căng thẳng.
  > "HQLA đủ tiêu chuẩn cấp 2A áp dụng hệ số thanh khoản là 85% khi tính giá trị HQLA đủ điều kiện, trừ trường hợp quy định tại khoản 2 Mục này."
  > "Có hệ số rủi ro là tối đa 20% theo phương pháp tiêu chuẩn;"
  > "Được doanh nghiệp xếp hạng tín nhiệm độc lập xếp hạng tín nhiệm từ AA- trở lên;"
  > — PL1.A.III ^pl1-a3

- Tài sản cấp 2B: RMBS xếp hạng từ AA, LTV trung bình tối đa 80% (hệ số 75%); chứng khoán nợ doanh nghiệp phi tài chính từ BBB- (50%); chứng khoán Chính phủ/NHTW nước ngoài từ BBB- và hệ số rủi ro tối đa 50% (50%); cổ phiếu phổ thông phi tài chính thuộc VN30 hoặc chỉ số quan trọng, giảm giá tối đa 40% (50%).
  > "Chứng khoán được bảo đảm bằng các khoản phải đòi bất động sản thế chấp bằng nhà ở (RMBS) được áp dụng hệ số thanh khoản là 75% khi đáp ứng tất cả các điều kiện sau:"
  > "Chứng khoán nợ doanh nghiệp được áp dụng hệ số thanh khoản là 50% khi đáp ứng tất cả các điều kiện sau:"
  > "Cổ phiếu phổ thông được áp dụng hệ số thanh khoản là 50% khi đáp ứng tất cả các điều kiện sau:"
  > "Là một cổ phiếu thuộc chỉ số chứng khoán VN30 hoặc thuộc danh mục của một chỉ số chứng khoán quan trọng theo quyết định của cơ quan nhà nước có thẩm quyền tại quốc gia nơi ngân hàng có rủi ro thanh khoản;"
  > — PL1.A.IV ^pl1-a4

#### Phần B. Dòng tiền ra

- Nguồn vốn có kỳ hạn còn lại trên 30 ngày không tính vào dòng tiền ra khi khách hàng không có quyền rút trước hạn trong 30 ngày, hoặc khi tiền gửi bán lẻ VNĐ rút trước hạn chỉ được hưởng tối đa lãi suất không kỳ hạn thấp nhất và không có lợi ích khác. Không xác định được thời hạn thì tính vào dòng tiền ra của ngày tiếp theo.
  > "Trường hợp không xác định được thời hạn thực hiện nghĩa vụ hoặc cam kết và trường hợp nguồn huy động có thời hạn còn lại trên 30 ngày quy định tại điểm b khoản 4 Mục này, số tiền phải thực hiện nghĩa vụ, cam kết đó phải tính vào “Dòng tiền ra” của “Ngày tiếp theo”."
  > "Khách hàng không có quyền rút tiền trước hạn theo thỏa thuận (bao gồm cả trường hợp tài sản tài chính của khách hàng đang bị ràng buộc) trong khoảng thời gian lớn hơn 30 ngày kể từ thời điểm tính tỷ lệ LCR;"
  > "Khách hàng có quyền rút tiền trước hạn khoản tiền gửi bán lẻ bằng VNĐ (bao gồm cả tiền gửi bán buôn được xác định như tiền gửi bán lẻ) mà khách hàng chỉ được áp dụng mức lãi suất tối đa bằng mức lãi suất tiền gửi không kỳ hạn bằng VNĐ thấp nhất của ngân hàng đó theo đối tượng khách hàng tại thời điểm khách hàng rút trước hạn tiền gửi và không được hưởng phần lợi ích khác (nếu có) phát sinh từ nguồn tiền gửi của khách hàng;"
  > — PL1.B.I.2–4 ^pl1-b1

- Tiền gửi bán lẻ (cá nhân, tổ hợp tác, hộ kinh doanh) ổn định: được Bảo hiểm tiền gửi Việt Nam bảo hiểm hoàn toàn và khách hàng có khoản vay trung dài hạn hoặc có tài khoản thanh toán phát sinh giao dịch trong 6 tháng gần nhất; hệ số rút tiền 5%. Phần vượt giới hạn bảo hiểm và tiền gửi ngoại tệ là kém ổn định, hệ số 10%. Khi stress test phải chia tiền gửi kém ổn định thành nhóm rủi ro tương đồng.
  > "Khách hàng bán lẻ là cá nhân, tổ hợp tác, hộ kinh doanh (không bao gồm doanh nghiệp tư nhân và tổ chức khác không có tư cách pháp nhân) tại ngân hàng."
  > "Tiền gửi ngoại tệ là tiền gửi bán lẻ kém ổn định."
  > "Tiền gửi bán lẻ ổn định là các khoản tiền gửi được bảo hiểm hoàn toàn bởi Bảo hiểm tiền gửi Việt Nam và đáp ứng một trong hai điều kiện sau:"
  > "Khách hàng đang có khoản nợ vay trung, dài hạn với ngân hàng;"
  > "Khách hàng có khoản tiền gửi (trừ khoản tiền gửi bắt buộc phải gửi theo yêu cầu tối thiểu) được duy trì trong tài khoản thanh toán tại ngân hàng và có phát sinh hoạt động thanh toán (trừ các hoạt động thu phí tự động của ngân hàng) trong 06 tháng gần nhất;"
  > "Phần số dư tiền gửi vượt giới hạn bảo hiểm thuộc tiền gửi kém ổn định."
  > "Đối với tiền gửi ổn định đáp ứng quy định tại khoản 2.1 Mục này, hệ số rút tiền là 5%."
  > "Hệ số rút tiền của tiền gửi bán lẻ kém ổn định là 10%."
  > — PL1.B.II.1–3 ^pl1-b2

- Nguồn vốn bán buôn không có bảo đảm: tiền gửi DNNVV đủ điều kiện (phi tài chính, tiền gửi bình quân tháng trước tại ngân hàng không quá 30 tỷ đồng) tính như bán lẻ (5%/10%); tiền gửi hoạt động 25% (chỉ phần không vượt mức yêu cầu; không xác định được phần vượt thì toàn bộ không đủ điều kiện); doanh nghiệp phi tài chính, Chính phủ, NHNN, KBNN, UBND cấp tỉnh, BHTG, BHXH, tổ chức quốc tế 40%; nguồn khác 100%.
  > "Tổng số dư tiền gửi bình quân trong tháng liền kề trước thời điểm tính tỷ lệ LCR của doanh nghiệp này tại chính ngân hàng không quá 30 tỷ đồng;"
  > "Các khoản tiền gửi hoạt động áp dụng hệ số rút tiền là 25%;"
  > "Trường hợp ngân hàng nhận tiền gửi không thể xác định số dư vượt mức yêu cầu thì toàn bộ số tiền gửi được xác định là không đủ điều kiện và không được áp dụng hệ số rút tiền 25%."
  > "Nguồn vốn theo điểm a khoản này, hệ số rút tiền là 40%."
  > "Hệ số rút tiền là 100%."
  > — PL1.B.III.2 ^pl1-b3

- Nguồn vốn bán buôn có bảo đảm (Bảng 4): bảo đảm bằng HQLA cấp 1 hoặc với NHNN 0%; HQLA cấp 2A 15%; tài sản khác với Chính phủ, KBNN, UBND, ngân hàng chính sách, VAMC, DATC, BHTG, BHXH, tổ chức quốc tế 25%; RMBS cấp 2B 25%; cấp 2B khác 50%; tài sản tài chính khác 100%.
  > "Nguồn vốn được bảo đảm bằng HQLA cấp 1 hoặc nguồn vốn được bảo đảm trong giao dịch với Ngân hàng Nhà nước"
  > "Nguồn vốn được bảo đảm bằng HQLA cấp 2A"
  > "Nguồn vốn được bảo đảm bằng các HQLA cấp 2B khác"
  > — PL1.B.III.3.2.2, Bảng 4 ^pl1-b3-3

- Dòng tiền ra bổ sung: dòng ra ròng phái sinh 100%; hạ bậc tín nhiệm tối đa 3 bậc tính 100%; thay đổi giá trị tài sản bảo đảm không phải HQLA cấp 1 tính 20%; thay đổi định giá thị trường khi có thoả thuận bù trừ tính theo dòng ký quỹ ròng lớn nhất trong 30 ngày của 24 tháng trước.
  > "Ngân hàng phải tính thêm toàn bộ (100%) vào dòng tiền ra đối với phần giá trị được yêu cầu thực hiện khi ngân hàng bị hạ tối đa 3 bậc trong xếp hạng tín nhiệm."
  > "Ngân hàng phải tính thêm 20% giá trị của tất cả tài sản bảo đảm đó vào dòng tiền ra"
  > "Tính thêm toàn bộ vào dòng tiền ra đối với giá trị tuyệt đối của dòng tiền ký quỹ ròng lớn nhất trong 30 ngày đã phát sinh trong 24 tháng liền kề trước đó;"
  > — PL1.B.IV ^pl1-b4

- Hạn mức cam kết chưa sử dụng (Bảng 5, hạn mức tín dụng / thanh khoản): cá nhân và DNNVV 5%/5%; DN phi tài chính 10%/30%; Chính phủ, NHTW, KBNN, UBND, BHTG, tổ chức quốc tế 10%/30%; TCTD 40%/40%; tổ chức tài chính khác 40%/100%; đối tượng khác 100%/100%. Nghĩa vụ giải ngân trong 30 ngày cho tổ chức tài chính 100%.
  > "Hạn mức cam kết (bao gồm hạn mức tín dụng và hạn mức thanh khoản) là các thỏa thuận không thể hủy ngang hoặc hủy ngang có điều kiện nhằm cung cấp vốn vào một thời điểm trong tương lai cho khách hàng mà khách hàng có quyền nhưng không bắt buộc phải rút vốn trong vòng 30 ngày tiếp theo."
  > "Đối với các nghĩa vụ theo thỏa thuận phải giải ngân, thanh toán trong vòng 30 ngày tiếp theo cho các tổ chức tài chính (bao gồm cả Ngân hàng Nhà nước), hệ số rút tiền là 100%."
  > — PL1.B.V.1–2, Bảng 5 ^pl1-b5

  | Đối tượng | Hạn mức tín dụng | Hạn mức thanh khoản |
  |---|---|---|
  | a) Cá nhân và DNNVV đủ điều kiện | 5% | 5% |
  | b) Doanh nghiệp không phải tổ chức tài chính | 10% | 30% |
  | c) Chính phủ, NHTW, PSE nước ngoài, KBNN, UBND cấp tỉnh, BHTG, tổ chức tài chính quốc tế | 10% | 30% |
  | d) TCTD, chi nhánh NHNNg | 40% | 40% |
  | đ) Tổ chức tài chính khác | 40% | 100% |
  | e) Đối tượng khác | 100% | 100% |

- Nghĩa vụ nợ tiềm ẩn: hạn mức cam kết huỷ ngang vô điều kiện 0%; công cụ tài trợ thương mại 3%; bảo lãnh ngân hàng, bảo lãnh dự thầu, thực hiện hợp đồng và autocallable 5%; nghĩa vụ phi hợp đồng và cam kết khác do ngân hàng xác định từ dữ liệu lịch sử; nghĩa vụ đã bị kích hoạt và phải thanh toán trong 30 ngày 100%.
  > "Đối với các nghĩa vụ quy định tại điểm a(i) và điểm a(iv) khoản 3.1 Mục này, hệ số rút tiền là 0%;"
  > "Đối với các nghĩa vụ quy định tại điểm a(ii) khoản 3.1 Mục này, hệ số rút tiền là 3%;"
  > "Đối với các nghĩa vụ quy định tại điểm a(iii) và điểm a(v) khoản 3.1 Mục này, hệ số rút tiền là 5%;"
  > "Đối với các nghĩa vụ quy định tại điểm b và điểm c khoản 3.1 Mục này, hệ số rút tiền do ngân hàng xác định dựa trên dữ liệu lịch sử đối với từng loại nghĩa vụ và sự kiện pháp lý khác có liên quan."
  > — PL1.B.V.3 ^pl1-b5-3

#### Phần C. Dòng tiền vào

- Chỉ ghi nhận dòng vào của khoản phải đòi nợ nhóm 1 và không vỡ nợ; dòng vào mang tính điều kiện (kể cả cam kết từ NHNN) không được tính; hạn mức do tổ chức khác cấp cho ngân hàng có hệ số thu tiền 0%.
  > "Khoản phải đòi không thuộc trường hợp khoản phải đòi vỡ nợ theo quy định tại Thông tư số 14/2025/TT-NHNN."
  > "Các dòng tiền vào mang tính chất điều kiện (contingent inflows) (bao gồm cả cam kết từ Ngân hàng Nhà nước hoặc đối tác khác) không được tính vào dòng tiền vào."
  > "Hạn mức tín dụng, hạn mức thanh khoản mà tổ chức khác cung cấp cho ngân hàng, hệ số thu tiền là 0%."
  > — PL1.C.I, C.III ^pl1-c1

- Reverse repo và cấp tín dụng có bảo đảm bằng tài sản tài chính đến 30 ngày (Bảng 7): tài sản cấp 1 0%; cấp 2A 15%; RMBS 25%; cấp 2B khác 50%; cho vay ký quỹ 50%; tài sản tài chính khác 100%.
  > "Giao dịch được bảo đảm hoặc sử dụng HQLA đủ tiêu chuẩn cấp 1, hệ số thu tiền là 0%."
  > "Các khoản cấp tín dụng cho khách hàng nhằm mục đích thực hiện các vị thế giao dịch có đòn bẩy (margin loans – khoản cho vay ký quỹ) cũng được coi là một hình thức khoản cấp tín dụng có bảo đảm bằng tài sản tài chính, hệ số thu tiền là 50%."
  > — PL1.C.II ^pl1-c2

- Dòng vào theo đối tác: bán lẻ và DNNVV 50%; tổ chức tài chính và NHNN 100%; DN phi tài chính, Chính phủ, KBNN, UBND, BHTG, tổ chức quốc tế và tổ chức khác 50%; chứng khoán không phải HQLA đáo hạn trong 30 ngày 100%; tiền gửi hoạt động tại tổ chức tài chính khác 0%; dư nợ hạn mức quay vòng không tính dòng vào.
  > "Các khoản phải đòi (bao gồm lãi và các khoản trả góp) từ khách hàng bán lẻ và doanh nghiệp nhỏ và vừa đủ điều kiện, hệ số thu tiền là 50%."
  > "Hệ số thu tiền là 100% đối với các tổ chức tài chính và Ngân hàng Nhà nước;"
  > "Hệ số thu tiền là 50% đối với các khách hàng bán buôn, bao gồm:"
  > "Dòng tiền vào từ chứng khoán đáo hạn trong vòng 30 ngày nhưng không thuộc danh mục HQLA đủ tiêu chuẩn, hệ số thu tiền là 100%."
  > "ngân hàng phải giả định rằng khoản cho vay trong hạn mức đó sẽ không được tính vào dòng tiền vào"
  > — PL1.C.IV ^pl1-c4

### PL2 — Hướng dẫn xác định tỷ lệ nguồn vốn ổn định ròng

#### Phần A. ASF

- Ngân hàng phân loại toàn bộ nợ phải trả và vốn chủ sở hữu để xác định hệ số ASF; giá trị theo giá trị ghi sổ, trừ nợ phái sinh NSFR (Đ25), cặp phụ thuộc (Đ26) và vốn tự có theo TT41/2016 hoặc TT14/2025.
  > "Ngân hàng thực hiện phân loại toàn bộ nợ phải trả và vốn chủ sở hữu trên báo cáo tài chính và những phần giá trị khác theo hướng dẫn tại Phụ lục này để xác định hệ số ASF."
  > "Giá trị các khoản mục thuộc vốn tự có và nợ phải trả xác định theo giá trị ghi sổ theo quy định pháp luật về kế toán, trừ các trường hợp sau:"
  > — PL2.A.I.1–2 ^pl2-a1

- Bảng hệ số ASF (Bảng 9, trích các dòng chính; cột: không kỳ hạn / < 6 tháng / 6 tháng – < 1 năm / ≥ 1 năm / không xác định kỳ hạn). Nguồn huy động được phân loại theo thứ tự từ trên xuống. Tiền gửi bán lẻ có kỳ hạn được rút trước hạn (không thuộc điểm a(iii) khoản 4 Mục I Phần B PL I) nhận 95% (ổn định) hoặc 90% (kém ổn định) kể cả khi kỳ hạn từ 1 năm trở lên.
  > "Nguồn huy động được phân loại theo thứ tự từ trên xuống dưới"
  > "Tiền gửi có kỳ hạn, được rút trước hạn không thuộc trường hợp tại khoản 9.1.1 Bảng này."
  > "Nguồn huy động từ các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài"
  > — PL2.A.II, Bảng 9 ^pl2-a2

  | Khoản | Phân loại | Không kỳ hạn | < 6T | 6T – < 1N | ≥ 1N | Không XĐ |
  |---|---|---|---|---|---|---|
  | 1.1 | Vốn cấp 1 (theo TT14/2025 hoặc TT41/2016, sau các khoản trừ nêu trong bảng) | 100% | | | | |
  | 1.2 | Vốn cấp 2 (sau các khoản trừ nêu trong bảng) | | 0% | 50% | 100% | 100% |
  | 1.3 | Công cụ vốn chủ sở hữu khác | 0% | 0% | 50% | 100% | 100% |
  | 3 | Chênh lệch dương nợ phái sinh NSFR − tài sản phái sinh NSFR | 0% | | | | |
  | 6 | Huy động từ phát hành trái phiếu | | 0% | 50% | 100% | |
  | 7.1–7.2 | Chính phủ, KBNN, UBND cấp tỉnh, BHTG, BHXH…: tiền gửi hoạt động / không phải hoạt động | 50% | 50% | 50% | 100% | |
  | 8.1 | NHNN, NHTW nước ngoài: tiền gửi hoạt động | 50% | 50% | 50% | 100% | |
  | 8.2–8.3 | NHNN, NHTW nước ngoài: tiền gửi không phải hoạt động / nguồn khác | 0% | 0% | 50% | 100% | |
  | 9.1.1 | Bán lẻ ổn định, có kỳ hạn không được rút trước hạn (hoặc thuộc điểm a(iii)) | | 95% | 95% | 100% | |
  | 9.1.2 | Bán lẻ ổn định, có kỳ hạn được rút trước hạn | | 95% | 95% | 95% | |
  | 9.1.3 | Bán lẻ ổn định, không kỳ hạn | 95% | | | | |
  | 9.2.1 | Bán lẻ kém ổn định, có kỳ hạn không được rút trước hạn (hoặc thuộc điểm a(iii)) | | 90% | 90% | 100% | |
  | 9.2.2 | Bán lẻ kém ổn định, có kỳ hạn được rút trước hạn | | 90% | 90% | 90% | |
  | 9.2.3 | Bán lẻ kém ổn định, không kỳ hạn | 90% | | | | |
  | 9.3 | Bán lẻ: vốn vay và nợ phải trả khác | | 0% | 50% | 100% | |
  | 10 | DNNVV đủ điều kiện: cùng hệ số như bán lẻ (95%/90%; vay khác 0/50/100%) | | | | | |
  | 11.1 | Tổ chức tài chính: tiền gửi hoạt động | 50% | 50% | 50% | 100% | |
  | 11.2 | TCTD, chi nhánh NHNNg | 0% | 0% | 50% | 100% | |
  | 11.3 | Tổ chức tài chính khác | 0% | 0% | 50% | 100% | |
  | 12.1–12.2 | DN phi tài chính: tiền gửi hoạt động / không phải hoạt động | 50% | 50% | 50% | 100% | |
  | 12.3 | DN phi tài chính: nguồn khác | | 50% | 50% | 100% | |
  | 13.2–13.3 | Tổ chức khác: tiền gửi không phải hoạt động / nguồn khác | 0% | 0% | 50% | 100% | |
  | 14.2 | Nợ và vốn khác không xác định được kỳ hạn (gồm short positions) | | | | | 0% |

#### Phần B. RSF

- Ngân hàng phân loại toàn bộ tài sản, cam kết ngoại bảng để xác định hệ số RSF; giá trị theo giá trị ghi sổ sau dự phòng cụ thể; cam kết ngoại bảng tính phần hạn mức chưa sử dụng; khoản phải đòi vỡ nợ xác định theo TT14/2025.
  > "Ngân hàng thực hiện phân loại toàn bộ tài sản trên báo cáo tài chính, cam kết ngoại bảng và những phần giá trị khác theo hướng dẫn tại Phụ lục này để xác định hệ số RSF."
  > "Giá trị khoản cam kết ngoại bảng là phần giá trị hạn mức cam kết chưa sử dụng theo hướng dẫn tại Phụ lục này."
  > "Ngân hàng phải xác định khoản phải đòi vỡ nợ theo quy định tại Thông tư số 14/2025/TT-NHNN"
  > — PL2.B.I.1–3 ^pl2-b1

- Bảng hệ số RSF (Bảng 10, trích các dòng chính). Tài sản từ khoản A.4 đến A.20 là tài sản không bị ràng buộc. Ngoài tài sản, RSF tính thêm 10% tổng nợ phái sinh (trước khi trừ ký quỹ biến động đã nộp) với hệ số 100%.
  > "Tài sản trên báo cáo tình hình tài chính, trong đó tất cả các tài sản từ Khoản A.4 đến A.20 của Bảng này là tài sản không bị ràng buộc."
  > "10% của tổng giá trị nợ phái sinh quy định tại khoản 1 Điều 25 Thông tư này (tổng giá trị trước khi trừ đi ký quỹ biến động đã nộp)."
  > "Tiền gửi dự trữ bắt buộc (bao gồm cả phần tiền gửi vượt dự trữ bắt buộc) tại Ngân hàng Nhà nước"
  > — PL2.B.II, Bảng 10 ^pl2-b2

  | Khoản | Phân loại | Không kỳ hạn | < 6T | 6T – < 1N | ≥ 1N | Không XĐ |
  |---|---|---|---|---|---|---|
  | A.1 | Khoản phải đòi vỡ nợ | 100% | | | | |
  | A.2 | Tài sản ký quỹ ban đầu cho phái sinh | 85% hoặc 100% | 85% hoặc 100% | 85% hoặc 100% | 100% | 100% |
  | A.3 | Tài sản bị ràng buộc | Theo Đ24.4.c | | 50% hoặc cao hơn (Đ24.4.b(ii)) | 100% | 100% |
  | A.4 | Tài sản thuộc cặp phụ thuộc (Đ26) | 0% | 0% | 0% | 0% | |
  | A.5 | Chênh lệch dương tài sản phái sinh NSFR − nợ phái sinh NSFR | 100% | | | | |
  | A.8.1 | Tiền mặt | 0% | | | | |
  | A.8.2 | Tiền gửi dự trữ bắt buộc (cả phần vượt) tại NHNN | 0% | | | | |
  | A.8.3 | HQLA do NHNN phát hành, thời hạn còn lại < 6 tháng | 0% | 0% | | | |
  | A.8.4 | HQLA cấp 1 khác | | 5% | 5% | 5% | 5% |
  | A.8.5 | HQLA cấp 2A | | 15% | 15% | 15% | 15% |
  | A.8.6 | HQLA cấp 2B | | 50% | 50% | 50% | 50% |
  | A.9 | Phải đòi Chính phủ, KBNN, UBND cấp tỉnh, BHTG, BHXH… | | 50% | 50% | 65% | |
  | A.10.1 | Phải đòi NHNN | 0% | 0% | 50% | 65% | |
  | A.11.1 | Cổ phiếu niêm yết | | | | | 85% |
  | A.11.2 | Trái phiếu niêm yết | | 50% | 50% | 85% | |
  | A.11.3 | Chứng khoán khác | | 50% | 50% | 100% | 100% |
  | A.12 | Hàng hoá giao dịch trên sàn, gồm vàng | | | | | 85% |
  | A.13 | Tài sản cố định | | | | | 100% |
  | A.14.1 | Cấp tín dụng cho tổ chức tài chính, bảo đảm bằng HQLA cấp 1 và được tái thế chấp | | 10% | 50% | 100% | |
  | A.14.2 | Cấp tín dụng khác cho tổ chức tài chính | | 15% | 50% | 100% | |
  | A.15.1 | Tiền gửi hoạt động tại TCTD khác | 50% | 50% | 50% | 100% | |
  | A.15.2 | Tiền gửi tại TCTD, chi nhánh NHNNg khác, TCTD nước ngoài | 15% | 15% | 50% | 100% | |
  | A.16.2.1 / A.17.1 | Phải đòi thế chấp nhà ở RW ≤ 35% | | 50% | 50% | 65% | |
  | A.16.2.2 / A.17.2 | Bất động sản khác RW > 35% | | 50% | 50% | 85% | |
  | A.16.1 | Phải đòi bất động sản không đủ tiêu chuẩn (TT14/2025) | | 50% | 50% | 100% | |
  | A.18.x.1 | Cấp tín dụng bán lẻ, DNNVV, DN phi tài chính, tổ chức khác: RW ≤ 35% | | 50% | 50% | 65% | |
  | A.18.x.2 | Như trên: RW > 35% | | 50% | 50% | 85% | |
  | A.19 | Tài sản khác xác định được kỳ hạn | | 50% | 50% | 100% | |
  | A.20 | Tài sản khác không xác định được kỳ hạn | | | | | 100% |
  | B.1 | 10% tổng nợ phái sinh (trước khi trừ ký quỹ biến động đã nộp) | 100% | | | | |
  | C.1 | Hạn mức cam kết, nghĩa vụ giải ngân (khoản 1, 2, 3.3 Mục V Phần B PL I) | 5% | | | | |
  | C.2 | Nghĩa vụ nợ tiềm ẩn khác (khoản 3.2 Mục V Phần B PL I) | 0% | | | | |

### PL4 — Nội dung công bố thông tin về các tỷ lệ thanh khoản

- Công bố tối thiểu gồm: tóm tắt chính sách quản lý rủi ro thanh khoản (chiến lược, nguyên tắc, khẩu vị rủi ro thanh khoản), khái niệm quan trọng, cấu trúc nguồn vốn và tài sản, biện pháp kiểm soát; và cơ cấu tổ chức quản lý rủi ro thanh khoản, cách quản lý tập trung hay phân tán.
  > "Tóm tắt chính sách quản lý rủi ro thanh khoản, trong đó bao gồm chiến lược, nguyên tắc quản lý rủi ro, khẩu vị rủi ro thanh khoản;"
  > "Cấu trúc nguồn vốn và tài sản của ngân hàng;"
  > "Biện pháp kiểm soát rủi ro thanh khoản."
  > "Thông tin tổng quan về cơ cấu tổ chức quản lý rủi ro thanh khoản, bao gồm cả thông tin về các bộ phận thực hiện quản lý rủi ro thanh khoản của ngân hàng; cách thức quản lý rủi ro thanh khoản (tập trung hay phân tán)."
  > — PL4.1–4.2 ^pl4-1

- Nội dung định lượng: LCR riêng lẻ, NSFR riêng lẻ, LDR, và LEV riêng lẻ khi Thống đốc quyết định áp dụng; thông tin khác theo quy định nội bộ và trên cơ sở hướng dẫn công bố thông tin của Uỷ ban Basel.
  > "Tỷ lệ LCR riêng lẻ;"
  > "Tỷ lệ NSFR riêng lẻ;"
  > "Tỷ lệ LDR;"
  > "Tỷ lệ LEV riêng lẻ trong trường hợp Thống đốc Ngân hàng Nhà nước quyết định áp dụng."
  > "Thông tin khác (nếu có) theo quy định nội bộ của ngân hàng và trên cơ sở hướng dẫn công bố thông tin của Ủy ban Basel."
  > — PL4.3–4.4 ^pl4-3

### C3 — Tổ chức thực hiện (chỉ Đ37.1–37.2; unit chưa ingest trọn)

- Thông tư có hiệu lực từ 01/10/2026, trừ Đ37.2: NHTM đang thực hiện Đ23.3 TT41/2016 tuân thủ các tỷ lệ của TT22/2019 và không phải tuân thủ Mục 4, Mục 5 TT50 cho đến khi kết thúc việc thực hiện đó. Thông tư sửa đổi, bổ sung một số điều của TT22/2019.
  > "Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 10 năm 2026, trừ trường hợp quy định tại khoản 2 Điều này."
  > "không phải tuân thủ quy định tại Mục 4, Mục 5 Thông tư này cho đến khi kết thúc việc thực hiện quy định tại khoản 3 Điều 23 Thông tư số 41/2016/TT-NHNN."
  > "Sửa đổi, bổ sung một số điều của Thông tư số 22/2019/TT-NHNN như sau:"
  > — Đ37.1–3 ^d37-1

- Đ37.3.a sửa Điều 2 TT22/2019: đối tượng áp dụng của TT22 chỉ còn ngân hàng hợp tác xã và NHTM đang thực hiện Đ23.3 TT41/2016.
  > "Sửa đổi, bổ sung Điều 2 như sau:"
  > "Ngân hàng hợp tác xã;"
  > "Ngân hàng thương mại đang trong thời gian thực hiện quy định tại khoản 3 Điều 23 Thông tư số 41/2016/TT-NHNN"
  > — Đ37.3.a ^d37-3a

## Node bị ảnh hưởng
- Tạo: [[tt50-2026]].
- Cập nhật: [[lcr]], [[nsfr]], [[hqla]], [[net-cash-outflows]], [[available-stable-funding]], [[required-stable-funding]], [[lcr-by-currency]], [[loan-to-deposit-ratio]], [[intraday-liquidity-risk]], [[contingency-funding-plan]], [[liquidity-stress-testing]].
- C1, PL4 [2026-10-20]: cập nhật [[tt50-2026]] (Đ1.2, Đ1.5, Đ4.3–4.4, Đ5, định nghĩa Đ3, PL4), [[asset-encumbrance]] (Đ3.17), [[committed-facilities]] (Đ3.5–3.7).

## Mâu thuẫn ghi nhận
- Không có mâu thuẫn cùng phạm vi. Khác Basel (khác jurisdiction): LCR VN có lộ trình 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; LCR áp dụng riêng lẻ, LCR hợp nhất do ngân hàng tự quản lý (Basel: hợp nhất).

## Ghi chú convert
- Công thức LCR, NSFR, ASF, RSF trong raw ở dạng `$$…$$` đọc được. Bảng 1 và Bảng 2 có `<br>` trong ô; khi chép bảng đã gộp dòng.
