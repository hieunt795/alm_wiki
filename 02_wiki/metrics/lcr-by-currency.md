---
title: "LCR by Significant Currency — Tỷ Lệ LCR Theo Ngoại Tệ Trọng Yếu (Basel SRP50)"
aliases: [LCR by Currency, LCR theo ngoại tệ, FX LCR, Significant Currency LCR, Tỷ lệ LCR theo từng đồng tiền]
type: metric
domains: [basel, alm]
status: active
maturity: draft
sources: ["[[src-bcbs-framework]]", "[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[bcbs]]", cite: "[[src-bcbs-framework#^srp50-1]]"}
  - {type: part-of, to: "[[lcr]]", cite: "[[src-bcbs-framework#^srp50-35]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-framework#^srp50-35]]"}
tags: [liquidity, lcr, fx-liquidity, foreign-currency, significant-currency, currency-mismatch, srp50, basel]
updated: 2026-10-20
reviewed:
---

## Tóm tắt Cấp cao (Executive Summary)

**LCR theo Ngoại tệ Trọng yếu (LCR by Significant Currency)** là chỉ số giám sát thanh khoản quy định tại **BCBS SRP50.35**, yêu cầu ngân hàng và cơ quan thanh tra giám sát phải theo dõi riêng biệt tỷ lệ đảm bảo khả năng thanh khoản cho từng loại tiền tệ cấu thành phần trọng yếu trong cơ cấu nợ của ngân hàng [[src-bcbs-framework#^srp50-35]].

Mặc dù chuẩn mực pháp định [[lcr]] chỉ bắt buộc tuân thủ ngưỡng $\ge 100\%$ trên cơ sở **tổng tiền tệ hợp nhất quy đổi (single consolidated currency)** [[src-bcbs-framework#^srp50-35]], thực tế lịch sử khủng hoảng tài chính chứng minh: **một ngân hàng có LCR tổng hợp đạt 150% vẫn có thể sụp đổ vì mất khả năng thanh toán nếu thặng dư thanh khoản nằm ở đồng nội tệ nhưng thâm hụt nghiêm trọng dòng tiền thanh toán bằng ngoại tệ mạnh (USD, EUR)**.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                     CÔNG THỨC VÀ TIÊU CHÍ XÁC ĐỊNH LCR THEO NGOẠI TỆ TRỌNG YẾU                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. NGƯỠNG ĐỊNH DANH NGOẠI TỆ TRỌNG YẾU (SIGNIFICANT CURRENCY THRESHOLD):                        │
│                                                                                                 │
│            Tổng Nợ Phải Trả bằng Ngoại tệ X                                                     │
│            ───────────────────────────────── ≥ 5.0% Tổng Nợ Toàn Ngân Hàng                      │
│                   Tổng Nợ Toàn Ngân Hàng                                                        │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. CÔNG THỨC XÁC ĐỊNH TỶ LỆ LCR RIÊNG BIỆT:                                                     │
│                                                                                                 │
│                           Kho HQLA bằng Ngoại tệ X                                              │
│         LCR_X = ───────────────────────────────────────────── (Theo dõi giám sát)               │
│                 Tổng Dòng Tiền Ra Ròng 30 Ngày bằng Ngoại tệ X                                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. BẢN CHẤT PHÁP LÝ & ĐIỀU HÀNH:                                                                │
│  • Không phải mức sàn pháp định cứng 100% của Basel (được áp dụng như công cụ giám sát Trụ cột 2)│
│  • Cơ quan giám sát quốc gia có quyền quyết định áp ngưỡng bắt buộc (National Discretion)       │
│  • Bóc trần rủi ro cạn kiệt thị trường hoán đổi tiền tệ (FX Swap Market Freeze)                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Tiêu Chí Xác Định Ngoại Tệ Trọng Yếu (SRP50.37)

Theo quy định tại **SRP50.37**, một loại tiền tệ được phân loại là **ngoại tệ trọng yếu (significant currency)** khi thỏa mãn điều kiện định lượng:
$$\text{Tỷ trọng Nợ Ngoại tệ } X = \frac{\text{Tổng Nợ Phải Trả danh nghĩa bằng Ngoại tệ } X}{\text{Tổng Nợ Phải Trả toàn bộ Bảng Cân đối}} \ge 5.0\%$$
[[src-bcbs-framework#^srp50-37]]

*Ví dụ thực tế*: Tại hệ thống ngân hàng thương mại Việt Nam, đồng Đô la Mỹ (**USD**) luôn là ngoại tệ trọng yếu vượt xa ngưỡng 5% tổng công nợ, đòi hỏi Khối Nguồn vốn & ALM Treasury phải thiết lập mô hình tính toán LCR bằng USD song song với LCR bằng VND.

---

## 2. Phương Pháp Luận Đo Lường LCR Ngoại Tệ

Phương pháp xác định các thành phần của LCR ngoại tệ tuân thủ toàn diện các quy tắc định giá dòng tiền của LCR chuẩn:
1. **Tử số — HQLA bằng Ngoại tệ X**:
   - Tiền mặt và dự trữ khả dụng bằng ngoại tệ X tại NHTW phát hành đồng tiền đó (ví dụ: tiền gửi USD tại Cục Dự trữ Liên bang Mỹ - Fed).
   - Trái phiếu chính phủ bằng ngoại tệ X đủ chuẩn Level 1 (ví dụ: Trái phiếu Kho bạc Mỹ - US Treasuries).
   - Nếu sử dụng HQLA bằng đồng tiền khác chuyển đổi qua phái sinh, phải áp dụng mức chiết khấu rủi ro tỷ giá tối thiểu $8\%$ theo quy chuẩn [[alternative-liquidity-approaches|ALA Option 2]].
2. **Mẫu số — Tổng Dòng Tiền Ra Ròng 30 Ngày bằng Ngoại tệ X**:
   - Dòng tiền rút vốn giả định của tiền gửi bán lẻ và bán buôn bằng ngoại tệ X.
   - Các nghĩa vụ phát sinh từ hợp đồng phái sinh ngoại hối (FX Forwards, FX Swaps, [[cross-currency-swap|Cross-Currency Swaps]]) đáo hạn trong 30 ngày.
   - Áp dụng trần khống chế dòng tiền vào $75\%$ trên tổng dòng tiền ra gộp bằng ngoại tệ X.

---

## 3. Rủi Ro Đóng Băng Thị Trường FX Swap (FX Swap Market Freeze)

Lý do sâu xa Ủy ban Basel thiết lập chỉ số LCR theo ngoại tệ bắt nguồn từ **cạm bẫy hoán đổi tiền tệ**:
* Trong điều kiện bình thường, các ngân hàng thường tự tin rằng họ có thể dễ dàng chuyển đổi thặng dư thanh khoản VND/EUR sang USD thông qua thị trường **FX Swap** liên ngân hàng ngắn hạn.
* **Cú sốc thị trường căng thẳng**: Khi khủng hoảng nổ ra, thị trường FX Swap toàn cầu hoặc cục bộ lập tức bị thắt chặt và đóng băng (*liquidity dislocation / dollar shortage*). Chi phí hoán đổi ngoại tệ (FX basis spread) tăng vọt, các đối tác quốc tế cắt đứt hạn mức tín chấp.
* Khi đó, ngân hàng nắm giữ hàng nghìn tỷ đồng nội tệ thặng dư cũng **không thể chuyển hóa thành USD** để thanh toán cho các khoản nợ vay quốc tế hoặc tiền gửi doanh nghiệp xuất nhập khẩu đến hạn, dẫn đến vỡ nợ kỹ thuật bằng ngoại tệ.

---

## 4. Cơ Chế Điều Hành của ALCO và ALM Treasury

Để kiểm soát rủi ro thanh khoản ngoại tệ:
1. **Thiết lập Khẩu vị Rủi ro Nội bộ**: [[alco|ALCO]] quy định ngưỡng chặn an toàn nội bộ $\text{LCR}_{\text{USD}} \ge 80\% – 100\%$, ngăn chặn tuyệt đối tình trạng lấy thanh khoản nội tệ bảo kê cho sự thâm hụt ngoại tệ dài hạn.
2. **Cơ cấu Kho Đệm HQLA Ngoại tệ**: Duy trì một tỷ lệ tối thiểu danh mục Trái phiếu Chính phủ Mỹ (US Treasuries) hoặc tiền gửi tại các ngân hàng đại lý hàng đầu để sẵn sàng monetise khi có biến cố.
3. **Giới hạn Lệch pha Kỳ hạn Ngoại tệ (FX Maturity Gap Limit)**: Đặt trần thâm hụt dòng tiền ròng USD tại các dải kỳ hạn 7 ngày, 30 ngày và 3 tháng.

---

## Nguyên tắc nền: [[bcbs-liquidity-principles|BCBS 144]] (P5 para 43–44, P6 para 61, 63)
- Ngân hàng nên đánh giá tổng nhu cầu thanh khoản ngoại tệ, xác định mức chênh lệch tiền tệ chấp nhận được, phân tích riêng từng đồng tiền có hoạt động đáng kể, tính đến rủi ro thị trường FX swap bị suy giảm hoặc đóng hẳn [[src-bcbs-liquidity-principles-2008#^lrm-43]].
- Biến động đột ngột của tỷ giá hoặc thanh khoản thị trường có thể nới rộng chênh lệch thanh khoản và làm giảm hiệu quả phòng hộ ngoại hối [[src-bcbs-liquidity-principles-2008#^lrm-44]].
- Hạn mức nội bộ theo đồng tiền nên chặt hơn khi khả năng chuyển đổi không chắc chắn [[src-bcbs-liquidity-principles-2008#^lrm-61]]; ngân hàng nên đánh giá rủi ro khả năng swap suy giảm nhanh trong stress [[src-bcbs-liquidity-principles-2008#^lrm-63]].

## Góc nhìn VN (TT50/2026)

- TT50 phân biệt ba loại LCR: LCR quy VNĐ, LCR VNĐ, LCR ngoại tệ trọng yếu [[src-tt50-2026-nhnn#^d16-1]].
- Ngân hàng phải quản lý LCR VNĐ riêng lẻ; LCR ngoại tệ trọng yếu và LCR hợp nhất được quản lý theo quy định nội bộ. Ngân hàng báo cáo NHNN LCR quy VNĐ và LCR VNĐ riêng lẻ [[src-tt50-2026-nhnn#^d16-2]].
- Với đồng tiền trọng yếu (VNĐ và ngoại tệ trọng yếu theo quy định nội bộ), ngân hàng phải xét đặc điểm thị trường và khả năng hoán đổi tiền tệ trong căng thẳng [[src-tt50-2026-nhnn#^d14-4]].

*Diễn giải:* SRP50 dùng LCR theo đồng tiền làm công cụ giám sát, không đặt ngưỡng tối thiểu. TT50 cũng không đặt ngưỡng cho LCR ngoại tệ trọng yếu, nhưng tiêu chí "trọng yếu" do ngân hàng tự đặt thay vì ngưỡng 5% của SRP50.

## 5. Ma trận Liên kết Hệ thống ALM Wiki

* **Chuẩn mực Nguồn**: [[src-bcbs-framework]] (Chương SRP50, claims ^srp50-35 đến ^srp50-39), [[src-bcbs-lcr]].
* **Các Chỉ số & Khái niệm**: [[lcr]], [[hqla]], [[net-cash-outflows]], [[contractual-maturity-mismatch]], [[funding-concentration-risk]], [[alternative-liquidity-approaches]].
* **Chiến lược Quản trị**: [[synthetic-balance-sheet-liquidity-risk]], [[integrated-alm-liquidity-strategy]].

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
