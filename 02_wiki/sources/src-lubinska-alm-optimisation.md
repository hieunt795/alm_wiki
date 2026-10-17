---
title: "Asset Liability Management Optimisation — Beata Lubinska"
aliases: [src-lubinska-alm-optimisation, Lubinska ALM Optimisation, Asset Liability Management Optimisation]
type: source
source_id: src-lubinska-alm-optimisation
domains: [alm, product]
status: active
maturity: draft
tier: T4
doc_status: final
issuer: Wiley
published: 2020-04-20
raw: 01_sources/alm book/A - Asset liability optimization.md
units_done: [u03, u04, u05, u06, u07, u08, u09, u10, u11]
updated: 2026-10-17
---

## Thông tin nguồn
- Tác giả: Beata Lubinska (Chuyên gia quốc tế về ALM và FTP).
- Sách chuyên khảo: *Asset Liability Management Optimisation: A Practitioner's Guide to Balance Sheet Management and Remodelling* (Wiley Finance, 2020).
- Tier T4 (Tài liệu chuyên khảo quốc tế chuẩn mực cao nhất về thực chiến tối ưu hóa bảng cân đối và định giá điều chuyển vốn FTP).
- Raw: `01_sources/alm book/A - Asset liability optimization.md` (5.055 dòng).
- Units covered:
  - `u03`: Chapter 2 — The Role of Funds Transfer Pricing in Banks, Pricing of Products in the Banking Book, Target Operating Model, Incentive Premium Scheme, and Behaviouralisation (lines 958–1376).
  - `u04`: Chapter 2/3/4 — Contingent Liquidity & CASA Profiling, Customer Behaviour in Banking Book, Mortgage Prepayment (Statistical vs Financial Prepayment, Burnout Effect), NMD Volatility Models, and Inequality-Constrained Optimisation (KKT Conditions & Interior-Point Method) (lines 1377–1806).
  - `u05`: Chapter 4 — Definition of the Initial Banking Book Profile (Geographical Preferences), Building Objective and Constraint Functions (Survival Horizon, Structural Liquidity, A/D Ratio, IRRBB 4% Limit, CAR 10.5%, Funding Concentration 80%, Non-Negativity Condition), and Model Risk Management (MRM: Parsimony, OCC/Fed SR 11-7, 3 Sources of Risk, Effective Challenge & 4 Validation Pillars) (lines 1807–2246).
  - `u06`: Chapter 4/5 — Definition of the Sensitivity Parameters for the Optimisation Model, What-if Scenarios, Empirical Case Studies: Small Bank 1 (EUR 3.4bn) vs Large UK Bank 2 (USD 549bn) (lines 2247–2680).
  - `u07`: Chapter 5 — Conclusions, Dual Return-Risk Improvement, Initial Balance Sheet Structure as Destiny Driver, and Numerical Proof Data for Bank 1 (Asset & Funding Sides) (lines 2681–3093).
  - `u08`: Chapter 5 — Changes in the Initial Proportions of the Asset Base, Funding Sensitivity Scenarios for Bank 1 (Asset Base Changes, One-Notch Downgrade, CPR Inclusion), and Bank 2 Asset-Side Optimisation across Base & Interest Rate Risk Scenarios (Oil Supply Crisis, Earthquake, Inflation Expectation) (lines 3094–3567).
  - `u09`: Chapter 5 — Bank 2 Asset-Side Remaining Scenarios (Inflation Expectation, Downgrade, CPR, Deposit Characterisation, Fixed-Rate Asset Proportions) and Bank 2 Liabilities-Side Base Scenario (lines 3568–3971).
  - `u10`: Chapter 5 — Bank 2 Liabilities-Side Sensitivity Scenarios (Inflation Expectation, Oil Supply Crisis, Earthquake, Deposit Characterisation, CPR, One-Notch Downgrade, Fixed-Rate Asset Proportions) (lines 3972–4417).
  - `u11`: Chapter 5 — Bank 2 Liabilities-Side Final Sensitivity Scenarios (Fixed-Rate Asset Proportions, Floating-Rate Asset Proportions), Comprehensive Synthesis & Bibliography (lines 4418–5055).

## Tóm tắt Nội dung Nguồn

### 1. Vai trò Chiến lược của Hệ thống FTP trong Tối ưu hóa Bảng cân đối
Beata Lubinska xác định FTP là tổng thể các chính sách và phương pháp luận mà ngân hàng áp dụng để tính phí hoặc ghi nhận lợi ích thanh khoản tiêu thụ hoặc đóng góp. Trong bối cảnh nguồn lực khan hiếm và các tỷ lệ Basel III (LCR, NSFR) áp đặt ngưỡng sàn cấu trúc, quản trị bảng cân đối chủ động qua FTP là ưu tiên sống còn để tối ưu hóa vốn và nguồn tài trợ.

FTP vận hành dựa trên cơ chế MMFTP (Matched Maturity Funds Transfer Pricing), trong đó ALM đóng vai trò là "ngân hàng bên trong một ngân hàng" (a bank within a bank):
- ALM cấp vốn cho Asset Centre và thu phí FTP; đồng thời "mua" vốn từ Liability Centre và trả lãi FTP.
- Toàn bộ rủi ro không khớp kỳ hạn lãi suất (IRRBB) và thanh khoản được chuyển giao về ALM quản trị tập trung.
- ALM hưởng chênh lệch spread giữa lãi suất FTP thu từ tài sản và trả cho nợ, đồng thời quản lý danh mục đệm tài sản thanh khoản (Liquid Asset Buffer - LAB).

### 2. Định Giá Đúng Chi Phí Kinh Tế (True and Fair Value) và Cơ Chế Định Hướng Động Lực (Incentive Scheme)
Lubinska nhấn mạnh nguyên tắc bất biến: **Mọi ưu đãi (incentives) hoặc trợ cấp (subsidies) điều hành bảng cân đối phải minh bạch tuyệt đối và được đặt lên trên nền tảng của một bức tranh chi phí thanh khoản kinh tế thực tế và công bằng ("true and fair view")**.

Nếu thiếu sự minh bạch và kỷ luật kỹ trị, hệ thống FTP sẽ trở thành công cụ phá hủy giá trị của ngân hàng:
- **Nếu chi phí vốn bị đánh giá thấp (underestimated)**: Đơn vị kinh doanh cung cấp các khoản vay giá rẻ cho khách hàng và tăng trưởng quy mô tài trợ ảo tưởng rằng mình đang sinh lời, trong khi thực tế gây thâm hụt thanh khoản và ăn mòn vốn của ngân hàng.
- **Nếu chi phí vốn bị đánh giá cao (overestimated)**: Đơn vị kinh doanh buộc phải đòi hỏi mức lãi suất khách hàng cao hơn mức cần thiết, đánh mất khách hàng tốt và làm suy giảm khả năng cạnh tranh của ngân hàng.

### 3. Khung Đánh Giá Thực Tiễn của Cơ Quan Giám Sát PRA và Bài Học Về Quản Trị
Báo cáo rà soát toàn diện hệ thống ngân hàng Anh của Cơ quan Quản lý Thận trọng (Prudential Regulation Authority - PRA, Cadamagnani et al. 2015) chỉ ra lỗi nghiêm trọng phổ biến: **Các ngân hàng không bóc tách các điều chỉnh quản trị (management overlays) khỏi đường cong chi phí vốn cơ sở**. Việc dùng hai đường cong chi phí vốn ngầm khác nhau để vừa kích thích cho vay vừa kích thích huy động đã bóp méo động lực kinh doanh, che giấu hiệu quả kinh tế thực sự của sản phẩm trước và sau điều chỉnh. Mọi quyết định chiến lược phải dựa trên bản chất kinh tế thực sự của hoạt động kinh doanh (true economics of business).

### 4. Hành vi Khách hàng và Rủi ro Trả nợ Trước hạn (Prepayment) (u04)
Lubinska bóc tách rủi ro trả nợ trước hạn thành hai cấu phần:
- *Statistical (Structural) Prepayments*: Phi duy lý kinh tế, xuất phát từ các biến cố xã hội/nhân khẩu học của khách hàng (ly hôn, thừa kế, tăng lương, chuyển chỗ ở). Tỷ lệ này có mức sàn thống kê tối thiểu, được mô hình hóa từ dữ liệu lịch sử theo niên độ giải ngân (vintage cohorts).
- *Financial Prepayments*: Duy lý kinh tế, gắn liền trực tiếp với mức chênh lệch lãi suất thị trường (interest rate spread), kỳ hạn còn lại của khoản vay và hiệu ứng trơ lãi suất (*burnout phenomenon*). Các mô hình tham số tuyến tính truyền thống thường thất bại khi dự báo tính lồi âm phi tuyến của prepayment. Nếu ngân hàng không tính toán hành vi này trong chiến lược hedge, ngân hàng sẽ rơi vào trạng thái overhedging (thừa swap payer) và gây tổn thất PV01.

### 5. Mô hình Hóa CASA và Tối ưu hóa Bảng cân đối bằng Thuật toán Điểm trong (u04)
- *Mô hình hóa CASA / NMDs*: Phân tách số dư thành phần lõi (core) và phi lõi (non-core) theo 2 phương pháp: Mô hình tăng trưởng hàm mũ (*Exponential fit*) hạ đường xu hướng bằng $3.1\sigma$ (độ tin cậy 99.9%, tương đương 1 tháng rớt đáy trong 83 năm) và Mô hình biến động tháng (*Monthly Volatility 95th percentile* quy năm bằng $\sqrt{12}$).
- *Tối ưu hóa Bảng cân đối ALM*: Bài toán tối ưu hóa sổ ngân hàng là bài toán phi tuyến chịu các ràng buộc bất đẳng thức (giới hạn biến động NII, tỷ lệ thanh khoản ngắn hạn và cấu trúc). Bài toán được giải bằng điều kiện Karush-Kuhn-Tucker (KKT) và thuật toán điểm trong (*Interior-point algorithm / logarithmic barrier method* trong MATLAB `fmincon`). Thiết lập hai hàm mục tiêu kép: tối đa hóa thu nhập tài sản (Max Asset Income) và tối thiểu hóa chi phí vốn (Min Funding Cost) trên giả định bảng cân đối không đổi (*constant balance sheet / like-for-like*).

### 6. Hồ sơ Ban đầu của Sổ Ngân hàng và Đặc thù theo Khu vực Địa lý (u05)
- *Điểm khởi đầu $t_0$*: Bước đầu tiên trong quy trình tối ưu hóa ALM là nhận diện cấu trúc ban đầu của bảng cân đối và các giả định hành vi về thanh khoản (tỷ lệ tái tục tiền gửi có kỳ hạn, độ biến động CASA, độ nhạy lãi suất, lịch khấu hao dòng tiền và tỷ lệ trả nợ trước hạn CPR).
- *Khác biệt cấu trúc theo khu vực*:
  - **Ngân hàng tại Ý**: Ưa chuộng tài sản lãi suất thả nổi neo theo Euribor (tần suất định giá lại 1M, 3M, 6M); nguồn vốn chủ yếu dựa vào tài khoản thanh toán giao dịch (transactional current accounts) của khách hàng bán lẻ và doanh nghiệp.
  - **Ngân hàng tại Anh**: Ưa chuộng sản phẩm lãi suất điều hành (administered rate mortgages) có mức độ tương quan trên 80% với lãi suất cơ bản của Bank of England; sản phẩm thả nổi neo theo GBP LIBOR 3M; nguồn vốn chủ yếu từ CASA bán lẻ và tiền gửi kỳ hạn bán lẻ; nguồn vốn bán buôn ngắn hạn chủ yếu dùng để tài trợ cho đệm thanh khoản (LAB) và ký quỹ tài sản bảo đảm.
  - **Ngân hàng tại Mỹ**: Có xu hướng và sở thích nắm giữ tài sản lãi suất cố định dài hạn.
  - Xu thế chuẩn hóa toàn cầu theo Basel III và EBA (IRRBB, LCR, NSFR) thúc đẩy sự hội tụ trong kỹ thuật mô hình hóa hành vi và quản trị rủi ro.

### 7. Thiết lập Hệ thống Hàm Mục tiêu và Ràng buộc Tối ưu hóa ALM (u05)
- *Hàm mục tiêu kép*:
  - **Tối đa hóa Thu nhập Tài sản**: $\max \sum_{j} x_j r_j A$ (với $x_j$ là tỷ trọng danh mục tài sản $j$, $r_j$ là lợi suất hàng năm gộp gồm lãi suất cơ sở, phần bù thanh khoản FTP và biên thương mại tín dụng, $A$ là quy mô tổng tài sản).
  - **Tối thiểu hóa Chi phí Nguồn vốn**: $\min \sum_{j} w_j c_j$ (với $w_j$ là tỷ trọng nguồn vốn $j$, $c_j$ là chi phí huy động bình quân năm).
  - *Điều kiện không âm (Non-negativity condition)*: $x_j > 0, w_j > 0$ bắt buộc duy trì mọi phân khúc sản phẩm hiện hữu nhằm bảo toàn mô hình kinh doanh và thương quyền của ngân hàng, không cho phép mô hình triệt tiêu một nhóm sản phẩm về 0.
- *Hệ thống 6 ràng buộc cốt lõi*:
  1. **Chân trời Sinh tồn (Survival Horizon - SH)**: $(\text{LAB} + \text{TI}) / \text{TO} \ge 100\%$ trong 30, 60, 90 ngày chịu căng thẳng; quy mô đệm LAB tối thiểu phải tương đương dòng tiền ra ròng xấu nhất.
  2. **Thanh khoản Cấu trúc (Structural Liquidity Limit)**: $(\text{TI}_{T > 1\text{Y}} + \text{Tier 1 Capital}) / \text{TO}_{T > 1\text{Y}} \ge 100\%$ nhằm giới hạn mức độ chuyển đổi kỳ hạn vượt quá 1 năm.
  3. **Tỷ lệ Tín dụng trên Tiền gửi (Advances-to-Deposits - A/D Ratio)**: $A / D \le 80\%$ bảo đảm ngân hàng được tài trợ chủ yếu từ tiền gửi khách hàng và hạn chế phụ thuộc bán buôn.
  4. **Giới hạn Tập trung Nguồn vốn (Funding Concentration Limit)**: Tỷ trọng của bất kỳ nguồn tài trợ đơn lẻ nào không được vượt quá $80\%$ tổng nguồn vốn ($w_j \le 80\%$).
  5. **Độ nhạy Thu nhập Lãi thuần (IRRBB NII Sensitivity Limit)**: $|\Delta\text{NII}| / \text{NII} \le 4\%$ dưới kịch bản sốc lãi suất tức thời $\pm 200$ bps (chuẩn ECB) trên constant balance sheet; tích hợp sàn 0% (Floor 0%) ngăn chặn lãi suất âm cho tiền gửi bán lẻ và các khoản vay có quyền chọn sàn tự động.
  6. **Tỷ lệ An toàn Vốn (Capital Adequacy Ratio - CAR)**: $\text{Capital} / \text{RWA} \ge 10.5\%$ (gồm vốn tối thiểu 8%, đệm bảo toàn vốn 2.5%, đệm chống chu kỳ lên tới 2.5% theo Basel III).

### 8. Quản trị Rủi ro Mô hình trong Tối ưu hóa Bảng cân đối (Model Risk Management - MRM) (u05)
- *Nguyên lý Tinh gọn (Parsimony Principle)*: Mô hình càng tinh gọn càng tốt. Sự tinh vi hoặc phức tạp hóa không cần thiết chỉ làm gia tăng rủi ro mô hình và gây khó khăn cho việc quản trị, hiệu chuẩn và kiểm định mô hình.
- *Định nghĩa Mô hình theo OCC/Fed SR 11-7*: Là thuật toán định lượng, hệ thống hoặc phương pháp tiếp cận áp dụng các lý thuyết thống kê, kinh tế, tài chính để xử lý dữ liệu đầu vào thành các ước lượng định lượng. Mô hình gồm 3 cấu phần: Dữ liệu đầu vào (Inputs), Phương pháp chuyển đổi (Transformation Method) và Cấu phần báo cáo thông tin kinh doanh (Reporting).
- *Ba nguồn rủi ro mô hình*: (1) Khiếm khuyết dữ liệu (thiếu chiều sâu lịch sử, sai số nạp liệu); (2) Bất định ước lượng và sai số mô hình (giả định khiếm khuyết, thiết kế sai); và (3) Sử dụng sai mục đích (Model misuse, dùng sai phạm vi hoặc không hiệu chuẩn định kỳ).
- *Nguyên tắc "Phản biện hiệu quả" (Effective Challenge)*: Phản biện độc lập, có năng lực chuyên môn và thâm niên thực chiến là trụ cột tối thượng của MRM. Khung kiểm định mô hình gồm 4 trụ cột: Kiểm định kết quả đầu ra (Outcome), Kiểm định tính phù hợp của các giả định (Assumptions), Kiểm định phương pháp luận (Methodology), và Kiểm định dữ liệu đầu vào (Data feeding), chịu sự giám sát độc lập của Kiểm toán nội bộ.

