---
title: "Kiểm tra tính phản ánh economic cost và cơ chế định hướng incentive của hệ thống FTP"
aliases: [ftp-economic-cost-and-incentive-validation, Kiểm tra Economic Cost và Incentive FTP, FTP Economic Cost and Incentive Validation, FTP Governance and Behavioral Steering Validation, Định giá đúng chi phí kinh tế và động lực FTP]
type: synthesis
domains: [alm, product]
status: active
maturity: canonical
origin: query
question: "Làm thế nào để kiểm tra FTP đã phản ánh đúng economic cost của bảng cân đối và tạo đúng incentive cho các đơn vị kinh doanh?"
sources: [src-lubinska-alm-optimisation, src-choudhry-principles-banking, src-vab-ftp, src-ftp-transmission-analysis]
relations: []
updated: 2026-10-17
---

# Kiểm Tra Tính Phản Ánh Economic Cost và Cơ Chế Định Hướng Incentive Của Hệ Thống FTP

## 1. Bản Chất Vấn Đề: Tại Sao Kiểm Tra Economic Cost và Incentive Là Sống Còn?

Hệ thống Định giá Điều chuyển Vốn Nội bộ (Funds Transfer Pricing — FTP) là tổng hợp các chính sách và phương pháp luận mà ngân hàng áp dụng để tính phí hoặc ghi nhận quyền lợi cho thanh khoản tiêu thụ hoặc đóng góp trên bảng cân đối [[src-lubinska-alm-optimisation#^lubinska-ftp-1]]. Ranh giới phân định giữa chuyển đổi kỳ hạn (maturity transformation) và thương quyền khách hàng (customer franchise) chính là hệ thống FTP [[src-choudhry-principles-banking#^choudhry-ftp-3]]. 

Tuy nhiên, FTP là một cơ chế định giá nội bộ giả định dựa trên việc phòng ngừa rủi ro danh nghĩa (notional hedge) mà không có thị trường giao dịch bên ngoài để tự động sửa chữa sai lệch [[src-choudhry-principles-banking#^choudhry-ftp-5]]. Do đó, hệ thống FTP có nguy cơ bị sai lệch cấu trúc nếu không được kiểm định định kỳ.

Theo Beata Lubinska (2020) và nghiên cứu của Cơ quan Quản lý Thận trọng Vương quốc Anh (PRA) [[src-lubinska-alm-optimisation#^lubinska-ftp-13]], [[src-lubinska-alm-optimisation#^lubinska-ftp-14]]:
1. **Nếu chi phí vốn bị đánh giá thấp (underestimated)**: Các đơn vị kinh doanh (Business Units — BU) cung cấp các khoản vay giá rẻ cho khách hàng và tăng trưởng quy mô tài sản trong ảo tưởng rằng mình đang sinh lời cao, trong khi thực tế ngân hàng bị thâm hụt thanh khoản và ăn mòn vốn tự có.
2. **Nếu chi phí vốn bị đánh giá cao (overestimated)**: Các BU buộc phải đòi hỏi mức lãi suất cho vay khách hàng cao hơn mức thị trường chấp nhận, dẫn đến đánh mất khách hàng tốt vào tay đối thủ cạnh tranh và làm suy giảm thị phần.

*Diễn giải:* Để bảo đảm hệ thống FTP vận hành đúng chức năng, Ủy ban Quản lý Tài sản - Nợ (ALCO) và Khối Quản trị Rủi ro phải thiết lập một **Khung kiểm định kép (Dual-Validation Framework)** nhằm trả lời đồng thời hai câu hỏi:
- *Khía cạnh Chi phí Kinh tế (Economic Cost)*: Mức giá FTP có phản ánh chính xác chi phí cơ hội cận biên, chi phí thanh khoản kỳ hạn, chi phí đệm dự phòng pháp định và các quyền chọn ẩn trên bảng cân đối hay không?
- *Khía cạnh Động lực Hành vi (Incentive Alignment)*: Hệ thống FTP có tạo ra động lực kinh doanh lành mạnh, bảo vệ biên thương mại của chi nhánh, ngăn chặn trục lợi nội bộ (internal gaming/arbitrage) và dẫn dắt cấu trúc bảng cân đối theo đúng mục tiêu chiến lược của ALCO hay không?

```
+----------------------------------------------------------------------------------------------------+
|               KHUNG KIỂM ĐỊNH KÉP HỆ THỐNG FTP (DUAL-VALIDATION FRAMEWORK)                         |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  [TRỤ CỘT A: ECONOMIC COST VALIDATION]             [TRỤ CỘT B: INCENTIVE & BEHAVIORAL VALIDATION]  |
|  1. Kiểm thử Chi phí Cơ hội Cận biên (Marginality) 1. Phân tách True Cost vs Management Overlays   |
|  2. Kiểm thử Hạch toán Đầy đủ Cấu phần Phụ phí    2. Kiểm thử Miễn nhiễm Biên Thương mại chi nhánh |
|  3. Kiểm định Lãi/Lỗ Thặng dư CFU/Treasury P&L     3. Phát hiện Trục lợi Giá Nội bộ (Anti-Gaming)   |
|  4. Backtest Mô hình Hành vi (CASA & Prepayment)   4. Đo lường Hiệu quả Dẫn dắt Bảng cân đối ALCO  |
|                                                                                                    |
+----------------------------------------------------------------------------------------------------+
                                                │
                                                ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│      HỘI ĐỒNG ALCO & 3 TUYẾN PHÒNG THỦ: HIỆU CHỈNH THƯỜNG NIÊN VÀ TỐI ƯU HÓA BẢNG CÂN ĐỐI          │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Trụ Cột A: Bốn Kiểm Định Phản Ánh Đúng Economic Cost Của Bảng Cân Đối

### 2.1 Kiểm thử 1: Nguyên Tắc Chi Phí Cơ Hội Cận Biên (Marginality Principle Test)

Theo Choudhry (2022) và Lubinska (2020), chi phí lịch sử đã phát sinh của nguồn vốn hiện có hoàn toàn không có giá trị cho việc định giá các khoản vay mới; các khoản vay mới và tiền gửi mới đều phải được định giá dựa trên chi phí/lợi ích cơ hội cận biên tại thời điểm giao dịch [[src-choudhry-principles-banking#^choudhry-ftp-12]], [[src-lubinska-alm-optimisation#^lubinska-ftp-8]].

**Tiêu chí kiểm tra:**
- **Đường cong Base Rate**: Đường cong FTP chuẩn có bám sát lãi suất giao dịch thực tế trên thị trường vốn bán buôn (Interbank/VNIBOR, lợi suất Trái phiếu Chính phủ, chi phí phát hành giấy tờ có giá/chứng chỉ tiền gửi CD) hay không?
- **Khả năng giao dịch phòng ngừa (Transactability Check)**: Mức lãi suất FTP mà Treasury gán cho BU có thể thực hiện phòng ngừa danh nghĩa (notional hedge) trên thị trường tài chính tại thời điểm đó hay không? [[src-lubinska-alm-optimisation#^lubinska-ftp-8]].
- **Loại bỏ chi phí bình quân sổ sách (Historical Average Trap)**: Nếu ngân hàng sử dụng chi phí huy động vốn bình quân quá khứ (historical blended cost) để làm giá bán vốn cho khoản vay mới trong môi trường lãi suất tăng, ngân hàng đang trợ cấp ngầm cho bên vay và tự đặt mình vào rủi ro thanh khoản.

### 2.2 Kiểm thử 2: Hạch Toán Toàn Diện và Không Bỏ Sót Phụ Phí (Decomposition & Non-Omission Test)

Mức giá FTP kinh tế chuẩn tắc phải bóc tách đầy đủ các cấu phần chi phí trực tiếp và gián tiếp theo cấu trúc tích hợp [[src-ftp-transmission-analysis#^ftp-trans-3]]:

$$\text{FTP Rate} = \text{Base Rate} + \text{Liquidity Spread} + \text{Credit/Capital Spread} + \text{Optionality Cost}$$

Theo Lubinska (2020), chi phí duy trì đệm tài sản thanh khoản (Liquid Asset Buffer — LAB) phải được phân bổ chính xác cho đối tượng gây ra rủi ro thanh khoản [[src-lubinska-alm-optimisation#^lubinska-ftp-11]].

**Bảng Tiêu Chí Kiểm Tra Tính Đầy Đủ Của Chi Phí Kinh Tế:**

| Cấu phần Economic Cost | Bản chất chi phí kinh tế | Kiểm tra sự hiện diện trong hệ thống FTP | Dấu hiệu bỏ sót chi phí (Under-pricing) |
|:---|:---|:---|:---|
| **Term Liquidity Premium (TLP)** | Chênh lệch thanh khoản dài hạn của cam kết vốn [[src-vab-ftp#^vab-ftp-12]] | Đã áp dụng cho toàn bộ khoản vay thả nổi giữa kỳ hạn gốc và kỳ hạn repricing chưa? [[src-vab-ftp#^vab-ftp-33]] | Cho vay dài hạn thả nổi bằng giá Base ngắn hạn mà không cộng TLP. |
| **HQLA Negative Carry** | Khoản lỗ cơ hội khi giữ đệm thanh khoản theo LCR/TT22 | Đã tính phụ phí Buffer Charge phân bổ vào tài sản có sinh lời chưa? [[src-lubinska-alm-optimisation#^lubinska-ftp-11]] | Chi phí duy trì TPCP/tiền gửi NHNN bị hạch toán dồn vào lỗ của Treasury. |
| **Chi phí Pháp định** | Tiền nộp Bảo hiểm tiền gửi (0,15%) và Dự trữ bắt buộc (DTBB) | Đã quy đổi thành spread cộng vào COF và trừ khỏi VOF chưa? [[src-vab-ftp#^vab-ftp-1]] | Ngân hàng chịu thâm hụt biên do không tính chi phí DTBB vào giá bán vốn. |
| **Contingent Liquidity Fee** | Chi phí cam kết thanh khoản ngoại bảng chưa giải ngân | Đã thu phí đối với phần hạn mức tín dụng cam kết chưa rút chưa? [[src-vab-ftp#^vab-ftp-35]] | Cấp hạn mức tín dụng khủng nhưng không thu phí thanh khoản dự phòng. |
| **Prepayment Cost** | Rủi ro tái đầu tư giá rẻ khi khách hàng trả trước | Đã tính kỳ hạn hiệu lực WAL qua mô hình CPR và thu phí bù đắp chưa? [[src-vab-ftp#^vab-ftp-19]] | Định giá theo kỳ hạn hợp đồng 20 năm trong khi khách hàng trả hết sau 3 năm. |
| **Early Redemption Penalty** | Rủi ro rút tiền gửi trước hạn khi lãi suất tăng | Đã áp dụng cơ chế hồi tố lãi suất KKH theo Thông tư 04/2022 chưa? [[src-vab-ftp#^vab-ftp-18]] | Chi nhánh vẫn được nhận VOF kỳ hạn dài dù khách hàng đã rút tiền trước hạn. |

### 2.3 Kiểm thử 3: Kiểm Định Lãi/Lỗ Thặng Dư Của Trung Tâm Vốn (Treasury Residual P&L Test)

ALM/Treasury đóng vai trò là "ngân hàng bên trong một ngân hàng" [[src-lubinska-alm-optimisation#^lubinska-ftp-4]]. Treasury mua vốn từ đơn vị huy động và bán vốn cho đơn vị tín dụng, kế thừa toàn bộ trạng thái không khớp kỳ hạn (mismatch) về thanh khoản và lãi suất [[src-choudhry-principles-banking#^choudhry-ftp-10]], [[src-ftp-transmission-analysis#^ftp-trans-10]].

**Quy tắc kiểm định P&L của Treasury:**
1. **Mục tiêu Hedged Residual P&L $\approx 0$**: Khi Treasury thực hiện phòng ngừa rủi ro hoàn toàn (fully hedged) đối với các vị thế mismatch đã nhận từ chi nhánh, lợi nhuận ròng thặng dư của Treasury (sau khi trừ chi phí vận hành và chi phí phòng ngừa) phải tiệm cận mức 0.
2. **Cảnh báo lỗi định giá cấu trúc**:
   - *Nếu Treasury liên tục lỗ âm nặng kéo dài*: Giá bán vốn COF đang quá thấp (trợ cấp cho bên cho vay) hoặc giá mua vốn VOF đang quá cao (trợ cấp cho bên huy động), hoặc các phụ phí pháp định/đệm HQLA bị bỏ sót.
   - *Nếu Treasury liên tục lãi đột biến bất thường*: Treasury đang "ăn chặn" biên lợi nhuận của các chi nhánh thông qua việc định giá spread nội bộ quá rộng, làm triệt tiêu động lực mở rộng kinh doanh của chi nhánh.
3. **Phân tách P&L Rõ Ràng**: Báo cáo tài chính quản trị phải phân rã P&L của Treasury thành 3 sổ riêng biệt: Sổ rủi ro lãi suất (IRR Book), Sổ thanh khoản (Liquidity Book), và Sổ đầu tư đệm thanh khoản (LAB Management Book) [[src-lubinska-alm-optimisation#^lubinska-ftp-11]].

### 2.4 Kiểm thử 4: Backtesting và Kiểm Định Mô Hình Hành Vi (Behavioral Backtest)

Định giá sản phẩm phi kỳ hạn (CASA) và sản phẩm có quyền chọn ẩn phụ thuộc hoàn toàn vào các giả định mô hình hành vi [[src-vab-ftp#^vab-ftp-14]], [[src-vab-ftp#^vab-ftp-19]]:
- **Backtest Mô hình Danh mục Sao chép CASA (Replicating Portfolio Model)**:
  - So sánh tỷ lệ tiền gửi không ổn định (non-core CASA) và tiền gửi ổn định lõi (core CASA) trong mô hình với biến động số dư thực tế qua các chu kỳ thị trường [[src-vab-ftp#^vab-ftp-15]].
  - Kiểm tra độ nhạy rút tiền khi lãi suất thị trường tăng 100–200 bps. Nếu số dư CASA sụt giảm mạnh hơn giả định, tỷ lệ gán kỳ hạn dài của Core CASA đang quá cao, dẫn đến việc trả VOF vượt quá giá trị kinh tế thực tế.
- **Backtest Tỷ lệ Trả nợ Trước hạn (CPR)**:
  - So sánh tỷ lệ CPR kỳ vọng dùng để tính kỳ hạn bình quân gia quyền (WAL) với tỷ lệ trả nợ trước hạn thực tế của từng danh mục cho vay.
  - Nếu khách hàng trả trước ồ ạt khi lãi suất giảm nhưng ngân hàng không thu đủ phí bù đắp, mô hình định giá quyền chọn ẩn (Optionality Charge) đã bị định giá thấp.

---

## 3. Trụ Cột B: Bốn Kiểm Định Tạo Đúng Incentive Cho Đơn Vị Kinh Doanh

### 3.1 Kiểm thử 5: Phân Tách Minh Bạch True Economic Cost và Management Overlays (The PRA Rule)

Theo khuyến nghị từ cuộc rà soát của cơ quan giám sát PRA (Cadamagnani et al. 2015) và Beata Lubinska (2020) [[src-lubinska-alm-optimisation#^lubinska-ftp-13]]:

> "A Prudential Regulation Authority (PRA) cross-firm review of the FTP practices at major UK banks revealed important issues in banks' internal transfer pricing policies and framework. One of the major issues, underlined in the PRA's review, was that banks were not separating the management overlays from their funding curve... dampening practice skews business incentives and makes it less clear what the performance is for individual products before and after any management overlay."

> "any incentives and subsidies need to be made very transparent and come on top of a 'true and fair view' of the bank's liquidity costs." [[src-lubinska-alm-optimisation#^lubinska-ftp-6]]

**Quy tắc kiểm định bắt buộc:**
1. **Cấm dùng hai đường cong ngầm định**: Ngân hàng tuyệt đối không được áp dụng các đường cong chi phí vốn khác nhau một cách thiếu minh bạch (dampened curve) để vừa kích thích cho vay vừa kích thích huy động cùng lúc mà che giấu chi phí thực.
2. **Quy tắc Kiến trúc 2 Tầng (Two-Tier Pricing Architecture)**:
   $$\text{Final FTP Rate} = \underbrace{\text{True Economic Funding Rate}}_{\text{Tầng 1: Chi phí kinh tế thực tế khách quan}} \pm \underbrace{\text{Incentive Premium / Management Overlay}}_{\text{Tầng 2: Phụ phí khuyến khích/trợ cấp chiến lược của ALCO}}$$
3. **Báo cáo Lợi nhuận Quản trị Kép**:
   Mọi báo cáo P&L đơn vị kinh doanh và sản phẩm phải hiển thị 2 dòng chỉ tiêu song song:
   - *Biên lợi nhuận thuần túy trước điều chỉnh (Margin before Management Overlay)*.
   - *Biên lợi nhuận thương mại sau điều chỉnh (Margin after Management Overlay)*.
4. **Bốn Kỷ luật Đối với Gói Ưu đãi Chiến lược (Incentive Premium Rules)** [[src-lubinska-alm-optimisation#^lubinska-ftp-9]]:
   - Phải có thời hạn áp dụng cụ thể (Sunset clause, tối đa 3–6 tháng), không được kéo dài vĩnh viễn.
   - Phải có ngân sách phân bổ rõ ràng do ALCO phê duyệt.
   - Không được dùng để thay thế vai trò phản ánh chi phí vốn cận biên của đường cong chuẩn.
   - Phải được ghi nhận và hạch toán minh bạch đối ứng giữa các đơn vị.

### 3.2 Kiểm thử 6: Kiểm Định Miễn Nhiễm Biên Thương Mại (Commercial Margin Immunization Test)

Theo Giáo sư Moorad Choudhry, nguyên tắc sống còn của hệ thống FTP là phân định rạch ròi giữa chuyển đổi kỳ hạn và thương quyền khách hàng [[src-choudhry-principles-banking#^choudhry-ftp-3]]:

$$\text{Biên thương mại (Commercial Margin)} = \text{Lãi suất Khách hàng} - \text{Lãi suất FTP nội bộ}$$

Do lãi suất FTP nội bộ được xác lập trên cơ sở trùng khớp kỳ hạn (matched basis), biên lợi nhuận thương mại của đơn vị kinh doanh phải giữ nguyên không đổi trước các biến động sau đó của đường cong lãi suất thị trường [[src-choudhry-principles-banking#^choudhry-ftp-8]].

**Phương pháp kiểm thử:**
- Theo dõi biến động biên thương mại ($\text{NIM}_{\text{BU}}$) của từng chi nhánh qua chu kỳ biến động lãi suất $\pm 100$ đến $\pm 200$ bps.
- **Tiêu chuẩn đạt**: Độ lệch chuẩn của biên thương mại các hợp đồng lãi suất cố định phải tiệm cận bằng 0.
- **Tiêu chuẩn lỗi**: Nếu khi lãi suất thị trường tăng vọt, biên lợi nhuận của chi nhánh cho vay bị co hẹp nghiêm trọng, điều đó chứng tỏ chi nhánh vẫn đang phải gánh chịu rủi ro tái định giá lãi suất (IRRBB) do hệ thống FTP chưa thực hiện matched-maturity hoàn toàn.

### 3.3 Kiểm thử 7: Phát Hiện Trọng Tài Giá Nội Bộ và Hành Vi "Gaming" (Anti-Gaming & Internal Arbitrage)

Các đơn vị kinh doanh luôn có xu hướng tối ưu hóa chỉ số KPI cá nhân bằng cách tìm kiếm kẽ hở trong quy tắc định giá FTP thay vì tối ưu hóa lợi ích toàn hàng (moral hazard) [[src-lubinska-alm-optimisation#^lubinska-ftp-5]].

**Bảng Dấu Hiệu Trục Lợi Nội Bộ Cần Kiểm Soát:**

| Kẽ hở hệ thống FTP | Hành vi trục lợi của Đơn vị Kinh doanh (Gaming Behavior) | Hậu quả đối với Bảng cân đối | Giải pháp kỹ thuật ngăn chặn |
|:---|:---|:---|:---|
| **Bậc thang kỳ hạn (Tenor Cliff)** | BU cố tình cấu trúc hợp đồng vay ở mức 364 ngày thay vì 366 ngày để né bước nhảy vọt của TLP kỳ hạn 1 năm. | Bảng cân đối bị tích tụ rủi ro kỳ hạn ngầm ngay sát ranh giới bucket. | Áp dụng cơ chế **Nội suy tuyến tính liên tục (Linear Interpolation)** cho mọi kỳ hạn lẻ [[src-vab-ftp#^vab-ftp-30]]. |
| **Lách TLP Thả nổi** | BU thuyết phục khách hàng chuyển từ vay cố định sang vay thả nổi kỳ hạn tái định giá 1 tháng nhằm hưởng Base Rate rẻ mà không bị charge đủ TLP. | Ngân hàng chịu rủi ro rút cạn thanh khoản dài hạn. | Khóa chặt **TLP theo kỳ hạn hiệu lực WAL** không đổi suốt vòng đời khoản vay [[src-vab-ftp#^vab-ftp-34]]. |
| **CASA Ảo cuối tháng** | BU chi nhánh thỏa thuận với khách hàng doanh nghiệp đẩy tiền gửi vãng lai vào tài khoản đúng ngày chốt số liệu cuối tháng để hưởng VOF cao. | ALM bị lừa về quy mô nguồn vốn ổn định lõi; thanh khoản bốc hơi ngay đầu tháng sau. | Áp dụng tính **Số dư bình quân ngày (Daily Average Balance)** thay vì số dư thời điểm. |
| **Treo Hạn mức Ngoại bảng** | BU cấp hạn mức tín dụng dự phòng rất lớn cho khách hàng thân thiết để thu phí cam kết danh nghĩa nhưng không bị tính phí thanh khoản dự phòng. | Khi khủng hoảng nổ ra, khách hàng đồng loạt rút vốn, ngân hàng vỡ thanh khoản. | Áp dụng triệt để **Contingent Liquidity Charge** theo công thức $C \times \text{CCF} \times \text{TSTK Fee}$ [[src-vab-ftp#^vab-ftp-35]]. |

### 3.4 Kiểm thử 8: Kiểm Định Vòng Lặp Điều Tiết Hành Vi Khép Kín (Closed-Loop Steering Effectiveness)

Quản trị bảng cân đối thông qua FTP là một vòng lặp điều khiển khép kín [[src-ftp-transmission-analysis#^ftp-trans-13]]:

$$\text{Tín hiệu Basel III/NHNN} \rightarrow \text{Hiệu chỉnh FTP Engine} \rightarrow \text{Thay đổi Hành vi BU} \rightarrow \text{Định hình lại Bảng Cân Đối} \rightarrow \text{Cải thiện Chỉ số}$$

**Phương pháp đo lường hiệu quả điều tiết:**
- **Đo lường Độ co giãn Hành vi (Elasticity of BU Origination to FTP Adjustment)**:
  $$E = \frac{\% \Delta \text{ Quy mô giải ngân / huy động}}{\Delta \text{ FTP Spread (bps)}}$$
- **Kiểm tra độ trễ truyền dẫn (Transmission Lag)**: Sau khi ALCO quyết định tăng VOF kỳ hạn 12M–24M thêm 40 bps để cải thiện tỷ lệ nguồn vốn ngắn hạn cho vay trung dài hạn (hoặc chỉ số NSFR), mất bao nhiêu tuần/tháng thì cơ cấu huy động của toàn hệ thống chi nhánh chuyển dịch theo đúng mục tiêu?
- Nếu ALCO điều chỉnh spread mà tỷ trọng danh mục mục tiêu không thay đổi (độ co giãn $E \approx 0$), hệ thống FTP đã bị "đứt gãy truyền dẫn": KPI của chi nhánh không gắn với FTP margin, hoặc chi nhánh bị áp đặt chỉ tiêu doanh số thuần túy (volume-based target) thay vì chỉ tiêu lợi nhuận thuần (NII/RAROC) [[src-vab-ftp#^vab-ftp-38]].

---

## 4. Bộ Chỉ Số Định Lượng Giám Sát Sức Khỏe Hệ Thống FTP (FTP Health-Check Dashboard)

Ủy ban ALCO cần định kỳ giám sát sức khỏe của hệ thống định giá vốn thông qua 6 chỉ số định lượng cốt lõi:

```
+----------------------------------------------------------------------------------------------------+
|                       BỘ CHỈ SỐ KIỂM TRA SỨC KHỎE HỆ THỐNG FTP (ALCO DASHBOARD)                    |
+----------------------------------------------------------------------------------------------------+
| 1. TREASURY RESIDUAL MISMATCH P&L RATIO                                                            |
|    Công thức: |Net P&L Treasury Hedged| / Tổng NII Toàn hàng                                        |
|    Ngưỡng an toàn: ≤ 3.0% (Nếu > 5%, có sự bù chéo rủi ro hoặc định giá sai cơ cấu).              |
|                                                                                                    |
| 2. COMMERCIAL MARGIN STABILITY INDEX (CMSI)                                                        |
|    Công thức: Độ lệch chuẩn của BU Margin qua các kỳ điều chỉnh lãi suất                           |
|    Ngưỡng an toàn: Tiệm cận 0 đối với các sản phẩm cố định và sản phẩm thả nổi đã hedge TLP.      |
|                                                                                                    |
| 3. INCENTIVE OVERLAY TRANSPARENCY RATIO (IOTR)                                                     |
|    Công thức: Tổng giá trị tuyệt đối các khoản Incentive Overlays / Tổng Thu nhập FTP             |
|    Ngưỡng an toàn: ≤ 5.0% (Nếu vượt quá, hệ thống đang bị lạm dụng trợ cấp hành chính).            |
|                                                                                                    |
| 4. ARBITRAGE ANOMALY RATE (AAR)                                                                    |
|    Công thức: Tỷ trọng các món vay/gửi phát sinh ngay sát mốc ranh giới kỳ hạn (cliff tenors)      |
|    Ngưỡng an toàn: Tương đương phân phối chuẩn (Không có sự đột biến bất thường sát ranh giới).   |
|                                                                                                    |
| 5. BEHAVIORAL DRIFT RATIO (BDR)                                                                    |
|    Công thức: |WAL Thực tế - WAL Mô hình| / WAL Mô hình                                            |
|    Ngưỡng an toàn: ≤ 10% đối với danh mục cho vay thế chấp và tiền gửi CASA.                      |
|                                                                                                    |
| 6. BASEL III STEERING SENSITIVITY                                                                  |
|    Công thức: Tốc độ hội tụ của LCR và NSFR về ngưỡng an toàn mục tiêu sau mỗi lần hiệu chỉnh FTP  |
|    Thời gian chuẩn: 1 đến 2 quý kế toán.                                                           |
+----------------------------------------------------------------------------------------------------+
```

---

## 5. Khung Quản Trị Ba Tuyến Phòng Thủ Đối Với Hệ Thống FTP (FTP Governance)

Theo thông lệ quản trị quốc tế và Beata Lubinska (2020), hệ thống FTP tác động trực tiếp đến việc phân chia hàng nghìn tỷ đồng lợi nhuận và định hình cấu trúc rủi ro toàn hàng, do đó bắt buộc phải vận hành theo mô hình ba tuyến phòng thủ độc lập [[src-lubinska-alm-optimisation#^lubinska-ftp-5]], [[src-lubinska-alm-optimisation#^lubinska-ftp-12]]:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    HỘI ĐỒNG QUẢN TRỊ / ỦY BAN ALCO (CẤP PHÊ DUYỆT TỐI CAO)                          │
│ - Phê duyệt Chính sách & Phương pháp luận FTP toàn hàng.                                           │
│ - Phê duyệt Biểu lãi suất FTP định kỳ và các gói Incentive Premium chiến lược.                     │
│ - Trọng tài giải quyết xung đột lợi ích giữa Treasury và các Khối Kinh doanh.                      │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                ▲
                                                │
         ┌──────────────────────────────────────┼──────────────────────────────────────┐
         │                                      │                                      │
┌─────────────────────────┐            ┌─────────────────────────┐            ┌─────────────────────────┐
│     TUYẾN 1: CFU /      │            │    TUYẾN 2: RISK MGMT   │            │   TUYẾN 3: INTERNAL     │
│        TREASURY         │            │   (THẨM ĐỊNH ĐỘC LẬP)   │            │         AUDIT           │
│ - Xây dựng đường cong   │            │ - Độc lập thẩm định mô  │            │ - Kiểm toán định kỳ quy │
│   FTP và tính toán các  │            │   hình FTP và đường     │            │   trình và thuật toán   │
│   phụ phí thanh khoản.  │            │   cong tham chiếu.      │            │   trên Core Banking.    │
│ - Vận hành hệ thống     │            │ - Giám sát tính tuân    │            │ - Đảm bảo tính minh     │
│   tính toán hàng ngày.  │            │   thủ nguyên tắc không  │            │   bạch và ngăn ngừa     │
│ - Đề xuất ALCO điều     │            │   bù chéo rủi ro.       │            │   xung đột lợi ích.     │
│   chỉnh steering spread.│            │ - Backtest mô hình CASA.│            │                         │
└─────────────────────────┘            └─────────────────────────┘            └─────────────────────────┘
         ▲                                                                             ▲
         │                                                                             │
         └─────────────────── CƠ CHẾ PHẢN BIỆN TỪ ĐƠN VỊ KINH DOAN ────────────────────┘
             (Business resistance acts as a healthy check against unrealistic assumptions)
```

> [!NOTE]
> **Vai trò của sự phản biện từ Đơn vị Kinh doanh (Business Resistance):**
> Fidelio Tata (2025) và Schäfer et al. (2017) chỉ ra rằng các đơn vị kinh doanh nhận thức rất rõ mức giá FTP ảnh hưởng trực tiếp đến kết quả kinh doanh và tiền lương thưởng của họ. Sự kháng cự và phản biện lành mạnh của các chi nhánh trước các giả định FTP phi thực tế chính là cơ chế chốt chặn quan trọng chống lại sự lạm quyền hoặc sự áp đặt quan liêu từ bộ phận Treasury trung tâm.

---

## 6. Quy Trình Rà Soát Định Kỳ 5 Bước Dành Cho Ủy Ban ALCO (The 5-Step Practical Review Workflow)

Để bảo đảm hệ thống FTP phản ánh đúng chi phí kinh tế và tạo đúng động lực, Ủy ban ALCO cần chỉ đạo thực hiện quy trình rà soát định kỳ hàng quý theo 5 bước chuẩn hóa:

```
+----------------------------------------------------------------------------------------------------+
|                  QUY TRÌNH 5 BƯỚC RÀ SOÁT HIỆU LỰC HỆ THỐNG FTP DÀNH CHO ALCO                       |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  BƯỚC 1: RÀ SOÁT ĐƯỜNG CONG THAM CHIẾU VÀ TÍNH KHẢ THI PHÒNG NGỪA (TRANSACTABILITY)                 |
|  - Đối chiếu Base Curve với biến động lợi suất TPCP, VNIBOR và lãi suất phát hành CD thực tế.      |
|  - Loại bỏ hoàn toàn dấu vết của chi phí bình quân sổ sách lịch sử trong biểu giá mới.             |
|                                                                                                    |
|  BƯỚC 2: RÀ SOÁT TÍNH ĐẦY ĐỦ CỦA CÁC PHỤ PHÍ THANH KHOẢN VÀ PHÁP ĐỊNH                              |
|  - Tính toán lại chi phí âm duy trì đệm HQLA/TT22 và cập nhật vào Buffer Charge.                   |
|  - Cập nhật tỷ lệ chi phí DTBB và BHTG theo số dư thực tế phát sinh.                               |
|  - Đảm bảo các khoản vay thả nổi đều bị charge TLP theo kỳ hạn hiệu lực WAL.                       |
|                                                                                                    |
|  BƯỚC 3: ĐỘC LẬP BACKTEST CÁC MÔ HÌNH HÀNH VI (CASA VÀ TRẢ NỢ TRƯỚC HẠN)                           |
|  - Khối Quản trị Rủi ro (Tuyến 2) đối soát dữ liệu rút tiền CASA thực tế với Replicating Portfolio.|
|  - Cập nhật tỷ lệ CPR cho từng nhóm sản phẩm cho vay cá nhân và doanh nghiệp.                      |
|                                                                                                    |
|  BƯỚC 4: ĐỐI SOÁT P&L TREASURY VÀ PHÂN TÍCH HIỆU QUẢ INCENTIVE PREMIUM                             |
|  - Phân tích độ biến động của Treasury Residual Mismatch P&L; rà soát các khoản thâm hụt bất thường.|
|  - Đánh giá hiệu quả kinh tế (ROI) của các gói ưu đãi Incentive Premium; kích hoạt điều khoản kết   |
|    thúc (sunset clause) đối với các gói hết hạn.                                                   |
|                                                                                                    |
|  BƯỚC 5: HỌP BÁO CÁO ALCO VÀ RA NGHỊ QUYẾT HIỆU CHỈNH BIỂU GIÁ FTP KỲ TIẾP THEO                    |
|  - Ban hành Biểu giá FTP kỳ tiếp theo với sự đồng thuận của ALCO.                                  |
|  - Truyền thông minh bạch đến toàn bộ mạng lưới chi nhánh và cập nhật tham số trên Core Banking.   |
|                                                                                                    |
+----------------------------------------------------------------------------------------------------+
```

---

## 7. Kết Luận: Chuẩn Mực Vận Hành FTP Chuyên Nghiệp

Một hệ thống FTP được coi là thành công khi và chỉ khi thỏa mãn đồng thời hai tiêu chí:
1. **Phản ánh trung thực kinh tế học của bảng cân đối**: Không có bất kỳ rủi ro hay chi phí ngầm nào bị "thả nổi" hoặc bị dồn tích vô lý vào bảng cân đối của Treasury; mọi rủi ro thanh khoản, lãi suất, pháp định và quyền chọn ẩn đều được định giá sòng phẳng theo nguyên tắc chi phí cơ hội cận biên.
2. **Định hướng động lực kinh doanh minh bạch**: Tách bạch tuyệt đối giữa giá vốn kinh tế khách quan và các công cụ trợ cấp hành chính; bảo vệ trọn vẹn biên thương mại thương quyền của chi nhánh; đồng thời biến FTP thành chiếc "bánh lái" chuẩn xác đưa bảng cân đối kế toán của ngân hàng tiến tới trạng thái tối ưu hóa toàn diện giữa **An toàn thanh khoản (LCR, NSFR, TT22)**, **Kiểm soát rủi ro lãi suất (IRRBB)** và **Tối đa hóa Lợi nhuận điều chỉnh theo Rủi ro (RAROC/ROE)**.

## Khái niệm và Liên kết
- [[src-lubinska-alm-optimisation]]: Chuyên khảo về tối ưu hóa ALM, Target Operating Model của FTP, khuyến nghị giám sát PRA và quy tắc Incentive Premium.
- [[src-choudhry-principles-banking]]: Chuyên khảo nền tảng về chuyển giao rủi ro nội bộ, matched-maturity, nguyên tắc cận biên và bảo toàn biên thương mại.
- [[src-vab-ftp]]: Sổ tay phương pháp luận định giá FTP thực chiến tại ngân hàng thương mại Việt Nam.
- [[src-ftp-transmission-analysis]]: Nghiên cứu kênh truyền dẫn FTP đến các yếu tố rủi ro và mô hình tối ưu hóa bảng cân đối.
- [[ftp-nature-and-balance-sheet-management]]: Bản chất, mục tiêu và 5 vấn nạn kinh điển được giải quyết bởi FTP.
- [[ftp-risk-and-cost-components]]: Các cấu phần chi phí vốn, thanh khoản, pháp định và quyền chọn ẩn trong định giá FTP.
- [[ftp-curve-construction-methodology]]: Phương pháp luận xây dựng đường cong FTP theo kỳ hạn, đồng tiền và loại sản phẩm.
- [[ftp-portfolio-and-bucket-allocation]]: Phương pháp phân bổ giao dịch và sản phẩm vào danh mục và thang kỳ hạn FTP.
- [[ftp-cost-benefit-allocation-principles]]: Nguyên tắc phân bổ chi phí và lợi ích của từng FTP portfolio cho các đơn vị kinh doanh.
- [[ftp-final-rate-determination]]: Xác định mức lãi suất FTP cuối cùng cho từng giao dịch sau khi tích hợp 4 chiều kích.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản theo Moorad Choudhry.
- [[practical-alm-liquidity-governance]]: Khung điều hành quản trị thanh khoản thực chiến.
- [[ftp-transmission-mechanism]]: Chi tiết các kênh truyền dẫn điều tiết của FTP.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa bảng cân đối ALM toàn diện.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.
- [[gap-risk]]: Rủi ro khe hở tái định giá lãi suất.
- [[non-maturity-deposits]]: Mô hình hóa hành vi tiền gửi không kỳ hạn CASA.
- [[behavioural-options]]: Quyền chọn trả nợ trước hạn và rút tiền gửi sớm.
- [[replicating-portfolio-model]]: Mô hình danh mục sao chép tiền gửi CASA.
