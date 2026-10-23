---
title: "Credit Rating Scale Mapping"
aliases: [Credit Rating Scale Mapping, Bảng quy đổi thang xếp hạng tín nhiệm, Thang thứ hạng tín nhiệm]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[external-credit-rating-use]]", cite: "[[src-tt14-2025-nhnn#^d24-3a]]"}
tags: [capital, credit-risk, rating, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ24.3a phân bố thang thứ hạng của Standard & Poor's, Moody's và Fitch Rating vào sáu nhóm tương ứng mức độ rủi ro khi tính tỷ lệ an toàn vốn [[src-tt14-2025-nhnn#^d24-3a]]. Doanh nghiệp xếp hạng có thang khác phải chuyển đổi về thang của Moody's, Standard & Poor's hoặc Fitch Rating [[src-tt14-2025-nhnn#^d24-3b]]. Xem [[external-credit-rating-use]].

## Cơ chế & drivers
**Bảng sáu nhóm** [[src-tt14-2025-nhnn#^d24-3a]]:

| Nhóm | Standard & Poor's | Moody's | Fitch Rating |
|---|---|---|---|
| 1 | AAA, AA+, AA, AA- | Aaa, Aa1, Aa2, Aa3 | AAA, AA+, AA, AA- |
| 2 | A+, A, A- | A1, A2, A3 | A+, A, A- |
| 3 | BBB+, BBB, BBB- | Baa1, Baa2, Baa3 | BBB+, BBB, BBB- |
| 4 | BB+, BB, BB- | Ba1, Ba2, Ba3 | BB+, BB, BB- |
| 5 | B+, B, B- | B1, B2, B3 | B+, B, B- |
| 6 | CCC+ và thứ hạng thấp hơn | Caa1 và thứ hạng thấp hơn | CCC+ và thứ hạng thấp hơn |

Cột "Nhóm" do wiki đánh số theo thứ tự hàng của bảng; nguồn không đánh số.

**Chuyển đổi thang khác.** Doanh nghiệp xếp hạng độc lập có thang khác thang ở Đ24.3a phải chuyển đổi thứ hạng tương ứng, phù hợp với thang của Moody's hoặc Standard & Poor's hoặc Fitch Rating, để xác định mức độ rủi ro của khách hàng, đối tác, khoản phải đòi [[src-tt14-2025-nhnn#^d24-3b]].

**Nối với bảng CRW.** Các bảng CRW dùng cụm thứ hạng theo thang S&P (ví dụ "AAA đến AA-", "A+ đến BBB-"):

| Bảng CRW | Cách gộp thứ hạng | Nguồn |
|---|---|---|
| Chính phủ, ngân hàng trung ương nước ngoài (Đ13.5) | Năm cột: AAA đến AA-; A+ đến A-; BBB+ đến BBB-; BB+ đến B-; dưới B- hoặc không xếp hạng | [[src-tt14-2025-nhnn#^d13-5]] |
| Tổ chức tín dụng nước ngoài (Đ14.1) | Bốn cột: AAA đến AA-; A+ đến BBB-; BB+ đến B-; dưới B- hoặc không xếp hạng | [[src-tt14-2025-nhnn#^d14-1]] |
| Tổ chức tín dụng trong nước (Đ14.3) | Năm cột: AAA đến AA-; A+ đến BBB-; BB+ đến BB-; B+ đến B-; dưới B- hoặc không xếp hạng | [[src-tt14-2025-nhnn#^d14-3]] |

*Diễn giải:* ba bảng CRW gộp thứ hạng theo ba cách khác nhau và không bảng nào dùng đúng sáu nhóm của Đ24.3a. Đ14.3 tách nhóm BB và B, còn Đ13.5 và Đ14.1 gộp BB+ đến B-. Khi gán thứ hạng cho bảng CRW, ngân hàng quy về thứ hạng chi tiết (ví dụ BB hay B) rồi tra cột tương ứng của từng bảng; nhóm 6 của Đ24.3a (CCC+ trở xuống) rơi vào cột "dưới B-".

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Đ24.3a chỉ nêu ba tổ chức quốc tế; thang của doanh nghiệp xếp hạng trong nước phải chuyển đổi theo Đ24.3b [[src-tt14-2025-nhnn#^d24-3b]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* trong hệ thống dữ liệu, bảng quy đổi nên lưu thứ hạng gốc của từng tổ chức và nhóm quy đổi, không chỉ nhóm cuối. Bảng CRW cần thứ hạng chi tiết ở một số ranh giới (BB, B).

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Phương pháp chuyển đổi thang của doanh nghiệp xếp hạng trong nước: nguồn không nêu [cần nguồn].
