---
title: "IRRBB Standardised Framework (Khuôn khổ chuẩn hoá đo lường rủi ro lãi suất Basel)"
aliases: [IRRBB Standardised Framework, Basel IRRBB Standardised Approach, Khuôn khổ chuẩn hoá IRRBB, Standardised EVE Framework]
type: model
domains: [alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: measures, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: input-to, to: "[[outlier-bank-test]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
  - {type: governs, to: "[[non-maturity-deposits]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-4]]"}
  - {type: governs, to: "[[behavioural-options]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-5]]"}
tags: [irrbb, standardised-framework, eve, cash-flow-slotting, 19-time-buckets, kao, basel]
updated: 2026-10-16
reviewed:
---

## Mục tiêu

### Định nghĩa & Vị trí pháp lý

Khuôn khổ chuẩn hoá IRRBB (Standardised Framework for IRRBB) được quy định chi tiết tại **Phần IV (Section IV)** của Chuẩn mực [[bcbs-irrbb]] (văn bản d368) [[src-bcbs-irrbb-2016#^irrbb-u05-1]]. Đây là phương pháp luận định lượng quy chuẩn do Ủy ban Basel xây dựng nhằm xác định mức độ nhạy cảm của Giá trị kinh tế của Vốn chủ sở hữu ([[economic-value-of-equity|$\Delta\text{EVE}$]]) dưới 6 kịch bản sốc lãi suất ([[standardised-interest-rate-shocks]]) [[src-bcbs-irrbb-2016#^irrbb-u05-1]].

Về mặt giám sát, Khuôn khổ chuẩn hoá đóng hai vai trò trọng yếu:
1. **Thước đo dự phòng bắt buộc (Supervisory Fallback Mandate)**: Khi cơ quan thanh tra giám sát xác định rằng Hệ thống Đo lường Nội bộ (Internal Measurement System - IMS) của ngân hàng có khiếm khuyết nghiêm trọng hoặc không phản ánh đầy đủ rủi ro, cơ quan giám sát có thẩm quyền bắt buộc ngân hàng phải chuyển sang áp dụng Khuôn khổ chuẩn hoá này để tính toán $\Delta\text{EVE}$ (Nguyên tắc 11) [[src-bcbs-irrbb-2016#^irrbb-p11-2]].
2. **Khuôn khổ đối chuẩn Trụ cột 2 & 3 (Pillar 2 Benchmarking & Pillar 3 Disclosure)**: Cung cấp hệ quy chiếu thống nhất để cơ quan giám sát so sánh mức độ rủi ro giữa các ngân hàng và thực hiện kiểm tra [[outlier-bank-test|Ngân hàng ngoại lai (Outlier Bank Test)]] [[src-bcbs-irrbb-2016#^irrbb-p10-1]] [[src-bcbs-irrbb-2016#^irrbb-p12-1]].

---

## Công thức

### Cấu trúc Quy trình Đo lường 5 Giai đoạn

Theo quy định tại par 100 của d368, quy trình đo lường $\Delta\text{EVE}$ chuẩn hoá bao gồm **5 giai đoạn tuần tự** [[src-bcbs-irrbb-2016#^irrbb-u05-1]]:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│             QUY TRÌNH 5 GIAI ĐOẠN ĐO LƯỜNG ∆EVE CHUẨN HOÁ BASEL             │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ GIAI ĐOẠN 1: PHÂN LOẠI VỊ THẾ BẢNG CÂN ĐỐI THEO 3 NHÓM KHẢ NĂNG CHUẨN HOÁ   │
│ • Có thể chuẩn hoá (Amenable)                                               │
│ • Ít có khả năng chuẩn hoá (Less amenable: bóc tách quyền chọn tự động)     │
│ • Không thể chuẩn hoá (Not amenable: NMDs, Prepayment, Early Redemption)    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ GIAI ĐOẠN 2: PHÂN BỔ DÒNG TIỀN DANH NGHĨA VÀO 19 DẢI KỲ HẠN CHUẨN HOÁ        │
│ • Phân bổ tài sản, nợ (loại trừ CET1) và ngoại bảng vào 19 điểm giữa tk    │
│ • Áp dụng trần NMDs Table 2, scalar trả trước γi, scalar rút sớm ui         │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ GIAI ĐOẠN 3: TÍNH TOÁN ∆EVE CHO TỪNG KỊCH BẢN SỐC VÀ TỪNG LOẠI TIỀN TỆ       │
│ • Chiết khấu dòng tiền liên tục DF(tk) = exp(-R(tk) * tk)                   │
│ • Xác định ∆EVE_stage3 = EVE_0 - EVE_i cho mỗi kịch bản i và đồng tiền c    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ GIAI ĐOẠN 4: TÍNH GIÁ TRỊ GIA TĂNG QUYỀN CHỌN TỰ ĐỘNG (KAO ADD-ON)          │
│ • Định giá lại toàn bộ quyền chọn tự động (caps, floors, swaptions)         │
│ • Áp dụng kịch bản sốc lãi suất kết hợp tăng 25% biến động ngầm định        │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ GIAI ĐOẠN 5: TỔNG HỢP ĐA TIỀN TỆ VÀ XÁC ĐỊNH MỨC TỔN THẤT EVE CỰC ĐẠI        │
│ • Tổng hợp phi đối xứng đa tiền tệ: ∆EVE_i = ∑_c max(0, ∆EVE_{i,c})         │
│ • Thước đo rủi ro tổng thể: ∆EVE* = max_{i=1..6} ∆EVE_i                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### Chi tiết Từng Giai đoạn Kỹ thuật

#### Giai đoạn 1: Phân loại Vị thế (Position Categorisation)
Tất cả các tài sản, nợ phải trả nhạy cảm lãi suất và các khoản cam kết/phái sinh ngoại bảng trên sổ ngân hàng (xem chi tiết tại [[irrbb-balance-sheet-portfolios]]) được chia thành 3 nhóm [[src-bcbs-irrbb-2016#^irrbb-u05-1]]:
1. **Vị thế có thể chuẩn hoá (Amenable to standardisation)**: Dòng tiền và ngày tái định giá được xác định hoàn toàn theo hợp đồng, không chứa quyền chọn nhúng (ví dụ: trái phiếu coupon cố định, tiền gửi cố định không được rút sớm, khoản vay thả nổi theo lãi suất chuẩn không có cap/floor).
2. **Vị thế ít có khả năng chuẩn hoá (Less amenable to standardisation)**: Các công cụ có nhúng **quyền chọn tự động** (automatic interest rate options) như trần lãi suất (caps), sàn lãi suất (floors), quyền chọn đổi lãi suất (swaptions) [[src-bcbs-irrbb-2016#^irrbb-u05-3]]. *Quy tắc xử lý*: Bóc tách quyền chọn tự động chuyển sang Giai đoạn 4; dòng tiền cơ sở không quyền chọn được xếp vào Giai đoạn 2 như công cụ thông thường [[src-bcbs-irrbb-2016#^irrbb-u05-3]].
3. **Vị thế không thể chuẩn hoá (Not amenable to standardisation)**: Các hợp đồng bán lẻ chịu sự chi phối của hành vi khách hàng ([[behavioural-options]]):
   - Tiền gửi không kỳ hạn ([[non-maturity-deposits|NMDs]]).
   - Cho vay lãi suất cố định chịu rủi ro trả nợ trước hạn (prepayments).
   - Tiền gửi có kỳ hạn chịu rủi ro rút trước hạn (early redemption).

#### Giai đoạn 2: Phân bổ Dòng tiền vào 19 Dải kỳ hạn (Slotting into 19 Time Buckets)
Ngân hàng phải phóng chiếu tất cả các dòng tiền tái định giá danh nghĩa ([[notional-repricing-cash-flow]]; gốc và lãi tái định giá) lên **19 dải kỳ hạn chuẩn hoá** hoặc các điểm giữa của dải kỳ hạn ($t_k$) theo Bảng 1 của Section IV [[src-bcbs-irrbb-2016#^irrbb-u05-2]]; khoảng kỳ hạn và điểm giữa từng dải trong bảng dưới theo Table 1 [[src-bcbs-irrbb-2016#^irrbb-u05-25]]:
- Notional repricing cash flow gồm hoàn trả gốc, tái định giá gốc, hoặc thanh toán lãi trên phần gốc chưa hoàn trả hay chưa tái định giá; ngày của mỗi khoản là repricing date [[src-bcbs-irrbb-2016#^irrbb-u05-9]].
- Tái định giá xảy ra tại ngày sớm nhất ngân hàng hoặc đối tác được quyền đơn phương thay đổi lãi suất, hoặc ngày lãi suất thả nổi tự động thay đổi theo benchmark [[src-bcbs-irrbb-2016#^irrbb-u05-10]]. Phần spread không tái định giá phải được slot tới contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-11]].
- Công cụ thả nổi được giả định tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]]. Vị thế cố định slot theo contractual maturity; vị thế thả nổi được coi là chuỗi coupon tới lần tái định giá kế tiếp cộng một dòng par notional tại điểm giữa gần nhất với dải chứa next reset date [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]].

| Dải $k$ | Khoảng kỳ hạn | Điểm giữa dải kỳ hạn ($t_k$ tính bằng năm) |
|:---:|---|:---:|
| **1** | Qua đêm (Overnight - O/N) | 0.0028 năm (1 ngày) |
| **2** | > O/N đến 1 tháng | 0.0417 năm |
| **3** | > 1 tháng đến 3 tháng | 0.1667 năm |
| **4** | > 3 tháng đến 6 tháng | 0.3750 năm |
| **5** | > 6 tháng đến 9 tháng | 0.6250 năm |
| **6** | > 9 tháng đến 1 năm | 0.8750 năm |
| **7** | > 1 năm đến 1.5 năm | 1.2500 năm |
| **8** | > 1.5 năm đến 2 năm | 1.7500 năm |
| **9** | > 2 năm đến 3 năm | 2.5000 năm |
| **10** | > 3 năm đến 4 năm | 3.5000 năm |
| **11** | > 4 năm đến 5 năm | 4.5000 năm |
| **12** | > 5 năm đến 6 năm | 5.5000 năm |
| **13** | > 6 năm đến 7 năm | 6.5000 năm |
| **14** | > 7 năm đến 8 năm | 7.5000 năm |
| **15** | > 8 năm đến 9 năm | 8.5000 năm |
| **16** | > 9 năm đến 10 năm | 9.5000 năm |
| **17** | > 10 năm đến 15 năm | 12.5000 năm |
| **18** | > 15 năm đến 20 năm | 17.5000 năm |
| **19** | > 20 năm | 25.0000 năm |

##### Quy tắc phân bổ đặc thù:
- **Loại trừ Vốn chủ sở hữu**: Toàn bộ vốn cổ phần phổ thông Cấp 1 (CET1) bị loại trừ khỏi bảng cân đối khi phóng chiếu dòng tiền [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Tiền gửi không kỳ hạn ([[non-maturity-deposits|NMDs]])**: Phân tách thành tiền gửi phi lõi (đưa 100% vào Dải 1 qua đêm) và tiền gửi lõi (phân bổ theo danh mục tái lập nhưng không được vượt trần tỷ lệ và kỳ hạn bình quân tại Table 2: Bán lẻ giao dịch trần 90% & 5 năm; Bán lẻ phi giao dịch trần 70% & 4.5 năm; Bán buôn trần 50% & 4 năm) [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
- **Cho vay có trả nợ trước hạn ([[behavioural-options]])**: Điều chỉnh tỷ lệ trả trước theo hệ số $\gamma_i$ (0.8 khi lãi suất tăng; 1.2 khi lãi suất giảm) [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
- **Tiền gửi rút sớm ([[behavioural-options]])**: Điều chỉnh tỷ lệ rút sớm theo hệ số $u_i$ (1.2 khi lãi suất tăng; 0.8 khi lãi suất giảm) [[src-bcbs-irrbb-2016#^irrbb-u05-6]].

Dòng tiền thuần tái định giá tại mỗi dải $k$, đồng tiền $c$, dưới kịch bản $i$ là:

$$
CF_{i,c}(k) = CF_{A,i,c}(k) - CF_{L,i,c}(k) + CF_{\text{OBS},i,c}(k)
$$

#### Giai đoạn 3: Tính toán $\Delta\text{EVE}$ Cơ sở
Tại mỗi loại tiền tệ trọng yếu $c$ và kịch bản sốc $i$, dòng tiền dương và âm trong mỗi dải được bù trừ thành một vị thế ròng $CF_{i,c}(k)$ [[src-bcbs-irrbb-2016#^irrbb-u05-17]]; vị thế ròng được chiết khấu bằng **thừa số chiết khấu liên tục (continuous discount factors)**, với $R_{i,c}(t_k)$ phản ánh kịch bản $i$ theo Annex 2 [[src-bcbs-irrbb-2016#^irrbb-u05-18]]:

$$
DF_{i,c}(t_k) = \exp\left(-R_{i,c}(t_k) \cdot t_k\right)
$$

[[src-bcbs-irrbb-2016#^irrbb-u05-18]]

Lãi suất chiết khấu là risk-free zero coupon rate, hoặc risk-free rate cộng commercial margin và spread component nếu ngân hàng đã đưa các phần này vào dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-19]].

*Diễn giải:* có thể tách $R_{i,c}(t_k) = R_{0,c}(t_k) + \Delta R_{i,c}(t_k)$, trong đó $R_{0,c}$ là đường cong hiện tại và $\Delta R_{i,c}$ là biên độ sốc từ [[standardised-interest-rate-shocks]]. Nguồn không viết công thức tách này.

Giá trị EVE không gồm quyền chọn tự động ($\text{EVE}^{\text{nao}}$) theo cấu trúc kỳ hạn hiện tại và sau sốc:

$$
\text{EVE}_{0,c}^{\text{nao}} = \sum_{k=1}^{K} CF_{0,c}(k) \cdot DF_{0,c}(t_k)
$$

$$
\text{EVE}_{i,c}^{\text{nao}} = \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k)
$$

[[src-bcbs-irrbb-2016#^irrbb-u05-20]]

Biến động EVE Giai đoạn 3 (quy ước dương là tổn thất):

$$
\Delta\text{EVE}_{\text{stage3},i,c} = \text{EVE}_{0,c}^{\text{nao}} - \text{EVE}_{i,c}^{\text{nao}}
$$

[[src-bcbs-irrbb-2016#^irrbb-u05-21]]

Giả định của bước này:
- Intra-bucket mismatch: dòng tiền khác ngày đáo hạn nhưng cùng dải được giả định khớp hoàn toàn; rủi ro này được giảm nhờ dùng $K = 19$ dải [[src-bcbs-irrbb-2016#^irrbb-u05-22]].
- Tuỳ cách xử lý NMD, prepayment và behavioural option nhúng, notional repricing cash flow có thể khác nhau theo kịch bản $i$ [[src-bcbs-irrbb-2016#^irrbb-u05-23]].

#### Giai đoạn 4: Giá trị Gia tăng Quyền chọn Tự động ($\text{KAO}_{i,c}$ Add-on)
Đối với các quyền chọn tự động đã bóc tách từ Giai đoạn 1, ngân hàng định giá lại toàn bộ các hợp đồng theo mô hình định giá quyền chọn chuẩn (Black-Scholes, Hull-White) [[src-bcbs-irrbb-2016#^irrbb-u05-7]]:
- Áp dụng đường cong lãi suất sau sốc của kịch bản $i$.
- **Cộng thêm mức tăng độ biến động ngầm định tương đối 25%** ($\sigma_{\text{new}} = 1.25 \cdot \sigma_{\text{base}}$) nhằm phản ánh sự gia tăng bất định thị trường khi lãi suất biến động mạnh [[src-bcbs-irrbb-2016#^irrbb-u05-7]].

Công thức tính giá trị gia tăng $\text{KAO}_{i,c}$:

$$
\text{KAO}_{i,c} = \sum_{o=1}^{n_c} \Delta \text{FVAO}_{i,c}^o - \sum_{q=1}^{m_c} \Delta \text{FVAO}_{i,c}^q
$$

Trong đó $\Delta\text{FVAO}_{i,c}^o$ là biến động giá trị hợp lý của quyền chọn bán (sold options - ngân hàng có nghĩa vụ thanh toán), và $\Delta\text{FVAO}_{i,c}^q$ là biến động giá trị hợp lý của quyền chọn mua (bought options - quyền chọn ngân hàng nắm giữ để phòng hộ) [[src-bcbs-irrbb-2016#^irrbb-u05-7]].

Tổng tổn thất EVE cho đồng tiền $c$ dưới kịch bản $i$ là:

$$
\Delta\text{EVE}_{i,c} = \Delta\text{EVE}_{\text{stage3},i,c} + \text{KAO}_{i,c}
$$

#### Giai đoạn 5: Tổng hợp Đa tiền tệ và Xác định Tổn thất Cực đại
Ngân hàng thực hiện tổng hợp rủi ro qua toàn bộ các đồng tiền trọng yếu và 6 kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-u05-8]]. Cơ quan giám sát quốc gia được phép quy định cách gộp tiền tệ khác, nếu chứng minh được bằng bằng chứng rằng cách đó vẫn phù hợp khẩu vị IRRBB của jurisdiction [[src-bcbs-irrbb-2016#^irrbb-u05-24]]:

##### Quy tắc tổng hợp đa tiền tệ phi đối xứng (Asymmetric Aggregation)
Basel quy định nghiêm ngặt: **Các khoản lãi EVE (tức $\Delta\text{EVE} < 0$) ở một loại tiền tệ không được phép bù trừ cho các khoản lỗ EVE ($\Delta\text{EVE} > 0$) ở loại tiền tệ khác** [[src-bcbs-irrbb-2016#^irrbb-u05-8]]:

$$
\Delta\text{EVE}_i = \sum_{c} \max\left(0,\; \Delta\text{EVE}_{i,c}\right)
$$

*Ý nghĩa kinh tế*: Khi khủng hoảng thị trường xảy ra, tương quan giữa các đồng tiền có thể bị phá vỡ hoàn toàn, và thanh khoản giữa các đồng tiền không thể chuyển giao tự do tức thời. Quy tắc phi đối xứng ngăn chặn ngân hàng làm đẹp số liệu rủi ro tổng hợp.

##### Thước đo EVE Chuẩn hoá Toàn diện ($\Delta\text{EVE}^*$)
Thước đo rủi ro EVE tổng thể là tổn thất lớn nhất trong số 6 kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-u05-8]]:

$$
\Delta\text{EVE}^* = \max_{i=1..6} \Delta\text{EVE}_i = \max_{i=1..6} \left[ \sum_{c} \max\left(0,\; \Delta\text{EVE}_{i,c}\right) \right]
$$

Giá trị $\Delta\text{EVE}^*$ này là đầu vào của phép thử ngân hàng ngoại lai ([[outlier-bank-test]]): phép thử 15% Tier 1 là should theo par 88 [[src-bcbs-irrbb-2016#^irrbb-p12-1]]; ngân hàng bị xác định là outlier được coi là có khả năng mang IRRBB quá mức và phải được rà soát [[src-bcbs-irrbb-2016#^irrbb-p12-4]].

---

## Output & usage

### Mối liên hệ Hệ thống trong ALM

1. **Ràng buộc an toàn vốn Trụ cột 2**: Kết quả $\Delta\text{EVE}^*$ chuẩn hoá là tấm gương phản chiếu mức độ rủi ro cơ cấu của bảng cân đối. Khi ngân hàng bị cơ quan giám sát chỉ trích IMS và áp đặt Khuôn khổ chuẩn hoá, các giả định bảo thủ (đặc biệt là trần kỳ hạn NMDs và quy tắc tổng hợp phi đối xứng) sẽ làm $\Delta\text{EVE}$ vọt lên, đe dọa trực tiếp giới hạn 15% Vốn cấp 1 [[outlier-bank-test]].
2. **Kích hoạt tái cơ cấu danh mục HQLA**: Vì danh mục [[hqla]] nắm giữ nhiều trái phiếu chính phủ Level 1 dài hạn có thời lượng lớn, dòng tiền của HQLA rơi vào các Dải 10–19 (kỳ hạn $> 3$ năm đến 25 năm). Dưới công thức chiết khấu liên tục $DF_{i,c}(t_k)$, các dải này chịu mức chiết khấu lũy thừa cực lớn khi lãi suất tăng, đòi hỏi Treasury phải sử dụng các hợp đồng hoán đổi lãi suất (IRS) nhận lãi suất thả nổi để triệt tiêu dòng tiền tại các dải dài hạn [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
3. **Phối hợp LCR – NSFR – IRRBB**: Xem phân tích chuyên sâu tại [[irrbb-alm-governance-strategy-and-tradeoffs]] và [[integrated-alm-liquidity-strategy]].

## Hạn chế & validation

### Bảng so sánh: Khuôn khổ Chuẩn hoá vs. Mô hình Nội bộ (IMS)

| Tiêu chí | Khuôn khổ Chuẩn hoá (Standardised Framework) | Mô hình Đo lường Nội bộ (Internal Measurement System - IMS) |
|---|---|---|
| **Mục đích sử dụng** | Thước đo dự phòng giám sát (Principle 11), công bố Trụ cột 3, Outlier Test | Quản trị điều hành ALM tác nghiệp, lập kế hoạch kinh doanh, ICAAP (Principle 9) |
| **Phân bổ dòng tiền** | 19 dải kỳ hạn cố định, điểm giữa $t_k$ chuẩn | Dải kỳ hạn linh hoạt theo ngày/tuần thực tế, dòng tiền chính xác |
| **Giả định NMDs** | Bắt buộc tuân thủ trần Table 2 (tỷ lệ lõi 50%–90%, kỳ hạn tối đa 4–5 năm) | Mô hình hoá kinh tế lượng nội bộ (Replicating Portfolio, Cointegration, Logit/Probit) |
| **Quyền chọn hành vi** | Áp dụng hệ số nhân cứng ($\gamma_i = 0.8/1.2$, $u_i = 1.2/0.8$) | Đường cong CPR động phụ thuộc tỷ lệ chênh lệch lãi suất thị trường (incentive function) |
| **Quyền chọn tự động** | Bóc tách riêng, cộng biến động ngầm định 25% ($\text{KAO}$) | Tích hợp trực tiếp vào mô hình Monte Carlo mô phỏng đường cong lãi suất đa yếu tố |
| **Tổng hợp đa tiền tệ** | Bắt buộc phi đối xứng: $\sum \max(0, \Delta\text{EVE}_{i,c})$ | Có thể tính đến tương quan lịch sử đa tiền tệ trong mô hình VaR/EVE nội bộ |

---

## Đề xuất cập nhật
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đề xuất thêm cite cho câu phóng chiếu dòng tiền tái định giá (dòng 89): định nghĩa CF(t) và repricing date [[src-bcbs-irrbb-2016#^irrbb-u05-9]], thời điểm tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-10]], spread không tái định giá slot tới contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-11]], công cụ thả nổi tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]], quy tắc slot fixed và floating [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]]. → đã áp [2026-10-19]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; đề xuất link ở lần nhắc đầu "dòng tiền tái định giá danh nghĩa" (dòng 89). → đã áp [2026-10-19]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 105, 132): (1) dòng 126 cite [[src-bcbs-irrbb-2016#^irrbb-u05-1]] (par 100, chỉ liệt kê 5 giai đoạn) cho bước chiết khấu; đề xuất cite [[src-bcbs-irrbb-2016#^irrbb-u05-17]] (bù trừ trong dải ra CF_{i,c}(k)) và [[src-bcbs-irrbb-2016#^irrbb-u05-18]] (DF liên tục); câu "hoặc bao gồm commercial margin nếu dòng tiền đã bao gồm margin" cite [[src-bcbs-irrbb-2016#^irrbb-u05-19]]. (2) Công thức DF_i = exp(−(R_0 + ∆R_i)·t_k) ở dòng 133: nguồn chỉ viết R_{i,c}(t_k) phản ánh kịch bản i theo Annex 2 [[src-bcbs-irrbb-2016#^irrbb-u05-18]]; cách tách R_0 + ∆R nên đặt dưới *Diễn giải:*. (3) Công thức EVE_{0,c}, EVE_{i,c} (dòng 141–145) và ∆EVE (dòng 150–170) cite [[src-bcbs-irrbb-2016#^irrbb-u05-20]], [[src-bcbs-irrbb-2016#^irrbb-u05-21]]; nguồn viết Σ tới K và gọi là EVE^nao (không gồm quyền chọn tự động). (4) Giai đoạn 5: thêm ngoại lệ cơ quan giám sát quốc gia được quy định cách gộp tiền tệ khác [[src-bcbs-irrbb-2016#^irrbb-u05-24]]. (5) Có thể thêm giả định intra-bucket mismatch [[src-bcbs-irrbb-2016#^irrbb-u05-22]] và CF phụ thuộc kịch bản [[src-bcbs-irrbb-2016#^irrbb-u05-23]]. → đã áp [2026-10-19]
- [2026-10-19] review (đối chiếu Table 1, ^irrbb-u05-25) — user duyệt [2026-10-19]: (1) bảng 19 dải ở Giai đoạn 2, dải 6 (9M–1Y) ghi điểm giữa 0.7917 năm; raw ghi 0.875Y [[src-bcbs-irrbb-2016#^irrbb-u05-25]]. Đề xuất sửa thành 0.8750 và cite u05-25 cho bảng. (2) Câu "nếu ∆EVE* > 15% Tier 1 Capital, ngân hàng chính thức bị xác định là ngân hàng ngoại lai" mâu thuẫn với [[outlier-bank-test]] đã sửa [2026-10-18]: phép thử 15% Tier 1 là should (par 88), outlier bị coi là có khả năng mang IRRBB quá mức và phải được rà soát [[src-bcbs-irrbb-2016#^irrbb-p12-4]]. Đề xuất viết lại theo cách đó. → đã áp [2026-10-19]
