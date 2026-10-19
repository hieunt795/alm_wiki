---
title: "RWA IRRBB"
aliases: [RWA IRRBB, Tổng tài sản tính theo rủi ro lãi suất trên sổ ngân hàng, Risk-weighted assets for IRRBB]
type: metric
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[economic-capital]]", cite: "[[src-tt83-2025-nhnn#^pl6-1b]]"}
tags: [capital, irrbb, icaap]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
$RWA_{IRRBB}$ là tổng tài sản tính theo rủi ro lãi suất trên sổ ngân hàng. Đây là một cấu phần của tổng tài sản tính theo rủi ro $RWA^*_E$, dùng để tính [[economic-capital]] [[src-tt83-2025-nhnn#^pl6-1b]].

## Công thức
Ngân hàng tự xây dựng phương pháp xác định $RWA_{IRRBB}$. Chậm nhất từ 01/01/2028, ngân hàng phải tính $RWA_{IRRBB}$ theo chỉ tiêu ΔEVE theo TT83/2025 [[src-tt83-2025-nhnn#^pl6-1c]]. Cách đo ΔEVE: [[economic-value-of-equity]].

*Diễn giải (tái dựng, chưa có nguồn):* PL6 không nêu cách quy đổi ΔEVE thành RWA. Một cách quy đổi thường gặp là $RWA_{IRRBB} = \Delta EVE / CAR_R$, để vốn tương ứng bằng đúng ΔEVE. Cách này ngoài wiki, chưa có nguồn, và phải được ngân hàng tự quy định.

## Diễn giải
Lộ trình của $RWA_{IRRBB}$ khớp với lộ trình chỉ tiêu đo lường IRRBB:

| Giai đoạn | Chỉ tiêu đo lường IRRBB | $RWA_{IRRBB}$ | Nguồn |
|---|---|---|---|
| 01/07/2026 – 31/12/2027 | ΔNII hoặc ΔEVE | Phương pháp ngân hàng tự xây dựng | [[src-tt83-2025-nhnn#^d74-4a]] [[src-tt83-2025-nhnn#^pl6-1c]] |
| Chậm nhất từ 01/01/2028 | Cả ΔNII và ΔEVE | Theo ΔEVE | [[src-tt83-2025-nhnn#^d74-4b]] [[src-tt83-2025-nhnn#^pl6-1c]] |

Trong stress test vốn, giả định lãi suất phải được tính tác động lên tổng tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]. Phần tăng thêm ở kịch bản bất lợi đi vào $\Delta RWA_B$ của vốn kinh tế [[src-tt83-2025-nhnn#^pl6-1a]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Vốn cho IRRBB | Pillar 2; không có vốn yêu cầu Pillar 1 chuẩn hoá [[src-bcbs-irrbb-2016#^irrbb-u01-2]]; xét trong ICAAP theo rủi ro giá trị kinh tế, capital buffers cho rủi ro thu nhập [[src-bcbs-irrbb-2016#^irrbb-p09-2]] | $RWA_{IRRBB}$ trong vốn kinh tế ICAAP; theo ΔEVE từ 01/01/2028 [[src-tt83-2025-nhnn#^pl6-1c]] | TT83 PL6.I.1.d(iv) | 01/07/2026; ΔEVE từ 01/01/2028 |

Khác biệt: d368 nói vốn cho IRRBB xét theo rủi ro giá trị kinh tế [[src-bcbs-irrbb-2016#^irrbb-p09-2]]. VN cụ thể hoá điều này bằng cách bắt buộc dùng ΔEVE cho $RWA_{IRRBB}$ từ 2028.

## Ứng dụng trong ALM
- Bộ phận ALM kiểm soát hoạt động kinh doanh tuân thủ tổng tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d25-3]].
- Kế hoạch vốn phân bổ vốn mục tiêu theo tài sản tính theo rủi ro cho từng rủi ro trọng yếu, làm cơ sở xác định hạn mức [[src-tt83-2025-nhnn#^d61-1]]. *Diễn giải:* phần vốn phân bổ cho IRRBB giới hạn mức ΔEVE tối đa mà hạn mức ΔEVE [[src-tt83-2025-nhnn#^d53-2]] được phép đặt.

## Nhầm lẫn thường gặp
- *Diễn giải:* $RWA_{IRRBB}$ thuộc vốn kinh tế nội bộ (ICAAP), không thuộc mẫu số của CAR theo quy định NHNN. PL6 chỉ dẫn quy định NHNN cho $RWA_{CR}$, $RWA_{OR}$, $RWA_{MR}$ [[src-tt83-2025-nhnn#^pl6-1b]], không dẫn cho $RWA_{IRRBB}$.
