---
title: "Cash-flow Survival Period"
aliases: [Cash-flow Survival Period, Survival period, Thời gian tồn tại dòng tiền, Survival horizon]
type: metric
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[ilaap]]", cite: "[[src-choudhry-principles-banking#^choudhry-ilaap-5]]"}
  - {type: measures, to: "[[liquidity-risk-management]]", cite: "[[src-choudhry-principles-banking#^choudhry-ilaap-5]]"}
tags: [liquidity, stress-test, risk-appetite]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
Cash-flow survival period là số ngày mà nguồn thanh khoản của ngân hàng (tài sản thanh khoản, dòng tiền vào, giải ngân hạn mức dự phòng) bù được dòng ra giả định trong một kịch bản stress. Đây là output chính của liquidity stress testing [[src-choudhry-principles-banking#^choudhry-ilaap-5]] [[src-choudhry-principles-banking#^choudhry-st-19]].

## Công thức
*Diễn giải (tái dựng, chưa đối chiếu bản gốc):* nguồn chỉ mô tả bằng lời. Gọi $L_0$ là nguồn thanh khoản ban đầu, $I_s$ và $O_s$ là dòng vào và dòng ra stress của ngày $s$. Survival period là ngày cuối cùng trước khi số dư thanh khoản lũy kế âm:

$$SP = \max\left\{ t : L_0 + \sum_{s=1}^{t} (I_s - O_s) \ge 0 \right\}$$
[[src-choudhry-principles-banking#^choudhry-ilaap-5]]

## Diễn giải
- Ngân hàng đặt survival period tối thiểu trong Liquidity Risk Appetite Statement [[src-choudhry-principles-banking#^choudhry-ilaap-5]].
- OLAR của PRA yêu cầu dự trữ thanh khoản đủ cho stress phù hợp khẩu vị tự công bố; 92 ngày trong ví dụ Figure 20.16 do ngân hàng tự chọn [[src-choudhry-principles-banking#^choudhry-ilaap-6]].

| Ví dụ khẩu vị trong nguồn | Giá trị | Nguồn |
|---|---|---|
| Board ngân hàng mẫu (stress kết hợp toàn thị trường và đặc thù) | > 90 ngày | [[src-choudhry-principles-banking#^choudhry-rmf-11]] |
| Risk register mẫu (stress đặc thù) | 90 ngày | [[src-choudhry-principles-banking#^choudhry-rmf-5]] |
| OLAR trong ILAAP mẫu ngân hàng UK | 92 ngày | [[src-choudhry-principles-banking#^choudhry-ilaap-6]] |
| Quy mô LAB theo Choudhry | stress 2 tuần và stress toàn thị trường 3 tháng | [[src-choudhry-principles-banking#^choudhry-lab-3]] |

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Survival period tối thiểu | [cần nguồn] | [cần nguồn] | | |

*Diễn giải:* [[lcr]] là một thước đo survival chuẩn hoá với horizon 30 ngày. TT83/2025 Đ48 không ấn định horizon kịch bản; xem [[liquidity-stress-testing]].

## Ứng dụng trong ALM
- Survival period ngắn hơn khẩu vị thì cần biện pháp khắc phục: giảm phơi nhiễm, giảm hạn mức dòng ra hợp đồng, rà lại [[contingency-funding-plan]] [[src-choudhry-principles-banking#^choudhry-ilaap-7]].
- Ví dụ Choudhry: survival period tăng từ 49 lên 93 ngày sau khi tính tác động stress và áp observed behavioural forecasting cho độ bám của nợ phải trả [[src-choudhry-principles-banking#^choudhry-st-20]].
- Báo cáo ILAAP mẫu tách số dư thanh khoản trước và sau management actions theo từng mốc thời gian [[src-choudhry-principles-banking#^choudhry-ilaap-9]].

## Nhầm lẫn thường gặp
- *Diễn giải:* survival period phụ thuộc hoàn toàn vào kịch bản và giả định hành vi; hai ngân hàng cùng báo "90 ngày" có thể dùng kịch bản khác nhau, nên con số không so sánh trực tiếp được nếu không kèm kịch bản.
