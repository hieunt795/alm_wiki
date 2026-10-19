---
title: "Phương Pháp Đo Lường EVE và NII Dưới Các Kịch Bản Sốc Lãi Suất Chuẩn Hóa"
aliases: [IRRBB Standardised Shocks Measurement, Đo lường EVE và NII theo kịch bản sốc, EVE and NII Standardised Measurement, 6 kịch bản sốc lãi suất Basel, Parallel Steepener Flattener Measurement]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Phương pháp đo lường Giá trị kinh tế của vốn chủ sở hữu (EVE) và Độ nhạy thu nhập lãi thuần (NII) dưới các kịch bản sốc lãi suất chuẩn hóa (Parallel, Steepener, Flattener) được thực hiện như thế nào theo chuẩn mực BCBS d368 và phân tích của Fidelio Tata?"
as_of: 2026-10-19
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]"]
relations: []
tags: [irrbb, eve, nii, standardised-shocks, parallel-shock, steepener, flattener, time-buckets, kao, outlier-test, synthesis]
updated: 2026-10-19
reviewed:
---

## Câu hỏi

- **Q1**: Phương pháp đo lường Giá trị kinh tế của vốn chủ sở hữu ($\Delta\text{EVE}$) dưới 6 kịch bản sốc chuẩn hóa được thực hiện như thế nào (chiết khấu dòng tiền 19 dải kỳ hạn, giả định run-off, phụ trội quyền chọn tự động $KAO$, tổng hợp đa tiền tệ và ngưỡng ngoại lai 15% Tier 1 Capital)?
- **Q2**: Phương pháp đo lường Độ nhạy thu nhập lãi thuần ($\Delta\text{NII}$) dưới các kịch bản sốc chuẩn hóa được xây dựng như thế nào (khung thời gian 12 tháng, giả định constant balance sheet vs dynamic balance sheet và nén biên lãi ròng NIM)?
- **Q3**: Cấu trúc toán học và tham số của 6 kịch bản sốc lãi suất chuẩn hóa Basel (Parallel up/down, Steepener, Flattener, Short rate up/down) được xác định như thế nào (hàm suy giảm xoay trục $e^{-t_k/4}$, ma trận biên độ sốc theo đồng tiền, hệ thống sàn 100 bps và trần biên độ)?

---

## Kết luận

