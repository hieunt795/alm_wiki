---
title: Secured funding (LCR)
aliases: [Secured funding, Nguồn vốn có bảo đảm, Repo funding]
type: metric
domains: [alm, basel, vn-reg, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-45]]"}
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr40-46]]"}
tags: [repo, collateral, liquidity]
updated: 2026-10-21
reviewed:
---

## Định nghĩa

Nợ có bảo đảm bằng quyền pháp lý trên tài sản cụ thể của ngân hàng khi phá sản hoặc thanh lý. Không gồm giao dịch bảo đảm bằng tài sản không giao dịch được trên thị trường (nhà xưởng, thiết bị), trừ khi đối tác là NHTW [[src-bcbs-lcr#^lcr40-45]]. Nhóm này gồm repo, collateral swap và các giao dịch tương tự.

## Công thức & tham số

### Cơ chế & drivers
Trong stress, khả năng tái tục repo **phụ thuộc chất lượng tài sản bảo đảm**, không phụ thuộc đối tác:

| Tài sản bảo đảm / đối tác | Dòng ra | Nguồn |
|---|---|---|
| Level 1 hoặc với NHTW | 0% | [[src-bcbs-lcr#^lcr40-47]] [[src-bcbs-lcr#^lcr40-48]] |
| Level 2A | 15% | [[src-bcbs-lcr#^lcr40-48]] |
| Với chính phủ, PSE (RW ≤ 20%), MDB trong nước, tài sản bảo đảm không phải L1/L2A | 25% | [[src-bcbs-lcr#^lcr40-47]] |
| RMBS đủ điều kiện Level 2B | 25% | [[src-bcbs-lcr#^lcr40-48]] |
| Level 2B khác | 50% | [[src-bcbs-lcr#^lcr40-48]] |
| Còn lại | 100% | [[src-bcbs-lcr#^lcr40-48]] |

**Hoán đổi TSBĐ và Cho vay bán khống (*Collateral Swaps & Customer Shorts*)**:
Theo [[src-bcbs-lcr#^lcr40-46]], giao dịch hoán đổi tài sản bảo đảm (*collateral swaps*) được xử lý tương đương repo/reverse repo. Tài sản mà ngân hàng cho khách hàng mượn để thực hiện bán khống (*customer short positions*) cũng được xử lý như một hình thức secured funding, với dòng tiền ra tính trên số tiền huy động được chứ không tính trên giá trị tài sản làm gốc [[src-bcbs-lcr#^lcr40-46]]. Vị thế bán khống của khách hàng xử lý theo giả định roll-off của LCR40.48, tách biệt với vị thế bán khống của chính ngân hàng [[src-bcbs-lcr#^lcr40-79-faq]]. Cho mượn tài sản non-HQLA nhận làm TSBĐ cho margin loan để bù vị thế bán khống của khách hàng khác: dòng ra 50% theo LCR40.73, đối xứng với inflow 50% của margin loan, tuỳ quyết định quốc gia [[src-bcbs-lcr#^lcr40-73-faq]].

**Quy tắc phân bổ danh mục tài sản thế chấp hỗn hợp (*Collateral Pool Waterfall*)**:
- Basel: Nếu ngân hàng cầm cố một nhóm tài sản hỗn hợp (*pool of assets*) và không thể tách bạch tài sản nào bảo đảm cho giao dịch có kỳ hạn $> 30$ ngày, chuẩn mực yêu cầu gán tài sản có giá trị thanh khoản thấp nhất (haircut cao nhất hoặc non-HQLA) cho các giao dịch có kỳ hạn dài nhất trước, nhằm dành tối đa tài sản chất lượng cao cho các nghĩa vụ ngắn hạn [[src-bcbs-lcr#^lcr40-48]].
- VN: TT50 PL1.B.III.3.2.1.b quy định nguyên tắc tương ứng: tài sản được áp dụng hệ số rút tiền cao nhất khi tính LCR sẽ được sử dụng trước cho các giao dịch có thời gian đáo hạn ngắn nhất trước [[src-tt50-2026-nhnn#^pl1-b3-3]].

**Tài trợ cho vị thế bán khống của chính ngân hàng (*Firm Shorts Funding*)**:
Theo [[src-bcbs-lcr#^lcr40-80]], nếu vị thế bán khống của ngân hàng được bù đắp bằng việc vay chứng khoán không bảo đảm, ngân hàng phải tính dòng ra 100% (do đối tác sẽ đòi lại chứng khoán). Nếu bù đắp bằng giao dịch tài trợ chứng khoán có bảo đảm, vị thế được giả định duy trì trong 30 ngày và nhận dòng ra 0%.

Chiều ngược lại (reverse repo, dòng vào): bảo đảm bằng L1 thì giả định được roll-over, inflow 0%. Bảo đảm bằng L2 thì inflow bằng haircut. Bảo đảm bằng tài sản không phải HQLA thì inflow 100% [[src-bcbs-lcr#^lcr40-78]]. Nếu TSBĐ nhận về dùng để bù đắp vị thế bán khống thì inflow nhận 0% [[src-bcbs-lcr#^lcr40-79]]. Xem chi tiết tại [[cash-inflows]].

## Diễn giải

### Phụ thuộc regime
*Diễn giải:* trong stress toàn thị trường, haircut trên repo tăng và thị trường repo với tài sản kém chất lượng có thể đóng băng. Bảng trên là giả định tĩnh của chuẩn mực.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **Product**: repo/reverse repo là công cụ quản lý thanh khoản ngắn hạn. Node instrument `repo` chưa có.
- **ALM**: *Diễn giải* — nguồn vốn có bảo đảm bằng trái phiếu chính phủ (Level 1) gần như không làm tăng dòng ra LCR. Đây là lợi thế của danh mục trái phiếu chính phủ ngoài vai trò HQLA.
- **VN**: theo [[tt50-2026|TT50/2026]], nguồn vốn bán buôn có bảo đảm bằng HQLA cấp 1 hoặc trong giao dịch với NHNN có hệ số rút tiền 0%; bằng HQLA cấp 2A 15%; bằng tài sản khác với Chính phủ, KBNN, UBND, ngân hàng chính sách, VAMC, DATC, BHTG, BHXH, tổ chức quốc tế 25%; RMBS cấp 2B 25%; cấp 2B khác 50%; tài sản tài chính khác 100% [[src-tt50-2026-nhnn#^pl1-b3-3]]. Nguồn vốn có bảo đảm là nguồn được thế chấp bằng tài sản tài chính thuộc sở hữu ngân hàng (kể cả repo); hệ số áp cho nguồn đang được bảo đảm tại thời điểm tính LCR [[src-tt50-2026-nhnn#^pl1-b3-31]]. Như vậy repo với NHNN có hệ số 0% bất kể loại tài sản bảo đảm.

## Câu hỏi mở (Đã giải quyết)
- *Repo với NHNN (OMO) có được 0% không*: Đã được quy định rõ tại Bảng 4 điểm a TT50: Nguồn vốn được bảo đảm bằng HQLA cấp 1 hoặc trong giao dịch với Ngân hàng Nhà nước áp dụng hệ số rút tiền 0% [[src-tt50-2026-nhnn#^pl1-b3-3]]. Do đó mọi giao dịch repo với NHNN đều hưởng hệ số 0%.
