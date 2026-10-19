---
title: "Asset Encumbrance"
aliases: [Asset Encumbrance, Tài sản bị cầm cố, Tài sản bị ràng buộc, Contingent encumbrance, Structural subordination]
type: concept
domains: [alm, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [asset-encumbrance, collateral, structural-subordination, contingent-encumbrance, gone-concern, alco]
updated: 2026-10-19
reviewed:
---

## Ý chính
Asset encumbrance là việc tài sản của ngân hàng chịu các thoả thuận tài sản bảo đảm (financial collateral arrangements). Các thoả thuận này trao cho chủ nợ hoặc bên bảo lãnh quyền sở hữu tạm thời hoặc quyền ưu tiên trên tài sản [[src-choudhry-principles-banking#^choudhry-enc-1]].

Choudhry coi asset encumbrance là chỉ số "gone concern", vì mức encumbrance chỉ thực sự quan trọng khi ngân hàng vỡ nợ. LCR hay tỷ lệ cho vay/tiền gửi là chỉ số "going concern" [[src-choudhry-principles-banking#^choudhry-enc-6]].

## Cơ chế & drivers
**Nguồn phát sinh encumbrance**: ngân hàng encumber tài sản trong hoạt động thường ngày. Tài sản dùng làm tài sản bảo đảm trong repo, hoặc làm pool cho ABS và covered bond, đều bị encumber [[src-choudhry-principles-banking#^choudhry-enc-2]]. Xem [[securitisation]].

**Các cơ chế làm tăng rủi ro:**
- **Overcollateralisation**: tài sản bảo đảm có giá trị cao hơn phơi nhiễm được bảo đảm, thường qua haircut hoặc margin ratio [[src-choudhry-principles-banking#^choudhry-enc-3]].
- **Structural subordination**: do haircut, một phần tài sản mà chủ nợ có bảo đảm được ưu tiên lại do chủ nợ không bảo đảm tài trợ. Chủ nợ không bảo đảm vì vậy trở thành thứ cấp so với chủ nợ có bảo đảm [[src-choudhry-principles-banking#^choudhry-enc-4]].
- **Contingent encumbrance**: phần encumbrance tăng thêm khi stress. Mức này có thể tạo vòng phản hồi bất lợi tới khi ngân hàng hết tài sản đủ điều kiện và không còn khả năng huy động có bảo đảm [[src-choudhry-principles-banking#^choudhry-enc-5]].

**Thước đo.** Thước đo thường là biến thể của asset encumbrance ratio, tức tài sản bị encumber chia tổng tài sản [[src-choudhry-principles-banking#^choudhry-enc-8]].

| Tỷ lệ (Table 10.1) | Nguồn |
|---|---|
| Encumbered Assets / Total Assets | [[src-choudhry-principles-banking#^choudhry-enc-8]] |
| Encumbered assets and off-balance sheet collateral / Total assets and off-balance sheet collateral | [[src-choudhry-principles-banking#^choudhry-enc-8]] |
| Encumbered Assets / Assets available for encumbrance | [[src-choudhry-principles-banking#^choudhry-enc-8]] |
| Unsecured liabilities / Total unencumbered assets | [[src-choudhry-principles-banking#^choudhry-enc-8]] |
| Unsecured liabilities / Assets available for encumbrance | [[src-choudhry-principles-banking#^choudhry-enc-8]] |
| Unsecured debt excluding retail deposits / Assets available for encumbrance | [[src-choudhry-principles-banking#^choudhry-enc-8]] |

Hạn chế của các tỷ lệ này [[src-choudhry-principles-banking#^choudhry-enc-8]]:
- một số tài sản không hiện thực hoá được khi mất khả năng thanh toán;
- một số tài sản chưa encumber nhưng không thể encumber vì ràng buộc kinh tế hoặc pháp lý;
- tỷ lệ không phản ánh structural subordination do overcollateralisation.

**Khung quản trị encumbrance (Choudhry Ch10)** [[src-choudhry-principles-banking#^choudhry-enc-11]]:

| Bước | Nội dung | Nguồn |
|---|---|---|
| Định nghĩa và nhận diện | Nguồn encumbrance; tài sản đã encumber và chưa encumber nhưng có thể encumber | [[src-choudhry-principles-banking#^choudhry-enc-11]] |
| Xây dựng và tích hợp | Chỉ số theo mô hình kinh doanh, hiệu chỉnh vùng warm/hot, MI; tích hợp với chính sách tín dụng, thanh khoản, thị trường, CFP, FTP, quản lý tài sản bảo đảm, sản phẩm mới, stress test | [[src-choudhry-principles-banking#^choudhry-enc-11]] |
| Đo lường và theo dõi | Theo dõi mức, diễn biến, loại tài sản; stress test contingent encumbrance | [[src-choudhry-principles-banking#^choudhry-enc-11]] |
| Quản lý chủ động | Quản lý vị thế encumbrance theo chính sách; đánh giá lại khung | [[src-choudhry-principles-banking#^choudhry-enc-11]] |

Chính sách asset encumbrance nên được Board phê duyệt và rà soát ít nhất hằng năm [[src-choudhry-principles-banking#^choudhry-hacc-5]]. Ngân hàng dùng nhiều funding có bảo đảm nên đưa hạn mức encumbrance vào RAS [[src-choudhry-principles-banking#^choudhry-salm-10]]; xem [[risk-appetite]].

## Phụ thuộc regime
Rủi ro từ encumbrance thường tăng trong khủng hoảng: giá tài sản bảo đảm giảm, haircut cao hơn, và margin bổ sung cho rủi ro đối tác [[src-choudhry-principles-banking#^choudhry-enc-5]].

## Góc nhìn theo domain
- **ALM**: encumbrance cao có thể làm giảm khả năng huy động thêm hoặc làm tăng chi phí funding. Vì vậy ALCO cần nắm rõ mức encumbrance của ngân hàng [[src-choudhry-principles-banking#^choudhry-enc-7]]. Chính sách ALM nên bao gồm cách xử lý và khẩu vị đối với asset encumbrance, kể cả hạn mức encumbrance [[src-choudhry-principles-banking#^choudhry-enc-10]]. Xem [[alco]].
- **Basel**: theo Choudhry, LCR và NSFR ưu đãi funding có bảo đảm và covered bond [[src-choudhry-principles-banking#^choudhry-enc-9]]. Xem [[lcr]], [[nsfr]], [[rsf-securities-financing-and-encumbrance]].
- **Quy định ở các nước**: Australia, Canada và Singapore đặt giới hạn asset encumbrance [[src-choudhry-principles-banking#^choudhry-enc-9]].
- **VN**: [cần nguồn]

*Diễn giải:* trong NSFR, tài sản bị encumber chịu hệ số RSF cao hơn theo thời gian encumber ([[rsf-securities-financing-and-encumbrance]]). Đó là cách Basel đưa encumbrance vào một chỉ số going concern, khác góc nhìn gone concern của Choudhry.

## Bằng chứng thực nghiệm
[cần nguồn] Phần số liệu repo-haircut index 2007–2008 (Gorton và Metrick, 2012) nằm trong raw u14 nhưng chưa trích.

## Câu hỏi mở
- TT50/2026 hay TT83/2025 có hạn mức encumbrance không [cần nguồn].