1. **Về phương pháp đo lường $\Delta\text{EVE}$ (Q1)**:
   - Được đo lường qua quy trình 5 giai đoạn chuẩn hóa của Basel d368 [[src-bcbs-irrbb-2016#^irrbb-u05-1]]: toàn bộ notional repricing cash flow (trừ vốn CET1) được phân bổ vào 19 dải kỳ hạn chuẩn hóa [[src-bcbs-irrbb-2016#^irrbb-u05-2]] theo giả định bảng cân đối co cụm (*run-off balance sheet*, không tính tài sản/công nợ mới) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Dòng tiền ròng của từng dải được chiết khấu bằng discount factor liên tục theo kịch bản sốc $i$ [[src-bcbs-irrbb-2016#^irrbb-u05-18]]; $\Delta\text{EVE}_{i,c}$ bằng EVE theo cấu trúc kỳ hạn hiện tại trừ EVE của kịch bản $i$, cộng $\text{KAO}_{i,c}$ [[src-bcbs-irrbb-2016#^irrbb-u05-21]].
   - Quyền chọn tự động được bỏ qua khi slot dòng tiền và tính riêng thành phụ trội rủi ro $\text{KAO}_{i,c}$ với mức tăng tương đối 25% của implicit volatility [[src-bcbs-irrbb-2016#^irrbb-u05-3]] [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
   - Thước đo rủi ro EVE là khoản lỗ lớn nhất qua 6 kịch bản, sau khi cộng các khoản lỗ $\Delta\text{EVE}_{i,c} > 0$ của các đồng tiền trọng yếu (trên 5% tài sản hoặc nợ sổ ngân hàng) [[src-bcbs-irrbb-2016#^irrbb-u05-8]]. Supervisor nên áp dụng ít nhất một outlier test so sánh $\max \Delta\text{EVE}$ với 15% Vốn cấp 1 [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
2. **Về phương pháp đo lường $\Delta\text{NII}$ (Q2)**:
   - $\Delta\text{NII}$ công bố là chênh lệch thu nhập lãi tương lai trong giai đoạn 12 tháng liên tục [[src-bcbs-irrbb-2016#^irrbb-p08-3]]; ngân hàng nên áp dụng 2 kịch bản sốc quy định cho NII [[src-bcbs-irrbb-2016#^irrbb-u07-1]] và phải công bố $\Delta\text{NII}$ dưới các kịch bản này [[src-bcbs-irrbb-2016#^irrbb-p08-1]].
   - $\Delta\text{NII}$ công bố nên được tính theo giả định bảng cân đối không đổi (*constant balance sheet*): dòng tiền đáo hạn hoặc tái định giá được thay bằng dòng tiền mới cùng số tiền, kỳ tái định giá và spread component [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Theo Tata, earning gap đo độ nhạy NII năm đầu bằng net repricing gap × cú sốc × phần còn lại của năm đầu [[src-tata-bank-alm#^tata-egap-1]].
3. **Về cấu trúc 6 kịch bản sốc chuẩn hóa (Q3)**:
   - Bao gồm 2 sốc song song (Parallel up/down), 2 sốc xoay trục (Steepener/Flattener) và 2 sốc ngắn hạn (Short rate up/down) [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. Sốc xoay trục áp dụng hàm suy giảm sốc ngắn hạn $S_{\text{short}}(t_k) = e^{-t_k/4}$ với tham số $x=4$ [[src-bcbs-irrbb-2016#^irrbb-u07-3]].
   - Biên độ sốc được xác định riêng cho từng đồng tiền dựa trên chuỗi số liệu lịch sử 2000–2015 (Table 1 Annex 2), kiểm soát bởi mức sàn tối thiểu 100 bps và trần biên độ (500 bps ngắn hạn, 400 bps song song, 300 bps dài hạn) [[src-bcbs-irrbb-2016#^irrbb-u07-2]] [[src-bcbs-irrbb-2016#^irrbb-u07-5]] [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
   - *Lưu ý tuân thủ tại Việt Nam*: Phụ lục V của [[tt83-2025]] dùng 6 kịch bản cho ΔEVE [[src-tt83-2025-nhnn#^pl5-a3-1]] và 2 kịch bản song song cho ΔNII [[src-tt83-2025-nhnn#^pl5-b3]]. Bảng 5 không có VND [[src-tt83-2025-nhnn#^pl5-c1-1]]; tham số sốc VND do ngân hàng tính theo PL5.C.I.2 [[src-tt83-2025-nhnn#^pl5-c1-2]] hoặc tự xác định theo hướng dẫn BCBS cập nhật [[src-tt83-2025-nhnn#^pl5-c2]].

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
│• Định giá lại dưới sốc + 25% implicit volatility             ││• Chọn kịch bản lỗ cực đại    │
│• KAO = Tổn thất quyền chọn bán - Quyền chọn mua phòng ngừa   ││• So sánh với 15% Vốn cấp 1   │
└──────────────────────────────────────────────────────────────┘└──────────────────────────────┘
```

1. **Phân loại vị thế và slotting vào 19 dải kỳ hạn**:
   - Mọi notional repricing cash flow của tài sản, nợ và khoản mục ngoại bảng nhạy cảm lãi suất, theo từng đồng tiền, được phân bổ vào 19 dải kỳ hạn hoặc điểm giữa dải [[src-bcbs-irrbb-2016#^irrbb-u05-2]] theo khả năng chuẩn hoá của vị thế [[src-bcbs-irrbb-2016#^irrbb-u05-16]]. Vị thế amenable to standardisation được slot theo contractual maturity nếu coupon cố định, hoặc vào kỳ tái định giá kế tiếp nếu coupon thả nổi [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-tata-bank-alm#^tata-gap-1]]; chi tiết ở [[notional-repricing-cash-flow]].
   - Áp dụng giả định bảng cân đối co cụm (*run-off balance sheet*): dòng tiền hiện hữu đáo hạn và không được thay thế bằng tài sản hay khoản nợ mới [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Ngân hàng nên loại vốn chủ sở hữu của mình khỏi phép tính ∆EVE [[src-bcbs-irrbb-2016#^irrbb-p08-2]]; dòng tiền slot vào 19 dải là dòng tiền của nợ trừ CET1 [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
   - Tuỳ cách xử lý NMD, prepayment và sản phẩm có behavioural option nhúng, notional repricing cash flow có thể khác nhau theo kịch bản $i$ [[src-bcbs-irrbb-2016#^irrbb-u05-23]]. Vì vậy công thức dưới đây viết $CF_{i,c}(k)$ theo từng kịch bản, không dùng một bộ dòng tiền chung.
2. **Chiết khấu và tính biến động $\Delta\text{EVE}_{i,c}$** (par 132, bước 1–4):
   - Bước 1: trong mỗi dải $k$, dòng tiền dương và âm được bù trừ thành một vị thế long hoặc short duy nhất, phần bù trừ bị loại khỏi phép tính [[src-bcbs-irrbb-2016#^irrbb-u05-17]]. Các dòng tiền khác ngày đáo hạn nhưng cùng dải được giả định khớp hoàn toàn (intra-bucket mismatch risk); BCBS giảm rủi ro này bằng $K = 19$ dải [[src-bcbs-irrbb-2016#^irrbb-u05-22]].
   - Bước 2: dòng tiền ròng của mỗi dải được nhân với discount factor liên tục phản ánh kịch bản $i$ của đồng tiền $c$, với $t_k$ là điểm giữa dải $k$ [[src-bcbs-irrbb-2016#^irrbb-u05-18]]:
     $$DF_{i,c}(t_k) = \exp(-R_{i,c}(t_k) \cdot t_k)$$
     Dòng tiền nên được chiết khấu bằng risk-free rate, hoặc risk-free rate cộng commercial margin và spread component nếu ngân hàng đã đưa các phần này vào dòng tiền; discount factor phải đại diện cho risk-free zero coupon rate [[src-bcbs-irrbb-2016#^irrbb-u05-19]].
   - Bước 3: cộng các vị thế ròng có trọng số ra EVE của đồng tiền $c$ trong kịch bản $i$, không gồm vị thế quyền chọn lãi suất tự động [[src-bcbs-irrbb-2016#^irrbb-u05-20]]:
     $$EVE_{i,c}^{nao} = \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k)$$
   - Bước 4: $\Delta\text{EVE}_{i,c}$ bằng EVE theo cấu trúc kỳ hạn hiện tại trừ EVE của kịch bản $i$, cộng $\text{KAO}_{i,c}$ [[src-bcbs-irrbb-2016#^irrbb-u05-21]]:
     $$\Delta EVE_{i,c} = \sum_{k=1}^{K} CF_{0,c}(k) \cdot DF_{0,c}(t_k) - \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k) + KAO_{i,c}$$
     Theo quy ước này, $\Delta EVE_{i,c} > 0$ là khoản lỗ [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
3. **Phụ trội quyền chọn tự động ($\text{KAO}_{i,c}$)**:
   - Với vị thế có quyền chọn lãi suất tự động nhúng, optionality nên được bỏ qua khi slot notional repricing cash flow [[src-bcbs-irrbb-2016#^irrbb-u05-3]]. Với mỗi quyền chọn tự động đã bán, ngân hàng tính thay đổi giá trị dưới từng kịch bản sốc $i$ kết hợp mức tăng tương đối 25% của implicit volatility [[src-bcbs-irrbb-2016#^irrbb-u05-7]]. Mô hình định giá quyền chọn cụ thể: [cần nguồn].
4. **Tổng hợp đa tiền tệ và Phép thử ngoại lai (Supervisory Outlier Test)**:
   - $\Delta EVE_{i,c}$ được tính cho từng đồng tiền có exposure trọng yếu, tức trên 5% tài sản hoặc nợ sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
   - Trong mỗi kịch bản $i$, chỉ các khoản lỗ $\Delta EVE_{i,c} > 0$ được cộng; khoản lỗ lớn nhất qua 6 kịch bản là thước đo rủi ro EVE [[src-bcbs-irrbb-2016#^irrbb-u05-8]]. Par 132 không cho bù trừ phần lãi của đồng tiền khác:
     $$\Delta EVE^{*} = \max_{i=1..6} \sum_{c} \max(0, \Delta EVE_{i,c})$$
     *Diễn giải:* công thức trên là cách viết gọn của câu "the EVE losses $\Delta EVE_{i,c} > 0$ are aggregated", không phải công thức chép từ nguồn.
   - Cơ quan giám sát quốc gia được phép quy định cách gộp tiền tệ khác, nếu chứng minh được bằng bằng chứng rằng cách đó vẫn phù hợp khẩu vị IRRBB của jurisdiction [[src-bcbs-irrbb-2016#^irrbb-u05-24]].
   - **Phép thử ngoại lai**: supervisor nên áp dụng ít nhất một outlier/materiality test so sánh $\max \Delta\text{EVE}$ dưới 6 kịch bản với 15% Tier 1 capital; ngân hàng bị xác định là outlier phải được coi là có khả năng mang IRRBB quá mức [[src-bcbs-irrbb-2016#^irrbb-p12-1]]. Khi supervisor kết luận ngân hàng quản trị IRRBB không đầy đủ hoặc rủi ro quá mức so với vốn, thu nhập, supervisor phải yêu cầu một hoặc nhiều biện pháp: giảm exposure (ví dụ hedging), tăng vốn, đặt ràng buộc lên tham số nội bộ, cải thiện khung quản trị rủi ro [[src-bcbs-irrbb-2016#^irrbb-p12-3]].

---

### Q2 — Phương pháp đo lường Độ nhạy thu nhập lãi thuần (ΔNII) dưới kịch bản sốc chuẩn hóa

1. **Khung thời gian và Kịch bản sốc áp dụng**:
   - $\Delta\text{NII}$ công bố là chênh lệch thu nhập lãi tương lai trong giai đoạn **12 tháng liên tục** (rolling 12-month period) [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Choudhry mô tả góc độ thu nhập qua thu nhập và chi phí lãi của tài sản, nợ tái định giá trong chân trời 12 tháng [[src-choudhry-principles-banking#^choudhry-irrbb-3]].
   - Ngân hàng nên áp dụng **2 kịch bản sốc** quy định cho NII [[src-bcbs-irrbb-2016#^irrbb-u07-1]] và phải công bố $\Delta\text{NII}$ dưới các kịch bản sốc ở Annex 2 [[src-bcbs-irrbb-2016#^irrbb-p08-1]].
2. **Giả định Bảng cân đối kế toán (Balance Sheet Assumptions)**:
   - **Constant Balance Sheet (Bảng cân đối tĩnh)**: $\Delta\text{NII}$ công bố nên được tính theo giả định constant balance sheet, trong đó dòng tiền đáo hạn hoặc tái định giá được thay bằng dòng tiền mới có cùng số tiền, kỳ tái định giá và spread component [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Dòng tiền dự kiến dùng cho $\Delta\text{NII}$ nên gồm cả commercial margin và spread component [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
   - **Dynamic Balance Sheet (Bảng cân đối động)**: [cần nguồn] — các claim đã ingest của d368 chỉ nêu constant balance sheet cho $\Delta\text{NII}$ công bố. *Diễn giải:* (ngoài wiki, chưa có nguồn) bảng cân đối động thường dùng cho quản trị nội bộ, kết hợp kế hoạch tăng trưởng và định giá.
3. **Cơ chế tính toán qua Khe hở tái định giá**:
   - Theo Tata, periodic earning gap bằng net repricing gap × 1% × phần còn lại của năm đầu tính từ điểm giữa dải (tỷ lệ trên 12 tháng); tổng các periodic earning gap là độ nhạy NII năm đầu với cú sốc song song 1% [[src-tata-bank-alm#^tata-egap-1]] [[src-tata-bank-alm#^tata-egap-2]]. Viết dưới dạng tổng, với $\tau_k$ là điểm giữa dải $k$ tính theo năm:
     $$\Delta\text{NII} = \sum_{k=1}^{M} \text{Gap}_k \cdot \Delta R \cdot (1 - \tau_k)$$
   - Với ngân hàng mô hình của Tata, total earning gap −0.25 nghĩa là NII năm đầu giảm 0.25 cho mỗi 1% lãi suất tăng song song [[src-tata-bank-alm#^tata-egap-2]]. *Diễn giải:* earning gap âm cho thấy nợ tái định giá trong năm nhiều hơn tài sản, nên NIM bị thu hẹp khi lãi suất tăng.

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
  $$\Delta R_{\text{steepener},c}(t_k) = -0.65 \cdot |\Delta R_{\text{short},c}| \cdot S_{\text{short}}(t_k) + 0.9 \cdot |\Delta R_{\text{long},c}| \cdot S_{\text{long}}(t_k)$$
  [[src-bcbs-irrbb-2016#^irrbb-u07-3]]
- **Sốc Flattener**:
  $$\Delta R_{\text{flattener},c}(t_k) = +0.8 \cdot |\Delta R_{\text{short},c}| \cdot S_{\text{short}}(t_k) - 0.6 \cdot |\Delta R_{\text{long},c}| \cdot S_{\text{long}}(t_k)$$
  [[src-bcbs-irrbb-2016#^irrbb-u07-3]]

#### 2. Ma trận biên độ sốc theo đồng tiền và Hệ thống Sàn / Trần (Table 1 Annex 2):
- **Biên độ sốc quy định theo đồng tiền** [[src-bcbs-irrbb-2016#^irrbb-u07-2]] [[src-bcbs-irrbb-2016#^irrbb-u07-5]] (bảng đủ 21 đồng tiền ở claim u07-5; Table 1 không ghi đơn vị, *Diễn giải:* đọc là bp theo sàn/trần ở u07-4):
  - **USD**: Parallel = 200 bps; Short = 300 bps; Long = 150 bps [[src-bcbs-irrbb-2016#^irrbb-u07-5]].
  - **EUR**: Parallel = 200 bps; Short = 250 bps; Long = 100 bps [[src-bcbs-irrbb-2016#^irrbb-u07-5]].
  - **JPY**: Parallel = 100 bps; Short = 100 bps; Long = 100 bps [[src-bcbs-irrbb-2016#^irrbb-u07-5]].
- **Hệ thống sàn (Floor) và trần (Caps) bảo vệ** [[src-bcbs-irrbb-2016#^irrbb-u07-4]]:
  - Mức sàn biên độ sốc tối thiểu: **100 bps** cho mọi loại tiền tệ [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
  - Trần biên độ sốc tối đa: **500 bps** cho ngắn hạn, **400 bps** cho song song, **300 bps** cho dài hạn [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
  - Supervisor có thể, theo national discretion, đặt mức sàn cao hơn trong kịch bản sốc nội địa cho home currency [[src-bcbs-irrbb-2016#^irrbb-u07-4]].

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
  - Floor 100 bp trong u07-4 là sàn của **biên độ sốc**, không phải sàn của lãi suất sau sốc [[src-bcbs-irrbb-2016#^irrbb-u07-4]]. Quy định về sàn lãi suất sau sốc (post-shock floor): [cần nguồn].
  - *Diễn giải:* (ngoài wiki, chưa có nguồn) tiền gửi bán lẻ khó giảm lãi suất dưới 0%, nên trong kịch bản Parallel down ngân hàng khó chuyển phần giảm lãi suất sang người gửi tiền và NIM bị thu hẹp.
- **Môi trường đường cong lãi suất đảo ngược (Inverted Yield Curve)**:
  - *Diễn giải:* (ngoài wiki, chưa có nguồn) với ngân hàng có nợ tái định giá ngắn và tài sản cố định dài, sốc Flattener (ngắn hạn tăng, dài hạn giảm) làm giảm NII 12 tháng qua chi phí nợ, còn tác động lên EVE tuỳ cấu trúc vị thế theo kỳ hạn.

---

## Hàm ý ALM / quy định

- **Khung quản trị ALCO và Treasury**:
  - *Diễn giải:* ALCO có thể đặt hai hạn mức riêng cho $\Delta\text{EVE}$ (góc độ vốn) và $\Delta\text{NII}$ (góc độ thu nhập), tương ứng hai góc độ Choudhry mô tả [[src-choudhry-principles-banking#^choudhry-irrbb-3]].
  - *Diễn giải:* Sử dụng các công cụ hoán đổi lãi suất ([[interest-rate-swap|IRS]]) và quyền chọn ([[swaption]], [[interest-rate-cap-floor]]) để phòng ngừa có chọn lọc các điểm kỳ hạn nhạy cảm cao trên 19 dải kỳ hạn thay vì chỉ phòng ngừa sốc song song.
- **Quy định pháp lý tại Việt Nam**:
  - [[tt83-2025]] có hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] và là căn cứ; BCBS d368 là tham chiếu. Ngân hàng phải có hạn mức ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-2]]; từ 01/07/2026 đến 31/12/2027 được dùng một trong hai chỉ tiêu [[src-tt83-2025-nhnn#^d74-4a]], chậm nhất từ 01/01/2028 phải dùng cả hai [[src-tt83-2025-nhnn#^d74-4b]].
  - ΔEVE: 6 kịch bản [[src-tt83-2025-nhnn#^pl5-a3-1]], tổng hợp các khoản giảm ΔEVE dương giữa các đồng tiền và lấy kịch bản lớn nhất [[src-tt83-2025-nhnn#^pl5-a5]]. ΔNII: chân trời 01 năm, constant balance sheet [[src-tt83-2025-nhnn#^pl5-b2]], 2 kịch bản song song, lấy giá trị giảm lớn nhất [[src-tt83-2025-nhnn#^pl5-b3]].
  - Tham số sốc VND: lãi suất bình quân hằng ngày 16 năm (kỳ hạn 3 tháng – 20 năm) nhân $\hat{\alpha}$ 60% / 85% / 40%, sàn 100 bp, trần 400 bp song song, 500 bp ngắn hạn, 300 bp dài hạn [[src-tt83-2025-nhnn#^pl5-c1-2]].
  - Ngưỡng outlier: C3-M7 và Phụ lục V không có phép thử so ΔEVE với Tier 1 `[cần nguồn: src-tt83-2025-nhnn PL6, C3-M9]`.

---

## Bất định

- Biên độ sốc VND: đã có phương pháp tính [2026-10-19] [[src-tt83-2025-nhnn#^pl5-c1-2]]; giá trị bp cụ thể phụ thuộc chuỗi lãi suất ngân hàng chọn, wiki chưa có số liệu `[cần nguồn]`.
- Ngưỡng outlier tại Việt Nam: không có trong C3-M7, PL5 (đã ingest [2026-10-19]). Ứng viên: PL6 (raw dòng 2794 có `RWA_IRRBB`, tài sản tính theo rủi ro IRRBB) và C3-M9 (ICAAP) `[cần nguồn: src-tt83-2025-nhnn PL6, C3-M9]`.
- Table 1 Annex 2 (biên độ Parallel/Short/Long theo đồng tiền): giá trị USD, EUR, JPY ở mục Q3 khớp raw u07 dòng 947–955, nhưng claim [[src-bcbs-irrbb-2016#^irrbb-u07-2]] chưa chép bảng. Unit u07 đã `done`; cần `/ingest src-bcbs-irrbb-2016 u07` bổ sung claim Table 1. → đã bổ sung [2026-10-18]: [[src-bcbs-irrbb-2016#^irrbb-u07-5]].
- Claim [[src-bcbs-irrbb-2016#^irrbb-u07-4]] ghi "sàn không âm hoặc sàn âm cho lãi suất sau sốc", trong khi trích nguyên văn nói supervisor có thể đặt "a higher floor … for their home currency". Synthesis này đã viết theo trích dẫn; claim source note cần sửa qua `/lint` hoặc `/ingest`. → đã sửa diễn đạt claim [2026-10-18] (trích dẫn và block-id giữ nguyên).
- Sàn lãi suất sau sốc (post-shock floor) và mô hình định giá quyền chọn cho $\text{KAO}$: `[cần nguồn]`; có thể nằm trong u07 (Annex 2) hoặc u05 par 130–131.
- Dynamic balance sheet cho $\Delta\text{NII}$: `[cần nguồn]`; claim đã ingest của d368 (p08-3) chỉ nêu constant balance sheet.

---
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation ở mục slotting. → đã rà [2026-10-18]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại các đoạn về dòng tiền tái định giá và citation par 101–106. → đã rà [2026-10-18]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 105, 132): có claim cho 4 bước tính ∆EVE ([[src-bcbs-irrbb-2016#^irrbb-u05-17]] … [[src-bcbs-irrbb-2016#^irrbb-u05-21]]), intra-bucket mismatch (u05-22), CF phụ thuộc kịch bản (u05-23), ngoại lệ gộp tiền tệ (u05-24); công thức ∆EVE^base = Σ CF_k·[DF_i − DF_0] (dòng 79) đổi dấu so với nguồn (EVE_0 − EVE_i) và dùng một CF cho cả hai kịch bản; công thức gộp tiền tệ có bù trừ 50% phần lãi (dòng 84) không có trong par 132, nơi chỉ cộng các khoản lỗ ∆EVE_{i,c} > 0 ([[src-bcbs-irrbb-2016#^irrbb-u05-8]]); cần rà lại mục đo lường ∆EVE. → đã rà [2026-10-18]
- [2026-10-18] ingest src-bcbs-irrbb-2016 U07 (bổ sung Table 1): có claim [[src-bcbs-irrbb-2016#^irrbb-u07-5]] — biên độ Parallel/Short/Long cho 21 đồng tiền; claim u07-4 sửa diễn đạt sàn; cần rà lại Q3. → đã rà [2026-10-18]
- [2026-10-18] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 90–93, 95): có claim outlier phải bị rà soát [[src-bcbs-irrbb-2016#^irrbb-p12-4]], IMS kém → dùng standardised framework [[src-bcbs-irrbb-2016#^irrbb-p12-6]], rủi ro quá mức so với thu nhập theo ∆NII dưới sốc [[src-bcbs-irrbb-2016#^irrbb-p12-7]], thời hạn khắc phục [[src-bcbs-irrbb-2016#^irrbb-p12-8]]; cần rà lại Q1 (phép thử ngoại lai) và Q2 (vai trò ∆NII trong đánh giá giám sát).
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]
- [2026-10-19] ingest src-bcbs-irrbb-2016 U07 (bổ sung): claim mới về phương pháp dựng Table 1 (16 năm, 60/85/40%, sàn/trần) [[src-bcbs-irrbb-2016#^irrbb-u07-7]] [[src-bcbs-irrbb-2016#^irrbb-u07-8]] [[src-bcbs-irrbb-2016#^irrbb-u07-9]] và chu kỳ rà soát hiệu chỉnh [[src-bcbs-irrbb-2016#^irrbb-u07-6]]; [[tt83-2025]] PL5.C.I.2 dùng cùng phương pháp cho VND; cần rà lại Q3 (biên độ theo đồng tiền) và mục sốc VND.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế.
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.

## Liên Kết Quan Hệ
- **Đầu vào từ**: [[repricing-balance-sheet]], [[irrbb-balance-sheet-portfolios]], [[non-maturity-deposits]]
- **Chỉ số đo lường**: [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[outlier-bank-test]]
- **Kịch bản & Mô hình**: [[standardised-interest-rate-shocks]], [[irrbb-standardised-framework]], [[key-rate-duration]], [[duration-gap-model]]
- **Quy định giám sát**: [[bcbs-irrbb]]
- **Nguồn trích dẫn**: [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]], [[src-choudhry-principles-banking]]
