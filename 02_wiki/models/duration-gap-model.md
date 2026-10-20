---
title: "Duration Gap Model (Mô hình chênh lệch thời lượng)"
aliases: [DGAP, Duration Gap Analysis, Thời lượng bảng cân đối, Immunization Model, Mô hình khoảng cách thời lượng]
type: model
domains: [alm, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-lubinska-alm-optimisation]]", "[[src-tata-bank-alm]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-7]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-5]]"}
  - {type: drives, to: "[[economic-value-of-equity]]", direction: "-", regime: rising_rate, cite: "[[src-bcbs-irrbb-2016#^irrbb-u07-1]]"}
tags: [irrbb, model, duration-gap, macaulay-duration, modified-duration, convexity, immunization]
updated: 2026-10-20
reviewed:
---

## Khái niệm và Mục tiêu Quản trị
Mô hình chênh lệch thời lượng (Duration Gap Model - DGAP) là mô hình định lượng nền tảng trong quản trị cân đối Tài sản - Nợ (ALM), dùng để đo lường mức độ nhạy cảm của toàn bộ Giá trị kinh tế của Vốn chủ sở hữu ([[economic-value-of-equity|$\Delta\text{EVE}$]]) trước các biến động song song của đường cong lãi suất thị trường [[src-bcbs-irrbb-2016#^irrbb-u06-5]] [[src-bcbs-irrbb-2016#^irrbb-u06-7]].

Khác với phân tích khoảng cách tái định giá đơn thuần (Repricing Gap Analysis) chỉ quan tâm đến thời điểm dòng tiền tái định giá trong từng kỳ ngắn hạn, mô hình DGAP tính đến giá trị thời gian của tiền và thời lượng bình quân gia quyền của tất cả dòng tiền tương lai cho đến khi đáo hạn [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

## Các Định nghĩa Thời lượng Cốt lõi

### 1. Thời lượng Macaulay (Macaulay Duration)
Đo lường thời gian bình quân (tính theo năm) để nhà đầu tư thu hồi toàn bộ vốn gốc và lãi từ một công cụ tài chính:
$$D_{\text{Mac}} = \frac{\sum_{t=1}^n t \cdot \frac{CF_t}{(1+y)^t}}{\sum_{t=1}^n \frac{CF_t}{(1+y)^t}} = \frac{1}{P} \sum_{t=1}^n t \cdot \frac{CF_t}{(1+y)^t}$$
Trong đó $P$ là giá thị trường (giá trị hiện tại), $CF_t$ là dòng tiền tại kỳ $t$, $y$ là lợi suất đáo hạn (YTM).

### 2. Thời lượng hiệu chỉnh (Modified Duration)
Đo lường phần trăm thay đổi giá trị của công cụ khi lợi suất thị trường dịch chuyển một đơn vị nhỏ:
$$D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1 + y} = -\frac{1}{P} \frac{\partial P}{\partial y}$$
Khi lãi suất thay đổi $\Delta y$, biến động phần trăm giá trị tài sản xấp xỉ bằng:
$$\frac{\Delta P}{P} \approx -D_{\text{Mod}} \cdot \Delta y$$

### 3. Thời lượng thực tế (Effective Duration)
Áp dụng cho các công cụ có dòng tiền không chắc chắn hoặc chứa quyền chọn nhúng (như trái phiếu có thể thu hồi, các khoản vay có quyền trả nợ trước hạn):
$$D_{\text{Eff}} = \frac{P_- - P_+}{2 \cdot P_0 \cdot \Delta y}$$
Trong đó $P_-$ và $P_+$ là giá trị định giá lại của danh mục khi lãi suất giảm và tăng một biên độ $\Delta y$.

## Phương trình Chênh lệch Thời lượng Bảng Cân đối (DGAP Equation)

Bảng cân đối kế toán của ngân hàng thỏa mãn phương trình cơ bản về giá trị kinh tế:
$$A = L + E \implies E = A - L$$
Trong đó: $A$ là tổng giá trị thị trường của tài sản sinh lời, $L$ là tổng giá trị thị trường của nợ phải trả nhạy cảm lãi suất, và $E$ là giá trị kinh tế của vốn chủ sở hữu (Economic Value of Equity).

Lấy vi phân hai vế theo lãi suất $y$ (giả định lãi suất tài sản và nợ dịch chuyển song song cùng biên độ $\Delta y$):
$$\frac{\partial E}{\partial y} = \frac{\partial A}{\partial y} - \frac{\partial L}{\partial y}$$
Biểu diễn theo thời lượng hiệu chỉnh của tài sản ($D_A$) và nợ ($D_L$):
$$\Delta E \approx -\left( D_A \cdot A - D_L \cdot L \right) \Delta y$$
Đặt $k = \frac{L}{A}$ (hệ số đòn bẩy nợ trên tài sản), ta có:
$$\Delta E \approx -\left( D_A - \frac{L}{A} D_L \right) \cdot A \cdot \Delta y$$

### Chỉ số Chênh lệch Thời lượng (Duration Gap):
$$\text{DGAP} = D_A - \left(\frac{L}{A}\right) D_L$$
Biến động giá trị vốn chủ sở hữu rút gọn thành:
$$\Delta E = -\text{DGAP} \cdot A \cdot \Delta y$$

## Phân tích Ý nghĩa và Tác động Rủi ro

| Trạng thái DGAP | Đặc tính Bảng cân đối | Khi Lãi suất Tăng ($\Delta y > 0$) | Khi Lãi suất Giảm ($\Delta y < 0$) |
|---|---|---|---|
| **$\text{DGAP} > 0$**<br>(Dương) | Thời lượng tài sản dài hơn thời lượng nợ đã nhân hệ số đòn bẩy ($D_A > \frac{L}{A} D_L$). Mô hình kinh doanh NHTM truyền thống: huy động ngắn hạn cho vay dài hạn. | **$\Delta E < 0$ (Tổn thất EVE)**<br>Giá trị tài sản sụt giảm mạnh hơn mức giảm giá trị nợ phải trả. Ngân hàng chịu tổn thất vốn tự có [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. | **$\Delta E > 0$ (Gia tăng EVE)**<br>Giá trị tài sản tăng mạnh hơn giá trị nợ. [[economic-capital|Vốn kinh tế]] mở rộng. |
| **$\text{DGAP} < 0$**<br>(Âm) | Thời lượng nợ dài hơn thời lượng tài sản ($D_A < \frac{L}{A} D_L$). | **$\Delta E > 0$ (Gia tăng EVE)**<br>Nợ giảm giá trị nhiều hơn mức sụt giảm của tài sản. | **$\Delta E < 0$ (Tổn thất EVE)**<br>Tài sản không tăng kịp đà gia tăng giá trị của nghĩa vụ nợ. |
| **$\text{DGAP} = 0$**<br>(Miễn nhiễm) | Điều kiện miễn nhiễm hoàn toàn (Immunization condition): $D_A = \frac{L}{A} D_L$. | **$\Delta E \approx 0$**<br>Giá trị kinh tế của vốn được bảo toàn trước các cú sốc lãi suất song song nhỏ. | **$\Delta E \approx 0$** |

### Ví dụ và cách dùng theo nguồn T4

- **Công thức theo Lubinska**: DGAP = DA − w·DL với w = L/A; mức chấp nhận rủi ro do chính sách [[alco|ALCO]] quy định [[src-lubinska-alm-optimisation#^lubinska-u02-45]]. Lubinska phân biệt Modified duration và Macaulay duration [[src-lubinska-alm-optimisation#^lubinska-u02-44]].
- **Ví dụ miễn nhiễm (Kaufman 1984, qua Lubinska)**: DA 4,17 năm, DL 1 năm, tỷ lệ nợ/tài sản 0,9 cho DGAP 3,27 năm; đưa về 0 bằng cách rút duration tài sản về 0,9 hoặc kéo duration tiền gửi lên 4,63 [[src-lubinska-alm-optimisation#^lubinska-u02-46]].
- **Chiến lược chủ động**: DGAP 1 năm, tài sản 1.000 euro, lãi suất tăng 200 bp thì vốn giảm 20 euro [[src-lubinska-alm-optimisation#^lubinska-u02-47]].
- **Hạn chế (Lubinska)**: cần dữ liệu đầy đủ, bỏ qua trả nợ trước hạn, chỉ đúng với sốc nhỏ và song song [[src-lubinska-alm-optimisation#^lubinska-u02-48]]. Xem [[pv01]], [[repricing-gap-analysis]].
- **Ví dụ [[silicon-valley-bank]] (Tata)**: giả định tiền gửi gửi tạm có duration 1 năm, duration gap của SVB vẫn khoảng 3 năm, tương ứng lỗ khoảng 12,5 tỷ USD (hơn 100% vốn) khi sốc 200 bp [[src-tata-bank-alm#^tata-svb-7]]; sổ HTM có duration khoảng 6,25 năm [[src-tata-bank-alm#^tata-svb-5]].
- *Diễn giải:* ΔE từ DGAP là xấp xỉ bậc một của ΔEVE; con số này dùng để kiểm tra nhanh trước khi đưa ΔEVE đầy đủ vào [[icaap]].

## Hiệu chỉnh Tính lồi (Convexity Adjustment)
Xấp xỉ bậc 1 bằng Duration chỉ chính xác đối với các biến động lãi suất vô cùng nhỏ. Đối với các cú sốc lãi suất lớn (ví dụ sốc chuẩn hoá 200–400 bps của Basel), cần bổ sung số hạng bậc 2 đại diện cho tính lồi (Convexity $C$):
$$\Delta E \approx -\text{DGAP} \cdot A \cdot \Delta y + \frac{1}{2} C_E \cdot A \cdot (\Delta y)^2$$
Trong đó tính lồi của vốn tự có là:
$$C_E = C_A - \left(\frac{L}{A}\right) C_L$$
- **Tính lồi dương ($C_E > 0$)**: Mang lại lợi ích cho ngân hàng (khi lãi suất tăng, tài sản giảm chậm hơn dự tính; khi lãi suất giảm, tài sản tăng nhanh hơn dự tính).
- **Tính lồi âm ($C_E < 0$)**: Thường xuất hiện khi danh mục tài sản chứa nhiều khoản vay thế chấp có quyền trả nợ trước hạn hoặc danh mục nợ chứa quyền rút tiền gửi sớm ([[behavioural-options]]), khuếch đại tổn thất vốn trong các kịch bản sốc lãi suất mạnh [[src-bcbs-irrbb-2016#^irrbb-u06-4]].

## Hạn chế của Mô hình DGAP
Theo phân tích của Ủy ban Basel d368 (Annex 1, par 4.2), mô hình DGAP có 3 nhược điểm cốt tử khiến cơ quan giám sát không thể chỉ dựa vào nó [[src-bcbs-irrbb-2016#^irrbb-u06-7]]:
1. **Chỉ giả định dịch chuyển song song (Parallel Shift)**: Bỏ qua hoàn toàn rủi ro độ dốc và độ cong đường cong lợi suất (Steepener, Flattener, Twists) [[src-bcbs-irrbb-2016#^irrbb-u07-1]].
2. **Không đo lường được rủi ro cơ sở (Basis Risk)**: Giả định lãi suất tài sản và nợ biến động với tỷ lệ 1:1, bỏ qua chênh lệch spread giữa các chỉ số tham chiếu [[src-bcbs-irrbb-2016#^irrbb-u06-4]].
3. **Mâu thuẫn với Quản trị Thu nhập**: Miễn nhiễm thời lượng ($\text{DGAP} = 0$) đòi hỏi kéo dài kỳ hạn nợ hoặc rút ngắn kỳ hạn tài sản, điều này trực tiếp gây ra sự bấp bênh và biến động dữ dội cho Thu nhập lãi thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]] [[src-bcbs-irrbb-2016#^irrbb-u02-4]].

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9 — chờ user duyệt: đã có node [[icaap]] (và stub [[economic-capital]]); đề xuất link ở lần nhắc đầu ICAAP / vốn kinh tế. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: thêm ví dụ SVB: duration gap khoảng 3 năm (giả định tiền gửi gửi tạm duration 1 năm) ứng với lỗ khoảng 12,5 tỷ USD, hơn 100% vốn, khi sốc 200 bp; sổ HTM duration 6,25 năm [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-5]]; link [[silicon-valley-bank]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm nguồn T4 thứ hai: DGAP = DA − w·DL với w = L/A, mức chấp nhận rủi ro theo chính sách ALCO [[src-lubinska-alm-optimisation#^lubinska-u02-45]]; ví dụ miễn nhiễm (Kaufman 1984) DA 4,17, DL 1, P/A 0,9 → DGAP 3,27 năm, về 0 bằng rút duration tài sản về 0,9 hoặc kéo duration tiền gửi lên 4,63 [[src-lubinska-alm-optimisation#^lubinska-u02-46]]; chiến lược chủ động DGAP 1 năm, tài sản 1.000 euro, lãi suất tăng 200 bp → vốn giảm 20 euro [[src-lubinska-alm-optimisation#^lubinska-u02-47]]; hạn chế (cần dữ liệu đầy đủ, bỏ qua trả trước, chỉ đúng với sốc nhỏ song song) [[src-lubinska-alm-optimisation#^lubinska-u02-48]]; Modified vs Macaulay duration [[src-lubinska-alm-optimisation#^lubinska-u02-44]]. Link [[pv01]], [[repricing-gap-analysis]]. → đã áp dụng [2026-10-20]
