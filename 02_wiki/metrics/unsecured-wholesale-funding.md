---
title: Unsecured wholesale funding
aliases: [Unsecured wholesale funding, Nguồn vốn bán buôn không có bảo đảm, Wholesale funding]
type: metric
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]"]
relations:
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-19]]"}
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr40-20]]"}
tags: [funding, liquidity]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

Nợ và nghĩa vụ huy động từ pháp nhân (kể cả doanh nghiệp tư nhân, hợp danh), không có tài sản bảo đảm cụ thể; không gồm nghĩa vụ phái sinh [[src-bcbs-lcr#^lcr40-19]]. Trong LCR chỉ tính phần đáo hạn hoặc có thể bị rút trong 30 ngày, kể cả quyền chọn của nhà đầu tư [[src-bcbs-lcr#^lcr40-20]].

## Công thức & tham số

### Cơ chế & drivers
[[run-off-rate]] tăng theo mức "nhạy cảm" của đối tác:

| Đối tác | Run-off | Nguồn |
|---|---|---|
| SME (< 1 triệu EUR, quản lý như bán lẻ) | như tiền gửi bán lẻ: 5% / ≥ 10% | [[src-bcbs-lcr#^lcr40-22]] [[src-bcbs-lcr#^lcr40-23]] |
| Operational deposits | 25% | [[operational-deposits]] |
| DN phi tài chính, chính phủ, NHTW, MDB, PSE | 40%; 20% nếu bảo hiểm toàn bộ | [[src-bcbs-lcr#^lcr40-40]] [[src-bcbs-lcr#^lcr40-41]] |
| Ngân hàng, công ty chứng khoán, bảo hiểm, fiduciary, SPV, công ty liên kết | 100% | [[src-bcbs-lcr#^lcr40-42]] |
| Trái phiếu ngân hàng tự phát hành | 100% (trừ bán riêng cho bán lẻ/SME) | [[src-bcbs-lcr#^lcr40-43]] |
| Prime brokerage customer balances | loại trừ khỏi HQLA, tách riêng và đối ứng dòng vào tại LCR40.87 | [[src-bcbs-lcr#^lcr40-44]] |

**Quyền chọn rút vốn và kỳ vọng thị trường (*Call Options & Reputational Triggers*)**:
Nếu công cụ nợ bán buôn có quyền chọn mua lại (*call option*) do ngân hàng nắm giữ, nhưng thị trường kỳ vọng ngân hàng sẽ thực hiện quyền chọn trước hạn, thì ngân hàng bắt buộc phải giả định sẽ mua lại và ghi nhận dòng ra [[src-bcbs-lcr#^lcr40-20]]. Việc từ chối thực hiện quyền chọn mua lại có thể bị thị trường diễn giải là dấu hiệu ngân hàng đang kiệt quệ thanh khoản (*reputational damage*, xem [[reputational-risk]]).

**Quy tắc cộng gộp đối với SME (*Consolidated SME Threshold*)**:
Ngưỡng 1 triệu EUR vốn huy động được tính trên tổng số dư gộp (không bù trừ tín dụng đã cấp) và trên cơ sở hợp nhất: nếu nhiều khách hàng doanh nghiệp nhỏ có quan hệ sở hữu hoặc liên kết với nhau, họ phải được coi là một chủ nợ duy nhất để so sánh với ngưỡng 1 triệu EUR (footnote của LCR40.23).

**Điều kiện nghiêm ngặt đối với trái phiếu bán lẻ**:
Đối với trái phiếu ngân hàng tự phát hành, để thoát khỏi mức run-off 100% và xếp vào nhóm bán lẻ, việc sản phẩm được tiếp thị cho bán lẻ là chưa đủ; hợp đồng phải có điều khoản ràng buộc pháp lý ngăn cấm việc chuyển nhượng hoặc nắm giữ bởi các đối tượng không phải khách hàng bán lẻ [[src-bcbs-lcr#^lcr40-43]].

## Diễn giải

### Phụ thuộc regime
*Diễn giải:* wholesale funding từ tổ chức tài chính là nguồn vốn đầu tiên bị rút khi có stress. Run-off 100% phản ánh giả định "không tái tục" trong 30 ngày.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM**: *Diễn giải* — phụ thuộc vào nguồn vốn liên ngân hàng ngắn hạn làm [[lcr]] giảm mạnh, vì nguồn này vừa có run-off 100% vừa không được bù bởi dòng vào bán lẻ (50%).
- **VN**: [cần nguồn] — TT50/2026 PL1 chưa ingest.

## Câu hỏi mở
- Tiền gửi của tổ chức kinh tế lớn tại VN (DN nhà nước) được xếp nhóm nào theo TT50/2026?
