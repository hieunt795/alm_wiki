---
title: "Thông tư 83/2025/TT-NHNN — Hệ thống kiểm soát nội bộ của NHTM, CN NHNNg"
aliases: []
type: source
source_id: src-tt83-2025-nhnn
domains: [vn-reg, alm]
status: active
maturity: draft
tier: T1
doc_status: final
issuer: SBV
published: 2025-12-31
effective: 2026-07-01
raw: 01_sources/alm/TT83_2025_SBV/TT83_2025_SBV.md
units_done: [C1, C3-M1, C3-M5, C3-M7, C3-M8, C3-M9, PL2, PL5, PL6]
updated: 2026-10-19
---

## Thông tin nguồn
- Issuer: Ngân hàng Nhà nước Việt Nam (NHNN), Thống đốc ban hành; số 83/2025/TT-NHNN, ký ngày 31/12/2025.
- Tier T1, `doc_status: final`.
- Hiệu lực: 01/07/2026, với lộ trình riêng cho IRRBB tới 01/01/2028 (Đ74.4). Bãi bỏ TT13/2018, TT40/2018 và Điều 3 TT09/2024 (Đ74.6).
- Raw: `01_sources/alm/TT83_2025_SBV/TT83_2025_SBV.md` (2.867 dòng); bản gốc pdf và docx cùng thư mục.
- Conversion: ok (xem `03_meta/sources.yaml`).
- Node regulation tương ứng: [[tt83-2025]].
- Đã ingest: C1 (Đ1–10), C3-M1 (Đ17–25), C3-M5 (Đ45–49), C3-M7 (Đ53–55), C3-M8 (Đ56–58), C3-M9 (Đ59–63), PL2, PL5, PL6. Đ74 thuộc C5 được đọc riêng để lấy hiệu lực và lộ trình; C5 chưa mark done.

## Tóm tắt
- Chương III Mục 7 (Đ53–55) quy định quản lý rủi ro lãi suất trên sổ ngân hàng: chiến lược, hạn mức, nhận dạng, đo lường, theo dõi, kiểm soát và báo cáo nội bộ.
- Chiến lược phải dùng tối thiểu trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile), ΔNII và ΔEVE. Hạn mức phải có cho cả ΔNII và ΔEVE.
- Phụ lục V hướng dẫn đo lường ΔEVE theo 5 bước (phân nhóm, phân bổ 19 thang kỳ hạn, tính EVE theo 6 kịch bản, KAO, tổng hợp) và ΔNII 1 năm theo 2 kịch bản song song.
- Cấu trúc Phụ lục V bám theo Section IV BCBS d368. Bảng 1, Bảng 2, Bảng 3, Bảng 4 và Bảng 5 có cùng giá trị với Table 1, Table 2, multiplier và Annex 2 Table 1 của d368.
- Lộ trình: từ 01/07/2026 đến 31/12/2027 ngân hàng được dùng ΔNII hoặc ΔEVE; chậm nhất từ 01/01/2028 phải dùng cả hai.

## Key claims

### C1 — Quy định chung (Đ1–10)

- Thông tư quy định hệ thống kiểm soát nội bộ của ngân hàng thương mại và chi nhánh ngân hàng nước ngoài; ngân hàng thương mại được kiểm soát đặc biệt không phải tuân thủ Mục 9 Chương III (đánh giá nội bộ về mức đủ vốn).
  > "1. Thông tư này quy định về hệ thống kiểm soát nội bộ của ngân hàng thương mại, chi nhánh ngân hàng nước ngoài (sau đây gọi tắt là ngân hàng)."
  > "2. Ngân hàng thương mại được kiểm soát đặc biệt không phải tuân thủ quy định tại Mục 9 Chương III Thông tư này."
  > — Đ1 ^d1-1

- Vốn kinh tế là mức vốn ngân hàng tự xác định để bù đắp các rủi ro trọng yếu và bảo đảm tỷ lệ an toàn vốn trong kịch bản bất lợi. Đánh giá nội bộ về mức đủ vốn là việc ngân hàng tự đánh giá mức đủ vốn bảo đảm tuân thủ quy định NHNN về tỷ lệ an toàn vốn và Thông tư này.
  > "Đánh giá nội bộ về mức đủ vốn là việc ngân hàng tự đánh giá mức đủ vốn đảm bảo tuân thủ quy định của Ngân hàng Nhà nước Việt Nam (sau đây gọi tắt là Ngân hàng Nhà nước) về tỷ lệ an toàn vốn và quy định tại Thông tư này."
  > "Vốn kinh tế là mức vốn do ngân hàng tự xác định trên cơ sở tính toán mức vốn cần thiết để bù đắp các rủi ro trọng yếu và đảm bảo tỷ lệ an toàn vốn trong kịch bản có diễn biến bất lợi."
  > — Đ3.6–7 ^d3-7

- Kiểm tra sức chịu đựng là công cụ quản lý rủi ro mang tính dự báo, đánh giá tác động tiềm ẩn của biến động bất lợi để xác định khả năng chịu đựng rủi ro của ngân hàng.
  > "Kiểm tra sức chịu đựng là công cụ quản lý rủi ro mang tính dự báo để đánh giá tác động tiềm ẩn của biến động, thay đổi bất lợi, qua đó xác định khả năng chịu đựng rủi ro của ngân hàng."
  > — Đ3.8 ^d3-8

- Rủi ro là khả năng xảy ra tổn thất (tài chính, phi tài chính) hoặc kết quả bất lợi ảnh hưởng tiêu cực tới thu nhập, vốn, thanh khoản; gồm rủi ro tín dụng, thị trường, hoạt động, thanh khoản, tập trung, IRRBB, mô hình, danh tiếng, chiến lược và rủi ro khác.
  > "Rủi ro là khả năng xảy ra tổn thất (tổn thất tài chính, tổn thất phi tài chính) hoặc khả năng xảy ra kết quả bất lợi có thể ảnh hưởng tiêu cực đến thu nhập, vốn, thanh khoản của ngân hàng."
  > — Đ3.9 ^d3-9

- Khẩu vị rủi ro là mức độ rủi ro ngân hàng sẵn sàng chấp nhận khi thực hiện chiến lược kinh doanh, thể hiện bằng các tỷ lệ và chỉ tiêu tại Đ19.2.a.
  > "Khẩu vị rủi ro là mức độ rủi ro mà ngân hàng sẵn sàng chấp nhận trong quá trình thực hiện chiến lược kinh doanh được thể hiện bằng các tỷ lệ và chỉ tiêu quy định tại điểm a khoản 2 Điều 19 Thông tư này."
  > — Đ3.10 ^d3-10

- Trạng thái rủi ro là mức độ rủi ro tại một thời điểm, thể hiện qua giá trị sau khi quy đổi theo rủi ro của tài sản có, nợ phải trả, khoản mục ngoại bảng có rủi ro.
  > "Trạng thái rủi ro là mức độ rủi ro của ngân hàng tại một thời điểm thể hiện thông qua giá trị sau khi đã được quy đổi theo rủi ro của tài sản có rủi ro, nợ phải trả có rủi ro, khoản mục ngoại bảng có rủi ro."
  > — Đ3.11 ^d3-11

- Rủi ro trọng yếu gồm: (a) rủi ro tín dụng, thị trường, hoạt động, thanh khoản, tập trung, IRRBB; (b) rủi ro khác theo quy định nội bộ.
  > "Rủi ro trọng yếu bao gồm:"
  > "a) Rủi ro tín dụng, rủi ro thị trường, rủi ro hoạt động, rủi ro thanh khoản, rủi ro tập trung, rủi ro lãi suất trên sổ ngân hàng;"
  > "b) Rủi ro khác theo quy định nội bộ của ngân hàng."
  > — Đ3.13 ^d3-13

- Rủi ro lãi suất (thuộc rủi ro thị trường) là rủi ro do lãi suất biến động bất lợi tác động tới giá trị giấy tờ có giá, công cụ tài chính có lãi suất, phái sinh lãi suất trên sổ kinh doanh.
  > "a) Rủi ro lãi suất là rủi ro do biến động bất lợi của lãi suất trên thị trường đối với giá trị của giấy tờ có giá, công cụ tài chính có lãi suất, sản phẩm phái sinh lãi suất trên sổ kinh doanh của ngân hàng;"
  > — Đ3.15.a ^d3-15a

- Rủi ro thanh khoản là rủi ro do ngân hàng không có khả năng thực hiện nghĩa vụ tài chính khi đến hạn, hoặc có khả năng nhưng phải trả chi phí cao hơn mức bình quân của thị trường theo quy định nội bộ.
  > "a) Ngân hàng không có khả năng thực hiện nghĩa vụ tài chính khi đến hạn;"
  > "b) Ngân hàng có khả năng thực hiện nghĩa vụ tài chính khi đến hạn nhưng phải trả chi phí cao hơn mức chi phí bình quân của thị trường theo quy định nội bộ của ngân hàng."
  > — Đ3.20 ^d3-20

- Rủi ro tập trung là rủi ro do hoạt động kinh doanh tập trung vào một khách hàng, một khách hàng và người có liên quan, hoặc một số khách hàng, đối tác, sản phẩm, giao dịch, ngành kinh tế ở mức tác động đáng kể tới thu nhập, trạng thái rủi ro.
  > "Rủi ro tập trung là rủi ro do ngân hàng có hoạt động kinh doanh tập trung vào một khách hàng; một khách hàng và người có liên quan; một hoặc một số khách hàng, đối tác, sản phẩm, giao dịch, ngành kinh tế ở mức độ có tác động đáng kể theo quy định nội bộ của ngân hàng đến thu nhập, trạng thái rủi ro của ngân hàng."
  > — Đ3.21 ^d3-21

- IRRBB là rủi ro do lãi suất biến động bất lợi tác động tới trạng thái sổ ngân hàng, ảnh hưởng tới vốn và thu nhập; gồm: rủi ro chênh lệch (gap risk) do không khớp thời điểm định giá lại hoặc kỳ hạn giữa tài sản và nợ (kể cả ngoại bảng); rủi ro cơ sở (basis risk) do khác nhau giữa lãi suất dùng để định giá lại tài sản và nợ cùng kỳ hạn; rủi ro quyền chọn (option risk), gồm quyền chọn tự động (chắc chắn thực hiện theo hợp đồng khi lãi suất thay đổi) và quyền lựa chọn hành vi (lãi suất thay đổi có thể làm thay đổi hành vi khách hàng).
  > "Rủi ro lãi suất trên sổ ngân hàng là rủi ro do biến động bất lợi của lãi suất tác động tới trạng thái sổ ngân hàng, làm ảnh hưởng tới vốn và thu nhập của ngân hàng."
  > "phát sinh từ sự không khớp về thời điểm định giá lại lãi suất hoặc không khớp về kỳ hạn giữa tài sản và nợ phải trả (bao gồm cả các khoản mục ngoại bảng) trên sổ ngân hàng;"
  > "phát sinh từ sự khác nhau giữa lãi suất được sử dụng để định giá lại tài sản và nợ phải trả (bao gồm cả các khoản mục ngoại bảng) có cùng kỳ hạn;"
  > "phát sinh từ việc thực hiện quyền chọn tự động hoặc quyền lựa chọn hành vi gắn với tài sản và nợ phải trả (bao gồm cả khoản mục ngoại bảng) trên sổ ngân hàng làm thay đổi giá trị và thời điểm phát sinh dòng tiền, bao gồm:"
  > "phát sinh khi lãi suất thay đổi dẫn đến việc chắc chắn thực hiện quyền chọn theo quy định tại hợp đồng;"
  > "phát sinh khi lãi suất thay đổi có thể làm thay đổi hành vi của khách hàng."
  > — Đ3.22 ^d3-22

- Mô hình là phương pháp, hệ thống, cách tiếp cận định lượng (dùng giả định, kỹ thuật toán, thống kê, kinh tế, tài chính, ý kiến chuyên gia) xử lý dữ liệu đầu vào thành kết quả đầu ra. Rủi ro mô hình là rủi ro do lỗi mô hình khi xây dựng, triển khai hoặc do dùng mô hình không phù hợp. Vòng đời mô hình gồm tối thiểu: xây dựng, triển khai, sử dụng, theo dõi giám sát, kiểm định.
  > "Mô hình là phương pháp, hệ thống, cách thức tiếp cận định lượng (trong đó sử dụng các giả định, kỹ thuật, lý thuyết về toán học, thống kê, kinh tế, tài chính, ý kiến chuyên gia) để xử lý dữ liệu đầu vào thành kết quả đầu ra sử dụng trong hoạt động của ngân hàng."
  > "Rủi ro mô hình là rủi ro do lỗi mô hình (model errors) trong giai đoạn xây dựng mô hình, triển khai mô hình hoặc do sử dụng mô hình không phù hợp."
  > "Vòng đời mô hình bao gồm tối thiểu các giai đoạn sau:"
  > "đ) Kiểm định mô hình."
  > — Đ3.23–25 ^d3-24

- Sổ kinh doanh ghi nhận trạng thái của: giao dịch tự doanh; giao dịch bảo lãnh phát hành công cụ tài chính; phái sinh phòng ngừa rủi ro cho giao dịch tự doanh; giao dịch mua bán ngoại tệ, vàng, tài sản tài chính phục vụ nhu cầu khách hàng, đối tác và giao dịch đối ứng. Giao dịch tự doanh là giao dịch mua, bán, trao đổi với mục đích trong thời hạn không quá một năm để thu lợi từ chênh lệch giá.
  > "Sổ kinh doanh là danh mục ghi nhận các trạng thái của:"
  > "a) Giao dịch tự doanh;"
  > "b) Giao dịch để thực hiện nghiệp vụ bảo lãnh phát hành công cụ tài chính;"
  > "c) Giao dịch sản phẩm phái sinh để phòng ngừa rủi ro của các giao dịch tự doanh của ngân hàng;"
  > "d) Giao dịch mua bán ngoại tệ, vàng, tài sản tài chính để phục vụ nhu cầu của khách hàng, đối tác và các giao dịch để đối ứng với các giao dịch này."
  > "với mục đích mua, bán, trao đổi trong thời hạn không quá một năm để thu lợi từ chênh lệch giá thị trường cho ngân hàng đối với các công cụ tài chính, bao gồm:"
  > — Đ3.32, Đ3.34 ^d3-32

- Sổ ngân hàng ghi nhận trạng thái của: repo và reverse repo; phái sinh phòng ngừa rủi ro cho các khoản mục của báo cáo tình hình tài chính (kể cả ngoại bảng), trừ giao dịch đã vào sổ kinh doanh; giao dịch mua bán tài sản tài chính với mục đích dự trữ khả năng thanh khoản; các giao dịch còn lại không thuộc sổ kinh doanh.
  > "Sổ ngân hàng là danh mục ghi nhận trạng thái của:"
  > "a) Giao dịch mua lại (repo) và giao dịch mua lại đảo ngược (reso);"
  > "b) Giao dịch sản phẩm phái sinh để phòng ngừa rủi ro cho các khoản mục của Báo cáo tình hình tài chính (bao gồm cả các khoản mục ngoại bảng) của ngân hàng, trừ các giao dịch đã phân loại vào sổ kinh doanh của ngân hàng quy định tại điểm a và điểm c khoản 32 Điều này;"
  > "c) Giao dịch mua bán tài sản tài chính với mục đích dự trữ khả năng thanh khoản;"
  > "d) Các giao dịch còn lại không thuộc sổ kinh doanh của ngân hàng."
  > — Đ3.33 ^d3-33

- Hệ thống kiểm soát nội bộ phải có 3 tuyến bảo vệ độc lập: tuyến 1 là bộ phận tạo ra rủi ro (tạo doanh thu, thực hiện quyết định có rủi ro, phân bổ hạn mức theo hoạt động), có chức năng nhận dạng, kiểm soát, theo dõi, giảm thiểu rủi ro; tuyến 2 gồm tối thiểu bộ phận tuân thủ và bộ phận quản lý rủi ro, có chức năng xây dựng chính sách, quy định nội bộ về quản lý rủi ro, đo lường, theo dõi, kiểm soát rủi ro toàn ngân hàng và tuân thủ pháp luật; tuyến 3 là kiểm toán nội bộ. Rủi ro mô hình có 3 tuyến bảo vệ riêng theo Đ56.7.
  > "2. Hệ thống kiểm soát nội bộ của ngân hàng phải có 03 tuyến bảo vệ độc lập như sau:"
  > "a) Tuyến bảo vệ thứ nhất là các bộ phận tạo ra rủi ro gồm bộ phận tạo ra doanh thu, thực hiện các quyết định có rủi ro, thực hiện phân bổ hạn mức rủi ro theo từng hoạt động kinh doanh, hoạt động nghiệp vụ cụ thể; và bộ phận tạo ra rủi ro khác. Tuyến bảo vệ thứ nhất có chức năng nhận dạng, thực hiện các biện pháp kiểm soát, theo dõi, giảm thiểu rủi ro;"
  > "b) Tuyến bảo vệ thứ hai gồm tối thiểu Bộ phận tuân thủ và Bộ phận quản lý rủi ro. Tuyến bảo vệ thứ hai có chức năng xây dựng chính sách quản lý rủi ro, quy định nội bộ về quản lý rủi ro; đo lường, theo dõi, kiểm soát rủi ro toàn ngân hàng và tuân thủ quy định của pháp luật;"
  > "c) Tuyến bảo vệ thứ ba có chức năng kiểm toán nội bộ do bộ phận kiểm toán nội bộ thực hiện theo quy định tại Luật Các tổ chức tín dụng và Thông tư này;"
  > "d) Đối với việc quản lý rủi ro mô hình, ngân hàng có 03 tuyến bảo vệ độc lập theo quy định tại khoản 7 Điều 56 Thông tư này."
  > — Đ4.2 ^d4-2

