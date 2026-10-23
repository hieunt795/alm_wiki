---
title: "Cơ Chế Chuyển Giao Rủi Ro Nội Bộ Qua FTP (Internal Risk Transfer)"
aliases: [Internal Risk Transfer, Cơ chế chuyển giao rủi ro nội bộ, FTP Risk Transfer, Chuyển giao rủi ro qua FTP]
type: concept
domains: [alm, product]
status: active
maturity: draft
sources: ["[[src-choudhry-principles-banking]]", "[[src-vab-ftp]]", "[[src-bcbs-framework]]", "[[src-lubinska-alm-optimisation]]", "[[src-bardaeva-alm]]"]
relations: []
tags: [ftp, internal-risk-transfer, alm, treasury, matched-maturity, concept]
updated: 2026-10-22
reviewed:
---

## 1. Bản chất: chuyển giao rủi ro nội bộ

FTP không phải phòng ngừa rủi ro ra bên ngoài và không phải điều chuyển vốn vật lý nội bộ; FTP là chuyển giao rủi ro nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-10]]. Hệ thống FTP là ranh giới giữa hai nguồn lợi nhuận:

1. **Customer franchise**: năng lực bán sản phẩm cho khách hàng ở lãi suất khác lãi suất thị trường vốn [[src-choudhry-principles-banking#^choudhry-ftp-2]].
2. **Risky [[maturity-transformation|maturity transformation]]**: lợi nhuận rủi ro từ chênh lệch kỳ hạn có chủ đích hoặc không giữa tài sản và nợ [[src-choudhry-principles-banking#^choudhry-ftp-1]].

Ranh giới giữa hai nguồn này là hệ thống FTP của ngân hàng [[src-choudhry-principles-banking#^choudhry-ftp-3]].

Cơ chế chuyển giao theo Lubinska ("bank within a bank"): ALM thu FTP rate của asset centre và ghi có FTP rate cho liability centre; rủi ro lãi suất và rủi ro funding được tách khỏi business unit (BU) và chuyển về ALM quản lý [[src-lubinska-alm-optimisation#^lubinska-u01-7]]. Giữa BU và ALM không có phòng ngừa thật mà chỉ có hedge giả định (fictitious); rủi ro duy nhất BU còn quản lý là quan hệ với khách hàng ngoài và mức commercial spread [[src-lubinska-alm-optimisation#^lubinska-u01-12]].

- **Thông lệ (Choudhry, T4)**: toàn bộ rủi ro lãi suất tập trung về Treasury qua giao dịch funding; vị thế của các mảng khác được Treasury match fund hoặc phòng ngừa bằng internal swap [[src-choudhry-principles-banking#^choudhry-st-11]].
- **Phân biệt với khái niệm cùng tên của Basel**: RBC25.18 dùng tên "internal risk transfer" cho bản ghi nội bộ chuyển rủi ro giữa banking book và trading book, có hệ quả về vốn quy định [[src-bcbs-framework#^rbc25-18]]. Khái niệm đó nằm ở node [[regulatory-internal-risk-transfer]], khác với việc BU chuyển rủi ro sang Treasury qua FTP ở node này.

### Gap còn lại ở ALM (Lubinska)

ALM huy động vốn với đặc tính không nhất thiết khớp vốn cấp cho asset centre, nên còn lại chênh lệch kỳ hạn và lãi suất. Treasurer tách chênh lệch này thành tài khoản rủi ro lãi suất (IRRM) và tài khoản thanh khoản, rồi quyết định phòng ngừa bằng phái sinh hay để mở [[src-lubinska-alm-optimisation#^lubinska-u01-13]]. Ví dụ với khoản vay cố định 5 năm [[src-lubinska-alm-optimisation#^lubinska-u01-14]]:

| Lựa chọn | Payer swap | Trái phiếu phát hành | Receiver swap | Kết quả | Nguồn |
|---|---|---|---|---|---|
| a | 5Y | 5Y | 5Y | Đóng mọi rủi ro | [[src-lubinska-alm-optimisation#^lubinska-u01-14]] |
| b | 5Y | 3Y | 3Y | Đóng rủi ro lãi suất, mở rủi ro thanh khoản | [[src-lubinska-alm-optimisation#^lubinska-u01-14]] |
| c | 3Y | 5Y | 5Y | Đóng rủi ro thanh khoản, rủi ro lãi suất chưa phòng ngừa hết | [[src-lubinska-alm-optimisation#^lubinska-u01-14]] |

Phần chi phí thanh khoản còn mở: [[liquidity-cost-risk]].

## 2. Rủi ro nào chuyển về ALM, rủi ro nào không

FTP phản ánh các rủi ro mà bộ phận FTP phải quản lý, gồm rủi ro thanh khoản và rủi ro lãi suất sổ ngân hàng [[src-vab-ftp#^vab-ftp-4]].

| Rủi ro | Chuyển về ALM? | Nguồn |
|---|---|---|
| Rủi ro lãi suất | Có: tách khỏi BU, chuyển về ALM | [[src-lubinska-alm-optimisation#^lubinska-u01-7]] |
| Rủi ro funding | Có: tách khỏi BU, chuyển về ALM | [[src-lubinska-alm-optimisation#^lubinska-u01-7]] |
| Chi phí thanh khoản | BU tạo tài sản gây áp lực thanh khoản phải chịu chi phí tìm nguồn qua phí FTP | [[src-choudhry-principles-banking#^choudhry-ftp-15]] |
| Rủi ro tín dụng | Không: theo định nghĩa không chuyển về ALM | [[src-lubinska-alm-optimisation#^lubinska-u01-8]] |
| Rủi ro không phòng ngừa ra thị trường được | Không hết: do FTP thiết lập sai (phương pháp, dựng đường cong) hoặc thị trường phái sinh kém thanh khoản | [[src-lubinska-alm-optimisation#^lubinska-u01-8]] |

Commercial margin của BU là chênh lệch giữa lãi suất khách hàng bên ngoài và lãi suất FTP nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-7]]. Lãi suất FTP cố định trên cơ sở trùng khớp với lãi suất khách hàng (cùng kỳ hạn, đồng tiền, cơ sở lãi suất), nên commercial margin không đổi trước thay đổi đường cong FTP hay tỷ giá về sau [[src-choudhry-principles-banking#^choudhry-ftp-8]]. Giá giao dịch khách hàng hiện tại và commercial margin của BU không bị trợ cấp chéo bằng P&L kỳ vọng chưa thực hiện từ vị thế chênh lệch kỳ hạn [[src-choudhry-principles-banking#^choudhry-ftp-9]].

## 3. Gom vị thế và phòng ngừa phần ròng

- Trong thực hành, phòng ngừa IRRBB làm trên cơ sở macro hoặc tổng bảng cân đối: ngân hàng không làm IRS cho từng khoản thế chấp mà gom số dư phát sinh trong tháng rồi làm pool IRS cuối tháng. Vì vậy thường không áp được hedge accounting và ngân hàng chịu biến động P&L mark-to-market của macro hedge [[src-choudhry-principles-banking#^choudhry-cs-14]].
- Cách thay thế cho việc Centre phòng ngừa riêng từng tài sản và nợ: phòng ngừa vị thế ròng của tài sản và nợ sau khi khớp tenor hành vi tương tự, tận dụng natural hedge sẵn có (vay cố định với tiền gửi cố định, vay thả nổi với tiền gửi thả nổi); structural balance sheet hedging nên áp trên cơ sở ròng A − L [[src-choudhry-principles-banking#^choudhry-cs-17]].
- *Diễn giải:* khi Treasury nhận rủi ro từ nhiều BU, các vị thế ngược chiều có thể bù trừ nhau trước khi ra thị trường. Quy mô tiết kiệm chi phí phòng ngừa chưa có số liệu trong nguồn đã ingest. [cần nguồn]

## 4. Bóc tách lợi nhuận theo ba trung tâm

Lubinska đo lợi nhuận của asset centre và liability centre bằng chênh lệch giữa giá sản phẩm bên ngoài và FTP rate; phần maturity transformation do ALM quản lý và tạo lợi nhuận cho ngân hàng [[src-lubinska-alm-optimisation#^lubinska-u01-16]]. Trong ví dụ của Lubinska, P&L của asset centre là 2,69%, liability centre là −0,68% (chi phí vốn bên ngoài cao hơn FTP rate) và ALM là 0,99% [[src-lubinska-alm-optimisation#^lubinska-u01-16]].

$$
\text{Asset centre} + \text{Liability centre} + \text{ALM} = 2{,}69\% - 0{,}68\% + 0{,}99\% = 3{,}00\%
$$

*Diễn giải:* ba phần cộng lại bằng chênh lệch giữa lãi suất tài sản bên ngoài và chi phí nợ bên ngoài, vì FTP rate bị triệt tiêu giữa các trung tâm. Phép cộng 3,00% là số học trên ví dụ của Lubinska, không phải claim của nguồn. Sự tách giữa "rủi ro" (maturity transformation) và "phi rủi ro" (customer franchise) là một hệ quả quan trọng của hệ thống FTP [[src-choudhry-principles-banking#^choudhry-ftp-13]].

## 5. Quản trị và xung đột lợi ích

- ALM xác định nguyên tắc định giá điều chuyển, dựng đường cong FTP nội bộ và quy tắc lãi suất khách hàng tối thiểu [[src-bardaeva-alm#^ch11-5]]. Nguyên tắc gán kỳ hạn trên đường cong cho một loại giao dịch không được do đơn vị thực hiện giao dịch quyết định [[src-bardaeva-alm#^ch11-11]].
- Choudhry khuyến nghị trước khi trình ALCO: bảo đảm sự ủng hộ của các business line, nêu rõ chế độ FTP không hỗ trợ P&L của Treasury nếu được sắp xếp đúng nên không có xung đột lợi ích, và thể hiện FTP bằng nỗ lực viết chung của Finance và Treasury [[src-choudhry-principles-banking#^choudhry-cs-6]].
- Vai trò ALCO trong phê duyệt phương pháp FTP: xem [[alco]]. [cần nguồn] nếu cần nêu thẩm quyền cụ thể của ALCO với đường cong và biên điều chỉnh.

## Khái niệm và Liên kết
- [[funds-transfer-pricing]]: node tổng về FTP.
- [[liquidity-transfer-pricing]]: định giá điều chuyển thanh khoản nội bộ.
- [[ftp-transmission-mechanism]]: cơ chế truyền dẫn của FTP.
- [[ftp-pricing-methodology]]: phương pháp định giá chi tiết VOF, COF và phụ phí tuân thủ.
- [[gap-risk]]: rủi ro khe hở tái định giá.
- [[interest-rate-swap]]: công cụ phòng ngừa của Treasury.
- [[replicating-portfolio-model]]: mô hình danh mục tái lập cho sản phẩm không kỳ hạn.
- [[lcr]], [[nsfr]]: tỷ lệ thanh khoản chi phối chi phí thanh khoản trong FTP.

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
