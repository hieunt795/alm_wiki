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
sources: ["[[src-bcbs-lcr]]", "[[src-bardaeva-alm]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: measures, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: measures, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: limits, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr20-4]]"}
  - {type: limits, to: "[[balance-sheet-optimisation-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u04-12]]"}
tags: [liquidity, stress-test, short-term]
updated: 2026-10-21
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

### Xử lý khi LCR dưới ngưỡng

| Nội dung | Basel | VN ([[tt50-2026|TT50/2026]]) |
|---|---|---|
| Nguyên tắc | Khi có stress, ngân hàng được dùng HQLA và xuống dưới 100% [[src-bcbs-lcr#^lcr20-5]]; supervisor phản ứng có phân biệt, tương xứng [[src-bcbs-lcr#^lcr20-6]] | Vi phạm LCR quy VNĐ riêng lẻ: NHNN xử lý theo quy định xử phạt vi phạm hành chính và giám sát trên cơ sở báo cáo của ngân hàng [[src-tt50-2026-nhnn#^d17-2a]] |
| Thông báo | Ngân hàng phải thông báo ngay khi LCR đã hoặc dự kiến dưới 100% [[src-bcbs-lcr#^lcr20-8]] | Báo cáo hằng ngày trước 12 giờ sáng hôm sau; ngày đầu báo cáo bổ sung trước 17 giờ [[src-tt50-2026-nhnn#^d17-2]] |
| Nội dung đánh giá, báo cáo | Supervisor xét nguyên nhân, cú sốc riêng hay toàn thị trường, sức khoẻ và hồ sơ rủi ro, quy mô và thời gian giảm; ngân hàng tối thiểu trình yếu tố làm LCR giảm, biện pháp, thời gian dự kiến [[src-bcbs-lcr#^lcr20-6b]] | Báo cáo ngày đầu tối thiểu gồm: nguyên nhân (riêng hay toàn thị trường) và mức độ từng cấu phần; biện pháp dự kiến; thời gian kéo dài; tình hình tài chính và hồ sơ rủi ro; biến động giá HQLA [[src-tt50-2026-nhnn#^d17-2b]] |
| Biện pháp của ngân hàng | Supervisor có thể yêu cầu giảm rủi ro thanh khoản, tăng cường quản trị, cải thiện kế hoạch tài trợ dự phòng [[src-bcbs-lcr#^lcr20-6b]] | Ngân hàng phải ngay lập tức dùng biện pháp tự xử lý (vay TCTD, cam kết không thể huỷ ngang); từ 10% giá trị HQLA đủ điều kiện trở lên thì NHNN giám sát tăng cường [[src-tt50-2026-nhnn#^d17-2]]; vẫn khó khăn thì báo cáo ngay NHNN [[src-tt50-2026-nhnn#^d17-2b]] |
| Biện pháp khắc phục do cơ quan giám sát yêu cầu | Như trên [[src-bcbs-lcr#^lcr20-6b]] | Căn cứ thanh tra, giám sát, NHNN yêu cầu hoàn thiện chính sách, kế hoạch dự phòng, giảm rủi ro (duy trì HQLA cao hơn), hạn chế cấp tín dụng, mở rộng kinh doanh, áp tỷ lệ an toàn vốn cao hơn [[src-tt50-2026-nhnn#^d15-1]] [[src-tt50-2026-nhnn#^d15-2]] |
| Nguy cơ mất khả năng chi trả | [cần nguồn] | HQLA đủ điều kiện < 90% mức phải đáp ứng trong 30 ngày liên tục [[src-tt50-2026-nhnn#^d18-1]]; ngân hàng phải kịp thời báo cáo thực trạng, nguyên nhân, biện pháp, đề xuất [[src-tt50-2026-nhnn#^d18-3]] |

*Diễn giải:* năm nội dung báo cáo ngày đầu của TT50 Đ17.2.b(iii) tương ứng gần sát các yếu tố supervisor đánh giá tại LCR20.6(3) và yêu cầu tối thiểu tại LCR20.6(4)(a); TT50 biến chúng thành nghĩa vụ báo cáo có hạn giờ. Basel coi LCR dưới 100% trong stress là cách dùng HQLA hợp lệ, còn TT50 gọi là "vi phạm" và gắn với xử phạt hành chính.

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
| Phạm vi áp dụng | Hợp nhất (consolidated) [[src-bcbs-lcr#^lcr10-1]] | Riêng lẻ: phải quản lý và báo cáo LCR quy VNĐ, LCR VNĐ; LCR hợp nhất và LCR ngoại tệ trọng yếu theo quy định nội bộ [[src-tt50-2026-nhnn#^d16-2]] | LCR10.1 / TT50 Đ16.1.d–đ, Đ16.2 | Basel: 15/12/2019; VN: 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Ngưỡng tối thiểu | ≥ 100% [[src-bcbs-lcr#^lcr20-5]] | LCR quy VNĐ riêng lẻ 50% (01/10/2028), +10 điểm mỗi năm, 100% từ 01/10/2033 [[src-tt50-2026-nhnn#^d16-1c]] | LCR20.5 / TT50 Đ16.1.c | Basel: 15/12/2019; VN: theo lộ trình |
| Horizon stress | 30 ngày [[src-bcbs-lcr#^lcr20-1]] | Dòng tiền ra ròng trong 30 ngày tiếp theo [[src-tt50-2026-nhnn#^d16-1]] | LCR20.1 / TT50 Đ16.1.b | |
| Trần Level 2 trong HQLA | ≤ 40% [[src-bcbs-lcr#^lcr30-31]] | KĐC40% loại phần cấp 2 vượt 2/3 cấp 1 sau unwinding, tương đương ≤ 40% [[src-tt50-2026-nhnn#^pl1-a1]] | LCR30.31 / TT50 PL1 | |
| Trần Level 2B trong HQLA | ≤ 15% [[src-bcbs-lcr#^lcr30-31]] | KĐC15% dùng hệ số 15/85 và 15/60, tương đương ≤ 15% [[src-tt50-2026-nhnn#^pl1-a1]] | LCR30.33 / TT50 PL1 | |
| Haircut Level 1 | 0% [[src-bcbs-lcr#^lcr30-41]] | Hệ số thanh khoản 100% (haircut 0%) [[src-tt50-2026-nhnn#^pl1-a2]] | LCR30.40 / TT50 PL1 | |
| Haircut Level 2A | 15% [[src-bcbs-lcr#^lcr30-43]] | Hệ số thanh khoản 85% [[src-tt50-2026-nhnn#^pl1-a3]] | LCR30.43 / TT50 PL1 | |
| Haircut Level 2B | 25% – 50% [[src-bcbs-lcr#^lcr30-45]] | Hệ số thanh khoản 75% (RMBS) hoặc 50% (TP doanh nghiệp, chứng khoán Chính phủ nước ngoài BBB-, cổ phiếu VN30) [[src-tt50-2026-nhnn#^pl1-a4]] | LCR30.45 / TT50 PL1 | |
| Trần dòng vào | 75% dòng ra [[src-bcbs-lcr#^lcr40-77]] | 75% tổng dòng tiền ra [[src-tt50-2026-nhnn#^d21-2]] | LCR40.77 / TT50 Đ21.2 | |
| Run-off stable retail | 5% (tuỳ chọn 3%) [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-11]] | 5%; điều kiện: bảo hiểm hoàn toàn bởi BHTG và có vay trung dài hạn hoặc tài khoản thanh toán hoạt động 6 tháng [[src-tt50-2026-nhnn#^pl1-b2]] | LCR40.7, 40.11 | |
| Run-off less stable retail | ≥ 10% [[src-bcbs-lcr#^lcr40-13]] | 10%; gồm phần vượt giới hạn bảo hiểm và mọi tiền gửi ngoại tệ [[src-tt50-2026-nhnn#^pl1-b2]] | LCR40.13 | |
| Tần suất báo cáo | ≥ hàng tháng [[src-bcbs-lcr#^lcr20-7]] | Theo chế độ báo cáo thống kê [[src-tt50-2026-nhnn#^d16-2]]; bộ phận tại trụ sở chính theo dõi LCR hằng ngày [[src-tt50-2026-nhnn#^d17-1]] | LCR20.7 / TT50 Đ16.2, Đ17.1 | |

Các dòng VN về trần cấp 2, hệ số thanh khoản và hệ số rút tiền lấy từ TT50 Phụ lục I. Tên VN của chỉ tiêu là "tỷ lệ khả năng chi trả" [[src-tt50-2026-nhnn#^d16-1]]. Trước khi áp dụng LCR, ngân hàng tuân thủ tỷ lệ khả năng chi trả trong 30 ngày theo TT22/2019 [[src-tt50-2026-nhnn#^d13-4]]. Xem [[tt50-2026]].

Khác biệt: VN áp LCR riêng lẻ với lộ trình 5 năm từ 50%, Basel áp hợp nhất ở mức 100%. Từ 01/10/2028 ngân hàng phải áp dụng cả LCR và NSFR [[src-tt50-2026-nhnn#^d13-1]]. Khi vi phạm LCR quy VNĐ riêng lẻ, ngân hàng phải dùng biện pháp tự xử lý và báo cáo hằng ngày; Basel chỉ yêu cầu thông báo ngay cho supervisor [[src-bcbs-lcr#^lcr20-8]] [[src-tt50-2026-nhnn#^d17-2]].

## Ứng dụng trong ALM
- Ngoài LCR, TT83/2025 yêu cầu ngân hàng tự kiểm tra sức chịu đựng về thanh khoản với tối thiểu 3 kịch bản [[src-tt83-2025-nhnn#^d48-2]]. Xem [[liquidity-stress-testing]], [[liquidity-risk-management]].
- **Ví dụ tính toán đệm thanh khoản LCR mục tiêu 110% (Bardaeva, Table 5.1)**:
  Giả định trong kịch bản stress 30 ngày, tổng dòng tiền ra ước tính là 100 đơn vị và tổng dòng tiền vào là 90 đơn vị. Do áp dụng trần dòng tiền vào tối đa 75% dòng tiền ra ($75\% \times 100 = 75$), dòng tiền ra ròng chịu căng thẳng (*net cash outflows*) là:
  $$\text{Net Outflows} = 100 - \min(90, 75) = 25$$
  Để duy trì tỷ lệ LCR ở mức mục tiêu 110%, quy mô đệm thanh khoản HQLA ngân hàng cần dự trữ là:
  $$\text{Target HQLA} = 110\% \times 25 = 27.5$$
  Trần 75% inflows đảm bảo ngân hàng luôn phải tự trang bị đệm tài sản thanh khoản chất lượng cao tối thiểu bằng 25% tổng dòng ra gộp mà không được bù trừ hoàn toàn bằng dòng tiền vào dự kiến [[src-bardaeva-alm#^ch5-1]] [[src-bardaeva-alm#^ch5-2]] (xem bối cảnh thời kỳ biên sinh lời thấp tại [[alm-evolution]]).

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
