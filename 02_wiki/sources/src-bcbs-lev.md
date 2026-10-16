---
title: "BCBS — LEV Leverage Ratio (Basel Framework)"
aliases: [src-bcbs-lev, BCBS LEV, Basel III Leverage Ratio Standard]
type: source
source_id: src-bcbs-lev
domains: [basel, alm]
status: active
maturity: draft
tier: T2
doc_status: final
issuer: BCBS
published: 2025-12-17
effective: 2023-01-01
raw: 01_sources/alm/Basel/LEV/LEV.md
units_done: [LEV10, LEV20, LEV30, LEV40]
updated: 2026-10-16
---

## Thông tin nguồn
- Issuer: Basel Committee on Banking Supervision ([[bcbs]])
- Tier T2, `doc_status: final`. Bản consolidated framework sinh từ website BIS ngày 17/12/2025, có hiệu lực chính thức từ 01/01/2023.
- Scope: Chuẩn mực đo lường và giám sát Tỷ lệ Đòn bẩy (Leverage Ratio) độc lập với rủi ro (non-risk-based), đóng vai trò chốt chặn (backstop) cho khuôn khổ an toàn vốn theo trọng số rủi ro (RWA).
- Raw: `01_sources/alm/Basel/LEV/LEV.md` (390 dòng).
- Units covered:
  - `LEV10`: Definitions and application (phạm vi hợp nhất)
  - `LEV20`: Calculation (công thức, tử số Vốn cấp 1, mẫu số Exposure Measure, mức tối thiểu 3%)
  - `LEV30`: Exposure measurement (chi tiết 4 cấu phần: nội bảng, phái sinh SA-CCR alpha 1.4, SFTs, ngoại bảng CCF 10%–100%)
  - `LEV40`: Leverage ratio requirements for global systemically important banks (G-SIB buffer = 50% risk-based buffer)

## Tóm tắt Chuẩn mực LEV
Chuẩn mực LEV thiết lập tỷ lệ đòn bẩy đơn giản, minh bạch và phi rủi ro nhằm hạn chế sự tích tụ đòn bẩy quá mức trong hệ thống ngân hàng, ngăn ngừa vòng xoáy giảm đòn bẩy gây bất ổn (destabilising deleveraging process).

Tỷ lệ đòn bẩy được định nghĩa bằng Vốn cấp 1 (Tier 1 Capital) chia cho Tổng quy mô phơi nhiễm (Total Exposure Measure):
$$\text{Leverage Ratio} = \frac{\text{Tier 1 Capital}}{\text{Total Exposure Measure}} \ge 3\%$$

Mẫu số (Exposure Measure) bao gồm 4 cấu phần được tính toán theo nguyên tắc gộp (gross accounting value), cấm bù trừ tài sản và nợ hoặc dùng tài sản bảo đảm để giảm phơi nhiễm (trừ trường hợp bù trừ song phương đủ điều kiện pháp lý và ký quỹ biến đổi bằng tiền mặt CVM):
1. **Phơi nhiễm nội bảng (On-balance sheet exposures)**: Toàn bộ tài sản theo sổ sách kế toán trừ các khoản khấu trừ Vốn cấp 1 và dự phòng rủi ro cụ thể.
2. **Phơi nhiễm phái sinh (Derivative exposures)**: Đo lường theo chuẩn mực SA-CCR sửa đổi bằng $\alpha \times (\text{RC} + \text{PFE})$ với $\alpha = 1.4$, không cho phép giảm phơi nhiễm bằng tài sản bảo đảm nhận về (ngoại trừ Cash Variation Margin hợp lệ). Các hợp đồng bán phái sinh tín dụng (written credit derivatives) phải cộng thêm giá trị danh nghĩa hiệu lực (effective notional amount).
3. **Phơi nhiễm tài trợ chứng khoán (SFT exposures)**: Tổng tài sản SFT gộp (chỉ cho phép bù trừ tiền mặt ròng theo điều kiện DvP thanh toán cùng ngày cực kỳ khắt khe) cộng thêm phơi nhiễm rủi ro đối tác hiện tại $E^* = \max(0, \sum E_i - \sum C_i)$.
4. **Khoản mục ngoại bảng (Off-balance sheet items)**: Quy đổi bằng cách nhân giá trị cam kết chưa rút với các hệ số chuyển đổi tín dụng (CCF) từ 10% (cam kết hủy ngang vô điều kiện UCC), 20% (L/C thương mại), 40% (cam kết tín dụng thông thường), 50% (bảo lãnh dự thầu/thực hiện hợp đồng) đến 100% (cam kết thay thế tín dụng trực tiếp).

