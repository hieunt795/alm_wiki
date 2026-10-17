---
title: "Mô Hình Bảng Cân Đối Tái Định Giá (Repricing Balance Sheet)"
aliases: [Repricing Balance Sheet, Bảng cân đối tái định giá, Repricing Schedule, Thang tái định giá lãi suất, Repricing Gap Schedule]
type: model
domains: [alm, basel]
status: active
maturity: draft
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-tata-bank-alm#^tata-gap-1]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-tata-bank-alm#^tata-nii-1]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-tata-bank-alm#^tata-ev-1]]"}
  - {type: input-to, to: "[[irrbb-standardised-framework]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: input-to, to: "[[duration-gap-model]]", cite: "[[src-tata-bank-alm#^tata-dgap-1]]"}
  - {type: input-to, to: "[[balance-sheet-optimisation-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u04-13]]"}
tags: [irrbb, model, repricing-balance-sheet, repricing-gap, cash-flow-slotting, reset-date, time-bands, alm]
updated: 2026-10-17
reviewed:
---

## Mục tiêu

Bảng cân đối tái định giá (Repricing Balance Sheet / Repricing Schedule) là mô hình lượng hóa nền tảng trong Quản trị Tài sản Có - Tài sản Nợ (ALM), dùng để tái cấu trúc toàn bộ Bảng cân đối kế toán từ góc nhìn kỳ hạn hợp đồng danh nghĩa (*contractual maturity*) sang góc nhìn **kỳ hạn tái định giá lãi suất (*repricing maturity / reset date*)** [[src-bcbs-irrbb-2016#^irrbb-u05-2]] [[src-tata-bank-alm#^tata-gap-1]].

Mô hình này là đầu vào bắt buộc để:
1. Xác định Khe hở định giá lại ròng (Net Repricing Gap) trên từng dải kỳ hạn [[src-tata-bank-alm#^tata-gap-1]].
2. Lượng hóa độ nhạy của Thu nhập lãi thuần ([[net-interest-income-sensitivity|$\Delta\text{NII}$]]) trong chân trời 12–36 tháng [[src-bcbs-irrbb-2016#^irrbb-p08-3]] [[src-tata-bank-alm#^tata-nii-1]].
3. Lượng hóa biến động của Giá trị kinh tế của Vốn chủ sở hữu ([[economic-value-of-equity|$\Delta\text{EVE}$]]) theo mô hình khe hở thời lượng ([[duration-gap-model|Duration Gap]]) và khuôn khổ chuẩn hóa [[irrbb-standardised-framework|Basel d368 Stage 2]] [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-tata-bank-alm#^tata-dgap-1]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    CHUYỂN ĐỔI TỪ BẢNG CÂN ĐỐI KẾ TOÁN SANG REPRICING BALANCE SHEET              │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│  BẢNG CÂN ĐỐI KẾ TOÁN (ACCOUNTING BS)         │     REPRICING BALANCE SHEET (ALM)               │
│  - Phân loại: Tài sản, Nợ, Vốn CSH            │     - Lọc phạm vi: Chỉ giữ Banking Book         │
│  - Kỳ hạn: Đáo hạn hợp đồng (Maturity)        │     - Kỳ hạn: Ngày Reset Date tiếp theo         │
│  - Định giá: Giá trị phân bổ (Amortised Cost) │     - Bóc tách: Dòng tiền gốc & lãi             │
│  - Không xét ngoại bảng                       │     - Ngoại bảng: IRS (Receive Leg / Pay Leg)   │
└───────────────────────────────────────────────┴─────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   HỆ THỐNG DẢI KỲ HẠN TÁI ĐỊNH GIÁ (REPRICING TIME BANDS)                       │
│     [<1M]   [1-3M]   [3-6M]   [6-12M]   [1-2Y]   [2-3Y]   [3-4Y]   [4-5Y]   [>5Y] ... (19 TBs)  │
│  RSA: Khoản vay thả nổi (Reset 3M) ➔ Bucket 1-3M; Trái phiếu cố định 5Y ➔ Bucket 4-5Y           │
│  RSL: Tiền gửi kỳ hạn 3M ➔ Bucket 1-3M; CASA Core ➔ Mô hình hóa dàn trải qua các Buckets        │
│  OBS: Receiver Swap ➔ Nhận Cố định (+RSA Bucket 2-3Y), Trả Thả nổi (+RSL Bucket 3-6M)           │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Phạm vi Xác định: Banking Book vs. Trading Book

Theo chuẩn mực Basel d368 và phân tích của Fidelio Tata, bảng cân đối của ngân hàng được phân tách thành hai sổ với các quy định quản lý khác biệt [[src-tata-bank-alm#^tata-scope-1]] [[src-tata-bank-alm#^tata-scope-2]]:

1. **Sổ ngân hàng (Banking Book / Non-trading Book)**: Bao gồm toàn bộ các giao dịch và vị thế có tính chất dài hạn liên quan đến hoạt động kinh doanh khách hàng (*client business*) và việc tài trợ cho chúng, bao gồm cả vốn chủ sở hữu [[src-tata-bank-alm#^tata-scope-1]]. IRRBB chỉ điều chỉnh các vị thế thuộc sổ ngân hàng.
2. **Sổ kinh doanh (Trading Book / Regulatory Trading Book)**: Bao gồm các vị thế nắm giữ nhằm mục đích tự doanh, bán lại ngắn hạn, hưởng lợi từ biến động giá, ăn chênh lệch giá (arbitrage) hoặc phòng ngừa rủi ro cho hoạt động trading [[src-tata-bank-alm#^tata-scope-2]]. Sổ kinh doanh chịu sự điều chỉnh của rủi ro thị trường (FRTB).

### A. Danh mục Thuộc Phạm vi IRRBB (Inclusions)
Trong sổ ngân hàng, chỉ các công cụ **nhạy cảm với lãi suất (Interest rate-sensitive instruments)** mới được đưa vào Repricing Balance Sheet [[src-tata-bank-alm#^tata-scope-3]]:
- **Tài sản nội bảng**:
  - Dư nợ cho vay khách hàng (Cho vay bán lẻ, mua nhà thế chấp, cho vay doanh nghiệp, thấu chi).
  - Chứng khoán nợ đầu tư nắm giữ đến ngày đáo hạn (HTM / Amortised Cost) và sẵn sàng để bán (FVOCI / AFS) thuộc sổ ngân hàng [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
  - Tiền gửi và cho vay liên ngân hàng, các giao dịch mua lại (repo) phục vụ quản trị thanh khoản hạch toán theo giá trị phân bổ.
  - Dự trữ thanh khoản và tiền gửi tại Ngân hàng Trung ương.
- **Nợ phải trả nội bảng**:
  - Tiền gửi khách hàng có kỳ hạn (Term deposits).
  - Tiền gửi không kỳ hạn ([[non-maturity-deposits|NMDs / CASA]]), bao gồm cả tiền gửi không trả lãi (*non-remunerated deposits*).
  - Tiền gửi và vay mượn từ các tổ chức tín dụng khác, repo huy động vốn.
  - Công cụ nợ phát hành (Giấy tờ có giá, trái phiếu thường, trái phiếu thứ cấp đủ điều kiện vốn cấp 2).
- **Khoản mục ngoại bảng (Off-balance sheet items)**:
  - Phái sinh lãi suất phòng ngừa rủi ro ([[interest-rate-swap|IRS]], OIS, FRAs, Futures, [[interest-rate-cap-floor|Caps/Floors]], [[swaption|Swaptions]]) [[src-tata-bank-alm#^tata-scope-5]].
  - Cam kết tín dụng và hạn mức cấp vốn chưa giải ngân (*undrawn credit commitments*) chịu rủi ro đường ống giải ngân (*pipeline risk*) [[src-choudhry-principles-banking#^choudhry-irrbb-6]].

### B. Danh mục Loại trừ Bắt buộc (Exclusions)
Các khoản mục sau đây bị loại trừ hoàn toàn khỏi Repricing Balance Sheet [[src-bcbs-irrbb-2016#^irrbb-u05-2]] [[src-tata-bank-alm#^tata-scope-4]]:
1. **Các vị thế thuộc Sổ kinh doanh (Trading Book)**.
2. **Vốn cấp 1 phổ thông (CET1 Capital)**: Loại trừ khỏi tính toán phơi nhiễm EVE vì vốn chủ sở hữu là giá trị thặng dư ròng giữa tài sản và nợ [[src-bcbs-irrbb-2016#^irrbb-p08-2]] [[src-tata-bank-alm#^tata-nii-5]].
3. **Các tài sản bị khấu trừ khỏi CET1**: Bất động sản trực tiếp, tài sản cố định vô hình (phần mềm), lợi thế thương mại (goodwill), tài sản thuế hoãn lại (DTA) [[src-tata-bank-alm#^tata-scope-4]].
4. **Khoản đầu tư cổ phần sổ ngân hàng (Equity exposures)**: Cổ phiếu chưa niêm yết, quỹ đầu tư không có báo giá hàng ngày [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
5. **Các khoản mục phi tài chính hoặc không nhạy cảm với lãi suất**: Tiền mặt tại quỹ (về mặt kinh tế không hưởng lãi và không thay đổi theo đường cong lãi suất), các khoản phải thu/phải trả thương mại ngắn hạn [[src-tata-bank-alm#^tata-nii-5]].

---

## Quy Trình 5 Bước Chuyển Đổi Kế Toán Sang Repricing Balance Sheet

Theo phương pháp luận của Fidelio Tata (2025) và chuẩn mực Basel d368, việc xây dựng Repricing Balance Sheet được thực thi qua 5 bước tuần tự [[src-tata-bank-alm#^tata-gap-1]]:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    QUY TRÌNH 5 BƯỚC XÂY DỰNG REPRICING BALANCE SHEET                            │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 1: TẬP HỢP DANH MỤC VÀO CÁC NHÓM SẢN PHẨM ĐỒNG NHẤT (PRODUCT AGGREGATION)                  │
│ ➔ Bóc tách bảng cân đối thành các nhóm: Cho vay, Trái phiếu, Tiền gửi kỳ hạn, CASA, Phái sinh   │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 2: XÁC ĐỊNH CHU KỲ TÁI ĐỊNH GIÁ (ASSIGN RESET PERIODS) — QUY TẮC RESET DATE               │
│ ➔ Cố định: Theo kỳ hạn còn lại; Thả nổi: Theo ngày reset lãi suất tiếp theo (Next Reset Date)    │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 3: TRẢI DÒNG TIỀN VÀO CÁC DẢI KỲ HẠN TÁI ĐỊNH GIÁ (CASH FLOW SLOTTING)                     │
│ ➔ Phân bổ vào 19 Time Bands (Basel) hoặc 8-12 Buckets (Nội bộ); Điều chỉnh CASA, CPR, TDRR      │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 4: TÍNH TOÁN KHE HỞ ĐỊNH GIÁ LẠI RÒNG (NET REPRICING GAPS)                                 │
│ ➔ Xác định Periodic Gap = RSA - RSL + OBS và Cumulative Gap tại từng mốc thời gian              │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 5: LƯỢNG HÓA TÁC ĐỘNG RỦI RO (WEIGHT & AGGREGATE SENSITIVITIES)                            │
│ ➔ Tính toán Độ nhạy Thu nhập ΔNII (12-36 tháng) và Độ nhạy Giá trị kinh tế ΔEVE (Duration Gap) │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Bước 1: Tập Hợp Danh Mục Thành Các Nhóm Sản Phẩm (Product Aggregation)
Toàn bộ các tài khoản kế toán chi tiết (General Ledger — GL) được làm sạch, loại bỏ các khoản mục phi nhạy cảm và gộp thành các nhóm sản phẩm đồng nhất về đặc tính dòng tiền và lãi suất:
- Bên Tài sản: Trái phiếu chính phủ cố định, Khoản vay khách hàng lãi suất cố định, Khoản vay thả nổi (theo kỳ hạn reset 1M, 3M, 6M), Thấu chi.
- Bên Nợ phải trả: Tiền gửi tiết kiệm có kỳ hạn, Tiền gửi thanh toán/CASA, Vay mượn liên ngân hàng.
- Vị thế Ngoại bảng: Hợp đồng hoán đổi lãi suất (IRS), Hợp đồng tương lai lãi suất (Futures), Cam kết hạn mức tín dụng.

### Bước 2: Xác Định Chu Kỳ Tái Định Giá (Assign Reset Periods)
Đây là nguyên tắc kinh tế quan trọng nhất được Fidelio Tata nhấn mạnh: **Rủi ro lãi suất chỉ tính đến ngày thiết lập lại lãi suất tiếp theo (*next reset date*), không tính đến ngày đáo hạn hợp đồng (*contractual maturity date*)** [[src-tata-bank-alm#^tata-gap-2]].
- **Công cụ lãi suất cố định (Fixed-rate instruments)**: Lãi suất giữ nguyên suốt kỳ hạn, do đó ngày tái định giá trùng với ngày đáo hạn gốc hoặc lịch hoàn trả gốc từng phần.
- **Công cụ lãi suất thả nổi (Floating-rate instruments)**: Dù kỳ hạn hợp đồng kéo dài 5 hay 10 năm, nếu lãi suất được định kỳ thiết lập lại mỗi 3 tháng một lần (3M reset), thì sau khi reset theo lãi suất thị trường, công cụ sẽ giao dịch lại theo đúng mệnh giá (*par value*) [[src-tata-bank-alm#^tata-gap-2]]. Vì vậy, kỳ hạn phơi nhiễm rủi ro định giá lại chỉ tối đa là 3 tháng!

### Bước 3: Trải Dòng Tiền Vào Dải Kỳ Hạn Tái Định Giá (Cash Flow Slotting)
Phân bổ dòng tiền gốc và lãi tái định giá danh nghĩa vào hệ thống dải kỳ hạn chuẩn:
- **Khuôn khổ Chuẩn hóa Basel d368**: Quy định **19 dải kỳ hạn chuẩn** (từ Overnight, 1M, 3M, 6M, 9M, 1Y, 1.5Y... đến >20Y) [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
- **Mô hình Quản trị ALM Nội bộ**: Thường gom cụm thành 8 đến 12 dải kỳ hạn (vd: <1M, 1–3M, 3–6M, 6–12M, 1–2Y, 2–3Y, 3–4Y, 4–5Y, >5Y).

#### Xử lý các cấu phần phi kỳ hạn và quyền chọn hành vi:
1. **Tiền gửi không kỳ hạn (NMDs / CASA)**:
   - Tách thành hai cấu phần: Tiền gửi phi lõi (*Non-core deposits*) phân bổ 100% vào dải ngắn nhất (<1 tháng / qua đêm) do có thể rút bất kỳ lúc nào; Tiền gửi lõi (*Core deposits*) được mô hình hóa hành vi và phân bổ dàn trải qua các kỳ hạn trung dài hạn (áp trần kỳ hạn bình quân 4,5–5 năm theo Bảng 2 Basel d368) [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
2. **Cho vay có quyền trả nợ trước hạn (Prepayment / CPR)**:
   - Dòng tiền gốc nhận về sớm hơn hợp đồng được đẩy về các dải kỳ hạn ngắn dựa trên tỷ lệ CPR mô hình hóa theo từng kịch bản sốc lãi suất [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
3. **Tiền gửi kỳ hạn rút trước hạn (Early Redemption / TDRR)**:
   - Phần tiền gửi dự kiến rút sớm được điều chỉnh rơi vào các dải kỳ hạn sớm hơn dựa trên hệ số TDRR [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
4. **Xử lý phái sinh ngoại bảng (IRS Legs)**:
   - Một hợp đồng hoán đổi lãi suất được tách thành 2 chân: Chân nhận (Receive Leg) và Chân trả (Pay Leg).
   - *Ví dụ*: Fidelio Tata minh hoạ một receiver swap kỳ hạn 3 năm, notional EUR 100, chân cố định 4.16%, chân thả nổi ban đầu 3.95% và tái định giá mỗi sáu tháng [[src-tata-bank-alm#^tata-nii-15]]. Thêm swap này vào phân tích giá trị kinh tế làm repricing gap tăng từ 1.74 lên 3.63 [[src-tata-bank-alm#^tata-nii-10]].
   - *Diễn giải:* theo nguyên tắc reset date [[src-tata-bank-alm#^tata-gap-2]], chân nhận cố định 3 năm rơi vào RSA dải 24–36 tháng, còn chân trả thả nổi reset 6 tháng rơi vào RSL dải 3–6 tháng. Table 2.35 của nguồn (bản convert bị lỗi định dạng) cũng xếp hai chân vào hai dải này.

### Bước 4: Tính Toán Khe Hở Định Giá Lại Ròng (Net Repricing Gaps)
Tại mỗi dải kỳ hạn thứ $k$:
$$\text{GAP}_k = \text{RSA}_k - \text{RSL}_k + \text{OBS}_k$$
- **Khe hở kỳ hạn định kỳ (Periodic Repricing Gap)**: Đo lường mức độ mất cân đối ròng phát sinh trong dải kỳ hạn đó [[src-tata-bank-alm#^tata-gap-1]].
  - $\text{GAP}_k > 0$: Nhạy cảm tài sản (Asset-sensitive), hưởng lợi khi lãi suất tăng trong kỳ [[src-choudhry-principles-banking#^choudhry-irrbb-5]].
  - $\text{GAP}_k < 0$: Nhạy cảm nợ (Liability-sensitive), hưởng lợi khi lãi suất giảm nhưng chịu tổn thất khi lãi suất tăng [[src-choudhry-principles-banking#^choudhry-irrbb-5]].
- **Khe hở lũy kế (Cumulative Repricing Gap)**:
  $$\text{CGAP}_K = \sum_{k=1}^K \text{GAP}_k$$
  Thể hiện tổng phơi nhiễm tái định giá tích lũy từ thời điểm hiện tại đến cuối kỳ hạn $K$.

### Bước 5: Lượng Hóa Tác Động Rủi Ro (Weight & Aggregate)
1. **Lượng hóa Độ nhạy Thu nhập ($\Delta\text{NII}$)** trong chân trời 12 tháng (earning gap), với $t_k$ là điểm giữa dải $k$ tính theo tháng [[src-tata-bank-alm#^tata-egap-1]]:
   $$\Delta\text{NII}_{12M} = \sum_{k=1}^m \text{GAP}_k \cdot \Delta r_k \cdot \left( \frac{12 - t_k}{12} \right)$$
2. **Lượng hóa Độ nhạy Giá trị kinh tế ($\Delta\text{EVE}$)**:
   Mỗi khe hở ròng $\text{GAP}_k$ được nhân với mức giảm giá trị kinh tế ước tính khi lãi suất tăng 1%, dựa trên modified duration $D^*_k$ của tài sản và nợ trong dải; cộng dồn các khe hở có trọng số cho ra total repricing gap, tức mức giảm EVE ứng với 1% lãi suất tăng song song [[src-tata-bank-alm#^tata-gap-3]]:
   $$\Delta\text{EVE} \approx - \sum_{k=1}^n \text{GAP}_k \cdot D^*_k \cdot \Delta y$$

---

## Mô Hình Minh Họa Số Học (Model Bank của Fidelio Tata)

Để thấy rõ cơ chế vận hành của Repricing Balance Sheet, xét Bảng cân đối của một ngân hàng mô hình có Tổng tài sản bằng 500 và Vốn chủ sở hữu bằng 50 [[src-tata-bank-alm#^tata-gap-4]]. Nguồn không ghi đơn vị tiền tệ cho ví dụ này.

### 1. Bảng Cân Đối Kế Toán Theo Kỳ Hạn Hợp Đồng (Contractual Balance Sheet)
Quy mô theo Table 2.2 [[src-tata-bank-alm#^tata-gap-4]], kỳ hạn hợp đồng theo Table 2.3 [[src-tata-bank-alm#^tata-gap-5]].

| Tài sản (Assets) | Quy mô | Kỳ hạn hợp đồng | Nợ & Vốn (Liabilities & Equity) | Quy mô | Kỳ hạn hợp đồng |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Trái phiếu (Bonds)** | 50 | 60 tháng (5 năm) | **Tiền gửi kỳ hạn (Term deposits)** | 150 | 3 tháng |
| **Khoản cho vay (Loans)** | 300 | 6 tháng | **Tài khoản tiết kiệm (Savings)** | 200 | 36 tháng |
| **Cho vay thế chấp (Mortgages)** | 150 | 60 tháng (5 năm) | **Tiền gửi liên ngân hàng (Interbank)** | 100 | 24 tháng |
| | | | **Vốn chủ sở hữu (Equity)** | 50 | Không kỳ hạn |
| **Tổng tài sản** | **500** | | **Tổng nợ & Vốn** | **500** | |

### 2. Chu Kỳ Thiết Lập Lại Lãi Suất Thực Tế (Reset Periods)
Nguồn ghi đây là chu kỳ tái định giá bình quân ước tính [[src-tata-bank-alm#^tata-gap-5]]:
- Trái phiếu (Bonds): kỳ hạn 60 tháng, reset period = 60 tháng.
- Khoản cho vay (Loans): kỳ hạn 6 tháng, reset period = 6 tháng.
- Cho vay thế chấp (Mortgages): kỳ hạn 60 tháng nhưng **reset period = 12 tháng**.
- Tiền gửi kỳ hạn (Term deposits): kỳ hạn 3 tháng, reset period = 3 tháng.
- Tài khoản tiết kiệm (Savings accounts): kỳ hạn 36 tháng nhưng **reset period = 6 tháng**.
- Tiền gửi liên ngân hàng (Interbank deposits): kỳ hạn 24 tháng, reset period = 24 tháng.
- Vốn chủ sở hữu: không được phân bổ vào dải tái định giá nào [[src-tata-bank-alm#^tata-gap-6]].

### 3. Bảng Cân Đối Tái Định Giá (Repricing Balance Sheet)
Phân bổ khối lượng tài sản và nợ vào các dải kỳ hạn tái định giá theo Table 2.4–2.5 [[src-tata-bank-alm#^tata-gap-6]]. Dòng Cumulative Gap do wiki tự cộng dồn, nguồn không có.

| Khoản mục | <1M | 1–3M | 3–6M | 6–12M | 12–24M | 24–36M | 36–48M | 48–60M | Tổng |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **TÀI SẢN (RSA)** | | | | | | | | | |
| Trái phiếu (Bonds) | — | — | — | — | — | — | — | 50 | 50 |
| Cho vay (Loans) | — | — | 300 | — | — | — | — | — | 300 |
| Cho vay thế chấp (Mortgages) | — | — | — | 150 | — | — | — | — | 150 |
| **Tổng RSA** | **0** | **0** | **300** | **150** | **0** | **0** | **0** | **50** | **500** |
| **NỢ PHẢI TRẢ (RSL)** | | | | | | | | | |
| Tiền gửi kỳ hạn (Term deposits) | — | 150 | — | — | — | — | — | — | 150 |
| Tiết kiệm (Savings accounts) | — | — | 200 | — | — | — | — | — | 200 |
| Liên ngân hàng (Interbank) | — | — | — | — | 100 | — | — | — | 100 |
| **Tổng RSL** | **0** | **150** | **200** | **0** | **100** | **0** | **0** | **0** | **450** |
| **NET REPRICING GAP** | **0** | **-150** | **+100** | **+150** | **-100** | **0** | **0** | **+50** | **+50** |
| **CUMULATIVE GAP** | **0** | **-150** | **-50** | **+100** | **0** | **0** | **0** | **+50** | — |

### Nhận xét phân tích:
- **Góc nhìn EVE (mục đích chính của ví dụ trong nguồn)**: sau khi nhân khe hở với trọng số duration, total repricing gap bằng 1.74, nghĩa là EVE giảm 1.74 khi lãi suất tăng 1%; với vốn 50, mức này tương đương 3.48% vốn cho mỗi 100 bp [[src-tata-bank-alm#^tata-gap-7]].
- **Góc nhìn NII năm đầu (earning gap)**: dải 1–3 tháng có $\text{GAP} = -150$, tức nhạy cảm nợ: tiền gửi kỳ hạn 150 tái định giá trước mọi tài sản. Các periodic earning gap ứng với 1% lãi suất tăng là −1.25 (dải 1–3M), +0.625 (dải 3–6M) và +0.375 (dải 6–12M) [[src-tata-bank-alm#^tata-egap-1]]. Total earning gap bằng −0.25, nghĩa là NII năm đầu **giảm** 0.25 cho mỗi 1% lãi suất tăng song song [[src-tata-bank-alm#^tata-egap-2]].
- *Diễn giải:* $\text{CGAP}_{12M} = +100$ dương nhưng NII năm đầu vẫn giảm khi lãi suất tăng. Lý do là khe hở âm ở dải 1–3 tháng chịu tác động gần trọn năm (10/12), còn khe hở dương ở dải 6–12 tháng chỉ chịu tác động 3/12 năm. Vì vậy dấu của khe hở lũy kế không đủ để kết luận chiều biến động NII nếu không tính đến thời điểm tái định giá.

---

## Hạn Chế Của Mô Hình Repricing Balance Sheet

Mặc dù là công cụ trực quan và phổ biến nhất, Repricing Balance Sheet có một số giới hạn kỹ trị mà ALM phải bổ sung bằng các mô hình nâng cao:

1. **Giả định dịch chuyển song song (Parallel Shift Trap)**: Mô hình ngầm định lãi suất tại mọi kỳ hạn đều thay đổi cùng một biên độ. Nó không nắm bắt được rủi ro biến dạng đường cong (**Yield Curve Risk** như làm dốc Steepener hoặc phẳng Flattener) [[src-choudhry-principles-banking#^choudhry-irrbb-4]].
2. **Bỏ qua Rủi ro Cơ sở (Basis Risk)**: Hai công cụ cùng rơi vào dải 3–6 tháng nhưng tài sản neo theo SOFR còn nợ neo theo lãi suất huy động điều hành; khi hai chỉ số này phân kỳ, khe hở bằng 0 trên bảng vẫn gây tổn thất nặng cho NII [[src-choudhry-principles-banking#^choudhry-irrbb-4]].
3. **Bỏ qua giá trị thời gian của tiền trong từng dải**: Dòng tiền ở đầu tháng 7 và cuối tháng 12 cùng nằm trong dải 6–12 tháng nhưng có hiện giá chiết khấu khác nhau.
4. **Phụ thuộc vào giả định hành vi (Behavioral Risk)**: Việc ấn định kỳ hạn tái định giá cho CASA hay tỷ lệ trả nợ trước hạn (CPR) chỉ là ước tính; nếu hành vi khách hàng đột ngột thay đổi (như rút tiền hàng loạt trong kỷ nguyên số), toàn bộ cấu trúc Repricing Schedule sẽ bị phá vỡ.

---

## Xem Thêm
- Xem phân tích chuyên sâu về ba phương pháp xác định Repricing Profile (Contractual vs Reset vs Behavioral Maturity) và khung mô hình hóa hành vi tại [[irrbb-repricing-profiles-and-behavioral-modeling]].
- Xem phương pháp đo lường EVE và NII dưới 6 kịch bản sốc lãi suất chuẩn hóa tại [[irrbb-standardised-shocks-eve-and-nii-measurement]].
- Xem mô hình danh mục sao chép (Replicating Portfolio) cho tiền gửi CASA và kỹ thuật phòng ngừa rủi ro bằng IRS tại [[irrbb-casa-replicating-portfolio-and-irs-hedging]].
- Xem cơ chế truyền dẫn của các cấu phần IRRBB đến NII và EVE tại [[irrbb-transmission-mechanisms-to-nii-and-eve]].
- Xem phương pháp xác định và phân bổ dòng tiền gốc (Principal) và dòng tiền lãi (Interest) của từng portfolio vào 19 dải kỳ hạn tại [[irrbb-principal-and-interest-cash-flows]].
- Xem mô hình tối ưu hóa cấu trúc tài sản - nợ phi tuyến ràng buộc bất đẳng thức tại [[balance-sheet-optimisation-model]].



