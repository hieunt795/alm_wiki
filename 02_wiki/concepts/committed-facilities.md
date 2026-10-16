---
title: Committed credit and liquidity facilities
aliases: [Committed facilities, Hạn mức tín dụng cam kết, Drawdown rate, Liquidity facility]
type: concept
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]"]
relations:
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-59]]"}
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr40-64]]"}
tags: [off-balance-sheet, liquidity, contingent]
updated: 2026-10-15
reviewed:
---

## Ý chính
Thoả thuận cấp vốn trong tương lai cho khách hàng bán lẻ hoặc wholesale, không huỷ ngang (committed) hoặc huỷ ngang có điều kiện. Phần chưa giải ngân được giả định bị rút theo drawdown rate trong stress. Phần đã rút được coi là dư nợ không được trả lại, bất kể kỳ hạn [[src-bcbs-lcr#^lcr40-59]].

## Cơ chế & drivers
Drawdown rate trên phần chưa giải ngân [[src-bcbs-lcr#^lcr40-64]]:

| Đối tượng | Credit facility | Liquidity facility |
|---|---|---|
| Bán lẻ, SME | 5% | 5% |
| DN phi tài chính, chính phủ, NHTW, PSE, MDB | 10% | 30% |
| Ngân hàng chịu giám sát an toàn | 40% | 40% |
| Định chế tài chính khác (chứng khoán, bảo hiểm, fiduciary) | 40% | 100% |
| Pháp nhân khác (SPE, conduit, SPV) | 100% | 100% |

**Định nghĩa phân biệt Credit Facility vs Liquidity Facility**:
Theo [[src-bcbs-lcr#^lcr40-61]], *Liquidity Facility* là bất kỳ hạn mức cam kết chưa rút nào được dùng để tái tài trợ các nghĩa vụ nợ của khách hàng trong trường hợp khách hàng không thể đảo nợ trên thị trường tài chính (ví dụ bảo lãnh thanh khoản cho chương trình thương phiếu ABCP). Quy mô tính là liquidity facility giới hạn ở phần nợ của khách hàng đáo hạn trong 30 ngày; phần cam kết vượt quá được tính là credit facility. Các hạn mức tài trợ vốn lưu động thông thường (*revolving working capital*) cho doanh nghiệp bắt buộc xếp vào *Credit Facility* [[src-bcbs-lcr#^lcr40-61]].

Mọi hạn mức cung cấp cho quỹ đầu cơ (*hedge funds*), quỹ thị trường tiền tệ (*MMFs*), SPE, conduit đều bị ấn định 100% là liquidity facility (drawdown 100%) [[src-bcbs-lcr#^lcr40-62]] [[src-bcbs-lcr#^lcr40-64]].

**Tính ròng với HQLA bảo đảm (*Collateral Netting*)**:
Phần hạn mức chưa giải ngân được tính ròng với giá trị thanh khoản của [[hqla]] mà đối tác đã đặt cọc hoặc cam kết theo hợp đồng sẽ đặt cọc khi giải ngân (ví dụ hạn mức cơ cấu dạng repo), với điều kiện ngân hàng có đầy đủ quyền pháp lý và năng lực vận hành để tái sử dụng tài sản đó, và không có tương quan bất lợi giữa xác suất rút vốn và giá trị tài sản bảo đảm [[src-bcbs-lcr#^lcr40-60]].

Các quy tắc bổ sung:
- Nghĩa vụ theo hợp đồng cấp vốn trong 30 ngày cho các tổ chức tài chính và NHTW: dòng ra **100%** [[src-bcbs-lcr#^lcr40-65]].
- Nghĩa vụ cấp vốn theo hợp đồng cho khách bán lẻ và wholesale phi tài chính: phần vượt 50% dòng vào hợp đồng từ chính nhóm đó tính là dòng ra **100%** [[src-bcbs-lcr#^lcr40-66]].
- Hạn mức mà **ngân hàng được cấp** từ tổ chức khác (kể cả NHTW): inflow **0%** [[src-bcbs-lcr#^lcr40-82]] [[src-bcbs-lcr#^lcr40-75]].
- Trade finance: run-off thấp, ví dụ ≤ 5%, do cơ quan quốc gia quyết định [[src-bcbs-lcr#^lcr40-71]].
- Dòng ra hợp đồng khác: **100%** (không bao gồm chi phí hoạt động nội bộ) [[src-bcbs-lcr#^lcr40-74]].

## Phụ thuộc regime
*Diễn giải:* tỷ lệ rút hạn mức tăng mạnh khi khách hàng doanh nghiệp mất khả năng tiếp cận thị trường vốn. Vì thế liquidity facility (backup cho phát hành giấy tờ nợ) có drawdown cao hơn credit facility.

## Góc nhìn theo domain
- **ALM**: *Diễn giải* — hạn mức chưa giải ngân là nguồn dòng ra tiềm tàng thường bị đánh giá thấp. Cần theo dõi theo đối tượng và theo loại (credit/liquidity).
- **VN**: [cần nguồn].

## Câu hỏi mở
- Hạn mức thấu chi và hạn mức tín dụng "có thể huỷ ngang" tại VN được xử lý thế nào theo TT50/2026?