- Phân cấp thẩm quyền quyết định căn cứ mức độ tin cậy của cấp có thẩm quyền và năng lực người thực hiện, thể hiện bằng tiêu chí quy mô, mức độ phức tạp giao dịch, hạn mức rủi ro; phải phân tách chức năng nhằm ngăn ngừa xung đột lợi ích, không cá nhân nào chi phối toàn bộ một giao dịch hoặc quy trình; có kiểm soát trước, trong và sau giao dịch.
  > "b) Việc phân cấp thẩm quyền quyết định phải căn cứ mức độ tin cậy của cấp có thẩm quyền và năng lực của cá nhân, bộ phận thực hiện. Thẩm quyền quyết định phải được thể hiện bằng tiêu chí về quy mô, mức độ phức tạp của giao dịch, hạn mức rủi ro, các giới hạn, tiêu chí khác theo quy định nội bộ của ngân hàng;"
  > "(iv) Phân tách rõ ràng chức năng và nhiệm vụ trong các giao dịch, quy trình nghiệp vụ nhằm ngăn ngừa, kiểm soát xung đột lợi ích; bảo đảm không có cá nhân nào chi phối toàn bộ một giao dịch hoặc quy trình nghiệp vụ; không giao đồng thời cho một cá nhân các nhiệm vụ có khả năng phát sinh xung đột lợi ích; có nguyên tắc kiểm soát trước, trong và sau khi thực hiện giao dịch, quy trình nghiệp vụ;"
  > — Đ5.1.b–c ^d5-1

- Quy định nội bộ về báo cáo nội bộ phải có: thời điểm lấy số liệu; thời điểm hoàn thành; cá nhân, bộ phận lập, phê duyệt, nhận báo cáo; trách nhiệm xử lý đề xuất, kiến nghị.
  > "k) Quy định nội bộ về báo cáo nội bộ đảm bảo có các nội dung về: thời điểm lấy số liệu để lập báo cáo; thời điểm hoàn thành báo cáo; cá nhân, bộ phận lập, phê duyệt, nhận báo cáo; trách nhiệm xử lý đối với đề xuất, kiến nghị trong báo cáo (nếu có)."
  > — Đ5.1.k ^d5-1k

- HĐQT, HĐTV phải thành lập các ủy ban theo Luật Các TCTD; Ủy ban quản lý rủi ro và Ủy ban nhân sự phải có trên một nửa số thành viên có quyền biểu quyết không phải người điều hành.
  > "a) Hội đồng quản trị, Hội đồng thành viên phải thành lập các ủy ban theo quy định tại khoản 5 Điều 50 Luật Các tổ chức tín dụng. Cơ cấu tổ chức, chức năng, nhiệm vụ của Ủy ban quản lý rủi ro, Ủy ban nhân sự thực hiện theo quy định của Ngân hàng Nhà nước và phải đảm bảo mỗi ủy ban có ít nhất trên một phần hai (1/2) số thành viên có quyền biểu quyết không phải là người điều hành."
  > — Đ6.2.a ^d6-2a

- Hội đồng rủi ro giúp việc Tổng giám đốc: đề xuất, tham mưu về quản lý rủi ro (Đ25.5.a) và theo dõi trạng thái rủi ro so với hạn mức (Đ25.5.b); Chủ tịch là người điều hành chuyên trách quản lý rủi ro tại trụ sở chính (không phải Tổng giám đốc); họp định kỳ tối thiểu mỗi quý 1 lần và đột xuất.
  > "a) Hội đồng rủi ro có nhiệm vụ đề xuất, tham mưu Tổng giám đốc (Giám đốc) về nội dung quản lý rủi ro quy định tại điểm a khoản 5 Điều 25 Thông tư này; thực hiện nội dung quy định tại điểm b khoản 5 Điều 25 Thông tư này."
  > "Hội đồng rủi ro gồm: Chủ tịch là người điều hành chuyên trách về quản lý rủi ro tại trụ sở chính (không phải là Tổng giám đốc (Giám đốc)), có kinh nghiệm, hiểu biết, trình độ chuyên môn về quản lý rủi ro và thành viên khác thuộc các bộ phận có liên quan theo quy định nội bộ của ngân hàng thương mại."
  > "Tổng giám đốc (Giám đốc) quyết định quy chế làm việc của Hội đồng rủi ro, tối thiểu bao gồm chức năng, nhiệm vụ, cơ chế ra quyết định, cơ chế họp (họp định kỳ tối thiểu mỗi quý 01 lần, họp đột xuất);"
  > — Đ6.4.a ^d6-4a

- Hội đồng ALCO đề xuất, tham mưu Tổng giám đốc về nội dung quản lý tài sản/nợ phải trả tại Đ25.3; Chủ tịch là Tổng giám đốc hoặc người điều hành khác tại trụ sở chính; Tổng giám đốc quyết định quy chế làm việc (chức năng, nhiệm vụ, cơ chế ra quyết định, cơ chế họp); họp định kỳ tối thiểu mỗi quý 1 lần và đột xuất.
  > "b) Hội đồng quản lý Tài sản/Nợ phải trả (Hội đồng ALCO) có nhiệm vụ đề xuất, tham mưu Tổng giám đốc (Giám đốc) về nội dung quản lý Tài sản/Nợ phải trả quy định tại khoản 3 Điều 25 Thông tư này."
  > "Hội đồng ALCO gồm: Chủ tịch là Tổng giám đốc (Giám đốc) hoặc người điều hành khác tại trụ sở chính và thành viên khác thuộc các bộ phận có liên quan theo quy định nội bộ của ngân hàng thương mại."
  > "Tổng giám đốc (Giám đốc) quyết định quy chế làm việc của Hội đồng ALCO, tối thiểu bao gồm chức năng, nhiệm vụ, cơ chế ra quyết định, cơ chế họp (họp định kỳ tối thiểu mỗi quý 01 lần, họp đột xuất);"
  > — Đ6.4.b ^d6-4b

- Hội đồng quản lý vốn đề xuất, tham mưu Tổng giám đốc về đánh giá nội bộ mức đủ vốn (Đ25.4); Chủ tịch là Tổng giám đốc hoặc người điều hành chuyên trách tài chính tại trụ sở chính; họp định kỳ tối thiểu 6 tháng 1 lần và đột xuất.
  > "c) Hội đồng quản lý vốn có nhiệm vụ đề xuất, tham mưu Tổng giám đốc (Giám đốc) về nội dung thực hiện đánh giá nội bộ về mức đủ vốn quy định tại khoản 4 Điều 25 Thông tư này."
  > "Tổng giám đốc (Giám đốc) quyết định quy chế làm việc của Hội đồng quản lý vốn, tối thiểu bao gồm chức năng, nhiệm vụ, cơ chế ra quyết định, cơ chế họp (họp định kỳ tối thiểu 06 tháng 01 lần, họp đột xuất);"
  > — Đ6.4.c ^d6-4c

- Hệ thống thông tin quản lý tối thiểu gồm dữ liệu phục vụ quản lý, kể cả dữ liệu rủi ro theo Đ24, và các báo cáo nội bộ (tối thiểu về hoạt động kiểm soát, quản lý rủi ro, đánh giá nội bộ về mức đủ vốn, kiểm toán nội bộ); phải được rà soát tối thiểu hằng năm.
  > "c) Dữ liệu để phục vụ việc quản lý, điều hành và ra quyết định trong hoạt động của ngân hàng, bao gồm cả dữ liệu rủi ro được quản lý theo quy định tại Điều 24 Thông tư này;"
  > "d) Các báo cáo nội bộ (tối thiểu có các báo cáo nội bộ về hoạt động kiểm soát, quản lý rủi ro, đánh giá nội bộ về mức đủ vốn, kiểm toán nội bộ) và thông tin quản lý khác được gửi, tiếp nhận, xử lý theo quy định nội bộ của ngân hàng;"
  > — Đ8.2 ^d8-2

- Ngân hàng phải lập và gửi NHNN báo cáo về hệ thống kiểm soát nội bộ theo khoản 2, 3, 4 Đ9; báo cáo thiếu, lỗi, sai thì NHNN yêu cầu báo cáo, giải trình hoặc làm việc trực tiếp.
  > "Ngân hàng phải lập và gửi Ngân hàng Nhà nước (Ngân hàng Nhà nước chi nhánh Khu vực theo đối tượng thanh tra, giám sát vi mô; Cục Quản lý, giám sát tổ chức tín dụng; Thanh tra Ngân hàng Nhà nước) báo cáo về hệ thống kiểm soát nội bộ theo quy định tại khoản 2, 3 và 4 Điều này."
  > — Đ9.1 ^d9-1

- Báo cáo về hệ thống kiểm soát nội bộ gồm báo cáo hằng năm về quản lý rủi ro theo Phụ lục II.
  > "b) Báo cáo hằng năm về quản lý rủi ro theo Phụ lục II ban hành kèm theo Thông tư này;"
  > — Đ9.2.b ^d9-2b

- Báo cáo quản lý rủi ro (cùng báo cáo Phụ lục I, III) được gửi trong 90 ngày kể từ ngày kết thúc năm tài chính.
  > "a) Đối với các báo cáo quy định tại điểm a, b và c khoản 2 Điều này: Trong thời hạn 90 ngày kể từ ngày kết thúc năm tài chính, ngân hàng gửi báo cáo của năm tài chính;"
  > — Đ9.3.a ^d9-3a

- Tổng giám đốc (Giám đốc) của ngân hàng thương mại phê duyệt báo cáo quản lý rủi ro; ở chi nhánh ngân hàng nước ngoài, Tổng giám đốc (Giám đốc) chi nhánh phê duyệt.
  > "c) Tổng giám đốc (Giám đốc) của ngân hàng thương mại chịu trách nhiệm phê duyệt các báo cáo quy định tại điểm b và điểm c khoản 2 Điều này;"
  > "d) Tổng giám đốc (Giám đốc) của chi nhánh ngân hàng nước ngoài chịu trách nhiệm phê duyệt các báo cáo quy định tại điểm a, b và c khoản 2 Điều này."
  > — Đ9.4.c–d ^d9-4c

- Báo cáo phải cập nhật các hạn chế, rủi ro mới phát sinh của hệ thống kiểm soát nội bộ trong toàn ngân hàng.
  > "Báo cáo về hệ thống kiểm soát nội bộ quy định tại khoản 2 Điều này phải cập nhật các hạn chế, rủi ro mới phát sinh của hệ thống kiểm soát nội bộ trong toàn bộ ngân hàng."
  > — Đ9.5 ^d9-5

### C3-M1 — Quy định chung về hoạt động quản lý rủi ro (Đ17–25)

- Quản lý rủi ro phải: nhận dạng đầy đủ, đo lường hợp lý, theo dõi thường xuyên rủi ro trọng yếu (đo lường áp dụng tối thiểu cho rủi ro trọng yếu tại Đ3.13.a); kiểm soát trạng thái rủi ro bảo đảm tuân thủ hạn mức; phân cấp thẩm quyền phê duyệt, thực hiện biện pháp phòng ngừa cho từng rủi ro trọng yếu.
  > "b) Nhận dạng đầy đủ, đo lường hợp lý, theo dõi thường xuyên để kịp thời phòng ngừa, giảm thiểu rủi ro trọng yếu. Việc đo lường quy định tại điểm này áp dụng tối thiểu đối với các loại rủi ro trọng yếu quy định tại điểm a khoản 13 Điều 3 Thông tư này;"
  > "c) Kiểm soát trạng thái rủi ro đảm bảo tuân thủ các hạn mức rủi ro;"
  > "e) Phân cấp cụ thể thẩm quyền phê duyệt, thực hiện các biện pháp phòng ngừa tối thiểu đối với từng loại rủi ro trọng yếu."
  > — Đ17.1 ^d17-1

- Quy định nội bộ về quản lý rủi ro tối thiểu gồm hạn mức rủi ro cho từng rủi ro trọng yếu, kể cả phương pháp xây dựng, người xây dựng, phân bổ hạn mức và xử lý vi phạm; cùng các nội dung về kiểm tra sức chịu đựng, quản lý dữ liệu rủi ro, quy trình đánh giá nội bộ về mức đủ vốn.
  > "b) Việc xây dựng, ban hành và thực hiện hạn mức rủi ro đối với tối thiểu từng loại rủi ro trọng yếu quy định tại điểm a khoản 13 Điều 3 Thông tư này (bao gồm cả các phương pháp xây dựng hạn mức rủi ro, cá nhân, bộ phận thực hiện xây dựng hạn mức rủi ro, phân bổ hạn mức rủi ro và xử lý vi phạm đối với các trường hợp vi phạm hạn mức rủi ro);"
  > "e) Kiểm tra sức chịu đựng;"
  > "h) Quy trình đánh giá nội bộ về mức đủ vốn;"
  > — Đ18.1 ^d18-1

- Trạng thái rủi ro và vi phạm về quản lý rủi ro phải được báo cáo kịp thời, đầy đủ cho HĐQT, HĐTV, Ban kiểm soát, ngân hàng mẹ; phải có cơ chế xử lý vi phạm.
  > "b) Các trạng thái rủi ro, hành vi vi phạm về quản lý rủi ro phải được báo cáo kịp thời, đầy đủ cho Hội đồng quản trị, Hội đồng thành viên, Ban kiểm soát, ngân hàng mẹ; có cơ chế xử lý đối với các vi phạm về quản lý rủi ro."
  > — Đ18.2.b ^d18-2b

- Chính sách quản lý rủi ro của ngân hàng thương mại do HĐQT, HĐTV ban hành, sửa đổi, bổ sung; của chi nhánh ngân hàng nước ngoài theo quy định của ngân hàng mẹ.
  > "1. Chính sách quản lý rủi ro của ngân hàng thương mại do Hội đồng quản trị, Hội đồng thành viên ban hành, sửa đổi, bổ sung."
  > — Đ19.1 ^d19-1

- Chính sách quản lý rủi ro tối thiểu gồm: khẩu vị rủi ro (tỷ lệ an toàn vốn mục tiêu; chỉ tiêu thu nhập ROE, RAROC; chỉ tiêu và mức độ chấp nhận rủi ro định tính khác); danh sách rủi ro trọng yếu; chiến lược quản lý từng rủi ro trọng yếu.
  > "a) Khẩu vị rủi ro bao gồm:"
  > "(i) Tỷ lệ an toàn vốn mục tiêu;"
  > "(ii) Chỉ tiêu về thu nhập: Tỷ suất giữa Lợi nhuận so với Vốn chủ sở hữu (Returns on Equity - ROE), Tỷ suất giữa lợi nhuận có điều chỉnh rủi ro so với vốn tự có (Risk Adjusted Returns on Capital - RAROC);"
  > "(iii) Chỉ tiêu và mức độ chấp nhận rủi ro (định tính) khác theo quy định nội bộ của ngân hàng;"
  > "b) Danh sách các rủi ro trọng yếu;"
  > "c) Chiến lược quản lý rủi ro đối với từng rủi ro trọng yếu."
  > — Đ19.2 ^d19-2

- Chính sách quản lý rủi ro được lập cho tối thiểu 3 năm, không quá 5 năm tiếp theo; đánh giá định kỳ tối thiểu một năm một lần và đột xuất; phải phù hợp với mức vốn tự có và nguồn tăng vốn; có tính kế thừa qua các chu kỳ kinh tế.
  > "a) Được lập cho thời gian tối thiểu 03 năm nhưng không quá 05 năm tiếp theo, được đánh giá định kỳ tối thiểu một năm một lần và đánh giá đột xuất do ngân hàng thương mại, ngân hàng mẹ quy định để điều chỉnh kịp thời khi có thay đổi về môi trường kinh doanh, pháp lý;"
  > "c) Phù hợp với mức vốn tự có và mức độ sẵn có của nguồn tăng vốn tự có;"
  > "d) Có tính kế thừa, liên tục để bảo đảm tính khả thi qua các chu kỳ kinh tế."
  > — Đ19.3 ^d19-3

- Hạn mức rủi ro của ngân hàng thương mại do Tổng giám đốc (Giám đốc) ban hành, sửa đổi, bổ sung; của chi nhánh ngân hàng nước ngoài theo quy định của ngân hàng mẹ.
  > "1. Hạn mức rủi ro của ngân hàng thương mại do Tổng giám đốc (Giám đốc) ban hành, sửa đổi, bổ sung."
  > — Đ20.1 ^d20-1

- Hạn mức rủi ro phải: tuân thủ các hạn chế bảo đảm an toàn theo Luật Các TCTD và quy định NHNN; có hạn mức kiểm soát các rủi ro trọng yếu; phù hợp khẩu vị rủi ro, chiến lược quản lý rủi ro và tổng tài sản có rủi ro phân bổ; rà soát tối thiểu một năm một lần hoặc khi có thay đổi lớn (nới lỏng thì Tổng giám đốc báo cáo HĐQT, HĐTV sau khi điều chỉnh); được phổ biến cho cá nhân, bộ phận liên quan.
  > "a) Tuân thủ các quy định về các hạn chế để bảo đảm an toàn trong hoạt động của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài tại Luật Các tổ chức tín dụng và quy định của Ngân hàng Nhà nước;"
  > "b) Có hạn mức rủi ro để kiểm soát các rủi ro trọng yếu phát sinh quy định tại điểm a khoản 13 Điều 3 Thông tư này;"
  > "c) Phù hợp với khẩu vị rủi ro, chiến lược quản lý rủi ro và tổng tài sản có rủi ro phân bổ cho rủi ro đó;"
  > "d) Phải được rà soát, đánh giá lại (sửa đổi, bổ sung nếu cần thiết) định kỳ tối thiểu một năm một lần hoặc khi có thay đổi lớn ảnh hưởng đến trạng thái rủi ro theo quy định nội bộ của ngân hàng. Trường hợp sửa đổi, bổ sung hạn mức rủi ro của ngân hàng thương mại theo hướng nới lỏng hơn, Tổng giám đốc (Giám đốc) phải báo cáo Hội đồng quản trị, Hội đồng thành viên sau khi điều chỉnh;"
  > "đ) Được phổ biến cho các cá nhân, bộ phận có liên quan."
  > — Đ20.2 ^d20-2