Đối với các ngân hàng có tầm quan trọng hệ thống toàn cầu (G-SIBs), Basel áp dụng thêm phần đệm tỷ lệ đòn bẩy (Leverage Ratio Buffer) bằng 50% phần đệm vốn rủi ro bổ sung (higher loss-absorbency requirement), vi phạm phần đệm sẽ kích hoạt cơ chế hạn chế phân phối lợi nhuận và cổ tức.

## Key Claims & Verbatim Quotes

### LEV10 — Definitions and Application
- Khuôn khổ tỷ lệ đòn bẩy áp dụng cùng phạm vi hợp nhất quản lý như khuôn khổ vốn dựa trên rủi ro.
  > "The leverage ratio framework follows the same scope of regulatory consolidation, including consolidation criteria, as is used for the risk-based capital framework."
  > — LEV10.1 ^lev10-1

### LEV20 — Calculation
- Mục đích kép của tỷ lệ đòn bẩy Basel III: hạn chế tích tụ đòn bẩy quá mức và gia cố yêu cầu an toàn vốn bằng chốt chặn phi rủi ro.
  > "restrict the build-up of leverage in the banking sector to avoid destabilising deleveraging processes that can damage the broader financial system and the economy;"
  > "reinforce the risk-based capital requirements with a simple, non-risk-based "backstop" measure."
  > — LEV20.1 ^lev20-1

- Tỷ lệ đòn bẩy được định nghĩa là tử số thước đo vốn chia cho mẫu số thước đo quy mô phơi nhiễm, tính theo phần trăm.
  > "The leverage ratio is defined as the capital measure (the numerator) divided by the exposure measure (the denominator), with this ratio expressed as a percentage:"
  > — LEV20.3 ^lev20-3

- Thước đo vốn cho tỷ lệ đòn bẩy là Vốn cấp 1 (Tier 1 Capital) gồm Vốn cấp 1 phổ thông (CET1) và Vốn cấp 1 bổ sung (AT1) theo định nghĩa tại CAP10.
  > "The capital measure for the leverage ratio is Tier 1 capital comprising Common Equity Tier 1 and/or Additional Tier 1 instruments – as defined in CAP10."
  > — LEV20.4 ^lev20-4

- Tổng quy mô phơi nhiễm tỷ lệ đòn bẩy là tổng của 4 cấu phần: (1) nội bảng, (2) phái sinh, (3) tài trợ chứng khoán SFTs, và (4) ngoại bảng.
  > "A bank's total leverage ratio exposure measure is the sum of the following exposures, as defined in LEV30:"
  > "on-balance sheet exposures (excluding on-balance sheet derivative and securities financing transaction exposures);"
  > — LEV20.5 ^lev20-5

- Ngân hàng phải duy trì tỷ lệ đòn bẩy tối thiểu 3% tại mọi thời điểm.
  > "Banks must meet a 3% leverage ratio minimum requirement at all times."
  > — LEV20.7 ^lev20-7

### LEV30 — Exposure Measurement
- Quy mô phơi nhiễm tỷ lệ đòn bẩy nhìn chung tuân theo giá trị kế toán gộp.
  > "The leverage ratio exposure measure generally follows gross accounting values."
  > — LEV30.1 ^lev30-1

- Cấm áp dụng tài sản bảo đảm vật chất/tài chính, bảo lãnh hoặc kỹ thuật giảm thiểu rủi ro tín dụng để giảm quy mô phơi nhiễm, và cấm bù trừ tài sản với công nợ trừ khi có quy định khác.
  > "Unless specified differently below, banks must not take account of physical or financial collateral, guarantees or other credit risk mitigation techniques to reduce the leverage ratio exposure measure, nor may banks net assets and liabilities."
  > — LEV30.2 ^lev30-2

