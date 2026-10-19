---
title: "Interest Rate Futures"
aliases: [Interest Rate Futures, Short-term interest-rate futures, STIR futures, Hợp đồng tương lai lãi suất, Strip hedge]
type: instrument
domains: [product, alm]
status: active
maturity: draft
sources: ["[[src-choudhry-principles-banking]]"]
relations:
  - {type: hedges, to: "[[gap-risk]]", cite: "[[src-choudhry-principles-banking#^choudhry-hedge-4]]"}
  - {type: exposed-to, to: "[[basis-risk]]", cite: "[[src-choudhry-principles-banking#^choudhry-hedge-7]]"}
tags: [futures, stir, bond-futures, strip-hedge, hedging, irrbb]
updated: 2026-10-19
reviewed:
---

## Định nghĩa & cashflow
Short-term interest-rate futures cố định lãi suất trên một khoản tiền gửi danh nghĩa, kỳ hạn cố định, cho một kỳ trong tương lai. Đây là công cụ ngoại bảng: không có khoản tiền thực tế được gửi khi mua hoặc bán hợp đồng [[src-choudhry-principles-banking#^choudhry-hedge-5]].

- Mua hợp đồng tương đương gửi tiền danh nghĩa; bán hợp đồng tương đương vay danh nghĩa [[src-choudhry-principles-banking#^choudhry-hedge-5]].
- Hợp đồng điển hình: short sterling 90 ngày (LIFFE) cho GBP, Eurodollar cho USD, Euribor cho EUR [[src-choudhry-principles-banking#^choudhry-hedge-4]].
- Short-term interest-rate futures chỉ thanh toán tiền mặt. Bond futures giao vật chất trái phiếu [[src-choudhry-principles-banking#^choudhry-hedge-26]].

## Pricing
[cần nguồn] Công thức lãi suất ngụ ý từ giá futures trong nguồn đã ingest bị mất khi convert.

## Risk factors & sensitivities
- **Basis risk**: basis là chênh lệch giữa giá tiền mặt và giá futures. Basis risk là rủi ro basis thay đổi không dự đoán được [[src-choudhry-principles-banking#^choudhry-hedge-27]]. Xem [[basis-risk]].
- Trong strip hedge, dealer vẫn chịu basis risk khi mua lại hợp đồng kỳ sau lúc hợp đồng kỳ trước đáo hạn [[src-choudhry-principles-banking#^choudhry-hedge-7]].

## ALM & hedging usage
- **Gap kỳ hạn tương lai**: forward-term interest-rate gap có thể phòng ngừa bằng interest-rate futures. Strip futures dùng cho cả kỳ gap [[src-choudhry-principles-banking#^choudhry-hedge-4]]. Xem [[gap-risk]].
- **Ví dụ 6.8 (strip hedge)**:
  - nhu cầu vay 6 tháng GBP 30 triệu cần 60 hợp đồng, mỗi hợp đồng GBP 500.000 cho kỳ danh nghĩa 3 tháng [[src-choudhry-principles-banking#^choudhry-hedge-6]];
  - dealer bán 30 hợp đồng tháng 9 và 30 hợp đồng tháng 12 [[src-choudhry-principles-banking#^choudhry-hedge-6]];
  - lãi suất vay thực đạt 6,5325%, gần strip rate mục tiêu 6,53% [[src-choudhry-principles-banking#^choudhry-hedge-7]].
- **Bond futures**: ALM desk dùng government bond futures để phòng ngừa IRR của danh mục trái phiếu, hiếm khi cho danh mục cho vay. Bond futures dùng cho phơi nhiễm lãi suất dài hạn [[src-choudhry-principles-banking#^choudhry-hedge-26]].
- FRA, futures và swap trong phần lớn trường hợp là đủ để phòng ngừa rủi ro lãi suất [[src-choudhry-principles-banking#^choudhry-hedge-19]]. Xem [[forward-rate-agreement]], [[interest-rate-swap]].

*Diễn giải:* futures là hợp đồng chuẩn hoá trên sàn nên khó khớp đúng kỳ gap của sổ ngân hàng. Vì vậy basis risk khi roll hợp đồng là chi phí của tính thanh khoản cao.

## Kế toán
[cần nguồn]

## Basel treatment
[cần nguồn]

## Lưu ý tại VN
[cần nguồn]
