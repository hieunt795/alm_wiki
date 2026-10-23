---
title: "Options Risk Capital Requirement"
aliases: [Options Risk Capital Requirement, K_OPT, KOPT, Vốn yêu cầu cho giao dịch quyền chọn]
type: metric
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[market-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^d74-6]]"}
tags: [capital, market-risk, options, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
Vốn yêu cầu cho giao dịch quyền chọn ($K_{OPT}$) là cấu phần của $K_{MR}$ cho hợp đồng quyền chọn có tài sản gốc là công cụ tài chính có rủi ro lãi suất, giá cổ phiếu, ngoại hối và giá hàng hóa [[src-tt14-2025-nhnn#^pl4-v-1]]. $K_{OPT}$ chỉ áp dụng khi tổng giá trị các giao dịch quyền chọn lớn hơn 2% vốn tự có ([[own-funds]]) [[src-tt14-2025-nhnn#^d74-6]]. Xem [[market-risk-capital-requirement]].

## Công thức
Công thức phụ thuộc vị thế của ngân hàng.

| Vị thế | Công thức | Nguồn |
|---|---|---|
| Mua quyền chọn bán (long put) khi có tài sản gốc dương, hoặc mua quyền chọn mua (long call) khi có tài sản gốc âm | $K_{OPT} = \max\{0;\ MV_{und} \times (SRW + GRW) - \max(0; V_{OPT})\}$ | [[src-tt14-2025-nhnn#^pl4-v-2ai]] |
| Mua quyền chọn mua hoặc quyền chọn bán (các trường hợp còn lại) | $K_{OPT} = \min\{MV_{und} \times (SRW + GRW);\ MV_{OPT}\}$ | [[src-tt14-2025-nhnn#^pl4-v-2aii]] |
| Bán quyền chọn (short option) | Phương pháp Delta-plus: $K_{DWP} + K_{Gamma} + K_{VR}$ ([[delta-plus-method]]) | [[src-tt14-2025-nhnn#^pl4-v-2b]] |

Ký hiệu $MV_{und}$ thay cho $MV_{underlying}$ của nguồn; dấu $\max\{0;\ \cdot\}$ là cách viết lại của wiki [[src-tt14-2025-nhnn#^pl4-v-2ai]].

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| $MV_{und}$ | Giá trị thị trường của tài sản gốc của hợp đồng quyền chọn (khi quyền chọn được thực hiện ở trường hợp mua quyền chọn mua/bán) | [[src-tt14-2025-nhnn#^pl4-v-2ai]] [[src-tt14-2025-nhnn#^pl4-v-2aii]] |
| SRW, GRW | Hệ số rủi ro quyền chọn cụ thể, chung (bảng dưới) | [[src-tt14-2025-nhnn#^pl4-v-2ai-w]] |
| $V_{OPT}$ | Giá trị bằng tiền của quyền chọn (nếu có) hoặc bằng 0 | [[src-tt14-2025-nhnn#^pl4-v-2ai]] |
| $MV_{OPT}$ | Giá trị thị trường của giao dịch quyền chọn | [[src-tt14-2025-nhnn#^pl4-v-2aii]] |

**Hệ số rủi ro quyền chọn** [[src-tt14-2025-nhnn#^pl4-v-2ai-w]]:

| Loại quyền chọn | Hệ số cụ thể (SRW) | Hệ số chung (GRW) |
|---|---|---|
| Lãi suất | SRW lãi suất cụ thể, Mục I ([[specific-interest-rate-risk-weight]]) | Hệ số rủi ro của bảng thang kỳ hạn, Mục I ([[maturity-ladder-method]]) |
| Giá cổ phiếu | Hệ số rủi ro giá cổ phiếu cụ thể, Mục II ([[equity-risk-capital-requirement]]) | 8% |
| Ngoại hối | (không nêu) | 8% |
| Giá hàng hóa | Tổng SRW và GRW là 15% | |

## Diễn giải
**Ví dụ 1 và 2 của nguồn (mua quyền chọn bán để phòng ngừa).** Ngân hàng A có trạng thái ngoại tệ dương 1 triệu USD, tỷ giá 22.000 VND/USD [[src-tt14-2025-nhnn#^pl4-v-2ai-vd]]:

| Giá chọn bán | $V_{OPT}$ | $K_{OPT}$ |
|---|---|---|
| 21.000 VND/USD | max(0; (21.000 − 22.000) × 1 triệu) = 0 | max(0; 1 triệu × 22.000 × 8% − 0) = 1,76 tỷ đồng |
| 23.000 VND/USD | (23.000 − 22.000) × 1 triệu = 1 tỷ đồng | max(0; 1 triệu × 22.000 × 8% − 1 tỷ đồng) = 0,76 tỷ đồng |

*Diễn giải:* kiểm lại: 1 triệu × 22.000 = 22 tỷ đồng; × 8% = 1,76 tỷ đồng; trừ 1 tỷ đồng ra 0,76. Cả hai khớp nguồn. Quyền chọn bán có giá chọn bán càng cao (càng gần tiền) thì $V_{OPT}$ càng lớn và $K_{OPT}$ càng nhỏ.

> [!conflict] Ví dụ mua quyền chọn mua/bán (PL4.B.V.2a(ii)): 8.000 hay 80.000 USD
> - Nguồn ghi "MV × (SRW + GRW) = 1 triệu (đôla Mỹ) × 8% = 8.000 đôla Mỹ" và K_OPT = Min(8.000; 12.000) = 8.000 USD [[src-tt14-2025-nhnn#^pl4-v-2aii-vd]].
> - 1 triệu USD × 8% bằng 80.000 USD. Nếu dùng 80.000 thì K_OPT = Min(80.000; 12.000) = 12.000 USD.
> - Lỗi số học trong ví dụ của nguồn (khác với công thức). Giữ cả hai; chưa kết luận, cần đối chiếu bản gốc.

*Diễn giải:* công thức min{MV × (SRW + GRW); MV_OPT} giới hạn vốn ở mức giá trị thị trường của quyền chọn, vì bên mua quyền chọn không lỗ quá giá trị này. Với giá quyền chọn 12.000 USD, vốn không vượt 12.000 USD; con số 8.000 USD của nguồn thấp hơn mức giới hạn này nên khó khớp với công thức.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Ngưỡng áp dụng | [cần nguồn] (MAR chưa ingest) | Tổng giá trị quyền chọn > 2% vốn tự có [[src-tt14-2025-nhnn#^d74-6]] | Đ74.6 | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Mua quyền chọn | [cần nguồn] | Hai công thức theo vị thế [[src-tt14-2025-nhnn#^pl4-v-2ai]] [[src-tt14-2025-nhnn#^pl4-v-2aii]] | PL4.B.V.2a | Như trên |
| Bán quyền chọn | [cần nguồn] | Delta-plus [[src-tt14-2025-nhnn#^pl4-v-2b]] | PL4.B.V.2b | Như trên |
| Hệ số quyền chọn ngoại hối | [cần nguồn] | GRW 8% [[src-tt14-2025-nhnn#^pl4-v-2ai-w]] | PL4.B.V.2a(i) | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* ngân hàng mua quyền chọn bán ngoại tệ để phòng ngừa trạng thái ngoại tệ dương vẫn chịu $K_{OPT}$, nhưng nhỏ hơn $K_{FXR}$ của trạng thái không phòng ngừa (trong ví dụ 1,76 tỷ đồng với giá chọn bán 21.000 và 0,76 tỷ đồng với giá chọn bán 23.000). Bán quyền chọn tính Delta-plus và tốn vốn cho gamma, vega. Vị thế phái sinh lãi suất có tài sản gốc là quyền chọn lãi suất (cap, floor, swaption) đi qua $K_{OPT}$ khi vượt ngưỡng 2%: xem [[interest-rate-cap-floor]], [[swaption]].

## Nhầm lẫn thường gặp
- Quyền chọn bán ra (short option) không dùng công thức max hoặc min của quyền chọn mua vào [[src-tt14-2025-nhnn#^pl4-v-2b]].
- Tài sản gốc của quyền chọn không bị tính lại vào rủi ro lãi suất, cổ phiếu hay ngoại hối [[src-tt14-2025-nhnn#^pl4-i-1]].
