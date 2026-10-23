---
title: "Delta-Plus Method"
aliases: [Delta-Plus Method, Delta-plus, Phương pháp Delta-plus]
type: concept
domains: [vn-reg, basel, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[options-risk-capital-requirement]]", cite: "[[src-tt14-2025-nhnn#^pl4-v-2b]]"}
tags: [capital, market-risk, options, tt14]
updated: 2026-10-23
reviewed:
---

## Ý chính
Phương pháp Delta-plus tính vốn yêu cầu cho quyền chọn mà ngân hàng bán (short option), bằng tổng ba cấu phần: Delta ($K_{DWP}$), Gamma ($K_{Gamma}$) và Vega ($K_{VR}$) [[src-tt14-2025-nhnn#^pl4-v-2b]]. Kết quả là phần tính cho quyền chọn bán ra trong [[options-risk-capital-requirement]].

## Cơ chế & drivers
**Delta** [[src-tt14-2025-nhnn#^pl4-v-delta]]:

$$
K_{DWP} = MV_{und} \times D_{OPT} \times (SRW + GRW)
$$
[[src-tt14-2025-nhnn#^pl4-v-delta]]

$D_{OPT}$ là Delta của giao dịch quyền chọn do ngân hàng xác định theo hướng dẫn của Ủy ban Basel hoặc dùng giá trị trên thị trường (nếu có). SRW, GRW xác định như ở [[options-risk-capital-requirement]].

**Gamma** [[src-tt14-2025-nhnn#^pl4-v-gamma]]: các tác động gamma riêng lẻ của quyền chọn có cùng tài sản gốc được cộng thành tác động gamma ròng cho từng tài sản gốc. Vốn cho gamma bằng tổng giá trị tuyệt đối của các tác động gamma ròng âm.

$$
GI = 0{,}5 \times Gamma \times (VU)^{2}
$$
[[src-tt14-2025-nhnn#^pl4-v-gamma]]

| Tài sản gốc | VU (mức biến động) | Nguồn |
|---|---|---|
| Công cụ có rủi ro lãi suất | $MV_{und} \times RW$, RW là hệ số rủi ro chung của bảng thang kỳ hạn ([[maturity-ladder-method]]) | [[src-tt14-2025-nhnn#^pl4-v-gamma]] |
| Cổ phiếu, công cụ có tính chất cổ phiếu, phái sinh cổ phiếu, chỉ số chứng khoán, ngoại tệ (gồm vàng tiêu chuẩn) | $MV_{und} \times 8\%$ | [[src-tt14-2025-nhnn#^pl4-v-gamma]] |
| Hàng hóa | $MV_{und} \times 15\%$ | [[src-tt14-2025-nhnn#^pl4-v-gamma]] |

**Vega** [[src-tt14-2025-nhnn#^pl4-v-vega]]: $K_{VR}$ bằng tổng giá trị tuyệt đối vốn cho tác động Vega của từng tài sản gốc.

$$
K_{VR} = 25\% \times \Delta_{rel} \times \left| \sum Vega \right|
$$
[[src-tt14-2025-nhnn#^pl4-v-vega]]

$\Delta_{rel}$ là tỷ lệ trong thay đổi giá trị của tài sản gốc (ký hiệu của wiki; nguồn viết bằng chữ), $\sum Vega$ là tổng giá trị Vega của các hợp đồng quyền chọn của cùng tài sản gốc. Tỷ lệ thay đổi và Vega do ngân hàng xác định theo hướng dẫn của Ủy ban Basel hoặc dùng giá trị thị trường (nếu có) [[src-tt14-2025-nhnn#^pl4-v-vega]].

## Phụ thuộc regime
Phương pháp tiêu chuẩn của Phụ lục IV; bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]].

## Góc nhìn theo domain
**VN Regulator.** Ví dụ của nguồn: bán quyền chọn mua hàng hóa, giá thực hiện 490 USD, giá thị trường 500 USD, thời hạn còn lại 12 tháng, lãi suất phi rủi ro 8%/năm, biến động 20%, giá trị quyền chọn 65,48 USD; Delta −0,721, Gamma −0,0034, tổng Vega 168 [[src-tt14-2025-nhnn#^pl4-v-vd]]:

| Cấu phần | Phép tính | Kết quả (USD) | Nguồn |
|---|---|---|---|
| $K_{DWP}$ | 500 × 0,721 × 15% | 54,075 | [[src-tt14-2025-nhnn#^pl4-v-vd]] |
| $K_{Gamma}$ | 1/2 × 0,0034 × (500 × 0,15)² | 9,5625 | [[src-tt14-2025-nhnn#^pl4-v-vd]] |
| $K_{VR}$ | 25% × 20% × 168 | 8,4 | [[src-tt14-2025-nhnn#^pl4-v-vd]] |
| Tổng | | 72,0375 | [[src-tt14-2025-nhnn#^pl4-v-vd]] |

*Diễn giải:* kiểm lại: 500 × 0,721 = 360,5; × 15% = 54,075. (500 × 0,15)² = 5.625; × 0,0034 = 19,125; ÷ 2 = 9,5625. 25% × 20% × 168 = 8,4. Tổng 72,0375, khớp nguồn. Ví dụ dùng độ lớn của Delta (0,721), không dùng dấu âm; quy ước dấu của $K_{DWP}$ khi Delta âm không được nguồn nêu [cần nguồn].

**Basel.** [cần nguồn] (MAR chưa ingest).

**ALM.** *Diễn giải:* Delta-plus đòi hỏi ngân hàng tính Greeks của sổ quyền chọn (mô hình Black-Scholes trong ví dụ) và dữ liệu nhất quán với đường cong lãi suất. Treasury bán cap, floor hoặc swaption cho khách hàng cần hệ thống định giá cung cấp Delta, Gamma, Vega theo từng tài sản gốc ([[interest-rate-cap-floor]], [[swaption]]).

## Bằng chứng thực nghiệm
Chưa có.

## Câu hỏi mở
- Cách xác định "tỷ lệ trong thay đổi giá trị của tài sản gốc" trong $K_{VR}$: nguồn chỉ dẫn tới hướng dẫn của Ủy ban Basel [cần nguồn].
