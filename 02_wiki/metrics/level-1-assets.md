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
updated: 2026-10-16
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
| **4. Trái phiếu Chính phủ / NHTW nội tệ (khi Sovereign có RW > 0%)** | Chứng khoán nợ do chính phủ hoặc NHTW phát hành bằng đồng nội tệ tại quốc gia nơi ngân hàng gánh chịu rủi ro thanh khoản hoặc tại quốc gia của ngân hàng mẹ [[src-bcbs-lcr#^lcr30-41]]. | Áp dụng tại các quốc gia mà xếp hạng tín nhiệm của chính phủ không đạt mức RW 0% (ví dụ các thị trường mới nổi có RW 20%, 50%...). Toàn bộ trái phiếu chính phủ phát hành bằng đồng nội tệ vẫn được công nhận là Level 1 vì NHTW có quyền năng tối thượng trong việc tạo lập thanh khoản đồng nội tệ [[src-bcbs-lcr#^lcr30-41]]. |
| **5. Trái phiếu Chính phủ / NHTW ngoại tệ (khi Sovereign có RW > 0%)** | Chứng khoán nợ do chính phủ hoặc NHTW sở tại phát hành bằng đồng ngoại tệ (khi chính phủ có RW > 0%) [[src-bcbs-lcr#^lcr30-41]]. | **Giới hạn trần đặc thù**: Chỉ được công nhận là Level 1 tối đa bằng quy mô **dòng tiền ra ròng chịu stress của chính đồng ngoại tệ đó** phát sinh từ hoạt động của ngân hàng tại quốc gia liên quan [[src-bcbs-lcr#^lcr30-41]]. Phần giá trị vượt quá nhu cầu ròng của đồng ngoại tệ này không được tính vào Level 1. |

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

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **Basel**: Thiết lập Level 1 là lớp bảo vệ tuyệt đối, miễn trừ toàn bộ haircut và trần định lượng, chỉ chấp nhận các tài sản gần như phi rủi ro tín dụng hoặc được bảo trợ bởi NHTW [[src-bcbs-lcr#^lcr30-31]] [[src-bcbs-lcr#^lcr30-41]].
- **ALM / Quản trị bảng cân đối**:
  - *Chi phí cơ hội (Negative Carry)*: Tài sản Level 1 (đặc biệt là tiền gửi NHTW và trái phiếu chính phủ ngắn hạn) có lợi suất thấp nhất trên bảng cân đối, gây áp lực bào mòn tỷ lệ thu nhập lãi thuần ([[net-interest-margin|NIM]]). Bộ phận ALM phải tính toán bài toán tối ưu giữa chi phí nắm giữ Level 1 và chi phí an toàn thanh khoản.
  - *Rủi ro lãi suất trên sổ ngân hàng ([[bcbs-irrbb|IRRBB]])*: Việc nắm giữ trái phiếu chính phủ dài hạn cố định lãi suất để đáp ứng Level 1 tiềm ẩn rủi ro giảm giá trị kinh tế [[economic-value-of-equity|$\Delta\text{EVE}$]] khi lãi suất tăng vọt, đe dọa trực tiếp ngưỡng [[outlier-bank-test|15% Vốn cấp 1]]. ALM Desk phải thực hiện phòng ngừa thời lượng (duration hedging) qua hợp đồng hoán đổi lãi suất (IRS) hoặc ưu tiên phân bổ tín phiếu/trái phiếu thả nổi.
  - *Chuyển dịch NSFR*: Trong chuẩn mực [[nsfr]], tiền mặt và dự trữ tại NHTW nhận RSF 0% [[src-bcbs-nsfr#^nsf30-25]], trong khi chứng khoán nợ Level 1 unencumbered chỉ chịu hệ số RSF rất thấp là 5% [[src-bcbs-nsfr#^nsf30-26]], tạo ra đòn bẩy kép tối ưu cho bảng cân đối ALM.
- **VN**: theo [[tt50-2026|TT50/2026]], tài sản cấp 1 có hệ số thanh khoản 100%, không bị giới hạn; gồm tiền mặt, tiền gửi tại NHNN (kể cả dự trữ bắt buộc), công cụ nợ Chính phủ VN và tín phiếu NHNN bằng VNĐ và ngoại tệ, trái phiếu Chính phủ bảo lãnh 100%, trái phiếu chính quyền địa phương được dùng trong giao dịch NHNN theo quyết định của Thống đốc, và chứng khoán Chính phủ/NHTW nước ngoài có hệ số rủi ro 0%, niêm yết, giảm giá tối đa 5% trong 30 ngày căng thẳng [[src-tt50-2026-nhnn#^pl1-a2]]. Hạn mức chưa sử dụng bảo đảm bằng HQLA cấp 1 với NHNN được coi là tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a1-4]]. *Diễn giải:* Basel không yêu cầu niêm yết và lịch sử giá cho chứng khoán chủ quyền cấp 1; TT50 thêm hai điều kiện này cho chứng khoán nước ngoài.

## Câu hỏi mở
- Tại Việt Nam, theo cơ chế quản lý của NHNN, phần tiền gửi dự trữ bắt buộc hàng tháng có được coi là đủ điều kiện "cho phép rút ra trong giai đoạn stress" [[src-bcbs-lcr#^lcr30-41]] để tính toàn bộ hay một phần vào Tài sản cấp 1 theo TT50/2026?