- Mọi khoản mục bị khấu trừ khỏi Vốn cấp 1 (trừ phần liên quan đến nợ phải trả) được phép khấu trừ tương ứng khỏi thước đo phơi nhiễm.
  > "To ensure consistency, any item deducted from Tier 1 capital according to the Basel III framework and regulatory adjustments other than those related to liabilities may be deducted from the leverage ratio exposure measure."
  > — LEV30.3 ^lev30-3

- Quyền quyết định quốc gia cho phép miễn trừ tạm thời dự trữ tại ngân hàng trung ương khỏi mẫu số trong điều kiện kinh tế vĩ mô đặc biệt, kèm theo tăng tỷ lệ đòn bẩy tối thiểu tương ứng.
  > "At national discretion, and to facilitate the implementation of monetary policies, a jurisdiction may temporarily exempt central bank reserves from the leverage ratio exposure measure in exceptional macroeconomic circumstances."
  > — LEV30.7 ^lev30-7

- Toàn bộ tài sản nội bảng phải đưa vào mẫu số phơi nhiễm, bao gồm tài sản bảo đảm nhận về của phái sinh và SFTs hạch toán nội bảng.
  > "Banks must include all balance sheet assets in their leverage ratio exposure measure, including on-balance sheet derivatives collateral and collateral for SFTs, with the exception of on-balance sheet derivative and SFT assets that are covered in LEV30.13 to LEV30.44."
  > — LEV30.8 ^lev30-8

- Tài sản phi phái sinh nội bảng được tính theo giá trị kế toán sau khi trừ đi các khoản dự phòng rủi ro cụ thể liên quan.
  > "On-balance sheet, non-derivative assets are included in the leverage ratio exposure measure at their accounting values less deductions for associated specific provisions."
  > — LEV30.9 ^lev30-9

- Phơi nhiễm phái sinh được đo lường bằng hệ số nhân scalar alpha 1.4 nhân với tổng Chi phí thay thế (RC) và Phơi nhiễm tiềm tàng tương lai (PFE).
  > "Banks must calculate their exposures associated with all derivative transactions, including where a bank sells protection using a credit derivative, as a scalar multiplier alpha set at 1.4 times the sum of the RC4 and the PFE, as described in LEV30.15 to LEV30.16."
  > "alpha is 1.4;"
  > — LEV30.14 ^lev30-14

- Trong công thức SA-CCR của tỷ lệ đòn bẩy, hệ số nhân của PFE được ấn định cứng bằng 1, và chi phí thay thế RC được tính có khấu trừ ký quỹ biến đổi tiền mặt.
  > "alpha is 1.4;"
  > — LEV30.16 ^lev30-16

- Tài sản bảo đảm nhận về từ phái sinh không được bù trừ để làm giảm phơi nhiễm phái sinh, bất kể chuẩn mực kế toán cho phép hay không.
  > "As a general principle of the Basel III leverage ratio framework, collateral received may not be netted against derivative exposures whether or not netting is permitted under the bank's operative accounting or risk-based framework."
  > — LEV30.22 ^lev30-22

- Phần ký quỹ biến đổi bằng tiền mặt (cash variation margin) được coi là thanh toán trước hạn và được giảm RC nếu đáp ứng 5 điều kiện khắt khe.
  > "In the treatment of derivative exposures for the purpose of the leverage ratio exposure measure, the cash portion of variation margin exchanged between counterparties may be viewed as a form of pre-settlement payment if the following conditions are met:"
  > — LEV30.24 ^lev30-24

- Đối với các hợp đồng bán phái sinh tín dụng (written credit derivatives), giá trị danh nghĩa hiệu lực (effective notional amount) phải được tính vào mẫu số phơi nhiễm.
  > "In order to capture the credit exposure to the underlying reference entity, in addition to the above treatment for derivatives and related collateral, the effective notional amount referenced by a written credit derivative is to be included in the leverage ratio exposure measure"
  > — LEV30.31 ^lev30-31

