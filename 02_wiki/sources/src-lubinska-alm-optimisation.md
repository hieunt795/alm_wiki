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
units_done: [u01, u02, u03, u04, u05, u06, u07, u08, u09, u10, u11]
updated: 2026-10-21
---

## Thông tin nguồn
- Tác giả: Beata Lubinska (Chuyên gia quốc tế về ALM và FTP).
- Sách chuyên khảo: *Asset Liability Management Optimisation: A Practitioner's Guide to Balance Sheet Management and Remodelling* (Wiley Finance, 2020).
- Tier T4 (Tài liệu chuyên khảo quốc tế chuẩn mực cao nhất về thực chiến tối ưu hóa bảng cân đối và định giá điều chuyển vốn FTP).
- Raw: `01_sources/alm book/A - Asset liability optimization.md` (5.055 dòng).
- Units covered:
  - `u01`: Introduction và Chapter 1 — vai trò ALM (reactive → proactive, target profile, margin locked-in/at risk), MMFTP "bank within a bank", hai cách tổ chức ALM, các rủi ro tài chính trên sổ ngân hàng (IRRBB, liquidity, liquidity cost, FX, CSRBB), refinancing/reinvestment risk, intraday early indicators (lines 169–446)
  - `u02`: Chapter 1/2 — Regulatory Requirements Basel III (lịch sử Basel, 3 trụ cột, LCR/NSFR, vốn CRD IV, đòn bẩy), Literature Review (EBA GL IRRBB 2015/2018, Memmel), Ch2 IRRBB Measurement (maturity/repricing/refixing gap, phân loại IRRBB, EVE, PV01, duration gap, ICAAP) (lines 447–957)
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

### Unit u01 — Introduction & Ch1 ALM of the Banking Book (vai trò ALM, MMFTP "bank within a bank", tổ chức ALM, các rủi ro tài chính trên sổ ngân hàng)

- Vai trò ALM chuyển từ cách tiếp cận phản ứng (sổ ngân hàng là cấu trúc thụ động do chiến lược kinh doanh và funding tạo ra) sang chủ động (cấu trúc sổ ngân hàng được quyết định có chủ đích theo cơ cấu mục tiêu).
  > "A clear evolution can be seen as ALM managers realise that a reactive approach, which consists of the management of the banking book as a passive structure resulting from the commercial and funding strategy of a bank, should be replaced by a proactive approach where the banking book structure is decided in a conscious and active way in order to come up with the desired target structure of the banking book."
  > — Introduction, line 171 ^lubinska-u01-1

- Cách quản lý theo silo (tách IRRBB và rủi ro thanh khoản) dẫn tới quyết định chiến lược funding và chiến lược phòng ngừa dưới tối ưu; quy mô và cấu phần đệm thanh khoản thường được quyết định riêng, tác động lên chỉ số IRRBB chỉ được đánh giá sau khi dựng xong đệm.
  > "The silo-based approach consists of separated management of financial risks, in particular interest rate risk in the banking book and liquidity risk. The consequence of this is taking suboptimal decisions regarding the funding strategy (and consequently liquidity and funding risk) and suboptimal hedging strategies"
  > "Quite often the size and components of the liquidity buffer (also within the responsibilities of the treasury department) are decided separately and the impact on IRRBB metrics is assessed only after the whole process of building the liquidity buffer is already finalised."
  > — Introduction, lines 177–179 ^lubinska-u01-2

- Target position (target profile) là cơ cấu tài sản và nợ để lợi nhuận sổ ngân hàng đạt tối đa, có tính tới các ràng buộc quản lý và rủi ro nội bộ.
  > "Herein, the target profile means the definition of a composition of assets and liabilities so that the profitability of the banking book reaches its maximum, taking into account a number of regulatory and internal risk constraints."
  > — Introduction, line 183 ^lubinska-u01-3

- Margin locked in là biên của ALM đã kết tinh và được phân bổ; margin at risk là biên còn bất định do vị thế chịu rủi ro lãi suất. Ví dụ: khoản vay cố định (customer rate 3,50%, FTP base rate 2,00%, FTP liquidity spread 0,50%) tài trợ bằng FRN 3 tháng; margin ALM locked-in từ rủi ro lãi suất 0,75%, margin at risk 1% khi EURIBOR 3M giảm 25 bps (1,25% xuống 1%); margin locked-in từ thanh khoản 0,25%; tổng NIM tới 31/3/2019 là 1% (0,75% + 0,25%), giao cho ALM book trong Treasury.
  > "If this margin is already crystallised and attributed, we call it margin locked in . If there is uncertainty about the future spread because the position, at some point of time, is exposed to the risk of changes in interest rates, we call it margin at risk ."
  > "Repayment type: bullet Next (capital) payment date: 31/12/2019 Next repricing date: 31/12/2019 Customer Rate: 3.50% FTP Base Rate: 2.00% FTP Liquidity Spread: 0.50%"
  > "As regards the profitability of this position, due to the interest rate risk component, the locked-in ALM margin is equal to 0.75%, while the ALM margin at risk is equal to 1% under the assumption of a decrease in EURIBOR 3 M by 25 bps (from 1.25% to 1%)."
  > "The ALM locked-in margin deriving from this position is equal to 0.25% (the difference between the liquidity spread of the asset and the liability)."
  > "Consequently, the total net interest margin in the period until 31 March 2019 is equal to 1% (0.75% + 0.25%) and will be assigned to the ALM book within the treasury department."
  > — Introduction, lines 187–221 ^lubinska-u01-4

- ALM theo định nghĩa thông dụng là quản lý cấu trúc bảng cân đối với hai mục tiêu: giữ rủi ro trong giới hạn của risk bearing capacity, và sinh lời trên vốn dùng cho rủi ro sổ ngân hàng. ALCO đặt mục tiêu; mỗi ngân hàng có khẩu vị rủi ro khác nhau, có ngân hàng chọn riding the yield curve (tài trợ tài sản cố định bằng nợ thả nổi), có ngân hàng chọn immunisation.
  > "Under the common definition, Asset Liability Management (ALM) means the management of the balance sheet structure with two main objectives:"
  > "to keep risks within the limits of risk bearing capacity;"
  > "to earn on the capital utilised for banking book risks."
  > "For example, some banks are willing to take on more exposure in terms of riding the yield curve strategy through funding fixed rate assets with floating rate liabilities. Other banks opt for an immunisation strategy."
  > — Chapter 1, lines 269–274 ^lubinska-u01-5

- Theo tác giả, sau khủng hoảng 2008 ALM có thêm mục tiêu xác định cơ cấu funding rẻ nhất để tối ưu nguồn lực như thanh khoản và hỗ trợ mô hình kinh doanh.
  > "In my view, ALM also has another important objective which gained attention quite recently, i.e. after the financial crisis of 2008. It consists of the determination of the cheapest funding structure for the bank in order to optimise its resources, such as liquidity, and support the business model of the bank."
  > — Chapter 1, line 278 ^lubinska-u01-6

- ALM là "bank within a bank": ALM thu FTP rate của asset centre và ghi có FTP rate cho liability centre; nhờ đó rủi ro lãi suất và rủi ro funding được tách khỏi business unit và chuyển về ALM.
  > "ALMcharges the asset centre (the business unit responsible for delivering products to clients who intend to borrow from the bank, for example credit cards, mortgages, commercial loans) the FTP rate and recognises the FTP rate to the liability centre"
  > "In doing so, the financial risks (interest rate risk and funding risk) are stripped off the business unit and transferred to ALM to manage. This is why it adopts this 'bank within the bank' role."
  > — Chapter 1, line 282 ^lubinska-u01-7

- Một số rủi ro không chuyển ra thị trường qua phái sinh và quản lý trong ALM được, do FTP thiết lập sai (phương pháp hoặc dựng đường cong không đúng) hoặc thị trường phái sinh kém thanh khoản ở một số nơi, đồng tiền. Rủi ro tín dụng theo định nghĩa không chuyển về ALM.
  > "However, it must be noted that some of risks specific to the bank cannot be transferred to the financial market through derivatives and managed within ALM. This can be driven either by inappropriate FTP set up in the bank (incorrect methodologies or"
  > "curve construct) or an illiquid derivatives market in certain locations or currencies. By definition, credit risk cannot be transferred to ALM either."
  > "Thus, ALM is defined as the management of balance sheet risks with financial instruments; however, not all balance sheet risks can be managed within ALM and ALCO."
  > — Chapter 1, lines 284–292 ^lubinska-u01-8

- Các rủi ro do ALM quản lý: IRRBB (giảm thu nhập lãi và giảm giá trị thị trường, nên khái niệm, báo cáo, hạn mức phải phản ánh cả hai góc nhìn), liquidity risk, liquidity cost risk, FX risk, CSRBB. IRRBB, CSRBB, FX được giới hạn trong ICAAP; liquidity risk và funding cost risk thuộc ILAAP.
  > "Interest Rate Risk in the Banking Book (IRRBB) - the risk of reduction of interest income through unfavourable interest rate movements. It is also the risk of reduction in market value of the interest rate risk position. ALM management concepts, reporting, and limits have to reflect this dual view."
  > "Liquidity Risk - risk of insufficient funds resulting in illiquidity. This risk is managed by keeping liquidity buffers that can be turned into liquidity in the case of stress."
  > "Liquidity Cost Risk - risk of the reduction of interest income (or mark to market value) through an increase in liquidity cost (funding spread)."
  > "Credit Spread Risk in the Banking Book (CSRBB) - mark to market losses from spread variations in the bond and derivatives portfolio."
  > "IRRBB, CSRBB, and FX risks in ALM are limited within the Internal Capital Adequacy Assessment Process (ICAAP) by decisions of the Management and Supervisory Board (Risk Strategy); meanwhile, the Liquidity Risk and Funding Cost Risk are covered by the Internal Liquidity Adequacy Assessment (ILAAP)."
  > — Chapter 1, lines 300–306 ^lubinska-u01-9

- Hai cách tổ chức ALM. (1) ALM thuộc khối thị trường: treasurer dự báo lãi suất và định vị sổ ngân hàng (directional GAP, không phải trading); ALM có earnings budget, gọi là business unit model. (2) ALM thuộc khối phi thị trường (Finance, Risk): không tự mở vị thế, không có quyền tiếp cận thị trường, giao dịch phải giao cho đơn vị thị trường thực hiện; phổ biến khi chiến lược IRRBB là immunisation.
  > "ALM is a part of the Market Organisation (Financial Markets, Capital Markets, and Treasury). The ALM committee, headed by the respective board members, decides on risk positioning and the ALM department manages the positions within operative limits for daily management on its own."
  > "This technique is known as directional GAP (Figure 1.2 and Figure 1.3) and has nothing to do with trading (selling or buying positions at short term with the aim of making a profit)."
  > "In both cases ALM will have an earnings budget to fulfil; this setting is commonly known as a business unit model."
  > "ALM is a part of the Non-Market Organisation (Finance, Risk) and, in this case, ALMis not allowed to enter risk positions by itself."
  > "In addition, the ALM department must not have market access; therefore, the deals have to be handed over to some market unit for execution. This set-up is common in cases where the IRRBB strategy of a bank pursues an immunisation strategy."
  > — Chapter 1, lines 310–330 ^lubinska-u01-10

- Quy trình FTP là tập chính sách và phương pháp tách kết quả giao dịch thành customer contribution và risk contribution, chuyển rủi ro ALM (lãi suất và thanh khoản) từ business unit về ALM; FTP cũng là công cụ quản lý bảng cân đối để thực hiện chiến lược.
  > "The FTP process is a sum of policies and methodologies which separates the results of a transaction into the customer contribution and risk contribution and transfers the ALM risks (interest rate risk and liquidity risk) from business units to ALM to be managed. Additionally, FTP is an important balance sheet management tool to deliver a bank's strategy, and a robust FTP framework enables it to achieve the steering and control needed to attain strategic balance sheet goals."
  > — Chapter 1, line 332 ^lubinska-u01-11

- Matched Maturity FTP (MMFTP) theo nguyên tắc opportunity cost: chi phí phòng ngừa rủi ro của giao dịch được định ở giá thị trường, dù phòng ngừa có thực hiện hay không; mỗi giao dịch được giả định là đã được phòng ngừa. Giữa BU và ALM không có phòng ngừa thật mà là hedge "giả định" (fictitious); BU chỉ còn quản lý quan hệ khách hàng và commercial spread.
  > "Matched Maturity Funds Transfer Pricing (MMFTP) follows the opportunity cost principle - defining the cost of hedging risk inherent in the transaction at financial market prices and independently of whether the hedging will really take place or not. FTP separates the customer from risk business: the application of Funds Transfer Prices for each single transaction assumes that every deal will be hedged against risk."
  > "There is no real hedging between the business unit and ALM department (there is the 'fictitious' hedge instead)"
  > "The only risk the business has to manage is its relationship with the external client and the magnitude of the commercial spread which is gained through the deal."
  > — Chapter 1, lines 334–336 ^lubinska-u01-12

- ALM huy động vốn từ thị trường hoặc liability centre với đặc tính không nhất thiết khớp vốn cấp cho asset centre, nên còn lại chênh lệch kỳ hạn và lãi suất; treasurer tách chênh lệch này thành tài khoản rủi ro lãi suất (IRRM) và tài khoản thanh khoản, rồi quyết định phòng ngừa bằng phái sinh hay để mở.
  > "The financial characteristics of funds do not necessarily mirror the characteristics of those provided to the asset centre; consequently, ALM is left with a mismatch in terms of funds maturity and interest rate. The treasurer manages this inherited mismatching through a split between interest rate risk account (IRRM) and liquidity account. Then, they decide whether to mitigate the open exposure through derivatives (in our example, interest rate swaps) or to leave it 'open', hoping that the market will not turn against it."
  > — Chapter 1, line 344 ^lubinska-u01-13

