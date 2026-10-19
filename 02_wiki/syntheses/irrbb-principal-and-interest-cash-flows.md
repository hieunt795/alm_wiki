---
title: "Xác định dòng tiền gốc và dòng tiền lãi theo từng portfolio trong IRRBB"
aliases: [IRRBB Principal and Interest Cash Flows, Xac dinh dong tien goc va lai trong IRRBB, IRRBB Cash Flow Slotting and Portfolios]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Định nghĩa dòng tiền tái định giá danh nghĩa Par 102 · Phân bổ dòng tiền công cụ cố định vs thả nổi · Dòng tiền theo mô hình hành vi CASA CPR TDRR · Dòng tiền phái sinh IRS và bóc tách biên thương mại Par 103 · Khung quy định Basel vs NHNN · Payment Date, Maturity Date và Repricing Date khác nhau như thế nào? · Thời điểm thanh toán gốc/lãi có ảnh hưởng như thế nào đến việc xác định Repricing Cash Flow?"
as_of: 2026-10-19
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-tt83-2025-nhnn]]"]
relations: []
tags: [alm, irrbb, cash-flow-slotting, principal-cash-flow, interest-cash-flow, commercial-margin, fixed-rate, floating-rate, nmds, prepayment, synthesis]
updated: 2026-10-19
reviewed:
---

## Câu hỏi
1. Bản chất và định nghĩa của dòng tiền tái định giá danh nghĩa (Notional Repricing Cash Flow - Par 102 BCBS d368): Phân biệt Dòng tiền hoàn trả gốc, Dòng tiền tái định giá gốc, và Dòng tiền thanh toán lãi?
2. Cơ chế phân bổ dòng tiền (Cash Flow Slotting - Par 104, 106) vào 19 dải kỳ hạn chuẩn hóa cho các công cụ lãi suất cố định (Fixed-rate: Bullet vs Amortising) và công cụ lãi suất thả nổi (Floating-rate: quy tắc reset date và xử lý phần bù spread không tái định giá)?
3. Phương pháp xác định dòng tiền gốc và lãi đối với các danh mục có mô hình hành vi (Behavioral Modeling): Tiền gửi không kỳ hạn ([[non-maturity-deposits|CASA/NMDs]]), Cho vay trả nợ trước hạn (Prepayment CPR), và Tiền gửi có kỳ hạn rút trước hạn (Early Redemption TDRR)?
4. Cơ chế xác định dòng tiền của công cụ phái sinh ([[interest-rate-swap|IRS]]) và quy tắc bóc tách Biên thương mại (Commercial Margin Unbundling - Par 103): Khác biệt giữa khấu trừ biên thương mại (Deduct) và giữ lại biên thương mại (Include) tác động ra sao lên đường cong chiết khấu?
5. Chuẩn mực Basel ([[src-bcbs-irrbb-2016]]) và quy định của Ngân hàng Nhà nước Việt Nam (Thông tư 83/2025/TT-NHNN Phụ lục 5) quy định thế nào về phân bổ dòng tiền gốc/lãi? Đâu là khoảng trống pháp lý tại Việt Nam?
6. Payment Date, Maturity Date và Repricing Date khác nhau như thế nào?
7. Thời điểm thanh toán gốc/lãi có ảnh hưởng như thế nào đến việc xác định Repricing Cash Flow?