### 9. Tham số Độ nhạy và Các Kịch bản Phân tích "What-If" (u06)
- *Mục tiêu phân tích độ nhạy*: Áp dụng các kịch bản định trước lên cấu trúc nguồn vốn và tài sản để xác định mức độ tác động đến kết quả của mô hình tối ưu hóa, từ đó nhận diện những nhân tố trọng yếu đóng vai trò động lực chi phối cấu trúc sổ ngân hàng.
- *5 kịch bản phân tích*:
  1. **Kịch bản cơ sở (Base scenario)**: Dựa trên mặt bằng lãi suất hiện hành và cấu trúc ban đầu của sổ ngân hàng.
  2. **Kịch bản biến động lãi suất (Interest rate scenarios)**: Đánh giá tác động dịch chuyển đường cong lợi suất lên cấu trúc mục tiêu.
  3. **Kịch bản thay đổi mô hình đặc tính hóa tiền gửi (Deposit characterisation model)**: Biến động tỷ lệ tiền gửi lõi/phi lõi và độ nhạy lãi suất CASA (thay đổi hành vi người gửi tiền).
  4. **Kịch bản tích hợp tỷ lệ trả nợ trước hạn (Prepayment rate)**: Áp dụng tỷ lệ trả nợ trước hạn liên tục CPR 7% cho tài sản lãi suất cố định; việc đưa CPR vào mô hình tạo tác động kép lên cơ cấu IRRBB ($\Delta\text{NII}$) và thanh khoản do lượng tiền hoàn trả sớm cần phải tái đầu tư.
  5. **Kịch bản thay đổi cơ cấu tài sản ban đầu (Initial asset base)**: Thay đổi tỷ trọng giữa tài sản lãi suất thả nổi và cố định.

### 10. Kết quả Thực nghiệm Nghiên cứu Điển hình: Ngân hàng 1 (Quy mô nhỏ EUR 3.4 tỷ) (u06)
- *Cấu trúc ban đầu*: RSA đạt EUR 3.4 tỷ, phần lớn là cho vay doanh nghiệp lãi suất thả nổi neo theo Euribor 1M, trong khi nợ phải trả chủ yếu neo theo Euribor 3M và 6M (rủi ro cơ sở basis risk). CASA biến động cao: chỉ 35% được coi là ổn định, 65% biến động được phân bổ vào các dải kỳ hạn ngắn hạn (O/N đối với IRRBB và 1M đối với thanh khoản). Trước khi áp dụng mô hình, Ngân hàng 1 vi phạm tỷ lệ thanh khoản tích lũy ngắn hạn (<100%).
- *Gia tăng thu nhập*: Thu nhập bình quân gia quyền cải thiện trên mọi kịch bản, delta thặng dư trước và sau tối ưu dao động từ EUR 3.8 triệu đến EUR 7.63 triệu. Mức cải thiện cao nhất đạt được ở kịch bản thay đổi cơ cấu tài sản (EUR 7.63m), xác thực lợi ích của kỹ thuật tối ưu hóa định lượng đối với lợi nhuận ngân hàng.
- *Đánh đổi chi phí tuân thủ*: Dưới kịch bản kỳ vọng lạm phát, chi phí huy động vốn tăng nhẹ (từ EUR 34.37m lên 34.88m) do mô hình ràng buộc áp đặt cơ cấu nợ mới để đáp ứng yêu cầu thanh khoản ngắn hạn (short-term cumulative liquidity ratio).
- *Bất đối xứng độ nhạy hành vi*: Mô hình có độ nhạy rất cao trước các giả định hành vi, trong đó độ nhạy với giả định hành vi bên nợ phải trả (CASA) cao hơn đáng kể so với bên tài sản (prepayment).
- *Nguyên lý độ trễ vận hành (Operational Latency Principle)*: Mô hình chỉ ra hồ sơ cấu trúc mục tiêu lý tưởng (*target profile*), nhưng quá trình tái định hình bảng cân đối (*reshaping balance sheet*) đòi hỏi thời gian thực thi và không thể hoàn thành qua đêm (*cannot be done overnight*).

### 11. Kết quả Thực nghiệm Nghiên cứu Điển hình: Ngân hàng 2 (Quy mô lớn USD 549 tỷ) và Hiệu ứng Quy mô (u06)
- *Cấu trúc ban đầu*: RSA đạt USD 549 tỷ (109 tỷ bán lẻ administered rate chuẩn Anh, 178 tỷ doanh nghiệp, 202 tỷ thị trường tài chính, 60 tỷ HQLA).
- *Rủi ro mô hình tiềm ẩn (Embedded Model Risk)*: Trên cơ sở hợp đồng, **100% nợ phải trả có kỳ hạn bình quân dưới 1 năm**. Cấu trúc này đưa rủi ro mô hình trọng yếu vào sổ ngân hàng, phụ thuộc hoàn toàn vào các giả định và kết quả của mô hình đặc tính hóa tiền gửi không kỳ hạn (CASA kỳ hạn hợp đồng 1 ngày nhưng được mô hình hóa dài hạn).
- *Lợi ích kinh tế đột biến*: Mức thặng dư cao nhất đạt được dưới kịch bản tái cơ cấu tài sản lãi suất cố định, mang lại lợi ích kinh tế lên tới **USD 1.25 tỷ**.
- *Hiệu ứng Quy mô và Giảm chấn Đa dạng hóa (Bank Size Diversification Effect)*: Khác với Ngân hàng 1, ở Ngân hàng 2 kịch bản thay đổi giả định mô hình tiền gửi không nằm trong nhóm tác động lớn nhất. Ngân hàng quốc tế quy mô lớn phản ứng chậm hơn trước thay đổi giả định mô hình; cơ cấu tài sản và nguồn vốn đa dạng hóa cao giúp làm suy giảm và hấp thụ (*subdued*) tác động của các giả định hành vi đơn lẻ.

### 12. Kết luận Chiến lược về Tối ưu hóa Bảng cân đối và Động lực Cơ cấu Khởi điểm (u07)
- *Bản chất bài toán quy hoạch*: Tối ưu hóa sổ ngân hàng được thiết lập dưới dạng quy hoạch phi tuyến có ràng buộc (*constrained non-linear optimisation*) với cả ràng buộc đẳng thức và bất đẳng thức, giải tách biệt cho hai bài toán: tối đa hóa thu nhập tài sản và tối thiểu hóa chi phí nguồn vốn bằng thuật toán `fmincon` trong MATLAB.
- *Lợi ích kinh tế phổ quát tỷ lệ thuận với quy mô*: Kết quả tính toán cung cấp bằng chứng rõ ràng rằng thặng dư kinh tế đạt được trên **mọi kịch bản phân tích** (cả kịch bản cơ sở going-concern và các kịch bản kiểm định độ nhạy). Biên độ thặng dư tỷ lệ thuận với quy mô tổng tài sản sổ ngân hàng.
- *Cơ cấu khởi điểm là động lực quyết định "vận mệnh" thặng dư (Initial Structure as Destiny Driver)*: Phân tích mức độ giảm chi phí vốn chỉ ra rằng **nhân tố nhạy cảm nhất chính là cấu trúc ban đầu của sổ ngân hàng** ($t_0$). Cơ cấu tài sản ban đầu quyết định mức độ thặng dư đạt được; mô hình vận hành hiệu quả hơn đối với một số cơ cấu bảng cân đối nhất định so với các cơ cấu khác. Tác giả kết luận: một số ngân hàng dường như "được định sẵn" đạt khả năng sinh lời vượt trội hơn từ mô hình tối ưu hóa ngay từ đầu thông qua việc thiết lập cấu trúc khởi điểm của họ.
- *Tác động dịch chuyển đường cong lợi suất*: Khi đường cong lợi suất dịch chuyển đi lên (kịch bản Lạm phát, Khủng hoảng nguồn cung dầu), mức độ cắt giảm chi phí vốn đạt được cao hơn so với kịch bản cơ sở hoặc khi đường cong dịch chuyển đi xuống (kịch bản Động đất).
- *Cơ chế khôi phục tuân thủ các hạn mức bị vi phạm*: Ở ngân hàng nhỏ (Ngân hàng 1), tại thời điểm khởi điểm $t_0$, tỷ lệ thanh khoản tích lũy ngắn hạn bị vi phạm nghiêm trọng (chỉ đạt 59.7% so với hạn mức 100%). Việc áp dụng mô hình tối ưu hóa tự động điều phối cơ cấu sổ ngân hàng về trạng thái tuân thủ tuyệt đối hạn mức (100%), đồng thời vẫn mang lại thặng dư kinh tế. Trong trường hợp duy nhất không có thặng dư lợi nhuận (kịch bản lạm phát bên nợ), mức tăng nhẹ chi phí được hiểu là chi phí kinh tế tối thiểu bắt buộc phải trả để khôi phục sự tuân thủ các hạn mức an toàn nội bộ.
- *Cải thiện đồng thời lợi nhuận và quản trị rủi ro*: Mô hình tối ưu hóa đồng thời giảm thiểu độ nhạy rủi ro lãi suất ($\Delta\text{NII}$ giảm sâu từ 80.5% về 4%), đáp ứng các chỉ số thanh khoản, và ngăn chặn tình trạng giữ thừa thanh khoản dưới dạng đệm LAB không hiệu quả hoặc tích trữ nguồn vốn dài hạn quá mức làm triệt tiêu tiềm năng lợi nhuận từ hoạt động chuyển đổi kỳ hạn lành mạnh (*healthy maturity transformation*).

### 13. Minh chứng Định lượng Chi tiết tại Ngân hàng 1 (Tài sản & Nguồn vốn) (u07)
- *Danh mục Tài sản (Asset Side)*:
  - **Trạng thái ban đầu $t_0$**: Tài sản thả nổi $w = 78.37\%$, Tài sản cố định $w = 20.31\%$, Đệm thanh khoản LAB $w = 1.31\%$. Tổng thu nhập lãi = EUR 0.075 tỷ / 6 tháng. Chỉ số rủi ro: Thanh khoản ngắn hạn tích lũy = $59.7\%$ (vi phạm), Tỷ lệ cấu trúc = $91.9\%$, $\Delta\text{NII}_{+200\text{bps}} = 80.5\%$, $\text{CAR} = 26.2\%$.
  - **Sau tối ưu hóa (Kịch bản cơ sở)**: Tài sản thả nổi giảm xuống $30.58\%$, Tài sản cố định tăng lên $66.02\%$, Đệm LAB tăng lên $3.39\%$. Tổng thu nhập lãi đạt EUR 0.0819 tỷ / 6 tháng, tạo ra mức **tăng thặng dư thu nhập EUR 0.0069 tỷ** (EUR 6.9 triệu) trong 6 tháng.
  - **Chỉ số rủi ro sau tối ưu**: Thanh khoản ngắn hạn đạt chuẩn tuyệt đối $100\%$, Tỷ lệ cấu trúc đạt $93.9\%$, $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $80.5\%$ xuống ngưỡng an toàn **$4\%$**, $\text{CAR} = 22\%$.
  - **Dưới các kịch bản sốc lãi suất**: Khủng hoảng dầu mỏ tạo thặng dư thu nhập EUR 0.01049 tỷ; Kỳ vọng lạm phát tạo thặng dư EUR 0.0079 tỷ.
- *Danh mục Nguồn vốn (Funding Side)*:
  - **Trạng thái ban đầu $t_0$**: Tiền gửi thanh toán CASA DN $7.4\%$, Tiền gửi kỳ hạn DN $1.5\%$, Nguồn vốn bán buôn $70\%$, Trái phiếu phát hành $21\%$. Chi phí vốn = EUR 30.79 triệu / 6 tháng. Thanh khoản ngắn hạn = $59\%$ (vi phạm).
  - **Sau tối ưu hóa**: CASA giảm về $2.5\%$, Tiền gửi kỳ hạn tăng lên $7.67\%$, Nguồn vốn bán buôn tăng lên sát trần tập trung $79.99\%$, Trái phiếu giảm về $9.8\%$. Chi phí vốn giảm xuống EUR 30.49 triệu / 6 tháng, mang lại thặng dư kinh tế **EUR 0.2964 triệu / năm**, đồng thời khôi phục thanh khoản ngắn hạn lên $100\%$ và kéo giảm $\Delta\text{NII}$ từ $78\%$ xuống $70.2\%$.
  - **Thặng dư chi phí vốn dưới các kịch bản khác**: Khủng hoảng dầu mỏ đạt EUR 0.2812 triệu/năm; Rủi ro vỡ nợ HY/LBO đạt EUR 0.6677 triệu/năm; Thay đổi mô hình đặc tính hóa tiền gửi CASA mang lại thặng dư đột biến **EUR 1.1954 triệu / năm**.

### 14. Phân tích Độ nhạy Nguồn vốn Ngân hàng 1: Đổi Cơ cấu Tài sản, Hạ bậc Tín nhiệm và Phí phạt CPR (u08)
- **Đổi cơ cấu danh mục tài sản**: Khi tỷ trọng tài sản phân bổ lệch mạnh (Asset 1 chiếm 83.69%, Asset 2 chiếm 15%, Asset 3 chỉ còn 1.31%), cấu trúc vốn ban đầu vi phạm nghiêm trọng hạn mức thanh khoản ngắn hạn (tỷ lệ chỉ đạt $60.89\% < 100\%$) với chi phí vốn EUR 29.67 triệu / 6 tháng. Mô hình tối ưu hóa KKT điều chỉnh lại tỷ trọng vốn (tăng CASA từ 7.4% lên 13.43% hoặc 2.61%, tăng tiền gửi kỳ hạn lên 9.57% hoặc 7.61%, nâng wholesale funding lên 77.01% - 79.99%, giảm mạnh trái phiếu phát hành), đưa chi phí vốn giảm về EUR 24.7 triệu hoặc EUR 29.1 triệu / 6 tháng. Thặng dư kinh tế đạt từ **EUR 0.5663 triệu** đến **EUR 4.9560 triệu**, đồng thời khôi phục trọn vẹn tỷ lệ thanh khoản ngắn hạn về $100\%$.
- **Hạ 1 bậc tín nhiệm (Downgrade by One Notch)**: Xếp hạng tín nhiệm suy giảm đẩy chi phí huy động vốn vọt lên EUR 35.84 triệu / 6 tháng và tỷ lệ thanh khoản ngắn hạn rơi xuống mức vi phạm $59.8\%$. Mô hình KKT tái cơ cấu nguồn vốn (nâng wholesale funding lên 79.99%, giảm trái phiếu phát hành xuống 9.8%), hạ chi phí vốn xuống EUR 35.2 triệu, mang lại thặng dư kinh tế **EUR 0.6388 triệu / năm**, đưa thanh khoản ngắn hạn về $100\%$ và nén $\Delta\text{NII}_{+200\text{bps}}$ từ $72.18\%$ xuống mức an toàn vượt bậc **$6.8\%$**.
- **Tính đến tỷ lệ trả nợ trước hạn CPR của tài sản lãi suất cố định**: Dưới kịch bản gán tham số CPR, tỷ lệ thanh khoản ngắn hạn ban đầu bị vi phạm ở mức $62\%$. Sau khi chạy mô hình tối ưu hóa, chi phí vốn giảm từ EUR 29.67 triệu xuống EUR 28.44 triệu / 6 tháng, mang lại thặng dư kinh tế **EUR 1.2244 triệu / năm**, đồng thời khôi phục thanh khoản ngắn hạn lên $100\%$ và giảm $\Delta\text{NII}_{+200\text{bps}}$ từ $77\%$ xuống $67.68\%$.

### 15. Thực Nghiệm Tối Ưu Hóa Phía Tài Sản tại Ngân Hàng 2 (USD 549bn) và Cơ Chế Tinh Gọn Đệm Thanh Khoản (u08)
- **Hồ sơ danh mục tài sản ban đầu của Ngân hàng 2**:
  - Quy mô tài sản khổng lồ: USD 549 tỷ. Cơ cấu ban đầu gồm Tài sản bán lẻ $19.85\%$, Khách hàng doanh nghiệp $32.42\%$, Thị trường tài chính $36.79\%$ (cho vay liên ngân hàng 6 tháng, NBFI 4–9 tháng) và Đệm tài sản thanh khoản (Liquid Asset Buffer - LAB) $10.92\%$.
  - Thu nhập lãi ban đầu: USD 6.30 tỷ / 6 tháng.
  - Các chỉ số rủi ro ban đầu: $\text{AD ratio} = 80\%$, $\text{MTFR}_{\text{contractual}} = 60\%$, $\text{MTFR}_{\text{behavioural}} = 176\%$, $\text{SH\_2M} = 134\%$, $\Delta\text{NII}_{+200\text{bps}} = 38\%$, $\text{CAR} = 12.4\%$.