- Ví dụ khoản vay cố định 5 năm: treasurer có 3 lựa chọn. (a) payer swap 5Y, trái phiếu 5Y, receiver swap 5Y: đóng mọi rủi ro; (b) payer swap 5Y, trái phiếu 3Y, receiver swap 3Y: đóng rủi ro lãi suất, mở rủi ro thanh khoản; (c) payer swap 3Y, trái phiếu 5Y, receiver swap 5Y: đóng rủi ro thanh khoản, rủi ro lãi suất chưa phòng ngừa hết.
  > "enter the 5-year payer swap (m = 5Y), issue the 5-year coupon bond to fund the asset and enter the 5-year receiver swap (n = 5Y);"
  > "enter the 5-year payer swap (m = 5Y), issue the 3-year coupon bond to fund the asset and enter the 3-year receiver swap (n = 3Y); or"
  > "enter the 3-year payer swap (m = 3Y), issue the 5-year coupon bond and enter the 5-year receiver swap (n = 5Y)."
  > "In the first strategy, all risks are closed, as both maturity of funds (coupon bond) and rate tenor (payer swap) match the characteristics of funds provided to the external client. In the second case, the exposure to interest rate risk is closed (the tenor of the payer swap is the same as that of the originated loan) but liquidity risk remains open (maturity of coupon bond is shorter than originated loan). In the third case, the liquidity risk is closed, and interest rate risk remains not fully hedged."
  > — Chapter 1, lines 346–355 ^lubinska-u01-14

- Nhờ FTP, customer margin không đổi suốt vòng đời sản phẩm, bất kể lãi suất, chi phí thanh khoản hay tỷ giá; tách customer business khỏi risk business là điều kiện tiên quyết của target operating model FTP và tuân thủ quy định.
  > "Through the application of the FTP process, the customer margin remains constant during the whole product life, independently from interest movements, higher liquidity cost, or changing currency prices."
  > "Also, the separation of risk and customer business is a precondition to the sound target operating model within FTP and being compliant with the regulatory requirements."
  > — Chapter 1, line 359 ^lubinska-u01-15

- Từ góc nhìn ALM, quy trình FTP gom vốn từ liability centre ở FTP rate và cho asset centre vay ở FTP rate; maturity transformation do ALM quản lý. Lợi nhuận asset centre và liability centre đo bằng chênh lệch giá sản phẩm bên ngoài và FTP rate. Ví dụ: asset centre +2,69%, liability centre −0,68% (chi phí vốn bên ngoài cao hơn FTP rate), ALM +0,99% từ chuyển hoá kỳ hạn và lãi suất.
  > "As a result of this process, the maturity transformation run by the bank is managed by ALM and generates profitability for the bank. On the other hand, the profitability of the asset centre and liability centre is assessed through the difference between the external product price and FTP rate, i.e. the concept of external asset yield and external liability cost."
  > "The profitability (P&amp;L impact) of the asset centre is equal to 2.69% (the difference between the external asset rate and FTP rate); meanwhile, the profitability of the liability centre and ALM are equal to -0.68% and 0.99% respectively. There is a loss in the liability centre because the external cost of funds is higher than the FTP rate recognised by ALM."
  > — Chapter 1, lines 361–367 ^lubinska-u01-16

- Ví dụ IRRBB hai góc nhìn: ngân hàng có trái phiếu cố định và mortgage dài tài trợ bằng CASA, chỉ đặt hạn mức ΔNII, không có hạn mức ΔEVE; treasurer chờ lãi suất tăng nên giữ tiền mặt, nhưng lãi suất giảm. ΔNII lỗ, prepayment tăng làm duration tài sản ngắn lại, ngân hàng thành net liability ở đoạn trung dài và chịu lỗ ΔEVE không được đo bằng chỉ số chính thức nào.
  > "The bank chose as its objective variable the change in the Net Interest Income (herein Δ NII) and does not have any formal limit on the change in the economic value of equity ( Δ EVE)."
  > "The combination of increased prepayments with maturing (and not reinvested) bonds causes shortening of the total duration of the assets portfolio and opens the structural mismatching."
  > "The biggest problem here is that the treasurer drives banking book exposure based on only one IRRBB metric which aims to measure changes in NII under the short-term horizon and does not monitor the structural risk which is becoming a problem for the bank. If Δ EVE metrics were in place, the treasurer would probably breach the limit at some point and would be forced to increase the duration of the asset portfolio through deployment of cash."
  > — Chapter 1, lines 384–388 ^lubinska-u01-17

- Chênh lệch lãi suất tạo refinancing risk (kỳ hạn nợ ngắn hơn tài sản; lãi suất tăng làm giảm NII) và reinvestment risk (kỳ hạn tài sản ngắn hơn nợ; lãi suất giảm buộc tái đầu tư ở mức thấp hơn). Với khoản thả nổi, nếu kỳ refix của tài sản ngắn hơn của nợ thì ngân hàng vẫn chịu reinvestment risk dù kỳ hạn hợp đồng của tài sản dài hơn.
  > "Refinancing risk arises when the maturity of liabilities is shorter than the maturity of assets."
  > "Reinvestment risk arises when maturity of assets is shorter than liabilities."
  > "If the refixing period of assets is shorter than the refixing period of liabilities, the bank is still exposed to the reinvestment risk and consequently to the downward movement of the curve, even if the contractual maturity of this asset is longer than the maturity of liability."
  > — Chapter 1, lines 397–400 ^lubinska-u01-18

- Liquidity cost risk là rủi ro chi phí thanh khoản tăng mà không mất khả năng thanh toán; đây là rủi ro thị trường tương tự rủi ro lãi suất, làm giảm vốn (lợi nhuận) qua chi phí tái tài trợ tăng.
  > "Liquidity Cost Risk, which means an increase in liquidity costs without being exposed to illiquidity, is a market risk comparable to the interest rate risk. Increased liquidity costs reduce a bank's capital (profit) through increased cost of refinancing (Enthofer and Haas 2016)."
  > — Chapter 1, line 408 ^lubinska-u01-19

- Liquidity cost risk là một phần của ICAAP và phải được đo, giới hạn. Đo theo 3 góc nhìn do cơ quan quản lý định trong Trụ cột 2 ICAAP: going concern, gone concern, stress. Cách tính thông dụng: refinance các gap âm tích luỹ với giả định liquidity spread tăng, có thể lấy biến động credit spread theo holding period làm cơ sở; hoặc dùng Liquidity VaR có xét biến động và tương quan spread.
  > "The liquidity cost risk is part of Internal Capital Adequacy Assessment Process (ICAAP). The ICAAP assesses risk arising from the increase of liquidity costs, which impacts the bank's P&amp;L and therefore their own funds. This kind of risk must be measured and limited, ensuring the preservation of the bank's capital."
  > "This is done in three different views that are predetermined by the regulator in pillar 2 of the ICAAP, i.e. normal situation (going concern), liquidation (gone concern), and stress scenario."
  > "Generally, to calculate the liquidity cost risk, the negative cumulative gaps are refinanced under the assumption of an increased liquidity spread. As a base for the spread, the credit spread volatility per holding period can be used. Another way of calculating the liquidity risk is the use of the Value at Risk approach (Liquidity VaR) that considers spread volatility and correlations."
  > — Chapter 1, lines 429–431 ^lubinska-u01-20

- Liquidity risk (refinancing risk) là thiếu nguồn tái tài trợ để đáp ứng nghĩa vụ; phát sinh khi kỳ cam kết vốn phía tài sản dài hơn phía nợ (maturity transformation). Vị thế được thể hiện trên maturity ladder; quản lý thanh khoản phải bảo đảm nguồn funding đa dạng theo kỳ hạn.
  > "Liquidity Risk (Refinancing Risk), which means the lack of sources for the refinancing of the bank, needed to meet the obligations."
  > "Liquidity risk, therefore, occurs when the capital commitment on the assets side is longer than the capital commitment for liabilities - so-called maturity transformation, which represents a fundamental bank function."
  > "Therefore, the liquidity management process must ensure that a firm has access to diversified sources of funding in an appropriate range of tenors."
  > — Chapter 1, lines 404–410 ^lubinska-u01-21

- Quy trình intraday liquidity nên cho phép tính dòng vào, dòng ra gộp hằng ngày và dự báo thiếu hụt ròng trong ngày; nên có chỉ báo sớm cho trạng thái stress. Danh sách 12 chỉ báo:
  > "The intraday liquidity process should allow banks to calculate daily gross inflows and outflows and forecast the range of potential net funding shortfalls that may occur during the day. In order to appropriately monitor the intraday liquidity, early indicators should be put in place, indicating the stress conditions of the bank."
  > "Rapid asset growth, especially when funded with potential volatile liabilities."
  > "Growing concentrations in assets and liabilities."
  > "An increase in currency mismatching."
  > "A decrease of weighted average maturities of liabilities."
  > "A credit rating downgrade."
  > "Declining stock prices."
  > "Widening debt or credit default swaps."
  > "Increasing retail deposit outflow."
  > "Increasing redemptions of corporate deposits (CDs) before maturity."
  > "Counterparties that begin to request additional collateral for credit exposure."
  > "Correspondent banks that eliminate or decrease their credit lines."
  > "Difficulty placing short-term liabilities (commercial papers)."
  > — Chapter 1, lines 412–425 ^lubinska-u01-22

- CSRBB là rủi ro mất giá trị do credit spread thay đổi khi xếp hạng đối tác không đổi; Basel III/CRD IV/CRR yêu cầu đo riêng trong ICAAP; cơ quan quản lý đòi đo cho cả trading book và banking book. CSRBB được coi là rủi ro thị trường, đo bằng VaR; khi thiếu dữ liệu dùng benchmark theo nhóm trái phiếu, hoặc lấy spread từ CDS, chỉ số. Ngân hàng bị buộc tách kết quả danh mục trái phiếu thành phần credit spread và phần lãi suất.
  > "The credit spread risk represents the risk of a value loss which is caused by changes in credit spreads while the counterparty's rating remains the same."
  > "In recent years, however, the regulator has been demanding the measurement of the spread risk for both trading and banking book (Enthofer and Haas 2016)."
  > "Credit spread risk is seen as market risk, and for this reason, the common market risk measurement techniques apply here also. The VaR is the methodological approach followed in quantification of the credit spread risk."
  > "In such cases, the benchmark approaches are followed, i.e. a group of bonds for each asset class/credit rating."
  > "This situation is currently changing, as the regulator and the transparency principle within ALM results forced banks to split the total bond portfolio result into a separate credit spread and interest risk result."
  > — Chapter 1, lines 441–445 ^lubinska-u01-23

#### Ghi chú convert u01
- Figure 1.1–1.5 và Figure I.1–I.3 chỉ có ảnh (`<!-- image -->`); thông số Figure I.1 còn lại một dòng code block (dòng 194).
- Dòng 1–168 là bìa, bản quyền, mục lục, lời nói đầu, giới thiệu tác giả: không trích.


### Unit u02 — Regulatory Requirements Basel III, Literature Review & Ch2 IRRBB Measurement (gap, EVE, PV01, duration gap, ICAAP)

- Lịch sử Basel: Basel I có hiệu lực 1988, chỉ cho rủi ro tín dụng; quy định rủi ro thị trường bổ sung năm 1996; Basel II áp dụng từ 01/2007 (2008 với phương pháp nâng cao) đến 2013; Basel III được thống nhất 2010–2011, dự kiến áp dụng 2013–2015, sau đó gia hạn đến 31/3/2018 rồi 31/3/2019. Phạm vi của Uỷ ban vượt ra ngoài an toàn vốn: rủi ro lãi suất, thanh khoản, stress test.
  > "Since the financial crisis in 2008, the business of banks has been heavily discussed and regulators have taken serious steps to reduce systemic and economic risks coming from the banking sector. The global standard for capital is a relatively recent innovation. Basel I came into force in 1988 and was related only to credit risk. Before then, there were no standardised rules on capital adequacy for banks. In 1996, market risk rules were added. In December 1998, the BCBS recognised that Basel I needed to be revised to reflect credit risk more effectively and to prevent increasing use of arbitrage by the banks, which were using more and more sophisticated internal models to measure and understand risk. The Committee also decided to recommend a capital charge for operational risk. Basel II was born and took five years to be developed and then a further four years to be implemented. Basel II was in place from January 2007 (or 2008 for those on the advanced approaches under Basel II) to 2013. Basel III was agreed by the members of the Basel Committee on Banking Supervision in 2010-2011, and was scheduled to be introduced from 2013 until 2015; however, changes from 1 April 2013 extended implementation until 31 March 2018 and then again to 31 March 2019. The Basel Committee's remit extends a long way beyond capital adequacy. Its other global standards and consultations include interest rate risk, liquidity risk, stress testing, risk management, and alignment of risk and reward."
  > — Chapter 1, line 449 ^lubinska-u02-1

