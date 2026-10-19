---
title: "Cơ Chế Xác Định Dòng Tiền và Repricing Profile: Sản Phẩm Cố Định vs Thả Nổi trong IRRBB"
aliases: [IRRBB Fixed vs Floating Cash Flows and Repricing, Co che dong tien va repricing profile Fixed vs Floating, Fixed vs Floating Rate Repricing Mechanics]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Cơ chế xác định dòng tiền và repricing profile khác nhau như thế nào giữa sản phẩm lãi suất cố định (Fixed Rate) và lãi suất thả nổi (Floating Rate)?"
as_of: 2026-10-19
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]"]
relations: []
tags: [irrbb, cash-flows, repricing-profile, fixed-rate, floating-rate, reset-date, contractual-maturity, prepayment, commercial-margin, synthesis]
updated: 2026-10-19
reviewed:
---

## Câu hỏi

1. **Q1 (Xác định Dòng tiền Danh nghĩa)**: Dòng tiền gốc (Principal) và dòng tiền lãi/coupon (Interest/Coupon) được dự phóng và phân rã như thế nào giữa sản phẩm lãi suất cố định (Fixed Rate) và sản phẩm lãi suất thả nổi (Floating Rate) theo Par 102–104 BCBS d368?
2. **Q2 (Repricing Profile & Quy tắc Reset Date)**: Vì sao công cụ lãi suất cố định phân bổ theo Contractual Maturity (hoặc lịch khấu hao), trong khi công cụ lãi suất thả nổi bắt buộc áp dụng quy tắc Par Value tại Reset Date (slot 100% gốc danh nghĩa vào dải kỳ hạn chứa ngày reset đầu tiên, triệt tiêu rủi ro giá trị kinh tế của kỳ hạn gốc)?
3. **Q3 (Xử lý Phần bù không tái định giá & Quyền chọn nhúng)**: Phần bù biên thương mại cố định (Commercial Margin / Spread) và các quyền chọn nhúng/quyền chọn hành vi (Prepayment, Early Redemption, Cap/Floor) được xử lý ra sao giữa sản phẩm cố định vs thả nổi?
4. **Q4 (Khung Quy định Basel vs NHNN)**: Chuẩn mực BCBS d368 và Thông tư 83/2025/TT-NHNN (C3-M7, PL5) quy định và phân biệt việc lập thang kỳ hạn tái định giá giữa Fixed Rate và Floating Rate như thế nào?

## Kết luận

