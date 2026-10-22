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
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]", "[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr30-43]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "+", cite: "[[src-bcbs-lcr#^lcr30-43]]"}
tags: [liquidity, hqla, level-2]
updated: 2026-10-22
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
| **3. Chứng khoán công BBB- đến BBB+** | **50%** [[src-bcbs-lcr#^lcr30-45-faq3]] | Chứng khoán chính phủ/NHTW xếp hạng **BBB+ đến BBB-** không thuộc Level 1 theo LCR30.41(4)–(5), trong trần 15% [[src-bcbs-lcr#^lcr30-45-faq3]]; chứng khoán PSE từ BBB- [[src-bcbs-lcr#^lcr30-45-faq4]]. | PSE: giảm giá tối đa **20%** trong 30 ngày stress [[src-bcbs-lcr#^lcr30-45-faq4]]. | PSE phải đáp ứng các yêu cầu khác của LCR30.45(2) [[src-bcbs-lcr#^lcr30-45-faq4]]. Nhóm này nằm trong FAQ, không nằm trong danh mục LCR30.45 (*Diễn giải*). |
| **4. Cổ phiếu phổ thông (Common Equity Shares)** | **50%** [[src-bcbs-lcr#^lcr30-45]] | Cổ phiếu phổ thông giao dịch tập trung, là thành phần của **chỉ số chứng khoán chính (major stock index)** tại quốc gia sở tại [[src-bcbs-lcr#^lcr30-45]]. | Mức sụt giảm giá tối đa không vượt quá **40%** trong 30 ngày stress thị trường [[src-bcbs-lcr#^lcr30-45]]. | - Giao dịch bằng **đồng nội tệ**.<br>- Bù trừ qua Trung tâm Thanh toán Bù trừ Tập trung đủ điều kiện (QCCP).<br>- Cấm cổ phiếu của các định chế tài chính. |
| **5. Hạn mức thanh khoản cam kết có hạn chế (RCLF)** | Thỏa thuận [[src-bcbs-lcr#^lcr30-46]] | Hạn mức cam kết thanh khoản chưa giải ngân (undrawn) do NHTW cung cấp cho các tài sản thế chấp đủ điều kiện [[src-bcbs-lcr#^lcr30-46]]. | Không áp dụng biến động thị trường. | - Phí cam kết hàng năm tối thiểu bằng $\max(75\text{ bps},\; \Delta\text{Yield} + 25\text{ bps})$ [[src-bcbs-lcr#^lcr30-46]].<br>- Thế chấp bằng tài sản unencumbered, hợp đồng không thể hủy ngang trước hạn ngoài 30 ngày. |
| **6. Sản phẩm tài chính Hồi giáo (Sukuk)** | Supervisor quyết định [[src-bcbs-lcr#^lcr30-47]] | Các công cụ tài chính tuân thủ Shari'ah (như Sukuk) được supervisor quốc gia công nhận riêng cho các ngân hàng Hồi giáo [[src-bcbs-lcr#^lcr30-47]]. | Theo điều kiện quản trị của supervisor sở tại. | Chỉ áp dụng cho ngân hàng hoạt động theo nguyên tắc Hồi giáo. |

### Danh mục tài sản cấp 2 theo TT50/2026 (PL1 Phần A Mục III–IV, Bảng 3 mục 2)

Theo TT50/2026, tài sản cấp 2 gồm cấp 2A và cấp 2B [[src-tt50-2026-nhnn#^d19-1]]. Trong Bảng 3, dòng 2.1 là tổng các mục 2.1.1 đến 2.1.3, cột (4) cho ra Level 2A và cột (5) cho ra KĐC.L2A [[src-tt50-2026-nhnn#^pl1-a5-2a]]. Dòng 2.2 là tổng các mục 2.2.1 đến 2.2.5, cho ra Level 2B và KĐC.L2B [[src-tt50-2026-nhnn#^pl1-a5-2b]]. Cấp 2A có hệ số 85%, trừ khi NHNN yêu cầu hệ số thấp hơn [[src-tt50-2026-nhnn#^pl1-a3]] [[src-tt50-2026-nhnn#^pl1-a2-2]]. Cấp 2B có hệ số theo từng loại tài sản; NHNN có quyền hạ hệ số hoặc không cho tính tài sản vào cấp 2B [[src-tt50-2026-nhnn#^pl1-a4-1]]. TT50 có hiệu lực từ 01/10/2026; LCR áp dụng từ 01/10/2028 theo lộ trình [[src-tt50-2026-nhnn#^d13-1]].

| Mục Bảng 3 | Điểm | Tài sản (theo câu chữ TT50) | Hệ số | Điều kiện | Nguồn |
|---|---|---|---|---|---|
| 2.1.1 | 3a Mục III | Chứng khoán của Chính phủ, NHTW, PSE nước ngoài hoặc tổ chức tài chính quốc tế, hoặc được các đối tượng này bảo đảm | 85% | Đủ 4 điều kiện: (i) hệ số rủi ro ≤ 20% theo phương pháp tiêu chuẩn; (ii) niêm yết; (iii) lịch sử 10 năm, giảm giá hoặc tăng chiết khấu ≤ 10% trong 30 ngày căng thẳng; (iv) không do tổ chức tài chính hoặc công ty mẹ, con, liên kết phát hành | [[src-tt50-2026-nhnn#^pl1-a3-3a]] [[src-tt50-2026-nhnn#^pl1-a5-2a]] |
| 2.1.2 | 3b Mục III | Chứng khoán nợ doanh nghiệp | 85% | Đủ 4 điều kiện: (i) không do tổ chức tài chính hoặc công ty mẹ, con, liên kết phát hành; (ii) xếp hạng tín nhiệm độc lập từ AA-; (iii) niêm yết; (iv) lịch sử 10 năm, giảm giá ≤ 10% | [[src-tt50-2026-nhnn#^pl1-a3-3b]] [[src-tt50-2026-nhnn#^pl1-a5-2a]] |
| 2.1.3 | 3c Mục III | Tài sản trong danh mục HQLA của chi nhánh ở nước ngoài của NHTM | 85% | Phải đủ điều kiện HQLA cấp 2A đủ tiêu chuẩn theo TT50 | [[src-tt50-2026-nhnn#^pl1-a3-3c]] [[src-tt50-2026-nhnn#^pl1-a5-2a]] |
| 2.2.1 | 3a Mục IV | RMBS | 75% | Đủ 8 điều kiện: (i) không do ngân hàng hoặc công ty mẹ, con, liên kết phát hành; (ii) khoản phải đòi cơ sở không do các đối tượng này tạo lập; (iii) xếp hạng độc lập từ AA; (iv) niêm yết; (v) giảm giá ≤ 20%; (vi) tài sản cơ sở chỉ là khoản phải đòi thế chấp nhà ở, không gồm sản phẩm có cấu trúc; (vii) có quyền truy đòi, LTV trung bình ≤ 80% khi phát hành; (viii) chứng khoán hoá tuân thủ pháp luật nước thực hiện | [[src-tt50-2026-nhnn#^pl1-a4-3a]] [[src-tt50-2026-nhnn#^pl1-a5-2b]] |
| 2.2.2 | 3b Mục IV | Chứng khoán nợ doanh nghiệp | 50% | Đủ 4 điều kiện: (i) không do tổ chức tài chính phát hành; (ii) xếp hạng độc lập từ BBB-; (iii) niêm yết; (iv) giảm giá ≤ 20% | [[src-tt50-2026-nhnn#^pl1-a4-3b]] [[src-tt50-2026-nhnn#^pl1-a5-2b]] |
| 2.2.3 | 3c Mục IV | Chứng khoán của Chính phủ, NHTW, PSE nước ngoài hoặc tổ chức tài chính quốc tế, trừ chứng khoán đã đủ điều kiện cấp 1, 2A | 50% | Đủ 4 điều kiện: (i) xếp hạng độc lập từ BBB- và hệ số rủi ro ≤ 50%; (ii) niêm yết; (iii) giảm giá ≤ 20%; (iv) không do tổ chức tài chính phát hành | [[src-tt50-2026-nhnn#^pl1-a4-3c]] [[src-tt50-2026-nhnn#^pl1-a5-2b]] |
| 2.2.4 | 3d Mục IV | Cổ phiếu phổ thông | 50% | Đủ 5 điều kiện: (i) không do tổ chức tài chính phát hành; (ii) thuộc VN30 hoặc chỉ số chứng khoán quan trọng do cơ quan có thẩm quyền quyết định; (iii) phát hành bằng VNĐ hoặc đồng tiền nơi ngân hàng có rủi ro thanh khoản; (iv) niêm yết và thanh toán bù trừ tập trung; (v) giảm giá ≤ 40% | [[src-tt50-2026-nhnn#^pl1-a4-3d]] [[src-tt50-2026-nhnn#^pl1-a4]] [[src-tt50-2026-nhnn#^pl1-a5-2b]] |
| 2.2.5 | 3đ Mục IV | Tài sản trong danh mục HQLA của chi nhánh ở nước ngoài của NHTM | Theo từng loại | Phải đủ điều kiện HQLA cấp 2B đủ tiêu chuẩn theo TT50 | [[src-tt50-2026-nhnn#^pl1-a4-3dd]] [[src-tt50-2026-nhnn#^pl1-a5-2b]] |

Mọi đầu mục còn phải đáp ứng yêu cầu vận hành Đ20.2 [[src-tt50-2026-nhnn#^d20-2]]. Đối chiếu tiêu chí từng mục với Basel: mục `### Tiêu chí xác định theo đầu mục Bảng 3 TT50` bên dưới.

## Công thức & tham số

### Cơ chế tính toán sau Unwind và Thuật toán xác định Trần (LCR30.34–30.39)
*(Chi tiết chuyên sâu về cơ chế Unwind, các bút toán tài sản bảo đảm và 4 ca nghiên cứu số học xem tại: [[hqla-unwinding-mechanism]])*.

#### 1. Tại sao bắt buộc phải Unwind?
Trần 40% và 15% tính sau haircut và sau khi unwind giao dịch tài trợ có bảo đảm, cho vay có bảo đảm và hoán đổi tài sản bảo đảm ngắn hạn [[src-bcbs-lcr#^lcr30-34]]. *Diễn giải:* nếu chỉ tính trần trên số dư sổ sách tại ngày báo cáo, ngân hàng có thể thực hiện giao dịch repo ngắn hạn (ví dụ repo Level 2 để lấy tiền mặt hoặc Level 1 ngay trước ngày chốt số liệu), từ đó che giấu việc nắm giữ thực tế vượt trần. Basel yêu cầu giả định **hoàn trả (unwind)** toàn bộ các giao dịch tài trợ có bảo đảm và hoán đổi tài sản bảo đảm kỳ hạn $\le 30$ ngày để xác định lượng tài sản thực tế:
- $\text{Adjusted Level 1}$: Số dư Level 1 sau khi unwind [[src-bcbs-lcr#^lcr30-37]].
- $\text{Adjusted Level 2A}$: Số dư Level 2A (sau haircut 15%) sau khi unwind.
- $\text{Adjusted Level 2B}$: Số dư Level 2B (sau haircut tương ứng) sau khi unwind.

#### 2. Công thức toán học tính khoản khấu trừ do vượt trần

**Bước 1: Khấu trừ vượt trần 15% của Level 2B ($Adjustment_{15\%}$)**:
$$Adjustment_{15\%} = \max\left(\text{Adjusted L2B} - \frac{15}{85}(\text{Adjusted L1} + \text{Adjusted L2A}),\;\; \text{Adjusted L2B} - \frac{15}{60}\text{Adjusted L1},\;\; 0\right)$$
[[src-bcbs-lcr#^lcr30-34]]
- *Diễn giải:* hệ số $\frac{15}{85}$ áp dụng khi trần tổng thể 40% của Level 2 chưa bị chạm (vì khi Level 2B chiếm 15% thì phần còn lại là Level 1 + Level 2A chiếm $100\% - 15\% = 85\%$).
- *Diễn giải:* hệ số $\frac{15}{60} = \frac{1}{4}$ áp dụng khi trần tổng thể 40% của Level 2 bị chạm (khi đó Level 1 bắt buộc phải chiếm ít nhất 60% tổng HQLA, nên Level 2B tối đa bằng $\frac{15\%}{60\%} = \frac{1}{4}$ Level 1).

**Bước 2: Khấu trừ vượt trần tổng thể 40% của Level 2 ($Adjustment_{40\%}$)**:
$$Adjustment_{40\%} = \max\left(\big(\text{Adjusted L2A} + \text{Adjusted L2B} - Adjustment_{15\%}\big) - \frac{2}{3}\text{Adjusted L1},\;\; 0\right)$$
[[src-bcbs-lcr#^lcr30-34]]
- *Diễn giải:* do Level 2 tối đa chiếm 40% tổng HQLA [[src-bcbs-lcr#^lcr30-31]] thì Level 1 tối thiểu chiếm 60%, tỷ lệ trần Level 2 so với Level 1 là $\frac{40}{60} = \frac{2}{3}$.

**Bước 3: Giá trị HQLA cuối cùng đưa vào tử số LCR**:
$$\text{Stock of HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - Adjustment_{15\%} - Adjustment_{40\%}$$
[[src-bcbs-lcr#^lcr30-34]] [[src-tt50-2026-nhnn#^pl1-a1]]

#### 3. Bảng minh họa số học tính Cap Unwind
*Diễn giải:* ví dụ giả định (số tự đặt, áp công thức ở trên). Giả sử ngân hàng sau khi unwind có số liệu:
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
Haircut của tài sản Level 2 được phản chiếu sang tỷ lệ dòng tiền trong mẫu số [[src-bcbs-lcr#^lcr40-48]] [[src-bcbs-lcr#^lcr40-78]]:
- **Huy động vốn có bảo đảm ([[secured-funding]])**: Khoản vay có bảo đảm bằng Level 2 đáo hạn trong 30 ngày phải chịu tỷ lệ rút vốn bằng mức haircut [[src-bcbs-lcr#^lcr40-48]]:
  - Bảo đảm bằng Level 2A: Tỷ lệ rút tiền là **15%** [[src-bcbs-lcr#^lcr40-48]].
  - Bảo đảm bằng RMBS Level 2B: Tỷ lệ rút tiền là **25%** [[src-bcbs-lcr#^lcr40-48]].
  - Bảo đảm bằng tài sản Level 2B khác: Tỷ lệ rút tiền là **50%** [[src-bcbs-lcr#^lcr40-48]].
- **Cho vay có bảo đảm (Reverse repo)**: Giao dịch cho vay nhận tài sản bảo đảm là Level 2 đáo hạn trong 30 ngày đem lại dòng tiền vào tương ứng với haircut của tài sản nhận về (ví dụ nhận Level 2A đem lại dòng tiền vào **15%**, nhận Level 2B khác đem lại dòng vào **50%**) [[src-bcbs-lcr#^lcr40-78]].

### Phụ thuộc regime
- **Regime bình thường**: Bộ phận Treasury duy trì tỷ trọng Level 2 trong phạm vi an toàn để tạo đệm dự phòng (buffer headroom) dưới trần 40% và 15% [[src-bcbs-lcr#^lcr30-31]]. *Diễn giải:* (ngoài wiki, chưa có nguồn) mức nội bộ kiểu $\le 30-35\%$ Level 2 và $\le 10-12\%$ Level 2B là ví dụ thực hành, tránh khấu trừ trần khi số dư Level 1 biến động trong tháng.
- **Regime stress thanh khoản**:
  - *Diễn giải:* khi ngân hàng sử dụng tài sản Level 1 trước tiên để bù đắp dòng tiền ra, tỷ lệ $\text{Level 2} / \text{Level 1}$ sẽ tăng cơ học, có thể kích hoạt các khoản khấu trừ $Adjustment_{40\%}$ và $Adjustment_{15\%}$, làm tử số HQLA sụt giảm phi tuyến tính.
  - Ngân hàng có thể tận dụng quy tắc ân hạn 30 ngày khi các công cụ Level 2 bị biến động rating trên thị trường [[src-bcbs-lcr#^lcr30-28]].

### Bằng chứng thực nghiệm
- Trong các đợt khủng hoảng thị trường, thanh khoản của trái phiếu doanh nghiệp BBB- và RMBS suy giảm đột ngột hơn nhiều so với trái phiếu chính phủ, chênh lệch giá mua-bán (bid-ask spread) giãn rộng từ 3 đến 5 lần. Điều này lý giải tại sao Basel áp dụng mức haircut rất nặng (50%) và trần khống chế nghiêm ngặt (15%) đối với nhóm Level 2B [[src-bcbs-lcr#^lcr30-2]] [[src-bcbs-lcr#^lcr30-45]].

## Basel vs VN

| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Tên gọi | Level 2A, Level 2B [[src-bcbs-lcr#^lcr30-31]] | Tài sản cấp 2A, cấp 2B [[src-tt50-2026-nhnn#^d19-1]] | LCR30.31 / TT50 Đ19.1 | VN: LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Trần cấp 2 | Tối đa 40% HQLA; Level 2B tối đa 15% [[src-bcbs-lcr#^lcr30-31]] | KĐC40% (2/3 cấp 1), KĐC15% (15/85, 15/60) sau đảo ngược [[src-tt50-2026-nhnn#^pl1-a1]] | LCR30.34 / TT50 PL1.A.I.2–3 | |
| Level 2B có trong danh mục? | Theo quyết định của cơ quan quốc gia; supervisor phải bảo đảm tài sản đáp ứng đủ tiêu chí [[src-bcbs-lcr#^lcr30-44]] | Có sẵn trong danh mục; NHNN có quyền hạ hệ số hoặc không cho tính tài sản vào cấp 2B [[src-tt50-2026-nhnn#^pl1-a4-1]] | LCR30.33 / TT50 PL1.A.IV.1–2 | |
| Quyền hạ hệ số 2A | LCR30.43 không có quyền tương ứng; quyền yêu cầu haircut ở LCR30.40 chỉ áp cho Level 1 [[src-bcbs-lcr#^lcr30-40]] (*Diễn giải*) | NHNN có quyền yêu cầu hệ số thấp hơn [[src-tt50-2026-nhnn#^pl1-a2-2]] | TT50 PL1.A.III.2 | |
| 2A: chứng khoán công | Hệ số rủi ro 20%, haircut 15% [[src-bcbs-lcr#^lcr30-43]] | Hệ số rủi ro tối đa 20%, hệ số thanh khoản 85% [[src-tt50-2026-nhnn#^pl1-a3]]; niêm yết, không do tổ chức tài chính phát hành [[src-tt50-2026-nhnn#^pl1-a3-3]] | LCR30.43 / TT50 PL1.A.III.3.a | |
| 2A: trái phiếu doanh nghiệp | Từ AA-, haircut 15% [[src-bcbs-lcr#^lcr30-43]] | Từ AA-, 85% [[src-tt50-2026-nhnn#^pl1-a3]]; niêm yết, không do tổ chức tài chính phát hành [[src-tt50-2026-nhnn#^pl1-a3-3]] | LCR30.43 / TT50 PL1.A.III.3.b | |
| 2A: covered bond | Từ AA-, không do chính ngân hàng phát hành [[src-bcbs-lcr#^lcr30-43]] | Không có trong danh mục cấp 2A [[src-tt50-2026-nhnn#^pl1-a3-3]] | LCR30.43 / TT50 PL1.A.III.3 | |
| 2A: biến động giá | Giảm giá ≤ 10% trong 30 ngày stress [[src-bcbs-lcr#^lcr30-43]] | Giảm giá hoặc tăng chiết khấu ≤ 10% trong 30 ngày căng thẳng, lịch sử 10 năm [[src-tt50-2026-nhnn#^pl1-a3-3]] | LCR30.43 / TT50 PL1.A.III.3 | |
| 2B: RMBS | Từ AA, full recourse, LTV ≤ 80%, haircut 25% [[src-bcbs-lcr#^lcr30-45]]; LTV là bình quân gia quyền của pool tại thời điểm phát hành RMBS [[src-bcbs-lcr#^lcr30-45-faq1]] | Từ AA, có quyền truy đòi, LTV trung bình ≤ 80%, không sản phẩm cấu trúc, không do ngân hàng phát hành hoặc tạo lập, giảm giá ≤ 20%; hệ số 75% [[src-tt50-2026-nhnn#^pl1-a4-3a]] | LCR30.45 / TT50 PL1.A.IV.3.a | |
| 2B: trái phiếu doanh nghiệp | BBB- đến A+, haircut 50% [[src-bcbs-lcr#^lcr30-45]] | Từ BBB-, niêm yết, giảm giá ≤ 20%; hệ số 50% [[src-tt50-2026-nhnn#^pl1-a4-3b]] | LCR30.45 / TT50 PL1.A.IV.3.b | |
| 2B: chứng khoán công | Chính phủ/NHTW BBB+ đến BBB- không thuộc Level 1, haircut 50% [[src-bcbs-lcr#^lcr30-45-faq3]]; PSE từ BBB-, giảm giá ≤ 20% [[src-bcbs-lcr#^lcr30-45-faq4]] | Chính phủ/NHTW/PSE nước ngoài, tổ chức tài chính quốc tế từ BBB- và hệ số rủi ro ≤ 50%, trừ loại đã đủ cấp 1, 2A; hệ số 50% [[src-tt50-2026-nhnn#^pl1-a4-3c]] | TT50 PL1.A.IV.3.c | |
| 2B: cổ phiếu | Chỉ số chính nội địa, giảm giá ≤ 40%, haircut 50% [[src-bcbs-lcr#^lcr30-45]]; chỉ số ở nước sở tại hoặc nơi có rủi ro thanh khoản qua chi nhánh, pháp nhân; tiêu chí 40% áp mọi cổ phiếu, giai đoạn stress do quốc gia chọn; danh sách chỉ số do cơ quan quốc gia quyết định [[src-bcbs-lcr#^lcr30-45-faq5]] | VN30 hoặc chỉ số quan trọng; bằng VNĐ hoặc đồng tiền nơi có rủi ro thanh khoản; niêm yết, thanh toán bù trừ tập trung; giảm giá ≤ 40%; hệ số 50% [[src-tt50-2026-nhnn#^pl1-a4-3d]] | LCR30.45 / TT50 PL1.A.IV.3.d | |
| 2B: RCLF | Supervisor có thể đưa hạn mức NHTW (RCLF) vào Level 2B [[src-bcbs-lcr#^lcr30-46]] | Không có trong danh mục cấp 2B; hạn mức với NHNN bảo đảm bằng HQLA cấp 1 được coi là cấp 1 [[src-tt50-2026-nhnn#^pl1-a1-4]] | LCR30.46 / TT50 PL1.A.I.4 | |
| Sukuk | Supervisor có thể công nhận cho ngân hàng Hồi giáo [[src-bcbs-lcr#^lcr30-47]]; sản phẩm Shari'ah đã đạt chuẩn HQLA thì mọi ngân hàng được tính [[src-bcbs-lcr#^lcr30-47-faq]] | Không có [[src-tt50-2026-nhnn#^pl1-a5]] | LCR30.47 / TT50 Bảng 3 | |
| Tài sản của chi nhánh ở nước ngoài | LCR30.43–30.45 không có đầu mục tương ứng (*Diễn giải*) | Tài sản HQLA của chi nhánh ở nước ngoài đủ điều kiện cấp 2A (85%) [[src-tt50-2026-nhnn#^pl1-a3-3c]] hoặc cấp 2B (hệ số theo từng loại) [[src-tt50-2026-nhnn#^pl1-a4-3dd]] | TT50 PL1.A.III.3.c, IV.3.đ | |

### Tiêu chí xác định theo đầu mục Bảng 3 TT50

Áp cho mọi đầu mục: yêu cầu vận hành Đ20.2 [[src-tt50-2026-nhnn#^d20-2]]; hệ số rủi ro và xếp hạng tín nhiệm độc lập theo quy định tỷ lệ an toàn vốn ngân hàng đang áp dụng (TT14/2025 hoặc TT41/2016) [[src-tt50-2026-nhnn#^pl1-a1-6]]. NHNN có quyền yêu cầu hệ số thấp hơn cho cấp 2A [[src-tt50-2026-nhnn#^pl1-a2-2]], và hạ hệ số hoặc không cho tính tài sản vào cấp 2B [[src-tt50-2026-nhnn#^pl1-a4-1]]. Cột "Giảm giá tối đa" là mức giảm giá hoặc tăng chiết khấu tối đa trong 30 ngày căng thẳng, trên lịch sử thị trường 10 năm (hoặc thời gian tối đa có dữ liệu).

| Mục | Tài sản | Tổ chức phát hành / bảo đảm | Hệ số rủi ro / xếp hạng | Niêm yết | Giảm giá tối đa | Loại trừ, điều kiện khác | Hệ số | Basel tương ứng |
|---|---|---|---|---|---|---|---|---|
| 2.1.1 | Chứng khoán công nước ngoài, tổ chức tài chính quốc tế [[src-tt50-2026-nhnn#^pl1-a3-3a]] | Chính phủ, NHTW, PSE nước ngoài hoặc tổ chức tài chính quốc tế; phát hành hoặc bảo đảm [[src-tt50-2026-nhnn#^pl1-a3-3a]] | Hệ số rủi ro ≤ 20% [[src-tt50-2026-nhnn#^pl1-a3-3a]] | Phải niêm yết [[src-tt50-2026-nhnn#^pl1-a3-3a]] | ≤ 10% [[src-tt50-2026-nhnn#^pl1-a3-3a]] | Không do tổ chức tài chính hoặc công ty mẹ, con, liên kết phát hành [[src-tt50-2026-nhnn#^pl1-a3-3a]] | 85% [[src-tt50-2026-nhnn#^pl1-a5-2a]] | Chính phủ/NHTW/PSE/MDB hệ số rủi ro 20%; giảm giá ≤ 10%; haircut 15% [[src-bcbs-lcr#^lcr30-43]]; thị trường lớn, sâu, sôi động; không là nghĩa vụ của tổ chức tài chính [[src-bcbs-lcr#^lcr30-43a]]. Không yêu cầu niêm yết (*Diễn giải*) |
| 2.1.2 | Chứng khoán nợ doanh nghiệp [[src-tt50-2026-nhnn#^pl1-a3-3b]] | Doanh nghiệp | Xếp hạng độc lập từ AA- [[src-tt50-2026-nhnn#^pl1-a3-3b]] | Phải niêm yết [[src-tt50-2026-nhnn#^pl1-a3-3b]] | ≤ 10% [[src-tt50-2026-nhnn#^pl1-a3-3b]] | Không do tổ chức tài chính hoặc công ty mẹ, con, liên kết phát hành [[src-tt50-2026-nhnn#^pl1-a3-3b]] | 85% [[src-tt50-2026-nhnn#^pl1-a5-2a]] | Trái phiếu doanh nghiệp, kể cả CP, plain-vanilla; xếp hạng ECAI từ AA- hoặc PD nội bộ tương đương; không do tổ chức tài chính phát hành; thị trường lớn, sâu, sôi động; giảm giá ≤ 10%; haircut 15% [[src-bcbs-lcr#^lcr30-43b]] |
| — | Covered bond | Không có trong danh mục cấp 2A [[src-tt50-2026-nhnn#^pl1-a3-3]] | | | | | | Từ AA-, không do chính ngân hàng phát hành; haircut 15% [[src-bcbs-lcr#^lcr30-43]] |
| 2.1.3 | Tài sản HQLA của chi nhánh ở nước ngoài [[src-tt50-2026-nhnn#^pl1-a3-3c]] | | | | | Phải đủ điều kiện HQLA cấp 2A đủ tiêu chuẩn theo TT50 [[src-tt50-2026-nhnn#^pl1-a3-3c]] | 85% [[src-tt50-2026-nhnn#^pl1-a5-2a]] | Không có đầu mục tương ứng (*Diễn giải*) |
| 2.2.1 | RMBS [[src-tt50-2026-nhnn#^pl1-a4-3a]] | Không do chính ngân hàng hoặc công ty mẹ, con, liên kết phát hành; khoản phải đòi cơ sở không do các đối tượng này tạo lập [[src-tt50-2026-nhnn#^pl1-a4-3a]] | Xếp hạng độc lập từ AA [[src-tt50-2026-nhnn#^pl1-a4-3a]] | Phải niêm yết [[src-tt50-2026-nhnn#^pl1-a4-3a]] | ≤ 20% [[src-tt50-2026-nhnn#^pl1-a4-3a]] | Tài sản cơ sở là khoản phải đòi thế chấp nhà ở, không gồm sản phẩm có cấu trúc; có quyền truy đòi; LTV trung bình ≤ 80% khi phát hành; chứng khoán hoá tuân thủ pháp luật nước thực hiện [[src-tt50-2026-nhnn#^pl1-a4-3a]] | 75% [[src-tt50-2026-nhnn#^pl1-a4-3a]] | Không do ngân hàng phát hành, tài sản cơ sở không do ngân hàng khởi tạo; từ AA; thị trường lớn, sâu, sôi động; giảm giá ≤ 20%; chỉ vay thế chấp nhà ở, không sản phẩm cấu trúc; full recourse; LTV bình quân ≤ 80% khi phát hành; chịu quy định risk retention; haircut 25% [[src-bcbs-lcr#^lcr30-45a]] |
| 2.2.2 | Chứng khoán nợ doanh nghiệp [[src-tt50-2026-nhnn#^pl1-a4-3b]] | Doanh nghiệp | Xếp hạng độc lập từ BBB- [[src-tt50-2026-nhnn#^pl1-a4-3b]] | Phải niêm yết [[src-tt50-2026-nhnn#^pl1-a4-3b]] | ≤ 20% [[src-tt50-2026-nhnn#^pl1-a4-3b]] | Không do tổ chức tài chính hoặc công ty mẹ, con, liên kết phát hành [[src-tt50-2026-nhnn#^pl1-a4-3b]] | 50% [[src-tt50-2026-nhnn#^pl1-a4-3b]] | Xếp hạng ECAI từ BBB- hoặc PD nội bộ tương đương; không do tổ chức tài chính phát hành; thị trường lớn, sâu, sôi động; giảm giá ≤ 20%; haircut 50% [[src-bcbs-lcr#^lcr30-45b]]. Từ AA- mà giảm giá 10–20% cũng vào Level 2B [[src-bcbs-lcr#^lcr30-43-faq1]] |
| 2.2.3 | Chứng khoán công nước ngoài, tổ chức tài chính quốc tế [[src-tt50-2026-nhnn#^pl1-a4-3c]] | Chính phủ, NHTW, PSE nước ngoài hoặc tổ chức tài chính quốc tế; trừ chứng khoán đã đủ điều kiện cấp 1, 2A [[src-tt50-2026-nhnn#^pl1-a4-3c]] | Xếp hạng độc lập từ BBB- và hệ số rủi ro ≤ 50% [[src-tt50-2026-nhnn#^pl1-a4-3c]] | Phải niêm yết [[src-tt50-2026-nhnn#^pl1-a4-3c]] | ≤ 20% [[src-tt50-2026-nhnn#^pl1-a4-3c]] | Không do tổ chức tài chính hoặc công ty mẹ, con, liên kết phát hành [[src-tt50-2026-nhnn#^pl1-a4-3c]] | 50% [[src-tt50-2026-nhnn#^pl1-a4-3c]] | Chính phủ/NHTW BBB+ đến BBB- không thuộc Level 1, haircut 50%, trong trần 15% [[src-bcbs-lcr#^lcr30-45-faq3]]; PSE từ BBB-, giảm giá ≤ 20% [[src-bcbs-lcr#^lcr30-45-faq4]] |
| 2.2.4 | Cổ phiếu phổ thông [[src-tt50-2026-nhnn#^pl1-a4-3d]] | Không do tổ chức tài chính hoặc công ty mẹ, con, liên kết phát hành [[src-tt50-2026-nhnn#^pl1-a4-3d]] | Thuộc VN30 hoặc chỉ số chứng khoán quan trọng theo quyết định của cơ quan có thẩm quyền nơi ngân hàng có rủi ro thanh khoản [[src-tt50-2026-nhnn#^pl1-a4]] | Phải niêm yết và thanh toán bù trừ tập trung [[src-tt50-2026-nhnn#^pl1-a4-3d]] | ≤ 40% [[src-tt50-2026-nhnn#^pl1-a4-3d]] | Phát hành bằng VNĐ hoặc đồng tiền của nước nơi ngân hàng có rủi ro thanh khoản [[src-tt50-2026-nhnn#^pl1-a4-3d]] | 50% [[src-tt50-2026-nhnn#^pl1-a4-3d]] | Không do tổ chức tài chính phát hành; niêm yết và thanh toán bù trừ tập trung; thuộc chỉ số chính do supervisor nơi đặt chỉ số quyết định; bằng nội tệ nước gốc hoặc đồng tiền nơi chịu rủi ro thanh khoản; thị trường lớn, sâu, sôi động; giảm giá ≤ 40%; haircut 50% [[src-bcbs-lcr#^lcr30-45c]] |
| 2.2.5 | Tài sản HQLA của chi nhánh ở nước ngoài [[src-tt50-2026-nhnn#^pl1-a4-3dd]] | | | | | Phải đủ điều kiện HQLA cấp 2B đủ tiêu chuẩn theo TT50 [[src-tt50-2026-nhnn#^pl1-a4-3dd]] | Theo từng loại [[src-tt50-2026-nhnn#^pl1-a5-2b]] | Không có đầu mục tương ứng (*Diễn giải*) |

Ô trống nghĩa là TT50 không đặt tiêu chí đó cho đầu mục. Cột "Hệ số rủi ro / xếp hạng" của mục 2.2.4 ghi tiêu chí chỉ số chứng khoán vì cổ phiếu không có tiêu chí xếp hạng.

*Diễn giải:* cấp 2A của TT50 hẹp hơn Basel vì không có covered bond. Trái phiếu doanh nghiệp từ AA- giảm giá 10–20%: Basel FAQ cho vào Level 2B [[src-bcbs-lcr#^lcr30-43-faq1]], TT50 ghi "từ BBB- trở lên" nên cùng kết quả. Basel có tiêu chí thị trường lớn, sâu, sôi động cho mọi chứng khoán Level 1, 2A, 2B [[src-bcbs-lcr#^lcr30-41a]] [[src-bcbs-lcr#^lcr30-43a]] [[src-bcbs-lcr#^lcr30-45b]]; TT50 thay bằng điều kiện niêm yết. Basel chấp nhận PD nội bộ khi không có xếp hạng ECAI [[src-bcbs-lcr#^lcr30-43b]] [[src-bcbs-lcr#^lcr30-45b]]; TT50 chỉ dùng xếp hạng tín nhiệm độc lập. Basel yêu cầu RMBS chịu quy định risk retention [[src-bcbs-lcr#^lcr30-45a]]; TT50 yêu cầu chứng khoán hoá tuân thủ pháp luật nước thực hiện. Basel ghi haircut, TT50 ghi hệ số thanh khoản: haircut 25% tương đương hệ số 75%.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **Basel**: Cung cấp quyền tự quyết cho supervisor (national discretion) đối với việc chấp nhận Level 2B, nhưng đặt ra các hàng rào kỹ thuật nghiêm ngặt (full recourse, LTV $\le 80\%$, kiểm định sụt giá 10%–40%, cấm nợ định chế tài chính) nhằm bảo vệ tính toàn vẹn của đệm thanh khoản [[src-bcbs-lcr#^lcr30-43]] [[src-bcbs-lcr#^lcr30-45]].
- **ALM / Quản trị bảng cân đối**:
  - *Lợi suất chênh lệch (Yield Pick-up)*: *Diễn giải:* (ngoài wiki, chưa có nguồn) nắm giữ trái phiếu doanh nghiệp và cổ phiếu Level 2 đem lại lợi suất danh mục cao hơn rõ rệt so với trái phiếu chính phủ Level 1, hỗ trợ [[net-interest-margin|NIM]].
  - *Chi phí vốn rủi ro tín dụng (RWA)*: trái phiếu doanh nghiệp, cổ phiếu Level 2 chịu hệ số rủi ro tín dụng cao hơn Level 1 [cần nguồn: hệ số RW theo chuẩn mực vốn chưa ingest]. Bộ phận ALM phải cân đối giữa lợi ích thanh khoản LCR và chi phí tiêu hao vốn tự có (Tier 1 capital).
  - *Tác động NSFR*: Trong NSFR, tài sản Level 2A unencumbered chịu hệ số RSF 15% [[src-bcbs-nsfr#^nsf30-28]], Level 2B chịu RSF 50% [[src-bcbs-nsfr#^nsf30-29]], cao hơn mức 5% của Level 1 unencumbered [[src-bcbs-nsfr#^nsf30-26]].
- **VN**: theo [[tt50-2026|TT50/2026]], cấp 2A (hệ số 85%) gồm chứng khoán Chính phủ/NHTW/PSE nước ngoài, tổ chức quốc tế có hệ số rủi ro tối đa 20% và chứng khoán nợ doanh nghiệp phi tài chính từ AA-, đều niêm yết, giảm giá tối đa 10% [[src-tt50-2026-nhnn#^pl1-a3]]. Cấp 2B gồm RMBS từ AA (75%), chứng khoán nợ doanh nghiệp từ BBB- (50%), chứng khoán Chính phủ nước ngoài BBB- (50%) và cổ phiếu phổ thông phi tài chính thuộc VN30 hoặc chỉ số quan trọng (50%) [[src-tt50-2026-nhnn#^pl1-a4]]. Trái phiếu chính quyền địa phương dùng trong giao dịch NHNN thuộc cấp 1, không phải cấp 2A [[src-tt50-2026-nhnn#^pl1-a2]]. RMBS là cấu phần cấp 2B trong TT50, hệ số 75%, với điều kiện xếp hạng từ AA và LTV trung bình tối đa 80% [[src-tt50-2026-nhnn#^pl1-a4-3a]]. *Diễn giải:* TT50 có quy định RMBS nhưng không nói thị trường RMBS VN đã có hay chưa; số dư thực tế của cấu phần này [cần nguồn]. Đối chiếu từng tham số với Basel: mục `## Basel vs VN`.

## Câu hỏi mở
- Cổ phiếu trong rổ VN30 tại Việt Nam có thỏa mãn đầy đủ các tiêu chuẩn về độ sâu thanh khoản và kiểm định mức sụt giảm giá tối đa không quá 40% trong stress [[src-bcbs-lcr#^lcr30-45]] hay không?

## Xem thêm
- Chi tiết thuật toán và các kịch bản số học Unwind: [[hqla-unwinding-mechanism]]