- Một hoạt động, giao dịch, sản phẩm có hạn mức khác nhau cho các rủi ro khác nhau thì áp hạn mức thận trọng hơn.
  > "3. Trường hợp một hoạt động, giao dịch, sản phẩm có hạn mức rủi ro khác nhau đối với các rủi ro khác nhau, ngân hàng phải áp dụng hạn mức rủi ro thận trọng hơn."
  > — Đ20.3 ^d20-3

- Đo lường rủi ro xác định tác động ngắn hạn, dài hạn lên thu nhập, vốn, thanh khoản; phải kịp thời, tối thiểu bằng phương pháp hoặc mô hình; phương pháp, mô hình phải được kiểm tra, đánh giá định kỳ về tính chính xác và hợp lý. Theo dõi rủi ro phải cảnh báo sớm khả năng vi phạm hạn mức.
  > "a) Ngân hàng đo lường mức độ rủi ro trên cơ sở xác định tác động ngắn hạn, dài hạn của rủi ro đó đối với thu nhập, vốn, thanh khoản của ngân hàng;"
  > "Phương pháp, mô hình đo lường rủi ro phải được kiểm tra, đánh giá định kỳ về tính chính xác và tính hợp lý theo quy định nội bộ của ngân hàng."
  > "3. Theo dõi rủi ro: Ngân hàng phải theo dõi trạng thái rủi ro và đánh giá kịp thời, cảnh báo sớm khả năng vi phạm các hạn mức rủi ro, hạn chế để bảo đảm an toàn trong hoạt động."
  > — Đ22.2–3 ^d22-2

- Ngân hàng phải kiểm tra sức chịu đựng về vốn và cho tối thiểu các rủi ro trọng yếu: tín dụng, thị trường, IRRBB, thanh khoản.
  > "1. Ngân hàng phải thực hiện kiểm tra sức chịu đựng về vốn và thực hiện kiểm tra sức chịu đựng cho tối thiểu các rủi ro trọng yếu sau:"
  > "c) Rủi ro lãi suất trên sổ ngân hàng;"
  > "d) Rủi ro thanh khoản."
  > — Đ23.1 ^d23-1

- Quy định nội bộ về kiểm tra sức chịu đựng tối thiểu gồm: loại và mục tiêu; tần suất; phạm vi và trạng thái nội, ngoại bảng; phương pháp luận (giả định, yếu tố rủi ro, kịch bản, mô hình, dữ liệu, cách dùng kết quả); quy trình và trách nhiệm.
  > "b) Tần suất thực hiện kiểm tra sức chịu đựng;"
  > "c) Xác định phạm vi hoạt động của ngân hàng và các trạng thái nội bảng, ngoại bảng để thực hiện kiểm tra sức chịu đựng;"
  > "d) Phương pháp luận về kiểm tra sức chịu đựng, trong đó tối thiểu bao gồm: phạm vi các giả định, danh sách các yếu tố rủi ro, kịch bản (nếu có), mô hình (nếu có), dữ liệu được sử dụng trong kiểm tra sức chịu đựng và việc sử dụng kết quả kiểm tra sức chịu đựng;"
  > — Đ23.2 ^d23-2

- Cho rủi ro tín dụng, thị trường, ngân hàng chọn tối thiểu một trong ba phương pháp: phân tích độ nhạy (tối thiểu 2 mức nghiêm trọng); phân tích kịch bản (tối thiểu 2 kịch bản: bình thường và bất lợi); kiểm tra sức chịu đựng ngược (giả định trường hợp bất lợi nghiêm trọng rồi xác định sự kiện dẫn tới).
  > "3. Ngân hàng lựa chọn tối thiểu một trong các phương pháp sau đây để kiểm tra sức chịu đựng cho rủi ro tín dụng, rủi ro thị trường:"
  > "Phương pháp phân tích độ nhạy cần xem xét tối thiểu 02 mức độ nghiêm trọng có thể xảy ra;"
  > "Phương pháp phân tích kịch bản cần lập tối thiểu 02 kịch bản gồm kịch bản hoạt động bình thường và kịch bản có diễn biến bất lợi có thể xảy ra phù hợp với mục đích thực hiện kiểm tra sức chịu đựng;"
  > "c) Kiểm tra sức chịu đựng ngược (Reverse Stress Testing): Thực hiện dựa trên giả định ngân hàng xảy ra trường hợp bất lợi nghiêm trọng (như vi phạm yêu cầu về tỷ lệ an toàn vốn tối thiểu, vi phạm tỷ lệ bảo đảm an toàn khác, tác động bất lợi khác) và xác định sự kiện, yếu tố dẫn đến trường hợp đó."
  > — Đ23.3 ^d23-3

- Phương pháp kiểm tra sức chịu đựng về thanh khoản theo Đ48, cho IRRBB theo Đ54, về vốn theo Đ60.
  > "4. Phương pháp kiểm tra sức chịu đựng cho rủi ro thanh khoản (kiểm tra sức chịu đựng về thanh khoản) thực hiện theo quy định tại Điều 48 Thông tư này, kiểm tra sức chịu đựng cho rủi ro lãi suất trên sổ ngân hàng thực hiện theo quy định tại Điều 54 Thông tư này, kiểm tra sức chịu đựng về vốn thực hiện theo quy định tại Điều 60 Thông tư này."
  > — Đ23.4 ^d23-4

- Tần suất: thanh khoản tối thiểu hằng quý và khi có sự kiện có thể tác động nghiêm trọng tới thanh khoản; tín dụng, thị trường tối thiểu hằng năm; IRRBB tối thiểu hằng quý; vốn tối thiểu hằng năm và khi có sự kiện tác động nghiêm trọng tới mức đủ vốn.
  > "a) Kiểm tra sức chịu đựng về thanh khoản định kỳ tối thiểu hằng quý và bất cứ khi nào xảy ra các sự kiện có thể gây tác động nghiêm trọng đến tính thanh khoản của ngân hàng;"
  > "b) Kiểm tra sức chịu đựng cho rủi ro tín dụng, kiểm tra sức chịu đựng cho rủi ro thị trường định kỳ tối thiểu hằng năm;"
  > "c) Kiểm tra sức chịu đựng cho rủi ro lãi suất trên sổ ngân hàng định kỳ tối thiểu hằng quý;"
  > "d) Kiểm tra sức chịu đựng về vốn định kỳ tối thiểu hằng năm và bất cứ khi nào xảy ra các sự kiện có thể gây tác động nghiêm trọng đến mức đủ vốn của ngân hàng."
  > — Đ23.5 ^d23-5

- Căn cứ kết quả kiểm tra sức chịu đựng, ngân hàng phải: đánh giá khả năng tuân thủ tỷ lệ bảo đảm an toàn; dùng kết quả để xây dựng hoặc sửa kế hoạch, chiến lược kinh doanh, chính sách quản lý rủi ro, kế hoạch dự phòng, phương án khắc phục khi cần; lập kế hoạch dự phòng theo Đ48.4 (thanh khoản); tính vốn kinh tế để xác định vốn mục tiêu (vốn).
  > "a) Đánh giá khả năng tuân thủ các tỷ lệ bảo đảm an toàn, các hạn chế khác để bảo đảm an toàn trong hoạt động của ngân hàng liên quan đến các loại kiểm tra sức chịu đựng theo khoản 1 Điều này;"
  > "b) Sử dụng kết quả kiểm tra sức chịu đựng để xây dựng hoặc sửa đổi các kế hoạch, chiến lược kinh doanh, chính sách quản lý rủi ro, kế hoạch dự phòng, phương án khắc phục theo quy định tại Luật Các tổ chức tín dụng trong trường hợp cần thiết."
  > "c) Lập kế hoạch dự phòng theo quy định tại khoản 4 Điều 48 Thông tư này (đối với kết quả kiểm tra sức chịu đựng về thanh khoản);"
  > "d) Tính toán vốn kinh tế để xác định vốn mục tiêu quy định tại Mục 9 Chương này (đối với kết quả kiểm tra sức chịu đựng về vốn)."
  > — Đ23.6 ^d23-6

- Dữ liệu rủi ro phải chính xác và toàn vẹn, khái niệm dữ liệu nhất quán, có kênh báo cáo và kế hoạch khắc phục dữ liệu kém chất lượng; phải thu thập, tổng hợp được toàn bộ dữ liệu từ các rủi ro trọng yếu, nhanh chóng và đáp ứng các loại báo cáo khác nhau.
  > "1. Dữ liệu rủi ro phải chính xác (accuracy) và toàn vẹn (integrity) trong đó đảm bảo nhất quán các khái niệm về dữ liệu, có kênh báo cáo nội bộ và kế hoạch khắc phục về tình trạng dữ liệu kém chất lượng (nếu có)."
  > "2. Ngân hàng phải thu thập và tổng hợp được dữ liệu rủi ro, tối thiểu bao gồm toàn bộ dữ liệu rủi ro từ các rủi ro trọng yếu."
  > — Đ24 ^d24-1

- Bộ phận quản lý Tài sản/Nợ phải trả (ALM) có trách nhiệm: quản lý bảng cân đối hiệu quả, phù hợp chính sách quản lý rủi ro; rà soát, đề xuất kế hoạch huy động, sử dụng vốn và nguyên tắc xây dựng giá điều chuyển vốn nội bộ; xây dựng khung lãi suất, khung giá sản phẩm; kiểm soát kinh doanh tuân thủ hạn mức rủi ro thanh khoản, hạn mức IRRBB, tổng tài sản tính theo rủi ro IRRBB.
  > "3. Cá nhân, bộ phận quản lý Tài sản/Nợ phải trả của ngân hàng thương mại có trách nhiệm:"
  > "a) Quản lý bảng cân đối tài sản hiệu quả, phù hợp với chính sách quản lý rủi ro;"
  > "b) Rà soát, đề xuất kế hoạch huy động vốn, kế hoạch sử dụng vốn, nguyên tắc xây dựng giá điều chuyển vốn nội bộ;"
  > "c) Xây dựng khung lãi suất, khung giá cho các sản phẩm khác để quản lý tài sản tài chính và nợ phải trả tài chính;"
  > "d) Kiểm soát hoạt động kinh doanh đảm bảo tuân thủ hạn mức rủi ro thanh khoản, hạn mức rủi ro lãi suất trên sổ ngân hàng, tổng tài sản tính theo rủi ro lãi suất trên sổ ngân hàng;"
  > — Đ25.3 ^d25-3

- Bộ phận quản lý rủi ro giúp Hội đồng rủi ro tham mưu Tổng giám đốc xây dựng chính sách, xây dựng và phân bổ hạn mức; theo dõi trạng thái rủi ro so với hạn mức để cảnh báo sớm; xây dựng phương pháp đo lường; xây dựng phương pháp luận và kịch bản kiểm tra sức chịu đựng; thực hiện báo cáo nội bộ về quản lý rủi ro.
  > "(ii) Xây dựng, thực hiện và phân bổ hạn mức rủi ro;"
  > "b) Giúp Hội đồng rủi ro trong việc theo dõi trạng thái rủi ro so với các hạn mức rủi ro để cảnh báo, nhận biết sớm rủi ro và nguy cơ vi phạm hạn mức rủi ro;"
  > "d) Xây dựng và sử dụng các phương pháp đánh giá và đo lường rủi ro;"
  > "g) Xây dựng phương pháp luận và lập kịch bản cho kiểm tra sức chịu đựng trên cơ sở phối hợp với bộ phận kinh doanh, bộ phận tuân thủ và các bộ phận khác có liên quan;"
  > "h) Thực hiện báo cáo nội bộ về quản lý rủi ro theo quy định nội bộ của ngân hàng thương mại;"
  > — Đ25.5 ^d25-5

### C3-M5 — Quản lý rủi ro thanh khoản (Đ45–49)

- Quản lý rủi ro thanh khoản tối thiểu phải: duy trì đủ tài sản có tính thanh khoản cao theo quy định NHNN cho cả điều kiện bình thường và điều kiện có diễn biến bất lợi (gồm cả tổn thất, chi phí khi tiếp cận thanh khoản trên thị trường).
  > "a) Duy trì đủ tài sản có tính thanh khoản cao theo quy định của Ngân hàng Nhà nước để đáp ứng nhu cầu thanh khoản trong điều kiện ngân hàng hoạt động bình thường và trong điều kiện có diễn biến bất lợi về thanh khoản (bao gồm cả việc xác định tổn thất, chi phí khi tiếp cận thanh khoản trên thị trường);"
  > — Đ45.1.a ^d45-1a

- Ngân hàng phải xác định chi phí đáp ứng nhu cầu thanh khoản và rủi ro thanh khoản trong định giá vốn nội bộ và đánh giá kết quả kinh doanh của các hoạt động trọng yếu, cả nội bảng và ngoại bảng.
  > "b) Xác định được chi phí đáp ứng nhu cầu thanh khoản và rủi ro thanh khoản trong việc định giá vốn nội bộ, đánh giá kết quả kinh doanh đối với các hoạt động kinh doanh trọng yếu (bao gồm cả nội bảng và ngoại bảng)."
  > — Đ45.1.b ^d45-1b

- Chiến lược quản lý rủi ro thanh khoản tối thiểu gồm: nguyên tắc quản lý thanh khoản (tối thiểu theo Đ46); chiến lược đa dạng hoá nguồn vốn và thời hạn vốn huy động; nguyên tắc kiểm tra sức chịu đựng về thanh khoản.
  > "2. Ngân hàng phải ban hành chiến lược quản lý rủi ro thanh khoản, tối thiểu bao gồm:"
  > "a) Nguyên tắc quản lý thanh khoản, tối thiểu các quy định tại Điều 46 Thông tư này;"
  > "b) Chiến lược đa dạng hóa nguồn vốn huy động, thời hạn vốn huy động để tăng sự ổn định của nợ phải trả, hỗ trợ thanh khoản hằng ngày;"
  > "c) Nguyên tắc thực hiện kiểm tra sức chịu đựng về thanh khoản."
  > — Đ45.2 ^d45-2

- Hạn mức rủi ro thanh khoản gồm: hạn mức bảo đảm tuân thủ tỷ lệ khả năng chi trả; tỷ lệ dư nợ cho vay so với tổng tiền gửi và tỷ lệ tối đa nguồn vốn ngắn hạn cho vay trung, dài hạn (nếu áp dụng); tỷ lệ khác theo pháp luật; và hạn mức khác theo quy định nội bộ đáp ứng Đ20.
  > "3. Ngân hàng phải thiết lập hạn mức rủi ro thanh khoản bao gồm:"
  > "(i) Tỷ lệ khả năng chi trả;"
  > "(ii) Tỷ lệ dư nợ cho vay so với tổng tiền gửi, tỷ lệ tối đa của nguồn vốn ngắn hạn được sử dụng để cho vay trung hạn và dài hạn (đối với ngân hàng áp dụng tỷ lệ này);"
  > "(iii) Tỷ lệ khác theo quy định của pháp luật (đối với ngân hàng áp dụng tỷ lệ này);"
  > "b) Các hạn mức rủi ro khác theo quy định nội bộ của ngân hàng đáp ứng quy định tại Điều 20 Thông tư này."
  > — Đ45.3 ^d45-3

- Phạm vi quản lý thanh khoản: ngân hàng thương mại, chi nhánh của ngân hàng thương mại (theo quy định nội bộ), chi nhánh ngân hàng nước ngoài; theo đồng Việt Nam và đô la Mỹ (gồm các ngoại tệ khác quy đổi sang đô la Mỹ), ngoại tệ khác nếu cần.
  > "(ii) Chi nhánh của ngân hàng thương mại theo quy định nội bộ của ngân hàng thương mại;"
  > "b) Đồng Việt Nam và đô la Mỹ (bao gồm đô la Mỹ và các ngoại tệ khác được quy đổi thành đô la Mỹ), ngoại tệ khác (nếu cần thiết)."
  > — Đ46.1 ^d46-1

- Phạm vi quản lý thanh khoản gồm ngân hàng thương mại và chi nhánh ngân hàng nước ngoài (cùng chi nhánh của ngân hàng thương mại, trích ở ^d46-1).
  > "(i) Ngân hàng thương mại;"
  > "(iii) Chi nhánh ngân hàng nước ngoài;"
  > — Đ46.1.a(i), (iii) ^d46-1b

- Quản lý thanh khoản tối thiểu gồm 5 cấu phần: trong ngày; tài sản có tính thanh khoản cao theo giá trị thị trường và khả năng chuyển đổi thành tiền; nguồn vốn huy động; dòng tiền (xác định chênh lệch dòng tiền ra và dòng tiền vào); nguồn thanh khoản (khả năng tiếp cận trong điều kiện bình thường và khó khăn).
  > "a) Quản lý thanh khoản trong ngày: Theo dõi trạng thái thanh khoản, xác định các nguồn vốn và khả năng huy động nguồn vốn này để đảm bảo thanh khoản, dự báo các tình huống làm thay đổi bất thường thanh khoản và có biện pháp xử lý;"
  > "b) Quản lý tài sản có tính thanh khoản cao theo giá trị thị trường và khả năng chuyển đổi thành tiền để đáp ứng yêu cầu thanh khoản trong điều kiện thị trường hoạt động bình thường và thị trường khó khăn về thanh khoản;"
  > "c) Quản lý nguồn vốn huy động đảm bảo thống kê số liệu về tiền gửi, chỉ số khác tuân thủ quy định của Ngân hàng Nhà nước về các giới hạn, tỷ lệ bảo đảm an toàn trong hoạt động của ngân hàng và chỉ số theo quy định nội bộ của ngân hàng;"
  > "d) Quản lý dòng tiền phải xác định chênh lệch về dòng tiền thông qua so sánh dòng tiền ra và dòng tiền vào, đảm bảo tuân thủ quy định của Ngân hàng Nhà nước về các giới hạn, tỷ lệ bảo đảm an toàn trong hoạt động của ngân hàng và các tỷ lệ về thanh khoản khác theo quy định nội bộ của ngân hàng;"
  > "đ) Quản lý nguồn thanh khoản đảm bảo đánh giá khả năng tiếp cận các nguồn thanh khoản để đáp ứng nhu cầu thanh khoản tương lai trong điều kiện thị trường hoạt động bình thường và trong điều kiện thị trường khó khăn về thanh khoản."
  > — Đ46.2 ^d46-2

