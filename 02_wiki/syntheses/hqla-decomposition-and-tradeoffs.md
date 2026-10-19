---
title: HQLA decomposition, calculation mechanics, and ALM tradeoffs
aliases: [HQLA decomposition and tradeoffs, Phân tích thành phần HQLA và các đánh đổi ALM]
type: synthesis
domains: [alm, basel]
status: active
maturity: draft
origin: research
question: "Các thành phần HQLA trong Basel III được xác định và tính toán như thế nào, và bộ phận ALM Treasury phải đối mặt với những đánh đổi chiến lược nào giữa lợi suất, rủi ro thời lượng, vốn tự có và các ràng buộc tỷ lệ an toàn khác?"
as_of: 2026-10-15
sources: ["[[src-bcbs-lcr]]"]
relations: []
tags: [liquidity, hqla, alm-strategy, basel-iii]
updated: 2026-10-17
reviewed:
---

## Câu hỏi
1. Danh mục [[hqla]] của tỷ lệ [[lcr]] theo chuẩn mực Basel III được phân tầng thành [[level-1-assets]], Level 2A, và Level 2B dựa trên những tiêu chuẩn định tính, chất lượng tín dụng và kiểm định biến động giá stress nào?
2. Cơ chế hoàn trả (unwind) đối với các giao dịch tài trợ ngắn hạn và hệ thống trần tỷ trọng kép (40% Level 2, 15% Level 2B) vận hành toán học ra sao để triệt tiêu hành vi che giấu cấu trúc rủi ro thực tế của bảng cân đối?
3. Khi xây dựng và quản trị danh mục HQLA, bộ phận Nguồn vốn và Quản trị Bảng cân đối kế toán (ALM Treasury) phải xử lý những xung đột chiến lược nào giữa mục tiêu an toàn thanh khoản ngắn hạn với thu nhập lãi thuần (NIM), rủi ro thời lượng (IRRBB), nguồn vốn ổn định dài hạn (NSFR), và tỷ lệ đòn bẩy (Leverage Ratio)?

