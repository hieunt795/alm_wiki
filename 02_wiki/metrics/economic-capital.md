---
title: "Economic Capital"
aliases: [Economic Capital, Vốn kinh tế]
type: metric
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-vab-ftp]]"]
relations:
  - {type: input-to, to: "[[target-capital]]", cite: "[[src-tt83-2025-nhnn#^pl6-2]]"}
  - {type: input-to, to: "[[raroc]]", cite: "[[src-tt83-2025-nhnn#^pl6-iii]]"}
  - {type: part-of, to: "[[icaap]]", cite: "[[src-tt83-2025-nhnn#^d59-2]]"}
  - {type: input-to, to: "[[funds-transfer-pricing]]", cite: "[[src-vab-ftp#^vab-ftp-67]]"}
tags: [capital, icaap]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
Vốn kinh tế ($C_E$) là mức vốn ngân hàng tự xác định, trên cơ sở tính mức vốn cần thiết để bù đắp các rủi ro trọng yếu và bảo đảm tỷ lệ an toàn vốn trong kịch bản có diễn biến bất lợi [[src-tt83-2025-nhnn#^d3-7]]. Chỉ tiêu này nằm trong khuôn khổ [[icaap]]. Bước 1 của ICAAP là đo lường rủi ro trọng yếu và xác định vốn kinh tế theo Phụ lục VI [[src-tt83-2025-nhnn#^d59-2]]. Bước 2 là kiểm tra sức chịu đựng về vốn để xác định vốn kinh tế trong kịch bản bất lợi [[src-tt83-2025-nhnn#^d59-2]].

## Công thức
$$
C_E = RWA^*_E \times CAR_{Target} + \Delta RWA_B \times CAR_R
$$
[[src-tt83-2025-nhnn#^pl6-1a]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $CAR_{Target}$ | Tỷ lệ an toàn vốn mục tiêu trong khẩu vị rủi ro | [[src-tt83-2025-nhnn#^pl6-1a]] |
| $CAR_R$ | Tỷ lệ an toàn vốn theo quy định NHNN | [[src-tt83-2025-nhnn#^pl6-1a]] |
| $\Delta RWA_B$ | Chênh lệch dương giữa tổng tài sản tính theo rủi ro ở kịch bản bất lợi và ở kịch bản bình thường | [[src-tt83-2025-nhnn#^pl6-1a]] |
| $RWA^*_E$ | Tổng tài sản tính theo rủi ro ở kịch bản bình thường | [[src-tt83-2025-nhnn#^pl6-1a]] |

$$
RWA^*_E = RWA_{CR} + RWA_{OR} + RWA_{MR} + RWA_{IRRBB} + RWA_{COR} + RWA_{OMR}
$$
[[src-tt83-2025-nhnn#^pl6-1b]]

| Cấu phần | Rủi ro | Cách xác định | Nguồn |
|---|---|---|---|
| $RWA_{CR}$ | Tín dụng | Theo quy định NHNN về tài sản có tính theo rủi ro tín dụng | [[src-tt83-2025-nhnn#^pl6-1b]] |
| $RWA_{OR}$, $RWA_{MR}$ | Hoạt động ([[operational-risk-management]]), thị trường ([[market-risk-management]]) | Phù hợp quy định NHNN về vốn yêu cầu | [[src-tt83-2025-nhnn#^pl6-1b]] |
| $RWA_{IRRBB}$ | IRRBB | Ngân hàng tự xây dựng; chậm nhất từ 01/01/2028 theo ΔEVE ([[rwa-irrbb]]) | [[src-tt83-2025-nhnn#^pl6-1c]] |
| $RWA_{COR}$ | Tập trung ([[concentration-risk-management]]) | Tự xây dựng, có sàn cho cấp tín dụng | [[src-tt83-2025-nhnn#^pl6-1d]] |
| $RWA_{OMR}$ | Rủi ro trọng yếu khác (không gồm thanh khoản) | Ngân hàng tự xây dựng | [[src-tt83-2025-nhnn#^pl6-1b]] |

**Sàn RWA tập trung tín dụng** [[src-tt83-2025-nhnn#^pl6-1d]]:
$$
RWA^{1*}_{COR} = \max(E_i - A \times C;\ 0) + \max(E_j - B \times C;\ 0)
$$
[[src-tt83-2025-nhnn#^pl6-1d]]

Ký hiệu:
- $E_i$: dư nợ cấp tín dụng với một khách hàng.
- $E_j$: dư nợ cấp tín dụng với một khách hàng và người có liên quan.
- $E_i$ và $E_j$ đều trừ khoản có hệ số rủi ro 0% và khoản đã trừ khỏi vốn tự có.
- $C$: vốn tự có.

| Từ | A (%) | B (%) | Nguồn |
|---|---|---|---|
| 01/07/2026 | 8,7 | 16,8 | [[src-tt83-2025-nhnn#^pl6-1d]] |
| 01/01/2027 | 8 | 15,2 | [[src-tt83-2025-nhnn#^pl6-1d]] |
| 01/01/2028 | 7,3 | 13,6 | [[src-tt83-2025-nhnn#^pl6-1d]] |
| 01/01/2029 | 6,5 | 12 | [[src-tt83-2025-nhnn#^pl6-1d]] |

## Diễn giải
*Diễn giải:*
- Số hạng thứ nhất là vốn cho rủi ro ở kịch bản bình thường, tính theo CAR mục tiêu (cao hơn mức tối thiểu).
- Số hạng thứ hai là vốn cho phần RWA tăng thêm khi chuyển sang kịch bản bất lợi, chỉ tính theo CAR tối thiểu.
- Như vậy, kết quả stress test vốn ([[stress-testing]]) đi thẳng vào $C_E$ qua $\Delta RWA_B$.

Vốn kinh tế dùng để:
- xác định [[target-capital]] (lấy max với vốn đáp ứng CAR quy định) [[src-tt83-2025-nhnn#^pl6-2]];
- làm mẫu số của [[raroc]] [[src-tt83-2025-nhnn#^pl6-iii]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Vị trí của IRRBB | Pillar 2, không có vốn yêu cầu chuẩn hoá Pillar 1 [[src-bcbs-irrbb-2016#^irrbb-u01-1]] [[src-bcbs-irrbb-2016#^irrbb-u01-2]]; vốn cho IRRBB xét trong ICAAP [[src-bcbs-irrbb-2016#^irrbb-p09-1]] | $RWA_{IRRBB}$ là một cấu phần của $RWA^*_E$ trong vốn kinh tế [[src-tt83-2025-nhnn#^pl6-1b]] | TT83 PL6.I.1 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Rủi ro thanh khoản | [cần nguồn] | Không tính vào $RWA^*_E$ [[src-tt83-2025-nhnn#^pl6-1b]] | TT83 PL6.I.1.d | 01/07/2026 |

Khác biệt: vốn kinh tế là chỉ tiêu nội bộ của ICAAP, không phải vốn yêu cầu Pillar 1. *Diễn giải:* vì vậy việc VN đưa $RWA_{IRRBB}$ vào $C_E$ vẫn nằm trong logic Pillar 2 của d368. Điểm khác là VN ấn định cấu trúc công thức.

## Ứng dụng trong ALM
- Bộ phận ALM kiểm soát hoạt động kinh doanh tuân thủ tổng tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d25-3]]. Đó chính là cấu phần $RWA_{IRRBB}$ trong công thức trên.
- Báo cáo ICAAP hằng năm nêu vốn kinh tế và vốn mục tiêu [[src-tt83-2025-nhnn#^d63-1]].
- Trong quy định FTP của VAB (T4), khi ngân hàng đã áp khung RAROC, chi phí VCSH tính cho đơn vị kinh doanh bằng (ROE% − COF%) × vốn RAROC dự kiến × WAT/365; vốn RAROC dự kiến được phân bổ cho từng đơn vị kinh doanh theo kế hoạch [[src-vab-ftp#^vab-ftp-67]]. Xem [[funds-transfer-pricing]].

## Nhầm lẫn thường gặp
- *Diễn giải:* $CAR_{Target}$ và $CAR_R$ không thay thế nhau trong công thức: $CAR_{Target}$ nhân với RWA ở kịch bản bình thường, còn $CAR_R$ nhân với phần RWA tăng thêm ở kịch bản bất lợi [[src-tt83-2025-nhnn#^pl6-1a]].
