---
title: Committed credit and liquidity facilities
aliases: [Committed facilities, Hạn mức tín dụng cam kết, Drawdown rate, Liquidity facility]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]", "[[src-bcbs-liquidity-principles-2008]]", "[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-59]]"}
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr40-64]]"}
tags: [off-balance-sheet, liquidity, contingent]
updated: 2026-10-21
reviewed:
---

## Ý chính

Hạn mức cam kết tín dụng và thanh khoản (**committed credit and liquidity facilities**) là thỏa thuận cấp vốn trong tương lai cho khách hàng bán lẻ hoặc khách hàng bán buôn, bao gồm các hợp đồng không thể hủy ngang (*committed*) hoặc chỉ có thể hủy ngang có điều kiện (*conditionally cancellable*) [[src-bcbs-lcr#^lcr40-59]].

Trong kịch bản kiểm tra sức chịu tải thanh khoản 30 ngày của [[lcr]], phần hạn mức cam kết chưa giải ngân được giả định sẽ bị khách hàng rút vốn theo tỷ lệ giải ngân (*drawdown rate*) tương ứng với mức độ rủi ro của từng nhóm đối tác [[src-bcbs-lcr#^lcr40-59]] [[src-bcbs-lcr#^lcr40-64]]. Toàn bộ phần hạn mức đã rút trước đó được tính vào dư nợ nội bảng và giả định không được hoàn trả trong 30 ngày căng thẳng [[src-bcbs-lcr#^lcr40-59]].

## Cơ chế & drivers

### 1. Ma trận Drawdown Rate Chuẩn mực theo Basel (LCR40.64)

Phần giá trị hạn mức chưa giải ngân chịu tỷ lệ rút vốn giả định như sau [[src-bcbs-lcr#^lcr40-64]]:

| Đối tượng nhận hạn mức | Credit facility | Liquidity facility | Căn cứ Basel |
|---|:---:|:---:|---|
| Khách hàng bán lẻ và doanh nghiệp nhỏ (SME) | 5% | 5% | [[src-bcbs-lcr#^lcr40-64]] |
| Doanh nghiệp phi tài chính, chính phủ, NHTW, PSE, MDB | 10% | 30% | [[src-bcbs-lcr#^lcr40-64]] |
| Ngân hàng chịu giám sát an toàn vi mô | 40% | 40% | [[src-bcbs-lcr#^lcr40-64]] |
| Định chế tài chính khác (công ty chứng khoán, bảo hiểm, quỹ tín thác) | 40% | 100% | [[src-bcbs-lcr#^lcr40-64]] |
| Pháp nhân chuyên biệt và đối tượng khác (SPE, conduit, SPV) | 100% | 100% | [[src-bcbs-lcr#^lcr40-64]] |

### 2. Tiêu chí Phân biệt Credit Facility vs Liquidity Facility

- **Liquidity Facility** (Hạn mức thanh khoản): Là bất kỳ hạn mức cam kết chưa rút nào được thiết lập nhằm mục đích tái tài trợ các nghĩa vụ nợ của khách hàng trong trường hợp khách hàng không thể đảo nợ trên thị trường tài chính (ví dụ: bảo lãnh thanh khoản cho chương trình thương phiếu ABCP) [[src-bcbs-lcr#^lcr40-61]]. Quy mô tính là liquidity facility bị khống chế tối đa bằng phần nghĩa vụ nợ của khách hàng đáo hạn trong vòng 30 ngày; phần cam kết vượt quá mức nợ này được phân loại sang credit facility [[src-bcbs-lcr#^lcr40-61]].
- **Credit Facility** (Hạn mức tín dụng): Mọi hạn mức cam kết cấp vốn lưu động thông thường (*revolving working capital facilities*) cấp cho doanh nghiệp để phục vụ sản xuất kinh doanh bắt buộc phải xếp vào Credit Facility [[src-bcbs-lcr#^lcr40-61]].
- **Quy tắc Phạt Định chế Đầu cơ**: Mọi hạn mức cung cấp cho quỹ đầu cơ (*hedge funds*), quỹ thị trường tiền tệ (*MMFs*), công ty chứng khoán, SPE, conduit đều bị ấn định 100% là Liquidity Facility và áp dụng drawdown rate 100% [[src-bcbs-lcr#^lcr40-62]] [[src-bcbs-lcr#^lcr40-64]].

### 3. Bù trừ với Tài sản Bảo đảm HQLA (Collateral Netting)

Phần hạn mức chưa giải ngân được phép tính ròng với giá trị thanh khoản của [[hqla]] mà khách hàng đã ký quỹ hoặc cam kết theo hợp đồng sẽ ký quỹ khi rút vốn (ví dụ hạn mức cơ cấu dạng repo) [[src-bcbs-lcr#^lcr40-60]]. Điều kiện áp dụng bao gồm:
1. Ngân hàng có đầy đủ quyền pháp lý và năng lực vận hành để tái sử dụng tài sản bảo đảm đó [[src-bcbs-lcr#^lcr40-60]].
2. Không tồn tại tương quan đồng biến bất lợi giữa xác suất khách hàng rút vốn và giá trị thị trường của tài sản bảo đảm [[src-bcbs-lcr#^lcr40-60]].

### 4. Các Quy tắc Bổ sung về Nghĩa vụ Ngoại bảng

- **Nghĩa vụ giải ngân cho định chế tài chính**: Các hợp đồng có nghĩa vụ phải giải ngân trong vòng 30 ngày cho các tổ chức tài chính và NHTW nhận dòng ra **100%** [[src-bcbs-lcr#^lcr40-65]].
- **Nghĩa vụ giải ngân cho khách hàng bán lẻ và doanh nghiệp**: Nếu tổng nghĩa vụ giải ngân theo hợp đồng trong 30 ngày vượt quá 50% tổng dòng tiền vào theo hợp đồng từ chính nhóm khách hàng đó, phần chênh lệch dương phải tính vào dòng ra với tỷ lệ **100%** [[src-bcbs-lcr#^lcr40-66]].
- **Hạn mức ngân hàng được cấp**: Hạn mức tín dụng hoặc thanh khoản do tổ chức khác (kể cả NHTW) cấp cho ngân hàng có hệ số thu tiền là **0%** (không được tính vào dòng tiền vào) [[src-bcbs-lcr#^lcr40-75]] [[src-bcbs-lcr#^lcr40-82]].
- **Tài trợ thương mại (*Trade finance*)**: cơ quan quốc gia có thể áp tỷ lệ rút tương đối thấp (ví dụ $\le 5\%$) [[src-bcbs-lcr#^lcr40-71]] cho công cụ gắn trực tiếp với lưu chuyển hàng hoá, dịch vụ: L/C chứng từ thương mại, nhờ thu, hối phiếu xuất nhập khẩu, bảo lãnh nhận hàng [[src-bcbs-lcr#^lcr40-71b]]. Cam kết cho vay xuất nhập khẩu trực tiếp cho doanh nghiệp phi tài chính không thuộc nhóm này, áp tỷ lệ rút hạn mức cam kết của LCR40.64 [[src-bcbs-lcr#^lcr40-72]].
- **Không đếm trùng chương trình tài trợ cấu trúc**: với phần chương trình đã tính ở LCR40.57, 40.58, 40.64 (đáo hạn hoặc có liquidity put trong 30 ngày), ngân hàng cung cấp hạn mức thanh khoản liên quan không được đếm trùng công cụ tài trợ đáo hạn và hạn mức thanh khoản [[src-bcbs-lcr#^lcr40-63]].
- **Dòng tiền ra hợp đồng khác**: Mọi cam kết hợp đồng khác phát sinh dòng tiền ra trong 30 ngày (loại trừ chi phí vận hành thường xuyên) tính dòng ra **100%** [[src-bcbs-lcr#^lcr40-74]].

### 5. Yêu cầu Quản trị Thanh khoản Ngoại bảng theo BCBS 144

- Ngân hàng phải dự phóng quy mô dòng tiền ra tiềm tàng từ việc cam kết chưa giải ngân bị rút đồng loạt trong thời kỳ căng thẳng, có tính đến mức độ tín nhiệm của đối tác và mức độ tập trung danh mục theo ngành hoặc khu vực địa lý [[src-bcbs-liquidity-principles-2008#^lrm-31]].
- Cam kết cho vay chưa giải ngân, thư tín dụng và bảo lãnh tài chính là nguồn hao hụt thanh khoản trọng yếu; ngân hàng cần xác định mức dòng tiền ra trong điều kiện bình thường và mô hình hóa mức tăng đột biến khi xảy ra khủng hoảng [[src-bcbs-liquidity-principles-2008#^lrm-41]].

## Phụ thuộc regime

*Diễn giải:* Trong điều kiện thị trường bình thường, tỷ lệ rút hạn mức cam kết thường duy trì ở mức thấp do khách hàng tối ưu hóa chi phí trả lãi. Tuy nhiên, khi thị trường vốn đóng băng hoặc khi khủng hoảng niềm tin lan rộng, các doanh nghiệp và định chế phi ngân hàng sẽ chủ động kích hoạt quyền rút vốn hạn mức (*precautionary drawdowns*) để tích trữ thanh khoản mặt, đẩy tỷ lệ drawdown thực tế tăng vọt. Vì vậy, các hạn mức thanh khoản (backstop cho phát hành giấy tờ có giá) luôn bị áp tỷ lệ rút vốn nghiêm ngặt hơn hạn mức tín dụng tài trợ vốn lưu động.

## Góc nhìn theo domain

- **ALM Treasury**: *Diễn giải* — Hạn mức cam kết chưa giải ngân là cấu phần dòng ra tiềm tàng thường bị các mô hình dòng tiền hợp đồng bỏ sót. Khối ALM phải chủ động quản lý hạn mức theo hai chiều: (i) định giá chi phí thanh khoản cho hạn mức cam kết thông qua cơ chế FTP, và (ii) theo dõi chặt chẽ hạn mức thanh khoản cấp cho các định chế tài chính để tránh rủi ro thanh khoản lan truyền.
- **VN Regulator**: Theo [[tt50-2026|Thông tư 50/2026/TT-NHNN]], NHNN đã nội luật hóa chi tiết khung quản lý hạn mức cam kết tại Điều 3 và Phụ lục I Phần B Mục V [[src-tt50-2026-nhnn#^d3-5]] [[src-tt50-2026-nhnn#^pl1-b5]]. Điểm đặc thù là phân định pháp lý rõ ràng giữa cam kết hủy ngang có điều kiện và hủy ngang vô điều kiện, đồng thời ấn định cụ thể mức 0% cho cam kết hủy ngang vô điều kiện [[src-tt50-2026-nhnn#^pl1-b5-3]]. Đối với tỷ lệ [[nsfr]], hạn mức cam kết chưa sử dụng và nghĩa vụ giải ngân theo thỏa thuận chịu hệ số RSF là **5%** [[src-tt50-2026-nhnn#^pl2-b2]].

## Basel vs VN

| Nhóm đối tượng & cấu phần cam kết | Tham số Basel (LCR40 / NSF30) | Tham số VN (TT50/2026/TT-NHNN) | Điều khoản TT50 | Hiệu lực |
|---|---|---|---|---|
| **Cá nhân và DNNVV đủ điều kiện** | Tín dụng 5% / Thanh khoản 5% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 5% / Thanh khoản 5% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Doanh nghiệp phi tài chính** | Tín dụng 10% / Thanh khoản 30% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 10% / Thanh khoản 30% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Chính phủ, NHTW, PSE, KBNN, UBND, BHTG** | Tín dụng 10% / Thanh khoản 30% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 10% / Thanh khoản 30% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Tổ chức tín dụng, chi nhánh NHNNg** | Tín dụng 40% / Thanh khoản 40% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 40% / Thanh khoản 40% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Tổ chức tài chính khác (chứng khoán, bảo hiểm, quỹ)** | Tín dụng 40% / Thanh khoản 100% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 40% / Thanh khoản 100% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Đối tượng khác (SPE, conduit, SPV)** | Tín dụng 100% / Thanh khoản 100% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 100% / Thanh khoản 100% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Cam kết hủy ngang vô điều kiện** | Supervisor quyết định (thường 0%) [[src-bcbs-lcr#^lcr40-64]] | Hệ số rút tiền 0% [[src-tt50-2026-nhnn#^pl1-b5-31]] | Đ3.7, PL1.B.V.3.1.a(i) | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Cam kết hủy ngang có điều kiện** | Tính như cam kết (5%–100%) [[src-bcbs-lcr#^lcr40-59]] [[src-bcbs-lcr#^lcr40-64]] | Bắt buộc tính vào hạn mức cam kết (5%–100%) [[src-tt50-2026-nhnn#^d3-5]] [[src-tt50-2026-nhnn#^pl1-b5]] | Đ3.6, PL1.B.V.1 | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Nghĩa vụ giải ngân 30 ngày cho TCTD / NHNN** | Dòng ra 100% [[src-bcbs-lcr#^lcr40-65]] | Hệ số rút tiền 100% [[src-tt50-2026-nhnn#^pl1-b5-2]] | PL1.B.V.2.1 | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Giải ngân hợp đồng cho cá nhân & DN phi tài chính** | Phần vượt 50% dòng vào tính 100% [[src-bcbs-lcr#^lcr40-66]] | Phần vượt 50% dòng vào tính 100% [[src-tt50-2026-nhnn#^pl1-b5-2]] | PL1.B.V.2.2 | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Tài trợ thương mại (Trade finance)** | $\le 5\%$ do supervisor quyết định [[src-bcbs-lcr#^lcr40-71]] | Hệ số rút tiền 3% [[src-tt50-2026-nhnn#^pl1-b5-31]] | PL1.B.V.3.1.a(ii) | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Hạn mức cam kết trong NSFR (RSF)** | RSF 5% phần chưa rút [[src-bcbs-nsfr#^nsf30-34]] | RSF 5% phần chưa rút [[src-tt50-2026-nhnn#^pl2-b2]] | PL2.B Bảng 10 Mục C.1 | Áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |

*Điểm khác biệt trọng yếu giữa chuẩn Basel và Thông tư 50/2026*:
1. **Phân định pháp lý về quyền hủy ngang**:
   - Chuẩn mực Basel dùng thuật ngữ *unconditionally cancellable* nhưng không chi tiết hóa các điều kiện kích hoạt hủy ngang trong văn bản pháp quy [[src-bcbs-lcr#^lcr40-64]].
   - TT50 Điều 3.5–3.7 định nghĩa tường minh: (i) *Thỏa thuận hủy ngang có điều kiện* (khi khả năng trả nợ của khách hàng suy giảm hoặc vi phạm thỏa thuận) không được miễn trừ mà vẫn phải tính vào hạn mức cam kết và chịu drawdown rate theo Bảng 5 [[src-tt50-2026-nhnn#^d3-5]] [[src-tt50-2026-nhnn#^pl1-b5]]; (ii) Chỉ *Thỏa thuận hủy ngang vô điều kiện* (hủy ngang không cần bất kỳ điều kiện nào và việc hủy không gây rủi ro cho ngân hàng) mới được hưởng hệ số **0%** [[src-tt50-2026-nhnn#^d3-5]] [[src-tt50-2026-nhnn#^pl1-b5-3]].
2. **Quy chuẩn đối tượng DNNVV (SME)**:
   - Basel LCR40.22 khống chế quy mô SME trên cơ sở tập đoàn hợp nhất với ngưỡng doanh thu/dư nợ dưới 1 triệu EUR [[src-bcbs-lcr#^lcr40-22]].
   - TT50 xác định tiêu chí SME đủ điều kiện trên cơ sở tiền gửi bình quân trong tháng liền kề tại chính ngân hàng không quá 30 tỷ đồng [[src-tt50-2026-nhnn#^pl1-b3-22]].
3. **Ấn định tỷ lệ tài trợ thương mại**:
   - Basel để ngỏ tỷ lệ $\le 5\%$ cho cơ quan thẩm quyền quốc gia [[src-bcbs-lcr#^lcr40-71]].
   - TT50 ấn định cụ thể mức **3%** cho các công cụ tài trợ thương mại (nhờ thu chứng từ, nhờ thu hóa đơn nhập khẩu và xuất khẩu, bảo lãnh vận chuyển) [[src-tt50-2026-nhnn#^pl1-b5-31]].

## Đọc thêm

- [[lcr]] — Tỷ lệ khả năng chi trả thanh khoản.
- [[net-cash-outflows]] — Tổng dòng tiền ra ròng (mẫu số của LCR).
- [[cash-outflows]] — Tổng dòng tiền ra kỳ vọng và ma trận phân loại 5 trụ cột.
- [[run-off-rate]] — Tỷ lệ rút vốn giả định trong kịch bản căng thẳng thanh khoản.
- [[derivatives-and-contingent-outflows]] — Dòng tiền ra từ phái sinh và các nghĩa vụ nợ tiềm ẩn.
- [[nsfr]] — Tỷ lệ nguồn vốn ổn định ròng và hệ số RSF ngoại bảng.
- [[tt50-2026]] — Thông tư 50/2026/TT-NHNN của Ngân hàng Nhà nước Việt Nam.

