---
title: "Commodity Risk Capital Requirement"
aliases: [Commodity Risk Capital Requirement, K_CMR, KCMR, Vốn yêu cầu cho rủi ro giá hàng hóa]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[market-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d74-5]]"}
tags: [capital, market-risk, commodity, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho rủi ro giá cả hàng hóa ($K_{CMR}$) là cấu phần của $K_{MR}$ cho trạng thái sản phẩm phái sinh giá cả hàng hóa trên sổ kinh doanh [[src-tt14-2025-nhnn#^pl4-iii-12]]. Xem [[market-risk-capital-requirement]].

## Công thức
$$
K_{CMR} = K_{CMR}^{\text{trực tiếp}} + K_{CMR}^{\text{khác}}
$$
[[src-tt14-2025-nhnn#^pl4-iii-35]]

$$
K_{CMR}^{\text{trực tiếp}} = NP \times 15\%
$$
[[src-tt14-2025-nhnn#^pl4-iii-35]]

$$
K_{CMR}^{\text{khác}} = (LP + SP) \times 3\%
$$
[[src-tt14-2025-nhnn#^pl4-iii-35]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $K_{CMR}^{\text{trực tiếp}}$ | Rủi ro giá cả hàng hóa trực tiếp, phát sinh do thay đổi giá giao ngay | [[src-tt14-2025-nhnn#^pl4-iii-35]] |
| $K_{CMR}^{\text{khác}}$ | Rủi ro giá cả hàng hóa khác, phát sinh do thay đổi giá kỳ hạn vì chênh lệch kỳ hạn hoặc do thay đổi quan hệ giá giữa hai loại hàng hóa tương tự nhưng không hoàn toàn giống nhau | [[src-tt14-2025-nhnn#^pl4-iii-35]] |
| NP | Trạng thái ròng của loại sản phẩm phái sinh giá cả hàng hóa | [[src-tt14-2025-nhnn#^pl4-iii-35]] |
| LP, SP | Trạng thái dương, âm của loại sản phẩm phái sinh giá cả hàng hóa | [[src-tt14-2025-nhnn#^pl4-iii-35]] |

## Diễn giải
**Xác định trạng thái.** Trạng thái xác định cho từng loại hàng hóa, trừ vàng tiêu chuẩn đã tính rủi ro tỷ giá. Sản phẩm cùng loại được bù trừ. Trạng thái tính bằng Việt Nam đồng, quy đổi đơn vị đo lường tiêu chuẩn theo giá giao ngay tại thời điểm tính [[src-tt14-2025-nhnn#^pl4-iii-12]].

**Rủi ro lãi suất, ngoại hối từ trạng thái hàng hóa.** Tính vào trạng thái rủi ro lãi suất ([[interest-rate-risk-capital-requirement]]) và ngoại hối ([[foreign-exchange-risk-capital-requirement]]) [[src-tt14-2025-nhnn#^pl4-iii-6]].

*Diễn giải:* ví dụ số do wiki dựng: trạng thái ròng NP = 20 tỷ đồng, LP = 50 tỷ đồng, SP = 30 tỷ đồng (giá trị tuyệt đối) thì $K_{CMR}^{\text{trực tiếp}}$ = 20 × 15% = 3 tỷ đồng và $K_{CMR}^{\text{khác}}$ = (50 + 30) × 3% = 2,4 tỷ đồng. Cách lấy SP trong tổng (LP + SP) như ở [[equity-risk-capital-requirement]] [cần nguồn].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Hệ số trực tiếp | [cần nguồn] (MAR chưa ingest) | 15% trạng thái ròng [[src-tt14-2025-nhnn#^pl4-iii-35]] | PL4.B.III.4 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Hệ số khác | [cần nguồn] | 3% tổng trạng thái dương và âm [[src-tt14-2025-nhnn#^pl4-iii-35]] | PL4.B.III.5 | Như trên |
| Ngưỡng áp dụng | [cần nguồn] | Không có [[src-tt14-2025-nhnn#^d74-5]] | Đ74.5 | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* ngân hàng thương mại Việt Nam ít có sổ phái sinh hàng hóa; mục này quan trọng với ngân hàng có nghiệp vụ phái sinh hàng hóa cho khách hàng. Không có ngưỡng 2% vốn tự có như $K_{FXR}$ và $K_{OPT}$ [[src-tt14-2025-nhnn#^d74-5]].

## Nhầm lẫn thường gặp
- Vàng tiêu chuẩn tính ở [[foreign-exchange-risk-capital-requirement]], không tính ở $K_{CMR}$ [[src-tt14-2025-nhnn#^pl4-iii-12]].
