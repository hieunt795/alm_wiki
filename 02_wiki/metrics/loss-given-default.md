---
title: "Loss Given Default"
aliases: [Loss Given Default, LGD, Tỷ lệ tổn thất khi khách hàng vỡ nợ]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[irb-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d41-1]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Tỷ lệ tổn thất khi khách hàng vỡ nợ (LGD) là tỷ lệ giữa giá trị tổn thất và giá trị khoản phải đòi tại thời điểm khách hàng vỡ nợ, đo bằng số thập phân hoặc phần trăm [[src-tt14-2025-nhnn#^d2-31]]. Với khoản phải đòi doanh nghiệp, LGD do Thông tư ấn định theo loại bên vay và tài sản bảo đảm (IRB cơ bản) [[src-tt14-2025-nhnn#^d43-1]].

## Công thức
LGD khi không giảm thiểu rủi ro [[src-tt14-2025-nhnn#^d43-1]]:

| Loại khoản phải đòi | LGD | Nguồn |
|---|---|---|
| Nợ thứ cấp của doanh nghiệp | 75% | [[src-tt14-2025-nhnn#^d43-1]] |
| Khoản phải đòi của công ty chứng khoán, công ty bảo hiểm | 45% | [[src-tt14-2025-nhnn#^d43-1]] |
| Khoản phải đòi của doanh nghiệp khác | 40% | [[src-tt14-2025-nhnn#^d43-1]] |

LGD sau khi dùng tài sản bảo đảm đủ điều kiện:

$$
LGD^{*} = LGD_u \times \frac{E_u}{E} + \sum_i \left( LGD_{S_i} \times \frac{E_{S_i}}{E} \right)
$$
[[src-tt14-2025-nhnn#^d44-2]]

Giá trị tài sản bảo đảm sau hiệu chỉnh:

$$
C_i^{*} = C_i \times \frac{t_i - 0{,}25}{T - 0{,}25} \times (1 - H_{c_i} - H_{fxc_i})
$$
[[src-tt14-2025-nhnn#^d44-3]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $E$ | Số dư khoản phải đòi còn lại sau khi trừ bảo lãnh $G_l^{*}$ và phái sinh tín dụng $CD_n^{*}$ | [[src-tt14-2025-nhnn#^d44-2]] |
| $E_{S_i}$ | Phần số dư được đảm bảo bằng $C_i^{*}$, $E_{S_i} = C_i^{*}$ và $\sum E_{S_i} \le E$ | [[src-tt14-2025-nhnn#^d44-2]] |
| $E_u$ | Phần không được bảo đảm, $E_u = E - \sum E_{S_i}$ | [[src-tt14-2025-nhnn#^d44-2]] |
| $LGD_u$ | LGD của phần không giảm thiểu rủi ro (Đ43.1b) | [[src-tt14-2025-nhnn#^d44-2]] |
| $LGD_{S_i}$ | LGD của phần có tài sản bảo đảm thứ i, theo bảng dưới | [[src-tt14-2025-nhnn#^d44-4]] |
| $C_i$ | Giá trị tài sản bảo đảm thứ i | [[src-tt14-2025-nhnn#^d44-3]] |
| $T$ | Giá trị nhỏ hơn giữa 05 năm và thời hạn còn lại của khoản phải đòi (năm) | [[src-tt14-2025-nhnn#^d44-3]] |
| $t_i$ | Giá trị nhỏ hơn giữa $T$ và thời hạn còn lại của tài sản bảo đảm thứ i (năm) | [[src-tt14-2025-nhnn#^d44-3]] |
| $H_{c_i}$ | Hệ số hiệu chỉnh tài sản bảo đảm theo bảng dưới | [[src-tt14-2025-nhnn#^d44-4]] |
| $H_{fxc_i}$ | Hệ số hiệu chỉnh độ lệch tiền tệ, 8% | [[src-tt14-2025-nhnn#^d44-3]] |

LGD_S và Hc theo loại tài sản bảo đảm [[src-tt14-2025-nhnn#^d44-4]]:

| Loại tài sản bảo đảm | $LGD_S$ | $H_c$ |
|---|---|---|
| Tài sản được ghi nhận theo Đ26 ([[eligible-collateral-haircuts]]) | 0% | Như phương pháp tiêu chuẩn |
| Đủ tiêu chuẩn theo Đ44.1b (Đ16.3a và có bảo hiểm thiệt hại, hỏng hóc) | 20% | 40% |
| Khác theo Đ44.1c (tài sản hữu hình không phải bất động sản, có giá thị trường) | 25% | 50% |

## Diễn giải
- Tài sản bảo đảm đủ điều kiện gồm ba nhóm; nhóm c đòi hỏi quyền ưu tiên thanh toán, mô tả chi tiết trong hợp đồng, quyền kiểm tra và định giá lại, và xử lý trong không quá 01 năm kể từ khi có quyền xử lý [[src-tt14-2025-nhnn#^d44-1]].
- Tài sản bảo đảm không đủ điều kiện thì khoản phải đòi tính LGD như khoản không giảm thiểu rủi ro [[src-tt14-2025-nhnn#^d44-5]].
- Khi dùng nhiều biện pháp giảm thiểu, tổng giá trị phân bổ không vượt tổng giá trị biện pháp đủ điều kiện và không vượt EAD từng khoản [[src-tt14-2025-nhnn#^d43-23]].
- LGD của phần được bảo lãnh hoặc phái sinh tín dụng lấy của bên bảo lãnh hoặc bên phát hành, xem [[irb-credit-risk-mitigation]] [[src-tt14-2025-nhnn#^d45-3]] [[src-tt14-2025-nhnn#^d46-3]].

*Diễn giải:* $LGD^{*}$ là trung bình có trọng số theo giá trị, nên phần tài sản bảo đảm Đ26 có $LGD_S$ bằng 0% kéo LGD hiệu dụng xuống theo tỷ lệ $E_{S_i}/E$.

**Khoản phải đòi bán lẻ (Đ51).** LGD là giá trị lớn hơn giữa LGD ngân hàng tính và LGD sàn [[src-tt14-2025-nhnn#^d51-1]]. Tài sản bảo đảm đủ điều kiện gồm tài sản đáp ứng Đ44.1a, b, c và nhà ở xã hội đáp ứng Đ16.4 [[src-tt14-2025-nhnn#^d51-2]].

| Trường hợp | LGD sàn | Nguồn |
|---|---|---|
| Bảo đảm toàn bộ, cho vay thế chấp nhà ở | 5% | [[src-tt14-2025-nhnn#^d51-3a]] |
| Bảo đảm toàn bộ, bán lẻ khác, tài sản Đ44.1a | 0% | [[src-tt14-2025-nhnn#^d51-3a]] |
| Bảo đảm toàn bộ, bán lẻ khác, bất động sản Đ44.1b | 10% | [[src-tt14-2025-nhnn#^d51-3a]] |
| Bảo đảm toàn bộ, bán lẻ khác, tài sản Đ44.1c | 15% | [[src-tt14-2025-nhnn#^d51-3a]] |
| Không bảo đảm hoặc tài sản không đủ điều kiện, QRRE | 50% | [[src-tt14-2025-nhnn#^d51-3c]] |
| Không bảo đảm hoặc tài sản không đủ điều kiện, bán lẻ khác | 30% | [[src-tt14-2025-nhnn#^d51-3c]] |

Bảo đảm một phần thì LGD sàn* là trung bình có trọng số theo giá trị của LGD sàn từng phần, cùng cấu trúc với $LGD^{*}$ ở trên [[src-tt14-2025-nhnn#^d51-3b]]. Yêu cầu ước tính LGD (không thấp hơn LGD trung bình dài hạn, LGD suy thoái, dữ liệu thu hồi lịch sử, quan sát tối thiểu 05 năm) xem [[irb-retail-parameter-estimation]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| LGD nợ thứ cấp | [cần nguồn] (CRE32 chưa ingest) | 75% [[src-tt14-2025-nhnn#^d43-1]] | Đ43.1a | Khi áp dụng IRB |
| LGD công ty chứng khoán, bảo hiểm | [cần nguồn] | 45% [[src-tt14-2025-nhnn#^d43-1]] | Đ43.1b(i) | Như trên |
| LGD doanh nghiệp khác | [cần nguồn] | 40% [[src-tt14-2025-nhnn#^d43-1]] | Đ43.1b(ii) | Như trên |
| $LGD_S$ / $H_c$ tài sản bảo đảm đủ tiêu chuẩn / khác | [cần nguồn] | 20% / 40% và 25% / 50% [[src-tt14-2025-nhnn#^d44-4]] | Đ44.4 | Như trên |
| LGD sàn bán lẻ | [cần nguồn] | 5% thế chấp nhà ở; 0% / 10% / 15% theo tài sản; 50% QRRE và 30% khác khi không bảo đảm [[src-tt14-2025-nhnn#^d51-3a]] [[src-tt14-2025-nhnn#^d51-3c]] | Đ51.3 | Khi áp dụng IRB |

## Ứng dụng trong ALM
*Diễn giải:* LGD cố định theo Thông tư với khoản phải đòi doanh nghiệp, nên đòn bẩy quản trị nằm ở cấu trúc tài sản bảo đảm và bảo lãnh. Kỳ hạn còn lại của tài sản bảo đảm so với khoản vay (hệ số $(t_i - 0{,}25)/(T - 0{,}25)$) làm giá trị ghi nhận giảm khi tài sản đáo hạn sớm hơn khoản vay.

## Nhầm lẫn thường gặp
- LGD 75% chỉ áp cho nợ thứ cấp của doanh nghiệp; không phải mặc định cho mọi khoản phải đòi [[src-tt14-2025-nhnn#^d43-1]].
- LGD cho khoản phải đòi bán lẻ do ngân hàng tự ước tính theo AIRB, thuộc C3-M5 [cần nguồn].