- **Cơ chế Tinh gọn Đệm Thanh khoản (Liquidity Buffer Right-Sizing / Negative Carry Elimination)**:
  - Điểm phát hiện mấu chốt: Ngân hàng 2 nắm giữ đệm tài sản thanh khoản LAB quá mức cần thiết ($10.92\%$), dẫn đến chỉ số sinh tồn 2 tháng SH_2M đạt tới $134\%$, vượt xa hạn mức nội bộ $100\%$. Khoản đệm dư thừa này tạo ra chi phí cơ hội lợi suất (negative carry) rất lớn vì lãi suất của LAB chỉ đem lại USD 0.1113 tỷ.
  - Mô hình KKT tự động nhận diện khoản thặng dư kém hiệu quả này và cắt giảm tỷ trọng LAB từ $10.92\%$ xuống đúng mức cận biên **$4.66\%$** để SH_2M đạt đúng $100\%$ (Active Boundary).
  - Nguồn vốn thanh khoản giải phóng được tái phân bổ vào các tài sản sinh lời cao: Tài sản bán lẻ tăng từ $19.85\%$ lên **$26.76\%$** và Tài sản thị trường tài chính tăng từ $36.79\%$ lên **$43.19\%$**.
- **Hiệu quả kinh tế và kiểm soát rủi ro qua các kịch bản sốc lãi suất**:
  - **Kịch bản Cơ sở (Base Scenario)**: Thu nhập lãi tăng từ USD 6.30 tỷ lên **USD 6.588 tỷ**, mang lại thặng dư kinh tế **USD 0.2849 tỷ** (USD 284.9 triệu / 6 tháng), đồng thời $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $38\%$ xuống **$30.37\%$**.
  - **Kịch bản Khủng hoảng Dầu mỏ (Oil Supply Crisis - sốc lãi suất tăng)**: Thu nhập lãi tăng từ USD 6.945 tỷ lên **USD 7.29 tỷ**, tạo thặng dư kinh tế kỷ lục **USD 0.3452 tỷ** (USD 345.2 triệu / 6 tháng), $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $35\%$ xuống **$27.68\%$**, $\text{SH\_2M} = 100\%$.
  - **Kịch bản Động đất (Earthquake - sốc lãi suất giảm)**: Thu nhập lãi tăng từ USD 5.86 tỷ lên **USD 6.1365 tỷ**, tạo thặng dư kinh tế **USD 0.2730 tỷ** (USD 273.0 triệu / 6 tháng), $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $39.5\%$ xuống **$31.5\%$**, $\text{SH\_2M} = 100\%$.
  - **Kịch bản Kỳ vọng Lạm phát (Inflation Expectation - đường cong dịch chuyển lên)**: Thu nhập lãi ban đầu đạt USD 7.645 tỷ với SH_2M ban đầu 134% và $\Delta\text{NII}_{+200\text{bps}} = 31.06\%$.

### 16. Phân tích Sâu Sắc Phía Tài Sản Ngân Hàng 2 Qua Các Kịch Bản Khắc Nghiệt (u09)
- **Kịch bản Kỳ vọng Lạm phát (Inflation Expectation - đường cong dịch chuyển lên)**: Mô hình tối ưu hóa nâng thu nhập lãi từ USD 7.645 tỷ lên **USD 8.0287 tỷ**, tạo thặng dư kinh tế **USD 0.3829 tỷ** (USD 382.9 triệu / 6 tháng), đưa SH_2M về 100% và nén $\Delta\text{NII}_{+200\text{bps}}$ từ 31.06% xuống **24.64%**.
- **Kịch bản Hạ 1 bậc tín nhiệm (Downgrade by One Notch) — Tái phân bổ cơ cấu cực đoan**:
  - Khi ngân hàng bị hạ bậc tín nhiệm, mô hình KKT đưa ra phản ứng cơ cấu ngoạn mục: Tỷ trọng tài sản bán lẻ vọt lên **52.14%** (từ 19.85%), trong khi tài sản khách hàng doanh nghiệp bị cắt giảm gần như triệt để về **0.00011%** (từ 32.42%) do chi phí biên và spread doanh nghiệp giãn rộng.
  - Thu nhập lãi tăng từ USD 6.44 tỷ lên **USD 6.8331 tỷ**, mang lại thặng dư **USD 0.3929 tỷ** / 6 tháng; CAR tăng vọt lên **14.56%** (từ 12.4%), phản ánh sự tích lũy vốn thận trọng cao độ khi bị hạ bậc.
- **Kịch bản Tích hợp CPR và Thay đổi mô hình tiền gửi**: Thu nhập lãi đều tăng từ USD 6.304 tỷ lên **USD 6.5889 tỷ**, tạo thặng dư **USD 0.2849 tỷ** / 6 tháng, SH_2M đạt 100% và $\Delta\text{NII}_{+200\text{bps}}$ được kiểm soát nghiêm ngặt ở mức 24.31%–30.37%.
- **Kịch bản Thay đổi tỷ trọng tài sản cố định — Thặng dư kinh tế kỷ lục toàn bộ công trình**:
  - Ở trạng thái ban đầu, ngân hàng nắm giữ tỷ trọng LAB lên tới **25.13%**, khiến SH_2M vọt lên **214%** và thu nhập lãi chỉ đạt USD 5.334 tỷ.
  - Mô hình tối ưu hóa cắt giảm LAB từ 25.13% về **4.66%**, đưa SH_2M về đúng 100%, tái phân bổ nguồn vốn sang tài sản sinh lời cao, nâng thu nhập lên **USD 6.588 tỷ**. Thặng dư kinh tế đạt mức kỷ lục toàn bộ cuốn sách: **USD 1.255 tỷ / 6 tháng** (hơn **USD 2.5 tỷ quy năm**)!

### 17. Thực Nghiệm Tối Ưu Hóa Phía Nguồn Vốn tại Ngân Hàng 2 (USD 549bn) — Kịch Bản Cơ Sở (u09)
- **Hồ sơ nguồn vốn ban đầu tại $t_0$**:
  - Cơ cấu: Retail CASA $28.3\%$, CASA giao dịch Treasury/TB $27.8\%$, Trái phiếu cao cấp (Senior debt) $11.4\%$, Tiền gửi kỳ hạn doanh nghiệp $20.5\%$, Tiền gửi cấu trúc $4.2\%$, Giấy tờ có giá ngắn hạn (CP/CD) $7.8\%$.
  - Tổng chi phí vốn ban đầu: **USD 2.8493 tỷ / 6 tháng**.
  - Chỉ số rủi ro ban đầu: $\text{AD ratio} = 80.2\%$, $\text{MTFR}_{\text{contractual}} = 60\%$, $\text{MTFR}_{\text{behavioural}} = 176\%$, $\text{SH\_2M} = 133\%$, $\Delta\text{NII}_{+200\text{bps}} = 65\%$.
- **Cơ cấu nguồn vốn mục tiêu sau tối ưu hóa**:
  - *Tối đa hóa tiền gửi bán lẻ giá rẻ*: Tỷ trọng Retail CASA tăng vọt từ $28.3\%$ lên **$51.16\%$**, tận dụng tối đa lợi thế nguồn vốn chi phí cực thấp ($c_A = \text{USD } 0.0125\text{bn}$).
  - *Cắt giảm tiền gửi giao dịch biến động*: TB CASA giảm mạnh từ $27.8\%$ xuống **$10\%$** để kiểm soát rủi ro thanh khoản rút vốn nhanh.
  - *Cắt giảm nguồn vốn bán buôn chi phí cao*: Senior debt giảm từ $11.4\%$ xuống **$3.8\%$**; CP/CD giảm từ $7.8\%$ xuống **$2\%$**. Tiền gửi kỳ hạn doanh nghiệp tăng lên **$30\%$**.
- **Hiệu quả kinh tế và kiểm soát rủi ro nguồn vốn**:
  - Tổng chi phí vốn giảm từ USD 2.8493 tỷ xuống **USD 2.1967 tỷ / 6 tháng**.
  - Mức cắt giảm chi phí vốn đạt **USD 0.6526 tỷ** (USD 652.6 triệu / 6 tháng, tương đương thặng dư hơn **USD 1.3 tỷ / năm**).
  - Tỷ lệ cho vay trên tiền gửi (AD ratio) giảm lành mạnh từ $80.2\%$ xuống **$72\%$**, SH_2M đạt **$156\%$**, và độ nhạy lãi suất $\Delta\text{NII}_{+200\text{bps}}$ giảm từ $65\%$ xuống **$54\%$**.

### 18. Phân Tích Độ Nhạy Toàn Diện Phía Nguồn Vốn Ngân Hàng 2 Qua Các Kịch Bản Lãi Suất và Thị Trường (u10)
- **Kịch bản Kỳ vọng Lạm phát (Inflation Expectation - lãi suất tăng)**:
  - Chi phí vốn ban đầu: USD 3.3356 tỷ / 6 tháng. Sau tối ưu hóa, chi phí vốn giảm về USD 2.6928 tỷ, mang lại mức tiết kiệm **USD 0.6428 tỷ** (USD 642.8 triệu / 6 tháng).
  - Chỉ số rủi ro mục tiêu: AD ratio đạt $72\%$, SH_2M đạt $156\%$, $\Delta\text{NII}_{+200\text{bps}}$ giảm từ mức ban đầu xuống **$49\%$**.
- **Kịch bản Khủng hoảng Nguồn cung Dầu mỏ (Oil Supply Crisis - sốc lãi suất tăng đột ngột)**:
  - Chi phí vốn ban đầu: USD 3.0597 tỷ / 6 tháng với $\Delta\text{NII}_{+200\text{bps}} = 62\%$.
  - Sau tối ưu hóa, chi phí vốn giảm về USD 2.4 tỷ, mang lại mức tiết kiệm **USD 0.6591 tỷ** (USD 659.1 triệu / 6 tháng); $\Delta\text{NII}_{+200\text{bps}}$ giảm về **$51.7\%$**, SH_2M đạt $156\%$.
- **Kịch bản Động đất (Earthquake - sốc lãi suất giảm)**:
  - Chi phí vốn ban đầu: USD 2.6525 tỷ / 6 tháng với $\Delta\text{NII}_{+200\text{bps}} = 64\%$.
  - Mô hình tối ưu hóa giúp cắt giảm chi phí vốn thêm **USD 0.6496 tỷ** (USD 649.6 triệu / 6 tháng); $\Delta\text{NII}_{+200\text{bps}}$ giảm về **$53\%$**, SH_2M đạt $156\%$.
- **Kịch bản Thay đổi Đặc tính hóa Tiền gửi CASA và Tích hợp Phí phạt CPR**:
  - Dưới các kịch bản hành vi tiền gửi và trả nợ sớm, mô hình đều mang lại mức cắt giảm chi phí vốn ổn định từ **USD 0.6526 tỷ** đến **USD 0.6698 tỷ** / 6 tháng; $\Delta\text{NII}_{+200\text{bps}}$ duy trì an toàn trong dải $54.6\% - 61.85\%$.
- **Kịch bản Hạ 1 bậc tín nhiệm (Downgrade by One Notch) — Thặng dư Tiết kiệm Chi phí Vốn Cao Nhất**:
  - Khi ngân hàng bị hạ bậc tín nhiệm, chi phí vốn ban đầu bị đội lên USD 2.9893 tỷ / 6 tháng do các nhà đầu tư bán buôn yêu cầu spread cao hơn.
  - Mô hình KKT tái cấu trúc danh mục nợ (nâng CASA bán lẻ lên $51.16\%$, cắt giảm mạnh nợ bán buôn đắt đỏ), kéo chi phí vốn xuống USD 2.2439 tỷ. Mức cắt giảm chi phí vốn đạt đỉnh cao nhất trong tất cả các kịch bản: **USD 0.7455 tỷ** (USD 745.5 triệu / 6 tháng, tương đương **USD 1.49 tỷ quy năm**), trong khi $\Delta\text{NII}_{+200\text{bps}}$ duy trì ở mức an toàn $54.26\%$.
- **Kịch bản Thay đổi Tỷ trọng Tài sản Cố định ban đầu**:
  - Cấu trúc ban đầu đối mặt với rủi ro lãi suất cực hạn với $\Delta\text{NII}_{+200\text{bps}} = 129\%$. Mô hình KKT đẩy tỷ trọng CASA bán lẻ lên mức cao nhất **$54.9\%$** và cắt giảm nợ cao cấp (Senior debt) gần như tuyệt đối xuống **$0.00011\%$** (từ $11.4\%$), bảo vệ ngân hàng trước nguy cơ tổn thương thu nhập nghiêm trọng.

### 19. Tối Ưu Hóa Nguồn Vốn Dưới Biến Động Cơ Cấu Tài Sản Cố Định / Thả Nổi và Đúc Kết Toàn Diện Cuốn Sách (u11)
- **Kịch bản Biến động Tỷ trọng Tài sản Cố định (Changes in the Initial Proportions of Fixed Rate Assets - Funding side)**:
  - Chi phí vốn ban đầu: USD 2.8493 tỷ / 6 tháng.
  - Sau tối ưu hóa: Tổng chi phí vốn giảm về **USD 1.982 tỷ / 6 tháng**. Mức giảm chi phí vốn lên tới **USD 0.8666 tỷ** (USD 866.6 triệu / 6 tháng, tương đương **USD 1.733 tỷ quy năm**)!
  - Hồ sơ rủi ro mục tiêu: $\text{AD ratio} = 50\%$, $\text{MTFR}_{\text{contractual}} = 39\%$, $\text{MTFR}_{\text{behavioural}} = 216\%$, tỷ lệ sống sót thanh khoản ngắn hạn $\text{SH\_2M} = 247\%$. Tuy nhiên, do tài sản cố định chiếm tỷ trọng áp đảo tạo khe hở nhạy cảm lãi suất cố hữu, độ nhạy $\Delta\text{NII}_{+200\text{bps}}$ duy trì ở mức cao **$121\%$**, minh chứng rằng khi không sử dụng công cụ hoán đổi lãi suất (IRS) để phòng hộ phái sinh, việc tái cấu trúc nợ đơn thuần không thể loại bỏ hoàn toàn rủi ro tái định giá của tài sản cố định dài hạn.
- **Kịch bản Biến động Tỷ trọng Tài sản Thả nổi (Changes in the Initial Proportions of Floating Rate Assets - Funding side)**:
  - Cấu trúc ban đầu: Chi phí vốn USD 2.8493 tỷ, $\text{AD ratio} = 72\%$, $\text{MTFR}_{\text{contractual}} = 66.74\%$, $\text{MTFR}_{\text{behavioural}} = 193\%$, $\text{SH\_2M} = 165\%$, $\Delta\text{NII}_{+200\text{bps}} = 75.48\%$.
  - Tái phân bổ nợ mục tiêu: Tăng mạnh Retail CASA từ $28.3\%$ lên **$53.23\%$**, nén TB CASA về **$10\%$**, giảm nợ cao cấp Senior debt từ $11.4\%$ xuống **$1.77\%$**, tiền gửi kỳ hạn doanh nghiệp tăng lên **$30\%$**, tiền gửi cấu trúc $3\%$ và CP/CD nén về **$2\%$**.
  - Kết quả: Chi phí vốn giảm xuống **USD 2.08 tỷ / 6 tháng**, tiết kiệm **USD 0.6526 tỷ** (USD 652.6 triệu / 6 tháng, tương đương thặng dư hơn **USD 1.3 tỷ quy năm**).
  - Hồ sơ rủi ro mục tiêu: $\text{AD ratio} = 63.38\%$, $\text{MTFR}_{\text{contractual}} = 35\%$, $\text{MTFR}_{\text{behavioural}} = 193\%$, $\text{SH\_2M} = 192\%$, $\Delta\text{NII}_{+200\text{bps}} = 66\%$.
- **Tổng kết Chiến lược Toàn diện Công trình Tối ưu hóa ALM của Beata Lubinska (Chương 1–5)**:
  1. *Quy luật Cải thiện Đồng thời Lợi nhuận và Rủi ro (Dual Return-Risk Improvement)*: Xuyên suốt cả Ngân hàng 1 (EUR 3.4 tỷ) và Ngân hàng 2 (USD 549 tỷ), qua 16 kịch bản sốc lãi suất, thanh khoản, hành vi và xếp hạng tín nhiệm, mô hình KKT / Interior-point chứng minh rằng: tối ưu hóa toán học không đánh đổi rủi ro lấy lợi nhuận mà đồng thời gia tăng thu nhập lãi (hoặc cắt giảm chi phí vốn từ vài trăm triệu đến hơn 1.25 tỷ USD) trong khi siết chặt và làm lành mạnh hóa toàn diện các chỉ số an toàn (AD ratio, MTFR, SH_2M, CAR, $\Delta\text{NII}$).
  2. *CASA Bán Lẻ là Trọng Tâm Sống Còn*: Trong mọi kịch bản tái cơ cấu nợ, mô hình luôn đẩy tỷ trọng CASA bán lẻ lên tối đa trong dải cho phép ($51\% - 55\%$) nhờ tính chất chi phí cực thấp và tính ổn định hành vi cao ($3.1\sigma$ decay). Ngược lại, nợ bán buôn ngắn hạn và tiền gửi giao dịch TB CASA biến động bị cắt giảm mạnh nhất.
  3. *Kỷ trị FTP và TOM*: FTP phải phản ánh đúng chi phí kinh tế biên gộp ("true and fair view"). Việc che giấu chi phí vốn hoặc gộp chung management overlays sẽ phá hủy tín hiệu thị trường nội bộ, dẫn tới các quyết định phân bổ sai lệch của các đơn vị kinh doanh.

