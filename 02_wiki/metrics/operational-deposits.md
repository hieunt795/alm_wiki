---
title: Operational deposits
aliases: [Operational deposits, Tiền gửi phục vụ hoạt động, Tiền gửi thanh toán vận hành]
type: metric
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[unsecured-wholesale-funding]]", cite: "[[src-bcbs-lcr#^lcr40-26]]"}
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-26]]"}
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
tags: [deposit, cash-management, liquidity]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

Tiền gửi do khách hàng (tài chính hoặc phi tài chính) để lại ngân hàng để dùng dịch vụ clearing, custody, cash management. [[run-off-rate]] là 25%, thay vì 40% hoặc 100% như wholesale funding thông thường, nhưng chỉ khi khách hàng **phụ thuộc thực chất** vào ngân hàng. Việc áp dụng cần supervisor chấp thuận [[src-bcbs-lcr#^lcr40-26]].

## Công thức & tham số

### Cơ chế & drivers
Điều kiện của dịch vụ [[src-bcbs-lcr#^lcr40-27]]:
1. Khách hàng dựa vào ngân hàng như bên trung gian thứ ba độc lập trong 30 ngày tới.
2. Có hợp đồng ràng buộc với khách hàng tổ chức.
3. Chấm dứt hợp đồng phải báo trước ≥ 30 ngày, hoặc chịu chi phí chuyển đổi đáng kể.

Chỉ phần số dư **thực sự phục vụ nhu cầu vận hành** mới được hưởng 25%. Phần dư (excess balance) xếp vào non-operational. Ngân hàng không xác định được excess thì toàn bộ là non-operational [[src-bcbs-lcr#^lcr40-29]].

**Phương pháp luận xác định số dư thặng dư (*Excess Balance Methodology*)**:
Theo [[src-bcbs-lcr#^lcr40-30]], ngân hàng phải thiết lập phương pháp luận định lượng ở mức độ chi tiết (*granular level*) để nhận diện các khách hàng duy trì số dư vượt quá nhu cầu chi trả. Các chỉ báo giám sát bao gồm: tỷ lệ số dư tài khoản trên khối lượng thanh toán/quyết toán bình quân (*account balance to payment volume*), hoặc tỷ lệ số dư trên tổng giá trị tài sản lưu ký (*assets under custody*).

**Phạm vi dịch vụ tạo tiền gửi operational**:
- *Clearing* (bù trừ thanh toán, thấu chi trong ngày daylight overdraft, post-settlement balances) [[src-bcbs-lcr#^lcr40-33]].
- *Custody* (lưu ký chứng khoán, xử lý cổ tức, nhận tiền mua/bán lại chứng chỉ quỹ, dịch vụ escrow/trust) [[src-bcbs-lcr#^lcr40-34]].
- *Cash management* (quản lý tiền mặt tập trung, chi trả lương payroll, thu hộ/chi hộ) [[src-bcbs-lcr#^lcr40-35]].

Loại trừ: correspondent banking (tài khoản nostro/vostro) và prime brokerage [[src-bcbs-lcr#^lcr40-32]].

**Tiền gửi trong mạng lưới ngân hàng hợp tác xã (*Institutional Networks of Cooperative Banks*)**:
Tiền gửi của các ngân hàng thành viên tại định chế trung ương của mạng lưới được áp run-off **25%** (thay vì 100% như liên ngân hàng thông thường) nếu hai bên cùng tham gia quỹ bảo vệ thanh khoản và khả năng thanh toán tương hỗ, và khoản tiền gửi bắt nguồn từ yêu cầu tối thiểu theo luật định hoặc phân công nhiệm vụ chung [[src-bcbs-lcr#^lcr40-37]] [[src-bcbs-lcr#^lcr40-39]].

Đối xứng: bên gửi tiền operational (hoặc gửi trong mạng lưới hợp tác xã) bắt buộc phải tính **inflow 0%** [[src-bcbs-lcr#^lcr40-31]] [[src-bcbs-lcr#^lcr40-38]] [[src-bcbs-lcr#^lcr40-89]] [[src-bcbs-lcr#^lcr40-90]].

Phần được bảo hiểm toàn bộ có thể xử lý như stable retail [[src-bcbs-lcr#^lcr40-36]].

## Diễn giải

### Phụ thuộc regime
Khi lãi suất gần 0, tài khoản operational nên không trả lãi. Trong giai đoạn lãi suất thấp kéo dài, excess balance có thể rất lớn [[src-bcbs-lcr#^lcr40-28]].

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM**: *Diễn giải* — dịch vụ cash management cho doanh nghiệp tạo nguồn vốn có run-off thấp hơn đáng kể so với tiền gửi doanh nghiệp thông thường (25% so với 40%). Đổi lại, ngân hàng phải có phương pháp tách excess balance đủ chi tiết.
- **VN**: [[tt50-2026|TT50/2026]] dùng khái niệm "tiền gửi hoạt động" phát sinh từ thanh toán bù trừ, lưu ký, quản lý tiền mặt, hệ số rút tiền 25%; phần vượt mức yêu cầu không được áp 25%, và nếu không xác định được phần vượt thì toàn bộ không đủ điều kiện [[src-tt50-2026-nhnn#^pl1-b3]]. Ngân hàng phải có phương pháp xác định số dư vượt mức trong quy định nội bộ [[src-tt50-2026-nhnn#^d14-5]]. ASF của tiền gửi hoạt động 50% [[src-tt50-2026-nhnn#^pl2-a2]].

## Câu hỏi mở
- [[tt50-2026|TT50/2026]] có khái niệm tương đương "operational deposits" không?
