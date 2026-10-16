---
title: "BCBS LCR standard (Basel Framework — LCR)"
aliases: [Basel LCR, LCR standard, Basel III LCR]
type: regulation
domains: [basel, alm]
status: active
maturity: draft
issuer: BCBS
number: "Basel Framework — LCR"
jurisdiction: INTL
doc_status: final
issued:
valid_from: 2019-12-15
valid_to:
supersedes: []
superseded_by:
amends: []
implements: []
sources: ["[[src-bcbs-lcr]]"]
relations:
  - {type: governs, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr10-1]]"}
  - {type: governs, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr30-1]]"}
  - {type: governs, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: governs, to: "[[alternative-liquidity-approaches]]", cite: "[[src-bcbs-lcr#^lcr31-1]]"}
  - {type: governs, to: "[[liquidity-transfer-restrictions]]", cite: "[[src-bcbs-lcr#^lcr30-24]]"}
tags: [liquidity, basel-iii]
updated: 2026-10-15
reviewed:
---

## Mục đích & phạm vi
Tăng khả năng chống chịu thanh khoản ngắn hạn: ngân hàng phải giữ đủ [[hqla]] để vượt qua kịch bản stress 30 ngày [[src-bcbs-lcr#^lcr20-1]].
- Do [[bcbs]] ban hành, là một standard trong Basel Framework.
- Version effective trong framework hợp nhất: 15/12/2019. LCR40 có FAQ bổ sung ngày 30/03/2023.
- Phạm vi áp dụng: Bắt buộc trên cơ sở hợp nhất (consolidated basis) cho tất cả các ngân hàng hoạt động quốc tế; cơ quan quản lý có thể mở rộng áp dụng cho các ngân hàng khác hoặc từng nhóm thực thể độc lập [[src-bcbs-lcr#^lcr10-1]].
- Giám sát đa tầng: Ngân hàng phải chủ động kiểm soát rủi ro thanh khoản ở cấp độ từng pháp nhân độc lập, chi nhánh nước ngoài, công ty con và toàn tập đoàn, có tính đến các rào cản chuyển giao vốn [[src-bcbs-lcr#^lcr10-3]].
- Đầu tư không hợp nhất: Khoản đầu tư vào thực thể tài chính/chứng khoán mà tập đoàn là bên cấp thanh khoản chính khi stress (do cam kết hoặc rủi ro uy tín) phải được lượng hóa vào mục nghĩa vụ tiềm tàng [[src-bcbs-lcr#^lcr10-2]].
- Đồng tiền trọng yếu: LCR phải được đáp ứng trên cơ sở hợp nhất bằng đồng tiền chung, nhưng phải giám sát riêng thanh khoản theo từng đồng tiền trọng yếu; không giả định các đồng tiền có thể tự do chuyển đổi khi stress [[src-bcbs-lcr#^lcr10-9]].

## Yêu cầu chính

| Điều khoản | Yêu cầu | Ngưỡng | Hiệu lực / lộ trình |
|---|---|---|---|
| LCR10.1 | Phạm vi áp dụng | Ngân hàng hoạt động quốc tế (consolidated) [[src-bcbs-lcr#^lcr10-1]] | 15/12/2019 (consolidated) |
| LCR10.5, 10.6 | Nguyên tắc Home vs Host | Tiền gửi bán lẻ/SME theo Host; các khoản khác theo Home [[src-bcbs-lcr#^lcr10-5]] [[src-bcbs-lcr#^lcr10-6]] | |
| LCR10.7 | Rào cản chuyển giao thanh khoản | Loại bỏ thặng dư HQLA bị ring-fence khỏi LCR hợp nhất [[src-bcbs-lcr#^lcr10-7]] | |
| LCR20.4–20.5 | LCR = HQLA / total net cash outflows 30 ngày | ≥ 100% khi không có stress [[src-bcbs-lcr#^lcr20-5]] | |
| LCR20.7 | Báo cáo supervisor | ≥ hàng tháng; độ trễ lý tưởng ≤ 2 tuần [[src-bcbs-lcr#^lcr20-7]] | |
| LCR20.8 | Thông báo khi < 100% | ngay lập tức [[src-bcbs-lcr#^lcr20-8]] | |
| LCR30.31, 30.34 | Trần Level 2 trong HQLA | ≤ 40% sau haircut & unwind 30 ngày [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-34]] | |
| LCR30.31, 30.45 | Trần Level 2B trong HQLA | ≤ 15% sau haircut & unwind 30 ngày [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-45]] | |
| LCR30.16, 30.18 | Yêu cầu vận hành HQLA | unencumbered, treasury control, monetisation test [[src-bcbs-lcr#^lcr30-15]] [[src-bcbs-lcr#^lcr30-16]] [[src-bcbs-lcr#^lcr30-18]] | |
| LCR31.1–31.20 | Phương pháp thanh khoản thay thế (ALA) | Option 1 (CLF), Option 2 (FX HQLA min 8%), Option 3 (Level 2A min 20%) [[src-bcbs-lcr#^lcr31-1]] [[src-bcbs-lcr#^lcr31-3]] [[src-bcbs-lcr#^lcr31-4]] [[src-bcbs-lcr#^lcr31-14]] [[src-bcbs-lcr#^lcr31-17]] | Áp dụng có trần (ví dụ 80%), rà soát 5 năm [[src-bcbs-lcr#^lcr31-4]] [[src-bcbs-lcr#^lcr31-58]] |
| LCR40.1, 40.77 | Dòng vào bù trừ dòng ra | trần 75% dòng ra [[src-bcbs-lcr#^lcr40-77]] | |
| LCR40.5–40.43 | Run-off theo loại nguồn vốn | xem [[run-off-rate]] | |
| LCR40.45–40.48 | Secured funding | xem [[secured-funding]] | |
| LCR40.59–40.66 | Committed facilities | xem [[committed-facilities]] | |
| LCR40.75–40.89 | Dòng vào | xem [[net-cash-outflows]] | |

## Định nghĩa đáng chú ý
- HQLA [[src-bcbs-lcr#^lcr30-1]]; Level 1 [[src-bcbs-lcr#^lcr30-41]]; Level 2A [[src-bcbs-lcr#^lcr30-43]]; Level 2B [[src-bcbs-lcr#^lcr30-45]]; Alternative liquidity approaches (ALA) [[src-bcbs-lcr#^lcr31-1]]; Committed liquidity facility (CLF) [[src-bcbs-lcr#^lcr31-12]]; Liquidity transfer restrictions / ring-fencing [[src-bcbs-lcr#^lcr10-7]]; Retail deposits [[src-bcbs-lcr#^lcr40-5]]; stable deposits [[src-bcbs-lcr#^lcr40-7]]; effective deposit insurance scheme [[src-bcbs-lcr#^lcr40-8]]; unsecured wholesale funding [[src-bcbs-lcr#^lcr40-19]]; secured funding [[src-bcbs-lcr#^lcr40-45]]; committed facilities [[src-bcbs-lcr#^lcr40-59]].

## Báo cáo & nghĩa vụ
Xem LCR20.7–20.8 ở bảng trên. Tham số thuộc national discretion phải được công bố công khai [[src-bcbs-lcr#^lcr40-2]].

## Sửa đổi / thay thế
- Chưa ingest lịch sử phiên bản (Basel III LCR 2013 → consolidated framework 2019). Đánh dấu [cần nguồn].
- Phần chuyển tiếp nằm ở LCR90, chưa ingest.

## Tác động ALM
Xem [[lcr]] (mục Ứng dụng trong ALM) và [[net-cash-outflows]].
