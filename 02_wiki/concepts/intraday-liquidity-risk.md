---
title: "Intraday Liquidity Risk — Quản Trị Rủi Ro Thanh Khoản Trong Ngày (Basel SRP50 & BCBS 248)"
aliases: [Intraday Liquidity Risk, Thanh khoản trong ngày, Quản trị thanh khoản trong ngày, Intraday Monitoring Metrics, BCBS 248]
type: concept
domains: [basel, alm, vn-reg]
status: active
maturity: canonical
sources: ["[[src-bcbs-framework]]", "[[src-bcbs-lcr]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[bcbs]]", cite: "[[src-bcbs-framework#^srp50-1]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
  - {type: governs, to: "[[contractual-maturity-mismatch]]", cite: "[[src-bcbs-framework#^srp50-47]]"}
tags: [liquidity, intraday-liquidity, payment-systems, lvps, rtgs, settlement-risk, srp50, bcbs248, basel]
updated: 2026-10-20
reviewed:
---

## Tóm tắt Cấp cao (Executive Summary)

**Rủi ro thanh khoản trong ngày (Intraday Liquidity Risk)** là rủi ro phát sinh khi một ngân hàng không có đủ tiền mặt hoặc thanh khoản khả dụng trong từng thời điểm của ngày làm việc để thực hiện các nghĩa vụ thanh toán và quyết toán theo thời gian thực [[src-bcbs-framework#^srp50-47]].

Theo chuẩn mực **BCBS SRP50.47 – SRP50.92** (phát triển từ văn bản gốc BCBS 248), sự thất bại trong việc quản trị thanh khoản trong ngày không chỉ đe dọa sự tồn vong của chính ngân hàng mà còn **kích hoạt sự đứt gãy thanh khoản lan truyền có tính hệ thống (systemic contagion)** trên toàn bộ các hệ thống thanh toán giá trị lớn (**Large-Value Payment Systems - LVPS / RTGS**) và các thị trường tài chính quốc tế [[src-bcbs-framework#^srp50-47]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│               HỆ THỐNG CÔNG CỤ GIÁM SÁT THANH KHOẢN TRONG NGÀY (SRP50 / BCBS 248)               │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ NHÓM A: ÁP DỤNG CHO TOÀN BỘ CÁC NGÂN HÀNG (ALL REPORTING BANKS)                                 │
│ 1. Mức sử dụng thanh khoản đỉnh trong ngày (Daily maximum intraday liquidity usage)            │
│ 2. Thanh khoản khả dụng đầu ngày (Available intraday liquidity at start of day)                 │
│ 3. Tổng giá trị các giao dịch thanh toán (Total gross payments sent & received)                 │
│ 4. Nghĩa vụ tại mốc thời gian cụ thể (Time-specific obligations: CLS, margins, tax...)         │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ NHÓM B: ÁP DỤNG CHO NGÂN HÀNG ĐẠI LÝ (CORRESPONDENT BANKS)                                      │
│ 5. Giá trị thanh toán thực hiện hộ khách hàng đại lý (Payments on behalf of customers)          │
│ 6. Hạn mức tín dụng trong ngày đã cấp (Intraday credit lines extended)                          │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ NHÓM C: ÁP DỤNG CHO THÀNH VIÊN TRỰC TIẾP HỆ THỐNG LVPS (DIRECT PARTICIPANTS)                    │
│ 7. Tỷ lệ thông lượng thanh toán trong ngày (Intraday throughput: % lệnh gửi đi theo giờ)       │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ BỐN KỊCH BẢN CĂNG THẲNG THANH KHOẢN TRONG NGÀY (STRESS SCENARIOS):                             │
│ [ Stress Tài chính Nội tại ] ── [ Stress Đối tác ] ── [ Stress Ngân hàng Đại lý ] ── [ Stress Thị trường ] │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Nguồn Cung và Nhu Cầu Thanh Khoản Trong Ngày (SRP50.49)

Một ngân hàng quản trị thanh khoản trong ngày thông qua sự cân bằng động giữa hai dòng chảy:

### A. Nguồn Cung Thanh Khoản Trong Ngày (Intraday Liquidity Sources)
1. **Số dư đầu ngày**: Tiền gửi thanh toán tại tài khoản quyết toán ở NHTW hoặc ngân hàng đại lý.
2. **Hạn mức thấu chi / Tín dụng trong ngày của NHTW (Intraday Credit)**: Các khoản vay thấu chi trong ngày được cấp bởi NHTW (thường yêu cầu có tài sản bảo đảm unencumbered).
3. **Dòng tiền thanh toán nhận được (Incoming Payments)**: Tiền chuyển đến từ các ngân hàng khác qua hệ thống RTGS.
4. **Hạn mức tín dụng từ ngân hàng đại lý (Credit lines from correspondent banks)**.
5. **Tài sản sạch có thể huy động vốn ngay trong ngày**: Chứng khoán khả nhượng có thể bán hoặc Repo trong ngày để tạo số dư tiền mặt.

### B. Nhu Cầu Sử Dụng Thanh Khoản Trong Ngày (Intraday Liquidity Usage)
1. **Dòng tiền thanh toán chuyển đi (Outgoing Payments)**: Lệnh chuyển tiền của chính ngân hàng và khách hàng.
2. **Nghĩa vụ tại mốc thời gian cố định (Time-Specific Obligations)**: Lệnh thanh toán bắt buộc phải hoàn thành trước một giờ cụ thể (ví dụ: thanh toán giao dịch ngoại hối CLS trước 08:00 CET, nộp tiền ký quỹ phái sinh CCP trước 11:00, hoàn trả nợ vay liên ngân hàng qua đêm trước 14:00) [[src-bcbs-framework#^srp50-73]].
3. **Hạn mức tín dụng cấp cho các ngân hàng khách hàng**: Việc tài trợ thanh khoản tức thời cho các tổ chức khác khi họ chưa kịp chuyển tiền vào.

---

## 2. Bảy Công Cụ Giám Sát Chi Tiết của Basel SRP50

### 2.1. Nhóm Công cụ Nền tảng (Áp dụng cho mọi ngân hàng)
* **Công cụ 1 — Mức sử dụng đỉnh trong ngày (Daily maximum intraday liquidity usage)**: Đo lường chênh lệch âm ròng lũy kế lớn nhất (*largest negative net cumulative position*) giữa các khoản tiền gửi đi và nhận về trên tài khoản thanh toán tại bất kỳ thời điểm nào trong ngày [[src-bcbs-framework#^srp50-64]]. Báo cáo trung bình và 3 ngày có mức thâm hụt đỉnh cao nhất.
* **Công cụ 2 — Thanh khoản khả dụng đầu ngày (Available intraday liquidity at start of day)**: Đo lường tổng nguồn lực tiền mặt và tài sản thế chấp sạch sẵn sàng ngay đầu giờ làm việc [[src-bcbs-framework#^srp50-69]].
* **Công cụ 3 — Tổng giá trị thanh toán (Total payments)**: Theo dõi quy mô dòng tiền gộp chuyển đi và nhận về hàng ngày để đánh giá mức độ phơi nhiễm thanh toán [[src-bcbs-framework#^srp50-72]].
* **Công cụ 4 — Nghĩa vụ tại mốc thời gian xác định (Time-specific obligations)**: Đo lường tổng giá trị các cam kết bắt buộc phải trả đúng hạn để tránh bị phạt pháp lý, phạt tài chính hoặc tổn hại nghiêm trọng uy tín thị trường [[src-bcbs-framework#^srp50-73]].

### 2.2. Nhóm Công cụ dành cho Ngân hàng Đại lý (Correspondent Banking)
* **Công cụ 5 — Thanh toán hộ khách hàng (Value of payments on behalf of customers)**: Giám sát quy mô và tỷ trọng giao dịch thực hiện thay cho các ngân hàng con/đối tác.
* **Công cụ 6 — Hạn mức tín dụng trong ngày đã cấp (Intraday credit lines extended)**: Đo lường lượng hạn mức thấu chi cam kết và chưa cam kết đã cấp cho khách hàng đại lý.

### 2.3. Nhóm Công cụ Thành viên Trực tiếp (Direct Participants)
* **Công cụ 7 — Thông lượng thanh toán trong ngày (Intraday Throughput)**: 
  - Yêu cầu các thành viên trực tiếp của hệ thống LVPS phải giải phóng lệnh chuyển tiền đi theo tỷ lệ phần trăm phân bổ đều trong ngày thay vì dồn toàn bộ vào cuối ngày làm tắc nghẽn hệ thống [[src-bcbs-framework#^srp50-80]].
  - *Ví dụ chuẩn mực thực hành*: Tối thiểu $35\%$ giá trị thanh toán phải được hoàn tất trước 12:00 trưa, và tối thiểu $70\%$ phải được hoàn tất trước 15:00 chiều.

---

## 3. Bốn Kịch Bản Căng Thẳng Thanh Khoản Trong Ngày (SRP50.82)

Theo quy định tại **SRP50.82**, ngân hàng phải mô hình hóa tác động lên các công cụ thanh khoản trong ngày dưới 4 kịch bản căng thẳng [[src-bcbs-framework#^srp50-82]]:
1. **Căng thẳng tài chính nội tại của ngân hàng (Own Financial Stress)**: Ngân hàng bị hạ bậc xếp hạng tín nhiệm hoặc vướng tin đồn tiêu cực; các ngân hàng đại lý lập tức cắt đứt hạn mức thấu chi trong ngày và đòi hỏi tiền nộp trước $100\%$ trước khi xử lý lệnh.
2. **Căng thẳng đối tác thanh toán (Counterparty Stress)**: Một đối tác thanh toán lớn gặp trục trặc kỹ thuật hoặc mất khả năng thanh toán, khiến dòng tiền chuyển đến (incoming payments) dự kiến bị tắc nghẽn hoàn toàn.
3. **Căng thẳng ngân hàng khách hàng đại lý (Customer Bank Stress)**: Ngân hàng khách hàng đại lý rút tiền ồ ạt, sử dụng cạn kiệt hạn mức tín dụng trong ngày mà không có dòng tiền hoàn trả.
4. **Căng thẳng toàn thị trường (Market-wide Stress)**: Hệ thống thanh toán giá trị lớn LVPS hoặc hạ tầng lưu ký chứng khoán bị tê liệt kỹ thuật, giá trị tài sản bảo đảm bị định giá lại giảm sâu.

---

## 4. Ma trận Liên kết Hệ thống ALM Wiki

* **Chuẩn mực Nguồn**: [[src-bcbs-framework]] (Chương SRP50, claims ^srp50-47 đến ^srp50-82).
* **Các Chỉ số & Khái niệm**: [[lcr]], [[hqla]], [[available-unencumbered-assets]], [[contractual-maturity-mismatch]], [[funding-concentration-risk]].
* **Hạ tầng & Vận hành**: [[integrated-alm-liquidity-strategy]], [[synthetic-balance-sheet-liquidity-risk]].

* **Góc nhìn VN**: theo [[tt83-2025]], quản lý thanh khoản trong ngày là cấu phần bắt buộc của quản lý thanh khoản (theo dõi trạng thái, xác định nguồn vốn, dự báo thay đổi bất thường) [[src-tt83-2025-nhnn#^d46-2]]; ngân hàng phải có công cụ đo cho hoạt động ngân hàng đại lý, lưu ký, thanh toán [[src-tt83-2025-nhnn#^d47-2]]. *Diễn giải:* TT83 không có bộ 7 công cụ giám sát của SRP50.

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M5 — chờ user duyệt: thêm góc nhìn VN: quản lý thanh khoản trong ngày là cấu phần bắt buộc (theo dõi trạng thái, xác định nguồn vốn, dự báo thay đổi bất thường) [[src-tt83-2025-nhnn#^d46-2]]; phải có công cụ đo cho hoạt động ngân hàng đại lý, lưu ký, thanh toán [[src-tt83-2025-nhnn#^d47-2]]. → đã áp dụng [2026-10-20]
