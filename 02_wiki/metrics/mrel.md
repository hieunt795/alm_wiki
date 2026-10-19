---
title: "MREL"
aliases: [MREL, Minimum Requirement for Own Funds and Eligible Liabilities, Yêu cầu tối thiểu về vốn tự có và nợ đủ điều kiện]
type: metric
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[recovery-and-resolution-planning]]", cite: "[[src-bardaeva-alm#^ch14-6]]"}
tags: [resolution, capital, funding]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
MREL (Minimum Requirement for Own Funds and Eligible Liabilities) là yêu cầu về vốn tự có và nợ đủ điều kiện mà ngân hàng phải giữ để có đủ năng lực hấp thụ lỗ và tái cấp vốn trong kịch bản resolution [[src-bardaeva-alm#^ch14-6]]. Ngân hàng nhận MREL target sau khi cơ quan xử lý xác định chiến lược xử lý; ngân hàng được thanh lý thông thường thì không có yêu cầu MREL bổ sung ngoài vốn tự có [[src-bardaeva-alm#^ch16-8]].

## Công thức
Theo logic SRB cập nhật 2020 [[src-bardaeva-alm#^ch16-8]]:

$$MREL = LAA + RCA + MCC$$
[[src-bardaeva-alm#^ch16-8]]

| Cấu phần | Nội dung | Nguồn |
|---|---|---|
| LAA (loss absorbency amount) | Yêu cầu vốn trong kịch bản căng thẳng, gồm P1 + P2R | [[src-bardaeva-alm#^ch16-8]] |
| RCA (recapitalisation amount) | Yêu cầu P1 + P2R trong điều kiện căng thẳng, sau khi vốn ban đầu bị lỗ tiêu hết | [[src-bardaeva-alm#^ch16-8]] |
| MCC (market confidence charge) | CBR trừ phần dùng để đáp ứng CCyB | [[src-bardaeva-alm#^ch16-8]] |

**Điều kiện cơ bản của nợ đủ chuẩn MREL** [[src-bardaeva-alm#^ch16-9]]:
- kỳ hạn còn lại trên một năm;
- không phải tiền gửi (bán lẻ) được bảo hiểm tiền gửi (DGS);
- không phải nợ với cơ quan nhà nước hay bảo hiểm xã hội;
- không do chính ngân hàng mua lại.

## Diễn giải
*Diễn giải:* LAA và RCA đều dựa trên P1 + P2R, nên MREL tăng theo P2R mà ngân hàng nhận qua [[srep]]. MCC gắn với combined buffer, nên MREL cũng đổi khi CBR đổi.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Yêu cầu nợ hấp thụ lỗ khi xử lý | [cần nguồn] (MREL là khung EU theo Bardaeva) | [cần nguồn] | | |

## Ứng dụng trong ALM
- Khi add-on resolution vượt thặng dư vốn, ALM chịu trách nhiệm huy động nguồn đủ chuẩn MREL và duy trì qua chu kỳ [[src-bardaeva-alm#^ch16-9]].
- Công cụ T2 bị khấu trừ dần 20% mỗi năm khỏi vốn khi kỳ hạn còn lại dưới 5 năm [[src-bardaeva-alm#^ch12-6]]; khả năng phần bị khấu trừ vẫn tính vào MREL chưa được trích [cần nguồn].
- Choudhry liệt kê các điểm cần xét trong cấu trúc funding: MREL cao hơn tỷ lệ vốn, CoCos ([[contingent-convertible-bond]]), nơi đặt nợ (single hay multiple point of entry), tác động xếp hạng; quỹ xử lý EU hỗ trợ sau khi 8% tổng nợ đã bị bail-in [[src-choudhry-principles-banking#^choudhry-rrp-16]]. Xem [[bail-in]].

## Nhầm lẫn thường gặp
- Quan hệ giữa MREL (EU) và TLAC của FSB chưa có nguồn trong wiki [cần nguồn].
