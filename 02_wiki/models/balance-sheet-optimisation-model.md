---
title: "Mô Hình Tối Ưu Hóa Bảng Cân Đối Kế Toán (Balance Sheet Optimisation Model)"
aliases: [Balance Sheet Optimisation Model, Mô hình tối ưu hóa bảng cân đối, KKT Balance Sheet Optimisation, Interior Point ALM Optimisation, Tối ưu hóa cấu trúc tài sản nợ]
type: model
domains: [alm, basel]
status: active
maturity: draft
sources: ["[[src-lubinska-alm-optimisation]]", "[[src-vab-ftp]]", "[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-bardaeva-alm]]"]
relations:
  - {type: drives, to: "[[repricing-balance-sheet]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u04-13]]"}
tags: [alm, model, balance-sheet-optimisation, kkt-conditions, interior-point, constant-balance-sheet, matlab-fmincon]
updated: 2026-10-20
reviewed:
---

## Mục tiêu

Mô hình Tối ưu hóa Bảng cân đối Kế toán (Balance Sheet Optimisation Model) là công cụ toán học định lượng dùng để xác định cơ cấu phân bổ tối ưu của các nhóm tài sản sinh lời và nguồn vốn huy động nhằm đạt được mục tiêu tài chính cao nhất (tối đa hóa thu nhập từ tài sản và tối thiểu hóa chi phí nguồn vốn) trong khi vẫn thỏa mãn đồng thời các giới hạn an toàn quy định và khẩu vị rủi ro nội bộ [[src-lubinska-alm-optimisation#^lubinska-u04-13]].

Theo Bardaeva (2021), sự ra đời của Banking Package (Basel IV, CRR II, CRD V, BRRD II) tạo ra sự liên kết toàn diện (complete interrelation) giữa Vốn, Thanh khoản (LCR/NSFR, tránh cliff effect), IRRBB và MREL [[src-bardaeva-alm#^ch6-1]] [[src-bardaeva-alm#^ch6-2]]. Nếu ngân hàng duy trì riêng lẻ từng tỷ lệ thì chi phí gánh chịu sẽ quá lớn và triệt tiêu khả năng sinh lời. Do đó, ALM hiện đại chuyển trọng tâm sang giải bài toán tối ưu hoá đa tham số nhằm nhận diện và điều phối "điểm nghẽn" (the most binding restriction / bottleneck) giữa các rào cản quy định và khả năng sinh lời kinh doanh [[src-bardaeva-alm#^ch6-3]] [[src-bardaeva-alm#^ch6-4]].

Theo Beata Lubinska (2020), bài toán tối ưu hóa sổ ngân hàng hầu như luôn là bài toán phi tuyến chịu các ràng buộc bất đẳng thức (inequality constraints) [[src-lubinska-alm-optimisation#^lubinska-u04-12]]:
- Ràng buộc biến động thu nhập lãi thuần ([[net-interest-income-sensitivity|NII volatility]]) được biểu diễn dưới dạng bất đẳng thức xác lập khoảng dao động chấp nhận được [[src-lubinska-alm-optimisation#^lubinska-u04-12]].
- Ràng buộc tỷ lệ thanh khoản ngắn hạn ([[lcr|LCR]] / Survival Horizon) và tỷ lệ thanh khoản cấu trúc ([[structural-liquidity-risk]]; [[nsfr|NSFR]] / Structural Liquidity Ratio) được thiết lập như các ngưỡng sàn tối thiểu [[src-lubinska-alm-optimisation#^lubinska-u04-12]].

Mô hình được giải thông qua việc thỏa mãn các điều kiện Karush-Kuhn-Tucker (KKT) và ứng dụng thuật toán điểm trong (Interior-point algorithm / logarithmic barrier method) [[src-lubinska-alm-optimisation#^lubinska-u04-12]] [[src-lubinska-alm-optimisation#^lubinska-u04-13]].

---

## Công thức

### 1. Thiết Lập Hàm Mục Tiêu Kép (Dual Objective Functions)
Bài toán tối ưu hóa được phân tách thành hai hàm mục tiêu riêng biệt [[src-lubinska-alm-optimisation#^lubinska-u04-13]]:

1. **Hàm tối đa hóa thu nhập từ danh mục tài sản**:
   $$\max_{w_A} \; f_A(w_A) = \sum_{j=1}^J w_{A,j} \cdot r_{A,j}$$
   Trong đó $w_{A,j}$ là tỷ trọng của nhóm tài sản thứ $j$ trong tổng tài sản, và $r_{A,j}$ là lợi suất danh nghĩa hoặc lợi suất điều chỉnh rủi ro của tài sản $j$ [[src-lubinska-alm-optimisation#^lubinska-u04-13]].

2. **Hàm tối thiểu hóa chi phí danh mục nguồn vốn**:
   $$\min_{w_L} \; f_L(w_L) = \sum_{k=1}^K w_{L,k} \cdot c_{L,k}$$
   Trong đó $w_{L,k}$ là tỷ trọng của nguồn vốn thứ $k$ trong tổng nguồn nợ, và $c_{L,k}$ là chi phí huy động vốn cận biên (gồm cả lãi suất khách hàng và phụ phí thanh khoản) của nguồn vốn $k$ [[src-lubinska-alm-optimisation#^lubinska-u04-13]].

### 2. Hệ Thống Ràng Buộc Đa Tầng (Multi-Tier Constraints System)
Theo Beata Lubinska (2020), hệ thống ràng buộc trong mô hình phản ánh khẩu vị rủi ro (xem [[risk-appetite]]) và các chuẩn mực pháp định gồm các nhóm bất đẳng thức cụ thể sau [[src-lubinska-alm-optimisation#^lubinska-u04-12]] [[src-lubinska-alm-optimisation#^lubinska-u05-11]]:

$$\begin{aligned}
\text{Tổng tỷ trọng:} \quad & \sum_{j=1}^J w_{A,j} = 1, \quad \sum_{k=1}^K w_{L,k} = 1 \\
\text{Cân đối bảng:} \quad & \text{Total Assets} = \text{Total Liabilities} + \text{Equity} \\
\text{Điều kiện không âm:} \quad & w_{A,j} > 0, \quad w_{L,k} > 0 \quad (\text{bảo toàn mô hình kinh doanh}) \\
\text{Chân trời sinh tồn (SH):} \quad & \frac{\text{LAB} + \text{TI}_{30-90\text{d}}}{\text{TO}_{30-90\text{d}}} \ge 100\% \\
\text{Thanh khoản cấu trúc:} \quad & \frac{\text{TI}_{T > 1\text{Y}} + \text{Tier 1 Capital}}{\text{TO}_{T > 1\text{Y}}} \ge 100\% \\
\text{Tín dụng trên tiền gửi:} \quad & \frac{\text{Loans}}{\text{Deposits}} \le 80\% \\
\text{Tập trung nguồn vốn:} \quad & w_{L,k} \le 80\% \quad (\forall k) \\
\text{Độ nhạy thu nhập lãi thuần:} \quad & \frac{|\Delta\text{NII}_{\pm 200\text{bps}}|}{\text{NII}} \le 4\% \quad (\text{kèm sàn Floor } 0\%) \\
\text{Tỷ lệ an toàn vốn (CAR):} \quad & \frac{\text{Tier 1} + \text{Tier 2}}{\text{RWA}} \ge 10.5\%
\end{aligned}$$

- **Điều kiện không âm (Non-negativity condition)**: Mô hình nghiêm cấm triệt tiêu bất kỳ phân khúc sản phẩm nào về 0 ($w_{A,j} > 0, w_{L,k} > 0$) vì mục tiêu là tái cấu trúc tỷ trọng tối ưu, không làm biến dạng mô hình kinh doanh hoặc phá hủy thương quyền khách hàng [[src-lubinska-alm-optimisation#^lubinska-u05-10]].
- **Chân trời sinh tồn (Survival Horizon - SH)**: Đệm tài sản thanh khoản LAB tối thiểu phải tương đương dòng tiền ra ròng chịu căng thẳng trong 30, 60, 90 ngày [[src-lubinska-alm-optimisation#^lubinska-u05-4]] [[src-lubinska-alm-optimisation#^lubinska-u05-5]].
- **Thanh khoản cấu trúc và tỷ lệ A/D**: Hạn chế chuyển đổi kỳ hạn ([[maturity-transformation]]) vượt quá 1 năm và giữ tỷ lệ tín dụng trên tiền gửi dưới 80% để tránh phụ thuộc bán buôn [[src-lubinska-alm-optimisation#^lubinska-u05-6]] [[src-lubinska-alm-optimisation#^lubinska-u05-7]].
- **Giới hạn tập trung nguồn vốn**: Khống chế trần 80% cho từng nguồn tài trợ nhằm bảo đảm đa dạng hóa nguồn vốn [[src-lubinska-alm-optimisation#^lubinska-u05-11]].
- **Độ nhạy thu nhập lãi thuần $\Delta\text{NII}$ và sàn lãi suất 0%**: Giới hạn tổn thất thu nhập lãi thuần dưới 4% khi sốc lãi suất $\pm 200$ bps (chuẩn ECB) trên constant balance sheet [[src-lubinska-alm-optimisation#^lubinska-u05-8]] [[src-lubinska-alm-optimisation#^lubinska-u05-11]], đồng thời đặt sàn Floor 0% phản ánh quyền chọn sàn tự động trong hợp đồng tín dụng và cam kết không áp lãi suất âm cho tiền gửi bán lẻ [[src-lubinska-alm-optimisation#^lubinska-u05-9]]. Xem [[negative-interest-rates]].
- **Ràng buộc an toàn vốn (CAR)**: Tuân thủ mức vốn tối thiểu 10.5% theo chuẩn Basel III (gồm 8% tối thiểu và 2.5% đệm bảo toàn vốn) [[src-lubinska-alm-optimisation#^lubinska-u05-11]].

### 3. Điều Kiện Tối Ưu Karush-Kuhn-Tucker (KKT)
Điều kiện Karush-Kuhn-Tucker là điều kiện cần bậc nhất cho nghiệm tối ưu của bài toán quy hoạch phi tuyến có ràng buộc bất đẳng thức $c_i(x) \ge 0$ và đẳng thức $h_j(x) = 0$ [[src-lubinska-alm-optimisation#^lubinska-u04-13]]:

$$L(x, \lambda, \mu) = f(x) - \sum_{i} \lambda_i c_i(x) - \sum_{j} \mu_j h_j(x)$$

Các điều kiện KKT bao gồm [[src-lubinska-alm-optimisation#^lubinska-u04-13]]:
1. **Tính dừng (Stationarity)**: $\nabla_x f(x^*) - \sum_i \lambda_i^* \nabla_x c_i(x^*) - \sum_j \mu_j^* \nabla_x h_j(x^*) = 0$.
2. **Khả thi nguyên thủy (Primal feasibility)**: $c_i(x^*) \ge 0, \; h_j(x^*) = 0$.
3. **Khả thi đối ngẫu (Dual feasibility)**: $\lambda_i^* \ge 0$.
4. **Bù trừ tương hỗ (Complementary slackness)**: $\lambda_i^* \cdot c_i(x^*) = 0, \quad \forall i$.

### 4. Thuật Toán Điểm Trong (Interior-Point / Barrier Algorithm)
Vì các bài toán trong ngân hàng thường có số lượng biến lớn và phi tuyến, hệ phương trình KKT không thể giải giải tích dạng đóng mà phải dùng phương pháp số [[src-lubinska-alm-optimisation#^lubinska-u04-12]]. Thuật toán điểm trong xấp xỉ bài toán ràng buộc bất đẳng thức bằng hàm rào cản logarithmic (*logarithmic barrier function*) [[src-lubinska-alm-optimisation#^lubinska-u04-12]]:

$$B(x, \mu) = f(x) - \mu \sum_{i} \ln(c_i(x))$$

Trong đó $\mu > 0$ là tham số rào cản (*barrier parameter*). Khi $\mu \to 0$, nghiệm của hàm rào cản $B(x, \mu)$ hội tụ về nghiệm tối ưu của bài toán ban đầu, và nghiệm luôn được tiếp cận từ phần không gian khả thi bên trong (*strict interior of the feasible region*) [[src-lubinska-alm-optimisation#^lubinska-u04-12]]. Thuật toán này được hiện thực hóa qua hàm `fmincon` trong MATLAB [[src-lubinska-alm-optimisation#^lubinska-u04-12]].

---

## Inputs & giả định

1. **Giả định bảng cân đối không đổi (Constant balance sheet / Like-for-like assumption)**:
   - Các dòng tiền đáo hạn hoặc tái định giá của tài sản và nợ được giả định thay thế bằng các công cụ mới có cùng đặc tính tài chính và kỳ hạn tái định giá [[src-lubinska-alm-optimisation#^lubinska-u04-13]].
2. **Dữ liệu phân loại tài sản và nợ**:
   - Tỷ trọng ban đầu của từng danh mục trên [[repricing-balance-sheet|Bảng cân đối tái định giá]].
   - Lợi suất tài sản danh nghĩa $r_{A,j}$ và chi phí huy động nợ $c_{L,k}$.
3. **Các tham số hành vi và điều chỉnh rủi ro**:
   - Tỷ lệ tiền gửi không kỳ hạn lõi (Core %) và phi lõi (Non-core %) theo mô hình hàm mũ $3.1\sigma$ hoặc độ biến động tháng 95% [[src-lubinska-alm-optimisation#^lubinska-u04-6]] [[src-lubinska-alm-optimisation#^lubinska-u04-7]].
   - Tỷ lệ trả nợ trước hạn CPR (phân rã thành structural và financial prepayments có tính đến burnout effect) [[src-lubinska-alm-optimisation#^lubinska-u04-8]] [[src-lubinska-alm-optimisation#^lubinska-u04-10]].
   - Tỷ lệ rút tiền gửi có kỳ hạn sớm TDRR [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
4. **Hạn mức khẩu vị rủi ro của ALCO ([[alco]])**:
   - Sàn LCR (thường $\ge 105\% - 110\%$), sàn NSFR (thường $\ge 105\%$).
   - Trần tổn thất EVE ($15\%$ Vốn cấp 1 CET1) và trần biến động NII.

---

## Calibration

- Hiệu chỉnh tham số rào cản $\mu$ trong thuật toán Interior-point giảm dần qua từng bước lặp để đảm bảo tính hội tụ ổn định.
- Hiệu chỉnh các trọng số ràng buộc dựa trên ma trận chi phí vốn FTP (bóc tách chi phí duy trì đệm thanh khoản dự phòng contingent liquidity cost và phụ phí kỳ hạn TLP) [[src-lubinska-alm-optimisation#^lubinska-u04-3]] [[src-vab-ftp#^vab-ftp-12]].

---

## Output & usage

- **Regulatory**: Đảm bảo cấu trúc tài sản - nợ tuân thủ tuyệt đối các chuẩn mực Basel III / NHNN (LCR, NSFR, Leverage Ratio, Outlier Bank Test) trong mọi kịch bản sốc lãi suất.
- **Management**:
  - Cung cấp cho Hội đồng ALCO cơ cấu bảng cân đối mục tiêu (*target balance sheet profile*) cho chu kỳ lập kế hoạch 1–3 năm.
  - Xác lập các gói định hướng ưu đãi hoặc hạn chế (*incentive / disincentive overlays*) thông qua hệ thống [[ftp-pricing-methodology|FTP]] để điều hướng mạng lưới chi nhánh tăng/giảm quy mô từng sản phẩm cụ thể.

---

## Thực Nghiệm Kiểm Chứng & Động Lực Nhạy Cảm (Empirical Case Studies & Sensitivity Drivers)

Theo Beata Lubinska (2020), việc ứng dụng mô hình tối ưu hóa định lượng trên dữ liệu thực tế tại hai ngân hàng điển hình (Ngân hàng 1 quy mô nhỏ EUR 3.4 tỷ và Ngân hàng 2 quy mô lớn USD 549 tỷ) đã xác thực các quy luật thực tiễn quan trọng [[src-lubinska-alm-optimisation#^lubinska-u06-6]] [[src-lubinska-alm-optimisation#^lubinska-u06-13]]:

### 1. Phân Tích Kịch Bản "What-If" và Các Nhân Tố Độ Nhạy
Mô hình thực hiện kiểm định độ nhạy qua 5 kịch bản định trước [[src-lubinska-alm-optimisation#^lubinska-u06-1]] [[src-lubinska-alm-optimisation#^lubinska-u06-2]]:
- **Kịch bản cơ sở (Base scenario)**: Dựa trên mặt bằng lãi suất hiện hành và cấu trúc ban đầu của sổ ngân hàng [[src-lubinska-alm-optimisation#^lubinska-u06-2]].
- **Kịch bản biến động lãi suất (Interest rate scenarios)**: Đánh giá tác động dịch chuyển đường cong lợi suất lên cấu trúc mục tiêu; khi đường cong dịch chuyển đi lên (lạm phát, sốc dầu mỏ), mức cắt giảm chi phí vốn cao hơn so với kịch bản dịch chuyển đi xuống [[src-lubinska-alm-optimisation#^lubinska-u06-2]] [[src-lubinska-alm-optimisation#^lubinska-u07-6]].
- **Kịch bản thay đổi mô hình đặc tính hóa tiền gửi (Deposit characterisation model)**: Biến động tỷ lệ tiền gửi lõi/phi lõi và độ nhạy lãi suất CASA [[src-lubinska-alm-optimisation#^lubinska-u06-2]].
- **Kịch bản tích hợp tỷ lệ trả nợ trước hạn (Prepayment scenario)**: Áp dụng tỷ lệ trả nợ trước hạn liên tục CPR 7% cho tài sản lãi suất cố định, gây tác động kép lên biến động $\Delta\text{NII}$ và thanh khoản do phải tái đầu tư dòng tiền thu hồi sớm [[src-lubinska-alm-optimisation#^lubinska-u06-3]].
- **Kịch bản thay đổi cấu trúc tài sản ban đầu (Initial asset base)**: Thay đổi tỷ trọng giữa tài sản lãi suất thả nổi và cố định [[src-lubinska-alm-optimisation#^lubinska-u06-2]].
- **Cấu trúc khởi điểm là nhân tố nhạy cảm cốt tử (Initial Structure as Destiny Driver)**: Phân tích thực nghiệm chứng minh nhân tố nhạy cảm nhất quyết định biên độ thặng dư chính là cấu trúc bảng cân đối ban đầu tại thời điểm $t_0$ [[src-lubinska-alm-optimisation#^lubinska-u07-5]]. Tác giả nhận định một số ngân hàng dường như "được định sẵn" sinh lời vượt trội hơn từ mô hình tối ưu hóa ngay từ đầu thông qua cách thiết lập cơ cấu tài sản khởi điểm của họ [[src-lubinska-alm-optimisation#^lubinska-u07-5]].
- **Biên độ thặng dư tỷ lệ thuận với quy mô sổ ngân hàng**: Lợi ích kinh tế được xác nhận trên mọi kịch bản, và quy mô thặng dư tỷ lệ thuận với tổng quy mô tài sản [[src-lubinska-alm-optimisation#^lubinska-u07-4]].

### 2. Kết Quả Thực Nghiệm: Ngân Hàng 1 (Quy Mô Nhỏ EUR 3.4 Tỷ)
Ngân hàng 1 là minh chứng định lượng chi tiết cho toàn bộ chu trình tối ưu hóa [[src-lubinska-alm-optimisation#^lubinska-u07-9]] [[src-lubinska-alm-optimisation#^lubinska-u07-10]]:
- **Cấu trúc ban đầu $t_0$**: RSA đạt EUR 3.4 tỷ, phần lớn là cho vay doanh nghiệp thả nổi neo theo Euribor 1M ($78.37\%$), tài sản cố định ($20.31\%$), đệm LAB ($1.31\%$), trong khi nợ neo theo Euribor 3M/6M (chịu basis risk) [[src-lubinska-alm-optimisation#^lubinska-u06-4]] [[src-lubinska-alm-optimisation#^lubinska-u07-9]]. CASA có độ biến động cao (chỉ 35% stable, 65% biến động xếp vào dải O/N cho IRRBB và 1M cho thanh khoản) [[src-lubinska-alm-optimisation#^lubinska-u06-5]]. Trước khi tối ưu, ngân hàng vi phạm nghiêm trọng tỷ lệ thanh khoản ngắn hạn tích lũy ($59.7\%$ so với hạn mức $100\%$) và độ nhạy lãi suất $\Delta\text{NII}_{+200\text{bps}}$ lên tới $80.5\%$ [[src-lubinska-alm-optimisation#^lubinska-u07-9]].
- **Minh chứng định lượng tái cấu trúc Tài sản**:
  - Cơ cấu sau tối ưu: Tài sản thả nổi giảm về $30.58\%$, Tài sản cố định tăng lên $66.02\%$, Đệm LAB tăng lên $3.39\%$ [[src-lubinska-alm-optimisation#^lubinska-u07-10]].
  - Thu nhập lãi tăng từ EUR 0.075 tỷ lên EUR 0.0819 tỷ / 6 tháng, tạo thặng dư thu nhập **EUR 6.9 triệu** trong 6 tháng (EUR 13.8 triệu quy năm) [[src-lubinska-alm-optimisation#^lubinska-u07-11]]. Dưới kịch bản khủng hoảng dầu mỏ, thặng dư thu nhập 6 tháng đạt EUR 10.49 triệu [[src-lubinska-alm-optimisation#^lubinska-u06-6]].
- **Minh chứng định lượng tái cấu trúc Nguồn vốn**:
  - Cơ cấu ban đầu $t_0$: CASA DN $7.4\%$, Tiền gửi kỳ hạn $1.5\%$, Vốn bán buôn $70\%$, Trái phiếu $21\%$. Chi phí vốn: EUR 30.79 triệu / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u07-9]].
  - Cơ cấu sau tối ưu: CASA giảm về $2.5\%$, Tiền gửi kỳ hạn tăng lên $7.67\%$, Vốn bán buôn tăng lên sát trần tập trung $79.99\%$, Trái phiếu giảm về $9.8\%$. Chi phí vốn giảm xuống EUR 30.49 triệu / 6 tháng, mang lại thặng dư chi phí vốn **EUR 0.2964 triệu / năm** [[src-lubinska-alm-optimisation#^lubinska-u07-12]].
  - Thặng dư chi phí vốn đạt EUR 0.6677 triệu/năm dưới kịch bản vỡ nợ HY/LBO [[src-lubinska-alm-optimisation#^lubinska-u07-13]], và đạt mức đột biến **EUR 1.1954 triệu / năm** dưới kịch bản thay đổi mô hình đặc tính hóa CASA [[src-lubinska-alm-optimisation#^lubinska-u07-14]].
  - **Kịch bản thay đổi tỷ trọng danh mục tài sản**: Khi tỷ trọng tài sản phân bổ lệch mạnh (Asset 1 chiếm 83.69%), chi phí vốn ban đầu là EUR 29.67 triệu và ngân hàng vi phạm hạn mức thanh khoản ngắn hạn ($60.89\% < 100\%$) [[src-lubinska-alm-optimisation#^lubinska-u08-2]]. Mô hình tối ưu hóa tái phân bổ nguồn vốn (tăng tiền gửi thanh toán và kỳ hạn, đẩy wholesale funding lên $77.01\% - 79.99\%$, cắt giảm trái phiếu phát hành), giảm chi phí vốn xuống EUR 24.7 triệu hoặc EUR 29.1 triệu / 6 tháng, tạo thặng dư kinh tế từ **EUR 0.5663 triệu** đến **EUR 4.9560 triệu** và khôi phục thanh khoản ngắn hạn về $100\%$ [[src-lubinska-alm-optimisation#^lubinska-u08-1]] [[src-lubinska-alm-optimisation#^lubinska-u08-3]].
  - **Kịch bản hạ 1 bậc tín nhiệm (Downgrade by One Notch)**: Xếp hạng tín nhiệm giảm đẩy chi phí vốn vọt lên EUR 35.84 triệu / 6 tháng và tỷ lệ thanh khoản ngắn hạn rơi xuống mức vi phạm $59.8\%$. Mô hình KKT hạ chi phí vốn về EUR 35.2 triệu, tạo thặng dư **EUR 0.6388 triệu / năm**, khôi phục thanh khoản ngắn hạn về $100\%$ và nén $\Delta\text{NII}_{+200\text{bps}}$ từ $72.18\%$ xuống mức an toàn vượt trội **$6.8\%$** [[src-lubinska-alm-optimisation#^lubinska-u08-4]].
  - **Kịch bản tính đến tỷ lệ trả nợ trước hạn CPR**: Tỷ lệ thanh khoản ngắn hạn ban đầu bị vi phạm ở mức $62\%$. Mô hình tối ưu hóa giảm chi phí vốn từ EUR 29.67m xuống EUR 28.44m, tạo thặng dư **EUR 1.2244 triệu / năm**, đồng thời đưa thanh khoản ngắn hạn về $100\%$ và giảm $\Delta\text{NII}_{+200\text{bps}}$ từ $77\%$ về $67.68\%$ [[src-lubinska-alm-optimisation#^lubinska-u08-5]].
- **Khôi phục tuân thủ các hạn mức bị vi phạm (Boundary Restoration)**: Dù bước vào quá trình tối ưu với tỷ lệ thanh khoản ngắn hạn bị vi phạm (59.7%–62%), mô hình đã tự động đưa tỷ lệ thanh khoản về mức tuân thủ tuyệt đối **$100\%$** mà vẫn bảo toàn thặng dư kinh tế [[src-lubinska-alm-optimisation#^lubinska-u07-7]] [[src-lubinska-alm-optimisation#^lubinska-u07-10]] [[src-lubinska-alm-optimisation#^lubinska-u08-2]]. Dưới kịch bản kỳ vọng lạm phát, chi phí huy động vốn tăng nhẹ từ EUR 34.37m lên 34.88m được giải thích là chi phí kinh tế tối thiểu bắt buộc để khôi phục sự tuân thủ hạn mức thanh khoản ngắn hạn [[src-lubinska-alm-optimisation#^lubinska-u06-8]] [[src-lubinska-alm-optimisation#^lubinska-u06-9]] [[src-lubinska-alm-optimisation#^lubinska-u07-7]].
- **Tối ưu hóa đồng thời Lợi nhuận và Quản trị Rủi ro (Dual Optimization)**: Mô hình tối ưu hóa phi tuyến không đánh đổi liều lĩnh để lấy lợi nhuận mà đồng thời nén độ nhạy rủi ro lãi suất $\Delta\text{NII}_{+200\text{bps}}$ từ mức rủi ro cực cao $80.5\%$ xuống ngưỡng an toàn **$4\%$** [[src-lubinska-alm-optimisation#^lubinska-u07-10]], đáp ứng toàn diện các chỉ số thanh khoản, và ngăn chặn việc giữ thanh khoản đệm LAB dư thừa không hiệu quả hoặc tích trữ nguồn vốn dài hạn quá mức làm triệt tiêu tiềm năng lợi nhuận từ chuyển đổi kỳ hạn lành mạnh (*healthy maturity transformation*) [[src-lubinska-alm-optimisation#^lubinska-u07-8]].
- **Bất đối xứng độ nhạy hành vi**: Mô hình nhạy cảm cao hơn với các giả định hành vi bên nợ phải trả (CASA) so với bên tài sản (prepayment) [[src-lubinska-alm-optimisation#^lubinska-u06-10]].
- **Nguyên lý độ trễ vận hành (Operational Latency Principle)**: Mô hình chỉ ra hồ sơ cấu trúc mục tiêu lý tưởng (*target profile*), nhưng quá trình tái định hình bảng cân đối (*reshaping balance sheet*) đòi hỏi thời gian thực thi chiến lược và không thể hoàn thành qua đêm (*cannot be done overnight*) [[src-lubinska-alm-optimisation#^lubinska-u06-7]].

### 3. Kết Quả Thực Nghiệm: Ngân Hàng 2 (Quy Mô Lớn USD 549 Tỷ) & Tối Ưu Hóa Phía Tài Sản
- **Cấu trúc tài sản ban đầu**: RSA đạt USD 549 tỷ, gồm Tài sản bán lẻ $19.85\%$, Khách hàng doanh nghiệp $32.42\%$, Thị trường tài chính $36.79\%$ (cho vay liên ngân hàng 6 tháng, NBFI 4–9 tháng) và Đệm tài sản thanh khoản (LAB) $10.92\%$ [[src-lubinska-alm-optimisation#^lubinska-u06-11]] [[src-lubinska-alm-optimisation#^lubinska-u08-6]]. Tổng thu nhập lãi ban đầu đạt USD 6.30 tỷ / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u08-6]].
- **Chỉ số rủi ro ban đầu**: $\text{AD ratio} = 80\%$, $\text{MTFR}_{\text{contractual}} = 60\%$, $\text{MTFR}_{\text{behavioural}} = 176\%$, $\text{SH\_2M} = 134\%$, $\Delta\text{NII}_{+200\text{bps}} = 38\%$, $\text{CAR} = 12.4\%$ [[src-lubinska-alm-optimisation#^lubinska-u08-7]]. Đáng chú ý, 100% nợ phải trả có kỳ hạn bình quân dưới 1 năm, tạo ra rủi ro mô hình tiềm ẩn rất lớn từ các giả định tiền gửi không kỳ hạn [[src-lubinska-alm-optimisation#^lubinska-u06-12]].
- **Cơ Chế Tinh Gọn Đệm Thanh Khoản & Triệt Tiêu Âm Lợi Suất (Buffer Right-Sizing / Negative Carry Elimination)**:
  - Ở trạng thái ban đầu, Ngân hàng 2 nắm giữ đệm LAB quá lớn ($10.92\%$), đẩy chỉ số sinh tồn 2 tháng SH_2M lên tới $134\%$ (vượt xa hạn mức nội bộ $100\%$). Do LAB sinh lời rất thấp (chỉ đem lại USD 0.1113 tỷ), lượng thanh khoản dư thừa này tạo ra chi phí cơ hội lợi suất (*negative carry*) nghiêm trọng [[src-lubinska-alm-optimisation#^lubinska-u07-8]] [[src-lubinska-alm-optimisation#^lubinska-u08-6]].
  - Thuật toán KKT tự động tinh gọn tỷ trọng LAB từ $10.92\%$ xuống đúng mức tối thiểu **$4.66\%$** để SH_2M chạm đúng hạn mức $100\%$ (ràng buộc tích cực - active constraint) [[src-lubinska-alm-optimisation#^lubinska-u08-8]] [[src-lubinska-alm-optimisation#^lubinska-u08-10]].
  - Lượng vốn thanh khoản giải phóng được tái phân bổ sang tài sản bán lẻ sinh lời cao (từ $19.85\%$ lên **$26.76\%$**) và tài sản thị trường tài chính (từ $36.79\%$ lên **$43.19\%$**) [[src-lubinska-alm-optimisation#^lubinska-u08-8]].
- **Hiệu quả kinh tế vượt trội qua các kịch bản sốc lãi suất**:
  - **Kịch bản Cơ sở (Base Scenario)**: Thu nhập lãi tăng từ USD 6.30 tỷ lên **USD 6.588 tỷ**, mang lại thặng dư kinh tế **USD 0.2849 tỷ** (USD 284.9 triệu / 6 tháng), đồng thời $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $38\%$ xuống **$30.37\%$** [[src-lubinska-alm-optimisation#^lubinska-u08-9]] [[src-lubinska-alm-optimisation#^lubinska-u08-10]].
  - **Kịch bản Khủng hoảng Dầu mỏ (Oil Supply Crisis - lãi suất tăng)**: Thu nhập lãi tăng từ USD 6.945 tỷ lên **USD 7.29 tỷ**, tạo thặng dư kinh tế kỷ lục **USD 0.3452 tỷ** (USD 345.2 triệu / 6 tháng), $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $35\%$ xuống **$27.68\%$**, $\text{SH\_2M} = 100\%$ [[src-lubinska-alm-optimisation#^lubinska-u08-11]] [[src-lubinska-alm-optimisation#^lubinska-u08-12]].
  - **Kịch bản Động đất (Earthquake - sốc lãi suất giảm)**: Thu nhập lãi tăng từ USD 5.86 tỷ lên **USD 6.1365 tỷ**, tạo thặng dư kinh tế **USD 0.2730 tỷ** (USD 273.0 triệu / 6 tháng), $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $39.5\%$ xuống **$31.5\%$**, $\text{SH\_2M} = 100\%$ [[src-lubinska-alm-optimisation#^lubinska-u08-13]] [[src-lubinska-alm-optimisation#^lubinska-u08-14]].
  - **Kịch bản Kỳ vọng Lạm phát (Inflation Expectation)**: Thu nhập lãi tăng từ USD 7.645 tỷ lên **USD 8.0287 tỷ**, thặng dư kinh tế đạt **USD 0.3829 tỷ** / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u09-1]], $\text{SH\_2M} = 100\%$ và $\Delta\text{NII}_{+200\text{bps}}$ nén về **$24.64\%$** [[src-lubinska-alm-optimisation#^lubinska-u09-2]].
  - **Kịch bản Hạ 1 bậc tín nhiệm (Downgrade by One Notch) — Tái cơ cấu tài sản cực đoan**: Khi bị hạ bậc tín nhiệm, mô hình đẩy tỷ trọng bán lẻ vọt lên **$52.14\%$** (từ 19.85%) và cắt giảm tài sản doanh nghiệp về gần như triệt để **$0.00011\%$** (từ 32.42%) [[src-lubinska-alm-optimisation#^lubinska-u09-3]]; thu nhập lãi tăng thêm **USD 0.3929 tỷ** / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u09-4]] và CAR tăng vọt lên **$14.56\%$** để phòng thủ vốn [[src-lubinska-alm-optimisation#^lubinska-u09-5]].
  - **Kịch bản Tích hợp CPR và Thay đổi mô hình tiền gửi**: Thu nhập lãi tăng thêm **USD 0.2849 tỷ** / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u09-6]] [[src-lubinska-alm-optimisation#^lubinska-u09-7]], duy trì SH_2M 100% và $\Delta\text{NII}_{+200\text{bps}}$ ở mức $24.31\% - 30.37\%$ [[src-lubinska-alm-optimisation#^lubinska-u09-8]].
  - **Kịch bản Thay đổi tỷ trọng tài sản cố định — Thặng dư kỷ lục toàn chu kỳ**: Nắm giữ ban đầu LAB lên tới $25.13\%$ khiến SH_2M vọt lên $214\%$ và thu nhập chỉ đạt USD 5.334 tỷ [[src-lubinska-alm-optimisation#^lubinska-u09-9]]. Việc cắt giảm LAB về $4.66\%$ và tái phân bổ sang tài sản sinh lời cao mang lại thặng dư kinh tế kỷ lục toàn bộ công trình: **USD 1.255 tỷ / 6 tháng** (hơn USD 2.5 tỷ quy năm) [[src-lubinska-alm-optimisation#^lubinska-u06-13]] [[src-lubinska-alm-optimisation#^lubinska-u09-10]] [[src-lubinska-alm-optimisation#^lubinska-u09-11]].
- **Hiệu ứng quy mô và giảm chấn đa dạng hóa (Bank Size Diversification Effect)**: Khác với ngân hàng nhỏ, kịch bản thay đổi giả định mô hình tiền gửi không nằm trong nhóm tác động lớn nhất tại Ngân hàng 2. Ngân hàng quốc tế quy mô lớn phản ứng chậm hơn trước thay đổi giả định mô hình; cấu trúc tài sản và nguồn vốn đa dạng hóa cao giúp làm suy giảm và hấp thụ (*subdued*) tác động của các giả định hành vi đơn lẻ [[src-lubinska-alm-optimisation#^lubinska-u06-14]].

### 4. Kết Quả Thực Nghiệm: Ngân Hàng 2 (USD 549 Tỷ) — Tối Ưu Hóa Phía Nguồn Vốn
- **Cấu trúc nguồn vốn ban đầu tại $t_0$**:
  - Gồm CASA bán lẻ $28.3\%$, CASA giao dịch Treasury/TB $27.8\%$, Trái phiếu cao cấp (Senior debt) $11.4\%$, Tiền gửi kỳ hạn doanh nghiệp $20.5\%$, Tiền gửi cấu trúc $4.2\%$, Giấy tờ có giá ngắn hạn (CP/CD) $7.8\%$ [[src-lubinska-alm-optimisation#^lubinska-u09-12]].
  - Tổng chi phí vốn ban đầu: **USD 2.8493 tỷ / 6 tháng** [[src-lubinska-alm-optimisation#^lubinska-u09-13]].
  - Chỉ số rủi ro ban đầu: $\text{AD ratio} = 80.2\%$, $\text{MTFR}_{\text{contractual}} = 60\%$, $\text{MTFR}_{\text{behavioural}} = 176\%$, $\text{SH\_2M} = 133\%$, $\Delta\text{NII}_{+200\text{bps}} = 65\%$.
- **Cấu trúc nguồn vốn mục tiêu sau tối ưu hóa**:
  - *Tối đa hóa tiền gửi bán lẻ giá rẻ*: Tỷ trọng Retail CASA tăng vọt từ $28.3\%$ lên **$51.16\%$**, tận dụng tối đa lợi thế nguồn vốn chi phí cực thấp ($c_A = \text{USD } 0.0125\text{bn}$) [[src-lubinska-alm-optimisation#^lubinska-u09-14]].
  - *Cắt giảm tiền gửi giao dịch biến động*: TB CASA giảm mạnh từ $27.8\%$ xuống **$10\%$** để kiểm soát rủi ro thanh khoản rút vốn nhanh [[src-lubinska-alm-optimisation#^lubinska-u09-14]].
  - *Cắt giảm nguồn vốn bán buôn chi phí cao*: Senior debt giảm từ $11.4\%$ xuống **$3.8\%$**; CP/CD giảm từ $7.8\%$ xuống **$2\%$** [[src-lubinska-alm-optimisation#^lubinska-u09-14]]. Tiền gửi kỳ hạn doanh nghiệp tăng lên **$30\%$**.
- **Hiệu quả kinh tế và kiểm soát rủi ro nguồn vốn**:
  - Tổng chi phí vốn giảm từ USD 2.8493 tỷ xuống **USD 2.1967 tỷ / 6 tháng**.
  - Mức cắt giảm chi phí vốn đạt **USD 0.6526 tỷ** (USD 652.6 triệu / 6 tháng, tương đương thặng dư hơn **USD 1.3 tỷ / năm**) [[src-lubinska-alm-optimisation#^lubinska-u09-15]].
  - Tỷ lệ cho vay trên tiền gửi (AD ratio) giảm lành mạnh từ $80.2\%$ xuống **$72\%$**, SH_2M đạt **$156\%$**, và độ nhạy lãi suất $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $65\%$ xuống **$54\%$**.
- **Phân tích độ nhạy nguồn vốn qua các kịch bản sốc thị trường**:
  - **Kịch bản Lạm phát (Inflation Expectation)**: Chi phí vốn ban đầu USD 3.3356 tỷ [[src-lubinska-alm-optimisation#^lubinska-u10-1]] giảm về USD 2.6928 tỷ [[src-lubinska-alm-optimisation#^lubinska-u10-2]], tiết kiệm **USD 0.6428 tỷ** / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u10-3]], $\Delta\text{NII}_{+200\text{bps}}$ nén về mức an toàn **$49\%$** [[src-lubinska-alm-optimisation#^lubinska-u10-4]].
  - **Kịch bản Khủng hoảng Dầu mỏ (Oil Supply Crisis)**: Chi phí vốn ban đầu USD 3.0597 tỷ [[src-lubinska-alm-optimisation#^lubinska-u10-5]] giảm về USD 2.4 tỷ, tiết kiệm **USD 0.6591 tỷ** / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u10-6]], $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $62\%$ xuống **$51.7\%$** [[src-lubinska-alm-optimisation#^lubinska-u10-7]].
  - **Kịch bản Động đất (Earthquake - lãi suất giảm)**: Chi phí vốn ban đầu USD 2.6525 tỷ [[src-lubinska-alm-optimisation#^lubinska-u10-8]], tiết kiệm **USD 0.6496 tỷ** / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u10-9]], $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $64\%$ xuống **$53\%$**.
  - **Kịch bản Đặc tính hóa tiền gửi và CPR**: Chi phí vốn giảm về USD 2.1967 tỷ và USD 2.1795 tỷ, tiết kiệm **USD 0.6526 tỷ** và **USD 0.6698 tỷ** [[src-lubinska-alm-optimisation#^lubinska-u10-10]] [[src-lubinska-alm-optimisation#^lubinska-u10-11]] [[src-lubinska-alm-optimisation#^lubinska-u10-12]] [[src-lubinska-alm-optimisation#^lubinska-u10-13]].
  - **Kịch bản Hạ 1 bậc tín nhiệm (Downgrade by One Notch) — Tiết kiệm chi phí vốn đạt đỉnh**: Chi phí vốn ban đầu tăng vọt lên USD 2.9893 tỷ [[src-lubinska-alm-optimisation#^lubinska-u10-14]] do spread nợ bán buôn nới rộng. Mô hình KKT kéo chi phí vốn xuống USD 2.2439 tỷ [[src-lubinska-alm-optimisation#^lubinska-u10-15]], mang lại mức tiết kiệm chi phí vốn cao nhất toàn chu kỳ: **USD 0.7455 tỷ** / 6 tháng (tương đương **USD 1.49 tỷ quy năm**) [[src-lubinska-alm-optimisation#^lubinska-u10-16]], đồng thời khống chế $\Delta\text{NII}_{+200\text{bps}}$ ở mức $54.26\%$ [[src-lubinska-alm-optimisation#^lubinska-u10-17]].
  - **Kịch bản Thay đổi tỷ trọng tài sản cố định**: Đối mặt với rủi ro lãi suất ban đầu $\Delta\text{NII}_{+200\text{bps}} = 129\%$, mô hình đẩy CASA lên **$54.9\%$** và cắt giảm nợ cao cấp senior debt gần như triệt để về **$0.00011\%$** [[src-lubinska-alm-optimisation#^lubinska-u10-18]]. Tổng chi phí vốn giảm về **USD 1.982 tỷ** [[src-lubinska-alm-optimisation#^lubinska-u11-1]], mang lại mức cắt giảm chi phí vốn lên tới **USD 0.8666 tỷ** / 6 tháng (tương đương **USD 1.733 tỷ quy năm**) [[src-lubinska-alm-optimisation#^lubinska-u11-2]]. Chỉ số rủi ro mục tiêu đạt AD ratio 50%, MTFR hành vi 216%, SH_2M vọt lên 247% và $\Delta\text{NII}_{+200\text{bps}} = 121\%$ [[src-lubinska-alm-optimisation#^lubinska-u11-3]].
  - **Kịch bản Thay đổi tỷ trọng tài sản thả nổi**: Chi phí vốn ban đầu là USD 2.8493 tỷ [[src-lubinska-alm-optimisation#^lubinska-u11-4]]. Sau tối ưu hóa, Retail CASA tăng lên **$53.23\%$**, tiền gửi kỳ hạn doanh nghiệp đạt $30\%$, và Senior debt giảm mạnh về **$1.77\%$** [[src-lubinska-alm-optimisation#^lubinska-u11-5]]. Tổng chi phí vốn giảm về **USD 2.08 tỷ** [[src-lubinska-alm-optimisation#^lubinska-u11-6]], tạo thặng dư chi phí vốn **USD 0.6526 tỷ** / 6 tháng [[src-lubinska-alm-optimisation#^lubinska-u11-7]], đồng thời đưa AD ratio về 63.38%, MTFR hành vi 193%, SH_2M đạt 192% và $\Delta\text{NII}_{+200\text{bps}}$ duy trì ở mức $66\%$ [[src-lubinska-alm-optimisation#^lubinska-u11-8]].

### 2. Trình bày của Choudhry (Ch5, đồng tác giả Lubinska)
- Vai trò ALM đã chuyển từ cơ chế phản ứng, tập trung immunisation sổ ngân hàng, sang bảo đảm ngân hàng có lãi và giữ [[net-interest-margin|NIM]] [[src-choudhry-principles-banking#^choudhry-opt-1]].
- Ví dụ có mục tiêu tối thiểu hoá tổng chi phí vốn bằng cách chọn tỷ trọng các nguồn vốn. Bài toán chịu hạn mức nội bộ và quy định về thanh khoản, funding và rủi ro lãi suất [[src-choudhry-principles-banking#^choudhry-opt-2]].
- Chọn phương pháp theo dạng hàm:

  | Dạng hàm mục tiêu và ràng buộc | Phương pháp | Nguồn |
  |---|---|---|
  | Tuyến tính | Linear programming (LPP), thuật toán simplex (Matlab hoặc Excel Solver) | [[src-choudhry-principles-banking#^choudhry-opt-3]] |
  | Phi tuyến | Lagrange multiplier | [[src-choudhry-principles-banking#^choudhry-opt-3]] |
  | Phi tuyến, nhiều biến, ràng buộc bất đẳng thức | Interior-point dựa trên Lagrange multiplier (Matlab `fmincon`) | [[src-choudhry-principles-banking#^choudhry-opt-4]] |

- Phần lớn ràng buộc là bất đẳng thức. Ví dụ Survival Days yêu cầu HQLA đủ bù dòng ra ròng trong stress tối thiểu (ví dụ) 90 ngày [[src-choudhry-principles-banking#^choudhry-opt-4]].
- Với ChoudWest Bank (giả định), cấu trúc funding mục tiêu tiết kiệm 0,6 tỷ USD mỗi năm [[src-choudhry-principles-banking#^choudhry-opt-5]].
- Bảng cân đối mục tiêu có lợi từ quản lý tích hợp thanh khoản và rủi ro lãi suất. Choudhry đối lập cách này với quản lý silo thanh khoản và IRRBB, mà nguồn gọi là cách phổ biến nhất. Kết quả là chỉ số IRRBB và thanh khoản được giữ ở mức mong muốn, "không quá cao, không quá thấp" [[src-choudhry-principles-banking#^choudhry-opt-6]].

*Diễn giải:* Choudhry ghi tiết kiệm 0,6 tỷ USD "mỗi năm" cho ChoudWest Bank. Lubinska ghi thặng dư chi phí vốn 0,6526 tỷ USD cho 6 tháng ở Ngân hàng 2 (mục 1 ở trên). Hai con số gần nhau và cùng tác giả phương pháp, nhưng nguồn không nói đây là cùng một bài toán. Chưa đủ căn cứ để mở callout conflict; xem Câu hỏi mở ở mục Hạn chế.

---

## Hạn chế & validation

1. **Độ nhạy đối với giả định tham số hành vi**: Nghiệm tối ưu rất nhạy cảm với tỷ lệ phân tách CASA core/non-core và tốc độ trả nợ trước hạn CPR; nếu hành vi khách hàng thay đổi đột ngột (như rút tiền hàng loạt trong kỷ nguyên số), cơ cấu tối ưu có thể bị sai lệch.
2. **Khả năng không tồn tại nghiệm duy nhất**: Trong bài toán quy hoạch phi tuyến đa ràng buộc, nghiệm tối ưu có thể không tồn tại hoặc tồn tại nhiều cực trị địa phương (local optima); cần kiểm tra điều kiện chính quy (*regularity conditions*) của ràng buộc [[src-lubinska-alm-optimisation#^lubinska-u04-13]].
3. **Giả định thị trường hấp thụ hoàn hảo**: Mô hình ngầm định ngân hàng có thể mở rộng hoặc thu hẹp tỷ trọng sản phẩm theo ý muốn mà không làm thay đổi mặt bằng lãi suất thương mại của thị trường.
4. **Quản trị rủi ro mô hình và Nguyên lý Tinh gọn**: Theo Beata Lubinska (2020), việc gia tăng độ phức tạp không cần thiết sẽ làm tăng rủi ro mô hình và rủi ro bị cơ quan giám sát xử phạt Trụ cột 2 [[src-lubinska-alm-optimisation#^lubinska-u05-12]]; mô hình phải tuân thủ nguyên lý tinh gọn và chịu sự phản biện hiệu quả (*Effective Challenge*) qua 4 trụ cột kiểm định độc lập (Outcome, Assumptions, Methodology, Data feeding) [[src-lubinska-alm-optimisation#^lubinska-u05-15]] (xem [[model-risk-management]]).

5. **Câu hỏi mở**: ví dụ ChoudWest (Choudhry, 0,6 tỷ USD/năm) và Ngân hàng 2 (Lubinska, 0,6526 tỷ USD/6 tháng) có phải cùng một bài toán không? Cần đối chiếu file companion website Chapter 5 [cần nguồn].

---

## Xem Thêm
- [[model-risk-management]]
- [[repricing-balance-sheet]]
- [[ftp-pricing-methodology]]
- [[net-interest-income-sensitivity]]
- [[economic-value-of-equity]]
- [[src-lubinska-alm-optimisation]]
