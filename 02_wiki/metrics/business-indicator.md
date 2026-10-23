---
title: "Business Indicator"
aliases: [Business Indicator, BI, Chỉ số kinh doanh]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[business-indicator-component]]", cite: "[[src-tt14-2025-nhnn#^d70-2a]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Chỉ số kinh doanh (Business indicator, BI) là đại lượng quy mô hoạt động làm đầu vào của [[business-indicator-component]] [[src-tt14-2025-nhnn#^d70-2a]]. BI bằng tổng ba cấu phần [[src-tt14-2025-nhnn#^d70-2b]].

## Công thức
$$
BI = ILDC + SC + FC
$$
[[src-tt14-2025-nhnn#^d70-2b]]

| Ký hiệu | Ý nghĩa | Công thức (Phụ lục III) | Node | Nguồn |
|---|---|---|---|---|
| ILDC | Cấu phần lãi | min(\|thu nhập lãi − chi phí lãi\|; 2,25% × tài sản tạo lãi) + thu nhập từ góp vốn, mua cổ phần | [[interest-leases-and-dividend-component]] | [[src-tt14-2025-nhnn#^pl3-1-ildc]] |
| SC | Cấu phần dịch vụ | max(thu nhập, chi phí dịch vụ) + max(thu nhập, chi phí hoạt động khác) | [[services-component]] | [[src-tt14-2025-nhnn#^pl3-1-sc]] |
| FC | Cấu phần tài chính | \|ngoại hối (gồm vàng tiêu chuẩn)\| + \|chứng khoán kinh doanh\| + \|chứng khoán đầu tư\| | [[financial-component]] | [[src-tt14-2025-nhnn#^pl3-1-fc]] |

Mỗi cấu phần (ILDC, SC, FC) là giá trị trung bình của 03 năm gần nhất của các thành phần theo công thức [[src-tt14-2025-nhnn#^d70-2b2]] [[src-tt14-2025-nhnn#^pl3-1-avg]]. Với dữ liệu hằng quý, giá trị theo năm lấy bằng tổng 4 quý liên tiếp, riêng [[interest-earning-assets]] lấy bằng trung bình số dư 4 thời điểm [[src-tt14-2025-nhnn#^pl3-3-ildc1]] [[src-tt14-2025-nhnn#^pl3-3-ildc2]].

## Diễn giải
BI phân ngân hàng vào ba nhóm: không quá 600 tỷ đồng, trên 600 đến 18.000 tỷ đồng, và trên 18.000 tỷ đồng [[src-tt14-2025-nhnn#^d70-2a]]. Ngưỡng 600 tỷ đồng còn quyết định ILM có bằng 1 hay không [[src-tt14-2025-nhnn#^d70-3b]]. Xem [[internal-loss-multiplier]].

**Bốn khoản mục không tính vào bất cứ cấu phần nào của BI** [[src-tt14-2025-nhnn#^pl3-2]]:
- thu nhập và chi phí từ hoạt động kinh doanh bảo hiểm hoặc tái bảo hiểm (TK716);
- phí bảo hiểm đã thanh toán và các khoản bồi hoàn từ hợp đồng bảo hiểm hoặc tái bảo hiểm đã mua (gồm Tài khoản 883 và một phần TK79);
- thay đổi trong lợi thế thương mại đã ghi vào Báo cáo kết quả hoạt động (phần Tài khoản 79 hoặc 89);
- thu nhập từ việc thu hồi chi phí vận hành, gồm thu hồi các khoản thanh toán thay cho khách hàng (phần Tài khoản 79, ứng với thu hồi khoản nộp phạt vi phạm hành chính ngân hàng đã trả thay).

Khi ngân hàng mua lại doanh nghiệp thành công ty con, sáp nhập hoặc hợp nhất, các cấu phần BI phải gồm cả doanh nghiệp đó, kể cả thời gian trước khi mua lại, sáp nhập, hợp nhất [[src-tt14-2025-nhnn#^d72-8]].

*Diễn giải:* ba cấu phần dùng ba cách ghép cặp khác nhau: ILDC lấy trần theo tài sản và giá trị tuyệt đối của lãi thuần, SC lấy max của từng cặp thu nhập và chi phí, FC cộng giá trị tuyệt đối của ba khoản. Hệ quả: cùng một mức lãi/lỗ, ILDC và FC không phân biệt dấu, còn SC chỉ nhận phía lớn hơn.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu phần của BI | [cần nguồn] (OPE chưa ingest) | ILDC + SC + FC, trung bình 03 năm [[src-tt14-2025-nhnn#^d70-2b]] [[src-tt14-2025-nhnn#^d70-2b2]] | Đ70.2b | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Khoản mục chi tiết | [cần nguồn] | Phụ lục III Bảng 24 ([[interest-leases-and-dividend-component]], [[services-component]], [[financial-component]]) [[src-tt14-2025-nhnn#^pl3-1-ildc]] | PL3.1 | Như trên |
| Khoản loại trừ | [cần nguồn] | Bốn nhóm: bảo hiểm, phí bảo hiểm, lợi thế thương mại, thu hồi chi phí vận hành [[src-tt14-2025-nhnn#^pl3-2]] | PL3.2 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* thu nhập và chi phí lãi (qua ILDC) và kết quả ngoại hối, chứng khoán (qua FC) đều đi vào BI bằng giá trị tuyệt đối hoặc theo trần tài sản, nên các quyết định về cấu trúc bảng cân đối và vị thế Treasury có tác động tới $K_{OR}$ theo hai kênh này. Xem [[operational-risk-capital-requirement]].

## Nhầm lẫn thường gặp
- BI là giá trị trung bình 03 năm, không phải số liệu một năm [[src-tt14-2025-nhnn#^d70-2b2]].
- BI không phải vốn. BI qua BIC và ILM mới thành $K_{OR}$ ([[operational-risk-capital-requirement]]).
- Hệ số 2,25% của ILDC có mâu thuẫn nội bộ trong nguồn (2,25% so với "2,25 lần"): xem callout trong [[interest-leases-and-dividend-component]].
