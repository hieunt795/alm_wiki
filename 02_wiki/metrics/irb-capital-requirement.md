---
title: "IRB Capital Requirement (K) and Risk Weight"
aliases: [IRB Capital Requirement, Yêu cầu vốn K theo IRB, Trọng số rủi ro IRB, Công thức RWA theo IRB cho doanh nghiệp]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[customer-credit-risk-rwa]]", cite: "[[src-tt14-2025-nhnn#^d41-2ab]]"}
tags: [capital, credit-risk, irb, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Yêu cầu vốn K là tỷ lệ vốn trên EAD mà công thức IRB của TT14/2025 suy ra từ PD, LGD, hệ số tương quan R và kỳ hạn M; trọng số rủi ro IRB bằng K nhân 12,5 [[src-tt14-2025-nhnn#^d41-2ab]]. Đ41 áp dụng cho khoản phải đòi doanh nghiệp, Đ49 cho bán lẻ. Đ49 áp dụng cho khoản phải đòi bán lẻ; khoản mua lại khoản phải thu dùng cùng công thức qua [[purchased-receivables-rwa]]. Xem [[internal-ratings-based-approach]].

## Công thức
$$
RWA = \sum RW_i \times EAD_i
$$
[[src-tt14-2025-nhnn#^d41-2ab]]

$$
RW = K \times 12{,}5
$$
[[src-tt14-2025-nhnn#^d41-2ab]]

$$
K = \left[ LGD \times N\left( \frac{G(PD)}{\sqrt{1-R}} + \sqrt{\frac{R}{1-R}} \times G(0{,}999) \right) - PD \times LGD \right] \times \frac{1 + (M - 2{,}5) \times b}{1 - 1{,}5 \times b}
$$
[[src-tt14-2025-nhnn#^d41-2c]]

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $PD$ | Xác suất vỡ nợ | [[probability-of-default]] | [[src-tt14-2025-nhnn#^d41-1]] |
| $LGD$ | Tỷ lệ tổn thất khi vỡ nợ | [[loss-given-default]] | [[src-tt14-2025-nhnn#^d41-1]] |
| $EAD_i$ | Giá trị khoản phải đòi tại thời điểm vỡ nợ | [[exposure-at-default]] | [[src-tt14-2025-nhnn#^d41-2ab]] |
| $R$ | Hệ số tương quan | [[asset-correlation]] | [[src-tt14-2025-nhnn#^d41-2d]] |
| $M$, $b$ | Thời hạn hiệu lực và điều chỉnh kỳ hạn | [[maturity-adjustment]] | [[src-tt14-2025-nhnn#^d41-2dd]] |
| $N(x)$, $G(z)$ | Hàm phân phối tích lũy chuẩn hóa và hàm nghịch đảo | | [[src-tt14-2025-nhnn#^d41-2dd]] |

## Diễn giải
$RW_i$ và $EAD_i$ xác định theo PD, LGD của từng phần giá trị khoản phải đòi, nên một khoản có tài sản bảo đảm, bảo lãnh hoặc phái sinh tín dụng được tách thành nhiều phần với tham số khác nhau [[src-tt14-2025-nhnn#^d41-2ab]]. Cách tách xem [[irb-credit-risk-mitigation]] và [[loss-given-default]].

*Diễn giải:* K có dạng công thức một nhân tố, trong đó $G(0{,}999)$ là phân vị 99,9% của nhân tố hệ thống và $PD \times LGD$ trừ tổn thất dự kiến khỏi tổn thất ở phân vị đó. Nguồn TT14 chỉ nêu công thức, không giải thích cấu trúc này. Phần giải thích là suy luận từ dạng công thức [cần nguồn Basel CRE31].

**Khoản phải đòi bán lẻ (Đ49).** RWA = RW × EAD, RW = K × 12,5, nhưng K của bán lẻ không có nhân tử kỳ hạn: $K = LGD \times N\left( \frac{G(PD)}{\sqrt{1-R}} + \sqrt{\frac{R}{1-R}} \times G(0{,}999) \right) - PD \times LGD$ [[src-tt14-2025-nhnn#^d49-2]] [[src-tt14-2025-nhnn#^d49-4]]. Ngân hàng phải tự tính PD, LGD và EAD [[src-tt14-2025-nhnn#^d49-1]]. R theo từng nhóm xem [[asset-correlation]]; sàn tham số xem [[irb-retail-parameter-estimation]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| RW | [cần nguồn] (CRE31 chưa ingest) | $K \times 12{,}5$ [[src-tt14-2025-nhnn#^d41-2ab]] | Đ41.2b | Áp dụng khi được NHNN chấp thuận IRB ([[irb-approval-process]]) |
| M mặc định | [cần nguồn] | 2,5 năm cho khoản phải đòi doanh nghiệp [[src-tt14-2025-nhnn#^d48-1]] | Đ48 | Như trên |
| K bán lẻ | [cần nguồn] | K không có nhân tử kỳ hạn của Đ41.2c [[src-tt14-2025-nhnn#^d49-2]] | Đ49.2c | Khi áp dụng IRB |

## Ứng dụng trong ALM
*Diễn giải:* K tăng theo PD và LGD, nên dịch chuyển xếp hạng nội bộ hoặc cơ cấu tài sản bảo đảm đổi RWA trực tiếp. RWA theo IRB bị chặn dưới bởi [[output-floor]], nên lợi ích vốn của IRB so với phương pháp tiêu chuẩn có giới hạn.

## Nhầm lẫn thường gặp
- $\sum RW_i \times EAD_i$ dùng EAD sau bù trừ nội bảng và CCF theo Đ47, không phải số dư gốc [[src-tt14-2025-nhnn#^d47-1]].
- K đã trừ $PD \times LGD$; tổn thất dự kiến không nằm trong K và được xử lý riêng với dự phòng rủi ro, xem [[irb-expected-loss]] và [[el-provision-difference-treatment]] (cách đọc "không nằm trong K" là suy luận từ công thức K).
