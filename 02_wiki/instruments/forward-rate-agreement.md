---
title: "Forward Rate Agreement"
aliases: [Forward Rate Agreement, FRA, Hợp đồng kỳ hạn lãi suất, Thoả thuận lãi suất kỳ hạn]
type: instrument
domains: [product, alm]
status: active
maturity: draft
sources: ["[[src-choudhry-principles-banking]]"]
relations:
  - {type: hedges, to: "[[gap-risk]]", cite: "[[src-choudhry-principles-banking#^choudhry-hedge-8]]"}
tags: [fra, hedging, irrbb, money-market, derivatives]
updated: 2026-10-19
reviewed:
---

## Định nghĩa & cashflow
FRA là hợp đồng ngoại bảng. Bên mua vay danh nghĩa, bên bán cho vay danh nghĩa một số tiền ở lãi suất cố định cho một kỳ bắt đầu ở một ngày tương lai [[src-choudhry-principles-banking#^choudhry-hedge-8]].

- **Fixing date**: lãi suất thực tế được lấy vào ngày bắt đầu kỳ danh nghĩa [[src-choudhry-principles-banking#^choudhry-hedge-8]].
- **Thanh toán**: bên vay hoặc bên cho vay nhận khoản bằng chênh lệch giữa lãi suất hợp đồng và lãi suất thực tế, tính trên notional [[src-choudhry-principles-banking#^choudhry-hedge-8]].
- **Chiết khấu**: khoản thanh toán được present-value vì chuyển vào đầu kỳ danh nghĩa, trong khi giao dịch tiền mặt trả lãi cuối kỳ [[src-choudhry-principles-banking#^choudhry-hedge-8]].
- Không có khoản vay hay cho vay tiền mặt thực tế [[src-choudhry-principles-banking#^choudhry-hedge-8]].

Ký hiệu "3×15" chỉ FRA cho kỳ 12 tháng bắt đầu sau 3 tháng [[src-choudhry-principles-banking#^choudhry-hedge-9]].

## Pricing
[cần nguồn] Công thức định giá FRA trong nguồn đã ingest bị mất khi convert.

## Risk factors & sensitivities
*Diễn giải:* FRA chịu rủi ro lãi suất kỳ hạn của đúng kỳ danh nghĩa. FRA giống interest-rate futures về khái niệm ([[interest-rate-futures]]) nhưng là hợp đồng OTC [[src-choudhry-principles-banking#^choudhry-hedge-8]].

## ALM & hedging usage
- Để phòng ngừa interest-rate gap trong kỳ tiền mặt, trader mua FRA ứng với kỳ gap, notional bằng phơi nhiễm trên thị trường tiền mặt [[src-choudhry-principles-banking#^choudhry-hedge-8]]. Xem [[gap-risk]].
- **Ví dụ 6.9**: ngân hàng cần vay GBP 10 triệu sau 3 tháng, kỳ 12 tháng, để tài trợ một khoản cho vay doanh nghiệp. Treasury mua FRA 3×15 ở 5½%, notional GBP 10 triệu. Khi Libor lên 6%, khoản thanh toán FRA bù phần chi phí vay tăng, và ngân hàng đã khoá lãi suất funding cho giao dịch bắt đầu trong tương lai [[src-choudhry-principles-banking#^choudhry-hedge-9]].
- FRA, futures và swap trong phần lớn trường hợp là đủ để phòng ngừa rủi ro lãi suất [[src-choudhry-principles-banking#^choudhry-hedge-19]]. Với ngân hàng *liability-sensitive*, phái sinh điều chỉnh phơi nhiễm ngay lập tức, và FRA có thể che rủi ro funding [[src-choudhry-principles-banking#^choudhry-hedge-22]]. Xem [[interest-rate-cap-floor]].
- Khác với option, FRA buộc ngân hàng trả tiền khi lãi suất đi theo chiều ngược lại [[src-choudhry-principles-banking#^choudhry-hedge-24]].

## Kế toán
[cần nguồn]

## Basel treatment
[cần nguồn]

## Lưu ý tại VN
[cần nguồn]
