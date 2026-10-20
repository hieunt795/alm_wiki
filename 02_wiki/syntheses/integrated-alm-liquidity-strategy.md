---
title: "Chiến lược Quản trị Thanh khoản và Bảng cân đối Kế toán Tổng hợp LCR – NSFR tại ALM Treasury"
aliases: [Chiến lược Quản trị Tổng hợp LCR-NSFR, Integrated ALM Liquidity Strategy, Quản trị Bảng cân đối LCR NSFR, Chiến lược thanh khoản tích hợp]
type: synthesis
domains: [alm, basel]
status: active
maturity: draft
origin: query
question: "Làm thế nào để ALM Treasury và Hội đồng ALCO thiết kế một chiến lược quản trị tổng hợp có thể giải quyết triệt để các xung đột kỹ thuật, tối ưu hóa bảng cân đối kế toán đa mục tiêu trước hai ràng buộc pháp định song hành LCR >= 100% và NSFR >= 100%?"
as_of: 2026-10-17
sources: ["[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-bcbs-irrbb-2016]]", "[[src-lubinska-alm-optimisation]]", "[[src-tt50-2026-nhnn]]", "[[src-bcbs-liquidity-principles-2008]]"]
relations: []
tags: [alm-strategy, lcr, nsfr, irrbb, balance-sheet-optimization, alco, liquidity-ftp, collateral-waterfall]
updated: 2026-10-17
reviewed:
---

## Câu hỏi

Làm thế nào để Khối Quản trị Nguồn vốn & ALM (Treasury ALM) và Hội đồng Quản lý Tài sản - Nợ (ALCO) thiết kế và vận hành một **Chiến lược Quản trị Tổng hợp (*Integrated Balance Sheet & Liquidity Strategy*)** nhằm giải quyết các xung đột kỹ thuật, tối ưu hóa phân bổ nguồn lực và đáp ứng đồng thời hai ràng buộc pháp định song hành: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn ([[lcr]] $\ge 100\%$) và Tỷ lệ nguồn vốn ổn định ròng dài hạn ([[nsfr]] $\ge 100\%$)?

---

## Kết luận