- Basel II có ba trụ cột (yêu cầu vốn tối thiểu, giám sát, kỷ luật thị trường), gắn vốn kinh tế với vốn quy định chặt hơn Basel I. Kết luận của Uỷ ban Basel không có hiệu lực pháp lý; mỗi cơ quan quản lý thực thi qua quy định quốc gia; ngay trong EU (CRD IV) vẫn có khác biệt khi diễn giải và thực thi.
  > "The cornerstone of the Basel II rules was, as already mentioned, the three-pillar approach. These are minimum capital requirements, the supervisory review, and market discipline. The idea under pillar 1 was to create a closer link between economic and regulatory capital through a more tailored regime with more specific targeting of individual credits rather than the broad-brush approach of Basel I which targeted whole asset classes. The clear example of this point was the treatment of corporate loans regardless of their credit quality, which under Basel I all received 100% risk-weighting. Basel II provided the distinction according to their credit quality."
  > "However, it is important to highlight that the Committee conclusions and recommendations do not have legal force - its role is to formulate supervisory standards and guidelines. It recommends best practice that individual authorities are supposed to implement through detailed national arrangements which are best suited to their own national systems. The Committee encourages convergence towards common approaches and standards without attempting detailed harmonisation of member countries. Even in the EU, where Basel III is enshrined in version four of the Capital Requirements Directive (CRD), there are differences in national interpretation and implementation."
  > — Chapter 1, line 453 ^lubinska-u02-2

- Bộ khuyến nghị Basel III ban hành 12/2010 (sửa 6/2011); để thực thi ở EU, 6/2013 ban hành CRD IV (Chỉ thị 2013/36/EU, hiệu lực 01/01/2014) và CRR (Quy định (EU) 575/2013).
  > "Basel III's main set of recommendations were issued by the Basel Committee on Banking Supervision (BCBS) in December 2010 (revised June 2011) and titled Basel III: A Global Regulatory Framework for More Resilient Banks and Banking Systems . With a view to implementing the agreements of Basel III and harmonising banking solvency regulations across the European Union as a whole, in June 2013 the European Parliament and the Council of the European Union adopted the following legislation:"
  > "Capital Requirements Directive 2013/36/EU (hereinafter CRD IV) on access to the activity of credit institutions and the prudential supervision of credit institutions and investment firms. CRD IV entered into the force in the EU on 1 January 2014."
  > "Regulation (EU) No 575/2013 of the European Parliament and of the Council of 26 June 2013 on prudential requirements for credit institutions and investment firms (hereinafter CRR)."
  > — Chapter 1, line 459 ^lubinska-u02-3

- Ba trụ cột của khung an toàn vốn: Trụ cột 1 yêu cầu vốn tối thiểu cho rủi ro tín dụng, thị trường, hoạt động; Trụ cột 2 (SREP) xét vốn bổ sung cho rủi ro ngoài Trụ cột 1, trong đó ICAAP là tự đánh giá của ngân hàng; Trụ cột 3 công bố thông tin.
  > "The capital adequacy framework consists of three pillars, each of which focus on different aspects of capital adequacy:"
  > "Pillar 1, called 'Minimum Capital Requirements', establishes the minimum amount of capital that a bank should have against its credit, market, and operational risks. It provides the guidelines for calculating the risk exposures in the assets of a bank's balance sheet (the 'risk weighted assets' and the components and sets the minimum capital requirements."
  > "Pillar 2, called 'Supervisory Review and Evaluation Process' involves both banks and regulators taking a view on whether a firm should hold additional capital against risks not covered in Pillar 1. Part of the Pillar 2 process is the 'Internal Capital Adequacy Assessment Process' (ICAAP), which is a bank's self-assessment of risks not captured by Pillar 1."
  > "Pillar 3, called 'Market Discipline', aims to encourage market discipline by requiring banks to disclose specific, prescribed details of their risks, capital, and risk management."
  > — Chapter 1, line 464 ^lubinska-u02-4

- BCBS chốt LCR tháng 1/2013, ngân hàng tuân thủ từ kỳ báo cáo đầu tiên sau 01/01/2015. LCR nhằm bảo đảm đủ HQLA không bị cầm cố để vượt qua kịch bản căng thẳng 30 ngày; NSFR nhằm giảm rủi ro nguồn vốn trong dài hạn.
  > "In January 2013, the BCBS agreed the final form of the Liquidity Coverage Ratio. These requirements aim to improve the transparency of regulatory liquidity requirements and enhance market discipline. Consistent with the Basel III agreement, national authorities gave effect to these disclosure requirements, and banks are required to comply with them, from the date of the first reporting period after 1 January 2015. These standards aim to achieve two separate but complementary objectives. The first objective is to promote short-term resilience of a bank's liquidity risk profile while ensuring that it has sufficient high-quality liquid assets (HQLA) to survive a significant stress scenario lasting for 30 days. To this end, the Committee published Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools. The second objective is to reduce funding risk over a longer time horizon by requiring banks to fund their activities with sufficiently stable sources of funding in order to mitigate the risk of future funding stress. To achieve this objective, the Committee published Basel III: The Net Stable Funding Ratio. These standards are an essential component of the set of reforms introduced by Basel III and together will increase banks' resilience to liquidity shocks, promote a more stable funding profile, and enhance overall liquidity risk management (Lekatis 2014)."
  > "As stated above, the Liquidity Coverage Ratio aims to ensure that a bank has an adequate stock of unencumbered HQLA to meet its liquidity needs for a 30-calendar day liquidity stress scenario. HQLA consists of cash or assets that can be converted into cash at little or no loss of value in private markets. At a minimum, the stock of unencumbered HQLA should enable the bank to survive until day 30 of the stress scenario, by which time it is assumed that appropriate corrective actions can be taken by management and supervisors or that the bank can be resolved in an orderly way."
  > — Chapter 1, line 471 ^lubinska-u02-5

- Có hai cấp tài sản trong HQLA: Level 1 không giới hạn, Level 2 tối đa 40% tổng dự trữ và chịu haircut; nguồn liệt kê tài sản Level 1 (tiền mặt, dự trữ tại NHTW, chứng khoán chính phủ, NHTW, PSE, BIS, IMF, ECB, MDB đủ điều kiện) và Level 2 (chứng khoán chính phủ đủ điều kiện, trái phiếu doanh nghiệp, covered bond, RMBS, cổ phiếu phổ thông đủ điều kiện).
  > "There are two categories of assets that can be included in the stock. Assets to be included in each category are those that the bank is holding on the first day of the stress period, irrespective of their residual maturity. 'Level 1' assets can be included without limit, while 'Level 2' assets can only comprise up to 40% of the stock (Ahmed 2015)."
  > "Level 1 assets are limited to:"
  > "coins and banknotes;"
  > "central bank reserves;"
  > "marketable securities representing claims on or guaranteed by sovereigns, central banks, PSEs, the Bank for International Settlements, the International Monetary Fund, the European Central Bank and European Community, or multilateral development banks which satisfy prescribed by Basel III conditions."
  > "Level 2 assets comprise:"
  > "marketable securities representing claims on or guaranteed by sovereigns, central banks, PSEs, or multilateral development banks which satisfy prescribed by Basel III conditions;"
  > "corporate debt securities (including commercial paper) and covered bonds which satisfy prescribed by Basel III conditions;"
  > "residential mortgage back securities (RMBS) that satisfy prescribed conditions;"
  > "common equity shares that satisfy prescribed conditions."
  > "Certain additional assets may be included in Level 2 at the discretion of national authorities. In addition, the Level 2 assets are subject to a haircut in the market value of those assets."
  > — Chapter 1, line 477 ^lubinska-u02-6

- Tổng dòng tiền ra ròng là dòng ra kỳ vọng trừ dòng vào kỳ vọng trong 30 ngày; dòng ra bằng số dư nhân tỷ lệ run-off/rút vốn, dòng vào bị giới hạn ở 75% tổng dòng ra.
  > "The term total net cash outflows - in the denominator of the liquidity coverage ratio (LCR) equation - is defined as the total expected cash outflows minus total expected cash inflows in the specified stress scenario for the subsequent 30 calendar days. Total expected cash outflows are calculated by multiplying the outstanding balances of various categories or types of liabilities and off-balance sheet commitments by the rates at which they are expected to run off or be drawn down. Total expected cash inflows are calculated by multiplying the outstanding balances of various categories of contractual receivables by the rates at which they are expected to flow in under the scenario up to an aggregate cap of 75% of total expected cash outflows (BCBS January 2013)."
  > — Chapter 1, line 495 ^lubinska-u02-7

- Công cụ giám sát thanh khoản ngoài LCR: chênh lệch kỳ hạn hợp đồng, tập trung nguồn vốn (theo đối tác, sản phẩm quan trọng so với tổng nợ, theo đồng tiền), tài sản không bị cầm cố, LCR theo đồng tiền quan trọng, công cụ theo thị trường.
  > "In addition to LCR, there are monitoring tool metrics which provide the cornerstone of information that aids supervisors in assessing the liquidity risk of a bank. These metrics include the following:"
  > "Contractual maturity mismatch - represents contractual cash and security inflows and outflows from all on- and off-balance sheet items, mapped to defined time bands based on their respective maturities,"
  > "Concentration of funding - includes the reporting of funding liabilities sourced from each significant counterparty as a percentage of total liabilities, funding liabilities sourced from each significant product/instrument as a percentage of total liabilities, and the list of asset and liability amounts by significant currency."
  > "Available unencumbered assets - represents available unencumbered assets that are marketable as collateral in secondary markets and available unencumbered assets that are eligible for central banks' standing facilities."
  > "LCR by significant currency - calculated as foreign currency LCR which is equal to the stock of HQLA in each significant currency divided by total net cash outflows over a 30-day time period in each significant currency."
  > "Market-related monitoring tools."
  > — Chapter 1, line 497 ^lubinska-u02-8

- NSFR là ASF chia RSF, phải đạt ít nhất 100% liên tục, nhằm hạn chế phụ thuộc vốn bán buôn ngắn hạn. ASF dựa trên độ ổn định của nguồn vốn (kỳ hạn hợp đồng, xu hướng rút vốn; quyền chọn mua giả định thực hiện sớm nhất); RSF bằng hệ số RSF nhân giá trị ghi sổ tài sản, xấp xỉ phần tài sản phải tài trợ trong một năm; một số yếu tố thuộc quyết định quốc gia.
  > "The Net Stable Funding ratio is another initiative of the Basel Committee to promote a more resilient banking sector. It requires banks to maintain a stable funding profile in relation to the composition of their balance sheet. As a consequence, it limits overreliance on the short-term wholesale funding and promotes funding stability. The problems related to the excessive maturity transformation run by financial institutions arose during the financial crisis in 2007 when most banks experienced difficulties coming from improper liquidity management and framework."
  > "The NSFR is defined as amount of available stable funding relative to the amount of required stable funding. The ratio should be equal at least 100% on an ongoing basis. The NSFR is calculated through the following equation:"
  > "The amount of available stable funding (ASF) is measured based on the broad characteristics of the relative stability of the institution's funding resources, including contractual maturity of its liabilities and the difference in the propensity of different types of funding providers to withdraw their funding. When determining the maturity of an equity or liability instrument, investors are assumed to redeem the call option at the earliest possible date. Instead, the amount of required stable funding (RSF) is measured based on the broad characteristics of the liquidity risk profile of an institution's assets and off-balance sheet (OBS) exposures. The amount of required stable funding is calculated through the application of the RSF factor to the carrying value of assets to the categories prescribed by the BCBS. The RSF factors assigned to various types of assets are intended to approximate the amount of assets that would have to be funded, either because it will roll over or because it could not be monetised through sale or used as collateral in a secured borrowed transaction over the course of one year without significant expense (BCBS 2014). It is important to highlight that it consists of internationally agreed calibrations and definitions. Some elements, however, remain subject to national discretion."
  > — Chapter 1, line 505 ^lubinska-u02-9

- Hiệu chỉnh NSFR theo hai chiều cho nợ (kỳ hạn dài ổn định hơn; tiền gửi bán lẻ và doanh nghiệp nhỏ ổn định hơn bán buôn cùng kỳ hạn) và bốn tiêu chí cho RSF (duy trì tín dụng, hành vi ngân hàng tái cấp vốn khoản vay đáo hạn, kỳ hạn tài sản dưới 1 năm cần ít vốn ổn định hơn, chất lượng và tính thanh khoản tài sản); một phần nhỏ vốn ổn định cho cam kết ngoại bảng.
  > "The calibration reflects the stability of liabilities across two dimensions:"
  > "1. Funding tenor - the NSFR is calibrated so that longer-term liabilities are assumed to be more stable than short-term liabilities."
  > "2. Funding type and counterparty - short-term deposits provided by retail customers and funding provided by small business customers are behaviourally more stable than wholesale funding of the same maturity from other counterparties."
  > "With reference to RSF for various assets, the following criteria have been taken into account:"
  > "1. Resilient credit creation - some portion of lending needs to be financed by stable funding to ensure the continuity of intermediation and business."
  > "2. Bank behaviour - the bank may seek to roll over a significant portion of the maturing loans to preserve the customer relationships."
  > "3. Asset tenor - short-term dated assets (maturing in less than 1 year) require a smaller portion of stable funding because banks would be able to allow some portion of those assets to mature instead of rolling them over."
  > "4. Asset quality and liquidity value - the unencumbered, high-quality assets that can be securitised or traded and can be readily used as collateral to secure addition funding or sold in the market do not need to be fully funded with stable funding."
  > "Additionally, a small part of stable funding is required to support at least a small portion of the potential calls on liquidity arising from off-balance sheet commitments and contingent funding obligations (BCBS 2014)."
  > — Chapter 1, line 513 ^lubinska-u02-10

