---
title: "On-Balance-Sheet Netting"
aliases: [On-Balance-Sheet Netting, Bù trừ số dư nội bảng]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[credit-risk-mitigation]]", cite: "[[src-tt14-2025-nhnn#^d25-2]]"}
tags: [capital, credit-risk, netting, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Bù trừ số dư nội bảng là việc ngân hàng điều chỉnh giảm giá trị khoản phải đòi của khách hàng theo số dư tiền gửi của chính khách hàng đó tại ngân hàng, khi tính tổng tài sản có rủi ro tín dụng [[src-tt14-2025-nhnn#^d27-1]]. Giá trị tiền gửi hiệu chỉnh $L^{*}$ là đầu vào của $E_k$ trong công thức $E_i^{*}$ ([[credit-risk-mitigation]]) [[src-tt14-2025-nhnn#^d25-4-h]].

## Cơ chế & drivers
**Bốn điều kiện (Đ27.1)** [[src-tt14-2025-nhnn#^d27-1]]:
- có đầy đủ hồ sơ pháp lý về thỏa thuận bù trừ số dư khoản phải đòi và tiền gửi, kể cả khi khách hàng mất khả năng thanh toán hoặc phá sản; thỏa thuận phù hợp với pháp luật dân sự và pháp luật liên quan;
- xác định được số dư khoản phải đòi và số dư tiền gửi của từng khách hàng theo thỏa thuận tại mọi thời điểm;
- theo dõi và kiểm soát được việc đáo hạn của số dư tiền gửi;
- theo dõi và kiểm soát được số dư bù trừ giữa các khoản phải đòi và tiền gửi của khách hàng đó.

**Độ lệch thời hạn (Đ27.2).** $L^{*} = L \times (t - 0{,}25) / (T - 0{,}25)$. L là số dư tiền gửi của khách hàng; T là giá trị nhỏ hơn giữa 05 năm và thời hạn còn lại của khoản phải đòi, giao dịch (năm); t là giá trị nhỏ hơn giữa T và thời hạn còn lại của nợ phải trả nội bảng (năm) [[src-tt14-2025-nhnn#^d27-2]].

**Độ lệch tiền tệ (Đ27.3).** Hệ số hiệu chỉnh $H_{fxl}$ bằng 8% [[src-tt14-2025-nhnn#^d27-2]].

Phần giảm thiểu trong $E_i^{*}$ là $\max\{0;\ E_k - \sum L_k^{*}(1 - H_{fxl,k})\}$ [[src-tt14-2025-nhnn#^d25-4]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]]. Khác với bù trừ hai bên của giao dịch phái sinh và repo ([[bilateral-netting]]).

## Góc nhìn theo domain
**VN Regulator.** Bù trừ nội bảng chỉ áp dụng với tiền gửi của chính khách hàng có khoản phải đòi tại chính ngân hàng [[src-tt14-2025-nhnn#^d27-1]].

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* tiền gửi không kỳ hạn của khách hàng khó đáp ứng điều kiện theo dõi đáo hạn của Đ27.1c và hệ số thời hạn (t − 0,25) / (T − 0,25), nên giá trị giảm thiểu thực tế nhỏ hơn số dư. Ngân hàng cần hệ thống liên kết khoản vay với tiền gửi của cùng khách hàng theo thỏa thuận bù trừ. Nguồn không nêu xử lý tiền gửi không kỳ hạn [cần nguồn].

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Cách xác định t với tiền gửi không kỳ hạn: nguồn không nêu [cần nguồn].
