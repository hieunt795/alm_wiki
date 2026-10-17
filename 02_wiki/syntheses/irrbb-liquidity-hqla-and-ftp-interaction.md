---
title: "Tương tác giữa IRRBB và thanh khoản (LCR/NSFR) qua đệm HQLA và định giá FTP"
aliases: [IRRBB Liquidity HQLA and FTP Interaction, Tuong tac giua IRRBB va thanh khoan qua HQLA va FTP, ALM IRRBB Liquidity HQLA FTP Interaction]
type: synthesis
domains: [alm, basel]
status: active
maturity: draft
origin: research
question: "Xung đột cấu trúc giữa LCR/NSFR và IRRBB · Đệm HQLA và bẫy thời lượng phòng hộ bằng IRS · Cơ chế FTP bóc tách chi phí thanh khoản và lãi suất · Xung đột tham số trong mô hình hành vi · Khung quy định Basel vs NHNN · Quản trị tích hợp ALCO và tối ưu hóa bảng cân đối"
as_of: 2026-10-17
sources: ["[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-bcbs-irrbb-2016]]", "[[src-vab-ftp]]", "[[src-ftp-transmission-analysis]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-tata-bank-alm]]"]
relations: []
tags: [alm, irrbb, liquidity, lcr, nsfr, hqla, ftp, term-liquidity-premium, buffer-carry-cost, duration-gap, synthesis]
updated: 2026-10-17
reviewed:
---

## Câu hỏi
1. Xung đột cấu trúc và sự đánh đổi (trade-offs) giữa quản trị rủi ro thanh khoản ([[lcr]]/[[nsfr]]) và rủi ro lãi suất ([[bcbs-irrbb|IRRBB]]) trên bảng cân đối kế toán ngân hàng diễn ra như thế nào?
2. Đệm tài sản thanh khoản cao ([[hqla]]) truyền dẫn rủi ro sang IRRBB như thế nào (chi phí negative carry, rủi ro sụt giảm [[economic-value-of-equity|EVE]] của TPCP), và kỹ thuật Treasury sử dụng [[interest-rate-swap|IRS]] để hóa giải bẫy thời lượng mà vẫn đảm bảo tính unencumbered?
3. Hệ thống [[ftp-pricing-methodology|định giá điều chuyển vốn nội bộ (FTP)]] phân tách và truyền dẫn đồng thời rủi ro IRRBB và rủi ro thanh khoản ra sao (Term Liquidity Premium, Buffer Carry Cost, phụ phí NSFR, và chi phí DTBB/BHTG)?
4. Các giả định [[behavioural-options|mô hình hành vi]] (CASA, rút tiền gửi trước hạn, trả nợ trước hạn) tương tác và tạo ra xung đột tham số như thế nào giữa khung thanh khoản (LCR Run-off, NSFR ASF) và khung lãi suất (Replicating Portfolio, CPR)?
5. Chuẩn mực Basel ([[src-bcbs-lcr]], [[src-bcbs-nsfr]], [[src-bcbs-irrbb-2016]]) và quy định pháp lý của NHNN (TT 50/2026, TT 83/2025, TT 22/2019) quy định thế nào về mối liên kết giữa đệm thanh khoản, IRRBB và FTP? Đâu là khoảng trống pháp lý tại Việt Nam?
6. ALCO và Treasury thiết lập cơ chế quản trị tích hợp và giải bài toán tối ưu hóa bảng cân đối (Balance Sheet Optimization) như thế nào để cân bằng đồng thời IRRBB, LCR, NSFR, NIM và Tỷ lệ đòn bẩy?

