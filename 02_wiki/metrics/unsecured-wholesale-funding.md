---
title: Unsecured wholesale funding
aliases: [Unsecured wholesale funding, Nguồn vốn bán buôn không có bảo đảm, Wholesale funding]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-19]]"}
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr40-20]]"}
tags: [funding, liquidity]
updated: 2026-10-21
reviewed:
---

## Định nghĩa

Nợ và nghĩa vụ huy động từ pháp nhân (kể cả doanh nghiệp tư nhân, hợp danh), không có tài sản bảo đảm cụ thể; không gồm nghĩa vụ phái sinh [[src-bcbs-lcr#^lcr40-19]]. Trong LCR chỉ tính phần đáo hạn hoặc có thể bị rút trong 30 ngày, kể cả quyền chọn của nhà đầu tư [[src-bcbs-lcr#^lcr40-20]].

## Công thức & tham số

### Cơ chế & drivers
[[run-off-rate]] tăng theo mức "nhạy cảm" của đối tác:

| Đối tác | Run-off | Nguồn |
|---|---|---|
| SME (< 1 triệu EUR, quản lý như bán lẻ) | như tiền gửi bán lẻ: 5% / ≥ 10%; tiền gửi có kỳ hạn như tiền gửi có kỳ hạn bán lẻ | [[src-bcbs-lcr#^lcr40-22]] [[src-bcbs-lcr#^lcr40-23]] [[src-bcbs-lcr#^lcr40-24]] [[src-bcbs-lcr#^lcr40-25]] |
| Operational deposits | 25% | [[operational-deposits]] |
| DN phi tài chính, chính phủ, NHTW, MDB, PSE | 40%; 20% nếu bảo hiểm toàn bộ | [[src-bcbs-lcr#^lcr40-40]] [[src-bcbs-lcr#^lcr40-41]] |
| Ngân hàng, công ty chứng khoán, bảo hiểm, fiduciary, SPV, công ty liên kết | 100% | [[src-bcbs-lcr#^lcr40-42]] |
| Trái phiếu ngân hàng tự phát hành | 100% (trừ bán riêng cho bán lẻ/SME) | [[src-bcbs-lcr#^lcr40-43]] |
| Prime brokerage customer balances | loại trừ khỏi HQLA, tách riêng và đối ứng dòng vào tại LCR40.87 | [[src-bcbs-lcr#^lcr40-44]] |

**Thời hạn báo trước vượt 30 ngày**: vốn bán buôn bên cấp vốn có quyền đòi nhưng phải tuân thời hạn báo trước theo hợp đồng vượt 30 ngày thì không tính vào dòng ra [[src-bcbs-lcr#^lcr40-21]]. TT50: nguồn vốn có quyền rút trước hạn với thời gian thông báo trên 30 ngày mà khách hàng chưa thông báo rút thì không tính [[src-tt50-2026-nhnn#^pl1-b1-4a]].

**SME khi ngân hàng không có dư nợ với khách hàng**: vẫn được xếp vào nhóm SME nếu tổng vốn huy động dưới 1 triệu EUR và được quản lý như tiền gửi bán lẻ [[src-bcbs-lcr#^lcr40-24]].

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
- **VN**: theo [[tt50-2026|TT50/2026]], tiền gửi DNNVV đủ điều kiện (tiền gửi bình quân tháng liền kề không quá 30 tỷ đồng) tính như bán lẻ (5% ổn định / 10% kém ổn định) [[src-tt50-2026-nhnn#^pl1-b3-22]]; tiền gửi hoạt động 25% (chi phí chuyển đổi tối thiểu toàn bộ lãi + 10% gốc) [[src-tt50-2026-nhnn#^pl1-b3-23a]] [[src-tt50-2026-nhnn#^pl1-b3-23c]]; doanh nghiệp không phải DNNVV đủ điều kiện, không phải tổ chức tài chính, và Chính phủ, NHNN, NHTW, PSE nước ngoài, KBNN, UBND cấp tỉnh, ngân hàng chính sách, BHTG, BHXH, tổ chức tài chính quốc tế 40% [[src-tt50-2026-nhnn#^pl1-b3-24]]; nguồn vốn không có bảo đảm khác (không thuộc các nhóm trên) 100% [[src-tt50-2026-nhnn#^pl1-b3-25]]. Nghĩa vụ phái sinh không thuộc nguồn vốn bán buôn không có bảo đảm [[src-tt50-2026-nhnn#^pl1-b3-1]].

## Câu hỏi mở (Đã giải quyết)
- *Phân loại tiền gửi DNNN theo TT50/2026* (*Diễn giải*, TT50 không nhắc DNNN): Doanh nghiệp nhà nước tại Việt Nam hoạt động theo Luật Doanh nghiệp dưới hình thức công ty TNHH hoặc CTCP, là doanh nghiệp phi tài chính. Theo TT50 PL1.B.III.2.4 [[src-tt50-2026-nhnn#^pl1-b3-24]], nếu không đủ điều kiện là DNNVV ($\le 30$ tỷ đồng) và không phải tiền gửi hoạt động (25%), tiền gửi của DNNN thuộc nhóm doanh nghiệp phi tài chính với hệ số rút tiền 40%.
