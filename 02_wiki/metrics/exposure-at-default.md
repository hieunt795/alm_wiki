---
title: "Exposure at Default"
aliases: [Exposure at Default, EAD, Giá trị khoản phải đòi tại thời điểm khách hàng vỡ nợ]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[irb-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d41-2ab]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Giá trị khoản phải đòi tại thời điểm khách hàng vỡ nợ (EAD) là giá trị khoản phải đòi hoặc giá trị dự kiến tại thời điểm khách hàng vỡ nợ, tính bằng đồng Việt Nam [[src-tt14-2025-nhnn#^d2-31]]. Với khoản phải đòi doanh nghiệp, EAD gồm số dư gốc, lãi phải thu và phí phải thu đang hạch toán vào thu nhập [[src-tt14-2025-nhnn#^d47-1]].

## Công thức
$$
EAD_i = EADon_i - L_i^{*} \times (1 - H_{fxl}) + EADoff_i \times CCF_i
$$
[[src-tt14-2025-nhnn#^d47-1]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $EADon_i$ | Số dư phần nội bảng của khoản phải đòi thứ i | [[src-tt14-2025-nhnn#^d47-1]] |
| $EADoff_i$ | Số dư phần cam kết ngoại bảng | [[src-tt14-2025-nhnn#^d47-1]] |
| $CCF_i$ | Hệ số chuyển đổi của phần ngoại bảng, Đ10 ([[credit-conversion-factor]]) | [[src-tt14-2025-nhnn#^d47-2]] |
| $L_i^{*}$, $H_{fxl}$ | Theo Đ27.2 và Đ27.3 ([[on-balance-sheet-netting]]) khi đáp ứng Đ25 và Đ27.1; bằng 0 nếu không đáp ứng | [[src-tt14-2025-nhnn#^d47-1]] |

Nếu $EAD_i < 0$ thì $EAD_i$ bằng 0 [[src-tt14-2025-nhnn#^d47-1]].

## Diễn giải
- Phần ngoại bảng chuyển đổi theo CCF của Đ10. Số dư áp CCF là giá trị thấp hơn giữa hạn mức tín dụng đã cam kết chưa sử dụng và hạn mức mà ngân hàng có thể cấp thêm theo quy định nội bộ, với điều kiện có quy trình quản lý và giám sát hạn mức đó [[src-tt14-2025-nhnn#^d47-2]].
- Cấu trúc tương tự giá trị khoản phải đòi $E_i$ của phương pháp tiêu chuẩn, nhưng bù trừ nội bảng nằm trong chính EAD [[exposure-value]].

**Khoản phải đòi bán lẻ (Đ53).** EAD là giá trị lớn hơn giữa EAD ngân hàng tính và EAD sàn; EAD sàn bằng số dư nội bảng cộng 50% của số dư ngoại bảng nhân CCF của phương pháp tiêu chuẩn [[src-tt14-2025-nhnn#^d53-1]]. Chỉ giảm được EAD tự ước tính và EAD sàn bằng bù trừ nội bảng đáp ứng Đ25 và Đ27 [[src-tt14-2025-nhnn#^d53-23]]. Yêu cầu ước tính EAD xem [[irb-retail-parameter-estimation]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| EAD khoản phải đòi doanh nghiệp | [cần nguồn] (CRE32 chưa ingest) | $EADon - L^{*}(1 - H_{fxl}) + EADoff \times CCF$ [[src-tt14-2025-nhnn#^d47-1]] | Đ47.1 | Khi áp dụng IRB |
| EAD sàn bán lẻ | [cần nguồn] | Nội bảng + 50% × ngoại bảng × CCF tiêu chuẩn [[src-tt14-2025-nhnn#^d53-1]] | Đ53.1 | Khi áp dụng IRB |

## Ứng dụng trong ALM
*Diễn giải:* hạn mức cam kết chưa giải ngân tác động vào EAD qua CCF, nên chính sách hạn mức và quy trình giám sát hạn mức có thể đổi EAD. Điều kiện "đủ quy trình quản lý và giám sát hạn mức" ở Đ47.2 cho phép thu hẹp phần cam kết tính vào EAD.

## Nhầm lẫn thường gặp
- Đ47.2b và Đ47.2c trong bản raw gần như trùng nhau, chỉ khác "có thể cấp thêm" và "thực tế có thể cấp"; chưa đối chiếu bản gốc để xác định ý định (xem ghi chú convert trong [[src-tt14-2025-nhnn]]).
