---
title: "Tài sản Thanh khoản cao và Dự trữ NHTW trong NSFR (HQLA and Central Bank Reserves)"
aliases: [HQLA trong NSFR, Central Bank Reserves NSFR, RSF Tài sản thanh khoản]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[required-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-25]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "-", cite: "[[src-bcbs-nsfr#^nsf30-26]]"}
tags: [nsfr, rsf, hqla, central-bank-reserves, level-1-assets, level-2-assets]
updated: 2026-10-21
reviewed:
---

## Định nghĩa

Tài sản có tính thanh khoản cao ([[hqla]]) và dự trữ tại Ngân hàng Trung ương là nhóm tài sản đòi hỏi ít nguồn vốn ổn định nhất trong mẫu số [[required-stable-funding|RSF]], nhận hệ số **RSF từ 0% đến 50%** tùy thuộc vào mức độ khả mại và phân tầng chất lượng tài sản [[src-bcbs-nsfr#^nsf30-25]] [[src-bcbs-nsfr#^nsf30-26]] [[src-bcbs-nsfr#^nsf30-28]] [[src-bcbs-nsfr#^nsf30-29]]. Do có thể nhanh chóng chuyển hóa thành tiền mặt hoặc dùng làm tài sản bảo đảm trên thị trường repo, danh mục này hầu như không cần phải tài trợ hoàn toàn bằng nguồn vốn dài hạn 1 năm [[src-bcbs-nsfr#^nsf30-3]].

## Công thức & tham số

### 1. Phân tầng Hệ số RSF cho Tiền tệ và HQLA

| Hệ số RSF | Cấu phần tài sản đủ điều kiện | Căn cứ chuẩn mực |
|:---:|---|---|
| **0%** | - Tiền mặt, tiền xu có sẵn ngay lập tức để thực hiện nghĩa vụ thanh toán [[src-bcbs-nsfr#^nsf30-25]].<br>- Toàn bộ dự trữ tại Ngân hàng Trung ương (bao gồm cả dự trữ bắt buộc và dự trữ vượt mức) [[src-bcbs-nsfr#^nsf30-25]].<br>- Mọi khiếu nại đối với NHTW có kỳ hạn còn lại dưới 6 tháng (tín phiếu NHTW, tiền gửi qua đêm) [[src-bcbs-nsfr#^nsf30-25]].<br>- Các khoản phải thu ngày giao dịch (trade date receivables) từ bán chứng khoán, ngoại tệ [[src-bcbs-nsfr#^nsf30-25]]. | NSF30.25 |
| **5%** | - Tài sản [[level-1-assets]] unencumbered theo định nghĩa LCR30.41 (trừ tài sản nhận 0% RSF ở trên) [[src-bcbs-nsfr#^nsf30-26]].<br>- Chứng khoán thị trường gán trọng số rủi ro 0% theo CRE20 do chính phủ, NHTW, PSE, BIS, IMF, ECB phát hành hoặc bảo lãnh [[src-bcbs-nsfr#^nsf30-26]].<br>- Trái phiếu chính phủ hoặc NHTW phát hành bằng ngoại tệ (kể cả phần vượt hạn mức stressed net outflows ngoại tệ của LCR) [[src-bcbs-nsfr#^nsf30-26]]. | NSF30.26 |
| **15%** | - Tài sản [[level-2-assets\|Level 2A]] unencumbered theo định nghĩa LCR30.43 [[src-bcbs-nsfr#^nsf30-28]].<br>- Chứng khoán thị trường gán trọng số rủi ro 20% của chính phủ, NHTW, PSE hoặc MDB [[src-bcbs-nsfr#^nsf30-28]].<br>- Trái phiếu doanh nghiệp (kể cả thương phiếu) và trái phiếu có bảo đảm (covered bonds) có xếp hạng tín nhiệm tối thiểu từ **AA-** trở lên [[src-bcbs-nsfr#^nsf30-28]]. | NSF30.28 |
| **50%** | - Tài sản Level 2B unencumbered theo định nghĩa LCR30.45 [[src-bcbs-nsfr#^nsf30-29]].<br>- Chứng khoán bảo đảm bằng thế chấp nhà ở (RMBS) xếp hạng tối thiểu **AA** [[src-bcbs-nsfr#^nsf30-29]].<br>- Trái phiếu doanh nghiệp có xếp hạng từ **BBB- đến A+** [[src-bcbs-nsfr#^nsf30-29]].<br>- Cổ phiếu phổ thông giao dịch trên sàn lớn không do định chế tài chính phát hành [[src-bcbs-nsfr#^nsf30-29]]. | NSF30.29 |

## Diễn giải

### Cơ chế & drivers

#### 2. Điểm Khác biệt Cốt lõi giữa HQLA trong NSFR và LCR
- **Không áp dụng Trần Khống chế (Caps Relief)**: Trong chuẩn mực [[lcr]], tài sản Level 2 bị khống chế tối đa 40% và Level 2B tối đa 15% của tổng HQLA sau khi unwind giao dịch ngắn hạn [[src-bcbs-lcr#^lcr30-31]]. Ngược lại, **trong NSFR, toàn bộ tài sản thỏa mãn tiêu chí Level 1, 2A, 2B đều được áp hệ số RSF tương ứng (5%, 15%, 50%) mà không bị giới hạn bởi bất kỳ trần tỷ trọng nào** (Footnote NSF30 Footnote 12) [[src-bcbs-nsfr#^nsf10-2]].
- **Không áp dụng Yêu cầu Vận hành (Operational Requirements Relief)**: Các yêu cầu vận hành khắt khe của LCR (như bắt buộc phải bán thử nghiệm định kỳ *periodic monetisation*, hoặc yêu cầu Treasury độc lập kiểm soát) không hạn chế việc phân loại tài sản vào danh mục HQLA để tính RSF trong NSFR [[src-bcbs-nsfr#^nsf10-2]].

#### 3. Đối xử Ngoại tệ Trọng yếu và Nợ công Ngoại tệ
- Trong LCR, trái phiếu chính phủ phát hành bằng ngoại tệ chỉ được tính vào Level 1 tối đa bằng mức dòng tiền ra ròng dự kiến trong ngoại tệ đó [[src-bcbs-lcr#^lcr30-41]].
- Nhưng trong NSFR, toàn bộ số dư trái phiếu chính phủ ngoại tệ này đều được công nhận là Level 1 và nhận hệ số **RSF 5%** [[src-bcbs-nsfr#^nsf30-26]].

### Phụ thuộc regime
- **Khi NHTW Thắt chặt Tiền tệ (Quantitative Tightening - QT)**:
  - Khi NHTW thu hẹp bảng cân đối kế toán, dự trữ NHTW (RSF 0%) của hệ thống ngân hàng bị sụt giảm.
  - Các ngân hàng phải chuyển hướng sang nắm giữ trái phiếu chính phủ (RSF 5%) hoặc mở rộng tín dụng, làm gia tăng tổng quy mô mẫu số RSF.

### Bằng chứng thực nghiệm
- Khảo sát của EBA (Cơ quan Ngân hàng Châu Âu) cho thấy, danh mục HQLA chiếm trung bình 18% tổng tài sản của các ngân hàng Châu Âu nhưng chỉ đóng góp chưa đầy 3% vào tổng mẫu số RSF, chứng minh hiệu quả giải phóng vốn ổn định vượt trội của nhóm tài sản này.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Tiền mặt, dự trữ NHTW | 0% [[src-bcbs-nsfr#^nsf30-25]] | 0%: tiền mặt, tiền gửi dự trữ bắt buộc kể cả phần vượt [[src-tt50-2026-nhnn#^pl2-b2-8]] | TT50 PL2 Bảng 10 khoản A.8.1–A.8.2 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Phải đòi NHTW dưới 6 tháng | 0% [[src-bcbs-nsfr#^nsf30-25]] | HQLA do NHNN phát hành còn dưới 6 tháng: 0%; phải đòi NHNN không kỳ hạn, dưới 6 tháng: 0% [[src-tt50-2026-nhnn#^pl2-b2-8]] [[src-tt50-2026-nhnn#^pl2-b2-9]] | TT50 PL2 Bảng 10 khoản A.8.3, A.10.1 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Phải đòi NHTW từ 6 tháng | 6 tháng – dưới 1 năm: 50% [[src-bcbs-nsfr#^nsf30-29]] | 50% từ 6 tháng tới dưới 1 năm; từ 1 năm: 65% (NHNN, NHTW hệ số rủi ro tới 35%) hoặc 85% [[src-tt50-2026-nhnn#^pl2-b2-9]] | TT50 PL2 Bảng 10 khoản A.10 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Level 1 | 5% [[src-bcbs-nsfr#^nsf30-26]] | HQLA cấp 1 khác: 5% [[src-tt50-2026-nhnn#^pl2-b2-8]] | TT50 PL2 Bảng 10 khoản A.8.4 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Level 2A | 15% [[src-bcbs-nsfr#^nsf30-28]] | HQLA cấp 2A: 15% [[src-tt50-2026-nhnn#^pl2-b2-8]] | TT50 PL2 Bảng 10 khoản A.8.5 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Level 2B | 50% [[src-bcbs-nsfr#^nsf30-29]] | HQLA cấp 2B: 50% [[src-tt50-2026-nhnn#^pl2-b2-8]] | TT50 PL2 Bảng 10 khoản A.8.6 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Trade date receivables | 0% [[src-bcbs-nsfr#^nsf30-25]] | 0% [[src-tt50-2026-nhnn#^pl2-b2-1]] | TT50 PL2 Bảng 10 khoản A.6 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |

*Diễn giải:* TT50 gắn hệ số RSF của chứng khoán vào phân loại HQLA theo PL I, không dùng hạng tín nhiệm như NSF30.28–29.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM Treasury**:
  - Tối ưu hóa đệm HQLA: Việc phân bổ danh mục HQLA vào Trái phiếu Chính phủ Level 1 (RSF 5%) là lựa chọn ưu việt nhất về mặt vốn ổn định so với việc nắm giữ Trái phiếu Doanh nghiệp Level 2B (RSF 50%).
  - Với mỗi 1.000 tỷ VND tài sản Level 1, Treasury chỉ cần chuẩn bị 50 tỷ VND nguồn vốn ổn định (ASF); nhưng nếu nắm giữ 1.000 tỷ VND tài sản Level 2B, Treasury phải chuẩn bị tới 500 tỷ VND nguồn vốn ổn định!
- **Chính sách Tiền tệ**:
  - Dự trữ bắt buộc tại NHTW được gán RSF 0%: Chuẩn mực Basel cho phép cơ quan giám sát và NHTW thỏa thuận áp dụng hệ số 0% nếu dự trữ bắt buộc có thể sử dụng linh hoạt theo cơ chế bình quân kỳ duy trì [[src-bcbs-nsfr#^nsf30-25]].

## Câu hỏi mở
- Tại Việt Nam, quy định tại [[tt50-2026|Thông tư 50/2026/TT-NHNN]] có cho phép áp dụng hệ số RSF 0% cho toàn bộ số dư dự trữ bắt buộc tại NHNN hay yêu cầu phân loại theo kỳ hạn?
  - TT50 PL2: tiền gửi dự trữ bắt buộc tại NHNN, kể cả phần vượt dự trữ bắt buộc, nhận RSF 0% ở cột không kỳ hạn [[src-tt50-2026-nhnn#^pl2-b2]].
