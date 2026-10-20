---
title: Retail deposit stability (stable vs less stable)
aliases: [Stable deposits, Less stable deposits, Tiền gửi ổn định, Tiền gửi kém ổn định]
type: metric
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-5]]"}
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[run-off-rate]]", cite: "[[src-bcbs-lcr#^lcr40-6]]"}
tags: [deposit, deposit-insurance, liquidity]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

Basel chia tiền gửi bán lẻ (của thể nhân) thành hai nhóm, mỗi nhóm có [[run-off-rate]] tối thiểu riêng: "stable" và "less stable" [[src-bcbs-lcr#^lcr40-5]] [[src-bcbs-lcr#^lcr40-6]]. Vốn từ SME (< 1 triệu EUR mỗi khách hàng) được xử lý giống hệt [[src-bcbs-lcr#^lcr40-22]] [[src-bcbs-lcr#^lcr40-23]].

## Công thức & tham số

### Cơ chế & drivers
**Stable** (run-off thường 5%) phải thoả **cả hai** điều kiện [[src-bcbs-lcr#^lcr40-7]]:
1. Được bảo hiểm toàn bộ bởi một *effective deposit insurance scheme*, tức đáp ứng 4 tiêu chí: chi trả nhanh, phạm vi rõ, công chúng biết rộng rãi, tổ chức bảo hiểm có quyền pháp lý và độc lập [[src-bcbs-lcr#^lcr40-8]].
2. Người gửi có quan hệ khác với ngân hàng, hoặc tiền nằm trong tài khoản giao dịch (ví dụ tài khoản nhận lương).

Chỉ có bảo hiểm tiền gửi thì chưa đủ [[src-bcbs-lcr#^lcr40-10]]. Mức 3% chỉ được áp khi quỹ bảo hiểm có prefunding, có nguồn vốn dự phòng và chi trả nhanh [[src-bcbs-lcr#^lcr40-11]].

**Nguyên tắc hạn mức bảo hiểm tiền gửi (*Deposit Insurance Limit*)**:
Theo footnote 45-0 của LCR40.7, "fully insured" áp dụng cho phần số dư nằm trong hạn mức bảo hiểm. Nếu khách hàng có khoản tiền gửi 150 triệu VND trong khi hạn mức bảo hiểm tối đa là 100 triệu VND, thì 100 triệu VND được coi là "fully insured" (xếp vào stable 5%), còn 50 triệu VND vượt hạn mức bắt buộc xếp vào less stable (≥ 10%). Nếu cơ chế bảo hiểm chỉ chi trả theo tỷ lệ phần trăm (ví dụ 90% ngay từ đồng đầu tiên) thì toàn bộ khoản tiền gửi không đáp ứng tiêu chí "fully insured".

**Less stable** (≥ 10%). Supervisor lập thêm các bucket với run-off cao hơn cho: tiền gửi không được bảo hiểm toàn bộ, tiền gửi giá trị lớn, khách hàng HNW, internet deposits, tiền gửi ngoại tệ [[src-bcbs-lcr#^lcr40-13]]. Ngân hàng không xác định được tiền gửi nào stable thì xếp toàn bộ vào less stable [[src-bcbs-lcr#^lcr40-14]]. Run-off của tiền gửi ngoại tệ do supervisor quyết định [[src-bcbs-lcr#^lcr40-15]].

**Tiền gửi có kỳ hạn**: phần có kỳ hạn còn lại > 30 ngày được loại khỏi dòng ra nếu người gửi không có quyền rút trong 30 ngày, hoặc rút trước hạn bị phạt lớn hơn rõ rệt so với mất lãi [[src-bcbs-lcr#^lcr40-16]]. Nếu ngân hàng cho rút mà không phạt thì **toàn bộ nhóm** bị coi là không kỳ hạn [[src-bcbs-lcr#^lcr40-17]]. Supervisor có thể quy định các trường hợp bất khả kháng hoặc hoàn cảnh đặc biệt (*hardship circumstances*) cho phép người gửi rút trước hạn mà không kích hoạt quy tắc lây lan đối với toàn bộ danh mục [[src-bcbs-lcr#^lcr40-17]].

**Tiền gửi cầm cố bảo đảm khoản vay (*Pledged Deposits*)**:
Theo FAQ1 của LCR40.5, tiền gửi bán lẻ được cầm cố theo hợp đồng để bảo đảm cho một khoản vay do ngân hàng cấp được loại trừ khỏi dòng tiền ra nếu: (1) khoản vay không đáo hạn trong vòng 30 ngày; (2) có điều khoản pháp lý ràng buộc cấm rút tiền gửi trước khi khoản vay được thanh toán hết; và (3) số tiền gửi loại trừ không vượt quá dư nợ của khoản vay. Nếu cầm cố cho hạn mức chưa giải ngân, ngân hàng phải áp dụng tỷ lệ dòng ra cao hơn giữa hạn mức và tiền gửi.

## Diễn giải

### Phụ thuộc regime
*Diễn giải:* phân loại stable/less stable phản ánh hành vi trong stress. Tiền gửi nhạy lãi suất (internet deposits, tiền gửi tìm lợi suất) có thể rút nhanh hơn khi lãi suất thị trường tăng hoặc khi niềm tin giảm. Cần nguồn thực nghiệm để định lượng.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **Basel**: khung bucket và mức sàn [[src-bcbs-lcr#^lcr40-6]].
- **ALM**: *Diễn giải* — tỷ trọng stable deposits là một driver chính của chi phí thanh khoản. Chương trình tài khoản lương và quan hệ đa sản phẩm giúp chuyển tiền gửi từ less stable sang stable.
- **VN**: theo [[tt50-2026|TT50/2026]], tiền gửi bán lẻ ổn định là tiền gửi được Bảo hiểm tiền gửi Việt Nam bảo hiểm hoàn toàn và khách hàng có khoản vay trung dài hạn hoặc có tài khoản thanh toán phát sinh giao dịch trong 6 tháng gần nhất; hệ số rút tiền 5%. Phần vượt giới hạn bảo hiểm và mọi tiền gửi ngoại tệ là kém ổn định, hệ số 10% [[src-tt50-2026-nhnn#^pl1-b2]]. ASF: ổn định 95%, kém ổn định 90% [[src-tt50-2026-nhnn#^pl2-a2]]. *Diễn giải:* Basel cho run-off 3% với tiền gửi ổn định nếu đáp ứng điều kiện BHTG; TT50 không có mức 3%.

## Câu hỏi mở
- Hạn mức bảo hiểm tiền gửi tại VN và cơ chế quỹ (có prefunding không) có đáp ứng tiêu chí LCR40.8 và LCR40.11 không?
- Chính sách rút trước hạn không phạt (phổ biến tại VN) có khiến toàn bộ tiền gửi có kỳ hạn bị coi là không kỳ hạn theo logic LCR40.17 không?
