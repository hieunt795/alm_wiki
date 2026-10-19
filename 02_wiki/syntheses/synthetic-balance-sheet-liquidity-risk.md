---
title: "Synthetic Balance Sheet — Mô hình Bảng Cân đối Mục tiêu Quản trị Rủi ro Thanh khoản LCR – NSFR"
aliases: [Synthetic Balance Sheet Liquidity Risk, Bảng cân đối tổng hợp rủi ro thanh khoản, Mô hình cân đối TSN TSC LCR NSFR, Synthetic ALM Balance Sheet, Target Liquidity Balance Sheet, Bảng cân đối thanh khoản Basel]
type: synthesis
domains: [alm, basel, product]
status: active
maturity: canonical
origin: research
question: "Làm thế nào để xây dựng một Bảng cân đối Kế toán Tổng hợp (Synthetic Balance Sheet) chuẩn mực quốc tế, mô hình hóa giải tích sự cân đối Tài sản Nợ (TSN) và Tài sản Có (TSC) nhằm thỏa mãn đồng thời hai ràng buộc thanh khoản bắt buộc LCR >= 100% và NSFR >= 100%, đồng thời tối ưu hóa lợi nhuận NIM và kiểm soát rủi ro lãi suất IRRBB?"
sources: ["[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-bcbs-irrbb-2016]]", "[[src-bcbs-lev]]", "[[src-choudhry-principles-banking]]"]
relations: []
tags: [synthetic-balance-sheet, liquidity-risk, lcr, nsfr, leverage-ratio, tsn-tsc-balance, balance-sheet-optimization, alco, term-liquidity-ftp, duration-trap, basel]
updated: 2026-10-17
reviewed:
---

## Tóm tắt Quản trị Cấp cao (Executive Summary)