## Key Claims & Verbatim Quotes

### Unit u03 — The Role of Funds Transfer Pricing in Banks & Target Operating Model

- Định nghĩa quy trình Funds Transfer Pricing (FTP) là tổng hợp các chính sách và phương pháp luận để tính phí hoặc ghi có lợi ích thanh khoản.
  > "The funds transfer pricing (FTP) process is the sum of polices and methodologies that banks apply to charge or credit products for the liquidity consumed or gathered during a bank's activity"
  > — Chapter 2, line 1175 ^lubinska-ftp-1

- Khung FTP được sử dụng như một công cụ tạo động lực hành vi nhằm đạt được các mục tiêu của ngân hàng và định giá công bằng chi phí lãi suất và thanh khoản.
  > "Therefore, the FTP framework is used as a tool to incentivise behaviour that helps to achieve a bank's goals and the fair pricing of interest rate and liquidity costs."
  > — Chapter 2, line 1177 ^lubinska-ftp-2

- Ngân hàng phải có một giá trị thực và công bằng (true and fair value) và hệ thống FTP phải gắn kết với các mục tiêu chiến lược thông qua việc định hướng hoặc trợ cấp cho các hoạt động phù hợp chiến lược tổng thể.
  > "Banks must have a true and fair value and the FTP scheme has to be aligned to their strategic objectives through incentivising or subsidising businesses and activities which are aligned with the overall strategy."
  > — Chapter 2, line 1179 ^lubinska-ftp-3

- Trong cơ chế MMFTP, ALM đóng vai trò là "ngân hàng bên trong một ngân hàng", cung cấp vốn cho tài sản và mua vốn từ nguồn nợ, gánh nhận toàn bộ rủi ro chênh lệch kỳ hạn lãi suất và thanh khoản.
  > "In this process, ALM (treasury) plays the role of 'a bank within a bank', which means it provides funds to the asset centre and charges the FTP rate for it. At the same time, it 'buys' funds from the liability centre and pays the FTP rate. As a result of this intermediation, ALM is left with all the mismatches from the interest rate risk and liquidity risk perspective and its main mandate consists of managing those mismatches."
  > — Chapter 2, line 1189 ^lubinska-ftp-4

- FTP định hình bảng cân đối thông qua cơ chế khuyến khích hoặc không khuyến khích; tuy nhiên sự thiếu minh bạch có thể phá hủy giá trị ngân hàng, do đó một mô hình vận hành mục tiêu chuẩn mực (TOM) là bắt buộc.
  > "If there is a need to gather more funds from, for example, the retail current accounts then ALM can potentially increase the FTP rate paid for this particular product. This additional mark up on the FTP rate will boost the product profitability and encourage the business line to increase its share in the total funding structure. Conversely, charging more for a certain asset class will act as a disincentive for the business unit, decreasing the product's share in the total asset base. This simple mechanism forms a strategic tool for a bank to get rid of unprofitable products and to retain only the profitability boosters. However, lack of transparency in the framework could turn to be value detrimental to the institution; therefore, a proper target operating model around FTP is an imperative."
  > — Chapter 2, line 1193 ^lubinska-ftp-5

- Mọi khoản ưu đãi và trợ cấp bắt buộc phải minh bạch tuyệt đối và được đặt lên trên nền tảng của một bức tranh chi phí thanh khoản kinh tế thực và công bằng ("true and fair view").
  > "Thus, any incentives and subsidies need to be made very transparent and come on top of a 'true and fair view' of the bank's liquidity costs."
  > — Chapter 2, line 1219 ^lubinska-ftp-6

- FTP là công cụ giúp phân tách thu nhập lãi thuần toàn hàng thành các đơn vị và tiểu đơn vị khởi tạo, phục vụ chu trình lập kế hoạch, giám sát và kiểm soát hiệu quả.
  > "In fact, FTP is the means by which a bank's overall net interest income can be split into originating units and subunits, thus enabling the bank's management to perform an effective planning, monitoring, and control cycle"
  > — Chapter 2, line 1221 ^lubinska-ftp-7

- Phương pháp luận FTP dựa trên phương cận biên gộp (gross marginal cost approach), phản ánh chi phí cơ hội để tài trợ một đơn vị tài sản mới trên thị trường.
  > "The FTP methodology is based on a gross marginal cost approach, which reflects the opportunity cost to fund one unit of new asset volume in the market; however, this approach should be adjusted in order to reflect the funding characteristics of the balance sheet."
  > — Chapter 2, line 1250 ^lubinska-ftp-8

- Quy tắc quản trị nghiêm ngặt khi ban hành gói ưu đãi (Incentive Premium - IP): chỉ là công cụ điều tiết ngắn hạn tạm thời, không được bù đắp giá trị thanh khoản pháp định và không được thay thế vai trò xác lập chi phí vốn cận biên của đường cong.
  > "On some occasions a bank's senior management may decide to introduce an incentive premium (IP) on specific assets or liabilities with an offsetting charge on specific assets or liabilities to achieve precisely defined, short-term balance sheet objectives. There are very precise rules that need to be followed when introducing the IP scheme. In particular, it should be recognised/charged out to businesses, it should only represent a temporary tool for steering, it should not seek to compensate for regulatory liquidity value, and it should not replace the role of the curve in establishing marginal funding costs."
  > — Chapter 2, line 1266 ^lubinska-ftp-9

- FTP phải phân bổ đúng chi phí hoặc lợi ích thanh khoản và vốn cho các mảng kinh doanh và sản phẩm để hỗ trợ ra quyết định kinh doanh phù hợp và quản trị rủi ro thanh khoản nhất quán.
  > "FTP should attribute liquidity and funding cost or benefits to the businesses and products to enable appropriate business decisions and to allow ALM to manage the liquidity and funding risks in an effective and consistent manner."
  > — Chapter 2, line 1280 ^lubinska-ftp-10

- Chi phí duy trì đệm dự phòng thanh khoản (hoặc LAB) phải được phân bổ chính xác cho nguồn gốc gây ra rủi ro thanh khoản.
  > "Cost of maintaining a liquidity reserve (or LAB) should be allocated to the source of liquidity risk."
  > — Chapter 2, line 1282 ^lubinska-ftp-11

- Một trong những mục tiêu chính của mô hình vận hành mục tiêu (Target Operating Model - TOM) đối với FTP là bảo đảm tính minh bạch; rủi ro lãi suất và thanh khoản phải được tách thành các danh mục riêng biệt trong Treasury/ALM.
  > "Oneofthe main objectives of the target operating model for the FTP is to ensure that transparency is the main principle in the FTP framework. To achieve this transparency, interest rate risk and liquidity risk need to be separated into different portfolios within Treasury/ALM."
  > — Chapter 2, line 1297 ^lubinska-ftp-12

- Kết quả rà soát của cơ quan giám sát PRA (Cadamagnani et al. 2015): Cảnh báo việc các ngân hàng không tách bạch các điều chỉnh quản trị (management overlays) khỏi đường cong huy động vốn, áp dụng đường cong lệch làm méo mó động lực kinh doanh và che giấu hiệu quả kinh tế thực sự.
  > "A Prudential Regulation Authority (PRA) cross-firm review of the FTP practices at major UK banks revealed important issues in banks' internal transfer pricing policies and framework. One of the major issues, underlined in the PRA's review, was that banks were not separating the management overlays from their funding curve. Some banks were found to be applying different cost of funding curves to new loans and deposits to incentivise loan origination and deposit-gathering simultaneously. The PRA view is that this is a vulnerability in the FTP framework of the bank, as dampening practice skews business incentives and makes it less clear what the performance is for individual products before and after any management overlay. An important point was made that strategic decisions need to be made acknowledging the true economics of business, and not unwittingly as a result of the inappropriate internal pricing methodologies"
  > — Chapter 2, line 1303 ^lubinska-ftp-13

- Hậu quả của việc định giá sai chi phí vốn trong hệ thống FTP: Đánh giá thấp dẫn đến cho vay rẻ và tăng trưởng tài trợ ảo tưởng có lãi; đánh giá cao dẫn đến đòi hỏi lãi suất khách hàng quá cao làm mất cơ hội kinh doanh.
  > "Given that the internal FTP methodologies play a key part in profit allocation within a bank and influence business lines' activities, a robust FTP regime is a must. If funding costs are underestimated, business lines offer customers cheaper loans and increase funding volumes in the mistaken belief that they are profitable. If funding costs are overestimated, business lines may mistakenly require higher customer rates to be perceived as profitable."
  > — Chapter 2, line 1304 ^lubinska-ftp-14

### Unit u04 — Customer Behaviour, Prepayment, NMDs, and Optimisation Methodology

- Hồ sơ lãi suất của CASA luôn bao gồm hai phần: phần biến động được mô hình hóa tái định giá trên cơ sở qua đêm (O/N) theo chuẩn BCBS d368, và phần ổn định được coi là nhạy cảm lãi suất theo thị trường hoặc phần lõi phi nhạy cảm lãi suất đóng vai trò nguồn vốn dài hạn lãi suất 0%.
  > "CASA interest rate profiling is always composed of two parts, i.e. the volatile portion of the balance, which won't stay within the bank for the long term, thus it is modelled as a portion which reprices on the O/N basis (in line with the BCBS 368 requirements), and the stable portion. The stable portion is considered to be either risk sensitive, i.e. reprices in line with the market rate, or a core part, which is non-sensitive to the interest rate movements and therefore could be seen as a long-term funding with rate at 0%."
  > — Chapter 2, line 1383 ^lubinska-u04-1

- FTP behaviouralisation là phương pháp luận nhằm nắm bắt toàn bộ rủi ro lãi suất và chi phí/giá trị thanh khoản hành vi của sản phẩm; việc chuyển giao đúng rủi ro từ ALM sang đơn vị kinh doanh có ý nghĩa quyết định đến phân bổ lợi nhuận và định hướng hành vi kinh doanh.
  > "The FTP behaviouralisation is a methodology that attempts to capture the full (and behavioural) interest rate risk and liquidity cost/value of the product. The correct transference of interest rate risk and liquidity risk from ALM to business units is especially important in profit allocation within the bank, as it directly influences business line activities. If funding costs are underestimated, business lines offer customers cheaper loans and increase funding volumes in mistaken belief that they are profitable. If funding costs are overestimated, business lines may mistakenly require higher customer rates to be perceived as profitable (Lubinska 2017)."
  > — Chapter 2, line 1391 ^lubinska-u04-2

- Hồ sơ thanh khoản phải bao gồm chi phí thanh khoản dự phòng (contingent liquidity costs) phát sinh từ bất định và kịch bản căng thẳng; việc nắm giữ đệm thanh khoản bảo vệ trước dòng tiền ra bất ngờ có chi phí đắt đỏ nên chi phí dự phòng này phải được phân bổ ngược lại cho mảng kinh doanh.
  > "Additionally, the liquidity profiling should encompass the contingent liquidity costs, i.e. those which are driven by uncertainty and stress situation. Under stress, customers behaviour can change radically; therefore, banks needs to hold a liquidity buffer which protects them against unexpected cash outflows."
  > "However, as already mentioned, holding a liquidity buffer is expensive as the cost of funding them usually exceeds generated return. This contingent liquidity cost has to be allocated back to business."
  > — Chapter 2, lines 1393-1395 ^lubinska-u04-3

- Rủi ro khách hàng tất toán tài sản trước hạn (early redemption / prepayment), nếu không được tính đến trong chiến lược phòng ngừa rủi ro của ngân hàng, sẽ gây ra tình trạng phòng hộ quá mức (overhedging) do số lượng swap payer vượt quá dư nợ tài sản lãi suất cố định thực tế, làm ngân hàng chịu rủi ro lệch dải kỳ hạn và tác động tiêu cực đến chỉ số PV01.
  > "Early redemption of assets, if not accounted for in the hedging strategies of the bank, cause overhedging because the number of swap payers is higher than the actual amount of fixed rate assets. Consequently, the bank has to adjust hedging positions and, in the meantime, is left open to time bucket sensitivity and negative impact in terms of the PV01 metric."
  > — Chapter 3, line 1427 ^lubinska-u04-4

- Phân tích biến động số dư chia tiền gửi thành số dư lõi (core) - duy trì tại ngân hàng dưới hầu hết điều kiện kinh tế, và số dư phi lõi (non-core) - có xu hướng rút khỏi ngân hàng do yếu tố đặc thù hoặc biến động kinh tế vĩ mô.
  > "Balance volatility analysis splits the balances as core balances, which stay with the bank under almost all economic conditions, and non-core balances, which tend to leave the bank either idiosyncratically or with the movements of macroeconomic factors."
  > "The balance volatility model determines what level of balances will remain with the bank in the long term, given a level of confidence. As an output, the balance volatility model divides the balances into two portions: core balances which remain with the bank under almost all market conditions, and non-core balances which fluctuate over time due to market and idiosyncratic reasons and are typically characterised as short term."
  > — Chapter 3, lines 1483-1485 ^lubinska-u04-5

- Phương pháp hàm mũ (Exponential fit) xác định số dư lõi bằng cách hạ đường xu hướng hồi quy một khoảng bằng 3.1 lần độ lệch chuẩn ($3.1\sigma$), tương đương mức tin cậy 99.9%, nhằm hạ xác suất tổng số dư rơi xuống dưới mức lõi chỉ còn 0.1% thời gian (khoảng 1 tháng trong mỗi 83 năm).
  > "To ensure that the probability of core balances dropping below the actual balances is minimal, the fitted equation is lowered with some multiple of standard deviation (see Figure 3.1). Approximately 99.9% corresponds to a 3.1 standard deviation shift in balances for a normal distribution. The growth rate is decreased by n ∗ /u1D70E , or 3.1 times the standard deviation, to decrease the chance of the total balance level falling below the core level to 0.1% of the time, or approximately one month in every 83 years."
  > — Chapter 3, line 1511 ^lubinska-u04-6

- Phương pháp biến động tháng (Monthly Volatility) xác định phần phi lõi bằng cách lấy mức sụt giảm số dư tồi tệ nhất ở phân vị 95 (95th percentile worst decline over 1 month) và quy năm bằng cách nhân với căn bậc hai của 12 ($\sqrt{12}$); tỷ lệ lõi là phần bù so với 100%.
  > "The 95th percentile worst decline in balance is taken and represents the volume which the bank considers to flow out of the portfolio over 1 month at a 95% confidence level."
  > "The non-core portion is calculated by annualising the monthly volatility. This is done by multiplying MV by the square root of time (as MV is annualised then a 12-month time interval is used). The core % is the difference between 100% of the portfolio and the computed non-core %."
  > — Chapter 3, lines 1537-1539 ^lubinska-u04-7

- Trả nợ trước hạn bao gồm hai loại: Financial prepayments có tính chu kỳ và lý do duy lý kinh tế theo mặt bằng lãi suất; Structural prepayments mang tính phi duy lý kinh tế xuất phát từ các biến cố cá nhân của người vay và tạo ra tỷ lệ trả nợ trước hạn tối thiểu mang tính thống kê.
  > "There are two types of prepayments:"
  > "- ■ Financial prepayments - these prepayments are potentially cyclical and have rational reasons, such as interest rate levels or other macroeconomic conditions."
  > "- ■ Structural prepayments - these prepayments are partially irrational from an economic point of view as statistically there is always a minimum prepayment rate. The driver of structural prepayment is mainly related to the personal events occurring to mortgagors."
  > — Chapter 3, lines 1621-1624 ^lubinska-u04-8

- Structural prepayments chịu chi phối bởi các yếu tố xã hội học như ly hôn, thừa kế, tăng lương (thay đổi vị thế tài chính) hoặc chuyển dịch nơi cư trú, hoàn toàn không liên quan đến mặt bằng lãi suất trên thị trường.
  > "As already anticipated, statistical prepayments are driven by sociological reasons and are not related to the level of the interest rates in the market. For example, divorce, inheritance, salary increases (change of the financial status of the client), or geographic mobility affect the financial situation of the client and consequently his willingness to prepay the mortgage."
  > — Chapter 3, line 1630 ^lubinska-u04-9

