---
title: "Funding Concentration Risk — Rủi Ro Tập Trung Nguồn Vốn (Basel SRP50)"
aliases: [Funding Concentration Risk, Concentration of Funding, Rủi ro tập trung nguồn vốn, Tập trung người gửi tiền, Wholesale Funding Concentration]
type: concept
domains: [basel, alm, vn-reg]
status: active
maturity: draft
sources: ["[[src-bcbs-framework]]", "[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-tata-bank-alm]]", "[[src-tt83-2025-nhnn]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[bcbs]]", cite: "[[src-bcbs-framework#^srp50-1]]"}
  - {type: input-to, to: "[[unsecured-wholesale-funding]]", cite: "[[src-bcbs-framework#^srp50-14]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
  - {type: input-to, to: "[[liquidity-stress-testing]]", cite: "[[src-tt83-2025-nhnn#^d48-3]]"}
tags: [liquidity, funding-concentration, counterparty-concentration, instrument-concentration, wholesale-funding, srp50, basel]
updated: 2026-10-20
reviewed:
---

## Tóm tắt Cấp cao (Executive Summary)

**Rủi ro tập trung nguồn vốn (Funding Concentration Risk)** là công cụ giám sát trọng yếu thuộc **BCBS SRP50**, được thiết kế nhằm nhận diện các nguồn vốn bán buôn có quy mô lớn đến mức hành vi rút vốn đột ngột từ một đối tác, một loại sản phẩm hoặc một đồng tiền có thể lập tức kích hoạt cuộc khủng hoảng thanh khoản nghiêm trọng [[src-bcbs-framework#^srp50-14]].

Một bài học kinh điển từ cuộc khủng hoảng tài chính toàn cầu 2008 và sự sụp đổ của các ngân hàng như Northern Rock, [[silicon-valley-bank|Silicon Valley Bank]] (SVB; hơn 88% tiền gửi không được bảo hiểm cuối 2021 [[src-tata-bank-alm#^tata-svb-4]], khoảng 45% là tiền gửi tạm của start-up và VC [[src-tata-bank-alm#^tata-svb-7]]) hay Credit Suisse là: **sự phụ thuộc quá mức vào một nhóm người gửi tiền bán buôn hoặc một sản phẩm huy động tập trung sẽ biến rủi ro thanh khoản thành sự kiện sụp đổ chớp nhoáng**. Chuẩn mực SRP50 thiết lập hệ thống ngưỡng định lượng và dải thời gian theo dõi bắt buộc để thúc đẩy đa dạng hóa cơ cấu nguồn vốn [[src-bcbs-framework#^srp50-14]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│               BA LĂNG KÍNH ĐỊNH LƯỢNG RỦI RO TẬP TRUNG NGUỒN VỐN (SRP50)                         │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ LĂNG KÍNH 1: TẬP TRUNG THEO ĐỐI TÁC (COUNTERPARTY CONCENTRATION)                                │
│ • Ngưỡng: Đối tác đơn lẻ hoặc nhóm liên quan chiếm > 1% Tổng Bảng Cân Đối                       │
│ • Công thức: Nợ từ Đối tác_k / Tổng Nợ Phải Trả                                                 │
│ • Kiểm soát: Giới hạn trần hạn mức cho Top 10 / Top 20 người gửi tiền lớn nhất                  │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ LĂNG KÍNH 2: TẬP TRUNG THEO SẢN PHẨM / CÔNG CỤ (INSTRUMENT / PRODUCT CONCENTRATION)             │
│ • Ngưỡng: Một sản phẩm đơn lẻ hoặc nhóm tương tự chiếm > 1% Tổng Bảng Cân Đối                   │
│ • Phân loại: Chứng chỉ tiền gửi (CDs), Thương phiếu (CP), Repo, Trái phiếu cấp 2, Vay LNH       │
│ • Kiểm soát: Tránh phụ thuộc vào các công cụ có tính thanh khoản thứ cấp mỏng                   │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ LĂNG KÍNH 3: TẬP TRUNG THEO NGOẠI TỆ (CURRENCY CONCENTRATION)                                    │
│ • Ngưỡng: Tổng nợ bằng một loại ngoại tệ chiếm ≥ 5% Tổng Nợ Phải Trả                            │
│ • Kiểm soát: Theo dõi cân đối tài sản - nợ ngoại tệ và tỷ lệ [[lcr-by-currency]]               │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ NĂM DẢI THỜI GIAN THEO DÕI BẮT BUỘC:                                                            │
│ [ < 1 tháng ] ─── [ 1 - 3 tháng ] ─── [ 3 - 6 tháng ] ─── [ 6 - 12 tháng ] ─── [ > 12 tháng ]    │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Ba Ngưỡng Định Lượng Chuẩn Mực của Basel SRP50

Theo **SRP50.14 – SRP50.21**, bộ công cụ giám sát đo tập trung nguồn vốn qua 3 chỉ số: theo đối tác, theo sản phẩm (đều chia tổng nợ phải trả) và danh mục tài sản, nợ theo đồng tiền trọng yếu [[src-bcbs-framework#^srp50-15]]:

### 1.1. Tập Trung Theo Đối Tác Trọng Yếu (Significant Counterparty)
* **Định nghĩa**: Một đối tác đơn lẻ hoặc một nhóm các đối tác có liên quan/liên kết sở hữu tổng số dư tiền gửi và nợ vay chiếm **vượt quá 1% tổng tài sản/bảng cân đối kế toán của ngân hàng** [[src-bcbs-framework#^srp50-17]].
* **Quy tắc xác định nhóm liên quan**: Khái niệm nhóm đối tác liên quan được đồng nhất với quy định về Giới hạn Cấp tín dụng Lớn (*Large Exposure regulation - LEX*) của nước sở tại [[src-bcbs-framework#^srp50-17b]].
* **Xử lý giao dịch nội bộ tập đoàn (Intra-group Deposits)**: Tiền gửi từ các công ty con, chi nhánh hoặc các bên liên quan nên được nhận diện riêng, dù chỉ số tính ở cấp pháp nhân hay tập đoàn, vì giao dịch nội bộ có thể bị hạn chế khi stress [[src-bcbs-framework#^srp50-17b]]. Xem [[liquidity-transfer-restrictions]].
* **Công thức**: nợ huy động từ từng đối tác trọng yếu chia tổng nợ phải trả; ngân hàng và cơ quan giám sát nên theo dõi cả tỷ lệ tuyệt đối lẫn mức tăng đáng kể [[src-bcbs-framework#^srp50-15]]. Ngưỡng nhận diện (1%) tính trên tổng bảng cân đối, còn mẫu số của chỉ số là tổng nợ phải trả.

### 1.2. Tập Trung Theo Loại Sản Phẩm / Công Cụ (Significant Instrument/Product)
* **Định nghĩa**: Một sản phẩm hoặc nhóm sản phẩm tài trợ tương tự có tổng quy mô **chiếm trên 1% tổng bảng cân đối kế toán** [[src-bcbs-framework#^srp50-19]].
* **Ý nghĩa ALM**: Nhận diện rủi ro khi thị trường của một sản phẩm huy động vốn cụ thể bị đóng băng (ví dụ: thị trường thương phiếu tài trợ bằng tài sản ABCP bị tắc nghẽn trong năm 2007–2008, hoặc thị trường repo trái phiếu doanh nghiệp bị từ chối).

### 1.3. Cấu Trúc Bất Cân Xứng Tiền Tệ (Significant Currency)
* **Định nghĩa**: Một đồng tiền được xác định là trọng yếu khi tổng nợ phải trả bằng đồng tiền đó **chiếm từ 5% trở lên trong tổng nợ của ngân hàng** [[src-bcbs-framework#^srp50-21]].
* Ngân hàng phải lập danh mục chi tiết tài sản và nợ phải trả theo từng đồng tiền trọng yếu để phát hiện nguy cơ mất cân đối cơ cấu ngoại tệ [[src-bcbs-framework#^srp50-21]].

---

## 2. Năm Dải Thời Gian Báo Cáo Bắt Buộc (Time Horizons)

Theo quy định tại **SRP50.22**, để nhận diện rủi ro đáo hạn tập trung (*cliff-edge risk / refinancing roll-off*), toàn bộ các chỉ số tập trung đối tác, sản phẩm và tiền tệ bắt buộc phải được phân rã thành **5 dải kỳ hạn còn lại** [[src-bcbs-framework#^srp50-22]]:
1. Dưới 1 tháng ($< 1$ month)
2. Từ 1 đến 3 tháng (1–3 months)
3. Từ 3 đến 6 tháng (3–6 months)
4. Từ 6 đến 12 tháng (6–12 months)
5. Trên 12 tháng ($> 12$ months)

> *Ý nghĩa [[alco|ALCO]]*: Nếu một ngân hàng có 10% tổng nguồn vốn huy động từ 3 tập đoàn lớn và toàn bộ 10% này cùng đáo hạn trong dải kỳ hạn $< 1$ tháng, ngân hàng đang đối mặt với rủi ro đứt gãy thanh khoản nghiêm trọng ngay cả khi tỷ lệ [[nsfr]] tổng thể đang đạt trên 100%.

---

## 3. Tương Tác Giữa Funding Concentration với LCR và NSFR

Rủi ro tập trung nguồn vốn là chiếc kính hiển vi bổ trợ cho hai chỉ số chuẩn mực:
* **Tương tác với [[lcr]]**: trong vốn bán buôn không bảo đảm ([[unsecured-wholesale-funding]]), run-off là 100% với ngân hàng và định chế tài chính [[src-bcbs-lcr#^lcr40-42]], 40% với DN phi tài chính, chính phủ, NHTW, MDB, PSE [[src-bcbs-lcr#^lcr40-40]]. *Diễn giải:* nếu vốn từ DN phi tài chính tập trung ở vài đối tác, khi xảy ra căng thẳng [[reputational-risk|danh tiếng]] tỷ lệ rút thực tế có thể vượt 40% giả định, vượt sức chịu đựng của đệm [[hqla]].
* **Tương tác với [[nsfr]]**: nợ có kỳ hạn dưới 6 tháng từ ngân hàng và định chế tài chính nhận [[asf-wholesale-and-operational-funding|ASF 0%]] [[src-bcbs-nsfr#^nsf30-14]]; vốn từ DN phi tài chính dưới 1 năm nhận ASF 50% [[src-bcbs-nsfr#^nsf30-13]]. *Diễn giải:* tập trung vào công cụ thị trường tiền tệ ngắn hạn làm giảm ASF và kéo NSFR xuống.
* **Cơ chế Điều hành ALCO**:
  - *Diễn giải (ví dụ minh hoạ, không có nguồn):* trần tập trung kiểu tỷ trọng nợ từ 1 đối tác $\le 1.5–2\%$, Top 10 đối tác $\le 10–15\%$ tổng nguồn vốn. SRP50 không đặt hạn mức, chỉ đặt ngưỡng nhận diện 1% [[src-bcbs-framework#^srp50-17]]; TT83 không đặt hạn mức tập trung nguồn vốn trong các unit đã ingest [cần nguồn].
  - Áp dụng phụ phí thanh khoản FTP (FTP Concentration Surcharge) đối với các đơn vị kinh doanh huy động các món tiền gửi bán buôn quá lớn vượt ngưỡng [[risk-appetite|khẩu vị rủi ro]].

* **Ví dụ hạn mức (Choudhry, T4)**: không bucket kỳ hạn nào vượt 20% tổng nhu cầu vốn (case công ty chứng khoán Anh trước 2008) [[src-choudhry-principles-banking#^choudhry-cs-8]]; rủi ro tập trung theo ngành (định chế tài chính) là một tiêu chí trong chiến lược tiền gửi [[src-choudhry-principles-banking#^choudhry-cs-20]].

---

## 4. Ma trận Liên kết Hệ thống ALM Wiki

* **Chuẩn mực Nguồn**: [[src-bcbs-framework]] (Chương SRP50, claims ^srp50-14 đến ^srp50-22, cùng ^srp50-15, ^srp50-17b); Pillar 2 SRP30.22; [[src-bcbs-liquidity-principles-2008]] P7; [[tt83-2025]] Đ45.2, Đ48.3, Đ50.1.
* **Các Chỉ số & Khái niệm**: [[unsecured-wholesale-funding]], [[lcr]], [[nsfr]], [[retail-deposit-stability]], [[contractual-maturity-mismatch]], [[lcr-by-currency]].
* **Chiến lược & Bảng Cân đối**: [[synthetic-balance-sheet-liquidity-risk]], [[integrated-alm-liquidity-strategy]].

## Nguyên tắc nền: [[bcbs-liquidity-principles|BCBS 144]] Principle 7
- Ngân hàng nên có chiến lược funding đa dạng hoá hiệu quả nguồn và kỳ hạn vốn, và thường xuyên đánh giá năng lực huy động nhanh từ từng nguồn [[src-bcbs-liquidity-principles-2008#^lrm-p07]].
- Mục tiêu đa dạng hoá nằm trong kế hoạch funding trung và dài hạn, gắn với ngân sách; gồm hạn mức theo đối tác, có/không bảo đảm, loại công cụ, phương tiện chứng khoán hoá, đồng tiền và thị trường địa lý [[src-bcbs-liquidity-principles-2008#^lrm-65]].
- Ngân hàng nên hạn chế tập trung vào một nguồn hoặc một kỳ hạn; ngân hàng dựa vào vốn bán buôn nên giữ tỷ trọng tài sản thanh khoản cao không bị cầm cố lớn hơn ngân hàng chủ yếu dựa vào vốn bán lẻ [[src-bcbs-liquidity-principles-2008#^lrm-66]].
- Nguồn vốn thay thế (bán hoặc repo tài sản thanh khoản cao, rút hạn mức cam kết, vay NHTW…) không phải lúc nào cũng sẵn có, một số chỉ có với độ trễ đáng kể [[src-bcbs-liquidity-principles-2008#^lrm-74]].

*Diễn giải:* BCBS 144 chỉ nêu nguyên tắc đa dạng hoá, không đặt ngưỡng định lượng. Ngưỡng 1% theo đối tác và sản phẩm ở mục 1 là bộ công cụ giám sát SRP50 về sau.

## 5. Góc nhìn VN và Basel Pillar 2

* **VN ([[tt83-2025]])**:
  - Mức độ tập trung huy động vốn và việc mất khả năng thu hút vốn từ khách gửi tiền quan trọng là yếu tố bắt buộc trong kiểm tra sức chịu đựng về thanh khoản [[src-tt83-2025-nhnn#^d48-3]]. Xem [[liquidity-stress-testing]].
  - Chiến lược quản lý rủi ro thanh khoản phải có đa dạng hoá nguồn vốn [[src-tt83-2025-nhnn#^d45-2]].
  - Chiến lược rủi ro tập trung theo Đ50 áp cho cấp tín dụng và tự doanh, không nêu nguồn vốn [[src-tt83-2025-nhnn#^d50-1]]. Xem [[concentration-risk-management]].
* **Basel Pillar 2 (SRP30)**: SRP30.22 liệt kê nguồn vốn là một trong chín tình huống tập trung rủi ro [[src-bcbs-framework#^srp30-22]].
* *Diễn giải:* VN và SRP50 khác phạm vi, không phải conflict. Ở VN, tập trung nguồn vốn được kiểm soát gián tiếp qua stress test thanh khoản, không có hạn mức bắt buộc theo Đ50.

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
