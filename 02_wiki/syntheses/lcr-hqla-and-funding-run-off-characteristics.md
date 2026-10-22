---
title: "LCR: phân loại HQLA và đặc điểm run-off theo nguồn vốn"
aliases: [HQLA classification and funding run-off characteristics, Phân loại HQLA và đặc điểm rủi ro thanh khoản theo nguồn vốn, Tử số và dòng ra LCR theo sản phẩm]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Phương pháp phân loại HQLA Level 1, Level 2A và Level 2B; tiêu chuẩn chất lượng, tính thanh khoản, haircut, operational requirements, unwinding và các giới hạn tỷ trọng. · Đặc điểm rủi ro thanh khoản của retail deposits, wholesale funding, operational deposits, secured funding, derivatives và off-balance-sheet commitments."
as_of: 2026-10-22
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]", "[[src-choudhry-principles-banking]]"]
relations: []
tags: [lcr, hqla, level-1, level-2, haircut, unwinding, run-off, deposits, wholesale-funding, derivatives, research]
updated: 2026-10-22
reviewed:
---

## Câu hỏi
Thuộc bộ "Liquidity Risk — LCR & HQLA" (7 câu). Cụm này trả lời:
- **Q3.** Phương pháp phân loại HQLA Level 1, Level 2A và Level 2B; tiêu chuẩn chất lượng, tính thanh khoản, haircut, operational requirements, unwinding và các giới hạn tỷ trọng.
- **Q4.** Đặc điểm rủi ro thanh khoản của retail deposits, wholesale funding, operational deposits, secured funding, derivatives và off-balance-sheet commitments.

Khung kịch bản và công thức mẫu số (Q1–Q2): [[lcr-stress-scenario-and-net-cash-outflows]]. Tác động biên (Q5, Q7): [[lcr-model-marginal-impact-and-alm-levers]]. Đánh đổi (Q6): [[lcr-hqla-buffer-tradeoffs]].

Node dùng, đều ở maturity `draft`: [[hqla]], [[level-1-assets]], [[level-2-assets]], [[hqla-unwinding-mechanism]], [[alternative-liquidity-approaches]], [[retail-deposit-stability]], [[operational-deposits]], [[unsecured-wholesale-funding]], [[secured-funding]], [[derivatives-and-contingent-outflows]], [[committed-facilities]]. Tham số VN theo TT50/2026, áp dụng cho LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]].

