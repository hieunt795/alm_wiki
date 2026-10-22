---
title: "Net Interest Margin (NIM)"
aliases: [Net Interest Margin, NIM, Biên lãi ròng, Tỷ lệ thu nhập lãi cận biên]
type: metric
domains: [alm, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [nim, nii, profitability, interest-earning-assets, balance-sheet-mix]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
Net interest margin (NIM) là NII chia một thước đo tài sản bình quân [[src-choudhry-principles-banking#^choudhry-nim-14]]. Trong case study ChoudWest, NIM bằng NII chia tài sản sinh lãi (interest earning assets) [[src-choudhry-principles-banking#^choudhry-nim-2]]. Ở Ví dụ 6.12, Choudhry định nghĩa NIM là chênh lệch thu nhập lãi và chi phí lãi, tính theo phần trăm tài sản sinh lời bình quân [[src-choudhry-principles-banking#^choudhry-hedge-21]].

## Công thức
$$
\text{NIM} = \frac{\text{NII}}{\text{Interest earning assets}} = \frac{\text{Thu nhập lãi} - \text{Chi phí lãi}}{\text{Tài sản sinh lãi}}
$$
[[src-choudhry-principles-banking#^choudhry-nim-2]]

- Tài sản sinh lãi gồm mọi tài sản có khả năng sinh lãi. Nợ xấu ròng dự phòng vẫn được tính vào, vì loại trừ tài sản không sinh lời sẽ không phản ánh đúng khả năng sinh lời [[src-choudhry-principles-banking#^choudhry-nim-2]].
- Ví dụ cơ sở ChoudWest: NII £461,0m, tài sản sinh lãi £16,0bn, NIM 2,88% [[src-choudhry-principles-banking#^choudhry-nim-2]].

## Diễn giải
**NII và NIM có thể đi ngược chiều.** NII đo thu nhập tuyệt đối, NIM đo khả năng sinh lời trên tài sản. Case study ChoudWest (lãi suất cơ sở 5%, bảng cân đối không đổi, không có FTP, đường cong phẳng) [[src-choudhry-principles-banking#^choudhry-nim-1]]:

| Kịch bản | NII | NIM | Nguồn |
|---|---|---|---|
| Cơ sở | £461,0m | 2,88% | [[src-choudhry-principles-banking#^choudhry-nim-2]] |
| 1. Lãi suất +3% | £525,7m (+£64,7m) | 3,29% | [[src-choudhry-principles-banking#^choudhry-nim-4]] |
| 2. Tăng liquidity buffer £1,5bn | £416m (−£45m) | 2,38% | [[src-choudhry-principles-banking#^choudhry-nim-5]] |
| 3. Lãi suất giảm xuống 4% | £431,5m (−£29,5m) | 2,70% | [[src-choudhry-principles-banking#^choudhry-nim-6]] |
| 4. Thẻ 0% và relaunch tiền gửi rút ngay | £430,0m (−£31,0m) | 2,61% | [[src-choudhry-principles-banking#^choudhry-nim-7]] |
| 5. Tăng trưởng mortgage | £470,5m (+£9,5m) | 2,69% | [[src-choudhry-principles-banking#^choudhry-nim-8]] |

Ở kịch bản 5, NII tăng nhưng NIM giảm, vì nghiệp vụ mới kém sinh lời hơn nghiệp vụ hiện có [[src-choudhry-principles-banking#^choudhry-nim-8]]. NII và NIM chịu tác động của cả biến động lãi suất và thay đổi cơ cấu bảng cân đối [[src-choudhry-principles-banking#^choudhry-nim-9]].

*Diễn giải:* kịch bản 2 cho thấy chi phí của việc giảm rủi ro thanh khoản. Tài sản tăng làm mẫu số NIM lớn hơn, đồng thời net cost of carry 3% làm NII giảm. Hai hiệu ứng cộng lại làm NIM giảm 0,50 điểm %. Xem [[hqla]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| NIM | Không thuộc phạm vi các chuẩn Basel đã ingest | [cần nguồn] | | |

## Ứng dụng trong ALM
- NII thường chiếm 40–80% tổng thu nhập ngân hàng. NIM bình quân ở UK, châu Âu và Mỹ thường 1–2,5%/năm. Không có mức NIM tối ưu vì phụ thuộc cơ cấu bảng cân đối, nhưng NIM là chỉ số then chốt trong định giá của chuyên viên phân tích, nên ngân hàng nên giữ và tối đa hoá NIM [[src-choudhry-principles-banking#^choudhry-nim-14]].
- Kỷ luật ALM nhằm giữ NIM, kể cả khi lãi suất âm [[src-choudhry-principles-banking#^choudhry-opt-1]] [[src-choudhry-principles-banking#^choudhry-neg-2]]. Xem [[negative-interest-rates]].

**Hành động quản lý NIM (Table 1.10)** [[src-choudhry-principles-banking#^choudhry-nim-11]]:

| Hành động | Kết quả NIM có thể | Nguồn |
|---|---|---|
| Tăng tỷ trọng tài sản rủi ro hơn | Có thể tăng NIM ngắn hạn, nhưng có thể không dài hạn do tổn thất tín dụng | [[src-choudhry-principles-banking#^choudhry-nim-11]] |
| Phân phối sản phẩm khớp đặc tính lãi suất tài sản/nợ đã có | Giảm độ nhạy NII, bảo vệ NIM | [[src-choudhry-principles-banking#^choudhry-nim-11]] |
| Chủ động tạo lệch kỳ tái định giá | Có thể tăng NIM khi đường cong dốc lên; tăng rủi ro lãi suất nên phải nằm trong khẩu vị đã duyệt | [[src-choudhry-principles-banking#^choudhry-nim-11]] |
| Dùng phái sinh lãi suất (IRS) | Tạo tài sản, nợ tổng hợp để đạt kết quả như hai dòng trên | [[src-choudhry-principles-banking#^choudhry-nim-11]] |
| Tăng nợ không chịu lãi | Tăng NIM | [[src-choudhry-principles-banking#^choudhry-nim-11]] |
| Giảm tài sản không sinh lãi | Giảm chi phí funding, tăng NIM | [[src-choudhry-principles-banking#^choudhry-nim-11]] |

Xem [[net-interest-income-sensitivity]], [[nii-planning]], [[interest-rate-swap]]. Phân tích NII theo cấu trúc bảng cân đối và [[maturity-transformation|maturity transformation]]: [[balance-sheet-structure-and-transformation]].

## Nhầm lẫn thường gặp
- Mẫu số NIM khác nhau giữa các định nghĩa: tài sản sinh lãi cuối kỳ trong case study [[src-choudhry-principles-banking#^choudhry-nim-2]], tài sản sinh lời bình quân ở Ví dụ 6.12 [[src-choudhry-principles-banking#^choudhry-hedge-21]], hoặc "một thước đo tài sản bình quân" ở phần tóm tắt [[src-choudhry-principles-banking#^choudhry-nim-14]]. *Diễn giải:* khi so NIM giữa ngân hàng hay giữa kỳ, cần thống nhất mẫu số.
- NIM không phải ΔNII: ΔNII là chỉ số IRRBB đo thay đổi NII khi sốc lãi suất. Xem [[net-interest-income-sensitivity]].
