---
title: "ICAAP"
aliases: [ICAAP, Internal Capital Adequacy Assessment Process, Đánh giá nội bộ về mức đủ vốn]
type: concept
domains: [alm, vn-reg, basel]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-bcbs-framework]]", "[[src-bcbs-irrbb-2016]]", "[[src-lubinska-alm-optimisation]]", "[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: input-to, to: "[[risk-limits]]", cite: "[[src-tt83-2025-nhnn#^d61-1]]"}
tags: [capital, icaap, internal-control]
updated: 2026-10-20
reviewed:
---

## Ý chính
Đánh giá nội bộ về mức đủ vốn (ICAAP) là quy trình ngân hàng tự xác định lượng vốn cần cho các rủi ro trọng yếu theo kế hoạch kinh doanh, kể cả trong kịch bản bất lợi. Theo [[tt83-2025]], ICAAP phải bảo đảm [[src-tt83-2025-nhnn#^d59-1]]:
- tuân thủ quy định về tỷ lệ an toàn vốn ([[capital-adequacy-ratio]]);
- duy trì tỷ lệ an toàn vốn mục tiêu ở cả kịch bản bình thường lẫn kịch bản bất lợi;
- phù hợp với [[risk-appetite]];
- làm cơ sở cho kế hoạch kinh doanh.

ICAAP thực hiện tối thiểu hằng năm và đột xuất [[src-tt83-2025-nhnn#^d59-1]]. Ngân hàng thương mại được kiểm soát đặc biệt không phải thực hiện ICAAP (Mục 9 Chương III) [[src-tt83-2025-nhnn#^d1-1]].

Ở ngân hàng thương mại, Tổng giám đốc (Giám đốc) có trách nhiệm tổ chức thực hiện ICAAP [[src-tt83-2025-nhnn#^d25-2b]]. **Hội đồng quản lý vốn** tham mưu Tổng giám đốc về ICAAP. Chủ tịch là Tổng giám đốc hoặc người điều hành chuyên trách tài chính; họp tối thiểu 6 tháng một lần [[src-tt83-2025-nhnn#^d6-4c]]. Xem [[alco]].

## Cơ chế & drivers
**Sáu bước, cho kỳ 3–5 năm tới** [[src-tt83-2025-nhnn#^d59-2]]:

| Bước | Nội dung | Nguồn |
|---|---|---|
| 1 | Đo lường rủi ro trọng yếu, xác định [[economic-capital]] theo kế hoạch kinh doanh (Phụ lục VI) | [[src-tt83-2025-nhnn#^d59-2]] |
| 2 | Kiểm tra sức chịu đựng về vốn: tài sản có rủi ro và vốn kinh tế trong kịch bản bất lợi | [[src-tt83-2025-nhnn#^d59-2]] |
| 3 | Xác định [[target-capital]], [[projected-own-funds]] (Phụ lục VI) | [[src-tt83-2025-nhnn#^d59-2]] |
| 4 | Lập [[capital-plan]] | [[src-tt83-2025-nhnn#^d59-2]] |
| 5 | Giám sát mức đủ vốn theo vốn mục tiêu, điều chỉnh kế hoạch vốn khi cần | [[src-tt83-2025-nhnn#^d59-2]] |
| 6 | Rà soát quy trình | [[src-tt83-2025-nhnn#^d59-2]] |

**Kiểm tra sức chịu đựng về vốn** [[src-tt83-2025-nhnn#^d60-1]]:
- 2 kịch bản (bình thường và bất lợi); giả định tối thiểu về lãi suất, tỷ giá, giá vàng, chất lượng tín dụng;
- tính tác động lên tài sản có rủi ro theo từng loại rủi ro và lên tỷ lệ an toàn vốn.

Ma trận giả định – rủi ro chịu tác động:

| Giả định | Tài sản tính theo rủi ro chịu tác động | Nguồn |
|---|---|---|
| Lãi suất | Rủi ro hoạt động ([[operational-risk-management]]); rủi ro thị trường (lãi suất, xem [[market-risk-management]]); IRRBB | [[src-tt83-2025-nhnn#^d60-1]] |
| Tỷ giá, giá vàng | Rủi ro hoạt động; rủi ro thị trường (ngoại hối, vàng) | [[src-tt83-2025-nhnn#^d60-1]] |
| Chất lượng tín dụng | Rủi ro hoạt động; rủi ro tín dụng (xem [[credit-risk-management]]); rủi ro tập trung | [[src-tt83-2025-nhnn#^d60-1]] |

Giả định và phương pháp phải được rà soát mức độ phù hợp [[src-tt83-2025-nhnn#^d60-2]]. Tần suất: tối thiểu hằng năm và khi có sự kiện có thể tác động nghiêm trọng tới mức đủ vốn [[src-tt83-2025-nhnn#^d23-5]]. Kết quả dùng để tính vốn kinh tế, từ đó xác định vốn mục tiêu [[src-tt83-2025-nhnn#^d23-6]]. Phần RWA tăng thêm ở kịch bản bất lợi ($\Delta RWA_B$) đi vào công thức vốn kinh tế [[src-tt83-2025-nhnn#^pl6-1a]]; $RWA_{IRRBB}$ tính theo ΔEVE chậm nhất từ 01/01/2028 [[src-tt83-2025-nhnn#^pl6-1c]] ([[rwa-irrbb]]). Khung chung: [[stress-testing]].

**Rà soát độc lập.** Quy trình ICAAP được rà soát tối thiểu hằng năm bởi một bộ phận độc lập với bộ phận xây dựng và thực hiện. Nội dung rà soát gồm [[src-tt83-2025-nhnn#^d62-1]]:
- sự phù hợp giữa khẩu vị rủi ro và kế hoạch kinh doanh;
- sự phù hợp giữa tài sản tính theo rủi ro và hạn mức;
- dữ liệu đầu vào;
- giả định stress test vốn;
- tính khả thi của phương án tăng vốn.

**Báo cáo gửi NHNN.** Ngân hàng lập báo cáo hằng năm về ICAAP theo Phụ lục III [[src-tt83-2025-nhnn#^d9-2c]], gửi trong 90 ngày kể từ ngày kết thúc năm tài chính [[src-tt83-2025-nhnn#^d9-3a]]. Cấu trúc báo cáo:

| Mục PL3 | Nội dung | Nguồn |
|---|---|---|
| 1 | Tuân thủ tỷ lệ an toàn vốn theo NHNN và thực hiện tỷ lệ an toàn vốn mục tiêu năm $t_0$ | [[src-tt83-2025-nhnn#^pl3-1]] |
| 2 | Hoạt động trọng yếu, rủi ro trọng yếu; khẩu vị rủi ro năm $t_0$ đến $t_0+3$: $CAR_{target}$, ROE, RAROC | [[src-tt83-2025-nhnn#^pl3-2]] |
| 3.a | Bảng vốn mục tiêu $t_0$ đến $t_0+3$: $C_R$, $RWA^*_E$ theo 6 cấu phần, $C_E$, $C_{Target}$, chênh lệch $C_A - C_{Target}$ | [[src-tt83-2025-nhnn#^pl3-3a]] |
| 3.b | Thuyết minh phương pháp xác định từng RWA và $\Delta RWA_B$: mô tả, điểm mạnh, hạn chế, điều chỉnh trong kỳ | [[src-tt83-2025-nhnn#^pl3-3b]] |
| 4 | Stress test vốn: giả định bất lợi, phương pháp tính tác động lên RWA từng loại rủi ro, RWA ở hai kịch bản | [[src-tt83-2025-nhnn#^pl3-4]] |
| 5–6 | Kế hoạch vốn (phương án tăng vốn, cổ tức, phân bổ vốn, cảnh báo sớm); kết quả rà soát ICAAP và kiến nghị | [[src-tt83-2025-nhnn#^pl3-5]] |

*Diễn giải:* bảng PL3 có 4 cột năm ($t_0$ đến $t_0+3$) [[src-tt83-2025-nhnn#^pl3-3a]], nằm trong kỳ 3–5 năm của Đ59.2 [[src-tt83-2025-nhnn#^d59-2]].

**Báo cáo nội bộ.** Lập hằng năm, gồm vốn mục tiêu, vốn kinh tế, kết quả stress test vốn, kế hoạch vốn, kết quả phân bổ vốn [[src-tt83-2025-nhnn#^d63-1]].

## Phụ thuộc regime
Không ghi nhận trong nguồn đã ingest.

## Góc nhìn theo domain
- **Basel (SRP30, Pillar 2)**:
  - ICAAP nên làm trên cơ sở hợp nhất, và ở cấp pháp nhân của từng ngân hàng trong tập đoàn khi cơ quan giám sát thấy cần. ICAAP nên gồm stress testing để bổ trợ và kiểm chứng các phương pháp định lượng, định tính khác [[src-bcbs-framework#^srp30-2]].
  - ICAAP là quy trình do ngân hàng dẫn dắt, dựa trên quy trình quản trị rủi ro nội bộ. Một ICAAP có thể dùng cho cả mục đích nội bộ và giám sát [[src-bcbs-framework#^srp30-2c]].
  - ICAAP nên xét nhu cầu vốn ngắn hạn và dài hạn, cân nhắc tích luỹ vốn dư trong giai đoạn thuận lợi của chu kỳ tín dụng. Ngân hàng nên phân tích khả năng hấp thụ lỗ của công cụ vốn khi stress [[src-bcbs-framework#^srp30-2b]].
  - Chênh lệch giữa ICAAP và đánh giá Pillar 2 của cơ quan giám sát nên dẫn tới đối thoại tương xứng với mức chênh lệch [[src-bcbs-framework#^srp30-2b]].
  - Pillar 1 là mức tối thiểu. Mọi rủi ro nội bảng và ngoại bảng nên được phủ đủ vốn, kể cả qua Pillar 2 vượt mức Pillar 1 [[src-bcbs-framework#^srp30-3]]. Các yếu tố Pillar 1 không bao quát hết (tập trung, chứng khoán hoá, ngoại bảng, định giá) nên được đưa vào ICAAP [[src-bcbs-framework#^srp30-5]] [[src-bcbs-framework#^srp30-6]].
  - Mức vốn cho rủi ro tập trung nên có trong ICAAP và đánh giá Pillar 2. Đánh giá không máy móc mà theo điểm yếu riêng của mô hình kinh doanh [[src-bcbs-framework#^srp30-27]]. Xem [[concentration-risk-management]].
  - [[reputational-risk]] nên được xử lý trong ICAAP và kế hoạch dự phòng thanh khoản [[src-bcbs-framework#^srp30-30]].
  - *Diễn giải:* TT83/2025 có các yếu tố tương ứng: stress test vốn [[src-tt83-2025-nhnn#^d60-1]] và rủi ro tập trung trong RWA của vốn kinh tế [[src-tt83-2025-nhnn#^d60-1]]. Phần đã ingest của TT83 không nêu yêu cầu ICAAP ở cấp pháp nhân trong tập đoàn, cũng không nêu cơ chế đối thoại khi ICAAP lệch đánh giá của NHNN.
- **Basel (IRRBB)**:
  - d368 Nguyên tắc 9 yêu cầu mức đủ vốn cho IRRBB phải được xét cụ thể trong ICAAP do governing body phê duyệt, phù hợp khẩu vị rủi ro IRRBB [[src-bcbs-irrbb-2016#^irrbb-p09-1]].
  - Vốn cho IRRBB xét theo rủi ro giá trị kinh tế. Với rủi ro thu nhập tương lai, ngân hàng nên xét capital buffers [[src-bcbs-irrbb-2016#^irrbb-p09-2]].
- **EU (EBA GL 2018, qua nguồn T4)**: trước chuẩn BCBS, vốn nội bộ cho IRRBB thường dựa trên VaR; GL EBA 19/7/2018 yêu cầu đóng góp của IRRBB vào vốn nội bộ xét cả ΔEVE dưới nhiều kịch bản và đệm theo ΔNII [[src-lubinska-alm-optimisation#^lubinska-u02-49]]. Khi đánh giá phải xét: vốn cho rủi ro giá trị kinh tế và nhu cầu vốn từ tác động lên thu nhập tương lai; quy mô, kỳ hạn hạn mức IRRBB và việc hạn mức có bị chạm khi tính vốn; hiệu quả và chi phí phòng ngừa vị thế mở; độ nhạy với giả định mô hình; basis risk; động lực rủi ro nền [[src-lubinska-alm-optimisation#^lubinska-u02-50]].
- **Basel II/III (nguồn T4)**: ICAAP là một phần của Trụ cột 2 ([[srep]]), là tự đánh giá rủi ro ngoài Trụ cột 1 [[src-lubinska-alm-optimisation#^lubinska-u02-4]].
- **EU SREP (Bardaeva, T4)**: P2R lấy tính toán ICAAP theo từng rủi ro làm điểm xuất phát. Với phần lớn ngân hàng, cơ quan quản lý không lấy y nguyên ICAAP vì không coi là đáng tin cậy, mà dùng thêm benchmark giám sát [[src-bardaeva-alm#^ch13-8]]. Bardaeva cũng nêu mức đủ vốn cho IRRBB phải được xét riêng trong ICAAP [[src-bardaeva-alm#^ch11-19]]. Xem [[irrbb-management]].
- **Độ tin cậy (Bardaeva, T4)**: cơ quan giám sát đánh giá tính toán ICAAP theo bốn tiêu chí: granularity (chia theo loại rủi ro), credibility (tương quan và cấu trúc danh mục thực tế, mô hình được công nhận, giả định thận trọng), understandability (driver nêu rõ), comparability (so sánh được với ngân hàng cùng nhóm và benchmark giám sát) [[src-bardaeva-alm#^ch13-9]].
- **Normative và economic perspective (ECB 11/2018, qua nguồn T4)**: cách tiếp cận tuân thủ tỷ lệ quy định (normative perspective) không còn được coi là đủ và phải liên kết với economic perspective [[src-bardaeva-alm#^ch16-1]]. ALM nên xét dòng ra thanh khoản và tổn thất vốn trong kịch bản xấu nhất mà normative perspective không phản ánh [[src-bardaeva-alm#^ch16-2]]. IRRBB mang bản chất kinh tế này vì xét EVE trên toàn vòng đời [[src-bardaeva-alm#^ch16-3]].
- **VN**: TT83/2025 đưa IRRBB vào ICAAP qua giả định lãi suất trong stress test vốn: tác động lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]. Hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]].
- **ALM**:
  - Bộ phận ALM kiểm soát hoạt động kinh doanh tuân thủ tổng tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d25-3]].
  - *Diễn giải:* phần vốn mục tiêu phân bổ cho IRRBB [[src-tt83-2025-nhnn#^d61-1]] là ngân sách rủi ro mà hạn mức ΔEVE và ΔNII của ALM phải nằm trong đó.
- **Tích hợp (Choudhry, T4)**: ICAAP, ILAAP, recovery planning và resolution planning được làm tích hợp trong cùng RMF; capital contingency plan (CaCP) liệt kê mọi KRI và hành động quản lý vốn [[src-choudhry-principles-banking#^choudhry-rmf-9]]. Risk Taxonomy là đầu vào của quy trình đánh giá vốn và thanh khoản [[src-choudhry-principles-banking#^choudhry-rmf-3]]. Mọi cơ quan quản lý quốc gia yêu cầu quy trình đánh giá mức đủ vốn hằng năm [[src-choudhry-principles-banking#^choudhry-st-2]].
- **UK/PRA (Choudhry, T4)**:
  - ICAAP thuộc trách nhiệm cơ quan quản trị, gồm stress testing và phân tích kịch bản, cập nhật ít nhất hằng năm [[src-choudhry-principles-banking#^choudhry-icaap-1]]. Ở tổ chức lớn quy trình mất khoảng 8–12 tháng; ICAAP không được coi là thủ tục tuân thủ [[src-choudhry-principles-banking#^choudhry-icaap-10]].
  - Trình tự: chốt một ngày bảng cân đối gốc cho mọi mô hình [[src-choudhry-principles-banking#^choudhry-icaap-2]]; nhận diện rủi ro qua Risk Register, rủi ro không trọng yếu vẫn ghi lại kèm lý do [[src-choudhry-principles-banking#^choudhry-icaap-3]]; kịch bản gồm kịch bản vĩ mô PRA và kịch bản riêng của ngân hàng, nghiêm trọng nhưng hợp lý [[src-choudhry-principles-banking#^choudhry-icaap-4]]; vốn sau stress dưới tỷ lệ tối thiểu thì xét biện pháp như phòng ngừa, cắt hoạt động rủi ro, rút khỏi mảng kinh doanh [[src-choudhry-principles-banking#^choudhry-icaap-5]].
  - Mục lục mẫu có so sánh với risk-bearing capacity, [[reverse-stress-testing]], phân bổ vốn và use test [[src-choudhry-principles-banking#^choudhry-icaap-6]]. Use test đạt được khi output ICAAP đi vào hạn mức rủi ro, định giá hoặc phân bổ vốn [[src-choudhry-principles-banking#^choudhry-icaap-14]].
  - Management actions phải được rà lại theo từng kịch bản; bán danh mục trading không làm được trong khủng hoảng 2007–2008 [[src-choudhry-principles-banking#^choudhry-icaap-12]].
  - Một chủ sở hữu ICAAP duy nhất (Risk, Treasury hoặc Finance); senior management và Board review, challenge và sign-off [[src-choudhry-principles-banking#^choudhry-icaap-13]].
  - Sau SREP, PRA đưa Individual Capital Guidance (Pillar 2A) và có thể đưa buffer Pillar 2B [[src-choudhry-principles-banking#^choudhry-icaap-9]]. Xem [[srep]].
  - Ở US, CCAR gồm cả Recovery and Resolution Planning; ở UK, RRP tách khỏi ICAAP [[src-choudhry-principles-banking#^choudhry-icaap-16]]. Cặp tương ứng phía thanh khoản là [[ilaap]].

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Không còn câu hỏi mở từ nguồn đã ingest.
