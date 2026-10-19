---
title: "Effective Interest Rate"
aliases: [Effective Interest Rate, EIR, Lãi suất thực tế, Lãi suất hiệu dụng, Phương pháp lãi suất thực]
type: metric
domains: [alm, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [eir, ifrs-9, amortised-cost, income-recognition, hqla, behavioural]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
Effective interest rate (EIR) là cách ghi nhận thu nhập theo lợi suất đều, phân bổ các khoản phí và hoa hồng gắn liền qua vòng đời kỳ vọng của tài sản [[src-choudhry-principles-banking#^choudhry-eir-1]].

## Công thức
[cần nguồn] Nguồn đã ingest định nghĩa EIR bằng lời, không có công thức tường minh.

**Quy tắc tính và đặt lại:**

| Quy tắc | Nội dung | Nguồn |
|---|---|---|
| Thời điểm tính | Khi ghi nhận ban đầu; cố định suốt đời tài sản | [[src-choudhry-principles-banking#^choudhry-eir-2]] |
| Thay đổi dòng tiền kỳ vọng | Ghi thẳng vào P&L, là chênh lệch hai bộ dòng tiền chiết khấu theo EIR gốc | [[src-choudhry-principles-banking#^choudhry-eir-2]] |
| Đặt lại EIR | Chỉ khi lãi suất thị trường của tài sản thả nổi thay đổi | [[src-choudhry-principles-banking#^choudhry-eir-2]] |
| Sản phẩm lãi suất bậc thang | Phải giả định thời gian khách hàng ở mức lãi cao trước khi chuyển | [[src-choudhry-principles-banking#^choudhry-eir-1]] |

## Diễn giải
EIR là lãi suất hành vi. Nó chịu ảnh hưởng của hành vi khách hàng, kể cả phản ứng với điều kiện tín dụng chung [[src-choudhry-principles-banking#^choudhry-eir-2]].

*Diễn giải:* vì EIR dựa trên vòng đời kỳ vọng, giả định prepayment trong mô hình IRRBB và giả định vòng đời trong EIR nên nhất quán. Xem [[behavioural-options]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Phương pháp ghi nhận lãi | Không thuộc phạm vi các chuẩn Basel đã ingest | [cần nguồn] | | |

*Diễn giải:* EIR là khái niệm kế toán, nguồn trình bày cùng mục IFRS 9. Chuẩn mực kế toán VN tương ứng chưa có nguồn trong wiki.

## Ứng dụng trong ALM
- HQLA đo theo amortised cost hoặc FVTOCI đều chịu ảnh hưởng của phương pháp EIR. EIR cũng liên quan tới tiền gửi, vì tiền gửi ghi nhận theo amortised cost [[src-choudhry-principles-banking#^choudhry-eir-3]].
- EIR có thể ảnh hưởng giá trị ghi sổ của HQLA và tiền gửi, nên cần xét trong tính LCR. Khi xét tác động P&L lên HQLA, EIR phân bổ premium hoặc discount qua vòng đời kỳ vọng của tài sản [[src-choudhry-principles-banking#^choudhry-eir-3]]. Xem [[hqla]], [[lcr]].
- Chính sách EIR nên được Board phê duyệt và rà soát ít nhất hằng năm [[src-choudhry-principles-banking#^choudhry-hacc-5]].

## Nhầm lẫn thường gặp
- EIR khác lãi suất hợp đồng: thu nhập và chi phí lãi được ghi nhận qua P&L theo EIR, không chỉ theo lãi suất hợp đồng [[src-choudhry-principles-banking#^choudhry-eir-3]].
