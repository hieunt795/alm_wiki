---
title: "Swaption (Quyền chọn hoán đổi lãi suất)"
aliases: [Swaption, Swap Option, Payer Swaption, Receiver Swaption, Bermudan Swaption, European Swaption]
type: instrument
domains: [product, alm, basel]
status: active
maturity: draft
sources: ["[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: hedges, to: "[[behavioural-options]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: part-of, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[irrbb-standardised-framework]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-7]]"}
tags: [irrbb, instrument, swaption, prepayment-hedging, non-linear-risk, bermudan]
updated: 2026-10-22
reviewed:
---

## Khái niệm và Định nghĩa
Quyền chọn hoán đổi lãi suất (Swaption, viết tắt của Swap Option) là một hợp đồng phái sinh trao cho người mua (buyer) quyền, nhưng không có nghĩa vụ, được tham gia vào một hợp đồng hoán đổi lãi suất cơ sở ([[interest-rate-swap|IRS]]) tại một mức lãi suất cố định định trước (Strike Swap Rate $K$) vào hoặc trước một ngày đáo hạn xác định [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

Trong cấu trúc quản trị ALM hiện đại, Swaption là công cụ phái sinh phi tuyến tính cao cấp nhất được Treasury sử dụng để phòng ngừa các rủi ro quyền chọn hành vi phức tạp ([[behavioural-options]]), đặc biệt là rủi ro người vay trả nợ trước hạn (prepayment risk trên danh mục cho vay mua nhà) và rủi ro cam kết hạn mức tín dụng (pipeline risk) [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

## Phân loại Cốt lõi của Swaption

### 1. Phân loại theo Quyền thực thi
- **Payer Swaption (Right to Pay Fixed)**:
  - Trao quyền cho người nắm giữ được tham gia vào một hợp đồng IRS với vị thế **trả lãi suất cố định $K$ và nhận lãi suất thả nổi** [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
  - *Hành vi giá trị*: Tương tự một quyền chọn mua (Call option on swap rate / Put option on bond price). Khi lãi suất swap trên thị trường $S_n$ tăng cao hơn giá thực hiện $K$ ($S_n > K$), Payer Swaption ở trạng thái In-the-Money (ITM).
  - *Ứng dụng ALM*: Bảo vệ ngân hàng khỏi rủi ro lãi suất tăng vọt khi ngân hàng dự kiến sẽ phải phát hành trái phiếu dài hạn trong tương lai hoặc dự kiến giải ngân các khoản vay lãi suất cố định.
- **Receiver Swaption (Right to Receive Fixed)**:
  - Trao quyền cho người nắm giữ được tham gia vào một hợp đồng IRS với vị thế **nhận lãi suất cố định $K$ và trả lãi suất thả nổi** [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
  - *Hành vi giá trị*: Tương tự một quyền chọn bán (Put option on swap rate / Call option on bond price). Khi lãi suất swap thị trường $S_n$ giảm xuống dưới mức $K$ ($S_n < K$), Receiver Swaption ở trạng thái ITM.
  - *Ứng dụng ALM*: Công cụ phòng ngừa hoàn hảo đối với hiện tượng trả nợ trước hạn (prepayment).

### 2. Phân loại theo Phong cách Thực thi (Exercise Style)
- **European Swaption**: Chỉ được thực hiện quyền duy nhất vào ngày đáo hạn hợp đồng.
- **Bermudan Swaption**: Có thể được thực hiện quyền tại một tập hợp các ngày cụ thể định trước (thường trùng với các ngày thanh toán định kỳ của hợp đồng swap cơ sở).
  - *Ý nghĩa ALM*: Đa số các khoản cho vay thế chấp cho phép khách hàng trả nợ trước hạn tại bất kỳ thời điểm nào. Do đó, việc nắm giữ Bermudan Receiver Swaption cung cấp cấu trúc dòng tiền đối ứng gần như hoàn hảo để trung hòa [[convexity|tính lồi âm]] (negative convexity) của danh mục tín dụng thế chấp [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

## Ứng dụng Quản trị ALM Chuyên sâu

### 1. Phòng ngừa Rủi ro Trả nợ trước hạn (Prepayment Hedging)
- Các khoản cho vay mua nhà cố định lãi suất 15–30 năm bản chất chứa đựng một quyền chọn trả trước ngầm định (embedded prepayment option) trao cho người vay [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- Khi lãi suất thị trường giảm sâu:
  - Người vay ồ ạt tái tài trợ (refinance) ở mức lãi suất thấp hơn, làm dòng tiền thu hồi vốn gốc của ngân hàng tăng đột biến đúng thời điểm lãi suất tái đầu tư thấp nhất.
  - Vị thế tài sản của ngân hàng bị co cụm thời lượng (duration contraction) và chịu tính lồi âm ([[behavioural-options]]).
- *Giải pháp*: Ngân hàng mua các hợp đồng **Receiver Swaption**. Khi lãi suất giảm, giá trị Receiver Swaption tăng mạnh, bù đắp trực tiếp tổn thất sụt giảm dòng thu lãi trên danh mục cho vay.

### 2. Phòng ngừa Rủi ro Cam kết Giải ngân (Mortgage Pipeline Risk)
- Khi ngân hàng phát hành cam kết cho vay lãi suất cố định trong thời gian 30–60 ngày chờ giải ngân (loan commitment pipeline):
  - Nếu lãi suất tăng trước khi giải ngân: Giá trị kinh tế của khoản vay giảm, ngân hàng chịu lỗ ngay khi khoản vay được ghi nhận trên sổ sách.
  - Nếu lãi suất giảm: Khách hàng có xu hướng từ bỏ cam kết để đi vay nơi khác có lãi suất rẻ hơn.
- Ngân hàng sử dụng Swaption để phòng ngừa bất đối xứng này mà không làm phát sinh trạng thái rủi ro ngược chiều nếu cam kết bị hủy bỏ.

## Định giá Swaption theo Mô hình Black-76

Giá trị của một European Receiver Swaption với kỳ hạn quyền chọn $T_{\text{exp}}$, kỳ hạn swap cơ sở $T_n - T_{\text{exp}}$, lãi suất thực hiện $K$ được định giá bằng công thức Black-76:
$$V_{\text{rec}}(0) = N \cdot A(0) \cdot \left[ K \cdot \Phi(-d_2) - S(0) \cdot \Phi(-d_1) \right]$$
Trong đó:
- $S(0)$ là lãi suất hoán đổi kỳ hạn (Forward Swap Rate) tại thời điểm hiện tại:
  $$S(0) = \frac{DF(0, T_{\text{exp}}) - DF(0, T_n)}{A(0)}$$
- $A(0)$ là hệ số tích lũy niên kim (Annuity factor / PV01 của swap cơ sở):
  $$A(0) = \sum_{i=1}^m \tau_i \cdot DF(0, T_i)$$
- $d_1 = \frac{\ln(S(0)/K) + \frac{1}{2}\sigma_{\text{swap}}^2 T_{\text{exp}}}{\sigma_{\text{swap}} \sqrt{T_{\text{exp}}}}, \quad d_2 = d_1 - \sigma_{\text{swap}} \sqrt{T_{\text{exp}}}$
- $\sigma_{\text{swap}}$ là độ biến động ngầm định bề mặt swaption (Swaption Volatility Surface theo ma trận Option Expiry $\times$ Swap Tenor).

## Đo lường Rủi ro theo Khuôn khổ Chuẩn hoá Basel d368
Tương tự Cap và Floor, các vị thế Swaption độc lập hoặc Swaption nhúng trong các khoản nợ cấu trúc (như callable/putable wholesale debt) chịu sự chi phối của cấu phần phụ trội rủi ro tự động **$\text{KAO}_{i,c}$** [[src-bcbs-irrbb-2016#^irrbb-u05-7]]:
- Các vị thế bán Swaption (Short Swaption) phải được đánh giá lại dưới mức tăng 25% của bề mặt biến động ngầm định kết hợp với 6 kịch bản sốc lãi suất của Basel [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
- Toàn bộ chênh lệch suy giảm giá trị hợp lý được cộng vào tổn thất $\Delta\text{EVE}$ của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
