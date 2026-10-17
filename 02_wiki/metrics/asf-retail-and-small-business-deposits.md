---
title: "Tiền gửi Bán lẻ và Doanh nghiệp nhỏ trong NSFR (Retail and Small Business Deposits)"
aliases: [Tiền gửi bán lẻ NSFR, Retail and SME Deposits NSFR, ASF Tiền gửi bán lẻ]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-bcbs-lcr]]"]
relations:
  - {type: part-of, to: "[[available-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-11]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "+", cite: "[[src-bcbs-nsfr#^nsf30-11]]"}
tags: [nsfr, asf, retail-deposits, sme, deposit-stability]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

Tiền gửi của khách hàng cá nhân (bán lẻ) và khách hàng doanh nghiệp nhỏ (SME) là nguồn vốn có tính bám dính hành vi (*behavioural stickiness*) cao nhất trong hệ thống huy động vốn của ngân hàng, được gán hệ số **ASF 90% đến 95%** ngay cả khi là tiền gửi không kỳ hạn hoặc có kỳ hạn dưới 1 năm [[src-bcbs-nsfr#^nsf30-2]] [[src-bcbs-nsfr#^nsf30-11]] [[src-bcbs-nsfr#^nsf30-12]]. Chuẩn mực NSFR ghi nhận rằng người gửi tiền bán lẻ ít nhạy cảm với biến động thị trường và được bảo vệ bởi bảo hiểm tiền gửi, do đó nguồn vốn này mang lại độ ổn định thực chất vượt xa kỳ hạn hợp đồng danh nghĩa [[src-bcbs-nsfr#^nsf30-2]].

## Công thức & tham số

### 1. Phân loại 3 tầng Tiền gửi Bán lẻ và SME trong NSFR

| Tầng Hệ số ASF | Loại hình tiền gửi và Tiêu chí điều kiện | Căn cứ pháp lý |
|:---:|---|---|
| **100%** | **Tiền gửi có kỳ hạn $\ge 1$ năm có phạt nặng**: Tiền gửi có kỳ hạn còn lại từ 1 năm trở lên mà khách hàng không có quyền rút trước hạn hoặc rút trước hạn sẽ bị phạt một khoản đáng kể lớn hơn nhiều so với mất tiền lãi [[src-bcbs-nsfr#^nsf30-10]]. | NSF30.10 |
| **95%** | **Tiền gửi Bán lẻ và SME Stable (Ổn định)**:<br>- Tiền gửi không kỳ hạn (*demand deposits*) và tiền gửi có kỳ hạn $< 1$ năm thuộc nhóm "stable" theo định nghĩa [[retail-deposit-stability]] (LCR40.7–12) [[src-bcbs-nsfr#^nsf30-11]].<br>- Tiền gửi có kỳ hạn $> 1$ năm nhưng cho phép rút trước hạn không bị phạt nặng [[src-bcbs-nsfr#^nsf30-11]].<br>- *Điều kiện tiên quyết*: Được bảo hiểm toàn bộ bởi một quỹ bảo hiểm tiền gửi hiệu quả (*effective deposit insurance scheme*) và khách hàng có quan hệ giao dịch lâu năm hoặc tài khoản lương [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-nsfr#^nsf30-11]]. | NSF30.11 |
| **90%** | **Tiền gửi Bán lẻ và SME Less Stable (Kém ổn định hơn)**:<br>- Tiền gửi không kỳ hạn và tiền gửi có kỳ hạn $< 1$ năm không thỏa mãn đầy đủ tiêu chí "stable" (ví dụ: số dư vượt hạn mức bảo hiểm tiền gửi, tài khoản mở trực tuyến không gắn kết dịch vụ, khách hàng giàu có có độ nhạy lãi suất cao) [[src-bcbs-nsfr#^nsf30-12]].<br>- Tiền gửi có kỳ hạn $> 1$ năm cho phép rút trước hạn không bị phạt nặng [[src-bcbs-nsfr#^nsf30-12]]. | NSF30.12 |

## Diễn giải

### Cơ chế & drivers

#### 2. Sự khác biệt giữa Bản chất Hợp đồng và Giả định Hành vi
- **Kỳ hạn danh nghĩa vs Kỳ hạn hành vi**: Trên góc độ hợp đồng thuần túy, tiền gửi thanh toán (CASA) có kỳ hạn bằng 0 (khách hàng có thể rút bất kỳ lúc nào). Tuy nhiên, trong mô hình NSFR, Basel gán cho khoản tiền gửi này hệ số ASF $90\%\text{–}95\%$ [[src-bcbs-nsfr#^nsf30-11]] [[src-bcbs-nsfr#^nsf30-12]].
- **Nguyên nhân của hệ số 90%–95%**: Basel nhận định rằng trong khoảng thời gian 1 năm ở điều kiện bình thường và căng thẳng vừa phải, khối khách hàng cá nhân không rút ồ ạt tiền gửi sinh hoạt, mà luôn duy trì một số dư lõi (*core deposit balance*) ổn định phục vụ nhu cầu chi tiêu và thanh toán hàng ngày [[src-bcbs-nsfr#^nsf30-2]].

#### 3. Quy tắc gom cụm Doanh nghiệp nhỏ (SME Aggregation Rule)
- Khách hàng doanh nghiệp nhỏ chỉ được quản lý và đối xử tương đương tiền gửi bán lẻ (hưởng ASF 90%–95%) nếu tổng số dư tiền gửi của khách hàng (hoặc nhóm khách hàng liên quan) không vượt quá **1 triệu EUR** (hoặc giá trị tương đương bằng nội tệ) và ngân hàng quản lý khách hàng này trên cơ sở danh mục bán lẻ đồng nhất [[src-bcbs-lcr#^lcr40-23]] [[src-bcbs-nsfr#^nsf30-11]].
- Nếu số dư vượt quá 1 triệu EUR, khoản tiền gửi lập tức bị phân loại sang nhóm bán buôn doanh nghiệp phi tài chính và hệ số ASF giảm mạnh xuống **50%** [[src-bcbs-nsfr#^nsf30-13]].

### Phụ thuộc regime
- **Môi trường Số hóa Ngân hàng (Digital Banking Regime)**:
  - Sự phổ biến của ngân hàng số và ứng dụng di động cho phép chuyển tiền tức thời 24/7 làm gia tăng độ nhạy rút tiền của người gửi tiền cá nhân.
  - Các khoản tiền gửi trực tuyến quy mô lớn có thể chuyển dịch nhanh chóng khi có biến động lãi suất hoặc tin đồn tiêu cực trên mạng xã hội, tạo áp lực nghi ngờ đối với mức hệ số ASF 90% cố định của Basel.

### Bằng chứng thực nghiệm
- Dữ liệu lịch sử qua nhiều chu kỳ kinh tế của hệ thống ngân hàng toàn cầu cho thấy, tốc độ suy giảm số dư tiền gửi bán lẻ trong 1 năm bình thường chỉ dao động từ 3% đến 8%, hoàn toàn phù hợp với giả định hệ số ASF 90%–95% của chuẩn mực Basel.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM Treasury**:
  - Tiền gửi bán lẻ là "mỏ vàng" thanh khoản: Mỗi 100 đồng tiền gửi bán lẻ stable mang lại 95 đồng nguồn vốn ổn định, trong khi chi phí lãi suất thường thấp hơn nhiều so với việc phát hành trái phiếu dài hạn (ASF 100%).
  - Khối Treasury luôn xây dựng cơ chế trả thưởng FTP nội bộ (Stable Funding Credit) cho mạng lưới chi nhánh để khuyến khích phát triển cơ sở khách hàng cá nhân và tiền gửi CASA.
- **Bảo hiểm Tiền gửi (Deposit Insurance)**:
  - Sự tồn tại của hệ thống bảo hiểm tiền gửi công khai, minh bạch và có năng lực chi trả nhanh là điều kiện pháp lý bắt buộc để ngân hàng được hưởng hệ số ASF ưu đãi 95% [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-nsfr#^nsf30-11]].

## Câu hỏi mở
- Tại Việt Nam, hạn mức bảo hiểm tiền gửi hiện hành là 125 triệu VND/người gửi tiền. Liệu phần tiền gửi của khách hàng cá nhân vượt quá 125 triệu VND có bị cơ quan thanh tra giám sát yêu cầu chuyển từ nhóm stable (ASF 95%) sang less stable (ASF 90%) hoặc áp dụng tỷ lệ thấp hơn?
