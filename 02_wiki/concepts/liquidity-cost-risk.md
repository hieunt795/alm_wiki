---
title: "Liquidity cost risk"
aliases: [Liquidity Cost Risk, Funding Cost Risk, Rủi ro chi phí thanh khoản, Rủi ro chi phí funding, Liquidity VaR]
type: concept
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-lubinska-alm-optimisation]]", "[[src-tt83-2025-nhnn]]"]
relations: []
tags: [liquidity-cost-risk, funding-spread, icaap, ilaap, liquidity-var, concept]
updated: 2026-10-21
reviewed:
---

## Ý chính

- Liquidity cost risk là rủi ro chi phí thanh khoản tăng mà ngân hàng không mất khả năng thanh toán. Lubinska xếp đây là rủi ro thị trường tương tự rủi ro lãi suất: chi phí thanh khoản tăng làm giảm vốn (lợi nhuận) qua chi phí tái tài trợ tăng [[src-lubinska-alm-optimisation#^lubinska-u01-19]].
- Trong danh sách rủi ro do ALM quản lý, Lubinska định nghĩa liquidity cost risk là rủi ro giảm thu nhập lãi (hoặc giá trị mark to market) do chi phí thanh khoản (funding spread) tăng [[src-lubinska-alm-optimisation#^lubinska-u01-9]].
- Liquidity cost risk khác liquidity risk (refinancing risk). Liquidity risk là thiếu nguồn tái tài trợ để đáp ứng nghĩa vụ, phát sinh từ maturity transformation [[src-lubinska-alm-optimisation#^lubinska-u01-21]]. Xem [[liquidity-risk-management]].

## Cơ chế & drivers

- **Nguồn phát sinh**: các gap âm tích luỹ trên maturity ladder phải được tái tài trợ; khi liquidity spread tăng, chi phí tái tài trợ tăng [[src-lubinska-alm-optimisation#^lubinska-u01-20]].
- **Cách đo**: refinance các gap âm tích luỹ với giả định liquidity spread tăng. Cơ sở cho mức spread có thể là biến động credit spread theo holding period. Cách khác là Liquidity VaR, có xét biến động và tương quan của spread [[src-lubinska-alm-optimisation#^lubinska-u01-20]].
- **Ba góc nhìn đo**: going concern, gone concern và stress, do cơ quan quản lý định trong Trụ cột 2 của ICAAP [[src-lubinska-alm-optimisation#^lubinska-u01-20]].
- **Ví dụ margin at risk**: trong ví dụ của Lubinska, margin ALM locked-in từ phần thanh khoản là 0,25% (chênh lệch liquidity spread của tài sản và nợ). Margin at risk phụ thuộc liquidity spread mới khi nợ đến hạn phải roll over [[src-lubinska-alm-optimisation#^lubinska-u01-4]].

*Diễn giải:* liquidity cost risk là phía rủi ro của [[liquidity-transfer-pricing]]. Liquidity FTP chuyển chi phí thanh khoản theo kỳ hạn về BU tại thời điểm giao dịch. Phần gap mà ALM giữ lại sau FTP vẫn chịu biến động của funding spread khi tái tài trợ.

## Phụ thuộc regime

- Đo theo ba góc nhìn going concern, gone concern và stress [[src-lubinska-alm-optimisation#^lubinska-u01-20]]. Nguồn chưa nêu tham số stress cụ thể [cần nguồn].

## Góc nhìn theo domain

- **ALM**: Lubinska xếp liquidity cost risk vào nhóm rủi ro ALM quản lý, cùng IRRBB, liquidity risk, FX risk và [[csrbb]] [[src-lubinska-alm-optimisation#^lubinska-u01-9]].

> [!conflict] ICAAP hay ILAAP
> Cùng nguồn, cùng Ch1, hai đoạn xếp rủi ro này vào hai quy trình khác nhau.
> - Dòng 306: liquidity risk và funding cost risk thuộc ILAAP; IRRBB, CSRBB, FX thuộc ICAAP [[src-lubinska-alm-optimisation#^lubinska-u01-9]].
> - Dòng 429: liquidity cost risk là một phần của ICAAP, phải được đo và giới hạn để bảo toàn vốn [[src-lubinska-alm-optimisation#^lubinska-u01-20]].
>
> *Diễn giải:* hai đoạn có thể nhìn cùng rủi ro từ hai phía: ILAAP quản lý thanh khoản và funding, còn ICAAP lượng hoá tác động lên vốn. Wiki chưa có nguồn quy định (EBA, PRA, NHNN) xác định rủi ro này thuộc quy trình nào [cần nguồn]. Xem [[icaap]], [[ilaap]].

## Bằng chứng thực nghiệm

*Chưa có nguồn số liệu.*

## Câu hỏi mở

- TT83/2025 có yêu cầu đo chi phí thanh khoản tăng như một rủi ro riêng không? Wiki mới có yêu cầu đưa chi phí thanh khoản vào định giá vốn nội bộ [[src-tt83-2025-nhnn#^d45-1b]] [cần nguồn cho phần đo rủi ro].
