---
title: "Behavioural Options in IRRBB (Quyền chọn hành vi trong sổ ngân hàng)"
aliases: [Behavioural Options, Quyền chọn hành vi, Prepayment Risk, Early Redemption Risk, CPR, TDRR]
type: concept
domains: [alm, product, basel, vn-reg]
status: active
maturity: draft
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-lubinska-alm-optimisation]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: drives, to: "[[economic-value-of-equity]]", direction: "-", regime: falling_rate, cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-5]]"}
  - {type: input-to, to: "[[repricing-balance-sheet]]", cite: "[[src-tata-bank-alm#^tata-gap-1]]"}
tags: [irrbb, behavioural-options, prepayment, early-redemption, negative-convexity, basel]
updated: 2026-10-20
reviewed:
---

## Định nghĩa & Bản chất
Quyền chọn hành vi (Behavioural Options / Embedded Options) trong Chuẩn mực [[bcbs-irrbb]] và lý thuyết ALM là các điều khoản quyền chọn được nhúng trong các hợp đồng tài chính của khách hàng, trao cho khách hàng quyền tự đưa ra quyết định cá nhân làm thay đổi thời điểm và quy mô của các dòng tiền hoàn trả nợ hoặc rút tiền gửi [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-tata-bank-alm#^tata-opt-1]]. Quyền chọn hành vi có thể tồn tại đối với cả các sản phẩm có kỳ hạn hợp đồng danh nghĩa cụ thể (như cho vay thả nổi, cho vay mua nhà thế chấp, tiền gửi tiết kiệm có kỳ hạn) [[src-tata-bank-alm#^tata-opt-2]].

Khác với quyền chọn tự động (*automatic options*) thực thi theo quy tắc xác định và được người nắm giữ thực hiện một cách duy lý thuần túy theo giá thị trường, quyền chọn hành vi chịu sự chi phối phức tạp của các yếu tố phi tài chính và nhân khẩu học (như chuyển nhà, ly hôn, thay đổi việc làm hoặc tử vong) khiến việc thực hiện quyền có thể không tối ưu theo lý thuyết định giá quyền chọn chuẩn [[src-tata-bank-alm#^tata-opt-4]]. Vì quyền chọn hành vi làm giảm kỳ hạn kỳ vọng thực tế so với kỳ hạn hợp đồng, chúng tạo ra tác động trọng yếu lên cả Giá trị kinh tế của vốn chủ sở hữu ([[economic-value-of-equity|$\Delta\text{EVE}$]]) và Thu nhập lãi thuần ([[net-interest-income-sensitivity|$\Delta\text{NII}$]]) [[src-tata-bank-alm#^tata-opt-3]].

> **Nguyên tắc phân định của Basel**: Quy định về quyền chọn hành vi chỉ áp dụng đối với khách hàng **Bán lẻ**. Bất kỳ quyền chọn nào của khách hàng **Bán buôn (Wholesale)** làm thay đổi cấu trúc dòng tiền đều bắt buộc phải xếp vào nhóm **Quyền chọn tự động** và định giá theo giả định khách hàng sẽ luôn thực hiện quyền theo cách bất lợi nhất cho ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u05-7]].

## 1. Rủi ro Trả nợ Trước hạn (Prepayment Risk)

### Bản chất & Hiện tượng Co cụm Thời lượng (Contraction Risk)
Đối với các khoản cho vay lãi suất cố định (đặc biệt là cho vay mua nhà ở - mortgages), người vay có quyền tất toán khoản nợ trước hạn theo hợp đồng hoặc theo quy định bảo vệ người tiêu dùng [[src-bcbs-irrbb-2016#^irrbb-u06-4]]:
- Khi lãi suất thị trường giảm sâu, người vay có động lực kinh tế mạnh mẽ để đảo nợ hoặc tái tài trợ (refinancing) với lãi suất thấp hơn. Dòng tiền gốc bị trả về dồn dập khiến thời lượng tài sản co ngắn lại đột ngột (*contraction risk*). Ngân hàng buộc phải tái đầu tư dòng tiền này ở mức lợi suất thấp hơn, gây suy giảm lợi nhuận.
- Khi lãi suất thị trường tăng vọt, người vay giữ chặt các khoản vay cố định lãi suất thấp, khiến kỳ hạn thực tế của danh mục bị kéo dài ra (*extension risk*), trong khi chi phí huy động vốn của ngân hàng tăng lên.

### Phân rã Hai Tầng Prepayment theo Beata Lubinska (Structural vs Financial)
Theo Beata Lubinska (2020), tổng tỷ lệ trả nợ trước hạn của danh mục cho vay mua nhà được cấu thành từ hai thành phần độc lập [[src-lubinska-alm-optimisation#^lubinska-u04-8]]:
1. **Structural (Statistical) Prepayments (Trả nợ trước hạn phi duy lý / cấu trúc)**:
   - Phát sinh từ các biến cố xã hội học và hoàn cảnh cá nhân của người vay (ly hôn, thừa kế tài sản, tăng lương, chuyển dịch chỗ ở địa lý) và hoàn toàn không liên quan đến mặt bằng lãi suất thị trường [[src-lubinska-alm-optimisation#^lubinska-u04-9]].
   - Luôn tồn tại một tỷ lệ trả trước tối thiểu mang tính thống kê ngay cả khi lãi suất tăng cao [[src-lubinska-alm-optimisation#^lubinska-u04-8]].
   - Được mô hình hóa dựa trên dữ liệu lịch sử quan sát nhiều năm, phân nhóm theo niên độ giải ngân (vintage cohorts), tiền tệ và loại hợp đồng [[src-lubinska-alm-optimisation#^lubinska-u04-9]].
2. **Financial Prepayments (Trả nợ trước hạn duy lý / tài chính)**:
   - Gắn liền trực tiếp với mức độ chênh lệch giữa lãi suất hợp đồng và lãi suất thị trường (*interest rate spread*), kỳ hạn còn lại (*residual maturity*) và các yếu tố kinh tế vĩ mô (thất nghiệp, GDP, lạm phát giá nhà) [[src-lubinska-alm-optimisation#^lubinska-u04-10]].
   - **Hiện tượng trơ lãi suất (Burnout phenomenon)**: Đo lường độ nhạy cảm và sự phân hóa mức độ sẵn sàng phản ứng giữa các nhóm khách hàng trước các đợt giảm lãi suất; một nhóm khách hàng duy lý sẽ trả nợ ngay khi có lời, trong khi nhóm còn lại có ngưỡng kích hoạt chậm hơn [[src-lubinska-alm-optimisation#^lubinska-u04-10]].
   - *Hạn chế của mô hình tham số*: Các mô hình tham số truyền thống thường có năng lực dự báo ngoài mẫu kém do hàm trả nợ trước hạn mang tính phi tuyến cao; việc ứng dụng các phương pháp phi tham số (non-parametric techniques) giúp nắm bắt tốt hơn tương tác đa biến và tính phi tuyến này [[src-lubinska-alm-optimisation#^lubinska-u04-11]].

### Rủi ro Phòng Hộ Quá Mức (Overhedging Risk)
Lubinska chỉ ra rằng nếu ngân hàng không tính toán chính xác hành vi trả nợ trước hạn trong các chiến lược phái sinh phòng ngừa rủi ro (hedging), ngân hàng sẽ rơi vào trạng thái phòng hộ quá mức (overhedging): số lượng vị thế hoán đổi trả lãi cố định (swap payer) sẽ vượt quá quy mô dư nợ tài sản lãi suất cố định thực tế còn lại [[src-lubinska-alm-optimisation#^lubinska-u04-4]]. Hậu quả là ngân hàng phải tái cân bằng vị thế khẩn cấp, để lộ khe hở nhạy cảm dải kỳ hạn (*time bucket sensitivity*) và chịu tổn hại trực tiếp lên độ nhạy PV01 [[src-lubinska-alm-optimisation#^lubinska-u04-4]].

### Mô hình hoá Chuẩn hoá: Tỷ lệ Trả nợ Trước hạn có Điều kiện (CPR)
Theo Basel d368 Section IV, đối với các khoản trả nợ trước hạn không bị phạt kinh tế bù đắp đầy đủ tổn thất (uncompensated prepayments), ngân hàng xác định tỷ lệ trả trước cơ sở $CPR_{0,c}^p$ và điều chỉnh theo hệ số nhân kịch bản $\gamma_i$ [[src-bcbs-irrbb-2016#^irrbb-u05-5]]:

$$
CPR_{i,c}^p = \min\left(1,\; \gamma_i \cdot CPR_{0,c}^p\right)
$$

Dòng tiền điều chỉnh tại dải kỳ hạn $k$ được tính toán:

$$
CF_{i,c}^p(k) = CF_{i,c}^s(k) + CPR_{i,c}^p \cdot N_{i,c}^p(k-1)
$$

Trong đó:
- $CF_{i,c}^s(k)$: Dòng tiền gốc và lãi theo lịch trả nợ ban đầu.
- $N_{i,c}^p(k-1)$: Số dư nợ danh nghĩa còn lại tại dải kỳ hạn trước đó.

### Bảng Hệ số nhân Kịch bản Trả nợ Trước hạn (Table 3)

| Kịch bản sốc lãi suất ($i$) | Mô tả hướng đường cong | Hệ số nhân kịch bản $\gamma_i$ | Diễn giải hành vi khách hàng |
|---|---|---|---|
| **1. Parallel up** | Dịch chuyển song song tăng | **0.8** | Lãi suất tăng $\rightarrow$ Khách hàng giữ nợ cố định $\rightarrow$ Tốc độ trả nợ giảm 20% |
| **2. Parallel down** | Dịch chuyển song song giảm | **1.2** | Lãi suất giảm $\rightarrow$ Khách hàng ồ ạt đảo nợ $\rightarrow$ Tốc độ trả nợ tăng 20% |
| **3. Steepener** | Lãi suất dài hạn tăng, ngắn hạn giảm | **0.8** | Kỳ hạn vay dài chịu lãi suất tăng $\rightarrow$ Tốc độ trả trước giảm 20% |
| **4. Flattener** | Lãi suất ngắn hạn tăng, dài hạn giảm | **1.2** | Lãi suất dài hạn giảm $\rightarrow$ Khách hàng tái cấp vốn $\rightarrow$ Tốc độ trả trước tăng 20% |
| **5. Short rate up** | Lãi suất ngắn hạn tăng | **0.8** | Lãi suất tăng $\rightarrow$ Tốc độ trả nợ trước hạn giảm 20% |
| **6. Short rate down** | Lãi suất ngắn hạn giảm | **1.2** | Lãi suất giảm $\rightarrow$ Tốc độ trả nợ trước hạn tăng 20% |

## 2. Rủi ro Rút Tiền gửi có Kỳ hạn Sớm (Early Redemption Risk)

### Bản chất & Điều kiện Miễn trừ
Tiền gửi có kỳ hạn (term deposits) ấn định một mức lãi suất cố định cho một kỳ hạn xác định và thường được ngân hàng phòng ngừa rủi ro trên cơ sở đó [[src-bcbs-irrbb-2016#^irrbb-u05-6]]. Tuy nhiên, khách hàng có quyền rút tiền trước ngày đáo hạn.

Theo quy định Basel, tiền gửi có kỳ hạn **chỉ được coi là nợ cố định đến hạn hợp đồng** nếu ngân hàng chứng minh được một trong hai điều kiện khắt khe sau [[src-bcbs-irrbb-2016#^irrbb-u05-6]]:
1. Người gửi tiền không có bất kỳ quyền pháp lý nào để rút tiền trước hạn; HOẶC
2. Việc rút trước hạn sẽ phải chịu mức phạt kinh tế đáng kể (significant penalty), bù đắp đầy đủ cho ngân hàng khoản chênh lệch lãi suất và chi phí kinh tế phá vỡ hợp đồng.

Nếu không đáp ứng 2 điều kiện trên, tiền gửi bắt buộc phải xử lý như công cụ chịu rủi ro rút trước hạn.

### Mô hình hoá Chuẩn hoá: Tỷ lệ Rút tiền gửi sớm (TDRR)
Ngân hàng xác định tỷ lệ rút sớm cơ sở $TDRR_{0,c}^p$ và nhân với hệ số co giãn kịch bản $u_i$ [[src-bcbs-irrbb-2016#^irrbb-u05-6]]:

$$
TDRR_{i,c}^p = \min\left(1,\; u_i \cdot TDRR_{0,c}^p\right)
$$

Toàn bộ phần số dư dự kiến bị rút trước hạn được **bắt buộc phân bổ vào dải kỳ hạn qua đêm (overnight / k = 1)** [[src-bcbs-irrbb-2016#^irrbb-u05-6]]:

$$
CF_{i,c}^p(1) = TD_{0,c}^p \cdot TDRR_{i,c}^p
$$

### Bảng Hệ số Co giãn Rút Tiền gửi Sớm (Table 4)

| Kịch bản sốc lãi suất ($i$) | Hướng đường cong | Hệ số co giãn kịch bản $u_i$ | Diễn giải hành vi người gửi tiền |
|---|---|---|---|
| **1. Parallel up** | Dịch chuyển song song tăng | **1.2** | Lãi suất tăng vọt $\rightarrow$ Khách hàng rút tiền sớm tìm lãi cao $\rightarrow$ Tỷ lệ rút tăng 20% |
| **2. Parallel down** | Dịch chuyển song song giảm | **0.8** | Lãi suất giảm $\rightarrow$ Khách hàng giữ nguyên tiền gửi lãi suất cao $\rightarrow$ Rút sớm giảm 20% |
| **3. Steepener** | Ngắn hạn giảm, dài hạn tăng | **0.8** | Lãi suất ngắn hạn giảm $\rightarrow$ Không có động lực rút sớm |
| **4. Flattener** | Ngắn hạn tăng, dài hạn giảm | **1.2** | Lãi suất ngắn hạn tăng cao $\rightarrow$ Khách hàng rút sớm gửi ngắn hạn $\rightarrow$ Tăng 20% |
| **5. Short rate up** | Lãi suất ngắn hạn tăng | **1.2** | Chi phí cơ hội tăng $\rightarrow$ Rút sớm tăng 20% |
| **6. Short rate down** | Lãi suất ngắn hạn giảm | **0.8** | Duy trì tiền gửi lãi suất cũ $\rightarrow$ Rút sớm giảm 20% |

## Tính chất Lồi Âm (Negative Convexity) và Tác động Vốn ALM

```
Giá trị Hiện tại (PV)
      ▲
      │          / Đường cong lồi dương chuẩn (Trái phiếu thường không quyền chọn)
      │         /
      │        /
      │       /───\  <- Vùng Lồi Âm (Negative Convexity): Khi lãi suất giảm,
      │      /     \    giá trị không tăng tương xứng do khách hàng trả nợ trước hạn!
      │     /       \
      │    /         \
      └─────────────────────► Lãi suất (r)
```

1. **Phá vỡ mối quan hệ định giá tuyến tính**: Các công cụ có quyền chọn hành vi tạo ra tính chất **lồi âm (*negative convexity*)**. Khi lãi suất thị trường giảm, giá trị tài sản không tăng mạnh như trái phiếu thông thường (do bị chặn trên bởi quyền trả nợ trước hạn); ngược lại khi lãi suất tăng, giá trị tài sản sụt giảm nhanh hơn bình thường.
2. **Kích hoạt tổn thất [[economic-value-of-equity|$\Delta\text{EVE}$]]**: Quyền chọn hành vi cộng hưởng với [[gap-risk|Gap Risk]] làm khuếch đại mức sụt giảm giá trị kinh tế, đẩy ngân hàng vào nguy cơ vi phạm phép thử [[outlier-bank-test|Outlier Bank Test (15% Tier 1 Capital)]]. Để phòng ngừa rủi ro này, Treasury mua các hợp đồng [[swaption|Receiver Swaption]] nhằm trung hòa tính lồi âm của danh mục cho vay thế chấp.
3. **Tác động lên [[lcr]] và [[nsfr]]**: Khách hàng rút tiền gửi trước hạn đột ngột biến nguồn nợ kỳ hạn dài (được hưởng ASF 100% trong NSFR) thành dòng tiền rút ngay lập tức trong 30 ngày, đe dọa trực tiếp tỷ lệ an toàn thanh khoản kép.
- Xem chi tiết tại [[non-maturity-deposits]], [[option-risk]], [[gap-risk]], [[swaption]], [[integrated-alm-liquidity-strategy]], [[irrbb-repricing-profiles-and-behavioral-modeling]].

### Mô hình hoá hành vi trong thực tế (Tata, T4)
- **Yêu cầu EBA (qua Tata)**: xét tác động lên tốc độ trả trước hiện tại và tương lai từ kịch bản lãi suất, môi trường kinh tế, đặc điểm hợp đồng và độ co giãn lãi suất của sản phẩm [[src-tata-bank-alm#^tata-beh-1]]. Bốn nhóm cần mô hình hành vi: NMD, thấu chi, khoản vay có quyền trả trước, tiền gửi có kỳ hạn rút sớm; dữ liệu thời kỳ lãi suất âm không dùng để backtest thời kỳ lãi suất dương và ngược lại [[src-tata-bank-alm#^tata-beh-2]]. Xem [[negative-interest-rates]].
- **Phân khúc khách hàng**: mô hình hành vi phân khúc theo đặc điểm (số dư ban đầu, lãi khuyến mãi, quan hệ, tuổi, kênh mở), hiệu chỉnh riêng từng nhóm và backtest liên tục [[src-tata-bank-alm#^tata-fut-5]]. Báo cáo EU yêu cầu tỷ lệ trả trước và rút trước hạn có điều kiện [[src-tata-bank-alm#^tata-rep-3]]. DeFi thiếu dữ liệu lịch sử để hiệu chỉnh hành vi [[src-tata-bank-alm#^tata-fut-2]].
- **Khi lãi suất tăng nhanh**: khoản vay cố định lãi thấp được giữ lâu hơn (trả trước chậm), khoản vay thả nổi trả trước nhanh hơn [[src-tata-bank-alm#^tata-rr-3]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Định nghĩa | Behavioural option là một dạng của option risk, cùng với automatic option [[src-bcbs-irrbb-2016#^irrbb-u02-2]] | Rủi ro quyền lựa chọn hành vi phát sinh khi lãi suất thay đổi có thể làm thay đổi hành vi khách hàng [[src-tt83-2025-nhnn#^d3-22]] | d368 par 13; TT83 Đ3.22 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Đơn vị tính tham số cơ sở | [cần nguồn] | $CPR_0$ và $TDRR_0$ xác định cho từng danh mục p gồm các khoản cùng đồng tiền, cùng đặc điểm, trong điều kiện hiện hành; $CF^S$ là khoản trả gốc, lãi định kỳ [[src-tt83-2025-nhnn#^pl5-a2-3b2]]; $TD_0$ là số dư tiền gửi còn lại của danh mục [[src-tt83-2025-nhnn#^pl5-a2-3c2]] | TT83 PL5.A.II.3.b, c | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Tiêu chí xác định | [cần nguồn] | Ngân hàng phải có quy định nội bộ về tiêu chí xác định khoản vay có rủi ro trả trước hạn [[src-tt83-2025-nhnn#^pl5-a2-3b]] và tiền gửi có rủi ro rút trước hạn [[src-tt83-2025-nhnn#^pl5-a2-3c]] | TT83 PL5.A.II.3.b–c | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| $\gamma_i$ (prepayment) | 0,8 khi lãi suất tăng, 1,2 khi giảm [[src-bcbs-irrbb-2016#^irrbb-u05-5]] | Bảng 3, cùng giá trị [[src-tt83-2025-nhnn#^pl5-a2-3b]] | d368 par 123; TT83 Bảng 3 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| $u_i$ (TDRR) | 1,2 khi lãi suất tăng, 0,8 khi giảm [[src-bcbs-irrbb-2016#^irrbb-u05-6]] | Bảng 4, cùng giá trị [[src-tt83-2025-nhnn#^pl5-a2-3c]] | d368 par 128; TT83 Bảng 4 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Khách hàng tổ chức | [cần nguồn] | Ngân hàng tự xác định dòng tiền khoản vay [[src-tt83-2025-nhnn#^pl5-a2-3b]] và tiền gửi [[src-tt83-2025-nhnn#^pl5-a2-3c]] của tổ chức | TT83 PL5.A.II.3.b(iii), c(iii) | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |

Khác biệt: công thức CPR, TDRR của [[tt83-2025]] chỉ áp cho khách hàng cá nhân.

- **Quản trị mô hình (VN)**: mô hình $CPR_0$, $TDRR_0$ chịu yêu cầu vòng đời mô hình và kiểm soát override [[src-tt83-2025-nhnn#^d56-4]], kiểm định tối thiểu hằng năm [[src-tt83-2025-nhnn#^d56-4d]]. Xem [[model-validation]].

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