- Nhận dạng rủi ro thanh khoản dựa trên phân tích nhu cầu và nguồn thanh khoản của từng hoạt động, cơ cấu tài sản/nợ, dòng tiền nội và ngoại bảng, khả năng tiếp cận thị trường; và nhận dạng rủi ro thanh khoản phát sinh từ rủi ro tín dụng, thị trường, hoạt động, danh tiếng và rủi ro khác.
  > "a) Thực hiện trên cơ sở phân tích nhu cầu thanh khoản, nguồn thanh khoản của từng hoạt động kinh doanh, cơ cấu Tài sản/Nợ phải trả và dòng tiền của các khoản mục nội bảng và ngoại bảng, khả năng tiếp cận thanh khoản trên thị trường;"
  > "b) Nhận dạng rủi ro thanh khoản phát sinh từ rủi ro tín dụng, rủi ro thị trường, rủi ro hoạt động, rủi ro danh tiếng và các rủi ro khác."
  > — Đ47.1 ^d47-1

- Công cụ đo lường rủi ro thanh khoản tối thiểu cho: dòng tiền tương lai của tài sản/nợ; nhu cầu thanh khoản bất thường và nghĩa vụ ngoại bảng; đồng tiền giao dịch; hoạt động ngân hàng đại lý, lưu ký và thanh toán.
  > "a) Dòng tiền tương lai của Tài sản/Nợ phải trả;"
  > "b) Nhu cầu thanh khoản bất thường và các trường hợp phải thực hiện nghĩa vụ của các khoản ngoại bảng;"
  > "c) Đồng tiền giao dịch;"
  > "d) Các hoạt động ngân hàng đại lý, lưu ký và thanh toán."
  > — Đ47.2 ^d47-2

- Theo dõi, kiểm soát phải bảo đảm tuân thủ hạn mức rủi ro thanh khoản và có chỉ tiêu cảnh báo sớm để xử lý thiếu hụt thanh khoản tạm thời và dài hạn.
  > "a) Theo dõi, kiểm soát trạng thái rủi ro thanh khoản đảm bảo tuân thủ các hạn mức rủi ro thanh khoản;"
  > "b) Có các chỉ tiêu cảnh báo sớm về rủi ro thanh khoản để có các biện pháp xử lý thiếu hụt thanh khoản tạm thời và dài hạn."
  > — Đ47.3 ^d47-3

- Kiểm tra sức chịu đựng về thanh khoản phải có phương pháp tính tác động của giả định để đánh giá khả năng thực hiện nghĩa vụ, cam kết và tuân thủ hạn mức; giả định và phương pháp phải được rà soát, tự đánh giá.
  > "1. Khi thực hiện kiểm tra sức chịu đựng về thanh khoản, ngân hàng phải có phương pháp tính toán tác động của các giả định đảm bảo đánh giá được khả năng thực hiện các nghĩa vụ, cam kết và tuân thủ các hạn mức rủi ro thanh khoản. Các giả định, phương pháp tính toán tác động của giả định phải được rà soát, tự đánh giá."
  > — Đ48.1 ^d48-1

- Tối thiểu 3 kịch bản: đặc thù ngân hàng (khủng hoảng thanh khoản ở ngân hàng khi hệ thống vẫn ổn định); toàn hệ thống (khủng hoảng tài chính quy mô rộng); hỗn hợp (khủng hoảng đặc thù lây lan ra toàn hệ thống).
  > "2. Ngân hàng phải áp dụng tối thiểu 03 kịch bản sau khi thực hiện kiểm tra sức chịu đựng về thanh khoản:"
  > "a) Kịch bản đặc thù của ngân hàng: Giả định xảy ra khủng hoảng thanh khoản đối với ngân hàng trong khi thanh khoản toàn hệ thống ngân hàng vẫn ổn định"
  > "b) Kịch bản toàn hệ thống ngân hàng: Giả định xảy ra khủng hoảng tài chính quy mô rộng có thể ảnh hưởng đến nhiều ngân hàng hoặc toàn bộ hệ thống ngân hàng (như: Có cú sốc kinh tế vĩ mô, gián đoạn thị trường tài chính…);"
  > "c) Kịch bản hỗn hợp là kịch bản kết hợp yếu tố của sự kiện đặc thù của ngân hàng và toàn hệ thống: Giả định xảy ra khủng hoảng đặc thù của một ngân hàng lây lan ra toàn hệ thống ngân hàng."
  > — Đ48.2 ^d48-2

- Ví dụ của kịch bản đặc thù: chất lượng tài sản xấu đi, nợ phải trả tăng cao, tài sản có tính thanh khoản cao sụt giảm nghiêm trọng, thâm hụt thanh khoản gia tăng, xếp hạng tín nhiệm giảm, ngân hàng bị tấn công thông tin.
  > "(như: Chất lượng tài sản bị xấu đi, nợ phải trả tăng cao, tài sản có tính thanh khoản cao bị sụt giảm nghiêm trọng, gia tăng thâm hụt thanh khoản, xếp hạng tín nhiệm của ngân hàng giảm, ngân hàng bị tấn công thông tin"
  > — Đ48.2.a ^d48-2b

- Kịch bản gồm các yếu tố rủi ro của tài sản có, nợ phải trả, cam kết ngoại bảng; tối thiểu phải xét: loại tiền tệ (VND, USD quy đổi, ngoại tệ khác); việc mua lại nợ hoặc thực hiện nghĩa vụ khác để giảm rủi ro danh tiếng; run-off rate thực tế của nợ phải trả trong thời kỳ căng thẳng; mức độ tập trung huy động vốn; mất hoặc giảm đáng kể khả năng thu hút vốn từ khách gửi tiền quan trọng, chủ nợ khác (kể cả liên ngân hàng).
  > "3. Các kịch bản được quy định tại khoản 2 Điều này bao gồm tập hợp các yếu tố rủi ro liên quan đến tài sản có, nợ phải trả, cam kết ngoại bảng. Việc phân tích các yếu tố rủi ro phải xem xét tối thiểu bao gồm:"
  > "b) Việc ngân hàng phải thực hiện mua lại nợ hoặc thực hiện nghĩa vụ khác để giảm thiểu rủi ro danh tiếng;"
  > "c) Tỷ lệ rút trước hạn (run-off rate) của nợ phải trả thực tế trong thời kỳ căng thẳng gia tăng;"
  > "d) Mức độ tập trung của huy động vốn;"
  > "đ) Mất hoặc giảm đáng kể khả năng thu hút vốn từ các khách hàng gửi tiền quan trọng hoặc các chủ nợ khác của ngân hàng (bao gồm cả thị trường liên ngân hàng)."
  > — Đ48.3 ^d48-3

- Yếu tố loại tiền tệ (VND, USD gồm ngoại tệ quy đổi, ngoại tệ khác) của tài sản có, nợ phải trả và cam kết ngoại bảng được xét để phản ánh khả năng chuyển đổi tiền tệ.
  > "a) Loại tiền tệ (Đồng Việt Nam và đô la Mỹ (bao gồm đô la Mỹ và các ngoại tệ khác được quy đổi thành đô la Mỹ), ngoại tệ khác (nếu có)) của tài sản có, nợ phải trả và các cam kết ngoại bảng để phản ánh khả năng chuyển đổi tiền tệ;"
  > — Đ48.3.a ^d48-3b

- Căn cứ kết quả kiểm tra sức chịu đựng, ngân hàng phải lập kế hoạch dự phòng, tối thiểu gồm: nhận diện khủng hoảng và sự kiện kích hoạt; thẩm quyền kích hoạt, vai trò và trách nhiệm; nguồn dự phòng tài chính (lượng vốn, mức độ sẵn có, điều kiện sử dụng, mức độ tin cậy, thời gian huy động); báo cáo, trao đổi thông tin trong và ngoài ngân hàng (kể cả NHNN); rà soát định kỳ và điều chỉnh.
  > "4. Căn cứ kết quả kiểm tra sức chịu đựng, ngân hàng phải lập kế hoạch dự phòng trong trường hợp không đáp ứng được các yêu cầu về thanh khoản, tối thiểu bao gồm:"
  > "a) Nhận diện khủng hoảng thanh khoản và sự kiện kích hoạt kế hoạch dự phòng;"
  > "b) Xác định rõ thẩm quyền kích hoạt kế hoạch dự phòng và vai trò, trách nhiệm của cá nhân, bộ phận có liên quan trong việc thực hiện kế hoạch này;"
  > "c) Xác định rõ các nguồn dự phòng tài chính bao gồm lượng vốn có thể huy động, mức độ sẵn có, các điều kiện để được sử dụng, mức độ tin cậy, thời gian huy động dự kiến của những nguồn này;"
  > "d) Việc báo cáo, trao đổi thông tin đảm bảo kịp thời, hiệu quả trong và ngoài ngân hàng (bao gồm cả Ngân hàng Nhà nước, cơ quan có thẩm quyền khác) trong quá trình thực hiện kế hoạch dự phòng;"
  > "đ) Kế hoạch dự phòng phải được rà soát định kỳ và điều chỉnh (nếu cần thiết)."
  > — Đ48.4 ^d48-4

- Báo cáo nội bộ về rủi ro thanh khoản lập định kỳ tối thiểu hằng quý hoặc đột xuất; tối thiểu gồm: xếp hạng tín nhiệm và thanh khoản thị trường; cơ cấu bảng cân đối, sản phẩm huy động mới, đối tượng gửi tiền, kỳ hạn và lãi suất tiền gửi; nguồn thanh khoản, chênh lệch dòng tiền, kỳ hạn nguồn vốn, tuân thủ hạn mức; kết quả kiểm tra sức chịu đựng (nếu có); đề xuất, kiến nghị; kết quả khắc phục kiến nghị.
  > "1. Định kỳ tối thiểu hằng quý hoặc đột xuất, ngân hàng có báo cáo nội bộ về rủi ro thanh khoản theo quy định tại khoản 2 Điều này."
  > "a) Nhận định về chỉ số xếp hạng tín nhiệm của ngân hàng và tình hình thanh khoản trên thị trường;"
  > "b) Cơ cấu của bảng cân đối tài sản, sản phẩm huy động vốn mới, đối tượng gửi tiền, kỳ hạn và lãi suất tiền gửi;"
  > "c) Các nguồn thanh khoản, chênh lệch về dòng tiền, kỳ hạn nguồn vốn, tình hình tuân thủ các hạn mức rủi ro thanh khoản;"
  > "d) Kết quả kiểm tra sức chịu đựng về thanh khoản trong kỳ báo cáo (nếu có);"
  > "đ) Đề xuất, kiến nghị về quản lý rủi ro thanh khoản với cấp nhận báo cáo;"
  > — Đ49.1–2 ^d49-1

- Báo cáo nội bộ về rủi ro thanh khoản gồm kết quả xử lý, khắc phục kiến nghị của kiểm toán nội bộ, NHNN, kiểm toán độc lập, cơ quan có thẩm quyền khác (nếu có).
  > "e) Kết quả xử lý, khắc phục theo yêu cầu, kiến nghị của kiểm toán nội bộ, Ngân hàng Nhà nước, tổ chức kiểm toán độc lập, cơ quan có thẩm quyền khác (nếu có)."
  > — Đ49.2.e ^d49-2e

### C3-M7 — Quản lý rủi ro lãi suất trên sổ ngân hàng (Đ53–55)

- Ngân hàng phải ban hành chiến lược quản lý rủi ro lãi suất trên sổ ngân hàng. Chiến lược tối thiểu gồm nguyên tắc quản lý theo chỉ số trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile): chênh lệch giữa giá trị tài sản nhạy cảm với lãi suất và nợ phải trả nhạy cảm với lãi suất (đều gồm cả khoản mục ngoại bảng) theo thời điểm ấn định mức lãi suất mới hoặc thời điểm định giá lại.
  > "Ngân hàng phải ban hành chiến lược quản lý rủi ro lãi suất trên sổ ngân hàng, tối thiểu bao gồm:"
  > "(i) Trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile) là mức chênh lệch giữa giá trị tài sản nhạy cảm với lãi suất (bao gồm cả khoản mục ngoại bảng) và nợ phải trả nhạy cảm với lãi suất (bao gồm cả khoản mục ngoại bảng) theo thời điểm ấn định mức lãi suất mới hoặc thời điểm định giá lại."
  > — Đ53.1.a(i) ^d53-1a1

- Chỉ số đo lường tác động của biến động lãi suất phải gồm ΔNII và ΔEVE; cách tính hai chỉ tiêu theo Phụ lục V.
  > "(ii) Chỉ số đo lường tác động của biến động lãi suất phải bao gồm chỉ tiêu thay đổi thu nhập lãi thuần (Change in Net Interest Income - ΔNII) và chỉ tiêu thay đổi giá trị kinh tế của vốn chủ sở hữu (Change in Economic Value of Equity - ΔEVE). Việc tính toán 2 chỉ tiêu này thực hiện theo quy định tại Phụ lục V ban hành kèm theo Thông tư này;"
  > — Đ53.1.a(ii) ^d53-1a2

- Chiến lược gồm nguyên tắc áp dụng biện pháp phòng ngừa rủi ro lãi suất trên sổ ngân hàng, kể cả thẩm quyền phê duyệt biện pháp phòng ngừa.
  > "b) Nguyên tắc áp dụng biện pháp phòng ngừa rủi ro lãi suất trên sổ ngân hàng (bao gồm cả thẩm quyền phê duyệt biện pháp phòng ngừa rủi ro lãi suất trên sổ ngân hàng)."
  > — Đ53.1.b ^d53-1b

- Ngân hàng phải thiết lập hạn mức rủi ro lãi suất trên sổ ngân hàng, tối thiểu gồm hạn mức về thay đổi thu nhập lãi thuần và hạn mức về thay đổi giá trị kinh tế của vốn chủ sở hữu do thay đổi của lãi suất.
  > "Ngân hàng phải thiết lập hạn mức rủi ro lãi suất trên sổ ngân hàng, tối thiểu bao gồm:"
  > "a) Hạn mức về thay đổi thu nhập lãi thuần do thay đổi của lãi suất;"
  > "b) Hạn mức về thay đổi giá trị kinh tế của vốn chủ sở hữu do thay đổi của lãi suất."
  > — Đ53.2 ^d53-2

- Ngân hàng phải có quy trình và thực hiện nhận dạng, đo lường, theo dõi, kiểm soát rủi ro lãi suất trên sổ ngân hàng định kỳ tối thiểu hằng quý và đột xuất theo quy định nội bộ.
  > "a) Có quy trình và thực hiện nhận dạng, đo lường, theo dõi và kiểm soát rủi ro lãi suất trên sổ ngân hàng định kỳ tối thiểu hằng quý và đột xuất theo quy định nội bộ của ngân hàng;"
  > — Đ54.1.a ^d54-1a

- Cá nhân, bộ phận đo lường, theo dõi và kiểm soát rủi ro lãi suất trên sổ ngân hàng phải độc lập với cá nhân, bộ phận kinh doanh phát sinh rủi ro đó.
  > "b) Có cá nhân, bộ phận thực hiện đo lường, theo dõi và kiểm soát rủi ro lãi suất trên sổ ngân hàng phải độc lập với cá nhân, bộ phận kinh doanh phát sinh rủi ro lãi suất trên sổ ngân hàng."
  > — Đ54.1.b ^d54-1b

- Nhận dạng phải xác định nguyên nhân, yếu tố làm phát sinh rủi ro, kể cả rủi ro mới phát sinh từ hoạt động phòng ngừa rủi ro lãi suất trên sổ ngân hàng.
  > "Nhận dạng rủi ro lãi suất trên sổ ngân hàng phải xác định nguyên nhân, yếu tố làm phát sinh rủi ro lãi suất trên sổ ngân hàng (bao gồm cả rủi ro mới phát sinh từ việc thực hiện hoạt động phòng ngừa rủi ro lãi suất trên sổ ngân hàng)."
  > — Đ54.2 ^d54-2

- Đo lường phải có phương pháp phù hợp với nguyên tắc quản lý tại Đ53.1.a và phải kiểm tra sức chịu đựng thông qua đo lường tác động của biến động lãi suất theo ΔNII và ΔEVE.
  > "a) Có phương pháp đo lường phù hợp với nguyên tắc quản lý rủi ro lãi suất trên sổ ngân hàng quy định tại điểm a khoản 1 Điều 53 Thông tư này;"
  > "b) Thực hiện kiểm tra sức chịu đựng về rủi ro lãi suất trên sổ ngân hàng thông qua đo lường tác động của biến động lãi suất theo các chỉ tiêu quy định tại điểm a(ii) khoản 1 Điều 53 Thông tư này;"
  > — Đ54.3.a–b ^d54-3b

