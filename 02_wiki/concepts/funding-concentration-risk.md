---
title: "Funding Concentration Risk — Rủi Ro Tập Trung Nguồn Vốn (Basel SRP50)"
aliases: [Funding Concentration Risk, Concentration of Funding, Rủi ro tập trung nguồn vốn, Tập trung người gửi tiền, Wholesale Funding Concentration]
type: concept
domains: [basel, alm]
status: active
maturity: canonical
sources: ["[[src-bcbs-framework]]", "[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[bcbs]]", cite: "[[src-bcbs-framework#^srp50-1]]"}
  - {type: input-to, to: "[[unsecured-wholesale-funding]]", cite: "[[src-bcbs-framework#^srp50-14]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
tags: [liquidity, funding-concentration, counterparty-concentration, instrument-concentration, wholesale-funding, srp50, basel]
updated: 2026-10-16
reviewed:
---

## Tóm tắt Cấp cao (Executive Summary)

**Rủi ro tập trung nguồn vốn (Funding Concentration Risk)** là công cụ giám sát trọng yếu thuộc **BCBS SRP50**, được thiết kế nhằm nhận diện các nguồn vốn bán buôn có quy mô lớn đến mức hành vi rút vốn đột ngột từ một đối tác, một loại sản phẩm hoặc một đồng tiền có thể lập tức kích hoạt cuộc khủng hoảng thanh khoản nghiêm trọng [[src-bcbs-framework#^srp50-14]].

Một bài học kinh điển từ cuộc khủng hoảng tài chính toàn cầu 2008 và sự sụp đổ của các ngân hàng như Northern Rock, Silicon Valley Bank (SVB) hay Credit Suisse là: **sự phụ thuộc quá mức vào một nhóm người gửi tiền bán buôn hoặc một sản phẩm huy động tập trung sẽ biến rủi ro thanh khoản thành sự kiện sụp đổ chớp nhoáng**. Chuẩn mực SRP50 thiết lập hệ thống ngưỡng định lượng và dải thời gian theo dõi bắt buộc để thúc đẩy đa dạng hóa cơ cấu nguồn vốn [[src-bcbs-framework#^srp50-14]].

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

Theo quy định tại **SRP50.14 – SRP50.21**, cơ quan giám sát yêu cầu ngân hàng định lượng sự tập trung nguồn vốn qua 3 chỉ số cốt lõi:

### 1.1. Tập Trung Theo Đối Tác Trọng Yếu (Significant Counterparty)
* **Định nghĩa**: Một đối tác đơn lẻ hoặc một nhóm các đối tác có liên quan/liên kết sở hữu tổng số dư tiền gửi và nợ vay chiếm **vượt quá 1% tổng tài sản/bảng cân đối kế toán của ngân hàng** [[src-bcbs-framework#^srp50-17]].
* **Quy tắc xác định nhóm liên quan**: Khái niệm nhóm đối tác liên quan được đồng nhất với quy định về Giới hạn Cấp tín dụng Lớn (*Large Exposure regulation - LEX*) [[src-bcbs-framework#^srp50-17]].
* **Xử lý giao dịch nội bộ tập đoàn (Intra-group Deposits)**: Tiền gửi từ các công ty con, chi nhánh hoặc các bên liên quan bắt buộc phải được bóc tách định danh riêng biệt do rào cản pháp lý bảo hộ cục bộ (*ring-fencing*) có thể ngăn chặn việc chuyển giao thanh khoản khi xảy ra khủng hoảng [[src-bcbs-framework#^srp50-17]].

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

> *Ý nghĩa ALCO*: Nếu một ngân hàng có 10% tổng nguồn vốn huy động từ 3 tập đoàn lớn và toàn bộ 10% này cùng đáo hạn trong dải kỳ hạn $< 1$ tháng, ngân hàng đang đối mặt với rủi ro đứt gãy thanh khoản nghiêm trọng ngay cả khi tỷ lệ [[nsfr]] tổng thể đang đạt trên 100%.

---

## 3. Tương Tác Giữa Funding Concentration với LCR và NSFR

Rủi ro tập trung nguồn vốn là chiếc kính hiển vi bổ trợ cho hai chỉ số chuẩn mực:
* **Tương tác với [[lcr]]**: Nguồn vốn bán buôn không bảo đảm ([[unsecured-wholesale-funding]]) chịu tỷ lệ rút vốn giả định $100\%$ trong LCR. Nếu nguồn vốn này tập trung cao ở một vài đối tác, khi xảy ra căng thẳng danh tiếng, tỷ lệ rút tiền thực tế sẽ là $100\%$ ngay lập tức, vượt xa sức chịu đựng của đệm [[hqla]].
* **Tương tác với [[nsfr]]**: Các khoản tài trợ bán buôn ngắn hạn dưới 6 tháng nhận hệ số [[asf-wholesale-and-operational-funding|ASF = 0%]]. Việc phân bổ tập trung vào các công cụ thị trường tiền tệ ngắn hạn khiến tử số ASF suy giảm mạnh, kéo sụt NSFR.
* **Cơ chế Điều hành ALCO**:
  - Thiết lập trần tập trung: Giới hạn tối đa tỷ trọng nợ từ 1 đối tác đơn lẻ $\le 1.5–2\%$, Top 10 đối tác $\le 10–15\%$ tổng nguồn vốn.
  - Áp dụng phụ phí thanh khoản FTP (FTP Concentration Surcharge) đối với các đơn vị kinh doanh huy động các món tiền gửi bán buôn quá lớn vượt ngưỡng khẩu vị rủi ro.

---

## 4. Ma trận Liên kết Hệ thống ALM Wiki

* **Chuẩn mực Nguồn**: [[src-bcbs-framework]] (Chương SRP50, claims ^srp50-14 đến ^srp50-22).
* **Các Chỉ số & Khái niệm**: [[unsecured-wholesale-funding]], [[lcr]], [[nsfr]], [[retail-deposit-stability]], [[contractual-maturity-mismatch]], [[lcr-by-currency]].
* **Chiến lược & Bảng Cân đối**: [[synthetic-balance-sheet-liquidity-risk]], [[integrated-alm-liquidity-strategy]].

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M5 — chờ user duyệt: thêm góc nhìn VN: mức độ tập trung huy động vốn và mất khả năng thu hút vốn từ khách gửi tiền quan trọng là yếu tố bắt buộc trong kiểm tra sức chịu đựng về thanh khoản [[src-tt83-2025-nhnn#^d48-3]]; chiến lược phải có đa dạng hoá nguồn vốn [[src-tt83-2025-nhnn#^d45-2]]; có thể thêm relation `input-to` → [[liquidity-stress-testing]] (cite d48-3).
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1 — chờ user duyệt: đã có node [[risk-appetite]]; đề xuất link ở lần nhắc đầu risk appetite.
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M6 — chờ user duyệt: thêm góc nhìn VN: TT83 Đ50 áp chiến lược rủi ro tập trung cho cấp tín dụng và tự doanh, không nêu nguồn vốn [[src-tt83-2025-nhnn#^d50-1]]; tập trung huy động vốn chỉ là yếu tố phải phân tích trong kịch bản stress thanh khoản [[src-tt83-2025-nhnn#^d48-3]]. Khác phạm vi so với SRP50, không phải conflict. Link [[concentration-risk-management]].
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: đã có node [[silicon-valley-bank]] (nguồn Tata u07); đề xuất link ở chỗ nhắc SVB và đối chiếu số liệu đang viết với [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]].
- [2026-10-19] ingest src-choudhry-principles-banking u25 — chờ user duyệt: thêm ví dụ hạn mức: không bucket kỳ hạn nào quá 20% tổng nhu cầu vốn (case công ty chứng khoán Anh, trước 2008) [[src-choudhry-principles-banking#^choudhry-cs-8]]; rủi ro tập trung theo ngành (định chế tài chính) là một tiêu chí trong chiến lược tiền gửi [[src-choudhry-principles-banking#^choudhry-cs-20]].