- Theo Basel III/CRR/CRD IV, từ 01/01/2019 (hết chuyển tiếp): CET1 tối thiểu 7% (4,5% tối thiểu + 2,5% đệm bảo toàn vốn), Tier 1 tối thiểu 8,5%, tổng vốn 10,5%; tối thiểu không gồm đệm bảo toàn vẫn là 8% như Basel II; đệm phản chu kỳ 0%–2,5%; bỏ Tier 3; đệm rủi ro hệ thống và đệm tổ chức quan trọng xác định từng trường hợp; cộng yêu cầu Trụ cột 2 (SREP), tổng yêu cầu vốn có thể lên 20% hoặc hơn. Tier 1 bù lỗ khi hoạt động liên tục (going concern), Tier 2 dùng khi mất khả năng thanh toán (gone concern).
  > "Accordingly, the Common Equity Tier 1 (CET 1) has to make up at least 7% of the total risks of the bank as of 1 January 2019, i.e. after the expiration of the transition period. CET 1 is composed of 4.5% minimum rate and 2.5% capital conservation buffer. The entire Tier 1 capital (Common Equity plus Additional Tier 1) must be at least 8.5% and the total capital (Tier 1 plus Tier 2) must be 10.5%. The minimum rate for regulatory capital, which is calculated as total capital less capital conservation buffer, therefore remains as under Basel II at 8%."
  > "In addition, Basel III introduces the countercyclical buffer which depends on the state of the economy and varies from 0% to 2.5%."
  > "Tier 3 capital will be no longer counted. Also, the systemic risk buffer and the buffer for systemically important institutions are allocated on a case-by-case basis and depend on the bank/country and economic situation. Furthermore, the internal capital requirement prescribed by the regulator under Pillar 2 has to be met (Supervisory Review and Evaluation Process, or SREP). Thus, the total capital requirement can add up to be 20% or more. To ensure the quality of the regulatory capital there are strict rules regarding eligibility of capital instruments which can be included in the regulatory capital. Tier 1 capital is primarily to be used to cover the bank's losses from ongoing operations; meanwhile, Tier 2 capital is intended to be taken as a liability mass in cases of insolvency (gone concern)."
  > — Chapter 1, line 531 ^lubinska-u02-11

- CET1 gồm cổ phiếu phổ thông đủ điều kiện, thặng dư vốn cổ phần liên quan, lợi nhuận giữ lại, thu nhập toàn diện khác luỹ kế, cổ phần của công ty con hợp nhất do bên thứ ba nắm đủ điều kiện, và các điều chỉnh quy định; AT1 chủ yếu là công cụ vốn lai (CoCo, trái phiếu chuyển đổi bắt buộc).
  > "Common Equity Tier 1 includes the following items:"
  > "common shares issues by the bank that met the criteria of this category;"
  > "share premium accounts related to CET1 items;"
  > "retained earnings;"
  > "accumulated other comprehensive income;"
  > "common shares which were issued by consolidated subsidiaries held by third parties and meet the requirements for CET 1;"
  > "'regulatory adjustments' that are applied in determining Common Equity Tier capital."
  > "The Additional Tier 1 capital essentially comprises hybrid capital instruments (contingent convertible bonds, mandatory convertible notes) and consists of the sum of the following components:"
  > — Chapter 1, line 537 ^lubinska-u02-12

- Basel III/CRR đưa vào tỷ lệ đòn bẩy, bằng Tier 1 đủ điều kiện chia tổng tài sản nội và ngoại bảng không theo trọng số rủi ro; nguồn ghi Basel III/CRR yêu cầu tỷ lệ này 'a maximum of 3%' (diễn đạt của nguồn, xem Mâu thuẫn ghi nhận).
  > "In addition to the risk-sensitive capital requirements in the area of Pillar 1, a leverage ratio is introduced under Basel III/CRR as a key figure, which restricts the excessive build-up of debts in the banking system and prevents on- and off-balance sheet growth in relation to equity. The leverage ratio determines a maximum debt ratio to avoid deleveraging processes that could harm the whole financial system. The leverage ratio is defined as the ratio of the total eligible Tier 1 capital to the total of both (not weighted) on- and off-balance sheet assets. Basel III/CRR demands it to be a maximum of 3% (Enthofer and Haas 2016)."
  > — Chapter 1, line 559 ^lubinska-u02-13

- ALM được định nghĩa là cơ chế xử lý rủi ro do chênh lệch giữa tài sản và nợ về thanh khoản hoặc lãi suất, phát triển từ khớp kỳ hạn đơn giản đến duration matching và mô phỏng tĩnh, động. IRR là mối quan tâm của giám sát từ 1997 (BCBS 1997, 2004). Có hai cách tiếp cận đo: góc nhìn thu nhập (gap management, mục tiêu là biên lãi) và góc nhìn giá trị kinh tế (EBA coi là best practice).
  > "In its formal definition, Asset Liability Management (ALM) can be defined as a mechanism to address risks faced by a bank due to a mismatch between assets and liabilities, either due to liquidity or changes in interest rates. Although ALM is not a relatively new tool, it has evolved from the simple idea of maturity matching of assets and liabilities across various time horizons into a framework that includes sophisticated concepts, such as duration matching and the use of static and dynamic simulations."
  > "The interest rate risk for financial intermediaries, defined by Zen as the possibility of fluctuations in the market rate producing significant variations in one direction or the other on the balance of assets (Zen 2008), has been an object of attention for the supervisor since 1997 when the Basel Committee published guidelines on interest rate management (BCBS 1997 and 2004). The literature has amply debated the various types of interest rate risk to which banks are exposed; such a debate is reflected in works of Gualandri (1991) and Lusignani (2004). The various types of interest rate risk are discussed in detail in the next chapter."
  > "The main contributions published over the years focus on analysing the various approaches used to assess exposure to this risk. The first one is based on 'earnings perspective' and comprises the so called 'gap management' models, in which the objective (target) variable is set to be the operating interest margin (Resti and Sironi 2007). The second approach, 'economic value perspective' measures the effects of variations in the interest rate on the market value of a bank's financial assets and liabilities. The analytical models most often used in this context rely on techniques originally developed to measure the interest rate risk in bond portfolios (Brigo and Mercurio 2007; Staikouras 2006; Grundke 2004). The progress in risk management techniques has extended this concept to all banking book items and currently is adopted as a best practice by the European regulator (EBA)."
  > — Chapter 1, line 565 ^lubinska-u02-14

- Memmel (2011), mẫu 1.562 ngân hàng Đức 9/2005–12/2009: mức chịu IRR đi theo lợi nhuận kỳ vọng từ chuyển hoá kỳ hạn nhưng phụ thuộc mạnh vào quy mô; ngân hàng nhỏ và vừa chịu rủi ro đáng kể, ngân hàng lớn ít hơn; ngân hàng challenger sẵn sàng 'riding the yield curve'.
  > "The interest rate term structure and its relationship with the interest rate risk exposure of banks and, consequently, the level of profitability achieved has been investigated by Memmel in 2011 through the sampling of 1562 German banks during the period between September 2005 and December 2009. The results showed that the exposure to the interest rate risk moves in accordance with the possible earnings from term transformation, but it is very much determined by the bank's size and particularities. Thus, small and medium-sized banks showed significant exposure while the large banks seemed to have much less risk on their banking book. This trend can be still observed in banks. The challenger banks are willing to accept higher exposure in terms of 'riding the yield curve strategy' while larger and international banks keep their exposure limited."
  > — Chapter 1, line 573 ^lubinska-u02-15

- EBA ban hành GL về IRRBB tháng 5/2015 (thay CEBS từ 1/2016); BCBS ban hành chuẩn IRRBB tháng 4/2016 thay Nguyên tắc 2004. Ngày 19/7/2018 EBA ban hành bản cập nhật, là bản chuyển hoá chuẩn BCBS 2016 vào luật EU, áp dụng từ 30/6/2019, hơn 40% điều khoản mới; GL buộc đưa CSRBB vào khung IRRBB và đưa thay đổi giá trị thị trường vào thước đo thu nhập (không chỉ NII), gây khó cho phái sinh hạch toán phòng ngừa và danh mục AFS.
  > "Given the importance of IRRBB, in terms of the impact on capital base and earnings stability, the management of this risk has received increasing attention from the regulator and from the banking industry in recent years. As such, it has become a hot topic for national and European regulators. In May 2015, the EBA issued 'Guidelines on the management of the interest rate risk arising from non-trading activities' which was addressed to institutions in Europe and replaced the CEBS guidelines as of January 2016. In April 2016, the Basel Committee on Banking Supervision (BCBS) issued Standards on IRRBB that replaced the 2004 Principles. The new standards set out the Committee's expectations on the management of IRRBB in terms of identification, measurement, monitoring, control, and supervision. The updated IRRBB Principles reflect recent changes in market and supervisory practices due to a low and negative interest rate environment and provide methods and models to be used by banks in a wider and enhanced risk management framework."
  > "Finally, on 19 July 2018 the EBA published a final version on the update of its 'Guidelines on the management of the interest rate risk arising from non-trading book activities'. The long-awaited update for the management of IRRBB builds on the original guidelines published in May 2015. It is effectively the translation to European law of the IRRBB Standards published by the BCBS in April 2016. The guidelines will apply from 30 June 2019. As this book is being written, the EBA is still working on a number of technical standards as part of the ongoing CRD and CRR revisions in which they will prescribe disclosure requirements and the standardised approach for IRRBB. These technical standards will be published separately at a later stage. Compared to the 2015 version, the guidelines have increased in size significantly. It contains over 40% of new articles, which originate partly from BCBS Standards but also contain some new guidelines. The EBA guidelines, among other things, impose the inclusion of credit spread risk in the banking book (CSRBB) into the IRRBB framework. It is an important step towards standardisation of risk management across the banking industry and attempts to integrate the IRRBB with another kind of financial risk. Another main addition to the guidelines is the requirement to include market value changes in earnings metrics. This change will require banks to start modelling a true IFRS Profit and Loss at Risk and take into account the increase and reduction in total earnings and capital. Traditionally, earnings metrics just focus on NII and ignore any interest rate sensitivity in other areas of the P&amp;L account. It will have a significant impact on the modelling of earnings measures, as the accounting treatment of instruments will start to determine how the measure will be impacted. Although this seems a logical extension of earnings metrics, it presents challenges, especially in the areas of derivatives used for hedge accounting and instruments in an Available for Sale (AFS) portfolio, for which only the coupon payment was included until now. The updated EBA guidelines indicate an important trend that seems to be emerging on the banking horizon, i.e. the necessity to revise the current silo basis approach towards the management of different kind of risks and to implement a more holistic view on risk management practices."
  > — Chapter 1, line 575 ^lubinska-u02-16

- Tháng 1/2018 EBA khởi động stress test toàn EU với kịch bản vĩ mô tác động đồng thời lên rủi ro tín dụng, thị trường, thanh khoản; GL stress test của EBA 7/2018 nhấn mạnh liên kết và tương quan giữa các loại rủi ro, phải bao phủ mọi loại rủi ro trọng yếu.
  > "In January 2018, EBA launched its EU-wide stress test based on a number of macroeconomic scenarios which simultaneously have an impact on the credit risk, market risk, and liquidity risk of financial institutions. This is a clear attempt, from the regulator side, to see the overall picture, in terms of the exposure to financial and credit risks. The integrated stress testing is also promoted in the updated 'Guidelines on institutions' stress testing' published by the EBA in July 2018. These guidelines aim to achieve convergence of the practices followed by institutions for stress testing across the EU. They provide detailed guidance to be complied with by institutions when designing and conducting a stress testing programme/framework. The consideration of links and correlations between different risk types while performing the stress testing is emphasised by the Regulator. In fact, institutions should cover all material risk categories (and sub-categories) that the institutions are exposed to with regard to both on- and off-balance-sheet assets and liabilities in relation to all material portfolios."
  > — Chapter 1, line 581 ^lubinska-u02-17

- Resti (2011): LCR và NSFR bắt buộc sẽ giảm lợi nhuận ngân hàng do phải kéo dài kỳ hạn huy động và giữ đệm HQLA. Chuyển hoá kỳ hạn tạo đồng thời rủi ro lãi suất và thanh khoản; Baldan, Zen và Rebonato nghiên cứu một ngân hàng nhỏ Ý 2009–2010 thấy điều chỉnh thanh khoản theo Basel III đồng thời giảm IRR.
  > "In fact, the topic of liquidity risk attracted the interest of scholars well before the financial crisis in 2007, as the first papers date from the nineteenth century when Knies (1876) underlined the need for a liquidity buffer to compensate for negative gaps between inflows and outflows. In 1942, Saraceno claimed that 'the search for the most fruitful combination of lending and borrowing operations among all the operations that ensure the bank has the necessary balance between income and expenditure is the core problem of banks management. A bank's liquidity can be defined as its capacity to achieve this balance economically and at all times.' The most recent contributions provided the definition of liquidity and consequently the bank's liquidity risk (Gualandri 2009). In 2011, Cornett et al. analysed the financial crisis of 2007-2009. They pointed out the correlation of the liquidity risk exposure to loan growth during the crisis and also the growth in liquid assets which displaced funding to support new lending. The new international rules on liquidity risk management, standards, and monitoring were introduced by the Basel Committee on Banking Supervision in 2010. This new framework established standards for funding liquidity: Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR). Resti (2011) makes the point that the introduction of the mandatory LCR and NSFR will have significant impact on a bank's activity in terms of a decrease of their profitability. The necessity to extend funding maturities and to build a high-quality liquid assets buffer will give rise to reduction in a bank's interest margin and opportunity costs."
  > "The link between financial risks can be seen in one of the main functions of credit institution, i.e. maturity transformation. Banks finance their investments by issuing liabilities with a shorter maturity than that of their investments; the resulting imbalance between the terms for the assets and liabilities means that they take on the interest rate risk and liquidity risk. Baldan, Zen, and Rebonato launched the hypothesis that there is a direct relationship, so that reducing the exposure to the liquidity risk induces a reduction in the interest rate risk as well. Their study analysed a small Italian bank during the years 2009 and 2010 which had to modify its liquidity profile in order to become compliant with the Basel III requirements. As a result, it generated a simultaneous reduction in its exposure to the interest rate risk exposure. The authors conclude that in order to achieve integrated risk management, the control of each of these risks is placed in relation to the bank's different functions and influences its strategic decisions."
  > — Chapter 1, line 583 ^lubinska-u02-18

