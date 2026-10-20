---
title: Level 2 assets
aliases: [Level 2 assets, Tài sản cấp 2, Level 2 HQLA]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr30-43]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "+", cite: "[[src-bcbs-lcr#^lcr30-43]]"}
tags: [liquidity, hqla, level-2]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

Level 2 assets là lớp tài sản thanh khoản bổ sung trong danh mục [[hqla]] của [[lcr]], bao gồm **Level 2A assets** và **Level 2B assets** (được áp dụng tùy theo quyết định của cơ quan giám sát quốc gia - national discretion) [[src-bcbs-lcr#^lcr30-31]]. Khác biệt cốt lõi so với [[level-1-assets]]:
1. Toàn bộ tài sản Level 2 phải chịu mức chiết khấu định giá bắt buộc (**haircuts**) từ **15% đến 50%** để phản ánh rủi ro thị trường và biến động giá khi bị thanh lý cưỡng bức [[src-bcbs-lcr#^lcr30-43]] [[src-bcbs-lcr#^lcr30-45]].
2. Bị khống chế bởi hệ thống **trần tỷ trọng kép (two-tier caps)**: Tổng Level 2 tối đa **40%**, trong đó Level 2B tối đa **15%** tổng danh mục HQLA sau khi đã áp dụng cơ chế hoàn trả (unwind) các giao dịch tài trợ ngắn hạn [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-34]].

### Chi tiết các cấu phần của Level 2A assets (Haircut 15%)

Tài sản Level 2A được áp dụng mức haircut cố định **15%** trên giá trị thị trường hiện hành và bao gồm 3 nhóm tài sản thỏa mãn các tiêu chí định tính và định lượng khắt khe [[src-bcbs-lcr#^lcr30-43]]:

| Nhóm tài sản Level 2A | Tiêu chuẩn chất lượng tín dụng | Tiêu chuẩn thanh khoản thị trường & Kiểm định stress | Điều kiện loại trừ nghiêm ngặt |
|---|---|---|---|
| **1. Chứng khoán công hệ số rủi ro 20%** | Phát hành hoặc bảo lãnh bởi chính phủ, NHTW, PSE, hoặc MDBs có hệ số rủi ro 20% theo CRE20 [[src-bcbs-lcr#^lcr30-43]]. | Giao dịch trên thị trường giao ngay/repo sâu rộng; mức sụt giảm giá tối đa không quá **10%** (hoặc haircut tăng không quá 10 điểm %) trong 30 ngày stress thanh khoản [[src-bcbs-lcr#^lcr30-43]]. | Không phải là nghĩa vụ nợ của một định chế tài chính hoặc pháp nhân liên kết (trừ khi là PSE) [[src-bcbs-lcr#^lcr30-43]]. |
| **2. Trái phiếu doanh nghiệp (Corporate Debt & CP)** | Xếp hạng tín nhiệm dài hạn từ tổ chức định mức tín nhiệm được công nhận (ECAI) tối thiểu **AA-** (hoặc xếp hạng ngắn hạn tương đương, hoặc PD nội bộ tương đương AA-) [[src-bcbs-lcr#^lcr30-43]]. | Cấu trúc thông thường (plain vanilla, không chuyển đổi, không thứ cấp); mức sụt giá thị trường tối đa không quá **10%** trong thời kỳ 30 ngày stress [[src-bcbs-lcr#^lcr30-43]]. | Tuyệt đối không do ngân hàng, công ty chứng khoán, bảo hiểm hoặc tổ chức tài chính liên kết phát hành [[src-bcbs-lcr#^lcr30-43]]. |
| **3. Trái phiếu có bảo đảm (Covered Bonds)** | Xếp hạng tín nhiệm ECAI tối thiểu **AA-** (hoặc PD tương đương) [[src-bcbs-lcr#^lcr30-43]]. | Phát hành bởi tổ chức tín dụng chịu sự giám sát đặc biệt của luật định nhằm bảo vệ trái chủ; cover pool đạt chuẩn; mức sụt giá tối đa không quá **10%** trong 30 ngày stress [[src-bcbs-lcr#^lcr30-43]]. | Không do chính ngân hàng báo cáo hoặc bất kỳ pháp nhân liên kết nào của ngân hàng phát hành [[src-bcbs-lcr#^lcr30-43]]. |

### Chi tiết các cấu phần của Level 2B assets (Haircuts 25% – 50%)

Supervisor quốc gia có toàn quyền quyết định cho phép hoặc không cho phép đưa Level 2B vào HQLA. Khi được phê chuẩn, danh mục Level 2B giới hạn trong các nhóm tài sản sau [[src-bcbs-lcr#^lcr30-45]]:

| Cấu phần Level 2B | Haircut | Tiêu chuẩn chất lượng tín dụng & Tài sản cơ sở | Kiểm định biến động giá stress 30 ngày | Tiêu chuẩn bổ sung & Loại trừ |
|---|---|---|---|---|
| **1. Chứng khoán đảm bảo bằng thế chấp nhà ở (RMBS)** | **25%** [[src-bcbs-lcr#^lcr30-45]] | - Xếp hạng ECAI tối thiểu **AA** [[src-bcbs-lcr#^lcr30-45]].<br>- Khoản vay thế chấp cơ sở là **full recourse** (người vay chịu trách nhiệm bằng toàn bộ tài sản cá nhân) [[src-bcbs-lcr#^lcr30-45]].<br>- Tỷ lệ LTV bình quân gia quyền tối đa **$\le 80\%$** tại thời điểm phát hành RMBS [[src-bcbs-lcr#^lcr30-45]]. | Mức sụt giảm giá tối đa không vượt quá **20%** (hoặc haircut tăng không quá 20 điểm %) trong 30 ngày stress [[src-bcbs-lcr#^lcr30-45]]. | - Không do chính ngân hàng hoặc công ty con khởi tạo (originate).<br>- **Cấm tuyệt đối**: Chứng khoán bảo đảm nợ thế chấp thương mại (CMBS), CDO, CLO, ABCP bị loại hoàn toàn. |
| **2. Trái phiếu doanh nghiệp (BBB- đến A+)** | **50%** [[src-bcbs-lcr#^lcr30-45]] | Plain vanilla corporate bonds và giấy tờ có giá ngắn hạn (CP) có rating dài hạn từ **BBB- đến A+** (thuộc dải đầu tư thấp hơn) [[src-bcbs-lcr#^lcr30-45]]. | Mức sụt giảm giá tối đa không vượt quá **20%** trong 30 ngày stress [[src-bcbs-lcr#^lcr30-45]]. | Không do định chế tài chính hoặc pháp nhân liên kết tài chính phát hành [[src-bcbs-lcr#^lcr30-45]]. |
| **3. Chứng khoán công BBB- đến BBB+** | **50%** [[src-bcbs-lcr#^lcr30-45]] | Nợ khả nhượng của chính phủ, NHTW, PSE có xếp hạng tín nhiệm trong dải từ **BBB- đến BBB+** [[src-bcbs-lcr#^lcr30-45]]. | Mức sụt giảm giá tối đa không quá **20%** trong 30 ngày stress [[src-bcbs-lcr#^lcr30-45]]. | Thị trường giao dịch tích cực, minh bạch thông tin. |
| **4. Cổ phiếu phổ thông (Common Equity Shares)** | **50%** [[src-bcbs-lcr#^lcr30-45]] | Cổ phiếu phổ thông giao dịch tập trung, là thành phần của **chỉ số chứng khoán chính (major stock index)** tại quốc gia sở tại [[src-bcbs-lcr#^lcr30-45]]. | Mức sụt giảm giá tối đa không vượt quá **40%** trong 30 ngày stress thị trường [[src-bcbs-lcr#^lcr30-45]]. | - Giao dịch bằng **đồng nội tệ**.<br>- Bù trừ qua Trung tâm Thanh toán Bù trừ Tập trung đủ điều kiện (QCCP).<br>- Cấm cổ phiếu của các định chế tài chính. |
| **5. Hạn mức thanh khoản cam kết có hạn chế (RCLF)** | Thỏa thuận [[src-bcbs-lcr#^lcr30-46]] | Hạn mức cam kết thanh khoản chưa giải ngân (undrawn) do NHTW cung cấp cho các tài sản thế chấp đủ điều kiện [[src-bcbs-lcr#^lcr30-46]]. | Không áp dụng biến động thị trường. | - Phí cam kết hàng năm tối thiểu bằng $\max(75\text{ bps},\; \Delta\text{Yield} + 25\text{ bps})$ [[src-bcbs-lcr#^lcr30-46]].<br>- Thế chấp bằng tài sản unencumbered, hợp đồng không thể hủy ngang trước hạn ngoài 30 ngày. |
| **6. Sản phẩm tài chính Hồi giáo (Sukuk)** | Supervisor quyết định [[src-bcbs-lcr#^lcr30-47]] | Các công cụ tài chính tuân thủ Shari'ah (như Sukuk) được supervisor quốc gia công nhận riêng cho các ngân hàng Hồi giáo [[src-bcbs-lcr#^lcr30-47]]. | Theo điều kiện quản trị của supervisor sở tại. | Chỉ áp dụng cho ngân hàng hoạt động theo nguyên tắc Hồi giáo. |

## Công thức & tham số

### Cơ chế tính toán sau Unwind và Thuật toán xác định Trần (LCR30.34–30.39)
*(Chi tiết chuyên sâu về cơ chế Unwind, các bút toán tài sản bảo đảm và 4 ca nghiên cứu số học xem tại: [[hqla-unwinding-mechanism]])*.

#### 1. Tại sao bắt buộc phải Unwind?
Nếu chỉ tính trần 40% và 15% trên số dư sổ sách tại ngày báo cáo, ngân hàng có thể thực hiện giao dịch repo ngắn hạn (ví dụ repo Level 2 để lấy tiền mặt hoặc Level 1 ngay trước ngày chốt số liệu), từ đó che giấu việc nắm giữ thực tế vượt trần. Basel yêu cầu giả định **hoàn trả (unwind)** toàn bộ các giao dịch tài trợ có bảo đảm và hoán đổi tài sản bảo đảm kỳ hạn $\le 30$ ngày để xác định lượng tài sản thực tế:
- $\text{Adjusted Level 1}$: Số dư Level 1 sau khi unwind.
- $\text{Adjusted Level 2A}$: Số dư Level 2A (sau haircut 15%) sau khi unwind.
- $\text{Adjusted Level 2B}$: Số dư Level 2B (sau haircut tương ứng) sau khi unwind.

#### 2. Công thức toán học tính khoản khấu trừ do vượt trần

**Bước 1: Khấu trừ vượt trần 15% của Level 2B ($Adjustment_{15\%}$)**:
$$Adjustment_{15\%} = \max\left(\text{Adjusted L2B} - \frac{15}{85}(\text{Adjusted L1} + \text{Adjusted L2A}),\;\; \text{Adjusted L2B} - \frac{15}{60}\text{Adjusted L1},\;\; 0\right)$$
- Hệ số $\frac{15}{85}$ áp dụng khi trần tổng thể 40% của Level 2 chưa bị chạm (vì khi Level 2B chiếm 15% thì phần còn lại là Level 1 + Level 2A chiếm $100\% - 15\% = 85\%$).
- Hệ số $\frac{15}{60} = \frac{1}{4}$ áp dụng khi trần tổng thể 40% của Level 2 bị chạm (khi đó Level 1 bắt buộc phải chiếm ít nhất 60% tổng HQLA, nên Level 2B tối đa bằng $\frac{15\%}{60\%} = \frac{1}{4}$ Level 1).

**Bước 2: Khấu trừ vượt trần tổng thể 40% của Level 2 ($Adjustment_{40\%}$)**:
$$Adjustment_{40\%} = \max\left(\big(\text{Adjusted L2A} + \text{Adjusted L2B} - Adjustment_{15\%}\big) - \frac{2}{3}\text{Adjusted L1},\;\; 0\right)$$
- Do Level 2 tối đa chiếm 40% tổng HQLA thì Level 1 tối thiểu chiếm 60%, tỷ lệ trần Level 2 so với Level 1 là $\frac{40}{60} = \frac{2}{3}$.

**Bước 3: Giá trị HQLA cuối cùng đưa vào tử số LCR**:
$$\text{Stock of HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - Adjustment_{15\%} - Adjustment_{40\%}$$

#### 3. Bảng minh họa số học tính Cap Unwind
Giả sử ngân hàng sau khi unwind có số liệu:
- $\text{Adjusted L1} = 100$
- Trường hợp A (Không vượt trần): $\text{Adjusted L2A} = 30$, $\text{Adjusted L2B} = 10$.
  - Kiểm tra 15%: $10 \le \frac{15}{85}(100 + 30) = 22.94 \implies Adjustment_{15\%} = 0$.
  - Kiểm tra 40%: $(30 + 10) = 40 \le \frac{2}{3}(100) = 66.67 \implies Adjustment_{40\%} = 0$.
  - Tổng HQLA = $100 + 30 + 10 = 140$ (được công nhận 100%).
- Trường hợp B (Bị trần Level 2B khống chế): $\text{Adjusted L2A} = 20$, $\text{Adjusted L2B} = 35$.
  - Kiểm tra 15%: $\text{L2B} - \frac{15}{85}(100 + 20) = 35 - 21.18 = 13.82$.
  - $Adjustment_{15\%} = 13.82 \implies \text{L2B sau trừ} = 21.18$.
  - Kiểm tra 40%: $(20 + 21.18) = 41.18 \le \frac{2}{3}(100) = 66.67 \implies Adjustment_{40\%} = 0$.
  - Khoản bị loại bỏ khỏi HQLA là 13.82.
- Trường hợp C (Bị trần tổng 40% khống chế): $\text{Adjusted L2A} = 60$, $\text{Adjusted L2B} = 20$.
  - Mức trần tổng Level 2 tối đa $= \frac{2}{3} \times 100 = 66.67$.
  - Tổng Level 2 nắm giữ $= 60 + 20 = 80 \implies$ Vượt trần và bị loại bỏ $80 - 66.67 = 13.33$.

## Diễn giải

### Cơ chế & drivers

#### Quy tắc ân hạn 30 ngày (Cliff-Edge Relief - LCR30.28)
Khi một tài sản trong danh mục Level 2 bị hạ bậc tín nhiệm dẫn đến vi phạm tiêu chuẩn (ví dụ trái phiếu doanh nghiệp Level 2A bị hạ từ AA- xuống A+, hoặc Level 2B bị hạ từ BBB- xuống BB+), Basel cho phép ngân hàng được **giữ tài sản đó trong danh mục HQLA thêm 30 ngày dương lịch** kể từ ngày hạ bậc [[src-bcbs-lcr#^lcr30-28]]. Quy tắc này nhằm ngăn ngừa hiệu ứng vách đá (cliff effect) buộc ngân hàng phải bán tháo tài sản ra thị trường trong hoảng loạn làm trầm trọng thêm khủng hoảng thanh khoản.

#### Tác động tới dòng tiền mẫu số của LCR (LCR40)
Haircut của tài sản Level 2 được phản chiếu nhất quán sang tỷ lệ dòng tiền trong mẫu số:
- **Huy động vốn có bảo đảm ([[secured-funding]])**: Khoản vay có bảo đảm bằng Level 2 đáo hạn trong 30 ngày phải chịu tỷ lệ rút vốn tương đương với mức haircut:
  - Bảo đảm bằng Level 2A: Tỷ lệ rút tiền là **15%** [[src-bcbs-lcr#^lcr40-48]].
  - Bảo đảm bằng RMBS Level 2B: Tỷ lệ rút tiền là **25%** [[src-bcbs-lcr#^lcr40-48]].
  - Bảo đảm bằng tài sản Level 2B khác: Tỷ lệ rút tiền là **50%** [[src-bcbs-lcr#^lcr40-48]].
- **Cho vay có bảo đảm (Reverse repo)**: Giao dịch cho vay nhận tài sản bảo đảm là Level 2 đáo hạn trong 30 ngày đem lại dòng tiền vào tương ứng với haircut của tài sản nhận về (ví dụ nhận Level 2A đem lại dòng tiền vào **15%**, nhận Level 2B khác đem lại dòng vào **50%**) [[src-bcbs-lcr#^lcr40-78]].

### Phụ thuộc regime
- **Regime bình thường**: Bộ phận Treasury duy trì tỷ trọng Level 2 trong phạm vi an toàn (thường $\le 30-35\%$ Level 2 và $\le 10-12\%$ Level 2B) để tạo đệm dự phòng (buffer headroom), tránh nguy cơ bị trừng phạt khấu trừ trần khi số dư Level 1 biến động trong tháng [[src-bcbs-lcr#^lcr30-34]].
- **Regime stress thanh khoản**:
  - Khi ngân hàng sử dụng tài sản Level 1 trước tiên để bù đắp dòng tiền ra, tỷ lệ $\text{Level 2} / \text{Level 1}$ sẽ tăng cơ học, có thể kích hoạt các khoản khấu trừ $Adjustment_{40\%}$ và $Adjustment_{15\%}$, làm tử số HQLA sụt giảm phi tuyến tính.
  - Ngân hàng có thể tận dụng quy tắc ân hạn 30 ngày khi các công cụ Level 2 bị biến động rating trên thị trường [[src-bcbs-lcr#^lcr30-28]].

### Bằng chứng thực nghiệm
- Trong các đợt khủng hoảng thị trường, thanh khoản của trái phiếu doanh nghiệp BBB- và RMBS suy giảm đột ngột hơn nhiều so với trái phiếu chính phủ, chênh lệch giá mua-bán (bid-ask spread) giãn rộng từ 3 đến 5 lần. Điều này lý giải tại sao Basel áp dụng mức haircut rất nặng (50%) và trần khống chế nghiêm ngặt (15%) đối với nhóm Level 2B [[src-bcbs-lcr#^lcr30-2]] [[src-bcbs-lcr#^lcr30-45]].

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **Basel**: Cung cấp quyền tự quyết cho supervisor (national discretion) đối với việc chấp nhận Level 2B, nhưng đặt ra các hàng rào kỹ thuật nghiêm ngặt (full recourse, LTV $\le 80\%$, kiểm định sụt giá 10%–40%, cấm nợ định chế tài chính) nhằm bảo vệ tính toàn vẹn của đệm thanh khoản [[src-bcbs-lcr#^lcr30-43]] [[src-bcbs-lcr#^lcr30-45]].
- **ALM / Quản trị bảng cân đối**:
  - *Lợi suất chênh lệch (Yield Pick-up)*: Nắm giữ trái phiếu doanh nghiệp và cổ phiếu Level 2 đem lại lợi suất danh mục cao hơn rõ rệt so với trái phiếu chính phủ Level 1, hỗ trợ [[net-interest-margin|NIM]].
  - *Chi phí vốn rủi ro tín dụng (RWA)*: Trái phiếu doanh nghiệp Level 2A chịu hệ số rủi ro tín dụng từ 20% đến 50%, trái phiếu Level 2B chịu RW từ 50% đến 100%, và cổ phiếu chịu RW 100% đến 250% theo Basel III. Bộ phận ALM phải cân đối giữa lợi ích thanh khoản LCR và chi phí tiêu hao vốn tự có (Tier 1 capital).
  - *Tác động NSFR*: Trong tỷ lệ NSFR, tài sản Level 2A unencumbered chịu hệ số RSF là 15%, trong khi Level 2B chịu RSF là 50% (đòi hỏi ngân hàng phải có nguồn vốn ổn định tài trợ tương ứng), cao hơn nhiều so với mức 0% của Level 1.
- **VN**: theo [[tt50-2026|TT50/2026]], cấp 2A (hệ số 85%) gồm chứng khoán Chính phủ/NHTW/PSE nước ngoài, tổ chức quốc tế có hệ số rủi ro tối đa 20% và chứng khoán nợ doanh nghiệp phi tài chính từ AA-, đều niêm yết, giảm giá tối đa 10% [[src-tt50-2026-nhnn#^pl1-a3]]. Cấp 2B gồm RMBS từ AA (75%), chứng khoán nợ doanh nghiệp từ BBB- (50%), chứng khoán Chính phủ nước ngoài BBB- (50%) và cổ phiếu phổ thông phi tài chính thuộc VN30 hoặc chỉ số quan trọng (50%) [[src-tt50-2026-nhnn#^pl1-a4]]. Trái phiếu chính quyền địa phương dùng trong giao dịch NHNN thuộc cấp 1, không phải cấp 2A [[src-tt50-2026-nhnn#^pl1-a2]].

## Câu hỏi mở
- Thị trường chứng khoán hóa nợ mua nhà (RMBS) tại Việt Nam hiện chưa phát triển và chưa có chuẩn tín nhiệm nội địa cho RMBS, liệu TT50/2026 có áp dụng cấu phần RMBS của Level 2B không?
- Cổ phiếu trong rổ VN30 tại Việt Nam có thỏa mãn đầy đủ các tiêu chuẩn về độ sâu thanh khoản và kiểm định mức sụt giảm giá tối đa không quá 40% trong stress [[src-bcbs-lcr#^lcr30-45]] hay không?

## Xem thêm
- Chi tiết thuật toán và các kịch bản số học Unwind: [[hqla-unwinding-mechanism]]
- Phân tích tổng hợp chuyên sâu và đánh đổi chiến lược ALM Treasury: [[hqla-decomposition-and-tradeoffs]]