## Kết luận
- **HQLA là đệm thanh khoản tiền tệ hóa tức thì**: HQLA không đơn thuần là tài sản có giá trị thị trường, mà phải duy trì năng lực chuyển đổi thành tiền mặt nguyên vẹn thông qua bán đứt hoặc repo ngay cả khi xảy ra cú sốc kết hợp giữa rủi ro đặc thù ngân hàng và căng thẳng toàn thị trường [[src-bcbs-lcr#^lcr20-2]] [[src-bcbs-lcr#^lcr30-2]].
- **Phân tầng 3 lớp dựa trên mức độ suy giảm thanh khoản trong stress**:
  - [[level-1-assets]] (haircut 0%, không giới hạn trần) đóng vai trò là "mỏ neo" thanh khoản tối thượng, gồm tiền mặt, dự trữ NHTW khả dụng, và chứng khoán công 0% rủi ro (loại trừ nợ định chế tài chính theo Footnote 11) [[src-bcbs-lcr#^lcr30-41]].
  - Level 2A (haircut 15%, trần 40%) gồm chứng khoán công 20% rủi ro, trái phiếu doanh nghiệp và covered bond rating $\ge AA-$, với mức sụt giá stress $\le 10\%$ [[src-bcbs-lcr#^lcr30-43]].
  - Level 2B (haircuts 25%–50%, trần 15%) gồm RMBS full recourse LTV $\le 80\%$, trái phiếu doanh nghiệp BBB- đến A+, và cổ phiếu thuộc chỉ số chính nội tệ bù trừ QCCP [[src-bcbs-lcr#^lcr30-45]].
- **Cơ chế Unwind biến Level 1 thành biến số quyết định**: Việc hoàn trả toàn bộ các giao dịch tài trợ ngắn hạn $\le 30$ ngày trước khi áp trần ngăn ngừa triệt để hiện tượng lách trần bằng repo ngắn hạn. Mọi sự sụt giảm của Adjusted Level 1 đều làm co hẹp mức trần Level 2 theo tỷ lệ $2/3$, tạo ra hiệu ứng sụt giảm HQLA phi tuyến tính [[src-bcbs-lcr#^lcr30-34]].
- **Bộ tứ đánh đổi ALM Treasury**: Nắm giữ HQLA buộc Treasury phải cân đối 4 mặt trận:
  1. *Chi phí cơ hội (Negative Carry)*: Tài sản Level 1 có lợi suất thấp nhất, bào mòn NIM.
  2. *Rủi ro thời lượng (IRRBB)*: Kéo dài kỳ hạn trái phiếu chính phủ để tìm kiếm lợi suất sẽ làm gia tăng tổn thất Mark-to-Market khi mặt bằng lãi suất tăng vọt.
  3. *Tiêu hao vốn (RWA) và Rủi ro kẹt trần (Cap Trap)*: Nắm giữ tài sản Level 2 mang lại lợi suất cao hơn nhưng đòi hỏi vốn tự có theo Basel III và đối mặt nguy cơ bị loại bỏ khỏi HQLA nếu chạm trần.
  4. *Xung đột Tỷ lệ Đòn bẩy (Leverage Ratio)*: Tích trữ đệm HQLA làm phình to Exposure Measure, trực tiếp đe dọa tỷ lệ đòn bẩy tối thiểu 3%.

## Cơ chế

### 1. Bảng phân tầng và tiêu chuẩn kỹ thuật các cấu phần HQLA

| Cấp độ | Cấu phần chi tiết | Haircut | Giới hạn trần (Cap) | Tiêu chuẩn chất lượng tín dụng | Kiểm định sụt giá stress 30 ngày | Điều kiện loại trừ nghiêm ngặt |
|---|---|---|---|---|---|---|
| **Level 1** | Tiền mặt (Coins & Banknotes) [[src-bcbs-lcr#^lcr30-41]] | 0% | Không trần | Tuyệt đối unencumbered, sẵn sàng chi trả tức thì [[src-bcbs-lcr#^lcr30-16]] | Không áp dụng | Tiền đang vận chuyển chịu ràng buộc hợp đồng. |
| | Dự trữ tại NHTW [[src-bcbs-lcr#^lcr30-41]] | 0% | Không trần | Tiền gửi qua đêm, dự trữ bắt buộc rút được khi stress; tiền gửi kỳ hạn rút theo thông báo hoặc thế chấp vay lại [[src-bcbs-lcr#^lcr30-41]] | Không áp dụng | Tiền gửi kỳ hạn bị phong tỏa quá 30 ngày (nếu đáo hạn $\le 30$ ngày thì xử lý là dòng vào 100% [[src-bcbs-lcr#^lcr40-87]]). |
| | Chứng khoán công 0% rủi ro tín dụng [[src-bcbs-lcr#^lcr30-41]] | 0% | Không trần | RW 0% CRE20; phát hành/bảo lãnh bởi Sovereign, CB, PSE, MDB, BIS, IMF, ECB [[src-bcbs-lcr#^lcr30-41]] | Không áp dụng | **Footnote 11**: Cấm nợ do định chế tài chính phát hành, kể cả được chính phủ bảo lãnh. |
| | Trái phiếu chính phủ/NHTW nội tệ khi RW > 0% [[src-bcbs-lcr#^lcr30-41]] | 0% | Không trần | Phát hành bằng đồng nội tệ tại quốc gia sở tại hoặc quốc gia ngân hàng mẹ [[src-bcbs-lcr#^lcr30-41]] | Không áp dụng | Trái phiếu ngoại tệ vượt quá dòng tiền ra ròng ngoại tệ. |
| | Trái phiếu chính phủ/NHTW ngoại tệ khi RW > 0% [[src-bcbs-lcr#^lcr30-41]] | 0% | Khống chế ròng | Phát hành bằng ngoại tệ; giới hạn tối đa bằng **stressed net cash outflows của chính đồng ngoại tệ đó** [[src-bcbs-lcr#^lcr30-41]] | Không áp dụng | Phần vượt quá nhu cầu ròng ngoại tệ bị loại hoàn toàn khỏi Level 1. |
| **Level 2A** | Chứng khoán công 20% rủi ro tín dụng [[src-bcbs-lcr#^lcr30-43]] | 15% | Trần 40% Level 2 | RW 20% CRE20; thị trường giao ngay/repo sâu rộng [[src-bcbs-lcr#^lcr30-43]] | Sụt giá $\le 10\%$ trong 30 ngày stress [[src-bcbs-lcr#^lcr30-43]] | Không do định chế tài chính phát hành (trừ khi là PSE). |
| | Trái phiếu doanh nghiệp thông thường & CP [[src-bcbs-lcr#^lcr30-43]] | 15% | Trần 40% Level 2 | Plain vanilla; rating ECAI tối thiểu **AA-** (hoặc PD tương đương) [[src-bcbs-lcr#^lcr30-43]] | Sụt giá $\le 10\%$ trong 30 ngày stress [[src-bcbs-lcr#^lcr30-43]] | Tuyệt đối cấm nợ do ngân hàng, chứng khoán, bảo hiểm phát hành. |
| | Trái phiếu có bảo đảm (Covered Bonds) [[src-bcbs-lcr#^lcr30-43]] | 15% | Trần 40% Level 2 | Giám sát công đặc biệt; cover pool đạt chuẩn; rating ECAI tối thiểu **AA-** [[src-bcbs-lcr#^lcr30-43]] | Sụt giá $\le 10\%$ trong 30 ngày stress [[src-bcbs-lcr#^lcr30-43]] | Không do chính ngân hàng hoặc bên liên kết phát hành. |
| **Level 2B** | RMBS đủ điều kiện [[src-bcbs-lcr#^lcr30-45]] | 25% | Trần 15% tổng HQLA | Rating ECAI $\ge$ **AA**; khoản vay cơ sở là **full recourse**; LTV bình quân gia quyền $\le 80\%$ tại phát hành [[src-bcbs-lcr#^lcr30-45]] | Sụt giá $\le 20\%$ trong 30 ngày stress [[src-bcbs-lcr#^lcr30-45]] | Cấm nợ do ngân hàng tự khởi tạo; cấm CMBS, CDO, CLO, ABCP. |
| | Trái phiếu doanh nghiệp BBB- đến A+ [[src-bcbs-lcr#^lcr30-45]] | 50% | Trần 15% tổng HQLA | Plain vanilla; rating ECAI từ **BBB- đến A+** [[src-bcbs-lcr#^lcr30-45]] | Sụt giá $\le 20\%$ trong 30 ngày stress [[src-bcbs-lcr#^lcr30-45]] | Tuyệt đối cấm nợ do định chế tài chính phát hành. |
| | Chứng khoán công BBB- đến BBB+ [[src-bcbs-lcr#^lcr30-45]] | 50% | Trần 15% tổng HQLA | Nợ chính phủ, PSE có rating BBB- đến BBB+ [[src-bcbs-lcr#^lcr30-45]] | Sụt giá $\le 20\%$ trong 30 ngày stress [[src-bcbs-lcr#^lcr30-45]] | Thị trường giao dịch tích cực, minh bạch. |
| | Cổ phiếu phổ thông rổ chỉ số chính [[src-bcbs-lcr#^lcr30-45]] | 50% | Trần 15% tổng HQLA | Thuộc major stock index; đồng nội tệ; bù trừ QCCP [[src-bcbs-lcr#^lcr30-45]] | Sụt giá $\le 40\%$ trong 30 ngày stress [[src-bcbs-lcr#^lcr30-45]] | Cấm cổ phiếu của các định chế tài chính. |
| | Cam kết thanh khoản có hạn chế (RCLF) [[src-bcbs-lcr#^lcr30-46]] | Thỏa thuận | Trần 15% tổng HQLA | Hạn mức chưa giải ngân từ NHTW; unencumbered collateral [[src-bcbs-lcr#^lcr30-46]] | Theo hợp đồng | Phí cam kết $\ge \max(75\text{ bps},\; \Delta\text{Yield} + 25\text{ bps})$. |
| | Sản phẩm tài chính Hồi giáo (Sukuk) [[src-bcbs-lcr#^lcr30-47]] | Supervisor | Trần 15% tổng HQLA | Supervisor quyết định riêng cho ngân hàng Hồi giáo [[src-bcbs-lcr#^lcr30-47]] | Theo tiêu chuẩn sở tại | Chỉ áp dụng cho ngân hàng hoạt động theo Shari'ah. |

### 2. Thuật toán Unwinding và Công thức tính Trần kép (LCR30.34–30.39)
*(Chi tiết toàn diện về cơ chế Unwind, bút toán biến động tài sản bảo đảm và 4 ca nghiên cứu số học xem tại: [[hqla-unwinding-mechanism]])*.

Để ngăn chặn việc dùng repo ngắn hạn hoán đổi tài sản Level 2 lấy Level 1 ngay trước ngày chốt số liệu báo cáo, Basel yêu cầu thực hiện hoàn trả (unwind) toàn bộ các giao dịch tài trợ có bảo đảm và hoán đổi tài sản bảo đảm kỳ hạn $\le 30$ ngày:
$$\text{Adjusted L1} = \text{L1 hiện hữu} + \text{L1 nhận lại từ repo unwind} - \text{L1 hoàn trả từ reverse repo unwind}$$
$$\text{Adjusted L2A} = \text{L2A hiện hữu} + \text{L2A nhận lại} - \text{L2A hoàn trả (sau haircut 15\%)}$$
$$\text{Adjusted L2B} = \text{L2B hiện hữu} + \text{L2B nhận lại} - \text{L2B hoàn trả (sau haircut tương ứng)}$$

Sau khi xác định bộ ba số dư điều chỉnh, thuật toán áp dụng 2 bước khấu trừ trần:
1. **Khấu trừ vượt trần 15% của Level 2B**:
   $$Adjustment_{15\%} = \max\left(\text{Adjusted L2B} - \frac{15}{85}(\text{Adjusted L1} + \text{Adjusted L2A}),\;\; \text{Adjusted L2B} - \frac{15}{60}\text{Adjusted L1},\;\; 0\right)$$
   *(Hệ số 15/85 áp dụng khi trần 40% chưa chạm; hệ số 15/60 = 1/4 áp dụng khi trần 40% bị chạm, buộc Level 1 phải chiếm ít nhất 60% HQLA)* [[src-bcbs-lcr#^lcr30-34]].
2. **Khấu trừ vượt trần 40% tổng Level 2**:
   $$Adjustment_{40\%} = \max\left(\big(\text{Adjusted L2A} + \text{Adjusted L2B} - Adjustment_{15\%}\big) - \frac{2}{3}\text{Adjusted L1},\;\; 0\right)$$
   *(Tỷ lệ trần Level 2 / Level 1 = 40% / 60% = 2/3)* [[src-bcbs-lcr#^lcr30-34]].
3. **Tổng HQLA đủ điều kiện đưa vào tử số LCR**:
   $$\text{Stock of HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - Adjustment_{15\%} - Adjustment_{40\%}$$

### 3. Khung 7 yêu cầu vận hành bắt buộc (Operational Requirements)
1. **Unencumbered tuyệt đối**: Không bị cầm cố, gán nợ, hoặc ký quỹ đảm bảo cho các nghĩa vụ khác; không dùng để dự phòng chi phí hoạt động [[src-bcbs-lcr#^lcr30-16]].
2. **Quyền kiểm soát độc quyền của Treasury**: Danh mục thuộc thẩm quyền trực tiếp và liên tục của Treasurer, đảm bảo năng lực pháp lý và vận hành để thanh khoản hóa bất kỳ ngày nào trong 30 ngày [[src-bcbs-lcr#^lcr30-18]].
3. **Kiểm tra định kỳ tính thanh khoản (Periodic Monetisation)**: Định kỳ bán đứt hoặc repo một tỷ lệ đại diện trên thị trường để thử nghiệm hạ tầng và hạn chế rủi ro phát tín hiệu tiêu cực khi stress [[src-bcbs-lcr#^lcr30-15]].
4. **Loại trừ tài sản tái thế chấp có quyền đòi**: Không tính tài sản nhận được qua repo nếu chủ sở hữu có quyền rút lại trong 30 ngày [[src-bcbs-lcr#^lcr30-24]].
5. **Đồng bộ cơ cấu tiền tệ (Currency Matching)**: Duy trì danh mục HQLA tương ứng với cơ cấu tiền tệ của dòng tiền ra ròng [[src-bcbs-lcr#^lcr30-27]].
6. **Rào cản chuyển giao thanh khoản tập đoàn ([[liquidity-transfer-restrictions]])**: Thặng dư HQLA ở công ty con chịu rào cản chuyển giao không được cộng gộp vào LCR hợp nhất vượt quá net outflows cục bộ [[src-bcbs-lcr#^lcr10-7]] [[src-bcbs-lcr#^lcr30-27]].
7. **Quy tắc ân hạn 30 ngày (Cliff-Edge Relief)**: Tài sản bị hạ bậc tín nhiệm vi phạm chuẩn được giữ lại trong HQLA thêm 30 ngày để tái cơ cấu trật tự [[src-bcbs-lcr#^lcr30-28]].

## Bằng chứng ủng hộ
- **Khủng hoảng 2008 & Cú sốc COVID-19 tháng 3/2020**: Trong cả hai cuộc khủng hoảng thanh khoản hệ thống, chỉ có tiền mặt, dự trữ NHTW và trái phiếu chính phủ ngắn hạn duy trì được thanh khoản thị trường và biên độ giá ổn định (flight-to-quality) [[src-bcbs-lcr#^lcr30-2]].
- **Thực tế đóng băng nợ định chế tài chính**: Trong khủng hoảng 2008, trái phiếu do các ngân hàng lớn phát hành (kể cả các định chế có bảo lãnh ngầm từ chính phủ) đều bị sụp đổ thanh khoản thứ cấp và không thể repo trên thị trường liên ngân hàng, khẳng định tính cần thiết của việc cấm nợ định chế tài chính theo Footnote 11 [[src-bcbs-lcr#^lcr30-41]].
- **Kiểm định sụt giá 10%–40%**: Dữ liệu lịch sử thị trường cho thấy trong giai đoạn khủng hoảng, trái phiếu doanh nghiệp BBB- và RMBS có mức sụt giảm giá vượt xa 15–20%, chứng minh mức haircut 25%–50% và trần 15% là hoàn toàn tương xứng với rủi ro thanh lý cưỡng bức [[src-bcbs-lcr#^lcr30-45]].

## Bằng chứng trái chiều
- **Nghịch lý chủ quyền tiền tệ (Sovereign Paradox)**: Basel cho phép trái phiếu chính phủ phát hành bằng đồng nội tệ được xếp vào Level 1 không giới hạn ngay cả khi chính phủ có xếp hạng tín nhiệm thấp (RW > 0%) [[src-bcbs-lcr#^lcr30-41]]. Tuy nhiên, trong cuộc khủng hoảng nợ công Châu Âu 2011–2012, trái phiếu của một số chính phủ ngoại vi suy giảm giá trị và thanh khoản nghiêm trọng hơn cả trái phiếu doanh nghiệp đa quốc gia hạng AAA, làm dấy lên tranh cãi về giả định phi rủi ro của trái phiếu chủ quyền nội tệ.
- **Rủi ro đóng băng thanh khoản do quy định (Regulatory Lock-in)**: Việc quy định tài sản HQLA phải unencumbered và tách biệt dưới sự kiểm soát của Treasury khiến một khối lượng khổng lồ trái phiếu chất lượng cao bị "khóa cứng" trong các danh mục dự phòng, làm giảm vòng quay vốn trên thị trường repo và hạn chế nguồn cung tài sản bảo đảm cho nền kinh tế thực.

## Phụ thuộc regime
- **Regime bình thường**: Ngân hàng bắt buộc phải duy trì $\text{LCR} \ge 100\%$ liên tục [[src-bcbs-lcr#^lcr20-5]]. Treasury phải kiểm soát chặt chẽ tỷ trọng Level 2 trong ngưỡng an toàn ($\le 30-35\%$) để tạo khoảng trống dự phòng (headroom), tránh bị phạt trừ trần khi số dư Level 1 biến động trong tháng [[src-bcbs-lcr#^lcr30-34]].
- **Regime stress thanh khoản**:
  - Ngân hàng được toàn quyền sử dụng danh mục HQLA để bù đắp thâm hụt tiền mặt, chấp nhận tỷ lệ LCR có thể tạm thời tụt xuống dưới 100% [[src-bcbs-lcr#^lcr20-5]].
  - Cơ quan giám sát áp dụng biện pháp phản ứng linh hoạt có phân biệt (differentiated response) dựa trên nguyên nhân và triển vọng phục hồi, không tự động kích hoạt chế độ xử phạt vi phạm hành chính [[src-bcbs-lcr#^lcr20-6]].
  - Khi ngân hàng sử dụng Level 1 trước tiên để bán hoặc repo, tỷ lệ Level 2 / Level 1 tăng lên, có thể kích hoạt các khoản khấu trừ trần $\text{Adjustment}_{40\%}$ và $\text{Adjustment}_{15\%}$, làm tử số HQLA giảm nhanh hơn tốc độ tiêu hao thực tế.

## Hàm ý ALM / quy định

### 1. Chiến lược quản trị danh mục HQLA tại Treasury
- **Chiến lược Barbell (Quả tạ) tối ưu hóa Carry & Duration**:
  - Một đầu của quả tạ tập trung vào tiền gửi thanh toán NHTW và tín phiếu kho bạc siêu ngắn hạn (0–3 tháng) để đáp ứng nhu cầu thanh khoản tức thì và giảm thiểu rủi ro thời lượng (IRRBB).
  - Đầu kia của quả tạ phân bổ vào trái phiếu doanh nghiệp Level 2A rating cao (AA-) và trái phiếu chính phủ thả nổi (FRN) hoặc trái phiếu cố định được phòng ngừa rủi ro lãi suất bằng hợp đồng hoán đổi lãi suất (IRS receiver sang payer) nhằm gia tăng lợi suất thu nhập lãi thuần (NIM).
- **Quản trị giới hạn trần (Cap Headroom Management)**:
  - Thiết lập hạn mức nội bộ cho Level 2 tối đa ở mức 30–35% tổng HQLA (thay vì dùng hết trần quy định 40%) và Level 2B tối đa 10–12% (thay vì 15%). Khoảng đệm an toàn này giúp ngân hàng không bị kích hoạt khấu trừ trần khi giá trị Level 1 sụt giảm trong stress.

### 2. Xung đột đa chiều giữa các tỷ lệ an toàn của Basel
- **LCR vs NSFR**: Tài sản Level 1 unencumbered có hệ số Required Stable Funding (RSF) là 0% trong NSFR, nghĩa là không đòi hỏi nguồn vốn ổn định dài hạn tài trợ. Ngược lại, Level 2A chịu RSF 15% và Level 2B chịu RSF 50%. Việc tối đa hóa Level 1 do đó hỗ trợ đồng thời cả hai tỷ lệ LCR và NSFR.
- **LCR vs Tỷ lệ Đòn bẩy (Leverage Ratio)**: Toàn bộ HQLA trên bảng cân đối (kể cả tiền gửi NHTW và trái phiếu 0% rủi ro) đều bị tính 100% vào Mẫu số Exposure Measure của Leverage Ratio. Tích lũy đệm HQLA càng lớn thì áp lực đòn bẩy càng nặng nề.
- **LCR vs Rủi ro lãi suất (IRRBB)**: Bài học từ sự sụp đổ của Silicon Valley Bank (SVB) năm 2023 cho thấy việc nắm giữ danh mục HQLA gồm trái phiếu chính phủ dài hạn cố định lãi suất có thể thỏa mãn LCR trên giấy tờ nhưng phá hủy giá trị kinh tế của ngân hàng (EVE) khi lãi suất thị trường tăng vọt. Quản trị HQLA không thể tách rời việc đo lường độ nhạy lãi suất $\Delta\text{EVE}$ và $\Delta\text{NII}$ (xem phân tích cơ chế chi tiết và kỹ thuật phòng hộ tại [[irrbb-liquidity-hqla-and-ftp-interaction]]).

## Bất định
- **Quy chế rút dự trữ bắt buộc tại Việt Nam**: Hiện tại NHNN áp dụng cơ chế quản lý dự trữ bắt buộc theo kỳ duy trì tháng. Mức độ mà các ngân hàng thương mại Việt Nam được phép rút phần dự trữ bắt buộc để đáp ứng điều kiện "drawdown in times of stress" [[src-bcbs-lcr#^lcr30-41]] theo TT50/2026 vẫn đang chờ văn bản hướng dẫn chi tiết từ Cơ quan Thanh tra Giám sát Ngân hàng.
- **Tính khả thi của Level 2B tại thị trường cận biên**: Thị trường RMBS và trái phiếu doanh nghiệp có định mức tín nhiệm độc lập tại Việt Nam hiện còn sơ khai. Liệu các ngân hàng có thể tận dụng cấu phần Level 2B hay buộc phải dựa gần như 100% vào trái phiếu Chính phủ và tín phiếu NHNN để duy trì LCR?
- [2026-10-19] ingest src-tata-bank-alm u07: đã có node [[silicon-valley-bank]] có nguồn (số liệu bảng cân đối, phòng ngừa, duration gap 3 năm, giả định duration tiền gửi) [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-9]]; cần rà lại chỗ nhắc SVB, đối chiếu số liệu và thay bằng citation.
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15: [[liquidity-transfer-restrictions]] thêm intra-group lending (UK: hạn mức 25% capital base, Integrated Group) và nguyên tắc stand-alone; cần rà lại phần ràng buộc chuyển giao HQLA trong tập đoàn.
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04: đã có node [[net-interest-margin]] (định nghĩa, case ChoudWest 5 kịch bản: NII và NIM có thể đi ngược chiều, buffer £1,5bn làm NIM −0,50 điểm %, Table 1.10 hành động quản lý NIM); cần rà lại chỗ dùng NIM làm chỉ số đánh đổi.