- Đo lường theo từng loại tiền tệ khi tổng tài sản hoặc tổng nợ phải trả hạch toán bằng loại tiền tệ đó chiếm từ 5% trở lên trên tổng tài sản trên sổ ngân hàng.
  > "c) Đo lường rủi ro lãi suất trên sổ ngân hàng theo từng loại tiền tệ khi có tổng giá trị tài sản hoặc tổng nợ phải trả được hạch toán bằng loại tiền tệ đó chiếm từ 5% trở lên trên tổng tài sản trên sổ ngân hàng của ngân hàng;"
  > — Đ54.3.c ^d54-3c

- Các giả định và thay đổi giả định trong đo lường cần được ghi nhận và lưu trữ.
  > "d) Các giả định và thay đổi của giả định trong đo lường rủi ro lãi suất trên sổ ngân hàng cần được ghi nhận và lưu trữ."
  > — Đ54.3.d ^d54-3d

- Theo dõi phải bao gồm thời điểm ấn định mức lãi suất mới, thời điểm định giá lại của tài sản, nợ phải trả, khoản mục ngoại bảng nhạy cảm với lãi suất. Khi không xác định được thời gian đáo hạn hoặc thời điểm ấn định lãi suất mới, ngân hàng có thể dùng giả định; giả định phải được cấp có thẩm quyền phê duyệt theo quy định nội bộ.
  > "a) Theo dõi các thời điểm ấn định mức lãi suất mới, thời điểm định giá lại của tài sản, nợ phải trả, khoản mục ngoại bảng nhạy cảm với lãi suất. Trường hợp không xác định được thời gian đáo hạn, thời điểm ấn định mức lãi suất mới, ngân hàng có thể sử dụng giả định và giả định được sử dụng phải được cấp có thẩm quyền phê duyệt theo quy định nội bộ của ngân hàng."
  > — Đ54.4.a ^d54-4a

- Theo dõi, kiểm soát phải bảo đảm trạng thái rủi ro tuân thủ hạn mức; có cảnh báo sớm trường hợp gần vượt hạn mức và biện pháp xử lý kịp thời trường hợp vượt hạn mức.
  > "b) Trạng thái rủi ro lãi suất trên sổ ngân hàng đảm bảo tuân thủ các hạn mức rủi ro lãi suất trên sổ ngân hàng;"
  > "c) Có cảnh báo sớm các trường hợp gần vượt hạn mức rủi ro lãi suất trên sổ ngân hàng và biện pháp xử lý kịp thời các trường hợp vượt hạn mức rủi ro lãi suất trên sổ ngân hàng."
  > — Đ54.4.b–c ^d54-4c

- Ngân hàng có báo cáo nội bộ về rủi ro lãi suất trên sổ ngân hàng định kỳ tối thiểu hằng quý hoặc đột xuất. Báo cáo tối thiểu gồm: trạng thái chênh lệch kỳ định lại lãi suất; ΔNII, ΔEVE (kết quả kiểm tra sức chịu đựng); tình hình tuân thủ hạn mức; biện pháp phòng ngừa đã dùng và kết quả; đề xuất, kiến nghị; kết quả xử lý kiến nghị của kiểm toán nội bộ, NHNN, kiểm toán độc lập, cơ quan có thẩm quyền khác (nếu có).
  > "Định kỳ tối thiểu hằng quý hoặc đột xuất, ngân hàng có báo cáo nội bộ về rủi ro lãi suất trên sổ ngân hàng theo quy định tại khoản 2 Điều này."
  > "b) Thay đổi thu nhập lãi thuần, thay đổi giá trị kinh tế của vốn chủ sở hữu quy định tại điểm a(ii) khoản 1 Điều 53 Thông tư này (kết quả kiểm tra sức chịu đựng);"
  > "c) Tình hình tuân thủ các hạn mức rủi ro lãi suất trên sổ ngân hàng;"
  > — Đ55.1–2 ^d55-1

### C3-M8 — Quản lý rủi ro mô hình (Đ56–58)

- Ngân hàng xác định danh mục mô hình cần quản lý theo quy định nội bộ; định kỳ xếp hạng thành mô hình rủi ro cao, trung bình, thấp dựa trên các yếu tố như tính trọng yếu, độ phức tạp, mục đích sử dụng, chất lượng mô hình. Mô hình dùng trong phương pháp xếp hạng nội bộ (khi chuyển đổi sang phương pháp này) phải là mô hình rủi ro cao.
  > "1. Ngân hàng xác định danh mục mô hình cần quản lý theo quy định nội bộ; định kỳ xếp hạng, phân loại thành mô hình có rủi ro cao, trung bình, thấp dựa trên các yếu tố (như tính trọng yếu (materiality), tính phức tạp (complexity), mục đích sử dụng của mô hình, chất lượng mô hình (quality)"
  > "mô hình được sử dụng trong phương pháp xếp hạng nội bộ phải được xác định là mô hình có rủi ro cao."
  > — Đ56.1 ^d56-1

- Mục 8 áp dụng tối thiểu cho mô hình rủi ro cao; mô hình rủi ro thấp, trung bình quản lý theo quy định nội bộ.
  > "2. Ngân hàng thực hiện quản lý rủi ro mô hình theo quy định tại Mục này, tối thiểu bao gồm các mô hình có rủi ro cao tại khoản 1 Điều này."
  > "3. Ngân hàng thực hiện quản lý rủi ro mô hình có rủi ro thấp, trung bình theo quy định nội bộ của ngân hàng."
  > — Đ56.2–3 ^d56-2

- Với mô hình tự xây dựng (kể cả thuê ngoài), quản lý rủi ro mô hình theo vòng đời: xây dựng (xác định mục đích, phạm vi, đánh giá chất lượng dữ liệu đầu vào tối thiểu về tính chính xác, đầy đủ); triển khai (kể cả UAT) thống nhất với kết quả xây dựng đã phê duyệt, thay đổi không thống nhất phải được phê duyệt lại; sử dụng đúng mục đích, phạm vi, quản lý việc ghi đè (override) dữ liệu đầu vào và kết quả đầu ra (phải được phê duyệt, lưu thông tin, đánh giá), xử lý phản hồi người dùng; theo dõi, giám sát và đánh giá hiệu quả sử dụng.
  > "a) Trong giai đoạn xây dựng mô hình, ngân hàng phải xác định mục đích sử dụng, phạm vi sử dụng dự kiến và đánh giá chất lượng dữ liệu đầu vào của mô hình (tối thiểu về tính chính xác, tính đầy đủ) theo quy định nội bộ của ngân hàng;"
  > "b) Trong giai đoạn triển khai mô hình (bao gồm cả việc kiểm thử chấp nhận người dùng (user acceptance testing)), ngân hàng phải đảm bảo triển khai thống nhất với kết quả xây dựng mô hình đã được phê duyệt; trường hợp phát sinh thay đổi không thống nhất thì phải được cấp có thẩm quyền của ngân hàng phê duyệt lại và lưu giữ trong hồ sơ mô hình;"
  > "(i) Mô hình được sử dụng đúng mục đích, phạm vi;"
  > "phải được quản lý, tối thiểu bao gồm trường hợp được ghi đè, trường hợp thực hiện ghi đè phải được cấp có thẩm quyền phê duyệt, lưu giữ thông tin và đánh giá việc ghi đè;"
  > "d) Ngân hàng phải theo dõi, giám sát mô hình, trong đó đánh giá về hiệu quả của việc sử dụng mô hình;"
  > — Đ56.4.a–d ^d56-4

- Kiểm định mô hình tối thiểu gồm: kiểm định trước khi sử dụng, khi mô hình có thay đổi trọng yếu (theo quy định nội bộ), và định kỳ tối thiểu hằng năm. Kết quả kiểm định phải gồm báo cáo đánh giá khả năng đáp ứng mục tiêu ban đầu và hiệu quả sử dụng thực tế.
  > "đ) Ngân hàng phải kiểm định mô hình tối thiểu bao gồm: Kiểm định trước khi sử dụng, kiểm định khi mô hình có những thay đổi trọng yếu được xác định theo quy định nội bộ của ngân hàng, kiểm định định kỳ tối thiểu hằng năm. Kết quả kiểm định mô hình phải bao gồm báo cáo đánh giá về khả năng đáp ứng mục tiêu ban đầu và hiệu quả sử dụng thực tế của mô hình."
  > — Đ56.4.đ ^d56-4d

- Với mô hình mua (kể cả dùng từ ngân hàng mẹ): yêu cầu bên bán hoặc ngân hàng mẹ cung cấp thông tin về mô hình để đánh giá, sử dụng; đánh giá hiệu quả sử dụng. Ngân hàng phải lập, quản lý hồ sơ mô hình cho tối thiểu các mô hình rủi ro cao (kể cả đang dùng, đã điều chỉnh, đã ngừng sử dụng).
  > "a) Yêu cầu bên bán hoặc ngân hàng mẹ cung cấp thông tin liên quan về mô hình để phục vụ việc đánh giá, sử dụng mô hình;"
  > "b) Đánh giá hiệu quả của việc sử dụng mô hình theo quy định của ngân hàng."
  > "6. Ngân hàng phải lập, quản lý hồ sơ mô hình đối với tối thiểu các mô hình quy định tại khoản 2 Điều này (bao gồm cả mô hình đang sử dụng, mô hình được điều chỉnh, mô hình đã ngừng sử dụng)."
  > — Đ56.5–6 ^d56-5

- Quản lý rủi ro mô hình có 3 tuyến bảo vệ độc lập: tuyến 1 là bộ phận, cá nhân xây dựng, triển khai, sử dụng mô hình, nhận dạng, kiểm soát, theo dõi, giảm thiểu rủi ro; tuyến 2 là bộ phận, cá nhân kiểm định mô hình, xây dựng chính sách và quy định nội bộ về quản lý rủi ro, theo dõi, kiểm soát rủi ro toàn ngân hàng và tuân thủ pháp luật; tuyến 3 là kiểm toán nội bộ.
  > "a) Tuyến bảo vệ thứ nhất là bộ phận hoặc cá nhân thực hiện chức năng xây dựng, triển khai, sử dụng mô hình, nhận dạng, thực hiện các biện pháp kiểm soát, theo dõi, giảm thiểu rủi ro;"
  > "b) Tuyến bảo vệ thứ hai là bộ phận hoặc cá nhân thực hiện chức năng kiểm định mô hình, xây dựng chính sách quản lý rủi ro, quy định nội bộ về quản lý rủi ro; theo dõi, kiểm soát rủi ro toàn ngân hàng và tuân thủ quy định của pháp luật;"
  > "c) Tuyến bảo vệ thứ ba là bộ phận hoặc cá nhân thực hiện chức năng kiểm toán nội bộ."
  > — Đ56.7 ^d56-7

- Nhận dạng rủi ro mô hình phải xác định nguyên nhân phát sinh; theo dõi, kiểm soát để phòng ngừa, giảm thiểu, xử lý và có biện pháp khắc phục (remedial action) với hạn chế của mô hình.
  > "1. Nhận dạng rủi ro mô hình phải xác định nguyên nhân làm phát sinh rủi ro mô hình."
  > "2. Theo dõi, kiểm soát rủi ro mô hình để có biện pháp phòng ngừa, giảm thiểu, xử lý rủi ro phát sinh, biện pháp khắc phục (remedial action) đối với hạn chế của mô hình (nếu có)."
  > — Đ57 ^d57-1

- Báo cáo nội bộ về rủi ro mô hình lập tối thiểu hằng năm hoặc đột xuất; tối thiểu gồm danh mục mô hình theo mức rủi ro, mô hình điều chỉnh và ngừng sử dụng trong kỳ, tình hình xây dựng, triển khai, sử dụng (kể cả thuê ngoài, mua), kết quả kiểm định, đề xuất kiến nghị, kết quả khắc phục kiến nghị.
  > "1. Định kỳ tối thiểu hằng năm hoặc đột xuất, ngân hàng có báo cáo nội bộ về rủi ro mô hình theo quy định tại khoản 2 Điều này."
  > "b) Danh mục mô hình được điều chỉnh, mô hình đã ngừng sử dụng trong kỳ báo cáo;"
  > "d) Kết quả kiểm định mô hình định kỳ hoặc đột xuất (nếu có);"
  > — Đ58 ^d58-1

### C3-M9 — Đánh giá nội bộ về mức đủ vốn (Đ59–63)

- Đánh giá nội bộ về mức đủ vốn phải: tuân thủ quy định về tỷ lệ an toàn vốn của NHNN; duy trì tỷ lệ an toàn vốn mục tiêu trong kịch bản bình thường và kịch bản bất lợi; phù hợp khẩu vị rủi ro và diễn biến rủi ro trọng yếu; làm cơ sở xây dựng, điều chỉnh kế hoạch kinh doanh; thực hiện tối thiểu hằng năm và đột xuất khi có thay đổi dẫn đến không đáp ứng vốn mục tiêu.
  > "a) Tuân thủ quy định về tỷ lệ an toàn vốn của Ngân hàng Nhà nước;"
  > "b) Duy trì tỷ lệ an toàn vốn mục tiêu trong kịch bản hoạt động bình thường và kịch bản có diễn biến bất lợi;"
  > "c) Phù hợp với khẩu vị rủi ro và diễn biến của các rủi ro trọng yếu;"
  > "d) Làm cơ sở cho việc xây dựng, điều chỉnh kế hoạch kinh doanh của ngân hàng;"
  > "đ) Thực hiện định kỳ tối thiểu hằng năm và đột xuất khi có thay đổi về môi trường kinh doanh, các yếu tố có thể tác động đến rủi ro, nguồn vốn dẫn đến không đáp ứng được chỉ tiêu về vốn mục tiêu."
  > — Đ59.1 ^d59-1

- Đánh giá nội bộ về mức đủ vốn cho tối thiểu 3 năm, không quá 5 năm tiếp theo, gồm 6 bước: đo lường rủi ro trọng yếu và xác định vốn kinh tế theo kế hoạch kinh doanh (Phụ lục VI); kiểm tra sức chịu đựng về vốn để xác định tài sản có rủi ro và vốn kinh tế trong kịch bản bất lợi; xác định vốn mục tiêu, vốn tự có dự kiến (Phụ lục VI); lập kế hoạch vốn; giám sát mức đủ vốn theo vốn mục tiêu; rà soát quy trình.
  > "2. Ngân hàng thực hiện đánh giá nội bộ mức đủ vốn cho khoảng thời gian tối thiểu 03 năm nhưng không quá 05 năm tiếp theo theo các bước như sau:"
  > "a) Thực hiện đo lường rủi ro đối với các loại rủi ro trọng yếu và xác định vốn kinh tế theo kế hoạch kinh doanh theo hướng dẫn tại Phụ lục VI ban hành kèm theo Thông tư này;"
  > "b) Thực hiện kiểm tra sức chịu đựng về vốn để xác định tổng tài sản có rủi ro của các rủi ro trọng yếu, vốn kinh tế trong kịch bản có diễn biến bất lợi;"
  > "c) Xác định vốn mục tiêu, vốn tự có dự kiến theo hướng dẫn tại Phụ lục VI ban hành kèm theo Thông tư này;"
  > "d) Lập kế hoạch vốn;"
  > "đ) Giám sát về mức đủ vốn để quản lý vốn theo vốn mục tiêu và điều chỉnh kế hoạch vốn (khi cần thiết);"
  > "e) Rà soát quy trình đánh giá nội bộ về mức đủ vốn."
  > — Đ59.2 ^d59-2

- Kiểm tra sức chịu đựng về vốn: lập 2 kịch bản (bình thường, bất lợi) với tối thiểu giả định về lãi suất, tỷ giá, giá vàng, chất lượng tín dụng, và có phương pháp tính tác động lên tài sản có rủi ro theo từng loại rủi ro và tỷ lệ an toàn vốn. Giả định lãi suất tác động lên tài sản tính theo rủi ro hoạt động, rủi ro thị trường (lãi suất), IRRBB; tỷ giá, giá vàng lên rủi ro hoạt động, rủi ro thị trường (ngoại hối); chất lượng tín dụng lên rủi ro hoạt động, tín dụng, tập trung.
  > "1. Ngân hàng lập 02 kịch bản là kịch bản hoạt động bình thường và kịch bản có diễn biến bất lợi với tối thiểu các giả định về lãi suất, tỷ giá, giá vàng, chất lượng tín dụng và có phương pháp tính toán tác động của các giả định đối với tổng tài sản có rủi ro theo từng loại rủi ro và tỷ lệ an toàn vốn, tối thiểu đảm bảo:"
  > "a) Tính toán tác động theo giả định về lãi suất đối với tổng tài sản tính theo rủi ro hoạt động, rủi ro thị trường (rủi ro lãi suất), rủi ro lãi suất trên sổ ngân hàng;"
  > "b) Tính toán tác động theo giả định về tỷ giá, giá vàng đối với tổng tài sản tính theo rủi ro hoạt động, rủi ro thị trường (rủi ro ngoại hối nếu phát sinh trạng thái ngoại hối, vàng);"
  > "c) Tính toán tác động theo giả định về chất lượng tín dụng đối với tổng tài sản tính theo rủi ro hoạt động, rủi ro tín dụng, rủi ro tập trung."
  > — Đ60.1 ^d60-1

- Ngân hàng rà soát, đánh giá mức độ phù hợp của giả định và phương pháp tính tác động lên tỷ lệ an toàn vốn theo quy định nội bộ.
  > "2. Ngân hàng rà soát, đánh giá mức độ phù hợp của các giả định, phương pháp tính toán tác động của các giả định đối với tỷ lệ an toàn vốn theo quy định nội bộ của ngân hàng."
  > — Đ60.2 ^d60-2

