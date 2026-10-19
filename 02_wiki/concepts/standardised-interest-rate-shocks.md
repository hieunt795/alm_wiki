---
title: "Standardised Interest Rate Shocks (Các kịch bản sốc lãi suất chuẩn hoá Basel)"
aliases: [Standardised Interest Rate Shocks, Prescribed Interest Rate Shocks, 6 Kịch bản sốc lãi suất, Supervisory Interest Rate Shocks]
type: concept
domains: [alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: part-of, to: "[[bcbs-irrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u07-1]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p08-1]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p08-1]]"}
  - {type: input-to, to: "[[outlier-bank-test]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
tags: [irrbb, interest-rate-shocks, parallel-shock, rotation-shocks, steepener, flattener, basel]
updated: 2026-10-18
reviewed:
---

## Định nghĩa & Mục đích
Các kịch bản sốc lãi suất chuẩn hoá (Standardised / Prescribed Interest Rate Shock Scenarios) trong Chuẩn mực [[bcbs-irrbb]] (Phụ lục Annex 2) là hệ thống 6 kịch bản biến động đường cong lãi suất do Ủy ban Basel ban hành bắt buộc, nhằm đo lường mức độ phơi lượng rủi ro lãi suất của ngân hàng một cách nhất quán và có khả năng so sánh xuyên suốt các tổ chức tín dụng toàn cầu [[src-bcbs-irrbb-2016#^irrbb-u07-1]].

Hệ thống sốc được áp dụng riêng biệt cho từng loại tiền tệ mà ngân hàng có vị thế trọng yếu (chiếm từ 5% tổng tài sản hoặc nợ của sổ ngân hàng trở lên) [[src-bcbs-irrbb-2016#^irrbb-u07-2]]:
- **Đối với [[economic-value-of-equity|$\Delta\text{EVE}$]]**: Bắt buộc áp dụng toàn bộ **6 kịch bản sốc** để nắm bắt đầy đủ rủi ro khe hở song song và phi song song ([[gap-risk]]) [[src-bcbs-irrbb-2016#^irrbb-u07-1]].
- **Đối với [[net-interest-income-sensitivity|$\Delta\text{NII}$]]**: Bắt buộc áp dụng **2 kịch bản sốc song song** (Parallel Up và Parallel Down) cho mục đích công bố Trụ cột 3 [[src-bcbs-irrbb-2016#^irrbb-u07-1]].
- **Đối với [[outlier-bank-test|Outlier Bank Test]]**: Là bộ kịch bản dùng trong phép thử mà cơ quan giám sát nên (should) áp dụng: so sánh $\max_{i=1..6} \Delta\text{EVE}_i$ với 15% Vốn cấp 1 (Tier 1 Capital) [[src-bcbs-irrbb-2016#^irrbb-p12-1]].

```
                  ┌─────────────────────────────────────────────────────────────┐
                  │          6 KỊCH BẢN SỐC LÃI SUẤT CHUẨN HOÁ BASEL             │
                  └──────────────────────────────┬──────────────────────────────┘
                                                 │
          ┌──────────────────────────────────────┼──────────────────────────────────────┐
          ▼                                      ▼                                      ▼
┌───────────────────┐                  ┌───────────────────┐                  ┌───────────────────┐
│ SỐC SONG SONG     │                  │ SỐC XOAY TRỤC     │                  │ SỐC ĐẦU NGẮN      │
│ (PARALLEL SHOCKS) │                  │ (ROTATION SHOCKS) │                  │ (SHORT SHOCKS)    │
├───────────────────┤                  ├───────────────────┤                  ├───────────────────┤
│ 1. Parallel Up    │                  │ 3. Steepener      │                  │ 5. Short Rate Up  │
│ 2. Parallel Down  │                  │ 4. Flattener      │                  │ 6. Short Rate Down│
└───────────────────┘                  └───────────────────┘                  └───────────────────┘
```

---

## 1. Chi tiết 6 kịch bản sốc lãi suất

Theo Annex 2 (par 930–940), 6 kịch bản sốc được định nghĩa như sau [[src-bcbs-irrbb-2016#^irrbb-u07-1]]:

1. **Dịch chuyển song song tăng (Parallel shock up)**: Toàn bộ các điểm kỳ hạn trên đường cong lợi suất dịch chuyển tăng một khoảng không đổi $\bar{\Delta R}_{\text{parallel},c}$.
2. **Dịch chuyển song song giảm (Parallel shock down)**: Toàn bộ các điểm kỳ hạn dịch chuyển giảm một khoảng không đổi $-\bar{\Delta R}_{\text{parallel},c}$.
3. **Đường cong dốc lên (Steepener shock)**: Lãi suất ngắn hạn giảm và lãi suất dài hạn tăng.
4. **Đường cong phẳng đi (Flattener shock)**: Lãi suất ngắn hạn tăng và lãi suất dài hạn giảm.
5. **Lãi suất ngắn hạn tăng (Short rates shock up)**: Lãi suất ngắn hạn tăng vọt và tác động suy giảm dần về 0 khi kỳ hạn kéo dài về đuôi dài.
6. **Lãi suất ngắn hạn giảm (Short rates shock down)**: Lãi suất ngắn hạn giảm sâu và tác động suy giảm dần về 0 đối với các kỳ hạn dài.

---

## 2. Công thức toán học định hình đường cong xoay trục

Để mô phỏng chính xác sự biến dạng của đường cong lợi suất theo thời gian, Basel thiết lập hàm suy giảm sốc (decay shaping function) và công thức kết hợp xoay trục [[src-bcbs-irrbb-2016#^irrbb-u07-3]]:

### Hàm định hình sốc đầu ngắn và đầu dài
Tại điểm kỳ hạn $t_k$ (tính bằng năm), hàm suy giảm sốc đầu ngắn $S_{\text{short}}(t_k)$ được định nghĩa:

$$
S_{\text{short}}(t_k) = e^{-\frac{t_k}{x}}
$$

Trong đó tham số phân rã mặc định là $x = 4$ đối với hầu hết các loại tiền tệ [[src-bcbs-irrbb-2016#^irrbb-u07-3]]. 
- Khi $t_k \to 0$ (qua đêm): $S_{\text{short}}(0) = 1$ (hấp thụ 100% sốc đầu ngắn).
- Khi $t_k = 4$ năm: $S_{\text{short}}(4) = e^{-1} \approx 36.8\%$.
- Khi $t_k = 20$ năm: $S_{\text{short}}(20) = e^{-5} \approx 0.67\%$ (sốc đầu ngắn triệt tiêu hoàn toàn).

Từ đó, mức sốc ngắn hạn và dài hạn thuần tuý tại điểm kỳ hạn $t_k$ đối với đồng tiền $c$ là:

$$
\Delta R_{\text{short},c}(t_k) = \bar{\Delta R}_{\text{short},c} \cdot S_{\text{short}}(t_k) = \bar{\Delta R}_{\text{short},c} \cdot e^{-\frac{t_k}{4}}
$$

$$
\Delta R_{\text{long},c}(t_k) = \bar{\Delta R}_{\text{long},c} \cdot \left(1 - S_{\text{short}}(t_k)\right) = \bar{\Delta R}_{\text{long},c} \cdot \left(1 - e^{-\frac{t_k}{4}}\right)
$$

### Công thức Sốc Dốc lên (Steepener)
Kịch bản đường cong dốc lên kết hợp mức giảm đầu ngắn với trọng số 0.65 và mức tăng đầu dài với trọng số 0.90 [[src-bcbs-irrbb-2016#^irrbb-u07-3]]:

$$
\Delta R_{\text{steepener},c}(t_k) = -0.65 \cdot |\Delta R_{\text{short},c}(t_k)| + 0.90 \cdot |\Delta R_{\text{long},c}(t_k)|
$$

- Tại kỳ hạn siêu ngắn ($t_k \to 0$): $\Delta R \approx -0.65 \cdot \bar{\Delta R}_{\text{short},c}$ (lãi suất giảm mạnh).
- Tại kỳ hạn siêu dài ($t_k \to \infty$): $\Delta R \approx +0.90 \cdot \bar{\Delta R}_{\text{long},c}$ (lãi suất tăng mạnh).
- Điểm đảo chiều (pivot point nơi $\Delta R = 0$) thường nằm quanh kỳ hạn 3–5 năm tuỳ theo tỷ lệ giữa $\bar{\Delta R}_{\text{short}}$ và $\bar{\Delta R}_{\text{long}}$.

### Công thức Sốc Phẳng đi (Flattener)
Kịch bản đường cong phẳng đi kết hợp mức tăng đầu ngắn với trọng số 0.80 và mức giảm đầu dài với trọng số 0.60 [[src-bcbs-irrbb-2016#^irrbb-u07-3]]:

$$
\Delta R_{\text{flattener},c}(t_k) = +0.80 \cdot |\Delta R_{\text{short},c}(t_k)| - 0.60 \cdot |\Delta R_{\text{long},c}(t_k)|
$$

- Tại kỳ hạn ngắn: lãi suất tăng mạnh ($+0.80 \cdot \bar{\Delta R}_{\text{short},c}$).
- Tại kỳ hạn dài: lãi suất giảm đáng kể ($-0.60 \cdot \bar{\Delta R}_{\text{long},c}$).

---

## 3. Biên độ sốc quy định theo loại tiền tệ (Table 1 Annex 2)

Basel d368 xác định biên độ sốc cơ sở $\bar{\Delta R}$ dựa trên chuỗi số liệu lịch sử 2000–2015 [[src-bcbs-irrbb-2016#^irrbb-u07-2]]; phương pháp thống kê (phân vị, cửa sổ thời gian) dùng để suy ra biên độ `[cần nguồn]`.

Bảng 1 (Annex 2) quy định mức sốc cơ sở cho từng đồng tiền; bảng dưới trích 7 đồng tiền, đủ 21 đồng tiền ở claim [[src-bcbs-irrbb-2016#^irrbb-u07-5]]. Table 1 không ghi đơn vị; *Diễn giải:* đọc là bp, nhất quán với sàn 100 bp và các trần ở [[src-bcbs-irrbb-2016#^irrbb-u07-4]].

| Đồng tiền | Ký hiệu | Sốc song song ($\bar{\Delta R}_{\text{parallel}}$) | Sốc đầu ngắn ($\bar{\Delta R}_{\text{short}}$) | Sốc đầu dài ($\bar{\Delta R}_{\text{long}}$) | Nguồn |
|---|---|:---:|:---:|:---:|---|
| Đô la Mỹ | **USD** | 200 bps | 300 bps | 150 bps | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |
| Euro | **EUR** | 200 bps | 250 bps | 100 bps | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |
| Yên Nhật | **JPY** | 100 bps | 100 bps | 100 bps | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |
| Bảng Anh | **GBP** | 250 bps | 300 bps | 150 bps | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |
| Franc Thụy Sĩ | **CHF** | 100 bps | 150 bps | 100 bps | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |
| Đô la Canada | **CAD** | 200 bps | 300 bps | 150 bps | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |
| Đô la Úc | **AUD** | 300 bps | 450 bps | 200 bps | [[src-bcbs-irrbb-2016#^irrbb-u07-5]] |

> Cách xác định biên độ sốc cho đồng tiền không có trong Table 1 (gồm VND) `[cần nguồn: src-tt83-2025-nhnn PL5]`. Cơ quan giám sát có thể (may) đặt mức sàn cao hơn trong kịch bản sốc địa phương cho đồng nội tệ [[src-bcbs-irrbb-2016#^irrbb-u07-4]].

---

## 4. Hệ thống Sàn (Floors) và Trần (Caps) bảo vệ

Để đảm bảo tính thận trọng và duy trì một sân chơi bình đẳng trên toàn cầu, Basel thiết lập các cơ chế ràng buộc biên độ [[src-bcbs-irrbb-2016#^irrbb-u07-4]]:

### Mức sàn biên độ sốc tối thiểu (Floor of 100 bps)
- Biên độ sốc áp dụng cho bất kỳ đồng tiền nào không được thấp hơn **100 bps** ($\bar{\Delta R} \ge 100 \text{ bps}$), ngay cả khi dữ liệu lịch sử trong giai đoạn lãi suất siêu thấp tính ra biến động nhỏ hơn 100 bps [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
- Cơ quan giám sát quốc gia có quyền quyết định áp dụng mức sàn cao hơn đối với đồng nội tệ [[src-bcbs-irrbb-2016#^irrbb-u07-4]].

### Trần khống chế sốc tối đa (Variable Caps)
Để ngăn ngừa các kịch bản sốc phi thực tế đối với các nền kinh tế đang phát triển có biến động lãi suất quá cao trong lịch sử, Basel quy định trần tối đa [[src-bcbs-irrbb-2016#^irrbb-u07-4]]:
- **Trần sốc ngắn hạn**: tối đa **500 bps** ($\bar{\Delta R}_{\text{short}} \le 500 \text{ bps}$).
- **Trần sốc song song**: tối đa **400 bps** ($\bar{\Delta R}_{\text{parallel}} \le 400 \text{ bps}$).
- **Trần sốc dài hạn**: tối đa **300 bps** ($\bar{\Delta R}_{\text{long}} \le 300 \text{ bps}$).

### Giới hạn sàn lãi suất sau sốc (Post-shock Rate Lower Bound)
Trong các kịch bản sốc giảm (Parallel down, Short rate down, Steepener), nếu lãi suất ban đầu đang ở mức thấp, việc trừ đi biên độ sốc có thể đẩy lãi suất xuống mức âm sâu phi thực tế. Basel quy định mức sàn cho lãi suất sau sốc:
- Kỳ hạn qua đêm đến 1 năm: sàn âm tối đa là **-100 bps** (hoặc do cơ quan quản lý quốc gia quy định).
- Kỳ hạn trên 1 năm: mức sàn âm thu hẹp dần 5 bps mỗi năm, đạt mức **0 bps** tại kỳ hạn 20 năm trở lên.

---

## 5. Ý nghĩa quản trị ALM và Tác động tương hỗ

1. **Kiểm tra sức chịu đựng toàn diện**: Khung 6 kịch bản triệt tiêu điểm mù của các mô hình truyền thống vốn chỉ kiểm tra sốc song song $\pm 200$ bps. Ví dụ, một ngân hàng phòng ngừa hoàn hảo rủi ro song song (duration gap = 0) vẫn có thể bị sụp đổ giá trị kinh tế nghiêm trọng dưới kịch bản **Steepener** (nếu nắm giữ nhiều trái phiếu dài hạn tài trợ bằng tiền gửi ngắn hạn) hoặc **Flattener**.
2. **Kích hoạt hành vi khách hàng phi tuyến**: Biên độ sốc lớn ($\pm 200 \dots 300$ bps) kích hoạt dữ dội các [[behavioural-options]]: kịch bản lãi suất giảm thúc đẩy trả nợ vay trước hạn ($\gamma_i = 1.2$), kịch bản lãi suất tăng thúc đẩy rút tiền gửi có kỳ hạn sớm ($u_i = 1.2$).
3. **Mối liên hệ với Đệm HQLA trong [[lcr]]**: Danh mục HQLA Level 1 gồm trái phiếu chính phủ kỳ hạn dài (10Y–30Y) có độ nhạy cảm cực cao với kịch bản Parallel Up và Steepener. Nếu ALCO không sử dụng các công cụ hoán đổi lãi suất (IRS) để phòng hộ, tổn thất $\Delta\text{EVE}$ từ HQLA có thể đẩy ngân hàng vi phạm ngưỡng [[outlier-bank-test]].
4. **Cơ sở định giá FTP**: Các đường cong sốc cung cấp dữ liệu đầu vào chuẩn xác để tính toán chi phí rủi ro kỳ hạn và rủi ro quyền chọn trong hệ thống Chuyển giá vốn nội bộ ([[integrated-alm-liquidity-strategy]]).

## Đề xuất cập nhật

- [2026-10-18] ingest src-bcbs-irrbb-2016 U07 (bổ sung Table 1): có claim [[src-bcbs-irrbb-2016#^irrbb-u07-5]] chép đủ Table 1. Đề xuất: → đã áp [2026-10-18]
  - Bảng biên độ sốc (mục Bảng 1): dòng **AUD** ghi Short = 400 bps, raw và claim u07-5 là **450**; đổi cite của bảng từ `^irrbb-u07-2` sang `^irrbb-u07-5`, cite riêng từng dòng. Table 1 không ghi đơn vị; "bps" là cách đọc theo sàn/trần ở [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
  - Câu "lấy các phân vị thứ 1% và 99% … trong khoảng thời gian 6 tháng" cite `^irrbb-u07-2`, nhưng claim đó chỉ nói chuỗi 2000–2015; phân vị và cửa sổ 6 tháng chưa có claim `[cần nguồn]`.
  - Callout "đồng tiền không nằm trong Bảng 1 (bao gồm VND) … phải tính toán … hoặc áp dụng mức sốc tối thiểu" cite `^irrbb-u07-4`, nhưng claim đó nói về sàn 100 bp, trần và quyền đặt sàn cao hơn cho home currency; cách xử lý đồng tiền ngoài Table 1 `[cần nguồn]`.
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 25 "Là căn cứ bắt buộc để xác định mức tổn thất cực đại …": đề xuất "Là bộ kịch bản dùng trong phép thử mà cơ quan giám sát nên (should) áp dụng: so max ∆EVE dưới 6 kịch bản với 15% Tier 1" ([[src-bcbs-irrbb-2016#^irrbb-p12-1]]). → đã áp [2026-10-18]
