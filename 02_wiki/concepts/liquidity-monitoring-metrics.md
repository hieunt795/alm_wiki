---
title: "Liquidity Monitoring Metrics — Khuôn Khổ Bộ Chỉ Số Giám Sát Thanh Khoản (Basel SRP50)"
aliases: [Liquidity Monitoring Metrics, Basel SRP50, Bộ chỉ số giám sát thanh khoản Basel, Monitoring Tools for Liquidity Risk, SRP50]
type: concept
domains: [basel, alm]
status: active
maturity: draft
sources: ["[[src-bcbs-framework]]", "[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[bcbs]]", cite: "[[src-bcbs-framework#^srp50-1]]"}
  - {type: governs, to: "[[contractual-maturity-mismatch]]", cite: "[[src-bcbs-framework#^srp50-6]]"}
  - {type: governs, to: "[[funding-concentration-risk]]", cite: "[[src-bcbs-framework#^srp50-14]]"}
  - {type: governs, to: "[[available-unencumbered-assets]]", cite: "[[src-bcbs-framework#^srp50-27]]"}
  - {type: governs, to: "[[lcr-by-currency]]", cite: "[[src-bcbs-framework#^srp50-35]]"}
  - {type: governs, to: "[[intraday-liquidity-risk]]", cite: "[[src-bcbs-framework#^srp50-47]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
tags: [liquidity, liquidity-monitoring-metrics, srp50, supervisory-review, maturity-mismatch, funding-concentration, unencumbered-assets, currency-lcr, intraday-liquidity, basel]
updated: 2026-10-20
reviewed:
---

## Tóm tắt Cấp cao (Executive Summary)

**Bộ Chỉ Số Giám Sát Rủi Ro Thanh Khoản (Liquidity Monitoring Metrics — BCBS SRP50)** là hợp phần giám sát chuyên sâu thuộc Trụ cột 2 của Khuôn khổ Basel, được thiết kế đồng bộ nhằm bổ trợ cho hai chuẩn mực định lượng bắt buộc là [[lcr]] và [[nsfr]] [[src-bcbs-framework#^srp50-1]]. 

Nếu như LCR và NSFR đóng vai trò là hai "chiếc neo" định lượng bắt buộc (ngưỡng tối thiểu $\ge 100\%$) [[src-bcbs-framework#^srp50-1]], thì SRP50 cung cấp **bức tranh toàn cảnh đa chiều về dòng tiền, cấu trúc bảng cân đối, đệm tài sản bảo đảm và các tín hiệu thị trường** mà hai chỉ số LCR/NSFR không thể phản ánh hết [[src-bcbs-framework#^srp50-1]] [[src-bcbs-framework#^srp50-2]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                 KIẾN TRÚC BỘ CÔNG CỤ GIÁM SÁT THANH KHOẢN BASEL SRP50                           │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                  HỘI ĐỒNG ALCO & CƠ QUAN GIÁM SÁT                               │
│                         Mục tiêu: Nhận diện sớm khó khăn thanh khoản nội tại                    │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                 NĂM CÔNG CỤ GIÁM SÁT THANH KHOẢN CỐT LÕI                        │
├────────────────────────────────────────────────┬────────────────────────────────────────────────┤
│ 1. [[contractual-maturity-mismatch]]           │ 2. [[funding-concentration-risk]]              │
│ • Thang kỳ hạn hợp đồng 13 dải thời gian       │ • Tập trung theo đối tác (> 1% tổng TS)        │
│ • Bóc tách Liquidity Gap thuần túy pháp lý     │ • Tập trung theo sản phẩm/công cụ (> 1%)       │
│ • Không giả định rollover nợ và tài sản mới    │ • Phân rã theo 5 dải kỳ hạn đến hạn            │
├────────────────────────────────────────────────┼────────────────────────────────────────────────┤
│ 3. [[available-unencumbered-assets]]           │ 4. [[lcr-by-currency]]                         │
│ • Định lượng kho tài sản sạch không cầm cố     │ • Tính LCR riêng cho ngoại tệ chiếm ≥ 5% nợ    │
│ • Báo cáo 2 tầng haircut: Thị trường & NHTW    │ • Ngăn ngừa rủi ro cạn kiệt thị trường FX Swap │
│ • Tuyến phòng thủ thứ cấp sau đệm HQLA         │ • Kiểm soát lệch pha tiền tệ cơ cấu            │
├────────────────────────────────────────────────┴────────────────────────────────────────────────┤
│ 5. CÔNG CỤ CẢNH BÁO SỚM THỊ TRƯỜNG (MARKET-RELATED MONITORING TOOLS)                            │
│ • Dữ liệu tần suất cao: Giá cổ phiếu ngân hàng, chênh lệch CDS, lợi suất TP, lãi suất LNH      │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ HỢP PHẦN BỔ SUNG: [[intraday-liquidity-risk]] (BCBS 248)                                        │
│ • Giám sát thâm hụt đỉnh trong ngày, thanh khoản khả dụng đầu ngày và tỷ lệ thông lượng (LVPS) │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Bản Chất Pháp Lý và Nguyên Tắc Vận Hành (SRP50.1 – SRP50.4)

1. **Tính chất bổ trợ bắt buộc**: SRP50 không thay thế LCR hay NSFR mà cùng với hai chuẩn mực này cấu thành nền tảng thông tin đầy đủ nhất để giám sát rủi ro thanh khoản [[src-bcbs-framework#^srp50-2]].
2. **Không có ngưỡng sàn cứng (No Regulatory Minimum Ratio)**: Khác với LCR $\ge 100\%$ hay NSFR $\ge 100\%$, các chỉ số SRP50 là **công cụ giám sát định tính và định lượng (*monitoring tools*)** [[src-bcbs-framework#^srp50-4]]. Cơ quan giám sát sẽ can thiệp khi nhận thấy xu hướng suy giảm tiêu cực hoặc sự xuất hiện của các điểm thâm hụt dị biệt.
3. **Không công bố thông tin đại chúng (No Public Disclosure)**: Dữ liệu SRP50 chỉ phục vụ công tác thanh tra giám sát và quản trị nội bộ giữa ngân hàng và cơ quan thanh tra; không bắt buộc phải công bố rộng rãi ra công chúng để tránh gây ra tâm lý hoảng loạn rút tiền (*bank run*) không cần thiết [[src-bcbs-framework#^srp50-3]].
4. **Phạm vi áp dụng**: Bắt buộc áp dụng trên cơ sở hợp nhất cho toàn bộ các ngân hàng hoạt động quốc tế [[src-bcbs-framework#^srp50-4]].

---

## 2. Tổng Hợp Năm Trụ Cột Giám Sát Cốt Lõi

| Cấu phần SRP50 | Định nghĩa & Thước đo chính | Câu hỏi Quản trị ALM Trả lời |
|---|---|---|
| **1. [[contractual-maturity-mismatch]]** | Thang 13 dải kỳ hạn đo lường chênh lệch dòng tiền vào/ra theo hợp đồng, không rollover [[src-bcbs-framework#^srp50-6]] | Nếu không thể huy động thêm nợ mới và khách hàng rút sạch khi đáo hạn, ngân hàng thiếu hụt bao nhiêu tiền? |
| **2. [[funding-concentration-risk]]** | Tỷ trọng nợ từ đối tác lớn ($>1\%$), sản phẩm lớn ($>1\%$) và ngoại tệ lớn ($\ge 5\%$) [[src-bcbs-framework#^srp50-17]] [[src-bcbs-framework#^srp50-19]] | Ngân hàng có đang phụ thuộc quá mức vào một vài "ông lớn" gửi tiền hoặc một sản phẩm ngắn hạn nhạy cảm không? |
| **3. [[available-unencumbered-assets]]** | Báo cáo quy mô, vị trí lưu ký và 2 tầng haircut (NHTW và thị trường thứ cấp) của tài sản sạch [[src-bcbs-framework#^srp50-27]] | Nếu bị thị trường tín chấp từ chối, ngân hàng còn bao nhiêu tài sản sạch để đem đi Repo hoặc chiết khấu tại NHTW? |
| **4. [[lcr-by-currency]]** | Tỷ lệ LCR riêng cho từng đồng tiền chiếm $\ge 5\%$ tổng nợ [[src-bcbs-framework#^srp50-35]] [[src-bcbs-framework#^srp50-37]] | Ngân hàng có bị ảo tưởng thặng dư nội tệ nhưng thực chất đang đối mặt với khủng hoảng thiếu hụt USD không? |
| **5. Market-related Tools** | Giám sát giá cổ phiếu, CDS spread, lợi suất nợ thứ cấp và lãi suất thị trường tiền tệ [[src-bcbs-framework#^srp50-40]] [[src-bcbs-framework#^srp50-43]] | Thị trường có đang phát tín hiệu mất niềm tin vào chất lượng tín dụng và thanh khoản của ngân hàng không? |

---

## 3. Tương Tác với Bảng Cân Đối Mục Tiêu (Synthetic Balance Sheet)

Trong mô hình:
* **Kiểm định Khe hở Kỳ hạn**: Phân rã dòng tiền gốc theo thang kỳ hạn hợp đồng SRP50 giúp ALM Treasury xác định chính xác điểm thâm hụt lũy kế cực đại (Maximum Cumulative Outflow) để thiết kế quy mô đệm [[hqla]].
* **Hạn mức Tập trung Nguồn vốn**: [[alco|ALCO]] sử dụng ngưỡng $1\%$ của SRP50 để ấn định hạn mức trần huy động cho khối khách hàng doanh nghiệp lớn và định chế tài chính, đồng thời định giá chuyển nhượng vốn nội bộ (FTP) lũy tiến đối với các khoản tiền gửi tập trung.
* **Cơ cấu Tiền tệ**: Bắt buộc bảng cân đối tổng hợp phải có sub-balance sheet cho từng đồng tiền trọng yếu nhằm duy trì $\text{LCR}_{\text{USD}} \ge 100\%$.

---

## Nền tảng nguyên tắc: [[bcbs-liquidity-principles|BCBS 144]] Principle 5
- Không có chỉ số đơn lẻ đo trọn rủi ro thanh khoản, nên ngân hàng nên dùng bộ công cụ đo tuỳ biến, gồm thước đo cấu trúc bảng cân đối và thước đo dự phóng dòng tiền [[src-bcbs-liquidity-principles-2008#^lrm-47]].
- Thước đo trong stress làm cơ sở cho hạn mức rủi ro thanh khoản và chỉ báo sớm [[src-bcbs-liquidity-principles-2008#^lrm-47]]; ví dụ hạn mức chênh lệch dòng tiền hợp đồng luỹ kế theo kỳ hạn [[src-bcbs-liquidity-principles-2008#^lrm-50]] và danh sách chỉ báo sớm như tập trung tăng, chênh lệch tiền tệ tăng [[src-bcbs-liquidity-principles-2008#^lrm-53]].
- MIS nên tính được vị thế thanh khoản theo mọi đồng tiền, từng pháp nhân và hợp nhất [[src-bcbs-liquidity-principles-2008#^lrm-56]].

*Diễn giải:* năm công cụ SRP50 ở mục 2 chuẩn hoá một phần bộ thước đo mà Principle 5 để ngân hàng tự thiết kế.

## 4. Ma trận Liên kết Hệ thống ALM Wiki

* **Chuẩn mực Nguồn**: [[src-bcbs-framework]] (Chương SRP50, claims ^srp50-1 đến ^srp50-4).
* **Các Hợp phần Trực thuộc**: [[contractual-maturity-mismatch]], [[funding-concentration-risk]], [[available-unencumbered-assets]], [[lcr-by-currency]], [[intraday-liquidity-risk]].
* **Các Chuẩn mực Định lượng**: [[lcr]], [[nsfr]], [[hqla]], [[net-cash-outflows]].
* **Chiến lược & Bảng Cân đối**: [[lcr-nsfr-interlinkages]].

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