- Cách tiếp cận silo đang được thay bằng quản trị ALM tích hợp; Choudhry (2018) cho rằng ngân hàng phải chuyển từ ALM 'phản ứng' sang quản trị bảng cân đối tích hợp, chủ động; IRR (cả sổ ngân hàng và sổ kinh doanh) không thể xét tách khỏi thanh khoản, FTP, quản trị vốn.
  > "After the regulatory updates, the silo basis approach is being slowly replaced by more integrated management of ALM risks. This is because profitability remains a key concern for the EU banking sector. The low profitability and widespread dispersion for some countries, along with high operating costs, continues to dampen the profitability prospects for the European banking sector as a whole. Thus, there is a need to come up with new approaches which could address shrinking profitability, a heavily regulated landscape, and exposure to financial risks. This necessity has been highlighted by Choudhry 2018 in 'Strategic ALM and integrated balance sheet management: the future of bank risk management'. In this article, Choudhry suggests that the discipline of ALM, as practised by banks worldwide for over 40 years, needs to be updated to meet the challenges presented by globalisation and Basel III regulatory requirements. In order to maintain viability and a sustainable balance sheet, banks need to move from the traditional 'reactive' ALM approach to a more proactive, integrated balance sheet management framework. This will enable them to solve the multidimensional optimisation problem they are faced with at present. In his book Anthology - Past, Present and Future Principles of Banking and Finance the author describes a 'vision of the future' with respect to a sustainable bank business model. This vision of the future contains the concepts of strategic, integrated, and optimised ALM. The need for integration is becoming recognised by treasurers, risk managers, and regulators. It has also started to be considered among the ALM systems providers. They attempt to build ALM solutions which focus on the integration between IRRBB, liquidity, and FTP, supporting the view that, today, more holistic balance sheet risk management is required. Interest rate risk, both in the banking and the trading book, cannot be viewed in isolation from liquidity risk, funds transfer pricing, or capital management. Balance sheets have become more volatile - a result of changing term structures, optionality, better informed customers, and the use of derivatives. This book represents an attempt to further develop the integrated ALM concept and contributes to the work of Professor Moorad Choudhry, advisory firms, and others who acknowledge the need for change. It attempts, at least partially, to address the regulatory requirements and proposes potential solutions to arising challenges in the banking industry."
  > — Chapter 1, line 587 ^lubinska-u02-19

- IRR đo theo hai góc nhìn: thu nhập (tác động lên NII trong 1–2 năm, có thể bỏ sót chênh lệch ngoài kỳ phân tích) và giá trị kinh tế (thay đổi giá trị hiện tại của mọi dòng tiền dưới cú sốc quy định).
  > "It is important to highlight the main difference between IRRBB and liquidity risk. Interest rate risk is measured from two different perspectives: the earnings approach and the economic value approach. The first approach concentrates on the effects of interest rates movements on the bank's net interest income (NII) over short time horizons that could span from 1 to 2 years. However, the earnings perspective fails to indicate the long-term impacts of interest rate movements, as mismatches might be hidden beyond the horizon of the analysis (as already shown in the example in the previous chapter). In order to have a comprehensive view of the long-term effects of changes in rates, banks must adopt the economic value approach, which is based on the change in the present value of all cash flows under prescribed interest rate shocks."
  > — Chapter 2, line 595 ^lubinska-u02-20

- Rủi ro thanh khoản phải xét trong bối cảnh phân tích kịch bản; stress test xác định nguồn căng thẳng, xét dòng tiền hợp đồng và hành vi; trọng tâm là xác định quy mô đệm tài sản thanh khoản (LAB). Không có cách đo phù hợp cho mọi ngân hàng.
  > "Liquidity risk cannot be discussed, measured, or managed outside the context of scenario analysis. Stress and scenario testing is accepted as a key tool to identify, measure, monitor, and control liquidity risk. Stress testing is used to identify sources of potential liquidity strain, to ensure that current exposures continue to conform to the liquidity risk tolerance. Through stress testing, banks evaluate the resilience to liquidity stress and consider contractual and behavioural cash flows. The purpose of liquidity analysis is to identify future periods where the inflows can be lower than the outflows. The main point for the liquidity analysis is the determination of the size of liquidity asset buffer (LAB). In order to determine its size, the stress test tool is employed to reflect the expected requirements under stress. A detailed analysis of these two risks follows, based on the practices employed by a number of banks across Europe. It must be emphasised that there are many techniques to measure these risks and there is no one-size-fits-all approach. This chapter is intended to walk the reader through some of techniques employed by banks."
  > — Chapter 2, line 601 ^lubinska-u02-21

- Nguyên tắc tương xứng: ngân hàng càng lớn (theo tài sản nhạy lãi suất RSA) thì phương pháp đo IRRBB càng phải phức tạp. Maturity gap là kỹ thuật đơn giản nhất: phân tài sản, nợ, ngoại bảng nhạy lãi suất vào các dải thời gian theo kỳ hạn (lãi suất cố định) hoặc thời gian đến lần tái định giá kế tiếp (thả nổi); khoản không có kỳ tái định giá xác định (tiền gửi không kỳ hạn) hoặc kỳ hạn thực khác hợp đồng (vay có quyền trả trước) phân bổ theo đánh giá và kinh nghiệm của ngân hàng.
  > "Current financial regulation requires banks to have interest rate risk methods in place which are commensurate with the size and complexity of the bank. This is known as a proportionality approach. The bigger the bank in terms of size of risk sensitive assets (RSA), the more sophisticated the methods should be for the measurement of IRRBB. This chapter is focused mainly on the static methods, and contains an interpretation of results obtained through the application of those methods based on practical examples."
  > "According to the regulator, the maturity gap is the simplest technique for measuring a bank's interest rate risk exposure. It distributes interest-sensitive assets, liabilities, and off-balance sheet positions into a certain number of predefined time bands according to their maturity (if fixed rate) or time remaining to their next repricing (if floating rate). Those assets and liabilities lacking definitive repricing intervals (e.g. sight deposits or savings accounts) or actual maturities that could vary from contractual maturities (a mortgage with an option for early repayment) are assigned to repricing time bands according to the judgement and past experience of the bank. There are statistical methods to support the allocation decision for behavioural items and some of these are described in Chapter 3."
  > — Chapter 2, line 607 ^lubinska-u02-22

- Repricing gap của mỗi dải bằng tài sản nhạy lãi suất trừ nợ nhạy lãi suất; nhân với thay đổi lãi suất giả định cho xấp xỉ thay đổi NII. Độ lớn cú sốc dựa vào kinh nghiệm, mô phỏng và đánh giá của ban điều hành; nguồn ghi hướng dẫn quy định hiện hành yêu cầu sốc song song ±200 bp cho phân tích này.
  > "To evaluate earnings exposure, interest rate sensitive liabilities in each time band are subtracted from the corresponding interest rate sensitive assets to produce a repricing gap for that time band. This gap can be multiplied by an assumed change in interest rates to yield an approximation of the change in net interest income that would result from such an interest rate movement. The size of the interest rate movement used in the analysis can be based on a variety of factors, including the historical experience of the bank, a simulation of the potential future interest rate movements, and the judgement of the bank's management (Basel Committee on Banking Supervision 2016). Current regulatory guidelines require banks apply + / -200 bps parallel shock for this analysis."
  > — Chapter 2, line 611 ^lubinska-u02-23

- Hạn chế của maturity gap tĩnh: chỉ xét giao dịch hiện có (không có nghiệp vụ mới); coi mọi giao dịch trong cùng dải có cùng hồ sơ rủi ro; chỉ ước tính dịch chuyển lãi suất đồng đều; giả định tài sản, nợ đáo hạn được tái đầu tư/tái cấp vốn trong kỳ mà không đổi cấu trúc. Một số hạn chế khắc phục được bằng mô-đun mô phỏng NII.
  > "The static maturity gap method presents, however, significant limitations. For example:"
  > "It considers only transactions existing in the banking book at the date of analysis (there is no new business assumption)."
  > "It disregards different maturities of the transaction within the same time buckets (all transactions falling into the same time bucket have the same risk profile)."
  > "It allows for estimation only of the uniform movements of the interest rates."
  > "It assumes that asset and liabilities in maturity will be reinvested/refinanced within the gapping period (without altering the balance sheet structure) - there is no new business strategy applied here."
  > "However, some of these limitations can be quite easily overcome by application of a simulation module for net interest income in order to get a more precise picture of the risks run by the bank on the short end of the curve."
  > — Chapter 2, line 619 ^lubinska-u02-24

- ΔNII bằng tích của thay đổi lãi suất Δi với GAP (RSA trừ RSL trong kỳ phân tích); RSA là tài sản nhạy lãi suất (vay cố định hoặc thả nổi), RSL là nợ nhạy lãi suất (vốn bán buôn, tiền gửi không kỳ hạn); gapping period là kỳ phân tích, ví dụ 1 năm.
  > "The impact on the net interest income ( Δ NII) resulting from the movements of the interest rates is calculated as a product between the changes in the interest rates and the difference between an interest rate risk sensitive asset and liabilities known as GAP:"
  > "RSA represents assets sensitive to interest rates movements (for example, fixed or floating rate loans);"
  > "RSL represents liabilities sensitive to interest rate movements (for example, wholesale funding or sight deposits);"
  > "GAP is the difference between outstanding of RSA and RSL over the given time horizon;"
  > "Δ i represents magnitude of the interest rate shock."
  > "The concept of the gapping period (GP) is now introduced, which represents the time horizon chosen for this type of analysis, for example 1 year."
  > — Chapter 2, line 628 ^lubinska-u02-25

- Quản trị theo maturity gap: phòng ngừa miễn nhiễm (giữ GAP gần 0) hoặc GAP định hướng theo kỳ vọng lãi suất. GAP > 0: chịu rủi ro tái đầu tư, lãi khi lãi suất tăng, lỗ khi giảm; GAP < 0: chịu rủi ro tái cấp vốn, lỗ khi lãi suất tăng, lãi khi giảm; GAP = 0 thì miễn nhiễm.
  > "Using the maturity gap method, the bank can manage its position to the interest rate risk through:"
  > "The immunisation of interest rate risk keeping the GAP close to zero."
  > "Directional GAP keeping the voluntary mismatching according to the expectation of the future movements of the interest rate curve and an analytical understanding of the maturity profile of the balance sheet."
  > "If GAP &gt; 0, then the bank is exposed to reinvestment risk, meaning that in cases of interest rate increases it is going to show a profit. Conversely, in cases of interest rate decreases it is going to show a loss."
  > "If GAP &lt; 0, then the bank is exposed to refinancing risk meaning that in cases of interest rate increases it is going to show a loss. On the other hand, it realises profits if the interest rates decrease."
  > "In consequence, if GAP = 0, the bank is immune to interest rate risk and movements of the curve. Of course, in this sense the directional GAP strategy consists of the adjustment of the sign of the GAP (increasing it when there are upward expectations for the interest rates and reducing it when there are downward pressures from the market)."
  > — Chapter 2, line 646 ^lubinska-u02-26

- Ví dụ: tổng GAP ngắn hạn 500MM nên ngân hàng nhạy tài sản, NII 12 tháng tăng khi lãi suất tăng; ở phần trung–dài hạn ngân hàng ở vị thế nợ ròng nên lãi suất tăng làm EVE tăng. Khác biệt giữa hai thước đo là tầm thời gian.
  > "The repricing gap shows that under a short-term time horizon the bank is asset sensitive as the total GAP is equal to 500MM, which means that, under a 12-month time horizon, the NII will increase if the rates go up. Conversely, the opposite will happen if the rates go down. On the other side, on the medium-long part of the curve, the bank behaves as a net liability position, as an increase in rates will have a positive"
  > "impact on the economic value of equity (EVE), while a decrease will have a negative one. The difference between those two metrics is the time horizon. The first metric looks at the short time period and immediate impact on NII; the latter measures the change in the present value of the banking book for all items in the banking book while they exist."
  > — Chapter 2, line 679 ^lubinska-u02-27

- Maturity gap làm được trên Excel nhưng hạn chế đáng kể; phương pháp incremental gap cộng các gap theo trọng số thời gian, tức thời gian từ điểm giữa dải đến cuối gapping period (T là độ dài gapping period, t là kỳ hạn của dải, Δi là cú sốc).
  > "Amaturity gap analysis, as described by the regulator, can be easily performed in an Excel spreadsheet; however, the significant limitations deriving from this approach cannot be underestimated (Lubinska 2014). This basic method has been enriched through the introduction of the incremental gap method where the incremental gap is obtained by the summation of the subsequent gaps weighted for the time factor (Lusignani 1996). This time factor represents the time between the central value of the bucket and the end of the gapping period: ∑"
  > "T represents the length of the gapping period;"
  > "t maturity related to the time bucket;"
  > "Δ i shock in the interest rates curve."
  > — Chapter 2, line 693 ^lubinska-u02-28