## Kết luận
- **Q3.** Tài sản là HQLA khi chuyển được thành tiền dễ dàng, ngay lập tức, ít hoặc không mất giá, kể cả trong stress [[src-bcbs-lcr#^lcr30-2]]. Basel chia hai cấp: Level 1 không trần, haircut 0%; Level 2 tối đa 40% HQLA sau haircut, trong đó Level 2B tối đa 15% [[src-bcbs-lcr#^lcr30-31]]. Level 2A chịu haircut 15%, Level 2B 25–50% [[src-bcbs-lcr#^lcr30-43]] [[src-bcbs-lcr#^lcr30-45]]. Hai trần được tính sau khi unwind repo, reverse repo và collateral swap đáo hạn trong 30 ngày [[src-bcbs-lcr#^lcr30-34]]. TT50 dùng cùng cấu trúc với "hệ số thanh khoản" 100% / 85% / 75% hoặc 50% [[src-tt50-2026-nhnn#^pl1-a2]] [[src-tt50-2026-nhnn#^pl1-a3]] [[src-tt50-2026-nhnn#^pl1-a4]] và cùng công thức KĐC15%, KĐC40% [[src-tt50-2026-nhnn#^pl1-a1]].
- **Q3 (vận hành).** HQLA phải unencumbered và do bộ phận quản lý thanh khoản kiểm soát liên tục [[src-bcbs-lcr#^lcr30-16]] [[src-bcbs-lcr#^lcr30-18]]. TT50 thêm yêu cầu xác định danh mục hằng ngày, và cho giữ HQLA mất chuẩn thêm 30 ngày [[src-tt50-2026-nhnn#^d20-2]].
- **Q4.** Hai yếu tố quyết định run-off rate: loại đối tác và mức phụ thuộc của đối tác vào ngân hàng. Run-off thấp nhất thuộc về tiền gửi bán lẻ được bảo hiểm toàn bộ và có quan hệ khác với ngân hàng (5%). Mức cao nhất là vốn không bảo đảm từ tổ chức tài chính (100%) [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-42]]. Secured funding phụ thuộc chất lượng tài sản bảo đảm thay vì đối tác [[src-bcbs-lcr#^lcr40-47]]. Phái sinh và cam kết ngoại bảng tạo dòng ra tiềm tàng từ hạ bậc tín nhiệm, ký quỹ và rút hạn mức [[src-bcbs-lcr#^lcr40-51]] [[src-bcbs-lcr#^lcr40-64]]. TT50 giữ phần lớn hệ số Basel; các khác biệt nằm ở định nghĩa đối tượng (DNNVV ≤ 30 tỷ đồng, điều kiện tiền gửi ổn định) và hệ số tài trợ thương mại, bảo lãnh [[src-tt50-2026-nhnn#^pl1-b3]] [[src-tt50-2026-nhnn#^pl1-b2-2]] [[src-tt50-2026-nhnn#^pl1-b5-3]].

## Cơ chế

### Q3 — Phân loại HQLA

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[level-1-assets]] | part-of | [[hqla]] | | [[src-bcbs-lcr#^lcr30-41]] |
| [[level-2-assets]] | part-of | [[hqla]] | | [[src-bcbs-lcr#^lcr30-43]] |
| [[hqla-unwinding-mechanism]] | limits | [[level-2-assets]] | | [[src-bcbs-lcr#^lcr30-37]] |
| [[alternative-liquidity-approaches]] | part-of | [[hqla]] | | [[src-bcbs-lcr#^lcr31-1]] |
| [[tt50-2026]] | governs | [[hqla]] | | [[src-tt50-2026-nhnn#^d19-1]] |
| [[level-2-assets]] | drives | [[lcr]] | + | [[src-bcbs-lcr#^lcr30-43]] |

**Tiêu chuẩn chất lượng và tính thanh khoản.** Basel nêu hai nhóm đặc điểm:
- **Đặc điểm cơ bản**: rủi ro thấp (tổ chức phát hành uy tín, ít nhạy với lãi suất và rủi ro thị trường), định giá dễ và chắc chắn, tương quan thấp với tài sản rủi ro, niêm yết trên sở giao dịch phát triển [[src-bcbs-lcr#^lcr30-6]].
- **Đặc điểm thị trường**: thị trường bán đứt hoặc repo sôi động và đủ lớn mọi lúc [[src-bcbs-lcr#^lcr30-10]].

Hai nhóm đặc điểm được lượng hoá thành tiêu chí giảm giá tối đa trong 30 ngày stress cho từng cấp.

| Cấp | Basel: tài sản, haircut | VN (TT50 PL1 Phần A): tài sản, hệ số thanh khoản |
|---|---|---|
| Level 1 / cấp 1 | tiền mặt, dự trữ NHTW rút được khi stress, chứng khoán khả nhượng 0% RW; haircut 0% [[src-bcbs-lcr#^lcr30-41]] | tiền mặt, tiền gửi tại NHNN (cả DTBB), công cụ nợ Chính phủ VN, tín phiếu NHNN (VNĐ và ngoại tệ), trái phiếu được Chính phủ bảo lãnh 100%; chứng khoán nước ngoài 0% RW giảm giá tối đa 5%; hệ số 100% [[src-tt50-2026-nhnn#^pl1-a2]] |
| Level 2A / cấp 2A | chứng khoán công 20% RW; trái phiếu doanh nghiệp phi tài chính và covered bond từ AA−; haircut 15% [[src-bcbs-lcr#^lcr30-43]]; giảm giá tối đa 10% trong 30 ngày stress [[src-bcbs-lcr#^lcr30-43a]] | chứng khoán công nước ngoài RW tối đa 20%, chứng khoán nợ DN phi tài chính từ AA−; niêm yết; giảm giá tối đa 10%; hệ số 85% [[src-tt50-2026-nhnn#^pl1-a3]] |
| Level 2B / cấp 2B | RMBS từ AA (25%); trái phiếu DN BBB− đến A+ (50%); cổ phiếu thuộc chỉ số chính (50%) [[src-bcbs-lcr#^lcr30-45]] | RMBS từ AA, LTV bình quân ≤ 80% (75%); chứng khoán nợ DN phi tài chính từ BBB− (50%); chứng khoán Chính phủ nước ngoài từ BBB− (50%); cổ phiếu VN30, giảm giá tối đa 40% (50%) [[src-tt50-2026-nhnn#^pl1-a4]] |
| Quyền điều chỉnh của cơ quan giám sát | supervisor có thể yêu cầu haircut cho Level 1 dựa trên độ nhạy lãi suất, thị trường, tín dụng, thanh khoản [[src-bcbs-lcr#^lcr30-40]]; Level 2B chỉ đưa vào theo quyết định quốc gia [[src-bcbs-lcr#^lcr30-44]] | NHNN có quyền yêu cầu hệ số thấp hơn cho cấp 1, 2A, 2B [[src-tt50-2026-nhnn#^pl1-a2-2]]; có quyền không cho tính tài sản vào cấp 2B [[src-tt50-2026-nhnn#^pl1-a4-1]] |

Level 1 và Level 2A đều đo theo current market value [[src-bcbs-lcr#^lcr30-40]] [[src-bcbs-lcr#^lcr30-43]]. TT50 lấy số dư theo giá thị trường hoặc mark-to-model [[src-tt50-2026-nhnn#^pl1-a5]].

**Operational requirements.**

| Yêu cầu | Basel | VN (TT50 Đ20.2) |
|---|---|---|
| Chuyển thành tiền trong 30 ngày stress | dùng ngay làm nguồn vốn dự phòng, qua bán đứt hoặc repo [[src-bcbs-lcr#^lcr30-14]] | chuyển đổi được thành tiền (bán trực tiếp, repo, giao dịch với NHNN) [[src-tt50-2026-nhnn#^d20-2]] |
| Unencumbered | không có hạn chế pháp lý, quy định, hợp đồng với việc bán, chuyển nhượng [[src-bcbs-lcr#^lcr30-16]] | không bị ràng buộc; tài sản ràng buộc một phần coi là bị ràng buộc [[src-tt50-2026-nhnn#^d20-2]] |
| Kiểm soát | bộ phận quản lý thanh khoản (ví dụ Treasurer) kiểm soát liên tục [[src-bcbs-lcr#^lcr30-18]] | bộ phận quản lý thanh khoản kiểm soát và có thẩm quyền quyết định chuyển đổi [[src-tt50-2026-nhnn#^d20-2d]] |
| Thử thị trường | định kỳ monetise một phần qua repo hoặc bán đứt [[src-bcbs-lcr#^lcr30-15]] | [cần nguồn] |
| Tài sản phòng ngừa rủi ro | vẫn tính, trừ chi phí đóng hợp đồng phòng ngừa [[src-bcbs-lcr#^lcr30-19]] | vẫn tính; giá trị thị trường trừ chi phí đóng phòng ngừa trước hạn [[src-tt50-2026-nhnn#^d20-2dd]] |
| Tài sản bán không được hoặc giảm giá vượt mức | loại nếu có trở ngại khi bán [[src-bcbs-lcr#^lcr30-23]] | phải loại khỏi HQLA đủ tiêu chuẩn [[src-tt50-2026-nhnn#^d20-2g]] |
| Tài sản mất chuẩn | giữ thêm 30 ngày [[src-bcbs-lcr#^lcr30-28]] | giữ thêm 30 ngày [[src-tt50-2026-nhnn#^d20-2]] |
| Chuyển giao trong tập đoàn | thặng dư ở pháp nhân con chỉ tính khi chuyển giao được cho công ty mẹ trong stress [[src-bcbs-lcr#^lcr30-27]] [[src-bcbs-lcr#^lcr10-7]] | LCR hợp nhất quản lý theo quy định nội bộ [[src-tt50-2026-nhnn#^d16-2]] |

**Giới hạn tỷ trọng và unwinding.**

$$
\text{Adj}_{15\%} = \max\Big(L2B^{a} - \tfrac{15}{85}(L1^{a} + L2A^{a}),\; L2B^{a} - \tfrac{15}{60} L1^{a},\; 0\Big)
$$
[[src-bcbs-lcr#^lcr30-34]] [[src-tt50-2026-nhnn#^pl1-a1]]

$$
\text{Adj}_{40\%} = \max\Big(L2A^{a} + L2B^{a} - \text{Adj}_{15\%} - \tfrac{2}{3} L1^{a},\; 0\Big)
$$
[[src-bcbs-lcr#^lcr30-34]] [[src-tt50-2026-nhnn#^pl1-a1]]

$$
\text{HQLA} = L1 + L2A + L2B - \text{Adj}_{15\%} - \text{Adj}_{40\%}
$$
[[src-bcbs-lcr#^lcr30-37]] [[src-tt50-2026-nhnn#^pl1-a1]]

Ký hiệu $^{a}$ là số dư sau haircut và sau khi unwind giao dịch đáo hạn ≤ 30 ngày [[src-bcbs-lcr#^lcr30-37]]. Tài sản nhận được rồi đem tái thế chấp trong một giao dịch ngắn hạn khác thì phải unwind cả hai giao dịch [[src-bcbs-lcr#^lcr30-37]] [[src-tt50-2026-nhnn#^pl1-a1-1b]]. TT50 cộng thêm vào HQLA hạn mức chưa sử dụng bảo đảm bằng HQLA cấp 1 trong giao dịch với NHNN [[src-tt50-2026-nhnn#^pl1-a1-4]].

Ví dụ của TT50: ngân hàng có 100 tỷ đồng tiền mặt, đã repo một tài sản cấp 2A, cam kết mua lại trong 30 ngày giá 40 tỷ đồng. Sau unwinding, KĐC.L1 = 60 tỷ đồng và KĐC.L2A = 34 tỷ đồng nếu tài sản cấp 2A đạt yêu cầu vận hành [[src-tt50-2026-nhnn#^pl1-a1-vd]].

*Diễn giải:* tính tiếp ví dụ trên (số học của synthesis): $\text{Adj}_{40\%} = \max(34 - \tfrac{2}{3}\times 60, 0) = 0$, nên HQLA sau unwinding = 94 tỷ đồng, thấp hơn 100 tỷ đồng trước unwinding. Repo làm tăng tiền mặt (Level 1) nhưng không tạo HQLA mới. Một ví dụ khác cho thấy trần hoạt động thế nào: với $L1 = 50$, $L2A = 30$, $L2B = 20$ (sau haircut, không có giao dịch cần unwind), ta có $\text{Adj}_{15\%} = \max(20 - 14{,}12;\ 20 - 12{,}5;\ 0) = 7{,}5$ và $\text{Adj}_{40\%} = \max(30 + 20 - 7{,}5 - 33{,}33;\ 0) = 9{,}17$. Kết quả HQLA = 83,33: Level 1 chiếm 60%, Level 2 chiếm 40%, Level 2B chiếm 15%. Phần vượt trần không làm tăng LCR.

### Q4 — Đặc điểm rủi ro thanh khoản theo nguồn vốn

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[retail-deposit-stability]] | drives | [[run-off-rate]] | | [[src-bcbs-lcr#^lcr40-6]] |
| [[operational-deposits]] | part-of | [[unsecured-wholesale-funding]] | | [[src-bcbs-lcr#^lcr40-26]] |
| [[unsecured-wholesale-funding]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-20]] |
| [[secured-funding]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-46]] |
| [[derivatives-and-contingent-outflows]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-51]] |
| [[committed-facilities]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-64]] |

**Retail deposits** ([[retail-deposit-stability]]).
- Run-off của tiền gửi bán lẻ là mức sàn; jurisdiction có thể đặt cao hơn [[src-bcbs-lcr#^lcr40-6]].
- Stable (5%) cần hai điều kiện: được bảo hiểm toàn bộ bởi quỹ bảo hiểm tiền gửi hiệu quả, và người gửi có quan hệ khác với ngân hàng hoặc dùng tài khoản giao dịch [[src-bcbs-lcr#^lcr40-7]]. Có bảo hiểm tiền gửi thôi chưa đủ [[src-bcbs-lcr#^lcr40-10]].
- Less stable chịu tối thiểu 10%. Supervisor có thể lập bucket cao hơn cho tiền gửi lớn, khách hàng HNW, internet deposits, ngoại tệ [[src-bcbs-lcr#^lcr40-13]].
- Tiền gửi có kỳ hạn > 30 ngày được loại khỏi dòng ra nếu rút trước hạn bị phạt đáng kể [[src-bcbs-lcr#^lcr40-16]]. Ngân hàng cho rút không phạt thì toàn bộ nhóm đó bị coi là không kỳ hạn [[src-bcbs-lcr#^lcr40-17]].
- VN: stable cần được BHTG bảo hiểm hoàn toàn, và khách hàng có khoản vay trung dài hạn hoặc tài khoản thanh toán có phát sinh giao dịch trong 6 tháng gần nhất. Phần vượt giới hạn bảo hiểm là kém ổn định [[src-tt50-2026-nhnn#^pl1-b2-2]]. Tiền gửi ngoại tệ thuộc nhóm kém ổn định [[src-tt50-2026-nhnn#^pl1-b2]]. Khi stress test, ngân hàng phải chia tiền gửi kém ổn định thành các nhóm để xác định hệ số riêng [[src-tt50-2026-nhnn#^pl1-b2-3]].

**Unsecured wholesale funding** ([[unsecured-wholesale-funding]]).
- Chỉ tính phần đáo hạn hoặc có thể bị rút trong 30 ngày, kể cả phần nhà đầu tư có quyền chọn [[src-bcbs-lcr#^lcr40-20]].
- SME được xử lý như bán lẻ khi tổng vốn huy động từ một khách hàng < 1 triệu EUR [[src-bcbs-lcr#^lcr40-22]] [[src-bcbs-lcr#^lcr40-23]]. TT50 đặt ngưỡng DNNVV là tiền gửi bình quân tháng trước tại ngân hàng không quá 30 tỷ đồng [[src-tt50-2026-nhnn#^pl1-b3]].
- DN phi tài chính và khu vực công: 40%, hoặc 20% nếu được bảo hiểm toàn bộ [[src-bcbs-lcr#^lcr40-40]] [[src-bcbs-lcr#^lcr40-41]]. TT50 áp 40% và xếp cả KBNN, UBND cấp tỉnh, BHTG, BHXH, ngân hàng chính sách vào nhóm này [[src-tt50-2026-nhnn#^pl1-b3-24]].
- Tổ chức tài chính: 100% [[src-bcbs-lcr#^lcr40-42]]. Trái phiếu do ngân hàng phát hành cũng thuộc nhóm 100%, trừ khi chỉ bán cho và chỉ do khách bán lẻ/SME nắm giữ [[src-bcbs-lcr#^lcr40-43]]. TT50 xếp nguồn không bảo đảm khác vào nhóm 100% [[src-tt50-2026-nhnn#^pl1-b3-25]].

**Operational deposits** ([[operational-deposits]]).
- Tiền gửi phát sinh từ clearing, custody, cash management chịu 25% khi khách hàng phụ thuộc thực chất vào ngân hàng [[src-bcbs-lcr#^lcr40-26]]. Điều kiện: có hợp đồng ràng buộc; chấm dứt phải báo trước ≥ 30 ngày hoặc chịu chi phí chuyển đổi đáng kể [[src-bcbs-lcr#^lcr40-27]].
- Excess balance không được hưởng 25%; không xác định được phần excess thì toàn bộ là non-operational [[src-bcbs-lcr#^lcr40-29]]. Correspondent banking và prime brokerage không phải hoạt động operational [[src-bcbs-lcr#^lcr40-32]].
- VN: TT50 lượng hoá "chi phí chuyển đổi" là tối thiểu toàn bộ lãi và 10% gốc, và yêu cầu áp lãi suất không kỳ hạn thấp nhất [[src-tt50-2026-nhnn#^pl1-b3]].

**Secured funding** ([[secured-funding]]).
- Run-off theo tài sản bảo đảm, không theo đối tác. Bảo đảm bằng Level 1 hoặc với NHTW trong nước: 0%. Level 2: bằng haircut. Với chính phủ, PSE trong nước (RW ≤ 20%) bảo đảm bằng tài sản khác: 25% [[src-bcbs-lcr#^lcr40-47]]. Giao dịch khác: 100% [[src-bcbs-lcr#^lcr40-48]].
- VN: cấp 1 hoặc với NHNN 0%; cấp 2A 15%; tài sản khác với khu vực công trong nước 25%; RMBS 25%; cấp 2B khác 50%; tài sản tài chính khác 100% [[src-tt50-2026-nhnn#^pl1-b3-3]].

**Derivatives** ([[derivatives-and-contingent-outflows]]).
- Dòng ra phái sinh ròng tính 100%; chỉ netting theo đối tác khi có master netting agreement; quyền chọn in the money được giả định thực hiện [[src-bcbs-lcr#^lcr40-49]].
- Dòng ra tiềm tàng gồm: tài sản bảo đảm khi hạ tới 3 notch, 100% [[src-bcbs-lcr#^lcr40-51]]; cộng 20% cho tài sản bảo đảm không phải Level 1 đã đặt cọc [[src-bcbs-lcr#^lcr40-52]]; tài sản bảo đảm dư thừa mà đối tác đòi được bất kỳ lúc nào, 100% [[src-bcbs-lcr#^lcr40-53]]; biến động định giá theo look-back 24 tháng [[src-bcbs-lcr#^lcr40-56]].
- VN: TT50 giữ cùng bộ tham số. FX swap, forward trong cùng ngày được bù trừ ròng; giao dịch có quyền chọn tài sản giao giả định giao tài sản thanh khoản thấp nhất (cheapest to deliver) [[src-tt50-2026-nhnn#^pl1-b4]].

**Off-balance-sheet commitments** ([[committed-facilities]]).
- Phần hạn mức được giả định rút coi là dư nợ không được trả lại [[src-bcbs-lcr#^lcr40-59]]. Drawdown rate phân biệt credit facility và liquidity facility theo đối tác (5% đến 100%) [[src-bcbs-lcr#^lcr40-64]] [[src-tt50-2026-nhnn#^pl1-b5]].
- Nghĩa vụ cấp vốn hợp đồng cho khách bán lẻ và wholesale phi tài chính: phần vượt 50% dòng vào hợp đồng từ chính nhóm đó tính 100% [[src-bcbs-lcr#^lcr40-66]] [[src-tt50-2026-nhnn#^pl1-b5]].
- Nghĩa vụ tiềm tàng khác do supervisor quốc gia quyết định [[src-bcbs-lcr#^lcr40-67]]; tài trợ thương mại có thể áp run-off thấp, ví dụ ≤ 5% [[src-bcbs-lcr#^lcr40-71]]. TT50 ấn định: hạn mức huỷ ngang vô điều kiện 0%, tài trợ thương mại 3%, bảo lãnh 5%, nghĩa vụ phi hợp đồng do ngân hàng xác định từ dữ liệu lịch sử, nghĩa vụ đã bị kích hoạt 100% [[src-tt50-2026-nhnn#^pl1-b5-3]].

*Diễn giải:* có thể xếp các nguồn vốn theo mức "dính" mà LCR giả định:
1. Tiền gửi bán lẻ stable (5%).
2. Tiền gửi bán lẻ less stable (10%).
3. Operational deposits (25%).
4. Wholesale phi tài chính (40%).
5. Wholesale tài chính (100%).

Thứ tự này phản ánh hai yếu tố: bảo hiểm tiền gửi và chi phí chuyển đổi của khách hàng. Với secured funding, thứ tự đi theo chất lượng tài sản bảo đảm. Choudhry ghi nhận số dư rút ngay chịu chi phí đệm dòng ra LCR cao nhất, nên có giá trị thấp nhất với ngân hàng [[src-choudhry-principles-banking#^choudhry-cs-20]].

## Bằng chứng ủng hộ
- Tham số của TT50 (T1) trùng với Basel (T2) ở trần 40%/15%, haircut 2A 15%, run-off bán lẻ 5%/10%, operational 25%, wholesale 40%/100%, secured funding và drawdown rate (các bảng trên).

## Bằng chứng trái chiều
Không ghi nhận trong nguồn đã ingest. Các khác biệt Basel – VN là lựa chọn jurisdiction (xem Phụ thuộc regime).

## Phụ thuộc regime
- **Jurisdiction.** TT50 không có tuỳ chọn 3% cho tiền gửi stable như LCR40.11 [[src-bcbs-lcr#^lcr40-11]] [[src-tt50-2026-nhnn#^pl1-b2]]. Cấp 2A của TT50 gồm ba nhóm tài sản và không nêu covered bond [[src-tt50-2026-nhnn#^pl1-a3-3]]. Level 1 của TT50 gồm toàn bộ công cụ nợ Chính phủ VN, không kèm điều kiện [[src-tt50-2026-nhnn#^pl1-a2-3d]].
- **Stress.** Tài sản không còn đạt tiêu chí giảm giá tối đa trong 30 ngày stress thì ra khỏi HQLA sau 30 ngày [[src-bcbs-lcr#^lcr30-28]] [[src-tt50-2026-nhnn#^d20-2]].
- **Quốc gia thiếu HQLA nội tệ.** Basel có phương pháp thanh khoản thay thế (ALA) cho số ít quốc gia thiếu Level 1 nội tệ; thiếu riêng Level 2 thì không đủ điều kiện [[src-bcbs-lcr#^lcr31-1]].

## Hàm ý ALM / quy định
- **Nghĩa vụ NHNN.** Hệ số thanh khoản, hệ số rút tiền và yêu cầu vận hành áp theo TT50 PL1 và Đ20 từ khi áp dụng LCR (01/10/2028) [[src-tt50-2026-nhnn#^d13-1]]. NHNN có quyền hạ hệ số thanh khoản dựa trên độ nhạy rủi ro [[src-tt50-2026-nhnn#^pl1-a2-2]]. Basel là tham chiếu.
- *Diễn giải:* với ngân hàng VN, tài sản cấp 1 sẵn có là tiền gửi NHNN và công cụ nợ Chính phủ VN, nên trần 40%/15% chủ yếu ràng buộc ngân hàng giữ nhiều trái phiếu doanh nghiệp. Phía nguồn vốn, cải thiện LCR nhanh nhất là chuyển tiền gửi kém ổn định sang ổn định theo đúng hai điều kiện của TT50 (BHTG và quan hệ vay hoặc thanh toán), và phân loại tiền gửi hoạt động đủ điều kiện.

## Bất định
- Giới hạn bảo hiểm tiền gửi (con số) để chia ổn định/kém ổn định: TT50 không nêu [[src-tt50-2026-nhnn#^pl1-b2-2]]; cần nguồn quy định BHTG.
- Yêu cầu monetise định kỳ (LCR30.15) chưa thấy tương ứng trong claim TT50 đã ingest.
- Hệ số cho nghĩa vụ phi hợp đồng ở VN do ngân hàng tự xác định từ dữ liệu lịch sử [[src-tt50-2026-nhnn#^pl1-b5-3]]; chưa có nguồn hướng dẫn phương pháp.
