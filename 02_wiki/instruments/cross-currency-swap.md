---
title: "Cross-Currency Swap"
aliases: [Cross-Currency Swap, Currency swap, CCS, Hoán đổi tiền tệ chéo, Hoán đổi lãi suất tiền tệ chéo]
type: instrument
domains: [product, alm]
status: active
maturity: draft
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [cross-currency-swap, fx-hedging, structural-fx-risk, hedging]
updated: 2026-10-19
reviewed:
---

## Định nghĩa & cashflow
Cross-currency swap là giao dịch ngoại bảng, trong đó hai bên trao đổi gốc và lãi bằng hai đồng tiền khác nhau. Khác với [[interest-rate-swap]], cross-currency swap có trao đổi gốc [[src-choudhry-principles-banking#^choudhry-fxs-2]].

- Đầu kỳ: hai bên trao đổi notional bằng hai đồng tiền, ngầm định một tỷ giá [[src-choudhry-principles-banking#^choudhry-fxs-2]].
- Trong kỳ: mỗi bên trả lãi định kỳ bằng đồng tiền của gốc đã nhận [[src-choudhry-principles-banking#^choudhry-fxs-2]].
- Đáo hạn: hai bên đổi lại đúng số gốc theo cùng tỷ giá ban đầu [[src-choudhry-principles-banking#^choudhry-fxs-2]].

Chính việc trao đổi gốc rồi đảo lại cùng số tiền cho phép ngân hàng quản lý rủi ro FX và rủi ro lãi suất liên quan trên đồng ngoại tệ [[src-choudhry-principles-banking#^choudhry-fxs-2]].

## Pricing
[cần nguồn]

## Risk factors & sensitivities
- Swap cố định hoặc phòng ngừa phơi nhiễm tiền tệ và lãi suất. Đổi lại, ngân hàng chịu chi phí cơ hội khi tỷ giá đi theo chiều có lợi cho phơi nhiễm translation [[src-choudhry-principles-banking#^choudhry-fxs-3]].
- **Trả nợ trước hạn**: với khách hàng wholesale, ngân hàng có thể áp phí trả trước theo mark-to-market. Với khách hàng bán lẻ, quy ước có thể khác, nên chấm dứt sớm swap có thể tốn kém [[src-choudhry-principles-banking#^choudhry-fxs-4]].
- **Khoản vay không trả được**: điều khoản swap vẫn phải thực hiện [[src-choudhry-principles-banking#^choudhry-fxs-4]].
- **Biên lãi bằng ngoại tệ**: biên lãi tích luỹ bằng ngoại tệ, ngân hàng cần quyết định cách quy đổi về đồng tiền báo cáo (spot hoặc forward) [[src-choudhry-principles-banking#^choudhry-fxs-4]].

## ALM & hedging usage
- Mục đích của kỷ luật ALM khi dùng cross-currency swap là loại bỏ bất định và giữ [[net-interest-margin|NIM]] [[src-choudhry-principles-banking#^choudhry-fxs-3]].
- Chênh lệch tiền tệ nên nằm trong khẩu vị rủi ro structural FX (và lãi suất) do Board phê duyệt trong RAS [[src-choudhry-principles-banking#^choudhry-fxs-3]].
- Khoảng 95% nhu cầu phòng ngừa FX của các ngân hàng có thể đáp ứng bằng sản phẩm tiền mặt hoặc phái sinh plain vanilla [[src-choudhry-principles-banking#^choudhry-fxs-1]].

**Ví dụ 6.6 (ChoudWest Bank)** [[src-choudhry-principles-banking#^choudhry-fxs-5]]:

| Giao dịch | Điều kiện | Nguồn |
|---|---|---|
| Tiền gửi | GBP 50 triệu, cố định 0,30%, 2 năm, trả lãi 6 tháng | [[src-choudhry-principles-banking#^choudhry-fxs-5]] |
| Cho vay | USD 65 triệu bullet, USD RFR 6 tháng + 2,0% | [[src-choudhry-principles-banking#^choudhry-fxs-5]] |
| Cross-currency swap | 2 năm, nhận cố định GBP 0,20%, trả USD thả nổi 6 tháng, tỷ giá GBP/USD 1,30 | [[src-choudhry-principles-banking#^choudhry-fxs-5]] |
| Thu nhập USD hằng năm | USD 1,3 triệu | [[src-choudhry-principles-banking#^choudhry-fxs-5]] |

Ngân hàng có thể dùng FX forward để bảo vệ giá trị GBP của thu nhập USD [[src-choudhry-principles-banking#^choudhry-fxs-5]].

*Diễn giải:* chân trả USD thả nổi của swap khớp với khoản cho vay USD thả nổi, nên thu nhập USD còn lại là spread 2,0% của khoản vay. Con số USD 1,3 triệu chưa tính chênh lệch âm bên GBP: swap trả cho ngân hàng 0,20%, trong khi ngân hàng trả người gửi 0,30%.

## Kế toán
[cần nguồn]

## Basel treatment
[cần nguồn]

## Lưu ý tại VN
[cần nguồn]