- IRRBB là rủi ro hiện tại hoặc tương lai đối với giá trị kinh tế ròng, vốn và thu nhập do lãi suất biến động bất lợi ảnh hưởng tới vị thế sổ ngân hàng; phát sinh từ thay đổi lãi suất ở ngày fixing (chỉ với giao dịch thả nổi, phần refixing) và từ vị thế đáo hạn tái đầu tư/tái cấp vốn ở lãi suất mới (giao dịch cố định).
  > "Interest rate risk in the banking book (IRRBB) refers to the current or prospective risk to the bank's net economic value (EV), capital, and earnings arising from adverse movements in interest rates that affect the bank's banking book positions. The exposure"
  > "to the interest rate risk derives both from the variation of the interest rate to which the transaction is linked at the fixing date and consequently having an impact on the interest flow and the interest margin, and from the positions in maturity which are going to be reinvested or refinanced at the new rate. The first type of risk exists only in the case of floating rate transactions and only for the component in refixing (as opposed to the component in maturity). The second one refers to transactions at fixed rate."
  > — Chapter 2, line 715 ^lubinska-u02-29

- Gap risk phát sinh từ cấu trúc kỳ hạn của công cụ sổ ngân hàng, tức thời điểm đổi lãi suất; tuỳ đường cong dịch chuyển song song hay không song song; đo bằng repricing gap và chênh lệch ròng theo từng dải và đồng tiền trọng yếu.
  > "Gap risk, which arises from the term structure of banking book instruments, and describes the risk arising from the timing of instrument rate changes. The risk to the bank arises when the rate of interest paid on liabilities increases before the rate of interest received on assets or reduces on assets before liabilities. The extent of gap risk depends on whether changes to term structure of interest rates occur consistently across the whole yield curve (parallel risk) or differently by period (non-parallel risk). Banks measure and control the gap risk through the repricing gap and analysis of the net mismatch for every time band and by material currency."
  > — Chapter 2, line 727 ^lubinska-u02-30

- Basis risk là tác động của thay đổi tương đối giữa lãi suất các công cụ cùng kỳ hạn nhưng định giá theo chỉ số khác nhau; đo bằng theo dõi benchmark của tài sản và nợ theo từng dải và sốc 1 bp xem tác động P&L; một số ngân hàng mặc định khớp yếu tố rủi ro hai phía.
  > "Basis risk describes the impact of relative changes in interest rates for financial instruments that have similar tenors, but are priced using different interest rate indices (bases). It arises from the imperfect correlation in the adjustment of the rates earned and paid on different instruments with otherwise similar rate change characteristics. Banks measure basis risk by monitoring different benchmarks of assets and liabilities by every time bucket and shocking them by 1 bp to see the potential impact on the P&amp;L. Certain banks, by default, adopt the strategy in terms of the minimisation of the exposure to the basis risk, which consists of an attempt to match the risk factors on the asset and liability side as much as possible."
  > — Chapter 2, line 728 ^lubinska-u02-31

- Option risk phát sinh từ quyền chọn tường minh hoặc nhúng trong vị thế sổ ngân hàng; quyền chọn tự động đánh giá theo ΔEVE; quyền rút tiền của người gửi là quyền chọn hành vi. Yield risk là rủi ro từ dịch chuyển không song song ngoài dự kiến (dốc lên, phẳng, đảo ngược) và dịch chuyển song song phần trung–dài.
  > "Option risk arises from option derivative positions explicitly or implicitly embedded within the banking book positions. Those automatic options aim to protect a bank from the decrease/increase in the interest rates and their impact needs to be assessed on the potential change in the EVE (the impact of automatic options on EVE is presented in Chapter 3). There is also an optional element embedded in banks' customer deposits providing them with a contractual right to withdraw their balance. This phenomenon is known as behavioural optionality embedded in the banking book and is thoroughly examined in Chapter 3."
  > "Yield risk - the risk arising from unanticipated non-parallel shifts of the yield curve such as steepening, flattening, inverted curve, and parallel shifts on the medium-long part of the curve."
  > — Chapter 2, line 729 ^lubinska-u02-32

- Theo Final Report của EBA (19/7/2018), maturity gap trên Excel không còn phù hợp; mô phỏng NII là thách thức lớn vì phục vụ nhiều mục đích: stress test EBA giả định về giá, tầm thời gian và thay đổi cấu trúc sổ, còn thước đo nội bộ thường chỉ đo tác động thuần của lãi suất trong ngắn hạn với sổ không đổi (khoản đáo hạn thay bằng khoản cùng đặc điểm). Cách tiếp cận nâng cao cần chỉ ra yếu tố rủi ro chỉ số của vị thế trong từng dải và tách bằng FTP thành phần lãi suất, thanh khoản, biên thương mại.
  > "IRRBB has received increasing regulatory attention and has become one of the hot topics for national and European regulators in recent years. There are clear prescriptions on how this kind of risk needs to be measured, monitored, and mitigated. The IRRBB guidelines known as the Final Report were issued on 19 July 2018. As a result, adequate IRRBB management needs to consider several dimensions, not only in terms of integrated software solutions, but also revision of metrics and introduction of a model validation framework. The simple maturity gap analysis performed in an Excel spreadsheet is no longer fit for purpose. The technical implementation of an NII simulation, clearly needed for the strategic positioning and definition of a steering approach, is a major challenge for banks. This is because the results of expected NII are required for different purposes and under various views. For example, an NII simulation required for European Banking Authority (EBA) stress testing implied certain assumptions related to pricing, time horizon, and changes in the banking book structure over time, while the internal measure is usually focused on the pure impact of interest rates on NII under a short time horizon and does not include any changes in the composition of the banking book. It is said that the banking book is constant for the purposes of this kind of analysis, i.e. without a new business assumption. Expiring items are replaced on a like for like basis, i.e. based on the same financial characteristics. Consequently, in order to capture all the above aspects, an integrated and flexible approach is needed, and it requires software solutions that serve the various purposes of NII simulation (not just a static approach). The advanced approach to the measurement of the impact on NII needs to include additional essential features; for example, to provide an indication of which risk factors banking book positions are indexed to in every single time bucket, and if this is the simple (one risk factor) or average indexation (a number of risk factors). Secondly, there has to be clear separation through FTP between the interest rate risk component, liquidity component, and commercial spread in order to allocate the interest income to sales and Treasury."
  > — Chapter 2, line 732 ^lubinska-u02-33

- So sánh maturity gap cơ bản và advanced repricing gap: cơ bản đặt dòng tiền ở điểm giữa dải, nâng cao đặt ở ngày rủi ro chính xác; cả hai tính thay đổi biên lãi trong gapping period với sốc song song 200 bp (có thể chọn mức khác). Repricing gap nâng cao chỉ ra yếu tố rủi ro, tách dòng đáo hạn (tái đầu tư ở lãi suất forward) với dòng refixing, và bắt độ nhạy từ indexation không hoàn hảo (kỳ fixing khác kỳ trả lãi, có spread tài chính, trọng số chỉ số khác 1, chỉ số bình quân).
  > "Brief Comparison of Two Approaches (Basic Maturity Gap and Advanced Repricing Gap) Both methods take into consideration the flows related to the underlying transactions and position them at the date at which they become sensitive to the interest rates. Meanwhile, the simple maturity gap classifies them in the function of the time bucket into which they are expected to fall and, as such, the position is weighted by the mid-point of the time bucket; under the advanced repricing gap approach it is expected to position transactions at the exact date of risk. In both cases these flows are used to determine the expected change in the interest margin for a predetermined gapping period, given a parallel shock of 200 bps (obviously it is possible to assign any other magnitude of shock) to the rate curve associated with the transaction. One of the most important limits of the maturity gap analysis consists of the impossibility of the identification of the parameters (risk factors) to which the transaction is linked. This means that the transaction at floating rate is distributed to the appropriate time bucket according to the time left until its repricing. Therefore, if the transaction falls into the time bucket of 3-6 months, it is not clear to which market parameter it is linked. Instead, the advanced repricing gap approach allows for estimating the impact of each parameter in terms of its contribution to the interest margin for each time bucket. Additionally, using the simple maturity gap approach it is not possible to know if the estimated sensitivity of the expected margin is derived from maturity flows (the transactions which amortise or mature and have to be reinvested or refinanced at the 'new' interest rate) or from the flows in refixing. This is an important disadvantage with respect to the advanced repricing gap approach, which calculates the NII sensitivity caused by the component in maturity reinvesting (refinancing) it at the forward rate until the end of the gapping period. Finally, the most important thing which gives such a big advantage to the repricing gap, locating it at the top of the static methods family, is that it captures the sensitivity deriving from the non-perfect indexation of the transaction. In particular, if the transaction is the floating rate perfectly indexed, the repricing flow is positioned at the first rate reset date for the transaction as a whole. If not, the sensitivity captured from the non-perfect indexation is calculated and shown also for the subsequent refixing dates. Imperfect indexation arises in the following situations:"
  > "the rate fixing period is different to the interest payment period;"
  > "in the presence of financial spreads;"
  > "the weight of the indexation parameter is not equal to 1;"
  > "average indexation."
  > — Chapter 2, line 734 ^lubinska-u02-34

- Hai cách nhìn maturity gap: flow approach (dòng tiền với khoản cố định, dư nợ tại ngày tái định giá với khoản thả nổi) dùng để tính ΔNII; stock analysis (dư nợ từng khoản) dùng để tính phơi nhiễm theo dải và phòng ngừa.
  > "The first view is known as the fl ow approach as shown in Figure 2.2, and designs the maturity gap in terms of cash flows (for the fixed rate items) and outstanding at repricing (items at floating rate). This approach is commonly used for the calculation of the Δ NII for a certain gapping period and shock magnitude."
  > "The second view is known as stock analysis , shown in Figure 2.3, and designs the maturity gap in terms of outstanding for every item. The residual gap creates NII sensitivity and indicates the extent of the exposure to interest rate risk. This approach is usually used for calculation of the bucket exposure and hedging."
  > — Chapter 2, line 743 ^lubinska-u02-35

- Repricing gap thường thể hiện phơi nhiễm trong 12 tháng chia theo tháng, gồm khoản cố định đáo hạn và khoản thả nổi đổi lãi suất, nhưng chỉ 'thấy' ngày rủi ro đầu tiên (ví dụ khoản EURIBOR 3M tái định giá 1, 4, 7, 10/2019 chỉ hiện tháng 1 khi phân tích ở 12/2018); tách vị thế đáo hạn và refixing giúp diễn giải.
  > "Repricing Gap Analysis and Refixing Gap Analysis The repricing gap here refers to the advanced derivation of the maturity gap which was described above. In this stage, the purpose is to focus on its application and the difference with respect to the refixing gap which shows all flows in refixing (not only the first refixing date but also the subsequent dates). The repricing gap usually shows a picture of the exposure to the interest rate risk within a short time period (12 months). It captures the positions both at the fixed rate, which matures and needs to be reinvested (if assets) or refinanced (if liabilities), and the floating rate, which will reset its rate, generating in this way the interest rate risk exposure. The gapping period (usually 12 months) is split into monthly time buckets, giving in this way more precise information about the time when the risk is present. The more precise information about the timing related to the presence of risk, the more"
  > "accurate the measure of the exposure to the interest rate risk. It is worth highlighting at this point that even if it delivers a fast overview from the interest rate risk perspective, it does not consider the structure and the positions of the subsequent repricing gaps related to the given position. Instead, it 'sees' only the first risk date of the position in the fixation. For example, imagine that a bank has an amount of liabilities which reprice in January 2019, April 2019, July 2019, and October 2019 (it is indexed to EURIBOR 3M). Under the repricing gap approach, we will see only the repricing in January 2019 if analysed in December 2018 (the cut-off date). Under this approach, the positions in maturity and in refixing are separated, which greatly facilitates interpretation of the results. The bank is aware of when the risk derives from the expiration of the position and when it is caused by refixing. In order to calculate the sensitivity of the interest income, flows in refixing and in maturity are summed up. Again, the sensitivity of the interest income driven by the amount in refixing is separated from the sensitivity caused by the flows in maturity. This helps a lot in the analysis of the results. The repricing gap of the bank is now analysed, as shown in Figure 2.4."
  > — Chapter 2, line 747 ^lubinska-u02-36

