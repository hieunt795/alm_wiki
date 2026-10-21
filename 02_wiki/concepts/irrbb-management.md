---
title: "IRRBB Management"
aliases: [IRRBB Management, Quản trị IRRBB, Quản lý rủi ro lãi suất trên sổ ngân hàng, Interest rate risk in the banking book management]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bardaeva-alm]]", "[[src-bcbs-irrbb-2016]]", "[[src-tt83-2025-nhnn]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: input-to, to: "[[icaap]]", cite: "[[src-bardaeva-alm#^ch11-19]]"}
tags: [irrbb, governance, risk-management]
updated: 2026-10-21
reviewed:
---

## Ý chính
IRRBB (interest rate risk in the banking book) là rủi ro hiện tại hoặc tiềm năng đối với vốn và thu nhập của ngân hàng do biến động bất lợi của lãi suất tác động lên vị thế trên [[banking-book]] [[src-bcbs-irrbb-2016#^irrbb-u02-1]] [[src-bardaeva-alm#^ch11-13]]. Tác động đi qua hai kênh [[src-bardaeva-alm#^ch11-14]]:
- thu nhập và chi phí nhạy lãi suất thay đổi, đo bằng [[net-interest-income-sensitivity]];
- giá trị hiện tại và thời điểm của dòng tiền tương lai thay đổi, đo bằng [[economic-value-of-equity]].

Node này mô tả quy trình quản trị IRRBB và phân công tổ chức. Chuẩn mực BCBS nằm ở [[bcbs-irrbb]], quy định NHNN nằm ở [[tt83-2025]], khung đo lường chuẩn hoá nằm ở [[irrbb-standardised-framework]].

## Cơ chế & drivers

### Quy trình ba bước (Bardaeva)
| Bước | Nội dung | Nguồn |
|---|---|---|
| 1. Nhận diện | Chọn các loại rủi ro lãi suất liên quan tới ngân hàng. [[gap-risk]], [[basis-risk]] và yield curve risk là chung cho mọi ngân hàng; [[option-risk]] (kể cả [[behavioural-options]]) có thể nhỏ hoặc đặc thù | [[src-bardaeva-alm#^ch11-15]] |
| 2. Đo lường | Đo tác động của các kịch bản sốc lãi suất lên vốn, NII và EVE. Thước đo giá trị kinh tế xét toàn bộ vòng đời bảng cân đối; thước đo thu nhập xét trong horizon thường là horizon ngân sách 3–4 năm | [[src-bardaeva-alm#^ch11-16]] |
| 2. Đo lường (vị thế không chuẩn) | Nên chú ý công cụ không xác định kỳ hạn, ví dụ [[non-maturity-deposits]] | [[src-bardaeva-alm#^ch11-17]] |
| 3. Quản lý | Quyết định quản lý những tác động không phù hợp [[risk-appetite]] (RAS). Công cụ: phòng ngừa bằng phái sinh, đầu tư equity, công cụ không nhạy lãi suất, dự báo lãi suất, kế hoạch bảng cân đối | [[src-bardaeva-alm#^ch11-18]] |
| Vốn | Mức đủ vốn cho IRRBB phải được xét riêng trong [[icaap]] | [[src-bardaeva-alm#^ch11-19]] |

BCBS d368 dùng ba nhóm cấu phần là gap risk, basis risk và option risk [[src-bcbs-irrbb-2016#^irrbb-u02-2]]. Bardaeva tách thêm yield curve risk thành một loại riêng [[src-bardaeva-alm#^ch11-15]].

*Diễn giải:* Trong d368, yield curve risk (thay đổi hình dạng đường cong) thuộc gap risk dạng phi song song, như node [[gap-risk]] đang mô tả. Hai cách phân loại khác nhau ở cách gom nhóm, không khác về phạm vi rủi ro được đo.

### Phân công tổ chức
- Risk lập báo cáo phân tích rủi ro, ví dụ gap analysis, rồi chuyển cho ALM [[src-bardaeva-alm#^ch11-22]].
- ALM dùng kết quả của Risk và đề xuất công cụ quản lý; Trading Desk thực hiện giao dịch do ALM đề xuất sau khi hội đồng có thẩm quyền phê duyệt [[src-bardaeva-alm#^ch11-4]].
- ALM gửi yêu cầu đã được [[alco]] duyệt cho Trading Desk làm giao dịch phòng ngừa, hoặc cho đơn vị kinh doanh đổi chiến lược về khối lượng và lãi suất [[src-bardaeva-alm#^ch11-22]].
- Amber zone của khẩu vị rủi ro cho các rủi ro ALM được đặt ở ALCO [[src-bardaeva-alm#^ch11-20]].
- Trong SREP, IRRBB thuộc trách nhiệm của ALM, và chính sách, mô hình phù hợp nên chứng minh được tính bền vững của ngân hàng [[src-bardaeva-alm#^ch13-6]]. Xem [[srep]].

Cách đặt bộ phận ALM để tránh xung đột lợi ích nằm ở [[alm-operating-model]].

### Đặc thù thị trường
- Thị trường chỉ có tài khoản tiết kiệm đòi hỏi đánh giá stickiness và chia tài khoản không kỳ hạn vào khung thời gian [[src-bardaeva-alm#^ch12-13]].
- Thị trường bất định với kỳ hạn huy động tối đa 1 năm cho tài sản dài hạn đòi hỏi dùng [[interest-rate-swap]] (thường kèm phái sinh FX) để phòng ngừa IRR [[src-bardaeva-alm#^ch12-13]].
- Công ty con ở thị trường không phòng ngừa được mọi rủi ro làm việc quản lý khó hơn [[src-bardaeva-alm#^ch12-15]]; Group Treasury tối thiểu hoá vị thế với rủi ro phòng ngừa được và kiểm soát chặt rủi ro không phòng ngừa được [[src-bardaeva-alm#^ch12-2]].

### Thị trường phát triển và thị trường mới nổi
| Đặc điểm | Thị trường phát triển | Thị trường mới nổi | Nguồn |
|---|---|---|---|
| Độ nhạy bảng cân đối | Asset sensitive, cho vay thả nổi, tiền gửi bán lẻ sticky | Liability sensitive, không có swap, tài sản rất sticky, tiền gửi bán lẻ biến động hơn với phần core ổn định thấp hơn | [[src-bardaeva-alm#^ch14-14]] [[src-bardaeva-alm#^ch14-15]] |
| Trọng tâm ALM | Liquidity buffer, mục tiêu chuyển hoá kỳ hạn, tái định giá tài khoản tiết kiệm | Biến động thị trường cao, gần với vai trò trong khủng hoảng | [[src-bardaeva-alm#^ch14-14]] [[src-bardaeva-alm#^ch14-15]] |
| Phòng ngừa | Khả năng phòng ngừa cao | Khả năng phòng ngừa hạn chế; nợ dài hạn và công cụ phòng ngừa kém thanh khoản hoặc không có | [[src-bardaeva-alm#^ch14-16]] [[src-bardaeva-alm#^ch14-11]] |
| Đường cong nội bộ | Dễ dựng; cần định giá quyền chọn nhúng | Khó dựng; áp dụng cách tiếp cận đơn giản hơn | [[src-bardaeva-alm#^ch14-16]] |
| Hành vi khách hàng | Gắn bó lâu dài, mô hình hoá được | Lo âu, quyết định đột ngột theo tin tức | [[src-bardaeva-alm#^ch14-12]] [[src-bardaeva-alm#^ch14-11]] |
| Yêu cầu mô hình của giám sát | Mô hình và cách tiếp cận do cơ quan giám sát định sẵn | Không yêu cầu mô hình phức tạp | [[src-bardaeva-alm#^ch14-15]] |

*Diễn giải:* mô tả thị trường mới nổi của Bardaeva (liability sensitive, thiếu swap, tiền gửi bán lẻ biến động) gần với bối cảnh ngân hàng VN mà wiki đang ghi nhận, nhưng nguồn không nói về VN; cần số liệu VN để kiểm chứng.

### Trong khủng hoảng
- IRRBB và FTP là hai trong các mảng ALM nên có kế hoạch hành động định sẵn theo mức độ nghiêm trọng của khủng hoảng [[src-bardaeva-alm#^ch15-1]].
- Đường cong FTP phải được định giá lại và/hoặc áp steering margin; điều chỉnh độ dốc đường cong FTP để quản lý tác động của kết quả chuyển hoá kỳ hạn lên NII [[src-bardaeva-alm#^ch15-8]].

## Phụ thuộc regime
- Xung đột lợi ích trong ALM, kể cả quanh việc chấp nhận thêm gap lãi suất, có xu hướng tăng trong suy thoái và khủng hoảng [[src-bardaeva-alm#^ch11-23]] [[src-bardaeva-alm#^ch11-12]].

## Góc nhìn theo domain
- **Basel**: IRRBB thuộc Trụ cột 2 [[src-bcbs-irrbb-2016#^irrbb-u01-1]]. Nguyên tắc 1 yêu cầu nhận diện, đo lường, theo dõi và kiểm soát IRRBB [[src-bcbs-irrbb-2016#^irrbb-p01-1]]; Nguyên tắc 3 yêu cầu khẩu vị rủi ro thể hiện theo cả economic value và earnings [[src-bcbs-irrbb-2016#^irrbb-p03-1]]; Nguyên tắc 9 yêu cầu xét mức đủ vốn cho IRRBB trong ICAAP [[src-bcbs-irrbb-2016#^irrbb-p09-1]].
- **ALM**: Bardaeva xếp IRRBB vào trách nhiệm của ALM, không phải của Risk [[src-bardaeva-alm#^ch13-6]]. Bản chất kinh tế của IRRBB (EVE trên toàn vòng đời) là một ví dụ của economic perspective bổ sung cho normative perspective [[src-bardaeva-alm#^ch16-3]].
- **Thông lệ (Choudhry, T4)**: risk register mẫu ghi khẩu vị rủi ro lãi suất là hạn mức chênh lệch tái định giá [[src-choudhry-principles-banking#^choudhry-rmf-5]]; Banking Book được kiểm soát bằng hạn mức BPV và Interest Rate Gap Limits, Treasury quản lý rủi ro lãi suất trong hạn mức do ALCO đặt [[src-choudhry-principles-banking#^choudhry-bbp-5]] [[src-choudhry-principles-banking#^choudhry-bbp-4]]. Toàn bộ rủi ro lãi suất nên tập trung về Treasury qua giao dịch funding hoặc internal swap [[src-choudhry-principles-banking#^choudhry-st-11]]. Non-traded market risk do Head of Treasury sở hữu ở tuyến 1 [[src-choudhry-principles-banking#^choudhry-rmf-4]]. Xem [[key-risk-indicators]], [[stress-testing]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Định nghĩa | Rủi ro với vốn và thu nhập do lãi suất biến động bất lợi tác động lên vị thế sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u02-1]] | [cần nguồn] | | |
| Chiến lược | [cần nguồn] | Phải ban hành chiến lược IRRBB, tối thiểu dùng repricing gap profile [[src-tt83-2025-nhnn#^d53-1a1]], ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-1a2]], nguyên tắc phòng ngừa và thẩm quyền phê duyệt [[src-tt83-2025-nhnn#^d53-1b]] | TT83 Đ53.1 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Hạn mức | Khẩu vị rủi ro theo cả economic value và earnings [[src-bcbs-irrbb-2016#^irrbb-p03-1]] | Tối thiểu hạn mức ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-2]] | TT83 Đ53.2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Tần suất quy trình | [cần nguồn] | Nhận dạng, đo lường, theo dõi, kiểm soát tối thiểu hằng quý và đột xuất [[src-tt83-2025-nhnn#^d54-1a]] | TT83 Đ54.1.a | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Độc lập | [cần nguồn] | Bộ phận đo lường, theo dõi, kiểm soát IRRBB phải độc lập với bộ phận kinh doanh phát sinh rủi ro [[src-tt83-2025-nhnn#^d54-1b]] | TT83 Đ54.1.b | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Vốn | Xét mức đủ vốn cho IRRBB trong ICAAP [[src-bcbs-irrbb-2016#^irrbb-p09-1]] | Xem [[rwa-irrbb]] và [[icaap]] | | |

Khác biệt: [[tt83-2025]] quy định tần suất tối thiểu hằng quý và tách bạch bộ phận đo lường với bộ phận kinh doanh; Bardaeva (T4) đặt ALM, không phải Risk, chịu trách nhiệm quản trị IRRBB [[src-bardaeva-alm#^ch13-6]], còn Risk đo lường và lập báo cáo [[src-bardaeva-alm#^ch11-22]].

## Bằng chứng thực nghiệm
- **Chỉ đặt hạn mức ΔNII (ví dụ của Lubinska)**: ngân hàng có trái phiếu cố định và mortgage dài tài trợ bằng CASA, chỉ đặt hạn mức ΔNII, không có hạn mức ΔEVE. Lãi suất giảm trái kỳ vọng; prepayment tăng cùng trái phiếu đáo hạn không tái đầu tư làm duration tài sản ngắn lại và mở chênh lệch cấu trúc. Nếu có ΔEVE, treasurer có thể đã vượt hạn mức và phải tăng duration tài sản [[src-lubinska-alm-optimisation#^lubinska-u01-17]]. Lubinska nêu IRRBB gồm giảm thu nhập lãi và giảm giá trị thị trường, nên khái niệm, báo cáo, hạn mức phải phản ánh cả hai góc nhìn [[src-lubinska-alm-optimisation#^lubinska-u01-9]]. Xem [[economic-value-of-equity]], [[net-interest-income-sensitivity]].
[cần nguồn]

## Câu hỏi mở
- Horizon earnings 3–4 năm của Bardaeva [[src-bardaeva-alm#^ch11-16]] là thực hành nội bộ; TT83 PL5 đo ΔNII trong 01 năm [[src-tt83-2025-nhnn#^pl5-b2]]. Wiki chưa có nguồn nói horizon nào ngân hàng VN nên dùng cho mục đích nội bộ.
- Định nghĩa IRRBB trong Đ3 TT83/2025 chưa được trích [cần nguồn].
