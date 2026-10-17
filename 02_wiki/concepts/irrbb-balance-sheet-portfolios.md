---
title: "IRRBB — Cấu phần Danh mục Bảng Cân đối Chịu Phơi nhiễm Rủi ro Lãi suất"
aliases: [Banking Book Portfolio Components, Cấu phần danh mục sổ ngân hàng IRRBB, Balance Sheet Portfolios IRRBB, Danh mục bảng cân đối IRRBB, Portfolio Components Subject to IRRBB]
type: concept
domains: [alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tata-bank-alm]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-1]]"}
  - {type: exposed-to, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: exposed-to, to: "[[basis-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: exposed-to, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: governs, to: "[[non-maturity-deposits]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-4]]"}
  - {type: governs, to: "[[behavioural-options]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-5]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p08-2]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p08-3]]"}
  - {type: input-to, to: "[[irrbb-standardised-framework]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: input-to, to: "[[repricing-balance-sheet]]", cite: "[[src-tata-bank-alm#^tata-gap-1]]"}
tags: [irrbb, balance-sheet-portfolios, banking-book, asset-classes, liability-classes, off-balance-sheet, amortised-cost, fvtoci, cash-flow-slotting, basel]
updated: 2026-10-17
reviewed:
---

## Tóm tắt Cấp cao (Executive Summary)

Rủi ro lãi suất trên sổ ngân hàng (IRRBB) là rủi ro hiện tại hoặc tiềm tàng đối với nguồn vốn và thu nhập của ngân hàng phát sinh từ các biến động bất lợi của lãi suất tác động lên toàn bộ các vị thế trên **sổ ngân hàng (Banking Book)** [[src-bcbs-irrbb-2016#^irrbb-u02-1]].

Để đo lường chính xác Giá trị kinh tế của Vốn ([[economic-value-of-equity|$\Delta\text{EVE}$]]) và Độ nhạy Thu nhập thuần từ lãi ([[net-interest-income-sensitivity|$\Delta\text{NII}$]]), Ủy ban Basel (**BCBS d368**) và các chuẩn mực ALM quốc tế thiết lập quy tắc nhận diện, bóc tách và phân bổ toàn diện các **cấu phần danh mục bảng cân đối chịu rủi ro IRRBB** theo 3 phân hệ cốt lõi:
1. **Phân hệ Tài sản (Assets)**: Cho vay khách hàng (bán lẻ, bán buôn), Danh mục trái phiếu đầu tư & đệm thanh khoản ([[hqla]]), Tiền gửi & cho vay thị trường liên ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
2. **Phân hệ Nợ phải trả (Liabilities)**: Tiền gửi không kỳ hạn ([[non-maturity-deposits|NMDs / CASA]]), Tiền gửi có kỳ hạn (Term Deposits), Vay nợ bán buôn & phát hành giấy tờ có giá [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
3. **Phân hệ Ngoại bảng & Phái sinh (Off-Balance Sheet & Derivatives)**: Cam kết tín dụng & rủi ro đường ống giải ngân (pipeline risk), Hợp đồng hoán đổi lãi suất ([[interest-rate-swap|IRS]]), Quyền chọn lãi suất ([[interest-rate-cap-floor|Caps/Floors]], [[swaption|Swaptions]]) [[src-bcbs-irrbb-2016#^irrbb-u05-2]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                     HỆ THỐNG CẤU PHẦN DANH MỤC BẢNG CÂN ĐỐI CHỊU RỦI RO IRRBB                   │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. PHẠM VI XÁC ĐỊNH & RANH GIỚI BẮT BUỘC                                                        │
│  ├── Bao gồm: Toàn bộ tài sản, nợ nhạy cảm lãi suất và cam kết ngoại bảng sổ ngân hàng          │
│  └── Loại trừ: Vốn cấp 1 CET1, Cổ phiếu sổ ngân hàng, Tài sản cố định (BĐS, vô hình)           │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. BA NHÓM KHẢ NĂNG CHUẨN HOÁ BASEL (STAGE 1 AMENABILITY)                                       │
│  ├── Amenable: Cố định/Thả nổi thuần túy theo hợp đồng, không có quyền chọn nhúng               │
│  ├── Less Amenable: Có quyền chọn tự động (Caps/Floors/Swaptions) ➔ Bóc tách tính KAO riêng     │
│  └── Not Amenable: Chịu chi phối quyền chọn hành vi ➔ NMDs (Core/Non-core), CPR, TDRR           │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. MA TRẬN PHÂN LOẠI KẾ TOÁN & CƠ CHẾ TRUYỀN DẪN RỦI RO                                         │
│  ├── Amortised Cost / HTM: Không ảnh hưởng P&L ngay, nhưng gánh toàn bộ rủi ro kinh tế ΔEVE    │
│  ├── Fair Value through OCI (AFS/FVTOCI): Lỗ chưa thực hiện trừ thẳng vào Vốn cấp 1 CET1        │
│  └── Fair Value through P&L (FVTPL): Biến động tức thì vào báo cáo thu nhập kế toán             │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. PHÂN BỔ DÒNG TIỀN VÀO 19 DẢI KỲ HẠN BASEL (STAGE 2 SLOTTING)                                 │
│  ├── Dòng tiền gốc (Principal Cash Flows) & Dòng tiền lãi (Interest Cash Flows)                 │
│  ├── Tài sản thả nổi: Tái định giá 100% gốc tại ngày reset đầu tiên (par value at reset date)   │
│  └── Bóc tách biên thương mại (Commercial Margin Unbundling - Par 103)                          │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Phạm vi Xác định & Ranh giới Pháp lý (Inclusion & Exclusion Scope)

Theo quy định tại **Đoạn 101 của Chuẩn mực Basel d368**, ranh giới danh mục sổ ngân hàng chịu sự điều chỉnh của IRRBB được xác định theo nguyên tắc bao hàm và loại trừ nghiêm ngặt [[src-bcbs-irrbb-2016#^irrbb-u05-2]]:

### A. Các Danh mục Bắt buộc Bao gồm (Mandatory Inclusions)
Ngân hàng phải phóng chiếu toàn bộ dòng tiền tái định giá danh nghĩa trong tương lai từ các nguồn sau vào 19 dải kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u05-2]]:
1. **Mọi tài sản nhạy cảm với lãi suất (Interest rate-sensitive assets)** trên sổ ngân hàng không bị khấu trừ khỏi Vốn cấp 1 phổ thông (CET1) [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
2. **Mọi nợ phải trả nhạy cảm với lãi suất (Interest rate-sensitive liabilities)**, bao gồm cả các khoản tiền gửi không trả lãi (*non-remunerated deposits*) như tiền gửi thanh toán, tài khoản vãng lai [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
3. **Các khoản mục cam kết và công cụ phái sinh ngoại bảng (Off-balance sheet items)** có tính chất nhạy cảm với biến động lãi suất [[src-bcbs-irrbb-2016#^irrbb-u05-2]].

### B. Các Danh mục Bắt buộc Loại trừ (Mandatory Exclusions)
1. **Vốn cấp 1 phổ thông (CET1 Capital)**: Loại trừ hoàn toàn khỏi dòng tiền chiết khấu của thước đo [[economic-value-of-equity|$\Delta\text{EVE}$]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Vốn chủ sở hữu được xem là giá trị thặng dư ròng giữa tài sản và nợ, do đó không thể đưa vào để tự chiết khấu chính nó.
2. **Khoản đầu tư vốn cổ phần trên sổ ngân hàng (Equity exposures in the banking book)**: Cổ phiếu niêm yết, cổ phần doanh nghiệp chưa niêm yết do ngân hàng nắm giữ dài hạn được xử lý theo khuôn khổ rủi ro vốn cổ phần Trụ cột 1 (Credit Risk / Equity Framework), không tạo ra dòng tiền tái định giá lãi suất theo hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
3. **Tài sản cố định (Fixed Assets)**: Bất động sản văn phòng, đất đai, máy móc thiết bị và tài sản vô hình (phần mềm công nghệ) [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
4. **Các khoản mục đã khấu trừ khỏi Vốn tự có**: Lợi thế thương mại (Goodwill), tài sản thuế hoãn lại (DTA) dựa trên lợi nhuận tương lai.

### C. Bản chất Kế toán Dồn tích (Accruals Book) & Nguồn gốc Rủi ro P&L Tiềm ẩn (Moorad Choudhry)
- **Hạch toán theo giá gốc (Par / Amortised Cost)**: Các sản phẩm huy động và cho vay truyền thống không tái định giá theo thị trường được ghi nhận trong sổ ngân hàng (còn gọi là sổ dồn tích - *accruals book*) theo giá trị gốc ban đầu (thường là 100 hay 'par') và giữ nguyên giá trị đó cho đến khi đáo hạn [[src-choudhry-principles-banking#^choudhry-irrbb-1]].
- **Rủi ro thị trường không triệt tiêu**: Việc không đánh giá lại thường xuyên theo giá thị trường (*absence of marking-to-market*) không đồng nghĩa với việc sổ ngân hàng miễn nhiễm rủi ro thị trường [[src-choudhry-principles-banking#^choudhry-irrbb-1]]. Cuốn sổ này luôn đối mặt với rủi ro thu nhập (*earnings/P&L risk*) và rủi ro chi phí cơ hội (*opportunity cost foregone / accounting risk*) do cấu trúc tài trợ (*funding structure*): tài sản có kỳ hạn dài trong khi nợ có kỳ hạn ngắn [[src-choudhry-principles-banking#^choudhry-irrbb-1]]. Khi chi phí huy động vốn tăng lên, thu nhập lãi thuần (NII) lập tức bị bào mòn [[src-choudhry-principles-banking#^choudhry-irrbb-1]].

### D. Phân định Banking Book vs. Trading Book & Công cụ ALM (Fidelio Tata)
- **Ranh giới Sổ ngân hàng vs Sổ kinh doanh**: Sổ ngân hàng (Banking Book / nonregulatory trading book) bao gồm toàn bộ các giao dịch và vị thế có tính chất dài hạn gắn liền với hoạt động kinh doanh khách hàng và tài trợ cho chúng, bao gồm cả vốn chủ sở hữu [[src-tata-bank-alm#^tata-scope-1]]. Ngược lại, Sổ kinh doanh (Trading Book / regulatory trading book) thường bao gồm các vị thế nắm giữ nhằm bán lại ngắn hạn, hưởng lợi từ biến động giá ngắn hạn, tạo lợi nhuận chênh lệch giá (arbitrage) hoặc phòng ngừa rủi ro [[src-tata-bank-alm#^tata-scope-2]].
- **Nguyên tắc nhạy cảm lãi suất**: Chỉ có các công cụ nhạy cảm với lãi suất mới được đưa vào tính toán IRRBB và xây dựng [[repricing-balance-sheet|Bảng cân đối tái định giá]] [[src-tata-bank-alm#^tata-scope-3]]. Các tài sản bị khấu trừ khỏi Vốn cấp 1 CET1 (bất động sản, tài sản vô hình, cổ phần phi kinh doanh) bắt buộc phải loại trừ [[src-tata-bank-alm#^tata-scope-4]].
- **Phái sinh phòng hộ vs Vị thế nội bảng**: Phái sinh có thể được dùng để phòng hộ vi mô (*micro hedges*) cho từng vị thế bảng cân đối riêng lẻ, ví dụ asset swap cho một khoản vay lãi suất cố định [[src-tata-bank-alm#^tata-scope-5]]. Tuy vậy, theo nhận xét của tác giả, các ngân hàng có vẻ bù trừ bất cân xứng duration bằng các vị thế nội bảng (*on-balance-sheet positions*) thay vì dùng swap [[src-tata-bank-alm#^tata-scope-6]].

---

## 2. Ba Nhóm Vị thế theo Khả năng Chuẩn hóa Basel (Stage 1 Classification)

Tại Giai đoạn 1 của [[irrbb-standardised-framework|Khuôn khổ chuẩn hóa]], mọi vị thế danh mục sổ ngân hàng phải được xếp vào một trong ba nhóm theo mức độ phức tạp của hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-1]]:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        PHÂN LOẠI 3 NHÓM VỊ THẾ BẢNG CÂN ĐỐI (STAGE 1)                           │
├───────────────────────────────┬───────────────────────────────┬─────────────────────────────────┤
│ NHÓM 1: CÓ THỂ CHUẨN HÓA      │ NHÓM 2: ÍT CÓ KHẢ NĂNG CHUẨN  │ NHÓM 3: KHÔNG THỂ CHUẨN HÓA     │
│ (Amenable to standardisation) │ (Less amenable: Quyền chọn TĐ)│ (Not amenable: Quyền chọn HV)   │
├───────────────────────────────┼───────────────────────────────┼─────────────────────────────────┤
│ • Cho vay cố định ko trả trước│ • Khoản vay thả nổi có Cap/Flr│ • Tiền gửi không kỳ hạn NMDs    │
│ • Khoản vay thả nổi chuẩn     │ • Quyền chọn sàn tiền gửi Flr │ • Khoản vay cố định có trả trước│
│ • TPCP / Trái phiếu Bullet    │ • Hợp đồng Swaptions nhúng    │ • Tiền gửi kỳ hạn rút sớm (TDRR)│
│ • Tiền gửi kỳ hạn ko rút trước│ • Trái phiếu Callable/Puttable│ • Cam kết tín dụng bán lẻ       │
├───────────────────────────────┼───────────────────────────────┼─────────────────────────────────┤
│ ➔ Phân bổ trực tiếp vào       │ ➔ Bóc tách quyền chọn tự động;│ ➔ Áp dụng mô hình định lượng    │
│   19 dải kỳ hạn theo hợp đồng │   tính phụ phí KAO riêng biệt │   hành vi (Bảng 2, CPR, TDRR)   │
└───────────────────────────────┴───────────────────────────────┴─────────────────────────────────┘
```

1. **Vị thế có thể chuẩn hóa (*Amenable to standardisation*)**: Dòng tiền và ngày tái định giá được xác định hoàn toàn chắc chắn theo hợp đồng cho đến ngày đáo hạn hoặc ngày reset lãi suất tiếp theo [[src-bcbs-irrbb-2016#^irrbb-u05-1]].
2. **Vị thế ít có khả năng chuẩn hóa (*Less amenable to standardisation*)**: Chứa các quyền chọn lãi suất tự động (*Automatic Options*). Người nắm giữ chắc chắn thực hiện quyền dựa trên lợi ích kinh tế duy lý thuần túy. *Quy tắc xử lý*: Bóc tách quyền chọn để tính toán phụ phí $\text{KAO}_{i,c}$ riêng ở Giai đoạn 4; dòng tiền cơ sở không quyền chọn được xếp vào Giai đoạn 2 như công cụ thông thường [[src-bcbs-irrbb-2016#^irrbb-u05-3]].
3. **Vị thế không thể chuẩn hóa (*Not amenable to standardisation*)**: Chứa các quyền chọn hành vi (*Behavioural Options*) của khách hàng bán lẻ, không thể dự báo hoàn hảo bằng hợp đồng: [[non-maturity-deposits|NMDs / CASA]], cho vay trả trước hạn ([[behavioural-options|CPR]]), tiền gửi rút trước hạn ([[behavioural-options|TDRR]]) [[src-bcbs-irrbb-2016#^irrbb-u05-4]] [[src-bcbs-irrbb-2016#^irrbb-u05-5]].

---

## 3. Chi tiết Từng Danh mục Cấu phần Bảng Cân đối

### 3.1. Danh mục Tài sản (Assets)

#### A. Dư nợ Cho vay Khách hàng (Loans & Advances to Customers)
Là tài sản sinh lời lớn nhất của NHTM, tạo ra nguồn phơi nhiễm chính đối với [[gap-risk]], [[basis-risk]] và [[option-risk]]:
* **Cho vay Khách hàng Cá nhân (Retail Loans)**:
  - *Cho vay mua nhà thế chấp (Mortgages)*: Kỳ hạn dài (15–30 năm), thường có lãi suất cố định ban đầu (teaser rate 1–3 năm) sau đó thả nổi. Đi kèm **quyền chọn trả nợ trước hạn (prepayment option)**. Khi lãi suất thị trường giảm, khách hàng tái tài trợ ở ngân hàng khác, tạo ra **tính lồi âm (Negative Convexity)** và làm co ngắn thời lượng tài sản.
  - *Cho vay tiêu dùng & mua ô tô (Consumer & Auto Loans)*: Thường áp dụng lãi suất cố định theo lịch trả nợ đều (amortising schedule). Dòng tiền gốc và lãi được phân bổ đều vào các dải kỳ hạn ngắn và trung hạn.
* **Cho vay Doanh nghiệp (Corporate & Commercial Loans)**:
  - Thường áp dụng lãi suất thả nổi định kỳ (1M, 3M, 6M) cộng biên độ tín dụng (Credit spread).
  - *Rủi ro cơ sở (Benchmark Basis Risk)*: Khoản vay neo theo Lãi suất cơ sở (Prime Rate), trong khi nguồn vốn tài trợ neo theo SOFR hoặc lãi suất liên ngân hàng VNIBOR.
  - *Quyền chọn trần/sàn nhúng (Embedded Caps/Floors)*: Khi ngân hàng cho vay có cam kết sàn lãi suất (Floor) để bảo vệ NIM, ngân hàng nắm giữ quyền chọn mua sàn (Long Floor). Ngược lại, nếu cam kết trần lãi suất (Cap), ngân hàng bán khống quyền chọn (Short Cap) [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

#### B. Danh mục Trái phiếu Đầu tư & Đệm Thanh khoản ([[hqla|HQLA]])
Danh mục này được Khối Nguồn vốn (Treasury) quản trị, nắm giữ chủ yếu Trái phiếu Chính phủ, Trái phiếu Chính quyền địa phương, và Trái phiếu Doanh nghiệp. 

Tác động của danh mục này lên IRRBB phụ thuộc chặt chẽ vào **Phân loại Kế toán (IFRS 9 / Chuẩn mực Kế toán)** [[src-bcbs-irrbb-2016#^irrbb-u06-1]]:

| Phân loại Kế toán | Bản chất & Mục đích Nắm giữ | Cơ chế Phản ánh Kế toán | Tác động lên IRRBB & Vốn |
|---|---|---|---|
| **Giá trị Phân bổ (Amortised Cost / HTM)** | Nắm giữ chứng khoán cho đến ngày đáo hạn để thu dòng tiền gốc và lãi. | Ghi nhận theo nguyên giá phân bổ. Biến động giá thị trường **bị bỏ qua** trên P&L và Bảng cân đối [[src-bcbs-irrbb-2016#^irrbb-u06-1]]. | **Gánh chịu toàn bộ rủi ro kinh tế $\Delta\text{EVE}$**. Nếu bị ép bán tháo để cứu thanh khoản, lỗ vô hình biến thành lỗ hữu hình phá hủy vốn (bài học SVB). |
| **Giá trị Hợp lý qua OCI (Fair Value through OCI / AFS)** | Danh mục sẵn sàng để bán hoặc duy trì đệm thanh khoản [[lcr]]. | Đánh giá lại theo giá thị trường hàng ngày/tháng. Lỗ/lãi chưa thực hiện **ghi nhận vào OCI** [[src-bcbs-irrbb-2016#^irrbb-u06-1]]. | **Ảnh hưởng trực tiếp đến Vốn cấp 1 CET1** và tỷ lệ an toàn vốn CAR [[src-bcbs-irrbb-2016#^irrbb-u06-1]]. Khi lãi suất tăng, OCI âm làm bốc hơi vốn tự có ngay lập tức. |
| **Giá trị Hợp lý qua P&L (FVTPL / Trading Book)** | Các chứng khoán đầu tư ngắn hạn có ý định kinh doanh chênh lệch giá. | Đánh giá theo thị trường (*mark-to-market*). | Biến động lãi suất **chảy trực tiếp vào P&L**, gây biến động thu nhập ngắn hạn [[src-bcbs-irrbb-2016#^irrbb-u06-1]]. |

* **Cạm bẫy Thời lượng của Đệm HQLA**: Để tối ưu hóa chỉ số thanh khoản [[lcr]] (hệ số haircut $0\%$) và [[nsfr]] (hệ số RSF $5\%$), Treasury thường tích lũy TPCP dài hạn 10Y–15Y, tạo ra thời lượng tài sản khổng lồ ($D_A > 8$ năm), đe dọa kích hoạt ngưỡng vi phạm 15% Vốn cấp 1 của [[outlier-bank-test]] khi lợi suất tăng vọt.

#### C. Tiền gửi & Cho vay Thị trường Tiền tệ / Liên ngân hàng
* **Dự trữ Bắt buộc & Tiền gửi Thanh toán tại Ngân hàng Trung ương**: Thường có lãi suất cố định rất thấp hoặc $0\%$, kỳ hạn tái định giá qua đêm.
* **Cho vay Liên ngân hàng (Interbank Placements / Reverse Repo)**: Kỳ hạn ngắn (qua đêm đến 3 tháng), tái định giá tức thì, đóng vai trò hấp thụ và truyền dẫn nhanh nhất các quyết định chính sách tiền tệ vào thu nhập $\Delta\text{NII}$.

---

### 3.2. Danh mục Nợ phải trả (Liabilities)

#### A. [[non-maturity-deposits|Tiền gửi Không kỳ hạn (Non-Maturity Deposits - NMDs / CASA)]]
Cấu phần nợ phức tạp nhất và có tầm ảnh hưởng lớn nhất đến kết quả đo lường IRRBB của NHTM [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:
* **Đặc tính kinh tế**: Khách hàng có quyền pháp lý rút tiền bất kỳ lúc nào tại mệnh giá mà không bị phạt ($T=0$), nhưng trên thực tế hành vi, một tỷ lệ lớn số dư tiền gửi này duy trì ổn định dài hạn với lãi suất cực thấp [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
* **Phân định Hai Cấu phần Bắt buộc (BCBS d368 Table 2)**:
  1. **Phần Phi Lõi (*Non-core Deposits*)**: Khối lượng tiền gửi không ổn định, biến động giật cục. Bắt buộc phải xếp vào **Dải kỳ hạn ngắn nhất / Qua đêm ($t_1 = 0.0028$ năm)** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
  2. **Phần Lõi (*Core Deposits*)**: Khối lượng tiền gửi khó có khả năng tái định giá ngay cả khi môi trường lãi suất thị trường thay đổi mạnh. Được phép phân bổ vào các dải kỳ hạn trung và dài hạn nhưng không được vượt quá các trần quy định [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:
     - *Bán lẻ - Tài khoản giao dịch*: Trần tiền gửi lõi **90%**, trần kỳ hạn bình quân **5.0 năm**.
     - *Bán lẻ - Tài khoản phi giao dịch*: Trần tiền gửi lõi **70%**, trần kỳ hạn bình quân **4.5 năm**.
     - *Bán buôn*: Trần tiền gửi lõi **50%**, trần kỳ hạn bình quân **4.0 năm** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
* **Hệ số Co giãn Lãi suất (Deposit Pass-through Beta - $\beta_{\text{dep}}$)**:
  $$\Delta r_{\text{dep}} = \beta_{\text{dep}} \cdot \Delta r_{\text{mkt}}$$
  Trong môi trường lãi suất thấp, $\beta_{\text{dep}} \approx 0.1 - 0.2$. Khi lãi suất tăng cao, khách hàng chuyển dịch mạnh từ CASA sang tiền gửi tiết kiệm có kỳ hạn (*deposit flight / cannibalisation*), đẩy $\beta_{\text{dep}} \rightarrow 0.6 - 0.8$, làm bùng nổ chi phí lãi vay và bào mòn $\Delta\text{NII}$.

#### B. Tiền gửi Có kỳ hạn (Term Deposits)
* **Tiền gửi Tiết kiệm Bán lẻ**:
  - Chịu rủi ro khách hàng rút tiền trước hạn ([[behavioural-options|Early Redemption Risk - TDRR]]) khi lãi suất thị trường tăng cao hơn lãi suất cam kết trên sổ tiết kiệm [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
  - Hệ số co giãn rút tiền trước hạn $u_i = 1.2$ trong kịch bản lãi suất tăng (Parallel up, Flattener) và $u_i = 0.8$ trong kịch bản lãi suất giảm [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
* **Tiền gửi Có kỳ hạn Bán buôn (Corporate & Institutional Term Deposits)**:
  - Doanh nghiệp lớn và định chế tài chính hành xử duy lý kinh tế. Nếu hợp đồng cho phép rút sớm không phạt kinh tế tương ứng, khoản mục này bị xếp vào nhóm **Quyền chọn tự động bán buôn** (Stage 4) [[src-bcbs-irrbb-2016#^irrbb-u05-3]].

#### C. Vay nợ Bán buôn & Giấy tờ có giá (Wholesale Funding & Debt Issuance)
* **Chứng chỉ tiền gửi (Certificates of Deposit - CDs) & Trái phiếu Ngân hàng**: Công cụ tài trợ có kỳ hạn cố định hoặc thả nổi, ngày tái định giá rõ ràng theo hợp đồng.
* **Vay chiết khấu / Tái cấp vốn từ Ngân hàng Trung ương**: Dòng tiền ngắn hạn neo chặt theo lãi suất điều hành chính sách.

---

### 3.3. Danh mục Ngoại bảng & Công cụ Phái sinh (Off-Balance Sheet & Derivatives)

#### A. Cam kết Tín dụng & Rủi ro Đường ống (Loan Commitments & Pipeline Risk)
* Khi ngân hàng cam kết cấp tín dụng hoặc cam kết mức lãi suất cho vay cố định trong thời gian chờ giải ngân (thường 30–90 ngày đối với mua nhà):
  - Ngân hàng đã cấp một **quyền chọn bán lãi suất miễn phí** cho khách hàng.
  - Khi lãi suất thị trường tăng vọt, khách hàng ồ ạt thực hiện cam kết giải ngân ở mức lãi suất rẻ đã chốt trước, buộc ngân hàng phải tài trợ tài sản lợi suất thấp bằng nguồn vốn huy động giá cao mới.

#### B. Các Công cụ Phái sinh Phòng hộ Danh mục (ALM Hedging Derivatives)
Là công cụ do Khối ALM Treasury giao dịch nhằm tái cấu trúc khe hở thời lượng tổng thể mà không làm thay đổi tài sản vật lý:
1. **[[interest-rate-swap|Hợp đồng Hoán đổi Lãi suất (IRS)]]**:
   - *Pay-Fixed IRS (Trả Cố định / Nhận Thả nổi)*: Rút ngắn thời lượng ròng của bảng cân đối ($D_{\text{net}} \downarrow$), phòng hộ danh mục trái phiếu TPCP hoặc dư nợ cho vay cố định dài hạn trước nguy cơ tăng lãi suất.
   - *Receiver IRS (Nhận Cố định / Trả Thả nổi)*: Kéo dài thời lượng ròng ($D_{\text{net}} \uparrow$), khóa biên lãi ròng NII khi dự báo lãi suất sắp giảm sâu.
2. **[[interest-rate-cap-floor|Interest Rate Caps & Floors]]**: Phòng hộ rủi ro phi tuyến tính, trung hòa các quyền chọn trần/sàn đã bán cho khách hàng vay hoặc gửi tiền.
3. **[[swaption|Swaptions]]**: Công cụ phòng vệ tối ưu nhất để triệt tiêu tính lồi âm phát sinh từ quyền chọn trả nợ trước hạn CPR của danh mục cho vay mua nhà.

---

## 4. Cơ chế Phân bổ Dòng tiền vào 19 Dải Kỳ hạn (Cash Flow Slotting Rules)

Quy trình phân bổ dòng tiền tái định giá danh nghĩa theo **Đoạn 101–104 của BCBS d368** tuân thủ các nguyên tắc giải tích sau [[src-bcbs-irrbb-2016#^irrbb-u05-2]]:

```
DÒNG TIỀN TÁI ĐỊNH GIÁ DANH NGHĨA CF(t_k)
├── 1. Dòng tiền Hoàn trả Gốc (Principal Repayments): Theo ngày đáo hạn hoặc phân kỳ trả nợ hợp đồng.
├── 2. Dòng tiền Tái định giá Gốc (Principal Repricings): Ngày đầu tiên mà lãi suất bị thay đổi đơn phương.
└── 3. Dòng tiền Thanh toán Lãi (Interest Payments): Dòng coupon cho đến ngày tái định giá hoặc đáo hạn.
```

### Quy tắc Xử lý Công cụ Lãi suất Thả nổi (Floating Rate Instruments)
Theo par 104, công cụ lãi suất thả nổi được giả định **tái định giá 100% về mệnh giá (par value) tại ngày xác định lại lãi suất tiếp theo (first reset date)** [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. Do đó:
* Toàn bộ giá trị danh nghĩa gốc được xếp vào dải kỳ hạn chứa ngày reset đầu tiên.
* Không phân bổ bất kỳ dòng tiền gốc nào vào các dải kỳ hạn sau ngày reset đầu tiên (trừ phần chênh lệch spread biên thương mại cố định nếu có) [[src-bcbs-irrbb-2016#^irrbb-u05-2]].

### Xử lý Biên Thương mại và Phần bù Spread (Commercial Margins - Par 103)
Theo par 103, ngân hàng có quyền lựa chọn:
1. **Loại trừ Biên Thương mại (Deduct Commercial Margins)**: Chiết khấu dòng tiền thuần theo đường cong phi rủi ro chuẩn (Risk-free curve / OIS) [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
2. **Giữ lại Biên Thương mại (Include Commercial Margins)**: Dòng tiền bao gồm cả biên thương mại, nhưng phải chiết khấu theo đường cong phi rủi ro cộng thêm phần bù biên thương mại tương ứng [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
*Quy tắc nhất quán*: Phương pháp luận được chọn phải minh bạch, thận trọng và áp dụng nhất quán xuyên suốt cho cả tài sản và nợ [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

---

## 5. Bảng Tổng hợp Ma trận Danh mục & Rủi ro Lãi suất

| Danh mục Bảng Cân đối | Loại hình Dòng tiền | Nhóm Chuẩn hóa (Stage 1) | Rủi ro IRRBB Trọng tâm | Thước đo Bị ảnh hưởng Nặng nhất |
|---|---|---|---|---|
| **Cho vay Nhà ở Lãi suất Cố định** | Dòng tiền giảm dần theo lịch khấu hao (Amortising) | Không chuẩn hóa (Not amenable) | [[gap-risk]], [[option-risk]] (Prepayment CPR) | [[economic-value-of-equity\|$\Delta\text{EVE}$]] (Tính lồi âm) |
| **Cho vay Doanh nghiệp Thả nổi** | Tái định giá định kỳ 3M/6M | Có thể chuẩn hóa (Amenable) | [[basis-risk]] (Prime vs SOFR), Cap/Floor | [[net-interest-income-sensitivity\|$\Delta\text{NII}$]] |
| **Trái phiếu Chính phủ HTM / AFS** | Bullet (gốc cuối kỳ, coupon định kỳ) | Có thể chuẩn hóa (Amenable) | [[gap-risk]] (Duration dài hạn) | [[economic-value-of-equity\|$\Delta\text{EVE}$]] & Vốn cấp 1 CET1 (AFS) |
| **Tiền gửi CASA (NMDs Lõi)** | Dòng tiền ổn định dài hạn (Replicating) | Không chuẩn hóa (Not amenable) | [[gap-risk]], Hành vi rút vốn & Beta | [[net-interest-income-sensitivity\|$\Delta\text{NII}$]] |
| **Tiền gửi CASA (Phi Lõi)** | Dòng tiền biến động ngắn hạn | Không chuẩn hóa ➔ Xếp dải Qua đêm | [[gap-risk]] ngắn hạn | [[net-interest-income-sensitivity\|$\Delta\text{NII}$]] |
| **Tiền gửi Tiết kiệm Kỳ hạn** | Dòng tiền hợp đồng cố định | Không chuẩn hóa (Not amenable) | [[option-risk]] (Rút trước hạn TDRR) | [[net-interest-income-sensitivity\|$\Delta\text{NII}$]] & $\Delta\text{EVE}$ |
| **Hoán đổi Lãi suất (Pay-Fixed IRS)** | Dòng tiền trao đổi cố định/thả nổi | Có thể chuẩn hóa (Derivative) | Phòng ngừa Gap Risk | Cân bằng cả $\Delta\text{EVE}$ và $\Delta\text{NII}$ |
| **Quyền chọn Caps / Floors / Swaptions** | Dòng tiền quyền chọn phi tuyến | Ít có khả năng chuẩn hóa (Stage 4) | [[option-risk]] tự động ($\text{KAO}$) | Phụ phí $\text{KAO}_{i,c}$ của $\Delta\text{EVE}$ |

---

## 6. Liên kết Hệ thống ALM Wiki

Khung phân loại danh mục bảng cân đối liên kết hữu cơ với toàn bộ kho tri thức ALM:
* **Kiến trúc Tổng thể**: [[irrbb-five-tier-architecture]] (Tầng 1 & Tầng 3), [[irrbb-alm-governance-strategy-and-tradeoffs]] (Mục 3: Cạm bẫy Thời lượng HQLA).
* **Phương pháp luận Đo lường**: [[irrbb-standardised-framework]] (Stage 1 & 2), [[economic-value-of-equity]], [[net-interest-income-sensitivity]].
* **Các Phân loại Rủi ro**: [[gap-risk]], [[basis-risk]], [[option-risk]], [[behavioural-options]], [[non-maturity-deposits]], [[csrbb]].
* **Công cụ & Mô hình Định lượng**: [[interest-rate-swap]], [[interest-rate-cap-floor]], [[swaption]], [[duration-gap-model]], [[key-rate-duration]], [[replicating-portfolio-model]].
* **Quy chuẩn Thanh khoản Basel**: [[hqla]], [[lcr]], [[nsfr]], [[lcr-nsfr-interlinkages]].

## Đề xuất cập nhật
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 103): mục "Xử lý Biên Thương mại và Phần bù Spread (Par 103)" (dòng 209–213) gán nội dung par 103 cho [[src-bcbs-irrbb-2016#^irrbb-p08-2]] (par 70, đường cong chiết khấu ∆EVE). Đề xuất: câu dẫn "Theo par 103, ngân hàng có quyền lựa chọn" cite [[src-bcbs-irrbb-2016#^irrbb-u05-15]] (trừ hay giữ commercial margin trong notional repricing cash flow, phương pháp thận trọng và minh bạch); hai bullet về đường cong chiết khấu giữ cite p08-2; dòng "Quy tắc nhất quán … cho cả tài sản và nợ" không có trong u05-15 lẫn p08-2, đổi thành "phương pháp phải thận trọng và minh bạch" [[src-bcbs-irrbb-2016#^irrbb-u05-15]] và ghi phần "nhất quán" là `[cần nguồn]`.
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; đề xuất link ở lần nhắc đầu "dòng tiền tái định giá danh nghĩa" (dòng 66).
