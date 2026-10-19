---
title: "Bail-in"
aliases: [Bail-in, Bail in, Creditor bail-in, Cơ chế bail-in]
type: concept
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]", "[[src-bardaeva-alm]]"]
relations:
  - {type: part-of, to: "[[recovery-and-resolution-planning]]", cite: "[[src-bardaeva-alm#^ch14-5]]"}
tags: [resolution, capital, brrd, loss-absorbency]
updated: 2026-10-19
reviewed:
---

## Ý chính
Bail-in là công cụ resolution buộc chủ sở hữu và chủ nợ không có bảo đảm gánh lỗ trước, theo thứ tự ưu tiên vốn truyền thống. Các khoản này bị ghi giảm hoặc chuyển thành vốn để tái cấp vốn cho ngân hàng [[src-choudhry-principles-banking#^choudhry-rrp-14]]. Theo BRRD, bail-in dùng để bù lỗ hoặc chuyển nợ đủ điều kiện thành vốn, và tổ chức tiếp tục hoạt động [[src-bardaeva-alm#^ch14-5]].

## Cơ chế & drivers

### Hai pha: hấp thụ lỗ và tái cấp vốn
Ví dụ số Figure 21.3 của Choudhry [[src-choudhry-principles-banking#^choudhry-rrp-15]]:

| Pha | Diễn biến | Nguồn |
|---|---|---|
| Lỗ | Ngân hàng lỗ £10, không còn vốn đỡ tài sản | [[src-choudhry-principles-banking#^choudhry-rrp-15]] |
| Hấp thụ lỗ | Xoá vốn £9 và £1 sub-debt | [[src-choudhry-principles-banking#^choudhry-rrp-15]] |
| Tái cấp vốn | Chuyển £2 sub-debt còn lại và £7 senior debt thành vốn | [[src-choudhry-principles-banking#^choudhry-rrp-15]] |
| Sau bail-in | Bảng cân đối £90, vốn £9; người gửi tiền được bảo hiểm không bị ảnh hưởng | [[src-choudhry-principles-banking#^choudhry-rrp-15]] |

*Diễn giải:* hai pha tương ứng với hai cấu phần của [[mrel]]: loss absorption amount và recapitalisation amount.

### Loại trừ
Cơ quan xử lý có thể loại một số khoản nợ khỏi bail-in; phần lớn đã chọn loại trừ tiền gửi bán lẻ [[src-choudhry-principles-banking#^choudhry-rrp-14]].

### Nguyên tắc bảo vệ
FSB Key Attributes (2011) yêu cầu tôn trọng thứ tự chủ nợ và nguyên tắc "no creditor worse off" [[src-choudhry-principles-banking#^choudhry-rrp-7]]. Bail-in nằm trong danh sách quyền của cơ quan xử lý [[src-choudhry-principles-banking#^choudhry-rrp-6]].

## Phụ thuộc regime
| Đặc điểm | EU | US | Nguồn |
|---|---|---|---|
| Văn bản | BRRD (7/2014); bail-in áp dụng từ 1/2016 | Dodd-Frank Title I, II (7/2011) | [[src-choudhry-principles-banking#^choudhry-rrp-11]] |
| Quỹ xử lý hỗ trợ khi | sau khi 8% tổng nợ đã bị bail-in | sau khi 10% tài sản hợp nhất bị xoá | [[src-choudhry-principles-banking#^choudhry-rrp-16]] |
| Quỹ xử lý dùng cho | bù lỗ sau nợ bail-in, thanh khoản và tái cấp vốn | tài trợ bridge company, không tái cấp vốn | [[src-choudhry-principles-banking#^choudhry-rrp-11]] |
| Point of entry | Single hoặc Multiple | ưu tiên Single | [[src-choudhry-principles-banking#^choudhry-rrp-12]] [[src-choudhry-principles-banking#^choudhry-rrp-13]] |

## Góc nhìn theo domain
- **ALM / Treasury**: cấu trúc funding cần xét CoCos ([[contingent-convertible-bond]]), nơi đặt nợ (single hay multiple point of entry), MREL cao hơn tỷ lệ vốn và tác động xếp hạng của nơi đặt nợ [[src-choudhry-principles-banking#^choudhry-rrp-16]]. Ngân hàng nên có bail-in playbook [[src-bardaeva-alm#^ch14-6]]. Xem [[mrel]].
- **VN**: wiki chưa có nguồn NHNN về bail-in [cần nguồn].

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Figure 21.2 (creditor waterfall) và Figure 21.3 chỉ có dạng ảnh; bảng trên dựng từ lời văn của nguồn.
- Chưa có văn bản gốc BRRD hay FSB Key Attributes trong wiki.
