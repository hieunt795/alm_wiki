---
title: "Government Bond Holdings"
aliases: [Government Bond Holdings, "Số dư mua, nắm giữ, đầu tư trái phiếu Chính phủ", Tử số tỷ lệ nắm giữ TPCP]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2026-10-01
valid_to:
as_of:
sources: ["[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[government-bond-holding-ratio]]", cite: "[[src-tt50-2026-nhnn#^d28-4]]"}
tags: [government-bond, vn-regulation]
updated: 2026-10-21
reviewed:
---

## Định nghĩa
Government Bond Holdings là tử số của [[government-bond-holding-ratio]] theo TT50/2026 Đ28.4: số dư mua, nắm giữ, đầu tư trái phiếu Chính phủ (TPCP) và trái phiếu được Chính phủ bảo lãnh (TPCPBL), tính bằng giá mua [[src-tt50-2026-nhnn#^d28-4]].

## Công thức

| Chiều | Cấu phần | Điều khoản | Căn cứ |
|---|---|---|---|
| + | Giá mua TPCP, TPCPBL thuộc sở hữu của ngân hàng | Đ28.4 | [[src-tt50-2026-nhnn#^d28-4]] |
| + | Các khoản uỷ thác mua, nắm giữ, đầu tư TPCP, TPCPBL theo quy định của pháp luật | Đ28.4 | [[src-tt50-2026-nhnn#^d28-4]] |
| − | Khoản mua, đầu tư bằng nguồn vốn uỷ thác mà ngân hàng không chịu rủi ro | Đ28.4.a | [[src-tt50-2026-nhnn#^d28-4]] |
| − | Trái phiếu ngân hàng nhận làm tài sản bảo đảm, chiết khấu, tái chiết khấu | Đ28.4.b | [[src-tt50-2026-nhnn#^d28-4]] |

Phạm vi trái phiếu:

| Loại | Gồm | Căn cứ |
|---|---|---|
| TPCP | Công cụ nợ của Chính phủ, kể cả tín phiếu Kho bạc, công trái xây dựng Tổ quốc | [[src-tt50-2026-nhnn#^d28-2]] |
| TPCPBL | Trái phiếu doanh nghiệp được Chính phủ bảo lãnh; trái phiếu ngân hàng chính sách được Chính phủ bảo lãnh | [[src-tt50-2026-nhnn#^d28-2]] |

## Diễn giải
- *Diễn giải:* tử số đo theo chủ thể chịu rủi ro. Uỷ thác cho bên khác mua thì ngân hàng vẫn chịu rủi ro nên vẫn tính. Mua bằng vốn nhận uỷ thác mà ngân hàng không chịu rủi ro thì không tính. Cách xử lý này giống L và D của LDR, nơi vốn uỷ thác chỉ vào D khi ngân hàng chịu rủi ro [[src-tt50-2026-nhnn#^d12-4d]].
- *Diễn giải:* trái phiếu nhận làm tài sản bảo đảm hay chiết khấu không vào tử số. Cách loại trừ này giống định nghĩa đầu tư trái phiếu doanh nghiệp ở Đ3.4 [[src-tt50-2026-nhnn#^d3-4]].
- *Diễn giải:* tử số dùng giá mua, không dùng giá trị thị trường. Lãi, lỗ đánh giá lại không làm đổi tử số. Đ28 không nói rõ có trừ phần trái phiếu đã đáo hạn từng phần hay phân bổ chiết khấu, phụ trội không [cần nguồn].
- *Diễn giải:* TPCP mua qua reverse repo với NHNN hay TCTD khác có thuộc "nhận làm tài sản bảo đảm" hay không phụ thuộc hình thức pháp lý của giao dịch [cần nguồn: quy định về mua, bán có kỳ hạn giấy tờ có giá].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Chỉ tiêu tương ứng | Không có trong chuẩn BCBS đã ingest [cần nguồn] | Giá mua TPCP, TPCPBL sở hữu và uỷ thác, trừ vốn uỷ thác không chịu rủi ro và tài sản bảo đảm, chiết khấu [[src-tt50-2026-nhnn#^d28-4]] | TT50 Đ28.4 | 01/10/2026 [[src-tt50-2026-nhnn#^d37-1]] |

## Ứng dụng trong ALM
- *Diễn giải:* tử số không trùng danh mục HQLA cấp 1. TPCPBL không bảo lãnh 100% gốc, lãi vẫn vào tử số [[src-tt50-2026-nhnn#^d28-2]] nhưng không phải tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a2-3e]]. Ngược lại, tín phiếu NHNN là tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a2-3d]] nhưng không thuộc công cụ nợ của Chính phủ theo lời văn Đ28.2.

## Nhầm lẫn thường gặp
- *Diễn giải:* tử số không bằng số dư trái phiếu Chính phủ trên báo cáo tài chính. Nó dùng giá mua, cộng phần uỷ thác mua và loại phần mua bằng vốn uỷ thác không chịu rủi ro [[src-tt50-2026-nhnn#^d28-4]].
