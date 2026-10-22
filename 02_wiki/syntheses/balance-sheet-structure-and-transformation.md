---
title: "Cấu trúc bảng cân đối và chuyển hoá kỳ hạn"
aliases: [Cấu trúc bảng cân đối và chuyển hoá kỳ hạn, Balance Sheet Structure and Transformation, Balance sheet structure and maturity transformation]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Cấu trúc tài sản, nguồn vốn, vốn chủ sở hữu và các cam kết ngoại bảng; đặc điểm contractual cash flows, maturity, repricing, currency và embedded options của từng nhóm sản phẩm. · Bản chất kinh tế của maturity transformation, liquidity transformation và interest rate transformation; cơ chế hình thành NII/NIM và các rủi ro phát sinh."
as_of: 2026-10-22
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tata-bank-alm]]", "[[src-lubinska-alm-optimisation]]", "[[src-vab-ftp]]", "[[src-bcbs-lcr]]", "[[src-tt83-2025-nhnn]]", "[[src-tt50-2026-nhnn]]"]
relations: []
tags: [balance-sheet, maturity-transformation, nii, nim, ftp, irrbb, research]
updated: 2026-10-22
reviewed:
---

## Câu hỏi
Thuộc bộ "Balance Sheet Fundamentals & Risk Transmission" (6 câu). Cụm này trả lời:
- **Q1.** Cấu trúc tài sản, nguồn vốn, vốn chủ sở hữu và các cam kết ngoại bảng; đặc điểm contractual cash flows, maturity, repricing, currency và embedded options của từng nhóm sản phẩm.
- **Q2.** Bản chất kinh tế của maturity transformation, liquidity transformation và interest rate transformation; cơ chế hình thành NII/NIM và các rủi ro phát sinh.

Q3–Q4 (các loại gap, truyền dẫn tới NII, EVE, LCR, NSFR, CAR, LEV: [[balance-sheet-gaps-and-risk-transmission]]) và Q5–Q6 (synthetic balance sheet, ví dụ định lượng) thuộc hai synthesis khác của cùng bộ câu hỏi.

