---
title: "Behavioural Options in IRRBB (Quyền chọn hành vi trong sổ ngân hàng)"
aliases: [Behavioural Options, Quyền chọn hành vi, Prepayment Risk, Early Redemption Risk, CPR, TDRR]
type: concept
domains: [alm, product, basel]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]"]
relations:
  - {type: part-of, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: drives, to: "[[economic-value-of-equity]]", direction: "-", regime: falling_rate, cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-5]]"}
  - {type: input-to, to: "[[repricing-balance-sheet]]", cite: "[[src-tata-bank-alm#^tata-gap-1]]"}
tags: [irrbb, behavioural-options, prepayment, early-redemption, negative-convexity, basel]
updated: 2026-10-16
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
2. **Kích hoạt tổn thất [[economic-value-of-equity|$\Delta\text{EVE}$]]**: Quyền chọn hành vi cộng hưởng với [Gap Risk](file:///d:/AI/202610%20ALM%20wiki/02_wiki/concepts/gap-risk.md) làm khuếch đại mức sụt giảm giá trị kinh tế, đẩy ngân hàng vào nguy cơ vi phạm phép thử [[outlier-bank-test|Outlier Bank Test (15% Tier 1 Capital)]]. Để phòng ngừa rủi ro này, Treasury mua các hợp đồng [[swaption|Receiver Swaption]] nhằm trung hòa tính lồi âm của danh mục cho vay thế chấp.
3. **Tác động lên [[lcr]] và [[nsfr]]**: Khách hàng rút tiền gửi trước hạn đột ngột biến nguồn nợ kỳ hạn dài (được hưởng ASF 100% trong NSFR) thành dòng tiền rút ngay lập tức trong 30 ngày, đe dọa trực tiếp tỷ lệ an toàn thanh khoản kép.
- Xem chi tiết tại [[non-maturity-deposits]], [[option-risk]], [[gap-risk]], [[swaption]], [[integrated-alm-liquidity-strategy]].
