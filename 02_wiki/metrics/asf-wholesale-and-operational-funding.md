---
title: "Nguồn vốn Bán buôn và Tiền gửi Vận hành trong NSFR (Wholesale and Operational Funding)"
aliases: [Nguồn vốn bán buôn NSFR, Wholesale and Operational Funding NSFR, ASF 50% và 0%]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[available-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-13]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "+", cite: "[[src-bcbs-nsfr#^nsf30-13]]"}
tags: [nsfr, asf, wholesale-funding, operational-deposits, interbank]
updated: 2026-10-21
reviewed:
---

## Định nghĩa

Nguồn vốn bán buôn (*Wholesale Funding*) trong chuẩn mực [[nsfr]] được phân hóa rõ rệt thành hai nhóm đối xử: nguồn vốn bán buôn từ doanh nghiệp phi tài chính, chính phủ và tiền gửi vận hành được gán hệ số **ASF 50%** [[src-bcbs-nsfr#^nsf30-13]], trong khi nguồn vốn ngắn hạn dưới 6 tháng từ các định chế tài chính và Ngân hàng Trung ương bị áp hệ số **ASF 0%** [[src-bcbs-nsfr#^nsf30-14]]. Sự phân hóa này nhằm triệt tiêu mô hình kinh doanh dựa vào vốn vay liên ngân hàng ngắn hạn để mở rộng tài sản, ngăn ngừa nguy cơ đóng băng thanh khoản toàn hệ thống [[src-bcbs-nsfr#^nsf20-1]].

## Công thức & tham số

### 1. Phân tầng Nguồn vốn Doanh nghiệp và Tiền gửi Vận hành (ASF 50%)
Theo NSF30.13, các khoản nợ có kỳ hạn còn lại dưới 1 năm từ các đối tác phi tài chính và tiền gửi vận hành nhận hệ số ASF 50% bao gồm [[src-bcbs-nsfr#^nsf30-13]]:
1. **Khách hàng Doanh nghiệp Phi tài chính**: Toàn bộ các khoản tài trợ (có bảo đảm và không bảo đảm) có kỳ hạn còn lại dưới 1 năm do các doanh nghiệp phi tài chính cung cấp [[src-bcbs-nsfr#^nsf30-13]].
2. **Tiền gửi Vận hành ([[operational-deposits]])**: Tiền gửi phát sinh trực tiếp từ các dịch vụ thanh toán (clearing), lưu ký chứng khoán (custody) và quản lý tiền mặt (cash management) thỏa mãn tiêu chí LCR40.26–36 [[src-bcbs-lcr#^lcr40-26]] [[src-bcbs-nsfr#^nsf30-13]]. Khoản tiền gửi này có độ bám dính cao do khách hàng không thể rút ra mà không làm gián đoạn chuỗi vận hành kinh doanh.
3. **Chính phủ và Khu vực Công**: Nguồn vốn có kỳ hạn còn lại dưới 1 năm từ các chính phủ (Sovereign), cơ quan khu vực công (PSE), ngân hàng phát triển đa phương (MDB) và ngân hàng phát triển quốc gia [[src-bcbs-nsfr#^nsf30-13]].
4. **Nguồn vốn Định chế Tài chính kỳ hạn 6 đến 12 tháng**: Nguồn vốn vay mượn từ Ngân hàng Trung ương và các tổ chức tài chính khác có kỳ hạn còn lại từ 6 tháng đến dưới 1 năm [[src-bcbs-nsfr#^nsf30-13]].

### 2. Sự triệt tiêu Nguồn vốn Bán buôn Ngắn hạn Liên ngân hàng (ASF 0%)
Theo NSF30.14, các khoản nợ sau đây bị ấn định hệ số **ASF 0%** (hoàn toàn không được công nhận là nguồn vốn ổn định) [[src-bcbs-nsfr#^nsf30-14]]:
1. **Nguồn vốn từ Định chế Tài chính kỳ hạn $< 6$ tháng**: Toàn bộ các khoản vay mượn liên ngân hàng, tiền gửi liên ngân hàng, chứng chỉ tiền gửi bán cho tổ chức tài chính và nguồn vốn vay từ NHTW có kỳ hạn còn lại dưới 6 tháng [[src-bcbs-nsfr#^nsf30-14]].
   - Định chế tài chính bao gồm: ngân hàng, công ty chứng khoán, công ty bảo hiểm, quỹ đầu tư, fiduciaries và beneficiaries [[src-bcbs-nsfr#^nsf10-3]].
2. **Các khoản nợ không kỳ hạn xác định (Non-stated maturity liabilities)**: Bao gồm các vị thế bán khống (short positions) và các vị thế phơi bày mở [[src-bcbs-nsfr#^nsf30-14]].
3. **Nợ phái sinh ròng NSFR**: Chênh lệch nợ phái sinh lớn hơn tài sản phái sinh [[src-bcbs-nsfr#^nsf30-14]].
4. **Khoản phải trả ngày giao dịch (Trade date payables)**: Các khoản tiền phát sinh từ mua chứng khoán, ngoại tệ, hàng hóa chờ quyết toán trong chu kỳ chuẩn [[src-bcbs-nsfr#^nsf30-14]].

```
+-------------------------------------------------------------------------+
|      MA TRẬN HỆ SỐ ASF CHO NGUỒN VỐN BÁN BUÔN THEO ĐỐI TÁC VÀ KỲ HẠN    |
+-------------------------------------------------------------------------+
| Kỳ hạn còn lại     | Doanh nghiệp phi tài chính / Chính phủ | Định chế Tài chính / NHTW |
|--------------------|----------------------------------------|---------------------------|
| $\ge 1$ năm        | ASF 100% (NSF30.10)                    | ASF 100% (NSF30.10)       |
| 6 tháng đến < 1 năm| ASF 50% (NSF30.13)                     | ASF 50% (NSF30.13)        |
| Dưới 6 tháng       | ASF 50% (NSF30.13)                     | ASF 0% (NSF30.14)         |
+-------------------------------------------------------------------------+
```

## Diễn giải

### Cơ chế & drivers

#### 3. Ngoại lệ Tiền gửi Mạng lưới Ngân hàng Hợp tác xã (Footnote NSF30 Footnote 10)
- Đối với các hệ thống ngân hàng hợp tác xã hoặc ngân hàng nhân dân có cơ chế bảo vệ lẫn nhau, cơ quan giám sát quốc gia có quyền quyết định cho phép gán hệ số ASF lên tới **85%** (bằng với hệ số RSF của bên gửi tiền) cho các khoản tiền gửi nội bộ mạng lưới, thay vì bị áp mức 0% [[src-bcbs-nsfr#^nsf30-14]].

### Phụ thuộc regime
- **Khi Thanh khoản Liên ngân hàng Dư thừa vs Căng thẳng**:
  - Khi thanh khoản hệ thống dồi dào, lãi suất liên ngân hàng rất rẻ. Nếu không có chuẩn mực NSFR, các ngân hàng sẽ bị cám dỗ đi vay qua đêm và vay 1–3 tháng trên thị trường liên ngân hàng để tài trợ tín dụng bất động sản hoặc mua trái phiếu dài hạn nhằm tối đa hóa [[net-interest-margin|NIM]].
  - Quy định ASF 0% đối với nguồn vốn liên ngân hàng $< 6$ tháng triệt tiêu hoàn toàn động lực này, buộc các ngân hàng phải tìm kiếm nguồn vốn bền vững ngay cả trong giai đoạn tiền rẻ [[src-bcbs-nsfr#^nsf20-1]].

### Bằng chứng thực nghiệm
- **Cuộc sụp đổ của Northern Rock (2007)**: Ngân hàng này phụ thuộc tới 75% nguồn vốn vào thị trường bán buôn và chứng khoán hóa ngắn hạn. Khi thị trường liên ngân hàng toàn cầu đóng băng trong khủng hoảng tín dụng dưới chuẩn, nguồn vốn ngắn hạn bốc hơi hoàn toàn, dẫn đến cuộc rút tiền hàng loạt đầu tiên tại Anh sau hơn một thế kỷ. Đây chính là bằng chứng thực nghiệm trực tiếp thúc đẩy Basel áp đặt hệ số ASF 0% cho vốn liên ngân hàng ngắn hạn.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| DN phi tài chính dưới 1 năm | 50% [[src-bcbs-nsfr#^nsf30-13]] | 50% cho tiền gửi hoạt động, tiền gửi khác và nguồn khác [[src-tt50-2026-nhnn#^pl2-a2-11]] | TT50 PL2 Bảng 9 khoản 12 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Tiền gửi hoạt động | 50% [[src-bcbs-nsfr#^nsf30-13]] | 50% dưới 1 năm cho mọi nhóm đối tác (Chính phủ, NHNN, tổ chức tài chính, DN, tổ chức khác) [[src-tt50-2026-nhnn#^pl2-a2-6]] [[src-tt50-2026-nhnn#^pl2-a2-11]] | TT50 PL2 Bảng 9 khoản 7.1, 8.1, 11.1, 12.1, 13.1 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Chính phủ, khu vực công dưới 1 năm | 50% [[src-bcbs-nsfr#^nsf30-13]] | Chính phủ, KBNN, UBND cấp tỉnh, BHTG, BHXH, PSE nước ngoài, tổ chức tài chính quốc tế: 50%, kể cả không kỳ hạn [[src-tt50-2026-nhnn#^pl2-a2-6]] | TT50 PL2 Bảng 9 khoản 7 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| NHTW dưới 6 tháng | 0% [[src-bcbs-nsfr#^nsf30-14]] | NHNN, NHTW nước ngoài: tiền gửi không phải tiền gửi hoạt động và nguồn khác 0% [[src-tt50-2026-nhnn#^pl2-a2-6]] | TT50 PL2 Bảng 9 khoản 8.2–8.3 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Tổ chức tài chính dưới 6 tháng | 0% [[src-bcbs-nsfr#^nsf30-14]] | TCTD, chi nhánh NHNNg, tổ chức tài chính khác: 0% [[src-tt50-2026-nhnn#^pl2-a2-11]] | TT50 PL2 Bảng 9 khoản 11.2–11.3 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Tổ chức tài chính, NHTW 6 tháng – dưới 1 năm | 50% [[src-bcbs-nsfr#^nsf30-13]] | 50% [[src-tt50-2026-nhnn#^pl2-a2-6]] [[src-tt50-2026-nhnn#^pl2-a2-11]] | TT50 PL2 Bảng 9 khoản 8, 11 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Tổ chức khác (không phải DN, không phải tổ chức tài chính) | [cần nguồn] | Tiền gửi không phải tiền gửi hoạt động và nguồn khác: 0% dưới 6 tháng, 50% từ 6 tháng [[src-tt50-2026-nhnn#^pl2-a2-11]] | TT50 PL2 Bảng 9 khoản 13 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Vị thế bán, nợ không xác định kỳ hạn | 0% [[src-bcbs-nsfr#^nsf30-14]] | 0% [[src-tt50-2026-nhnn#^pl2-a2-11]] | TT50 PL2 Bảng 9 khoản 14.2 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Trade date payables | 0% [[src-bcbs-nsfr#^nsf30-14]] | 0% [[src-tt50-2026-nhnn#^pl2-a2-2]] | TT50 PL2 Bảng 9 khoản 4 | 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |

Chi tiết nguồn từ Chính phủ, KBNN, NHNN: [[asf-public-sector-and-central-bank-funding]]; nợ phái sinh, trade date payables, vị thế bán: [[asf-other-liabilities]].

*Diễn giải:* TT50 thêm nhóm "tổ chức khác" với hệ số chặt hơn DN phi tài chính: tiền gửi không hoạt động dưới 6 tháng nhận 0% thay vì 50%. Tiền gửi KBNN không phải tiền gửi hoạt động vẫn nhận 50% dưới 1 năm [[src-tt50-2026-nhnn#^pl2-a2-6]].

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM Treasury**:
  - Nguồn tiền gửi doanh nghiệp phi tài chính kỳ hạn dưới 1 năm mang lại hệ số ASF 50%: Mỗi 100 đồng tiền gửi doanh nghiệp giúp tài trợ được 50 đồng tài sản tín dụng, đóng vai trò là cầu nối thanh khoản quan trọng cho Treasury.
  - Bóc tách tiền gửi vận hành (Operational Deposits): Treasury cần phối hợp chặt chẽ với Khối Khách hàng Doanh nghiệp (Transaction Banking) để xây dựng hệ thống định lượng granular excess balance, bảo đảm phần số dư vận hành thực chất được ghi nhận đầy đủ vào hệ số ASF 50% [[src-bcbs-lcr#^lcr40-30]] [[src-bcbs-nsfr#^nsf30-13]].
- **Rủi ro Thị trường Vốn**:
  - Các chứng chỉ tiền gửi (CDs) do ngân hàng phát hành nếu được mua bởi các quỹ tương hỗ (MMFs) hoặc công ty bảo hiểm sẽ bị coi là nguồn vốn từ định chế tài chính; khi kỳ hạn còn lại trôi về dưới 6 tháng, giá trị ASF của lô phát hành sẽ rớt thẳng về 0% [[src-bcbs-nsfr#^nsf30-14]].

## Câu hỏi mở
- Tại Việt Nam, thị trường liên ngân hàng (Thị trường 2) vận hành rất sôi động với kỳ hạn phổ biến từ qua đêm đến 3 tháng. Khi TT50 áp dụng đầy đủ NSFR, các ngân hàng phụ thuộc vào nguồn vốn Thị trường 2 sẽ phải điều chỉnh chiến lược huy động vốn như thế nào?
- Tiền gửi Kho bạc Nhà nước tại các NHTM (thường có kỳ hạn 1–3 tháng) được phân loại là nguồn vốn chính phủ (ASF 50%) hay áp dụng theo quy chế đặc thù nào khác?
