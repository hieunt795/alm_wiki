---
title: "Interest Rate Risk Capital Requirement (Trading Book)"
aliases: [K_IRR, KIRR, Vốn yêu cầu cho rủi ro lãi suất sổ kinh doanh, Interest Rate Risk Capital Requirement]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[market-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d74-1]]"}
tags: [capital, market-risk, interest-rate, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho rủi ro lãi suất ($K_{IRR}$) là cấu phần của $K_{MR}$ cho giao dịch không phải quyền chọn [[src-tt14-2025-nhnn#^d74-1]]. $K_{IRR}$ gồm vốn cho rủi ro lãi suất cụ thể ($K_{IRR}^{SR}$) và vốn cho rủi ro lãi suất chung ($K_{IRR}^{GMR}$) [[src-tt14-2025-nhnn#^d74-2]] [[src-tt14-2025-nhnn#^pl4-i-2a]]. Xem [[market-risk-capital-requirement]].

Phạm vi là mọi công cụ tài chính trên sổ kinh doanh, trạng thái dương hoặc âm, có giá trị thị trường chịu ảnh hưởng của lãi suất [[src-tt14-2025-nhnn#^pl4-i-1]].

## Công thức
$$
K_{IRR} = K_{IRR}^{SR} + K_{IRR}^{GMR}
$$
[[src-tt14-2025-nhnn#^d74-2]]

Dạng tổng này là cách đọc của wiki: Đ74.2 nêu K_IRR "được xác định theo công thức sau" nhưng raw không giữ công thức, và Phụ lục IV nêu hai thành phần [[src-tt14-2025-nhnn#^d74-2]] [[src-tt14-2025-nhnn#^pl4-i-2a]]. Chưa đối chiếu bản gốc [cần nguồn].

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $K_{IRR}^{SR}$ | Rủi ro lãi suất cụ thể: từ yếu tố liên quan đến đơn vị phát hành | [[specific-interest-rate-risk-capital]] | [[src-tt14-2025-nhnn#^pl4-i-2a]] |
| $K_{IRR}^{GMR}$ | Rủi ro lãi suất chung: từ thay đổi lãi suất thị trường; tổng giá trị tuyệt đối theo từng đồng tiền | [[general-interest-rate-risk-capital]] | [[src-tt14-2025-nhnn#^pl4-i-4b]] |

## Diễn giải
**Loại trừ khỏi phạm vi** [[src-tt14-2025-nhnn#^pl4-i-1]]:
- trái phiếu chuyển đổi đã tính vốn rủi ro giá cổ phiếu ([[equity-risk-capital-requirement]]);
- công cụ vốn chủ sở hữu, công cụ bổ sung vốn cấp 1 của đơn vị khác đã trừ khỏi vốn tự có theo Phụ lục I;
- tài sản gốc của quyền chọn đã tính vốn cho giao dịch quyền chọn ([[options-risk-capital-requirement]]);
- công cụ mua theo hợp đồng mua có kỳ hạn giấy tờ có giá giữa các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài.

**Quy đổi phái sinh.** Phái sinh lãi suất quy đổi thành trạng thái danh nghĩa của tài sản gốc theo giá trị thị trường để tính vốn rủi ro lãi suất chung. Hoán đổi tiền tệ và lãi suất, hợp đồng kỳ hạn lãi suất hoặc ngoại tệ, hợp đồng tương lai lãi suất, hợp đồng tương lai theo chỉ số lãi suất, hợp đồng tương lai ngoại tệ không phải tính rủi ro lãi suất cụ thể [[src-tt14-2025-nhnn#^pl4-i-2b]].
- Hợp đồng kỳ hạn, tương lai có tài sản gốc là chứng khoán nợ chuyển thành trạng thái dương (âm) của chứng khoán nợ và trạng thái âm (dương) của chứng khoán zero coupon có thời hạn bằng thời gian đến hạn của hợp đồng [[src-tt14-2025-nhnn#^pl4-i-2cd]].
- Hợp đồng lãi suất kỳ hạn chuyển thành hai trạng thái zero coupon, một có thời hạn bằng tổng thời gian đến hạn của hợp đồng và thời hạn tài sản gốc [[src-tt14-2025-nhnn#^pl4-i-2dd]].
- Hoán đổi ngoại tệ và hoán đổi lãi suất tính bằng hai trạng thái danh nghĩa [[src-tt14-2025-nhnn#^pl4-i-2e]]:

| Vai trò của ngân hàng | Trạng thái 1 (âm) | Trạng thái 2 (dương) |
|---|---|---|
| Nhận cố định, trả thả nổi | Chứng khoán lãi suất thả nổi, thời hạn là kỳ định lại lãi suất | Chứng khoán lãi suất cố định, thời hạn hợp đồng hoán đổi |
| Nhận thả nổi, trả cố định | Chứng khoán lãi suất cố định, thời hạn hợp đồng hoán đổi | Chứng khoán lãi suất thả nổi, thời hạn là kỳ định lại lãi suất |
| Nhận và trả thả nổi | Lãi suất thả nổi, thời hạn là kỳ định lại lãi suất | Lãi suất thả nổi, thời hạn là kỳ định lại lãi suất |
| Nhận và trả cố định | Lãi suất cố định, thời hạn hợp đồng hoán đổi | Lãi suất cố định, thời hạn hợp đồng hoán đổi |

Với hoán đổi ngoại tệ, hai trạng thái là hai chứng khoán nợ ở hai đồng tiền của giao dịch [[src-tt14-2025-nhnn#^pl4-i-2e]].

*Diễn giải:* tên thành phần chung ở Phụ lục IV là $K_{IRR}^{GMR}$ ("GMR"), còn Đ74 viết tắt "GR" ([[market-risk-capital-requirement]]). Hai ký hiệu chỉ cùng một thành phần.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu phần | [cần nguồn] (MAR chưa ingest) | Cụ thể và chung [[src-tt14-2025-nhnn#^pl4-i-2a]] | PL4.B.I.2a | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Phương pháp rủi ro chung | [cần nguồn] | Thang kỳ hạn [[src-tt14-2025-nhnn#^pl4-i-4b]] | PL4.B.I.4b | Như trên |
| Phái sinh lãi suất | [cần nguồn] | Không tính rủi ro cụ thể [[src-tt14-2025-nhnn#^pl4-i-2b]] | PL4.B.I.2b | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* $K_{IRR}$ chỉ áp dụng cho sổ kinh doanh. Rủi ro lãi suất sổ ngân hàng (IRRBB) không vào mẫu số CAR theo cấu phần này mà vào [[icaap]] ([[capital-adequacy-ratio]]). Treasury quản lý vị thế sổ kinh doanh và hoán đổi lãi suất cần biết cách quy đổi ra hai trạng thái, vì kỳ hạn hoán đổi và kỳ định lại lãi suất quyết định thang kỳ hạn của từng trạng thái ([[maturity-ladder-method]]).

## Nhầm lẫn thường gặp
- Hợp đồng kỳ hạn, tương lai lãi suất không bị tính rủi ro lãi suất cụ thể [[src-tt14-2025-nhnn#^pl4-i-2b]].
- Kỳ hạn của hoán đổi lãi suất thả nổi là kỳ định lại lãi suất, không phải kỳ hạn hợp đồng [[src-tt14-2025-nhnn#^pl4-i-2e]].
