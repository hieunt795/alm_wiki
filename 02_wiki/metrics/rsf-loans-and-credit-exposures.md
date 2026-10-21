---
title: "Danh mục Cho vay và Cấp tín dụng trong NSFR (Loans and Credit Exposures)"
aliases: [Cho vay trong NSFR, Loans and Credit Exposures NSFR, RSF Cho vay]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[required-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-15]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "-", cite: "[[src-bcbs-nsfr#^nsf30-31]]"}
tags: [nsfr, rsf, loans, credit-risk, mortgages, npl]
updated: 2026-10-21
reviewed:
---

## Định nghĩa

Danh mục cho vay khách hàng và các khoản phơi bày tín dụng là cấu phần chiếm tỷ trọng lớn nhất trong mẫu số [[required-stable-funding|RSF]], nhận hệ số **RSF từ 50% đến 100%** tùy thuộc vào kỳ hạn còn lại, đối tác, tài sản bảo đảm và trọng số rủi ro tín dụng theo chuẩn CRE20 [[src-bcbs-nsfr#^nsf30-15]] [[src-bcbs-nsfr#^nsf30-29]] [[src-bcbs-nsfr#^nsf30-30]] [[src-bcbs-nsfr#^nsf30-31]] [[src-bcbs-nsfr#^nsf30-32]]. Chuẩn mực NSFR được thiết kế có chủ đích nhằm bảo đảm hoạt động cấp tín dụng cho nền kinh tế thực được hỗ trợ bởi nguồn vốn ổn định vững chắc, đồng thời tính đến giả định hành vi ngân hàng buộc phải tái cấp vốn (*roll-over*) một tỷ lệ lớn các khoản vay đáo hạn để duy trì quan hệ thương mại với khách hàng [[src-bcbs-nsfr#^nsf30-3]].

## Công thức & tham số

### 1. Phân tầng Hệ số RSF cho Danh mục Tín dụng

| Hệ số RSF | Nhóm sản phẩm cho vay và Điều kiện áp dụng | Căn cứ chuẩn mực |
|:---:|---|---|
| **50%** | **Các khoản cho vay ngắn hạn $< 1$ năm**:<br>- Tất cả các khoản cho vay non-HQLA có kỳ hạn còn lại dưới 1 năm đối với khách hàng doanh nghiệp phi tài chính, bán lẻ, SME, chính phủ và PSE [[src-bcbs-nsfr#^nsf30-29]].<br>- Các khoản cho vay đối với định chế tài chính và NHTW có kỳ hạn từ **6 tháng đến dưới 1 năm** [[src-bcbs-nsfr#^nsf30-29]].<br>- Tiền gửi vận hành ([[operational-deposits]]) gửi tại định chế tài chính khác [[src-bcbs-nsfr#^nsf30-29]]. | NSF30.29 |
| **65%** | **Cho vay dài hạn $\ge 1$ năm chất lượng cao ($\text{RW} \le 35\%$)**:<br>- Cho vay thế chấp nhà ở (*residential mortgages*) unencumbered kỳ hạn $\ge 1$ năm có trọng số rủi ro $\text{RW} \le 35\%$ theo phương pháp Chuẩn hóa CRE20 [[src-bcbs-nsfr#^nsf30-30]].<br>- Các khoản cho vay unencumbered khác kỳ hạn $\ge 1$ năm có $\text{RW} \le 35\%$ đối với chính phủ, NHTW, MDB, PSE (loại trừ định chế tài chính) [[src-bcbs-nsfr#^nsf30-30]]. | NSF30.30 |
| **85%** | **Cho vay dài hạn $\ge 1$ năm thông thường ($\text{RW} > 35\%$)**:<br>- Các khoản cho vay unencumbered đủ tiêu chuẩn (*performing loans*) kỳ hạn còn lại từ 1 năm trở lên có $\text{RW} > 35\%$ theo CRE20 (cho vay doanh nghiệp thương mại, cho vay tiêu dùng không bảo đảm, thẻ tín dụng, thế chấp bất động sản có $\text{RW} > 35\%$) [[src-bcbs-nsfr#^nsf30-31]]. Loại trừ cho vay định chế tài chính. | NSF30.31 |
| **100%** | **Tín dụng kém chất lượng và Cho vay Định chế Tài chính dài hạn**:<br>- Toàn bộ nợ xấu (Non-performing loans - NPLs quá hạn $> 90$ ngày hoặc bị xếp vào nhóm vỡ nợ theo CRE20) [[src-bcbs-nsfr#^nsf30-32]].<br>- Cho vay đối với các định chế tài chính có kỳ hạn còn lại từ 1 năm trở lên [[src-bcbs-nsfr#^nsf30-32]].<br>- Các khoản cho vay không kỳ hạn xác định mà ngân hàng không chứng minh được sẽ đáo hạn thực tế trong vòng 1 năm [[src-bcbs-nsfr#^nsf30-32]]. | NSF30.32 |

## Diễn giải

### Cơ chế & drivers

#### 2. Giả định Hành vi Tái cấp vốn (Roll-over Assumption)
- Tại sao một khoản cho vay doanh nghiệp có kỳ hạn 3 tháng lại chịu hệ số **RSF 50%** thay vì 0%?
- Basel giải thích rằng: Trong hoạt động ngân hàng thực tế, nếu ngân hàng từ chối tái cấp vốn cho một doanh nghiệp khi khoản vay 3 tháng đến hạn, doanh nghiệp đó có thể phá sản hoặc chuyển sang ngân hàng đối thủ. Do đó, ngân hàng buộc phải tái cấp vốn cho khách hàng [[src-bcbs-nsfr#^nsf30-3]]. Giả định này phản ánh rằng ngân hàng chỉ có thể để tối đa 50% dư nợ tự nhiên đáo hạn thu tiền về, 50% còn lại bắt buộc phải được hỗ trợ bởi nguồn vốn ổn định dài hạn [[src-bcbs-nsfr#^nsf30-3]] [[src-bcbs-nsfr#^nsf30-29]].

#### 3. Nguyên tắc Phân tách Khoản vay Bảo đảm Một phần (Partially Secured Loans - NSF99.4)
- Khi một khoản vay chỉ được bảo đảm một phần bằng tài sản thế chấp (dẫn tới các trọng số rủi ro khác nhau giữa phần có bảo đảm và không bảo đảm), ngân hàng phải tách khoản vay thành hai phần tương ứng để áp dụng hệ số RSF phù hợp [[src-bcbs-nsfr#^nsf99-4]].
- **Quy tắc thận trọng tối đa**: Nếu hệ thống dữ liệu của ngân hàng không thể bóc tách rõ ràng giữa phần có bảo đảm và không bảo đảm, **ngân hàng bắt buộc phải áp dụng hệ số RSF cao hơn cho toàn bộ khoản vay** [[src-bcbs-nsfr#^nsf99-4]].

#### 4. Quy tắc Xử lý Khoản vay Khấu hao Dần (Amortising Loans)
- Đối với các khoản vay dài hạn trả góp định kỳ (gốc và lãi trả hàng tháng/hàng quý), phần giá trị gốc đến hạn thanh toán trong vòng 1 năm được bóc tách và phân loại vào nhóm kỳ hạn dưới 1 năm để hưởng hệ số **RSF 50%**, chỉ phần dư nợ gốc thực tế sau 1 năm mới phải chịu hệ số 65% hoặc 85% [[src-bcbs-nsfr#^nsf30-17]].

### Phụ thuộc regime
- **Chu kỳ Tín dụng Mở rộng vs Suy thoái**:
  - Trong giai đoạn tăng trưởng kinh tế, tín dụng trung dài hạn bùng nổ, kéo theo sự gia tăng nhanh chóng của các khoản vay chịu RSF 85%, đòi hỏi Treasury phải liên tục huy động thêm vốn tự có và trái phiếu dài hạn (ASF 100%).
  - Khi nợ xấu gia tăng trong suy thoái, các khoản vay chuyển nhóm từ đủ tiêu chuẩn (RSF 50%–85%) sang NPLs sẽ lập tức bị nâng hệ số RSF lên **100%** [[src-bcbs-nsfr#^nsf30-32]], tạo ra cú sốc làm suy giảm trực tiếp tỷ lệ NSFR của ngân hàng.

### Bằng chứng thực nghiệm
- Dữ liệu giám sát của Basel cho thấy danh mục cho vay khách hàng chiếm từ **60% đến 75%** tổng mẫu số RSF của các ngân hàng thương mại tổng hợp, chứng minh đây là động lực chính định hình nhu cầu nguồn vốn ổn định của toàn ngành ngân hàng.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cho vay khách hàng không phải tổ chức tài chính dưới 1 năm | 50% [[src-bcbs-nsfr#^nsf30-29]] | 50% (bán lẻ, DNNVV, DN, tổ chức khác) [[src-tt50-2026-nhnn#^pl2-b2-16]] | TT50 PL2 Bảng 10 khoản A.18 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Thế chấp nhà ở từ 1 năm, hệ số rủi ro tới 35% | 65% [[src-bcbs-nsfr#^nsf30-30]] | 65% (TT14: gồm nhà ở xã hội) [[src-tt50-2026-nhnn#^pl2-b2-16]] | TT50 PL2 Bảng 10 khoản A.16.2.1, A.17.1 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Cho vay khác từ 1 năm, hệ số rủi ro tới 35% | 65% [[src-bcbs-nsfr#^nsf30-30]] | 65% [[src-tt50-2026-nhnn#^pl2-b2-16]] | TT50 PL2 Bảng 10 khoản A.18.x.1 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Cho vay từ 1 năm, hệ số rủi ro trên 35% | 85% [[src-bcbs-nsfr#^nsf30-31]] | 85% [[src-tt50-2026-nhnn#^pl2-b2-16]] | TT50 PL2 Bảng 10 khoản A.16.2.2, A.18.x.2 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Phải đòi bất động sản không đủ tiêu chuẩn từ 1 năm | [cần nguồn] | 100% [[src-tt50-2026-nhnn#^pl2-b2-16]] | TT50 PL2 Bảng 10 khoản A.16.1 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Phải đòi Chính phủ từ 1 năm | 65% khi hệ số rủi ro tới 35% [[src-bcbs-nsfr#^nsf30-30]] | 65%, không phân biệt hệ số rủi ro [[src-tt50-2026-nhnn#^pl2-b2-9]] | TT50 PL2 Bảng 10 khoản A.9 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Cho vay tổ chức tài chính dưới 6 tháng, bảo đảm Level 1 tái thế chấp được | 10% [[src-bcbs-nsfr#^nsf30-27]] | 10% [[src-tt50-2026-nhnn#^pl2-b2-14]] | TT50 PL2 Bảng 10 khoản A.14.1 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Cho vay tổ chức tài chính khác dưới 6 tháng | 15% [[src-bcbs-nsfr#^nsf30-28]] | 15% [[src-tt50-2026-nhnn#^pl2-b2-14]] | TT50 PL2 Bảng 10 khoản A.14.2 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Cho vay tổ chức tài chính 6 tháng – dưới 1 năm; từ 1 năm | 50%; 100% [[src-bcbs-nsfr#^nsf30-29]] [[src-bcbs-nsfr#^nsf30-32]] | 50%; 100% [[src-tt50-2026-nhnn#^pl2-b2-14]] | TT50 PL2 Bảng 10 khoản A.14 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Tiền gửi tại TCTD khác | Tiền gửi hoạt động 50% [[src-bcbs-nsfr#^nsf30-29]] | Tiền gửi hoạt động 50%; tiền gửi tại TCTD, chi nhánh NHNNg, TCTD nước ngoài không kỳ hạn và dưới 6 tháng 15% [[src-tt50-2026-nhnn#^pl2-b2-14]] | TT50 PL2 Bảng 10 khoản A.15 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Nợ vỡ nợ | 100% [[src-bcbs-nsfr#^nsf30-32]] | Khoản phải đòi vỡ nợ (theo TT14) 100% [[src-tt50-2026-nhnn#^pl2-b2-1]] [[src-tt50-2026-nhnn#^pl2-b1]] | TT50 PL2 Bảng 10 khoản A.1 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Kỳ hạn khi có quyền gia hạn, cơ cấu nợ | Giả định nhà đầu tư thực hiện quyền gia hạn [[src-bcbs-nsfr#^nsf30-17]] | Tính tới thời điểm muộn nhất; cơ cấu lại theo pháp luật thì gồm cả thời gian cơ cấu lại tối đa [[src-tt50-2026-nhnn#^d24-3c]] | TT50 Đ24.3 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Khoản vay trả nhiều kỳ | [cần nguồn] | Tách từng phần trả nợ theo thời điểm trả [[src-tt50-2026-nhnn#^d24-5]] | TT50 Đ24.5 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |

*Diễn giải:* khoản vay đã hoặc có thể được cơ cấu lại thời hạn theo pháp luật bị đẩy kỳ hạn ra xa hơn [[src-tt50-2026-nhnn#^d24-3c]]. Phần trả gốc dưới 1 năm có thể rơi sang cột từ 1 năm và nhận 65% hoặc 85% thay vì 50%.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM Treasury**:
  - RSF định giá trực tiếp rủi ro cấu trúc bảng cân đối vào chính sách lãi suất cho vay: Một khoản vay thương mại dài hạn chịu RSF 85% tiêu tốn chi phí vốn ổn định cao hơn đáng kể so với khoản vay thế chấp nhà ở (RSF 65%).
  - Treasury bắt buộc phải đưa chỉ tiêu RSF vào ma trận thẩm định phê duyệt tín dụng của Hội đồng ALCO ([[alco]]).
- **Rủi ro Tín dụng**:
  - Trọng số rủi ro tín dụng (Risk-Weight) liên kết trực tiếp với thanh khoản: Ngân hàng có năng lực quản trị rủi ro tốt, lựa chọn các khoản vay có $\text{RW} \le 35\%$ sẽ tiết kiệm được 20% yêu cầu nguồn vốn ổn định (RSF 65% thay vì 85%) [[src-bcbs-nsfr#^nsf30-30]] [[src-bcbs-nsfr#^nsf30-31]].

## Câu hỏi mở
- Tại Việt Nam, các khoản cho vay trung dài hạn đối với các dự án bất động sản và hạ tầng BOT/BT (chiếm tỷ trọng đáng kể tại các NHTM) sẽ được phân loại chịu hệ số RSF 85% hay 100% theo hướng dẫn của TT50?
