---
title: "Specific Interest Rate Risk Capital"
aliases: [Specific Interest Rate Risk Capital, K_IRR^SR, Vốn yêu cầu cho rủi ro lãi suất cụ thể]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[interest-rate-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^pl4-i-2a]]"}
tags: [capital, market-risk, interest-rate, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho rủi ro lãi suất cụ thể ($K_{IRR}^{SR}$) là vốn cho rủi ro phát sinh từ yếu tố liên quan đến đơn vị phát hành công cụ tài chính [[src-tt14-2025-nhnn#^pl4-i-2a]]. Là thành phần của [[interest-rate-risk-capital-requirement]].

## Công thức
$$
K_{IRR}^{SR} = \sum_{i=1}^{n} e_i \times SRW_i
$$
[[src-tt14-2025-nhnn#^pl4-i-3]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $e_i$ | Giá trị thị trường của công cụ tài chính thứ i | [[src-tt14-2025-nhnn#^pl4-i-3]] |
| $SRW_i$ | Hệ số rủi ro lãi suất cụ thể của công cụ ([[specific-interest-rate-risk-weight]]) | [[src-tt14-2025-nhnn#^pl4-i-3]] |

Chỉ số dưới $i$ của $SRW$ là của wiki; nguồn viết SRW "của từng công cụ tài chính" [[src-tt14-2025-nhnn#^pl4-i-3]].

## Diễn giải
Công cụ do Chính phủ Việt Nam, NHNN, Kho bạc Nhà nước, UBND tỉnh/thành phố phát hành hoặc bảo lãnh thanh toán có SRW 0%, nên không đóng góp vào $K_{IRR}^{SR}$ [[src-tt14-2025-nhnn#^pl4-i-3a]]. Công cụ khác theo bảng [[specific-interest-rate-risk-weight]] [[src-tt14-2025-nhnn#^pl4-i-3b]].

Hợp đồng hoán đổi, kỳ hạn, tương lai lãi suất và ngoại tệ không phải tính rủi ro lãi suất cụ thể [[src-tt14-2025-nhnn#^pl4-i-2b]].

*Diễn giải:* $e_i$ cộng giá trị thị trường theo từng công cụ, không bù trừ trạng thái dương và âm của hai công cụ khác nhau trong công thức này. Nguồn không nêu rõ việc bù trừ; xem Đ73 về quản lý sổ kinh doanh [cần nguồn].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức | [cần nguồn] (MAR chưa ingest) | $\sum e_i \times SRW_i$ [[src-tt14-2025-nhnn#^pl4-i-3]] | PL4.B.I.3 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Công cụ Chính phủ Việt Nam | [cần nguồn] | SRW 0% [[src-tt14-2025-nhnn#^pl4-i-3a]] | PL4.B.I.3a | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* sổ kinh doanh trái phiếu Chính phủ Việt Nam không đóng góp $K_{IRR}^{SR}$ nhưng vẫn chịu rủi ro lãi suất chung ([[general-interest-rate-risk-capital]]). Trái phiếu doanh nghiệp không xếp hạng có SRW 12% (Nhóm 3), nên một đồng vị thế dương hay âm đều tốn vốn cụ thể.

## Nhầm lẫn thường gặp
- SRW 0% của công cụ Chính phủ Việt Nam chỉ áp dụng cho rủi ro cụ thể, không áp dụng cho rủi ro chung [[src-tt14-2025-nhnn#^pl4-i-3a]].