- Refixing gap thể hiện mọi ngày refixing trong gapping period theo từng yếu tố rủi ro (EURIBOR 3M, LIBOR 1M…), dạng đơn giản nhất không dự phóng khối lượng mới (vị thế run-off); là công cụ cơ bản để đặt chiến lược phòng ngừa. Ví dụ: nợ ròng EUR 1 tỷ theo EURIBOR 6M refixing tháng 10 tạo rủi ro tập trung, phòng ngừa bằng mua FRA. Phương pháp là tĩnh: vị thế run-off, tác động NII tính theo đường forward.
  > "The figure shows a significant negative gap in January, which refers to the liabilities in refixing. From the IRR perspective, this net amount of liabilities will reset its rate and consequently expose the bank to the upward movement of the curve. Furthermore, positive gaps in refixing can be noticed in successive months. Conversely, they expose the bank to the downward movement of the curve. The subsequent presence of both negative and positive gaps in refixing partially offsets the exposure to the fluctuations of interest rates. The refixing gap analysis enriches the details provided by the repricing gap. It gives information about the existing mismatching between assets and liabilities at the floating rate indexed to the different risk factors (EURIBOR 3 M, LIBOR1 M, etc.) grouped in monthly or bi-weekly time buckets (or even daily) within the predetermined time horizon (for example, 12 months). The simplest form of the refixing gap approach does not incorporate the projection of the new volumes which the bank is going to disburse under the examination period. Instead, the positions are inertial (in a run-off). Unlike the repricing gap, the refixing analysis takes into consideration all the refixing dates of accounts related to the assets and liabilities under the gapping period. This is important information for the bank in order to contain the risk of mismatching and the high sensitivity driven by interest rate fluctuations. It is a fundamental tool for setting the hedging strategy and containing the negative impact on the interest income of a bank. Let us consider Figure 2.5 representing the refixing gap of a bank:"
  > "Source: own elaboration The figure shows negative mismatching, in the analysed example, in October 2010 and April 2011, caused by the EUR1bn net position in liabilities. This position is linked to EURIBOR 6M. Instead, from the asset side, the numerous net positions in assets are distributed steadily over time (in this case 12 months) linked mainly to EURIBOR 6Mand3M.Thebankis significantly exposed to upward movements in the level of the EURIBOR 6M while approaching the refixing date in October. Furthermore, this risk is concentrated in a 1-month time period. Suppose that in October 2010, following some important sudden event, the market responds through a hike in interest rate level. This bank incurs losses due to the negative gap in refixing. Subsequently, the market adjusts interest rates to pre-October levels. The bank has positive mismatching in November and again incurs losses. As can be seen, not only is the magnitude of the single gap important, but also its distribution over time. The hedging strategy consists of entering into the Forward Rate Agreement (FRA). The bank, in this case, buys an FRA, locking the rate on the negative mismatched position in October."
  > "The method presented above is a static one. That is, with the evolution of the balance sheet from the perspective of new business production, customers' behaviour with reference to the items with embedded options and the future evolution of the interest rates are not taken into consideration. Instead, the positions of the balance sheet are in a run-off, and the impact on NII is calculated under a forward curve scenario."
  > — Chapter 2, line 775 ^lubinska-u02-37

- EVE đo thay đổi lý thuyết của giá trị hiện tại ròng của bảng cân đối không gồm vốn chủ (tài sản nhạy lãi suất trừ nợ nhạy lãi suất) dưới cú sốc so với kịch bản cơ sở. Độ chính xác phụ thuộc dòng tiền và lãi suất chiết khấu; chuẩn BCBS chiết khấu ở điểm giữa dải bằng lãi suất phi rủi ro (internal view) hoặc lãi suất điều chỉnh nếu dòng tiền gồm biên thương mại (external view); ngân hàng chọn có tách biên thương mại qua FTP không, và hệ số chiết khấu phải nhất quán với lựa chọn đó.
  > "Economic value of equity (EVE) measures the theoretical change in the net present value of the balance sheet excluding equity, i.e. risk sensitive assets - risk sensitive liabilities. The measure therefore depicts the change in equity value resulting from an interest rate shock. Under this method, the value of equity under alternative stress scenarios is compared with the value under a base scenario. This base interest rate scenario is the present value of assets less liabilities under the current interest rate environment. All cash flows from on-balance sheet and off-balance sheet interest rate-sensitive items in the banking book may be included in the computation. The market value of equity is computed as the present value of assets cash flows, less the present value of liabilities cash flows, without including assumptions on the interest rate sensitivity of equity (the equity position is excluded from this approach). The balance sheet is then revalued under the alternative interest rate scenarios and the difference between the value of equity under the base scenario and the alternative scenario is calculated. The accuracy of the valuation of the balance sheet positions is extremely dependent upon the cash flows calculated and the discount rate used. The discounting rates used should match the duration and risk of the cash flows (the category of the instrument which is discounted). In the BCBS Standards, there is an assumption that the cash flows in certain time buckets are discounted with the rates at the mid-point of the time bucket with the risk-free rate (internal view), or adjusted rates if the cash flows include the commercial margins (external view). Bank have the choice of whether to deduct the commercial margin and other spread components from the notional repricing cash flows through the FTP methodology. Consequently, the discounting factor must be consistent with the view chosen for the EVE cash flows calculation (see Figure 2.6)."
  > — Chapter 2, line 789 ^lubinska-u02-38

- Cách tiếp cận tĩnh (dòng tiền không điều kiện) giả định thời điểm và quy mô dòng tiền không đổi theo kịch bản; thực tế lãi suất giảm thì trả trước tăng, người gửi tìm kênh đầu tư mới; dòng tiền điều chỉnh theo hành vi gọi là conditional cash flows, là best practice khi tính EVE.
  > "Under the static approach (unconditional cash flows) there is an additional assumption related to the fact that the timing of the cash flows and their size do not differ under"
  > "the various scenarios as a result of customer behaviour. In reality, there is a specific relationship between the interest rate scenario and the extent of prepayment and growth of deposits. For example, if the rates go down the prepayment rate tends to go up, as the clients are shopping for cheaper borrowing opportunities. However, on the liability side, savers tend to search for the new investment opportunities and the volatility of this product could increase. The cash flows which are adjusted by the potential changes in behaviour of the clients are known as conditional cash flows and represent the best practice of the EVE calculation."
  > — Chapter 2, line 791 ^lubinska-u02-39

- Final Report EBA 2018 yêu cầu áp phương pháp chuẩn hoá cùng phương pháp nội bộ (không thay thế); với ΔEVE áp sáu cú sốc quy định (parallel up, parallel down, short up, short down, steepener, flattener), hiệu chỉnh theo từng đồng tiền trọng yếu. Ưu điểm của EVE là bắt được độ lồi của sổ ngân hàng; ΔEVE tĩnh là ảnh chụp tại một thời điểm, có thể mô phỏng tác động nghiệp vụ tương lai; cách tiếp cận động mô phỏng sổ theo yếu tố bên ngoài, bên trong.
  > "The new regulatory framework (the EBA Final Report on IRRBB issued on 19 July 2018) in Europe represents a clear attempt to standardise the IRRBB methodologies across countries and financial institutions demanding the application of the standardised approach (prescribed by the regulator) along with the internal methodology banks may have already adopted (for example value at risk ). The EBA Final Report does not claim to replace the existing methodologies. Instead, it is the additional analysis that banks must perform in order to comply. For smaller institutions, the standardised framework could be used as a platform on which to set up the whole IRRBB framework of the bank."
  > "Under the standardised approach, for the calculation of impact on EVE, institutions are expected to apply six regulatory shocks with prescribed movements in interest rates. These are as follows:"
  > "parallel up (the shift of the whole curve up);"
  > "parallel down (the shift of the whole curve down);"
  > "short up;"
  > "short down;"
  > "steepener (short rates go down and long rates go up);"
  > "flattener (short rates go up and long rates go down)."
  > "The above shocks are calibrated by material currency, i.e. the magnitude of the shock differs for EUR, GBP, USD, etc."
  > "Even though this approach is simple and easy to interpret, it has its own pros and cons. The main benefits of the EVE model are the ability to capture the convexity embedded in the banking book, i.e. the extent of the difference between the linear approximation and the full valuation under certain interest rate shock scenarios. Additionally, the objective variable in this approach is the economic value of the banking book and, as such, the risk is measured in terms of economic value."
  > "Under the static view, the Δ EVE approach shows a snapshot in time of the risk based upon the current portfolio or balance sheet composition; however, it is possible to 'simulate' the potential impact of the future business based on the assumption coming from forecast growth or cannibalisation of certain products. The impact of such a simulated position is made at the wide time interval, for example on an annual basis, and reflects the situation at that specific point of time taking into account the new composition of the banking book. Thus, it is still a static approach but the assumption about growth is taken into account. On the other hand, the dynamic approach simulates the position of the banking book based on a number of external and internal factors and the simulated curve at a certain point of time."
  > — Chapter 2, line 801 ^lubinska-u02-40

- Case study: không có kịch bản nào lỗ vì lỗ giá trị sổ ở các kịch bản giảm (parallel down, short down, steepener) được bù bởi thay đổi giá trị quyền chọn tự động; ở các kịch bản tăng sổ có lãi nhưng quyền chọn out of the money; nguồn kết luận ngân hàng có nợ trung–dài hạn (nợ hành vi hoá) tài trợ tài sản tái định giá ngắn hạn.

  | Kịch bản | ΔEVE | ΔOptions | ΔEVE + Options |
  |---|---|---|---|
  | 2010 scenario | 31.724 | (6.692) | 25.032 |
  | Parallel up | 39.615 | (6.787) | 32.828 |
  | Parallel down | (42.065) | 131.558 | 89.493 |
  | Short up | 24.539 | (6.238) | 18.301 |
  | Short down | (25.349) | 38.499 | 13.150 |
  | Flattener | 13.571 | (180) | 13.391 |
  | Steepener | (6.866) | 9.074 | 2.208 |
  | Worse | (42.065) | (6.787) | 2.208 |

  > "Case Study Imagine that the change in EVE metric under six regulatory shocks of a financial institution looks as in the table below:"
  > "It clearly appears that there is no loss under any of the interest rate shock scenarios. This is because the loss in the banking book value is compensated by the change in the economic value of the automatic options under all downward scenarios (parallel down, short down, and steepener). Instead, under all upward scenarios (parallel up, short up, and flattener) the bank shows a gain embedded in the banking book but the automatic options become out of the money (under upwards interest rate shocks the difference in the economic value of automatic options under the shocked scenario and base scenario is negative). This picture indicates that this illustrative financial institution has medium long-term liabilities (for example behaviouralised liabilities) which fund the short-term repricing assets. This is because under upward scenarios, the bank takes the net liability position and the increase in rates results in an increase in the economic value of its banking book. Overall, it is clear that this bank is not assuming any IRRBB risk on the medium-long part of the curve. Neither is it riding the yield curve at this particular point in time."
  > — Chapter 2, line 818 ^lubinska-u02-41

- Tính ΔEVE theo chuẩn BCBS (nguồn trích lại): slot dòng tiền tái định giá danh nghĩa vào dải, netting trong dải; chiết khấu bằng hệ số liên tục DF = exp(−R·t_k) tại điểm giữa dải, lãi suất phi rủi ro; cộng lại thành EVE kịch bản; ΔEVE bằng EVE sốc trừ EVE cơ sở cộng KAO (add-on quyền chọn tự động, tường minh hoặc nhúng). Đường phi rủi ro có thể là secured IRS hoặc OIS.
  > "The gain or loss in economic value of equity Δ EVEi , c under scenario i and currency c is calculated as follows:"
  > "1. Under each scenario i , all notional repricing cash flows are slotted to the respective time bucket k ∈ { 1, 2, . . . , K } . Within a given time bucket k , all positive and negative notional repricing cash flows are netted to form a single long or short position, with the cancelled parts removed from the calculation. Following this process across all time buckets leads to a set of notional repricing cash flows CFi , ( k ) , k ∈ { 1, 2, . . . , K } ."
  > "2. Net notional repricing cash flows in each time bucket k are weighted by a continuously compounded discount factor: DFi , c ( tk ) = exp (-Ri , c ( t k ) ⋅ t k ) that reflects the interest rate shock scenario i in currency c and where t k is the midpoint of time bucket k . This results in a weighted net position, which may be positive or negative for each time bucket. The discount factors represent the risk-free rate."
  > "Finally, the full change in EVE in currency c associated with scenario i is obtained by subtracting EVE 0 , c from the EVE under shocked interest rate term structure EVEi , c and by adding the total measure for automatic interest rate option risk KAOi , c as follows:"
  > "In this regard, if Δ EVEi , c &gt; 0 then the economic value of the banking book is going to increase, while in the case where Δ EVEi , c &lt; 0 the bank faces a reduction in its economic value. KAOi , c is an add-on for the calculation of the change in the value of the automatic interest rate options, whether explicit or embedded."
  > "An example of a risk-free curve, as specified in the BCBS Standards or ECB IRRBB stress test performed in 2017, could be a secured interest rate swap or Overnight Index Swap (OIS) curve."
  > — Chapter 2, line 841 ^lubinska-u02-42

- PV01 là thay đổi giá trị hiện tại khi đường lãi suất dịch 1 bp cho một đồng tiền, bằng PV theo lãi suất hiện tại trừ PV theo đường sốc 1 bp; dòng tiền đặt theo ngày hoặc dải (hợp đồng hoặc mô hình hoá), chiết khấu ở điểm giữa dải (đơn giản hoá) hoặc ngày rủi ro chính xác (hệ thống ALM); dùng để xác định kỳ hạn quá nhạy và 'đóng' bằng phòng ngừa; tổng độ nhạy bằng tổng theo dải. Ví dụ: độ nhạy tập trung ở dải 1–5 năm do vị thế nợ, lãi suất tăng 1 bp tạo lãi.
  > "Sensitivity analysis is a method for calculating the change in the present values of items due to a 1 bp shift in the interest rates curve for a given currency. The sensitivity ( PV01 ) of the transaction is calculated as the difference between its Present Value ( PV ) determined with the current market rates and its Present Value under the curve shocked with 1 bp ( PV *):"
  > "The traditional approach consists of positioning cash flows at the date (time bucket) at which the flow is expected to occur (according to its contractual or modelled maturity) with calculation of its Present Value with the discount factor corresponding to the mid-point of time bucket (in case of the simplified approach) or to the exact risk date of the transaction (in the ALM system). This representation has a crucial importance in hedging or monitoring of the IRRBB structural exposure (usually related to the items at fixed rate), as it allows for the identification of the tenors of the term structure of interest rates, which are excessively sensitive to the movements of interest rates, and 'closing' them with hedging or natural hedging. The total time bucket sensitivity is a sum of sensitivities by time bucket."
  > "It can be clearly seen that the sensitivity of this bank falls into the time buckets between 1 and 5 years and this is due to the liability position. An increase in rates by 1bp, in those time buckets, results in a gain for the institution. On an overall basis, the increase in rates will lead to the positive impact."
  > — Chapter 2, line 863 ^lubinska-u02-43

