---
title: "High-quality liquid assets (HQLA)"
aliases: [HQLA, Tài sản có tính thanh khoản cao, High-quality liquid assets]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2015-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tata-bank-alm]]", "[[src-tt83-2025-nhnn]]", "[[src-choudhry-principles-banking]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "+", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: drives, to: "[[net-interest-margin]]", direction: "-", cite: "[[src-choudhry-principles-banking#^choudhry-nim-5]]"}
tags: [liquidity, lcr, liquidity-buffer, hqla]
updated: 2026-10-20
reviewed:
---

## Định nghĩa chuẩn mực

**High-Quality Liquid Assets (HQLA)** là tử số của tỷ lệ [[lcr]], đại diện cho tổng giá trị danh mục tài sản không bị cầm cố (unencumbered), có tính thanh khoản cao, có khả năng chuyển đổi tức thì thành tiền mặt thông qua bán đứt hoặc thế chấp vay repo trên thị trường tư nhân với mức sụt giảm giá trị tối thiểu, nhằm bảo đảm khả năng sống sót của ngân hàng qua kịch bản kiểm tra sức chịu tải thanh khoản nghiêm ngặt kéo dài 30 ngày dương lịch [[src-bcbs-lcr#^lcr20-1]] [[src-bcbs-lcr#^lcr30-1]] [[src-bcbs-lcr#^lcr30-2]].

Một tài sản chỉ được công nhận là HQLA khi đáp ứng đồng thời cả đặc tính nền tảng (rủi ro tín dụng/thị trường thấp, định giá dễ dàng, tương quan thấp với tài sản rủi ro) và đặc tính thị trường (thị trường sâu rộng, biến động thấp, kênh trú ẩn an toàn flight-to-quality) [[src-bcbs-lcr#^lcr30-2]].

---

## Công thức xác định & Thuật toán Unwinding

Theo Chuẩn mực Basel (LCR30.34–30.39, LCR99.1), giá trị đệm HQLA khả dụng sau khi áp dụng các mức chiết khấu (haircuts) và khấu trừ vượt trần được tính toán theo công thức:

$$
\text{Total HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - \text{Adjustment for 15\% cap} - \text{Adjustment for 40\% cap}
$$

### Cơ chế Unwind Ngăn ngừa Lách trần (LCR30.34–30.39)
Để triệt tiêu các hành vi làm đẹp sổ sách (*window-dressing*) bằng cách thực hiện repo ngắn hạn trước ngày chốt số liệu, ngân hàng phải **hoàn trả giả định (unwind)** toàn bộ các giao dịch tài trợ có bảo đảm và hoán đổi tài sản bảo đảm kỳ hạn $\le 30$ ngày để tính toán: $\text{Adjusted L1}$, $\text{Adjusted L2A}$, và $\text{Adjusted L2B}$ [[src-bcbs-lcr#^lcr30-34]] [[src-bcbs-lcr#^lcr30-37]]. *(Chi tiết thuật toán và ví dụ số học xem tại: [[hqla-unwinding-mechanism]])*.

Hai mức khấu trừ trần được xác định tuần tự:
1. **Khoản khấu trừ trần 15% Level 2B**:
   $$Adjustment_{15\%} = \max\Big(\text{Adjusted L2B} - \frac{15}{85}(\text{Adjusted L1} + \text{Adjusted L2A}),\; \text{Adjusted L2B} - \frac{15}{60}\text{Adjusted L1},\; 0\Big)$$
2. **Khoản khấu trừ trần 40% Level 2**:
   $$Adjustment_{40\%} = \max\Big(\text{Adjusted L2A} + \text{Adjusted L2B} - Adjustment_{15\%} - \frac{2}{3}\text{Adjusted L1},\; 0\Big)$$

---

## Diễn giải & Bảng Phân loại Tổng thể HQLA (Master Classification Matrix)

Basel phân chia tài sản thanh khoản cao thành hai cấp bậc: **[[level-1-assets|Level 1]]** (chất lượng cao nhất, không trần, haircut 0%) và **[[level-2-assets|Level 2]]** (Level 2A haircut 15% và Level 2B haircut 25%–50% khống chế trong trần 40% và 15%) [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-lcr#^lcr30-43]]:

| Cấp độ tài sản | Cấu phần chi tiết | Haircut | Giới hạn trần (Cap) | Tiêu chuẩn chất lượng tín dụng | Kiểm định sụt giá stress 30 ngày |
|---|---|---|---|---|---|
| **[[level-1-assets]]** | Tiền mặt (Coins & Banknotes) [[src-bcbs-lcr#^lcr30-41]] | 0% | **Không giới hạn** | Tuyệt đối unencumbered, sẵn sàng chi trả tức thì [[src-bcbs-lcr#^lcr30-16]] | Không áp dụng |
| | Dự trữ tại NHTW (qua đêm, dự trữ bắt buộc rút được, tiền gửi kỳ hạn rút theo thông báo) [[src-bcbs-lcr#^lcr30-41]] | 0% | **Không giới hạn** | Thỏa mãn thỏa thuận rút vốn khi stress; không tính tiền gửi kỳ hạn bị phong tỏa quá 30 ngày [[src-bcbs-lcr#^lcr30-41]] | Không áp dụng |
| | Chứng khoán công rủi ro 0% (Sovereign/CB/PSE/MDB/BIS/IMF) [[src-bcbs-lcr#^lcr30-41]] | 0% | **Không giới hạn** | Hệ số rủi ro 0% CRE20; thị trường sâu rộng; **cấm nợ do định chế tài chính phát hành** (kể cả được chính phủ bảo lãnh) [[src-bcbs-lcr#^lcr30-41]] | Không áp dụng |
| | Trái phiếu chính phủ/NHTW nội tệ (khi Sovereign RW > 0%) [[src-bcbs-lcr#^lcr30-41]] | 0% | **Không giới hạn** | Phát hành bằng đồng nội tệ tại quốc gia sở tại hoặc quốc gia mẹ [[src-bcbs-lcr#^lcr30-41]] | Không áp dụng |
| | Trái phiếu chính phủ/NHTW ngoại tệ (khi Sovereign RW > 0%) [[src-bcbs-lcr#^lcr30-41]] | 0% | Giới hạn trần | Phát hành bằng ngoại tệ; **chỉ được tính tối đa bằng net cash outflows của chính đồng ngoại tệ đó** [[src-bcbs-lcr#^lcr30-41]] | Không áp dụng |
| **[[level-2-assets]] (Level 2A)** | Chứng khoán công rủi ro 20% (Sovereign/CB/PSE/MDB) [[src-bcbs-lcr#^lcr30-43]] | 15% | Nằm trong trần 40% Level 2 | Hệ số rủi ro 20% CRE20; không do định chế tài chính phát hành [[src-bcbs-lcr#^lcr30-43]] | Sụt giá $\le 10\%$ trong 30 ngày [[src-bcbs-lcr#^lcr30-43]] |
| | Trái phiếu doanh nghiệp thông thường & CP [[src-bcbs-lcr#^lcr30-43]] | 15% | Nằm trong trần 40% Level 2 | Rating ECAI tối thiểu **AA-**; không do định chế tài chính phát hành [[src-bcbs-lcr#^lcr30-43]] | Sụt giá $\le 10\%$ trong 30 ngày [[src-bcbs-lcr#^lcr30-43]] |
| | Trái phiếu có bảo đảm (Covered Bonds) [[src-bcbs-lcr#^lcr30-43]] | 15% | Nằm trong trần 40% Level 2 | Rating ECAI tối thiểu **AA-**; không do chính ngân hàng hoặc bên liên kết phát hành [[src-bcbs-lcr#^lcr30-43]] | Sụt giá $\le 10\%$ trong 30 ngày [[src-bcbs-lcr#^lcr30-43]] |
| **[[level-2-assets]] (Level 2B)** *(National Discretion)* | Chứng khoán thế chấp nhà ở (RMBS) [[src-bcbs-lcr#^lcr30-45]] | 25% | **Trần 15%** tổng HQLA (trong trần 40% L2) | Rating ECAI $\ge$ **AA**; khoản vay full recourse; LTV bình quân $\le 80\%$; cấm CMBS/CDO/CLO [[src-bcbs-lcr#^lcr30-45]] | Sụt giá $\le 20\%$ trong 30 ngày [[src-bcbs-lcr#^lcr30-45]] |
| | Trái phiếu doanh nghiệp BBB- đến A+ [[src-bcbs-lcr#^lcr30-45]] | 50% | **Trần 15%** tổng HQLA | Rating ECAI từ **BBB- đến A+**; không do định chế tài chính phát hành [[src-bcbs-lcr#^lcr30-45]] | Sụt giá $\le 20\%$ trong 30 ngày [[src-bcbs-lcr#^lcr30-45]] |
| | Chứng khoán công BBB- đến BBB+ [[src-bcbs-lcr#^lcr30-45]] | 50% | **Trần 15%** tổng HQLA | Nợ chính phủ, PSE có rating BBB- đến BBB+ [[src-bcbs-lcr#^lcr30-45]] | Sụt giá $\le 20\%$ trong 30 ngày [[src-bcbs-lcr#^lcr30-45]] |
| | Cổ phiếu phổ thông rổ chỉ số chính [[src-bcbs-lcr#^lcr30-45]] | 50% | **Trần 15%** tổng HQLA | Thuộc major stock index; đồng nội tệ; bù trừ QCCP; cấm cổ phiếu định chế tài chính [[src-bcbs-lcr#^lcr30-45]] | Sụt giá $\le 40\%$ trong 30 ngày [[src-bcbs-lcr#^lcr30-45]] |
| | Hạn mức cam kết có hạn chế (RCLF) từ NHTW [[src-bcbs-lcr#^lcr30-46]] | Thỏa thuận | **Trần 15%** tổng HQLA | Phí cam kết $\ge \max(75\text{ bps},\; \Delta\text{Yield} + 25\text{ bps})$; unencumbered collateral [[src-bcbs-lcr#^lcr30-46]] | Theo quy định hợp đồng |
| | Sản phẩm tài chính Hồi giáo (Sukuk) [[src-bcbs-lcr#^lcr30-47]] | Supervisor | **Trần 15%** tổng HQLA | Supervisor quốc gia quyết định riêng cho ngân hàng Hồi giáo [[src-bcbs-lcr#^lcr30-47]] | Theo tiêu chuẩn sở tại |

### 7 Yêu cầu Vận hành Nghiêm ngặt (Operational Requirements)
1. **Quyền kiểm soát của Treasury**: Đệm HQLA phải thuộc quyền quản lý trực tiếp của Khối Nguồn vốn & ALM Treasury [[src-bcbs-lcr#^lcr30-15]].
2. **Trạng thái Unencumbered**: Tài sản không bị đem đi thế chấp, phong tỏa, repo hoặc dùng để bảo lãnh cho bất kỳ nghĩa vụ nào khác [[src-bcbs-lcr#^lcr30-16]].
3. **Hiện thực hóa Định kỳ (Periodic Monetisation)**: Ngân hàng phải định kỳ bán đứt hoặc thực hiện repo một phần tài sản HQLA trên thị trường để kiểm tra năng lực thanh khoản thực tế [[src-bcbs-lcr#^lcr30-15]].
4. **Không bị Rào cản Chuyển giao**: Loại bỏ phần HQLA thặng dư tại các công ty con bị rào cản pháp lý hoặc rào cản chuyển giao biên giới (ring-fencing) theo [[liquidity-transfer-restrictions]] [[src-bcbs-lcr#^lcr10-8]].

---

## Nguồn gốc nguyên tắc: [[bcbs-liquidity-principles|BCBS 144]] Principle 12
- Ngân hàng nên duy trì đệm tài sản thanh khoản cao không bị cầm cố làm bảo hiểm trước nhiều kịch bản stress, kể cả mất nguồn vốn không bảo đảm và nguồn vốn có bảo đảm thông thường; không được có trở ngại pháp lý, quy định hay vận hành khi dùng các tài sản này [[src-bcbs-liquidity-principles-2008#^lrm-p12]].
- Quy mô đệm gắn tường minh với ước tính nhu cầu thanh khoản trong stress [[src-bcbs-liquidity-principles-2008#^lrm-123]] và phù hợp liquidity risk tolerance; yếu tố chính là quy mô chênh lệch dòng tiền, thời gian và mức độ stress, giá trị thanh lý hoặc giá trị vay của tài sản [[src-bcbs-liquidity-principles-2008#^lrm-124]].
- Lõi đệm là tài sản thanh khoản tin cậy nhất như tiền mặt và trái phiếu chính phủ chất lượng cao; với stress nhẹ hơn nhưng kéo dài, ngân hàng có thể mở rộng sang tài sản bán hoặc repo được mà không lỗ quá mức [[src-bcbs-liquidity-principles-2008#^lrm-125]].
- Không giả định thị trường thanh khoản tồn tại trong mọi kịch bản stress; đệm là tuyến phòng thủ dự phòng, không phải tuyến đầu [[src-bcbs-liquidity-principles-2008#^lrm-126]]. Ngân hàng không nên dựa vào việc NHTW thay đổi quy mô hay điều kiện cấp thanh khoản [[src-bcbs-liquidity-principles-2008#^lrm-127]].

*Diễn giải:* Principle 12 không đặt tỷ lệ hay phân cấp tài sản. Cấu trúc lõi/mở rộng ở para 125 tương ứng về ý với Level 1 / Level 2 của LCR; LCR là cách định lượng hoá đệm này bằng một kịch bản stress 30 ngày chuẩn hoá.

## Basel vs VN

| Tham số / Khoản mục | Chuẩn mực Basel (BCBS) | Việt Nam ([[tt50-2026\|TT50/2026/TT-NHNN]]) | Căn cứ Điều khoản | Ghi chú & Lộ trình |
|---|---|---|---|---|
| Tiền mặt & Dự trữ NHTW | HQLA Level 1 (Haircut 0%) | Tài sản cấp 1, hệ số thanh khoản 100% (tiền mặt, tiền gửi tại NHNN kể cả DTBB) [[src-tt50-2026-nhnn#^pl1-a2]] | LCR30.41 / TT50 PL1 | LCR áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Trái phiếu Chính phủ VN (VND) | Level 1 (Haircut 0%) | Tài sản cấp 1, 100%; công cụ nợ Chính phủ VN và tín phiếu NHNN bằng ngoại tệ cũng là cấp 1 [[src-tt50-2026-nhnn#^pl1-a2]] | LCR30.41 / TT50 PL1 | |
| Cấu trúc cấp | Level 1, Level 2A, Level 2B | Tài sản cấp 1, cấp 2A, cấp 2B theo Phụ lục I [[src-tt50-2026-nhnn#^d19-1]] | LCR30 / TT50 Đ19.1 | |
| Trần Level 2 (2A + 2B) | Tối đa 40% tổng HQLA | KĐC40%: phần cấp 2 vượt 2/3 cấp 1 (sau unwinding) bị loại [[src-tt50-2026-nhnn#^pl1-a1]] | LCR30.34 / TT50 PL1 | |
| Trần Level 2B | Tối đa 15% tổng HQLA | KĐC15%: hệ số 15/85 và 15/60 [[src-tt50-2026-nhnn#^pl1-a1]] | LCR30.34 / TT50 PL1 | |
| Yêu cầu vận hành | Unencumbered, kiểm soát bởi chức năng quản lý thanh khoản | Chuyển đổi được thành tiền trong căng thẳng 30 ngày; không bị ràng buộc (ràng buộc một phần coi là bị ràng buộc); bộ phận quản lý thanh khoản kiểm soát; xác định hằng ngày; giữ thêm 30 ngày khi mất tiêu chuẩn [[src-tt50-2026-nhnn#^d20-2]] | LCR30 / TT50 Đ20.2 | |
| Trái phiếu Doanh nghiệp trong HQLA | Level 2A (AA-) / Level 2B (BBB-) | Cấp 2A (85%) nếu phi tài chính, từ AA-, niêm yết, giảm giá ≤ 10% [[src-tt50-2026-nhnn#^pl1-a3]]; cấp 2B (50%) nếu từ BBB-, giảm giá ≤ 20% [[src-tt50-2026-nhnn#^pl1-a4]] | LCR30.43 / TT50 PL1 | Khả năng thị trường TPĐN VN chưa đủ sâu |
| Phương pháp thanh khoản thay thế (ALA) | Cho phép Option 1, 2, 3 | Không có quy định ALA trong phần TT50 đã ingest (C2-M5, PL1, PL2) [cần nguồn] | LCR31 / TT50 | Tùy chọn nếu thiếu nợ công |

- **Yêu cầu chung theo TT83/2025**: ngân hàng phải duy trì đủ tài sản có tính thanh khoản cao theo quy định NHNN cho điều kiện bình thường và bất lợi [[src-tt83-2025-nhnn#^d45-1a]], quản lý theo giá trị thị trường và khả năng chuyển thành tiền [[src-tt83-2025-nhnn#^d46-2]]. Định nghĩa và tỷ lệ HQLA của VN vẫn chờ ingest TT50/2026.

---

## Ứng dụng trong ALM

1. **Bộ tứ Đánh đổi tại ALM Treasury**:
   - Việc xây dựng đệm HQLA là bài toán cân bằng đa mục tiêu: Tối đa hóa tỷ lệ an toàn thanh khoản tức thì LCR nhưng phải kiểm soát chi phí cơ hội lợi suất (Carry cost), rủi ro thời lượng đối với giá trị kinh tế EVE ([[bcbs-irrbb]]), tiêu hao vốn tự có RWA và áp lực đòn bẩy Leverage Ratio [[hqla-decomposition-and-tradeoffs]].
2. **Cạm bẫy Thời lượng (Duration Trap)**:
   - Cuối 2022, sổ HTM của [[silicon-valley-bank|SVB]] (chủ yếu MBS dài hạn) có lỗ chưa thực hiện 15,2 tỷ USD, tương ứng duration khoảng 6,25 năm, trong khi vốn chủ sở hữu khoảng 12 tỷ USD [[src-tata-bank-alm#^tata-svb-5]]. Để không bị coi là outlier theo phép thử EVE, duration tiền gửi phải trên 3,7 năm [[src-tata-bank-alm#^tata-svb-7]]. *Diễn giải:* trường hợp SVB là MBS dài hạn, không phải danh mục HQLA Level 1 dùng cho LCR; bài học chung cho đệm HQLA là chứng khoán kỳ hạn dài không phòng ngừa lãi suất vẫn mang rủi ro giá trị kinh tế lớn, xem [[outlier-bank-test]].
   - [[alco|ALCO]] giải quyết bằng cách áp **Trần thời lượng HQLA (Duration Cap $\le 2.5–3.0$ năm)** và áp dụng chiến lược đòn gánh Barbell.

3. **Chính sách đầu tư hai danh mục (Choudhry, T4)**:
   - "HQLA book" theo Basel III và liquidity book không phải HQLA để tăng lợi suất [[src-choudhry-principles-banking#^choudhry-tig-1]]. Quy mô tối thiểu của HQLA book theo khẩu vị stress thanh khoản trong RAS và [[ilaap|ILAAP]], hướng dẫn bởi LCR và Survival Days ([[cash-flow-survival-period]]) [[src-choudhry-principles-banking#^choudhry-tig-2]].
4. **Mô hình vận hành LAB (Choudhry, T4)**:
   - LAB tài trợ bằng nguồn trên 90 ngày, lý tưởng trên 1 năm, không bằng repo; là danh mục riêng trong Treasury hoặc ALCO book; khả năng NHTW chấp nhận tài sản không quan trọng [[src-choudhry-principles-banking#^choudhry-lab-2]].
   - Quy mô đủ sống qua stress 2 tuần và stress toàn thị trường 3 tháng; ngày nay quy mô trước hết do LCR quyết định [[src-choudhry-principles-banking#^choudhry-lab-3]]. Định kỳ bán hoặc repo một phần để chứng minh thanh khoản [[src-choudhry-principles-banking#^choudhry-lab-4]].
5. **Chi phí carry của đệm (Choudhry Ex 1.5, kịch bản 2)**:
   - Tăng buffer £1,5bn tài trợ dài hạn, net cost of carry 3% (7,5% − 4,5%), NII giảm £45m, NIM giảm 0,50 điểm % xuống 2,38% [[src-choudhry-principles-banking#^choudhry-nim-5]]. Xem [[net-interest-margin]].
6. **Kế toán**: HQLA đo theo amortised cost hoặc FVTOCI chịu ảnh hưởng của [[effective-interest-rate|EIR]]; EIR ảnh hưởng giá trị ghi sổ HQLA và tiền gửi, cần xét khi tính LCR [[src-choudhry-principles-banking#^choudhry-eir-3]].

---

## Nhầm lẫn thường gặp

1. **Nhầm lẫn rằng Mọi Trái phiếu Chính phủ đều là Level 1**: Trái phiếu chính phủ phát hành bằng ngoại tệ chỉ được tính vào Level 1 tối đa bằng mức dòng tiền ra ròng (net cash outflows) của chính đồng ngoại tệ đó [[src-bcbs-lcr#^lcr30-41]].
2. **Hiểu sai về Trái phiếu Doanh nghiệp được Chính phủ Bảo lãnh**: Basel quy định rõ: Chứng khoán do các định chế tài chính phát hành (ngân hàng, công ty chứng khoán, bảo hiểm) tuyệt đối **không được xếp vào HQLA Level 1**, ngay cả khi chúng được chính phủ bảo lãnh thanh toán [[src-bcbs-lcr#^lcr30-41]].
3. **Bỏ qua Hoàn trả Unwind**: Tính toán trần 40% và 15% dựa trên số dư sổ sách thực tế mà không thực hiện unwind các giao dịch repo ngắn hạn là sai lệch quy chuẩn Basel và bị coi là hành vi gian lận kiểm toán [[src-bcbs-lcr#^lcr30-34]].

4. **Coi quan điểm của tác giả là chuẩn mực**: Choudhry (T4) cho rằng buffer nên chỉ gồm sovereign G7 hoặc trong nước, và gọi việc Basel mở rộng định nghĩa là "unfortunate" [[src-choudhry-principles-banking#^choudhry-liq-7]]. Đây là ý kiến tác giả; căn cứ định nghĩa HQLA là LCR30.

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
