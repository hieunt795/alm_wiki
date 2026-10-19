---
title: "Expected Credit Loss (IFRS 9)"
aliases: [Expected Credit Loss, ECL, Tổn thất tín dụng dự kiến, IFRS 9 ECL, IFRS 9 impairment]
type: metric
domains: [alm, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [ifrs-9, ecl, impairment, provisioning, sicr, staging]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
Expected credit loss (ECL) là khoản dự phòng suy giảm khoản vay theo IFRS 9. IAS 39 trước đây ghi nhận suy giảm theo incurred loss; IFRS 9 đưa vào ECL, nên gần như mọi tài sản có dự phòng từ ngày đầu ghi nhận [[src-choudhry-principles-banking#^choudhry-ecl-2]].

## Công thức
$$
\text{ECL} = \sum_i \text{EAD}_i \times \text{PD}_i \times \text{LGD}_i
$$
[[src-choudhry-principles-banking#^choudhry-ecl-2]]

- $\text{EAD}_i$: exposure at default của khoản thứ $i$ [[src-choudhry-principles-banking#^choudhry-ecl-2]].
- $\text{PD}_i$: PD 12 tháng hoặc lifetime, tuỳ stage [[src-choudhry-principles-banking#^choudhry-ecl-2]].
- $\text{LGD}_i$: loss given default [[src-choudhry-principles-banking#^choudhry-ecl-2]].

**Mô hình ba stage:**

| Stage | Điều kiện | ECL ghi nhận | Nguồn |
|---|---|---|---|
| 1 | Phần lớn tài sản performing | 12 tháng | [[src-choudhry-principles-banking#^choudhry-ecl-3]] |
| 2 | SICR đã xảy ra từ ghi nhận ban đầu; quá hạn 30 ngày là giả định có thể bác bỏ | Lifetime | [[src-choudhry-principles-banking#^choudhry-ecl-3]] |
| 3 | Credit impaired; quá hạn 90 ngày là giả định có thể bác bỏ; lãi ghi nhận trên cơ sở ròng | Lifetime | [[src-choudhry-principles-banking#^choudhry-ecl-3]] |

ECL 12 tháng là phần của ECL lifetime ứng với vỡ nợ trong 12 tháng sau ngày báo cáo, có trọng số xác suất [[src-choudhry-principles-banking#^choudhry-ecl-4]].

**SICR** là gia tăng đáng kể xác suất vỡ nợ kể từ ghi nhận ban đầu [[src-choudhry-principles-banking#^choudhry-ecl-5]]. Cách đánh giá:
- dịch chuyển PD, theo dõi tương đối chứ không tuyệt đối [[src-choudhry-principles-banking#^choudhry-ecl-5]];
- quá hạn 30 ngày là backstop của chuẩn mực [[src-choudhry-principles-banking#^choudhry-ecl-5]];
- đánh giá theo từng tài sản, trừ khi không xác định được yếu tố ở cấp công cụ thì đánh giá theo nhóm đồng nhất [[src-choudhry-principles-banking#^choudhry-ecl-5]].

## Diễn giải
Điểm cốt lõi của IFRS 9 là buộc ngân hàng trích lập dự phòng trước khi khoản vay vỡ nợ. Dự phòng Stage 1 được hoàn nhập khi khoản vay đáo hạn hoặc bán, nên tác động P&L chỉ là vấn đề thời điểm [[src-choudhry-principles-banking#^choudhry-ecl-4]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Phương pháp dự phòng | Không thuộc phạm vi các chuẩn Basel đã ingest; ECL do IFRS 9 đưa vào thay incurred loss của IAS 39 [[src-choudhry-principles-banking#^choudhry-ecl-2]] | [cần nguồn] | | |

*Diễn giải:* tại VN, dự phòng rủi ro tín dụng theo quy định NHNN (phân loại nợ) chưa có nguồn trong wiki để so với ECL.

## Ứng dụng trong ALM
- ALCO cần quen IFRS 9 vì tác động tới ALM, quan trọng nhất là trích lập dự phòng: dự phòng cao hơn theo expected loss, và dự phòng ngay ngày đầu khoản vay [[src-choudhry-principles-banking#^choudhry-ecl-1]]. Xem [[alco]].
- Chính sách IFRS 9 nên được Board phê duyệt và rà soát ít nhất hằng năm [[src-choudhry-principles-banking#^choudhry-hacc-5]].

*Diễn giải:* ECL ngày đầu làm giảm lợi nhuận kế toán của khoản vay mới. Vì vậy định giá khoản vay qua [[funds-transfer-pricing]] và RAROC cần tính chi phí dự phòng này, nếu không biên lợi nhuận báo cáo của khối kinh doanh sẽ cao hơn thực tế.

## Nhầm lẫn thường gặp
- ECL kế toán (IFRS 9) khác expected loss (EL) trong vốn IRB của Basel; EL theo mô hình danh mục của Choudhry xem [[expected-loss]]. Wiki chưa ingest phần Basel IRB để so sánh [cần nguồn].
