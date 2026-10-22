---
title: "Structural Liquidity Risk"
aliases: [Structural Liquidity Risk, Rủi ro thanh khoản cấu trúc, Structural funding risk]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-lubinska-alm-optimisation]]", "[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]", "[[src-bcbs-nsfr]]", "[[src-tt50-2026-nhnn]]"]
relations: []
tags: [liquidity, structural-funding, maturity-transformation, nsfr]
updated: 2026-10-22
reviewed:
---

## Ý chính
- Structural liquidity risk là nguy cơ tổn thất thực tế hoặc chi phí cơ hội khi ngân hàng không theo đuổi được chiến lược kinh doanh hay mục tiêu tăng trưởng, vì cơ cấu bảng cân đối dưới mức tối ưu [[src-lubinska-alm-optimisation#^lubinska-u05-6]].
- Lubinska đo rủi ro này bằng structural limit. Structural limit cho thấy mức [[maturity-transformation]] của ngân hàng, và đòi hỏi cơ cấu nguồn vốn ổn định tương ứng với cơ cấu bảng cân đối, qua đó giảm funding risk trong dài hạn [[src-lubinska-alm-optimisation#^lubinska-u05-6]].
- Phân biệt với các rủi ro gần nghĩa:
  - **Funding risk**: rủi ro ngân hàng không có nguồn vốn ổn định trung và dài hạn để trả nghĩa vụ khi đến hạn, hoặc chỉ trả được với chi phí quá cao [[src-lubinska-alm-optimisation#^lubinska-u05-16]]. Choudhry định nghĩa funding risk là rủi ro không huy động được vốn với giá hoặc kỳ hạn chấp nhận được, hoặc không tiếp cận thị trường kịp thời [[src-choudhry-principles-banking#^choudhry-rmf-12]].
  - **Rủi ro thanh khoản ngắn hạn**: Lubinska đo bằng survival horizon, tức số ngày ngân hàng sống sót trong stress thanh khoản cực đoan nhưng hợp lý, với horizon 30, 60 hoặc 90 ngày [[src-lubinska-alm-optimisation#^lubinska-u05-4]].
  - **[[liquidity-cost-risk]]**: rủi ro chi phí thanh khoản tăng mà ngân hàng không mất khả năng thanh toán.
- *Diễn giải:* structural liquidity risk nhìn vào cơ cấu bảng cân đối trên horizon trên 1 năm. Funding risk nhìn vào khả năng huy động và giá huy động. Structural limit là thước đo nối hai khái niệm: limit thấp nghĩa là cơ cấu đang dựa vào nguồn phải tái tài trợ, nên funding risk tương lai cao hơn.

## Cơ chế & drivers
- **Nguồn phát sinh.** Ngân hàng tài trợ tài sản bằng nợ có kỳ hạn ngắn hơn. Do đó ngân hàng nhận cả rủi ro lãi suất và rủi ro thanh khoản [[src-lubinska-alm-optimisation#^lubinska-u02-18]].
- **Vị trí trong khung rủi ro.** Bardaeva xếp structural maturity mismatch vào inherent funding risk, cùng với việc phụ thuộc vào một số nguồn funding cụ thể và thay đổi funding risk theo kế hoạch funding. Structural maturity mismatch nên được điều hành trong các structural liquidity limit nêu rõ trong chính sách [[src-bardaeva-alm#^ch13-16]].
- **Đo lường bằng structural limit.** Structural liquidity được đo bằng nhiều metric [[src-lubinska-alm-optimisation#^lubinska-u05-18]]. Structural limit dùng các thành phần sau:
  - dòng tiền vào phát sinh sau 1 năm [[src-lubinska-alm-optimisation#^lubinska-u05-18]];
  - dòng tiền ra phát sinh sau 1 năm [[src-lubinska-alm-optimisation#^lubinska-u05-18]];
  - vốn cấp 1, được coi là nguồn vốn ổn định [[src-lubinska-alm-optimisation#^lubinska-u05-18]];
  - ngưỡng do ngân hàng tự đặt để giới hạn mức chuyển hoá kỳ hạn [[src-lubinska-alm-optimisation#^lubinska-u05-18]].
  - Tỷ lệ này bảo đảm cân bằng cấu trúc giữa tài sản và nợ trên horizon sau 1 năm. Dòng tiền được xếp theo maturity ladder; khoản mục không có kỳ hạn hợp đồng được mô hình hoá bằng mô hình định lượng hoặc hành vi [[src-lubinska-alm-optimisation#^lubinska-u05-18]].
  - Mục tiêu là bảo đảm ngân hàng tài trợ hoạt động bằng nguồn đủ ổn định, để giảm rủi ro funding stress trong tương lai. Thông lệ thị trường tốt nhất đặt tỷ lệ này từ 100% trở lên [[src-lubinska-alm-optimisation#^lubinska-u05-17]].

*Diễn giải (tái dựng, chưa đối chiếu bản gốc):* công thức ở raw dòng 1949 bị mất khi convert. Từ lời văn của nguồn, có thể dựng lại như sau, với $TI$ là dòng tiền vào, $TO$ là dòng tiền ra và $n$ là ngưỡng nội bộ:

$$
\text{Structural limit} = \frac{TO_{T>1Y} + \text{Tier 1 capital}}{TI_{T>1Y}} \geq n
$$
*Diễn giải (tái dựng, chưa đối chiếu bản gốc):* tử số là nguồn ổn định (nợ trả sau 1 năm cộng vốn cấp 1), mẫu số là tài sản thu về sau 1 năm. Phần tổng quan của [[src-lubinska-alm-optimisation]] ghi tử số và mẫu số theo thứ tự ngược lại ($TI$ ở tử). Nguồn không có ví dụ số để kiểm.

- **Metric bổ trợ: A/D ratio.** A/D ratio bảo đảm ngân hàng chủ yếu được tài trợ bằng nguồn khách hàng và không phụ thuộc quá mức vào vốn bán buôn. Đây là phép kiểm đơn giản về structural integrity của bảng cân đối, với thông lệ tốt là ngưỡng dưới 80% [[src-lubinska-alm-optimisation#^lubinska-u05-7]]. Hạn chế là metric này không phân biệt chất lượng hay kỳ hạn của tiền gửi [[src-lubinska-alm-optimisation#^lubinska-u05-7]].
- **Nguyên tắc chiến lược funding** đi kèm khẩu vị funding risk [[src-lubinska-alm-optimisation#^lubinska-u05-16]]:
  - tài trợ tài sản khách hàng chủ yếu bằng nợ và tiền gửi khách hàng, để giảm phụ thuộc vào nguồn có thể mất khi stress, như vốn bán buôn;
  - đa dạng hoá nguồn khách hàng theo sản phẩm, kỳ hạn, vùng và ngành.
- **Góc nhìn tổ chức xếp hạng.** Fitch công bố năm tỷ lệ phản ánh structural funding strength:
  - customer loans / customer deposits;
  - customer loans / (customer deposits và short-term funding);
  - liquid assets / total assets;
  - liquid assets / wholesale funding;
  - wholesale funding / (total funding và capital) [[src-choudhry-principles-banking#^choudhry-peer-6]].

## Phụ thuộc regime
- **Lãi suất tăng**: ở Bank 1 của Lubinska, phần chi phí vốn tăng thêm khi lãi suất tăng được coi là chi phí tối thiểu để duy trì tuân thủ hạn mức nội bộ [[src-lubinska-alm-optimisation#^lubinska-u07-7]].
- **Khoản mục không kỳ hạn**: structural limit nội bộ phân bổ NMD theo kết quả phân tích hành vi [[src-lubinska-alm-optimisation#^lubinska-u05-17]]. Trong khi đó TT50 xếp tiền gửi không kỳ hạn vào cột "không kỳ hạn" của Bảng 9, với hệ số theo đối tác [[src-tt50-2026-nhnn#^pl2-a2-9]]. *Diễn giải:* hai thước đo vì vậy có thể cho kết luận khác nhau với cùng một bảng cân đối giàu CASA.

## Góc nhìn theo domain
- **Basel.** Choudhry ghi nhận Basel III đòi hỏi tuân thủ các structural liquidity metric, cùng với mục tiêu xây cấu trúc funding ổn định hơn, nhất là nguồn dài hạn chi phí cao [[src-choudhry-principles-banking#^choudhry-strat-13]]. BCBS yêu cầu NSFR duy trì cơ cấu tài trợ ổn định tương ứng với cơ cấu tài sản và hoạt động ngoại bảng, và hạn chế phụ thuộc quá mức vào vốn bán buôn ngắn hạn [[src-bcbs-nsfr#^nsf20-1]]. *Diễn giải:* nguồn không nói thẳng NSFR là thước đo của structural liquidity risk. Tuy vậy, định nghĩa NSFR dùng cùng ý "stable funding profile in relation to the composition" như structural limit của Lubinska. Điểm khác là NSFR dùng hệ số giám sát cố định trên giá trị ghi sổ, còn structural limit dùng dòng tiền sau 1 năm và mô hình hành vi nội bộ. Xem [[nsfr]].
- **VN.** TT50/2026 quy định NSFR = ASF / RSF × 100% [[src-tt50-2026-nhnn#^d22-1]], áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]], theo lộ trình ngưỡng riêng lẻ 90%, 95%, 100% [[src-tt50-2026-nhnn#^d22-2]]. Ngân hàng phải duy trì LDR tối đa 95% từ khi áp dụng LCR và NSFR [[src-tt50-2026-nhnn#^d12-6]]. *Diễn giải:* LDR là bản VN gần nhất của A/D ratio. Wiki chưa có nguồn NHNN yêu cầu hạn mức structural limit nội bộ [cần nguồn].
- **ALM.** *Diễn giải:* structural limit và NSFR là hai ràng buộc cấu trúc trong bài toán tối ưu bảng cân đối ([[balance-sheet-optimisation-model]]).

## Bằng chứng thực nghiệm
- Bank 1 của Lubinska (quy mô nhỏ):
  - Trước tối ưu: structural ratio 91,9%, tỷ lệ thanh khoản ngắn hạn tích luỹ 59,7% [[src-lubinska-alm-optimisation#^lubinska-u07-9]].
  - Sau tối ưu: structural ratio 93,9%, tỷ lệ thanh khoản ngắn hạn 100% [[src-lubinska-alm-optimisation#^lubinska-u07-10]].
  - Ngưỡng $n$ mà Bank 1 áp cho structural ratio không có trong claim đã ingest [cần nguồn].
- Baldan, Zen và Rebonato (dẫn trong Lubinska), nghiên cứu một ngân hàng nhỏ ở Ý giai đoạn 2009–2010: giảm rủi ro thanh khoản đi cùng giảm rủi ro lãi suất [[src-lubinska-alm-optimisation#^lubinska-u02-18]].

## Câu hỏi mở
- Công thức structural limit chưa đối chiếu được với bản gốc (raw dòng 1949 `formula-not-decoded`). Cần xem PDF của Lubinska Chapter 4 để chốt chiều tử số và mẫu số.
- NHNN có yêu cầu hạn mức thanh khoản cấu trúc nội bộ ngoài NSFR và LDR không, ví dụ trong TT83/2025 về quản trị rủi ro thanh khoản [cần nguồn].
