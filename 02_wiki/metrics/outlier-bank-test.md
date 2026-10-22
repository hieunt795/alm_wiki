---
title: "Outlier Bank Test (Kiểm tra ngân hàng ngoại lai IRRBB)"
aliases: [Outlier Bank Test, Ngân hàng ngoại lai, Supervisory Outlier Test, Phép thử ngoại lai, Ngưỡng 15% Tier 1]
type: metric
domains: [basel, alm]
status: active
maturity: draft
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
  - {type: measures, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
  - {type: limits, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
tags: [irrbb, outlier-test, supervisory-review, tier-1-capital, pillar-2, eve]
updated: 2026-10-20
reviewed:
---

## Định nghĩa

Kiểm tra ngân hàng ngoại lai (Outlier Bank Test, hay Phép thử ngoại lai giám sát) là phép thử định lượng mà cơ quan giám sát nên (should) áp dụng tối thiểu một lần theo Nguyên tắc 12; tiêu chí xác định ngân hàng ngoại lai phải (must) được công bố của Chuẩn mực [[bcbs-irrbb]] (d368), nhằm nhận diện các tổ chức tín dụng có mức độ phơi lượng rủi ro lãi suất trên sổ ngân hàng quá mức hoặc không tương xứng với quy mô vốn và năng lực quản trị rủi ro [[src-bcbs-irrbb-2016#^irrbb-u01-6]] [[src-bcbs-irrbb-2016#^irrbb-p12-1]].

Ngân hàng bị xác định là ngân hàng ngoại lai (outlier bank) phải được coi là có khả năng mang IRRBB quá mức và phải được rà soát [[src-bcbs-irrbb-2016#^irrbb-p12-4]]. Khi rà soát cho thấy [[irrbb-management|quản trị IRRBB]] không đầy đủ hoặc rủi ro quá mức so với vốn, thu nhập hay hồ sơ rủi ro chung, có giả định mạnh (strong presumption) về hệ quả giám sát và/hoặc vốn quy định [[src-bcbs-irrbb-2016#^irrbb-u01-6]] [[src-bcbs-irrbb-2016#^irrbb-p12-1]].

## Phép thử tối thiểu theo par 88

Ngân hàng bị coi là ngân hàng ngoại lai nếu thỏa mãn điều kiện:

$$
\frac{\max_{i \in \{1..6\}} \Delta\text{EVE}_i}{\text{Tier 1 Capital}} > 15\%
$$

Trong đó:
- $\Delta\text{EVE}_i$: Biến động sụt giảm giá trị kinh tế của vốn chủ sở hữu dưới kịch bản sốc lãi suất thứ $i$ trong 6 kịch bản quy định tại Annex 2 của d368 [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
- $\text{Tier 1 Capital}$: Vốn cấp 1 của ngân hàng theo định nghĩa của Basel III (tính tại cùng thời điểm báo cáo) [[src-bcbs-irrbb-2016#^irrbb-p12-1]].

### Các phép thử ngoại lai bổ sung (Nguyên tắc 12, đoạn 89)
Cơ quan giám sát quốc gia có quyền quyết định áp dụng thêm các phép thử ngoại lai khác trong phạm vi thẩm quyền của mình [[src-bcbs-irrbb-2016#^irrbb-p12-2]]:
- Dùng thước đo vốn hẹp hơn: So sánh $\Delta\text{EVE}$ với Vốn cấp 1 thông thường (**CET1 Capital**).
- Phép thử dựa trên rủi ro thu nhập: So sánh biến động thu nhập lãi thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]] với khả năng tạo lợi nhuận hoạt động để đánh giá nguy cơ ngân hàng mất khả năng trang trải chi phí và duy trì kinh doanh bình thường [[src-bcbs-irrbb-2016#^irrbb-p12-2]].
- **Quy tắc chặn dưới**: Mọi phép thử bổ sung đều phải có độ khắt khe tối thiểu tương đương ngưỡng 15% Tier 1 Capital [[src-bcbs-irrbb-2016#^irrbb-p12-2]].

## Diễn giải

### Tiêu chí định lượng và So sánh với Tiêu chuẩn 2004

Chuẩn mực d368 đã thắt chặt đáng kể ngưỡng xác định ngân hàng ngoại lai so với Hướng dẫn IRR 2004 [[src-bcbs-irrbb-2016#^irrbb-u01-6]]:

| Tiêu chí | Chuẩn mực 2004 (Cũ) | Chuẩn mực 2016 d368 (Hiện hành) |
|---|---|---|
| **Chỉ số rủi ro đo lường** | Giảm giá trị kinh tế $\Delta\text{EVE}$ | Giảm giá trị kinh tế cực đại $\max_{i=1..6} \Delta\text{EVE}_i$ [[src-bcbs-irrbb-2016#^irrbb-p12-1]] |
| **Kịch bản sốc lãi suất** | Sốc song song $\pm 200$ bps | **6 kịch bản sốc chuẩn hoá** (Parallel, Steepener, Flattener, Short rate) [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| **Mẫu số vốn so sánh** | Tổng vốn tự có (Total Regulatory Capital: Tier 1 + Tier 2) | **Vốn cấp 1 (Tier 1 Capital)** [[src-bcbs-irrbb-2016#^irrbb-p12-1]] |
| **Ngưỡng kích hoạt ngoại lai** | **$\Delta\text{EVE} > 20\%$ Tổng vốn tự có** | **$\max \Delta\text{EVE} > 15\%$ Vốn cấp 1 (Tier 1 Capital)** [[src-bcbs-irrbb-2016#^irrbb-p12-1]] |

#### Ý nghĩa của việc thắt chặt ngưỡng:
1. **Chuyển từ Tổng vốn sang Vốn cấp 1**: Vốn cấp 1 (Tier 1 Capital) có quy mô nhỏ hơn Tổng vốn tự có (do loại bỏ nợ thứ cấp Vốn cấp 2). Việc giảm từ 20% Tổng vốn xuống 15% Vốn cấp 1 đại diện cho một bước thắt chặt an toàn vĩ mô rất nghiêm ngặt, buộc các ngân hàng phải kiểm soát chặt chẽ danh mục tài sản nhạy cảm lãi suất.
2. **Áp dụng 6 kịch bản sốc**: Không chỉ kiểm tra sốc song song mà còn quét toàn diện các cú sốc xoay trục đường cong (Steepener, Flattener), ngăn chặn các cấu trúc phòng ngừa rủi ro giả tạo (chỉ triệt tiêu duration tổng mà vẫn gánh rủi ro xoắn đường cong cực lớn) [[src-bcbs-irrbb-2016#^irrbb-u07-1]].

### Chế tài và Biện pháp can thiệp của Cơ quan giám sát

Khi cơ quan giám sát kết luận ngân hàng quản trị IRRBB không đầy đủ hoặc có rủi ro quá mức so với vốn, thu nhập hay hồ sơ rủi ro chung, cơ quan giám sát phải (must) yêu cầu ngân hàng thực hiện một hoặc nhiều biện pháp sau [[src-bcbs-irrbb-2016#^irrbb-p12-3]]; việc giảm IRRBB và/hoặc nâng vốn nên (should) đạt được trong một thời hạn xác định [[src-bcbs-irrbb-2016#^irrbb-p12-8]]:
1. **Yêu cầu giảm phơi lượng rủi ro (Risk Mitigation)**: Buộc ngân hàng phải thực hiện các biện pháp tái cơ cấu danh mục hoặc phòng ngừa rủi ro (hedging qua lãi suất phái sinh) để hạ thời lượng và khe hở kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-p12-3]].
2. **Yêu cầu tăng thêm vốn quy định (Pillar 2 Capital Add-on)**: Bắt buộc ngân hàng phải phát hành thêm vốn cổ phần hoặc giữ lại lợi nhuận để bù đắp rủi ro lãi suất quá mức [[src-bcbs-irrbb-2016#^irrbb-p12-3]].
3. **Áp trần tham số mô hình nội bộ (Impose Parameter Constraints)**: Ràng buộc hoặc bác bỏ các giả định hành vi quá lạc quan của ngân hàng (ví dụ áp trần tiền gửi lõi NMDs thấp hơn, hoặc ấn định tỷ lệ rút vốn sớm cao hơn) [[src-bcbs-irrbb-2016#^irrbb-p12-3]].
4. **Bắt buộc áp dụng Khuôn khổ chuẩn hoá (Mandate Standardised Framework)**: Nếu hệ thống mô hình nội bộ (IMS) bị đánh giá là khiếm khuyết, cơ quan giám sát tước quyền dùng mô hình nội bộ và ép ngân hàng áp dụng phương pháp chuẩn hoá của Section IV [[src-bcbs-irrbb-2016#^irrbb-p11-2]].
5. **Cải thiện hệ thống quản trị**: Buộc thay đổi quy trình phê duyệt của HĐQT/[[alco|ALCO]], tăng cường [[model-validation|kiểm định mô hình]] độc lập và kiểm toán nội bộ [[src-bcbs-irrbb-2016#^irrbb-p12-3]].

### Góc nhìn EU (nguồn T4, khác jurisdiction)

*Fidelio Tata mô tả khung EU; đây là tham chiếu, không phải chuẩn BCBS, và khác jurisdiction nên không ghi conflict.*

| Mốc | Ngưỡng | Nguồn |
|---|---|---|
| Chỉ thị 2006/48/EC, CRD IV | Giá trị kinh tế giảm quá 20% vốn tự có, sốc 200 bp | [[src-tata-bank-alm#^tata-reg-5]] |
| CRD V | EVE giảm quá 15% vốn cấp 1 theo sáu kịch bản, hoặc NII suy giảm lớn theo hai kịch bản | [[src-tata-bank-alm#^tata-reg-5]] |
| EBA 2018 | Loại CET1, bảng cân đối run-off, kỳ hạn bình quân NMD tối đa 5 năm, cộng thay đổi dương giữa các đồng tiền với trọng số 50% | [[src-tata-bank-alm#^tata-reg-7]] |
| EBA 2018 (sàn) | Sàn sau sốc −100 bp, tăng 5 bp/năm, 0% từ 20 năm | [[src-tata-bank-alm#^tata-reg-8]] |
| RTS/2022/10, SOT EVE | 15% vốn cấp 1, bảng cân đối run-off; sàn tuyến tính −150 bp tăng 3 bp/năm tới 0% ở 50 năm | [[src-tata-bank-alm#^tata-sot-1]] [[src-tata-bank-alm#^tata-sot-2]] |
| RTS/2022/10, SOT NII | 5% vốn cấp 1; NII kế toán 1 năm, bảng cân đối không đổi, gồm biên thương mại, không áp sàn tuyến tính | [[src-tata-bank-alm#^tata-sot-3]] |

- Tuân thủ đồng thời: SOT EVE đặt cận trên và cận dưới cho tỷ trọng tài sản cố định theo duration, SOT NII đặt mức tối thiểu, nên vùng tuân thủ có thể rất nhỏ [[src-tata-bank-alm#^tata-sot-4]].
- Ví dụ [[silicon-valley-bank]]: để không là outlier theo phép thử EVE (sốc 2% dưới 15% vốn), duration tiền gửi phải trên 3,7 năm [[src-tata-bank-alm#^tata-svb-7]].
- *Diễn giải:* d368 và [[tt83-2025]] không có SOT NII; sàn EBA 2018 và sàn RTS 2022 khác nhau do khác hiệu lực, không phải conflict.

## Ứng dụng trong ALM

### Tác động mang tính chiến lược lên Bảng cân đối ALM
- **Giới hạn tự nhiên cho việc kéo dài kỳ hạn tài sản**: Phép thử 15% Tier 1 tạo ra một "hàng rào thép" ngăn các NHTM nắm giữ quá nhiều tài sản dài hạn (như trái phiếu chính phủ 10–20 năm trong đệm [[hqla]] hay các khoản vay mua nhà cố định 15–25 năm) khi chưa có nguồn vốn dài hạn tương ứng trong [[nsfr]].
- Xem thêm tại [[bcbs-irrbb]], [[economic-value-of-equity]], [[gap-risk]].

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
