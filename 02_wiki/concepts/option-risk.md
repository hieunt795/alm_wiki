---
title: "Option Risk (Rủi ro quyền chọn trong sổ ngân hàng)"
aliases: [Option Risk, Rủi ro quyền chọn, Automatic Options, Embedded Options]
type: concept
domains: [alm, product, basel, vn-reg]
status: active
maturity: draft
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]", "[[src-tata-bank-alm]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
tags: [irrbb, option-risk, automatic-options, embedded-options, caps-floors, kao]
updated: 2026-10-22
reviewed:
---

## Định nghĩa
Rủi ro quyền chọn (Option risk) phát sinh từ các vị thế phái sinh quyền chọn độc lập hoặc từ các điều khoản quyền chọn được nhúng sẵn (embedded options) bên trong các tài sản, nợ phải trả và cam kết ngoại bảng của ngân hàng, nơi mà ngân hàng hoặc khách hàng có quyền chủ động thay đổi quy mô và thời điểm của các dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

Theo Chuẩn mực [[bcbs-irrbb]] (d368), rủi ro quyền chọn được phân định thành 2 nhóm bản chất riêng biệt: **Quyền chọn tự động (Automatic Options)** và **Quyền chọn hành vi (Behavioural Options)** [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

## 1. Quyền chọn tự động (Automatic Options)

### Khái niệm và Đặc điểm
- Là các quyền chọn mà người nắm giữ sẽ **chắc chắn thực hiện quyền** nếu việc thực hiện mang lại lợi ích tài chính thuần tuý (hành vi hoàn toàn duy lý theo quy luật thị trường tài chính) [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- Bao gồm:
  - Các hợp đồng quyền chọn chuẩn hoá trên sàn hoặc OTC ([[interest-rate-cap-floor|caps, floors]], [[swaption|swaptions]]).
  - Các quyền chọn nhúng trong sản phẩm bán buôn: trần lãi suất ([[interest-rate-cap-floor|caps]]) hoặc sàn lãi suất ([[interest-rate-cap-floor|floors]]) gắn vào các khoản vay hoặc chứng khoán nợ lãi suất thả nổi; trái phiếu có quyền mua lại (callable bonds) hoặc quyền bán lại (puttable bonds) [[src-bcbs-irrbb-2016#^irrbb-u05-3]] [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
  - Bất kỳ quyền chọn hành vi nào của khách hàng bán buôn (wholesale) đều phải quy về xử lý như quyền chọn tự động [[src-bcbs-irrbb-2016#^irrbb-u05-7]].

### Phương pháp đo lường chuẩn hoá ($\text{KAO}_{i,c}$)
- Trong Khuôn khổ chuẩn hoá của d368, các quyền chọn tự động nhúng được bóc tách khỏi dòng tiền cơ sở và chuyển sang Giai đoạn 4 để tính giá trị gia tăng $\text{KAO}_{i,c}$ [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-bcbs-irrbb-2016#^irrbb-u05-3]].
- **Công thức tính add-on quyền chọn**:
  $$\text{KAO}_{i,c} = \sum_{o=1}^{n_c} \Delta\text{FVAO}_{i,c}^o - \sum_{q=1}^{m_c} \Delta\text{FVAO}_{i,c}^q$$
  Trong đó:
  - Mỗi quyền chọn bán $o$ được định giá lại toàn bộ dưới kịch bản sốc lãi suất $i$ kết hợp với mức **tăng độ biến động ngầm định tương đối 25%** so với đường cong ban đầu [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
  - Trừ đi biến động giá trị của các quyền chọn mua $q$, cũng định giá lại với mức tăng 25% implicit volatility [[src-bcbs-irrbb-2016#^irrbb-u05-27]].
- Swaptions của sản phẩm phi bán lẻ có thể được xử lý như quyền chọn tự động khi bên nắm quyền là đối tác thị trường tài chính chuyên nghiệp [[src-bcbs-irrbb-2016#^irrbb-u05-26]].
- Ngân hàng chọn đưa vào toàn bộ quyền chọn mua hoặc chỉ quyền chọn mua phòng ngừa quyền chọn bán; với cách thứ hai, thay đổi giá trị thị trường của quyền chọn mua còn lại đã phản ánh trong vốn pháp định phải cộng vào $\text{KAO}_{i,c}$ [[src-bcbs-irrbb-2016#^irrbb-u05-28]]. Chi tiết các bước: [[irrbb-standardised-framework]] Giai đoạn 4.

### Rủi ro Trần và Sàn Lãi suất (Cap & Floor Risk theo Moorad Choudhry)
- **Rủi ro trần (Cap risk)**: Phát sinh từ các hợp đồng cho vay kèm lãi suất trần tối đa [[src-choudhry-principles-banking#^choudhry-irrbb-7]]. Khi mặt bằng lãi suất tăng, các khoản nợ tài trợ nhạy cảm lãi suất tái định giá tăng lên, trong khi lãi suất thu được từ tài sản bị chặn trần, gây thu hẹp biên lãi thuần [[net-interest-margin|NIM]] và làm suy giảm NII [[src-choudhry-principles-banking#^choudhry-irrbb-7]].
- **Rủi ro sàn (Floor risk)**: Phát sinh khi lãi suất thị trường giảm sâu về mức thấp (gần 0%); các tài sản nhạy cảm lãi suất tái định giá giảm theo thị trường, nhưng các khoản tiền gửi của khách hàng không thể tái định giá giảm tương ứng do sàn ngầm định 0%, khiến biên lãi ròng của ngân hàng bị ép chặt [[src-choudhry-principles-banking#^choudhry-irrbb-7]].

### Kịch bản stress cho option risk (d368 Nguyên tắc 4)
- Ngân hàng có option risk đáng kể nên có kịch bản phản ánh việc thực hiện quyền chọn. Ví dụ, ngân hàng đã bán cap hoặc floor nên đánh giá vị thế rủi ro thay đổi thế nào khi cap/floor vào trạng thái in-the-money [[src-bcbs-irrbb-2016#^irrbb-p04-15]].
- Giá trị thị trường của quyền chọn biến động theo volatility lãi suất, nên ngân hàng nên xây dựng giả định lãi suất để đo IRRBB trước thay đổi volatility [[src-bcbs-irrbb-2016#^irrbb-p04-15]]. Xem [[stress-testing]].

### Ghi chú theo nguồn T4
- Lubinska đánh giá quyền chọn tự động theo ΔEVE; quyền rút tiền là quyền chọn hành vi; nguồn tách thêm "yield risk" (dịch chuyển không song song ngoài dự kiến) [[src-lubinska-alm-optimisation#^lubinska-u02-32]]. Case study của Lubinska: giá trị quyền chọn tự động bù lỗ EVE khi lãi suất giảm [[src-lubinska-alm-optimisation#^lubinska-u02-41]].
- Sàn 0% trên tiền gửi bán lẻ là quyền chọn nhúng, at hoặc in the money khi lãi suất thấp hay âm [[src-tata-bank-alm#^tata-neg-2]]. Coupon floor max(rI + x; 0%) và indicator floor max(rI; 0%) + x tác động ngược chiều ở tài sản và nợ [[src-tata-bank-alm#^tata-neg-3]]. Xem [[negative-interest-rates]].

## 2. Quyền chọn hành vi (Behavioural Options)

Phân tích chuyên sâu về mô hình hoá toán học, hệ số Table 3, Table 4 và tính chất [[convexity|lồi âm]] (negative convexity) được trình bày tại node chuyên biệt: [[behavioural-options]].

### Khái niệm và Đặc tính phi đối xứng
- Là các quyền chọn nhúng linh hoạt trong các hợp đồng tài chính bán lẻ, nơi quyết định thực hiện quyền của khách hàng bị chi phối bởi nhiều yếu tố phi tài chính (tâm lý, thu nhập, nhân khẩu học, bất động sản, thói quen tiêu dùng) thay vì chỉ hành vi tài chính duy lý [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- **Rủi ro lồi (Convexity Risk / Extension & Contraction Risk)**: Khách hàng thường thực hiện quyền bất lợi nhất cho ngân hàng:
  - Khi lãi suất giảm: Khách hàng ồ ạt trả nợ vay cố định trước hạn để vay mới lãi suất thấp (contraction risk), khiến ngân hàng nhận lại tiền và buộc phải tái đầu tư với lợi suất thấp [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
  - Khi lãi suất tăng: Khách hàng duy trì các khoản vay cố định lãi suất thấp (extension risk), trong khi người gửi tiền có kỳ hạn ồ ạt rút vốn trước hạn để gửi sang nơi có lãi suất cao hơn [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

### Ba sản phẩm chịu rủi ro hành vi trọng yếu

#### 1. Các khoản cho vay lãi suất cố định chịu rủi ro trả nợ trước hạn (Prepayment Risk)
- Basel chuẩn hoá bằng tỷ lệ trả nợ trước hạn có điều kiện (Conditional Prepayment Rate - CPR) [[src-bcbs-irrbb-2016#^irrbb-u05-5]]:
  $$\text{CPR}_{i,c}^p = \min(1, \gamma_i \cdot \text{CPR}_{0,c}^p)$$
- **Hệ số nhân kịch bản $\gamma_i$**:
  - Khi lãi suất giảm (Parallel down, Flattener, Short rate down): $\gamma_i = 1.2$ (tốc độ trả trước tăng 20%) [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
  - Khi lãi suất tăng (Parallel up, Steepener, Short rate up): $\gamma_i = 0.8$ (tốc độ trả trước giảm 20%) [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
- Xem chi tiết tại [[behavioural-options]].

#### 2. Tiền gửi có kỳ hạn chịu rủi ro rút trước hạn (Early Redemption Risk)
- Basel chuẩn hoá qua tỷ lệ rút tiền gửi sớm (Term Deposit Redemption Ratio - TDRR) [[src-bcbs-irrbb-2016#^irrbb-u05-6]]:
  $$\text{TDRR}_{i,c}^p = \min(1, u_i \cdot \text{TDRR}_{0,c}^p)$$
- **Hệ số co giãn kịch bản $u_i$**:
  - Khi lãi suất tăng (Parallel up, Flattener, Short rate up): $u_i = 1.2$ (khách hàng rút tiền sớm tăng 20% tìm lãi suất cao, phần rút chuyển về dải qua đêm) [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
  - Khi lãi suất giảm (Parallel down, Steepener, Short rate down): $u_i = 0.8$ (khách hàng giữ lại tiền gửi lãi suất cao).
- Xem chi tiết tại [[behavioural-options]].

#### 3. Tiền gửi không kỳ hạn (Non-Maturity Deposits - NMDs)
- NMDs không có ngày đáo hạn hợp đồng, người gửi có thể rút bất kỳ lúc nào nhưng số dư thực tế duy trì rất ổn định và chi phí vốn rất thấp [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
- Basel d368 quy định phân tách NMDs thành phần ổn định và phần lõi (Core deposits) với các trần khống chế nghiêm ngặt [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:
  - **Bán lẻ giao dịch (Retail transactional)**: Trần tiền gửi lõi 90%, trần kỳ hạn bình quân 5 năm.
  - **Bán lẻ phi giao dịch (Retail non-transactional)**: Trần tiền gửi lõi 70%, trần kỳ hạn bình quân 4,5 năm.
  - **Bán buôn (Wholesale)**: Trần tiền gửi lõi 50%, trần kỳ hạn bình quân 4 năm.
  - **Tiền gửi phi lõi (Non-core deposits)**: Bắt buộc phân bổ 100% vào dải kỳ hạn qua đêm (overnight) [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
- Xem chi tiết phương pháp luận Replicating Portfolio và trần Table 2 tại node chuyên biệt: [[non-maturity-deposits]].

#### 4. Rủi ro đường ống cam kết giải ngân (Pipeline Risk theo Moorad Choudhry)
- Xuất hiện trên các sản phẩm cho vay và tiền gửi lãi suất cố định khi khách hàng có quyền chọn (chứ không phải nghĩa vụ hợp đồng) giải ngân hoặc gửi tiền ở mức lãi suất đã cam kết trong thời hạn chào thầu [[src-choudhry-principles-banking#^choudhry-irrbb-6]].
- Khi lãi suất thị trường dịch chuyển trong thời hạn chào thầu, ngân hàng đối mặt với rủi ro tổn thất thu nhập hoặc rủi ro thặng dư vị thế phòng hộ [[src-choudhry-principles-banking#^choudhry-irrbb-6]]:
  - Khi lãi suất tăng: Khách hàng tìm thấy lãi suất tiền gửi nơi khác cao hơn nên không gửi tiền như dự kiến, buộc ngân hàng phải tất toán các hợp đồng hoán đổi lãi suất phòng hộ trước đó chịu lỗ [[src-choudhry-principles-banking#^choudhry-irrbb-6]].
  - Khi lãi suất giảm: Lãi suất cam kết trở nên hấp dẫn vượt trội, lượng khách hàng đăng ký vay/gửi vượt dự kiến, buộc ngân hàng phải bổ sung phòng hộ ở biên lợi nhuận thấp hơn hoặc âm [[src-choudhry-principles-banking#^choudhry-irrbb-6]].

#### 5. Quản trị rủi ro hành vi bằng Phòng hộ Động (Dynamic Hedging)
- Moorad Choudhry nhấn mạnh việc mua các hợp đồng quyền chọn hoán đổi (swaptions) để phòng ngừa rủi ro trả nợ trước hạn hay rút tiền sớm thường rất tốn kém (phí premium cao bào mòn biên sản phẩm) và thị trường swaptions không đủ thanh khoản cho quy mô danh mục ngân hàng [[src-choudhry-principles-banking#^choudhry-irrbb-8]].
- Thay vào đó, ngân hàng áp dụng phương pháp **phòng hộ động (dynamic hedging)**: xây dựng mô hình dự báo hành vi run-off của từng tập khách hàng (cohort) dựa trên dữ liệu lịch sử dưới nhiều kịch bản lãi suất; ban đầu thiết lập vị thế phòng hộ hoán đổi theo kỳ vọng run-off, và định kỳ hàng tháng tái đánh giá hồ sơ run-off thực tế để thực hiện giao dịch hoán đổi bù trừ (amortising pay fixed swap hoặc balloon receive fixed swap) [[src-choudhry-principles-banking#^choudhry-irrbb-8]].

### Định nghĩa của Choudhry (T4)
- Option risk là quyền của khách hàng chấm dứt hợp đồng trước hạn (CD, tài khoản séc, tiền gửi không kỳ hạn), ảnh hưởng NII khi quyền được thực hiện [[src-choudhry-principles-banking#^choudhry-irr-6]].

## Tác động lên EVE, NII và Thanh khoản

1. **Lên [[economic-value-of-equity|$\Delta\text{EVE}$]]**: Quyền chọn nhúng tạo ra tính chất lồi âm (negative convexity). Khi lãi suất tăng mạnh, add-on quyền chọn tự động $\text{KAO}$ và việc rút tiền gửi sớm $\text{TDRR}$ làm bốc hơi giá trị kinh tế nhanh hơn nhiều so với dự báo tuyến tính từ phân tích khoảng cách kỳ hạn đơn giản [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
2. **Lên [[net-interest-income-sensitivity|$\Delta\text{NII}$]]**: Sự gia tăng trả nợ trước hạn trong môi trường lãi suất thấp đè bẹp tỷ lệ thu nhập lãi thuần, trong khi hiện tượng rút tiền gửi chuyển sang kỳ hạn lãi suất cao trong môi trường lãi suất tăng đẩy chi phí huy động vốn vọt lên.
3. **Lên Thanh khoản [[lcr]] & [[nsfr]]**: Rút tiền gửi có kỳ hạn sớm biến một nguồn vốn có kỳ hạn ổn định (được hưởng tỷ lệ rút vốn thấp trong LCR và ASF 100% trong NSFR) thành dòng tiền rút ngay lập tức, đe dọa đồng thời cả vị thế thanh khoản 30 ngày và cơ cấu tài trợ 1 năm.
- Xem chi tiết tại [[gap-risk]], [[basis-risk]], [[csrbb]], [[behavioural-options]], [[non-maturity-deposits]].

## Basel vs VN
| Khía cạnh | Basel d368 | VN TT83/2025 | Nguồn |
|---|---|---|---|
| Định nghĩa | Quyền chọn tự động và quyền chọn hành vi | Quyền chọn tự động (lãi suất thay đổi dẫn tới chắc chắn thực hiện quyền chọn theo hợp đồng) và quyền lựa chọn hành vi (lãi suất thay đổi có thể làm thay đổi hành vi khách hàng) | [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-tt83-2025-nhnn#^d3-22]] |

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
