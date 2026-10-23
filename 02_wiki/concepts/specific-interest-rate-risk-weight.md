---
title: "Specific Interest Rate Risk Weight"
aliases: [Specific Interest Rate Risk Weight, SRW, Hệ số rủi ro lãi suất cụ thể]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[specific-interest-rate-risk-capital]]", cite: "[[src-tt14-2025-nhnn#^pl4-i-3b]]"}
tags: [capital, market-risk, interest-rate, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Hệ số rủi ro lãi suất cụ thể (SRW) là tham số do NHNN ấn định theo nhóm công cụ, xếp hạng tín nhiệm độc lập và thời hạn còn lại, dùng trong $K_{IRR}^{SR}$ ([[specific-interest-rate-risk-capital]]) [[src-tt14-2025-nhnn#^pl4-i-3b]]. SRW 0% áp dụng cho công cụ do Chính phủ Việt Nam, NHNN, Kho bạc Nhà nước, UBND tỉnh/thành phố phát hành hoặc bảo lãnh thanh toán [[src-tt14-2025-nhnn#^pl4-i-3a]]. SRW cũng là hệ số cụ thể của quyền chọn lãi suất ([[options-risk-capital-requirement]]).

## Cơ chế & drivers
**Ba nhóm công cụ** [[src-tt14-2025-nhnn#^pl4-i-3b]]:
- Nhóm 1: công cụ do Chính phủ, chính quyền địa phương của các nước phát hành.
- Nhóm 2: công cụ do tổ chức tài chính quốc tế hoặc doanh nghiệp nhà nước phát hành; công cụ khác được ít nhất 02 tổ chức xếp hạng BBB- hoặc tương đương trở lên; công cụ khác được 01 tổ chức xếp hạng BBB- hoặc tương đương trở lên và không có tổ chức nào xếp thấp hơn BBB-.
- Nhóm 3: công cụ còn lại.

**Bảng SRW** [[src-tt14-2025-nhnn#^pl4-i-3b]]:

| Nhóm | Xếp hạng tín nhiệm độc lập | SRW |
|---|---|---|
| 1 | AAA đến AA- | 0% |
| 1 | A+ đến BBB- | 0,25% nếu thời hạn còn lại từ 6 tháng trở xuống; 1% nếu trên 6 đến 24 tháng; 1,6% nếu trên 24 tháng |
| 1 | B- đến BB+ | 8% |
| 1 | Dưới B- | 12% |
| 1 | Không xếp hạng | 12% |
| 2 | (không phân theo xếp hạng) | 0,25% nếu từ 6 tháng trở xuống; 1% nếu trên 6 đến 24 tháng; 1,6% nếu trên 24 tháng |
| 3 | BB- đến BB+ | 8% |
| 3 | Dưới BB- | 12% |
| 3 | Không xếp hạng | 12% |

*Diễn giải:* thứ hạng của Nhóm 1 trong bảng nguồn dùng khoảng "B- đến BB+" và "A+ đến BBB-" theo cách viết của nguồn; khoảng "BBB- đến A+" trong raw đọc là A+ đến BBB-. Xếp hạng do doanh nghiệp xếp hạng độc lập ([[external-credit-rating-use]], [[credit-rating-scale-mapping]]).

## Phụ thuộc regime
Phương pháp tiêu chuẩn của Phụ lục IV; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Nhóm 2 gồm doanh nghiệp nhà nước phát hành, nên trái phiếu doanh nghiệp nhà nước có SRW theo thời hạn 0,25% đến 1,6%, không theo xếp hạng [[src-tt14-2025-nhnn#^pl4-i-3b]].

**Basel.** [cần nguồn] (MAR chưa ingest).

**ALM.** *Diễn giải:* với công cụ thuộc Nhóm 2, SRW tăng theo kỳ hạn còn lại (0,25%, 1%, 1,6%), nên kéo dài kỳ hạn danh mục trái phiếu doanh nghiệp nhà nước trong sổ kinh doanh làm $K_{IRR}^{SR}$ tăng. Ví dụ số do wiki dựng: 100 tỷ đồng trái phiếu Nhóm 2 kỳ hạn còn lại 3 năm có $K_{IRR}^{SR}$ = 100 × 1,6% = 1,6 tỷ đồng.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Bảng nguồn viết khoảng xếp hạng Nhóm 1 là "Từ BBB- đến A+" (raw) và "Từ B- đến BB+"; cách đọc giữ nguyên khoảng nguồn, cần đối chiếu bản gốc nếu muốn dùng làm tham số hệ thống [cần nguồn].