- Kế hoạch vốn tối thiểu gồm: phương án tăng vốn khi vốn tự có dự kiến không đáp ứng vốn mục tiêu (nguồn tăng Vốn cấp 1, cấp 2; thời gian, lộ trình); chính sách chia cổ tức, lợi nhuận bảo đảm vốn tự có dự kiến sau khi chia không thấp hơn vốn mục tiêu; phân bổ vốn mục tiêu theo tài sản tính theo rủi ro cho các rủi ro trọng yếu làm cơ sở xác định hạn mức rủi ro; các mức cảnh báo sớm về tài sản tính theo rủi ro của từng rủi ro trọng yếu.
  > "a) Phương án tăng vốn trong trường hợp vốn tự có dự kiến không đáp ứng được vốn mục tiêu bao gồm:"
  > "(i) Nguồn vốn để tăng Vốn cấp 1, Vốn cấp 2 đảm bảo tính khả thi và phù hợp với quy định của pháp luật;"
  > "(ii) Thời gian, lộ trình thực hiện phương án tăng vốn;"
  > "b) Chính sách thực hiện chia cổ tức, chia lợi nhuận phải đảm bảo sau khi chia cổ tức, chia lợi nhuận, vốn tự có dự kiến không thấp hơn vốn mục tiêu;"
  > "c) Phân bổ vốn mục tiêu theo tổng tài sản tính theo rủi ro cho các rủi ro trọng yếu để làm cơ sở xác định các hạn mức rủi ro;"
  > "d) Các mức cảnh báo sớm về tổng tài sản tính theo rủi ro của từng rủi ro trọng yếu để theo dõi, giám sát việc tuân thủ tổng tài sản tính theo rủi ro được phân bổ cho từng loại rủi ro tại điểm c khoản này và có biện pháp xử lý kịp thời."
  > — Đ61.1 ^d61-1

- Kế hoạch vốn của ngân hàng thương mại do HĐQT, HĐTV phê duyệt theo đề nghị của Tổng giám đốc (Giám đốc); của chi nhánh ngân hàng nước ngoài theo quy định của ngân hàng mẹ.
  > "2. Kế hoạch vốn của ngân hàng thương mại do Hội đồng quản trị, Hội đồng thành viên phê duyệt theo đề nghị của Tổng giám đốc (Giám đốc)."
  > "3. Kế hoạch vốn của chi nhánh ngân hàng nước ngoài thực hiện theo quy định của ngân hàng mẹ."
  > — Đ61.2–3 ^d61-2

- Quy trình đánh giá nội bộ về mức đủ vốn được rà soát tối thiểu hằng năm hoặc đột xuất bởi bộ phận độc lập với bộ phận xây dựng và thực hiện quy trình; nội dung rà soát gồm tính hợp lý của quy trình, sự phù hợp giữa khẩu vị rủi ro và kế hoạch kinh doanh, giữa tài sản tính theo rủi ro và hạn mức rủi ro, dữ liệu đầu vào, giả định stress test vốn, tính khả thi của phương án tăng vốn.
  > "1. Quy trình đánh giá nội bộ về mức đủ vốn phải được rà soát định kỳ tối thiểu hằng năm hoặc đột xuất bởi một bộ phận độc lập với bộ phận xây dựng và thực hiện quy trình đánh giá nội bộ về mức đủ vốn."
  > "b) Tính phù hợp giữa khẩu vị rủi ro với kế hoạch kinh doanh, giữa tổng tài sản tính theo rủi ro với các hạn mức rủi ro;"
  > "c) Tính chính xác, đầy đủ của dữ liệu đầu vào;"
  > "d) Tính hợp lý của các giả định sử dụng trong kịch bản kiểm tra sức chịu đựng về vốn;"
  > "đ) Tính khả thi của phương án tăng vốn;"
  > — Đ62 ^d62-1

- Báo cáo nội bộ về đánh giá nội bộ mức đủ vốn lập hằng năm, tối thiểu gồm: vốn mục tiêu, vốn kinh tế; kết quả stress test vốn; kế hoạch vốn; kết quả phân bổ vốn; kết quả rà soát quy trình; kết quả khắc phục kiến nghị.
  > "1. Định kỳ hằng năm, ngân hàng có báo cáo nội bộ về đánh giá nội bộ về mức đủ vốn theo quy định tại khoản 2 Điều này."
  > "a) Vốn mục tiêu, vốn kinh tế;"
  > "b) Kết quả kiểm tra sức chịu đựng về vốn;"
  > "c) Kế hoạch vốn;"
  > "d) Kết quả phân bổ vốn;"
  > — Đ63 ^d63-1

### C5 — Điều khoản thi hành (chỉ Đ74, đọc một phần)

- Thông tư có hiệu lực từ 01/07/2026, trừ khoản 2, 3 và 4 Điều 74.
  > "Thông tư này có hiệu lực thi hành kể từ ngày 01 tháng 07 năm 2026, trừ quy định tại khoản 2, 3 và 4 Điều này."
  > — Đ74.1 ^d74-1

- Từ 01/07/2026 đến 31/12/2027, ngân hàng được xác định hạn mức, đo lường và kiểm tra sức chịu đựng rủi ro lãi suất trên sổ ngân hàng theo chỉ tiêu ΔNII hoặc ΔEVE, trừ trường hợp tại điểm b.
  > "Kể từ ngày 01 tháng 07 năm 2026 đến ngày 31 tháng 12 năm 2027, ngân hàng được thực hiện xác định hạn mức, đo lường và kiểm tra sức chịu đựng rủi ro lãi suất trên sổ ngân hàng theo chỉ tiêu thay đổi thu nhập lãi thuần hoặc chỉ tiêu thay đổi giá trị kinh tế của vốn chủ sở hữu, trừ trường hợp quy định tại điểm b khoản này."
  > — Đ74.4.a ^d74-4a

- Chậm nhất từ 01/01/2028, ngân hàng phải xác định hạn mức, đo lường và kiểm tra sức chịu đựng theo cả ΔNII và ΔEVE.
  > "Chậm nhất kể từ ngày 01 tháng 01 năm 2028, ngân hàng phải thực hiện xác định hạn mức, đo lường và kiểm tra sức chịu đựng rủi ro lãi suất trên sổ ngân hàng theo chỉ tiêu thay đổi thu nhập lãi thuần và chỉ tiêu thay đổi giá trị kinh tế của vốn chủ sở hữu theo quy định tại Thông tư này."
  > — Đ74.4.b ^d74-4b

- Từ 01/07/2026, Thông tư bãi bỏ TT13/2018/TT-NHNN, TT40/2018/TT-NHNN và Điều 3 TT09/2024/TT-NHNN.
  > "Kể từ ngày 01 tháng 07 năm 2026, Thông tư này bãi bỏ các quy định sau đây:"
  > "a) Thông tư số 13/2018/TT-NHNN ngày 18 tháng 5 năm 2018 của Thống đốc Ngân hàng Nhà nước Việt Nam quy định về hệ thống kiểm soát nội bộ của ngân hàng thương mại, chi nhánh ngân hàng nước ngoài;"
  > — Đ74.6 ^d74-6

### PL2 — Báo cáo quản lý rủi ro

- Mẫu báo cáo quản lý rủi ro gửi NHNN, lập theo năm, gồm 3 phần: I Chính sách quản lý rủi ro; II Quản lý các rủi ro cụ thể (7 loại); III Đề xuất, kiến nghị đối với NHNN.
  > "Kính gửi: Ngân hàng Nhà nước Việt Nam"
  > "I. Chính sách quản lý rủi ro"
  > "II. Quản lý các rủi ro cụ thể"
  > "III. Đề xuất, kiến nghị đối với Ngân hàng Nhà nước"
  > — PL2 ^pl2-0

- Phần I gồm: khẩu vị rủi ro; hoạt động trọng yếu và rủi ro trọng yếu; thay đổi chính sách quản lý rủi ro, khẩu vị rủi ro trong kỳ và lý do; quản lý dữ liệu rủi ro.
  > "1. Khẩu vị rủi ro."
  > "2. Các hoạt động trọng yếu và rủi ro trọng yếu."
  > "3. Thay đổi về chính sách quản lý rủi ro, khẩu vị rủi ro trong kỳ báo cáo, lý do thay đổi."
  > "4. Quản lý dữ liệu rủi ro."
  > — PL2.I ^pl2-i

- Mục II.4 rủi ro thanh khoản: chiến lược, hạn mức (thay đổi, lý do, tình hình thực hiện); đánh giá nhận dạng, đo lường, theo dõi, kiểm soát; kiểm tra sức chịu đựng (giả định, phương pháp kèm điểm mạnh và hạn chế, kết quả); kế hoạch dự phòng thanh khoản; vi phạm; hạn chế, vướng mắc; kết quả khắc phục kiến nghị.
  > "a) Chiến lược quản lý rủi ro thanh khoản, thay đổi trong kỳ báo cáo (nếu có), lý do thay đổi và tình hình thực hiện;"
  > "b) Hạn mức rủi ro thanh khoản, thay đổi trong kỳ báo cáo (nếu có), lý do thay đổi và tình hình thực hiện;"
  > "d) Kiểm tra sức chịu đựng về rủi ro thanh khoản:"
  > "Đánh giá tính phù hợp của phương pháp (nêu rõ điểm mạnh, hạn chế);"
  > "(iii) Kết quả kiểm tra sức chịu đựng về rủi ro thanh khoản;"
  > "đ) Kế hoạch dự phòng nhằm đảm bảo khả năng thanh khoản;"
  > — PL2.II.4 ^pl2-ii4

- Mục II.6 IRRBB gồm: a) chiến lược, thay đổi trong kỳ, lý do và tình hình thực hiện; b) hạn mức, thay đổi trong kỳ, lý do và tình hình thực hiện; c) đánh giá nhận dạng, đo lường, theo dõi, kiểm soát; d) kiểm tra sức chịu đựng: giả định trong kịch bản, phương pháp tính tác động, kết quả; đ) vi phạm và lý do; e) hạn chế, vướng mắc và nguyên nhân; g) kết quả khắc phục kiến nghị của NHNN, kiểm toán độc lập, cơ quan có thẩm quyền khác.
  > "a) Chiến lược quản lý rủi ro lãi suất trên sổ ngân hàng, thay đổi trong kỳ báo cáo (nếu có), lý do thay đổi và tình hình thực hiện;"
  > "b) Hạn mức rủi ro lãi suất trên sổ ngân hàng, thay đổi trong kỳ báo cáo (nếu có), lý do thay đổi và tình hình thực hiện;"
  > "c) Đánh giá về việc nhận dạng, đo lường, theo dõi, kiểm soát rủi ro lãi suất trên sổ ngân hàng;"
  > "d) Kiểm tra sức chịu đựng về rủi ro lãi suất trên sổ ngân hàng:"
  > "(i) Các giả định đã sử dụng trong kịch bản;"
  > "(ii) Phương pháp tính toán tác động của các giả định;"
  > "(iii) Kết quả kiểm tra sức chịu đựng về rủi ro lãi suất trên sổ ngân hàng;"
  > "đ) Các trường hợp vi phạm về quản lý rủi ro lãi suất trên sổ ngân hàng, lý do vi phạm;"
  > "e) Hạn chế, vướng mắc trong quản lý rủi ro lãi suất trên sổ ngân hàng và nguyên nhân;"
  > "g) Kết quả xử lý, khắc phục theo yêu cầu, kiến nghị của Ngân hàng Nhà nước, tổ chức kiểm toán độc lập, cơ quan có thẩm quyền khác đối với quản lý rủi ro lãi suất trên sổ ngân hàng."
  > — PL2.II.6 ^pl2-ii6

### PL5 — Hướng dẫn đo lường rủi ro lãi suất trên sổ ngân hàng

- ΔEVE là mức thay đổi của giá trị hiện tại ròng giữa dòng tiền vào của tài sản nhạy cảm với lãi suất và dòng tiền ra của nợ phải trả nhạy cảm với lãi suất (đều gồm khoản mục ngoại bảng) khi lãi suất thay đổi.
  > "Thay đổi giá trị kinh tế của vốn chủ sở hữu (ΔEVE) là mức độ thay đổi của giá trị hiện tại ròng giữa dòng tiền vào của tài sản nhạy cảm với lãi suất (bao gồm cả các khoản mục ngoại bảng) và dòng tiền ra của nợ phải trả nhạy cảm với lãi suất (bao gồm cả các khoản mục ngoại bảng) khi thay đổi lãi suất."
  > — PL5.A ^pl5-a-0

- Bước 1: ngân hàng xác định tài sản, nợ phải trả, khoản mục ngoại bảng nhạy cảm với lãi suất trên sổ ngân hàng theo quy định nội bộ, bảo đảm các điểm a–c khoản 1.
  > "1. Ngân hàng xác định tài sản, nợ phải trả, các khoản mục ngoại bảng nhạy cảm với lãi suất trên sổ ngân hàng theo quy định nội bộ của ngân hàng đảm bảo:"
  > — PL5.A.I.1 ^pl5-a1-1-0

- Tài sản nhạy cảm với lãi suất không gồm các khoản giảm trừ khỏi Vốn lõi cấp 1, tài sản cố định và khoản đầu tư vốn chủ sở hữu trên sổ ngân hàng. Nợ phải trả nhạy cảm với lãi suất gồm cả tiền gửi không hưởng lãi.
  > "(i) Các khoản giảm trừ khỏi Vốn lõi cấp 1;"
  > "(ii) Tài sản cố định;"
  > "(iii) Các khoản đầu tư vốn chủ sở hữu trên sổ ngân hàng (equity exposures in the banking book);"
  > "b) Nợ phải trả nhạy cảm với lãi suất bao gồm cả các khoản tiền gửi không hưởng lãi (non-remunerated deposits);"
  > — PL5.A.I.1.a–b ^pl5-a1-1a

- Dòng tiền định giá lại giả định trong tương lai (future notional repricing cash flows, gọi tắt là dòng tiền) là: khoản trả gốc; khoản gốc được định giá lại tại ngày gần nhất mà ngân hàng hoặc đối tác có quyền đơn phương thay đổi lãi suất, hoặc ngày lãi suất thả nổi tự động thay đổi theo chỉ số tham chiếu bên ngoài; khoản trả lãi trên phần gốc chưa hoàn trả hoặc chưa định giá lại. Ngày định giá lại (repricing date) là ngày của mỗi khoản này.
  > "(i) Bất kỳ khoản trả gốc (ví dụ: tại ngày đáo hạn theo hợp đồng);"
  > "(ii) Bất kỳ khoản gốc được định giá lại tại ngày gần nhất mà ngân hàng hoặc đối tác của ngân hàng có quyền đơn phương thay đổi lãi suất hoặc tại ngày mà lãi suất của một công cụ lãi suất thả nổi tự động thay đổi để phản ánh sự thay đổi của chỉ số tham chiếu bên ngoài;"
  > "(iii) Bất kỳ khoản trả lãi trên một phần của gốc chưa được hoàn trả hoặc chưa được định giá lại."
  > "Ngày định giá lại (repricing date) được xác định là ngày của khoản trả gốc, định giá lại gốc, khoản trả lãi quy định tại điểm c(i), c(ii), c(iii) khoản này."
  > — PL5.A.I.1.c ^pl5-a1-1c

- Ba nhóm: đáp ứng đủ tiêu chuẩn (amenable: khoản mục lãi suất cố định và thả nổi; quyền chọn lãi suất đính kèm không xem xét việc thực hiện và được xếp vào nhóm chưa đáp ứng đủ tiêu chuẩn); chưa đáp ứng đủ tiêu chuẩn (less amenable: quyền chọn lãi suất tự động); không đáp ứng đủ tiêu chuẩn (not amenable: NMDs, cho vay lãi suất cố định có rủi ro trả trước hạn, tiền gửi có kỳ hạn có rủi ro rút trước hạn).
  > "a) Nhóm đáp ứng đủ tiêu chuẩn (Amenable to standardisation) bao gồm khoản mục có lãi suất cố định và khoản mục có lãi suất thả nổi (không bao gồm các khoản mục thuộc nhóm không đáp ứng đủ tiêu chuẩn). Trong đó, đối với khoản mục đính kèm quyền chọn liên quan đến lãi suất, ngân hàng không xem xét đến việc thực hiện quyền chọn và ngân hàng phân nhóm quyền chọn này vào nhóm chưa đáp ứng đủ tiêu chuẩn;"
  > "b) Nhóm chưa đáp ứng đủ tiêu chuẩn (Less amenable to standardisation) bao gồm các quyền chọn lãi suất tự động (automatic interest rate options) (nếu có);"
  > "(i) Tiền gửi không kỳ hạn (Non-maturity Deposits – NMDs);"
  > "(ii) Khoản cho vay có lãi suất cố định có rủi ro trả trước hạn (Fixed rate loans subject to prepayment risk);"
  > "(iii) Khoản tiền gửi có kỳ hạn có rủi ro rút trước hạn (Term deposits subject to early redemption risk)."
  > — PL5.A.I.2 ^pl5-a1-2

- Bước 2: ngân hàng phân bổ dòng tiền vào 19 thang kỳ hạn theo ngày định giá lại (Bảng 1) hoặc vào điểm giữa thang kỳ hạn. Khi phân bổ vào điểm giữa, ngân hàng giữ nguyên kỳ hạn của dòng tiền bằng cách chia nhỏ dòng tiền giữa hai điểm giữa liền kề.
  > "(i) 19 thang kỳ hạn có ngày định giá lại quy định tại Bảng 1 Phụ lục này,hoặc"
  > "(ii) điểm giữa của thang kỳ hạn quy định tại Bảng 1 Phụ lục này. Trường hợp phân bổ dòng tiền vào điểm giữa của thang kỳ hạn, ngân hàng đảm bảo giữ nguyên kỳ hạn của dòng tiền này bằng việc chia nhỏ (splitting up) các dòng tiền giữa hai điểm giữa của thang kỳ hạn liền kề."
  > — PL5.A.II ^pl5-a2-0

