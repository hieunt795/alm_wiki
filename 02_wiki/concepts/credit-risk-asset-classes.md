---
title: "Credit Risk Asset Classes"
aliases: [Credit Risk Asset Classes, Phân loại nhóm tài sản có rủi ro tín dụng, Nợ xấu trong RWA]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[credit-risk-weight]]", cite: "[[src-tt14-2025-nhnn#^d11-1]]"}
tags: [capital, credit-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ11 TT14/2025 chia tài sản có rủi ro tín dụng khách hàng thành các nhóm để gán hệ số rủi ro tín dụng ([[credit-risk-weight]]). Tài sản đã trừ khỏi vốn tự có theo Phụ lục I không thuộc các nhóm này [[src-tt14-2025-nhnn#^d11-1]]. Xem [[capital-deductions]].

## Cơ chế & drivers
**Bảy nhóm tài sản cấp 1** [[src-tt14-2025-nhnn#^d11-1]]:

| Nhóm | Nội dung | Hệ số rủi ro tín dụng | Nguồn |
|---|---|---|---|
| a(i) | Nợ xấu và số dư cam kết ngoại bảng nhóm 3, 4, 5 | 100% theo Đ12.1: dự phòng cụ thể lớn hơn 20% giá trị khoản nợ xấu; khoản thế chấp nhà ở đáp ứng Đ16.2a(i), (ii); cam kết ngoại bảng nhóm 3, 4, 5 (cách ghép ba vế cần đối chiếu bản gốc). 150% theo Đ12.2: dự phòng cụ thể đến 20%, trừ khoản thuộc Đ12.1 | [[src-tt14-2025-nhnn#^d12-1]] [[src-tt14-2025-nhnn#^d12-2]] |
| a(ii) | Khoản phải đòi còn lại (bốn nhóm cấp 2 bên dưới) | Theo Đ13–Đ22 | [[src-tt14-2025-nhnn#^d11-2]] |
| b | Tiền mặt, vàng và tương đương tiền mặt | 0% | [[src-tt14-2025-nhnn#^d23-1]] |
| c | Công cụ vốn chủ sở hữu của doanh nghiệp; cho vay giao dịch ký quỹ của công ty chứng khoán | 150% | [[src-tt14-2025-nhnn#^d23-1]] |
| d | Cho thuê tài chính | Cao hơn giữa hệ số doanh nghiệp thuê tài chính (Đ19.1 hoặc 19.2) và 160% | [[src-tt14-2025-nhnn#^d23-3]] |
| đ | Mua lại khoản phải thu của công ty tài chính, công ty cho thuê tài chính | Hệ số của khoản phải đòi đối với bên bán (có bảo lưu quyền truy đòi) hoặc của khoản phải đòi | [[src-tt14-2025-nhnn#^d23-4]] |
| e | Khoản phải thu từ bán nợ xấu (trừ bán cho Công ty quản lý tài sản và Công ty mua bán nợ) | 200% | [[src-tt14-2025-nhnn#^d23-5]] |
| g | Tài sản còn lại trên Báo cáo tình hình tài chính | 100% | [[src-tt14-2025-nhnn#^d23-5]] |

**Bốn nhóm cấp 2 của khoản phải đòi a(ii)** [[src-tt14-2025-nhnn#^d11-2]]:

| Nhóm | Nội dung | Node | Hệ số tóm tắt |
|---|---|---|---|
| a | Quốc gia, Chính phủ Việt Nam, NHNN, Kho bạc Nhà nước, UBND tỉnh/thành phố, ngân hàng chính sách, tổ chức tài chính quốc tế, Công ty quản lý tài sản, Công ty mua bán nợ | [[sovereign-and-bank-exposure-risk-weighting]] | 0% hoặc 20% cho nhóm trong nước [[src-tt14-2025-nhnn#^d13-1]] [[src-tt14-2025-nhnn#^d13-3]] |
| b | Tổ chức tín dụng, chi nhánh ngân hàng nước ngoài | [[sovereign-and-bank-exposure-risk-weighting]] | Theo xếp hạng và kỳ hạn gốc [[src-tt14-2025-nhnn#^d14-3]] |
| c | Doanh nghiệp, cá nhân: cho vay kinh doanh chứng khoán; bất động sản; tín dụng chuyên biệt; doanh nghiệp khác; nông nghiệp nông thôn; bán lẻ | [[real-estate-exposure-risk-weighting]], [[specialised-lending-risk-weighting]], [[corporate-exposure-risk-weighting]], [[retail-exposure-risk-weighting]] | Cho vay kinh doanh chứng khoán 150% [[src-tt14-2025-nhnn#^d15-1]] |
| d | Khoản phải đòi khác | node này | 100% [[src-tt14-2025-nhnn#^d22-1]] |

**Thứ tự phân loại theo sơ đồ Phụ lục VI.** Tài sản không phải khoản phải đòi đi thẳng tới Đ23 theo nhóm [[src-tt14-2025-nhnn#^pl6-2]]. Khoản phải đòi được kiểm tra lần lượt: nợ xấu và cam kết nhóm 3 đến 5 (Đ12); Chính phủ, chính quyền địa phương, Công ty quản lý tài sản, Công ty mua bán nợ, tổ chức tài chính quốc tế (Đ13); tổ chức tín dụng, chi nhánh ngân hàng nước ngoài (Đ14); cho vay kinh doanh chứng khoán (Đ15); bất động sản (Đ16–17); doanh nghiệp, gồm tín dụng chuyên biệt (Đ18) và doanh nghiệp khác (Đ19); cá nhân, gồm nông nghiệp nông thôn (Đ20) và bán lẻ (Đ21); khoản phải đòi khác (Đ22) [[src-tt14-2025-nhnn#^pl6-3]] [[src-tt14-2025-nhnn#^pl6-4]] [[src-tt14-2025-nhnn#^pl6-5]]. Nội dung đọc từ hình ảnh, chưa kiểm bằng máy [cần nguồn: đối chiếu pdf].

*Diễn giải:* thứ tự này giải thích vì sao khoản vay chứng khoán (Đ15) hay bất động sản (Đ16) được xử lý trước nhóm doanh nghiệp: một khoản vay cho doanh nghiệp để kinh doanh chứng khoán hoặc bất động sản không dùng bảng doanh thu và đòn bẩy của Đ19 trừ khi Đ17 dẫn tới ([[corporate-exposure-risk-weighting]]).

## Phụ thuộc regime
Phương pháp tiêu chuẩn của Chương II; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Đ11.1a(i) dẫn tới quy định của NHNN về phân loại tài sản có (nhóm 3, 4, 5); quy định đó chưa ingest [cần nguồn] [[src-tt14-2025-nhnn#^d11-1]]. Phụ lục VI minh hoạ thứ tự phân loại bằng sơ đồ [[src-tt14-2025-nhnn#^pl6-1]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* hệ số của nợ xấu phụ thuộc mức dự phòng cụ thể (100% khi trên 20%, 150% khi đến 20%), nên mức trích lập dự phòng đổi RWA của chính khoản đó. Xem [[specific-provision]].

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Đ12.1 nêu điều kiện về khoản thế chấp nhà ở theo Đ16.2a(i), (ii): nguồn dùng cấu trúc câu dài với lặp từ, cần đối chiếu pdf/docx để xác nhận phạm vi [cần nguồn].
