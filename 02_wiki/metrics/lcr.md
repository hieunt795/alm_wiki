---
title: Liquidity Coverage Ratio (LCR)
aliases: [LCR, Tỷ lệ khả năng chi trả LCR, Liquidity Coverage Ratio]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]"]
relations:
  - {type: measures, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: measures, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: limits, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr20-4]]"}
  - {type: limits, to: "[[balance-sheet-optimisation-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u04-12]]"}
tags: [liquidity, stress-test, short-term]
updated: 2026-10-19
reviewed:
---

## Định nghĩa
LCR đo khả năng chống chịu thanh khoản ngắn hạn. Ngân hàng phải có đủ [[hqla]] để vượt qua kịch bản stress đáng kể kéo dài 30 ngày [[src-bcbs-lcr#^lcr20-1]]. Kịch bản này kết hợp cú sốc riêng của ngân hàng (idiosyncratic) và cú sốc toàn thị trường [[src-bcbs-lcr#^lcr20-2]].

## Công thức

$$
\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Total net cash outflows}_{30d}} \geq 100\%
$$

### 1. Tử số: Xác định Stock of HQLA sau Unwinding và Khống chế Trần (LCR30.34–30.39)
Để tránh hành vi hoán đổi tài sản trước kỳ báo cáo, Basel yêu cầu **unwind** toàn bộ các giao dịch tài trợ có bảo đảm (repo, reverse repo, collateral swap) đáo hạn trong vòng 30 ngày có trao đổi HQLA để xác định số dư điều chỉnh: $\text{Adjusted L1}$, $\text{Adjusted L2A}$, $\text{Adjusted L2B}$ [[src-bcbs-lcr#^lcr30-34]].

Hai mức trần được tính theo công thức hai bước:
1. **Khoản khấu trừ trần 15% Level 2B**:
   $$Adjustment_{15\%} = \max\Big(\text{Adjusted L2B} - \frac{15}{85}(\text{Adjusted L1} + \text{Adjusted L2A}),\; \text{Adjusted L2B} - \frac{15}{60}\text{Adjusted L1},\; 0\Big)$$
2. **Khoản khấu trừ trần 40% Level 2**:
   $$Adjustment_{40\%} = \max\Big(\big(\text{Adjusted L2A} + \text{Adjusted L2B} - Adjustment_{15\%}\big) - \frac{2}{3}\text{Adjusted L1},\; 0\Big)$$
3. **Giá trị HQLA đưa vào tử số LCR**:
   $$\text{Stock of HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - Adjustment_{15\%} - Adjustment_{40\%}$$
*(Trường hợp áp dụng [[alternative-liquidity-approaches]] theo LCR31, lượng tài sản thay thế sau haircut được cộng thêm theo các điều kiện hạn mức của supervisor)* [[src-bcbs-lcr#^lcr31-4]].

### 2. Mẫu số: Xác định Total Net Cash Outflows (LCR40.1, LCR40.77)
$$\text{Total net cash outflows} = \text{Total cash outflows} - \min\big(\text{Total cash inflows},\; 0.75 \times \text{Total cash outflows}\big)$$
- Không đếm trùng: tài sản đã vào tử số thì dòng tiền phát sinh của nó không được tính ở mẫu số [[src-bcbs-lcr#^lcr40-4]].
- Trần bù trừ dòng vào 75% tạo ra mức sàn: $\text{Total net cash outflows} \ge 0.25 \times \text{Total cash outflows}$, nghĩa là ngân hàng luôn phải duy trì HQLA tối thiểu bằng 25% tổng dòng ra gộp [[src-bcbs-lcr#^lcr40-77]].

## Diễn giải
- LCR phải ≥ 100% một cách liên tục khi không có stress. Khi có stress, ngân hàng được phép dùng HQLA và xuống dưới 100% [[src-bcbs-lcr#^lcr20-5]]. Supervisor phản ứng có phân biệt, tương xứng với nguyên nhân, quy mô và thời gian thiếu hụt [[src-bcbs-lcr#^lcr20-6]].
- Áp dụng trên cơ sở hợp nhất: Chuẩn mực LCR bắt buộc trên cấp hợp nhất đối với ngân hàng hoạt động quốc tế [[src-bcbs-lcr#^lcr10-1]]. Khi một thực thể thành viên chịu rào cản chuyển giao ([[liquidity-transfer-restrictions]]), phần HQLA thặng dư vượt quá dòng tiền ra ròng cục bộ nếu không chuyển giao được phải bị loại hoàn toàn khỏi LCR hợp nhất [[src-bcbs-lcr#^lcr10-7]].
- Do trần dòng vào 75%, HQLA tối thiểu luôn bằng 25% tổng dòng ra, kể cả khi dòng vào hợp đồng rất lớn [[src-bcbs-lcr#^lcr40-77]].
- Quản lý đồng tiền trọng yếu: Báo cáo bằng đồng tiền chung nhưng phải theo dõi riêng thanh khoản cho từng đồng tiền trọng yếu; không giả định các đồng tiền có thể hoán đổi tự do trong stress [[src-bcbs-lcr#^lcr10-9]].
- Stress test của LCR chỉ là mức tối thiểu. Ngân hàng phải tự xây kịch bản với horizon dài hơn [[src-bcbs-lcr#^lcr20-3]].
- Báo cáo ít nhất hàng tháng, độ trễ lý tưởng ≤ 2 tuần [[src-bcbs-lcr#^lcr20-7]]. Phải báo ngay khi LCR đã hoặc dự kiến < 100% [[src-bcbs-lcr#^lcr20-8]].

## Mối quan hệ trong Basel Framework

*Diễn giải phân tích cấu trúc:*
LCR không vận hành biệt lập mà tạo thành một mạng lưới ràng buộc đa chiều với các trụ cột khác của Basel:

### 1. LCR và [[nsfr|NSFR (Net Stable Funding Ratio)]] — Ngắn hạn vs Dài hạn (chi tiết xem [[nsfr-structural-liquidity-and-alm-strategy]])
- **Tính bổ trợ thời gian**: LCR giải quyết kịch bản căng thẳng thanh khoản cấp tính trong 30 ngày (acute short-term stress - survival horizon), trong khi [[nsfr]] giải quyết rủi ro cơ cấu tài trợ kéo dài 1 năm (structural medium/long-term funding).
- **Ràng buộc hai chiều**:
  - *Về tài sản*: Tài sản nắm giữ cho HQLA của LCR nhận được trọng số yêu cầu nguồn vốn ổn định ([[required-stable-funding|RSF]]) rất thuận lợi trong NSFR (Level 1 có RSF 0% hoặc 5%; Level 2A có RSF 15%; Level 2B có RSF 50%), khuyến khích ngân hàng giữ tài sản thanh khoản cao.
  - *Về nguồn vốn*: Nếu ngân hàng tìm cách tài trợ danh mục HQLA bằng nguồn vốn ngắn hạn liên ngân hàng (< 30 ngày), LCR sẽ bị triệt tiêu do dòng tiền ra (cash outflows 100%) tăng tương ứng, đồng thời nguồn vốn này có hệ số nguồn vốn ổn định sẵn có ([[available-stable-funding|ASF]]) bằng 0% trong NSFR. Do đó, muốn duy trì LCR bền vững, ngân hàng bắt buộc phải dùng nguồn vốn trung dài hạn hoặc tiền gửi bán lẻ ổn định, giúp cải thiện đồng thời cả NSFR.

### 2. LCR và Tỷ lệ đòn bẩy (Leverage Ratio - LEV) — Xung đột quy mô bảng cân đối
- **Thế tiến thoái lưỡng nan của Treasury**: Tài sản Level 1 (như tiền gửi dự trữ tại NHTW hoặc trái phiếu chính phủ 0% rủi ro) có hệ số rủi ro tín dụng bằng 0% trong CAR (Tỷ lệ an toàn vốn theo rủi ro), nhưng lại bị tính 100% vào mẫu số tổng mức phơi bày (Exposure Measure) của Tỷ lệ đòn bẩy (Leverage Ratio, yêu cầu tối thiểu ≥ 3%).
- Khi ngân hàng tăng quy mô tích lũy HQLA để đẩy LCR lên cao, tổng tài sản phình to làm xói mòn trực tiếp Tỷ lệ đòn bẩy. Đây là điểm nghẽn chính sách lớn đối với các ngân hàng toàn cầu (G-SIBs) khi NHTW thực hiện chính sách nới lỏng định lượng (QE).

### 3. LCR và Rủi ro lãi suất trên sổ ngân hàng (IRRBB) — Đánh đổi Duration
- **Rủi ro định giá thị trường của HQLA**: Danh mục HQLA thường tập trung vào trái phiếu chính phủ trung dài hạn để hưởng lợi suất. Khi lãi suất thị trường tăng sốc, giá trị thị trường của trái phiếu sụt giảm mạnh.
- Dù ngân hàng hạch toán kế toán ở danh mục Giữ đến ngày đáo hạn (Hold-to-Maturity - HTM), nguyên tắc LCR30.40 bắt buộc HQLA phải được định giá theo **giá trị thị trường hiện hành (current market value)**. Thua lỗ lãi suất chưa thực hiện (unrealised losses) sẽ lập tức làm bốc hơi tử số HQLA, đẩy LCR xuống dưới 100% (bài học thực tiễn từ cuộc khủng hoảng SVB năm 2023). Xem [[silicon-valley-bank]].

### 4. LCR và Bộ công cụ giám sát thanh khoản (Basel Liquidity Monitoring Tools)
Bên cạnh chỉ số LCR cứng (≥ 100%), Basel quy định 5 công cụ giám sát bắt buộc (Pillar 2 / SRP):
1. **Contractual maturity mismatch**: Lập bảng chênh lệch kỳ hạn theo hợp đồng thuần túy để theo dõi các hố đen thanh khoản mà không bị che mờ bởi giả định hành vi của LCR.
2. **Concentration of funding**: Giám sát mức độ tập trung nguồn vốn vào một số ít người gửi tiền lớn hoặc sản phẩm đơn lẻ.
3. **Available unencumbered assets**: Theo dõi lượng tài sản tự do chưa cầm cố có thể huy động thêm trong trường hợp stress vượt quá 30 ngày.
4. **LCR by significant currency**: Bắt buộc tính và theo dõi LCR riêng biệt cho từng đồng tiền chiếm ≥ 5% tổng nợ phải trả, ngăn ngừa rủi ro thiếu hụt ngoại tệ cục bộ [[src-bcbs-lcr#^lcr10-9]].
5. **Market-related monitoring tools**: Theo dõi các tín hiệu cảnh báo sớm từ thị trường (CDS spread, giá cổ phiếu ngân hàng, chênh lệch lãi suất liên ngân hàng).

## Basel vs VN

| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Phạm vi áp dụng | Hợp nhất (consolidated) [[src-bcbs-lcr#^lcr10-1]] | [cần nguồn] | LCR10.1 / TT50 Đ13 | Basel: 15/12/2019 |
| Ngưỡng tối thiểu | ≥ 100% [[src-bcbs-lcr#^lcr20-5]] | [cần nguồn] | LCR20.5 / TT50 Đ16 | Basel: 15/12/2019 |
| Horizon stress | 30 ngày [[src-bcbs-lcr#^lcr20-1]] | [cần nguồn] | LCR20.1 | |
| Trần Level 2 trong HQLA | ≤ 40% [[src-bcbs-lcr#^lcr30-31]] | [cần nguồn] | LCR30.31 / TT50 PL1 | |
| Trần Level 2B trong HQLA | ≤ 15% [[src-bcbs-lcr#^lcr30-31]] | [cần nguồn] | LCR30.33 / TT50 PL1 | |
| Haircut Level 1 | 0% [[src-bcbs-lcr#^lcr30-41]] | [cần nguồn] | LCR30.40 / TT50 PL1 | |
| Haircut Level 2A | 15% [[src-bcbs-lcr#^lcr30-43]] | [cần nguồn] | LCR30.43 / TT50 PL1 | |
| Haircut Level 2B | 25% – 50% [[src-bcbs-lcr#^lcr30-45]] | [cần nguồn] | LCR30.45 / TT50 PL1 | |
| Trần dòng vào | 75% dòng ra [[src-bcbs-lcr#^lcr40-77]] | [cần nguồn] | LCR40.77 | |
| Run-off stable retail | 5% (tuỳ chọn 3%) [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-11]] | [cần nguồn] | LCR40.7, 40.11 | |
| Run-off less stable retail | ≥ 10% [[src-bcbs-lcr#^lcr40-13]] | [cần nguồn] | LCR40.13 | |
| Tần suất báo cáo | ≥ hàng tháng [[src-bcbs-lcr#^lcr20-7]] | [cần nguồn] | LCR20.7 | |

Cột VN để trống vì TT50/2026 chưa được ingest. Registry `src-tt50-2026-nhnn` đã có các unit tương ứng: `C2-M5` (LCR, NSFR; Đ13–Đ27) và `PL1` (hướng dẫn xác định tỷ lệ khả năng chi trả, gồm HQLA và dòng tiền ra). Theo ghi chú register, Đ13.1 quy định từ 01/10/2028 phải áp dụng cả LCR và NSFR. Claim này cần đưa vào source note khi ingest.

## Ứng dụng trong ALM
- Ngoài LCR, TT83/2025 yêu cầu ngân hàng tự kiểm tra sức chịu đựng về thanh khoản với tối thiểu 3 kịch bản [[src-tt83-2025-nhnn#^d48-2]]. Xem [[liquidity-stress-testing]], [[liquidity-risk-management]].
*Diễn giải:*
Trong thực tiễn điều hành tại Khối ALM Treasury, LCR không chỉ là một chỉ số tuân thủ pháp định thụ động mà là công cụ định hình toàn bộ cấu trúc bảng cân đối kế toán (phân tích toàn diện về ý nghĩa kinh tế, nghịch lý sử dụng đệm HQLA và phương pháp quản trị: xem [[lcr-economic-significance-and-alm-governance]]):
- **Khung thời gian sinh tồn 30 ngày (*Survival Horizon*)**: LCR được thiết kế để mua thời gian (buy time) cho Ban Điều hành kích hoạt Kế hoạch tài trợ dự phòng (CFP) và để Cơ quan Giám sát / NHTW can thiệp có trật tự trong khủng hoảng [[src-bcbs-lcr#^lcr20-1]] [[src-bcbs-lcr#^lcr20-6]].
- **Hệ thống Hạn mức Đèn tín hiệu 4 tầng (*Traffic-Light Limits*)**: Treasury không bao giờ vận hành ở mức 100% sát sàn mà thiết lập các tầng đệm: Green (Target: 115%–125%), Amber (Early Warning: 108%–114%), Red (Recovery: 101%–107%) và Breach (< 100% kích hoạt báo cáo khẩn cấp tức thì theo LCR20.8 [[src-bcbs-lcr#^lcr20-8]]).
- **Định giá Điều chuyển Vốn Nội bộ (Liquidity FTP)**: Phân bổ chi phí duy trì đệm HQLA (carry cost) vào tài sản rủi ro; áp phí thanh khoản đối với hạn mức cam kết tín dụng chưa rút (contingent outflow charge); và trả thưởng thanh khoản (stable funding credit) cho tiền gửi bán lẻ ổn định [[retail-deposit-stability]] và tiền gửi vận hành [[operational-deposits]].
- **Quản trị Đồng tiền Trọng yếu**: Tính toán và theo dõi [[lcr-by-currency]] riêng rẽ cho từng đồng tiền chiếm $\ge 5\%$ tổng nợ; nghiêm cấm giả định các ngoại tệ có thể hoán đổi tự do trong stress [[src-bcbs-lcr#^lcr10-9]].
- **Quy trình [[ilaap]] & Stress Test Nội bộ**: LCR là mức sàn tối thiểu; ngân hàng bắt buộc phải tự stress test với horizon dài hơn (60D, 90D, 1Y) và tích hợp rủi ro biến đổi khí hậu theo LCR20.3 [[src-bcbs-lcr#^lcr20-3]].
- **Hệ Thống Phân Tích Tổng Hợp**:
  1. Tử số và các đánh đổi chiến lược Treasury: [[hqla-decomposition-and-tradeoffs]]
  2. Mẫu số, cơ chế trần 75% và giả định hành vi bất đối xứng: [[lcr-net-cash-outflows-mechanics]]
  3. Ý nghĩa kinh tế, nghịch lý sử dụng đệm và khung quản trị ALM: [[lcr-economic-significance-and-alm-governance]]
  4. Kiến trúc giám sát thanh khoản đa tầng Basel III: [[basel-liquidity-monitoring-framework]] và [[synthetic-balance-sheet-liquidity-risk]]

## Nhầm lẫn thường gặp
- LCR không phải "tỷ lệ tài sản thanh khoản trên tiền gửi". Mẫu số là dòng tiền ra **ròng sau khi áp run-off/inflow rate** trong kịch bản stress, không phải số dư.
- Run-off rate của Basel là **mức sàn**. Jurisdiction được đặt cao hơn [[src-bcbs-lcr#^lcr40-6]], nên so sánh LCR giữa các quốc gia cần thận trọng.