- Bảng 1 — 19 thang kỳ hạn và điểm giữa $t_k$, từ Qua đêm (0,0028 năm) tới Từ trên 20 năm (25 năm).
  > "Bảng 1. 19 thang kỳ hạn"
  > — PL5.A.II, Bảng 1 ^pl5-a2-t1

  | STT | Thang kỳ hạn | Điểm giữa $t_k$ |
  |---|---|---|
  | 1 | Qua đêm | 0,0028 năm |
  | 2 | Qua đêm tới 1 tháng | 0,0417 năm |
  | 3 | Từ trên 1 tháng tới 3 tháng | 0,1667 năm |
  | 4 | Từ trên 3 tháng tới 6 tháng | 0,375 năm |
  | 5 | Từ trên 6 tháng tới 9 tháng | 0,625 năm |
  | 6 | Từ trên 9 tháng tới 1 năm | 0,875 năm |
  | 7 | Từ trên 1 năm tới 1,5 năm | 1,25 năm |
  | 8 | Từ trên 1,5 năm tới 2 năm | 1,75 năm |
  | 9 | Từ trên 2 năm tới 3 năm | 2,5 năm |
  | 10 | Từ trên 3 năm tới 4 năm | 3,5 năm |
  | 11 | Từ trên 4 năm tới 5 năm | 4,5 năm |
  | 12 | Từ trên 5 năm tới 6 năm | 5,5 năm |
  | 13 | Từ trên 6 năm tới 7 năm | 6,5 năm |
  | 14 | Từ trên 7 năm tới 8 năm | 7,5 năm |
  | 15 | Từ trên 8 năm tới 9 năm | 8,5 năm |
  | 16 | Từ trên 9 năm tới 10 năm | 9,5 năm |
  | 17 | Từ trên 10 năm tới 15 năm | 12,5 năm |
  | 18 | Từ trên 15 năm tới 20 năm | 17,5 năm |
  | 19 | Từ trên 20 năm | 25 năm |

- Nhóm đáp ứng đủ tiêu chuẩn: khoản mục lãi suất cố định phân bổ dòng tiền trả gốc, lãi vào thang kỳ hạn có ngày trả gốc, lãi. Khoản mục lãi suất thả nổi phân bổ dòng tiền trả gốc, lãi định kỳ tới ngày định giá lại tiếp theo gần nhất; phần gốc còn lại phân bổ vào thang kỳ hạn có ngày định giá lại tiếp theo gần nhất.
  > "a) Khoản mục có lãi suất cố định: Ngân hàng phân bổ dòng tiền từ tiền trả gốc, lãi (định kỳ hoặc cuối kỳ) vào thang kỳ hạn có ngày trả gốc, lãi hoặc vào điểm giữa của thang kỳ hạn."
  > "(i) Ngân hàng phân bổ dòng tiền từ tiền trả gốc, lãi định kỳ (nếu có) cho đến ngày định giá lại tiếp theo gần nhất vào thang kỳ hạn có ngày trả gốc, lãi hoặc vào điểm giữa của thang kỳ hạn;"
  > "(ii) Ngân hàng phân bổ dòng tiền từ tiền gốc còn lại sau khi thực hiện quy định tại điểm b(i) khoản này vào thang kỳ hạn có ngày định giá lại tiếp theo gần nhất hoặc vào điểm giữa của thang kỳ hạn."
  > — PL5.A.II.1 ^pl5-a2-1

- Nhóm chưa đáp ứng đủ tiêu chuẩn: ngân hàng không phân bổ dòng tiền.
  > "Đối với nhóm chưa đáp ứng đủ tiêu chuẩn: Ngân hàng không phân bổ dòng tiền đối với nhóm này."
  > — PL5.A.II.2 ^pl5-a2-2

- NMDs được phân loại thành tiền gửi cá nhân (tài khoản giao dịch hoặc không giao dịch) và tiền gửi tổ chức. Ngân hàng dùng dữ liệu lịch sử tách NMDs ổn định và không ổn định; từ NMDs ổn định xác định NMDs lõi. Tổng NMDs lõi và kỳ hạn trung bình của NMDs lõi phải đáp ứng Bảng 2. NMDs lõi phân bổ theo Bảng 2; NMDs không lõi phân bổ vào thang qua đêm.
  > "Tiền gửi cá nhân: được ghi nhận vào tài khoản giao dịch (transactional account) khi các giao dịch thường xuyên (như trả lương định kỳ) được thực hiện trên tài khoản đó (như tài khoản thanh toán). Các khoản tiền gửi cá nhân khác được ghi nhận vào tài khoản không giao dịch (non – transactional account)."
  > "ngân hàng sử dụng dữ liệu lịch sử để phân tách thành NMDs ổn định (stable NMDs) và NMDs không ổn định (non-stable NMDs)."
  > "NMDs lõi là phần NMDs ổn định và gần như không được định giá lại ngay cả khi lãi suất thay đổi đáng kể. Tổng giá trị NMDs lõi và kỳ hạn trung bình của NMDs lõi đáp ứng yêu cầu quy định tại Bảng 2 Phụ lục này."
  > "Phân bổ NMDs không lõi vào thang kỳ hạn qua đêm hoặc điểm giữa của thang kỳ hạn."
  > — PL5.A.II.3.a, Bảng 2 ^pl5-a2-3a

  | Loại NMDs | Giới hạn tỷ trọng NMDs lõi (%) | Giới hạn kỳ hạn trung bình NMDs lõi (năm) |
  |---|---|---|
  | NMDs lõi / tổng NMDs trên tài khoản giao dịch của cá nhân | 90 | 5 |
  | NMDs lõi / tổng NMDs trên tài khoản không giao dịch của cá nhân | 70 | 4,5 |
  | NMDs lõi / tổng NMDs tổ chức | 50 | 4 |

- NMDs ổn định là NMDs có khả năng cao khách hàng sẽ duy trì. NMDs lõi được xác định từ NMDs ổn định; NMDs không lõi là phần còn lại. NMDs lõi được phân bổ vào thang kỳ hạn hoặc điểm giữa sao cho đáp ứng Bảng 2.
  > "Trong đó, NMDs ổn định là NMDs có khả năng cao khách hàng sẽ duy trì khoản tiền gửi này."
  > "Từ NMDs ổn định, ngân hàng xác định NMDs lõi (core deposits)."
  > "NMDs không lõi (non-core deposits) là phần NMDs còn lại khác với NMDs lõi."
  > "Phân bổ NMDs lõi vào thang kỳ hạn hoặc điểm giữa của thang kỳ hạn đảm bảo đáp ứng yêu cầu quy định tại Bảng 2 phụ lục này."
  > — PL5.A.II.3.a(ii)–(iii) ^pl5-a2-3a2

- Cho vay lãi suất cố định có rủi ro trả trước hạn: ngân hàng phải có quy định nội bộ về tiêu chí xác định. Với khoản vay cá nhân, $CPR_{i,c}^p = \min(1, \gamma_i \times CPR_{0,c}^p)$ với $\gamma_i$ theo Bảng 3; dòng tiền $CF_{i,c}^p(k) = CF_{i,c}^S(k) + CPR_{i,c}^p \times N_{i,c}^p(k-1)$. Với khoản vay tổ chức, ngân hàng tự xác định dòng tiền.
  > "(i) Ngân hàng phải có quy định nội bộ quy định các tiêu chí xác định khoản cho vay có lãi suất cố định có rủi ro trả trước hạn của cá nhân, tổ chức;"
  > "Bảng 3. Hệ số nhân theo các kịch bản cú sốc lãi suất"
  > "là số dư gốc còn lại của khoản vay tại thang kỳ hạn (k-1)."
  > "(iii) Đối với khoản cho vay có lãi suất cố định có rủi ro trả trước hạn của tổ chức, ngân hàng tự xác định dòng tiền của khoản cho vay này để đo lường ΔEVE."
  > — PL5.A.II.3.b, Bảng 3 ^pl5-a2-3b

  | Kịch bản (i) | Kịch bản cú sốc lãi suất | $\gamma_i$ |
  |---|---|---|
  | 1 | Cú sốc tăng song song | 0,8 |
  | 2 | Cú sốc giảm song song | 1,2 |
  | 3 | Cú sốc dốc | 0,8 |
  | 4 | Cú sốc phẳng | 1,2 |
  | 5 | Cú sốc tăng lãi suất ngắn hạn | 0,8 |
  | 6 | Cú sốc giảm lãi suất ngắn hạn | 1,2 |

- $CPR_0$ được xác định cho từng danh mục p gồm các khoản cho vay cùng đồng tiền, cùng đặc điểm, trong điều kiện hiện hành. Trong công thức dòng tiền, $CF^S$ là khoản trả gốc, lãi định kỳ. Kịch bản i chạy từ 1 đến 6.
  > "(baseline conditional prepayment rate) cho mỗi danh mục p gồm các khoản cho vay theo đồng tiền c có cùng đặc điểm trong điều kiện hiện hành."
  > "là khoản trả gốc, lãi định kỳ."
  > "Kịch bản cú sốc lãi suất i được xác định tương ứng từ 1 đến 6."
  > — PL5.A.II.3.b(ii) ^pl5-a2-3b2

- Tiền gửi có kỳ hạn có rủi ro rút trước hạn: ngân hàng phải có quy định nội bộ về tiêu chí xác định. Với tiền gửi cá nhân, $TDRR_{i,c}^p = \min(1, u_i \times TDRR_{0,c}^p)$ với $u_i$ theo Bảng 4; dòng tiền rút trước hạn $CF_{i,c}^p(1) = TD_{0,c}^p \times TDRR_{i,c}^p$ được phân bổ vào thang qua đêm. Với tiền gửi tổ chức, ngân hàng tự xác định dòng tiền.
  > "(i) Ngân hàng phải có quy định nội bộ quy định các tiêu chí xác định khoản tiền gửi có kỳ hạn có rủi ro rút trước hạn của cá nhân, tổ chức;"
  > "Bảng 4. Hệ số nhân theo các kịch bản cú sốc lãi suất"
  > "Ngân hàng phân bổ dòng tiền gửi rút trước hạn này vào thang kỳ hạn qua đêm hoặc điểm giữa của thang kỳ hạn."
  > "(iii) Đối với khoản tiền gửi có kỳ hạn có rủi ro rút trước hạn của tổ chức, ngân hàng tự xác định dòng tiền của các khoản tiền gửi này để đo lường ΔEVE."
  > — PL5.A.II.3.c, Bảng 4 ^pl5-a2-3c

  | Kịch bản | Kịch bản cú sốc lãi suất | $u_i$ |
  |---|---|---|
  | 1 | Cú sốc tăng song song | 1,2 |
  | 2 | Cú sốc giảm song song | 0,8 |
  | 3 | Cú sốc dốc | 0,8 |
  | 4 | Cú sốc phẳng | 1,2 |
  | 5 | Cú sốc tăng lãi suất ngắn hạn | 1,2 |
  | 6 | Cú sốc giảm lãi suất ngắn hạn | 0,8 |

- $TDRR_0$ được xác định cho từng danh mục p gồm các khoản tiền gửi cùng đồng tiền, cùng đặc điểm, trong điều kiện hiện hành. $TD_0$ là số dư tiền gửi còn lại của danh mục p.
  > "baseline term deposit redemption ratio) cho mỗi danh mục p bao gồm các khoản tiền gửi theo đồng tiền c có cùng đặc điểm trong điều kiện hiện hành."
  > "là số dư tiền gửi còn lại của danh mục p."
  > — PL5.A.II.3.c(ii) ^pl5-a2-3c2

- Sáu kịch bản cú sốc lãi suất để tính EVE: tăng song song, giảm song song, dốc (giảm ngắn hạn, tăng dài hạn), phẳng (tăng ngắn hạn, giảm dài hạn), tăng lãi suất ngắn hạn, giảm lãi suất ngắn hạn.
  > "a) Cú sốc tăng song song (parallel shock up): Lãi suất tăng tương tự cho tất cả các kỳ hạn;"
  > "c) Cú sốc dốc (steepener shock): Giảm lãi suất cho kỳ hạn ngắn hạn và tăng lãi suất cho kỳ hạn dài hạn;"
  > "d) Cú sốc phẳng (flattener shock): Tăng lãi suất cho kỳ hạn ngắn hạn và giảm lãi suất cho kỳ hạn dài hạn;"
  > "đ) Cú sốc tăng lãi suất ngắn hạn (short rates shock up): Tăng lãi suất cho kỳ hạn ngắn hạn;"
  > — PL5.A.III.1 ^pl5-a3-1

- Bước 3: trong mỗi kịch bản, ngân hàng phân bổ dòng tiền vào thang $k$ hoặc điểm giữa $t_k$, tính dòng tiền ròng (vào trừ ra) cho từng thang. Dòng tiền ròng được chiết khấu theo hệ số chiết khấu lãi kép liên tục $DF_{i,c}(t_k) = \exp(-R_{i,c}(t_k) \times t_k)$, theo lãi suất phi rủi ro (risk-free rate). EVE theo kịch bản $i$ không gồm quyền chọn lãi suất tự động: $EVE_{i,c}^{nao} = \sum_k CF_{i,c}(k) \times DF_{i,c}(t_k)$.
  > "Tại mỗi thang kỳ hạn k hoặc tại điểm giữa của thang kỳ hạn"
  > "ngân hàng xác định dòng tiền vào và dòng tiền ra của tài sản, nợ phải trả, khoản mục ngoại bảng nhạy cảm với lãi suất để tính dòng tiền ròng (dòng tiền vào trừ dòng tiền ra) cho từng thang kỳ hạn."
  > "Dòng tiền tại mỗi thang kỳ hạn được chiết khấu theo lãi suất phi rủi ro (risk-free rate)."
  > "Ngân hàng xác định giá trị kinh tế của vốn chủ sở hữu đối với đồng tiền c theo kịch bản cú sốc lãi suất i (không bao gồm các quyền chọn lãi suất tự động) như sau:"
  > — PL5.A.III.2 ^pl5-a3-2

- Tổng các dòng tiền ròng tại các thang kỳ hạn là $CF_{i,c}(k)$ (hoặc $CF_{i,c}(t_k)$). Dòng tiền ròng được chiết khấu theo hệ số chiết khấu lãi kép liên tục theo kịch bản i và đồng tiền c; ngân hàng tính hệ số chiết khấu phù hợp với cách phân bổ dòng tiền của mình.
  > "Tổng kết quả các dòng tiền ròng tại tất cả các thang kỳ hạn là"
  > "được chiết khấu theo hệ số chiết khấu lãi kép liên tục (continuously compounded discount factor) theo kịch bản cú sốc lãi suất i đối với đồng tiền c."
  > "Ngân hàng tính hệ số chiết khấu phù hợp với việc phân bổ dòng tiền của ngân hàng."
  > — PL5.A.III.2 ^pl5-a3-2b

- Bước 4: ngân hàng tự đo lường rủi ro quyền chọn tự động $KAO_{i,c}$ (nếu có) theo từng kịch bản và đồng tiền.
  > "Bước 4: Ngân hàng tự đo lường rủi ro quyền chọn tự động đối với các quyền chọn lãi suất tự động (nếu có) theo kịch bản cú sốc lãi suất i đối với từng đồng tiền c"
  > — PL5.A.IV ^pl5-a4

- Bước 5: $\Delta EVE_{i,c} = EVE_{0,c}^{nao} - EVE_{i,c}^{nao} + KAO_{i,c}$. Ngân hàng cộng các khoản giảm $\Delta EVE_{i,c} > 0$ của tất cả đồng tiền theo từng kịch bản; giá trị giảm lớn nhất trong các kịch bản là giá trị đo lường IRRBB theo ΔEVE: $\Delta EVE = \max_{i} \{\max(0; \sum_{c: \Delta EVE_{i,c}>0} \Delta EVE_{i,c})\}$.
  > "Ngân hàng tính ΔEVE đối với đồng tiền c theo kịch bản i bằng cách lấy chênh lệch giữa giá trị kinh tế của vốn chủ sở hữu hiện hành"
  > "ngân hàng xác định các khoản giảm giá trị kinh tế của vốn chủ sở hữu"
  > "và tính tổng giá trị giảm cho tất cả các đồng tiền theo từng kịch bản cú sốc lãi suất i. Tổng giá trị giảm giá trị kinh tế của vốn chủ sở hữu lớn nhất trong tất cả các kịch bản cú sốc lãi suất được xác định là giá trị đo lường rủi ro lãi suất trên sổ ngân hàng theo"
  > — PL5.A.V ^pl5-a5

- ΔNII là mức thay đổi của thu nhập lãi thuần do thay đổi lãi suất từ tài sản, nợ phải trả, khoản mục ngoại bảng có lãi suất trên sổ ngân hàng.
  > "Thay đổi thu nhập lãi thuần (ΔNII) là mức độ thay đổi của thu nhập lãi thuần do thay đổi lãi suất từ các tài sản, nợ phải trả, khoản mục ngoại bảng có lãi suất trên sổ ngân hàng."
  > — PL5.B.I ^pl5-b1

- Ngân hàng đo lường ΔNII trong khoảng thời gian 01 năm, với giả định báo cáo tình hình tài chính không đổi (constant balance sheet).
  > "Ngân hàng đo lường ΔNII trong khoảng thời gian 01 năm với giả định báo cáo tình hình tài chính của ngân hàng không đổi (constant balance sheet)."
  > — PL5.B.II ^pl5-b2

- Ngân hàng dùng 2 kịch bản (tăng song song, giảm song song) để đo lường ΔNII; giá trị giảm lớn nhất của thu nhập lãi thuần trong 2 kịch bản là giá trị đo lường IRRBB theo ΔNII.
  > "Ngân hàng sử dụng 2 kịch bản gồm kịch bản cú sốc tăng song song và kịch bản cú sốc giảm song song để đo lường ΔNII. Giá trị giảm lớn nhất của thu nhập lãi thuần trong 2 kịch bản cú sốc lãi suất này là giá trị đo lường rủi ro lãi suất trên sổ ngân hàng theo ΔNII."
  > — PL5.B.III ^pl5-b3