## Kết luận
- **Ba cấu phần dòng tiền tái định giá danh nghĩa (Par 102)**: Dòng tiền tái định giá danh nghĩa $\text{CF}(t)$ trong IRRBB gồm 3 cấu phần: (1) Dòng hoàn trả gốc theo hợp đồng; (2) Dòng tái định giá gốc (thời điểm sớm nhất ngân hàng hoặc khách hàng được quyền đổi lãi suất); và (3) Dòng thanh toán lãi/coupon phát sinh trên phần dư nợ gốc chưa hoàn trả hoặc chưa tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-10]].
- **Quy tắc Par Value tại Reset Date cho công cụ thả nổi (Par 104, 106)**: Công cụ cố định trải toàn bộ coupon và gốc đến ngày đáo hạn hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-13]]. Ngược lại, công cụ thả nổi được giả định giao dịch lại ngang mệnh giá ($PV = Par$) tại ngày reset tiếp theo; do đó toàn bộ gốc danh nghĩa được slot vào dải kỳ hạn chứa ngày reset đầu tiên, không trải gốc vào các kỳ hạn sau đó [[src-bcbs-irrbb-2016#^irrbb-u05-12]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]] [[src-tata-bank-alm#^tata-gap-2]].
- **Điều chỉnh dòng tiền theo mô hình hành vi**: Tiền gửi CASA phi lõi (Non-core) bắt buộc xếp vào dải qua đêm; phần lõi (Core) trải theo danh mục sao chép tối đa 4–5 năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] [[src-tata-bank-alm#^tata-nmd-3]]. Trả nợ trước hạn (CPR) làm tăng dòng gốc thu hồi sớm và xóa bỏ dòng lãi tương lai (nhân hệ số 0.8 khi lãi suất tăng, 1.2 khi giảm) [[src-bcbs-irrbb-2016#^irrbb-u05-5]]. Tiền gửi rút trước hạn (TDRR) kéo dòng gốc về dải kỳ hạn ngắn hơn (nhân hệ số 1.2 khi lãi suất tăng) [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
- **Phái sinh IRS và bóc tách biên thương mại (Par 103)**: Chân cố định của IRS trải dòng coupon đến đáo hạn; chân thả nổi trải dòng lãi đến ngày reset kế tiếp và 100% gốc danh nghĩa tại ngày reset [[src-tata-bank-alm#^tata-nii-15]]. Ngân hàng được chọn có trừ commercial margin và spread component khỏi notional repricing cash flow hay không, với phương pháp thận trọng và minh bạch [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. Khi tính ∆EVE, đường cong chiết khấu đi theo lựa chọn đó: risk-free rate, hoặc risk-free rate cộng commercial margin nếu dòng tiền đã gồm margin [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Khoảng trống pháp lý tại Việt Nam**: Chuẩn mực BCBS d368 quy định chi tiết kỹ thuật 19 dải kỳ hạn và hệ số điều chỉnh hành vi, Phụ lục V của [[tt83-2025]] dùng cùng định nghĩa ba loại dòng tiền (trả gốc, định giá lại gốc, trả lãi) [[src-tt83-2025-nhnn#^pl5-a1-1c]], cùng 19 thang [[src-tt83-2025-nhnn#^pl5-a2-t1]] và cùng hệ số $\gamma_i$, $u_i$ [[src-tt83-2025-nhnn#^pl5-a2-3b]] [[src-tt83-2025-nhnn#^pl5-a2-3c]]; PL5 không quy định xử lý commercial margin.
- **Q6 — Ba mốc ngày**: BCBS d368 không định nghĩa Payment Date thành khái niệm riêng. Par 102 gọi ngày của mỗi khoản hoàn trả gốc, tái định giá gốc hay thanh toán lãi là repricing date của khoản đó [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Contractual maturity là một ví dụ của ngày hoàn trả gốc [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Tái định giá gốc xảy ra tại ngày sớm nhất mà ngân hàng hoặc đối tác được đơn phương đổi lãi suất, hoặc ngày lãi suất thả nổi tự đổi theo benchmark [[src-bcbs-irrbb-2016#^irrbb-u05-10]]. Tata cũng tách hai mốc: rủi ro lãi suất chỉ tính tới next reset date, không tới contractual maturity [[src-tata-bank-alm#^tata-gap-2]].
- **Q7 — Thời điểm trả gốc/lãi**: Công cụ lãi suất cố định có thể được slot theo contractual maturity; mọi coupon và khoản trả gốc nên được phân bổ theo mốc này [[src-bcbs-irrbb-2016#^irrbb-u05-13]]. Công cụ thả nổi được giả định tái định giá toàn bộ tại first reset date, nên toàn bộ gốc nằm ở dải chứa ngày đó; coupon chỉ được slot tới next reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]]. Ngoại lệ là phần spread không tái định giá: phần này phải được slot tới contractual maturity, kể cả khi gốc đã tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-11]].

## Cơ chế

### Q1 — Bản chất và Định nghĩa Dòng tiền Tái định giá Danh nghĩa (Par 102 BCBS d368)
Theo Đoạn 101–102 của chuẩn mực BCBS d368, ngân hàng bắt buộc phải dự phóng toàn bộ dòng tiền tái định giá danh nghĩa tương lai phát sinh từ tài sản, nợ phải trả (bao gồm tiền gửi không trả lãi) và các khoản mục ngoại bảng nhạy cảm với lãi suất trên sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u05-2]] [[src-tata-bank-alm#^tata-scope-3]].

Dòng tiền tái định giá danh nghĩa $\text{CF}(t)$ được định nghĩa gồm 3 cấu phần độc lập [[src-bcbs-irrbb-2016#^irrbb-u05-9]]:
1. **Dòng tiền hoàn trả gốc (Repayment of Principal)**:
   - Các khoản thanh toán gốc định kỳ theo lịch trình khấu hao hợp đồng hoặc thanh toán toàn bộ một lần khi đáo hạn (*bullet repayment*) [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]].
2. **Dòng tiền tái định giá gốc (Repricing of Principal)**:
   - Thời điểm sớm nhất mà ngân hàng hoặc đối tác có quyền đơn phương thay đổi lãi suất hợp đồng, hoặc thời điểm mà lãi suất của công cụ thả nổi tự động thay đổi theo chỉ số tham chiếu thị trường [[src-bcbs-irrbb-2016#^irrbb-u05-10]].
3. **Dòng tiền thanh toán lãi (Interest Payments / Coupon Flows)**:
   - Dòng tiền lãi phát sinh trên phần dư nợ gốc chưa hoàn trả và chưa tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-9]].
   - *Quy tắc phần bù biên thương mại*: Các cấu phần spread/biên thương mại của dòng tiền lãi không bị tái định giá bắt buộc phải được trải vào các dải kỳ hạn cho đến ngày đáo hạn hợp đồng, bất kể phần nợ gốc chưa khấu hao đã bị tái định giá hay chưa [[src-bcbs-irrbb-2016#^irrbb-u05-11]].

```
DÒNG TIỀN TÁI ĐỊNH GIÁ DANH NGHĨA CF(t) = GỐC HOÀN TRẢ + GỐC TÁI ĐỊNH GIÁ + THANH TOÁN LÃI
├── Gốc hoàn trả (Principal Repayment): Dòng tiền thanh toán gốc thực tế theo hợp đồng
├── Gốc tái định giá (Principal Repricing): Quy ước dòng gốc danh nghĩa đáo hạn và ký mới tại Reset Date
└── Thanh toán lãi (Interest Payment): Coupon cố định hoặc lãi thả nổi dự phóng + Spread cố định
```

### Q2 — Cơ chế Phân bổ Dòng tiền (Cash Flow Slotting) cho Công cụ Cố định vs Thả nổi
Chuẩn mực BCBS d368 quy định 19 dải kỳ hạn chuẩn hóa (Table 1) hoặc điểm giữa của 19 dải kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. Quy trình phân bổ dòng tiền phụ thuộc vào đặc tính lãi suất của từng công cụ [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]]:

1. **Công cụ Lãi suất Cố định (Fixed-Rate Instruments)**:
   - Dòng tiền gốc và lãi được xác định chắc chắn theo hợp đồng cho đến ngày đáo hạn [[src-bcbs-irrbb-2016#^irrbb-u05-13]].
   - *Khoản vay Bullet / Trái phiếu Bullet*: Dòng tiền lãi định kỳ (coupon) được slot vào từng dải kỳ hạn phát sinh; toàn bộ nợ gốc được slot vào dải kỳ hạn chứa ngày đáo hạn hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]].
   - *Khoản vay Khấu hao từng phần (Amortising Loans)*: Dòng tiền trả nợ mỗi kỳ gồm cả gốc và lãi ($\text{CF}_t = \text{Principal}_t + \text{Interest}_t$) được phân rã và slot vào các dải kỳ hạn tương ứng với từng kỳ thanh toán [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]].
2. **Công cụ Lãi suất Thả nổi (Floating-Rate Instruments)**:
   - Dòng tiền sau ngày tái định giá tiếp theo (*next reset date*) không thể dự báo trước nhưng giá trị hiện tại của công cụ được reset về ngang mệnh giá ($PV = Par$) tại ngày reset [[src-bcbs-irrbb-2016#^irrbb-u05-14]] [[src-tata-bank-alm#^tata-gap-2]].
   - *Quy tắc phân bổ (Par 104, 106)*:
     - Dòng thanh toán lãi từ hiện tại đến ngày reset đầu tiên được slot vào các dải kỳ hạn phát sinh [[src-bcbs-irrbb-2016#^irrbb-u05-14]].
     - **Toàn bộ 100% nợ gốc danh nghĩa được slot vào dải kỳ hạn chứa ngày reset đầu tiên** [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
     - Không phân bổ bất kỳ dòng gốc danh nghĩa nào vào các dải kỳ hạn sau ngày reset đầu tiên (trừ cấu phần spread biên thương mại cố định nếu có) [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
3. **Bảng đối chiếu cơ chế phân bổ dòng tiền giữa các nhóm công cụ**:
   | Nhóm công cụ | Dòng tiền gốc (Principal Cash Flow) | Dòng tiền lãi (Interest Cash Flow) | Điểm rơi tái định giá rủi ro |
   |---|---|---|---|
   | **Trái phiếu Chính phủ Cố định (Bullet)** | 100% gốc slot tại ngày đáo hạn hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-13]] | Coupon định kỳ slot vào từng kỳ hạn nhận lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]] | Toàn bộ kỳ hạn hợp đồng (Duration dài) [[src-tata-bank-alm#^tata-dgap-1]] |
   | **Cho vay Khấu hao Cố định (Amortising)** | Gốc định kỳ slot theo lịch trả nợ phân kỳ [[src-bcbs-irrbb-2016#^irrbb-u05-13]] | Lãi giảm dần theo dư nợ slot theo từng kỳ [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]] | Trọng số thời gian dòng tiền (WAL) |
   | **Cho vay Doanh nghiệp Thả nổi (Reset 3M)** | 100% gốc danh nghĩa slot vào dải kỳ hạn $\le 3\text{M}$ [[src-bcbs-irrbb-2016#^irrbb-u05-12]] | Lãi của kỳ hiện tại slot vào dải kỳ hạn $\le 3\text{M}$ [[src-bcbs-irrbb-2016#^irrbb-u05-14]] | Tái định giá tại ngày Reset tiếp theo ($PV = Par$) [[src-tata-bank-alm#^tata-gap-2]] |
   | **Tiền gửi Tiết kiệm Cố định 12M** | 100% gốc slot vào dải kỳ hạn 12 tháng [[src-bcbs-irrbb-2016#^irrbb-u05-13]] | Lãi trả cuối kỳ (hoặc định kỳ) slot tương ứng [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]] | Cố định 12 tháng (kỳ hạn hợp đồng) |

### Q3 — Xác định Dòng tiền theo Mô hình Hành vi (Behavioral Cash Flows)
Đối với các vị thế không thể chuẩn hóa theo hợp đồng (Not amenable to standardisation), dòng tiền gốc và lãi được điều chỉnh theo mô hình hành vi khách hàng [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-tata-bank-alm#^tata-ev-3]]:

1. **Tiền gửi không kỳ hạn (CASA / NMDs - Par 109–115)**:
   - *Phần phi lõi (Non-core deposits)*: Phần số dư biến động ngắn hạn, bắt buộc phải slot toàn bộ gốc vào **dải kỳ hạn qua đêm (Overnight)** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
   - *Phần lõi (Core deposits)*: Phần số dư ổn định được ngân hàng mô phỏng thành danh mục sao chép tái đầu tư định kỳ; dòng gốc danh nghĩa được trải đều vào các dải kỳ hạn trung và dài hạn nhưng không vượt trần Table 2 [[src-bcbs-irrbb-2016#^irrbb-u05-4]] [[src-tata-bank-alm#^tata-nmd-3]]:
     - Bán lẻ giao dịch: Trần Core 90%, kỳ hạn bình quân $\le 5$ năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
     - Bán lẻ phi giao dịch: Trần Core 70%, kỳ hạn bình quân $\le 4.5$ năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
     - Bán buôn: Trần Core 50%, kỳ hạn bình quân $\le 4$ năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
   - *Dòng tiền lãi CASA*: Lãi suất chi trả cực thấp, gồm phần phi lõi tái định giá theo lãi suất qua đêm và phần lõi chi phí vốn 0% hoặc biến động thấp theo thị trường [[src-lubinska-alm-optimisation#^lubinska-u04-1]].
2. **Cho vay chịu Rủi ro Trả nợ Trước hạn (Prepayment Risk - Par 116–123)**:
   - Khách hàng vay lãi suất cố định có quyền trả nợ trước hạn khi lãi suất thị trường giảm [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
   - Dòng tiền gốc hoàn trả tại dải kỳ hạn $k$ bao gồm gốc theo hợp đồng cộng thêm phần gốc trả trước: $\text{Principal}_k = \text{Principal}_{\text{contractual},k} + \text{Prepayment}_k$ [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
   - Tỷ lệ trả trước có điều kiện (CPR) được điều chỉnh theo hệ số kịch bản $\gamma_i$:
     $$\text{CPR}_{i,c} = \min(1, \gamma_i \cdot \text{CPR}_{0,c}) \quad \text{với } \gamma_i = 1.2 \text{ (khi lãi suất giảm) và } \gamma_i = 0.8 \text{ (khi lãi suất tăng)}$$
     [[src-bcbs-irrbb-2016#^irrbb-u05-5]]
   - *Tác động lên dòng lãi*: Dòng gốc bị rút ngắn làm triệt tiêu toàn bộ các dòng tiền lãi dự kiến trong tương lai sau thời điểm trả trước [[src-tata-bank-alm#^tata-ev-3]].
3. **Tiền gửi Có kỳ hạn Rút trước hạn (Early Redemption Risk - Par 124–129)**:
   - Khách hàng gửi tiền rút vốn trước hạn khi lãi suất tăng để tái gửi ở mức lãi suất cao hơn [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
   - Tỷ lệ rút tiền gửi trước hạn (TDRR) nhân hệ số $u_i = 1.2$ trong kịch bản lãi suất tăng và $u_i = 0.8$ trong kịch bản giảm [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
   - Phần tiền gửi bị rút trước hạn chuyển dịch dòng tiền gốc từ dải kỳ hạn hợp đồng (ví dụ 1Y–2Y) về dải kỳ hạn ngắn hạn ($\le 1\text{M}$ hoặc Overnight) [[src-bcbs-irrbb-2016#^irrbb-u05-6]].

### Q4 — Dòng tiền Phái sinh (IRS) và Bóc tách Biên Thương mại (Par 103)
1. **Dòng tiền Công cụ Hoán đổi Lãi suất (IRS Slotting)**:
   - Một hợp đồng IRS được tách thành hai dòng tiền độc lập đại diện cho hai chân hợp đồng [[src-tata-bank-alm#^tata-nii-15]]:
     - **Chân Cố định (Fixed Leg)**: Trải toàn bộ các khoản thanh toán coupon cố định vào từng dải kỳ hạn cho đến ngày đáo hạn hợp đồng [[src-tata-bank-alm#^tata-nii-15]].
     - **Chân Thả nổi (Floating Leg)**: Phân bổ dòng thanh toán lãi thả nổi của kỳ hiện tại vào dải kỳ hạn thanh toán tiếp theo, và **slot 100% gốc danh nghĩa của hợp đồng vào dải kỳ hạn chứa ngày Reset Date tiếp theo** (vì chân thả nổi quay về mệnh giá tại ngày reset) [[src-tata-bank-alm#^tata-gap-2]] [[src-tata-bank-alm#^tata-nii-15]].
   - *Payer IRS (Trả cố định / Nhận thả nổi)*: Tạo dòng tiền ra cố định dài hạn và dòng tiền vào thả nổi ngắn hạn, có tác dụng rút ngắn thời lượng và bảo vệ vốn EVE khi lãi suất tăng [[src-tata-bank-alm#^tata-nii-17]].
2. **Quy tắc Bóc tách Biên Thương mại (Commercial Margin Unbundling - Par 103)**:
   Par 103 cho ngân hàng chọn có trừ commercial margin và các spread component khác khỏi notional repricing cash flow hay không, với điều kiện phương pháp thận trọng và minh bạch [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. Khi tính ∆EVE, dòng tiền được chiết khấu bằng risk-free rate, hoặc bằng risk-free rate cộng commercial margin và spread component nếu dòng tiền đã gồm các phần đó [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Hai đoạn trích này không có yêu cầu áp dụng nhất quán cho cả tài sản và nợ; yêu cầu đó `[cần nguồn]`.
   - **Phương pháp 1 — Khấu trừ Biên thương mại (Deduct Commercial Margins)**:
     - Commercial margin và các spread component được trừ khỏi notional repricing cash flow [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. *Diễn giải:* phần còn lại là gốc và phần lãi theo lãi suất cơ sở.
     - *Đường cong chiết khấu*: BCBS nêu nên chiết khấu theo đường cong phi rủi ro (Risk-free discount curve / OIS / SOFR / TPCP) [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
   - **Phương pháp 2 — Giữ lại Biên thương mại (Include Commercial Margins)**:
     - Commercial margin và các spread component được giữ lại trong notional repricing cash flow [[src-bcbs-irrbb-2016#^irrbb-u05-15]].
     - *Đường cong chiết khấu*: BCBS nêu nên chiết khấu theo đường cong phi rủi ro cộng thêm phần bù biên thương mại tương ứng (Risk-free curve + Commercial spread). *Diễn giải:* nhờ vậy giá trị hiện tại không bị méo do dòng tiền và đường cong lệch nhau về margin [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

### Q5 — Khung quy định: So sánh Basel vs Ngân hàng Nhà nước Việt Nam
- **Chuẩn mực Basel (BCBS d368)**: Thiết lập khuôn khổ định lượng chi tiết cho 19 dải kỳ hạn, phân loại 3 mức độ chuẩn hóa (Amenable, Less amenable, Not amenable), bảng tra cứu tham số hành vi ($\gamma_i$, $u_i$) và trần Table 2 khống chế CASA [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
- **Quy định Ngân hàng Nhà nước Việt Nam**:
  - [[tt83-2025]] có hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]], bãi bỏ TT13/2018 [[src-tt83-2025-nhnn#^d74-6]], và là căn cứ tại Việt Nam; Basel d368 là tham chiếu.
  - Dòng tiền gồm khoản trả gốc, khoản gốc được định giá lại, khoản trả lãi trên phần gốc chưa hoàn trả hoặc chưa định giá lại; ngày của mỗi khoản là ngày định giá lại [[src-tt83-2025-nhnn#^pl5-a1-1c]]. Ba nhóm vị thế giống d368 [[src-tt83-2025-nhnn#^pl5-a1-2]].
  - Công thức CPR, TDRR chỉ áp cho khách hàng cá nhân; khoản vay và tiền gửi của tổ chức do ngân hàng tự xác định dòng tiền [[src-tt83-2025-nhnn#^pl5-a2-3b]] [[src-tt83-2025-nhnn#^pl5-a2-3c]].
  - Quản trị rủi ro mô hình đối với các giả định dòng tiền hành vi (CASA, trả nợ trước hạn) được điều chỉnh tại Chương 3 Mục 8 `[cần nguồn: src-tt83-2025-nhnn C3-M8]`.
  - Tham số sốc cho VND: Bảng 5 không có VND [[src-tt83-2025-nhnn#^pl5-c1-1]]; ngân hàng tính bằng lãi suất bình quân hằng ngày 16 năm nhân $\hat{\alpha}$, sàn 100 bp, trần 400/500/300 bp [[src-tt83-2025-nhnn#^pl5-c1-2]], hoặc tự xác định theo hướng dẫn BCBS cập nhật [[src-tt83-2025-nhnn#^pl5-c2]].

### Q6 — Payment Date, Maturity Date và Repricing Date
Par 102 định nghĩa [[notional-repricing-cash-flow]] CF(t) theo ba loại sự kiện. Ngày của mỗi sự kiện đều được gọi là repricing date [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Bảng dưới đối chiếu ba mốc ngày trong câu hỏi với cách BCBS dùng chúng:

| Mốc ngày | Theo BCBS d368 | Vai trò khi slot CF(t) | Nguồn |
|---|---|---|---|
| Payment date (ngày trả gốc hoặc trả lãi) | Không có định nghĩa riêng; ngày của mỗi khoản hoàn trả gốc hay thanh toán lãi được gọi là repricing date của khoản đó | Mỗi khoản là một CF(t) riêng | [[src-bcbs-irrbb-2016#^irrbb-u05-9]] |
| Maturity date (contractual maturity) | Ví dụ của ngày hoàn trả gốc | Mốc slot coupon và gốc của công cụ cố định; mốc slot phần spread không tái định giá | [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-bcbs-irrbb-2016#^irrbb-u05-11]] |
| Ngày tái định giá gốc (reset date) | Ngày sớm nhất mà ngân hàng hoặc đối tác được đơn phương đổi lãi suất, hoặc ngày lãi suất thả nổi tự đổi theo benchmark | Công cụ thả nổi: toàn bộ gốc slot vào dải chứa first reset date | [[src-bcbs-irrbb-2016#^irrbb-u05-10]] [[src-bcbs-irrbb-2016#^irrbb-u05-12]] |

Tata dùng cùng cách tách: lịch repricing xếp vị thế cố định theo kỳ hạn hợp đồng và vị thế thả nổi theo thời gian tới lần tái định giá kế tiếp [[src-tata-bank-alm#^tata-gap-1]]. Rủi ro lãi suất chỉ được tính tới next reset date, không tới contractual maturity [[src-tata-bank-alm#^tata-gap-2]].

*Diễn giải:* BCBS dùng "repricing date" theo hai nghĩa. Nghĩa rộng là ngày của mọi CF(t), kể cả ngày trả gốc và trả lãi. Nghĩa hẹp là ngày tái định giá gốc. Với công cụ cố định không có quyền đơn phương đổi lãi suất, ngày tái định giá gốc trùng contractual maturity (ngoài wiki, chưa có nguồn).

### Q7 — Thời điểm thanh toán gốc/lãi và Repricing Cash Flow

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[repricing-balance-sheet]] | measures | [[gap-risk]] | — | [[src-tata-bank-alm#^tata-gap-1]] |
| [[repricing-balance-sheet]] | input-to | [[irrbb-standardised-framework]] | — | [[src-bcbs-irrbb-2016#^irrbb-u05-1]] |
| [[repricing-balance-sheet]] | input-to | [[economic-value-of-equity]] | — | [[src-tata-bank-alm#^tata-ev-1]] |
| [[notional-repricing-cash-flow]] | input-to | [[repricing-balance-sheet]] | — | [[src-bcbs-irrbb-2016#^irrbb-u05-2]] |
| Thời điểm trả gốc/lãi | drives | Dải kỳ hạn của [[notional-repricing-cash-flow]] | — | *Diễn giải:* (ngoài wiki, chưa có nguồn) |

Thời điểm trả gốc và trả lãi quyết định dải kỳ hạn của từng CF(t), vì ngày của mỗi khoản là repricing date của khoản đó [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Quy tắc slot khác nhau theo loại coupon:
1. **Coupon cố định**: dòng tiền chắc chắn tới contractual maturity. Mọi coupon và mọi khoản trả gốc định kỳ hay cuối kỳ nên được phân bổ vào time bucket midpoint gần nhất với contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-13]].
2. **Coupon thả nổi**: dòng tiền không dự báo được sau next repricing date, ngoài việc giá trị hiện tại được đặt lại về par. Công cụ có thể được coi là chuỗi coupon tới lần tái định giá kế tiếp cộng một dòng par notional tại dải chứa next reset date [[src-bcbs-irrbb-2016#^irrbb-u05-14]]. Toàn bộ gốc nằm ở dải chứa first reset date; lịch trả gốc sau ngày đó không tạo thêm CF(t) [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
3. **Spread không tái định giá**: phần spread của khoản lãi trên gốc chưa hoàn trả phải được slot tới contractual maturity, bất kể gốc đã tái định giá hay chưa [[src-bcbs-irrbb-2016#^irrbb-u05-11]]. Đây là ngoại lệ duy nhất của par 104 [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
4. **Quyền chọn tự động nhúng** (cap, floor) không làm đổi thời điểm slot. Quyền chọn được bỏ qua khi slot và xử lý riêng [[src-bcbs-irrbb-2016#^irrbb-u05-3]].

*Diễn giải:* (ngoài wiki, chưa có nguồn) xét khoản vay 5 năm, lãi thả nổi reset 3M cộng spread cố định, trả lãi hàng tháng. Coupon tới ngày reset kế tiếp rơi vào các dải ≤ 3M. 100% gốc rơi vào dải chứa ngày reset kế tiếp, dù lịch trả gốc kéo dài 5 năm. Phần spread cố định được slot theo từng kỳ trả lãi tới năm thứ 5. Trả lãi hàng tháng hay hàng quý chỉ đổi số dòng coupon trước ngày reset, không đổi vị trí của dòng gốc.

Câu par 106 "allocated to the time bucket midpoints closest to the contractual maturity" có thể đọc theo hai cách: mỗi dòng tiền xếp theo ngày của chính nó (khớp với par 102), hoặc mọi dòng tiền xếp về mốc contractual maturity. Synthesis đọc theo cách thứ nhất vì par 102 coi ngày của mỗi khoản là repricing date [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]]. *Diễn giải:* cách đọc này chưa được nguồn thứ hai xác nhận (ngoài wiki, chưa có nguồn).

## Bằng chứng ủng hộ
- **Ủy ban Basel (BCBS d368)**: Định nghĩa toán học chặt chẽ về dòng tiền tái định giá danh nghĩa (Par 102), nguyên tắc Par Value tại Reset Date đối với công cụ thả nổi (Par 104, 106) và trần giám sát Table 2 bảo vệ tính thận trọng khi trải dòng tiền NMDs [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-12]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]] [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
- **Fidelio Tata (2025)**: Chứng minh bằng giải tích rằng rủi ro kinh tế của công cụ thả nổi triệt tiêu tại Reset Date ($PV = Par$), khẳng định tính đúng đắn của việc slot toàn bộ gốc danh nghĩa vào dải kỳ hạn reset tiếp theo thay vì kỳ hạn hợp đồng [[src-tata-bank-alm#^tata-gap-2]].
- **Moorad Choudhry**: Nhấn mạnh tầm quan trọng của việc phân tách chính xác dòng tiền gốc và lãi trong mô hình khe hở tái định giá để tránh định giá sai lệch trong hệ thống FTP [[src-choudhry-principles-banking#^choudhry-ftp-11]].

## Bằng chứng trái chiều
- **Giả định Par Value không hoàn hảo (Credit Spread Risk in the Banking Book - CSRBB)**: Par 104 giả định công cụ thả nổi quay về mệnh giá tại ngày reset [[src-bcbs-irrbb-2016#^irrbb-u05-12]]. Tuy nhiên, trên thực tế, nếu chất lượng tín dụng của người vay suy giảm hoặc spread thị trường dãn rộng, giá trị hiện tại của khoản vay thả nổi tại ngày reset sẽ thấp hơn mệnh giá ($PV < Par$). Việc bỏ qua rủi ro spread tín dụng (CSRBB) trong slotting có thể đánh giá thấp rủi ro sụt giảm giá trị vốn thực tế [[src-tata-bank-alm#^tata-gap-2]].
- **Tranh cãi về bóc tách Biên thương mại (Commercial Margins)**: Việc khấu trừ biên thương mại giúp phản ánh thuần túy rủi ro lãi suất thị trường nhưng làm mất đi lớp đệm lợi nhuận bảo vệ ngân hàng trước các cú sốc lãi suất. Ngược lại, giữ lại biên thương mại làm tăng tính phức tạp khi phải xây dựng đường cong chiết khấu riêng cho từng phân khúc khách hàng [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

## Phụ thuộc regime
- **Regime lãi suất tăng vọt**:
  - Dòng tiền gốc cho vay bị kéo dài do khách hàng giảm tốc độ trả trước ($\gamma_i = 0.8$) [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
  - Dòng tiền gốc tiền gửi có kỳ hạn bị rút ngắn do khách hàng đẩy mạnh rút tiền trước hạn ($u_i = 1.2$) [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
  - Dòng tiền lãi của các khoản vay thả nổi tăng lên, hỗ trợ NII ngắn hạn nhưng làm tăng áp lực trả nợ của người vay.
- **Regime lãi suất giảm sâu**:
  - Dòng tiền gốc cho vay đổ về ồ ạt do làn sóng tái tài trợ và trả nợ trước hạn ($\gamma_i = 1.2$) [[src-bcbs-irrbb-2016#^irrbb-u05-5]], làm tiêu tan các dòng tiền lãi tương lai cao và buộc ngân hàng tái đầu tư ở lãi suất thấp.
  - Tiền gửi tiết kiệm duy trì đến hạn ($u_i = 0.8$) [[src-bcbs-irrbb-2016#^irrbb-u05-6]], khóa chặt chi phí huy động vốn ở mức cao.

## Hàm ý ALM / quy định
- **Đối với ALM Analytics / MIS**: Hệ thống công nghệ thông tin ALM bắt buộc phải có khả năng bóc tách độc lập dòng tiền gốc hợp đồng, dòng tiền gốc tái định giá, dòng tiền lãi cơ sở và dòng biên thương mại trên từng tài khoản GL để phục vụ slotting chính xác [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-11]].
- **Đối với ALCO**: Khi phê duyệt mô hình dòng tiền hành vi (CASA, Prepayment), ALCO phải xem xét tác động đồng thời lên cả thước đo thu nhập ($\Delta\text{NII}$) và thước đo giá trị kinh tế ($\Delta\text{EVE}$), tránh việc kéo dài kỳ hạn CASA quá mức để làm đẹp chỉ số EVE nhưng vi phạm trần Table 2 [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
- **Đối với Ngân hàng Nhà nước**: Cần sớm ban hành hướng dẫn chi tiết về quy chuẩn phân bổ dòng tiền vào các dải kỳ hạn và hệ số điều chỉnh kịch bản phù hợp với thị trường tín dụng Việt Nam (theo TT83/2025).
- *Diễn giải:* (ngoài wiki, chưa có nguồn) Tại các NHTM Việt Nam, hầu hết dư nợ cho vay trung dài hạn đều áp dụng cơ chế lãi suất thả nổi định kỳ 3 tháng; do đó việc nắm vững quy tắc slotting toàn bộ nợ gốc vào dải kỳ hạn reset tiếp theo ($PV = Par$) là chìa khóa để tránh tính toán trùng lặp thời lượng tài sản.

## Bất định
- **Khoảng trống kỹ thuật Thông tư 83/2025/TT-NHNN**: PL5 (đã ingest [2026-10-19]) không quy định trừ hay giữ commercial margin; chỉ quy định chiết khấu theo risk-free rate [[src-tt83-2025-nhnn#^pl5-a3-2]] `[cần nguồn]`.
- **Dữ liệu lịch sử ước tính CPR và TDRR**: Tại Việt Nam, nhiều ngân hàng chưa xây dựng được chuỗi dữ liệu lịch sử đủ dài qua các chu kỳ lãi suất để hiệu chỉnh chính xác hệ số $\gamma_i$ và $u_i$, dẫn đến việc phải dựa vào tham số định tính hoặc tham chiếu chuẩn quốc tế.
- **Claim nguồn cho Q6–Q7**: đã ingest bổ sung BCBS u05 par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14) ngày 2026-10-17; Q6, Q7 đã viết lại theo các claim này. Cách đọc par 106 "closest to the contractual maturity" còn chờ nguồn thứ hai (xem Q7).
- **Citation scope**: các câu về par 102, 104, 106 đã chuyển từ `^irrbb-u05-2` (par 101) sang ^irrbb-u05-9 … ^irrbb-u05-14 ngày 2026-10-17. Ba câu về par 103 (bóc tách commercial margin, Q4) đã cite ^irrbb-u05-15 sau lần ingest bổ sung par 103 ngày 2026-10-17. Yêu cầu "áp dụng nhất quán cho cả tài sản và nợ" không có trong par 103 lẫn par 70, nên còn `[cần nguồn]`.
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation và Q1, Q2, Q6, Q7. → đã rà [2026-10-17]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 103): có claim ^irrbb-u05-15 cho quyền chọn trừ commercial margin khỏi CF(t); cần rà lại Q4. → đã rà [2026-10-17]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 (bổ sung): [[tt83-2025]], [[notional-repricing-cash-flow]] thêm căn cứ VN: $CF^S$ của khoản vay có rủi ro trả trước hạn là khoản trả gốc, lãi định kỳ ([[src-tt83-2025-nhnn#^pl5-a2-3b2]]); cần rà lại mục nhóm không đáp ứng đủ tiêu chuẩn có tính dòng lãi.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