- Khung đo lường phơi nhiễm giao dịch tài trợ chứng khoán (SFTs) nhận diện vay mượn có bảo đảm là nguồn sinh đòn bẩy trọng yếu.
  > "The treatment recognises that secured lending and borrowing in the form of SFTs is an important source of leverage, and ensures consistent international implementation by providing a common measure for dealing with the main differences in the operative accounting frameworks."
  > — LEV30.36 ^lev30-36

- Tổng phơi nhiễm SFT bao gồm tài sản SFT gộp theo kế toán (có điều chỉnh bù trừ DvP) cộng với phơi nhiễm rủi ro đối tác hiện tại E*.
  > "The treatment recognises that secured lending and borrowing in the form of SFTs is an important source of leverage, and ensures consistent international implementation by providing a common measure for dealing with the main differences in the operative accounting frameworks."
  > — LEV30.37 ^lev30-37

- Khoản mục ngoại bảng (OBS) bao gồm các cam kết, bảo lãnh thay thế tín dụng, chấp nhận thanh toán, thư tín dụng dự phòng và L/C thương mại.
  > "OBS items include commitments (including liquidity facilities), whether or not unconditionally cancellable, direct credit substitutes, acceptances, standby letters of credit and trade letters of credit."
  > — LEV30.45 ^lev30-45

- Các khoản mục ngoại bảng được quy đổi thành giá trị tương đương phơi nhiễm tín dụng bằng cách nhân hạn mức cam kết chưa rút với hệ số CCF.
  > "For the purposes of the leverage ratio, OBS items will be converted into credit exposures by multiplying the committed but undrawn amount by a CCF."
  > — LEV30.47 ^lev30-47

- Hệ số CCF 100% áp dụng cho các khoản thay thế tín dụng trực tiếp như bảo lãnh chung và chấp nhận thanh toán.
  > "A 100% CCF will be applied to the following items:"
  > "Direct credit substitutes, eg general guarantees of indebtedness (including standby letters of credit serving as financial guarantees for loans and securities) and acceptances (including endorsements with the character of acceptances)."
  > — LEV30.49 ^lev30-49

- Hệ số CCF 40% áp dụng cho các cam kết tín dụng thông thường bất kể kỳ hạn, trừ khi đủ điều kiện hưởng CCF thấp hơn.
  > "A 40% CCF will be applied to commitments, regardless of the maturity of the underlying facility, unless they qualify for a lower CCF."
  > — LEV30.52 ^lev30-52

- Hệ số CCF 10% áp dụng cho các cam kết có thể hủy ngang vô điều kiện (unconditionally cancellable commitments - UCC) tại mọi thời điểm không cần báo trước.
  > "A 10% CCF will be applied to commitments that are unconditionally cancellable at any time by the bank without prior notice, or that effectively provide for automatic cancellation due to deterioration in a borrower's creditworthiness."
  > — LEV30.54 ^lev30-54

### LEV40 — G-SIB Requirements
- Các ngân hàng có tầm quan trọng hệ thống toàn cầu (G-SIBs) phải duy trì thêm phần đệm tỷ lệ đòn bẩy bằng Vốn cấp 1.
  > "banks identified as global systemically important banks (G-SIBs) according to SCO40 must also meet a leverage ratio buffer requirement."
  > — LEV40.1 ^lev40-1

- Phần đệm tỷ lệ đòn bẩy của G-SIB được ấn định bằng 50% yêu cầu đệm vốn rủi ro bổ sung (higher loss-absorbency requirement).
  > "The leverage ratio buffer will be set at 50% of a G-SIB's higher loss-absorbency risk-based requirements."
  > — LEV40.2 ^lev40-2

- Ràng buộc phân phối lợi nhuận và vốn sẽ kích hoạt nếu ngân hàng G-SIB không đáp ứng đầy đủ yêu cầu đệm tỷ lệ đòn bẩy.
  > "A G-SIB which does not meet one of these requirements will be subject to the associated minimum capital conservation standards."
  > — LEV40.4 ^lev40-4