## Kết luận
- **Q1.** Wiki không có nguồn mô tả "bảng cân đối mẫu" theo từng dòng sản phẩm. Khung phân loại có nguồn là khung IRRBB: vị thế nhạy lãi suất của sổ ngân hàng được xếp vào ba nhóm theo mức độ chuẩn hoá được dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-1]], và ΔEVE tính dòng tiền của cả tài sản, nợ lẫn khoản mục ngoại bảng [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Đặc điểm quyết định gồm ngày tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-9]], quyền chọn tự động hoặc hành vi [[src-bcbs-irrbb-2016#^irrbb-u02-2]] và đồng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-1]]. Vốn chủ sở hữu nằm trong sổ ngân hàng [[src-tata-bank-alm#^tata-scope-1]] nhưng bị loại khỏi ΔEVE [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Cơ cấu bảng cân đối thay đổi mạnh theo môi trường lãi suất và mô hình kinh doanh [[src-tata-bank-alm#^tata-prac-1]] [[src-tata-bank-alm#^tata-prac-3]].
- **Q2.** Maturity transformation là việc tạo lợi nhuận có rủi ro từ chênh lệch cấu trúc kỳ hạn giữa tài sản và nợ [[src-choudhry-principles-banking#^choudhry-ftp-1]]. Choudhry gọi việc huy động ngắn, cho vay dài khi đường cong dốc lên là "định nghĩa của ngân hàng" [[src-choudhry-principles-banking#^choudhry-hedge-1]]. NII là thu nhập lãi trừ chi phí lãi, NIM là NII chia tài sản sinh lãi [[src-choudhry-principles-banking#^choudhry-nim-2]]. FTP tách NII thành phần customer franchise và phần maturity transformation [[src-choudhry-principles-banking#^choudhry-ftp-3]]. Rủi ro phát sinh gồm gap risk lên thu nhập [[src-choudhry-principles-banking#^choudhry-irr-2]], funding gap risk [[src-choudhry-principles-banking#^choudhry-lgap-1]], và đánh đổi giữa rủi ro EV với biến động thu nhập [[src-bcbs-irrbb-2016#^irrbb-u02-4]]. Liquidity transformation không có nguồn trong wiki [cần nguồn]. Interest rate transformation không xuất hiện như một thuật ngữ trong nguồn đã ingest; ý gần nhất là interest-rate gap [[src-choudhry-principles-banking#^choudhry-almb-7]].

## Cơ chế

### Q1 — Các nhóm vị thế và đặc điểm dòng tiền

**Ranh giới sổ.** Sổ ngân hàng gồm mọi giao dịch, vị thế dài hạn gắn với hoạt động khách hàng và việc tài trợ cho chúng, kể cả vốn chủ sở hữu [[src-tata-bank-alm#^tata-scope-1]]. Tại VN, sổ ngân hàng gồm repo, reverse repo, phái sinh phòng ngừa khoản mục báo cáo tình hình tài chính, tài sản tài chính dự trữ thanh khoản và mọi giao dịch không thuộc sổ kinh doanh [[src-tt83-2025-nhnn#^d3-33]]. Chi tiết: [[banking-book]].

**Ba nhóm theo khả năng chuẩn hoá dòng tiền (BCBS d368, Stage 1)** [[src-bcbs-irrbb-2016#^irrbb-u05-1]]. Xem [[irrbb-balance-sheet-portfolios]].

| Nhóm vị thế | Đặc điểm dòng tiền và tái định giá | Xử lý | Nguồn |
|---|---|---|---|
| Lãi suất thả nổi | Giả định tái định giá toàn bộ tại first reset date; chỉ phần spread không tái định giá được slot vào dải sau | Slot gốc vào dải chứa ngày reset | [[src-bcbs-irrbb-2016#^irrbb-u05-12]] |
| Có quyền chọn tự động nhúng (cap, floor) | Bỏ qua quyền chọn khi slot dòng tiền | Tính add-on riêng cho quyền chọn tự động | [[src-bcbs-irrbb-2016#^irrbb-u05-3]] [[src-bcbs-irrbb-2016#^irrbb-u05-1]] |
| Cho vay cố định có quyền trả trước | Tốc độ trả trước tăng khi lãi suất giảm, giảm khi lãi suất tăng | CPR nhân hệ số theo kịch bản | [[src-bcbs-irrbb-2016#^irrbb-u05-5]] |
| Tiền gửi có kỳ hạn có thể rút trước | Tỷ lệ rút trước thay đổi theo kịch bản | TDRR nhân hệ số theo kịch bản | [[src-bcbs-irrbb-2016#^irrbb-u05-6]] |
| Tiền gửi không kỳ hạn (NMD) | Phần non-core coi là qua đêm; phần core slot theo kỳ hạn, có trần tỷ lệ và kỳ hạn bình quân | Phân đoạn core/non-core theo Table 2 | [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |

Một dòng tiền được định nghĩa qua repricing date: ngày hoàn trả gốc, tái định giá gốc hoặc trả lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Trong lịch tái định giá, khoản lãi suất cố định xếp theo ngày đáo hạn, khoản thả nổi xếp theo thời gian tới lần tái định giá kế tiếp [[src-tata-bank-alm#^tata-gap-1]]. Xem [[repricing-balance-sheet]], [[non-maturity-deposits]], [[behavioural-options]].

**Embedded options.** Option risk phát sinh từ phái sinh quyền chọn hoặc từ yếu tố quyền chọn nhúng trong tài sản, nợ và khoản mục ngoại bảng, gồm automatic option và behavioural option [[src-bcbs-irrbb-2016#^irrbb-u02-2]]. TT83 dùng cùng cách chia: quyền chọn tự động chắc chắn thực hiện theo hợp đồng khi lãi suất thay đổi, quyền lựa chọn hành vi khi lãi suất thay đổi có thể làm đổi hành vi khách hàng [[src-tt83-2025-nhnn#^d3-22]].

**Vốn chủ sở hữu.** Ba nguồn nói ba khía cạnh khác nhau:
- vốn chủ sở hữu thuộc sổ ngân hàng [[src-tata-bank-alm#^tata-scope-1]];
- ΔEVE phải loại vốn chủ sở hữu của chính ngân hàng khỏi mức phơi nhiễm, và tính trên giả định run-off balance sheet [[src-bcbs-irrbb-2016#^irrbb-p08-2]];
- số dư không nhạy lãi suất, gồm vốn cổ đông, không tái định giá khi lãi suất đổi và là một nguồn mismatch [[src-choudhry-principles-banking#^choudhry-cs-13]].

Vốn cổ phần không có chi phí lãi thực nhưng có chi phí quy đổi là RoE mục tiêu [[src-choudhry-principles-banking#^choudhry-capm-11]]. Xem [[funds-transfer-pricing]].

**Ngoại bảng.** Cam kết tín dụng và thanh khoản gồm thoả thuận không huỷ ngang hoặc huỷ ngang có điều kiện để cấp vốn trong tương lai; phần giả định bị rút trong LCR được coi là dư nợ không hoàn trả [[src-bcbs-lcr#^lcr40-59]]. Tỷ lệ rút giả định phụ thuộc loại đối tác và loại hạn mức [[src-bcbs-lcr#^lcr40-64]]; xem [[committed-facilities]]. Trong IRRBB, ΔEVE và ΔNII đều tính dòng tiền của khoản mục ngoại bảng nhạy lãi suất trong sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-p08-2]] [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Gap risk theo TT83 cũng bao gồm khoản mục ngoại bảng [[src-tt83-2025-nhnn#^d3-22]].

**Đồng tiền.** ΔEVE chuẩn hoá được xác định cho từng kịch bản sốc và từng đồng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-1]]. Về thanh khoản, TT50 phân biệt LCR quy VNĐ, LCR VNĐ và LCR ngoại tệ trọng yếu [[src-tt50-2026-nhnn#^d16-1]]; LCR VNĐ riêng lẻ phải quản lý, còn LCR ngoại tệ trọng yếu quản lý theo quy định nội bộ [[src-tt50-2026-nhnn#^d16-2]]. Xem [[lcr-by-currency]].

**Cơ cấu theo mô hình kinh doanh.** Ở các MFI Đức 1999–2021, lãi suất giảm dài hạn đẩy tiền gửi không kỳ hạn từ 7,9% lên 29,3% tổng tài sản; hơn một nửa mức tăng đến từ khách hàng rời tiền gửi có kỳ hạn và tài khoản tiết kiệm [[src-tata-bank-alm#^tata-prac-1]]. Trong 2021–2023, lãi suất tăng làm tiền gửi không kỳ hạn giảm còn 26,1% và tiền gửi có kỳ hạn dưới 1 năm tăng từ 2,6% lên 5,9% [[src-tata-bank-alm#^tata-prac-2]]. Ngân hàng có mạng lưới huy động bán lẻ lớn không thể từ chối tiền gửi, trong khi ngân hàng dựa vào liên ngân hàng chủ động hơn về nguồn vốn; ALM phải theo mô hình kinh doanh [[src-tata-bank-alm#^tata-prac-3]].

*Diễn giải:* với ALM, đơn vị phân tích của Q1 không phải "khoản mục kế toán" mà là "nhóm dòng tiền có cùng hành vi tái định giá, cùng loại quyền chọn và cùng đồng tiền". Cách chia ba nhóm của d368 đã ngầm làm việc này (ngoài wiki, chưa có nguồn).

### Q2 — Transformation, NII/NIM và rủi ro

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[irrbb-balance-sheet-portfolios]] | exposed-to | [[gap-risk]] | | [[src-bcbs-irrbb-2016#^irrbb-u02-2]] |
| [[irrbb-balance-sheet-portfolios]] | exposed-to | [[basis-risk]] | | [[src-bcbs-irrbb-2016#^irrbb-u02-2]] |
| [[irrbb-balance-sheet-portfolios]] | exposed-to | [[option-risk]] | | [[src-bcbs-irrbb-2016#^irrbb-u02-2]] |
| [[gap-risk]] | drives | [[net-interest-margin]] | − · rising_rate | [[src-choudhry-principles-banking#^choudhry-hedge-1]] |
| [[gap-risk]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-4]] |
| [[funds-transfer-pricing]] | input-to | [[net-interest-margin]] | | [[src-vab-ftp#^vab-ftp-40]] |
| [[hqla]] | drives | [[net-interest-margin]] | − | [[src-choudhry-principles-banking#^choudhry-nim-5]] |
| [[nii-planning]] | drives | [[net-interest-margin]] | | [[src-choudhry-principles-banking#^choudhry-nim-12]] |
| [[maturity-transformation]] | exposed-to | [[gap-risk]] | | [[src-choudhry-principles-banking#^choudhry-hedge-1]] |
| liquidity transformation | drives | [[hqla]] · funding liquidity | | [cần nguồn] |

**Maturity transformation** ([[maturity-transformation]], node stub).
- Định nghĩa: việc tạo lợi nhuận có rủi ro từ chênh lệch, có chủ đích hoặc không, trong cấu trúc kỳ hạn của tài sản và nợ [[src-choudhry-principles-banking#^choudhry-ftp-1]].
- Hình thái điển hình: khi đường cong dốc lên, ngân hàng huy động ở đầu ngắn và cho vay ở đầu dài; phần "tail" là interest-rate gap, và nếu lãi suất ngắn hạn tăng thì biên lợi nhuận có thể thu hẹp hoặc chuyển thành lỗ funding [[src-choudhry-principles-banking#^choudhry-hedge-1]].
- Trong sổ accrual, tài sản dài hạn còn nợ chủ yếu ngắn hạn, nên chi phí funding tăng có thể làm giảm NII; tài sản, nợ lãi suất cố định còn tạo chi phí cơ hội khi lãi suất thị trường đổi [[src-choudhry-principles-banking#^choudhry-irrbb-1]].
- Theo Lubinska, maturity transformation do ALM quản lý và tạo lợi nhuận cho ngân hàng qua quy trình FTP [[src-lubinska-alm-optimisation#^lubinska-u01-16]].

**Interest rate transformation.** Nguồn đã ingest không dùng thuật ngữ này. Ý tương ứng có nguồn:
- Choudhry chia ALM gap thành liquidity gap (chênh lệch kỳ hạn) và interest-rate gap (chênh lệch cơ sở lãi suất của từng hợp đồng) [[src-choudhry-principles-banking#^choudhry-almb-7]].
- Lubinska: nếu kỳ refix của tài sản ngắn hơn của nợ, ngân hàng chịu reinvestment risk ngay cả khi kỳ hạn hợp đồng của tài sản dài hơn [[src-lubinska-alm-optimisation#^lubinska-u01-18]].

*Diễn giải:* hai claim trên cho thấy chuyển hoá lãi suất (theo kỳ tái định giá) tách khỏi chuyển hoá kỳ hạn (theo kỳ đáo hạn). Một khoản vay 5 năm thả nổi 3 tháng tạo maturity transformation nhưng gần như không tạo interest rate transformation (ngoài wiki, chưa có nguồn).

**Liquidity transformation** [cần nguồn]. Không source note nào định nghĩa. Claim gần nhất là về hệ quả: rủi ro thanh khoản là rủi ro không tái tài trợ được tài sản khi nợ đến hạn [[src-choudhry-principles-banking#^choudhry-almb-9]].

**Cơ chế hình thành NII/NIM.**

$$
\text{NII} = \text{Thu nhập lãi} - \text{Chi phí lãi}, \qquad \text{NIM} = \frac{\text{NII}}{\text{Tài sản sinh lãi}}
$$
[[src-choudhry-principles-banking#^choudhry-nim-2]]

- NII thường chiếm 40–80% tổng thu nhập; NIM bình quân ở UK, châu Âu, Mỹ khoảng 1–2,5%/năm, và không có mức NIM tối ưu vì phụ thuộc cơ cấu bảng cân đối [[src-choudhry-principles-banking#^choudhry-nim-14]].
- NII và NIM chịu tác động của cả mức lãi suất chung và thay đổi cơ cấu bảng cân đối; lãi suất tác động vì tài sản và nợ tái định giá ở các thời điểm khác nhau [[src-choudhry-principles-banking#^choudhry-nim-9]].
- FTP là ranh giới giữa maturity transformation và customer franchise [[src-choudhry-principles-banking#^choudhry-ftp-3]]; customer franchise là năng lực bán sản phẩm ở lãi suất khác lãi suất thị trường vốn [[src-choudhry-principles-banking#^choudhry-ftp-2]]. VAB định nghĩa NIM theo sản phẩm: phía tài sản là lãi suất cho vay trừ giá FTP bán vốn, phía nợ là giá FTP mua vốn trừ lãi suất huy động [[src-vab-ftp#^vab-ftp-40]].
- Ví dụ của Lubinska: asset centre +2,69%, liability centre −0,68% (chi phí vốn bên ngoài cao hơn FTP rate), ALM +0,99% [[src-lubinska-alm-optimisation#^lubinska-u01-16]].

*Diễn giải:* có thể viết NII thành tổng ba phần, đây là đồng nhất thức đại số chứ không phải công thức của nguồn (ngoài wiki, chưa có nguồn):

$$
\text{NII} = \underbrace{\textstyle\sum_a (r_a - \text{FTP}_a) A_a}_{\text{biên tài sản}} + \underbrace{\textstyle\sum_l (\text{FTP}_l - r_l) L_l}_{\text{biên nợ}} + \underbrace{\textstyle\sum_a \text{FTP}_a A_a - \sum_l \text{FTP}_l L_l}_{\text{kết quả chuyển hoá (ALM)}}
$$

Hai phần đầu khớp định nghĩa NIM theo sản phẩm của VAB [[src-vab-ftp#^vab-ftp-40]]; phần thứ ba là phần Choudhry gọi là lợi nhuận "rủi ro" của maturity transformation [[src-choudhry-principles-banking#^choudhry-ftp-13]].

**Case ChoudWest: tác động của lãi suất và cơ cấu** (bảng cân đối không đổi, không FTP, đường cong phẳng [[src-choudhry-principles-banking#^choudhry-nim-1]]):

| Kịch bản | NII | NIM | Nguồn |
|---|---|---|---|
| Cơ sở | £461,0m | 2,88% | [[src-choudhry-principles-banking#^choudhry-nim-2]] |
| Lãi suất +3% | £525,7m | 3,29% | [[src-choudhry-principles-banking#^choudhry-nim-4]] |
| Tăng liquidity buffer £1,5bn | £416m | 2,38% | [[src-choudhry-principles-banking#^choudhry-nim-5]] |
| Lãi suất giảm còn 4% | £431,5m | 2,70% | [[src-choudhry-principles-banking#^choudhry-nim-6]] |
| Tăng trưởng mortgage | £470,5m | 2,69% | [[src-choudhry-principles-banking#^choudhry-nim-8]] |

Kịch bản liquidity buffer có net cost of carry 3% (cost of funds 7,5% trừ lợi suất tài sản đệm 4,5%), nên giảm rủi ro thanh khoản làm giảm cả NII và NIM [[src-choudhry-principles-banking#^choudhry-nim-5]]. Kịch bản mortgage làm NII tăng nhưng NIM giảm, vì nghiệp vụ mới kém sinh lời hơn nghiệp vụ hiện có [[src-choudhry-principles-banking#^choudhry-nim-8]]. Xem [[net-interest-margin]].

**Rủi ro phát sinh.**

| Rủi ro | Cơ chế | Nguồn |
|---|---|---|
| Gap risk (income risk) | Lãi suất tiền gửi và funding thay đổi không đồng bộ làm mất thu nhập | [[src-choudhry-principles-banking#^choudhry-irr-2]] |
| Hướng theo dấu gap | Gap dương: asset sensitive, hưởng lợi khi lãi suất tăng; gap âm: liability sensitive, lỗ khi lãi suất tăng | [[src-choudhry-principles-banking#^choudhry-irrbb-5]] |
| Basis risk | Công cụ cùng kỳ hạn nhưng định giá theo chỉ số lãi suất khác nhau | [[src-bcbs-irrbb-2016#^irrbb-u02-2]] |
| Option risk | Quyền chọn tự động và quyền chọn hành vi nhúng trong tài sản, nợ, ngoại bảng | [[src-bcbs-irrbb-2016#^irrbb-u02-2]] |
| Funding gap risk | Tại mỗi điểm có liquidity gap: không huy động được vốn khi cần, hoặc lãi suất phải trả quá cao | [[src-choudhry-principles-banking#^choudhry-lgap-1]] |
| Refinancing / reinvestment risk | Kỳ hạn nợ ngắn hơn tài sản: refinancing risk; ngược lại: reinvestment risk | [[src-lubinska-alm-optimisation#^lubinska-u01-18]] |
| Rủi ro lãi suất từ nhu cầu funding tương lai | Ngân hàng không biết lãi suất sẽ phải trả cho khoản funding tương lai | [[src-choudhry-principles-banking#^choudhry-almb-9]] |

## Bằng chứng ủng hộ
- Định nghĩa maturity transformation và vai trò ranh giới của FTP chỉ có một nguồn T4 đứng sau (Choudhry Ch14) [[src-choudhry-principles-banking#^choudhry-ftp-1]] [[src-choudhry-principles-banking#^choudhry-ftp-3]]. Lubinska (T4) xác nhận độc lập rằng maturity transformation do ALM quản lý qua FTP [[src-lubinska-alm-optimisation#^lubinska-u01-16]].
- Khung ba nhóm vị thế và các loại quyền chọn có nguồn T2 (BCBS d368) [[src-bcbs-irrbb-2016#^irrbb-u05-1]] và T1 (TT83 Đ3.22) [[src-tt83-2025-nhnn#^d3-22]].
- Cơ chế NII/NIM dựa vào case ChoudWest (T4), một bảng cân đối giả định đơn giản hoá [[src-choudhry-principles-banking#^choudhry-nim-1]].

## Bằng chứng trái chiều
- Mẫu số NIM không thống nhất: tài sản sinh lãi trong case [[src-choudhry-principles-banking#^choudhry-nim-2]], "một thước đo tài sản bình quân" ở phần tóm tắt [[src-choudhry-principles-banking#^choudhry-nim-14]]. VAB định nghĩa NIM theo sản phẩm, so với FTP chứ không so với tài sản [[src-vab-ftp#^vab-ftp-40]]. Không phải conflict, nhưng so NIM giữa các nguồn cần thống nhất định nghĩa.
- Đánh đổi EV và earnings: khớp tái định giá ngoài kỳ hạn ngắn để triệt rủi ro EV có thể làm thu nhập biến động [[src-bcbs-irrbb-2016#^irrbb-u02-4]]. Vì vậy "giảm mismatch" không phải lúc nào cũng giảm rủi ro theo mọi thước đo.

## Phụ thuộc regime
- **Lãi suất tăng:** ngân hàng liability sensitive chịu lỗ [[src-choudhry-principles-banking#^choudhry-irrbb-5]]; với funding ngắn, biên có thể thu hẹp [[src-choudhry-principles-banking#^choudhry-hedge-1]]. Khách hàng chuyển từ tiền gửi không kỳ hạn sang có kỳ hạn [[src-tata-bank-alm#^tata-prac-2]], và tốc độ trả trước giảm [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
- **Lãi suất giảm:** ngân hàng nhiều tài sản nhạy lãi suất hơn nợ chịu giảm NII, như ChoudWest khi lãi suất xuống 4% [[src-choudhry-principles-banking#^choudhry-nim-6]]. Trả trước tăng [[src-bcbs-irrbb-2016#^irrbb-u05-5]], và tiền gửi không kỳ hạn tăng tỷ trọng [[src-tata-bank-alm#^tata-prac-1]].
- **Đường cong đảo ngược:** Choudhry nêu ngân hàng chuyển sang funding long [[src-choudhry-principles-banking#^choudhry-hedge-2]].
- **Mô hình kinh doanh:** ngân hàng tiết kiệm có tiền gửi không kỳ hạn lớn gặp vấn đề khi lãi suất âm [[src-tata-bank-alm#^tata-prac-3]].

## Hàm ý ALM / quy định
- **Nghĩa vụ NHNN (T1):** TT83 định nghĩa IRRBB và ba cấu phần gap, basis, option, kể cả khoản mục ngoại bảng [[src-tt83-2025-nhnn#^d3-22]]; phạm vi sổ ngân hàng theo Đ3.33 [[src-tt83-2025-nhnn#^d3-33]]. TT50 yêu cầu quản lý LCR VNĐ riêng lẻ [[src-tt50-2026-nhnn#^d16-2]].
- **Chưa có nguồn NHNN trong wiki** về NIM, về khái niệm maturity transformation hay liquidity transformation, và về cách phân nhóm sản phẩm theo dòng tiền cho mục đích ALM ngoài IRRBB.
- **Tham chiếu Basel (T2):** ba nhóm vị thế, CPR, TDRR, trần NMD core theo d368 [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-bcbs-irrbb-2016#^irrbb-u05-4]] là chuẩn Basel, không phải nghĩa vụ tại VN trừ khi TT83 nội luật hoá.
- *Diễn giải:* với ALCO, phân tích NII nên tách theo FTP ba phần (biên tài sản, biên nợ, kết quả chuyển hoá), vì chỉ phần thứ ba nhạy trực tiếp với hình dạng đường cong và là phần ALM chịu trách nhiệm; Table 1.10 của Choudhry liệt kê các hành động quản lý NIM tương ứng [[src-choudhry-principles-banking#^choudhry-nim-11]] (phần phân vai là ngoài wiki, chưa có nguồn).

## Bất định
- **Liquidity transformation** [cần nguồn]: chưa có source note nào. Cần /register một nguồn về lý thuyết trung gian tài chính, rồi /ingest. Gỡ Q2.
- **Interest rate transformation:** nguồn đã ingest không dùng thuật ngữ; phần trên dựa vào interest-rate gap và refix period. Mức phủ một phần.
- **Stub [[maturity-transformation]]** đã tạo (concept), kèm cạnh —exposed-to→ [[gap-risk]] (cite ^choudhry-hedge-1). Nội dung node chờ `/ingest --node maturity-transformation`.
- **Bảng mô tả từng sản phẩm** trong [[irrbb-balance-sheet-portfolios]] (mục 3.1–3.3, 5) phần lớn không có citation, nên synthesis này không dùng. Phải chạy `python tools/citations.py --node irrbb-balance-sheet-portfolios`.
- **Cạnh `gap-risk` —drives(−, rising_rate)→ `economic-value-of-equity`** cite [[src-bcbs-irrbb-2016#^irrbb-u07-1]], nhưng trích dẫn chỉ liệt kê sáu kịch bản sốc, không nói chiều tác động. Không dùng làm bằng chứng chiều; đề xuất /lint.
- Claim tóm tắt của [[src-lubinska-alm-optimisation#^lubinska-u01-16]] viết "chuyển hoá kỳ hạn và lãi suất", trong khi trích dẫn chỉ nói "maturity transformation". Diễn đạt lệch nhẹ, đề xuất rà khi /lint.
- Không có nguồn VN về cơ cấu bảng cân đối hệ thống ngân hàng (tương đương số liệu MFI Đức của Tata) [cần nguồn].
- [2026-10-22] ingest --node maturity-transformation: đã có node [[maturity-transformation]] (thêm claim refinancing risk ^lubinska-u01-21, rủi ro kép lãi suất – thanh khoản ^lubinska-u02-18, cạnh priced-by [[liquidity-transfer-pricing]]); cần rà lại Q2 (maturity transformation, rủi ro phát sinh) và dòng stub trong mục này.
