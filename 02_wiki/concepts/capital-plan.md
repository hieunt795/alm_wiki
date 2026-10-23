---
title: "Capital Plan"
aliases: [Capital Plan, Kế hoạch vốn, Capital Planning]
type: concept
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[icaap]]", cite: "[[src-tt83-2025-nhnn#^d59-2]]"}
  - {type: input-to, to: "[[risk-limits]]", cite: "[[src-tt83-2025-nhnn#^d61-1]]"}
  - {type: part-of, to: "[[bank-strategic-plan]]", cite: "[[src-choudhry-principles-banking#^choudhry-strat-10]]"}
tags: [capital, icaap, internal-control]
updated: 2026-10-19
reviewed:
---

## Ý chính
Kế hoạch vốn là bước thứ tư của [[icaap]] [[src-tt83-2025-nhnn#^d59-2]]. Nó trả lời ba câu hỏi:
- tăng vốn thế nào khi vốn tự có dự kiến ([[projected-own-funds]]) không đủ vốn mục tiêu;
- chia cổ tức tới đâu;
- vốn mục tiêu được phân bổ cho từng rủi ro trọng yếu ra sao [[src-tt83-2025-nhnn#^d61-1]].

## Cơ chế & drivers
**Nội dung tối thiểu** [[src-tt83-2025-nhnn#^d61-1]]:

| Cấu phần | Yêu cầu | Nguồn |
|---|---|---|
| Phương án tăng vốn | Nguồn tăng Vốn cấp 1, Vốn cấp 2 khả thi và hợp pháp; thời gian, lộ trình | [[src-tt83-2025-nhnn#^d61-1]] |
| Chính sách cổ tức | Sau khi chia cổ tức, lợi nhuận, vốn tự có dự kiến không thấp hơn vốn mục tiêu | [[src-tt83-2025-nhnn#^d61-1]] |
| Phân bổ vốn | Phân bổ vốn mục tiêu theo tài sản tính theo rủi ro cho các rủi ro trọng yếu, làm cơ sở xác định hạn mức rủi ro | [[src-tt83-2025-nhnn#^d61-1]] |
| Cảnh báo sớm | Mức cảnh báo sớm về tài sản tính theo rủi ro của từng rủi ro trọng yếu, so với phần được phân bổ | [[src-tt83-2025-nhnn#^d61-1]] |

**Chuẩn so sánh.** Vốn mục tiêu $C_{Target} = \max(C_R, C_E)$ [[src-tt83-2025-nhnn#^pl6-2]] được so với vốn tự có dự kiến $C_A$, dự phóng với giả định không tăng vốn và cổ tức bằng bình quân 3 năm [[src-tt83-2025-nhnn#^pl6-ii]]. Xem [[target-capital]], [[projected-own-funds]].

**Phê duyệt.** Ở ngân hàng thương mại, HĐQT hoặc HĐTV phê duyệt kế hoạch vốn theo đề nghị của Tổng giám đốc. Ở chi nhánh ngân hàng nước ngoài, việc này theo quy định của ngân hàng mẹ [[src-tt83-2025-nhnn#^d61-2]].

**Chuỗi vốn → hạn mức.** Vốn mục tiêu được phân bổ theo tài sản tính theo rủi ro, rồi làm cơ sở xác định [[risk-limits]] [[src-tt83-2025-nhnn#^d61-1]]. Đ20 cũng yêu cầu hạn mức phù hợp với tổng tài sản có rủi ro phân bổ cho rủi ro đó [[src-tt83-2025-nhnn#^d20-2]].

**Theo dõi và báo cáo.**
- Kế hoạch vốn được giám sát theo vốn mục tiêu và điều chỉnh khi cần [[src-tt83-2025-nhnn#^d59-2]].
- Báo cáo ICAAP hằng năm gồm kế hoạch vốn và kết quả phân bổ vốn [[src-tt83-2025-nhnn#^d63-1]].
- Rà soát ICAAP đánh giá tính khả thi của phương án tăng vốn [[src-tt83-2025-nhnn#^d62-1]].
- Báo cáo ICAAP gửi NHNN có mục kế hoạch vốn: phương án tăng vốn (nguồn, lộ trình, giải pháp), chính sách cổ tức, phân bổ vốn mục tiêu cho rủi ro trọng yếu, mức cảnh báo sớm [[src-tt83-2025-nhnn#^pl3-5]].

**Các bước lập kế hoạch vốn (Bardaeva, T4).** Xác định vốn tự có, RWA, CAR rồi so với yêu cầu quy định hoặc nội bộ để ra thặng dư. Với yêu cầu theo loại phơi nhiễm như CCyB, thêm bước tính CCyB bình quân gia quyền theo RWA cho tập đoàn và cộng vào yêu cầu (8% Trụ cột 1 + 2,5% CCB + CCyB tập đoàn) [[src-bardaeva-alm#^ch16-5]].

$$CCyB_{group} = \frac{\sum_i RWA_i \times CCyB_i}{RWA_{total}}$$
[[src-bardaeva-alm#^ch16-5]]

**Kế hoạch hành động vốn trong khủng hoảng (Bardaeva, T4)** [[src-bardaeva-alm#^ch15-5]]:
1. Lượng hoá tác động lên vốn: nội tệ mất giá làm tăng RWA của khoản vay bằng ngoại tệ mạnh, moratorium, trích lập dự phòng, đánh giá lại danh mục trái phiếu qua OCI [[src-bardaeva-alm#^ch15-6]].
2. Ước tính mức vốn sau tác động và so với yêu cầu.
3. Chuẩn bị biện pháp bù thiếu hụt: tối ưu RWA, chuyển RWA cho công ty mẹ hoặc tổ chức khác, cuối cùng là xin bơm vốn [[src-bardaeva-alm#^ch15-7]].
4. Ước tính thặng dư/thiếu hụt sau biện pháp.

**M&A (Bardaeva, T4).**
- Khi bán, IFRS 5 khiến lỗ giao dịch được ghi nhận ngay và tác động lên vốn [[src-bardaeva-alm#^ch16-12]].
- Khi mua, theo IFRS 3 ngày mua là ngày nắm quyền kiểm soát; goodwill dương là tài sản vô hình, bị trừ khỏi vốn tự có [[src-bardaeva-alm#^ch16-13]].

**Từ kết quả stress test (Choudhry, T4).**
- Vốn sau stress dưới tỷ lệ tối thiểu thì ngân hàng xét biện pháp: phòng ngừa, cắt hoạt động rủi ro, rút khỏi mảng kinh doanh [[src-choudhry-principles-banking#^choudhry-icaap-5]].
- Ví dụ stress suy thoái: CAR giảm xuống 14,66%, dưới mức 15%; kết luận nên tăng vốn bằng cổ phần hoặc contingent capital ([[contingent-convertible-bond]]), quyết định thuộc Board [[src-choudhry-principles-banking#^choudhry-st-18]].
- Ở UK, ngân hàng không đáp ứng buffer Pillar 2B nên lập kế hoạch khôi phục vốn [[src-choudhry-principles-banking#^choudhry-icaap-9]].

**Capital management trong strategic plan (Choudhry, T4).**
- Ba mục tiêu capital management: mức vốn tối ưu tuân thủ quy định và hỗ trợ tăng trưởng; vị thế vốn liên tục tạo yên tâm cho bên ngoài; cơ cấu vốn hiệu quả, chi phí vốn thấp, return bền vững cho cổ đông [[src-choudhry-principles-banking#^choudhry-capm-5]].
- Cách thực hiện: đặt mục tiêu vốn có tính tới thay đổi quy định và kỳ vọng các bên, dự báo nhu cầu vốn cho rủi ro trọng yếu theo risk appetite statement, rà kỳ hạn công cụ vốn hiện có [[src-choudhry-principles-banking#^choudhry-capm-5]].
- Capital strategy theo sau chiến lược tổng thể và mô tả cách phân bổ vốn cho từng mảng, dựa trên return on capital có và không điều chỉnh rủi ro [[src-choudhry-principles-banking#^choudhry-capm-1]]. Capital management plan là cấu phần lõi của [[bank-strategic-plan]] [[src-choudhry-principles-banking#^choudhry-strat-10]].
- Khung capital management nên nêu cho các bên: risk appetite khớp kỳ vọng thế nào, phân bổ và ràng buộc vốn gắn với năng lực funding ra sao, mức chịu đựng biến động lợi nhuận [[src-choudhry-principles-banking#^choudhry-capm-2]].
- Thứ tự ưu tiên: giữ niềm tin, thực hiện chiến lược hướng khách hàng, tối ưu return on capital điều chỉnh rủi ro [[src-choudhry-principles-banking#^choudhry-capm-3]].
- Capital strategy phải xử lý cấu trúc vốn trong kỳ kế hoạch để giữ chất lượng vốn, không chỉ số lượng [[src-choudhry-principles-banking#^choudhry-capm-4]].

**Capital management policy (Choudhry Ch16, T4).**
- Capital management nên được viết thành policy standard chính thức như chính sách thanh khoản, với 3 mục tiêu: đáp ứng nghĩa vụ pháp lý, duy trì nguồn vốn và đệm theo risk profile, lập kế hoạch vốn hiệu quả về chi phí [[src-choudhry-principles-banking#^choudhry-capm-10]]. Điểm xuất phát là các tỷ lệ vốn theo quy định, kể cả của cơ quan quản lý nước ngoài nơi ngân hàng hoạt động, rồi tới quy trình giám sát và escalation khi vượt hạn mức [[src-choudhry-principles-banking#^choudhry-capm-15]].
- Mẫu policy của Choudhry:
  - target Core Tier 1, Total Tier 1, Total capital; Finance duy trì dự báo cuốn chiếu 3 năm báo cáo ALCO; vi phạm dự báo hoặc thực tế báo Head of Treasury, ALCO và cơ quan quản lý [[src-choudhry-principles-banking#^choudhry-capm-16]];
  - Treasury làm capital stress test; khả năng vi phạm target phải báo ALCO [[src-choudhry-principles-banking#^choudhry-capm-17]];
  - RWA báo cáo hằng tuần, dự báo cuối tháng; giao dịch có thể làm giảm vốn báo ALCO ngay [[src-choudhry-principles-banking#^choudhry-capm-18]];
  - cấp vốn phải xin và duyệt trước, bởi Treasury hoặc ALCO tuỳ quy mô (ALCO không giới hạn); tái cấu trúc ảnh hưởng vốn/RWA do ALCO duyệt trước [[src-choudhry-principles-banking#^choudhry-capm-19]];
  - lợi nhuận ròng của mảng chuyển về Treasury ALCO book cuối năm [[src-choudhry-principles-banking#^choudhry-capm-20]].
- Capital resource management policy là tập con, bảo đảm từng mảng dùng vốn tối ưu; hiệu quả dùng vốn là thước đo đánh giá kết quả kinh doanh [[src-choudhry-principles-banking#^choudhry-capm-21]]. Finance đặt target RWA trong quy trình budget; Treasury trình hạn mức dùng vốn cuối tháng cho ALCO duyệt; Board (uỷ quyền ExCo) đặt target RoE và RWA cho từng mảng [[src-choudhry-principles-banking#^choudhry-capm-22]]. Ví dụ báo cáo RWA theo mảng: Figure 16.1 [[src-choudhry-principles-banking#^choudhry-capm-23]].

**Vốn chủ sở hữu trong mô hình kinh doanh (Choudhry Ch16).** Vốn không dùng để tài trợ hoạt động mà đặt vào tài sản phi rủi ro, thanh khoản ngay (tiền gửi NHTW hoặc trái phiếu chính phủ cùng đồng tiền) [[src-choudhry-principles-banking#^choudhry-capm-7]]. Thu nhập từ vốn ghi vào central ALCO book; RoE mục tiêu do Board đặt là hurdle rate cho các mảng [[src-choudhry-principles-banking#^choudhry-capm-8]]. Xem [[funds-transfer-pricing]].

**Capital strategy: tầng chiến lược và chiến thuật (Choudhry Ch16).**
- Tầng chiến lược: rà soát toàn bộ mô hình kinh doanh để xác định mảng nào còn khả thi dưới Basel III, rồi lập kế hoạch tăng, giữ hoặc thoát từng mảng [[src-choudhry-principles-banking#^choudhry-capm-24]]; cơ chế thưởng tối ưu dùng vốn, mục tiêu vốn định lượng cho mọi mảng, hạ tầng báo cáo vốn kịp thời, xem lại hình thức chi nhánh hay công ty con [[src-choudhry-principles-banking#^choudhry-capm-25]].
- Tầng chiến thuật: lãnh đạo nắm yêu cầu vốn và RoA của từng mảng, tính đúng chi phí vốn cho mảng, xét tác động vốn với đề xuất kinh doanh mới; rà soát định kỳ, không làm một lần [[src-choudhry-principles-banking#^choudhry-capm-26]].
- Trình tự: target RoE/RoC đặt trước → capital strategy phân bổ vốn cho mảng → target core Tier 1; [[contingent-convertible-bond]] có thể hỗ trợ bước cuối [[src-choudhry-principles-banking#^choudhry-capm-27]]. Tỷ lệ Tier 1 là kết quả, không phải điểm xuất phát; ngân hàng lập target tỷ lệ vốn 3 năm và 5 năm hằng năm, gắn với strategic funding plan [[src-choudhry-principles-banking#^choudhry-capm-28]].
- Capital planning truyền thống thuộc Finance, nhưng ALCO cần giám sát, sở hữu và chủ động dẫn dắt; quản trị vốn tích hợp với stress testing theo quy định và [[icaap]] [[src-choudhry-principles-banking#^choudhry-capm-30]].

## Phụ thuộc regime
- Output floor là sàn cho RWA tính bằng mô hình nội bộ; theo Bardaeva, lộ trình 5 năm từ 50% lên 72,5%, bắt đầu 2022 [[src-bardaeva-alm#^ch16-6]]. Wiki chưa có văn bản BCBS về output floor để đối chiếu lộ trình [cần nguồn].
- Phơi nhiễm với quốc gia, ngành có thể bị khủng hoảng phi tài chính nên được theo dõi riêng trong dự báo vốn [[src-bardaeva-alm#^ch16-7]].

## Góc nhìn theo domain
- **VN**: TT83/2025 Đ61, hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]]. Đánh giá nội bộ mức đủ vốn do Hội đồng quản lý vốn tham mưu Tổng giám đốc, họp tối thiểu 6 tháng 1 lần [[src-tt83-2025-nhnn#^d6-4c]]. *Diễn giải:* Choudhry đặt quyền sở hữu capital planning ở ALCO [[src-choudhry-principles-banking#^choudhry-capm-30]]; TT83 tách thành một hội đồng riêng bên cạnh [[alco]]. Đây là khác jurisdiction, không phải mâu thuẫn.
- **ALM**: *Diễn giải:* phân bổ vốn mục tiêu cho IRRBB là điểm nối giữa kế hoạch vốn và hạn mức ΔEVE/ΔNII [[src-tt83-2025-nhnn#^d53-2]]. Chi phí vốn của phần phân bổ này có thể đi vào [[funds-transfer-pricing]] (ngoài wiki, chưa có nguồn).

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Phương pháp phân bổ vốn mục tiêu cho từng rủi ro trọng yếu: TT83 không quy định chi tiết [cần nguồn].