- Ba biến số quan trọng nhất trong mô hình hóa tỷ lệ trả nợ trước hạn là: chênh lệch lãi suất (interest rate spread), kỳ hạn còn lại (residual maturity), và hiện tượng trơ lãi suất (burnout phenomenon) — đo lường mức độ sẵn sàng và ngưỡng kích hoạt phản ứng khác nhau giữa các nhóm khách hàng trước các đợt giảm lãi suất.
  > "Financial prepayments are strictly linked to the market rate level. It is rational behaviour fully explained by external factors which impact the mortgagors' decision. The relation between the market rate level and customer rates explains the greater part of these prepayments."
  > "There are three most important variables in modelling of the prepayment rate: interest rate spread, seniority/residual maturity, and burnout."
  > "The burnout phenomenon measures the customers' likelihood to react to the interest rate decrease. It turns out that there are different activating levels for the prepayment options among clients. The burnout variable tries to capture the difference in readiness of customers to prepay their mortgage."
  > — Chapter 3, lines 1650-1670 ^lubinska-u04-10

- Các mô hình tham số thông thường (parametric models) thường có năng lực dự báo ngoài mẫu kém do tính chất phi tuyến cao của hàm trả nợ trước hạn; các kỹ thuật phi tham số xử lý tốt hơn mối quan hệ phi tuyến và tương tác đa biến.
  > "It turns out that modelling prepayments on conventional parametric models often have bad out-of-sample predictive ability. A likely explanation is the highly non-linear nature of prepayment functions. Non-parametric techniques are much better at detecting non-linearity and multivariate interaction."
  > — Chapter 3, line 1679 ^lubinska-u04-11

- Tối ưu hóa sổ ngân hàng hầu như luôn liên quan đến các ràng buộc bất đẳng thức (như hạn mức biến động NII, các tỷ lệ thanh khoản ngắn hạn và trung dài hạn); các bài toán ràng buộc bất đẳng thức phi tuyến quy mô lớn này được giải bằng định lý Kuhn-Tucker và thuật toán điểm trong (Interior-point method / barrier method trong MATLAB toolbox `fmincon`).
  > "The optimisation exercise for the banking book of the bank involves almost always inequality constraints. For example, the limit related to the NII volatility is expressed as an inequality, indicating the range for the acceptable level of the NII volatility. The same point is valid for the liquidity ratios, both short term and medium long term. In such cases, where the constraints are expressed as inequalities, the optimisation problem can be solved applying the Kuhn-Tucker theorem."
  > "This section addresses the optimisation method known as the interior-point method which gets its name from the fact that the optimal solution is approached from the strict interior of the feasible region. This method is used in the MATLAB optimisation toolbox known as fmincon to find a minimum of a constrained nonlinear multivariable function. Interior-point (or barrier) methods have proved to be successful for non-linear optimisation and they are currently considered the most powerful algorithm for large-scale non-linear programming."
  > — Chapter 4, lines 1771-1773 ^lubinska-u04-12

- Điều kiện Karush-Kuhn-Tucker (KKT) là điều kiện cần bậc nhất cho nghiệm tối ưu trong quy hoạch phi tuyến có ràng buộc bất đẳng thức; bài toán tối ưu hóa ALM được thiết lập với 2 hàm mục tiêu riêng biệt: tối đa hóa thu nhập tài sản và tối thiểu hóa chi phí nguồn vốn dưới giả định bảng cân đối không đổi (constant balance sheet / like-for-like assumption).
  > "In order to find the solution to the optimisation problem it is necessary to satisfy the Karush-Kuhn-Tucker (KKT) optimality condition. KKT are first-order necessary conditions for a solution in non-linear programming to be optimal, provided that some regularity conditions are satisfied. Allowing inequality constraints, the KKT approach to non-linear programming generalises the method of Lagrange multipliers, which allows only equality constraints."
  > "The optimisation problem herein is defined through the construction of two separate optimisation functions, i.e. the maximisation of the assets income and minimisation of the funding costs of the bank subject to constraints. The analysis needs to be performed over a certain time horizon and predetermined maturity profile for the banking book items; for example, under a constant balance sheet scenario where there is a renewal of assets and liabilities falling under maturity/repricing with items with the same financial features ( like for like assumption)."
  > — Chapter 4, lines 1801-1805 ^lubinska-u04-13

### Unit u05 — Definition of the Initial Banking Book Profile, Constraint Functions & Model Risk Management

- Bước đầu tiên trong quy trình tối ưu hoá là xác định cấu trúc ban đầu của sổ ngân hàng đóng vai trò điểm khởi đầu tại thời điểm $t_0$, kết hợp với các giả định ban đầu về thanh khoản, tỷ lệ tái tục tiền gửi, độ biến động và độ nhạy lãi suất CASA, lịch khấu hao dòng tiền và tỷ lệ trả nợ trước hạn CPR.
  > "The first step in the optimisation process is to identify the initial structure of the banking book which will act as a 'starting point' at the time t 0 of the exercise. It defines the position, in terms of the asset and liability structure, which is given at the analysis date. In addition, certain assumptions related to the liquidity profile of the balance sheet items, in terms of the rollover of term deposits, volatility of current and savings accounts (CASA), and rate sensitivity, amortisation profile, and prepayment rate of assets have been defined as the initial conditions of the analysis and are built into the model."
  > — Chapter 4, line 1809 ^lubinska-u05-1

- Các ngân hàng thương mại tại Ý có thiên hướng ưu tiên tài sản lãi suất thả nổi neo theo Euribor (tần suất định giá lại 1M, 3M, 6M) và nguồn vốn phụ thuộc chủ yếu vào các tài khoản thanh toán giao dịch (transactional current accounts) của khách hàng bán lẻ và doanh nghiệp.
  > "commercial banks based in Italy have preferences towards floating rate assets. Personal and commercial loans products are usually indexed to an interbank market benchmark such as EURIBOR. The reset frequency differs between 1 M, 3 M, and 6 M. From the funding perspective, there is significant reliance on current accounts provided by retail and commercial clients and the banks are mostly funded by transactional current accounts."
  > — Chapter 4, line 1813 ^lubinska-u05-2

- Các ngân hàng tại Anh có thiên hướng ưu tiên các sản phẩm thế chấp lãi suất điều hành (administered rate mortgages) có độ tương quan trên 80% với lãi suất cơ bản của Bank of England; sản phẩm thả nổi neo theo GBP LIBOR 3M; nguồn vốn chủ yếu từ CASA bán lẻ và tiền gửi kỳ hạn; vốn bán buôn ngắn hạn dùng để tài trợ cho đệm thanh khoản LAB và ký quỹ tài sản bảo đảm.
  > "Banks based in the UK, however, tend towards administered rate products (mortgages) which show high correlation to the Bank of England base rate (more than 80%). Floating rate products are predominantly linked to GBP LIBOR 3 M. The retail banks are funded by retail current accounts and retail time deposits. The residual part of their funding structure consists of senior debt issuance. The short-term funding is mostly used for funding of LAB and collateral funding."
  > — Chapter 4, line 1815 ^lubinska-u05-3

- Rủi ro thanh khoản ngắn hạn được định lượng qua chỉ số Chân trời sinh tồn (Survival Horizon - SH) đo lường thời gian ngân hàng có thể sinh tồn trong điều kiện căng thẳng thanh khoản cực đoan nhưng hợp lý trước khi các biện pháp can thiệp quản trị được kích hoạt trên các khung thời gian 30, 60 hoặc 90 ngày.
  > "The short-term liquidity risk is quantified through the survival horizon (SH) metric that defines for how long, during an extreme but plausible liquidity stress, a bank can survive before management actions are deployed. The goal of this metric is to ensure that a financial institution would have sufficient time to react and make decisions in stress which mobilise further liquidity creating actions to offset a significant stress. The survival horizon analysis assesses the liquidity position under stress conditions lasting 30, 60, or even 90 days, constructed through the definition of different assumptions of inflows and outflows for items on the balance sheet."
  > — Chapter 4, line 1854 ^lubinska-u05-4

- Quy mô đệm tài sản thanh khoản (Liquid Asset Buffer - LAB) tối thiểu phải bằng tổng dòng tiền ra ròng chịu căng thẳng (stressed net outflows); kết quả xấu nhất của các kịch bản stress thanh khoản (nhu cầu HQLA cao nhất) là nhân tố quyết định quy mô đệm LAB của ngân hàng.
  > "The amount of liquidity buffer has to be at least equal to the net outflows calculated under stress scenarios. The worst result of the stress scenario (the highest requirement for the HQLA) is the driver of the liquidity buffer size which is held by a bank."
  > — Chapter 4, line 1854 ^lubinska-u05-5

- Rủi ro thanh khoản cấu trúc là nguy cơ tổn thất thực tế hoặc chi phí cơ hội do không thể theo đuổi chiến lược kinh doanh vì cơ cấu bảng cân đối dưới mức tối ưu; hạn mức cấu trúc (Structural Limit) khống chế mức độ chuyển đổi kỳ hạn và duy trì cấu trúc nguồn vốn ổn định vượt quá 1 năm.
  > "Structural liquidity risk is defined as the potential for actual or opportunity loss because the bank cannot pursue its desired business strategy or growth objectives due to suboptimal balance sheet composition. The structural limit shows the extent of the maturity transformation of a bank. It requires the maintenance of a stable funding profile in relation to the composition of the balance sheet and, consequently, the reduction of funding risk over a longer time."
  > — Chapter 4, line 1943 ^lubinska-u05-6

- Tỷ lệ Tín dụng trên Tiền gửi (Advances-to-Deposits - A/D Ratio) bảo đảm ngân hàng được tài trợ chủ yếu từ khách hàng và không phụ thuộc quá mức vào vốn bán buôn; thông lệ thị trường tốt nhất là thiết lập ngưỡng khống chế dưới 80%.
  > "The A/D ratio ensures that the bank remains largely client funded and does not become excessively reliant on wholesale funding. It is a simple metric but easily understandable, and provides a sense check for the structural integrity of the balance sheet. However, this metric does not differentiate for the quality or tenor of deposits nor the effect of the ongoing improvement initiatives and hence needs frequent re-evaluation."
  > — Chapter 4, line 1971 ^lubinska-u05-7

- Để đo lường mức độ biến động thu nhập kỳ vọng dưới các kịch bản sốc lãi suất, ngân hàng mô hình hóa thu nhập dưới 3 trạng thái bảng cân đối: Run-off balance sheet (không tái tục vị thế đáo hạn), Constant balance sheet (duy trì quy mô và cấu trúc qua tái tục like-for-like), và Dynamic balance sheet (tích hợp kỳ vọng kinh doanh tương lai).
  > "In order to be able to calculate changes in the expected earnings under different interest rate shocks and stress scenarios, an institution is expected to model earnings under three different states:"
  > "- a) Run-off balance sheet: existing assets and liabilities are not replaced as they mature, except to the extent necessary to fund the remaining balance sheet."
  > "- b) Constant balance sheet: total balance sheet size and shape maintained by assuming like for like replacement of assets and liabilities as they run off."
  > "- c) Dynamic balance sheet: incorporating future business expectations, adjusted for the relevant scenario in a consistent manner."
  > — Chapter 4, lines 2038-2040 ^lubinska-u05-8

- Khi đánh giá cú sốc lãi suất giảm -200 bps, sàn lãi suất 0% được áp dụng để ngăn ngừa lãi suất rơi vào vùng âm; điều này phản ánh quyền chọn sàn tự động (embedded floors) phổ biến trong hợp đồng vay thương mại và quyết định giữ lãi suất tiền gửi bán lẻ ở mức 0% vì lý do cạnh tranh thương mại.
  > "For the assessment of the -200 bps curve decrease, for some products a floor of 0% has been put in place preventing the interest rate curve going into negative interest rate territory. This is driven by the fact that, on the assets side, especially for commercial loans, it is very common to have an embedded automatic interest rate option (floors in case of the downward movements of the curve) included in the loan contract, which protect a bank from negative rates. Likewise, for the same reason, on the retail deposit side, a bank may decide to keep the customer deposit rate at zero in order not to charge depositors the negative rates."
  > — Chapter 4, lines 2044-2046 ^lubinska-u05-9

- Điều kiện không âm (Non-negativity condition) bắt buộc duy trì tỷ trọng các phân khúc sản phẩm lớn hơn 0 ($x_j > 0, w_j > 0$) vì mô hình tối ưu hóa không nhằm thay đổi mô hình kinh doanh qua việc loại bỏ các nhóm sản phẩm hiện hữu, mà nhằm tái cân bằng tỷ trọng tương đối giữa các danh mục để tối ưu hóa hàm mục tiêu.
  > "There is a non-negativity condition that must be maintained (the model does not allow the proportions to be set at zero). This is driven by the fact that the optimisation model is not meant to change the business model of the financial institution through excluding certain asset or liability classes. Instead, it is meant to change the relative proportions of the existing items in the total asset/funding base with the objective to maximise (for assets)/minimise (for liabilities) the objective function."
  > — Chapter 4, line 2158 ^lubinska-u05-10

- Hệ thống ràng buộc bao gồm giới hạn tập trung nguồn vốn khống chế tỷ trọng của từng nguồn tài trợ không vượt quá 80% tổng nguồn vốn, nhằm ngăn chặn sự phụ thuộc quá mức vào một kênh huy động đơn lẻ.
  > "The constraint functions include the concentration limits for all funding sources where it is assumed that the proportion of the certain funding source cannot be higher than 80%. It is an important constraint set up to limit the overreliance on one particular source of funding."
  > — Chapter 4, line 2174 ^lubinska-u05-11

- Nguyên lý Tinh gọn (Parsimony) trong xây dựng mô hình: mô hình càng tinh gọn càng tốt; sự tinh vi hoặc phức tạp hóa không cần thiết chỉ làm gia tăng rủi ro mô hình và gây khó khăn cho công tác quản trị, hiệu chuẩn và kiểm định mô hình.
  > "The author's view is that the more parsimonious the model, the better it is. This does not mean the author promotes rudimentary models being put in place. It means that unnecessary model sophistication increases the model risk and introduces complexity within the model management, calibration, and validation."
  > — Chapter 4, line 2208 ^lubinska-u05-12

- Định nghĩa mô hình theo chuẩn giám sát OCC/Fed SR 11-7 là thuật toán định lượng, hệ thống hoặc phương pháp tiếp cận chuyển đổi dữ liệu đầu vào thành các ước lượng định lượng; mô hình bao gồm 3 cấu phần cốt lõi: dữ liệu đầu vào (Inputs), phương pháp chuyển đổi (Transformation Method), và cấu phần báo cáo thông tin (Reporting).
  > "The term 'model' refers to a quantitative algorithm, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates (OCC, FED 2011-2012). There are at least three components of the model in the author's view:"
  > "- ■ The inputs, which introduce hypotheses and assumptions into the model."
  > "- ■ A method to transform the input into estimates. This method will generally rely on calculations to produce quantitative estimates."
  > "- ■ Areporting component that converts the estimates into useful business information."
  > — Chapter 4, lines 2212-2216 ^lubinska-u05-13

- Ba nguồn rủi ro mô hình cơ bản gồm: (1) Khiếm khuyết dữ liệu về tính sẵn có và chất lượng (sai số, thiếu chiều sâu lịch sử, cỡ mẫu không đủ); (2) Bất định ước lượng hoặc sai số mô hình (giả định khiếm khuyết, đơn giản hóa bất hợp lý, thiết kế sai); và (3) Sử dụng sai mục đích (Model misuse, dùng sai mục đích thiết kế hoặc không được hiệu chuẩn lại định kỳ).
  > "The sources of model risk can be classified into three different groups:"
  > "- ■ Data deficiencies in terms of both availability and quality, including data errors, lack of historical depth, errors in the feeding of variables, or insufficient sample size."
  > "- ■ Estimation uncertainty or model error in the form of simplifications, approximations and flawed assumptions, or incorrect model design."
  > "- ■ Model misuse, which includes using the model for purposes other than those for which it was designed and not recalibrated for a long time."
  > — Chapter 4, lines 2218-2222 ^lubinska-u05-14

- Nguyên tắc cốt lõi trong quản trị rủi ro mô hình là "Phản biện hiệu quả" (Effective Challenge) được hiểu là sự phân tích và phản biện mang tính phê phán bởi nhân sự độc lập, có năng lực chuyên môn và thâm niên thực chiến, có khả năng nhận diện các hạn chế và đề xuất điều chỉnh phù hợp.
  > "Finally, regulators emphasise that the fundamental principle in model risk management is 'effective challenge', understood as a critical analysis by objective, qualified people with experience in the line of business in which the model is used, who are able to identify model limitations and assumptions and suggest appropriate changes."
  > — Chapter 4, line 2237 ^lubinska-u05-15

