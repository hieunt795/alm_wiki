---
title: "Key Rate Duration (KRD — Thời lượng lãi suất từng kỳ hạn)"
aliases: [KRD, Partial Duration, Bucket PV01, BPV by Tenor, Thời lượng điểm then chốt, Phân rã độ nhạy đường cong]
type: model
domains: [alm, basel, product]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-8]]"}
  - {type: input-to, to: "[[irrbb-standardised-framework]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-2]]"}
tags: [irrbb, model, key-rate-duration, krd, non-parallel-risk, curve-shaping, pv01-bucket]
updated: 2026-10-16
reviewed:
---

## Định nghĩa và Ý nghĩa Khoa học
Thời lượng lãi suất từng kỳ hạn (Key Rate Duration - KRD, hay Partial Duration / Bucket PV01) đo lường độ nhạy cảm của giá trị tài sản, nợ hoặc toàn bộ bảng cân đối kế toán trước sự thay đổi của lãi suất tại một điểm kỳ hạn xác định trên đường cong lợi suất, trong điều kiện lãi suất tại tất cả các điểm kỳ hạn then chốt khác được giữ nguyên không đổi [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

Trong khi Thời lượng hiệu chỉnh tổng thể (Modified Duration) chỉ đo lường phản ứng trước các cú sốc song song (Parallel shifts), mô hình KRD cho phép Treasury nhận diện và bóc tách chính xác các rủi ro phi song song (Non-parallel gap risk) — bao gồm rủi ro dốc lên (Steepening), phẳng đi (Flattening) và xoắn đường cong hình cánh bướm (Butterfly twists) [[src-bcbs-irrbb-2016#^irrbb-u06-4]] [[src-bcbs-irrbb-2016#^irrbb-u07-1]].

## Công thức Toán học và Nguyên lý Phân rã

Giả định đường cong lợi suất được định nghĩa bởi một tập hợp $m$ điểm kỳ hạn then chốt (key rates) $t_1, t_2, \dots, t_m$ (ví dụ: 3 tháng, 6 tháng, 1 năm, 2 năm, 5 năm, 10 năm, 20 năm, 30 năm) [[src-bcbs-irrbb-2016#^irrbb-u05-2]].

### 1. Định nghĩa KRD tại kỳ hạn $k$ ($KRD_k$):
$$KRD_k = -\frac{1}{P} \frac{\partial P}{\partial y_k} \approx -\frac{P(y_k + \Delta y) - P(y_k - \Delta y)}{2 \cdot P_0 \cdot \Delta y}$$
Trong đó:
- $P_0$ là giá trị hiện tại của danh mục.
- $\partial y_k$ là mức thay đổi cục bộ tại kỳ hạn then chốt $k$. Sự thay đổi này được nội suy tuyến tính hoặc spline hình nón (tent-shaped shift) sang các điểm lân cận $t_{k-1}$ và $t_{k+1}$ để đảm bảo tính liên tục của đường cong.

### 2. Mối quan hệ với Thời lượng Tổng thể:
Tổng của tất cả các KRD thành phần đúng bằng Thời lượng hiệu chỉnh tổng thể của danh mục:
$$\sum_{k=1}^m \text{KRD}_k = D_{\text{Mod}}$$
*Hệ quả ALM quan trọng*: Một ngân hàng có thể có $\text{DGAP} = 0$ (tổng thời lượng tài sản và nợ cân bằng tuyệt đối trước sốc song song), nhưng cấu trúc KRD có thể lệch pha nghiêm trọng (ví dụ tài sản tập trung ở kỳ hạn 10 năm trong khi nợ tập trung ở kỳ hạn 2 năm). Khi đường cong xoay trục (xoắn dốc hoặc phẳng), ngân hàng vẫn phải gánh chịu những khoản tổn thất $\Delta\text{EVE}$ khổng lồ [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

### 3. Biến động Giá trị Danh mục trước Cú sốc Đường cong Bất kỳ:
Biến động phần trăm của giá trị tài sản hoặc vốn chủ sở hữu trước một vector sốc lãi suất tổng quát $\vec{\Delta y} = [\Delta y_1, \Delta y_2, \dots, \Delta y_m]^T$ được tính bằng:
$$\frac{\Delta P}{P} \approx -\sum_{k=1}^m \text{KRD}_k \cdot \Delta y_k$$
Đối với toàn bộ vốn chủ sở hữu ngân hàng ($\Delta E$):
$$\Delta E \approx -\sum_{k=1}^m \left[ \text{KRD}_{A,k} \cdot A - \text{KRD}_{L,k} \cdot L \right] \cdot \Delta y_k = -\sum_{k=1}^m \text{BPV}_{\text{net}, k} \cdot \Delta y_k$$
Trong đó $\text{BPV}_{\text{net}, k}$ là giá trị điểm cơ bản ròng (Net Basis Point Value) tại dải kỳ hạn $k$.

## Áp dụng trong Khuôn khổ Chuẩn hoá Basel d368

Khuôn khổ chuẩn hoá của Basel (Section IV, Annex 1) áp dụng trực tiếp nguyên lý KRD thông qua cấu trúc **19 dải kỳ hạn chuẩn hoá** (19 predefined time buckets) [[src-bcbs-irrbb-2016#^irrbb-u05-2]]:

| Dải kỳ hạn ($k$) | Khoảng thời gian | Điểm giữa dải ($t_k$) | Hệ số suy giảm ngắn hạn $S_{\text{short}}(t_k)$ |
|---|---|---|---|
| 1 | Qua đêm đến 1 ngày | 0.0028 năm | 0.999 |
| 2 | 1 ngày đến 1 tháng | 0.0417 năm | 0.990 |
| 3 | 1 tháng đến 3 tháng | 0.1667 năm | 0.959 |
| 4 | 3 tháng đến 6 tháng | 0.3750 năm | 0.911 |
| 5 | 6 tháng đến 9 tháng | 0.6250 năm | 0.855 |
| 6 | 9 tháng đến 12 tháng | 0.8750 năm | 0.804 |
| 7–12 | 1 năm đến 5 năm (chia 6 dải nhỏ) | 1.25 – 4.5 năm | 0.732 $\rightarrow$ 0.325 |
| 13–16 | 5 năm đến 10 năm (chia 4 dải) | 5.5 – 9.0 năm | 0.253 $\rightarrow$ 0.105 |
| 17–19 | 10 năm đến trên 20 năm | 12.5 – 25 năm | 0.044 $\rightarrow$ 0.004 |

Khoảng kỳ hạn và điểm giữa dải theo Table 1 [[src-bcbs-irrbb-2016#^irrbb-u05-25]]; cột hệ số suy giảm $S_{\text{short}}(t_k)$ [cần nguồn].

### Quy trình Đo lường theo KRD của Basel:
1. Dòng tiền tái định giá danh nghĩa ([[notional-repricing-cash-flow]]) ròng ($CF_{\text{net}, k} = CF_{\text{Asset}, k} - CF_{\text{Liab}, k}$) được xếp vào điểm giữa $t_k$ của 19 dải kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u05-2]].
2. Mỗi dải kỳ hạn được nhân với hệ số thời lượng chiết khấu chuẩn hoá để xác định độ nhạy giá trị hiện tại $S_{k,c}$ [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
3. Khi áp dụng các kịch bản sốc xoay trục đường cong (Steepener và Flattener tại Annex 2), mức thay đổi lãi suất $\Delta R_{i,c}(t_k)$ tại từng dải kỳ hạn được tính trực tiếp từ hàm mũ suy giảm $e^{-t_k / 4}$ [[src-bcbs-irrbb-2016#^irrbb-u07-3]].
4. Tổng hợp tổn thất $\Delta\text{EVE}$ phản ánh chính xác sự tương tác giữa vector KRD của ngân hàng và hình thái xoay trục của đường cong [[src-bcbs-irrbb-2016#^irrbb-u05-8]].

## Chiến lược Tái cân bằng ALM dựa trên KRD Profile
- **Khớp thời lượng cục bộ (Bucket-by-Bucket Immunization)**: Thay vì chỉ duy trì $\text{DGAP} = 0$, ALM Treasury sử dụng các hợp đồng [[interest-rate-swap|IRS]] có kỳ hạn khác nhau để triệt tiêu $\text{BPV}_{\text{net}, k}$ tại từng dải kỳ hạn trọng yếu (ví dụ thực hiện Payer Swap 10 năm kết hợp Receiver Swap 2 năm) [[src-bcbs-irrbb-2016#^irrbb-p12-3]].
- **Phòng ngừa rủi ro Cánh bướm (Butterfly Hedging)**: Triệt tiêu độ lồi và độ cong đường cong bằng cách thiết lập vị thế barbell (ngắn hạn + dài hạn) đối ứng với vị thế bullet (trung hạn).

## Đề xuất cập nhật
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; đề xuất link ở "Dòng tiền tái định giá danh nghĩa ròng" (dòng 62). → đã áp [2026-10-19]
- [2026-10-19] review (đối chiếu Table 1, ^irrbb-u05-25) — user duyệt [2026-10-19]: dòng bảng "17–19 | 10 năm đến trên 20 năm | 12.5 – 22.5 năm" sai điểm giữa dải cuối; raw ghi >20Y (25Y) [[src-bcbs-irrbb-2016#^irrbb-u05-25]]. Đề xuất sửa thành "12.5 – 25 năm" và cite u05-25. Cột hệ số (0.044 → 0.004) chưa có citation, cần rà nguồn. → đã áp [2026-10-19]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: đã có node [[pv01]] (định nghĩa PV − PV* theo sốc 1 bp, tổng theo dải) [[src-lubinska-alm-optimisation#^lubinska-u02-43]]; đề xuất link ở chỗ nhắc Bucket PV01.
