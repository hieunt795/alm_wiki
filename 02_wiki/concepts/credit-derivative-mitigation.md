---
title: "Credit Derivative Mitigation"
aliases: [Credit Derivative Mitigation, Giảm thiểu rủi ro bằng phái sinh tín dụng, Sản phẩm phái sinh tín dụng]
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
tags: [capital, credit-risk, credit-derivative, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ29 TT14/2025 cho phép giảm giá trị khoản phải đòi bằng sản phẩm phái sinh tín dụng khi đáp ứng các điều kiện về sự kiện tín dụng, nghĩa vụ tham chiếu, thời hạn và thông báo [[src-tt14-2025-nhnn#^d29-1a]] [[src-tt14-2025-nhnn#^d29-1bd]]. Ngân hàng đồng thời phải tính rủi ro tín dụng đối tác với bên phát hành phái sinh [[src-tt14-2025-nhnn#^d29-2]]. Xem [[credit-risk-mitigation]].

## Cơ chế & drivers
**Sự kiện tín dụng tối thiểu (Đ29.1a)** [[src-tt14-2025-nhnn#^d29-1a]]:
- khách hàng không thực hiện đúng hạn nghĩa vụ đã cam kết, sản phẩm phái sinh tín dụng có hiệu lực tại thời điểm xảy ra sự kiện, thời gian ân hạn phù hợp với nghĩa vụ cơ sở;
- khách hàng bị phá sản, không thực hiện hoặc không có khả năng thực hiện nghĩa vụ khi đến hạn, và các trường hợp tương tự;
- khách hàng phải cơ cấu lại nghĩa vụ (kể cả miễn, giảm lãi).

**Điều kiện khác (Đ29.1b–d)** [[src-tt14-2025-nhnn#^d29-1bd]]:
- không có khác biệt giữa nghĩa vụ cơ sở của khách hàng, đối tác và nghĩa vụ tham chiếu của sản phẩm phái sinh tín dụng;
- sản phẩm không kết thúc trước thời gian ân hạn của nghĩa vụ cơ sở;
- có quy định cụ thể về căn cứ và trách nhiệm xác định sự kiện; bên được bảo vệ có quyền hoặc khả năng thông báo cho bên bảo vệ khi sự kiện xảy ra.

**Rủi ro đối tác.** Phần được giảm thiểu bằng phái sinh tín dụng phải tính rủi ro tín dụng đối tác theo Đ8.4 đối với bên phát hành [[src-tt14-2025-nhnn#^d29-2]]. Xem [[counterparty-credit-risk-rwa]].

**Độ lệch thời hạn (Đ29.3).** $CD^{*} = CD \times (t - 0{,}25) / (T - 0{,}25)$; CD là giá trị sản phẩm phái sinh tín dụng; T là giá trị nhỏ hơn giữa 05 năm và thời hạn còn lại của khoản phải đòi, giao dịch; t là giá trị nhỏ hơn giữa T và thời hạn còn lại của nợ phải trả nội bảng [[src-tt14-2025-nhnn#^d29-3]].

**Độ lệch tiền tệ (Đ29.4).** Hệ số $H_{fxcd}$ bằng 8% [[src-tt14-2025-nhnn#^d29-3]].

Phần giảm thiểu trong $E_i^{*}$ là $\max\{0;\ E_n - \sum CD_n^{*}(1 - H_{fxcd,n})\}$ [[src-tt14-2025-nhnn#^d25-4]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Đ29.3 xác định t theo thời hạn còn lại của "nợ phải trả nội bảng", cùng chữ với Đ27.2; với phái sinh tín dụng, chữ này có vẻ chép từ Đ27 và có thể phải là thời hạn còn lại của sản phẩm phái sinh [cần nguồn] [[src-tt14-2025-nhnn#^d29-3]]. Wiki giữ nguyên chữ của nguồn.

**Basel.** [cần nguồn] (CRE chưa ingest).

**ALM.** *Diễn giải:* mua bảo hiểm tín dụng (CDS) để giảm RWA chỉ có hiệu lực nếu sản phẩm đáp ứng đủ các điều kiện sự kiện tín dụng, kể cả sự kiện cơ cấu lại nghĩa vụ. Sản phẩm không có sự kiện cơ cấu lại không đủ điều kiện. Phần bảo vệ lại tạo nghĩa vụ đối tác với bên bán bảo vệ, tính theo PL2 với chỉ số tăng thêm 5% hoặc 10% ([[add-on-factor]]).

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Ý nghĩa của t trong Đ29.3: thời hạn còn lại của nợ phải trả nội bảng hay của sản phẩm phái sinh tín dụng? Cần đối chiếu bản gốc [cần nguồn].
