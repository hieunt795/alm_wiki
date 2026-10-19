---
title: "NII Planning"
aliases: [NII Planning, Lập kế hoạch NII, Kế hoạch thu nhập lãi thuần, NII budgeting, NII forecast]
type: concept
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: drives, to: "[[net-interest-margin]]", cite: "[[src-choudhry-principles-banking#^choudhry-nim-12]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-tata-bank-alm#^tata-nii-3]]"}
tags: [nii, planning, budgeting, margin, scenario]
updated: 2026-10-19
reviewed:
---

## Ý chính
NII planning là việc dự phóng thu nhập lãi thuần cho các kỳ tương lai, khác với việc tính NII của kỳ đã qua để báo cáo [[src-tata-bank-alm#^tata-niip-1]]. Kế hoạch hằng năm tối thiểu gồm khối lượng và biên lãi kỳ vọng của từng mảng kinh doanh, cùng môi trường lãi suất kỳ vọng [[src-tata-bank-alm#^tata-niip-3]].

Nguồn nhấn mạnh quy trình này có chiều chính trị:
- đơn vị kinh doanh ngại lập kế hoạch NII giảm, vì kéo theo giảm phân bổ nguồn lực;
- cũng ngại kế hoạch tăng quá cao, vì dễ không đạt.

Vì vậy cần giữ quy trình khách quan, kiểm định giả định và dựa trên dữ liệu [[src-tata-bank-alm#^tata-niip-1]].

## Cơ chế & drivers
**Tầm hoạch định** [[src-tata-bank-alm#^tata-niip-2]]:

| Tầm | Nội dung | Nguồn |
|---|---|---|
| Forecast | Năm hiện tại: kết quả các tháng đã qua cộng dự báo các tháng còn lại; thường làm 3–4 lần/năm | [[src-tata-bank-alm#^tata-niip-2]] |
| Budget | Năm kế tiếp; là dự báo thuần | [[src-tata-bank-alm#^tata-niip-2]] |
| Plan | Các năm sau, đến 3–5 năm; là dự báo thuần | [[src-tata-bank-alm#^tata-niip-2]] |

**Kịch bản lãi suất.** Phải mô hình hoá nhiều môi trường lãi suất, mỗi môi trường đi kèm khối lượng và biên lãi nhất quán với nó. Kịch bản cơ sở thường là lãi suất spot hiện tại hoặc lãi suất forward. Các kịch bản thay thế cho thấy phân phối tiềm năng của NII [[src-tata-bank-alm#^tata-niip-3]].

**Kế hoạch khối lượng.** Lập riêng cho từng mảng, vì run-off mỗi mảng khác nhau, chẳng hạn có hay không có quyền trả trước. Run-off là hàm của môi trường lãi suất và hành vi khách hàng giả định. Sau đó cộng thêm nghiệp vụ mới, phần này cũng phụ thuộc lãi suất [[src-tata-bank-alm#^tata-niip-4]]. Xem [[behavioural-options]].

**Kế hoạch biên lãi.** Biên lãi cũng lập riêng cho từng mảng và phải ước tính margin compression. Nguồn dẫn hai bằng chứng thực nghiệm:
- Busch và cộng sự (2021, ngân hàng Đức): NIM giảm 5 bp cho mỗi năm thêm sau cú dịch chuyển xuống 100 bp [[src-tata-bank-alm#^tata-niip-5]];
- Cruz-García và cộng sự (2019, 32 nước, 2008–2014): biên lãi biến động khoảng 19 bp cho mỗi 100 bp lãi suất ngắn hạn [[src-tata-bank-alm#^tata-niip-5]].

Nếu giả định một "margin-beta" thì biên kế hoạch phải điều chỉnh theo từng kịch bản lãi suất. Trên thực tế, nhà quản lý thường giả định biên giữ nguyên [[src-tata-bank-alm#^tata-niip-5]].

**Kế hoạch ALM toàn diện.** Kế hoạch ALM phải dự phóng rủi ro lãi suất tương lai, tức tính độ nhạy EVE và NII kỳ vọng ([[economic-value-of-equity]], [[net-interest-income-sensitivity]]). Kế hoạch khối lượng thuần là không đủ; cần thêm hai thông tin [[src-tata-bank-alm#^tata-niip-6]]:
- khối lượng chia theo phân khúc hành vi lãi suất;
- kỳ hạn của nghiệp vụ mới, ví dụ cố định 5 năm hay 20 năm [[src-tata-bank-alm#^tata-niip-6]].

Kế hoạch cũng phải dự phóng LCR, NSFR và yêu cầu vốn, để đáp ứng mọi yêu cầu quy định cùng hạn mức và mục tiêu nội bộ [[src-tata-bank-alm#^tata-niip-6]]. Xem [[lcr]], [[nsfr]].

**Mô hình dự báo NII/NIM (Choudhry).** Dự báo NII/NIM để hiểu xu hướng, xét hành động quản trị khi thu nhập dự kiến giảm, và làm cơ sở cho phân tích kịch bản và stress test [[src-choudhry-principles-banking#^choudhry-nim-12]].

| Cách tiếp cận | Nội dung | Nguồn |
|---|---|---|
| Top-down | Dự báo theo xu hướng tổng hợp (ví dụ theo sản phẩm); thường dùng bảng tính rời của các khối, không có hệ thống tích hợp | [[src-choudhry-principles-banking#^choudhry-nim-12]] |
| Bottom-up | Thuộc tính từng tài sản, nợ (số dư, biên trên reference rate, lịch trả nợ dự kiến, kỳ hạn) cộng dự báo reference rate; cộng phần nghiệp vụ mới | [[src-choudhry-principles-banking#^choudhry-nim-13]] |

Sốc lãi suất và tính lại mô hình bottom-up, có thể với giả định trả nợ và nghiệp vụ mới khác, cho phép đánh giá độ nhạy NII [[src-choudhry-principles-banking#^choudhry-nim-13]]. Thách thức chính là luồng dữ liệu cấp tài khoản từ hệ thống giao dịch và chất lượng dữ liệu đó [[src-choudhry-principles-banking#^choudhry-nim-13]]. Xem [[net-interest-income-sensitivity]], [[net-interest-margin]], và các bài tổng hợp [[nii-nature-repricing-mechanisms-and-planning]], [[nii-shocks-regulation-hedging-and-alco-tradeoffs]].

Ngân hàng có thể hành động để bảo vệ hoặc tăng NIM (Table 1.10 của Choudhry) [[src-choudhry-principles-banking#^choudhry-nim-11]].

## Phụ thuộc regime
- Khối lượng phản ứng nhanh với lãi suất. Ở Đức 1999–2021, khi lãi suất giảm dài hạn, tiền gửi không kỳ hạn tăng từ 7,9% lên 29,3% tổng tài sản [[src-tata-bank-alm#^tata-prac-1]]. Chỉ trong 2021–2023, tỷ trọng này giảm còn 26,1% và tiền gửi có kỳ hạn dưới 1 năm tăng từ 2,6% lên 5,9% [[src-tata-bank-alm#^tata-prac-2]].
- Khi lãi suất âm, biên trung gian giảm, vì lợi suất tài sản giảm trong khi phần lớn chi phí vốn không đổi [[src-tata-bank-alm#^tata-neg-4]]. Xem [[negative-interest-rates]].

*Diễn giải:* margin-beta và deposit beta cùng quyết định NII trong mỗi kịch bản. Giữ biên không đổi ở mọi kịch bản tức là ngầm giả định margin-beta bằng 0, trái với cả hai bằng chứng thực nghiệm mà nguồn dẫn.

## Góc nhìn theo domain
- **ALM**: kế hoạch NII nối kế hoạch kinh doanh với đo lường IRRBB và thanh khoản tương lai [[src-tata-bank-alm#^tata-niip-6]]. FTP cho phép ALM vận hành như profit center [[src-tata-bank-alm#^tata-prac-4]]. Xem [[funds-transfer-pricing]].
- **VN**: TT83/2025 yêu cầu dự phóng vốn tự có và vốn mục tiêu trong ICAAP ([[projected-own-funds]], [[capital-plan]]). Phần đã ingest không có quy định riêng về kế hoạch NII [cần nguồn].

## Bằng chứng thực nghiệm
- Số liệu bảng cân đối MFI Đức 1999–2023 [[src-tata-bank-alm#^tata-prac-1]] [[src-tata-bank-alm#^tata-prac-2]].
- Ước lượng margin-beta của Busch và cộng sự (2021) và Cruz-García và cộng sự (2019) [[src-tata-bank-alm#^tata-niip-5]]. Cả hai đều lấy qua nguồn T4, chưa đối chiếu bản gốc.

## Câu hỏi mở
- Margin-beta của ngân hàng VN chưa có nguồn [cần nguồn].
- Quan hệ giữa kế hoạch NII và chỉ tiêu ΔNII trong báo cáo IRRBB theo TT83 chưa có nguồn nói trực tiếp.
