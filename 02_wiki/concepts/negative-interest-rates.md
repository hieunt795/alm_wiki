---
title: "Negative Interest Rates"
aliases: [Negative Interest Rates, Lãi suất âm, NIRP, ZIRP, Sàn lãi suất 0%, Zero floor]
type: concept
domains: [alm, macro]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: drives, to: "[[non-maturity-deposits]]", direction: "+", cite: "[[src-tata-bank-alm#^tata-neg-4]]"}
tags: [negative-rates, zero-floor, coupon-floor, indicator-floor, rigid-deposits, embedded-options]
updated: 2026-10-19
reviewed:
---

## Ý chính
Ngày 5/6/2014, ECB hạ lãi suất deposit facility xuống −0,10%. Giai đoạn khoảng tám năm sau đó thường được gọi là ZIRP/NIRP. Trước giai đoạn này, giả định mô hình phần lớn coi lãi suất bị chặn dưới ở 0, ví dụ giả định phân phối log-normal [[src-tata-bank-alm#^tata-neg-1]].

Với ALM, vấn đề chính là **sàn 0% trên tiền gửi bán lẻ**. Luật bảo vệ người tiêu dùng có thể cấm áp lãi suất âm cho người gửi bán lẻ, hoặc việc này không thực tế về quan hệ khách hàng. Khi đó lãi suất thực trả là $\max(r_I \pm x;\ 0\%)$ thay vì $r_I \pm x$ [[src-tata-bank-alm#^tata-neg-2]].

## Cơ chế & drivers
**Sàn 0% là quyền chọn nhúng.** Sàn 0% gần như không có giá trị khi lãi suất cao, nhưng at the money hoặc in the money khi lãi suất thấp hay âm. Khả năng khách hàng chống lại lãi suất âm là một ví dụ về quyền chọn nhúng hay quyền chọn hành vi [[src-tata-bank-alm#^tata-neg-2]]. Xem [[option-risk]], [[behavioural-options]], [[interest-rate-cap-floor]].

**Hai loại sàn** [[src-tata-bank-alm#^tata-neg-3]]:

| Loại | Lãi suất khách hàng | Biên $x$ | Ví dụ | Nguồn |
|---|---|---|---|---|
| Coupon floor | $\max(r_I + x;\ 0\%)$ | Có thể mất | Tài khoản tiết kiệm bán lẻ | [[src-tata-bank-alm#^tata-neg-3]] |
| Indicator floor | $\max(r_I;\ 0\%) + x$ | Được bảo vệ | Khoản vay doanh nghiệp có điều khoản tương ứng | [[src-tata-bank-alm#^tata-neg-3]] |

Coupon floor bất lợi cho phía nợ phải trả, vì ngân hàng không thể áp lãi âm lên tiền gửi. Ngược lại, nó có lợi cho phía tài sản [[src-tata-bank-alm#^tata-neg-3]]. Ghép hai phía lại:
- indicator floor ở tài sản và coupon floor ở nợ: lãi suất âm có lợi, nếu các yếu tố khác không đổi;
- coupon floor ở tài sản và indicator floor ở nợ: lãi suất âm gây lỗ tiềm năng [[src-tata-bank-alm#^tata-neg-3]].

**Giao dịch định chế.** Lãi suất âm gần như không gây vấn đề trong giao dịch định chế như IRS liên ngân hàng hay repo. Lãi suất chỉ số âm cũng không nhất thiết sinh dòng tiền âm, vì dòng tiền thường bằng chỉ số cộng spread [[src-tata-bank-alm#^tata-neg-2]].

**Chính sách sản phẩm trước khi phát sinh (Choudhry).** Khi lãi suất âm, kỷ luật ALM vẫn là quản lý rủi ro thanh khoản, rủi ro lãi suất và giữ [[net-interest-margin|NIM]]. Các điểm cần xử lý trong chính sách [[src-choudhry-principles-banking#^choudhry-neg-2]]:
- hợp đồng vay thả nổi nên ghi rõ lãi suất có sàn 0,00% [[src-choudhry-principles-banking#^choudhry-neg-2]];
- điều khoản tiền gửi nên được rà soát cho nhóm khách hàng không bao giờ chịu lãi âm. Ở eurozone, lãi suất tiền gửi bán lẻ phần lớn có sàn 0,00%, trong khi một số khách hàng private banking và doanh nghiệp có thể chịu lãi âm [[src-choudhry-principles-banking#^choudhry-neg-2]];
- với tài khoản thanh toán và tiền gửi operational, ngân hàng có thể thu phí vận hành để bù lãi âm mà chính ngân hàng chịu khi gửi tại NHTW.

**Xử lý NMD và hedging (Choudhry)** [[src-choudhry-principles-banking#^choudhry-neg-3]]:
- tiền gửi doanh nghiệp lớn và một số tiền gửi bán lẻ số dư lớn: ngân hàng có thể chuyển lãi âm sang khách hàng;
- tiền gửi bán lẻ và SME thường có sàn 0,00%, nên được coi như sản phẩm "fixed-rate" [[src-choudhry-principles-banking#^choudhry-neg-3]];
- coi NMD là fixed-rate thì có thể vào IRS nhận cố định, trả thả nổi, với tenor IRS bằng behavioural tenor của NMD. Xem [[non-maturity-deposits]], [[interest-rate-swap]];
- nếu có, IRS có thể là balance guarantee swap, tức notional điều chỉnh theo số dư NMD.

**Hành vi khách hàng khác (Choudhry)** [[src-choudhry-principles-banking#^choudhry-neg-4]]:
- huy động có kỳ hạn đắt hơn vì khách hàng ít động lực khoá tiền dài hạn; trả lãi dương để thu hút sẽ làm NIM giảm mạnh khi cả trái phiếu chính phủ dài hạn có lợi suất âm;
- khách hàng có xu hướng roll over khoản vay thay vì trả khi đáo hạn;
- cho mục đích IRR, khoản vay và tiền gửi thả nổi có thể xếp vào bucket 1 tháng [[src-choudhry-principles-banking#^choudhry-neg-4]].

**Rigid deposits.** Khi lãi suất âm, tiền gửi không kỳ hạn không chịu lãi âm trở thành tài sản hấp dẫn, và ngân hàng nhận dòng tiền gửi lớn. Nguồn gọi chúng là rigid deposits: tiền gửi có lãi suất không còn co giãn khi lãi suất thị trường xuống dưới 0 [[src-tata-bank-alm#^tata-neg-4]]. Xem [[non-maturity-deposits]].

## Phụ thuộc regime
- NIRP làm giảm biên trung gian, vì lợi suất tài sản giảm trong khi phần lớn chi phí vốn không đổi [[src-tata-bank-alm#^tata-neg-4]]. Xem [[nii-planning]].
- Nguồn ghi nhận ba cách ngân hàng phản ứng [[src-tata-bank-alm#^tata-neg-4]]:
  - ngân hàng phụ thuộc tiền gửi chuyển sang tài sản lợi suất cao hơn;
  - ngân hàng phụ thuộc NII tăng biên cho vay;
  - một số ngân hàng tìm thêm thu nhập phí.
- Ngân hàng tiết kiệm có tiền gửi không kỳ hạn lớn dễ gặp vấn đề khi lãi suất âm [[src-tata-bank-alm#^tata-prac-3]].
- Kỷ luật ALM không đổi về nguyên tắc khi lãi suất âm, nhưng hành vi khách hàng đổi. Tác động lớn nhất với ngân hàng không chuyển lãi âm sang số dư tiền gửi khách hàng [[src-choudhry-principles-banking#^choudhry-neg-5]].
- Dữ liệu hành vi của thời kỳ lãi suất âm không dùng để backtest cho thời kỳ lãi suất dương, và ngược lại [[src-tata-bank-alm#^tata-beh-2]]. Xem [[model-validation]].

## Góc nhìn theo domain
- **Basel/EU**: EBA yêu cầu ngân hàng, trong môi trường lãi suất thấp, xét các điểm sau [[src-tata-bank-alm#^tata-neg-5]]:
  - kịch bản lãi suất âm;
  - tác động bất đối xứng của lãi suất âm;
  - ràng buộc tái định giá tiền gửi bán lẻ, và ảnh hưởng của ràng buộc đó tới độ ổn định tiền gửi.

  Câu trích EBA này lấy qua nguồn T4.
- **ALM**: thách thức còn lại [[src-tata-bank-alm#^tata-neg-6]]:
  - dữ liệu lịch sử ngắn, khó hiệu chỉnh mô hình;
  - chưa có mô hình chuẩn;
  - chuyển từ EURIBOR sang RFR làm đổi chỉ số và spread, ảnh hưởng tới sàn;
  - hành vi người tiêu dùng chưa được hiểu hết;
  - ngân hàng có thể không thực thi sàn vì lý do danh tiếng.

  Nguồn kết luận rằng quản trị mô hình và rủi ro mô hình vẫn là trách nhiệm then chốt của ban điều hành [[src-tata-bank-alm#^tata-neg-6]].
- **VN**: phần TT83/2025 đã ingest không đề cập lãi suất âm hay sàn 0% [cần nguồn].

*Diễn giải:* trong khung chuẩn của d368, sàn lãi suất sau sốc là cơ chế giám sát áp lên kịch bản sốc. Sàn 0% trong node này là điều khoản hợp đồng hoặc ràng buộc pháp lý áp lên lãi suất khách hàng. Hai loại sàn khác nhau về bản chất, cần mô hình hoá riêng. Xem [[outlier-bank-test]].

## Bằng chứng thực nghiệm
- ECB áp lãi suất cơ bản âm từ tháng 6/2014. Ngày 6/7/2020, toàn bộ đường cong trái phiếu chính phủ Đức và đường cong EUR OIS nằm dưới 0,00%, tới kỳ hạn 30 và 40 năm [[src-choudhry-principles-banking#^choudhry-neg-1]].
- Ngân hàng nhận dòng tiền gửi không kỳ hạn lớn trong thời kỳ ZIRP/NIRP [[src-tata-bank-alm#^tata-neg-4]]. Ở Đức 1999–2021, tỷ trọng tiền gửi không kỳ hạn tăng từ 7,9% lên 29,3% [[src-tata-bank-alm#^tata-prac-1]].

## Câu hỏi mở
- Nguồn nói tiếp tục phải phân tích rủi ro lãi suất tăng đột ngột [[src-tata-bank-alm#^tata-neg-6]]. Xem [[silicon-valley-bank]].
- Quy định VN về lãi suất tiền gửi âm chưa có trong wiki [cần nguồn].