### Unit u06 — Sensitivity Parameters & Empirical Case Studies (Bank 1 vs Bank 2)

- Mục đích của phân tích kịch bản độ nhạy ("what-if" analysis) là áp dụng các kịch bản định trước lên cấu trúc vốn và tài sản để đo lường mức độ tác động đến kết quả của mô hình tối ưu hóa, từ đó nhận diện các động lực trọng yếu chi phối cấu trúc sổ ngân hàng.
  > "The intention of this analysis consists of the application of the predetermined scenarios to calculated funding structure and the determination of the impact which those scenarios have on the results obtained by the optimisation model. The outcome of 'what if' analysis helps to understand which factors are the most significant and could represent a driver in the determination of the banking book structure of the bank."
  > — Chapter 4/5, lines 2251-2252 ^lubinska-u06-1

- Phân tích độ nhạy được thực hiện qua 5 kịch bản: Kịch bản cơ sở theo lãi suất và cấu trúc hiện hành; Biến động lãi suất; Thay đổi mô hình đặc tính hóa tiền gửi (độ biến động và độ nhạy lãi suất CASA); Tích hợp tỷ lệ trả nợ trước hạn của các khoản vay cố định; và Thay đổi cơ cấu ban đầu của tài sản thả nổi và cố định.
  > "The analysis is performed under the following scenarios:"
  > "- ■ Base scenario based on the prevailing rates and the initial (pre-optimised) structure of the banking book."
  > "- ■ Changes in the interest rates scenarios - impact on the target structure."
  > "- ■ Changes in the output of deposit characterisation model - changes in the balance volatility and balance sensitivity rate (changes in the behaviour of depositors)."
  > "- ■ Inclusion of the prepayment rate of loans - inclusion of the prepayment rate in the fixed rate asset base (in analysed case studies, under base scenario, only contractual characteristics of loans have been taken into account)."
  > "- ■ Changes in initial asset base changes in the initial structure of floating and fixed rate assets."
  > — Chapter 4/5, lines 2253-2259 ^lubinska-u06-2

- Dưới kịch bản trả nợ trước hạn với tỷ lệ CPR 7% áp dụng cho tài sản lãi suất cố định, việc đưa CPR vào mô hình tạo tác động kép đáng kể lên cả cơ cấu rủi ro lãi suất (biến động delta NII) và các chỉ số thanh khoản do lượng thanh khoản dôi dư phát sinh cần phải tái đầu tư.
  > "Under the 'prepayment scenario' the constant prepayment rate is 7% and refers only to fixed rate assets. The introduction of the CPR in the model has significant impact both on the IRR structure of the banking book (in terms of delta NII ) and liquidity metrics, given the additional amount of liquidity which needs to be reinvested."
  > — Chapter 5, lines 2340-2342 ^lubinska-u06-3

- Ngân hàng 1 có quy mô RSA đạt EUR 3.4 tỷ, phần lớn là cho vay doanh nghiệp lãi suất thả nổi neo theo EURIBOR 1M, trong khi nợ phải trả chủ yếu neo theo EURIBOR 3M và 6M.
  > "Bank 1 has EUR3.4bn of risk sensitive assets and most of them are made up of lending to corporate customers at a floating rate. The remainder constitutes customers lending at a fixed rate and liquidity buffer. The corporate loans are indexed to EURIBOR 1M, while liabilities are mainly indexed to EURIBOR 3 M and 6M."
  > — Chapter 5, lines 2358-2360 ^lubinska-u06-4

- Tại Ngân hàng 1, tài khoản thanh toán CASA có độ biến động số dư cao khi chỉ có 35% được coi là ổn định, phần còn lại nhạy cảm trước các yếu tố đặc thù và vĩ mô nên được phân bổ vào các dải kỳ hạn ngắn hạn: O/N đối với IRRBB và 1M đối với thanh khoản.
  > "In the case of Bank 1, the current accounts have shown high balance volatility as only 35% of these products have been considered as stable. The remainder portion of balances is volatile and sensitive to the changes in external and idiosyncratic factors. Thus, it is assumed that current accounts, both from the liquidity perspective and interest rate perspective, have been allocated to the short-term buckets, i.e. O/N for IRRBB and 1 M for liquidity."
  > — Chapter 5, line 2360 ^lubinska-u06-5

- Kết quả thực nghiệm tại Ngân hàng 1 chứng minh thu nhập bình quân gia quyền được cải thiện trên mọi kịch bản với delta thặng dư dao động từ EUR 3.8 triệu đến EUR 7.63 triệu (cao nhất ở kịch bản thay đổi cơ cấu tài sản), xác thực việc áp dụng kỹ thuật tối ưu hóa định lượng nâng cao khả năng sinh lời của ngân hàng.
  > "It can be seen that, in the case of Bank 1, the weighted average income has improved for all scenarios and the delta between the results before and after optimisation varies from EUR3.8m to EUR7.63m depending on the scenario applied. It can be observed that the highest delta is achieved for the Change in the asset structure (7.63m). These results, displayed in the table, lead to the confirmation of our expectation, i.e. they confirm that the introduction of numerical optimisation techniques for the banking book has a positive impact on the bank's profitability in terms of the weighted average income"
  > — Chapter 5, lines 2382-2384 ^lubinska-u06-6

- Mô hình tính toán tỷ trọng mới giữa các nhóm tài sản để tối đa hóa lợi nhuận danh mục đồng thời bảo đảm tuân thủ hạn mức nội bộ và pháp định; mô hình chỉ ra cấu trúc mục tiêu tiềm năng, nhưng quá trình tái định hình bảng cân đối đòi hỏi thời gian và không thể hoàn thành qua đêm.
  > "The model calculates the new proportions of the different asset classes to increase overall portfolio profitability and, at the same time, to maintain compliance with the internal and regulatory limits. At this point, it is important to highlight that the optimisation exercise indicates, potentially, the target profile of the analysed portfolio subject to a certain set of assumptions. The process of reshaping of the portfolio, in order to achieve the desirable structure, is another side of the optimisation process in the sense that it takes time to shape the balance sheet, as it cannot be done overnight."
  > — Chapter 5, line 2390 ^lubinska-u06-7

- Ngân hàng 1 vi phạm tỷ lệ thanh khoản tích lũy ngắn hạn dưới mọi kịch bản trước khi triển khai mô hình tối ưu hóa; tuy nhiên hạn mức này đã được thỏa mãn tuyệt đối sau khi tối ưu hóa.
  > "Bank 1 breaches the short-term cumulative liquidity ratio under all scenarios before the implementation of optimisation model. However, this limit is respected after optimisation."
  > — Chapter 5, line 2424 ^lubinska-u06-8

- Dưới kịch bản kỳ vọng lạm phát, tổng chi phí huy động vốn của Ngân hàng 1 tăng nhẹ (từ EUR 34.37m lên EUR 34.88m) do mô hình tối ưu hóa ràng buộc bắt buộc phải áp đặt một cơ cấu nợ đáp ứng chuẩn tỷ lệ thanh khoản tích lũy ngắn hạn 100% mà ngân hàng từng vi phạm trước đó.
  > "Under the Inflation expectation scenario the total funding cost has slightly increased (from EUR34.37m to EUR34.88m). However, it is fully explained by the fact that Bank 1, before the implementation of the optimisation model, was not compliant with the short-term cumulative liquidity ratio set at 100% (see Table 5.2). Consequently, the constrained optimisation process imposes such a structure, in terms of liabilities, which complies with the liquidity requirement (and short-term cumulative liquidity ratio)."
  > — Chapter 5, line 2396 ^lubinska-u06-9

- Kết quả nhấn mạnh tầm quan trọng của các giả định hành vi trong việc giảm chi phí vốn và độ nhạy rất cao của mô hình tối ưu hóa trước yếu tố này; đặc biệt độ nhạy đối với các giả định hành vi bên nợ phải trả (CASA) cao hơn đáng kể so với bên tài sản (prepayment).
  > "This result indicates the importance of the behavioural assumption in the reduction of funding costs and high sensitivity of the optimisation model to this factor. In addition, the sensitivity to behavioural assumptions on the liability side appears to be higher than on the asset side."
  > — Chapter 5, line 2400 ^lubinska-u06-10

- Ngân hàng 2 có quy mô RSA đạt USD 549 tỷ (USD 109 tỷ tài sản bán lẻ chủ yếu là administered rate theo thông lệ thị trường Anh, USD 178 tỷ khách hàng doanh nghiệp, USD 202 tỷ thị trường tài chính, USD 60 tỷ HQLA); phần lớn tài sản là các khoản vay tài trợ thương mại lãi suất cố định ngắn hạn.
  > "In our case study we assume that the asset base is composed of USD109bn of retail assets, USD178bn of corporate client assets, USD202bn of financial market assets, and USD60bn of HQLA. In total, the RSA amounts to USD549bn. The majority of assets are short-term fixed-rate trade finance loans which are classified by the counterparty type, i.e. loans to banks and loans to non-bank financial institutions. The retail assets are mainly administered rate, which is a common feature in the UK market. The remainder is composed of floating rate assets indexed to LIBOR 1 M and 3 M."
  > — Chapter 5, lines 2511-2513 ^lubinska-u06-11

- Trên cơ sở hợp đồng, toàn bộ nợ phải trả của Ngân hàng 2 có kỳ hạn bình quân dưới 1 năm; cấu trúc này đưa rủi ro mô hình trọng yếu vào sổ ngân hàng do phụ thuộc hoàn toàn vào các giả định và kết quả của mô hình đặc tính hóa tiền gửi không kỳ hạn (sản phẩm kỳ hạn hợp đồng 1 ngày nhưng được mô hình hóa dài hạn cho mục đích quản trị).
  > "Bank 2, on a contractual basis, has all liabilities with an average maturity lower than 1 year (see Figure 5.10). This structure introduces material model risk embedded in the banking book which is driven by the assumptions and outcomes of the deposit characterisation model described in detail in the Chapter 3 section 'Modelling of Customers' Deposits - Liabilities Side'. This is driven by the fact that products without deterministic maturity (contractual maturity equal to 1 day), for risk management purposes, have to be analysed and modelled."
  > — Chapter 5, lines 2579-2580 ^lubinska-u06-12

- Phân tích danh mục tài sản của Ngân hàng 2 chỉ ra lợi ích kinh tế cao nhất từ mô hình tối ưu hóa đạt được ở kịch bản thay đổi cơ cấu tài sản lãi suất cố định với thặng dư lên tới USD 1.25 tỷ, tương đồng với kết quả độ nhạy cao nhất tại Ngân hàng 1.
  > "The analysis of Bank 2, for the asset base, indicates that the highest benefit from the application of the optimisation model was achieved under the Change in the fixed rate asset structure scenario, in which case the economic advantage totalled USD1.25bn. This is a very interesting result, as Bank 1 has shown the highest sensitivity to the same factor."
  > — Chapter 5, line 2585 ^lubinska-u06-13

- Tại Ngân hàng 2, kịch bản thay đổi giả định mô hình tiền gửi không nằm trong nhóm tác động lớn nhất do hiệu ứng quy mô: ngân hàng quốc tế quy mô lớn phản ứng chậm hơn trước thay đổi giả định mô hình so với ngân hàng nhỏ, cơ sở tài sản và nguồn vốn đa dạng hóa cao giúp giảm thiểu và hấp thụ tác động của các giả định hành vi.
  > "For Bank 2 the Change in the deposit modelling assumptions scenario is not amongst the highest impact factors, although still important. The author deduces that this fact can be justified by the size of the bank. Bank 2 is a large international bank which reacts more slowly to changes in modelling assumptions in comparison to Bank 1. The funding and asset base is more diversified, so the impact of changes in behavioural assumptions is subdued by the existence of other items in the banking book."
  > — Chapter 5, line 2673 ^lubinska-u06-14

### Unit u07 — Conclusions & Numerical Proof Data for Bank 1

- Quá trình tối ưu hóa sổ ngân hàng được phân tách thành hai bài toán tối ưu hóa riêng biệt cho bên tài sản (tối đa hóa thu nhập) và bên nợ (tối thiểu hóa chi phí vốn); các giả định nền tảng bao gồm mô hình hóa các khoản mục không có kỳ hạn xác định (độ nhạy lãi suất và độ biến động số dư CASA), tỷ lệ trả nợ trước hạn tài sản cố định, tỷ lệ tái tục tiền gửi có kỳ hạn, và các giả định định giá FTP phản ánh thị trường địa phương.
  > "The minimisation of the funding costs and maximisation of the assets income was articulated as two separate optimisation problems, i.e. it has been run for assets and liabilities separately. In addition, for each optimisation exercise, there are underlying assumptions which are related to the modelling of items without deterministic maturity (for example, the degree of rate sensitivity and balance volatility of CASA); the extent of fixed rate asset prepayments which banks face; the willingness of customers to roll over the time deposits upon their expiration; and the pricing assumptions for both assets and liabilities, i.e. the commercial spread and liquidity premium recognised to liabilities or charged to assets."
  > — Chapter 5, line 2683 ^lubinska-u07-1

- Bài toán tối ưu hóa sổ ngân hàng là bài toán tối ưu hóa có ràng buộc chịu sự chi phối của các hạn mức nội bộ và pháp định; các hàm ràng buộc bao gồm cả phương trình đẳng thức và bất đẳng thức, đưa thêm một lớp phức tạp vào phương pháp luận tối ưu hóa.
  > "Theproblemrepresents the constrained optimisation issue, since minimisation of the cost of funds and maximisation of the assets income are subject to internal limits (constraints) listed in Building the Objective and Constraint Functions in the Optimisation Process of Chapter 4. The constraint functions are both equality and inequality functions, which introduces an additional layer of complexity in the optimisation methodology."
  > — Chapter 5, line 2685 ^lubinska-u07-2

- Cuốn sách giải quyết câu hỏi trung tâm: liệu thông qua việc ứng dụng các kỹ thuật tối ưu hóa định lượng có thể tìm ra một cấu trúc mục tiêu của sổ ngân hàng mang lại kết quả kinh tế cải thiện, đồng thời bảo đảm tuân thủ tuyệt đối các hạn mức rủi ro nội bộ hay không.
  > "In general, this book has addressed the question of whether it is possible, through the application of optimisation techniques, to find the target structure of the banking book which provides the bank with an improved economic result and, at the same time, ensures respect for the internal limits for risks incurred by the bank."
  > — Chapter 5, line 2691 ^lubinska-u07-3

- Kết quả tính toán của mô hình tối ưu hóa cung cấp bằng chứng rõ ràng về lợi ích kinh tế đạt được dưới cả kịch bản cơ sở và các kịch bản kiểm định độ nhạy; biên độ của lợi ích kinh tế này tỷ lệ thuận với quy mô của sổ ngân hàng.
  > "The results calculated by the optimisation model provide clear evidence of the economic benefit under both the base and sensitivity scenarios. Further, the immediate observation is that the magnitude of this benefit is proportional to the size of the banking book."
  > — Chapter 5, line 2695 ^lubinska-u07-4

- Nhân tố nhạy cảm nhất trong việc cắt giảm chi phí vốn chính là cấu trúc ban đầu của sổ ngân hàng; cơ cấu tài sản ban đầu quyết định biên độ lợi ích đạt được từ mô hình; mô hình tối ưu hóa vận hành hiệu quả hơn đối với một số cấu trúc nhất định, và một số ngân hàng dường như "được định sẵn" đạt khả năng sinh lời cao hơn với mô hình ngay từ đầu thông qua thiết lập cấu trúc khởi điểm của họ.
  > "Analysing the outcome in terms of the reduction in the cost of funding, it turned out that the most sensitive factor is related to the initial structure of the banking book. The initial composition of the banking book, in terms of assets, seems to determine the level of magnitude of benefit achieved by the application of the model. This could drive towards the conclusion that the optimisation 'works better' for certain structures (compositions) of the banking book than others. This point appears to be valid either for the maximisation of the assets income or the minimisation of the cost of funding. The author goes slightly further with this conclusion and suggests that it could be that some banks are already destined to be more profitable with the optimisation model at the outset, i.e. through their initial structure set up."
  > — Chapter 5, line 2697 ^lubinska-u07-5

- Dưới kịch bản đường cong lợi suất dịch chuyển đi lên (kỳ vọng lạm phát và khủng hoảng nguồn cung dầu), mức độ cắt giảm chi phí huy động vốn đạt được cao hơn so với kịch bản cơ sở hoặc kịch bản đường cong dịch chuyển đi xuống; sự kiện hạ bậc tín nhiệm cũng thúc đẩy mức cắt giảm chi phí vốn cao hơn.
  > "Under upwards movement of the curve (scenarios: Inflation Expectation and the Oil Supply crisis ) the reduction in cost of funding is higher than under the base and downward movement of the term structure scenario (the Earthquake scenario). Also, under the downgrade event the model seems to drive higher reduction in funding cost in comparison to other factors."
  > — Chapter 5, line 2697 ^lubinska-u07-6

