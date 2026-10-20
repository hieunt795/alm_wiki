---
title: "Interest Rate Swap (IRS — Hợp đồng hoán đổi lãi suất)"
aliases: [IRS, Interest Rate Swap, Hoán đổi lãi suất, Payer Swap, Receiver Swap, Basis Swap]
type: instrument
domains: [product, alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tata-bank-alm]]"]
relations:
  - {type: hedges, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-3]]"}
  - {type: hedges, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-8]]"}
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-5]]"}
  - {type: hedges, to: "[[net-interest-income-sensitivity]]", cite: "[[src-tata-bank-alm#^tata-nii-16]]"}
tags: [irrbb, instrument, irs, payer-swap, receiver-swap, duration-hedging, basis-swap]
updated: 2026-10-20
reviewed:
---

## Khái niệm và Định nghĩa
Hợp đồng hoán đổi lãi suất (Interest Rate Swap - IRS) là một công cụ tài chính phái sinh phi tập trung (OTC) giữa hai bên nhằm trao đổi các dòng tiền lãi suất trong tương lai dựa trên một khoản vốn gốc danh nghĩa (notional principal) được xác định trước, mà không có sự chuyển giao vốn gốc thực tế [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

Trong hoạt động quản trị cân đối Tài sản - Nợ (ALM) của ngân hàng, IRS là công cụ phòng ngừa rủi ro (hedging instrument) chủ lực để tái cấu trúc thời lượng bảng cân đối kế toán, triệt tiêu rủi ro chênh lệch kỳ hạn [[gap-risk]], bảo vệ giá trị kinh tế của vốn chủ sở hữu [[economic-value-of-equity|$\Delta\text{EVE}$]] và bình ổn thu nhập lãi thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]] [[src-bcbs-irrbb-2016#^irrbb-p12-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

## Các cấu trúc IRS phổ biến trong ALM Ngân hàng

### 1. Plain Vanilla Fixed-for-Floating Swap
Cấu trúc cơ bản nhất gồm một vế trả lãi suất cố định (fixed rate) và một vế nhận lãi suất thả nổi (floating rate, ví dụ SOFR, Euribor, VNIBOR) hoặc ngược lại:
- **Payer Swap (Pay-Fixed Swap)**:
  - Ngân hàng trả lãi suất cố định $R_{\text{fix}}$ và nhận lãi suất thả nổi $R_{\text{flt}}$.
  - *Đặc tính thời lượng*: Payer swap mang thời lượng âm ($\text{Duration}_{\text{payer}} \approx -D_{\text{fix}} + D_{\text{flt}} < 0$). Giá trị thị trường của swap tăng khi lãi suất tăng và giảm khi lãi suất giảm.
  - *Ứng dụng ALM*: Sử dụng khi ngân hàng có chênh lệch thời lượng dương ($D_A > D_L$, ví dụ nắm giữ danh mục Trái phiếu Chính phủ hoặc cho vay trung dài hạn lãi suất cố định tài trợ bằng tiền gửi ngắn hạn). Payer swap giúp rút ngắn thời lượng tài sản, phòng ngừa tổn thất $\Delta\text{EVE}$ khi lãi suất thị trường tăng vọt [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
- **Receiver Swap (Receive-Fixed Swap)**:
  - Ngân hàng nhận lãi suất cố định $R_{\text{fix}}$ và trả lãi suất thả nổi $R_{\text{flt}}$.
  - *Đặc tính thời lượng*: Receiver swap mang thời lượng dương ($\text{Duration}_{\text{receiver}} \approx D_{\text{fix}} - D_{\text{flt}} > 0$). Giá trị swap tăng khi lãi suất giảm.
  - *Ứng dụng ALM*: Sử dụng khi ngân hàng có chênh lệch thời lượng âm hoặc dư thừa tiền gửi kỳ hạn cố định dài hạn tài trợ cho các khoản vay thả nổi ngắn hạn, giúp khóa chặt biên lãi ròng [[net-interest-margin|NIM]] khi lãi suất bước vào chu kỳ nới lỏng [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

### 2. Basis Swap (Hoán đổi cơ sở)
- Trao đổi hai dòng tiền lãi suất cùng thả nổi nhưng neo vào hai chỉ số tham chiếu hoặc kỳ hạn tái định giá khác nhau (ví dụ: SOFR 1 tháng vs SOFR 3 tháng, Prime rate vs SOFR, hoặc Fed Funds vs SOFR) [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
- *Ứng dụng ALM*: Triệt tiêu [[basis-risk]] khi tài sản sinh lời và nợ phải trả có cùng tần suất tái định giá nhưng biến động lệch pha do neo theo các chỉ số thị trường khác nhau.

### 3. Overnight Index Swap (OIS)
Node riêng: [[overnight-index-swap]]. Phân biệt với hoán đổi hai đồng tiền: [[cross-currency-swap]] trao đổi cả gốc và lãi bằng hai đồng tiền [[src-choudhry-principles-banking#^choudhry-fxs-2]].
- Trao đổi lãi suất cố định lấy lãi suất qua đêm tích lũy gộp (compounded overnight rate, ví dụ SOFR, €STR).
- *Ứng dụng ALM*: Dùng làm đường cong chiết khấu chuẩn phi rủi ro (RFR discounting) để định giá giá trị hợp lý toàn bộ danh mục tài sản nhạy cảm lãi suất và đo lường $\Delta\text{EVE}$ chuẩn xác theo Basel [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

### 4. Amortising / Accreting Swap
- Vốn gốc danh nghĩa thay đổi theo thời gian theo một lịch trình định trước (giảm dần đối với amortising swap hoặc tăng dần đối với accreting swap).
- *Ứng dụng ALM*: Khớp hoàn hảo với lịch trình hoàn trả gốc định kỳ của các gói tín dụng thế chấp mua nhà (mortgages) hoặc các dự án tài trợ hạ tầng, tránh hiện tượng thừa/thiếu phòng ngừa rủi ro (over/under-hedging).

### 5. Ứng dụng phòng ngừa IRRBB cấu trúc (Choudhry)
- **Macro hedge**: pool IRS thực hiện cuối tháng; thường không áp được hedge accounting nên chịu biến động MTM [[src-choudhry-principles-banking#^choudhry-cs-14]].
- **Chính sách "chính thống"**: tài sản cố định thì vào IRS trả cố định, nợ cố định thì vào IRS nhận cố định; hạn chế là chi phí tài sản bảo đảm [[src-choudhry-principles-banking#^choudhry-cs-16]].
- **Phòng ngừa theo phần ròng**: chỉ phòng ngừa phần còn lại sau natural hedge, ưu tiên sản phẩm tiền mặt để giữ hạn mức swap [[src-choudhry-principles-banking#^choudhry-cs-17]]. Xem [[structural-hedging]].
- **Khi lãi suất âm**: coi NMD có sàn 0% là khoản fixed-rate, vào IRS nhận cố định với tenor bằng behavioural tenor; balance guarantee swap điều chỉnh notional theo số dư NMD [[src-choudhry-principles-banking#^choudhry-neg-3]]. Xem [[negative-interest-rates]].

## Định giá và Đo lường Độ nhạy Lãi suất (DV01 / PV01)

### 1. Định giá theo Nguyên tắc Không kinh doanh chênh lệch giá (No-Arbitrage)
Giá trị hiện tại của một hợp đồng Payer IRS tại thời điểm $t$ là:
$$V_{\text{payer}}(t) = \text{PV}(\text{Floating Leg}) - \text{PV}(\text{Fixed Leg})$$
Tại thời điểm khởi tạo hợp đồng ($t=0$), giá trị của swap bằng 0 ($V=0$), lãi suất cố định ngang giá (Par Swap Rate $S_n$) được xác định bằng:
$$S_n = \frac{1 - DF(0, T_n)}{\sum_{i=1}^n \tau_i \cdot DF(0, T_i)}$$
Trong đó:
- $DF(0, T_i)$ là hệ số chiết khấu phi rủi ro từ thời điểm hiện tại đến ngày thanh toán $T_i$.
- $\tau_i$ là độ dài chu kỳ tính lãi (year fraction, ví dụ Actual/360 hoặc 30/360).

### 2. Độ nhạy điểm cơ bản (DV01 / PV01)
DV01 (Dollar Value of a Basis Point) đo lường sự thay đổi giá trị thị trường của swap khi đường cong lãi suất dịch chuyển 1 điểm cơ bản (0.01% = 1 bp):
$$\text{DV01}_{\text{IRS}} \approx \text{Notional} \times \sum_{i=1}^n \tau_i \cdot DF(0, T_i) \times 0.0001$$
Quy mô danh nghĩa của IRS cần thiết để miễn nhiễm một khoản chênh lệch thời lượng bảng cân đối ($\Delta\text{EVE} = 0$) được xác định bởi:
$$\text{Notional}_{\text{hedging}} = \frac{\Delta\text{EVE}_{\text{Balance Sheet}}}{\text{DV01}_{\text{IRS, unit}}}$$

### 3. Hedge ratio theo PVBP (Choudhry)
- Swap là công cụ phòng ngừa hiệu quả vì có convexity dương; PVBP là thước đo chính để tính hedge ratio [[src-choudhry-principles-banking#^choudhry-hedge-12]].
- Ví dụ: swap 5 năm notional £1 triệu có PVBP £425, so với trái phiếu cố định £488,45; quy tắc kinh nghiệm là PVBP của swap xấp xỉ PVBP trái phiếu tính từ ngày reset kế tiếp tới đáo hạn [[src-choudhry-principles-banking#^choudhry-hedge-13]].
- Hạn chế: giả định dịch chuyển song song, nên cần dynamic hedging [[src-choudhry-principles-banking#^choudhry-hedge-14]].
- Phân loại theo mục đích: asset-linked swap và liability-linked swap [[src-choudhry-principles-banking#^choudhry-hedge-11]].

## Xử lý Kế toán và Rủi ro Ngoại bảng theo Chuẩn mực Basel

- **Ghi nhận Ngoại bảng**: Dòng tiền danh nghĩa của IRS được phân bổ vào các dải kỳ hạn thích hợp (19 dải kỳ hạn theo Khuôn khổ chuẩn hoá Basel d368) tại hai vế đối ứng (nhận thả nổi tại dải ngắn hạn và trả cố định tại dải dài hạn) để xác định trạng thái tái định giá ròng rủi ro [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
- **Kế toán phòng ngừa rủi ro ([[hedge-accounting|Hedge Accounting]])**: Choudhry nêu tiêu chí hiệu quả hồi tố 80–125% [[src-choudhry-principles-banking#^choudhry-hacc-3]]. Theo IFRS 9, ngân hàng phải chứng minh mối quan hệ kinh tế giữa công cụ IRS và danh mục mục tiêu (Fair Value Hedge đối với tài sản cố định để bảo vệ EVE, hoặc Cash Flow Hedge đối với nợ thả nổi để bảo vệ NII) [[src-bcbs-irrbb-2016#^irrbb-u06-1]].
- **Rủi ro tín dụng đối tác (Counterparty Credit Risk - CCR)**: IRS ký kết song phương phải được bù trừ qua Trung tâm thanh toán bù trừ trung tâm (CCP) hoặc ký quỹ hoán đổi (variation margin / initial margin) để giảm thiểu rủi ro vỡ nợ tín dụng theo chuẩn mực Basel [[src-bcbs-irrbb-2016#^irrbb-u06-3]].

## Đề xuất cập nhật
- [2026-10-19] ingest src-choudhry-principles-banking u25 — chờ user duyệt: thêm ứng dụng phòng ngừa IRRBB: macro hedge bằng pool IRS cuối tháng, thường không áp được hedge accounting nên chịu biến động MTM [[src-choudhry-principles-banking#^choudhry-cs-14]]; chính sách 'chính thống' (tài sản cố định → IRS trả cố định, nợ cố định → IRS nhận cố định) và hạn chế của nó (chi phí tài sản bảo đảm) [[src-choudhry-principles-banking#^choudhry-cs-16]]; phòng ngừa theo phần ròng sau natural hedge, ưu tiên sản phẩm tiền mặt để giữ hạn mức swap [[src-choudhry-principles-banking#^choudhry-cs-17]]. Link [[structural-hedging]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: thêm hedge ratio theo PVBP/DV01: swap hiệu quả vì convexity dương, PVBP là thước đo chính để tính hedge ratio [[src-choudhry-principles-banking#^choudhry-hedge-12]]; ví dụ swap 5 năm £1 triệu PVBP £425 so với trái phiếu cố định £488,45, quy tắc kinh nghiệm PVBP swap ≈ trái phiếu từ ngày reset kế tiếp tới đáo hạn [[src-choudhry-principles-banking#^choudhry-hedge-13]]; hạn chế giả định dịch chuyển song song, cần dynamic hedging [[src-choudhry-principles-banking#^choudhry-hedge-14]]. Thêm phân loại asset-linked/liability-linked swap [[src-choudhry-principles-banking#^choudhry-hedge-11]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: đã có node [[overnight-index-swap]]; đề xuất bỏ alias `OIS Swap` khỏi node này (chuyển sang node mới) và link [[overnight-index-swap]] ở mục cấu trúc IRS. Đã có node [[cross-currency-swap]] [[src-choudhry-principles-banking#^choudhry-fxs-2]]; đề xuất link ở chỗ phân biệt với IRS. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10 — chờ user duyệt: thêm ứng dụng khi lãi suất âm: coi NMD sàn 0% là fixed-rate, vào IRS nhận cố định với tenor bằng behavioural tenor; balance guarantee swap điều chỉnh notional theo số dư NMD [[src-choudhry-principles-banking#^choudhry-neg-3]]. Xem [[negative-interest-rates]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u15 — chờ user duyệt: đã có node [[hedge-accounting]] (tiêu chí áp dụng, hiệu quả hồi tố 80–125% [[src-choudhry-principles-banking#^choudhry-hacc-3]]); đề xuất link ở mục Kế toán phòng ngừa rủi ro. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]
- [2026-10-20] research nii-shocks-regulation-hedging-and-alco-tradeoffs — chờ user duyệt: thêm cạnh `{type: hedges, to: "[[net-interest-income-sensitivity]]", cite: "[[src-tata-bank-alm#^tata-nii-16]]"}` (receiver swap ổn định NII dưới sốc −100 bp). Rà lại 2 cạnh hiện có: `input-to → [[net-interest-income-sensitivity]]` cite `irrbb-u06-5` và `hedges → [[economic-value-of-equity]]` cite `irrbb-u05-8`, cả hai trích dẫn không nhắc swap; ví dụ Tata còn cho thấy receiver swap làm repricing gap EVE tăng từ 1,74 lên 3,63 [[src-tata-bank-alm#^tata-nii-10]]. → đã áp dụng [2026-10-20]