- Duration là thời gian bình quân gia quyền theo giá trị hiện tại của dòng tiền; Modified Duration đo biến động giá (xấp xỉ tuyến tính, chỉ chính xác với dịch chuyển nhỏ); Macaulay duration đo bằng đơn vị thời gian, hai dạng chuyển đổi qua YTM và số kỳ trả lãi mỗi năm.
  > "Duration Gap Analysis Duration is a measure of the average life of the security. It represents the speed of payment of a security, and consequently the price risk relative to other securities with the same maturity. Duration is calculated as the weighted average time until the receipt of all cash flows from the security, where the weights are the present values of the cash flows to the total present value of the security:"
  > "where D is the duration of the security, t is the length (number of months, years, etc.) to the date of payment, and PVCF is the present value of the payment CF made at t , calculated as CFt ∕( 1 + r ) t , where the summation Σ is taken from the first to the last payment n and r is yield to maturity. Duration can be measured in two forms."
  > "The primary application of this metric is to measure the interest rate risk in the market and is known by the term Modified Duration (MD). This interpretation of duration represents the price volatility of the security and, consequently, its interest rate risk. Mathematically, duration is an approximation acceptable only for very small interest rate movements and it becomes imprecise in cases of significant shifts in the term structure."
  > "The second form of duration is measured in units of time, e.g. months or years, and is referred to as Macaulay's duration. The two forms are strictly related and can be transformed through the relation:"
  > — Chapter 2, line 873 ^lubinska-u02-44

- Duration gap DGAP dùng để theo dõi giá trị vốn khi đường lãi suất biến động; mức chấp nhận rủi ro do khẩu vị rủi ro của ban điều hành quy định, thường formalise trong chính sách ALCO. DGAP tính từ duration bình quân tài sản DA, của nợ DL và trọng số w = L/A (giá trị thị trường).
  > "Duration is very often used to monitor the value of capital of the financial institution in case of fluctuations of the curve. The assumption of a particular degree of risk exposure is a function of the bank's senior management risk appetite ('risk appetite' of the institution is usually formalised in the Asset/Liability Committee - ALCO - policy). The choice of selecting the capital value as a target position is dictated by the fact that this is a primary concern to the shareholders of the bank. While the interest rate sensitivity or risk of individual position is related to its modified duration, the interest rate risk of the target position is related to the difference, or gap, between the average duration of the assets of the institution and the average duration of the liabilities. The duration gap ( DGAP ) is:"
  > "where DA and DL are the average duration of assets and liabilities, respectively, and w is the weight defined as L/A (market value of liabilities to the market value of assets)."
  > — Chapter 2, line 907 ^lubinska-u02-45

- DGAP > 0: vị thế tài sản ròng, lãi suất tăng làm giá trị vốn giảm; DGAP < 0 ngược lại. Phòng ngừa miễn nhiễm đặt DGAP = 0. Ví dụ (Kaufman 1984): DA 4,17 năm, DL 1 năm, P/A 0,9, DGAP = 4,17 − 0,9 × 1 = 3,27 năm; về 0 bằng rút duration tài sản về 0,9 năm hoặc kéo duration tiền gửi lên 4,63 năm (0,9 × 4,63 = 4,17).
  > "Let us imagine that the DGAP of the banking book items of the financial institution is positive. In this case the bank behaves as a net asset position. Consequently, when the interest rates increase, the value of capital will diminish accordingly. Conversely, in the case of an interest rate decrease the capital value will increase as a function of the magnitude of the DGAP , the shock in the interest rate movement, and the dimension of the assets of the financial institution. Exactly the opposite will happen in the case of the DGAP &lt; 0. The institution can change its degree of interest rate exposure by any extent it wishes by changing the composition of the balance sheet in such a way as to obtain the desired duration gap for its target position. The greater the duration gap, the greater is the institution's risk exposure for a particular target position and, conversely, the smaller the gap, the smaller its exposure. The elimination of this risk consists of putting into place the immunisation strategy and setting the Duration Gap to zero. The financial institution, however, attempts to maximise its profits, but profit maximisation presumes a desired level of risk exposure. The desired risk-return tradeoff for a financial institution is determined by its ALCO policy and may be different from bank to bank. Managing the interest rate risk consists of determination of both the direction and size of its gap on the basis of its predicted interest rates. A bank may pursue two interest rate risk strategies: a passive (immunisation) strategy or an active strategy. The example below shows the immunisation strategy of a bank. It should be underlined that where a bank has gained income through correct interest rate management, it may it reduced or even lost as a consequence of the immunisation strategy. On the other hand, by immunising, the bank also decreases its chances of suffering losses if the risk is mismanaged. Let us consider that the initial value of capital is equal to 100 euro. The average duration of assets is equal to 4.17 years, meanwhile the average duration of liabilities (deposits P for example) is equal to 1 year and P/A = 0.9. This yields a duration gap: 4.17 -0.9 × 1 = 3.27 years. The immunisation condition is not maintained. The bank can reduce the gap to zero through:"
  > "Shortening the duration of its assets by 3.27 years to 0.9 years."
  > "Lengthening the duration of its deposits to 4.63 years so that 0.9 × 4.63 = 4.17."
  > "Let us suppose that the bank prefers to go through with the second possibility (lengthening the duration of deposits). It can do so by reducing the volume of the liabilities with shorter duration and increasing the volume of the liabilities with a longer duration. Consequently, the immunisation condition is satisfied. An interest rate increase, by say 200 bps, will decrease the value of assets in exactly the same way as before, changing the composition of the balance sheet (the assets side has not been changed). Instead, the composition of liabilities has been changed by reducing the proportion of shorter-term deposits. Through the immunisation strategy, the bank protects its capital level as the change in the asset market value is offset by the change in the market value of deposits (Kaufman 1984)."
  > — Chapter 2, line 917 ^lubinska-u02-46

- Chiến lược chủ động: ngân hàng dự báo lãi suất giảm, theo chính sách ALCO chấp nhận DGAP 1 năm; tổng tài sản 1.000 euro; nếu lãi suất tăng 200 bp thay vì giảm, giá trị thị trường của vốn giảm 20 euro (1000 × 2%). Chiến lược chủ động đòi hỏi dự báo đúng lãi suất.
  > "Managing the Interest Rate Risk through the Duration Gap Approach Let us suppose that the bank predicts a decline in the level of interest rates in the next period and, in accordance with its ALCO policy, accepts the risk in terms of duration gap of one year so that:"
  > "Imagine also that the average duration of assets is equal to 4.17 years, meanwhile the average duration of liabilities (deposits P for example) is equal to one year and P/A = 0.9. The market value of total assets is equal to 1000 euro. Again, as in the previous example, the bank can go through a strategy of shortening the duration of assets from 4.17 to 0.9 years or lengthening the duration of liabilities from 1 to 4.63 years. The bank will gain an increase in the value of capital if the interest rates decrease as predicted by the Treasurer of the bank. Now, contrary to the bank's expectations, let interest rates increase by 200 bps rather than decrease. The bank is worse off. The market value of capital has declined by 20 euro (1000 x 2%). The bank has deteriorated the market value of capital. However, it is worth remembering that in order to undertake the active strategy for the interest rate risk management, the bank has to be able to predict the interest rate movements and be right (Kaufman 1984)."
  > — Chapter 2, line 924 ^lubinska-u02-47

- Hạn chế của duration gap: cần dữ liệu đầy đủ từng vị thế, không xét trả trước và quyền chọn khác, chỉ chính xác với thay đổi nhỏ và giả định dịch chuyển song song; vẫn được dùng phổ biến.
  > "Limits of Duration Gap Analysis This is theoretically appealing, but requires the complete information of a data set related to items on the balance sheet (such as the maturity and the repricing frequency of every single position). Moreover, the early redemption of loans or other options included in the transactions are not taken into account. From a mathematical standpoint, a duration gap analysis works well only for small interest rate changes and it assumes that when the level of the interest rates changes, interest rates on all maturities change by exactly the same amount (parallel shift). However, despite all the above-mentioned limits, it is still commonly used in banking practice (Lubinska 2014)."
  > — Chapter 2, line 938 ^lubinska-u02-48

- Trước chuẩn BCBS, ngân hàng tự quyết khá nhiều về vốn nội bộ cho IRRBB, thường dựa trên VaR. GL EBA 19/7/2018 yêu cầu đóng góp của IRRBB vào vốn nội bộ xét cả ΔEVE và ΔNII: ΔEVE đánh giá dưới nhiều kịch bản, mức vốn tương xứng với rủi ro thực tế và khẩu vị rủi ro; cần đệm theo ΔNII để bù lỗ tức thời.
  > "ICAAP - Assessment of the Internal Capital to Cover IRRBB Risks Before the BCBS Standard was published, banks had quite a lot of discretion regarding the amount of internal capital to cover IRRBB risks. Many banks based their approach to ICAAP on the value at risk metric at a certain point of time. The maximum loss meant the need for potential capital coverage against risks."
  > "The revised final guidelines published on 19 July 2018 on the management of interest rate risk arising from non-trading book activities revised the methodological approach to ICAAP and set up new rules to be followed. In particular, it proclaims that institutions should base the contribution of IRRBB to the overall internal capital assessment, taking into account both the impact on the Δ EVE and Δ NII. The Δ EVE must be assessed under a number of interest rate scenarios at a certain point in time. The overall level of capital should be commensurate with both the institution's actual level of risk and its risk appetite, i.e. it represents the highest negative impact which the institution can face in terms of the Δ EVE. There is a need for a buffer, in terms of Δ NII impact to cover the immediate loss in case of adverse movement in the interest rates. This and additional requirements are clearly formulated by the regulator."
  > — Chapter 2, line 940 ^lubinska-u02-49

- Khi đánh giá vốn nội bộ cho IRRBB, tổ chức phải xét: vốn cho rủi ro giá trị kinh tế và nhu cầu vốn từ tác động lên thu nhập tương lai (hàm ý cho đệm vốn); quy mô và kỳ hạn hạn mức IRRBB nội bộ, và hạn mức có bị chạm khi tính vốn; hiệu quả và chi phí phòng ngừa vị thế mở theo kỳ vọng lãi suất; độ nhạy của thước đo nội bộ với giả định mô hình chủ chốt; tác động của sốc lên vị thế định giá theo chỉ số khác nhau (basis risk); động lực của rủi ro nền.
  > "Institutions must consider:"
  > "internal capital held for risks to economic value that could arise from adverse movements in interest rates and internal capital needs arising from the impact of rate changes on future earnings capacity and the resultant implications for the internal capital buffer levels;"
  > "the size and tenor of internal limits on IRRBB exposure, and whether these limits are reached at the point of capital calculations;"
  > "the effectiveness and effective cost of hedging open positions that are intended to take advantage of internal expectations of the future level of interest rates;"
  > "the sensitivity of the internal measures of IRRBB to key or imperfect modelling assumptions;"
  > "the impact of shocks and stress scenarios on positions priced with different interest rate indices (basis risk); and"
  > "the drivers of the underlying risks."
  > — Chapter 2, line 944 ^lubinska-u02-50

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
- u01 [2026-10-21]: tạo [[liquidity-cost-risk]]; cập nhật [[funds-transfer-pricing]], [[internal-risk-transfer]], [[alm-operating-model]], [[gap-risk]], [[irrbb-management]], [[intraday-liquidity-risk]], [[csrbb]] (draft).
- u02 [2026-10-19]: tạo [[repricing-gap-analysis]], [[pv01]]; cập nhật [[icaap]], [[repricing-balance-sheet]], [[ftp-transmission-mechanism]] (draft); đề xuất [[duration-gap-model]], [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[gap-risk]], [[basis-risk]], [[option-risk]], [[leverage-ratio]], [[key-rate-duration]] (canonical).
- [[internal-risk-transfer]]
- [[behavioural-options]]
- [[non-maturity-deposits]]
- [[ftp-pricing-methodology]]
- [[balance-sheet-optimisation-model]]
- [[repricing-balance-sheet]]
- [[model-risk-management]]
- [[net-interest-income-sensitivity]]

## Mâu thuẫn ghi nhận
- u02 [2026-10-19]: nguồn ghi tỷ lệ đòn bẩy Basel III/CRR 'a maximum of 3%' [[src-lubinska-alm-optimisation#^lubinska-u02-13]], trong khi LEV (T2) quy định tối thiểu 3%; coi là diễn đạt lệch của nguồn T4, không dùng câu này làm căn cứ; đã đề xuất ghi chú ở [[leverage-ratio]].
- Không có mâu thuẫn. Các nguyên tắc của Beata Lubinska (Wiley 2020) hoàn toàn tương thích và bổ trợ sâu sắc cho lý thuyết của Moorad Choudhry (Wiley 2022) và thực tiễn ngân hàng Việt Nam.

