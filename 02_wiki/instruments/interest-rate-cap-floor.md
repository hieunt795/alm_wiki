---
title: "Interest Rate Cap and Floor (Hạn mức trần và sàn lãi suất)"
aliases: [Cap, Floor, Collar, Automatic Interest Rate Options, Caplet, Floorlet, Lãi suất trần và sàn]
type: instrument
domains: [product, alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: part-of, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: hedges, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: input-to, to: "[[irrbb-standardised-framework]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-7]]"}
tags: [irrbb, instrument, cap, floor, collar, automatic-option, non-linear-risk]
updated: 2026-10-16
reviewed:
---

## Định nghĩa
Hạn mức trần lãi suất (Interest Rate Cap) và Hạn mức sàn lãi suất (Interest Rate Floor) là các công cụ phái sinh quyền chọn lãi suất phi tuyến tính (non-linear derivatives), được thiết kế để bảo vệ chủ thể nắm giữ khỏi các biến động bất lợi của lãi suất tham chiếu vượt qua một ngưỡng cố định (Strike Rate $K$) [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

Theo phân loại của Ủy ban Basel d368, Cap và Floor thuộc nhóm **Quyền chọn tự động (Automatic Options)**:
- Người sở hữu quyền chọn sẽ thực thi quyền một cách duy lý ngay khi đem lại lợi ích kinh tế (khi quyền chọn ở trạng thái In-the-Money - ITM) [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- Chúng có thể tồn tại dưới dạng hợp đồng phái sinh độc lập trên thị trường (standalone derivatives) hoặc nhúng ngầm định (embedded options) bên trong các sản phẩm tín dụng và tiền gửi của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u05-3]].

## Cấu trúc và Cơ chế Hoạt động

