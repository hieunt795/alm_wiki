---
title: "IRB Credit Risk Mitigation"
aliases: [IRB Credit Risk Mitigation, Giảm thiểu rủi ro theo IRB, Bảo lãnh và phái sinh tín dụng trong IRB]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[internal-ratings-based-approach]]", cite: "[[src-tt14-2025-nhnn#^d43-23]]"}
tags: [capital, credit-risk, irb, mitigation, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Đ43–46 và Đ52 TT14/2025 cho khoản phải đòi doanh nghiệp và bán lẻ theo IRB giảm thiểu rủi ro bằng ba biện pháp: tài sản bảo đảm, bảo lãnh của bên thứ ba, sản phẩm phái sinh tín dụng [[src-tt14-2025-nhnn#^d43-23]]. Tài sản bảo đảm làm LGD giảm ([[loss-given-default]]); bảo lãnh và phái sinh tín dụng thay PD, LGD của phần được bảo vệ bằng PD, LGD của bên bảo lãnh hoặc bên phát hành ([[probability-of-default]]) [[src-tt14-2025-nhnn#^d45-3]] [[src-tt14-2025-nhnn#^d46-3]]. Phương pháp tiêu chuẩn tương ứng nằm ở [[credit-risk-mitigation]]. Với bán lẻ, tác động được phản ánh qua điều chỉnh ước tính PD hoặc LGD của chính ngân hàng.

## Cơ chế & drivers
**Nguyên tắc chung (Đ43.3).** Biện pháp phải đáp ứng Đ25.3a–đ. Khi dùng nhiều biện pháp, ngân hàng được phân tách giá trị từng biện pháp theo thỏa thuận và quy định nội bộ để tính riêng LGD, tổng giá trị phân bổ không vượt tổng giá trị biện pháp đủ điều kiện và không vượt EAD từng khoản [[src-tt14-2025-nhnn#^d43-23]].

**Bảo lãnh (Đ45)** [[src-tt14-2025-nhnn#^d45-12]]:
- Điều kiện: đáp ứng Đ28 ([[third-party-guarantee-mitigation]]) và bên bảo lãnh có PD thấp hơn bên được bảo lãnh, trừ khi ngân hàng không dùng IRB cho bên bảo lãnh.
- Nếu không dùng IRB cho bên bảo lãnh: chọn một trong hai cách, tính phương pháp tiêu chuẩn cho khoản được bảo lãnh (gồm cả giảm thiểu theo tiêu chuẩn), hoặc tính IRB nhưng không giảm thiểu bằng bảo lãnh.
- Phần được bảo lãnh dùng PD, LGD của bên bảo lãnh; phần còn lại dùng PD, LGD của bên được bảo lãnh. Nếu bên bảo lãnh có tài sản bảo đảm đủ điều kiện Đ44.1, PD vẫn của bên bảo lãnh, LGD thay bằng LGD theo Đ44.4 [[src-tt14-2025-nhnn#^d45-3]].
- Nhiều bên bảo lãnh: phân tách theo từng bên; không phân tách được thì dùng PD cao nhất [[src-tt14-2025-nhnn#^d45-4]].

$$
G_l^{*} = G_l \times \left( 1 - \frac{PD_{gtor_l}}{PD} \right) \times \frac{t_l - 0{,}25}{T - 0{,}25} \times (1 - H_{fx_l})
$$
[[src-tt14-2025-nhnn#^d45-5]]

$G_l$ là giá trị bảo lãnh của bên bảo lãnh thứ l; $PD_{gtor_l}$ là PD của bên bảo lãnh; $PD$ là PD của bên được bảo lãnh; $T$ là giá trị nhỏ hơn giữa 05 năm và thời hạn còn lại của khoản phải đòi; $t_l$ là giá trị nhỏ hơn giữa $T$ và thời hạn còn lại của bảo lãnh; $H_{fx_l}$ là hệ số độ lệch tiền tệ 8% [[src-tt14-2025-nhnn#^d45-5]].

**Phái sinh tín dụng (Đ46)** [[src-tt14-2025-nhnn#^d46-12]]:
- Điều kiện: đáp ứng Đ29 ([[credit-derivative-mitigation]]) và bên phát hành có PD thấp hơn bên sử dụng, trừ khi ngân hàng không dùng IRB cho bên phát hành; hai cách lựa chọn như bảo lãnh.
- Phần tương ứng $CD^{*}$ dùng PD, LGD của bên phát hành; phần còn lại dùng của bên sử dụng [[src-tt14-2025-nhnn#^d46-3]].
- Nhiều sản phẩm: phân tách theo từng sản phẩm; không phân tách được thì dùng PD cao nhất [[src-tt14-2025-nhnn#^d46-5]].

$$
CD_n^{*} = CD_n \times \frac{t_n - 0{,}25}{T - 0{,}25} \times (1 - H_{fxcd_n})
$$
[[src-tt14-2025-nhnn#^d46-4]]

$H_{fxcd_n}$ là 8% [[src-tt14-2025-nhnn#^d46-4]].

**Bán lẻ (Đ52).** Ngân hàng tự điều chỉnh PD hoặc LGD thay vì thay bằng PD, LGD bên bảo lãnh, với ba điều kiện: một phương pháp thống nhất cho cùng loại hình, không tính ảnh hưởng vỡ nợ kép, và PD hoặc LGD sau điều chỉnh không thấp hơn của bên bảo lãnh hoặc bên bán phái sinh [[src-tt14-2025-nhnn#^d52-1]]. Yêu cầu tối thiểu: bảo lãnh đáp ứng Đ45.1, bên bảo lãnh được xếp hạng lúc cấp tín dụng và định kỳ, theo dõi thường xuyên; phái sinh tín dụng đáp ứng Đ46.1, có tiêu chí cho bảo hiểm một phần và lệch đồng tiền, đánh giá thận trọng cơ cấu thanh toán [[src-tt14-2025-nhnn#^d52-2]].

## Phụ thuộc regime
Đ43–46 áp dụng cho khoản phải đòi doanh nghiệp theo IRB cơ bản; Đ52 cho bán lẻ theo IRB nâng cao.

## Góc nhìn theo domain
**VN Regulator.** Các hệ số $(t - 0{,}25)/(T - 0{,}25)$ và độ lệch tiền tệ 8% dùng cùng cấu trúc với phương pháp tiêu chuẩn. Bảo lãnh được hiệu chỉnh thêm hệ số $1 - PD_{gtor}/PD$, tức giá trị bảo lãnh giảm khi PD bên bảo lãnh gần PD bên được bảo lãnh [[src-tt14-2025-nhnn#^d45-5]].

**Basel.** [cần nguồn] (CRE32 chưa ingest).

**ALM.** *Diễn giải:* bảo lãnh của bên có PD thấp (ví dụ tổ chức tín dụng) giảm PD và LGD của phần bảo vệ nhưng chỉ khi kỳ hạn bảo lãnh đủ dài so với khoản vay (hệ số kỳ hạn) và PD bên bảo lãnh thấp hơn. Bảo lãnh ngắn hơn khoản vay bị chiết khấu theo $(t_l - 0{,}25)/(T - 0{,}25)$.

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Tham số Đ25.3a–đ và Đ44.1c(ii) về quy trình định giá tài sản bảo đảm: đã ingest ở C2-M4, nhưng cách áp dụng IRB cho nhiều biện pháp giảm thiểu trên cùng một khoản chưa có ví dụ số trong nguồn.