- Ngân hàng áp dụng tham số $\bar{R}_{\text{loại sốc},c}$ (đơn vị bp) tại Bảng 5 cho 21 đồng tiền. Bảng 5 không có VND.
  > "Ngân hàng áp dụng tham số"
  > "quy định tại Bảng 5 Phụ lục này trong tính toán cú sốc lãi suất cho đồng tiền c quy định tại khoản 3 Mục I Phần C Phụ lục này."
  > — PL5.C.I.1, Bảng 5 ^pl5-c1-1

  |  | ARS | AUD | BRL | CAD | CHF | CNY | EUR | GBP | HKD | IDR | INR |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | Song song | 400 | 300 | 400 | 200 | 100 | 250 | 200 | 250 | 200 | 400 | 400 |
  | Ngắn hạn | 500 | 450 | 500 | 300 | 150 | 300 | 250 | 300 | 250 | 500 | 500 |
  | Dài hạn | 300 | 200 | 300 | 150 | 100 | 150 | 100 | 150 | 100 | 350 | 300 |

  |  | JPY | KRW | MXN | RUB | SAR | SEK | SGD | TRY | USD | ZAR |
  |---|---|---|---|---|---|---|---|---|---|---|
  | Song song | 100 | 300 | 400 | 400 | 200 | 200 | 150 | 400 | 200 | 400 |
  | Ngắn hạn | 100 | 400 | 500 | 500 | 300 | 300 | 200 | 500 | 300 | 500 |
  | Dài hạn | 100 | 200 | 300 | 300 | 150 | 150 | 100 | 300 | 150 | 300 |

- Đồng tiền không có trong Bảng 5 (hoặc ngân hàng không áp dụng Bảng 5): ngân hàng thu thập lãi suất hằng ngày 16 năm (hoặc khoảng thời gian tự xác định) ở các kỳ hạn 3 tháng, 6 tháng, 1, 2, 5, 7, 10, 15, 20 năm; lấy bình quân, nhân với tham số cú sốc toàn cầu cơ sở $\hat{\alpha}$ (song song 60%, ngắn hạn 85%, dài hạn 40%). Tham số phải có sàn tối thiểu 100 bp và trần 500 bp (ngắn hạn), 400 bp (song song), 300 bp (dài hạn).
  > "Trường hợp đồng tiền c không được quy định tại Bảng 5 Phụ lục này hoặc ngân hàng không áp dụng tham số"
  > "Ngân hàng thu thập lãi suất hằng ngày đối với đồng tiền c trong 16 năm hoặc khoảng thời gian khác do ngân hàng tự xác định đối với các kỳ hạn 3 tháng, 6 tháng, 1 năm, 2 năm, 5 năm, 7 năm, 10 năm, 15 năm và 20 năm."
  > "Bảng 6. Các tham số cú sốc lãi suất toàn cầu cơ sở"
  > "(i) Mức sàn tối thiểu 100bp;"
  > "Mức 500 bp đối với cú sốc lãi suất ngắn hạn;"
  > "Mức 400 bp đối với cú sốc lãi suất song song;"
  > "Mức 300 bp đối với cú sốc lãi suất dài hạn."
  > — PL5.C.I.2, Bảng 6 ^pl5-c1-2

  | Loại sốc | Tham số | Giá trị |
  |---|---|---|
  | Song song (parallel) | $\hat{\alpha}_{parallel}$ | 60% |
  | Lãi suất ngắn hạn (short rate) | $\hat{\alpha}_{short}$ | 85% |
  | Lãi suất dài hạn (long rate) | $\hat{\alpha}_{long}$ | 40% |

- Lãi suất bình quân hằng ngày của đồng tiền c là bình quân của tất cả mức lãi suất hằng ngày thuộc 9 kỳ hạn 3 tháng, 6 tháng, 1, 2, 5, 7, 10, 15 và 20 năm.
  > "Lãi suất bình quân hằng ngày đối với đồng tiền c được xác định bằng cách tính lãi suất bình quân từ tất cả các mức lãi suất hằng ngày thuộc các kỳ hạn 3 tháng, 6 tháng, 1 năm, 2 năm, 5 năm, 7 năm, 10 năm, 15 năm và 20 năm."
  > — PL5.C.I.2.a ^pl5-c1-2b

- Cú sốc theo kịch bản: song song $\pm\bar{R}_{parallel,c}$; ngắn hạn $\pm\bar{R}_{short,c} \times S_{short}(t_k)$ với $S_{short}(t_k) = e^{-t_k/x}$, $x = 4$; dài hạn $\pm\bar{R}_{long,c} \times (1 - e^{-t_k/x})$; dốc $-0,65|\Delta R_{short}| + 0,9|\Delta R_{long}|$; phẳng $+0,8|\Delta R_{short}| - 0,6|\Delta R_{long}|$.
  > "Ngân hàng xác định cú sốc lãi suất"
  > "a) Đối với kịch bản cú sốc song song cho đồng tiền c:"
  > "d) Đối với kịch bản cú sốc dốc và kịch bản cú sốc phẳng cho đồng tiền c:"
  > — PL5.C.I.3 ^pl5-c1-3

- Nếu không thực hiện Mục I Phần C, ngân hàng được tự xác định cú sốc lãi suất, bảo đảm phù hợp với hướng dẫn cập nhật của Ủy ban Basel về phương pháp xác định cú sốc (chú thích dẫn BCBS d578, bản hiệu chỉnh cú sốc IRRBB năm 2024).
  > "Trường hợp ngân hàng không thực hiện quy định tại Mục I Phần C Phụ lục này, ngân hàng được tự xác định cú sốc lãi suất, đảm bảo phù hợp với hướng dẫn cập nhật của Ủy ban Basel về phương pháp xác định cú sốc lãi suất"
  > "Văn bản BCBS D578 - Bản hiệu chỉnh cú sốc lãi suất trên sổ ngân hàng năm 2024 (Recalibration of shocks in the interest rate risk in the banking book standard) của Ủy ban Basel."
  > — PL5.C.II ^pl5-c2

### PL6 — Hướng dẫn cách xác định một số chỉ tiêu về vốn

- Vốn kinh tế $C_E = RWA^*_E \times CAR_{Target} + \Delta RWA_B \times CAR_R$. Trong đó $CAR_{Target}$ là tỷ lệ an toàn vốn mục tiêu trong khẩu vị rủi ro; $CAR_R$ là tỷ lệ an toàn vốn theo quy định NHNN; $\Delta RWA_B$ là chênh lệch dương giữa tổng tài sản tính theo rủi ro ở kịch bản bất lợi và ở kịch bản bình thường; $RWA^*_E$ là tổng tài sản tính theo rủi ro ở kịch bản bình thường.
  > "Tỷ lệ an toàn vốn mục tiêu trong khẩu vị rủi ro (%);"
  > "Tỷ lệ an toàn vốn theo quy định của Ngân hàng Nhà nước về tỷ lệ an toàn vốn đối với ngân hàng (%);"
  > "Giá trị chênh lệch dương giữa Tổng tài sản tính theo rủi ro trong kịch bản có diễn biến bất lợi trừ đi Tổng tài sản tính theo rủi ro trong kịch bản hoạt động bình thường;"
  > "Tổng tài sản tính theo rủi ro trong kịch bản hoạt động bình thường được xác định theo công thức sau đây:"
  > — PL6.I.1 ^pl6-1a

- $RWA^*_E = RWA_{CR} + RWA_{OR} + RWA_{MR} + RWA_{IRRBB} + RWA_{COR} + RWA_{OMR}$: tổng tài sản tính theo rủi ro tín dụng, hoạt động, thị trường, IRRBB, tập trung và các rủi ro trọng yếu khác (không gồm rủi ro thanh khoản). $RWA_{CR}$ theo quy định NHNN về tài sản có tính theo rủi ro tín dụng; $RWA_{OR}$, $RWA_{MR}$ phù hợp quy định NHNN về vốn yêu cầu cho rủi ro hoạt động, thị trường; $RWA_{OMR}$ theo phương pháp ngân hàng tự xây dựng.
  > "Tổng tài sản tính theo rủi ro lãi suất trên sổ ngân hàng;"
  > "Tổng tài sản tính theo các rủi ro trọng yếu khác (không bao gồm rủi ro thanh khoản)."
  > "được xác định theo quy định của Ngân hàng Nhà nước về tổng tài sản có tính theo rủi ro tín dụng."
  > "được xác định phù hợp với quy định của Ngân hàng Nhà nước về vốn yêu cầu đối với rủi ro hoạt động, vốn yêu cầu đối với rủi ro thị trường."
  > — PL6.I.1.d ^pl6-1b

- $RWA_{IRRBB}$ được xác định theo phương pháp ngân hàng tự xây dựng. Chậm nhất từ 01/01/2028, ngân hàng tính $RWA_{IRRBB}$ theo chỉ tiêu ΔEVE theo Thông tư này.
  > "được xác định theo phương pháp của ngân hàng tự xây dựng. Chậm nhất kể từ ngày 01 tháng 01 năm 2028, ngân hàng thực hiện tính"
  > "theo chỉ tiêu thay đổi giá trị kinh tế của vốn chủ sở hữu (ΔEVE) theo quy định tại Thông tư này."
  > — PL6.I.1.d(iv) ^pl6-1c

- $RWA_{COR} = RWA^1_{COR} + RWA^2_{COR}$. $RWA^1_{COR}$ (cấp tín dụng) theo phương pháp ngân hàng tự xây dựng nhưng không thấp hơn $RWA^{1*}_{COR} = \max(E_i - A \times C; 0) + \max(E_j - B \times C; 0)$, với $E_i$, $E_j$ là dư nợ cấp tín dụng với một khách hàng và với một khách hàng cùng người có liên quan (trừ khoản hệ số rủi ro 0% và khoản đã trừ khỏi vốn tự có), $C$ là vốn tự có; A, B theo lộ trình. $RWA^2_{COR}$ (tự doanh) theo phương pháp ngân hàng tự xây dựng.
  > "Tổng tài sản tính theo rủi ro tập trung đối với hoạt động cấp tín dụng được xác định theo phương pháp của ngân hàng tự xây dựng nhưng không thấp hơn mức"
  > "Tỷ lệ vốn tự có tương ứng cho một khách hàng, một khách hàng và người có liên quan theo lộ trình sau:"
  > "Tổng dư nợ cấp tín dụng đối với một khách hàng; không bao gồm các khoản cấp tín dụng có hệ số rủi ro bằng 0%, các khoản cấp tín dụng đã trừ khỏi Vốn tự có theo quy định của Ngân hàng Nhà nước về tỷ lệ an toàn vốn đối với ngân hàng;"
  > "Vốn tự có của ngân hàng được xác định theo quy định của Ngân hàng Nhà nước;"
  > "Tổng tài sản tính theo rủi ro tập trung đối với hoạt động tự doanh được xác định theo phương pháp của ngân hàng tự xây dựng."
  > — PL6.I.1.d(iii), Bảng 10 ^pl6-1d

  | Từ | Tỷ lệ với một khách hàng (A, %) | Tỷ lệ với một khách hàng và người có liên quan (B, %) |
  |---|---|---|
  | 01/07/2026 | 8,7 | 16,8 |
  | 01/01/2027 | 8 | 15,2 |
  | 01/01/2028 | 7,3 | 13,6 |
  | 01/01/2029 | 6,5 | 12 |

- Vốn mục tiêu $C_{Target} = \max(C_R, C_E)$, với $C_R$ là vốn tự có để đáp ứng tỷ lệ an toàn vốn theo quy định NHNN và $C_E$ là vốn kinh tế.
  > "Vốn tự có để đáp ứng tỷ lệ an toàn vốn theo quy định của Ngân hàng Nhà nước về tỷ lệ an toàn vốn đối với ngân hàng, chi nhánh ngân hàng nước ngoài;"
  > "Vốn kinh tế được xác định theo điểm 1 Mục này."
  > — PL6.I.2 ^pl6-2

- Vốn tự có dự kiến $C_A$ là vốn tự có theo quy định NHNN trên cơ sở kế hoạch kinh doanh 3–5 năm tới, với giả định: không có kế hoạch tăng vốn; không bổ sung vốn cho công ty con, công ty liên kết, khoản góp vốn; tỷ lệ chia cổ tức bằng bình quân 3 năm gần nhất; lợi nhuận giữ lại sau chia cổ tức được bổ sung vốn.
  > "là mức vốn tự có xác định theo quy định của Ngân hàng Nhà nước trên cơ sở kế hoạch kinh doanh tối thiểu 03 năm tiếp theo và không quá 05 năm tiếp theo với các giả định sau:"
  > "Không có kế hoạch tăng vốn;"
  > "Không có yêu cầu bổ sung vốn cho công ty con, công ty liên kết, các khoản đã góp vốn, mua cổ phần;"
  > "Tỷ lệ chia cổ tức bằng tỷ lệ chia cổ tức bình quân của 03 năm gần nhất;"
  > "Phần lợi nhuận giữ lại sau khi chia cổ tức được bổ sung vốn."
  > — PL6.II ^pl6-ii

- RAROC là tỷ lệ phần trăm giữa tổng lợi nhuận trước thuế và vốn kinh tế $C_E$.
  > "RAROC là tỷ lệ phần trăm giữa tổng lợi nhuận trước thuế so với Vốn kinh tế"
  > — PL6.III ^pl6-iii

## Node bị ảnh hưởng
- Tạo: [[tt83-2025]].
- Cập nhật (draft): [[notional-repricing-cash-flow]] (cột VN), [[repricing-balance-sheet]].
- Đề xuất (canonical): [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[standardised-interest-rate-shocks]], [[non-maturity-deposits]], [[behavioural-options]], [[irrbb-standardised-framework]], [[gap-risk]].
- C3-M8 [2026-10-19]: tạo [[model-validation]]; cập nhật [[model-risk-management]], [[three-lines-of-defence]], [[tt83-2025]]; đề xuất [[non-maturity-deposits]], [[behavioural-options]].
- C1 [2026-10-19]: tạo [[three-lines-of-defence]], [[alco]], [[banking-book]]; cập nhật [[tt83-2025]], [[economic-capital]], [[stress-testing]], [[risk-appetite]], [[liquidity-risk-management]], [[icaap]], [[model-risk-management]]; đề xuất [[gap-risk]], [[basis-risk]], [[option-risk]], [[behavioural-options]], [[irrbb-balance-sheet-portfolios]].
- PL6 [2026-10-19]: hoàn thiện [[economic-capital]]; tạo [[rwa-irrbb]], [[target-capital]], [[raroc]], [[projected-own-funds]]; cập nhật [[icaap]], [[capital-plan]], [[risk-appetite]], [[tt83-2025]]; đề xuất [[economic-value-of-equity]], [[bcbs-irrbb]].
- C3-M9 [2026-10-19]: tạo [[icaap]], [[capital-plan]], stub [[economic-capital]]; cập nhật [[stress-testing]], [[risk-limits]], [[risk-appetite]], [[tt83-2025]]; đề xuất [[bcbs-irrbb]], synthesis [[irrbb-alm-governance-strategy-and-tradeoffs]].
- C3-M1 [2026-10-19]: tạo [[risk-appetite]], [[risk-limits]], [[stress-testing]]; cập nhật [[tt83-2025]], [[liquidity-stress-testing]], [[liquidity-risk-management]]; đề xuất synthesis [[irrbb-alm-governance-strategy-and-tradeoffs]], [[practical-alm-liquidity-governance]].
- C3-M5 [2026-10-19]: tạo [[liquidity-stress-testing]]; hoàn thiện stub [[liquidity-risk-management]]; cập nhật [[tt83-2025]], [[run-off-rate]]; đề xuất [[contingency-funding-plan]], [[funding-concentration-risk]], [[intraday-liquidity-risk]], [[hqla]].
- PL2 + Đ9 [2026-10-19]: cập nhật [[tt83-2025]]; đề xuất synthesis [[irrbb-alm-governance-strategy-and-tradeoffs]].
- Bổ sung PL5 [2026-10-19]: cập nhật [[tt83-2025]], [[notional-repricing-cash-flow]]; đề xuất [[non-maturity-deposits]], [[behavioural-options]], [[economic-value-of-equity]], [[standardised-interest-rate-shocks]].

## Mâu thuẫn ghi nhận
Không có mâu thuẫn cùng phạm vi. Các khác biệt so với BCBS d368 (khác jurisdiction) ghi trong bảng Basel vs VN của từng node và trong [[tt83-2025]].

## Ghi chú convert
- PL5 dòng 2433: raw có chú thích "(tiền gửi kkh + fixed lãi suất có rủi ro trước hạn)" sau "bao gồm:", nhiều khả năng là ghi chú của người biên tập, không phải lời văn Thông tư. Không trích; cần đối chiếu pdf/docx.
- PL5 dòng 2641–2663: chỉ số tổng viết $\sum_{K=1}^{K}$ (chữ K hoa ở cận dưới). Claim ghi theo nghĩa $\sum_{k=1}^{K}$; cần đối chiếu bản gốc.
- Công thức PL5 không được trích nguyên văn (lint chuẩn hoá bỏ `_`, `\`); claim chép lại công thức và trích lời văn đi kèm.
- Raw dùng lẫn Unicode dựng sẵn (NFC) và tổ hợp (NFD), ví dụ dòng 1477, 1481, 1511 có dấu thanh tách rời. Lint so trích dẫn theo byte nên trích dẫn ở các dòng này được copy nguyên byte từ raw; khi thêm claim mới, copy từ `registry.py read` thay vì gõ lại.
- PL6 dòng 2770–2867: công thức viết bằng thẻ HTML `<sub>`/`<sup>` (không phải LaTeX). Không trích công thức nguyên văn; claim chép lại công thức dạng LaTeX và trích lời văn định nghĩa đi kèm.