### 1. Interest Rate Cap (Trần lãi suất)
- **Bản chất**: Một chuỗi liên tiếp các quyền chọn mua lãi suất kiểu châu Âu (European call options on interest rates), mỗi quyền chọn thành phần tương ứng với một chu kỳ thanh toán được gọi là một **Caplet** [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- **Khoản thanh toán của Caplet $i$** (thanh toán cuối kỳ $t_{i+1}$ theo cơ chế trả sau - in arrears):
  $$\text{Payoff}_{\text{caplet}, i} = N \cdot \tau_i \cdot \max(R(t_i) - K_{\text{cap}}, 0)$$
  Trong đó: $N$ là vốn gốc danh nghĩa, $\tau_i$ là độ dài chu kỳ tính lãi, $R(t_i)$ là lãi suất tham chiếu xác định đầu kỳ, và $K_{\text{cap}}$ là mức lãi suất trần.
- **Ứng dụng ALM**:
  - *Phòng ngừa nợ huy động thả nổi*: Bảo vệ chi phí vốn huy động của ngân hàng không vượt quá trần $K_{\text{cap}}$ khi lãi suất thị trường tăng vọt.
  - *Nhận diện rủi ro nhúng*: Khi ngân hàng cung cấp gói tín dụng cho vay thả nổi nhưng cam kết "lãi suất tối đa không quá $K$%", ngân hàng thực chất đã **bán một Cap cho khách hàng** (Short Cap position). Nếu lãi suất thị trường tăng cao hơn $K$, ngân hàng bị kẹt biên lợi nhuận thu nhập và chịu rủi ro phi tuyến nghiêm trọng [[src-bcbs-irrbb-2016#^irrbb-u05-3]].

### 2. Interest Rate Floor (Sàn lãi suất)
- **Bản chất**: Một chuỗi liên tiếp các quyền chọn bán lãi suất kiểu châu Âu (European put options on interest rates), mỗi quyền chọn thành phần gọi là một **Floorlet** [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- **Khoản thanh toán của Floorlet $i$**:
  $$\text{Payoff}_{\text{floorlet}, i} = N \cdot \tau_i \cdot \max(K_{\text{floor}} - R(t_i), 0)$$
- **Ứng dụng ALM**:
  - *Bảo vệ thu nhập cho vay thả nổi*: Khi lãi suất thị trường hạ sâu (môi trường nới lỏng tiền tệ), Floor đảm bảo lợi suất tài sản cho vay của ngân hàng không rơi xuống dưới ngưỡng sàn $K_{\text{floor}}$.
  - *Nhận diện rủi ro nhúng*: Khi ngân hàng cam kết trả lãi suất tối thiểu trên tiền gửi thanh toán hoặc tài khoản tiết kiệm (sàn lãi suất tiền gửi), ngân hàng đã **bán một Floor cho người gửi tiền** (Short Floor position), khiến chi phí trả lãi không thể giảm theo đà giảm của lợi suất đầu tư [[src-bcbs-irrbb-2016#^irrbb-u05-3]].

### 3. Interest Rate Collar (Biên độ lãi suất kết hợp)
- Sự kết hợp đồng thời giữa việc mua một Cap và bán một Floor (hoặc ngược lại) để giới hạn lãi suất thả nổi dao động trong một biên độ xác định $[K_{\text{floor}}, K_{\text{cap}}]$ [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- **Zero-cost Collar**: Thiết lập mức $K_{\text{cap}}$ và $K_{\text{floor}}$ sao cho phí mua Cap bằng đúng phí thu được từ việc bán Floor ($\text{Premium}_{\text{cap}} = \text{Premium}_{\text{floor}}$), giúp ngân hàng thiết lập rào chắn rủi ro mà không phát sinh chi phí bằng tiền mặt ban đầu.

## Định giá Cap / Floor theo Mô hình Black-76 và Bachelier

Mỗi Caplet và Floorlet thường được định giá thông qua công thức mở rộng Black-76 (giả định lãi suất kỳ hạn tuân theo phân phối log-normal) hoặc mô hình Bachelier (normal model, cho phép lãi suất âm) [[src-bcbs-irrbb-2016#^irrbb-u06-4]]:

### Công thức Black-76 cho Caplet:
$$V_{\text{caplet}, i} = N \cdot \tau_i \cdot DF(0, t_{i+1}) \cdot \left[ F_i \cdot \Phi(d_1) - K \cdot \Phi(d_2) \right]$$
$$d_1 = \frac{\ln(F_i / K) + \frac{1}{2}\sigma_i^2 t_i}{\sigma_i \sqrt{t_i}}, \quad d_2 = d_1 - \sigma_i \sqrt{t_i}$$
Trong đó:
- $F_i$ là lãi suất kỳ hạn (forward rate) áp dụng cho khoảng thời gian $[t_i, t_{i+1}]$.
- $DF(0, t_{i+1})$ là hệ số chiết khấu phi rủi ro.
- $\sigma_i$ là độ biến động ngầm định (implied volatility) của lãi suất kỳ hạn.
- $\Phi(\cdot)$ là hàm phân phối tích lũy chuẩn tắc.

### Các Hệ số Độ nhạy Hy Lạp (Greeks):
- **Delta ($\Delta$)**: Độ nhạy giá quyền chọn đối với thay đổi lãi suất cơ sở ($\partial V / \partial F$). Khi Cap ngày càng ITM, Delta tiến dần về 1 (hành xử giống một hợp đồng hoán đổi lãi suất cố định).
- **Vega ($\nu$)**: Độ nhạy giá trị quyền chọn theo độ biến động ngầm định ($\partial V / \partial \sigma$). Khi biến động thị trường tăng, giá trị của Cap và Floor đều tăng.
- **Gamma ($\Gamma$)**: Đo lường tốc độ biến động của Delta, thể hiện tính phi tuyến tính mạnh mẽ của rủi ro quyền chọn.

## Xử lý Chuẩn hoá theo Basel d368 (Add-on $\text{KAO}_{i,c}$)

Trong Khuôn khổ Chuẩn hoá Basel d368 (Section IV), rủi ro từ quyền chọn lãi suất tự động (cả độc lập và nhúng) không được phân bổ vào các dải kỳ hạn tái định giá thông thường mà được bóc tách để tính riêng thành phần phụ trội vốn **$\text{KAO}_{i,c}$ (Automatic Interest Rate Option Add-on)** [[src-bcbs-irrbb-2016#^irrbb-u05-3]] [[src-bcbs-irrbb-2016#^irrbb-u05-7]]:

1. **Bóc tách dòng tiền cơ sở**: Dòng tiền của hợp đồng mang quyền chọn nhúng được xếp vào 19 dải kỳ hạn như một công cụ tiêu chuẩn không có quyền chọn [[src-bcbs-irrbb-2016#^irrbb-u05-3]].
2. **Kịch bản sốc biến động kết hợp**: Đối với mọi vị thế quyền chọn tự động đã bán (sold options $o$), ngân hàng phải tái định giá toàn bộ giá trị quyền chọn dưới từng kịch bản sốc lãi suất $i$ kết hợp với **mức gia tăng tương đối 25% độ biến động ngầm định ($\Delta\sigma / \sigma = +25\%$)** [[src-bcbs-irrbb-2016#^irrbb-u05-7]]:
   $$\Delta V_{o,i,c} = V_o(R + \Delta R_{i,c}, \sigma \times 1.25) - V_o(R, \sigma)$$
3. **Cơ chế bù trừ phòng ngừa rủi ro**: Giá trị tổn thất từ các quyền chọn bán chỉ được bù trừ với mức tăng giá trị của các quyền chọn mua (bought options) nếu các quyền chọn mua này được chỉ định cụ thể nhằm mục đích phòng ngừa rủi ro cho quyền chọn bán tương ứng [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
4. Kết quả $\text{KAO}_{i,c}$ được cộng trực tiếp vào tổn thất giá trị kinh tế của loại tiền tệ $c$ dưới kịch bản sốc $i$ [[src-bcbs-irrbb-2016#^irrbb-u05-8]].

## Đề xuất cập nhật
- [2026-10-19] ingest src-tata-bank-alm u06 — chờ user duyệt: đã có node [[negative-interest-rates]]: nguồn so sánh sàn 0% trên tiền gửi bán lẻ với floor tự động (out of the money khi lãi suất cao, at/in the money khi thấp hoặc âm) [[src-tata-bank-alm#^tata-neg-2]]; đề xuất link ở mục mô hình Bachelier.
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: thêm ứng dụng ALM (ví dụ 6.12): ngân hàng liability-sensitive (gap tức thời −80 trên 200 triệu USD, +1% làm NII giảm 0,8 triệu, EAR khoảng 7,8%) [[src-choudhry-principles-banking#^choudhry-hedge-20]] [[src-choudhry-principles-banking#^choudhry-hedge-21]] mua cap notional 80 triệu USD, strike 3% ATM, 1 năm, loại bỏ EAR; strike 4% OTM rẻ hơn nhưng còn EAR [[src-choudhry-principles-banking#^choudhry-hedge-23]]; chi phí 5bp NIM, giữ lợi khi lãi suất giảm, khác swap/FRA [[src-choudhry-principles-banking#^choudhry-hedge-24]]; ngân hàng asset-sensitive mua floor [[src-choudhry-principles-banking#^choudhry-hedge-25]]. Xem [[structural-hedging]].
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[forward-rate-agreement]]; đề xuất link ở lần nhắc đầu FRA.
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM.
