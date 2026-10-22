---
title: "Economic Value of Equity (EVE)"
aliases: [EVE, Giá trị kinh tế của vốn chủ sở hữu, ΔEVE, Delta EVE]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: measures, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: measures, to: "[[basis-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: input-to, to: "[[outlier-bank-test]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
  - {type: input-to, to: "[[rwa-irrbb]]", cite: "[[src-tt83-2025-nhnn#^pl6-1c]]"}
tags: [irrbb, eve, economic-value, pillar-2, outlier-test, run-off]
updated: 2026-10-22
reviewed:
---

## Định nghĩa
Giá trị kinh tế của vốn chủ sở hữu (Economic Value of Equity - EVE) là giá trị hiện tại thuần (NPV) của toàn bộ dòng tiền dự kiến trong tương lai từ các tài sản, nợ phải trả và các vị thế ngoại bảng nhạy cảm với lãi suất trên sổ ngân hàng, loại trừ vốn chủ sở hữu kế toán [[src-bcbs-irrbb-2016#^irrbb-p08-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

Chỉ số biến động giá trị kinh tế ($\Delta\text{EVE}$) đo lường mức độ sụt giảm giá trị kinh tế của ngân hàng khi chịu tác động của các kịch bản sốc lãi suất chuẩn hoá so với kịch bản cơ sở theo đường cong lợi suất hiện hành [[src-bcbs-irrbb-2016#^irrbb-u01-4]] [[src-bcbs-irrbb-2016#^irrbb-u05-8]]:
- **Lăng kính dài hạn (Run-off Horizon)**: $\Delta\text{EVE}$ đánh giá tác động trên toàn bộ vòng đời còn lại của tất cả các công cụ tài chính hiện hữu cho đến khi chạy hết dòng tiền (run-off), không tính đến các giao dịch kinh doanh mới trong tương lai [[src-bcbs-irrbb-2016#^irrbb-p04-2]].
- **Thước đo an toàn vốn của Cơ quan giám sát**: Cơ quan giám sát Basel sử dụng $\Delta\text{EVE}$ làm thước đo chuẩn mực để đánh giá mức độ đủ vốn Trụ cột 2 và kiểm tra ngưỡng ngân hàng ngoại lai qua phép thử [[outlier-bank-test|Outlier Bank Test]] [[src-bcbs-irrbb-2016#^irrbb-u02-4]] [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
- **Nguyên tắc Reset Date theo Fidelio Tata**: Rủi ro lãi suất đối với giá trị kinh tế chỉ được tính đến ngày tái định giá tiếp theo (*next reset date*) chứ không phải ngày đáo hạn theo hợp đồng, bởi vì khi một công cụ được thiết lập lại theo lãi suất thị trường, nó sẽ giao dịch lại theo giá ngang mệnh giá (*par*) [[src-tata-bank-alm#^tata-gap-2]]. Đối với các công cụ có dòng tiền phụ thuộc vào mức lãi suất (như quyền chọn trả nợ trước hạn hay công cụ thả nổi), dự phóng dòng tiền bắt buộc phải được điều chỉnh tương ứng [[src-tata-bank-alm#^tata-ev-3]].

## Công thức tính toán chuẩn hoá

Theo Khuôn khổ chuẩn hoá của [[bcbs-irrbb]], với mỗi đồng tiền trọng yếu $c$ và kịch bản sốc lãi suất $i \in \{1..6\}$, biến động giá trị kinh tế $\Delta\text{EVE}_{i,c}$ được xác định qua 4 bước:

### 1. Chiết khấu dòng tiền tái định giá thuần
Trong mỗi kịch bản $i$, mọi notional repricing cash flow ([[notional-repricing-cash-flow]]) được slot vào dải $k$; dòng tiền dương và âm trong cùng dải được bù trừ thành một vị thế ròng $CF_{i,c}(k)$ [[src-bcbs-irrbb-2016#^irrbb-u05-17]]. Vị thế ròng tại dải $k$ (hoặc điểm giữa $t_k$) được chiết khấu theo hệ số chiết khấu liên tục:

$$
DF_{i,c}(t_k) = \exp\left(-R_{i,c}(t_k) \cdot t_k\right)
$$

[[src-bcbs-irrbb-2016#^irrbb-u05-18]]

Trong đó $R_{i,c}(t_k)$ phản ánh kịch bản sốc $i$ của đồng tiền $c$ theo Annex 2 [[src-bcbs-irrbb-2016#^irrbb-u05-18]]. Hệ số chiết khấu phải đại diện cho risk-free zero coupon rate; nếu ngân hàng đã đưa commercial margin và spread component vào dòng tiền thì lãi suất chiết khấu cũng cộng các phần này [[src-bcbs-irrbb-2016#^irrbb-u05-19]].

### 2. Giá trị kinh tế không bao gồm quyền chọn tự động ($\text{EVE}^{\text{nao}}$)

$$
\text{EVE}_{i,c}^{\text{nao}} = \sum_{k=1}^{K} CF_{i,c}(k) \cdot DF_{i,c}(t_k)
$$

[[src-bcbs-irrbb-2016#^irrbb-u05-20]]

### 3. Tổn thất EVE từng kịch bản và loại tiền tệ kèm add-on quyền chọn tự động

$$
\Delta\text{EVE}_{i,c} = \text{EVE}_{0,c}^{\text{nao}} - \text{EVE}_{i,c}^{\text{nao}} + \text{KAO}_{i,c}
$$

[[src-bcbs-irrbb-2016#^irrbb-u05-21]]

Trong đó:
- $\text{EVE}_{0,c}^{\text{nao}}$ là giá trị kinh tế theo đường cong lãi suất cơ sở ban đầu.
- $\text{KAO}_{i,c}$ là phần bù rủi ro quyền chọn lãi suất tự động (automatic interest rate options add-on) được định giá lại toàn bộ dưới kịch bản sốc lãi suất kết hợp mức tăng 25% độ biến động ngầm định [[src-bcbs-irrbb-2016#^irrbb-u05-7]].

### 4. Tổng hợp đa tiền tệ và Thước đo rủi ro EVE cực đại
Theo quy chuẩn Basel d368, tổng hợp tổn thất trên tất cả các đồng tiền trọng yếu với nguyên tắc thận trọng không bù trừ lãi từ đồng tiền khác nếu tổng thể đồng tiền đó sinh lời ($\Delta\text{EVE}_{i,c} > 0$ đại diện cho tổn thất):

$$
\Delta\text{EVE}_i = \max\left(0; \sum_{c: \Delta\text{EVE}_{i,c} > 0} \Delta\text{EVE}_{i,c}\right)
$$

Thước đo rủi ro EVE chuẩn hoá tổng thể là mức tổn thất lớn nhất trong 6 kịch bản sốc:

$$
\text{Standardised EVE risk measure} = \max_{i \in \{1..6\}} \Delta\text{EVE}_i
$$

[[src-bcbs-irrbb-2016#^irrbb-u05-8]]

Cơ quan giám sát quốc gia được phép quy định cách gộp tiền tệ khác cho ngân hàng của mình, nếu chứng minh được bằng bằng chứng rằng cách đó vẫn phù hợp khẩu vị IRRBB của jurisdiction [[src-bcbs-irrbb-2016#^irrbb-u05-24]].

## Quy chuẩn công bố Trụ cột 3 (Nguyên tắc 8)

Khi tính toán $\Delta\text{EVE}$ phục vụ công bố thông tin theo Bảng B [[src-bcbs-irrbb-2016#^irrbb-p08-1]], ngân hàng phải tuân thủ nghiêm ngặt các nguyên tắc:
1. **Loại trừ vốn chủ sở hữu**: Vốn chủ sở hữu không được gán lãi suất hay kỳ hạn mà bị loại bỏ hoàn toàn khỏi tính toán; tỷ lệ sụt giảm được so sánh trực tiếp với quy mô vốn tự có [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
2. **Dòng tiền toàn diện**: Bao gồm tất cả tài sản sinh lời, nợ phải trả và các cam kết ngoại bảng chịu lãi suất; loại trừ tài sản cố định và các khoản đầu tư vốn bị trừ khỏi vốn CET1 [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
3. **Đường cong chiết khấu**: Sử dụng lãi suất phi rủi ro (risk-free zero coupon rate, ví dụ đường cong [[overnight-index-swap|OIS]] hoặc swap có bảo đảm); nếu dòng tiền tính cả biên thương mại (commercial margin) thì lãi suất chiết khấu cũng phải cộng thêm biên tương ứng [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
4. **Giả định bảng cân đối**: Bắt buộc sử dụng giả định bảng cân đối run-off [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

## So sánh với Thước đo Thu nhập ($\Delta\text{NII}$)

| Đặc tính so sánh | Thước đo Giá trị kinh tế ($\Delta\text{EVE}$) | Thước đo Thu nhập ($\Delta\text{NII}$) |
|---|---|---|
| **Mục tiêu đo lường** | Biến động giá trị thị trường nội tại của vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-u06-5]] | Biến động lợi nhuận từ lãi trong kỳ kế toán [[src-bcbs-irrbb-2016#^irrbb-u06-5]] |
| **Đường chân trời** | Dài hạn — Run-off horizon đến khi tài sản/nợ cuối cùng đáo hạn [[src-bcbs-irrbb-2016#^irrbb-p04-2]] | Ngắn-trung hạn — 12 tháng (công bố) hoặc 1–3 năm [[src-bcbs-irrbb-2016#^irrbb-p08-3]] |
| **Giả định bảng cân đối** | Run-off balance sheet (không tái đầu tư) [[src-bcbs-irrbb-2016#^irrbb-p08-2]] | Constant balance sheet (tái đầu tư thay thế tương đương) hoặc Dynamic [[src-bcbs-irrbb-2016#^irrbb-p08-3]] |
| **Đối xử với Vốn chủ sở hữu** | Loại bỏ khỏi dòng tiền chiết khấu [[src-bcbs-irrbb-2016#^irrbb-p08-2]] | Vốn chủ sở hữu tạo ra thu nhập cơ sở (endowment return) [[src-bcbs-irrbb-2016#^irrbb-u06-6]] |
| **Cơ chế chiết khấu** | Chiết khấu dòng tiền theo đường cong phi rủi ro [[src-bcbs-irrbb-2016#^irrbb-p08-2]] | Không chiết khấu (tính toán số học chênh lệch thu nhập) [[src-bcbs-irrbb-2016#^irrbb-u06-5]] |
| **Trọng tâm quản trị** | Cơ quan giám sát (Pillar 2 capital adequacy & Outlier test) [[src-bcbs-irrbb-2016#^irrbb-u02-4]] | Ban điều hành & [[alco|ALCO]] (kế hoạch tài chính, cổ tức, P&L) [[src-bcbs-irrbb-2016#^irrbb-u02-4]] |

## Nghịch lý giữa EVE và Giá trị Thị trường Cổ phiếu (Moorad Choudhry)

Trong thực tế điều hành ngân hàng, tồn tại một nghịch lý thú vị giữa chỉ số EVE theo quy định giám sát và giá trị thị trường thực tế của ngân hàng (thị giá cổ phiếu nhân với số lượng cổ phiếu đang lưu hành), được Moorad Choudhry phân tích sâu sắc (*The Principles of Banking*, Ch. 7) [[src-choudhry-principles-banking#^choudhry-irrbb-11]]:

> "As one might conclude, the market itself views any rise in interest rates, or an expectation of rising interest rates, as a reason to mark up the price of a bank's shares. Up, not down. In other words, all else being equal (a faintly silly term, as all else is rarely, if ever, equal!), the market value of a bank, as measured by its share price multiplied by the number of its shares in issue, will rise when interest rates rise. This is in the opposite direction of movement to the EVE metric for most banks, when measured for the impact of a rise in rates."

### Phân tích Bản chất Nghịch lý
1. **Góc nhìn EVE (Run-off Balance Sheet & Giá trị hiện tại)**: Phần lớn các ngân hàng thương mại duy trì cấu trúc kỳ hạn tài sản dài hơn nợ phải trả (mismatch dương / duration gap dương). Khi lãi suất tăng, giá trị hiện tại của tài sản giảm mạnh hơn nợ, khiến $\Delta\text{EVE} < 0$ (sụt giảm giá trị kinh tế).
2. **Góc nhìn Thị trường Cổ phiếu (Going Concern & Lợi nhuận kỳ vọng)**: Thị trường cổ phiếu thường phản ứng tích cực với môi trường lãi suất tăng (hoặc kỳ vọng tăng lãi suất), đẩy giá cổ phiếu ngân hàng tăng lên. Nguyên nhân là các nhà đầu tư kỳ vọng lợi nhuận thuần từ lãi ([[net-interest-income-sensitivity|NII]]) và biên lãi thuần ([[net-interest-margin|Net Interest Margin]] - NIM) sẽ mở rộng nhờ hiệu ứng hưởng lợi từ tiền gửi chi phí thấp không kỳ hạn (endowment effect).
3. **Ý nghĩa quản trị ALCO**: Ban điều hành và ALCO không được nhầm lẫn giữa phản ứng ngắn hạn của giá cổ phiếu với mức độ an toàn vốn dài hạn. EVE đại diện cho giá trị nội tại dài hạn để bảo vệ quyền lợi của người gửi tiền và các chủ nợ theo tiêu chuẩn Trụ cột 2 của Basel d368 [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

### Xử lý Quy định khi Stressed EVE Vượt Khẩu vị Rủi ro
Theo Moorad Choudhry [[src-choudhry-principles-banking#^choudhry-irrbb-12]]:
> "In order to manage this risk a bank will measure the exposure sensitivity of this 'interest- rate risk in the banking book' by calculating the earnings and present value of the balance sheet baseline numbers, and then stressing the calculated values under different rate scenarios. If the stressed impact is outside the approved [[risk-appetite|risk appetite]], under regulatory rules it must either immunise this risk using organic hedges or derivative hedges, or assign more Tier 1 capital to cover the exposure, or otherwise remove the risk from the balance sheet."

Khi kết quả kiểm tra sức chịu đựng (stress test) EVE vượt khỏi mức khẩu vị rủi ro được phê duyệt (hoặc chạm ngưỡng [[outlier-bank-test]]), ngân hàng có 3 giải pháp bắt buộc theo quy định:
1. **Phòng ngừa rủi ro (Immunise)**: Thực hiện phòng ngừa tự nhiên (organic hedges - tái cơ cấu lại kỳ hạn tài sản và nợ trên bảng cân đối) hoặc sử dụng các công cụ phái sinh lãi suất (derivative hedges như [[interest-rate-swap]]).
2. **Bổ sung Vốn tự có (Assign Tier 1 Capital)**: Bổ sung thêm vốn Cấp 1 để bù đắp rủi ro theo yêu cầu Trụ cột 2 (Pillar 2 capital add-on).
3. **Giảm thiểu danh mục (De-risking)**: Bán hoặc loại bỏ các tài sản dài hạn nhạy cảm lãi suất ra khỏi bảng cân đối.

### Góc nhìn phương pháp (nguồn T4)
- **Internal view và external view (Lubinska)**: internal view chiết khấu theo lãi suất phi rủi ro, external view giữ biên thương mại; hệ số chiết khấu phải nhất quán với cách tách biên qua FTP [[src-lubinska-alm-optimisation#^lubinska-u02-38]]. Đường phi rủi ro có thể là secured IRS hoặc OIS [[src-lubinska-alm-optimisation#^lubinska-u02-42]].
- Dòng tiền có điều kiện (conditional cash flows) là best practice [[src-lubinska-alm-optimisation#^lubinska-u02-39]]. EVE bắt được độ lồi ([[convexity]]); ΔEVE tĩnh có thể mô phỏng nghiệp vụ tương lai [[src-lubinska-alm-optimisation#^lubinska-u02-40]]. Case study: KAO bù lỗ EVE ở mọi kịch bản giảm lãi suất [[src-lubinska-alm-optimisation#^lubinska-u02-41]]. Xem [[pv01]].
- **Tham chiếu EU (Tata)**: phương pháp chuẩn hoá của EBA cho EVE bằng EVE kịch bản sốc trừ EVE cơ sở, có add-on quyền chọn tự động và giới hạn giả định hành vi [[src-tata-bank-alm#^tata-eba-2]] [[src-tata-bank-alm#^tata-eba-3]]; SOT EVE dùng bảng cân đối run-off với sàn tuyến tính −150 bp tăng tới 0% ở 50 năm [[src-tata-bank-alm#^tata-sot-1]] [[src-tata-bank-alm#^tata-sot-2]]. Xem [[outlier-bank-test]].

## Mối liên kết chiến lược với Đệm HQLA và NSFR
- **Thời lượng HQLA**: Danh mục trái phiếu chính phủ Level 1 trong [[lcr]] có thời lượng bình quân lớn (ví dụ duration 5–7 năm) sẽ tạo ra mức nhạy cảm lãi suất cực lớn ($\text{PV01}$ cao). Khi chịu cú sốc tăng lãi suất song song (+200 bps USD/EUR), danh mục HQLA sẽ sụt giảm giá trị thị trường sâu sắc, kéo giảm nghiêm trọng $\Delta\text{EVE}$ và đẩy ngân hàng vào nguy cơ vi phạm ngưỡng ngoại lai 15% Tier 1 Capital.
- **Tài trợ chênh lệch kỳ hạn trong NSFR**: Một ngân hàng duy trì tài sản dài hạn (RSF 85%–100%) tài trợ bởi tiền gửi ngắn hạn sẽ chịu chênh lệch kỳ hạn âm lớn, khiến EVE cực kỳ tổn thương trước các cú sốc tăng dốc đường cong (steepener) hoặc tăng song song.
- **Mô hình định lượng và công cụ phòng ngừa liên quan**:
  - [[duration-gap-model|Mô hình Chênh lệch Thời lượng (Duration Gap Model)]]: Phân tích độ nhạy tổng thể và phương trình miễn nhiễm vốn tự có.
  - [[key-rate-duration|Thời lượng Lãi suất Từng Kỳ hạn (Key Rate Duration - KRD)]]: Phân rã độ nhạy trên 19 dải kỳ hạn để đo lường rủi ro xoay trục đường cong.
  - [[economic-value-at-risk|Giá trị Kinh tế Chịu Rủi ro (EVaR)]]: Đo lường tổn thất EVE tối đa theo phương pháp phân phối xác suất và mô phỏng Monte Carlo.
  - [[interest-rate-swap|Hợp đồng Hoán đổi Lãi suất (IRS)]]: Công cụ tái cân bằng thời lượng và phòng ngừa tổn thất EVE chủ lực.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Định nghĩa | Biến động giá trị kinh tế dưới các kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-u01-4]] | Thay đổi giá trị hiện tại ròng giữa dòng tiền vào của tài sản và dòng tiền ra của nợ phải trả nhạy cảm với lãi suất khi lãi suất thay đổi [[src-tt83-2025-nhnn#^pl5-a-0]] | d368 par 4; TT83 PL5.A | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Lãi suất chiết khấu | Risk-free rate, hoặc cộng commercial margin nếu dòng tiền gồm margin [[src-bcbs-irrbb-2016#^irrbb-u05-19]] | Lãi suất phi rủi ro (risk-free rate) [[src-tt83-2025-nhnn#^pl5-a3-2]] | d368 par 132; TT83 PL5.A.III.2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Hệ số chiết khấu (VN, chi tiết) | Theo đường cong phi rủi ro [[src-bcbs-irrbb-2016#^irrbb-p08-2]] | Dòng tiền ròng chiết khấu bằng hệ số lãi kép liên tục theo kịch bản và đồng tiền; ngân hàng tính hệ số phù hợp với cách phân bổ dòng tiền (thang hay điểm giữa) [[src-tt83-2025-nhnn#^pl5-a3-2b]] | TT83 PL5.A.III.2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| $\text{KAO}_{i,c}$ | Định giá lại quyền chọn với độ biến động ngầm định tăng tương đối 25% [[src-bcbs-irrbb-2016#^irrbb-u05-7]] | Ngân hàng tự đo lường [[src-tt83-2025-nhnn#^pl5-a4]] | d368 par 130; TT83 PL5.A.IV | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Tổng hợp đa tiền tệ | Cộng tổn thất dương giữa các đồng tiền, lấy kịch bản lớn nhất [[src-bcbs-irrbb-2016#^irrbb-u05-8]] | Như Basel [[src-tt83-2025-nhnn#^pl5-a5]] | d368 par 132; TT83 PL5.A.V | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| [[risk-limits|Hạn mức]] | Phải có policy limits nhất quán với risk appetite; risk appetite nên thể hiện theo cả economic value và earnings [[src-bcbs-irrbb-2016#^irrbb-p03-1]]; hạn mức tổng nên áp dụng hợp nhất, có thể gắn với kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-p03-3]] | Phải có hạn mức thay đổi giá trị kinh tế của vốn chủ sở hữu [[src-tt83-2025-nhnn#^d53-2]] | d368 Principle 3, par 29; TT83 Đ53.2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Vượt hạn mức | Vị thế vượt hoặc có khả năng vượt nên được xử lý kịp thời và báo cáo lên ngay [[src-bcbs-irrbb-2016#^irrbb-p03-4]] | Phải có cảnh báo sớm khi gần vượt và biện pháp xử lý kịp thời khi vượt [[src-tt83-2025-nhnn#^d54-4c]] | d368 par 32; TT83 Đ54.4.c | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Lộ trình | Hiệu lực 2018 [[src-bcbs-irrbb-2016#^irrbb-u04-2]] | Được dùng ΔNII hoặc ΔEVE [[src-tt83-2025-nhnn#^d74-4a]]; phải dùng cả hai [[src-tt83-2025-nhnn#^d74-4b]] | TT83 Đ74.4 | 01/07/2026 – 31/12/2027; chậm nhất 01/01/2028 |
| Phép thử outlier | ∆EVE so với 15% Tier 1 (should) [[src-bcbs-irrbb-2016#^irrbb-p12-1]] | Không có trong C3-M7, PL5 [cần nguồn] | d368 par 88 | |
| Stress test IRRBB | IMS tính tác động của nhiều kịch bản: kịch bản nội bộ theo ICAAP, kịch bản lịch sử và giả định, sáu kịch bản sốc chuẩn hoá [[src-bcbs-irrbb-2016#^irrbb-p04-3]] | Tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]] | TT83 Đ23.5 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Dùng cho vốn | Vốn IRRBB xét trong ICAAP theo rủi ro giá trị kinh tế [[src-bcbs-irrbb-2016#^irrbb-p09-2]] | [[rwa-irrbb\|RWA_IRRBB]] trong vốn kinh tế tính theo ΔEVE, chậm nhất từ 01/01/2028 [[src-tt83-2025-nhnn#^pl6-1c]] | d368 Nguyên tắc 9; TT83 PL6 | 01/01/2028 |

Khác biệt: [[tt83-2025]] chỉ cho chiết khấu theo risk-free rate và để ngân hàng tự đo KAO; C3-M7 và Phụ lục V không có phép thử outlier.

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
