---
title: Derivatives liquidity needs and contingent funding obligations (LCR)
aliases: [Derivatives and contingent outflows, Nhu cầu thanh khoản phái sinh và nghĩa vụ tiềm tàng, Contingent funding obligations, Phái sinh và nghĩa vụ tiềm tàng LCR]
type: metric
domains: [alm, basel, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]"]
relations:
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-49]]"}
  - {type: input-to, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr40-51]]"}
tags: [derivatives, collateral, contingent, liquidity, stress-test]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

**Nhu cầu thanh khoản phái sinh và nghĩa vụ tài trợ tiềm tàng** (*Derivatives liquidity needs and contingent funding obligations*) là nhóm dòng tiền ra phức tạp và có tính biến động cao nhất trong mẫu số [[net-cash-outflows]] của [[lcr]] [[src-bcbs-lcr#^lcr40-1]]. 

Không giống như các dòng tiền gửi có kỳ hạn hoặc khoản vay thông thường với lịch trả nợ cố định, nhóm này bao gồm:
1. Dòng tiền thanh toán ròng và nghĩa vụ ký quỹ tài sản bảo đảm (*margin collateral*) phát sinh từ các hợp đồng phái sinh khi thị trường biến động [[src-bcbs-lcr#^lcr40-49]] [[src-bcbs-lcr#^lcr40-56]].
2. Các nghĩa vụ thanh khoản bị kích hoạt tự động theo các sự kiện pháp lý hoặc tín dụng, đặc biệt là khi ngân hàng bị hạ bậc tín nhiệm dài hạn tới 3 bậc (*downgrade triggers*) [[src-bcbs-lcr#^lcr40-51]].
3. Rủi ro thanh khoản cấu trúc từ việc tài trợ công cụ nợ có bảo đảm bằng tài sản (ABCP, Conduits, SIVs) và các điều khoản quyền chọn bán thanh khoản (*liquidity puts*) [[src-bcbs-lcr#^lcr40-58]].
4. Các cam kết tài trợ tiềm tàng bắt nguồn từ [[reputational-risk|rủi ro uy tín]] (*reputational risk*) nhằm hỗ trợ các sản phẩm ngân hàng bảo trợ hoặc các liên doanh phi hợp nhất [[src-bcbs-lcr#^lcr40-68]] [[src-bcbs-lcr#^lcr40-70]].

---

## Công thức & tham số

### 1. Dòng tiền Phái sinh Ròng (Net Derivatives Cash Flows)

#### Nguyên tắc tính toán và Bù trừ Song phương
Theo [[src-bcbs-lcr#^lcr40-49]], tổng dòng tiền ra phái sinh ròng được áp hệ số **100%**:
- **Bù trừ theo đối tác (*Counterparty Netting*)**: Dòng tiền thu và dòng tiền chi phát sinh từ các giao dịch phái sinh chỉ được phép tính bù trừ ròng (*net basis*) khi và chỉ khi hai bên có một thỏa thuận bù trừ song phương có hiệu lực pháp lý (*valid bilateral master netting agreement*, ví dụ ISDA Master Agreement) [[src-bcbs-lcr#^lcr40-49]].
- Nếu không có master netting agreement hợp lệ, ngân hàng phải tính gộp toàn bộ dòng ra mà không được khấu trừ dòng vào.
- **Ngoại lệ giao dịch ngoại hối giao ngay/kỳ hạn (*FX Netting Exception*)**: Các giao dịch hoán đổi ngoại hối (FX swaps/forwards) có sự trao đổi toàn bộ tiền gốc diễn ra đồng thời (hoặc trong cùng một ngày) được phép ghi nhận theo dòng tiền ròng ngay cả khi không có master netting agreement [[src-bcbs-lcr#^lcr40-49]].

#### Giả định thực hiện Quyền chọn (*Option Exercise Assumptions*)
- Mọi hợp đồng quyền chọn (options) có thể được thực hiện trong vòng 30 ngày (bao gồm cả các quyền chọn kiểu Mỹ *American-style options* có ngày đáo hạn danh nghĩa $> 30$ ngày nhưng người mua có quyền thực hiện bất kỳ lúc nào) **bắt buộc phải giả định bị thực hiện nếu quyền chọn đang ở trạng thái có lãi (*in the money*) đối với bên mua** [[src-bcbs-lcr#^lcr40-49]].
- Nếu ngân hàng là bên bán quyền chọn (*option writer*) và quyền chọn đang *in the money*, ngân hàng phải ghi nhận 100% dòng tiền chi trả hoặc chuyển giao tài sản.
- Ngược lại, nếu ngân hàng là bên mua quyền chọn và đang *in the money*, ngân hàng được ghi nhận dòng tiền vào (xem [[cash-inflows]], [[src-bcbs-lcr#^lcr40-91]]).

#### Quy tắc Tài sản Rẻ nhất để Giao (*Cheapest to Deliver*)
- Đối với các hợp đồng phái sinh mà nghĩa vụ giao nhận có thể được thực hiện bằng nhiều loại tài sản khác nhau, chuẩn mực quy định áp dụng nguyên tắc bất đối xứng thận trọng: **bên có nghĩa vụ giao sẽ chọn tài sản có giá trị thanh khoản thấp nhất trong LCR (*cheapest to deliver / lowest liquidity value*)** [[src-bcbs-lcr#^lcr40-49]].
- Quy tắc này áp dụng đồng bộ cho cả hai vế: khi ngân hàng phải giao tài sản, ngân hàng giả định giao tài sản thanh khoản kém nhất; khi đối tác phải giao cho ngân hàng, ngân hàng cũng phải giả định đối tác sẽ giao tài sản có giá trị thanh khoản thấp nhất [[src-bcbs-lcr#^lcr40-49]].

#### Phái sinh bảo đảm bằng HQLA (Chống đếm trùng)
- Khi nghĩa vụ thanh toán phái sinh được bảo đảm bằng [[hqla]], dòng tiền ra được tính ròng với dòng tiền hoặc tài sản bảo đảm nhận về nếu ngân hàng có đầy đủ quyền pháp lý và năng lực vận hành để tái sử dụng tài sản đó trong các giao dịch huy động tiền mặt mới [[src-bcbs-lcr#^lcr40-50]].

---

### 4. Biến động Định giá Thị trường: Phương pháp Hồi quy 24 tháng (Look-back Approach)

Chuẩn mực LCR40.56 quy định cách đo lường rủi ro thanh khoản phát sinh từ các cuộc gọi ký quỹ (*variation margin calls*) khi giá trị thị trường của danh mục phái sinh biến động bất lợi:

#### Thuật toán Look-back Approach
1. **Dữ liệu lịch sử**: Ngân hàng phải thu thập toàn bộ dữ liệu dòng tiền và tài sản bảo đảm ký quỹ ròng hàng ngày trong suốt **24 tháng** gần nhất [[src-bcbs-lcr#^lcr40-56]].
2. **Cửa sổ trượt 30 ngày (*Rolling 30-day window*)**: Tính toán dòng ký quỹ ròng tích lũy tại ngày kết thúc của mọi khoảng thời gian 30 ngày liên tục trong 24 tháng đó (FAQ1 LCR40.56):
   $$\text{Net 30-day Collateral Flow}(t) = \sum_{k=0}^{29} \Big(\text{Collateral Outflows}(t-k) - \text{Collateral Inflows}(t-k)\Big)$$
3. **Xác định giá trị đỉnh**:
   $$\text{Look-back Outflow Buffer} = \max_{t \in [0, 24\text{M}]} \Big|\text{Net 30-day Collateral Flow}(t)\Big|$$
- Giá trị tuyệt đối lớn nhất này phải được đưa trực tiếp vào mẫu số LCR như một dòng tiền ra dự phòng bắt buộc [[src-bcbs-lcr#^lcr40-56]].
- **Phạm vi tính toán**: Tính trên cấp độ toàn bộ danh mục (*portfolio level*) sau khi đã bù trừ các giao dịch thuộc cùng master netting agreement.
- **Xử lý phái sinh STM (*Settled-to-Market*)**: Các khoản thanh toán biến động định giá hàng ngày đối với phái sinh bù trừ qua CCP có cấu trúc STM được xử lý bình đẳng như các dòng luân chuyển tài sản bảo đảm thông thường (FAQ2 LCR40.56).

---

## Diễn giải

### 2. Rủi ro Kích hoạt Hạ bậc Tín nhiệm (Downgrade Triggers)

#### Cơ chế hoạt động trong hợp đồng ISDA/CSA
Trong thực tiễn thị trường vốn quốc tế, các phụ lục bảo đảm tín dụng (*Credit Support Annex - CSA*) hoặc hợp đồng tài trợ thường có các điều khoản ràng buộc theo xếp hạng tín nhiệm (*credit rating triggers*):
- Khi một bên bị các tổ chức xếp hạng tín nhiệm (Moody's, S&P, Fitch) hạ bậc tín nhiệm xuống dưới một ngưỡng nhất định (ví dụ mất hạng A xuống BBB, hoặc mất hạng đầu tư *Investment Grade* xuống *High Yield*):
  1. Ngưỡng miễn trừ ký quỹ (*Threshold Amount*) bị hạ về 0, buộc bên bị hạ bậc phải nộp 100% tài sản bảo đảm cho toàn bộ giá trị phơi nhiễm thị trường (*mark-to-market*).
  2. Mức ký quỹ ban đầu tối thiểu (*Independent Amount*) tăng lên.
  3. Đối tác có quyền yêu cầu tất toán trước hạn (*early termination*) hợp đồng hoặc thu hồi các hạn mức tài trợ cam kết.

#### Yêu cầu của Basel LCR
Theo [[src-bcbs-lcr#^lcr40-51]]:
- Ngân hàng bắt buộc phải giả định kịch bản bị **hạ tới 3 bậc tín nhiệm dài hạn** (*up to and including a 3-notch downgrade*) đối với xếp hạng tín nhiệm của chính ngân hàng.
- Ngân hàng phải tính dòng ra bằng **100% lượng tiền mặt hoặc tài sản bảo đảm bổ sung** phải nộp hoặc các dòng tiền rút vốn bị kích hoạt bởi đợt hạ 3 bậc này [[src-bcbs-lcr#^lcr40-51]].
- Đối với các điều khoản gắn với xếp hạng ngắn hạn, ngân hàng phải quy đổi tương đương sang thang xếp hạng dài hạn theo tiêu chuẩn công bố của tổ chức xếp hạng.
- Đánh giá tác động phải bao gồm toàn bộ các thay đổi về quyền tái thế chấp (*rehypothecation rights*) đối với tài sản bảo đảm không tách biệt [[src-bcbs-lcr#^lcr40-51]].

---

### 3. Rủi ro Định giá và Thay thế Tài sản Bảo đảm (Collateral Valuation & Substitution)

Basel LCR40 đặt ra 4 quy định nghiêm ngặt để dự phòng các rủi ro sụt giá hoặc thất thoát tài sản bảo đảm:

```mermaid
graph TD
    CollateralRisks["Rủi Ro Tài Sản Bảo Đảm Phái Sinh"]
    CollateralRisks --> NonL1["1. Ký quỹ bằng Non-Level 1: Phạt thêm 20% giá trị (LCR40.52)"]
    CollateralRisks --> ExcessRecall["2. TSBĐ nộp thừa đối tác có quyền rút: Dòng ra 100% (LCR40.53)"]
    CollateralRisks --> DueNotCalled["3. Ký quỹ đến hạn chưa bị đòi: Dòng ra 100% (LCR40.54)"]
    CollateralRisks --> Substitution["4. Quyền thay thế TSBĐ sang non-HQLA: Dòng ra 100% (LCR40.55)"]
```

#### 1. Phạt bổ sung đối với Tài sản bảo đảm Non-Level 1 (LCR40.52)
- Hầu hết các giao dịch phái sinh trên thị trường được ký quỹ bằng tiền mặt hoặc trái phiếu chính phủ 0% rủi ro ([[level-1-assets]]). Khi sử dụng tài sản Level 1, chuẩn mực không yêu cầu dự phòng thêm.
- Tuy nhiên, nếu ngân hàng ký quỹ cho đối tác bằng các tài sản khác (Level 2A, Level 2B hoặc non-HQLA), để bù đắp rủi ro tài sản bị sụt giá khi thị trường biến động:
  $$\text{Dòng ra bổ sung} = 20\% \times \text{Giá trị danh nghĩa TSBĐ non-L1 đã ký quỹ}$$
- Khoản 20% này phải được tính ròng theo từng đối tác và **cấm tuyệt đối việc bù trừ dòng tài sản giữa các đối tác khác nhau** (FAQ3 LCR40.52) [[src-bcbs-lcr#^lcr40-52]].

#### 2. Tài sản bảo đảm không tách biệt nộp thừa (LCR40.53)
- Nếu đối tác đã nộp tài sản bảo đảm vượt mức yêu cầu ký quỹ hiện tại (*excess collateral*), và phần tài sản này không nằm trong tài khoản phong tỏa tách biệt (*non-segregated account*):
  - Do đối tác có quyền rút lại phần thừa này bất kỳ lúc nào theo hợp đồng, ngân hàng phải tính **100% dòng ra** cho toàn bộ phần tài sản bảo đảm dư thừa đó [[src-bcbs-lcr#^lcr40-53]].

#### 3. Tài sản bảo đảm đến hạn theo hợp đồng nhưng chưa bị đòi (LCR40.54)
- Nếu theo biến động định giá vị thế thị trường (*mark-to-market*), ngân hàng có nghĩa vụ phải nộp thêm tiền hoặc tài sản bảo đảm cho đối tác nhưng đối tác chưa gửi yêu cầu ký quỹ (*margin call*):
  - Ngân hàng không được chủ quan; chuẩn mực yêu cầu phải ghi nhận ngay **100% dòng ra** đối với khoản bảo đảm này [[src-bcbs-lcr#^lcr40-54]].

#### 4. Quyền thay thế tài sản bảo đảm đơn phương (LCR40.55)
- Nếu hợp đồng cho phép đối tác có quyền rút lại tài sản bảo đảm HQLA đang gửi tại ngân hàng và thay thế bằng tài sản non-HQLA mà **không cần sự chấp thuận của ngân hàng**:
  - Ngân hàng phải tính **100% dòng ra** đối với toàn bộ phần HQLA có thể bị thay thế [[src-bcbs-lcr#^lcr40-55]].
  - Nếu đối tác có quyền thay thế HQLA bậc cao (Level 1) bằng HQLA bậc thấp hơn (Level 2A hoặc 2B), dòng ra được tính bằng **chênh lệch giữa mức haircut** của hai loại tài sản [[src-bcbs-lcr#^lcr40-55]].

---

### 5. Rủi ro Tài trợ Cấu trúc: ABCP, Conduits, SIVs và Covered Bonds

#### 1. Trái phiếu bảo đảm (Covered Bonds) & ABS tự phát hành (LCR40.57)
- Các công cụ chứng khoán hóa (ABS), trái phiếu có bảo đảm (*covered bonds*) do chính ngân hàng phát hành đáo hạn trong vòng 30 ngày phải chịu dòng ra **100%** [[src-bcbs-lcr#^lcr40-57]].
- *Giả định*: Trong khủng hoảng, thị trường phát hành mới để đảo nợ (*refinancing market*) hoàn toàn biến mất.
- *Khấu trừ tài sản giải tỏa*: Dòng ra này được phép bù trừ với lượng HQLA nằm trong nhóm tài sản bảo đảm (*cover pool*) được giải chấp và trở nên khả dụng khi trái phiếu đáo hạn [[src-bcbs-lcr#^lcr40-57]].

#### 2. Thương phiếu bảo đảm bằng tài sản (ABCP) & SIVs (LCR40.58)
Đối với các cấu trúc tài trợ thông qua pháp nhân chuyên biệt (*Special Purpose Entity - SPE* như Conduit hay SIV), ngân hàng phải thực hiện **nhìn xuyên (*look-through*)** cấu trúc bất kể SPE có được hợp nhất vào báo cáo tài chính hay không [[src-bcbs-lcr#^lcr40-58]]:

| Yếu tố rủi ro thanh khoản tiềm ẩn | Lượng HQLA / Dòng ra bắt buộc | Căn cứ chuẩn mực |
|---|---|---|
| Nợ ngắn hạn (ABCP) do SPE phát hành đáo hạn $\le 30$ ngày | **100%** giá trị đáo hạn | [[src-bcbs-lcr#^lcr40-58]] |
| Điều khoản quyền chọn bán thanh khoản (*Liquidity Puts*) cho phép trả lại tài sản cho ngân hàng | **100%** giá trị tài sản có thể bị trả lại hoặc thanh khoản yêu cầu | [[src-bcbs-lcr#^lcr40-58]] |

---

### 6. Các Nghĩa vụ Tài trợ Tiềm tàng Khác (Contingent Funding Obligations)

Theo [[src-bcbs-lcr#^lcr40-67]] đến [[src-bcbs-lcr#^lcr40-74]], cơ quan thanh tra giám sát quốc gia có thẩm quyền quy định hệ số run-off đối với các nghĩa vụ tiềm tàng ngoài hợp đồng:

```mermaid
flowchart TD
    Contingent["Nghĩa Vụ Tài Trợ Tiềm Tàng Khác"]
    Contingent --> Trade["Tài trợ thương mại: Run-off <= 5% (LCR40.71)"]
    Contingent --> Reputational["Rủi ro uy tín & Quỹ bảo trợ: National discretion (LCR40.68)"]
    Contingent --> Structured["Trái phiếu Autocallable & Triggers: Phân tích kịch bản (LCR40.69)"]
    Contingent --> Unconsolidated["Liên doanh phi hợp nhất: Cấp thanh khoản chính (LCR40.70)"]
    Contingent --> MatchedShorts["Bán khống bù trừ nội bộ bằng non-HQLA: Run-off >= 50% (LCR40.73)"]
```

#### 1. Tài trợ thương mại (Trade Finance - LCR40.71)
- Các công cụ tài trợ thương mại gắn trực tiếp với sự luân chuyển hàng hóa và cung ứng dịch vụ thực tế (thư tín dụng chứng từ L/C, nhờ thu, bảo lãnh nhận hàng *shipping guarantees*) chịu tỷ lệ rút vốn rất thấp, thường là **$\le 5\%$** [[src-bcbs-lcr#^lcr40-71]].
- *Lưu ý*: Các khoản cam kết cho vay xuất nhập khẩu trực tiếp cho doanh nghiệp không được xếp vào trade finance mà phải chịu tỷ lệ drawdown của hạn mức tín dụng 10%–30% theo LCR40.64.

#### 2. Nghĩa vụ tiềm tàng phi hợp đồng vì Rủi ro Uy tín (Reputational Risk - LCR40.68)
- Phát sinh khi ngân hàng đóng vai trò tài trợ (*sponsor*) hoặc bán các sản phẩm đầu tư mà khách hàng có kỳ vọng về tính thanh khoản ổn định (ví dụ các quỹ tương hỗ thị trường tiền tệ MMF giữ giá trị ổn định *stable NAV*).
- Trong stress, nếu ngân hàng không can thiệp mua lại tài sản hoặc cấp vốn, uy tín thương hiệu sẽ bị tổn hại nghiêm trọng, dẫn đến tháo chạy tiền gửi. Supervisor có quyền yêu cầu trích lập dòng ra cho các cam kết ngầm định này [[src-bcbs-lcr#^lcr40-68]].

#### 3. Công cụ nợ có điều kiện kích hoạt thị trường (Autocallable Notes - LCR40.69)
- Các trái phiếu cấu trúc (*autocallable notes*) tự động đáo hạn khi một chỉ số thị trường chạm ngưỡng kích hoạt (*market-based trigger*). Ngân hàng và cơ quan giám sát phải phân tích xác suất chạm ngưỡng trong kịch bản stress để xác định dòng tiền mua lại trước hạn [[src-bcbs-lcr#^lcr40-69]].

#### 4. Vị thế bán khống của khách hàng bù trừ nội bộ (LCR40.73(5))
- Nếu ngân hàng ghép cặp nội bộ (*internally match*) tài sản của một khách hàng này để bù đắp cho vị thế bán khống của một khách hàng khác bằng tài sản **không phải HQLA (non-HQLA)**:
  - Ngân hàng phải áp dụng tỷ lệ dòng ra **tối thiểu 50%**, vì khi khách hàng sở hữu tài sản rút tiền, ngân hàng bắt buộc phải tìm nguồn tài trợ khẩn cấp từ bên ngoài để bù đắp vị thế bán khống đang hở [[src-bcbs-lcr#^lcr40-73]].

---

## Ứng dụng trong ALM

### 7. Góc nhìn Quản trị ALM Treasury & Chiến lược Tối ưu hóa

Nhóm nhu cầu thanh khoản phái sinh và nghĩa vụ tiềm tàng thường là "vùng mù" (*blind spot*) của các ngân hàng truyền thống, nhưng lại là nguồn rút cạn thanh khoản nhanh nhất trong khủng hoảng:

1. **Tối ưu hóa Tài sản Ký quỹ CSA (*Collateral Engineering*)**:
   - Khối Treasury phải thiết lập thuật toán lựa chọn tài sản ký quỹ tối ưu (*cheapest-to-deliver optimization*). Bằng mọi giá tránh sử dụng trái phiếu doanh nghiệp hoặc cổ phiếu non-Level 1 để ký quỹ phái sinh, vì khoản phạt cộng thêm 20% giá trị theo LCR40.52 sẽ làm gia tăng đáng kể mẫu số LCR.
2. **Quản trị Rủi ro Hạ bậc Tín nhiệm (*Downgrade Mitigation*)**:
   - Định kỳ chạy mô hình mô phỏng dòng tiền thanh toán tức thì khi bị hạ 1, 2 và 3 notch trên toàn bộ danh mục hợp đồng song phương ISDA/CSA.
   - Chủ động đàm phán chuyển đổi các giao dịch phái sinh song phương (*bilateral OTC*) sang thanh toán bù trừ qua đối tác trung tâm (*Central Counterparty - CCP*), nơi các yêu cầu ký quỹ được chuẩn hóa và không có các điều khoản downgrade triggers tùy nghi.
3. **Theo dõi Đỉnh Dòng tiền Ký quỹ 24 tháng (*Look-back Peak Monitoring*)**:
   - Xây dựng dashboard tự động tính toán dòng ký quỹ ròng lũy kế 30 ngày theo chuỗi thời gian thực.
   - Khi các đợt biến động mạnh trong quá khứ dần lùi ra khỏi cửa sổ 24 tháng, đệm dự phòng thanh khoản của ngân hàng sẽ tự động giảm xuống, giải phóng thanh khoản cho các hoạt động sinh lời.
4. **Kiểm soát các Sản phẩm Bảo trợ Ngoại bảng**:
   - Phối hợp với Khối Khách hàng Doanh nghiệp và Đầu tư để rà soát các điều khoản quyền chọn bán thanh khoản (*liquidity puts*) trong các cấu trúc tài trợ ABCP, ngăn ngừa rủi ro tài sản ngoại bảng ồ ạt đổ dồn về bảng cân đối kế toán khi thị trường đóng băng.

---

## Nhầm lẫn thường gặp

### 8. Những Nhầm lẫn Thường gặp

- ❌ **Hiểu nhầm về bù trừ tài sản ký quỹ phái sinh giữa các đối tác**: Bù trừ phần tài sản bảo đảm non-L1 nhận được từ đối tác A với phần tài sản non-L1 phải nộp cho đối tác B để giảm khoản phạt 20%.
  - *Thực tế*: LCR40.52 (FAQ3) nghiêm cấm việc bù trừ dòng tài sản ký quỹ giữa các đối tác khác nhau, vì rủi ro định giá và mức độ bất cân xứng thanh khoản giữa các đối tác là hoàn toàn độc lập.
- ❌ **Chủ quan với các khoản ký quỹ chưa bị đòi nộp**: Không tính dòng ra cho các khoản bảo đảm phái sinh đến hạn chỉ vì đối tác chưa gửi yêu cầu *margin call*.
  - *Thực tế*: LCR40.54 yêu cầu tính ngay **100% dòng ra** cho toàn bộ nghĩa vụ ký quỹ theo hợp đồng chưa bị đòi.
- ❌ **Đánh đồng tài trợ thương mại với cho vay xuất nhập khẩu**: Xếp các khoản giải ngân cho vay vốn lưu động tài trợ xuất khẩu vào nhóm Trade Finance để hưởng run-off $\le 5\%$.
  - *Thực tế*: LCR40.72 quy định các khoản cấp tín dụng trực tiếp bắt buộc phải chịu drawdown của hạn mức cam kết 10%–30% theo LCR40.64. Mức $\le 5\%$ chỉ áp dụng duy nhất cho các cam kết bảo lãnh, L/C gắn liền với luân chuyển hàng hóa thực tế.
