---
title: "Phương Pháp Đo Lường EVE và NII Dưới Các Kịch Bản Sốc Lãi Suất Chuẩn Hóa"
aliases: [IRRBB Standardised Shocks Measurement, Đo lường EVE và NII theo kịch bản sốc, EVE and NII Standardised Measurement, 6 kịch bản sốc lãi suất Basel, Parallel Steepener Flattener Measurement]
type: synthesis
domains: [alm, basel]
status: active
maturity: draft
origin: research
question: "Phương pháp đo lường Giá trị kinh tế của vốn chủ sở hữu (EVE) và Độ nhạy thu nhập lãi thuần (NII) dưới các kịch bản sốc lãi suất chuẩn hóa (Parallel, Steepener, Flattener) được thực hiện như thế nào theo chuẩn mực BCBS d368 và phân tích của Fidelio Tata?"
as_of: 2026-10-17
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: drives, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: drives, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p08-3]]"}
  - {type: input-to, to: "[[standardised-interest-rate-shocks]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u07-1]]"}
  - {type: input-to, to: "[[irrbb-standardised-framework]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-8]]"}
  - {type: input-to, to: "[[outlier-bank-test]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
tags: [irrbb, eve, nii, standardised-shocks, parallel-shock, steepener, flattener, time-buckets, kao, outlier-test, synthesis]
updated: 2026-10-17
reviewed:
---

## Câu hỏi

- **Q1**: Phương pháp đo lường Giá trị kinh tế của vốn chủ sở hữu ($\Delta\text{EVE}$) dưới 6 kịch bản sốc chuẩn hóa được thực hiện như thế nào (chiết khấu dòng tiền 19 dải kỳ hạn, giả định run-off, phụ trội quyền chọn tự động $KAO$, tổng hợp đa tiền tệ và ngưỡng ngoại lai 15% Tier 1 Capital)?
- **Q2**: Phương pháp đo lường Độ nhạy thu nhập lãi thuần ($\Delta\text{NII}$) dưới các kịch bản sốc chuẩn hóa được xây dựng như thế nào (khung thời gian 12 tháng, giả định constant balance sheet vs dynamic balance sheet và nén biên lãi ròng NIM)?
- **Q3**: Cấu trúc toán học và tham số của 6 kịch bản sốc lãi suất chuẩn hóa Basel (Parallel up/down, Steepener, Flattener, Short rate up/down) được xác định như thế nào (hàm suy giảm xoay trục $e^{-t_k/4}$, ma trận biên độ sốc theo đồng tiền, hệ thống sàn 100 bps và trần biên độ)?

---

## Kết luận

1. **Về phương pháp đo lường $\Delta\text{EVE}$ (Q1)**:
   - Được đo lường qua quy trình 5 giai đoạn chuẩn hóa của Basel d368 [[src-bcbs-irrbb-2016#^irrbb-u05-1]]: toàn bộ dòng tiền tái định giá danh nghĩa (trừ vốn CET1) được phân bổ vào 19 dải kỳ hạn chuẩn hóa [[src-bcbs-irrbb-2016#^irrbb-u05-2]] theo giả định bảng cân đối co cụm (*run-off balance sheet*, không tính tài sản/công nợ mới) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Dòng tiền được chiết khấu liên tục theo đường cong phi rủi ro sau sốc [[src-tata-bank-alm#^tata-ev-1]].
   - Quyền chọn tự động được bóc tách khỏi dòng tiền cơ sở và tính riêng thành phụ trội rủi ro $\text{KAO}_{i,c}$ với mức tăng độ biến động 25% [[src-bcbs-irrbb-2016#^irrbb-u05-3]] [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
   - Thước đo tổn thất tổng thể là mức sụt giảm EVE cực đại qua 6 kịch bản sau khi cộng dồn các khoản lỗ giữa các đồng tiền trọng yếu [[src-bcbs-irrbb-2016#^irrbb-u05-8]], chịu sự giám sát qua Phép thử ngoại lai (ngưỡng cảnh báo $\max \Delta\text{EVE} > 15\%$ Vốn cấp 1) [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
2. **Về phương pháp đo lường $\Delta\text{NII}$ (Q2)**:
   - Được đo lường trong khung thời gian 12 tháng liên tục dưới 2 kịch bản sốc song song (Parallel up / Parallel down) [[src-bcbs-irrbb-2016#^irrbb-u07-1]] [[src-bcbs-irrbb-2016#^irrbb-p08-1]].
   - Chuẩn mực quy định áp dụng giả định bảng cân đối tĩnh (*constant balance sheet* — tài sản và nợ đáo hạn được tái đầu tư với cùng kỳ hạn, cơ cấu và biên thương mại) để đảm bảo tính so sánh, hoặc mô hình động (*dynamic balance sheet*) phản ánh kế hoạch kinh doanh nội bộ [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Biến động thu nhập phản ánh trực tiếp qua khe hở tái định giá $\Delta\text{NII} \approx \text{Gap} \times \Delta r$ và nén biên lãi ròng NIM [[src-tata-bank-alm#^tata-nii-1]].
3. **Về cấu trúc 6 kịch bản sốc chuẩn hóa (Q3)**:
   - Bao gồm 2 sốc song song (Parallel up/down), 2 sốc xoay trục (Steepener/Flattener) và 2 sốc ngắn hạn (Short rate up/down) [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. Sốc xoay trục áp dụng hàm suy giảm sốc ngắn hạn $S_{\text{short}}(t_k) = e^{-t_k/4}$ với tham số $x=4$ [[src-bcbs-irrbb-2016#^irrbb-u07-3]].
   - Biên độ sốc được xác định riêng cho từng đồng tiền dựa trên phân vị lịch sử (Table 1 Annex 2), kiểm soát bởi mức sàn tối thiểu 100 bps và trần biên độ (500 bps ngắn hạn, 400 bps song song, 300 bps dài hạn) [[src-bcbs-irrbb-2016#^irrbb-u07-2]] [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
   - *Lưu ý tuân thủ tại Việt Nam*: Hiện wiki chưa có nguồn văn bản quy định của NHNN về biên độ sốc chuẩn hóa cho đồng VND và phương pháp đo lường bắt buộc (chờ ingest `src-tt83-2025-nhnn` unit `PL5` và `C3-M7`).

---

## Cơ chế

### Q1 — Phương pháp đo lường Giá trị kinh tế (ΔEVE) dưới 6 kịch bản sốc chuẩn hóa

Khuôn khổ chuẩn hóa Section IV của BCBS d368 quy định đo lường $\Delta\text{EVE}$ qua 5 giai đoạn chặt chẽ [[src-bcbs-irrbb-2016#^irrbb-u05-1]]:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    QUY TRÌNH 5 GIAI ĐOẠN ĐO LƯỜNG ΔEVE THEO BASEL d368 (SECTION IV)             │
└────────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                 │
  ┌──────────────────────────────┼──────────────────────────────┐
  ▼                              ▼                              ▼
┌──────────────────────────────┐┌──────────────────────────────┐┌──────────────────────────────┐
│  BƯỚC 1: PHÂN LOẠI VỊ THẾ    ││ BƯỚC 2: PHÂN BỔ DÒNG TIỀN    ││ BƯỚC 3: TÍNH TOÁN ΔEVE       │
├──────────────────────────────┤├──────────────────────────────┤├──────────────────────────────┤
│• Chuẩn hóa được (Fixed/Float)││• 19 dải kỳ hạn (Table 1)     ││• Chiết khấu đường cong sốc   │
│• Ít chuẩn hóa (CASA, Prepay) ││• Bảng cân đối Run-off        ││• Không tính vốn tự có CET1   │
│• Không chuẩn hóa (Auto option)││• Dòng tiền danh nghĩa gốc/lãi││• Tính riêng từng đồng tiền c │
└──────────────────────────────┘└──────────────────────────────┘└──────────────────────────────┘
                                 │
  ┌──────────────────────────────┴──────────────────────────────┐
  ▼                                                             ▼
┌──────────────────────────────────────────────────────────────┐┌──────────────────────────────┐
│  BƯỚC 4: TÍNH PHỤ TRỘI QUYỀN CHỌN TỰ ĐỘNG (KAO ADD-ON)        ││ BƯỚC 5: TỔNG HỢP VÀ SO NGƯỠNG│
├──────────────────────────────────────────────────────────────┤├──────────────────────────────┤
│• Bóc tách Caps/Floors khỏi dòng tiền cơ sở                   ││• Cộng dồn lỗ các đồng tiền c │
│• Định giá Black-76 / Hull-White dưới sốc + 25% biến động ngầm││• Chọn kịch bản lỗ cực đại    │
│• KAO = Tổn thất quyền chọn bán - Quyền chọn mua phòng ngừa   ││• So sánh với 15% Vốn cấp 1   │
└──────────────────────────────────────────────────────────────┘└──────────────────────────────┘
```

1. **Phân loại vị thế và slotting vào 19 dải kỳ hạn**:
   - Tài sản, công nợ nhạy cảm lãi suất và vị thế ngoại bảng được phân bổ vào 19 dải kỳ hạn (hoặc điểm giữa của 19 dải kỳ hạn, từ qua đêm đến $\ge 20$ năm) theo ngày định giá lại kế tiếp (*reset date*) hoặc kỳ hạn hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-2]] [[src-tata-bank-alm#^tata-gap-1]].
   - Áp dụng giả định bảng cân đối co cụm (*run-off balance sheet*): dòng tiền hiện hữu đáo hạn và không được thay thế bằng tài sản hay khoản nợ mới [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Toàn bộ vốn cổ phần phổ thông cấp 1 (CET1) bị loại trừ khỏi dòng tiền chiết khấu [[src-bcbs-irrbb-2016#^irrbb-u05-2]] [[src-tata-bank-alm#^tata-nii-5]].
2. **Chiết khấu và tính biến động $\Delta\text{EVE}_{i,c}$**:
   - Dòng tiền ròng trong từng dải kỳ hạn $k$ ($CF_{k,c}$) được chiết khấu theo yếu tố chiết khấu sau sốc $DF_{i,c}(t_k) = \exp(-R_{i,c}(t_k) \cdot t_k)$ so với yếu tố chiết khấu cơ sở $DF_{0,c}(t_k)$ [[src-tata-bank-alm#^tata-ev-1]]:
     $$\Delta\text{EVE}_{i,c}^{\text{base}} = \sum_{k=1}^{19} CF_{k,c} \cdot \left[ DF_{i,c}(t_k) - DF_{0,c}(t_k) \right]$$
3. **Phụ trội quyền chọn tự động ($\text{KAO}_{i,c}$)**:
   - Các quyền chọn nhúng tự động (caps/floors) bắt buộc phải bóc tách khỏi dòng tiền cơ sở [[src-bcbs-irrbb-2016#^irrbb-u05-3]]. Giá trị gia tăng $\text{KAO}_{i,c}$ được định giá theo mô hình quyền chọn chuẩn với giả định độ biến động ngầm định tăng tương đối 25% [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
4. **Tổng hợp đa tiền tệ và Phép thử ngoại lai (Supervisory Outlier Test)**:
   - Tổn thất EVE tổng hợp dưới kịch bản $i$ được tính bằng cách cộng dồn các khoản lỗ giữa các đồng tiền trọng yếu (chiếm $\ge 5\%$ bảng cân đối), trong đó phần bù lãi từ đồng tiền khác chỉ được bù trừ một phần [[src-bcbs-irrbb-2016#^irrbb-u05-8]]:
     $$\text{EVE Loss}_i = \max\left( 0, \sum_{c} \max\left( \Delta\text{EVE}_{i,c}, -0.5 \cdot \max(0, -\Delta\text{EVE}_{i,c}) \right) \right)$$
   - Thước đo rủi ro chuẩn hóa tổng thể: $\Delta\text{EVE}^* = \max_{i=1..6} (\text{EVE Loss}_i)$ [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
   - **Phép thử ngoại lai**: Nếu $\Delta\text{EVE}^* > 15\%$ Vốn cấp 1 (Tier 1 Capital), ngân hàng bị xác định là ngân hàng ngoại lai (*outlier bank*), kích hoạt nghĩa vụ can thiệp giám sát bắt buộc (tăng vốn hoặc phòng hộ giảm phơi nhiễm) [[src-bcbs-irrbb-2016#^irrbb-p12-1]] [[src-bcbs-irrbb-2016#^irrbb-p12-3]].

---

### Q2 — Phương pháp đo lường Độ nhạy thu nhập lãi thuần (ΔNII) dưới kịch bản sốc chuẩn hóa

1. **Khung thời gian và Kịch bản sốc áp dụng**:
   - Thước đo $\Delta\text{NII}$ lượng hóa biến động của thu nhập lãi thuần dồn tích trong khoảng thời gian ngắn hạn, tiêu chuẩn là **12 tháng liên tục** (1-year horizon) [[src-bcbs-irrbb-2016#^irrbb-p08-1]] [[src-choudhry-principles-banking#^choudhry-irrbb-3]].
   - Theo chuẩn Basel d368, ngân hàng bắt buộc áp dụng **2 kịch bản sốc song song (Parallel up và Parallel down)** cho đo lường $\Delta\text{NII}$ công bố Trụ cột 3 [[src-bcbs-irrbb-2016#^irrbb-u07-1]].
2. **Giả định Bảng cân đối kế toán (Balance Sheet Assumptions)**:
   - **Constant Balance Sheet (Bảng cân đối tĩnh)**: Tổng quy mô và cơ cấu tài sản, nợ phải trả được duy trì cố định; các khoản mục đáo hạn trong 12 tháng được tái đầu tư bằng các công cụ cùng loại, cùng kỳ hạn gốc và cùng biên thương mại (*commercial margin*) [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Đây là giả định chuẩn hóa bắt buộc nhằm triệt tiêu yếu tố chủ quan trong công bố thông tin giám sát [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
   - **Dynamic Balance Sheet (Bảng cân đối động)**: Cho phép kết hợp dự phóng tăng trưởng tín dụng, thay đổi cơ cấu huy động và phản ứng điều hành giá của ban điều hành [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Áp dụng cho quản trị nội bộ ALCO nhưng không thay thế chuẩn tĩnh khi báo cáo thanh tra.
3. **Cơ chế tính toán qua Khe hở tái định giá**:
   - $\Delta\text{NII}$ được xác định bằng tích của khe hở tái định giá lũy kế ($\text{Net Repricing Gap}_k$) trong từng khoảng thời gian với biên độ sốc lãi suất $\Delta R$ và độ dài thời gian chịu tác động còn lại trong năm ($1 - \tau_k$) [[src-tata-bank-alm#^tata-nii-1]]:
     $$\Delta\text{NII} = \sum_{k=1}^{M} \text{Gap}_k \cdot \Delta R \cdot (1 - \tau_k)$$
   - Phản ánh hiện tượng co hẹp biên lãi ròng (**NIM Compression**): khi lãi suất tăng mà bảng cân đối có khe hở âm ($\text{Gap} < 0$), chi phí nợ tái định giá tăng nhanh hơn thu nhập từ tài sản, làm xói mòn lợi nhuận ròng [[src-tata-bank-alm#^tata-nii-1]].

---

### Q3 — Cấu trúc toán học và tham số của 6 kịch bản sốc lãi suất chuẩn hóa Basel

Ủy ban Basel (Annex 2 d368) thiết lập 6 kịch bản sốc lãi suất tiêu chuẩn áp dụng cho từng loại tiền tệ trọng yếu [[src-bcbs-irrbb-2016#^irrbb-u07-1]] [[src-bcbs-irrbb-2016#^irrbb-u07-2]]:

| Kịch bản sốc ($i$) | Loại hình sốc | Diễn biến đường cong lãi suất | Áp dụng đo lường |
| :--- | :--- | :--- | :--- |
| **1. Parallel up** | Song song tăng | Lãi suất tăng đều cùng biên độ $\Delta R_{\text{parallel},c}$ tại mọi kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. | EVE và NII [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| **2. Parallel down** | Song song giảm | Lãi suất giảm đều cùng biên độ $\Delta R_{\text{parallel},c}$ tại mọi kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. | EVE và NII [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| **3. Steepener** | Xoay trục dốc lên | Lãi suất ngắn hạn giảm, lãi suất dài hạn tăng [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. | EVE [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| **4. Flattener** | Xoay trục phẳng đi | Lãi suất ngắn hạn tăng, lãi suất dài hạn giảm [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. | EVE [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| **5. Short rate up** | Ngắn hạn tăng | Lãi suất ngắn hạn tăng mạnh và suy giảm dần theo kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. | EVE [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| **6. Short rate down** | Ngắn hạn giảm | Lãi suất ngắn hạn giảm mạnh và suy giảm dần theo kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. | EVE [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |

#### 1. Công thức sốc xoay trục đường cong (Rotation Shocks):
Biên độ sốc tại từng điểm kỳ hạn $t_k$ được tính toán qua hàm suy giảm sốc ngắn hạn $S_{\text{short}}(t_k) = e^{-t_k / 4}$ và hàm sốc dài hạn $S_{\text{long}}(t_k) = 1 - S_{\text{short}}(t_k)$ [[src-bcbs-irrbb-2016#^irrbb-u07-3]]:
- **Sốc Steepener**:
  $$\Delta R_{\text{steepener},c}(t_k) = -0.65 \cdot |\Delta R_{\text{short},c}| \cdot S_{\text{short}}(t_k) + 0.9 \cdot |\Delta R_{\text{long},c}| \cdot S_{\text{long}}(t_k)$$ [[src-bcbs-irrbb-2016#^irrbb-u07-3]]
- **Sốc Flattener**:
  $$\Delta R_{\text{flattener},c}(t_k) = +0.8 \cdot |\Delta R_{\text{short},c}| \cdot S_{\text{short}}(t_k) - 0.6 \cdot |\Delta R_{\text{long},c}| \cdot S_{\text{long}}(t_k)$$ [[src-bcbs-irrbb-2016#^irrbb-u07-3]]

#### 2. Ma trận biên độ sốc theo đồng tiền và Hệ thống Sàn / Trần (Table 1 Annex 2):
- **Biên độ sốc quy định theo đồng tiền** [[src-bcbs-irrbb-2016#^irrbb-u07-2]]:
  - **USD**: Parallel = 200 bps; Short = 300 bps; Long = 150 bps [[src-bcbs-irrbb-2016#^irrbb-u07-2]].
  - **EUR**: Parallel = 200 bps; Short = 250 bps; Long = 100 bps [[src-bcbs-irrbb-2016#^irrbb-u07-2]].
  - **JPY**: Parallel = 100 bps; Short = 100 bps; Long = 100 bps [[src-bcbs-irrbb-2016#^irrbb-u07-2]].
- **Hệ thống sàn (Floor) và trần (Caps) bảo vệ** [[src-bcbs-irrbb-2016#^irrbb-u07-4]]:
  - Mức sàn biên độ sốc tối thiểu: **100 bps** cho mọi loại tiền tệ [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
  - Trần biên độ sốc tối đa: **500 bps** cho ngắn hạn, **400 bps** cho song song, **300 bps** cho dài hạn [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
  - Cơ quan giám sát quốc gia có quyền quyết định áp dụng mức sàn không âm hoặc sàn âm cho lãi suất sau sốc [[src-bcbs-irrbb-2016#^irrbb-u07-4]].

---

## Bằng chứng ủng hộ

- **Basel Committee on Banking Supervision (BCBS d368)**: Thiết lập chuẩn hóa toàn bộ cấu trúc 5 giai đoạn đo lường EVE [[src-bcbs-irrbb-2016#^irrbb-u05-1]], nguyên tắc công bố thông tin Trụ cột 3 (Table B) [[src-bcbs-irrbb-2016#^irrbb-p08-1]], Phép thử ngoại lai 15% Vốn cấp 1 [[src-bcbs-irrbb-2016#^irrbb-p12-1]] và đặc tả toán học chi tiết 6 kịch bản sốc đường cong tại Annex 2 [[src-bcbs-irrbb-2016#^irrbb-u07-1]] [[src-bcbs-irrbb-2016#^irrbb-u07-3]].
- **Fidelio Tata (2025)**: Chứng minh nền tảng giải tích của giá trị kinh tế qua chiết khấu dòng tiền [[src-tata-bank-alm#^tata-ev-1]], nguyên tắc $PV = Par$ tại Reset Date triệt tiêu rủi ro định giá ngoài kỳ hạn ngắn [[src-tata-bank-alm#^tata-gap-2]], và mô hình Duration Gap định hình độ nhạy $\Delta\text{EVE}$ [[src-tata-bank-alm#^tata-dgap-1]].
- **Moorad Choudhry**: Khẳng định sự bắt buộc phải đo lường song hành cả EVE và NII nhằm kiểm soát đồng thời rủi ro thanh toán dài hạn (solvency) và rủi ro lợi nhuận ngắn hạn (earnings volatility) [[src-choudhry-principles-banking#^choudhry-irrbb-3]].

---

## Bằng chứng trái chiều

- **Nghịch lý đánh đổi EVE vs NII (The EVE vs NII Trade-off Dilemma)**:
  - Nếu ngân hàng tìm cách triệt tiêu hoàn toàn rủi ro giá trị kinh tế ($\Delta\text{EVE} \approx 0$) bằng cách tái định giá toàn bộ tài sản và công nợ sang thả nổi ngắn hạn (matching duration ở mức tối thiểu), ngân hàng sẽ phơi nhiễm tối đa với biến động thu nhập lãi thuần $\Delta\text{NII}$ khi lãi suất thị trường thay đổi chu kỳ ngắn [[src-bcbs-irrbb-2016#^irrbb-u02-4]] [[src-tata-bank-alm#^tata-nii-11]].
  - Ngược lại, việc cố định hóa lãi suất dài hạn để khóa chặt thu nhập NII ổn định sẽ khiến giá trị kinh tế của vốn chủ sở hữu EVE biến động dữ dội dưới các kịch bản sốc xoay trục đường cong (Steepener/Flattener) [[src-tata-bank-alm#^tata-nii-11]].

---

## Phụ thuộc regime

- **Môi trường lãi suất âm hoặc siêu thấp**:
  - Kịch bản sốc song song giảm (*Parallel down*) kích hoạt cơ chế sàn lãi suất sau sốc (Post-shock interest rate floor), ngăn chặn lãi suất mô hình hóa âm vô lý [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
  - Tiền gửi bán lẻ chịu sàn lãi suất danh nghĩa 0% (Zero Lower Bound), khiến ngân hàng không thể chuyển tiếp lãi suất âm sang người gửi tiền, dẫn đến nén nghiêm trọng NIM và làm méo mó thước đo $\Delta\text{NII}$.
- **Môi trường đường cong lãi suất đảo ngược (Inverted Yield Curve)**:
  - Sốc Flattener (ngắn hạn tăng mạnh, dài hạn giảm) gây tác động kép tồi tệ nhất: vừa bóp nghẹt thu nhập lãi thuần NII trong 12 tháng, vừa làm sụt giảm EVE của các tài sản dài hạn cố định.

---

## Hàm ý ALM / quy định

- **Khung quản trị ALCO và Treasury**:
  - ALCO bắt buộc phải thiết lập hệ thống hạn mức rủi ro hai chiều độc lập: Hạn mức $\Delta\text{EVE}$ (bảo vệ an toàn vốn theo Trụ cột 2) và Hạn mức $\Delta\text{NII}$ (bảo vệ kế hoạch lợi nhuận kinh doanh).
  - Sử dụng các công cụ hoán đổi lãi suất ([[interest-rate-swap|IRS]]) và quyền chọn ([[swaption]], [[interest-rate-cap-floor]]) để phòng ngừa có chọn lọc các điểm kỳ hạn nhạy cảm cao trên 19 dải kỳ hạn thay vì chỉ phòng ngừa sốc song song.
- **Quy định pháp lý tại Việt Nam**:
  - *Chưa có nguồn quy định NHNN trong wiki*: Hiện tại wiki chưa ingest văn bản pháp quy của NHNN quy định về 6 kịch bản sốc chuẩn hóa và ngưỡng ngoại lai cho thị trường Việt Nam.
  - Chuẩn mực pháp lý chính thức dự kiến là **Thông tư 83/2025/TT-NHNN** (có hiệu lực từ 01/07/2026), trong đó quy định thẩm quyền quản trị IRRBB tại Chương 3 Mục 7 (`C3-M7`) và hướng dẫn kỹ thuật tính toán đo lường tại Phụ lục 5 (`PL5`).
  - *Diễn giải:* Các quy định của BCBS d368 hiện đóng vai trò là chuẩn mực kỹ thuật tham chiếu quốc tế. Đối với đồng VND, ngân hàng cần tuân thủ biên độ sốc và phương pháp đo lường do NHNN ban hành tại TT83.

---

## Bất định

- Biên độ sốc lãi suất chuẩn hóa áp dụng cho đồng Việt Nam (VND) trong 6 kịch bản (Parallel, Steepener, Flattener) hiện `[cần nguồn]` (chờ ingest `src-tt83-2025-nhnn` unit `PL5`).
- Ngưỡng cảnh báo ngoại lai áp dụng cho các NHTM tại Việt Nam (theo tỷ lệ % Vốn cấp 1 hoặc tỷ lệ an toàn vốn CAR) hiện `[cần nguồn]` (chờ ingest `src-tt83-2025-nhnn` unit `C3-M7` và `PL5`).

---

## Liên Kết Quan Hệ
- **Đầu vào từ**: [[repricing-balance-sheet]], [[irrbb-balance-sheet-portfolios]], [[non-maturity-deposits]]
- **Chỉ số đo lường**: [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[outlier-bank-test]]
- **Kịch bản & Mô hình**: [[standardised-interest-rate-shocks]], [[irrbb-standardised-framework]], [[key-rate-duration]], [[duration-gap-model]]
- **Quy định giám sát**: [[bcbs-irrbb]]
- **Nguồn trích dẫn**: [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]], [[src-choudhry-principles-banking]]
