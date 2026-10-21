---
title: Level 1 assets
aliases: [Level 1 assets, Tài sản cấp 1, Level 1 HQLA]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr30-41]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "+", cite: "[[src-bcbs-lcr#^lcr30-41]]"}
tags: [liquidity, hqla, level-1]
updated: 2026-10-21
reviewed:
---

## Định nghĩa

Level 1 assets là cấu phần cốt lõi có chất lượng tín dụng và tính thanh khoản cao nhất trong danh mục [[hqla]] của [[lcr]] [[src-bcbs-lcr#^lcr30-31]]. Tài sản Level 1 được đưa vào danh mục HQLA **không bị giới hạn tỷ trọng (unlimited)** và **không áp dụng mức chiết khấu định giá (haircut 0%)** [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-41]]. Lớp tài sản này đóng vai trò là "mỏ neo" thanh khoản cơ bản nhất của ngân hàng và là chuẩn số học để xác định giới hạn trần của [[level-2-assets]] [[src-bcbs-lcr#^lcr30-34]].

### Chi tiết 5 nhóm cấu phần của Level 1 assets (LCR30.41)

Basel III quy định danh mục Level 1 assets giới hạn nghiêm ngặt trong 5 nhóm tài sản sau:

| Nhóm cấu phần | Phạm vi chi tiết | Điều kiện ràng buộc kỹ thuật & Ngoại lệ |
|---|---|---|
| **1. Tiền mặt (Coins & Banknotes)** | Tiền giấy và tiền kim loại tại quỹ, tiền mặt tại các chi nhánh và mạng lưới ATM [[src-bcbs-lcr#^lcr30-41]]. | Phải là tài sản hoàn toàn không bị cầm cố (unencumbered) và sẵn sàng chi trả ngay lập tức cho khách hàng [[src-bcbs-lcr#^lcr30-16]]. Tiền đang vận chuyển chịu hạn chế pháp lý hoặc hợp đồng không được tính. |
| **2. Dự trữ tại Ngân hàng Trung ương (Central Bank Reserves)** | Tiền gửi thanh toán qua đêm (overnight deposits), dự trữ bắt buộc (required reserves), và tiền gửi có kỳ hạn tại NHTW [[src-bcbs-lcr#^lcr30-41]]. | - **Dự trữ bắt buộc**: Chỉ được tính phần mà chính sách NHTW cho phép rút ra trong giai đoạn căng thẳng thanh khoản (drawdown in times of stress) [[src-bcbs-lcr#^lcr30-41]].<br>- **Tiền gửi kỳ hạn (Footnote 7)**: Bắt buộc thỏa mãn một trong hai điều kiện:<br>  *(i)* Có điều khoản hợp đồng cho phép rút trước hạn theo thông báo (repayable on notice); HOẶC<br>  *(ii)* Được dùng làm tài sản bảo đảm để vay vốn có kỳ hạn hoặc vay qua đêm tự động tái tục từ NHTW [[src-bcbs-lcr#^lcr30-41]].<br>  *Loại trừ*: Tiền gửi kỳ hạn bị phong tỏa/không cho rút trước hạn quá 30 ngày bị loại khỏi HQLA (nếu đáo hạn trong 30 ngày thì xử lý là dòng vào 100% theo LCR40.87 [[src-bcbs-lcr#^lcr40-87]]). |
| **3. Chứng khoán khả nhượng có hệ số rủi ro 0% (0% RW Securities)** | Trái phiếu/chứng khoán phát hành hoặc được bảo lãnh vô điều kiện bởi chính phủ, NHTW, thực thể khu vực công (PSE), BIS, IMF, ECB, ESM, EFSF, hoặc MDBs [[src-bcbs-lcr#^lcr30-41]]. | Thỏa mãn đồng thời 4 điều kiện nghiêm ngặt:<br>1. Hệ số rủi ro tín dụng 0% theo Phương pháp chuẩn hóa (CRE20) [[src-bcbs-lcr#^lcr30-41]].<br>2. Giao dịch trên thị trường giao ngay hoặc repo quy mô lớn, sâu rộng, thanh khoản liên tục và mức tập trung thấp [[src-bcbs-lcr#^lcr30-41]].<br>3. Có bằng chứng lịch sử là kênh trú ẩn an toàn (flight-to-quality) và nguồn thanh khoản tin cậy ngay cả khi thị trường xảy ra stress nghiêm trọng [[src-bcbs-lcr#^lcr30-41]].<br>4. **Quy tắc loại trừ định chế tài chính (Footnote 11)**: Tuyệt đối không phải là nghĩa vụ nợ của một ngân hàng, công ty chứng khoán, bảo hiểm hoặc pháp nhân liên kết, **ngay cả khi được chính phủ bảo lãnh** (trừ trường hợp pháp nhân phát hành là một PSE theo quy định nước sở tại) [[src-bcbs-lcr#^lcr30-41]]. |
| **4. Trái phiếu Chính phủ / NHTW nội tệ (khi Sovereign có RW > 0%)** | Chứng khoán nợ do chính phủ hoặc NHTW phát hành bằng đồng nội tệ tại quốc gia nơi ngân hàng gánh chịu rủi ro thanh khoản hoặc tại quốc gia của ngân hàng mẹ [[src-bcbs-lcr#^lcr30-41]]. FAQ1: chỉ áp cho nước sở tại (home) hoặc nước có chi nhánh, công ty con (host); không áp cho nước mà ngân hàng chỉ có rủi ro thanh khoản bằng đồng tiền nước đó [[src-bcbs-lcr#^lcr30-41-faq]]. | Áp dụng tại các quốc gia mà xếp hạng tín nhiệm của chính phủ không đạt mức RW 0% (ví dụ các thị trường mới nổi có RW 20%, 50%...). Toàn bộ trái phiếu chính phủ phát hành bằng đồng nội tệ vẫn được công nhận là Level 1 vì NHTW có quyền năng tối thượng trong việc tạo lập thanh khoản đồng nội tệ [[src-bcbs-lcr#^lcr30-41]]. |
| **5. Trái phiếu Chính phủ / NHTW ngoại tệ (khi Sovereign có RW > 0%)** | Chứng khoán nợ do chính phủ hoặc NHTW sở tại phát hành bằng đồng ngoại tệ (khi chính phủ có RW > 0%) [[src-bcbs-lcr#^lcr30-41]]. FAQ2: phần tính vào Level 1 giới hạn ở rủi ro ngoại tệ tại chính jurisdiction của tổ chức phát hành, không dùng bù rủi ro ngoại tệ ở nước khác [[src-bcbs-lcr#^lcr30-41-faq]]. | **Giới hạn trần đặc thù**: Chỉ được công nhận là Level 1 tối đa bằng quy mô **dòng tiền ra ròng chịu stress của chính đồng ngoại tệ đó** phát sinh từ hoạt động của ngân hàng tại quốc gia liên quan [[src-bcbs-lcr#^lcr30-41]]. Phần giá trị vượt quá nhu cầu ròng của đồng ngoại tệ này không được tính vào Level 1. |

### Danh mục tài sản cấp 1 theo TT50/2026 (PL1 Phần A Mục II, Bảng 3 mục 1)

Theo TT50/2026, tài sản cấp 1 là tài sản tại khoản 3 Mục II; HQLA đủ tiêu chuẩn cấp 1 không bị giới hạn và có hệ số thanh khoản 100%, trừ khi NHNN yêu cầu hệ số thấp hơn [[src-tt50-2026-nhnn#^pl1-a2]] [[src-tt50-2026-nhnn#^pl1-a2-2]]. Trong Bảng 3, dòng 1 là tổng các mục 1.1 đến 1.7; cột (4) cho ra Level 1 và cột (5) cho ra KĐC.L1 [[src-tt50-2026-nhnn#^pl1-a5-1]]. TT50 có hiệu lực từ 01/10/2026; LCR áp dụng từ 01/10/2028 theo lộ trình [[src-tt50-2026-nhnn#^d13-1]].

| Mục Bảng 3 | Điểm Mục II | Tài sản (theo câu chữ TT50) | Điều kiện | Nguồn |
|---|---|---|---|---|
| 1.1 | 3a | Tiền mặt | Không kèm điều kiện | [[src-tt50-2026-nhnn#^pl1-a2-3c]] [[src-tt50-2026-nhnn#^pl1-a5-1]] |
| 1.2 | 3b | Tiền gửi (bao gồm cả tiền gửi dự trữ bắt buộc) tại NHNN | Không kèm điều kiện | [[src-tt50-2026-nhnn#^pl1-a2-3b]] |
| 1.3 | 3c | Chứng khoán của Chính phủ, NHTW, PSE các nước trừ VN, BIS, IMF, ECB và Cộng đồng Châu Âu, ESM, EFSF hoặc tổ chức tài chính quốc tế, hoặc được các đối tượng này bảo đảm | Đủ 5 điều kiện: (i) tổ chức phát hành/bảo đảm như trên; (ii) hệ số rủi ro 0% theo TT14/2025 hoặc TT41/2016; (iii) niêm yết; (iv) lịch sử 10 năm, giảm giá hoặc tăng chiết khấu ≤ 5% trong 30 ngày căng thẳng; (v) không do tổ chức tài chính hoặc công ty mẹ, con, liên kết phát hành | [[src-tt50-2026-nhnn#^pl1-a2-3c]] |
| 1.4.1 | 3d | Công cụ nợ của Chính phủ VN (gồm trái phiếu Chính phủ, tín phiếu Kho bạc Nhà nước), tín phiếu NHNN phát hành bằng VNĐ | Không kèm điều kiện | [[src-tt50-2026-nhnn#^pl1-a2-3d]] |
| 1.4.2 | 3đ | Công cụ nợ của Chính phủ VN, tín phiếu NHNN phát hành bằng ngoại tệ | Không kèm điều kiện hay trần | [[src-tt50-2026-nhnn#^pl1-a2-3dd]] |
| 1.5 | 3e | Trái phiếu Chính phủ bảo lãnh thanh toán 100% gốc, lãi khi đến hạn; trái phiếu chính quyền địa phương | Trái phiếu chính quyền địa phương phải được dùng trong giao dịch của NHNN theo quyết định của Thống đốc từng thời kỳ | [[src-tt50-2026-nhnn#^pl1-a2-3e]] |
| 1.6 | 3g | Tài sản trong danh mục HQLA của chi nhánh ở nước ngoài của NHTM | Phải đủ điều kiện HQLA cấp 1 đủ tiêu chuẩn theo TT50 | [[src-tt50-2026-nhnn#^pl1-a2-3g]] |
| 1.7 | 3h | Công cụ nợ của Chính phủ (kể cả trái phiếu Chính phủ), NHTW của nước nơi chi nhánh ở nước ngoài đặt trụ sở | Thuộc danh mục HQLA của chi nhánh, trừ tài sản đã tính theo điểm g; tổng giá trị tối đa bằng dòng tiền ra ròng của chi nhánh | [[src-tt50-2026-nhnn#^pl1-a2-3h]] |
| 5.1 | Mục I.4 | Hạn mức chưa sử dụng trong giao dịch với NHNN | Phải được bảo đảm bởi HQLA cấp 1; được coi là tài sản cấp 1 | [[src-tt50-2026-nhnn#^pl1-a1-4]] |

Mọi đầu mục còn phải đáp ứng yêu cầu vận hành Đ20.2 [[src-tt50-2026-nhnn#^d20-2]]. Đối chiếu tiêu chí từng mục với Basel: mục `### Tiêu chí xác định theo đầu mục Bảng 3 TT50` bên dưới.


## Công thức & tham số

### Tác động hai chiều giữa Level 1 và tính toán LCR

#### 1. Tác động tới Tử số (Stock of HQLA)
- Level 1 không chịu bất kỳ haircut nào ($\text{Haircut} = 0\%$) và không bị khống chế trần tỷ trọng [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-41]].
- Sau khi giả định hoàn trả (unwind) các giao dịch tài trợ ngắn hạn trong 30 ngày, giá trị **Adjusted Level 1** đóng vai trò là "mẫu số chuẩn" để xác định trần tối đa của Level 2:
  $$\text{Adjusted Level 2 Max} = \frac{2}{3} \times \text{Adjusted Level 1}$$
  Điều này đồng nghĩa nếu ngân hàng suy giảm tài sản Level 1, mức trần tài sản Level 2 được công nhận sẽ tự động co hẹp lại theo tỷ lệ 2/3 [[src-bcbs-lcr#^lcr30-34]].

#### 2. Tác động tới Mẫu số (Total Net Cash Outflows)
- **Huy động vốn có bảo đảm ([[secured-funding]]) bằng Level 1**: Các khoản vay có bảo đảm bằng tài sản Level 1 hoặc vay từ NHTW đáo hạn trong 30 ngày được giả định có **tỷ lệ rút vốn (run-off rate) là 0%** (ngân hàng được giả định có thể tái tục 100% nhờ chất lượng tối thượng của tài sản đảm bảo) [[src-bcbs-lcr#^lcr40-47]] [[src-bcbs-lcr#^lcr40-48]].
- **Cho vay có bảo đảm (Reverse repo) nhận bảo đảm bằng Level 1**: Đáo hạn trong 30 ngày được giả định sẽ tự động gia hạn (roll-over) để duy trì mối quan hệ thị trường, tạo ra **dòng tiền vào (inflow rate) là 0%** [[src-bcbs-lcr#^lcr40-78]].

## Diễn giải

### Cơ chế & drivers

#### Tiêu chuẩn vận hành đối với Level 1 (Operational Requirements)
Để duy trì tính đủ điều kiện trong danh mục HQLA, tài sản Level 1 phải đáp ứng đầy đủ các tiêu chuẩn vận hành theo LCR30:
1. **Trạng thái không bị cầm cố (Unencumbered)**: Toàn bộ tài sản phải hoàn toàn tự do khỏi các ràng buộc pháp lý, quy định hoặc hợp đồng về việc thanh lý, bán, chuyển nhượng [[src-bcbs-lcr#^lcr30-16]].
   - Tài sản ký quỹ tại các tổ chức thanh toán bù trừ hoặc làm tài sản thế chấp cho các khoản vay hiện hữu không được tính vào Level 1.
   - Tài sản nằm trong "collateral pool" dự phòng đặt sẵn tại NHTW (pre-positioned collateral) chỉ được tính phần giá trị thặng dư chưa bị cầm cố (unencumbered portion) và sẵn sàng rút ra trong ngày.
2. **Quyền kiểm soát thuộc Bộ phận Quản lý Thanh khoản (Treasury)**: Danh mục Level 1 phải thuộc thẩm quyền điều phối trực tiếp, liên tục và độc quyền của chức năng quản lý nguồn vốn (Treasury), đảm bảo năng lực pháp lý và vận hành để thanh khoản hóa bất kỳ ngày nào trong 30 ngày stress [[src-bcbs-lcr#^lcr30-18]].
3. **Thử nghiệm thanh khoản hóa định kỳ (Periodic Monetisation)**: Ngân hàng bắt buộc phải định kỳ bán đứt hoặc repo một tỷ lệ đại diện tài sản Level 1 trên thị trường thứ cấp để kiểm tra hạ tầng giao dịch, đường truyền thanh toán và giảm thiểu nguy cơ phát tín hiệu tiêu cực (negative signalling) khi khủng hoảng thực tế diễn ra [[src-bcbs-lcr#^lcr30-15]].
4. **Quyền tái thế chấp (Rehypothecation) và tài sản phái sinh**: Tài sản nhận được qua giao dịch repo hoặc phái sinh mà bên sở hữu hưởng lợi có quyền rút lại trong vòng 30 ngày không được tính vào Level 1 [[src-bcbs-lcr#^lcr30-24]]. Tài sản bảo đảm phái sinh nhận được không bị phong tỏa và được phép tái thế chấp hợp pháp chỉ được đưa vào Level 1 nếu ngân hàng ghi nhận dòng tiền ra tương ứng để hoàn trả [[src-bcbs-lcr#^lcr30-24]].

### Phụ thuộc regime
- **Regime bình thường**: Ngân hàng duy trì tỷ trọng Level 1 áp đảo trong đệm HQLA để tối ưu hóa hạn mức trần Level 2 và tuân thủ các quy định vận hành (segregation, periodic monetisation testing [[src-bcbs-lcr#^lcr30-15]]).
- **Regime stress thanh khoản**:
  - Ngân hàng được toàn quyền sử dụng tài sản Level 1 để bù đắp thâm hụt tiền mặt qua kênh repo với NHTW hoặc bán đứt trên thị trường mở, chấp nhận LCR có thể tạm thời tụt xuống dưới 100% [[src-bcbs-lcr#^lcr20-5]].
  - Cơ quan giám sát áp dụng phản ứng linh hoạt có phân biệt (differentiated response), không tự động xử phạt nếu ngân hàng sử dụng HQLA đúng mục đích phòng vệ thanh khoản [[src-bcbs-lcr#^lcr20-6]].

### Bằng chứng thực nghiệm
- Trong các đợt căng thẳng thanh khoản hệ thống (cuộc khủng hoảng tài chính toàn cầu 2008, khủng hoảng COVID-19 tháng 3/2020), chỉ có trái phiếu chính phủ Level 1 và dự trữ tại NHTW duy trì được biên độ chào mua/chào bán ổn định và năng lực thanh khoản hóa tức thì mà không bị chiết khấu giá trị sâu [[src-bcbs-lcr#^lcr30-2]].
- Ngược lại, các tài sản do định chế tài chính phát hành (kể cả được chính phủ bảo lãnh ngầm) đều bị đóng băng thanh khoản thứ cấp, khẳng định tính đúng đắn của Footnote 11 loại trừ nợ của định chế tài chính [[src-bcbs-lcr#^lcr30-41]].

## Basel vs VN

| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Tên gọi | Level 1 assets [[src-bcbs-lcr#^lcr30-31]] | Tài sản cấp 1 [[src-tt50-2026-nhnn#^d19-1]] | LCR30.31 / TT50 Đ19.1 | VN: LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| Hệ số / haircut | Không haircut, không giới hạn [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-41]] | Hệ số thanh khoản 100%, không bị giới hạn [[src-tt50-2026-nhnn#^pl1-a2]] | LCR30.41 / TT50 PL1.A.II.1 | |
| Quyền hạ hệ số | Supervisor có thể yêu cầu haircut cho chứng khoán Level 1 theo độ nhạy rủi ro lãi suất, thị trường, tín dụng, thanh khoản và haircut repo [[src-bcbs-lcr#^lcr30-40]] | NHNN có quyền yêu cầu hệ số thấp hơn theo độ nhạy rủi ro lãi suất, thị trường, tín dụng, thanh khoản và mức khấu trừ repo [[src-tt50-2026-nhnn#^pl1-a2-2]] | TT50 PL1.A.II.2 | |
| Dự trữ tại NHTW | Phần dự trữ, kể cả dự trữ bắt buộc, được rút khi stress; supervisor thống nhất với NHTW mức được tính [[src-bcbs-lcr#^lcr30-41b]]; tiền gửi kỳ hạn phải rút được theo thông báo hoặc dùng làm bảo đảm vay NHTW [[src-bcbs-lcr#^lcr30-41]] | Tiền gửi tại NHNN, kể cả tiền gửi dự trữ bắt buộc [[src-tt50-2026-nhnn#^pl1-a2]] | LCR30.40 / TT50 PL1.A.II.3.b | |
| Chứng khoán hệ số rủi ro 0% | Chính phủ/NHTW/PSE, BIS, IMF, ECB và Cộng đồng Châu Âu, ESM, EFSF, MDB; hệ số rủi ro 0%; thị trường lớn, sâu, sôi động; lịch sử nguồn thanh khoản tin cậy khi căng thẳng; không là nghĩa vụ của tổ chức tài chính [[src-bcbs-lcr#^lcr30-41a]] | Chính phủ/NHTW/PSE nước ngoài (trừ VN), BIS, IMF, ECB, ESM, EFSF, tổ chức tài chính quốc tế; hệ số rủi ro 0% theo TT14/2025 hoặc TT41/2016; niêm yết; không do tổ chức tài chính phát hành [[src-tt50-2026-nhnn#^pl1-a2-3]]; giảm giá tối đa 5% trong 30 ngày căng thẳng [[src-tt50-2026-nhnn#^pl1-a2]] | LCR30.41 / TT50 PL1.A.II.3.c | |
| Trái phiếu Chính phủ nội tệ | Khi hệ số rủi ro chủ quyền khác 0%: chứng khoán chính phủ/NHTW bằng nội tệ được tính [[src-bcbs-lcr#^lcr30-41]] | Công cụ nợ Chính phủ VN, tín phiếu NHNN bằng VNĐ [[src-tt50-2026-nhnn#^pl1-a2]] | LCR30.41 / TT50 PL1.A.II.3.d | |
| Trái phiếu Chính phủ ngoại tệ | Tối đa bằng dòng tiền ra ròng chịu stress của đồng ngoại tệ đó [[src-bcbs-lcr#^lcr30-41]] | Công cụ nợ Chính phủ VN, tín phiếu NHNN bằng ngoại tệ là cấp 1; điểm này không kèm trần [[src-tt50-2026-nhnn#^pl1-a2]] | LCR30.41 / TT50 PL1.A.II.3.đ | |
| Trái phiếu bảo lãnh, chính quyền địa phương | LCR30.41 không có đầu mục riêng; chứng khoán được chính phủ bảo lãnh vẫn phải hệ số rủi ro 0% và không là nghĩa vụ của tổ chức tài chính [[src-bcbs-lcr#^lcr30-41a]] (*Diễn giải*) | Trái phiếu Chính phủ bảo lãnh 100%; trái phiếu chính quyền địa phương dùng trong giao dịch NHNN theo quyết định của Thống đốc [[src-tt50-2026-nhnn#^pl1-a2]] | TT50 PL1.A.II.3.e | |
| Tài sản của chi nhánh ở nước ngoài | LCR30.41 không có đầu mục riêng; FAQ1 cho tính chứng khoán chính phủ, NHTW dưới AA- của nước có chi nhánh, công ty con (host) vào Level 1 [[src-bcbs-lcr#^lcr30-41-faq]] | Tài sản HQLA của chi nhánh ở nước ngoài đủ điều kiện cấp 1; công cụ nợ Chính phủ/NHTW nước sở tại tối đa bằng dòng tiền ra ròng của chi nhánh đó [[src-tt50-2026-nhnn#^pl1-a2-3g]] | TT50 PL1.A.II.3.g–h | |
| Hạn mức với NHTW | RCLF của NHTW thuộc Level 2B, tuỳ supervisor [[src-bcbs-lcr#^lcr30-46]]; tài sản bảo đảm RCLF không được đồng thời tính vào HQLA [[src-bcbs-lcr#^lcr30-46a]] | Hạn mức chưa sử dụng bảo đảm bằng HQLA cấp 1 với NHNN được coi là tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a1-4]] | TT50 PL1.A.I.4 | |
| Định giá | Level 1 đo không cao hơn giá trị thị trường hiện hành [[src-bcbs-lcr#^lcr30-40]] | Theo giá thị trường hoặc mark-to-model; giấy tờ có giá giao dịch với NHNN lấy giá trị giao dịch thấp nhất theo quy định NHNN [[src-tt50-2026-nhnn#^pl1-a5]] | TT50 PL1.A.V | |

### Tiêu chí xác định theo đầu mục Bảng 3 TT50

Áp cho mọi đầu mục: HQLA chỉ là HQLA đủ tiêu chuẩn khi đáp ứng yêu cầu vận hành Đ20.2 (chuyển đổi được thành tiền trong căng thẳng 30 ngày, không bị ràng buộc, do bộ phận quản lý thanh khoản kiểm soát, xác định hằng ngày) [[src-tt50-2026-nhnn#^d20-2]]. Hệ số rủi ro tính theo quy định tỷ lệ an toàn vốn ngân hàng đang áp dụng (TT14/2025 hoặc TT41/2016) [[src-tt50-2026-nhnn#^pl1-a1-6]]. NHNN có quyền yêu cầu hệ số thanh khoản thấp hơn 100% [[src-tt50-2026-nhnn#^pl1-a2-2]].

| Mục | Tài sản | Tổ chức phát hành / bảo đảm | Hệ số rủi ro | Niêm yết | Giảm giá tối đa 30 ngày căng thẳng | Loại trừ, điều kiện khác | Hệ số | Basel tương ứng |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Tiền mặt [[src-tt50-2026-nhnn#^pl1-a2-3c]] | | | | | Không kèm điều kiện [[src-tt50-2026-nhnn#^pl1-a2-3c]] | 100% [[src-tt50-2026-nhnn#^pl1-a5-1]] | Coins and banknotes [[src-bcbs-lcr#^lcr30-41]] |
| 1.2 | Tiền gửi tại NHNN, kể cả tiền gửi dự trữ bắt buộc [[src-tt50-2026-nhnn#^pl1-a2-3b]] | NHNN | | | | Không kèm điều kiện về khả năng rút khi căng thẳng [[src-tt50-2026-nhnn#^pl1-a2-3b]] | 100% [[src-tt50-2026-nhnn#^pl1-a5-1]] | Dự trữ NHTW, kể cả dự trữ bắt buộc, trong phạm vi được rút khi stress [[src-bcbs-lcr#^lcr30-41b]]; tiền gửi kỳ hạn phải rút được theo thông báo hoặc là khoản cho vay mà ngân hàng vay lại được [[src-bcbs-lcr#^lcr30-41]]; tiền gửi kỳ hạn khác không đủ điều kiện [[src-bcbs-lcr#^lcr30-41b]] |
| 1.3 | Chứng khoán nước ngoài, tổ chức quốc tế | Chính phủ, NHTW, PSE các nước trừ VN; BIS; IMF; ECB và Cộng đồng Châu Âu; ESM; EFSF hoặc tổ chức tài chính quốc tế; phát hành hoặc bảo đảm [[src-tt50-2026-nhnn#^pl1-a2-3c]] | 0% [[src-tt50-2026-nhnn#^pl1-a2-3c]] | Phải niêm yết [[src-tt50-2026-nhnn#^pl1-a2-3c]] | ≤ 5% (giá hoặc chiết khấu), lịch sử 10 năm [[src-tt50-2026-nhnn#^pl1-a2-3c]] | Không do tổ chức tài chính hoặc công ty mẹ, con, liên kết của tổ chức tài chính phát hành [[src-tt50-2026-nhnn#^pl1-a2-3c]] | 100% [[src-tt50-2026-nhnn#^pl1-a5-1]] | Cùng danh sách tổ chức phát hành, thêm MDB; hệ số rủi ro 0%; thị trường repo hoặc giao ngay lớn, sâu, sôi động, tập trung thấp; lịch sử nguồn thanh khoản tin cậy khi căng thẳng; không là nghĩa vụ của tổ chức tài chính (ngoại lệ ngân hàng là PSE) [[src-bcbs-lcr#^lcr30-41a]]. Không yêu cầu niêm yết, không đặt ngưỡng giảm giá 5% [[src-bcbs-lcr#^lcr30-41a]] (*Diễn giải*) |
| 1.4.1 | Công cụ nợ Chính phủ VN (trái phiếu Chính phủ, tín phiếu Kho bạc), tín phiếu NHNN bằng VNĐ [[src-tt50-2026-nhnn#^pl1-a2-3d]] | Chính phủ VN, NHNN | | | | Không kèm điều kiện [[src-tt50-2026-nhnn#^pl1-a2-3d]] | 100% [[src-tt50-2026-nhnn#^pl1-a5-1]] | Chứng khoán chính phủ/NHTW bằng nội tệ khi hệ số rủi ro chủ quyền khác 0% [[src-bcbs-lcr#^lcr30-41]] |
| 1.4.2 | Công cụ nợ Chính phủ VN, tín phiếu NHNN bằng ngoại tệ [[src-tt50-2026-nhnn#^pl1-a2-3dd]] | Chính phủ VN, NHNN | | | | Không kèm trần [[src-tt50-2026-nhnn#^pl1-a2-3dd]] | 100% [[src-tt50-2026-nhnn#^pl1-a5-1]] | Tối đa bằng dòng tiền ra ròng chịu stress của đồng ngoại tệ đó [[src-bcbs-lcr#^lcr30-41]] |
| 1.5 | Trái phiếu Chính phủ bảo lãnh 100% gốc, lãi; trái phiếu chính quyền địa phương [[src-tt50-2026-nhnn#^pl1-a2-3e]] | Chính phủ bảo lãnh; chính quyền địa phương | | | | Trái phiếu chính quyền địa phương phải được dùng trong giao dịch của NHNN theo quyết định của Thống đốc từng thời kỳ [[src-tt50-2026-nhnn#^pl1-a2-3e]] | 100% [[src-tt50-2026-nhnn#^pl1-a5-1]] | Không có đầu mục tương ứng trong LCR30.41 (*Diễn giải*) |
| 1.6 | Tài sản HQLA của chi nhánh ở nước ngoài của NHTM [[src-tt50-2026-nhnn#^pl1-a2-3g]] | | | | | Phải đủ điều kiện HQLA cấp 1 đủ tiêu chuẩn theo TT50 [[src-tt50-2026-nhnn#^pl1-a2-3g]] | 100% [[src-tt50-2026-nhnn#^pl1-a5-1]] | Không có đầu mục tương ứng trong LCR30.41 (*Diễn giải*) |
| 1.7 | Công cụ nợ Chính phủ, NHTW nước sở tại của chi nhánh ở nước ngoài [[src-tt50-2026-nhnn#^pl1-a2-3h]] | Chính phủ, NHTW nước sở tại | | | | Thuộc danh mục HQLA của chi nhánh; tối đa bằng dòng tiền ra ròng của chi nhánh đó [[src-tt50-2026-nhnn#^pl1-a2-3h]] | 100% [[src-tt50-2026-nhnn#^pl1-a5-1]] | Cùng logic trần ngoại tệ ở LCR30.41 [[src-bcbs-lcr#^lcr30-41]] (*Diễn giải*) |
| 5.1 | Hạn mức chưa sử dụng với NHNN [[src-tt50-2026-nhnn#^pl1-a1-4]] | NHNN | | | | Phải được bảo đảm bởi HQLA cấp 1; coi là tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a1-4]] | | RCLF của NHTW thuộc Level 2B, tuỳ supervisor [[src-bcbs-lcr#^lcr30-46]] |

Ô trống nghĩa là TT50 không đặt tiêu chí đó cho đầu mục.

*Diễn giải:*
- PL1 Phần A TT50 không đặt trần dòng tiền ra ròng cho công cụ nợ Chính phủ VN bằng ngoại tệ, khác LCR30.41; trần này chỉ xuất hiện ở công cụ nợ Chính phủ nước sở tại của chi nhánh ở nước ngoài. Chưa rà LCR ngoại tệ trọng yếu (Đ16) có bù cho điểm này hay không.
- Basel không yêu cầu niêm yết và lịch sử giá cho chứng khoán chủ quyền cấp 1. TT50 thêm hai điều kiện này cho chứng khoán nước ngoài.
- Quyền hạ hệ số của NHNN làm "hệ số 100%" không còn là hằng số với từng ngân hàng.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **Basel**: Thiết lập Level 1 là lớp bảo vệ tuyệt đối, miễn trừ toàn bộ haircut và trần định lượng, chỉ chấp nhận các tài sản gần như phi rủi ro tín dụng hoặc được bảo trợ bởi NHTW [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-41]].
- **ALM / Quản trị bảng cân đối**:
  - *Chi phí cơ hội (Negative Carry)*: Tài sản Level 1 (đặc biệt là tiền gửi NHTW và trái phiếu chính phủ ngắn hạn) có lợi suất thấp nhất trên bảng cân đối, gây áp lực bào mòn tỷ lệ thu nhập lãi thuần ([[net-interest-margin|NIM]]). Bộ phận ALM phải tính toán bài toán tối ưu giữa chi phí nắm giữ Level 1 và chi phí an toàn thanh khoản.
  - *Rủi ro lãi suất trên sổ ngân hàng ([[bcbs-irrbb|IRRBB]])*: Việc nắm giữ trái phiếu chính phủ dài hạn cố định lãi suất để đáp ứng Level 1 tiềm ẩn rủi ro giảm giá trị kinh tế [[economic-value-of-equity|$\Delta\text{EVE}$]] khi lãi suất tăng vọt, đe dọa trực tiếp ngưỡng [[outlier-bank-test|15% Vốn cấp 1]]. ALM Desk phải thực hiện phòng ngừa thời lượng (duration hedging) qua hợp đồng hoán đổi lãi suất (IRS) hoặc ưu tiên phân bổ tín phiếu/trái phiếu thả nổi.
  - *Chuyển dịch NSFR*: Trong chuẩn mực [[nsfr]], tiền mặt và dự trữ tại NHTW nhận RSF 0% [[src-bcbs-nsfr#^nsf30-25]], trong khi chứng khoán nợ Level 1 unencumbered chỉ chịu hệ số RSF rất thấp là 5% [[src-bcbs-nsfr#^nsf30-26]], tạo ra đòn bẩy kép tối ưu cho bảng cân đối ALM.
- **VN**: theo [[tt50-2026|TT50/2026]], tài sản cấp 1 có hệ số thanh khoản 100%, không bị giới hạn; gồm tiền mặt, tiền gửi tại NHNN (kể cả dự trữ bắt buộc), công cụ nợ Chính phủ VN và tín phiếu NHNN bằng VNĐ và ngoại tệ, trái phiếu Chính phủ bảo lãnh 100%, trái phiếu chính quyền địa phương được dùng trong giao dịch NHNN theo quyết định của Thống đốc, và chứng khoán Chính phủ/NHTW nước ngoài có hệ số rủi ro 0%, niêm yết, giảm giá tối đa 5% trong 30 ngày căng thẳng [[src-tt50-2026-nhnn#^pl1-a2]]. Hạn mức chưa sử dụng bảo đảm bằng HQLA cấp 1 với NHNN được coi là tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a1-4]]. Ngoài LCR, số dư TPCP, trái phiếu được Chính phủ bảo lãnh bị trần 30% Tổng Nợ phải trả bình quân tháng liền kề trước, xem [[government-bond-holding-ratio]] [[src-tt50-2026-nhnn#^d28-1]]. Đối chiếu từng tham số với Basel: mục `## Basel vs VN`.

## Câu hỏi mở
- Tại Việt Nam, theo cơ chế quản lý của NHNN, phần tiền gửi dự trữ bắt buộc hàng tháng có được coi là đủ điều kiện "cho phép rút ra trong giai đoạn stress" [[src-bcbs-lcr#^lcr30-41]] để tính toàn bộ hay một phần vào Tài sản cấp 1 theo TT50/2026?
