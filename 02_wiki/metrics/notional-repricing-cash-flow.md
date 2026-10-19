---
title: "Notional repricing cash flow — CF(t)"
aliases: [Notional repricing cash flow, Repricing cash flow, "CF(t)", Dòng tiền tái định giá danh nghĩa]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[repricing-balance-sheet]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-2]]"}
  - {type: input-to, to: "[[irrbb-standardised-framework]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
tags: [irrbb, cash-flow-slotting, repricing-date, eve, basel]
updated: 2026-10-19
reviewed:
---

## Định nghĩa

Notional repricing cash flow CF(t) là một trong ba loại dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-9]]:
- hoàn trả gốc, ví dụ tại contractual maturity;
- tái định giá gốc;
- thanh toán lãi trên phần gốc chưa hoàn trả hoặc chưa tái định giá.

Ngày của mỗi khoản hoàn trả, tái định giá hay thanh toán lãi đều được gọi là **repricing date** của khoản đó [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Tái định giá gốc xảy ra tại ngày sớm nhất mà ngân hàng hoặc đối tác được quyền đơn phương đổi lãi suất, hoặc ngày lãi suất của công cụ thả nổi tự động đổi theo benchmark bên ngoài [[src-bcbs-irrbb-2016#^irrbb-u05-10]].

Trong khung chuẩn hoá ∆EVE của BCBS, ngân hàng phải dự phóng mọi CF(t) phát sinh từ tài sản, nợ và khoản mục ngoại bảng nhạy cảm lãi suất lên 19 dải kỳ hạn định sẵn hoặc lên điểm giữa của các dải đó [[src-bcbs-irrbb-2016#^irrbb-u05-2]].

## Công thức

CF(t) không có công thức đại số trong nguồn đã ingest. Nguồn định nghĩa nó bằng loại dòng tiền và quy tắc slot theo loại lãi suất:

| Trường hợp | Quy tắc slot CF(t) | Mức bắt buộc | Nguồn |
|---|---|---|---|
| Coupon cố định | Slot theo contractual maturity | có thể | [[src-bcbs-irrbb-2016#^irrbb-u05-13]] |
| Vị thế lãi suất cố định | Mọi coupon và mọi khoản trả gốc định kỳ hay cuối kỳ vào time bucket midpoint gần nhất với contractual maturity | nên | [[src-bcbs-irrbb-2016#^irrbb-u05-13]] |
| Coupon thả nổi | Slot vào kỳ tái định giá kế tiếp | có thể | [[src-bcbs-irrbb-2016#^irrbb-u05-13]] |
| Công cụ thả nổi, phần gốc | Giả định tái định giá toàn bộ tại first reset date; toàn bộ gốc vào dải chứa ngày đó, không slot thêm vào dải sau | giả định của khung | [[src-bcbs-irrbb-2016#^irrbb-u05-12]] |
| Vị thế thả nổi, cách biểu diễn | Chuỗi coupon tới next repricing cộng một dòng par notional tại time bucket midpoint gần nhất với dải chứa next reset date | có thể | [[src-bcbs-irrbb-2016#^irrbb-u05-14]] |
| Spread không tái định giá | Slot tới contractual maturity, bất kể gốc chưa khấu hao đã tái định giá hay chưa | phải | [[src-bcbs-irrbb-2016#^irrbb-u05-11]] |
| Commercial margin và spread component | Ngân hàng được chọn trừ hoặc giữ trong CF(t), với phương pháp thận trọng và minh bạch | được chọn | [[src-bcbs-irrbb-2016#^irrbb-u05-15]] |
| Quyền chọn lãi suất tự động nhúng | Bỏ qua quyền chọn khi slot CF(t) | nên | [[src-bcbs-irrbb-2016#^irrbb-u05-3]] |

Việc chọn quy tắc slot nào phụ thuộc khả năng chuẩn hoá của vị thế [[src-bcbs-irrbb-2016#^irrbb-u05-16]].

**Từ CF(t) tới ∆EVE** (BCBS d368 par 132, theo từng đồng tiền c và kịch bản i):
1. Slot mọi CF(t) vào dải k hoặc điểm giữa t_k; trong mỗi dải, bù trừ dòng dương và âm thành một vị thế long hoặc short, ra CF_{i,c}(k) [[src-bcbs-irrbb-2016#^irrbb-u05-17]].
2. Nhân với discount factor liên tục theo kịch bản sốc ở Annex 2, t_k là điểm giữa dải [[src-bcbs-irrbb-2016#^irrbb-u05-18]]:
   $$DF_{i,c}(t_k) = \exp(-R_{i,c}(t_k) \cdot t_k)$$
   Discount factor phải đại diện cho risk-free zero coupon rate. Dòng tiền nên chiết khấu bằng risk-free rate, hoặc risk-free rate cộng commercial margin nếu CF(t) đã gồm margin [[src-bcbs-irrbb-2016#^irrbb-u05-19]].
3. Cộng các vị thế có trọng số, không gồm quyền chọn lãi suất tự động [[src-bcbs-irrbb-2016#^irrbb-u05-20]]:
   $$EVE_{i,c}^{nao} = \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k)$$
4. Lấy EVE^nao theo cấu trúc kỳ hạn hiện tại trừ EVE^nao của kịch bản i, cộng KAO_{i,c} [[src-bcbs-irrbb-2016#^irrbb-u05-21]]:
   $$\Delta EVE_{i,c} = \sum_{k=1}^{K} CF_{0,c}(k) \cdot DF_{0,c}(t_k) - \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k) + KAO_{i,c}$$

Công thức viết dạng dải k; dạng điểm giữa t_k thay CF(k) bằng CF(t_k) [[src-bcbs-irrbb-2016#^irrbb-u05-20]].

## Diễn giải

- *Diễn giải:* "repricing date" trong par 102 có hai nghĩa. Nghĩa rộng là ngày của mọi CF(t), gồm cả ngày trả lãi và ngày trả gốc [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Nghĩa hẹp là ngày tái định giá gốc [[src-bcbs-irrbb-2016#^irrbb-u05-10]]. Khi đọc các node khác, cần xem "repricing date" đang dùng theo nghĩa nào.
- *Diễn giải:* với công cụ thả nổi, lịch trả gốc sau first reset date không tạo thêm CF(t), vì toàn bộ gốc đã được slot tại ngày reset [[src-bcbs-irrbb-2016#^irrbb-u05-12]]. Ngoại lệ là phần spread không tái định giá, vẫn kéo tới contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-11]].
- Tata nêu cùng logic từ góc kinh tế: công cụ thả nổi reset theo lãi suất thị trường thì giao dịch lại theo par value, nên rủi ro lãi suất chỉ tính tới next reset date [[src-tata-bank-alm#^tata-gap-2]].
- *Diễn giải:* câu par 106 "closest to the contractual maturity" có thể đọc là dồn mọi coupon về dải đáo hạn, hoặc là mỗi dòng tiền vào dải gần ngày của chính nó. Node này đọc theo cách thứ hai, vì cách đó khớp định nghĩa CF(t) theo từng ngày ở par 102. Cách đọc này chưa có nguồn thứ hai xác nhận.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Định nghĩa CF(t) | Ba loại: trả gốc, tái định giá gốc, trả lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]] | Ba loại: khoản trả gốc, khoản gốc được định giá lại, khoản trả lãi trên phần gốc chưa hoàn trả hoặc chưa định giá lại [[src-tt83-2025-nhnn#^pl5-a1-1c]] | d368 par 102; TT83 PL5.A.I.1.c | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Dải kỳ hạn | 19 dải hoặc điểm giữa dải [[src-bcbs-irrbb-2016#^irrbb-u05-2]] | 19 thang kỳ hạn hoặc điểm giữa; phân bổ vào điểm giữa thì chia dòng tiền giữa hai điểm giữa liền kề [[src-tt83-2025-nhnn#^pl5-a2-0]] | d368 par 101; TT83 PL5.A.II | 01/07/2026 |
| Lãi suất thả nổi | Tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]] | Gốc, lãi định kỳ tới ngày định giá lại tiếp theo gần nhất; gốc còn lại vào thang có ngày định giá lại tiếp theo [[src-tt83-2025-nhnn#^pl5-a2-1]] | d368 par 104; TT83 PL5.A.II.1.b | 01/07/2026 |
| Spread không tái định giá | Phải slot tới contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-11]] | [cần nguồn] (PL5 không nêu) | d368 par 102 | |
| Commercial margin | Được chọn trừ hoặc giữ [[src-bcbs-irrbb-2016#^irrbb-u05-15]] | [cần nguồn] (PL5 không nêu); chiết khấu theo risk-free rate [[src-tt83-2025-nhnn#^pl5-a3-2]] | d368 par 103; TT83 PL5.A.III.2 | 01/07/2026 |

Khác biệt: Phụ lục V của [[tt83-2025]] không có quy định về phần spread không tái định giá và về lựa chọn trừ hay giữ commercial margin; phần còn lại cùng nội dung với d368.

Với cho vay lãi suất cố định có rủi ro trả trước hạn của cá nhân, PL5 định nghĩa $CF^S$ trong công thức dòng tiền là khoản trả gốc, lãi định kỳ [[src-tt83-2025-nhnn#^pl5-a2-3b2]]. *Diễn giải:* như vậy dòng tiền của nhóm không đáp ứng đủ tiêu chuẩn cũng gồm phần lãi, nhất quán với điểm c(iii) của định nghĩa CF(t).

## Ứng dụng trong ALM

- CF(t) là đầu vào của Stage 2 trong năm giai đoạn đo ∆EVE chuẩn hoá: xác định slot dòng tiền theo kỳ hạn tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-1]]. Cách lập bảng tái định giá: [[repricing-balance-sheet]]; khung tổng: [[irrbb-standardised-framework]].
- **Điều chỉnh hành vi.** Một số vị thế không slot theo hợp đồng mà theo giả định hành vi:
  - phần tiền gửi không kỳ hạn phi lõi nên được coi là tiền gửi qua đêm và đặt vào dải ngắn nhất; phần lõi slot theo quy trình của ngân hàng, trong trần kỳ hạn bình quân theo từng loại [[src-bcbs-irrbb-2016#^irrbb-u05-4]]. Xem [[non-maturity-deposits]];
  - tốc độ trả nợ trước hạn thay đổi theo kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-u05-5]];
  - tỷ lệ rút tiền gửi có kỳ hạn trước hạn nhân với hệ số phụ thuộc kịch bản [[src-bcbs-irrbb-2016#^irrbb-u05-6]]. Xem [[behavioural-options]].
  - Vì vậy CF(t) của các sản phẩm này có thể khác nhau theo kịch bản, nên công thức ∆EVE viết CF_{0,c} và CF_{i,c} riêng [[src-bcbs-irrbb-2016#^irrbb-u05-23]].
- Phân tích theo câu hỏi: [[irrbb-principal-and-interest-cash-flows]] (Q6–Q7: Payment date, Maturity date, Repricing date).

## Nhầm lẫn thường gặp

- **Slot gốc thả nổi theo contractual maturity.** BCBS giả định gốc thả nổi tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
- **Kéo cả spread của công cụ thả nổi về ngày reset.** Phần spread không tái định giá phải slot tới contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-11]].
- **Coi việc trừ commercial margin khỏi CF(t) là cùng một quy định với chọn đường cong chiết khấu.** Par 103 nói về CF(t) [[src-bcbs-irrbb-2016#^irrbb-u05-15]]; đường cong chiết khấu khi tính ∆EVE là quy định riêng [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Coi CF(t) trong cùng một dải là khớp nhau về thời điểm.** Đây là giả định của khung chuẩn hoá, tạo ra intra-bucket mismatch risk; BCBS giảm rủi ro này bằng 19 dải [[src-bcbs-irrbb-2016#^irrbb-u05-22]].
- **Đưa quyền chọn lãi suất tự động nhúng vào lịch CF(t).** Quyền chọn nên được bỏ qua khi slot CF(t) [[src-bcbs-irrbb-2016#^irrbb-u05-3]].