- **Về phân rã dòng tiền (Q1)**: Vị thế lãi suất cố định tạo dòng tiền chắc chắn tới contractual maturity; mọi coupon và khoản trả gốc định kỳ hay cuối kỳ nên được phân bổ vào time bucket midpoint tương ứng [[src-bcbs-irrbb-2016#^irrbb-u05-13]]. Vị thế thả nổi tạo dòng tiền không dự báo được sau next repricing date, ngoài việc giá trị hiện tại được đặt lại về par [[src-bcbs-irrbb-2016#^irrbb-u05-14]] [[src-tata-bank-alm#^tata-ev-3]].
- **Về quy tắc phân bổ Repricing Profile (Q2)**: Notional repricing cash flow có thể được slot theo contractual maturity nếu coupon cố định, hoặc vào kỳ tái định giá kế tiếp nếu coupon thả nổi [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-tata-bank-alm#^tata-gap-1]]. Công cụ thả nổi được giả định tái định giá toàn bộ tại first reset date, nên toàn bộ gốc được slot vào dải chứa ngày đó [[src-bcbs-irrbb-2016#^irrbb-u05-12]]. Tata giải thích quy ước này qua việc tại ngày reset, giá trị hiện tại của công cụ quay về mệnh giá ($PV = Par$) [[src-tata-bank-alm#^tata-gap-2]].
- **Về biên thương mại và quyền chọn nhúng (Q3)**: Phần spread của khoản thanh toán lãi trên gốc chưa hoàn trả và không tái định giá phải được slot tới contractual maturity, bất kể phần gốc đã tái định giá hay chưa [[src-bcbs-irrbb-2016#^irrbb-u05-11]] [[src-bcbs-irrbb-2016#^irrbb-u05-12]]. Optionality của quyền chọn tự động (cap/floor) nên được bỏ qua khi slot dòng tiền và tính riêng qua $\text{KAO}$ [[src-bcbs-irrbb-2016#^irrbb-u05-3]] [[src-bcbs-irrbb-2016#^irrbb-u05-7]]; quyền chọn hành vi (prepayment trên khoản vay cố định) làm dòng tiền thay đổi theo kịch bản qua hệ số $\gamma_i$ [[src-bcbs-irrbb-2016#^irrbb-u05-5]] [[src-bcbs-irrbb-2016#^irrbb-u05-23]].
- **Về quy định tại Việt Nam (Q4)**: Chuẩn mực BCBS d368 quy định 19 dải kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u05-2]] và cách slot cho hai nhóm công cụ cố định, thả nổi [[src-bcbs-irrbb-2016#^irrbb-u05-12]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]]. Tại Việt Nam, Phụ lục V của [[tt83-2025]] dùng cùng 19 thang kỳ hạn và điểm giữa [[src-tt83-2025-nhnn#^pl5-a2-t1]]. Khoản mục cố định phân bổ dòng tiền gốc, lãi theo ngày trả; khoản mục thả nổi phân bổ gốc, lãi định kỳ tới ngày định giá lại tiếp theo gần nhất, phần gốc còn lại vào thang có ngày định giá lại đó [[src-tt83-2025-nhnn#^pl5-a2-1]]. PL5 không có quy tắc riêng cho phần spread không tái định giá.

## Cơ chế

### Q1 — Phân rã dòng tiền danh nghĩa: Fixed Rate vs Floating Rate

Theo Par 101 của chuẩn mực BCBS d368, ngân hàng phải dự phóng toàn bộ notional repricing cash flow tương lai $\text{CF}(t)$ phát sinh từ tài sản, nợ phải trả và khoản mục ngoại bảng nhạy cảm lãi suất [[src-bcbs-irrbb-2016#^irrbb-u05-2]] [[src-tata-bank-alm#^tata-scope-3]]. Par 102 định nghĩa $\text{CF}(t)$ là một trong ba loại: hoàn trả gốc, tái định giá gốc, hoặc thanh toán lãi trên phần gốc chưa hoàn trả hay chưa tái định giá; ngày của mỗi khoản là repricing date của khoản đó [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Chi tiết ở [[notional-repricing-cash-flow]].

$$\text{CF}(t) = \text{Principal Repayment}(t) + \text{Principal Repricing}(t) + \text{Interest Payment}(t)$$

*Diễn giải:* công thức cộng ba loại là cách viết gọn của par 102; nguồn liệt kê ba loại chứ không viết thành tổng.

Sự khác biệt căn bản giữa sản phẩm Fixed Rate và Floating Rate:

| Tiêu chí | Sản phẩm Lãi suất Cố định (Fixed Rate) | Sản phẩm Lãi suất Thả nổi (Floating Rate) |
|---|---|---|
| **Dòng tiền gốc hoàn trả (Principal Repayment)** | Dòng tiền gốc phát sinh theo lịch trình hợp đồng (trả một lần khi đáo hạn hoặc khấu hao định kỳ) [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]]. | Dòng tiền gốc thực tế chỉ tất toán khi đáo hạn hợp đồng hoặc trả nợ định kỳ [[src-bcbs-irrbb-2016#^irrbb-u05-9]]; khi slot, toàn bộ gốc được coi là tái định giá tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]]. |
| **Dòng tiền gốc tái định giá (Principal Repricing)** | Trùng với ngày đáo hạn cuối cùng hoặc lịch hoàn trả gốc danh nghĩa [[src-tata-bank-alm#^tata-gap-1]]. | Phát sinh tại từng ngày thiết lập lại lãi suất (*reset date*); quy ước toàn bộ gốc danh nghĩa tái định giá tại kỳ reset tiếp theo [[src-tata-bank-alm#^tata-gap-2]]. |
| **Dòng tiền lãi (Interest / Coupon Flows)** | Toàn bộ các kỳ trả lãi tương lai được xác định chắc chắn bằng mức lãi suất cố định ghi trên hợp đồng: $\text{Interest}_t = \text{Balance}_t \cdot r_{\text{fixed}} \cdot \Delta t$ (công thức là *Diễn giải*) [[src-bcbs-irrbb-2016#^irrbb-u05-13]]. | Chỉ có dòng lãi của kỳ hiện tại (từ hiện tại đến next reset date) là đã chốt lãi suất; các dòng lãi sau reset date biến động theo chỉ số tham chiếu thị trường [[src-tata-bank-alm#^tata-ev-3]]. |
| **Mức độ phụ thuộc lãi suất** | Dòng tiền danh nghĩa không đổi theo lãi suất thị trường (trừ khi có quyền chọn trả trước) [[src-tata-bank-alm#^tata-ev-3]]. | Dòng tiền danh nghĩa phụ thuộc trực tiếp vào mức lãi suất thị trường tương lai [[src-tata-bank-alm#^tata-ev-3]]. |

```
1. SẢN PHẨM CỐ ĐỊNH (FIXED RATE BULLET 5 NĂM):
Năm 1        Năm 2        Năm 3        Năm 4        Năm 5 (Đáo hạn)
  │            │            │            │            │
  ▼            ▼            ▼            ▼            ▼
Coupon       Coupon       Coupon       Coupon       Coupon + 100% GỐC

2. SẢN PHẨM THẢ NỔI (FLOATING RATE RESET 3 THÁNG, KỲ HẠN 5 NĂM):
Tháng 3 (Next Reset Date)            Tháng 6      Tháng 9 ... Năm 5
  │                                    │            │
  ▼                                    ▼            ▼
Lãi kỳ 1 + 100% GỐC QUY ƯỚC ($PV=Par$)  (Lãi thả nổi tương lai reset theo thị trường)
```

### Q2 — Cơ chế Repricing Profile: Contractual Maturity vs Next Reset Date

Chuẩn mực BCBS d368 quy định 19 dải kỳ hạn chuẩn hóa (Table 1) để phân bổ dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-2]].

1. **Công cụ Lãi suất Cố định — Phân bổ theo Contractual Maturity**:
   - Khoản vay hoặc trái phiếu cố định trả lãi định kỳ và trả gốc cuối kỳ (*bullet*): Dòng coupon được xếp vào từng dải kỳ hạn phát sinh thanh toán; toàn bộ 100% nợ gốc được xếp vào dải kỳ hạn chứa ngày đáo hạn hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-13]].
   - Khoản vay cố định khấu hao (*amortising*): Gốc và lãi của từng kỳ thanh toán được tách rời và xếp vào dải kỳ hạn tương ứng với ngày trả nợ danh nghĩa [[src-bcbs-irrbb-2016#^irrbb-u05-9]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]].
   - Toàn bộ thời gian của hợp đồng chịu rủi ro định giá lại giá trị kinh tế (Duration dài) [[src-tata-bank-alm#^tata-dgap-1]].

2. **Công cụ Lãi suất Thả nổi — Quy tắc Par Value tại Next Reset Date**:
   - Theo Fidelio Tata (2025), sai lầm phổ biến trong ALM là nhầm lẫn giữa kỳ hạn hợp đồng và kỳ hạn nhạy cảm lãi suất [[src-tata-bank-alm#^tata-gap-1]].
   - Đối với khoản vay kỳ hạn 5–10 năm nhưng lãi suất thả nổi điều chỉnh 3 tháng một lần theo lãi suất thị trường (Euribor/SOFR):
     - Khoản vay không mang rủi ro lãi suất của một tài sản 5–10 năm [[src-tata-bank-alm#^tata-gap-2]].
     - Ngay tại ngày Reset Date, lãi suất được cập nhật bằng lãi suất thị trường hiện hành; giá trị chiết khấu dòng tiền của khoản vay quay về đúng mệnh giá danh nghĩa ($PV = Par$) [[src-tata-bank-alm#^tata-gap-2]].
     - Rủi ro biến động giá trị kinh tế chỉ tồn tại từ hiện tại cho đến ngày Reset Date kế tiếp [[src-tata-bank-alm#^tata-gap-2]].
   - *Quy tắc phân bổ (BCBS d368 Par 104, 106)*:
     - Công cụ thả nổi có thể được coi là chuỗi coupon tới lần tái định giá kế tiếp cộng một dòng par notional tại time bucket midpoint gần nhất với dải chứa next reset date [[src-bcbs-irrbb-2016#^irrbb-u05-14]].
     - **Toàn bộ gốc được slot vào dải kỳ hạn chứa first reset date** [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
     - Không slot thêm notional repricing cash flow vào các dải sau, trừ phần spread không tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-12]].

| Danh mục mẫu | Kỳ hạn hợp đồng | Chu kỳ Reset Date | Dải kỳ hạn phân bổ Gốc rủi ro (Repricing Slotting) |
|---|---|---|---|
| **Trái phiếu Chính phủ Cố định** | 5 năm | Không có (cố định) | Dải kỳ hạn 4–5 năm (Contractual Maturity) [[src-tata-bank-alm#^tata-gap-5]] |
| **Cho vay Doanh nghiệp Thả nổi** | 5 năm | 3 tháng / lần | Dải kỳ hạn 1–3 tháng (Next Reset Date) [[src-tata-bank-alm#^tata-gap-5]] |
| **Tiền gửi Tiết kiệm Cố định** | 12 tháng | Không có (cố định) | Dải kỳ hạn 9–12 tháng (Contractual Maturity) [[src-bcbs-irrbb-2016#^irrbb-u05-2]] [[src-bcbs-irrbb-2016#^irrbb-u05-13]] |
| **Tiền gửi Liên ngân hàng Thả nổi** | 2 năm | 6 tháng / lần | Dải kỳ hạn 3–6 tháng (Next Reset Date) [[src-tata-bank-alm#^tata-gap-2]] |
| **IRS — Payer Swap (3 năm)** | 3 năm | Chân trả cố định / Chân nhận thả nổi 6M | Chân nhận: Slot 100% gốc vào dải 3–6M; Chân trả: Trải dòng cố định đến 3 năm [[src-tata-bank-alm#^tata-nii-15]] |

### Q3 — Xử lý Cấu phần không tái định giá và Quyền chọn nhúng

1. **Xử lý Biên thương mại không tái định giá (Commercial Margins / Fixed Spread)**:
   - Một khoản vay thả nổi thường có lãi suất gồm: $\text{Lãi suất} = \text{Lãi suất tham chiếu (Reset)} + \text{Biên thương mại (Fixed Spread)}$.
   - Trong khi phần gốc danh nghĩa được slot vào dải chứa first reset date, phần spread không tái định giá của dòng tiền lãi phải được slot tới contractual maturity, bất kể phần gốc chưa khấu hao đã tái định giá hay chưa [[src-bcbs-irrbb-2016#^irrbb-u05-11]] [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
   - Ngân hàng được chọn có trừ commercial margin và spread component khác khỏi notional repricing cash flow hay không, với phương pháp thận trọng và minh bạch [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. Đường cong chiết khấu đi theo lựa chọn này: risk-free rate, hoặc risk-free rate cộng commercial margin và spread component chỉ khi ngân hàng đã đưa các phần này vào dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-19]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Chi tiết ở [[irrbb-commercial-margins-and-discount-curves]].

2. **Quyền chọn tự động (Automatic Options: Cap / Floor)**:
   - Thường xuất hiện trên sản phẩm thả nổi (cho vay có trần lãi suất cap, tiền gửi có sàn lãi suất floor) [[src-choudhry-principles-banking#^choudhry-irrbb-7]].
   - Theo Par 107 BCBS d368, khi phân bổ dòng tiền tái định giá danh nghĩa, ngân hàng **bỏ qua tính năng quyền chọn** (ignore optionality) để slot dòng tiền cơ sở như công cụ thả nổi thông thường [[src-bcbs-irrbb-2016#^irrbb-u05-3]]. Giá trị quyền chọn tự động được tính toán độc lập tại Bước 4 của khuôn khổ chuẩn hóa thông qua phụ trội vốn $\text{KAO}$ [[src-bcbs-irrbb-2016#^irrbb-u05-1]].

3. **Quyền chọn hành vi (Behavioral Options: Prepayment / Early Redemption)**:
   - Thường xuất hiện trên sản phẩm cố định (người vay trả nợ trước hạn trên khoản vay cố định, người gửi tiền rút trước hạn trên tiền gửi kỳ hạn cố định) [[src-tata-bank-alm#^tata-opt-3]] [[src-choudhry-principles-banking#^choudhry-irrbb-4]].
   - Khi lãi suất giảm, người vay trả trước làm tăng dòng gốc thu hồi sớm và làm triệt tiêu dòng coupon tương lai [[src-tata-bank-alm#^tata-ev-3]]. Tỷ lệ CPR được nhân hệ số $\gamma_i = 1.2$ trong kịch bản giảm và $0.8$ trong kịch bản tăng [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
   - Khi lãi suất tăng, người gửi tiền rút trước hạn làm chuyển dịch dòng tiền gốc từ dải dài hạn về dải ngắn hạn. Tỷ lệ TDRR nhân hệ số $u_i = 1.2$ trong kịch bản tăng và $0.8$ trong kịch bản giảm [[src-bcbs-irrbb-2016#^irrbb-u05-6]].

### Q4 — Khung quy định: Đối chiếu Chuẩn mực Basel d368 và NHNN Việt Nam

- **Chuẩn mực Basel (BCBS d368)**:
  - Par 104 giả định công cụ thả nổi tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]]; par 106 cho phép slot theo contractual maturity nếu coupon cố định, hoặc vào kỳ tái định giá kế tiếp nếu coupon thả nổi [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]].
  - Quy định khung chuẩn hóa 19 dải kỳ hạn, phân tách 3 cấu phần dòng tiền danh nghĩa và hệ số nhân sốc cho quyền chọn hành vi [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
- **Quy định Ngân hàng Nhà nước Việt Nam**:
  - [[tt83-2025]] có hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] và bãi bỏ TT13/2018/TT-NHNN từ cùng ngày [[src-tt83-2025-nhnn#^d74-6]]. Đây là căn cứ tại Việt Nam; Basel d368 là tham chiếu.
  - Ngày định giá lại là ngày gần nhất ngân hàng hoặc đối tác có quyền đơn phương thay đổi lãi suất, hoặc ngày lãi suất thả nổi tự động thay đổi theo chỉ số tham chiếu bên ngoài [[src-tt83-2025-nhnn#^pl5-a1-1c]]. Khoản mục cố định và thả nổi thuộc nhóm đáp ứng đủ tiêu chuẩn; quyền chọn lãi suất đính kèm được tách sang nhóm chưa đáp ứng đủ tiêu chuẩn [[src-tt83-2025-nhnn#^pl5-a1-2]].
  - Quy tắc phân bổ: cố định theo ngày trả gốc, lãi; thả nổi tới ngày định giá lại tiếp theo gần nhất [[src-tt83-2025-nhnn#^pl5-a2-1]]. Khi phân bổ vào điểm giữa, ngân hàng chia dòng tiền giữa hai điểm giữa liền kề để giữ nguyên kỳ hạn [[src-tt83-2025-nhnn#^pl5-a2-0]].
  - Quản trị rủi ro mô hình đối với các giả định hành vi được quy định tại Chương 3 Mục 8 `[cần nguồn: src-tt83-2025-nhnn C3-M8]`.
  - *Khoảng trống*: PL5 không quy định phần spread không tái định giá và việc trừ hay giữ commercial margin (đã ingest [2026-10-19]) `[cần nguồn]`.

## Bằng chứng ủng hộ

- **Ủy ban Basel (BCBS d368)**: Par 102 định nghĩa tái định giá xảy ra tại ngày sớm nhất mà ngân hàng hoặc đối tác được quyền đơn phương thay đổi lãi suất, hoặc ngày lãi suất công cụ thả nổi tự động thay đổi theo benchmark bên ngoài [[src-bcbs-irrbb-2016#^irrbb-u05-10]]. Par 106 nêu giá trị hiện tại của vị thế thả nổi được đặt lại về par tại next repricing date [[src-bcbs-irrbb-2016#^irrbb-u05-14]].
- **Fidelio Tata (2025)**: Minh chứng bằng giải tích tài chính rằng việc định giá một công cụ thả nổi tại ngày reset date cho giá trị hiện tại đúng bằng mệnh giá ($PV = Par$), loại bỏ hoàn toàn rủi ro lãi suất của kỳ hạn gốc dài hạn [[src-tata-bank-alm#^tata-gap-2]].
- **Moorad Choudhry (2022)**: Nhấn mạnh tính chất của sổ ngân hàng (accruals book) là ghi nhận theo giá trị gốc ban đầu; việc phân loại chính xác kỳ hạn tái định giá giữa sản phẩm cố định và thả nổi là điều kiện tiên quyết để tính toán đúng Khe hở kỳ hạn (Gap risk) [[src-choudhry-principles-banking#^choudhry-irrbb-1]] [[src-choudhry-principles-banking#^choudhry-irrbb-4]].

## Bằng chứng trái chiều

- **Rủi ro chênh lệch tín dụng trên sổ ngân hàng (CSRBB)**: Giả định $PV = Par$ tại ngày reset date chỉ đúng hoàn toàn khi lãi suất phi rủi ro thay đổi và chất lượng tín dụng của người vay không đổi [[src-tata-bank-alm#^tata-gap-2]]. Nếu biên chênh lệch tín dụng thị trường (*credit spread*) dãn rộng hoặc người vay bị hạ bậc tín nhiệm, giá trị hiện tại của khoản vay thả nổi tại ngày reset sẽ thấp hơn mệnh giá ($PV < Par$). Việc bỏ qua CSRBB trong slotting sẽ dẫn đến đánh giá thấp rủi ro sụt giảm giá trị vốn thực tế [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
- **Tính phi tuyến của Trần/Sàn (Caps/Floors)**: Việc bỏ qua quyền chọn tự động khi slot dòng tiền cơ sở theo Par 107 giúp đơn giản hóa bảng cân đối nhưng làm sai lệch khe hở tái định giá định kỳ nếu quyền chọn đang ở trạng thái sâu trong tiền (*deep in-the-money*) [[src-bcbs-irrbb-2016#^irrbb-u05-3]] [[src-choudhry-principles-banking#^choudhry-irrbb-7]].

## Phụ thuộc regime

- **Môi trường Lãi suất Tăng (Rising Rates)**:
  - *Sản phẩm Cố định*: Chịu sụt giảm mạnh về giá trị kinh tế ($\Delta\text{EVE} < 0$) do dòng tiền coupon cố định dài hạn bị chiết khấu ở mức lãi suất cao hơn [[src-choudhry-principles-banking#^choudhry-irrbb-3]]. Tốc độ trả trước CPR giảm ($\gamma_i = 0.8$), kéo dài kỳ hạn tài sản sinh lời thấp (*extension risk*) [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
  - *Sản phẩm Thả nổi*: Bảo toàn giá trị kinh tế vì quay về ngang mệnh giá tại ngày reset kế tiếp; đồng thời hỗ trợ tăng thu nhập lãi thuần ($\Delta\text{NII} > 0$) khi lãi suất cho vay được điều chỉnh tăng [[src-choudhry-principles-banking#^choudhry-irrbb-5]]. Tuy nhiên, khoản vay thả nổi có thể chạm trần lãi suất (loan cap), chuyển hóa thành sản phẩm cố định [[src-choudhry-principles-banking#^choudhry-irrbb-7]].
- **Môi trường Lãi suất Giảm (Falling Rates)**:
  - *Sản phẩm Cố định*: Tăng giá trị kinh tế nhưng đối mặt với làn sóng khách hàng trả nợ trước hạn tăng vọt ($\gamma_i = 1.2$) để tái tài trợ ở mức rẻ hơn (*contraction risk*), triệt tiêu dòng coupon cao trong tương lai [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
  - *Sản phẩm Thả nổi*: Thu nhập lãi thuần sụt giảm nhanh chóng tại mỗi kỳ reset; nếu thị trường giảm sâu chạm sàn (deposit/loan floor), ngân hàng không thể tiếp tục giảm lãi suất huy động, gây co hẹp biên lãi thuần [[src-choudhry-principles-banking#^choudhry-irrbb-7]].

## Hàm ý ALM / quy định

- **Đối với ALM / Treasury Analytics**:
  - Hệ thống dữ liệu ALM bắt buộc phải lưu trữ đồng thời hai trường thông tin cho từng hợp đồng: Ngày đáo hạn pháp lý (*contractual maturity date*) và Ngày thiết lập lại lãi suất tiếp theo (*next reset date*).
  - Đối với sản phẩm thả nổi, thuật toán slotting phải phân tách nợ gốc danh nghĩa về dải chứa first reset date, đồng thời slot phần spread không tái định giá tới contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-11]] [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
- **Đối với ALCO**:
  - Ngân hàng có tỷ trọng cho vay thả nổi cao sẽ có thời lượng tài sản ngắn, giúp hạn chế rủi ro $\Delta\text{EVE}$ nhưng khiến thu nhập $\Delta\text{NII}$ nhạy cảm cao với biến động lãi suất ngắn hạn [[src-tata-bank-alm#^tata-nii-10]].
  - ALCO cần sử dụng công cụ hoán đổi lãi suất (IRS) để cân bằng giữa hai mục tiêu: Payer Swap (trả cố định, nhận thả nổi) để rút ngắn thời lượng bảo vệ EVE; hoặc Receiver Swap (nhận cố định, trả thả nổi) để khóa chặt thu nhập NII [[src-tata-bank-alm#^tata-nii-15]].
- **Đối với Ngân hàng Nhà nước Việt Nam**:
  - *Diễn giải:* (ngoài wiki, chưa có nguồn) Tại thị trường Việt Nam, hầu hết các hợp đồng tín dụng trung và dài hạn (cho vay mua nhà, vay dự án) thường áp dụng lãi suất thả nổi điều chỉnh định kỳ theo lãi suất tham chiếu cộng biên độ (chu kỳ điều chỉnh và mức biên độ `[cần nguồn]`). Nếu ALM xếp các khoản vay này vào dải theo kỳ hạn hợp đồng thay vì first reset date, ∆EVE tính ra sẽ lệch và giao dịch phòng hộ có thể sai hướng.

## Bất định

- **Quy chuẩn kỹ thuật Thông tư 83/2025/TT-NHNN**: đã ingest PL5 [2026-10-19]; NHNN dùng 19 thang như d368 [[src-tt83-2025-nhnn#^pl5-a2-t1]]. Xử lý commercial margin và spread không tái định giá không có trong PL5 `[cần nguồn]`.
- *Diễn giải:* khoản vay thả nổi neo theo lãi suất do chính ngân hàng công bố có thể được coi là định giá lại tại ngày gần nhất ngân hàng có quyền đơn phương thay đổi lãi suất theo định nghĩa của PL5.A.I.1.c [[src-tt83-2025-nhnn#^pl5-a1-1c]]. Cách xác định ngày này cho từng hợp đồng là giả định của ngân hàng, cần được cấp có thẩm quyền phê duyệt khi không xác định được [[src-tt83-2025-nhnn#^d54-4a]].
- **Ranh giới giữa Option Risk và Basis Risk tại Việt Nam**: *Diễn giải:* (ngoài wiki, chưa có nguồn) nhiều khoản vay thả nổi tại VN neo theo lãi suất huy động của chính ngân hàng đó (thay vì neo theo chỉ số thị trường minh bạch như SOFR/VNIBOR), tạo ra độ trễ điều hành và rủi ro cơ sở phức tạp chưa được lượng hóa đầy đủ trong các mô hình chuẩn hóa.
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation và mục fixed vs floating. → đã rà [2026-10-18]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại các đoạn về dòng tiền tái định giá và citation par 101–106. → đã rà [2026-10-18]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
