---
title: "Corporate Exposure Risk Weighting"
aliases: [Corporate Exposure Risk Weighting, Hệ số rủi ro tín dụng khoản phải đòi doanh nghiệp, Khoản phải đòi doanh nghiệp]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[credit-risk-weight]]", cite: "[[src-tt14-2025-nhnn#^d19-1]]"}
tags: [capital, credit-risk, corporate, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ19 đặt hệ số rủi ro tín dụng (CRW) cho khoản phải đòi doanh nghiệp có tư cách pháp nhân, trừ khoản thuộc Đ12, 13, 14, 15, 16 và 18 [[src-tt14-2025-nhnn#^d19-1]]. Doanh nghiệp nhỏ và vừa có CRW 85% [[src-tt14-2025-nhnn#^d19-1]]. Doanh nghiệp khác có CRW theo doanh thu và tỷ lệ đòn bẩy, từ 50% đến 160% [[src-tt14-2025-nhnn#^d19-2a]]. Hệ số này cũng là đầu vào cho bất động sản thương mại, tài trợ chuyên biệt và cho thuê tài chính ([[credit-risk-weight]]).

## Cơ chế & drivers
**Chỉ tiêu đầu vào (Đ19.2)** lấy từ Báo cáo tài chính năm, hợp nhất nếu phải lập [[src-tt14-2025-nhnn#^d19-2]]:
- doanh thu là doanh thu bán hàng và cung cấp dịch vụ, lấy trên Báo cáo kết quả hoạt động kinh doanh;
- vốn chủ sở hữu lấy trên Bảng cân đối kế toán;
- tỷ lệ đòn bẩy bằng tổng nợ vay chia tổng tài sản; tổng nợ vay là tổng vay và nợ thuê tài chính ngắn hạn và dài hạn.

Tỷ lệ đòn bẩy của doanh nghiệp ở đây là đại lượng khác [[leverage-ratio]] của ngân hàng.

**Bảng CRW theo doanh thu và tỷ lệ đòn bẩy** [[src-tt14-2025-nhnn#^d19-2a]]:

| Tỷ lệ đòn bẩy \ Doanh thu | Dưới 100 tỷ đồng | 100 đến dưới 400 tỷ đồng | 400 đến 1500 tỷ đồng | Trên 1500 tỷ đồng |
|---|---|---|---|---|
| Dưới 25% | 100% | 80% | 60% | 50% |
| 25% đến 50% | 125% | 110% | 95% | 80% |
| Trên 50% | 160% | 150% | 140% | 120% |

**Ngoại lệ**:
- CRW 200% cho doanh nghiệp không cung cấp báo cáo tài chính cho ngân hàng, và doanh nghiệp có vốn chủ sở hữu âm hoặc bằng 0 [[src-tt14-2025-nhnn#^d19-2b]];
- CRW 150% cho doanh nghiệp thành lập mới hoạt động chưa được 01 năm, hoặc dưới 15 tháng nhưng được gộp kỳ kế toán theo Luật Kế toán [[src-tt14-2025-nhnn#^d19-2c]].

**Dùng làm đầu vào cho nhóm khác.**
- Bất động sản thương mại đủ tiêu chuẩn của doanh nghiệp (Đ17.3a), bất động sản không đủ tiêu chuẩn (Đ17.4a, 17.5): xem [[real-estate-exposure-risk-weighting]].
- Tài trợ dự án và máy móc thiết bị trước vận hành: xem [[specialised-lending-risk-weighting]].
- Cho thuê tài chính: cao hơn giữa hệ số theo Đ19.1 hoặc 19.2 và 160% [[src-tt14-2025-nhnn#^d23-3]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]]. Tiêu chí doanh nghiệp nhỏ và vừa không nằm trong C2-M2 [cần nguồn].

## Góc nhìn theo domain
**VN Regulator.** CRW doanh nghiệp giảm khi doanh thu cao và đòn bẩy thấp, từ 160% (đòn bẩy trên 50%, doanh thu dưới 100 tỷ đồng) xuống 50% (đòn bẩy dưới 25%, doanh thu trên 1500 tỷ đồng) [[src-tt14-2025-nhnn#^d19-2a]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* CRW của cùng một khoản vay đổi theo số liệu báo cáo tài chính của khách hàng, không đổi theo xếp hạng tín nhiệm nội bộ của ngân hàng. Ngân hàng cần kho dữ liệu doanh thu, nợ vay, tổng tài sản của từng doanh nghiệp để tính RWA; khách hàng không cung cấp báo cáo bị CRW 200%.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Tiêu chí doanh nghiệp nhỏ và vừa dùng cho Đ19.1: [cần nguồn].
