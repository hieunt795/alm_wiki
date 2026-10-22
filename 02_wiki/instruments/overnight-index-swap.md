---
title: "Overnight Index Swap"
aliases: [Overnight Index Swap, OIS, SONIA swap, €STR swap, Hoán đổi chỉ số lãi suất qua đêm]
type: instrument
domains: [product, alm]
status: active
maturity: draft
sources: ["[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[interest-rate-swap]]", cite: "[[src-choudhry-principles-banking#^choudhry-hedge-15]]"}
  - {type: hedges, to: "[[basis-risk]]", cite: "[[src-choudhry-principles-banking#^choudhry-hedge-18]]"}
tags: [ois, sonia, estr, rfr, nii-hedging, basis-risk]
updated: 2026-10-19
reviewed:
---

## Định nghĩa & cashflow
OIS là interest-rate swap giao dịch trên thị trường tiền tệ, trả cố định đổi lấy lãi suất qua đêm. Swap thông thường trả cố định đổi lấy khoản thả nổi hằng quý hoặc nửa năm [[src-choudhry-principles-banking#^choudhry-hedge-15]].

- Thị trường sterling gọi là SONIA swap; đồng euro gọi là €STR [[src-choudhry-principles-banking#^choudhry-hedge-15]].
- SONIA swap trao đổi lãi suất cố định (swap rate) lấy trung bình nhân của lãi suất qua đêm ghi nhận trong kỳ hợp đồng. Lãi được trao đổi hằng quý [[src-choudhry-principles-banking#^choudhry-hedge-16]].

## Pricing
Lãi suất cố định của SONIA swap phản ánh mức lãi suất qua đêm bình quân mà thị trường kỳ vọng trong kỳ swap [[src-choudhry-principles-banking#^choudhry-hedge-17]].

## Risk factors & sensitivities
SONIA tương quan chặt với lãi suất cơ bản của Bank of England [[src-choudhry-principles-banking#^choudhry-hedge-17]].

## ALM & hedging usage
- SONIA swap có thể phòng ngừa NII khi khoản vay lãi suất cố định được tài trợ bằng tiền gửi lãi suất biến đổi [[src-choudhry-principles-banking#^choudhry-hedge-17]].
- Tiền gửi bán lẻ và doanh nghiệp thường không gắn chính thức với chỉ số tham chiếu như SONIA, mà được đặt theo lãi suất thị trường và cung cầu [[src-choudhry-principles-banking#^choudhry-hedge-17]].
- **Ví dụ 6.11**: cho vay dài hạn cố định tạo rủi ro NII nếu chi phí tiền gửi tăng. Chi phí này đi theo, nhưng không gắn chính thức với, lãi suất cơ bản của NHTW. Choudhry coi đây là một dạng basis risk, và ngân hàng có thể vào OIS để phòng ngừa [[src-choudhry-principles-banking#^choudhry-hedge-18]]. Xem [[basis-risk]], [[net-interest-income-sensitivity]].

*Diễn giải:* OIS chỉ phòng ngừa phần lãi suất tiền gửi bám theo lãi suất qua đêm. Phần chênh lệch giữa lãi suất tiền gửi administered và lãi suất qua đêm vẫn còn.

## Kế toán
[cần nguồn]

## Basel treatment
[cần nguồn]

## Lưu ý tại VN
[cần nguồn]
