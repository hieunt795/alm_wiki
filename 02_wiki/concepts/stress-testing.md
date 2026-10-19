---
title: "Stress Testing"
aliases: [Stress Testing, Kiểm tra sức chịu đựng]
type: concept
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]"]
relations: []
tags: [stress-test, governance, internal-control]
updated: 2026-10-19
reviewed:
---

## Ý chính
Kiểm tra sức chịu đựng là công cụ quản lý rủi ro mang tính dự báo, đánh giá tác động tiềm ẩn của biến động bất lợi để xác định khả năng chịu đựng rủi ro của ngân hàng [[src-tt83-2025-nhnn#^d3-8]]. Theo [[tt83-2025]], ngân hàng phải kiểm tra sức chịu đựng về vốn và tối thiểu cho các rủi ro trọng yếu: tín dụng, thị trường, IRRBB, thanh khoản [[src-tt83-2025-nhnn#^d23-1]].

## Cơ chế & drivers
**Phương pháp.**
- Với rủi ro tín dụng và thị trường, ngân hàng chọn tối thiểu một trong ba phương pháp [[src-tt83-2025-nhnn#^d23-3]]:
  - phân tích độ nhạy: thay đổi một yếu tố hoặc nhóm yếu tố liên quan chặt, giữ nguyên phần còn lại; tối thiểu 2 mức nghiêm trọng;
  - phân tích kịch bản: thay đổi đồng thời nhiều yếu tố; tối thiểu 2 kịch bản (bình thường và bất lợi);
  - kiểm tra sức chịu đựng ngược (reverse stress testing): giả định trường hợp bất lợi nghiêm trọng (như vi phạm tỷ lệ an toàn vốn tối thiểu), rồi tìm sự kiện, yếu tố dẫn tới. Xem [[reverse-stress-testing]].
- Phương pháp cho thanh khoản, IRRBB và vốn quy định riêng ở Đ48, Đ54 và Đ60 [[src-tt83-2025-nhnn#^d23-4]]. Xem [[liquidity-stress-testing]]. Với IRRBB, kiểm tra sức chịu đựng dùng ΔNII, ΔEVE [[src-tt83-2025-nhnn#^d54-3b]].

Báo cáo ICAAP gửi NHNN nêu giả định kịch bản bất lợi, phương pháp tính tác động lên RWA từng loại rủi ro, và RWA ở cả hai kịch bản [[src-tt83-2025-nhnn#^pl3-4]]. Kiểm tra sức chịu đựng về vốn dùng 2 kịch bản (bình thường, bất lợi) với giả định tối thiểu về lãi suất, tỷ giá, giá vàng, chất lượng tín dụng. Giả định lãi suất phải được tính tác động lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]. Xem [[icaap]].

**Tần suất tối thiểu** [[src-tt83-2025-nhnn#^d23-5]]:

| Loại | Tần suất | Nguồn |
|---|---|---|
| Thanh khoản | Hằng quý, và khi có sự kiện có thể tác động nghiêm trọng tới thanh khoản | [[src-tt83-2025-nhnn#^d23-5]] |
| IRRBB | Hằng quý | [[src-tt83-2025-nhnn#^d23-5]] |
| Tín dụng, thị trường | Hằng năm; bắt buộc chậm nhất từ 01/01/2028 | [[src-tt83-2025-nhnn#^d23-5]] [[src-tt83-2025-nhnn#^d74-2]] |
| Vốn | Hằng năm, và khi có sự kiện có thể tác động nghiêm trọng tới mức đủ vốn | [[src-tt83-2025-nhnn#^d23-5]] |

**Quy định nội bộ** tối thiểu gồm [[src-tt83-2025-nhnn#^d23-2]]:
- loại và mục tiêu kiểm tra; tần suất;
- phạm vi và trạng thái nội, ngoại bảng;
- phương pháp luận: giả định, yếu tố rủi ro, kịch bản, mô hình, dữ liệu, cách dùng kết quả;
- quy trình và trách nhiệm.

**Theo loại rủi ro.** Chiến lược quản lý rủi ro tín dụng phải có nguyên tắc kiểm tra sức chịu đựng về rủi ro tín dụng [[src-tt83-2025-nhnn#^d26-2]]; báo cáo nội bộ hằng quý về rủi ro tín dụng nêu kết quả kiểm tra trong kỳ (nếu có) [[src-tt83-2025-nhnn#^d34-1]]. Xem [[credit-risk-management]]. Chiến lược quản lý rủi ro thị trường phải có nguyên tắc kiểm tra sức chịu đựng cho rủi ro thị trường [[src-tt83-2025-nhnn#^d35-1]]; báo cáo nội bộ 6 tháng về rủi ro thị trường nêu kết quả kiểm tra sức chịu đựng trong kỳ (nếu có) [[src-tt83-2025-nhnn#^d37-2]]. Xem [[market-risk-management]].

Bộ phận quản lý rủi ro xây dựng phương pháp luận và lập kịch bản, phối hợp với bộ phận kinh doanh, bộ phận tuân thủ và bộ phận khác [[src-tt83-2025-nhnn#^d25-5]].

**Dùng kết quả** [[src-tt83-2025-nhnn#^d23-6]]:
- đánh giá khả năng tuân thủ tỷ lệ bảo đảm an toàn và các hạn chế khác;
- xây dựng hoặc sửa kế hoạch, chiến lược kinh doanh, chính sách quản lý rủi ro, kế hoạch dự phòng, phương án khắc phục khi cần;
- với thanh khoản: lập kế hoạch dự phòng theo Đ48.4 ([[contingency-funding-plan]]);
- với vốn: tính vốn kinh tế để xác định vốn mục tiêu ([[target-capital]]).

**Khung stress testing theo Choudhry (T4, UK).**
- Stress testing là "uốn" bảng cân đối trên giấy theo điều kiện thị trường giả định để xem tác động lên vốn và thanh khoản [[src-choudhry-principles-banking#^choudhry-st-1]]. Stress là thay đổi định lượng của một yếu tố rủi ro; scenario là nhiều tham số thay đổi cùng lúc [[src-choudhry-principles-banking#^choudhry-st-8]].
- Mục tiêu gồm: đầu vào cho khẩu vị rủi ro và kế hoạch kinh doanh, hỗ trợ kế hoạch vốn và kế hoạch dự phòng vốn, và chứng minh ngân hàng sống sót qua suy thoái từ 1 trong 25 năm đến 1 trong 100 năm mà vẫn giữ CAR tối thiểu [[src-choudhry-principles-banking#^choudhry-st-7]].
- Yếu tố cần stress gồm lãi suất, tỷ giá, giá chứng khoán, PD, LGD, rủi ro tập trung, funding risk và tổn thất hoạt động [[src-choudhry-principles-banking#^choudhry-st-9]].
- Phương pháp: định giá lại tài sản và nợ theo mức thị trường khi stress; rủi ro thị trường stress theo lãi suất, tỷ giá, credit spread [[src-choudhry-principles-banking#^choudhry-st-10]]. Credit spread chỉ áp lên đường cong chiết khấu khi định giá trái phiếu [[src-choudhry-principles-banking#^choudhry-st-12]]. Stress tín dụng dịch hạng hai phần ba bậc và dùng recovery rate 0%, 20%, 40%, 60% [[src-choudhry-principles-banking#^choudhry-st-13]].
- Kết quả tách thành P&L (thay đổi PV của dòng lãi với phần tạo NII), vốn (thêm thay đổi giá danh mục available for sale) và thanh khoản [[src-choudhry-principles-banking#^choudhry-st-14]].
- Văn phòng CRO lưu stress test log; log mẫu có 34 stress test lãi suất và FX chạy hằng ngày, 9 stress test CAR và 12 stress test thanh khoản chạy hằng tháng [[src-choudhry-principles-banking#^choudhry-st-15]].
- Kết quả phải đi vào quản lý rủi ro qua hai cách: đặt hạn mức và giảm độ nhạy bằng phái sinh hoặc chứng khoán hoá [[src-choudhry-principles-banking#^choudhry-st-5]].

**Quản trị.**
- Stress Testing Policy do Executive Risk Committee sở hữu, gồm cả Reverse Stress Testing Policy; ALCO chịu trách nhiệm stress test rủi ro bảng cân đối theo cách tiếp cận "flight simulator" [[src-choudhry-principles-banking#^choudhry-rmf-7]].
- Liquidity Contingency Plan và Recovery Plan mở rộng mức stress từ "severe, but plausible" tới "extreme" dưới dạng reverse stress [[src-choudhry-principles-banking#^choudhry-rmf-10]].

**Với IRRBB.**
- Ví dụ độ nhạy banking book: thay đổi NIM khi lãi suất dịch song song +200bp; sổ "liability sensitive" mất thu nhập khi lãi suất tăng [[src-choudhry-principles-banking#^choudhry-st-3]]. Với ALM desk, chỉ số then chốt được stress là funding gap [[src-choudhry-principles-banking#^choudhry-st-4]].
- Table 20.2 (EUR, PV toàn danh mục Treasury): +200bp giảm 1.825.729, −200bp tăng 621.937; danh mục money market nhạy với lãi suất tăng [[src-choudhry-principles-banking#^choudhry-st-16]]. Xem [[irrbb-management]].

**Stress test suy thoái kinh tế và thanh khoản (Choudhry, T4).**
- Stress test suy thoái kinh tế đánh giá khả năng tồn tại như going concern qua tác động lên P&L, vốn quy định và thanh khoản [[src-choudhry-principles-banking#^choudhry-st-17]].
- Ví dụ: CAR giảm từ 17,98% xuống 14,66% ở iteration 2, dưới mức tối thiểu 15% của ngân hàng này; kết luận là nên tăng vốn bằng cổ phần hoặc contingent capital ([[contingent-convertible-bond]]), quyết định thuộc Board [[src-choudhry-principles-banking#^choudhry-st-18]]. Xem [[capital-plan]].
- Liquidity stress test có output chính là cash flow survival report [[src-choudhry-principles-banking#^choudhry-st-19]]; xem [[cash-flow-survival-period]], [[ilaap]]. Báo cáo stress thanh khoản từng dòng nên lập hằng quý hoặc theo yêu cầu cơ quan quản lý [[src-choudhry-principles-banking#^choudhry-st-21]].
- Kịch bản ICAAP gồm kịch bản vĩ mô của PRA và kịch bản riêng; ngân hàng tự làm thì có xu hướng đánh giá thấp xác suất kết cục bất lợi [[src-choudhry-principles-banking#^choudhry-icaap-4]].

## Phụ thuộc regime
Không ghi nhận trong nguồn đã ingest.

## Góc nhìn theo domain
- **ALM (Bardaeva, T4)**: phơi nhiễm với quốc gia, ngành có thể bị khủng hoảng phi tài chính nên được theo dõi riêng; stress test nên có kịch bản cho các phơi nhiễm này [[src-bardaeva-alm#^ch16-7]]. P2G được xác định từ tác động stress test [[src-bardaeva-alm#^ch13-13]]. Xem [[srep]], [[recovery-and-resolution-planning]].
- **VN**: khung chung tại TT83/2025 Đ23, hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]]; riêng kiểm tra sức chịu đựng tín dụng, thị trường chậm nhất từ 01/01/2028 [[src-tt83-2025-nhnn#^d74-2]]. Với IRRBB, từ 01/07/2026 đến 31/12/2027 ngân hàng được kiểm tra sức chịu đựng theo ΔNII hoặc ΔEVE [[src-tt83-2025-nhnn#^d74-4a]]. Áp dụng sớm việc kiểm tra theo cả ΔNII và ΔEVE (Đ74.4.b) hoặc kiểm tra tín dụng, thị trường trước 01/01/2028 phải thông báo NHNN trong 10 ngày [[src-tt83-2025-nhnn#^d74-5]].
- **Basel**: kịch bản sốc IRRBB chuẩn hoá xem [[standardised-interest-rate-shocks]]; kịch bản thanh khoản 30 ngày xem [[lcr]].
- **ALM**: *Diễn giải:* IRRBB và thanh khoản là hai loại stress test tần suất hằng quý, cùng nằm trong trách nhiệm kiểm soát hạn mức của bộ phận ALM [[src-tt83-2025-nhnn#^d25-3]]. Vì vậy hai bộ kịch bản nên dùng chung đường cong lãi suất và giả định hành vi tiền gửi.

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