## Kết luận
- **Sự lệch pha kỳ hạn kép**: Vị thế tài sản và công nợ lệch pha kỳ hạn trên bảng cân đối đồng thời sinh ra rủi ro thanh khoản và rủi ro lãi suất [[src-tata-bank-alm#^tata-ftp-2]]. Các hành động tối ưu hóa thanh khoản đơn lẻ (như tích trữ TPCP dài hạn hoặc huy động vốn dài hạn cố định) có thể làm gia tăng mạnh khe hở thời lượng và độ nhạy $\Delta\text{EVE}$ [[src-tata-bank-alm#^tata-dgap-1]] [[src-lubinska-alm-optimisation#^lubinska-u05-14]].
- **Hóa giải bẫy thời lượng HQLA bằng Payer IRS**: TPCP Level 1 được tính 100% vào LCR với haircut 0% [[src-bcbs-lcr#^lcr30-41]], nhưng chịu rủi ro sụt giảm giá trị nghiêm trọng khi lãi suất tăng [[src-tata-bank-alm#^tata-dgap-2]]. Treasury triệt tiêu rủi ro thời lượng bằng hợp đồng hoán đổi lãi suất Payer IRS (trả cố định, nhận thả nổi), đưa thời lượng ròng về 0 mà vẫn duy trì trái phiếu ở trạng thái unencumbered [[src-bcbs-lcr#^lcr30-16]] [[src-tata-bank-alm#^tata-nii-17]].
- **FTP bóc tách đa tầng và nội bộ hóa chi phí**: FTP phân rã tỷ suất thành Base Rate, Liquidity Premium, Buffer Carry Cost, IRRBB Spread và Optionality Charge [[src-ftp-transmission-analysis#^ftp-trans-3]]. Chi phí lỗ mang vác (negative carry) của kho HQLA được tính toán và phân bổ sòng phẳng vào giá bán vốn COF của các tài sản sinh lời [[src-vab-ftp#^vab-ftp-10]] [[src-choudhry-principles-banking#^choudhry-ftp-15]].
- **Xung đột tham số mô hình hành vi**: Tiền gửi CASA bị khung thanh khoản LCR giả định rút chạy nhanh trong 30 ngày (Run-off 5%–10%) [[src-bcbs-lcr#^lcr40-20]], trong khi khung IRRBB lại mô phỏng danh mục sao chép kéo dài kỳ hạn hoàn trả lên đến 4–5 năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] [[src-lubinska-alm-optimisation#^lubinska-u05-13]]. Việc phối hợp ALCO đòi hỏi phải thống nhất phân rã phần lõi (Core) và biến động (Non-core).
- **Khoảng trống pháp lý tại Việt Nam**: Chuẩn mực quốc tế đã tích hợp chặt chẽ LCR, NSFR và IRRBB; trong khi tại Việt Nam, các văn bản quy định của NHNN về LCR/NSFR (TT 50/2026) và hướng dẫn đo lường IRRBB/mô hình hành vi (TT 83/2025) chưa được ingest đầy đủ vào wiki `[cần nguồn: src-tt50-2026-nhnn C2-M5, PL1, PL2; src-tt83-2025-nhnn C3-M5, C3-M7, C3-M8, PL5]`.
- **Tối ưu hóa đa mục tiêu**: Treasury giải quyết bài toán $\max \text{NIM}$ hoặc $\max \text{EVE}$ dưới hệ thống 4 ràng buộc biên đồng thời: $\text{LCR} \ge 100\%$, $\text{NSFR} \ge 100\%$, $|\Delta\text{EVE}| \le 15\%$ Vốn cấp 1 và Đòn bẩy $\ge 3\%$ [[src-lubinska-alm-optimisation#^lubinska-u05-14]] [[src-bcbs-irrbb-2016#^irrbb-p12-1]].

## Cơ chế

### Q1 — Bản chất xung đột và sự đánh đổi cấu trúc giữa LCR/NSFR và IRRBB
Vị thế lệch pha kỳ hạn trên bảng cân đối kế toán tạo ra đồng thời rủi ro thanh khoản và rủi ro lãi suất [[src-tata-bank-alm#^tata-ftp-2]]:
- **Đánh đổi LCR vs IRRBB (Tài sản Có)**: Để đáp ứng $\text{LCR} \ge 100\%$ [[src-bcbs-lcr#^lcr20-1]], ngân hàng tích lũy khối lượng lớn [[level-1-assets|Trái phiếu Chính phủ Level 1]] (haircut 0%) [[src-bcbs-lcr#^lcr30-41]]. Nếu nắm giữ TPCP kỳ hạn 5–10 năm cố định lãi suất để tìm kiếm lợi suất, thời lượng tài sản có $D_A$ dãn rộng, đẩy chênh lệch thời lượng $\text{DGAP} = D_A - \left(\frac{L}{A}\right) D_L$ tăng vọt, làm bốc hơi giá trị kinh tế của vốn chủ sở hữu khi lãi suất tăng [[src-tata-bank-alm#^tata-dgap-1]] [[src-tata-bank-alm#^tata-dgap-2]].
- **Đánh đổi NSFR vs IRRBB (Tài sản Nợ)**: Để tăng tỷ lệ nguồn vốn ổn định ròng $\text{NSFR} \ge 100\%$ [[src-bcbs-nsfr#^nsf30-26]], ngân hàng phải huy động tiền gửi hoặc phát hành giấy tờ có giá kỳ hạn dài $\ge 1$ năm để nhận hệ số $\text{ASF} = 100\%$ [[src-bcbs-nsfr#^nsf30-8]]. Nếu huy động lãi suất cố định, chi phí vốn (COF) bị khóa ở mức cao, bào mòn thu nhập lãi thuần ([[net-interest-income-sensitivity|ΔNII]]) khi mặt bằng lãi suất thị trường hạ nhiệt.
- **Bảng đối chiếu mục tiêu và xung đột**:
  | Chỉ tiêu | Mục tiêu quy định | Tác động lên Thanh khoản | Rủi ro phát sinh sang IRRBB |
  |---|---|---|---|
  | **Tích trữ TPCP dài hạn** | Tăng tử số LCR [[src-bcbs-lcr#^lcr30-41]] | Tăng đệm thanh khoản ngay lập tức | Tăng khe hở thời lượng $\text{DGAP}$, nhạy cảm $\Delta\text{EVE}$ âm lớn [[src-tata-bank-alm#^tata-dgap-2]] |
  | **Huy động nợ dài hạn cố định** | Tăng tử số NSFR (ASF 100%) [[src-bcbs-nsfr#^nsf30-8]] | Cải thiện cấu trúc vốn ổn định dài hạn | Khóa chi phí vốn cao, chịu rủi ro tái tài trợ/giảm NIM khi lãi suất giảm |
  | **Chuyển dịch sang cho vay thả nổi** | Giảm rủi ro tái định giá IRRBB | Thu hồi dòng tiền lãi linh hoạt | Dòng tiền gốc vẫn dài hạn ($\text{RSF} = 65\%-85\%$) [[src-bcbs-nsfr#^nsf30-30]], không giải quyết được LCR |

### Q2 — Đệm HQLA, Bẫy thời lượng và Kỹ thuật hóa giải bằng Phái sinh
- **Cấu trúc HQLA và chi phí cơ hội**: [[level-1-assets|Tài sản Level 1]] (tiền mặt, dự trữ NHTW, TPCP 0% rủi ro) không bị giới hạn trần và có haircut 0% [[src-bcbs-lcr#^lcr30-41]], nhưng sinh lời thấp nhất. Việc duy trì đệm HQLA dẫn tới tình trạng lợi suất âm biên (**Negative Carry**) so với chi phí huy động vốn của ngân hàng [[src-vab-ftp#^vab-ftp-10]].
- **Điều kiện Unencumbered và Rủi ro Thời lượng**: Tài sản HQLA bắt buộc phải ở trạng thái không bị thế chấp, cầm cố hay hạn chế chuyển nhượng ([[available-unencumbered-assets|unencumbered]]) và nằm dưới sự kiểm soát độc lập của Treasury [[src-bcbs-lcr#^lcr30-16]]. Khi nắm giữ TPCP cố định dài hạn, ngân hàng đối mặt với rủi ro suy giảm giá trị thị trường (Mark-to-Market) khi lãi suất tăng.
- **Kỹ thuật phòng hộ bằng Payer IRS (Pay-Fixed, Receive-Floating)**:
  - Treasury duy trì danh mục TPCP trong kho HQLA (đáp ứng điều kiện unencumbered để tính LCR) [[src-bcbs-lcr#^lcr30-16]].
  - Thực hiện giao dịch hoán đổi lãi suất [[interest-rate-swap|IRS]]: Trả lãi suất cố định (khớp với coupon TPCP) và Nhận lãi suất thả nổi ngắn hạn (kỳ hạn reset 1M hoặc 3M) [[src-tata-bank-alm#^tata-nii-15]].
  - *Hiệu ứng*: Dòng tiền lãi cố định của TPCP tài trợ cho chân trả của IRS, trong khi chân nhận thả nổi đưa thời lượng hiệu lực của danh mục về xấp xỉ 0 (kỳ hạn reset 3 tháng), triệt tiêu phơi nhiễm DV01 của HQLA mà không làm suy giảm tỷ lệ LCR [[src-tata-bank-alm#^tata-nii-17]] [[src-choudhry-principles-banking#^choudhry-ftp-10]].

### Q3 — Cơ chế phân rã FTP và Phân bổ chi phí thanh khoản / Lãi suất
Cơ chế FTP bóc tách toàn diện các cấu phần rủi ro vào tỷ suất điều chuyển vốn nội bộ [[src-ftp-transmission-analysis#^ftp-trans-1]] [[src-ftp-transmission-analysis#^ftp-trans-3]]:
$$\text{FTP Rate} = \text{Base Rate} + \text{Term Liquidity Premium (TLP)} + \text{Buffer Carry Cost} + \text{IRRBB Spread} + \text{Optionality Charge}$$
1. **Chuyển giao rủi ro lãi suất (IRRBB Transfer)**:
   - Áp dụng nguyên tắc Trùng khớp kỳ hạn (Matched-Maturity): Đơn vị kinh doanh (BU) được chốt lãi suất cố định theo đúng kỳ hạn tái định giá, chuyển giao toàn bộ khe hở tái định giá về Treasury [[src-choudhry-principles-banking#^choudhry-ftp-11]] [[src-ftp-transmission-analysis#^ftp-trans-10]].
2. **Chi phí thanh khoản kỳ hạn (Term Liquidity Premium - TLP)**:
   - Các khoản tín dụng trung dài hạn thả nổi (ví dụ cho vay mua nhà 15 năm, reset lãi suất 3 tháng) tuy có kỳ hạn tái định giá 3 tháng nhưng ràng buộc thanh khoản gốc 15 năm [[src-choudhry-principles-banking#^choudhry-ftp-14]]. FTP áp phụ phí TLP dựa trên kỳ hạn pháp lý nhằm phản ánh chi phí huy động vốn dài hạn:
     $$\text{TLP} = \text{FTP Rate}(15\text{Y}) - \text{FTP Rate}(3\text{M})$$ [[src-ftp-transmission-analysis#^ftp-trans-3]]
3. **Chi phí Gánh đệm Thanh khoản (Liquidity Buffer Carry Cost)**:
   - Khoản lỗ âm phát sinh từ việc nắm giữ đệm HQLA được tính toán và phân bổ vào giá bán vốn COF của toàn bộ tài sản sinh lời [[src-vab-ftp#^vab-ftp-10]] [[src-choudhry-principles-banking#^choudhry-ftp-15]]:
     $$\text{Buffer Premium} = \frac{\text{Số dư bình quân TSTK} \times (\text{VOF bình quân} - \text{Lợi suất bình quân TSTK})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$ [[src-vab-ftp#^vab-ftp-10]]
4. **Phụ phí cấu trúc NSFR và Chi phí pháp định tại Việt Nam**:
   - Nguồn vốn có hệ số ASF cao được thưởng thêm biên độ giá mua vốn VOF; ngược lại tài sản đòi hỏi RSF cao bị phạt tăng giá bán vốn COF [[src-ftp-transmission-analysis#^ftp-trans-8]].
   - Chi phí Dự trữ bắt buộc (DTBB) tại NHNN [[src-vab-ftp#^vab-ftp-9]] và phí Bảo hiểm tiền gửi (BHTG 0,15%/năm) [[src-vab-ftp#^vab-ftp-8]] được tính vào biểu giá FTP cho vay.

### Q4 — Tương tác và Xung đột tham số trong các Mô hình Hành vi (Behavioral Modeling)
Các mô hình hành vi bộc lộ sự mâu thuẫn sâu sắc giữa góc nhìn Thanh khoản và góc nhìn Lãi suất:
- **Tiền gửi không kỳ hạn (CASA/NMDs)**:
  - *Góc nhìn Thanh khoản*: Trong LCR, CASA bị coi là nguồn vốn có thể bị rút nhanh trong 30 ngày (tỷ lệ rút vốn run-off 5% đối với tiền gửi cá nhân ổn định, 10% đối với kém ổn định, 25%–100% đối với bán buôn) [[src-bcbs-lcr#^lcr40-20]]. Trong NSFR, CASA nhận hệ số ASF từ 90% đến 95% [[src-bcbs-nsfr#^nsf30-8]].
  - *Góc nhìn Lãi suất*: Trong IRRBB, ngân hàng phân tách CASA thành cấu phần biến động (Non-core) và cấu phần ổn định (Core CASA); phần Core được giả định có kỳ hạn hành vi kéo dài và phân bổ vào [[replicating-portfolio-model|danh mục sao chép]] với kỳ hạn hoàn trả bình quân tối đa 4–5 năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] [[src-lubinska-alm-optimisation#^lubinska-u05-13]].
  - *Mâu thuẫn*: Nếu Treasury sử dụng kỳ hạn 4–5 năm của CASA để tài trợ cho tài sản dài hạn, bảng cân đối sẽ thỏa mãn IRRBB nhưng đối mặt nguy cơ đứt gãy thanh khoản tức thì nếu xảy ra đột biến rút tiền trong 30 ngày.
- **Rút tiền gửi trước hạn (Early Redemption)**:
  - Khách hàng thực thi quyền chọn rút trước hạn khi mặt bằng lãi suất tăng vọt [[src-bcbs-irrbb-2016#^irrbb-u05-6]]. Hành vi này đồng thời làm co hẹp thời lượng công nợ trong IRRBB và kích hoạt dòng tiền ra đột xuất làm sụt giảm LCR, biến rủi ro lãi suất thành khủng hoảng thanh khoản.
- **Bảng ma trận đối chiếu tham số hành vi**:
  | Sản phẩm Bảng cân đối | Xử lý trong Khung Thanh khoản (LCR / NSFR) | Xử lý trong Khung Lãi suất (IRRBB) | Xung đột phát sinh |
  |---|---|---|---|
  | **Tiền gửi CASA Cá nhân** | LCR Run-off: 5% (ổn định) / 10% (kém ổn định) [[src-bcbs-lcr#^lcr40-20]]; NSFR ASF: 90%–95% [[src-bcbs-nsfr#^nsf30-8]] | Phân tách Core vs Non-core; Core sao chép kỳ hạn bình quân trần $\le 4.5-5.0$ năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] | Gán thời lượng dài cho CASA hỗ trợ EVE nhưng làm sai lệch rủi ro tháo chạy thanh khoản |
  | **Tiền gửi Tiết kiệm có kỳ hạn** | LCR Run-off: 0% nếu không được rút trước hạn; rút được thì theo tỷ lệ tiền gửi không kỳ hạn [[src-bcbs-lcr#^lcr40-20]] | Mô hình hóa tỷ lệ rút trước hạn phụ thuộc chênh lệch lãi suất thị trường (TDRR multiplier 1.2 khi lãi suất tăng) [[src-bcbs-irrbb-2016#^irrbb-u05-6]] | Khách hàng rút khi lãi suất tăng làm trầm trọng hóa khe hở thanh khoản khi chi phí tái tài trợ đắt đỏ |
  | **Cho vay Trả góp (Mortgages)** | Dòng vào hợp đồng trong 30 ngày (LCR Inflow cap 50%) [[src-bcbs-lcr#^lcr40-77]]; RSF = 65% [[src-bcbs-nsfr#^nsf30-30]] | Mô hình tỷ lệ trả trước (CPR multiplier 1.2 khi lãi suất giảm) [[src-bcbs-irrbb-2016#^irrbb-u05-5]] | Trả trước tạo thặng dư thanh khoản ngắn hạn nhưng gây rủi ro tái đầu tư ở lãi suất thấp |

### Q5 — Khung quy định: So sánh Basel vs Ngân hàng Nhà nước Việt Nam
- **Khung chuẩn mực Basel**: Tích hợp toàn diện giữa tỷ lệ thanh khoản ngắn hạn LCR (BCBS d296) [[src-bcbs-lcr]], tỷ lệ cấu trúc vốn ổn định NSFR (BCBS d297) [[src-bcbs-nsfr]] và khung đo lường rủi ro lãi suất sổ ngân hàng (BCBS d368) [[src-bcbs-irrbb-2016]].
- **Quy định của Ngân hàng Nhà nước Việt Nam**:
  - *Tỷ lệ thanh khoản*: Thông tư 22/2019/TT-NHNN và Thông tư 50/2026/TT-NHNN (hiệu lực từ 01/10/2026, quy định lộ trình áp dụng LCR và NSFR từ 01/10/2028 theo Điều 13) `[cần nguồn: src-tt50-2026-nhnn C2-M5, PL1, PL2]`.
  - *Quản trị rủi ro lãi suất và thanh khoản*: Thông tư 83/2025/TT-NHNN (hiệu lực 01/07/2026, thay thế TT 13/2018) quy định [[liquidity-risk-management|quản trị rủi ro thanh khoản]] (C3-M5), quản trị IRRBB (C3-M7) và quản trị rủi ro mô hình (C3-M8) `[cần nguồn: src-tt83-2025-nhnn C3-M5, C3-M7, C3-M8, PL5]`.
  - *Thực tiễn FTP*: Các NHTM Việt Nam vận hành hệ thống FTP nội bộ theo cơ chế tập trung tại Hội sở chính, phân bổ chi phí DTBB, BHTG và chi phí đệm thanh khoản vào biểu giá bán vốn cho vay [[src-vab-ftp#^vab-ftp-10]].

### Q6 — Cơ chế Quản trị Tích hợp tại ALCO và Bài toán Tối ưu hóa Bảng cân đối
Để giải quyết các xung đột chéo, Treasury và ALCO vận hành mô hình tối ưu hóa bảng cân đối kế toán đa mục tiêu (Multi-objective Balance Sheet Optimization) [[src-lubinska-alm-optimisation#^lubinska-u05-14]]:
1. **Hàm mục tiêu**:
   $$\max \text{NIM} \quad \text{hoặc} \quad \max \text{EVE} \quad \text{hoặc} \quad \min \text{Risk}(\Delta\text{EVE}, \Delta\text{NII})$$
2. **Hệ thống ràng buộc pháp lý và thanh khoản đồng thời**:
   - *Ràng buộc LCR*: $\frac{\text{HQLA}}{\text{Net Cash Outflows 30D}} \ge 100\% + \Delta_{\text{LCR target}}$ [[src-bcbs-lcr#^lcr20-1]]
   - *Ràng buộc NSFR*: $\frac{\text{ASF}}{\text{RSF}} \ge 100\% + \Delta_{\text{NSFR target}}$ [[src-bcbs-nsfr#^nsf30-26]]
   - *Ràng buộc IRRBB EVE*: $|\Delta\text{EVE}| \le 15\% \times \text{Tier 1 Capital}$ (ngưỡng Outlier test chuẩn hóa) [[src-bcbs-irrbb-2016#^irrbb-p12-1]]
   - *Ràng buộc Đòn bẩy*: $\text{Leverage Ratio} = \frac{\text{Tier 1}}{\text{Exposure Measure}} \ge 3\%$ [[src-lubinska-alm-optimisation#^lubinska-u05-14]]
3. **Cơ chế điều phối hành vi**:
   - Treasury sử dụng giá FTP làm công cụ kinh tế để hướng lái hành vi của các BU: tăng phí TLP để hạn chế BU cấp tín dụng dài hạn khi NSFR căng thẳng; tăng giá mua VOF để khuyến khích huy động tiền gửi kỳ hạn dài [[src-ftp-transmission-analysis#^ftp-trans-8]].
   - Quản trị rủi ro thặng dư tập trung tại Treasury bằng các công cụ phái sinh vĩ mô (Macro IRS Hedging) nhằm trung hòa khe hở thời lượng mà không làm ảnh hưởng đến chỉ tiêu kinh doanh của các chi nhánh [[src-tata-bank-alm#^tata-ftp-1]].

## Bằng chứng ủng hộ
- **Chuẩn mực BCBS**: Khung Basel III gắn kết chặt chẽ tử số HQLA của LCR với hệ số RSF rất thấp (0%–5%) trong NSFR [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-nsfr#^nsf30-26]], tạo điều kiện cho Treasury nắm giữ TPCP Level 1 để giải quyết đồng thời cả hai chỉ số thanh khoản.
- **Thực tiễn quản trị ALM quốc tế**: Moorad Choudhry khẳng định việc tách rời quản trị thanh khoản và lãi suất tại ALCO là nguyên nhân gốc rễ dẫn đến định giá sai lệch và thất thoát biên lợi nhuận [[src-choudhry-principles-banking#^choudhry-ftp-10]].
- **Cơ chế FTP thực tế tại Việt Nam**: Quy chế FTP của VietABank chứng minh việc đưa chi phí đệm thanh khoản TT22 và chi phí DTBB/BHTG vào biểu giá FTP là giải pháp khả thi để bảo vệ biên lãi ròng của ngân hàng [[src-vab-ftp#^vab-ftp-8]] [[src-vab-ftp#^vab-ftp-10]].

## Bằng chứng trái chiều
- **Bài học sụp đổ của Silicon Valley Bank (SVB 2023)**: SVB duy trì tỷ lệ thanh khoản cao trên sổ sách nhờ sở hữu khối lượng lớn trái phiếu chính phủ Mỹ và chứng khoán bảo đảm bằng thế chấp (MBS). Tuy nhiên, việc không phòng hộ rủi ro lãi suất (unhedged IRRBB) khi FED tăng lãi suất đã tạo ra khoản lỗ phi thực tế (unrealized loss) khổng lồ ăn mòn toàn bộ vốn chủ sở hữu. Khi mạng xã hội và ngân hàng số kích hoạt làn sóng rút tiền với tốc độ vượt xa kịch bản LCR 30 ngày của Basel, SVB buộc phải bán tháo HQLA và phá sản. Điều này chứng minh rằng việc nắm giữ HQLA nếu không quản trị chặt chẽ rủi ro thời lượng sẽ trở thành mầm mống gây đổ vỡ thanh khoản.
- **Nghịch lý đóng băng tài sản**: Việc siết chặt điều kiện HQLA unencumbered và tỷ lệ LCR $\ge 100\%$ khiến một tỷ trọng vốn rất lớn bị khóa cứng trong tài sản có lợi suất thấp, làm giảm hiệu quả phân bổ vốn tín dụng cho nền kinh tế thực.

## Phụ thuộc regime
- **Regime lãi suất thấp / nới lỏng**: Chi phí mang vác đệm HQLA thấp; ngân hàng có xu hướng kéo dài thời lượng danh mục đầu tư để tìm kiếm lợi suất (yield chasing), tích lũy rủi ro thời lượng tiềm ẩn lớn.
- **Regime lãi suất tăng vọt / thắt chặt**: Kho HQLA cố định bị bào mòn giá trị kinh tế nhanh chóng; chi phí cơ hội của đệm thanh khoản tăng vọt; áp lực rút tiền gửi gia tăng khiến các giả định mô hình hành vi (CASA, Prepayment) bị bẻ gãy.
- **Regime căng thẳng thanh khoản (Stress)**: Ngân hàng được phép sử dụng đệm HQLA để thanh toán, chấp nhận LCR tạm thời dưới 100% [[src-bcbs-lcr#^lcr20-5]]. Khi đó, việc bán tháo hoặc repo HQLA mang lại tiền mặt nhưng có thể làm thay đổi đột ngột trạng thái phơi nhiễm IRRBB của ngân hàng.

## Hàm ý ALM / quy định
- **Đối với ALCO**: Phải chấm dứt mô hình quản trị "silo" (tách biệt rủi ro lãi suất và thanh khoản). Mọi quyết định cơ cấu tài sản HQLA bắt buộc phải được đánh giá đồng thời trên cả 3 chiều: Tác động LCR, Tác động NSFR và Tác động $\Delta\text{EVE} / \Delta\text{NII}$.
- **Đối với Treasury**:
  - Khi mua TPCP dài hạn để đáp ứng LCR, phải lập tức triển khai hợp đồng hoán đổi lãi suất Payer IRS hoặc mua TPCP lãi suất thả nổi (FRN) để khóa rủi ro thời lượng.
  - Vận hành hệ thống FTP đa tầng, đưa phụ phí thanh khoản kỳ hạn (TLP) và chi phí gánh đệm HQLA vào giá bán vốn tín dụng.
- **Đối với Ngân hàng Nhà nước**: Cần sớm ban hành hướng dẫn kỹ thuật chi tiết về đo lường IRRBB và kịch bản sốc lãi suất cho VND (theo TT83/2025) cũng như chuẩn hóa lộ trình áp dụng LCR/NSFR (theo TT50/2026), giúp các NHTM có căn cứ pháp lý đồng bộ để thiết lập hệ thống FTP và quản trị rủi ro tích hợp.
- *Diễn giải:* (ngoài wiki, chưa có nguồn) Các ngân hàng có quy mô vốn vừa và nhỏ tại Việt Nam nếu chưa triển khai được hệ thống phái sinh IRS sâu rộng có thể sử dụng chiến lược "Barbell" (kết hợp tín phiếu NHNN ngắn hạn và TPCP trung hạn) để vừa đảm bảo thanh khoản vừa hạn chế tổn thất EVE khi lãi suất biến động.

## Bất định
- **Khoảng trống pháp quy NHNN**: Các unit kỹ thuật quy định chi tiết về phương pháp tính toán LCR/NSFR theo Thông tư 50/2026/TT-NHNN (`C2-M5`, `PL1`, `PL2`) và hướng dẫn đo lường IRRBB/mô hình hành vi theo Thông tư 83/2025/TT-NHNN (`C3-M5`, `C3-M7`, `C3-M8`, `PL5`) vẫn đang ở trạng thái `pending` trong kho lưu trữ, cần được ingest để hoàn thiện căn cứ tuân thủ tại Việt Nam.
- **Tính khả thi của thị trường phái sinh lãi suất VND**: Độ sâu của thị trường hoán đổi lãi suất (IRS) tại Việt Nam còn hạn chế, tạo rào cản thanh khoản cho các ngân hàng khi muốn triển khai phòng hộ thời lượng danh mục HQLA quy mô lớn.