- Tại ngân hàng nhỏ (Ngân hàng 1), dù vi phạm hạn mức thanh khoản nội bộ tại thời điểm khởi đầu, mô hình quyết định vẫn dẫn dắt cấu trúc sổ ngân hàng hướng tới một cấu trúc thỏa mãn hạn mức và mang lại lợi ích kinh tế; dưới môi trường lãi suất tăng, sự gia tăng nhẹ chi phí ở kịch bản lạm phát là chi phí tối thiểu bắt buộc phải trả để khôi phục sự tuân thủ hạn mức.
  > "Consequently, to satisfy the constraints imposed in the model, under a rising interest rate environment, this result can be seen as a minimum cost required to maintain compliance with internal limits. An interesting point emerges in relation to the remainder of the scenarios analysed. As already mentioned, the smaller sized institution (Bank 1) breaches the internal liquidity limit at the initial stage of the optimisation exercise. Nevertheless, the application of the decision model drives the banking book structure towards a composition which satisfies the limit and provides the institution with economic benefit (except in the one case described above)."
  > — Chapter 5, line 2703 ^lubinska-u07-7

- Mô hình tối ưu hóa cải thiện đồng thời quản trị rủi ro lãi suất (kéo giảm độ nhạy NII) và các chỉ số thanh khoản, ngăn ngừa việc nắm giữ thanh khoản dư thừa không hiệu quả dưới dạng đệm LAB hoặc tích trữ nguồn vốn dài hạn quá mức làm hạn chế lợi nhuận từ chuyển đổi kỳ hạn lành mạnh.
  > "The optimisation model improves the management of the interest rate risk and liquidity risk in terms of the better result of internal risk metric in all scenarios applied. It can be clearly seen that in case of the NII sensitivity, the application of the model decreases the interest rate risk sensitivity. The same point is valid for the liquidity risk metrics. It appears that the model also optimises the short-term liquidity metrics, preventing the excess liquidity being kept under the form of a liquidity buffer, and the inefficient management of stable funding. In particular, it refers to the excessive long-term funding the banks have, and as a consequence, limitation of potential profit resulting from the healthy maturity transformation run by the bank."
  > — Chapter 5, line 2705 ^lubinska-u07-8

- Dưới cấu trúc ban đầu của Ngân hàng 1 ở kịch bản cơ sở, tỷ lệ thanh khoản tích lũy ngắn hạn bị vi phạm ở mức 59.7% và độ nhạy Delta NII sốc +200 bps lên tới 80.5%.
  > "Under the existing structure, the liquidity and interest rate risk exposure metrics are as follows:"
  > "- ■ Cumulative short-term liquidity ratio = 59.7%"
  > "- ■ Structural ratio = 91.9%"
  > "- ■ Delta NII + 200bps = 80.5%"
  > "- ■ Delta NII -200bps = 11.62%"
  > "- ■ CAR = 26.2%."
  > — Chapter 5, lines 2741-2745 ^lubinska-u07-9

- Dưới cấu trúc mục tiêu sau tối ưu hóa của Ngân hàng 1, tỷ lệ thanh khoản ngắn hạn đạt chuẩn tuyệt đối 100%, tỷ lệ cấu trúc đạt 93.9%, Delta NII sốc +200 bps giảm mạnh từ 80.5% về hạn mức 4%, và CAR duy trì ở mức an toàn 22%.
  > "Under the target structure, the liquidity and interest rate risk exposure metrics are as follows:"
  > "- ■ Cumulative short-term liquidity ratio = 100%"
  > "- ■ Structural ratio = 93.9%"
  > "- ■ Delta NII + 200bps = 4%"
  > "- ■ Delta NII -200bps = 7.8%"
  > "- ■ CAR = 22%."
  > — Chapter 5, lines 2766-2770 ^lubinska-u07-10

- Việc triển khai mô hình quyết định cho danh mục tài sản của Ngân hàng 1 mang lại mức gia tăng thu nhập lãi thuần lên tới EUR 0.069 tỷ (EUR 6.9 triệu) trong khoảng thời gian 6 tháng.
  > "The implementation of the decision model resulted in an increase in the interest income over the period of 6 months of EUR0.069bn ."
  > — Chapter 5, line 2758 ^lubinska-u07-11

- Đối với danh mục nguồn vốn của Ngân hàng 1 dưới kịch bản cơ sở, lợi ích kinh tế từ việc triển khai mô hình quyết định đạt EUR 0.2964 triệu tính trên cơ sở năm, đồng thời ngân hàng tuân thủ toàn bộ các hạn mức quy định.
  > "The economic benefit from the implementation of the decision model amounts to EUR0.2964m on an annual basis. In addition, the bank respects all limits imposed."
  > — Chapter 5, line 2928 ^lubinska-u07-12

- Dưới kịch bản rủi ro vỡ nợ HY/LBO của Ngân hàng 1, lợi ích kinh tế từ việc giảm chi phí vốn đạt EUR 0.6677 triệu tính trên cơ sở năm so với cấu trúc vốn ban đầu tại thời điểm t0.
  > "There is benefit resulting from the implementation of the decision model comparing to the initial structure of funding in t 0 . The economic benefit from the implementation of the decision model amounts to EUR0.6677m on an annual basis."
  > — Chapter 5, line 3038 ^lubinska-u07-13

- Dưới kịch bản thay đổi kết quả mô hình đặc tính hóa tiền gửi CASA của Ngân hàng 1, lợi ích kinh tế từ việc triển khai mô hình tối ưu hóa mang lại mức thặng dư vượt trội lên tới EUR 1.1954 triệu tính trên cơ sở năm.
  > "There is a benefit resulting from the implementation of the decision model compared to the initial structure of funding at t 0 . The economic benefit from the implementation of the decision model amounts to EUR 1.1954m on an annual basis."
  > — Chapter 5, line 3088 ^lubinska-u07-14

### Unit u08 — Changes in the Initial Proportions of the Asset Base, Funding Sensitivity for Bank 1 & Bank 2 Asset-Side Optimisation

- Thay đổi cơ cấu tài sản ban đầu mang lại lợi ích kinh tế đáng kể EUR 4.9560 triệu từ việc giảm chi phí vốn so với cấu trúc vốn ban đầu tại thời điểm t0.
  > "There is significant benefit resulting from the change in the initial amounts of asset portfolios compared to the cost of the initial structure of funding (at t 0 ). The economic benefit from implementation of the decision model amounts to EUR4.9560m ."
  > — Chapter 5, line 3135 ^lubinska-u08-1

- Dưới kịch bản thay đổi tỷ trọng danh mục tài sản (Asset 1 chiếm 83.69%), ngân hàng ban đầu vi phạm hạn mức thanh khoản ngắn hạn với tỷ lệ chỉ đạt 60.89%.
  > "The bank is breaching the short-term liquidity limit."
  > — Chapter 5, line 3177 ^lubinska-u08-2

- Việc áp dụng mô hình quyết định dưới kịch bản thay đổi tỷ trọng tài sản giúp giảm chi phí vốn và mang lại lợi ích kinh tế EUR 0.5663 triệu.
  > "The economic benefit from the implementation of the decision model amounts to EUR0.5663m ."
  > — Chapter 5, line 3199 ^lubinska-u08-3

- Dưới kịch bản ngân hàng bị hạ 1 bậc tín nhiệm, mô hình tối ưu hóa giúp giảm chi phí vốn và mang lại lợi ích kinh tế EUR 0.6388 triệu.
  > "The economic benefit from the implementation of the decision model amounts to EUR0.6388m ."
  > — Chapter 5, line 3251 ^lubinska-u08-4

- Dưới kịch bản tính đến tỷ lệ trả nợ trước hạn CPR của tài sản cố định, việc triển khai mô hình quyết định đem lại lợi ích kinh tế EUR 1.2244 triệu từ việc giảm chi phí nguồn vốn.
  > "The economic benefit from the implementation of the decision model amounts to EUR1.2244m ."
  > — Chapter 5, line 3305 ^lubinska-u08-5

- Cơ cấu tài sản ban đầu của Ngân hàng 2 (USD 549bn) dưới kịch bản cơ sở gồm 19.85% tài sản bán lẻ, 32.42% khách hàng doanh nghiệp, 36.79% thị trường tài chính và 10.92% đệm tài sản thanh khoản LAB.
  > "■ Retail assets wAsset1 = 19.85% ■ Corporate Clients assets wAsset2 = 32.42% ■ Financial Market assets wAsset3 = 36.79% ■ to Banks - 6 month (20% of Asset 3 ) ■ Non-Bank Financial Institution (NBFI) > 6m - 9 month (40% of Asset 3 ) ■ Non-Bank Financial Institution (NBFI) < 6m - 4 month (40% of Asset 3 ) ■ Liquid Asset buffer wAsset4 = 10.92%."
  > — Chapter 5, lines 3321–3323 ^lubinska-u08-6

- Các chỉ số rủi ro thanh khoản và lãi suất ban đầu của Ngân hàng 2 dưới kịch bản cơ sở phản ánh sự dư thừa thanh khoản (Survival Horizon SH_2M lên tới 134%).
  > "- ■ AD ratio = 80%"
  > "- ■ MTFR contractual = 60%"
  > "- ■ MTFR behavioural = 176%"
  > "- ■ SH\_2M = 134%"
  > "- ■ Delta NII + 200bps = 38%"
  > "- ■ Delta NII -200bps = 1.9%"
  > "- ■ CAR = 12.4%."
  > — Chapter 5, lines 3341–3347 ^lubinska-u08-7

- Cơ cấu tài sản mục tiêu của Ngân hàng 2 sau tối ưu hóa cắt giảm đệm LAB dư thừa xuống 4.66% và tái phân bổ sang tài sản bán lẻ (26.76%) và thị trường tài chính (43.19%).
  > "- ■ Retail assets wAsset1 = 26.76%"
  > "- ■ Corporate Clients assets wAsset2 = 25.40%"
  > "- ■ Financial Market assets wAsset3 = 43.19%"
  > "- ■ to Banks - 6 month (20% of Asset 3 )"
  > "- ■ Non-Bank Financial Institution (NBFI) &gt; 6m - 9 month (40% of Asset 3 )"
  > "- ■ Non-Bank Financial Institution (NBFI) &lt; 6m - 4 month (40% of Asset 3 )"
  > "- ■ Liquid Asset buffer wAsset4 = 4.66%."
  > — Chapter 5, lines 3351–3358 ^lubinska-u08-8

- Việc triển khai mô hình quyết định tại Ngân hàng 2 dưới kịch bản cơ sở giúp gia tăng thu nhập lãi thêm USD 0.2849 tỷ (USD 284.9 triệu) trong kỳ 6 tháng.
  > "The implementation of the decision model has resulted in an increase in the interest income over the period of 6 months of USD0.2849bn ."
  > — Chapter 5, line 3369 ^lubinska-u08-9

- Dưới cấu trúc tài sản mục tiêu của Ngân hàng 2, tỷ lệ sinh tồn 2 tháng SH_2M được tinh gọn về đúng hạn mức 100%, đồng thời độ nhạy lãi suất Delta NII +200bps giảm từ 38% xuống 30.37%.
  > "- ■ AD ratio = 80%"
  > "- ■ MTFR contractual = 60.15%"
  > "- ■ MTFR behavioural = 166%"
  > "- ■ SH\_2M = 100%"
  > "- ■ Delta NII + 200bps = 30.37%"
  > "- ■ Delta NII -200bps = 1.51%"
  > "- ■ CAR = 12%."
  > — Chapter 5, lines 3381–3387 ^lubinska-u08-10

- Dưới kịch bản khủng hoảng nguồn cung dầu mỏ (Oil Supply Crisis - lãi suất tăng), mô hình tối ưu hóa giúp gia tăng thu nhập lãi của Ngân hàng 2 thêm USD 0.3452 tỷ (USD 345.2 triệu) trong 6 tháng.
  > "The implementation of the decision model has resulted in an increase in the interest income over the period of 6 months of USD0.3452bn ."
  > — Chapter 5, line 3443 ^lubinska-u08-11

- Các chỉ số rủi ro mục tiêu của Ngân hàng 2 dưới kịch bản sốc lãi suất tăng (Oil Supply Crisis) duy trì tuân thủ nghiêm ngặt mọi hạn mức với Delta NII +200bps giảm về 27.68% và SH_2M đạt 100%.
  > "- ■ AD ratio = 79%"
  > "- ■ MTFR contractual = 60.15%"
  > "- ■ MTFR behavioural = 165.86%"
  > "- ■ SH\_2M = 100%"
  > "- ■ Delta NII + 200bps = 27.68%"
  > "- ■ Delta NII -200bps = 1.384%"
  > "- ■ CAR = 12%."
  > — Chapter 5, lines 3455–3461 ^lubinska-u08-12

- Dưới kịch bản động đất (Earthquake - lãi suất giảm), việc triển khai mô hình quyết định giúp thu nhập lãi tăng thêm USD 0.2730 tỷ (USD 273.0 triệu) trong kỳ 6 tháng.
  > "The implementation of the decision model has resulted in an increase in the interest income over the period of 6 months of USD0.2730bn ."
  > — Chapter 5, line 3515 ^lubinska-u08-13

- Các chỉ số rủi ro mục tiêu của Ngân hàng 2 dưới kịch bản sốc lãi suất giảm duy trì tỷ lệ sinh tồn SH_2M ở mức 100% và kéo giảm độ nhạy Delta NII +200bps từ 39.5% xuống 31.5%.
  > "- ■ AD ratio = 79.9%"
  > "- ■ MTFR contractual = 60.15%"
  > "- ■ MTFR behavioural = 165.9%"
  > "- ■ SH\_2M = 100%"
  > "- ■ Delta NII + 200bps = 31.5%"
  > "- ■ Delta NII -200bps = 1.57%"
  > "- ■ CAR = 12%."
  > — Chapter 5, lines 3527–3533 ^lubinska-u08-14

### Unit u09 — Bank 2 Asset-Side Scenarios & Liabilities-Side Base Scenario Optimization

- Dưới kịch bản kỳ vọng lạm phát, việc triển khai mô hình quyết định giúp thu nhập lãi tăng thêm USD 0.3829 tỷ trong kỳ 6 tháng.
  > "The implementation of the decision model has resulted in an increase in the interest income over the period of 6 months of USD0.3829bn ."
  > — Chapter 5, line 3587 ^lubinska-u09-1

- Các chỉ số rủi ro mục tiêu của Ngân hàng 2 dưới kịch bản kỳ vọng lạm phát duy trì tỷ lệ sinh tồn SH_2M ở mức 100% và nén Delta NII +200bps về 24.64%.
  > "- ■ AD ratio = 79.9%"
  > "- ■ MTFR contractual = 60.15%"
  > "- ■ MTFR behavioural = 166%"
  > "- ■ SH\_2M = 100%"
  > "- ■ Delta NII + 200bps = 24.64%"
  > "- ■ Delta NII -200bps = 1.23%"
  > "- ■ CAR = 12%."
  > — Chapter 5, lines 3599–3605 ^lubinska-u09-2

- Dưới kịch bản ngân hàng bị hạ 1 bậc tín nhiệm, mô hình phân bổ tỷ trọng cực đoan: nâng tài sản bán lẻ lên 52.14% và cắt giảm tài sản doanh nghiệp về 0.00011%.
  > "- ■ Retail assets wAsset1 = 52.14%"
  > "- ■ Corporate Clients assets wAsset2 = 0.00011%"
  > "- ■ Financial Market assets wAsset3 = 41.46%"
  > "- ■ to Banks - 6 month (20% of Asset 3 )"
  > "- ■ Non-Bank Financial Institution (NBFI) &gt; 6m - 9 month (40% of Asset 3 )"
  > "- ■ Non-Bank Financial Institution (NBFI) &lt; 6m - 4 month (40% of Asset 3 )"
  > "- ■ Liquid Asset buffer wAsset4 = 6.38%."
  > — Chapter 5, lines 3642–3648 ^lubinska-u09-3

- Triển khai mô hình quyết định dưới kịch bản hạ bậc tín nhiệm giúp gia tăng thu nhập lãi của Ngân hàng 2 thêm USD 0.3929 tỷ trong kỳ 6 tháng.
  > "The implementation of the decision model has resulted in an increase in the interest income over the period of 6 months of USD0.3929bn ."
  > — Chapter 5, line 3659 ^lubinska-u09-4

- Dưới kịch bản hạ bậc tín nhiệm, tỷ lệ an toàn vốn CAR tăng vọt lên 14.56% và SH_2M đạt đúng hạn mức 100%.
  > "- ■ AD ratio = 79.9%"
  > "- ■ MTFR contractual = 60.15%"
  > "- ■ MTFR behavioural = 152%"
  > "- ■ SH\_2M = 100%"
  > "- ■ Delta NII + 200bps = 59.9%"
  > "- ■ Delta NII -200bps = 2.99%"
  > "- ■ CAR = 14.56%."
  > — Chapter 5, lines 3671–3677 ^lubinska-u09-5

