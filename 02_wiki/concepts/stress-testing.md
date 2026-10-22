---
title: "Stress Testing"
aliases: [Stress Testing, Kiểm tra sức chịu đựng]
type: concept
domains: [alm, vn-reg, basel]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]", "[[src-bcbs-framework]]", "[[src-bcbs-irrbb-2016]]"]
relations: []
tags: [stress-test, governance, internal-control]
updated: 2026-10-22
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
- **Basel (SRP30, Pillar 2)**:
  - Stress testing là cấu phần của quản trị rủi ro và công cụ cốt lõi của giám sát. Kết quả chỉ ra nguồn lực tài chính có thể cần để hấp thụ tổn thất khi có cú sốc lớn [[src-bcbs-framework#^srp30-45]].
  - BCBS có bộ Stress testing principles (10/2018) và kỳ vọng ngân hàng hoạt động quốc tế lồng stress testing vào quản trị rủi ro [[src-bcbs-framework#^srp30-46]]. Nguyên tắc áp dụng tương xứng; ngân hàng nhỏ có thể dùng phương pháp đơn giản hơn khung chính thức [[src-bcbs-framework#^srp30-47]].
  - Ngân hàng nên stress testing liên tục để nhận diện tổn thất và nhu cầu thanh khoản khi bất lợi [[src-bcbs-framework#^srp30-5]]. ICAAP nên gồm stress testing [[src-bcbs-framework#^srp30-2]].
  - Stress test định kỳ nên gồm mọi tập trung rủi ro lớn [[src-bcbs-framework#^srp30-26]] và tính đến [[reputational-risk]] cùng hiệu ứng vòng hai [[src-bcbs-framework#^srp30-34]]. Kết quả stress test thanh khoản nên định hình [[contingency-funding-plan]] [[src-bcbs-framework#^srp30-51]].
  - *Diễn giải:* nguyên tắc tương xứng của SRP30.47 khác với TT83: TT83 Đ23.1 bắt buộc mọi ngân hàng kiểm tra tối thiểu bốn rủi ro trọng yếu và vốn [[src-tt83-2025-nhnn#^d23-1]], không có mức miễn cho ngân hàng nhỏ.
- **Basel (d368 Nguyên tắc 4, IRRBB)**:
  - Ngân hàng nên đo mức dễ tổn thất khi thị trường căng thẳng, kể cả khi giả định then chốt đổ vỡ, và dùng kết quả khi đặt, rà soát chính sách và hạn mức IRRBB [[src-bcbs-irrbb-2016#^irrbb-p04-5]].
  - Khung stress testing IRRBB nên làm đầu vào cho quyết định kế hoạch kinh doanh và kế hoạch vốn, và nên được xem xét trong [[icaap]] với stress test forward-looking có thể tác động tới vốn hoặc thu nhập qua thay đổi hành vi khách hàng [[src-bcbs-irrbb-2016#^irrbb-p04-6]].
  - Khung nên tương xứng với quy mô, độ phức tạp, gồm mục tiêu rõ, kịch bản phù hợp hoạt động, giả định có hồ sơ và phương pháp vững chắc [[src-bcbs-irrbb-2016#^irrbb-p04-7]]. Chọn kịch bản cần phối hợp traders, treasury, tài chính, [[alco]], quản lý rủi ro và chuyên gia kinh tế [[src-bcbs-irrbb-2016#^irrbb-p04-8]].
  - Dải kịch bản xác định theo từng đồng tiền, gồm kịch bản có yếu tố stress nghiêm trọng; trong môi trường lãi suất thấp nên xét lãi suất âm và tác động bất đối xứng [[src-bcbs-irrbb-2016#^irrbb-p04-9]]. Kịch bản nên đủ rộng để nhận diện [[gap-risk]] song song và phi song song, [[basis-risk]], [[option-risk]]; sốc tĩnh nhiều khi không đủ [[src-bcbs-irrbb-2016#^irrbb-p04-11]].
  - Yêu cầu cụ thể khi dựng kịch bản [[src-bcbs-irrbb-2016#^irrbb-p04-10]]:

    | Yêu cầu | Nguồn |
    |---|---|
    | Xem xét riêng công cụ, thị trường có tập trung vì khó thanh lý hoặc bù trừ khi căng thẳng | [[src-bcbs-irrbb-2016#^irrbb-p04-12]] |
    | Đánh giá tương tác IRRBB với credit risk, liquidity risk | [[src-bcbs-irrbb-2016#^irrbb-p04-13]] |
    | Đánh giá tác động lên NII khi spread của tài sản/nợ mới thay khoản đáo hạn biến động bất lợi | [[src-bcbs-irrbb-2016#^irrbb-p04-14]] |
    | Kịch bản thực hiện quyền chọn (cap/floor đã bán vào trạng thái in-the-money) và thay đổi volatility | [[src-bcbs-irrbb-2016#^irrbb-p04-15]] |
    | Chỉ rõ cấu trúc kỳ hạn và basis relationship giữa đường cong, chỉ số; ước lượng biến động lãi suất do ngân hàng quản lý (prime rate, tiền gửi bán lẻ) | [[src-bcbs-irrbb-2016#^irrbb-p04-16]] |
    | Kịch bản forward-looking phản ánh thay đổi cơ cấu danh mục, sản phẩm mới, rủi ro mới nổi | [[src-bcbs-irrbb-2016#^irrbb-p04-17]] |

  - Ngân hàng nên làm [[reverse-stress-testing]] định tính và định lượng cho IRRBB [[src-bcbs-irrbb-2016#^irrbb-p04-18]].
- **ALM**: *Diễn giải:* IRRBB và thanh khoản là hai loại stress test tần suất hằng quý, cùng nằm trong trách nhiệm kiểm soát hạn mức của bộ phận ALM [[src-tt83-2025-nhnn#^d25-3]]. Vì vậy hai bộ kịch bản nên dùng chung đường cong lãi suất và giả định hành vi tiền gửi.

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
