---
title: "Operational Risk Capital Requirement"
aliases: [Operational Risk Capital Requirement, K_OR, KOR, Vốn yêu cầu cho rủi ro hoạt động]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[capital-adequacy-ratio]]", cite: "[[src-tt14-2025-nhnn#^d5-1d]]"}
tags: [capital, operational-risk, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho rủi ro hoạt động ($K_{OR}$) là cấu phần của mẫu số tỷ lệ an toàn vốn, nhân 12,5 cùng với $K_{MR}$ [[src-tt14-2025-nhnn#^d5-1d]]. Xem [[capital-adequacy-ratio]]. $K_{OR}$ bằng tích của [[business-indicator-component]] (BIC) và [[internal-loss-multiplier]] (ILM) [[src-tt14-2025-nhnn#^d70-1]].

Rủi ro hoạt động theo TT14/2025 là rủi ro do quy trình nội bộ không đầy đủ hoặc có sai sót, do con người, do lỗi hoặc sự cố hệ thống, hoặc do yếu tố bên ngoài gây tổn thất tài chính hoặc tác động tiêu cực phi tài chính (gồm rủi ro pháp lý). Rủi ro danh tiếng và rủi ro chiến lược không thuộc rủi ro hoạt động [[src-tt14-2025-nhnn#^d2-20]].

## Công thức
$$
K_{OR} = BIC \times ILM
$$
[[src-tt14-2025-nhnn#^d70-1]]

| Ký hiệu | Ý nghĩa | Node | Nguồn |
|---|---|---|---|
| $K_{OR}$ | Vốn yêu cầu cho rủi ro hoạt động | node này | [[src-tt14-2025-nhnn#^d70-1]] |
| BIC | Cấu phần chỉ số kinh doanh (Business indicator component) | [[business-indicator-component]] | [[src-tt14-2025-nhnn#^d70-1]] |
| ILM | Hệ số tổn thất nội bộ (Internal loss multiplier) | [[internal-loss-multiplier]] | [[src-tt14-2025-nhnn#^d70-1]] |
| BI | Chỉ số kinh doanh, đầu vào của BIC; gồm [[interest-leases-and-dividend-component]], [[services-component]], [[financial-component]] | [[business-indicator]] | [[src-tt14-2025-nhnn#^d70-2b]] |
| LC | Cấu phần tổn thất, đầu vào của ILM | [[loss-component]] | [[src-tt14-2025-nhnn#^d70-3a]] |

## Diễn giải
**Hai nhánh.** Nhánh quy mô đi từ BI qua BIC và không cần dữ liệu tổn thất. Nhánh tổn thất đi từ [[operational-loss-data]] qua LC vào ILM. ILM bằng 1 khi BI không quá 600 tỷ đồng, hoặc khi BI trên 600 tỷ đồng mà chuỗi dữ liệu tổn thất chưa đủ 05 năm [[src-tt14-2025-nhnn#^d70-3b]]. Trong hai trường hợp đó, $K_{OR}$ bằng BIC.

**Hợp nhất.** Ngân hàng thương mại có công ty con được dùng LC tính trên dữ liệu tổn thất riêng lẻ (không gồm công ty con) khi tính tỷ lệ an toàn vốn hợp nhất [[src-tt14-2025-nhnn#^d70-3c4]]. Khi ngân hàng mua lại doanh nghiệp thành công ty con, sáp nhập hoặc hợp nhất, phạm vi tổn thất và các cấu phần BI phải gồm các doanh nghiệp đó, kể cả thời gian trước khi mua lại, sáp nhập, hợp nhất [[src-tt14-2025-nhnn#^d72-8]].

*Diễn giải:* nếu ILM bằng 1 và BI là 20.000 tỷ đồng thì $K_{OR}$ = BIC = 3.042 tỷ đồng theo ví dụ của nguồn [[src-tt14-2025-nhnn#^d70-2a-vd]], và cấu phần đóng góp vào mẫu số CAR là 12,5 × 3.042 = 38.025 tỷ đồng [[src-tt14-2025-nhnn#^d5-1d]]. Đây là phép nhân của wiki, nguồn không nêu ví dụ cho $K_{OR}$.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Công thức | [cần nguồn] (OPE chưa ingest) | $K_{OR}$ = BIC × ILM [[src-tt14-2025-nhnn#^d70-1]] | Đ70.1 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Hệ số biên BIC | [cần nguồn] | 12% / 15% / 18% ([[business-indicator-component]]) | Đ70.2a | Như trên |
| ILM bằng 1 | [cần nguồn] | BI ≤ 600 tỷ đồng, hoặc BI > 600 tỷ đồng và chuỗi tổn thất dưới 05 năm [[src-tt14-2025-nhnn#^d70-3b]] | Đ70.3b | Như trên |
| Hệ số LC | [cần nguồn] | 15 lần tổn thất ròng bình quân năm [[src-tt14-2025-nhnn#^d70-3c5]] | Đ70.3c(v) | Như trên |
| Ngưỡng thu thập tổn thất | [cần nguồn] | 12 triệu đồng [[src-tt14-2025-nhnn#^d71-1]] | Đ71.1 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* $K_{OR}$ không phụ thuộc cấu trúc kỳ hạn hay lãi suất của bảng cân đối. BI gồm cấu phần lãi (ILDC), tính từ giá trị tuyệt đối của lãi thuần với trần theo tài sản tạo lãi, nên thay đổi cấu trúc thu nhập lãi tác động tới BI và BIC [[src-tt14-2025-nhnn#^pl3-1-ildc]]. Kết quả ngoại hối và chứng khoán đi vào FC bằng giá trị tuyệt đối [[src-tt14-2025-nhnn#^pl3-1-fc]]. ALM và Treasury cần đưa $K_{OR}$ vào [[capital-plan]] như một cấu phần của mẫu số, cùng $K_{MR}$ ([[market-risk-capital-requirement]]). Quản trị rủi ro hoạt động theo TT83/2025 xem [[operational-risk-management]].

## Nhầm lẫn thường gặp
- ILM không bằng 1 trong mọi trường hợp. Chỉ khi BI không quá 600 tỷ đồng, hoặc chuỗi dữ liệu tổn thất chưa đủ 05 năm, ILM mới được đặt bằng 1 [[src-tt14-2025-nhnn#^d70-3b]].
- Rủi ro hoạt động không gồm rủi ro danh tiếng và rủi ro chiến lược [[src-tt14-2025-nhnn#^d2-20]]. Xem [[reputational-risk]].
