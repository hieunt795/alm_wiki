---
title: "Quy Mô Phơi Nhiễm Tỷ Lệ Đòn Bẩy (Leverage Ratio Exposure Measure)"
aliases: [Leverage Exposure Measure, Exposure Measure, Thước đo phơi nhiễm đòn bẩy, Mẫu số tỷ lệ đòn bẩy, LEV30 Exposure]
type: metric
domains: [basel, alm, vn-reg]
status: active
maturity: draft
sources: ["[[src-bcbs-lev]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[leverage-ratio]]", cite: "[[src-bcbs-lev#^lev20-3]]"}
  - {type: drives, to: "[[leverage-ratio]]", direction: "-", cite: "[[src-bcbs-lev#^lev20-3]]"}
tags: [leverage-ratio, basel-iii, exposure-measure, sa-ccr, sft, ccf, off-balance-sheet, concept]
updated: 2026-10-21
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

### Theo TT50/2026 (VN): tổng trạng thái rủi ro (EM)

TT50 gọi mẫu số của LEV là tổng trạng thái rủi ro (EM), gồm mọi tài sản có trên Báo cáo tình hình tài chính và cam kết ngoại bảng [[src-tt50-2026-nhnn#^pl3-1]]:

$$EM = E_{OnB} + E_{D} + E_{OffB} + E_{US}$$
[[src-tt50-2026-nhnn#^pl3-1]]

| Cấu phần | Nội dung theo TT50 | Căn cứ |
|---|---|---|
| $E_{OnB}$ | Tài sản nội bảng, không gồm phái sinh và giao dịch chưa tất toán; giá trị sau dự phòng cụ thể; gồm cả tài sản đã chuyển quyền sở hữu để thế chấp cho phái sinh và tài sản uỷ thác, nhận uỷ thác mà ngân hàng chịu rủi ro | [[src-tt50-2026-nhnn#^pl3-1]] [[src-tt50-2026-nhnn#^pl3-4]] |
| Repo, reverse repo (trong $E_{OnB}$) | RWA rủi ro tín dụng đối tác chia cho hệ số rủi ro tín dụng đối tác, theo quy định tỷ lệ an toàn vốn | [[src-tt50-2026-nhnn#^pl3-6]] |
| Cash pooling (trong $E_{OnB}$) | Số dư tài khoản chung nếu đáp ứng 4 điều kiện; nếu không, số dư từng tài khoản riêng lẻ | [[src-tt50-2026-nhnn#^pl3-5]] |
| $E_{D}$ | $\sum 1{,}4 \times (RC_i + PFE_i)$; $RC = \max(V - CVM_r + CVM_p;\ 0)$; PFE theo quy định tỷ lệ an toàn vốn | [[src-tt50-2026-nhnn#^pl3-7]] |
| $E_{OffB}$ | $\sum E_{off_i} \times CCF_i$; số dư cam kết và CCF theo quy định tỷ lệ an toàn vốn | [[src-tt50-2026-nhnn#^pl3-9]] |
| $E_{US}$ | Giao dịch chưa tất toán: phái sinh tính như phái sinh, còn lại tính như tài sản nội bảng | [[src-tt50-2026-nhnn#^pl3-2]] |

Nguyên tắc chung: giá trị kế toán; không dùng tài sản bảo đảm, bảo lãnh, giảm thiểu rủi ro tín dụng để giảm EM; không bù trừ tài sản với nợ, trừ trường hợp quy định riêng; khoản đã trừ khỏi Vốn cấp 1 thì không tính vào EM; chênh lệch giảm do đánh giá lại không được khấu trừ khỏi EM [[src-tt50-2026-nhnn#^pl3-3]]. Bù trừ hai bên chỉ cho hợp đồng không cho phép khách hàng thanh toán một phần hoặc không thanh toán; tài sản bảo đảm ngân hàng đã giao cho đối tác mà làm giảm tài sản kế toán thì tính lại vào nội bảng; ký quỹ biến động bằng tiền mặt được coi là thanh toán trước hạn khi đáp ứng Đ25.4.b [[src-tt50-2026-nhnn#^pl3-8]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Cấu phần | Nội bảng, phái sinh, SFT, ngoại bảng [[src-bcbs-lev#^lev20-5]] | Nội bảng, phái sinh, ngoại bảng, giao dịch chưa tất toán; không có cấu phần SFT riêng [[src-tt50-2026-nhnn#^pl3-1]] | TT50 PL3.I.1 | Khi Thống đốc quyết định áp dụng LEV [[src-tt50-2026-nhnn#^d8-1]] |
| Tài sản bảo đảm, bù trừ | Không dùng tài sản bảo đảm, bảo lãnh để giảm phơi nhiễm; không bù trừ tài sản với nợ [[src-bcbs-lev#^lev30-2]] | Như Basel [[src-tt50-2026-nhnn#^pl3-3]] | TT50 PL3.I.4 | |
| Khoản trừ Vốn cấp 1 | Được trừ khỏi phơi nhiễm [[src-bcbs-lev#^lev30-3]] | Không tính vào EM [[src-tt50-2026-nhnn#^pl3-3]] | TT50 PL3.I.5 | |
| Dự phòng | Trừ dự phòng cụ thể [[src-bcbs-lev#^lev30-9]] | Trừ dự phòng cụ thể [[src-tt50-2026-nhnn#^pl3-4]] | TT50 PL3.II.1.3 | |
| Phái sinh | $1{,}4 \times (RC + PFE)$, RC trừ ký quỹ tiền mặt đủ điều kiện [[src-bcbs-lev#^lev30-14]] [[src-bcbs-lev#^lev30-16]] | Cùng công thức; PFE theo quy định tỷ lệ an toàn vốn [[src-tt50-2026-nhnn#^pl3-7]] | TT50 PL3.II.2 | |
| Bán phái sinh tín dụng | Cộng giá trị danh nghĩa hiệu lực [[src-bcbs-lev#^lev30-31]] | Không có quy định riêng trong PL3 [[src-tt50-2026-nhnn#^pl3-7]] | | |
| Repo, reverse repo | Tài sản SFT gộp cộng $E^*$ [[src-bcbs-lev#^lev30-37]] | RWA tín dụng đối tác chia hệ số rủi ro tín dụng đối tác [[src-tt50-2026-nhnn#^pl3-6]] | TT50 PL3.II.1.5 | |
| Ngoại bảng | Cam kết chưa rút × CCF 10–100% [[src-bcbs-lev#^lev30-47]] | $E_{off} \times CCF$, CCF theo quy định tỷ lệ an toàn vốn [[src-tt50-2026-nhnn#^pl3-9]] | TT50 PL3.II.3 | |
| Cash pooling, giao dịch chưa tất toán | [cần nguồn: LEV30 phần cash pooling, unsettled trades chưa ingest] | Có quy định riêng [[src-tt50-2026-nhnn#^pl3-5]] [[src-tt50-2026-nhnn#^pl3-2]] | TT50 PL3.I.3, II.1.4 | |

*Diễn giải:*
- Khác biệt lớn nhất là repo. Basel tính toàn bộ tài sản reverse repo gộp vào mẫu số. TT50 tính "RWA tín dụng đối tác chia hệ số rủi ro", về bản chất là trạng thái tín dụng đối tác sau tài sản bảo đảm. Vì vậy reverse repo có tài sản bảo đảm tốt tạo EM nhỏ hơn nhiều so với Basel. Đây là ngoại lệ duy nhất cho nguyên tắc "không dùng tài sản bảo đảm để giảm EM".
- CCF và PFE dẫn chiếu sang TT14/2025 hoặc TT41/2016, nên EM của hai ngân hàng áp dụng hai thông tư khác nhau có thể khác nhau với cùng một danh mục.

---

## Ứng dụng trong ALM

### 3. Ứng Dụng Trong Tối Ưu Hóa Bảng Cân Đối ALM

Trong mô hình Bảng cân đối Kế toán Tổng hợp Quy mô Phơi nhiễm Tỷ lệ Đòn bẩy đặt ra một trần cứng cho quy mô tài sản:

1. **Hiệu chỉnh Danh mục Ngoại bảng**: 
   - Hạn mức cam kết tín dụng chưa rút nếu phân loại là Cam kết có thể hủy ngang vô điều kiện (UCC) chỉ chịu $\text{CCF} = 10\%$ [[src-bcbs-lev#^lev30-54]], tiết kiệm được 30% mẫu số so với cam kết thông thường ($\text{CCF} = 40\%$) [[src-bcbs-lev#^lev30-52]].
2. **Chiến lược Quản trị Phái sinh**:
   - Tối đa hóa tỷ trọng bù trừ song phương qua Đối tác bù trừ trung tâm (CCP) đủ chuẩn (QCCP) và chuẩn hóa thỏa thuận Credit Support Annex (CSA) cho phép hoán đổi ký quỹ bằng tiền mặt hàng ngày (Daily Cash Variation Margin) để triệt tiêu Chi phí thay thế (RC) về 0 [[src-bcbs-lev#^lev30-16]] [[src-bcbs-lev#^lev30-24]].
3. **Giám sát Hoạt động Repo**:
   - Sắp xếp kỳ hạn thanh toán trùng khớp (matching settlement dates) và vận hành cơ chế bù trừ DvP để tận dụng tối đa điều khoản bù trừ ròng tiền mặt của giao dịch SFTs [[src-bcbs-lev#^lev30-37]].
