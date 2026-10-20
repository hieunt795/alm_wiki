---
title: "Quy Mô Phơi Nhiễm Tỷ Lệ Đòn Bẩy (Leverage Ratio Exposure Measure)"
aliases: [Leverage Exposure Measure, Exposure Measure, Thước đo phơi nhiễm đòn bẩy, Mẫu số tỷ lệ đòn bẩy, LEV30 Exposure]
type: metric
domains: [basel, alm]
status: active
maturity: draft
sources: ["[[src-bcbs-lev]]"]
relations:
  - {type: part-of, to: "[[leverage-ratio]]", cite: "[[src-bcbs-lev#^lev20-3]]"}
tags: [leverage-ratio, basel-iii, exposure-measure, sa-ccr, sft, ccf, off-balance-sheet, concept]
updated: 2026-10-20
reviewed:
---

## Định nghĩa

### 1. Bản Chất và Nguyên Tắc Đo Lường Tổng Quát

Quy mô Phơi nhiễm Tỷ lệ Đòn bẩy (Leverage Ratio Exposure Measure) đóng vai trò là **mẫu số** trong công thức tính [[leverage-ratio|Tỷ lệ Đòn bẩy (LR $\ge 3\%$)]] theo chuẩn mực Basel III [[src-bcbs-lev#^lev20-3]].

Khác biệt căn bản với Tổng tài sản có rủi ro (RWA) trong Trụ cột 1 (vốn phân loại rủi ro theo xếp hạng tín nhiệm hay mô hình nội bộ), thước đo phơi nhiễm đòn bẩy quán triệt các nguyên tắc giám sát nghiêm ngặt:
1. **Nguyên tắc Giá trị Kế toán Gộp (Gross Accounting Values)**: Phơi nhiễm được tính toán dựa trên quy mô tài sản gộp, triệt tiêu các thủ thuật kế toán làm đẹp bảng cân đối [[src-bcbs-lev#^lev30-1]].
2. **Cấm Bù trừ và Giảm thiểu Rủi ro (Prohibition of Netting and CRM)**: Không được phép sử dụng tài sản bảo đảm vật chất, tài chính hay bảo lãnh bên thứ ba để làm giảm phơi nhiễm; cấm bù trừ tài sản với công nợ (trừ khi đáp ứng tiêu chuẩn bù trừ pháp lý song phương đặc biệt khắt khe) [[src-bcbs-lev#^lev30-2]].
3. **Bảo đảm Tính Nhất quán với Vốn Tự có (Capital Deduction Symmetry)**: Mọi khoản mục bị khấu trừ khỏi Vốn cấp 1 (như lợi thế thương mại goodwill, chênh lệch thiếu dự phòng lỗ kỳ vọng theo IRB) được phép khấu trừ tương ứng khỏi mẫu số phơi nhiễm để tránh tính trùng phạt kép [[src-bcbs-lev#^lev30-3]].

---

## Công thức & tham số

### 2. Bốn Trụ Cột Cấu Thành Quy Mô Phơi Nhiễm

Theo quy định tại LEV20.5, tổng quy mô phơi nhiễm là tổng của 4 cấu phần độc lập [[src-bcbs-lev#^lev20-5]]:

$$\text{Total Exposure Measure} = E_{\text{On-BS}} + E_{\text{Deriv}} + E_{\text{SFT}} + E_{\text{OBS}}$$

```
+---------------------------------------------------------------------------------------------------+
|                            TỔNG QUY MÔ PHƠI NHIỄM ĐÒN BẨY (LEV30)                                 |
+---------------------------------+---------------------------------+-------------------------------+
|  1. PHƠI NHIỄM NỘI BẢNG         |  2. PHƠI NHIỄM PHÁI SINH        |  3. PHƠI NHIỄM TÀI TRỢ SFTs   |
|  - Toàn bộ TSC kế toán gộp      |  - SA-CCR: 1.4 * (RC + PFE)     |  - Tài sản SFT gộp            |
|  - Trừ khấu trừ Vốn cấp 1       |  - Cộng nợ danh nghĩa bán CDS   |  - Bù trừ tiền mặt DvP        |
|  - Trừ dự phòng cụ thể          |  - Chỉ trừ ký quỹ tiền mặt CVM  |  - Cộng CCR hiện tại E*       |
+---------------------------------+---------------------------------+-------------------------------+
|                                    4. KHOẢN MỤC NGOẠI BẢNG (OBS)                                  |
|                       Giá trị cam kết chưa rút * Hệ số chuyển đổi tín dụng (CCF)                  |
|                                       (10% - 20% - 40% - 50% - 100%)                              |
+---------------------------------------------------------------------------------------------------+
```

#### A. Phơi Nhiễm Nội Bảng (On-balance Sheet Exposures — $E_{\text{On-BS}}$)
- Bao gồm toàn bộ tài sản nội bảng của ngân hàng theo giá trị ghi sổ, ngoại trừ tài sản phái sinh và tài sản SFTs (được bóc tách xử lý riêng) [[src-bcbs-lev#^lev30-8]].
- Bao gồm cả tài sản quyền sử dụng thuê tài chính (Right-of-use asset — ROU theo IFRS 16) và tài sản bảo đảm nhận về được hạch toán nội bảng [[src-bcbs-lev#^lev30-8]].
- **Các khoản được phép giảm trừ**:
  - Các khoản khấu trừ trực tiếp khỏi Vốn cấp 1 theo chuẩn CAP30 (như Goodwill, tài sản vô hình, đầu tư vào công ty con ngoài phạm vi hợp nhất) [[src-bcbs-lev#^lev30-3]].
  - Dự phòng rủi ro cụ thể (Specific provisions) trích lập cho từng tài sản [[src-bcbs-lev#^lev30-9]].
  - Dự phòng chung (General loan-loss reserves) đã làm giảm Vốn cấp 1 [[src-bcbs-lev#^lev30-9]].

#### B. Phơi Nhiễm Phái Sinh (Derivative Exposures — $E_{\text{Deriv}}$)
Được đo lường theo phương pháp chuẩn hóa rủi ro đối tác tín dụng (Standardised Approach for Counterparty Credit Risk — SA-CCR) nhưng có điều chỉnh riêng cho Tỷ lệ Đòn bẩy [[src-bcbs-lev#^lev30-14]]:

$$E_{\text{Deriv}} = \alpha \times (\text{RC} + \text{PFE}) + \text{Add-on}_{\text{Written CDS}}$$

- **Hệ số mở rộng (Scalar Multiplier)**: $\alpha = 1.4$ phản ánh mức độ biến động tiềm tàng của rủi ro đối tác [[src-bcbs-lev#^lev30-14]].
- **Chi phí thay thế (Replacement Cost — RC)**:
  $$\text{RC} = \max(V - \text{CVM}_r + \text{CVM}_p, 0)$$
  Trong đó: $V$ là giá trị thị trường của danh mục phái sinh; $\text{CVM}_r$ là ký quỹ biến đổi bằng tiền mặt nhận về; $\text{CVM}_p$ là ký quỹ biến đổi bằng tiền mặt chuyển đi [[src-bcbs-lev#^lev30-16]].
  - *Lưu ý quan trọng*: Tài sản bảo đảm nhận về bằng chứng khoán hay tài sản phi tiền mặt **không được phép giảm RC**, bất kể kế toán có ghi nhận hay không [[src-bcbs-lev#^lev30-22]]. Ký quỹ tiền mặt $\text{CVM}_r$ chỉ được giảm RC nếu đáp ứng đủ 5 điều kiện (tính toán hàng ngày, thanh toán bằng đồng tiền thỏa thuận, không bị phong tỏa và chuyển giao đầy đủ) [[src-bcbs-lev#^lev30-24]].
- **Phơi nhiễm tiềm tàng tương lai (Potential Future Exposure — PFE)**:
  - Tính theo chuẩn CRE52, nhưng hệ số nhân (multiplier) được cố định cứng bằng **1.0** (không được giảm trừ hệ số nhân do có tài sản bảo đảm) [[src-bcbs-lev#^lev30-16]].
- **Phụ trội Bán phái sinh tín dụng (Written Credit Derivatives)**:
  - Khi ngân hàng bán hợp đồng bảo hiểm tín dụng (như bán CDS), ngân hàng gánh chịu rủi ro tương đương một khoản cho vay tiền mặt [[src-bcbs-lev#^lev30-31]]. Do đó, giá trị danh nghĩa hiệu lực (effective notional amount) phải được cộng trực tiếp vào mẫu số phơi nhiễm (sau khi trừ đi các khoản mua bảo hiểm bù trừ hợp lệ trên cùng tên pháp nhân) [[src-bcbs-lev#^lev30-31]].

#### C. Phơi Nhiễm Giao Dịch Tài Trợ Chứng Khoán (SFT Exposures — $E_{\text{SFT}}$)
Bao gồm các giao dịch mua bán lại chứng khoán (Repo, Reverse Repo, Cho vay/Mượn chứng khoán) [[src-bcbs-lev#^lev30-36]]. Tổng phơi nhiễm SFT gồm 2 thành phần [[src-bcbs-lev#^lev30-37]]:

$$E_{\text{SFT}} = \text{Gross SFT Assets Adjusted} + E^*$$

1. **Tài sản SFT gộp đã điều chỉnh**: Giá trị các khoản phải thu bằng tiền mặt trong giao dịch repo ngược. Cấm bù trừ kế toán thông thường. Bù trừ tiền mặt ròng chỉ được chấp nhận nếu giao dịch có cùng ngày thanh toán xác định, có thỏa thuận bù trừ song phương có hiệu lực pháp lý và thực hiện thanh toán theo cơ chế Delivery-versus-Payment (DvP) trên cùng hệ thống thanh toán bù trừ [[src-bcbs-lev#^lev30-37]].
2. **Phơi nhiễm rủi ro đối tác hiện tại ($E^*$)**:
   $$E^* = \max\left(0, \sum E_i - \sum C_i\right)$$
   Trong đó: $\sum E_i$ là tổng giá trị chứng khoán và tiền mặt cho đối tác vay; $\sum C_i$ là tổng giá trị tiền mặt và chứng khoán nhận về theo Thỏa thuận khung bù trừ chuẩn (qualifying Master Netting Agreement — MNA) [[src-bcbs-lev#^lev30-37]].

#### D. Khoản Mục Ngoại Bảng (Off-Balance Sheet Items — $E_{\text{OBS}}$)
Bao gồm các cam kết cấp tín dụng, thư bảo lãnh, L/C thương mại và hạn mức thanh khoản chưa giải ngân [[src-bcbs-lev#^lev30-45]]. Giá trị phơi nhiễm bằng **Hạn mức cam kết chưa rút nhân với Hệ số chuyển đổi tín dụng (CCF)** [[src-bcbs-lev#^lev30-47]]:

$$E_{\text{OBS}} = \sum (\text{Committed Undrawn Amount}_k \times \text{CCF}_k)$$

##### Ma trận Hệ số Chuyển đổi Tín dụng (CCF Matrix):
| Hệ số CCF | Loại Khoản mục Ngoại bảng Chuẩn mực Basel III | Điều kiện Áp dụng & Ví dụ |
| :---: | :--- | :--- |
| **100%** | **Khoản mục thay thế tín dụng trực tiếp** [[src-bcbs-lev#^lev30-49]] | Bảo lãnh thanh toán, thư tín dụng dự phòng bảo đảm cho nghĩa vụ nợ, cam kết mua tài sản kỳ hạn. |
| **50%** | **Cam kết phát hành giấy tờ có giá / Bảo lãnh nghiệp vụ** | Note issuance facilities (NIFs), RUF; Bảo lãnh dự thầu, bảo lãnh thực hiện hợp đồng. |
| **40%** | **Cam kết tín dụng thông thường** [[src-bcbs-lev#^lev30-52]] | Mọi hạn mức tín dụng cam kết cấp cho doanh nghiệp/bán lẻ (bất kể kỳ hạn), trừ khi thuộc nhóm thấp hơn. |
| **20%** | **Thư tín dụng thương mại ngắn hạn** | L/C thương mại tự thanh lý ngắn hạn có thế chấp bằng lô hàng hóa xuất nhập khẩu đang vận chuyển. |
| **10%** | **Cam kết có thể hủy ngang vô điều kiện (UCC)** [[src-bcbs-lev#^lev30-54]] | Hạn mức thấu chi hoặc thẻ tín dụng mà ngân hàng có toàn quyền hủy ngang ngay lập tức không cần báo trước. |

---

## Ứng dụng trong ALM

### 3. Ứng Dụng Trong Tối Ưu Hóa Bảng Cân Đối ALM

Trong mô hình Bảng cân đối Kế toán Tổng hợp [[synthetic-balance-sheet-liquidity-risk]], Quy mô Phơi nhiễm Tỷ lệ Đòn bẩy đặt ra một trần cứng cho quy mô tài sản:

1. **Hiệu chỉnh Danh mục Ngoại bảng**: 
   - Hạn mức cam kết tín dụng chưa rút nếu phân loại là Cam kết có thể hủy ngang vô điều kiện (UCC) chỉ chịu $\text{CCF} = 10\%$ [[src-bcbs-lev#^lev30-54]], tiết kiệm được 30% mẫu số so với cam kết thông thường ($\text{CCF} = 40\%$) [[src-bcbs-lev#^lev30-52]].
2. **Chiến lược Quản trị Phái sinh**:
   - Tối đa hóa tỷ trọng bù trừ song phương qua Đối tác bù trừ trung tâm (CCP) đủ chuẩn (QCCP) và chuẩn hóa thỏa thuận Credit Support Annex (CSA) cho phép hoán đổi ký quỹ bằng tiền mặt hàng ngày (Daily Cash Variation Margin) để triệt tiêu Chi phí thay thế (RC) về 0 [[src-bcbs-lev#^lev30-16]] [[src-bcbs-lev#^lev30-24]].
3. **Giám sát Hoạt động Repo**:
   - Sắp xếp kỳ hạn thanh toán trùng khớp (matching settlement dates) và vận hành cơ chế bù trừ DvP để tận dụng tối đa điều khoản bù trừ ròng tiền mặt của giao dịch SFTs [[src-bcbs-lev#^lev30-37]].