Trong quản trị ALM hiện đại, **Bảng Cân đối Kế toán Tổng hợp (Synthetic / Target Balance Sheet)** không phải là một báo cáo kế toán tĩnh phản ánh lịch sử, mà là **bản thiết kế kiến trúc mục tiêu tối ưu** do Khối Nguồn vốn & Quản lý Tài sản - Nợ (ALM Treasury) và Hội đồng ALCO chủ động định hình [[src-bcbs-lcr#^lcr20-1]] [[src-bcbs-nsfr#^nsf20-1]]. 

Ngân hàng về bản chất là một thực thể chuyển đổi kỳ hạn (*maturity transformation*), thu hút nguồn vốn ngắn hạn từ người gửi tiền để tài trợ cho tài sản trung và dài hạn. Để bảo đảm hệ thống ngân hàng không sụp đổ trước các cuộc khủng hoảng thanh khoản cấp tính hay sự đổ vỡ cấu trúc nguồn vốn, Ủy ban Basel thiết lập hai chiếc "neo" giám sát song hành:
1. **Chiếc neo Ngắn hạn — [[lcr|Tỷ lệ Đảm bảo Khả năng Thanh khoản (LCR $\ge 100\%$)]]**: Kiểm soát khả năng sinh tồn trong kịch bản căng thẳng thanh khoản nghiêm trọng kéo dài 30 ngày [[src-bcbs-lcr#^lcr20-1]]. LCR quy định **Tài sản Có (TSC)** bắt buộc phải nắm giữ bao nhiêu tài sản thanh khoản cao ([[hqla|HQLA]]) dựa trên mức độ rút vốn giả định của **Tài sản Nợ (TSN)** [[src-bcbs-lcr#^lcr20-3]].
2. **Chiếc neo Dài hạn — [[nsfr|Tỷ lệ Nguồn Vốn Ổn định Ròng (NSFR $\ge 100\%$)]]**: Kiểm soát cấu trúc tài trợ bền vững trên đường chân trời 1 năm [[src-bcbs-nsfr#^nsf20-2]]. NSFR quy định **Tài sản Nợ (TSN)** phải cung cấp nguồn vốn ổn định ([[available-stable-funding|ASF]]) đủ để tài trợ cho tính kém thanh khoản của **Tài sản Có (TSC)** ([[required-stable-funding|RSF]]) [[src-bcbs-nsfr#^nsf20-2]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│               MÔ HÌNH CÂN ĐỐI TÀI SẢN NỢ (TSN) - TÀI SẢN CÓ (TSC) DỰA TRÊN LCR & NSFR           │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                     HỘI ĐỒNG ALCO & ALM TREASURY                                │
│                     Hàm mục tiêu: Cực đại hóa NIM & ROE sau điều chỉnh rủi ro                   │
├────────────────────────────────────────────────┬────────────────────────────────────────────────┤
│          TÀI SẢN CÓ (TSC - ASSETS)             │      TÀI SẢN NỢ & VỐN (TSN - LIABILITIES)       │
├────────────────────────────────────────────────┼────────────────────────────────────────────────┤
│ A1. Tiền mặt & Dự trữ NHTW (RSF 0%, L1 100%)   │ L1. CASA Bán lẻ Ổn định (ASF 95%, Run-off 5%)  │
│ A2. Trái phiếu Chính phủ Level 1 (RSF 5%, L1)  │ L2. Tiền gửi Tiết kiệm Bán lẻ (ASF 90%, 0-5%) │
│ A3. Cho vay Cá nhân Thế chấp (RSF 65%, Inflow) │ L3. Tiền gửi Doanh nghiệp Operational (ASF 50%)│
│ A4. Cho vay Doanh nghiệp / Vốn LĐ (RSF 85%)    │ L4. Vốn Bán buôn / Liên ngân hàng (ASF 0%)    │
│ A5. Tài sản Cố định & Khác (RSF 100%)          │ L5. Trái phiếu Dài hạn >= 1Y (ASF 100%)       │
│                                                │ E.  Vốn Chủ sở hữu CET1 (ASF 100%, Run-off 0%) │
├────────────────────────────────────────────────┴────────────────────────────────────────────────┤
│                                  HỆ THỐNG RÀNG BUỘC PHÁP ĐỊNH ĐỒNG THỜI                         │
│  ├── 1. Cân bằng Kế toán:  ∑ TSC = ∑ TSN + Vốn Chủ sở hữu (Total Balance Sheet Size)            │
│  ├── 2. Ràng buộc LCR:     HQLA / Net Outflows 30D ≥ 100% + Δ_LCR (Đệm an toàn mục tiêu)       │
│  ├── 3. Ràng buộc NSFR:    ASF / RSF 1Y ≥ 100% + Δ_NSFR (Đệm an toàn mục tiêu)                 │
│  ├── 4. Ràng buộc Đòn bẩy: Tier 1 Capital / Total Leverage Exposure ≥ 3% + Δ_LR                 │
│  └── 5. Ràng buộc IRRBB:   Max ΔEVE / Tier 1 Capital ≤ 15% (Outlier Bank Test, BCBS d368)       │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Khung Phương pháp luận Toán học: Mô hình Quy hoạch Tuyến tính Đa ràng buộc

Để thiết lập một bảng cân đối tổng hợp, ALM Treasury mô hình hóa toàn bộ các khoản mục tài sản và nguồn nợ dưới dạng một bài toán **Quy hoạch Tuyến tính Đa mục tiêu (Multi-Constraint Linear Programming)**:

### A. Các Biến số Danh mục
* **Tài sản Có (TSC)**: Vector quy mô tài sản $\mathbf{A} = [A_1, A_2, \dots, A_n]^T$ với tỷ suất sinh lời kỳ vọng $\mathbf{y} = [y_1, y_2, \dots, y_n]^T$.
* **Tài sản Nợ (TSN)**: Vector quy mô nợ phải trả $\mathbf{L} = [L_1, L_2, \dots, L_m]^T$ với chi phí lãi vay $\mathbf{c} = [c_1, c_2, \dots, c_m]^T$.
* **Vốn Chủ sở hữu**: Vốn tự có cấp 1 ($E = \text{CET1}$) đóng vai trò là nguồn vốn đệm vĩnh viễn.

### B. Hàm Mục tiêu (Objective Function)---

## 2. Bản chất Dòng tiền Kép của Bảng Cân đối: Phân rã Dòng Tiền Gốc (Thanh khoản & Kỳ hạn) và Dòng Tiền Lãi (Lãi suất & P&L)

### 2.1. Bản thể Luận của Bảng Cân đối: Cỗ máy Dòng tiền Kép (Dual Cash Flow Engine)

Một sai lầm phổ biến trong nhận thức kế toán truyền thống là nhìn nhận bảng cân đối kế toán như một tập hợp tĩnh các số dư tài sản và công nợ tại một thời điểm chốt sổ. Trong quản trị ALM hiện đại và toán tài chính ngân hàng, **bảng cân đối về thực chất là một Cỗ máy Tạo lập Dòng tiền Tương lai (Future Cash Flow Engine)**. 

Mọi công cụ trên bảng cân đối đều được phân rã thành hai dòng tiền bản thể độc lập về mặt quy luật nhưng gắn kết mật thiết trong cơ chế sinh tồn và khả năng sinh lời của ngân hàng:

1. **DÒNG TIỀN GỐC (Principal Cash Flows — $\mathbf{CF}^{\text{Prin}}$)**:
   * **Dòng tiền vào gốc (Principal Inflows)**: Thu hồi nợ gốc từ các tài sản sinh lời (cho vay đến hạn hoàn trả, dòng tiền trả nợ gốc định kỳ amortization, trái phiếu/GTCG đáo hạn, thu hồi tiền gửi liên ngân hàng).
   * **Dòng tiền ra gốc (Principal Outflows)**: Nghĩa vụ hoàn trả nợ gốc cho người gửi tiền và các chủ nợ (tiền gửi thanh toán CASA bị rút ra, tiền gửi tiết kiệm có kỳ hạn đáo hạn tất toán, trái phiếu/GTCG dài hạn đáo hạn, hoàn trả nợ vay liên ngân hàng).
   * **Quy luật chi phối**: Được quyết định trực tiếp bởi **Kỳ hạn Hợp đồng và Kỳ hạn Hành vi (Contractual vs Behavioural Maturity Tenor)**. Dòng tiền gốc này là đối tượng trực tiếp chi phối **Thanh khoản Nguồn vốn (Funding Liquidity)**, xác lập **Bảng Thang Kỳ hạn (Maturity Ladder / Liquidity Gap)**, cấu thành chỉ số sống còn 30 ngày [[lcr]] (Net Cash Outflows) [[src-bcbs-lcr#^lcr40-1]] và định hình cấu trúc cân đối nguồn vốn ổn định 1 năm [[nsfr]] (ASF vs RSF) [[src-bcbs-nsfr#^nsf20-2]].
2. **DÒNG TIỀN LÃI (Interest Cash Flows — $\mathbf{CF}^{\text{Int}}$)**:
   * **Dòng tiền vào lãi (Interest Inflows)**: Thu nhập lãi định kỳ từ tài sản sinh lời (tiền lãi cho vay định kỳ, lãi coupon trái phiếu đầu tư, lãi dự trữ tiền gửi tại NHTW).
   * **Dòng tiền ra lãi (Interest Outflows)**: Chi phí lãi định kỳ phải trả cho các cấu phần nợ (trả lãi tiền gửi tiết kiệm, trả lãi coupon trái phiếu phát hành, lãi vay trên thị trường tiền tệ).
   * **Quy luật chi phối**: Được quyết định trực tiếp bởi **Mặt bằng Lãi suất Thị trường, Biên độ Chênh lệch (Commercial Margin / Spread), và Tần suất / Kỳ hạn Định giá lại Lãi suất (Repricing Tenor / Reset Frequency)** [[src-bcbs-irrbb-2016#^irrbb-u02-2]]. Dòng tiền lãi này trực tiếp quyết định **Báo cáo Kết quả Hoạt động Kinh doanh (P&L)**, **Thu nhập Lãi thuần (NII)**, **Biên Lãi thuần (NIM)** [[src-bcbs-irrbb-2016#^irrbb-p08-3]] và khi chiết khấu toàn bộ dòng tiền về hiện tại sẽ quyết định **Giá trị Kinh tế của Vốn chủ sở hữu (EVE)** [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    BẢN CHẤT DÒNG TIỀN KÉP CỦA BẢNG CÂN ĐỐI KẾ TOÁN ALM                          │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                 BẢNG CÂN ĐỐI KẾ TOÁN (TSN - TSC)                                │
│                     (Cỗ máy tạo lập dòng tiền tương lai: CF_t = CF_t^Prin + CF_t^Int)           │
├────────────────────────────────────────────────┬────────────────────────────────────────────────┤
│       1. DÒNG TIỀN GỐC (PRINCIPAL FLOWS)       │       2. DÒNG TIỀN LÃI (INTEREST FLOWS)        │
├────────────────────────────────────────────────┼────────────────────────────────────────────────┤
│ • Dòng vào gốc: Thu hồi cho vay, đáo hạn TP... │ • Dòng vào lãi: Tiền lãi cho vay, coupon TP... │
│ • Dòng ra gốc: Rút tiền gửi, trả nợ vay...     │ • Dòng ra lãi: Trả lãi tiền gửi, chi phí vốn...│
│                                                │                                                │
│ ➔ Chi phối bởi: KỲ HẠN ĐÁO HẠN (Maturity Tenor)│ ➔ Chi phối bởi: KỲ HẠN LÃI SUẤT (Repricing)    │
│    (Contractual & Behavioural Maturity)        │    (Interest Rates, Reset Frequency, Spread)   │
│                                                │                                                │
│ ➔ Quyết định: THANH KHOẢN & SỰ SINH TỒN        │ ➔ Quyết định: LỢI NHUẬN & GIÁ TRỊ VỐN          │
│   ├── Liquidity Gap (Maturity Ladder)          │   ├── Thu nhập Lãi thuần (NII) & Biên lãi (NIM)│
│   ├── LCR (Dòng gốc ròng 30 ngày)              │   ├── P&L và Khả năng tích lũy vốn tự có       │
│   └── NSFR (Cấu trúc vốn gốc ổn định 1 năm)    │   └── EVE (Giá trị kinh tế của vốn chủ sở hữu) │
└────────────────────────────────────────────────┴────────────────────────────────────────────────┘
```

### 2.2. Sự Phân tách (Decoupling) giữa Kỳ hạn Đáo hạn Gốc và Kỳ hạn Tái định giá Lãi

Vấn đề cấu trúc cốt lõi của danh mục trên bảng cân đối là: **Kỳ hạn gốc (Maturity Tenor) và Kỳ hạn lãi (Repricing Tenor) không đồng nhất mà phân tách (decoupled) và bất đối xứng sâu sắc**.

1. **Maturity Tenor (Kỳ hạn Gốc)**: Thời điểm dòng tiền gốc thực sự di chuyển ra hoặc vào bảng cân đối theo hợp đồng hoặc theo mô hình hành vi. Thước đo này chi phối rủi ro thanh khoản dòng tiền (*liquidity mismatch, funding risk*), khoảng trống thanh khoản tại các dải thời gian (*liquidity gap*), và quyết định trực tiếp việc phân bổ hệ số [[asf-retail-and-small-business-deposits|ASF]] / [[rsf-loans-and-credit-exposures|RSF]] của [[nsfr]] cũng như tỷ lệ dòng rút/dòng thu trong 30 ngày của [[lcr]].
2. **Repricing Tenor (Kỳ hạn Lãi)**: Khoảng thời gian lãi suất của hợp đồng được giữ cố định trước khi thiết lập lại (*reset*) theo mặt bằng thị trường. Tái định giá xảy ra tại ngày sớm nhất ngân hàng hoặc đối tác được quyền đơn phương thay đổi lãi suất, hoặc ngày lãi suất thả nổi tự động thay đổi theo benchmark [[src-bcbs-irrbb-2016#^irrbb-u05-10]]; ngày của mỗi khoản hoàn trả, tái định giá hay thanh toán lãi là repricing date [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Thước đo này chi phối rủi ro tái định giá ([[gap-risk]]), rủi ro đường cong lợi suất, và phân bổ dòng tiền vào 19 dải kỳ hạn để tính $\Delta\text{EVE}$ theo khuôn khổ chuẩn hoá của [[irrbb-balance-sheet-portfolios]] [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. Việc $\Delta\text{NII}$ dùng cùng 19 dải này [cần nguồn].

Bốn hình thái lệch pha kỳ hạn điển hình trên bảng cân đối:
* **Hình thái 1: Kỳ hạn Gốc dài — Kỳ hạn Lãi ngắn (Long Maturity, Short Repricing)**:
  * *Điển hình*: Khoản cho vay mua nhà thế chấp 20 năm lãi suất thả nổi điều chỉnh 3 tháng/lần ($A_3$).
  * *Góc nhìn dòng gốc*: Dòng tiền vào gốc cực chậm (trả góp định kỳ hàng tháng), giam giữ nguồn vốn trong 20 năm $\rightarrow$ Tiêu tốn nguồn vốn ổn định dài hạn với $\text{RSF} = 65\%$.
  * *Góc nhìn dòng lãi*: Lãi suất được định giá lại mỗi quý một lần $\rightarrow$ Nằm ở dải kỳ hạn 3 tháng trong bảng IRRBB, rủi ro thời lượng lãi suất gần bằng 0 ($D \approx 0.25\text{Y}$), dòng tiền lãi vào tự động điều chỉnh theo lãi suất thị trường, bảo vệ NIM khi lãi suất tăng.
* **Hình thái 2: Kỳ hạn Gốc dài — Kỳ hạn Lãi dài (Long Maturity, Long Repricing)**:
  * *Điển hình*: Trái phiếu Chính phủ kỳ hạn 10 năm cố định lãi suất ($A_2$).
  * *Góc nhìn dòng gốc*: Mặc dù dòng tiền gốc đáo hạn sau 10 năm, tài sản này lại có thanh khoản tức thì vì có thể chuyển đổi thành tiền mặt trong ngày qua thị trường Repo $\rightarrow$ Được công nhận $100\%$ vào [[hqla]] Level 1 (haircut $0\%$) và chỉ tốn $\text{RSF} = 5\%$.
  * *Góc nhìn dòng lãi*: Dòng tiền lãi coupon bị khóa cứng trong 10 năm $\rightarrow$ Thời lượng Macaulay rất dài ($D \approx 7–8\text{Y}$), cực kỳ nhạy cảm với biến động lãi suất; khi lãi suất thị trường tăng 200 bps, giá trị hiện tại của trái phiếu sụt giảm nghiêm trọng, đe dọa trực tiếp EVE.
* **Hình thái 3: Kỳ hạn Gốc hợp đồng ngắn ($T=0$) — Kỳ hạn Gốc hành vi dài & Lãi suất cố định thấp**:
  * *Điển hình*: Tiền gửi không kỳ hạn CASA ($L_1$).
  * *Góc nhìn dòng gốc*: Theo hợp đồng pháp lý, khách hàng có quyền rút vốn bất kỳ lúc nào ($T=0$); nhưng theo mô hình hành vi danh mục (behavioural model), số dư tiền gửi lõi duy trì ổn định qua nhiều năm $\rightarrow$ Hưởng $\text{ASF} = 95\%$ trong NSFR và tỷ lệ run-off chỉ $5\%$ trong LCR [[src-bcbs-nsfr#^nsf30-10]] [[src-bcbs-lcr#^lcr40-13]].
  * *Góc nhìn dòng lãi*: Lãi suất do ngân hàng ấn định gần như $0\%$ (hoặc rất thấp) và ít co giãn theo lãi suất thị trường $\rightarrow$ Đóng vai trò như nguồn tài trợ có thời lượng ngầm dương lớn, mang lại biên lãi thuần vượt trội khi lãi suất thị trường tăng cao.
* **Hình thái 4: Kỳ hạn Gốc ngắn — Kỳ hạn Lãi ngắn**:
  * *Điển hình*: Vay mượn thị trường liên ngân hàng kỳ hạn 1 tháng ($L_4$).
  * *Góc nhìn dòng gốc*: Đáo hạn toàn bộ trong 30 ngày $\rightarrow$ Chịu run-off $100\%$ trong LCR và $\text{ASF} = 0\%$ trong NSFR [[src-bcbs-lcr#^lcr40-42]] [[src-bcbs-nsfr#^nsf30-14]].
  * *Góc nhìn dòng lãi*: Dòng tiền ra lãi nhạy cảm tức thì với các đợt tăng lãi suất điều hành của NHTW; chi phí lãi vay bùng nổ ngay khi thanh khoản hệ thống thắt chặt.

---

### 2.3. Bảng Phân rã Đa chiều: Kỳ hạn Gốc vs Kỳ hạn Lãi của Portfolio Mẫu

Dưới đây là ma trận phân rã chi tiết bản chất dòng tiền của từng cấu phần trên Bảng Cân đối Mẫu 100.000 tỷ VND:

| Mã | Danh mục Tài sản & Nguồn vốn | Quy mô | Kỳ hạn Gốc (Maturity Tenor) | Bản chất Dòng tiền Gốc & Tác động Thanh khoản | Kỳ hạn Lãi (Repricing Tenor) | Bản chất Dòng tiền Lãi & Tác động Lãi suất / P&L |
|:---:|---|:---:|:---:|---|:---:|---|
| **$A_1$** | **Tiền mặt & Dự trữ NHTW** | 3.000 (3%) | Tức thì ($T=0$) | Dòng tiền gốc khả dụng ngay; HQLA Level 1 (100%), RSF 0% | Tức thì ($T=0$) | Lãi suất thấp (0.8%); dòng vào lãi biến động tức thì theo lãi suất tiền gửi NHTW |
| **$A_2$** | **Trái phiếu Chính phủ L1** | 17.000 (17%) | 5.5 năm (đáo hạn) | Chuyển hóa dòng gốc tức thì qua Repo; HQLA Level 1, RSF 5% | 5.5 năm (cố định) | Coupon cố định 3.2%; dòng vào lãi cố định, thời lượng dài ($D_A = 5.5\text{Y}$), rủi ro EVE cao |
| **$A_3$** | **Cho vay Mua nhà BĐS** | 30.000 (30%) | 4.0 năm (bình quân) | Dòng vào gốc chậm qua trả góp; không HQLA, RSF 65%, LCR Inflow 50% | 3 tháng (thả nổi) | Lãi suất 8.5% reset theo quý; dòng vào lãi tự điều chỉnh theo thị trường, bảo vệ NIM |
| **$A_4$** | **Cho vay Doanh nghiệp** | 43.000 (43%) | 0.5–1.0 năm | Thu hồi gốc luân chuyển vốn lưu động; không HQLA, RSF 85%, Inflow 50% | 6 tháng (thả nổi) | Lãi suất 7.8% reset bán niên; dòng vào lãi nhạy cảm trung bình, biên tín dụng lớn |
| **$A_5$** | **Tài sản Cố định & Khác** | 7.000 (7%) | Vĩnh viễn / Dài hạn | Đóng băng vốn, không tạo dòng vào gốc; RSF 100%, không HQLA | Không nhạy cảm | Không phát sinh dòng tiền lãi (0.0%); chi phí cơ hội vốn |
| **$L_1$** | **CASA Bán lẻ Ổn định** | 20.000 (20%) | Hợp đồng 0D; Hành vi 2.5–5Y | Dòng ra gốc rất thấp khi stress (Run-off 5%); nguồn vốn ổn định ASF 95% | Ấn định (Administered) | Chi phí siêu rẻ 0.3%; dòng ra lãi cực thấp, tạo động lực chính cho NIM ngân hàng |
| **$L_2$** | **Tiết kiệm Kỳ hạn Bán lẻ** | 25.000 (25%) | 0.75 năm (hợp đồng) | Dòng ra gốc được kiểm soát (Run-off 0–5% nếu $>30$D); ASF 90% | 0.75 năm (cố định) | Lãi suất cố định 5.2%; dòng ra lãi cố định theo kỳ, chịu rủi ro rút trước hạn TDRR |
| **$L_3$** | **Tiền gửi DN Vận hành** | 15.000 (15%) | 0.25 năm (vận hành) | Dòng ra gốc trung bình gắn với thanh toán (Run-off 25%); ASF 50% | 0.25 năm | Lãi suất thỏa thuận 2.5%; dòng ra lãi ổn định theo nhu cầu dịch vụ doanh nghiệp |
| **$L_4$** | **Vay Bán buôn / LNH** | 15.000 (15%) | 1 tháng (ngắn hạn) | Dòng ra gốc cấp tính khi khủng hoảng (Run-off 100%); ASF 0% | 1 tháng (thị trường) | Lãi suất thị trường 4.8%; dòng ra lãi bùng nổ tức thì khi thanh khoản thắt chặt |
| **$L_5$** | **Giấy tờ có giá $\ge 1$Y** | 15.000 (15%) | 3.0 năm (trung hạn) | Không phát sinh dòng ra gốc trong 30D (Run-off 0%); ASF 100% | 3.0 năm (cố định) | Lãi suất cố định 6.5%; dòng ra lãi cố định, khóa chi phí vốn dài hạn cho ngân hàng |
| **$E$** | **Vốn CET1 Equity** | 10.000 (10%) | Vĩnh viễn (Perpetual) | Không bao giờ phát sinh dòng ra gốc; đệm hấp thụ tổn thất tuyệt đối, ASF 100% | Không lãi suất | Không chịu chi phí lãi hợp đồng; chi phí vốn cổ phần chi trả qua cổ tức từ P&L |

---

### 2.4. Vòng xoắn Phản hồi Động lực học (Dynamic Feedback Loop): Thanh khoản Dòng Gốc ↔ Chi phí Dòng Lãi

Trong thực tiễn điều hành ALM, sự tương tác giữa Dòng tiền Gốc và Dòng tiền Lãi không diễn ra độc lập mà tạo thành **vòng xoắn truyền dẫn phản hồi động lực học hai chiều**:

```
                  ┌────────────────────────────────────────────────────────┐
                  │          VÒNG XOẮN TRUYỀN DẪN ĐỘNG LỰC HỌC 2 CHIỀU      │
                  └────────────────────────────────────────────────────────┘

    [HƯỚNG 1: TỪ GỐC SANG LÃI]                          [HƯỚNG 2: TỪ LÃI SANG GỐC]
  Khủng hoảng Thanh khoản Dòng Gốc                    Cú sốc Biến động Mặt bằng Lãi suất
                 │                                                   │
                 ▼                                                   ▼
  • Dòng ra gốc tăng vọt (Run-off)                    • Lãi suất thị trường tăng sốc (+200 bps)
  • Dòng vào gốc chậm (Tài sản dài hạn)               • Gánh nặng trả nợ của người vay tăng vọt
  • Bảng cân đối thiếu hụt dòng gốc cấp tính          • Nợ xấu phát sinh, suy giảm khả năng trả nợ
                 │                                                   │
                 ▼                                                   ▼
  • Ngân hàng vay khẩn cấp / tăng lãi suất huy động   • Dòng vào gốc bị tắc nghẽn (Principal Freezing)
  • Chấp nhận chi phí tái tài trợ cắt cổ              • Người gửi rút CASA chạy sang kênh lợi suất cao
                 │                                                   │
                 ▼                                                   ▼
  ➔ BÙNG NỔ DÒNG TIỀN RA LÃI (Interest Outflows)      ➔ GIA TĂNG DÒNG TIỀN RA GỐC (Principal Outflows)
  ➔ NIM CO HẸP, NII ÂM, BÀO MÒN VỐN CET1              ➔ LCR & NSFR ĐỒNG THỜI SỤP ĐỔ
```

1. **Chiều thứ nhất — Từ Khủng hoảng Dòng Gốc kích nổ Chi phí Dòng Lãi (Liquidity Crunch to Interest Outflows Explosion)**:
   * Khi thị trường gặp cú sốc niềm tin, người gửi tiền và các chủ nợ bán buôn ồ ạt rút vốn, **Dòng tiền ra gốc (Principal Outflows)** bùng nổ.
   * Vì các tài sản sinh lời có kỳ hạn gốc dài ($A_3, A_4$) không thể thu hồi ngay lập tức, ngân hàng rơi vào trạng thái thiếu hụt dòng tiền gốc (*liquidity deficit*).
   * Để bù đắp dòng gốc nhằm duy trì tỷ lệ [[lcr]] trên ngưỡng 100% và tránh vỡ nợ kỹ thuật, Treasury buộc phải tìm kiếm thanh khoản khẩn cấp bằng cách phát hành chứng chỉ tiền gửi lãi suất cao hoặc vay mượn qua đêm trên thị trường liên ngân hàng với mức lãi suất cắt cổ.
   * **Kết quả**: Việc mua dòng tiền gốc trong hoảng loạn đẩy **Dòng tiền ra lãi (Interest Outflows)** tăng vọt, triệt tiêu toàn bộ NIM, bóp nghẹt NII và chuyển hóa một cuộc khủng hoảng thanh khoản thuần túy thành lỗ lũy kế P&L tàn phá vốn tự có.
2. **Chiều thứ hai — Từ Cú sốc Dòng Lãi bóp nghẹt Dòng Gốc (Interest Rate Shock to Principal Freezing & Run-off)**:
   * Khi NHTW tăng mạnh lãi suất điều hành (+200 đến +400 bps), các khoản cho vay thả nổi ($A_3, A_4$) tái định giá đẩy dòng tiền lãi phải trả của khách hàng lên mức kỷ lục.
   * Vượt quá năng lực tài chính của bên vay, tỷ lệ nợ quá hạn và nợ xấu gia tăng đột biến. Khách hàng không thể trả nợ gốc đúng hạn, khiến **Dòng tiền vào gốc (Principal Inflows)** của ngân hàng bị phong tỏa và đóng băng (*principal freezing*).
   * Cùng lúc đó, chênh lệch giữa lãi suất CASA ($0.3\%$) và lãi suất thị trường nới rộng khủng khiếp, kích hoạt làn sóng người gửi tiền rút dòng gốc khỏi tài khoản thanh toán để chuyển sang trái phiếu hoặc quỹ tiền tệ (*deposit disintermediation / deposit flight*).
   * **Kết quả**: Sốc lãi suất (biến đổi dòng lãi) đã trực tiếp bóp nghẹt dòng vào gốc và kích thích dòng ra gốc, làm sụp đổ đồng thời cả hai chỉ số thanh khoản [[lcr]] và [[nsfr]].

---

## 3. Bảng Cân đối Kế toán Tổng hợp Mẫu (The Benchmark Synthetic Balance Sheet)

Dưới đây là một mô hình bảng cân đối kế toán tổng hợp hoàn chỉnh (quy mô quy ước **100.000 tỷ VND** hoặc **100.0%**) được thiết kế tối ưu, cân bằng giữa lợi nhuận sinh lời và an toàn thanh khoản:

### 3.1. Phân hệ Tài sản Có (TSC - Assets Portfolio)

| Mã | Danh mục Tài sản Có (TSC) | Quy mô (Tỷ VND) | Tỷ trọng | Lợi suất ($y_i$) | Đặc tính [[lcr]] (30 ngày) | Đặc tính [[nsfr]] (1 năm) | Thời lượng Macaulay ($D_i$) |
|:---:|---|:---:|:---:|:---:|---|---|:---:|
| **$A_1$** | **Tiền mặt & Dự trữ tại NHTW** | 3.000 | **3.0%** | 0.8% | [[level-1-assets]]: Haircut 0% [[src-bcbs-lcr#^lcr30-41]] | [[rsf-hqla-and-central-bank-reserves]]: RSF = 0% [[src-bcbs-nsfr#^nsf30-24]] | 0.0Y |
| **$A_2$** | **Trái phiếu Chính phủ Level 1** | 17.000 | **17.0%** | 3.2% | [[level-1-assets]]: Haircut 0% [[src-bcbs-lcr#^lcr30-41]] | [[rsf-hqla-and-central-bank-reserves]]: RSF = 5% [[src-bcbs-nsfr#^nsf30-26]] | 5.5Y |
| **$A_3$** | **Cho vay Mua nhà Thế chấp BĐS** | 30.000 | **30.0%** | 8.5% | Không HQLA; Inflow thu hồi 50% [[src-bcbs-lcr#^lcr40-70]] | [[rsf-loans-and-credit-exposures]]: RSF = 65% [[src-bcbs-nsfr#^nsf30-30]] | 4.0Y |
| **$A_4$** | **Cho vay Doanh nghiệp & Vốn LĐ** | 43.000 | **43.0%** | 7.8% | Không HQLA; Inflow thu hồi 50% [[src-bcbs-lcr#^lcr40-70]] | [[rsf-loans-and-credit-exposures]]: RSF = 85% [[src-bcbs-nsfr#^nsf30-31]] | 0.5Y (thả nổi 6M) |
| **$A_5$** | **Tài sản Cố định & TSC Khác** | 7.000 | **7.0%** | 0.0% | Kém thanh khoản, không tạo dòng tiền | [[required-stable-funding]]: RSF = 100% [[src-bcbs-nsfr#^nsf30-3]] | — |
| **TỔNG** | **TỔNG TÀI SẢN CÓ (TSC)** | **100.000** | **100.0%** | **6.45%** | **Tổng HQLA = 20.000 tỷ VND (20%)** | **RSF Trung bình = 64.40%** | **$D_A \approx 2.35$ năm** |

---

### 3.2. Phân hệ Tài sản Nợ & Vốn (TSN - Liabilities & Equity Portfolio)

| Mã | Danh mục Tài sản Nợ & Vốn (TSN) | Quy mô (Tỷ VND) | Tỷ trọng | Chi phí vốn ($c_j$) | Đặc tính [[lcr]] (Run-off 30D) | Đặc tính [[nsfr]] (ASF Factor) | Thời lượng Macaulay ($D_j$) |
|:---:|---|:---:|:---:|:---:|---|---|:---:|
| **$L_1$** | **Tiền gửi CASA Bán lẻ Ổn định** | 20.000 | **20.0%** | 0.3% | [[retail-deposit-stability]]: Run-off = 5% [[src-bcbs-lcr#^lcr40-13]] | [[asf-retail-and-small-business-deposits]]: ASF = 95% [[src-bcbs-nsfr#^nsf30-10]] | 2.5Y (Replicating) |
| **$L_2$** | **Tiền gửi Tiết kiệm Kỳ hạn Bán lẻ** | 25.000 | **25.0%** | 5.2% | [[run-off-rate]]: Run-off = 0% (nếu $>30$D) / 5% [[src-bcbs-lcr#^lcr40-14]] | [[asf-retail-and-small-business-deposits]]: ASF = 90% [[src-bcbs-nsfr#^nsf30-11]] | 0.75Y |
| **$L_3$** | **Tiền gửi Doanh nghiệp Vận hành** | 15.000 | **15.0%** | 2.5% | [[operational-deposits]]: Run-off = 25% [[src-bcbs-lcr#^lcr40-26]] | [[asf-wholesale-and-operational-funding]]: ASF = 50% [[src-bcbs-nsfr#^nsf30-13]] | 0.25Y |
| **$L_4$** | **Vay Bán buôn / Liên ngân hàng $< 6$M** | 15.000 | **15.0%** | 4.8% | [[unsecured-wholesale-funding]]: Run-off = 100% [[src-bcbs-lcr#^lcr40-42]] | [[asf-wholesale-and-operational-funding]]: ASF = 0% [[src-bcbs-nsfr#^nsf30-14]] | 0.08Y (1 tháng) |
| **$L_5$** | **Giấy tờ có giá / Trái phiếu $\ge 1$ năm** | 15.000 | **15.0%** | 6.5% | Run-off = 0% (không đáo hạn trong 30D) | [[asf-capital-and-long-term-liabilities]]: ASF = 100% [[src-bcbs-nsfr#^nsf30-6]] | 3.0Y |
| **$E$** | **Vốn Cấp 1 Phổ thông (CET1 Equity)** | 10.000 | **10.0%** | 0.0% | Nguồn tài trợ vĩnh viễn, Run-off = 0% | [[asf-capital-and-long-term-liabilities]]: ASF = 100% [[src-bcbs-nsfr#^nsf30-6]] | — |
| **TỔNG** | **TỔNG TÀI SẢN NỢ & VỐN (TSN)** | **100.000** | **100.0%** | **3.44%** | | **ASF Trung bình = 74.00%** | **$D_L \approx 1.25$ năm** |

---

## 4. Kiểm chứng Số học Giải tích Từng Bước (Step-by-Step Verification)

### 4.1. Kiểm chứng Chỉ số Thanh khoản Dài hạn (NSFR)
Theo quy định tại **NSF20 & NSF30** của Chuẩn mực Basel [[src-bcbs-nsfr#^nsf20-2]] [[src-bcbs-nsfr#^nsf30-6]]:

1. **Tính Tổng Lượng Nguồn vốn Ổn định Sẵn có (Tử số ASF)**:
   $$\begin{aligned}
   \text{ASF} &= \sum_{j=1}^5 L_j \cdot \text{ASF}_j + E \cdot 100\% \\
   &= (20.000 \times 95\%) + (25.000 \times 90\%) + (15.000 \times 50\%) + (15.000 \times 0\%) + (15.000 \times 100\%) + (10.000 \times 100\%) \\
   &= 19.000 + 22.500 + 7.500 + 0 + 15.000 + 10.000 \\
   &= \mathbf{74.000 \text{ tỷ VND}} \quad (\text{đạt } 74.00\% \text{ tổng nguồn vốn})
   \end{aligned}$$

2. **Tính Tổng Lượng Nguồn vốn Ổn định Cần thiết (Mẫu số RSF)**:
   Giả định ngân hàng có **10.000 tỷ VND** cam kết cấp tín dụng và thanh khoản ngoại bảng chưa giải ngân ([[committed-facilities]], chịu RSF 5% theo NSF30.34) [[src-bcbs-nsfr#^nsf30-34]]:
   $$\begin{aligned}
   \text{RSF} &= \sum_{i=1}^5 A_i \cdot \text{RSF}_i + \text{OBS} \cdot 5\% \\
   &= (3.000 \times 0\%) + (17.000 \times 5\%) + (30.000 \times 65\%) + (43.000 \times 85\%) + (7.000 \times 100\%) + (10.000 \times 5\%) \\
   &= 0 + 850 + 19.500 + 36.550 + 7.000 + 500 \\
   &= \mathbf{64.400 \text{ tỷ VND}} \quad (\text{đạt } 64.40\% \text{ tổng tài sản})
   \end{aligned}$$

3. **Xác định Tỷ lệ NSFR Thực tế**:
   $$\text{NSFR} = \frac{\text{ASF}}{\text{RSF}} = \frac{74.000}{64.400} = \mathbf{114.91\%} \ge 100\% \quad \boldsymbol{\checkmark} \text{ (Thỏa mãn, có đệm an toàn } +14.91\%)$$

---

### 4.2. Kiểm chứng Chỉ số Thanh khoản Ngắn hạn (LCR)
Theo quy định tại **LCR20, LCR30 & LCR40** của Chuẩn mực Basel [[src-bcbs-lcr#^lcr20-3]] [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-lcr#^lcr40-1]]:

1. **Tính Tổng Tài sản Thanh khoản Cao Hợp lệ (Tử số HQLA)**:
   Toàn bộ tiền mặt, dự trữ NHTW và TPCP đều thuộc HQLA Level 1 (không trần hạn mức, haircut 0%):
   $$\text{HQLA} = A_1 \times (1 - 0\%) + A_2 \times (1 - 0\%) = 3.000 + 17.000 = \mathbf{20.000 \text{ tỷ VND}}$$

2. **Tính Tổng Dòng tiền Ra Dự kiến trong 30 ngày (Gross Cash Outflows)**:
   - Dòng tiền rút từ CASA bán lẻ ổn định ($L_1$): $20.000 \times 5\% = 1.000 \text{ tỷ}$ [[src-bcbs-lcr#^lcr40-7]].
   - Dòng tiền rút từ tiền gửi kỳ hạn bán lẻ ($L_2$ giả định $15\%$ đến hạn trong 30 ngày tới): $(25.000 \times 15\%) \times 5\% = 187.5 \text{ tỷ}$ [[src-bcbs-lcr#^lcr40-14]].
   - Dòng tiền rút từ tiền gửi doanh nghiệp vận hành ($L_3$): $15.000 \times 25\% = 3.750 \text{ tỷ}$ [[src-bcbs-lcr#^lcr40-26]].
   - Dòng tiền rút từ vay bán buôn / liên ngân hàng ngắn hạn ($L_4$ đến hạn trong 30 ngày): $15.000 \times 100\% = 15.000 \text{ tỷ}$ [[src-bcbs-lcr#^lcr40-42]].
   - Dòng tiền rút từ cam kết ngoại bảng (10.000 tỷ cam kết tín dụng SME/DN, rút 5% theo LCR40.61): $10.000 \times 5\% = 500 \text{ tỷ}$ [[src-bcbs-lcr#^lcr40-61]].
   $$\text{Gross Outflows} = 1.000 + 187.5 + 3.750 + 15.000 + 500 = \mathbf{20.437,5 \text{ tỷ VND}}$$

3. **Tính Tổng Dòng tiền Vào Hợp đồng trong 30 ngày (Cash Inflows)**:
   - Thu hồi nợ cho vay bán lẻ và doanh nghiệp đến hạn trong 30 ngày (giả định $8\%$ tổng dư nợ đến hạn hợp đồng, tỷ lệ công nhận dòng vào tối đa 50% để bảo đảm ngân hàng tiếp tục tái cấp tín dụng duy trì thương quyền) [[src-bcbs-lcr#^lcr40-86]] [[src-bcbs-lcr#^lcr40-87]]:
     $$\text{Inflows} = \big[(30.000 + 43.000) \times 8\%\big] \times 50\% = 5.840 \times 50\% = \mathbf{2.920 \text{ tỷ VND}}$$
   - **Kiểm tra Trần Khống chế Dòng vào 75% (75% Inflow Cap - LCR40.77)** [[src-bcbs-lcr#^lcr40-77]]:
     $$\text{Trần 75\%} = 75\% \times \text{Gross Outflows} = 75\% \times 20.437,5 = 15.328,1 \text{ tỷ VND}$$
     Do $\text{Inflows} = 2.920 < 15.328,1$ nên toàn bộ dòng tiền vào 2.920 tỷ được công nhận $100\%$.

4. **Tính Dòng tiền Ra Thuần trong 30 ngày (Mẫu số Total Net Cash Outflows)**:
   $$\text{Total Net Cash Outflows} = \text{Gross Outflows} - \text{Inflows} = 20.437,5 - 2.920 = \mathbf{17.517,5 \text{ tỷ VND}}$$

5. **Xác định Tỷ lệ LCR Thực tế**:
   $$\text{LCR} = \frac{\text{HQLA}}{\text{Net Outflows}} = \frac{20.000}{17.517,5} = \mathbf{114.17\%} \ge 100\% \quad \boldsymbol{\checkmark} \text{ (Thỏa mãn, có đệm an toàn } +14.17\%)$$

---

### 4.3. Hiệu quả Tài chính và Tỷ lệ Đòn bẩy
* **Biên Thu nhập Lãi thuần (NIM)**:
  $$\text{NIM} = \text{Lợi suất Tài sản Bình quân} - \text{Chi phí Vốn Bình quân} = 6.45\% - 3.44\% = \mathbf{3.01\%}$$
  Tạo ra mức Thu nhập lãi thuần hàng năm: $\text{NII} = 100.000 \times 3.01\% = \mathbf{3.010 \text{ tỷ VND}}$.
* **Tỷ lệ Đòn bẩy (Leverage Ratio)**:
  $$\text{LR} = \frac{\text{Tier 1 Capital}}{\text{Total On- and Off-Balance Sheet Exposure}} = \frac{10.000}{100.000 + 10.000 \times 100\%} = \frac{10.000}{110.000} = \mathbf{9.09\%} \ge 3.0\% \quad \boldsymbol{\checkmark}$$

---

## 5. Năm Quy luật Động lực học Cân đối TSN - TSC

Việc thiết lập bảng cân đối tổng hợp dựa trên LCR, NSFR và bản thể dòng tiền kép làm sáng tỏ 5 quy luật tài chính nền tảng:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        NĂM QUY LUẬT CÂN ĐỐI ĐỘNG LỰC HỌC TSN - TSC                              │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ QUY LUẬT 1: ĐÒN BẨY KÉP CỦA TRÁI PHIẾU CHÍNH PHỦ LEVEL 1 (A2)                                   │
│ • Đóng góp 100% vào HQLA của LCR nhưng chỉ tiêu tốn 5% RSF của NSFR.                            │
│ • Là tài sản bản lề: 17% TPCP giải quyết 85% HQLA và chỉ tốn 0.85% ASF.                         │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ QUY LUẬT 2: BẪY CHẾT THANH KHOẢN CỦA VỐN BÁN BUÔN NGẮN HẠN (L4)                                 │
│ • Run-off 100% trong LCR và ASF 0% trong NSFR.                                                  │
│ • Tỷ trọng L4 > 20% sẽ lập tức kéo sụp cả LCR và NSFR xuống dưới 100%.                          │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ QUY LUẬT 3: GIÁ TRỊ VÔ SONG CỦA TIỀN GỬI CASA BÁN LẺ ỔN ĐỊNH (L1)                               │
│ • Run-off chỉ 5% trong LCR, ASF lên tới 95% trong NSFR, chi phí vốn siêu rẻ (0.3%).             │
│ • Cung cấp 19.000 tỷ ASF ổn định mà chỉ kích hoạt 1.000 tỷ dòng tiền ra cấp tính.               │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ QUY LUẬT 4: CẠM BẪY THỜI LƯỢNG HQLA VÀ SỰ HÓA GIẢI BẰNG PHÁI SINH (TẦNG 4)                      │
│ • Gom 17% TPCP dài hạn để thỏa mãn LCR/NSFR làm tăng vọt thời lượng tài sản (DA > 2.3Y).        │
│ • Khi lãi suất tăng 200 bps, ΔEVE sụt giảm đe dọa Outlier Test 15% Tier 1.                      │
│ • Giải pháp: Thực hiện Pay-Fixed IRS hoán đổi TPCP 5Y về thả nổi 3M (giữ HQLA, triệt tiêu EVE). │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ QUY LUẬT 5: BẢN CHẤT DÒNG TIỀN KÉP GỐC - LÃI VÀ VÒNG XOẮN PHẢN HỒI THANH KHOẢN - P&L            │
│ • Dòng gốc quyết định khả năng sinh tồn (LCR, NSFR) theo kỳ hạn đáo hạn (Maturity Tenor).       │
│ • Dòng lãi quyết định P&L và vốn (NIM, EVE) theo kỳ hạn định giá lại (Repricing Tenor).          │
│ • Đứt gãy dòng gốc buộc ngân hàng mua vốn đắt đỏ làm nổ tung dòng ra lãi; sốc dòng lãi làm     │
│   đóng băng dòng vào gốc và kích hoạt làn sóng rút tiền hàng loạt (deposit flight).              │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Cơ chế Truyền dẫn Điều hành của ALCO (Operational Steering)

Để biến Bảng cân đối Mục tiêu thành hiện thực, ALCO không thể chỉ ra nghị quyết hành chính, mà sử dụng cơ chế **Điều chuyển Giá vốn Nội bộ Tích hợp ([[liquidity-transfer-pricing|Liquidity FTP]])** kết hợp với **Kế hoạch Tài trợ Dự phòng ([[contingency-funding-plan|CFP]])** [[src-choudhry-principles-banking#^choudhry-ftp-10]] [[src-choudhry-principles-banking#^choudhry-cfp-1]]:

$$\text{FTP}_{\text{Asset}} = \text{Base Rate} + \text{Term Liquidity Premium (TLP)} + \text{LCR Buffer Surcharge} + \text{NSFR Structural Term Charge}$$

1. **Khối Khách hàng Bán lẻ (Retail Banking)**:
   - Được trả thưởng thanh khoản cao (FTP credit) cho nguồn tiền gửi CASA ($L_1$) nhờ cung cấp $\text{ASF} = 95\%$ và $\text{Run-off} = 5\%$.
   - Các khoản cho vay thế chấp nhà ở ($A_3$) bị áp phí vốn cấu trúc tương ứng với mức $\text{RSF} = 65\%$.
2. **Khối Khách hàng Doanh nghiệp (Wholesale Banking)**:
   - Các khoản vay vốn lưu động ngắn hạn và tài trợ dự án ($A_4$) bị tính phí thanh khoản nặng do tiêu tốn $\text{RSF} = 85\%$.
   - Nguồn vốn tiền gửi thanh toán định danh là **Tiền gửi Vận hành (Operational Deposits - $L_3$)** được ưu đãi phí hơn tiền gửi đầu cơ ngắn hạn ($L_4$) vì hưởng $\text{ASF} = 50\%$ và $\text{Run-off} = 25\%$.
3. **Khối Nguồn vốn (ALM Treasury)**:
   - Duy trì hạn mức trần thời lượng bình quân cho danh mục $A_2$ (không vượt quá 2.5–3.0 năm).
   - Kiểm soát chặt chẽ ràng buộc chốt chặn [[leverage-ratio|Tỷ lệ Đòn bẩy (LR $\ge 3\%$)]] thông qua việc quản trị [[leverage-exposure-measure|Quy mô Phơi nhiễm]] nội và ngoại bảng.
   - Khi tỷ lệ NSFR tiệm cận ngưỡng cảnh báo $105\%$, Treasury lập tức kích hoạt chương trình phát hành Giấy tờ có giá dài hạn ($L_5$) kỳ hạn 2–3 năm để bổ sung $\text{ASF} = 100\%$.
   - Sẵn sàng kích hoạt các hành động dự phòng trong [[contingency-funding-plan|CFP]] để bảo vệ khả năng sinh tồn trong các kịch bản khủng hoảng theo mô hình [[practical-alm-liquidity-governance]].

---

## 7. Ma trận Liên kết Hệ thống ALM Wiki

Mô hình Synthetic Balance Sheet kết nối toàn diện các hợp phần tri thức cốt lõi:
* **Các Chỉ số Thanh khoản, Đòn bẩy & Dòng tiền**: [[lcr]], [[hqla]], [[net-cash-outflows]], [[cash-inflows]], [[cash-outflows]], [[nsfr]], [[available-stable-funding]], [[required-stable-funding]], [[lcr-by-currency]], [[leverage-ratio]].
* **Các Khái niệm Cấu phần & Kỳ hạn**: [[level-1-assets]], [[retail-deposit-stability]], [[operational-deposits]], [[unsecured-wholesale-funding]], [[non-maturity-deposits]], [[gap-risk]], [[contractual-maturity-mismatch]], [[funding-concentration-risk]], [[available-unencumbered-assets]], [[intraday-liquidity-risk]], [[liquidity-monitoring-metrics]], [[leverage-exposure-measure]], [[rsf-loans-and-credit-exposures]], [[rsf-hqla-and-central-bank-reserves]], [[lcr-nsfr-interlinkages]], [[irrbb-balance-sheet-portfolios]].
* **Thước đo Lãi suất & Định giá**: [[net-interest-income-sensitivity]], [[economic-value-of-equity]], [[duration-gap-model]], [[replicating-portfolio-model]].
* **Chiến lược Quản trị & Điều hành Thực chiến**: [[practical-alm-liquidity-governance]], [[contingency-funding-plan]], [[liquidity-transfer-pricing]], [[basel-liquidity-monitoring-framework]], [[integrated-alm-liquidity-strategy]], [[hqla-decomposition-and-tradeoffs]], [[irrbb-five-tier-architecture]], [[irrbb-alm-governance-strategy-and-tradeoffs]].
* **Chuẩn mực Giám sát**: [[bcbs-lcr]], [[bcbs-nsfr]], [[src-bcbs-lev]], [[bcbs-irrbb]], [[outlier-bank-test]].

## Đề xuất cập nhật
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation ở câu slotting. → đã rà [2026-10-18]
- [2026-10-18] research (rà sau U05 bổ sung) — đề xuất cho dòng 107 "Repricing Tenor (Kỳ hạn Lãi)", chờ user duyệt: → đã áp [2026-10-19]
  - Định nghĩa thời điểm reset nên cite par 102: tái định giá xảy ra tại ngày sớm nhất ngân hàng hoặc đối tác được quyền đơn phương thay đổi lãi suất, hoặc ngày lãi suất thả nổi tự động thay đổi theo benchmark [[src-bcbs-irrbb-2016#^irrbb-u05-10]]; repricing date là ngày của mỗi khoản hoàn trả, tái định giá hay thanh toán lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]].
  - 19 dải kỳ hạn của par 101 thuộc khuôn khổ chuẩn hoá đo ∆EVE [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-bcbs-irrbb-2016#^irrbb-u05-2]]; claim đã ingest không nói ∆NII dùng 19 dải này. Đề xuất bỏ "$\Delta\text{NII}$ và" khỏi câu, hoặc ghi `[cần nguồn]` cho phần ∆NII.
