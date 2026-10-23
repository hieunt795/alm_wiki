---
title: "Eligible Collateral and Haircuts"
aliases: [Eligible Collateral and Haircuts, Eligible Collateral, Collateral Haircut, Hệ số hiệu chỉnh tài sản bảo đảm, Tài sản bảo đảm đủ điều kiện giảm thiểu]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[credit-risk-mitigation]]", cite: "[[src-tt14-2025-nhnn#^d25-2]]"}
tags: [capital, credit-risk, collateral, haircut, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ26 TT14/2025 giới hạn giảm thiểu rủi ro tín dụng bằng tài sản bảo đảm ở sáu nhóm tài sản [[src-tt14-2025-nhnn#^d26-1]]. Hệ số hiệu chỉnh tài sản bảo đảm (Hc) nằm từ 0 đến 30% tuỳ loại tài sản, xếp hạng người phát hành và thời hạn còn lại [[src-tt14-2025-nhnn#^d26-3b]]. Hc là tham số do cơ quan quản lý ấn định, nên không phải metric. Xem [[credit-risk-mitigation]].

## Cơ chế & drivers
**Tài sản đủ điều kiện (Đ26.1)** [[src-tt14-2025-nhnn#^d26-1]]:
1. tiền mặt; giấy tờ có giá do tổ chức tín dụng, chi nhánh ngân hàng nước ngoài phát hành; số dư tiền gửi có kỳ hạn hoặc tiền gửi tiết kiệm (thỏa thuận gửi tiền);
2. vàng;
3. giấy tờ có giá do Chính phủ Việt Nam, NHNN, Kho bạc Nhà nước, UBND tỉnh/thành phố, ngân hàng chính sách phát hành hoặc bảo lãnh thanh toán;
4. chứng khoán nợ do Chính phủ các nước, tổ chức công lập của Chính phủ các nước phát hành, xếp hạng từ BB- trở lên;
5. chứng khoán nợ do doanh nghiệp phát hành, xếp hạng từ BBB- trở lên;
6. cổ phiếu niêm yết trên Sở giao dịch Chứng khoán Việt Nam.

Xếp hạng do doanh nghiệp xếp hạng tín nhiệm độc lập thực hiện ([[external-credit-rating-use]]).

**Điều kiện (Đ26.2)** [[src-tt14-2025-nhnn#^d26-2]]:
- tuân thủ pháp luật về giao dịch bảo đảm;
- giấy tờ có giá, chứng khoán nợ, cổ phiếu không do khách hàng, công ty mẹ, công ty con, công ty liên kết của khách hàng phát hành hoặc bảo lãnh thanh toán;
- chứng khoán nợ doanh nghiệp và cổ phiếu phải có giao dịch khớp lệnh trong 10 ngày làm việc liền kề trước thời điểm tính.

**Hc bằng 0 (Đ26.3a).** Tiền mặt, thỏa thuận gửi tiền, giấy tờ có giá do chính ngân hàng phát hành, giấy tờ có giá do Chính phủ Việt Nam, NHNN, Kho bạc Nhà nước, UBND tỉnh/thành phố, ngân hàng chính sách phát hành hoặc bảo lãnh thanh toán [[src-tt14-2025-nhnn#^d26-3a]].

**Bảng Hc (Đ26.3b)** [[src-tt14-2025-nhnn#^d26-3b]]. Đơn vị %:

| Xếp hạng người phát hành | Thời hạn còn lại | Chính phủ (gồm tổ chức áp dụng CRW tương đương) | Tổ chức phát hành khác |
|---|---|---|---|
| AAA đến AA- | ≤ 1 năm | 0,5 | 1 |
| AAA đến AA- | > 1 năm, ≤ 3 năm | 2 | 3 |
| AAA đến AA- | > 3 năm, ≤ 5 năm | (ô trống) | 4 |
| AAA đến AA- | > 5 năm, ≤ 10 năm | 4 | 6 |
| AAA đến AA- | > 10 năm | (ô trống) | 12 |
| A+ đến BBB-; thỏa thuận gửi tiền, giấy tờ có giá của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác (trừ Đ26.6) | ≤ 1 năm | 1 | 2 |
| như dòng trên | > 1 năm, ≤ 3 năm | 3 | 4 |
| như dòng trên | > 3 năm, ≤ 5 năm | (ô trống) | 6 |
| như dòng trên | > 5 năm, ≤ 10 năm | 6 | 12 |
| như dòng trên | > 10 năm | (ô trống) | 20 |
| BB+ đến BB-, trừ thỏa thuận gửi tiền, giấy tờ có giá của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác | Tất cả các loại thời hạn | 15 | Không có |
| Cổ phiếu trong chỉ số VN30/HNX30 (gồm trái phiếu chuyển đổi của các cổ phiếu này) và vàng | | 20 | |
| Cổ phiếu khác niêm yết trên Sở giao dịch chứng khoán Việt Nam | | 30 | |

Ô trống ở cột Chính phủ (các dòng > 3 năm, ≤ 5 năm và > 10 năm) là ô trống trong bảng raw; có thể là ô gộp với dòng liền trên, nguồn không xác nhận nên wiki không điền số [cần nguồn]. Với cổ phiếu và vàng, giá trị 20 và 30 nằm ở cột Chính phủ theo cấu trúc raw, dù hai nhóm này không có người phát hành Chính phủ; cột này ở các dòng đó nên đọc là Hc chung [cần nguồn].

**Độ lệch thời hạn (Đ26.4).** Tài sản bảo đảm trừ tiền mặt và vàng hiệu chỉnh $C^{*} = C \times (t - 0{,}25) / (T - 0{,}25)$. T là giá trị nhỏ hơn giữa 05 năm và thời hạn còn lại của khoản phải đòi, giao dịch; t là giá trị nhỏ hơn giữa T và thời hạn còn lại của tài sản bảo đảm, cả hai tính theo năm [[src-tt14-2025-nhnn#^d26-4]].

**Độ lệch tiền tệ (Đ26.5).** Hệ số hiệu chỉnh $H_{fxc}$ bằng 8% [[src-tt14-2025-nhnn#^d26-5]].

**Ngoại lệ thỏa thuận gửi tiền (Đ26.6).** Với thỏa thuận gửi tiền của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác, thời hạn còn lại để tra bảng Hc lấy theo thời hạn còn lại của khoản phải đòi và không phải hiệu chỉnh độ lệch thời hạn, nếu [[src-tt14-2025-nhnn#^d26-6]]:
- thỏa thuận có điều khoản tự động tiếp tục gửi khi đáo hạn và khách hàng không được rút trước hạn;
- ngân hàng thỏa thuận trong hợp đồng cấp tín dụng hoặc hợp đồng bảo đảm quyền kiểm soát toàn bộ thanh toán, dòng tiền của thỏa thuận gửi tiền để thu hồi nợ.

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]]. Đ26 cũng áp dụng cho tài sản bảo đảm của giao dịch phái sinh và repo theo Phụ lục II [[src-tt14-2025-nhnn#^pl2-2]].

## Góc nhìn theo domain
**VN Regulator.** Hc của trái phiếu Chính phủ Việt Nam bằng 0 theo Đ26.3a, khác cột Chính phủ (0,5% đến 4%) áp dụng cho Chính phủ nước ngoài xếp hạng AAA đến AA- [[src-tt14-2025-nhnn#^d26-3a]] [[src-tt14-2025-nhnn#^d26-3b]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* tài sản bảo đảm là giấy tờ có giá phát hành bởi Chính phủ Việt Nam hoặc NHNN không bị haircut theo Đ26.3a, nhưng vẫn chịu hiệu chỉnh độ lệch thời hạn và độ lệch tiền tệ. Treasury dùng trái phiếu Chính phủ làm tài sản bảo đảm cho repo có thể thấy RWA đối tác bằng $\max\{0; E - C(1 - 0 - 0)\} \times CRW$ khi cùng đồng tiền. Xem [[counterparty-credit-risk-rwa]].

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Hc của tài sản không xếp hạng: ví dụ Phụ lục II dùng 12% cho trái phiếu 10 năm của Ngân hàng C không có xếp hạng "theo Điều 26" [[src-tt14-2025-nhnn#^pl2-vd1]]. Bảng Đ26.3b không có dòng "không xếp hạng" (con số 12% trùng ô "A+ đến BBB-, > 5 đến 10 năm, tổ chức phát hành khác"). Cần đối chiếu bản gốc [cần nguồn].
