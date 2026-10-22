---
title: "Maturity Transformation"
aliases: [Maturity Transformation, Chuyển hoá kỳ hạn, Chuyển đổi kỳ hạn, Term transformation]
type: concept
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-bardaeva-alm]]"]
relations:
  - {type: exposed-to, to: "[[gap-risk]]", cite: "[[src-choudhry-principles-banking#^choudhry-hedge-1]]"}
  - {type: priced-by, to: "[[liquidity-transfer-pricing]]", cite: "[[src-choudhry-principles-banking#^choudhry-ftp-15]]"}
  - {type: exposed-to, to: "[[structural-liquidity-risk]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u05-6]]"}
tags: [maturity-transformation, ftp, gap-risk, liquidity-risk, nii]
updated: 2026-10-22
reviewed:
---

## Ý chính
Maturity transformation là việc tạo lợi nhuận có rủi ro từ chênh lệch, có chủ đích hoặc không, trong cấu trúc kỳ hạn của tài sản và nợ [[src-choudhry-principles-banking#^choudhry-ftp-1]]. Lubinska mô tả cùng hiện tượng từ phía thanh khoản: kỳ cam kết vốn phía tài sản dài hơn phía nợ, và gọi đây là một chức năng cơ bản của ngân hàng [[src-lubinska-alm-optimisation#^lubinska-u01-21]].

Hệ quả là ngân hàng chịu đồng thời hai loại rủi ro. Ngân hàng tài trợ khoản đầu tư bằng nợ có kỳ hạn ngắn hơn, nên chịu cả rủi ro lãi suất và rủi ro thanh khoản [[src-lubinska-alm-optimisation#^lubinska-u02-18]]. Xem [[gap-risk]], [[liquidity-risk-management]].

## Cơ chế & drivers
**Hình thái theo đường cong lãi suất.**

| Đường cong | Vị thế điển hình | Rủi ro | Nguồn |
|---|---|---|---|
| Dốc lên | Huy động ở đầu ngắn, cho vay ở đầu dài; Choudhry gọi đây là "định nghĩa của ngân hàng" | Phần "tail" là interest-rate gap; lãi suất ngắn tăng có thể làm biên thu hẹp hoặc thành lỗ funding | [[src-choudhry-principles-banking#^choudhry-hedge-1]] |
| Đảo ngược | Cho vay ngắn, huy động dài ("funding long") | [cần nguồn] | [[src-choudhry-principles-banking#^choudhry-hedge-2]] |

**FTP tách maturity transformation khỏi customer franchise.**
- Hệ thống FTP là ranh giới giữa maturity transformation và customer franchise [[src-choudhry-principles-banking#^choudhry-ftp-3]]. Choudhry gọi việc tách maturity transformation "rủi ro" khỏi customer franchise "phi rủi ro" là một hệ quả quan trọng của FTP [[src-choudhry-principles-banking#^choudhry-ftp-13]]. Xem [[funds-transfer-pricing]].
- Qua FTP, maturity transformation do ALM quản lý và tạo lợi nhuận cho ngân hàng. Trong ví dụ của Lubinska, asset centre lãi 2,69%, liability centre lỗ 0,68%, ALM lãi 0,99% [[src-lubinska-alm-optimisation#^lubinska-u01-16]].
- Đơn vị kinh doanh tạo ra tài sản gây áp lực thanh khoản vì nghiệp vụ ngân hàng gồm maturity transformation. Chi phí tìm nguồn thanh khoản đó phải do đơn vị kinh doanh chịu qua phí FTP [[src-choudhry-principles-banking#^choudhry-ftp-15]]. Xem [[liquidity-transfer-pricing]].

**Điều hành.**
- Strategic plan luôn cần quản trị vững hai lĩnh vực lõi: vốn, và mismatch funding (thanh khoản), vì maturity transformation là thành phần cơ bản của ngân hàng [[src-choudhry-principles-banking#^choudhry-strat-12]].
- Theo Bardaeva, ALM điều hành maturity transformation bằng phòng ngừa rủi ro lãi suất hoặc thay đổi cấu trúc bảng cân đối, trong phần phân tích khả năng sinh lời 12 tháng và tối thiểu 3 năm của mô hình kinh doanh [[src-bardaeva-alm#^ch13-5]].

*Diễn giải:* lợi nhuận từ maturity transformation là phần NII còn lại sau khi trừ biên thương mại của tài sản và nợ theo FTP. Phần này nhạy với hình dạng đường cong, còn biên thương mại được cố định tại thời điểm giao dịch. Xem [[net-interest-margin]].

## Phụ thuộc regime
- **Đường cong dốc lên và lãi suất ngắn tăng:** biên của vị thế funding short thu hẹp [[src-choudhry-principles-banking#^choudhry-hedge-1]].
- **Đường cong đảo ngược:** ngân hàng chuyển sang funding long [[src-choudhry-principles-banking#^choudhry-hedge-2]].
- **Khủng hoảng:** để khuyến khích huy động và hạn chế cho vay, đường cong FTP phải được định giá lại hoặc áp steering margin. Điều chỉnh độ dốc đường cong FTP giúp quản lý tác động bất lợi của kết quả chuyển hoá kỳ hạn lên NII [[src-bardaeva-alm#^ch15-8]].

## Góc nhìn theo domain
- **ALM**: maturity transformation là nguồn của cả [[gap-risk]] [[src-choudhry-principles-banking#^choudhry-hedge-1]] và refinancing risk [[src-lubinska-alm-optimisation#^lubinska-u01-21]].
- **Basel / VN**: chưa có nguồn chuẩn BCBS hay văn bản NHNN trong wiki định nghĩa maturity transformation [cần nguồn]. *Diễn giải:* NSFR và các hạn mức chênh lệch kỳ hạn là công cụ giới hạn mức chuyển hoá kỳ hạn, nhưng nguồn đã ingest không nói trực tiếp như vậy.

## Bằng chứng thực nghiệm
- **Memmel (2011), qua Lubinska:** mẫu 1.562 ngân hàng Đức từ 9/2005 đến 12/2009. Mức chịu rủi ro lãi suất đi theo lợi nhuận kỳ vọng từ term transformation, nhưng phụ thuộc mạnh vào quy mô và đặc thù ngân hàng [[src-lubinska-alm-optimisation#^lubinska-u02-15]].
- **Baldan, Zen và Rebonato, qua Lubinska:** đặt giả thuyết giảm phơi nhiễm rủi ro thanh khoản thì cũng giảm rủi ro lãi suất [[src-lubinska-alm-optimisation#^lubinska-u02-18]].
- Cả hai nghiên cứu đều lấy qua nguồn T4, chưa đối chiếu bản gốc.

## Câu hỏi mở
- **Liquidity transformation** [cần nguồn]: chưa có source note nào định nghĩa, nên chưa so sánh được với maturity transformation.
- **Quan hệ với [[liquidity-cost-risk]]:** Lubinska gắn maturity transformation với refinancing risk [[src-lubinska-alm-optimisation#^lubinska-u01-21]], còn liquidity cost risk là rủi ro khác. Chưa có claim nói maturity transformation tạo liquidity cost risk, nên chưa khai cạnh.
- Wiki chưa có node riêng cho liquidity risk (refinancing risk), nên chưa khai được cạnh `exposed-to` phía thanh khoản.
- Rủi ro của vị thế funding long khi đường cong đảo ngược chưa có nguồn.