1. **Từ Quản trị Đơn lẻ sang Quản trị Đa Ràng buộc Tích hợp**:
   - Nếu quản trị độc lập từng chỉ số, ngân hàng chắc chắn rơi vào các bẫy xung đột kỹ thuật: gia tăng vốn bán buôn 6–12 tháng để né dòng ra LCR nhưng làm mất 50% ASF trong NSFR; hoặc repo Trái phiếu Chính phủ dài hạn để lấy tiền mặt nhưng đẩy RSF của lô trái phiếu từ 5% vọt lên 100% [[src-bcbs-lcr#^lcr40-1]] [[src-bcbs-nsfr#^nsf30-13]] [[src-bcbs-nsfr#^nsf30-20]].
   - Chiến lược quản trị tổng hợp yêu cầu thiết lập **Mô hình Tối ưu hóa Bảng cân đối Kế toán Đa mục tiêu (*Multi-constraint Balance Sheet Optimization*)**, tìm kiếm cấu trúc tài sản - nợ tối ưu thỏa mãn đồng thời cả LCR, NSFR, Đòn bẩy (Leverage Ratio), Tỷ lệ An toàn Vốn (CAR) và Hạn mức Rủi ro Lãi suất (IRRBB duration) [[src-bcbs-lcr#^lcr20-1]] [[src-bcbs-nsfr#^nsf20-2]].
2. **Trục Điều phối Kinh tế: Cơ chế Định giá Điều chuyển Vốn Nội bộ Tích hợp (Integrated Multi-dimensional FTP)**:
   - FTP không còn là một mức lãi suất phẳng đơn kỳ hạn, mà được cấu thành từ 4 cấu phần phân rã: Lãi suất cơ sở (Base Rate) + Phí đệm thanh khoản ngắn hạn LCR + Phí/Thưởng vốn ổn định cấu trúc NSFR + Chi phí vốn tự có/RWA.
3. **Chiến lược Quản trị Tài sản Bảo đảm Phân tầng (Collateral Waterfall Strategy)**:
   - Khai thác triệt để "đòn bẩy kép" của Trái phiếu Chính phủ Level 1 (đóng góp 100% vào HQLA của LCR nhưng chỉ tiêu tốn 5% RSF của NSFR) bằng cách bảo tồn tuyệt đối trạng thái *unencumbered* [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-nsfr#^nsf30-26]].
   - Khi cần phát hành trái phiếu có bảo đảm (covered bonds) dài hạn $\ge 1$ năm, Treasury ưu tiên cầm cố các tài sản đã có hệ số RSF cao sẵn (như nợ vay thế chấp nhà ở RSF 65%, nợ vay doanh nghiệp RSF 85%) nhằm triệt tiêu tổn thất thanh khoản biên [[src-bcbs-nsfr#^nsf30-30]] [[src-bcbs-nsfr#^nsf30-31]].
4. **San bằng Thang Kỳ hạn Nợ Động (Dynamic Maturity Laddering)**:
   - Xây dựng Kế hoạch Tài trợ Cấu trúc (Structural Funding Plan) chia nhỏ và phát hành nợ dài hạn so le các năm; kích hoạt cửa sổ tái cấp vốn sớm (*Pre-funding Window*) tại tháng thứ 15 để hóa giải "hiệu ứng thác trôi kỳ hạn" (*roll-down cliff*) trước khi nợ trôi qua mốc 1 năm (mất 50% ASF), 6 tháng (mất 100% ASF) và 30 ngày (kích hoạt 100% dòng ra LCR) [[src-bcbs-nsfr#^nsf30-10]] [[src-bcbs-nsfr#^nsf30-14]] [[src-bcbs-lcr#^lcr40-42]].
5. **Ma trận Điều hành ALCO 4 Trạng thái (Cross-Metric ALCO Traffic-Light Matrix)**:
   - ALCO vận hành ma trận kết hợp 2 chiều LCR – NSFR, phân định rõ các kịch bản hành động chuẩn hóa cho từng vùng trạng thái (Green/Green, Amber/Green, Green/Amber, Red/Red).

---

## Khung Lý thuyết: Mô hình Tối ưu hóa Tuyến tính Bảng Cân đối Đa mục tiêu

ALM Treasury mô hình hóa bảng cân đối kế toán dưới dạng một bài toán quy hoạch toán học nhằm tối đa hóa lợi nhuận kỳ vọng sau điều chỉnh rủi ro, được cụ thể hóa tại [[balance-sheet-optimisation-model|Mô hình Tối ưu hóa Bảng cân đối Kế toán]] theo điều kiện Karush-Kuhn-Tucker (KKT) và thuật toán điểm trong (*Interior-point algorithm*) [[src-lubinska-alm-optimisation#^lubinska-u04-12]] [[src-lubinska-alm-optimisation#^lubinska-u04-13]]:

### 1. Hàm Mục tiêu (Objective Function)
Cực đại hóa Thu nhập Lãi thuần kỳ vọng ($\text{NII}$) hoặc Tỷ suất sinh lời trên vốn có điều chỉnh rủi ro ($\text{RoRWA}$):

$$
\max \; \Pi = \sum_{k} A_k \cdot y_k - \sum_{m} L_m \cdot c_m - \text{Operating Costs}
$$

Trong đó:
- $A_k, y_k$: Quy mô và lợi suất của danh mục tài sản $k$ (cho vay, TPCP, repo, liên ngân hàng).
- $L_m, c_m$: Quy mô và chi phí lãi của danh mục nguồn vốn $m$ (tiền gửi bán lẻ, tiền gửi doanh nghiệp, trái phiếu dài hạn, vay liên ngân hàng).

### 2. Hệ Ràng buộc Song hành (Simultaneous Regulatory Constraints)

$$\begin{cases}
\text{Cân bằng Kế toán:} & \sum_{k} A_k = \sum_{m} L_m + E \quad (E: \text{Vốn chủ sở hữu}) \\[8pt]
\text{Ràng buộc LCR:} & \displaystyle \frac{\sum_{k} A_k \cdot (1 - h_k)}{\sum_{m} L_m \cdot r_m^{\text{out}} - \min\Big(\sum_{k} A_k \cdot r_k^{\text{in}},\; 0.75 \times \text{Outflows}\Big)} \ge 100\% + \Delta_{\text{LCR}} \\[12pt]
\text{Ràng buộc NSFR:} & \displaystyle \frac{\sum_{m} L_m \cdot \text{ASF}_m + E \cdot 100\%}{\sum_{k} A_k \cdot \text{RSF}_k + \sum_{j} \text{OBS}_j \cdot 5\%} \ge 100\% + \Delta_{\text{NSFR}} \\[12pt]
\text{Ràng buộc Đòn bẩy:} & \displaystyle \frac{\text{Tier 1 Capital}}{\text{Total On- and Off-Balance Sheet Exposure}} \ge 3\% + \Delta_{\text{LR}} \\[8pt]
\text{Ràng buộc Outlier Test:} & \displaystyle \frac{\max_{i \in \{1..6\}} \Delta\text{EVE}_i}{\text{Tier 1 Capital}} \le 15\%
\end{cases}$$

Ràng buộc Outlier Test: xem [[outlier-bank-test]] và [[bcbs-irrbb]].

> **Ý nghĩa kinh tế**: Mỗi đồng tài sản được giải ngân hoặc mỗi đồng vốn được huy động đều đồng thời "tiêu hao" hoặc "bổ sung" các biến số trong cả 5 phương trình trên. Giải thuật tối ưu hóa xác định tỷ trọng tối ưu của từng loại tài sản và nợ trên bảng cân đối kế toán.

---

## Trục Điều phối: Cơ chế Định giá Điều chuyển Vốn Nội bộ Tích hợp (Multi-dimensional FTP)

Để truyền tải bài toán tối ưu hóa của ALCO xuống các chi nhánh và bàn kinh doanh, ALM Treasury vận hành cơ chế **Term Liquidity FTP Tích hợp**:

```
+-------------------------------------------------------------------------------+
|             CƠ CẤU PHÍ ĐỊNH GIÁ ĐIỀU CHUYỂN VỐN NỘI BỘ TÍCH HỢP (FTP)         |
+-------------------------------------------------------------------------------+
                                         |
     +-----------------+-----------------+-----------------+-----------------+
     |                 |                 |                 |                 |
     v                 v                 v                 v                 v
+----------------+ +----------------+ +----------------+ +----------------+ +----------------+
| LÃI SUẤT CƠ SỞ | | PHÍ ĐỆM LCR    | | PHÍ CẤU TRÚC   | | PHÍ VỐN & RWA  | | MARGIN KINH    |
| (Base Interest | | (Short-term    | | NSFR (Term     | | (Capital &     | | DOANH CHI NHÁNH|
|  Rate Curve)   | |  Liquidity)    | |  Liquidity FTP)| |  Buffer Charge)| | (Commercial    |
| Phản ánh đường | | Bù đắp chi phí | | Phạt RSF cao,  | | Chi phí đệm    | |  Spread/NIM)   |
| cong lợi suất  | | nắm giữ đệm    | | thưởng ASF bền | | vốn chủ sở hữu | |                |
| thị trường.    | | HQLA cấp tính. | | vững dài hạn.  | | theo Basel II. | |                |
+----------------+ +----------------+ +----------------+ +----------------+ +----------------+
```

### 1. Công thức Định giá Phân rã đối với Tài sản (Asset FTP Charge)
Mỗi khoản tín dụng hoặc đầu tư khi giải ngân sẽ chịu mức phí FTP tổng hợp:

$$
\text{FTP}_{\text{Asset}} = \text{Base Rate}(\text{Tenor}) + \text{LCR Charge} + \text{NSFR Charge} + \text{RWA Charge}
$$

Trong đó:
- **$\text{LCR Charge}$**: Áp dụng đối với các tài sản không tạo ra dòng tiền vào trong 30 ngày nhưng lại tiêu tốn thanh khoản:
  $$\text{LCR Charge} = \Big(1 - r^{\text{in}}\Big) \times \text{Spread}(\text{HQLA Buffer Carry})$$
- **$\text{NSFR Charge}$**: Khấu trừ chi phí duy trì nguồn vốn dài hạn tương ứng với hệ số RSF của tài sản:
  $$\text{NSFR Charge} = \text{RSF Factor} \times \text{Term Funding Spread}(\text{Tenor})$$
  - Cho vay BĐS thương mại ($\text{RSF} = 85\%$): Chịu phí bằng $85\% \times \text{Spread Trái phiếu 3–5 năm}$ [[src-bcbs-nsfr#^nsf30-31]].
  - Cho vay mua nhà ở xã hội ($\text{RSF} = 65\%$): Chịu phí bằng $65\% \times \text{Spread}$ [[src-bcbs-nsfr#^nsf30-30]].
  - Đầu tư TPCP Level 1 ($\text{RSF} = 5\%$): Chỉ chịu phí bằng $5\% \times \text{Spread}$ [[src-bcbs-nsfr#^nsf30-26]].

### 2. Công thức Trả thưởng đối với Nguồn vốn (Liability FTP Credit)
Mỗi khoản tiền gửi hoặc công cụ nợ huy động được Treasury trả thưởng thanh khoản nội bộ:

$$
\text{FTP Credit}_{\text{Liability}} = \text{Base Rate}(\text{Tenor}) + \text{LCR Benefit} + \text{NSFR Premium}
$$

- **Tiền gửi Bán lẻ Stable (CASA)**:
  - LCR Benefit: Nhận thưởng lớn vì chỉ có run-off 5% (tiết kiệm 95% đệm HQLA) [[src-bcbs-lcr#^lcr40-7]].
  - NSFR Premium: Nhận thưởng tối đa nhờ đóng góp $\text{ASF} = 95\%$ [[src-bcbs-nsfr#^nsf30-11]].
  - $\rightarrow$ Chi nhánh có động lực kinh tế cực lớn để phát triển tệp khách hàng trả lương mở tài khoản thanh toán.
- **Tiền gửi Liên ngân hàng $< 6$ tháng**:
  - LCR Benefit = 0% (do run-off 100% nếu $\le 30$ ngày) [[src-bcbs-lcr#^lcr40-42]].
  - NSFR Premium = 0% (do $\text{ASF} = 0\%$) [[src-bcbs-nsfr#^nsf30-14]].
  - $\rightarrow$ Triệt tiêu hoàn toàn NIM của các phòng kinh doanh muốn dùng vốn vay liên ngân hàng ngắn hạn để báo cáo tăng trưởng tài sản ảo.

---

## Ba Trụ cột Tác nghiệp Thực chiến tại ALM Treasury

```
+---------------------------------------------------------------------------------------+
|             BA TRỤ CỘT TÁC NGHIỆP TỔNG HỢP LCR - NSFR TẠI ALM TREASURY                |
+---------------------------------------------------------------------------------------+
                                           |
    +--------------------------------------+--------------------------------------+
    |                                                                             |
    v                                                                             v
+---------------------------------------------+ +---------------------------------------------+
| TRỤ CỘT 1: THÁC PHÂN BỔ TÀI SẢN THẾ CHẤP    | | TRỤ CỘT 2: BẬC THANG PHÁT HÀNH NỢ ĐỘNG      |
|           (COLLATERAL WATERFALL)            | |       (DYNAMIC MATURITY LADDERING)          |
| - Ưu tiên cầm cố tài sản có RSF cao sẵn     | | - Chia nhỏ các lô phát hành trái phiếu dài  |
|   (cho vay nhà ở 65%, cho vay DN 85%).      | |   hạn so le các kỳ hạn (2Y, 3Y, 4Y, 5Y).    |
| - Tuyệt đối bảo tồn trạng thái unencumbered | | - Kích hoạt Pre-funding Window trước        |
|   cho TPCP Level 1 để giữ RSF 5% & HQLA 100%| |   15 tháng (trước khi trôi qua mốc 1 năm).  |
+---------------------------------------------+ +---------------------------------------------+
                                           |
                                           v
+---------------------------------------------------------------------------------------+
| TRỤ CỘT 3: TÁI CẤU TRÚC DANH MỤC CAM KẾT NGOẠI BẢNG VÀ TỐI ƯU HÓA HQLA                |
| - Chuyển đổi Liquidity Facilities (LCR 30%-100%) sang Credit Facilities (LCR 10%).    |
| - Thu hồi các hạn mức tín dụng ngủ đông (dormant lines) để giảm 5% RSF ngoại bảng.    |
| - Khống chế tài sản Level 2 dưới trần 40% của LCR để triệt tiêu phần RSF chết.       |
+---------------------------------------------------------------------------------------+
```

### Trụ cột 1: Thác Phân bổ Tài sản Thế chấp (Collateral Waterfall)
Nhằm giải quyết triệt để **Cạm bẫy cầm cố tài sản dài hạn (Encumbrance Trap)** đã phân tích tại [[lcr-nsfr-interlinkages]], ALM Treasury thiết lập quy tắc thác phân bổ tài sản bảo đảm khi cần huy động vốn có bảo đảm hoặc phát hành trái phiếu có bảo đảm (Covered Bonds) dài hạn $\ge 1$ năm:
1. **Ưu tiên số 1**: Sử dụng các khoản cho vay mua nhà ở (Residential Mortgages) đã chịu $\text{RSF} = 65\%$ hoặc các khoản cho vay thương mại chịu $\text{RSF} = 85\%$ [[src-bcbs-nsfr#^nsf30-30]] [[src-bcbs-nsfr#^nsf30-31]].
   - *Lý do*: Khi bị encumbered $\ge 1$ năm, hệ số RSF tăng lên 100%, mức tăng thêm chỉ là $+35\%$ (đối với nhà ở) hoặc $+15\%$ (đối với nợ DN). Khoản vốn dài hạn nhận về (ASF 100%) thừa sức bù đắp cho mức tăng này và tạo ra thặng dư thanh khoản ròng lớn.
2. **Quy tắc Cấm kỵ**: Tuyệt đối không đem Trái phiếu Chính phủ Level 1 đi cầm cố với kỳ hạn $\ge 1$ năm.
   - *Hậu quả*: Đẩy RSF vọt từ 5% lên 100% (tăng $+95\%$), làm biến mất hoàn toàn giá trị thặng dư của khoản nợ dài hạn nhận về, đồng thời tước đoạt tư cách HQLA trong LCR [[src-bcbs-lcr#^lcr30-24]] [[src-bcbs-nsfr#^nsf30-20]].
3. **Quản trị Repo ngắn hạn**: Chỉ thực hiện các hợp đồng repo tài sản Level 1 với kỳ hạn dưới 6 tháng để bảo đảm hệ số RSF vẫn được giữ nguyên ở mức 5% [[src-bcbs-nsfr#^nsf30-20]].

---

### Trụ cột 2: Bậc thang Phát hành Nợ Động (Dynamic Maturity Laddering)
Nhằm ngăn ngừa **Hiệu ứng thác trôi kỳ hạn (Roll-down Cliff)**:
1. **Phát hành So le Đa kỳ hạn (*Staggered Issuance*)**:
   - Thay vì phát hành một lô trái phiếu duy nhất 10.000 tỷ VND kỳ hạn 5 năm, Treasury phát hành chia nhỏ thành 4 lô 2.500 tỷ VND với các kỳ hạn 2 năm, 3 năm, 4 năm và 5 năm.
   - Mỗi năm ngân hàng chỉ có đúng 2.500 tỷ VND nợ trôi qua mốc 1 năm và 6 tháng, xóa bỏ hiện tượng sụt giảm đột ngột tỷ lệ NSFR.
2. **Quy tắc Tái tài trợ Sớm 15 Tháng (*15-Month Pre-funding Window*)**:
   - Bộ phận Treasury ALM thiết lập hệ thống cảnh báo tự động khi bất kỳ lô nợ dài hạn nào bước vào khoảng thời gian còn lại 15 tháng.
   - Kế hoạch phát hành lô trái phiếu mới để thay thế bắt buộc phải hoàn tất trong khoảng thời gian từ tháng thứ 15 đến tháng thứ 13, đảm bảo dòng vốn mới (ASF 100%) được nạp đầy vào bảng cân đối kế toán **trước khi lô nợ cũ chạm mốc 365 ngày** (bị tụt hệ số xuống 50%) [[src-bcbs-nsfr#^nsf30-10]] [[src-bcbs-nsfr#^nsf30-13]].

---

### Trụ cột 3: Tái cấu trúc Cam kết Ngoại bảng và Kiểm soát Trần HQLA
1. **Tái cấu trúc Hợp đồng Tín dụng Doanh nghiệp**:
   - Rà soát các hợp đồng cấp hạn mức tín dụng cho các tập đoàn lớn: chuyển dịch tối đa các điều khoản cam kết hỗ trợ thanh khoản (Liquidity Facilities - chịu dòng ra LCR 30%–100%) sang hạn mức tài trợ vốn lưu động xoay vòng thông thường (Credit Facilities - chỉ chịu dòng ra LCR 10%) [[src-bcbs-lcr#^lcr40-61]] [[src-bcbs-lcr#^lcr40-64]].
   - Chấm dứt hoặc giảm hạn mức đối với các cam kết tín dụng "ngủ đông" (*dormant facilities*) không phát sinh giao dịch thực tế, trực tiếp cắt giảm 5% mẫu số RSF ngoại bảng trong NSFR [[src-bcbs-nsfr#^nsf30-34]].
2. **Kiểm soát Tỷ trọng Level 2 trong Kho HQLA**:
   - Theo dõi sát sao trần unwinding 40% của Level 2 và trần 15% của Level 2B [[src-bcbs-lcr#^lcr30-37]].
   - Ngay khi danh mục Level 2A chạm ngưỡng 35% tổng HQLA, ALM Treasury dừng giải ngân mua mới trái phiếu doanh nghiệp và chuyển toàn bộ dòng vốn tái đầu tư sang Trái phiếu Chính phủ Level 1, tránh hiện tượng tài sản Level 2 vượt trần tiêu tốn 15%–50% RSF mà không mang lại giá trị gia tăng nào cho LCR.

---

### Căn cứ BCBS 144 cho ba trụ cột
- Trụ cột 1 (tài sản thế chấp): ngân hàng nên quản lý vị thế tài sản bảo đảm, phân biệt tài sản bị cầm cố và không bị cầm cố [[src-bcbs-liquidity-principles-2008#^lrm-p09]], và có đủ tài sản bảo đảm cho nhu cầu vay dự kiến, bất ngờ và cho mức ký quỹ tăng thêm [[src-bcbs-liquidity-principles-2008#^lrm-91]]. Xem [[asset-encumbrance]].
- Trụ cột 2 (bậc thang phát hành): mục tiêu đa dạng hoá nên nằm trong kế hoạch funding trung và dài hạn, gồm hạn mức theo đối tác, có/không bảo đảm, loại công cụ, đồng tiền và thị trường [[src-bcbs-liquidity-principles-2008#^lrm-65]]; không nên giả định tiếp cận kịp thời thị trường mà ngân hàng chưa dùng định kỳ [[src-bcbs-liquidity-principles-2008#^lrm-69]]. Xem [[funding-concentration-risk]].
- Trụ cột 3 (đệm và cam kết ngoại bảng): quy mô đệm gắn với nhu cầu thanh khoản trong stress [[src-bcbs-liquidity-principles-2008#^lrm-123]]; đệm là tuyến dự phòng, không phải tuyến đầu [[src-bcbs-liquidity-principles-2008#^lrm-126]]; cam kết chưa giải ngân, thư tín dụng, bảo lãnh tài chính là nguồn hao hụt vốn tiềm tàng đáng kể [[src-bcbs-liquidity-principles-2008#^lrm-41]]. Xem [[committed-facilities]].
- Thanh khoản trong ngày nên được quản lý chủ động trong cả điều kiện bình thường và stress [[src-bcbs-liquidity-principles-2008#^lrm-p08]]; xem [[intraday-liquidity-risk]].

*Diễn giải:* BCBS 144 cho nguyên tắc định tính, mô hình tối ưu hoá ở các mục trên cho cách định lượng. Câu "đệm là tuyến dự phòng" đồng nghĩa với việc trụ cột 2 (cấu trúc funding) là tuyến đầu; ALCO không nên dùng đệm HQLA để bù cho cấu trúc funding yếu.

## Ma trận Điều hành ALCO Liên chỉ số (Cross-Metric ALCO Decision Matrix)

Hội đồng ALCO quản trị thanh khoản tổng thể thông qua ma trận 4 góc trạng thái phối hợp:

```
                  LCR >= 110% (Green)                 LCR < 105% (Amber / Red)
            +-----------------------------------+-----------------------------------+
            |                                   |                                   |
NSFR >= 110%|          VÙNG TỐI ƯU              |    VÙNG THIẾU HỤT CẤP TÍNH        |
(Green)     |       (Balanced Growth)           |     (Acute Stress / Normal ALM)   |
            | - Bảng cân đối an toàn toàn diện. | - Cấu trúc dài hạn tốt nhưng gặp  |
            | - Cho phép mở rộng giải ngân tín  |   cú sốc dòng tiền ngắn hạn 30D.  |
            |   dụng trung dài hạn theo kế hoạch| - HÀNH ĐỘNG: Bơm thanh khoản qua  |
            | - Duy trì phân bổ TPCP Level 1.   |   repo OMO, thanh lý Level 1;     |
            |                                   |   KHÔNG cần phát hành nợ dài hạn. |
            +-----------------------------------+-----------------------------------+
            |                                   |                                   |
NSFR < 103% |    VÙNG MẤT CÂN ĐỐI CẤU TRÚC      |        VÙNG KHỦNG HOẢNG KÉP       |
(Amber/Red) |       (Structural Vulnerability)  |       (Dual Liquidity Crisis)     |
            | - Thanh khoản 30D dồi dào nhưng   | - Cạn kiệt cả đệm HQLA lẫn nguồn  |
            |   chênh lệch kỳ hạn 1Y quá lớn!   |   vốn tài trợ cấu trúc dài hạn.   |
            | - Nguy cơ rủi ro như mô hình SVB. | - HÀNH ĐỘNG: Triệu tập ALCO khẩn  |
            | - HÀNH ĐỘNG: Đóng băng cho vay    |   cấp; kích hoạt đồng thời CFP    |
            |   dài hạn; tăng lãi suất huy động |   và Structural Capital Recovery; |
            |   trái phiếu/tiền gửi dài hạn;    |   báo cáo Cơ quan Giám sát (NHNN/ |
            |   tăng phí RSF Charge trong FTP.  |   BCBS) theo quy định.            |
            +-----------------------------------+-----------------------------------+
```

### Kịch bản Hành động Chi tiết cho từng Vùng Trạng thái:

1. **Vùng Thiếu hụt Cấp tính (LCR Amber/Red, NSFR Green)**:
   - *Bản chất*: Ngân hàng có cấu trúc tài trợ dài hạn rất vững chắc (NSFR $> 110\%$), nhưng gặp một đợt rút tiền đột biến trong 30 ngày hoặc có các lô nợ lớn đáo hạn cùng lúc khiến LCR tụt dốc.
   - *Sai lầm thường gặp*: Vội vàng phát hành trái phiếu dài hạn (vừa tốn chi phí lãi suất, vừa làm thừa thãi NSFR).
   - *Hành động đúng của Treasury*: Thực hiện các giao dịch hoán đổi tài sản bảo đảm (*collateral swap*) hoặc repo ngắn hạn $< 30$ ngày với NHTW để bổ sung tiền mặt HQLA tức thì; sử dụng đệm dự trữ bắt buộc tại NHTW [[src-bcbs-lcr#^lcr20-5]] [[src-bcbs-lcr#^lcr40-47]].
2. **Vùng Mất cân đối Cấu trúc (LCR Green, NSFR Amber/Red)**:
   - *Bản chất*: Ngân hàng dư thừa thanh khoản ngắn hạn (nhiều tiền mặt, liên ngân hàng qua đêm) nhưng lại tài trợ cho danh mục tài sản dài hạn bằng tiền gửi doanh nghiệp nhạy cảm lãi suất. Đây chính là trạng thái của Silicon Valley Bank trước khi sụp đổ năm 2023.
   - *Hành động đúng của Treasury*:
     - Tăng biểu phí RSF Charge trong FTP để ngăn chặn các chi nhánh giải ngân các gói vay trung dài hạn mới.
     - Phát hành trái phiếu ngân hàng kỳ hạn 2–5 năm (ASF 100%) để thay thế nguồn vốn ngắn hạn [[src-bcbs-nsfr#^nsf30-10]].
     - Triển khai chiến dịch huy động tiền gửi tiết kiệm dân cư kỳ hạn $\ge 1$ năm có điều khoản phạt nặng khi rút trước hạn [[src-bcbs-nsfr#^nsf30-10]].

---

## Bằng chứng Thực nghiệm & Khuyến nghị Triển khai tại Việt Nam

### 1. Bài học Quản trị Bảng Cân đối từ Khủng hoảng SVB (2023)
- Silicon Valley Bank duy trì tỷ lệ thanh khoản tức thì có vẻ ổn định trong điều kiện bình thường, nhưng cấu trúc bảng cân đối kế toán vi phạm nghiêm trọng nguyên lý cân bằng LCR – NSFR:
  - Nắm giữ danh mục đầu tư chứng khoán HTM/AFS khổng lồ kỳ hạn 10–30 năm (đòi hỏi nguồn vốn ổn định $\text{RSF} = 65\%\text{–}85\%$).
  - Nguồn vốn tài trợ lại chủ yếu là tiền gửi không kỳ hạn của các doanh nghiệp công nghệ không có quan hệ thanh toán operational thực chất (trong NSFR chỉ nhận $\text{ASF} = 50\%$, và khi có tin đồn rút tiền, run-off thực tế vọt lên 100% chỉ trong 48 giờ).
  - *Bài học ALM*: Nếu SVB vận hành ma trận điều hành tích hợp LCR – NSFR, hệ thống hạn mức đã cảnh báo đỏ về sự mất cân đối cấu trúc từ nhiều quý trước khi vụ sụp đổ diễn ra.

### 2. Khuyến nghị Thực thi cho Ngân hàng Thương mại Việt Nam
Trước thềm áp dụng tỷ lệ NSFR theo lộ trình Thông tư 50/2026/TT-NHNN từ ngày **01/10/2028** [[src-tt50-2026-nhnn#^d13-1]] [[src-tt50-2026-nhnn#^d22-2]]:
1. **Thiết lập Bộ phận ALM chuyên trách Quản trị Tích hợp**:
   - Hợp nhất việc theo dõi tỷ lệ LCR, NSFR và tỷ lệ tối đa nguồn vốn ngắn hạn cho vay trung dài hạn (S/L Ratio) về một đầu mối duy nhất tại Phòng ALM Treasury.
2. **Nâng cấp Hệ thống Core Banking & Dữ liệu Giao dịch**:
   - Bóc tách tự động dữ liệu hợp đồng: phân định tiền gửi bán lẻ, SME hợp nhất $< 1$M EUR, tiền gửi doanh nghiệp thông thường và tiền gửi định chế tài chính; gắn cờ chính xác điều khoản phạt rút trước hạn và quyền chọn mua lại (*call options*).
3. **Hiện đại hóa Hệ thống Liquidity FTP Đa chiều**:
   - Chuyển đổi từ mô hình FTP phẳng sang mô hình FTP đa cấu phần, đưa trực tiếp hệ số RSF và LCR run-off vào công thức tính lợi nhuận sau điều chỉnh rủi ro (RAROC) của từng sản phẩm và từng giám đốc quan hệ khách hàng (RM).
4. **Xây dựng Bảng Cân đối Kế toán Mục tiêu (Target Balance Sheet)**:
   - Vận hành mô hình [[synthetic-balance-sheet-liquidity-risk]] để giải bài toán quy hoạch tuyến tính đa ràng buộc, thiết lập tỷ trọng tối ưu giữa tài sản thanh khoản HQLA, dư nợ tín dụng và các tầng nguồn vốn huy động.
5. **Vận hành Khuôn khổ Giám sát Thanh khoản Đa tầng (Basel SRP50)**:
   - Tích hợp LCR, NSFR với thang kỳ hạn hợp đồng [[contractual-maturity-mismatch]], quản trị rủi ro tập trung nguồn vốn [[funding-concentration-risk]], kho tài sản sạch [[available-unencumbered-assets]], tỷ lệ [[lcr-by-currency]] và kiểm soát thanh khoản trong ngày [[intraday-liquidity-risk]] (chi tiết tại [[basel-liquidity-monitoring-framework]]).

## Bất định
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M6: đã có node [[concentration-risk-management]]; TT83 Đ50–52 không đặt hạn mức tập trung nguồn vốn [[src-tt83-2025-nhnn#^d50-1]], chỉ có yếu tố tập trung huy động vốn trong stress thanh khoản [[src-tt83-2025-nhnn#^d48-3]]; cần rà lại chỗ nhắc funding concentration và góc nhìn VN.
- [2026-10-19] ingest src-tata-bank-alm u07: đã có node [[silicon-valley-bank]] có nguồn (số liệu bảng cân đối, phòng ngừa, duration gap 3 năm, giả định duration tiền gửi) [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-9]]; cần rà lại chỗ nhắc SVB, đối chiếu số liệu và thay bằng citation.
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: [[alco]] thêm best practice FSA/PRA SS1/13 và ToR Choudhry (CFO chủ tịch, họp hằng tháng, báo cáo Board, pari passu với ExCo) đối chiếu TT83 (giúp việc TGĐ, tối thiểu hằng quý), MI pack có NII/NIM sensitivity và basis risk; cần rà lại phần quản trị ALCO.
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: [[balance-sheet-optimisation-model]] thêm trình bày Choudhry: tích hợp thanh khoản và IRRBB thay vì silo, ChoudWest tiết kiệm 0,6 tỷ USD/năm; cần rà lại mục tối ưu hoá bảng cân đối.
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: đã có node [[asset-encumbrance]] (gone-concern, 6 tỷ lệ đo, contingent encumbrance); cần rà lại chỗ nhắc encumbrance.
- [2026-10-20] ingest src-bcbs-framework SRP30: [[concentration-risk-management]] thêm góc nhìn Basel SRP30: SRP30.22 liệt kê nguồn vốn là một tình huống tập trung, còn TT83 Đ50 không đưa vào; cần rà lại phần tập trung nguồn vốn.
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → R2 đã rà [2026-10-20]: câu về nghĩa vụ LCR/NSFR tại VN đã dẫn TT50 Đ13.1, Đ16.1.c, Đ22.2.
- [2026-10-20] ingest src-tt50-2026-nhnn PL2: [[available-stable-funding]], [[required-stable-funding]], [[nsfr]] có hệ số ASF/RSF của VN (khác Basel: tiền gửi bán lẻ ≥ 1 năm được rút trước hạn chỉ 95%/90%; phải đòi Chính phủ/KBNN RSF 50–65%; add-on nợ phái sinh 10%); cần rà lại các ví dụ tính NSFR và bảng hệ số.
- [2026-10-20] ingest src-tt50-2026-nhnn PL1: [[lcr]], [[hqla]], [[cash-outflows]], [[retail-deposit-stability]], [[level-1-assets]], [[level-2-assets]] có hệ số VN (HQLA cấp 1/2A/2B 100/85/75–50%, run-off bán lẻ 5%/10%, tiền gửi ngoại tệ luôn kém ổn định, DNNVV ≤ 30 tỷ đồng, cổ phiếu VN30 vào cấp 2B); cần rà lại ví dụ tính LCR và bảng hệ số.
