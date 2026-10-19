---
title: "Credit Spread Risk in the Banking Book (CSRBB)"
aliases: [CSRBB, Rủi ro chênh lệch tín dụng trên sổ ngân hàng, Credit Spread Risk Banking Book]
type: concept
domains: [alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-3]]"}
  - {type: drives, to: "[[economic-value-of-equity]]", direction: "-", regime: stress, cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-3]]"}
tags: [csrbb, credit-spread, banking-book, basel, market-credit-spread, liquidity-spread]
updated: 2026-10-17
reviewed:
---

## Định nghĩa
Rủi ro chênh lệch tín dụng trên sổ ngân hàng (Credit Spread Risk in the Banking Book - CSRBB) là rủi ro phát sinh từ các biến động bất lợi của chênh lệch lợi suất (credit spread) đối với các công cụ tài chính chịu rủi ro tín dụng trên sổ ngân hàng, mà không được giải thích bởi rủi ro lãi suất trên sổ ngân hàng ([[bcbs-irrbb|IRRBB]]) hay rủi ro tín dụng dự kiến/rủi ro vỡ nợ đột ngột (jump-to-default risk) [[src-bcbs-irrbb-2016#^irrbb-u02-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]].

CSRBB phản ánh sự biến động trong mức độ chấp nhận rủi ro và nhận định của thị trường về chất lượng tín dụng chung hoặc tính thanh khoản của một nhóm công cụ tài chính, dẫn đến sự giãn rộng hoặc thu hẹp của phần bù rủi ro thị trường [[src-bcbs-irrbb-2016#^irrbb-u06-3]].

## Cấu trúc các thành phần Lãi suất và Phân định Ranh giới

Để làm rõ ranh giới giữa IRRBB và CSRBB, Chuẩn mực Basel d368 (Annex 1) chia tách lãi suất của mọi công cụ tài chính thành 5 thành phần cơ bản [[src-bcbs-irrbb-2016#^irrbb-u06-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]]:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TOÀN BỘ CẤU THÀNH LÃI SUẤT                            │
├──────────────────────────────────────┬──────────────────────────────────────┤
│           PHẠM VI IRRBB              │            PHẠM VI CSRBB             │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 1. Lãi suất phi rủi ro (Risk-free)   │ 3. Spread thanh khoản thị trường     │
│ 2. Spread thời lượng thị trường      │    (Market liquidity spread)         │
│    (Market duration spread)          │ 4. Spread tín dụng thị trường chung  │
│ *  Lãi suất tham chiếu (Reference)   │    (General market credit spread)    │
│ *  Biên tài trợ (Funding margin)     │                                      │
└──────────────────────────────────────┴──────────────────────────────────────┘
   [Loại trừ: 5. Spread tín dụng đặc thù của người vay (Idiosyncratic credit spread)
    -> Thuộc phạm vi đo lường rủi ro tín dụng Trụ cột 1 Credit Risk]
```

- **Thuộc phạm vi IRRBB**: Biến động của lãi suất phi rủi ro, spread thời lượng thị trường, lãi suất tham chiếu và biên tài trợ nội bộ [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- **Thuộc phạm vi CSRBB**: Tích hợp biến động của **spread thanh khoản thị trường** và **spread tín dụng thị trường chung** [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- **Ngoại trừ khỏi CSRBB**: Rủi ro tín dụng đặc thù (idiosyncratic credit spread) và rủi ro vỡ nợ (jump-to-default risk) vốn đã được tính toán trong yêu cầu vốn rủi ro tín dụng Trụ cột 1 [[src-bcbs-irrbb-2016#^irrbb-u02-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-2]].

## Tác động kế toán và Rủi ro thanh khoản

### 1. Phân loại kế toán và Tác động vốn (Accounting Impact)
Theo Annex 1 đoạn 1.2 của d368 [[src-bcbs-irrbb-2016#^irrbb-u06-1]]:
- **Tài sản định giá theo giá trị phân bổ (Amortised cost)**: Ví dụ các khoản cho vay và trái phiếu giữ đến ngày đáo hạn (HTM). Biến động của credit spread không làm thay đổi giá trị ghi sổ tức thời, nhưng khi phát sinh suy giảm giá trị (impairment), ngân hàng phải trích lập dự phòng rủi ro.
- **Tài sản định giá theo giá trị hợp lý (Fair value / FVTOCI / AFS)**: Ví dụ danh mục trái phiếu sẵn sàng để bán hoặc trái phiếu chính phủ/doanh nghiệp trong đệm thanh khoản. Khi credit spread thị trường giãn rộng (spread widening), giá trị thị trường của tài sản sụt giảm ngay lập tức, ghi nhận lỗ vào Vốn chủ sở hữu thông qua OCI (hoặc P&L nếu FVTPL), trực tiếp làm xói mòn Vốn cấp 1 (Tier 1 Capital) của ngân hàng.

### 2. Mối liên hệ với Đệm HQLA và LCR
- **Rủi ro kép đối với Trái phiếu Level 2A và Level 2B**: Khác với trái phiếu chính phủ Level 1 (không có rủi ro tín dụng), các tài sản Level 2A (trái phiếu chính quyền địa phương, trái phiếu doanh nghiệp bảo đảm) và Level 2B (trái phiếu doanh nghiệp thông thường) trong [[hqla]] vừa chịu rủi ro IRRBB vừa chịu rủi ro CSRBB rất cao.
### 3. Góc nhìn Thực tiễn Ngân hàng và Đo lường CS01 (Moorad Choudhry)
Theo Moorad Choudhry (*The Principles of Banking*, Ch. 7) [[src-choudhry-principles-banking#^choudhry-irrbb-13]]:
> "Under international guidance, credit spread risk (the risk of impact on earnings and balance sheet value as a result of changes in credit spread) is also in scope in IRRBB rules. The author's view is that this is most applicable to a bond portfolio, and it may be captured for EVE risk purposes using a 'CS01'- type measure."

- **Phạm vi áp dụng thực tế**: Dù định nghĩa lý thuyết của Basel có thể mở rộng sang các tài sản tín dụng khác, trong thực tế điều hành ngân hàng, rủi ro CSRBB áp dụng rõ ràng và trọng yếu nhất đối với **danh mục trái phiếu (bond portfolio)** — đặc biệt là danh mục Eurobonds và trái phiếu doanh nghiệp hạch toán theo giá trị hợp lý (FVOCI/AFS).
- **Thước đo độ nhạy CS01**: Để quản lý rủi ro EVE do credit spread biến động, Treasury và ALM sử dụng thước đo **CS01** (Credit Spread 01, tương tự như PV01/DV01 đối với rủi ro lãi suất chuẩn) — đo lường mức thay đổi giá trị hiện tại (Present Value) của danh mục tài sản khi biên độ tín dụng (credit spread) dịch chuyển song song 1 điểm cơ bản (1 bp = 0.01%).

## Yêu cầu quản trị theo Basel (Nguyên tắc 1)
- Dù trọng tâm văn bản d368 tập trung vào IRRBB, Nguyên tắc 1 và 15 nêu rõ tất cả ngân hàng phải thiết lập hệ thống nhận diện, theo dõi và đánh giá CSRBB một cách độc lập và đồng bộ với khung quản trị IRRBB và ICAAP [[src-bcbs-irrbb-2016#^irrbb-p01-1]].
- Xem thêm tại [[bcbs-irrbb]], [[economic-value-of-equity]], [[gap-risk]], [[basis-risk]], [[integrated-alm-liquidity-strategy]].

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9 — chờ user duyệt: đã có node [[icaap]] (và stub [[economic-capital]]); đề xuất link ở lần nhắc đầu ICAAP / vốn kinh tế.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M3 — chờ user duyệt: đã có node [[market-risk-management]]; đề xuất link ở chỗ phân định ranh giới sổ ngân hàng/sổ kinh doanh. TT83 Đ35–37 không nhắc credit spread; rủi ro lãi suất thuộc rủi ro thị trường gắn với sổ kinh doanh [[src-tt83-2025-nhnn#^d3-15a]].
- [2026-10-19] ingest src-bardaeva-alm u03 — chờ user duyệt: đã có node [[irrbb-management]]; đề xuất link ở lần nhắc đầu "quản trị IRRBB" / quy trình nhận diện, đo lường, kiểm soát.
