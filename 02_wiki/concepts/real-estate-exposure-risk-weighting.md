---
title: "Real Estate Exposure Risk Weighting"
aliases: [Real Estate Exposure Risk Weighting, Hệ số rủi ro tín dụng khoản phải đòi bất động sản, Khoản phải đòi bất động sản]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[credit-risk-weight]]", cite: "[[src-tt14-2025-nhnn#^d9-3a]]"}
tags: [capital, credit-risk, collateral, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Khoản phải đòi bất động sản là khoản phải đòi đối với cá nhân, pháp nhân để mua, thuê mua, xây dựng, cải tạo, sửa chữa, kinh doanh bất động sản hoặc dự án bất động sản, trừ khoản thuộc Đ12, 13, 14 [[src-tt14-2025-nhnn#^d16-1]]. Hệ số rủi ro tín dụng (CRW) phụ thuộc việc khoản đó có đủ tiêu chuẩn hay không, [[loan-to-value]] (LTV), nguồn trả nợ và số tài sản bảo đảm [[src-tt14-2025-nhnn#^d16-2]] [[src-tt14-2025-nhnn#^d9-3b]]. Xem [[credit-risk-weight]].

## Cơ chế & drivers
**Phân loại (Đ16.2)** [[src-tt14-2025-nhnn#^d16-2]]:
- đủ tiêu chuẩn: thế chấp bằng nhà ở xã hội; nhà ở đủ tiêu chuẩn; bất động sản thương mại đủ tiêu chuẩn;
- không đủ tiêu chuẩn (b(i)): nhà ở hoặc bất động sản thương mại có sẵn được chuyển nhượng nhưng chưa có giấy chứng nhận quyền sử dụng đất, quyền sở hữu tài sản gắn liền với đất;
- không đủ tiêu chuẩn (b(ii)): các trường hợp còn lại.

**Hai yếu tố của khoản đủ tiêu chuẩn (Đ16.3)** [[src-tt14-2025-nhnn#^d16-3]]:
- có tài sản bảo đảm đủ tiêu chuẩn: là nhà ở hoặc bất động sản thương mại có sẵn, được chuyển nhượng và có giấy chứng nhận; ngân hàng có quyền hợp pháp xử lý; ngân hàng xác định giá trị theo Đ16.5c;
- tổng giá trị định giá của tài sản bảo đảm đủ tiêu chuẩn duy trì tối thiểu bằng 100% giá trị khoản phải đòi.

**Nhà ở xã hội (Đ16.4).** Khoản cho cá nhân vay để mua, thuê mua nhà ở xã hội hoặc nhà ở theo chương trình hỗ trợ của Chính phủ, được đảm bảo bằng chính nhà ở hình thành từ vốn vay [[src-tt14-2025-nhnn#^d16-4]].

**Bảng CRW theo LTV (Đ17.1 và 17.2).** Mỗi loại có hai dòng theo nguồn trả nợ: không từ tài sản bảo đảm (điểm a) và từ tài sản bảo đảm (điểm b).

| LTV | Dưới 40% | 40% đến dưới 60% | 60% đến dưới 80% | 80% đến dưới 90% | 90% đến dưới 100% | Từ 100% | Nguồn |
|---|---|---|---|---|---|---|---|
| Nhà ở xã hội, nguồn trả nợ không từ tài sản bảo đảm | 20% | 25% | 30% | 35% | 40% | 45% | [[src-tt14-2025-nhnn#^d17-1a]] |
| Nhà ở xã hội, nguồn trả nợ từ tài sản bảo đảm | 25% | 30% | 35% | 40% | 45% | 50% | [[src-tt14-2025-nhnn#^d17-1b]] |
| Nhà ở đủ tiêu chuẩn, nguồn trả nợ không từ tài sản bảo đảm | 25% | 30% | 40% | 50% | 60% | 80% | [[src-tt14-2025-nhnn#^d17-2a]] |
| Nhà ở đủ tiêu chuẩn, nguồn trả nợ từ tài sản bảo đảm | 30% | 40% | 50% | 70% | 80% | 100% | [[src-tt14-2025-nhnn#^d17-2b]] |

**Bất động sản thương mại đủ tiêu chuẩn (Đ17.3).**
- Nguồn trả nợ từ tài sản bảo đảm [[src-tt14-2025-nhnn#^d17-3b]]:

| LTV | Dưới 60% | 60% đến dưới 75% | Từ 75% |
|---|---|---|---|
| CRW | 75% | 100% | 120% |

- Nguồn trả nợ không từ tài sản bảo đảm [[src-tt14-2025-nhnn#^d17-3a]]:

| Đối tượng | LTV dưới 60% | LTV từ 60% |
|---|---|---|
| Cá nhân | 60% | 75% nếu tổng số dư cấp tín dụng của các khoản phải đòi bất động sản của khách hàng không vượt quá 8 tỷ đồng; nếu không là 100% |
| Doanh nghiệp | Như CRW doanh nghiệp theo Đ19.1 hoặc 19.2, tối đa 60% | Đúng CRW doanh nghiệp theo Đ19.1 hoặc 19.2 |

**Bất động sản không đủ tiêu chuẩn.**
- Loại b(i) (Đ17.4): nguồn trả nợ không từ tài sản bảo đảm, cá nhân 75% nếu tổng số dư cấp tín dụng của các khoản phải đòi bất động sản không vượt quá 8 tỷ đồng, nếu không 100%; doanh nghiệp theo Đ19.1 hoặc 19.2 [[src-tt14-2025-nhnn#^d17-4a]]. Nguồn trả nợ từ tài sản bảo đảm: 150% [[src-tt14-2025-nhnn#^d17-4b]].
- Loại b(ii) (Đ17.5): cá nhân 100%; doanh nghiệp lấy giá trị lớn hơn giữa 150% và CRW doanh nghiệp theo Đ19.1 hoặc 19.2 [[src-tt14-2025-nhnn#^d17-5]].

CRW doanh nghiệp xem [[corporate-exposure-risk-weighting]].

**Nhiều tài sản bảo đảm (Đ9.3).**
- Một tài sản bảo đảm, hoặc thế chấp bằng nhà ở xã hội: áp dụng CRW tại Đ17 [[src-tt14-2025-nhnn#^d9-3a]].
- Nhiều tài sản bảo đảm (trừ nhà ở xã hội theo Đ16.4) [[src-tt14-2025-nhnn#^d9-3b]]:

| Trường hợp | CRW áp dụng | Nguồn |
|---|---|---|
| (i) Khoản đủ tiêu chuẩn; một hoặc nhiều tài sản bảo đảm đủ tiêu chuẩn có giá trị tối thiểu 100% khoản phải đòi | CRW thấp nhất trong các tài sản bảo đảm đủ tiêu chuẩn | [[src-tt14-2025-nhnn#^d9-3b1]] |
| (ii) Khoản đủ tiêu chuẩn; không tài sản bảo đảm đủ tiêu chuẩn nào có giá trị từ 100% khoản phải đòi trở lên | CRW cao nhất trong các tài sản bảo đảm đủ tiêu chuẩn theo Đ17 | [[src-tt14-2025-nhnn#^d9-3b2]] |
| (iii) Khoản không đủ tiêu chuẩn; có tài sản bảo đảm đủ tiêu chuẩn và tài sản theo Đ16.2b(i) với tổng giá trị tối thiểu 100%, hoặc chỉ có tài sản theo Đ16.2b(i) với giá trị tối thiểu 100% | CRW theo Đ17.4 | [[src-tt14-2025-nhnn#^d9-3b3]] |
| (iv) Các trường hợp còn lại | CRW theo Đ17.5 | [[src-tt14-2025-nhnn#^d9-3b4]] |

- Một tài sản bảo đảm cho nhiều khoản phải đòi: ngân hàng phân tách giá trị tài sản bảo đảm cho từng khoản theo thỏa thuận giữa các bên (nếu có) và quy định nội bộ, rồi áp dụng điểm a hoặc b [[src-tt14-2025-nhnn#^d9-3c]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** CRW bất động sản tăng theo LTV và cao hơn khi nguồn trả nợ phụ thuộc chính tài sản bảo đảm. Với bất động sản thương mại đủ tiêu chuẩn, khoản của cá nhân có trần 75% khi tổng dư cấp tín dụng bất động sản của khách hàng không quá 8 tỷ đồng, còn khoản của doanh nghiệp theo CRW doanh nghiệp [[src-tt14-2025-nhnn#^d17-3a]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* mức CRW trong bảng Đ17 tăng khi LTV tăng, nên giá bất động sản giảm làm RWA tăng ở chính các khoản đang nắm giữ. Khoản có nguồn trả nợ từ tài sản bảo đảm (ví dụ dự án cho thuê) có CRW cao hơn cùng mức LTV. Quy tắc (i) chọn CRW thấp nhất, quy tắc (ii) chọn CRW cao nhất; cơ cấu tài sản bảo đảm của một khoản vay đổi RWA ngay cả khi tổng giá trị bảo đảm không đổi.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Tiêu chí "nguồn trả nợ từ tài sản bảo đảm" trong thực tế danh mục (ví dụ cho vay dự án bất động sản): nguồn không định nghĩa trong C2-M2 [cần nguồn].
