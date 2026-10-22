---
title: "Available Unencumbered Assets — Tài Sản Không Bị Phong Tỏa Khả Dụng (Basel SRP50)"
aliases: [Available Unencumbered Assets, Unencumbered Collateral, Tài sản không bị phong tỏa, Tài sản sạch khả dụng, Đệm tài sản bảo đảm]
type: metric
domains: [basel, alm]
status: active
maturity: draft
sources: ["[[src-bcbs-framework]]", "[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[bcbs]]", cite: "[[src-bcbs-framework#^srp50-1]]"}
  - {type: input-to, to: "[[hqla]]", cite: "[[src-bcbs-framework#^srp50-27]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
tags: [liquidity, unencumbered-assets, collateral-management, secured-borrowing, repo, srp50, basel]
updated: 2026-10-20
reviewed:
---

## Định nghĩa

### Tóm tắt Cấp cao (Executive Summary)

**Tài sản không bị phong tỏa khả dụng (Available Unencumbered Assets)** là chỉ số giám sát thanh khoản cốt lõi quy định tại **BCBS SRP50**, cung cấp dữ liệu định lượng về quy mô, chất lượng, loại tiền tệ và địa điểm lưu ký của toàn bộ các tài sản "sạch" mà ngân hàng sở hữu và có quyền tự do định đoạt [[src-bcbs-framework#^srp50-27]].

Những tài sản này đóng vai trò là **tuyến phòng thủ thanh khoản thứ cấp**, có tiềm năng dùng làm tài sản bảo đảm (collateral) để vay có bảo đảm trên thị trường thứ cấp (thị trường Repo liên ngân hàng) hoặc tiếp cận các cửa sổ tái cấp vốn / chiết khấu của Ngân hàng Trung ương [[src-bcbs-framework#^srp50-27]] [[src-bcbs-framework#^srp50-28]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│              KHUNG QUẢN TRỊ TÀI SẢN SẠCH KHẢ DỤNG BASEL SRP50 (UNENCUMBERED ASSETS)              │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                               TỔNG TÀI SẢN CỦA NGÂN HÀNG (TOTAL ASSETS)                         │
├────────────────────────────────────────────────┬────────────────────────────────────────────────┤
│    1. TÀI SẢN BỊ PHONG TỎA (ENCUMBERED)        │      2. TÀI SẢN SẠCH KHẢ DỤNG (UNENCUMBERED)    │
│  • Đã cầm cố Repo lấy vốn ngắn hạn             │  • Nắm giữ tự do, không ràng buộc pháp lý      │
│  • Đã ký quỹ thanh toán bù trừ CCP             │  • Có thể chuyển đổi thành tiền mặt tức thì     │
│  • Thế chấp hạn mức thấu chi NHTW              │                                                │
├────────────────────────────────────────────────┴────────────────────────────────────────────────┤
│                     HAI KÊNH CHUYỂN HÓA THANH KHOẢN VÀ HAI TẦNG HAIRCUT                         │
│  ├── Kênh 1: Vay có bảo đảm Thị trường Thứ cấp (Repo) ➔ Chịu Haircut Thị trường Thứ cấp         │
│  └── Kênh 2: Tái cấp vốn / Chiết khấu tại NHTW        ➔ Chịu Haircut Quy định của NHTW          │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│                     SỰ PHÂN TÁCH VỚI TỬ SỐ HQLA CỦA LCR:                                        │
│  • HQLA (LCR): Phạm vi hẹp, chỉ gồm tài sản có tính thanh khoản siêu cao (Level 1, Level 2)     │
│  • Unencumbered Assets (SRP50): Phạm vi rộng hơn, bao gồm cả các tài sản không đủ chuẩn HQLA    │
│    (như khoản vay doanh nghiệp chất lượng cao đủ điều kiện thế chấp tại cửa sổ chiết khấu NHTW) │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 1. Tiêu Chí Xác Định Tài Sản Sạch (Unencumbered Status)

Một tài sản được xếp vào nhóm **không bị phong tỏa (unencumbered)** khi thỏa mãn đồng thời các điều kiện pháp lý và vận hành nghiêm ngặt:
1. **Không có gánh nặng pháp lý**: Không bị thế chấp, cầm cố, ký quỹ, hoặc làm tài sản bảo đảm cho bất kỳ giao dịch tài trợ nào khác.
2. **Quyền kiểm soát tự do của ALM Treasury**: Không bị ràng buộc bởi các quy định nội bộ hoặc rào cản chuyển giao xuyên biên giới (*ring-fencing*), sẵn sàng điều chuyển và chuyển đổi thành tiền mặt trong thời gian ngắn nhất.
3. **Thanh khoản thứ cấp khả thi**: Có thể huy động được nguồn vốn có bảo đảm trên thị trường thứ cấp ở mức chi phí hợp lý và mức chiết khấu định giá (*haircuts*) xác định được trước [[src-bcbs-framework#^srp50-28]].

---

## Công thức & tham số

### 2. Báo Cáo Hai Tầng Chiết Khấu (Two-Tier Haircut Reporting)

Theo chuẩn mực **SRP50.28 – SRP50.33**, ngân hàng phải báo cáo quy mô tài sản sạch khả dụng qua hai tầng định giá:

1. **Khả năng huy động vốn qua Ngân hàng Trung ương (Central Bank Collateral)**:
   - Toàn bộ tài sản sạch đủ điều kiện thế chấp tại các cơ chế cho vay thường xuyên (*Standing Facilities*) hoặc cửa sổ chiết khấu của NHTW.
   - Báo cáo số tiền vay tối đa có thể giải ngân sau khi trừ tỷ lệ chiết khấu theo quy chế của NHTW (*Central Bank haircut*).
2. **Khả năng huy động vốn trên Thị trường Thứ cấp (Secondary Market Collateral)**:
   - Các tài sản có thể giao dịch Repo với các định chế tài chính khác trên thị trường tiền tệ.
   - Báo cáo theo tỷ lệ chiết khấu thỏa thuận trước hoặc mức chiết khấu thị trường hiện hành (*Secondary market haircut*) [[src-bcbs-framework#^srp50-28]].

---

## Ứng dụng trong ALM

### 4. Ý Nghĩa Điều Hành ALCO và Kế Hoạch Dự Phòng Thanh Khoản (CFP)

Trong quản trị ALM hiện đại:
* **Tối ưu hóa Chi phí Tài trợ**: Treasury không nên giữ toàn bộ tài sản sạch dưới dạng tiền mặt hoặc TPCP lợi suất thấp. Thông qua việc quản trị danh mục tài sản thế chấp (Collateral Optimisation), ngân hàng có thể sử dụng các khoản cho vay bán lẻ hoặc doanh nghiệp đủ chuẩn để cầm cố tại NHTW, giải phóng các tài sản Level 1 có tính thanh khoản cao nhất để tối ưu tỷ lệ LCR.
* **Kế hoạch Dự phòng Thanh khoản (CFP)**: Khi thị trường liên ngân hàng đóng băng và LCR bị đe dọa, kho tài sản sạch unencumbered chính là cơ sở vật chất quyết định ngân hàng có thể kích hoạt bao nhiêu hạn mức cấp vốn khẩn cấp để tự cứu mình trước khi rơi vào tình trạng mất khả năng thanh toán.

---

## Nhầm lẫn thường gặp

### 3. Phân Biệt Giữa Available Unencumbered Assets và HQLA

Mặc dù có mối liên hệ mật thiết, hai khái niệm này phục vụ hai mục đích quản trị khác nhau:

| Tiêu chí | [[hqla\|Tài sản Thanh khoản Cao (HQLA - LCR30)]] | Tài sản Sạch Khả dụng (Available Unencumbered Assets - SRP50) |
|---|---|---|
| **Vị trí trong chuẩn mực** | Tử số bắt buộc của tỷ lệ [[lcr]] | Chỉ số giám sát bổ trợ thuộc Trụ cột 2 [[src-bcbs-framework#^srp50-27]] |
| **Phạm vi tài sản** | Nghiêm ngặt: Chỉ công nhận Tiền mặt, Dự trữ NHTW, TPCP, Trái phiếu PSE/MDB và Trái phiếu doanh nghiệp hạng cao (Level 1, 2A, 2B) | Mở rộng: Bao gồm toàn bộ tài sản có thể dùng làm tài sản bảo đảm (kể cả danh mục cho vay khách hàng đạt chuẩn chiết khấu tại NHTW) |
| **Cơ chế tiền tệ hóa** | Bán đứt trên thị trường hoặc Repo ngắn hạn 30 ngày | Báo cáo chi tiết theo vị trí lưu ký (*location*) và loại tiền tệ (*currency denomination*) [[src-bcbs-framework#^srp50-27]] |
| **Mục đích điều hành ALM** | Bảo đảm sinh tồn trong 30 ngày stress cấp tính | Tối ưu hóa quản trị tài sản bảo đảm (Collateral Management) và hoạch định phương án huy động vốn khẩn cấp (CFP) |

---

## 5. Ma trận Liên kết Hệ thống ALM Wiki

* **Chuẩn mực Nguồn**: [[src-bcbs-framework]] (Chương SRP50, claims ^srp50-27 đến ^srp50-34).
* **Các Khái niệm & Chỉ số**: [[hqla]], [[level-1-assets]], [[level-2-assets]], [[lcr]], [[nsfr]], [[contractual-maturity-mismatch]], [[funding-concentration-risk]].

* **Quản trị**: [[alco]] (điều hành kho tài sản bảo đảm và CFP, xem mục 4).

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