- Dưới kịch bản tính đến tỷ lệ trả nợ trước hạn CPR của tài sản cố định, việc triển khai mô hình quyết định mang lại mức tăng thu nhập lãi USD 0.2849 tỷ trong 6 tháng.
  > "The implementation of the decision model has resulted in an increase in the interest income over the period of 6 months of USD0.2849bn ."
  > — Chapter 5, line 3731 ^lubinska-u09-6

- Dưới kịch bản thay đổi kết quả mô hình đặc tính hóa tiền gửi CASA, việc triển khai mô hình giúp tăng thu nhập lãi thêm USD 0.2849 tỷ trong 6 tháng.
  > "The implementation of the decision model has resulted in an increase in the interest income over the period of 6 months of USD0.2849bn ."
  > — Chapter 5, line 3805 ^lubinska-u09-7

- Các chỉ số rủi ro mục tiêu dưới kịch bản thay đổi kết quả mô hình tiền gửi duy trì SH_2M ở mức 100% và kéo giảm Delta NII +200bps xuống 24.31%.
  > "- ■ SH\_2M = 100%"
  > "- ■ Delta NII + 200bps = 24.31%"
  > "- ■ Delta NII -200bps = 1.21%"
  > "- ■ CAR = 12%."
  > — Chapter 5, lines 3820–3823 ^lubinska-u09-8

- Dưới kịch bản tỷ trọng ban đầu của tài sản cố định thay đổi và nắm giữ đệm LAB lên tới 25.13%, tổng thu nhập lãi ban đầu chỉ đạt USD 5.334 tỷ.
  > "Total interest income = USD5.334bn."
  > — Chapter 5, line 3842 ^lubinska-u09-9

- Việc cắt giảm đệm LAB từ 25.13% về 4.66% và tái phân bổ sang tài sản sinh lời mang lại thặng dư thu nhập lãi kỷ lục USD 1.255 tỷ trong kỳ 6 tháng.
  > "The implementation of the decision model has resulted in an increase in the interest income over the period of 6 months of USD1.255bn ."
  > — Chapter 5, line 3877 ^lubinska-u09-10

- Cấu trúc mục tiêu sau khi thu hẹp đệm LAB dư thừa bảo đảm SH_2M đạt chuẩn 100% và Delta NII +200bps ở mức an toàn 30.37%.
  > "- ■ SH\_2M = 100%"
  > "- ■ Delta NII + 200bps = 30.37%"
  > "- ■ Delta NII -200bps = 1.51%"
  > "- ■ CAR = 12%."
  > — Chapter 5, lines 3892–3895 ^lubinska-u09-11

- Cấu trúc nguồn vốn ban đầu tại t0 của Ngân hàng 2 gồm 28.3% CASA bán lẻ, 27.8% CASA giao dịch, 11.4% trái phiếu cao cấp, 20.5% tiền gửi kỳ hạn DN, 4.2% tiền gửi cấu trúc và 7.8% CP/CD.
  > "- ■ Retail current accounts (CASA) wA = 28.3%"
  > "- ■ TB current accounts wB = 27.8%"
  > "- ■ Senior debt issuance wC = 11.4%"
  > "- ■ Corporate time deposits wD1 = 20.5%"
  > "- ■ Structured deposits wD2 = 4.2%"
  > "- ■ Commercial papers and certificates of deposits wD3 = 7.8%."
  > — Chapter 5, lines 3901–3907 ^lubinska-u09-12

- Tổng chi phí huy động vốn ban đầu của Ngân hàng 2 dưới kịch bản cơ sở là USD 2.8493 tỷ trong 6 tháng.
  > "Total cost = USD2.8493bn."
  > — Chapter 5, line 3918 ^lubinska-u09-13

- Cấu trúc nguồn vốn sau tối ưu hóa tăng CASA bán lẻ lên 51.16%, giảm CASA giao dịch xuống 10%, giảm trái phiếu cao cấp xuống 3.8% và CP/CD xuống 2%.
  > "- ■ Retail current accounts (CASA) wA = 51.16%"
  > "- ■ TB current accounts wB = 10%"
  > "- ■ Senior debt issuance wC = 3.8%"
  > "- ■ Corporate time deposits wD1 = 30%"
  > "- ■ Structured deposits wD2 = 3%"
  > "- ■ Commercial papers and certificates of deposits wD3 = 2%."
  > — Chapter 5, lines 3935–3940 ^lubinska-u09-14

- Việc triển khai mô hình quyết định mang lại mức cắt giảm chi phí vốn khổng lồ USD 0.6526 tỷ (USD 652.6 triệu) trong kỳ 6 tháng.
  > "The implementation of decision model has resulted in a reduction of the funding cost over the period of 6 months of USD0.6526bn ."
  > — Chapter 5, line 3957 ^lubinska-u09-15

### Unit u10 — Bank 2 Liabilities-Side Sensitivity Scenarios Across Interest Rate Shocks & Market Events

- Dưới kịch bản kỳ vọng lạm phát, chi phí huy động vốn ban đầu của Ngân hàng 2 là USD 3.3356 tỷ trong 6 tháng.
  > "Total cost = USD3.3356bn."
  > — Chapter 5, line 3993 ^lubinska-u10-1

- Sau khi áp dụng mô hình quyết định dưới kịch bản kỳ vọng lạm phát, chi phí vốn giảm xuống USD 2.6928 tỷ trong 6 tháng.
  > "Total cost = USD2.6928bn."
  > — Chapter 5, line 4018 ^lubinska-u10-2

- Triển khai mô hình tối ưu hóa dưới kịch bản kỳ vọng lạm phát giúp giảm chi phí vốn thêm USD 0.6428 tỷ trong kỳ 6 tháng.
  > "The implementation of the decision model has resulted in a reduction of funding costs over the period of 6 months of USD0.6428bn ."
  > — Chapter 5, line 4024 ^lubinska-u10-3

- Các chỉ số rủi ro mục tiêu của Ngân hàng 2 dưới kịch bản lạm phát bảo đảm SH_2M đạt 156% và nén Delta NII +200bps xuống 49%.
  > "- ■ AD ratio = 72%"
  > "- ■ MTFR contractual = 35%"
  > "- ■ MTFR behavioural = 175%"
  > "- ■ SH\_2M = 156%"
  > "- ■ Delta NII + 200bps = 49%"
  > "- ■ Delta NII -200bps = 2.47%."
  > — Chapter 5, lines 4032–4037 ^lubinska-u10-4

- Dưới kịch bản khủng hoảng nguồn cung dầu mỏ, chi phí huy động vốn ban đầu là USD 3.0597 tỷ trong 6 tháng.
  > "Total cost = USD3.0597bn."
  > — Chapter 5, line 4057 ^lubinska-u10-5

- Việc áp dụng mô hình quyết định dưới kịch bản khủng hoảng dầu mỏ giúp giảm chi phí vốn USD 0.6591 tỷ trong 6 tháng.
  > "The implementation of the decision model has resulted in a reduction of funding costs over the period of 6 months of USD0.6591bn."
  > — Chapter 5, line 4092 ^lubinska-u10-6

- Các chỉ số rủi ro mục tiêu dưới kịch bản khủng hoảng dầu mỏ khống chế AD ratio ở mức 72% và Delta NII +200bps ở mức 51.7%.
  > "- ■ AD ratio = 72%"
  > "- ■ MTFR contractual = 35%"
  > "- ■ MTFR behavioural = 175%"
  > "- ■ SH\_2M = 156%"
  > "- ■ Delta NII + 200bps = 51.7%"
  > "- ■ Delta NII -200bps = 2.58%."
  > — Chapter 5, lines 4104–4109 ^lubinska-u10-7

- Dưới kịch bản động đất (lãi suất giảm), chi phí huy động vốn ban đầu của Ngân hàng 2 là USD 2.6525 tỷ trong 6 tháng.
  > "Total cost = USD2.6525bn."
  > — Chapter 5, line 4129 ^lubinska-u10-8

- Áp dụng mô hình quyết định dưới kịch bản động đất giúp cắt giảm chi phí vốn thêm USD 0.6496 tỷ trong 6 tháng.
  > "The implementation of the decision model has resulted in a reduction of funding costs over the period of 6 months of USD0.6496bn."
  > — Chapter 5, line 4144 ^lubinska-u10-9

- Sau tối ưu hóa dưới kịch bản thay đổi đặc tính hóa tiền gửi CASA, tổng chi phí vốn giảm về USD 2.1967 tỷ trong 6 tháng.
  > "Total cost = USD2.1967bn."
  > — Chapter 5, line 4210 ^lubinska-u10-10

- Mức cắt giảm chi phí vốn dưới kịch bản thay đổi đặc tính hóa tiền gửi CASA đạt USD 0.6526 tỷ trong 6 tháng.
  > "The implementation of the decision model has resulted in a reduction of funding costs over the period of 6 months of USD0.6526bn ."
  > — Chapter 5, line 4212 ^lubinska-u10-11

- Sau khi áp dụng mô hình dưới kịch bản tính đến CPR tài sản cố định, tổng chi phí vốn giảm về USD 2.1795 tỷ trong 6 tháng.
  > "Total cost = USD2.1795bn."
  > — Chapter 5, line 4282 ^lubinska-u10-12

- Mức cắt giảm chi phí vốn dưới kịch bản tính đến tỷ lệ CPR đạt USD 0.6698 tỷ trong 6 tháng.
  > "The implementation of the decision model has resulted in a reduction of funding costs over the period of 6 months of USD0.6698bn ."
  > — Chapter 5, line 4284 ^lubinska-u10-13

- Khi ngân hàng bị hạ 1 bậc tín nhiệm, chi phí huy động vốn ban đầu tăng vọt lên USD 2.9893 tỷ trong 6 tháng.
  > "Total cost = USD2.9893bn."
  > — Chapter 5, line 4321 ^lubinska-u10-14

- Mô hình tối ưu hóa giúp giảm chi phí vốn dưới kịch bản hạ bậc tín nhiệm xuống USD 2.2439 tỷ trong 6 tháng.
  > "Total cost = USD2.2439bn."
  > — Chapter 5, line 4346 ^lubinska-u10-15

- Dưới kịch bản hạ 1 bậc tín nhiệm, việc tái cấu trúc nợ mang lại mức tiết kiệm chi phí vốn cao nhất toàn chu kỳ đạt USD 0.7455 tỷ trong 6 tháng.
  > "The implementation of the decision model has resulted in a reduction of funding costs over the period of 6 months of USD0.7455bn ."
  > — Chapter 5, line 4352 ^lubinska-u10-16

- Các chỉ số rủi ro mục tiêu dưới kịch bản hạ bậc tín nhiệm duy trì AD ratio ở mức 72%, SH_2M 156% và Delta NII +200bps ở mức 54.26%.
  > "- ■ AD ratio = 72%"
  > "- ■ MTFR contractual = 35%"
  > "- ■ MTFR behavioural = 176%"
  > "- ■ SH\_2M = 156%"
  > "- ■ Delta NII + 200bps = 54.26%"
  > "- ■ Delta NII -200bps = 2.713%."
  > — Chapter 5, lines 4360–4365 ^lubinska-u10-17

- Dưới kịch bản thay đổi tỷ trọng tài sản cố định, mô hình nâng CASA lên 54.9% và cắt giảm nợ cao cấp senior debt về 0.00011%.
  > "- ■ Retail current accounts (CASA) wA = 54.9%"
  > "- ■ TB current accounts wB = 10%"
  > "- ■ Senior debt issuance wC = 0.00011%"
  > "- ■ Corporate time deposits wD1 = 30%"
  > "- ■ Structured deposits wD2 = 3%"
  > "- ■ Commercial papers and certificates of deposits wD3 = 2%."
  > — Chapter 5, lines 4402–4407 ^lubinska-u10-18

### Unit u11 — Bank 2 Funding Side Final Scenarios & Synthesis

- Sau khi áp dụng mô hình quyết định dưới kịch bản thay đổi tỷ trọng tài sản cố định ban đầu, tổng chi phí vốn giảm về USD 1.982 tỷ trong 6 tháng.
  > "Total cost = USD1.982bn."
  > — Chapter 5, line 4418 ^lubinska-u11-1

- Mức cắt giảm chi phí vốn dưới kịch bản thay đổi tỷ trọng tài sản cố định đạt USD 0.8666 tỷ trong chu kỳ 6 tháng.
  > "The implementation of the decision model has resulted in a reduction of funding costs over the period of 6 months of USD0.8666bn ."
  > — Chapter 5, line 4420 ^lubinska-u11-2

- Các chỉ số rủi ro thanh khoản và rủi ro lãi suất mục tiêu dưới kịch bản thay đổi tỷ trọng tài sản cố định: AD ratio đạt 50%, MTFR hành vi đạt 216%, tỷ lệ sống sót SH_2M đạt 247% và Delta NII +200bps đạt 121%.
  > "- ■ AD ratio = 50%"
  > "- ■ MTFR contractual = 39%"
  > "- ■ MTFR behavioural = 216%"
  > "- ■ SH\_2M = 247%"
  > "- ■ Delta NII + 200bps = 121%"
  > "- ■ Delta NII -200bps = 6.08%."
  > — Chapter 5, lines 4432–4437 ^lubinska-u11-3

- Dưới kịch bản thay đổi tỷ trọng tài sản thả nổi ban đầu, tổng chi phí huy động vốn của Ngân hàng 2 ở mức USD 2.8493 tỷ trong 6 tháng.
  > "Total cost = USD2.8493bn."
  > — Chapter 5, line 4457 ^lubinska-u11-4

- Cơ cấu nguồn vốn mục tiêu sau khi áp dụng mô hình quyết định dưới kịch bản thay đổi tỷ trọng tài sản thả nổi: CASA bán lẻ tăng lên 53.23%, tiền gửi kỳ hạn doanh nghiệp 30%, và nợ cao cấp senior debt giảm về 1.77%.
  > "- ■ Retail current accounts (CASA) wA = 53.23%"
  > "- ■ TB current accounts wB = 10%"
  > "- ■ Senior debt issuance wC = 1.77%"
  > "- ■ Corporate time deposits wD1 = 30%"
  > "- ■ Structured deposits wD2 = 3%"
  > "- ■ Commercial papers and certificates of deposits wD3 = 2%."
  > — Chapter 5, lines 4474–4479 ^lubinska-u11-5

- Sau khi áp dụng mô hình quyết định dưới kịch bản thay đổi tỷ trọng tài sản thả nổi, tổng chi phí vốn giảm về USD 2.08 tỷ trong 6 tháng.
  > "Total cost = USD2.08bn."
  > — Chapter 5, line 4490 ^lubinska-u11-6

- Mức cắt giảm chi phí vốn dưới kịch bản thay đổi tỷ trọng tài sản thả nổi đạt USD 0.6526 tỷ trong chu kỳ 6 tháng.
  > "The implementation of the decision model has resulted in a reduction of funding costs over the period of 6 months of USD0.6526bn ."
  > — Chapter 5, line 4492 ^lubinska-u11-7

- Các chỉ số rủi ro mục tiêu dưới kịch bản thay đổi tỷ trọng tài sản thả nổi: AD ratio đạt 63.38%, MTFR hành vi 193%, SH_2M đạt 192% và Delta NII +200bps duy trì ở mức 66%.
  > "- ■ AD ratio = 63.38%"
  > "- ■ MTFR contractual = 35%"
  > "- ■ MTFR behavioural = 193%"
  > "- ■ SH\_2M = 192%"
  > "- ■ Delta NII + 200bps = 66%"
  > "- ■ Delta NII -200bps = 3.30%."
  > — Chapter 5, lines 4504–4509 ^lubinska-u11-8

## Node bị ảnh hưởng
- [[ftp-economic-cost-and-incentive-validation]]
- [[ftp-risk-and-cost-components]]
- [[ftp-cost-benefit-allocation-principles]]
- [[ftp-balance-sheet-optimization]]
- [[internal-risk-transfer]]
- [[practical-alm-liquidity-governance]]
- [[behavioural-options]]
- [[non-maturity-deposits]]
- [[ftp-pricing-methodology]]
- [[balance-sheet-optimisation-model]]
- [[repricing-balance-sheet]]
- [[integrated-alm-liquidity-strategy]]
- [[model-risk-management]]
- [[net-interest-income-sensitivity]]

## Mâu thuẫn ghi nhận
- Không có mâu thuẫn. Các nguyên tắc của Beata Lubinska (Wiley 2020) hoàn toàn tương thích và bổ trợ sâu sắc cho lý thuyết của Moorad Choudhry (Wiley 2022) và thực tiễn ngân hàng Việt Nam.

