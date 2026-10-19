---
title: "Cơ Chế Truyền Dẫn Của Các Cấu Phần Rủi Ro Lãi Suất (IRRBB) Đến NII Và EVE"
aliases: [IRRBB Transmission Mechanisms to NII and EVE, Cơ chế tác động của IRRBB đến NII và EVE, NII and EVE Transmission, Truyền dẫn rủi ro lãi suất sổ ngân hàng, IRRBB Impact on Earnings and Economic Value]
type: synthesis
domains: [alm, basel]
status: active
maturity: draft
origin: research
question: "Cơ chế tác động của từng loại rủi ro cấu phần trong IRRBB (Gap risk, Basis risk, Option risk và CSRBB) đến Thu nhập lãi thuần (NII) và Giá trị kinh tế của vốn chủ sở hữu (EVE) diễn ra như thế nào theo khuôn khổ chuẩn mực Basel d368, Moorad Choudhry và Fidelio Tata?"
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tata-bank-alm]]"]
relations: []
tags: [irrbb, nii, eve, gap-risk, basis-risk, option-risk, csrbb, transmission-mechanism, synthesis]
updated: 2026-10-17
reviewed:
---

## 1. Bản Chất Lưỡng Diện Của Đo Lường IRRBB: Góc Nhìn EVE Và NII

Khuôn khổ chuẩn mực của Ủy ban Basel về Giám sát Ngân hàng ([[bcbs-irrbb|BCBS d368]]), các nguyên lý của Giáo sư Moorad Choudhry và mô hình lượng hóa của Fidelio Tata đều khẳng định: Rủi ro lãi suất trong sổ ngân hàng ([[bcbs-irrbb|IRRBB]]) bắt buộc phải được lượng hóa đồng thời dưới hai lăng kính bổ trợ lẫn nhau: **Góc nhìn Giá trị kinh tế ([[economic-value-of-equity|EVE]])** và **Góc nhìn Thu nhập ([[net-interest-income-sensitivity|NII]])** [[src-bcbs-irrbb-2016#^irrbb-u01-4]] [[src-choudhry-principles-banking#^choudhry-irrbb-3]] [[src-tata-bank-alm#^tata-nii-11]].

```
+---------------------------------------------------------------------------------------------------+
|                        BẢN CHẤT LƯỠNG DIỆN CỦA ĐO LƯỜNG RỦI RO LÃI SUẤT (IRRBB)                    |
+---------------------------------------------------------------------------------------------------+
|                                                 |                                                 |
|          GÓC NHÌN GIÁ TRỊ KINH TẾ (EVE)          |             GÓC NHÌN THU NHẬP (NII)             |
|                                                 |                                                 |
|  - Bản chất: Chiết khấu toàn bộ dòng tiền       |  - Bản chất: Dòng thu nhập dồn tích kế toán     |
|    còn lại của bảng cân đối về hiện giá         |    trong một chân trời ngắn hạn (12-36 tháng)    |
|  - Trọng tâm: Bảo vệ giá trị vốn tự có (Solvency)|  - Trọng tâm: Bảo vệ lợi nhuận & cổ tức        |
|  - Giả định: Bảng cân đối co cụm (Run-off),      |  - Giả định: Bảng cân đối tĩnh/động             |
|    không có tài sản và công nợ mới thay thế     |    (Constant / Dynamic balance sheet)           |
|  - Phạm vi: Toàn bộ vòng đời còn lại            |  - Phạm vi: 1 năm đến 3 năm gần nhất            |
|  - Rủi ro tính đến: Reset Date tiếp theo        |  - Nhìn về tương lai: Prospective View          |
|    (sau reset, công cụ về giá ngang mệnh giá)   |    (sai số mô hình tự triệt tiêu khi tính ΔNII) |
+---------------------------------------------------------------------------------------------------+
```

### 1.1. Phương trình cốt lõi của Giá trị kinh tế (EVE)
Giá trị kinh tế của vốn chủ sở hữu được định nghĩa là hiện giá của toàn bộ tài sản trừ đi hiện giá của toàn bộ nợ phải trả, cộng/trừ vị thế ngoại bảng [[src-tata-bank-alm#^tata-ev-1]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]]:

$$\text{EVE} = \text{PV}(A) - \text{PV}(L) + \text{PV}(\text{OBS})$$

Khi lãi suất thị trường thay đổi một lượng $\Delta y$, biến động của EVE xấp xỉ qua mô hình khe hở thời lượng hiệu chỉnh ([[duration-gap-model|Duration Gap]]) [[src-tata-bank-alm#^tata-dgap-1]]:

$$\Delta\text{EVE} \approx - \left[ D^*_A \cdot \text{PV}(A) - D^*_L \cdot \text{PV}(L) \right] \cdot \Delta y + \frac{1}{2} \left[ C_A \cdot \text{PV}(A) - C_L \cdot \text{PV}(L) \right] (\Delta y)^2$$

Trong đó:
- $D^*_A, D^*_L$ là thời lượng hiệu chỉnh (modified duration) của tài sản và nợ phải trả.
- $C_A, C_L$ là độ lồi (convexity) của tài sản và nợ.
- **Quy tắc Reset Date của Fidelio Tata**: Rủi ro lãi suất chỉ được tính đến ngày thiết lập lại lãi suất tiếp theo (*next reset date*), chứ không tính đến ngày đáo hạn hợp đồng (*contractual maturity date*). Khi một công cụ thả nổi được định giá lại theo lãi suất thị trường, nó sẽ giao dịch lại theo đúng mệnh giá (*par*), triệt tiêu phơi nhiễm rủi ro định giá của kỳ hạn gốc [[src-tata-bank-alm#^tata-gap-2]].

### 1.2. Phương trình cốt lõi của Thu nhập lãi thuần (NII)
Thu nhập lãi thuần là chênh lệch giữa thu nhập lãi từ tài sản và chi phí lãi của nợ phải trả phát sinh trong một giai đoạn xác định [[src-tata-bank-alm#^tata-nii-1]]:

$$\text{NII}_H = \int_0^H \left[ r_A(t) \cdot A(t) - r_L(t) \cdot L(t) \right] dt$$

Độ nhạy thu nhập lãi thuần ($\Delta\text{NII}$) trong chân trời 12 tháng theo mô hình khe hở định giá lại kỳ hạn chuẩn [[gap-risk|Repricing Gap]] [[src-choudhry-principles-banking#^choudhry-irrbb-3]]:

$$\Delta\text{NII}_{12M} = \sum_{k=1}^m \text{GAP}_k \cdot \Delta r_k \cdot \left( \frac{12 - t_k}{12} \right)$$

Trong đó $\text{GAP}_k = \text{RSA}_k - \text{RSL}_k$ là khe hở định giá lại trong dải kỳ hạn thứ $k$, và $t_k$ là điểm giữa của dải kỳ hạn (tháng).
- **Nguyên lý triệt tiêu sai số mô hình (Error Cancellation)**: Khi lượng hóa $\Delta\text{NII}$, sai số trong dự báo NII cơ sở (*baseline forecast*) ít ảnh hưởng đến độ tin cậy của phân tích vì các giả định sai được áp dụng lặp lại đồng nhất trong cả kịch bản cơ sở và kịch bản sốc, do đó phần lớn sai số sẽ bị triệt tiêu khi lấy hiệu số [[src-tata-bank-alm#^tata-nii-3]].
- **Loại trừ các khoản mục không nhạy cảm**: Toàn bộ tài sản cố định, bất động sản, cổ phần đầu tư dài hạn và vốn chủ sở hữu kế toán được loại khỏi phân tích độ nhạy NII [[src-tata-bank-alm#^tata-nii-5]].

---

## 2. Cơ Chế Truyền Dẫn Chi Tiết Của Từng Loại Rủi Ro Cấu Phần

Chuẩn mực Basel d368 xác định rõ các cấu phần rủi ro trong IRRBB: **Rủi ro khe hở (Gap risk)**, **Rủi ro cơ sở (Basis risk)**, **Rủi ro quyền chọn (Option risk)** và **Rủi ro chênh lệch tín dụng sổ ngân hàng (CSRBB)** [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-bcbs-irrbb-2016#^irrbb-u02-3]] [[src-choudhry-principles-banking#^choudhry-irrbb-4]]. Mỗi cấu phần có cơ chế truyền dẫn vi mô và vĩ mô hoàn toàn khác biệt đến NII và EVE.

```
+---------------------------------------------------------------------------------------------------+
|                     MA TRẬN CƠ CHẾ TRUYỀN DẪN IRRBB ĐẾN NII VÀ EVE (D368 & ALM)                    |
+-------------------+---------------------------------------+---------------------------------------+
| LOẠI RỦI RO       | KÊNH TRUYỀN DẪN ĐẾN NII (NGẮN HẠN)    | KÊNH TRUYỀN DẪN ĐẾN EVE (DÀI HẠN)     |
+-------------------+---------------------------------------+---------------------------------------+
| 1. GAP RISK       | Khe hở định giá lại định kỳ (Periodic | Lệch pha thời lượng hiệu chỉnh        |
|    - Parallel     | Repricing Gap): Lãi suất biến động tác | (Duration Gap): Chiết khấu dòng tiền  |
|    - Non-parallel | động trực tiếp lên dòng tiền lãi thu  | tương lai; xoay đường cong làm biến   |
|      (Curve risk) | và chi phí lãi phải trả trong 12-36M. | dạng giá trị hiện tại theo dải kỳ hạn.|
+-------------------+---------------------------------------+---------------------------------------+
| 2. BASIS RISK     | Lệch pha giữa các chỉ số tham chiếu   | Thay đổi đường cong định giá cơ sở    |
|    - Tenor basis  | (SOFR vs Euribor, 1M vs 3M) và độ     | (basis discount curves) làm thay đổi  |
|    - Benchmark    | nhạy biên độ truyền dẫn (Pass-through | chênh lệch hiện giá giữa các dòng tiền|
|      basis        | beta) của lãi suất huy động/cho vay.  | tài sản và nợ qua toàn bộ vòng đời.   |
+-------------------+---------------------------------------+---------------------------------------+
| 3. OPTION RISK    |                                       |                                       |
|    - Automatic    | Điểm chạm Caps/Floors triệt tiêu hoặc | Độ lồi phi tuyến (Negative Convexity):|
|      (Embedded)   | bóp nghẹt NIM khi vượt ngưỡng kích    | Giá trị quyền chọn ngầm triệt tiêu    |
|                   | hoạt (strikes).                       | tiềm năng tăng giá trị của tài sản.   |
|    - Behavioral   | Khách hàng trả nợ trước hạn (CPR)     | Rút ngắn/kéo dài thời lượng hiệu lực  |
|      (Customer)   | làm giảm dư nợ lãi suất cao; rút tiền | thực tế; phá vỡ mô hình phân bổ kỳ hạn|
|                   | gửi kỳ hạn (TDRR) đẩy chi phí vốn tăng.| chuẩn mực (Table 2 Basel d368).       |
+-------------------+---------------------------------------+---------------------------------------+
| 4. CSRBB          | Tác động gián tiếp: Tăng chi phí huy  | Tác động trực tiếp & tức thì: Trừ trực|
|    (Credit Spread | động vốn mới dài hạn khi biên chênh   | tiếp khoản lỗ AOCI vào vốn CET1 qua   |
|     Banking Book) | lệch tín dụng thị trường mở rộng.     | danh mục FVOCI; đo lường bằng CS01.   |
+-------------------+---------------------------------------+---------------------------------------+
```

---

### 2.1. Rủi Ro Khe Hở Tái Định Giá (Gap Risk & Yield Curve Risk)

Gap risk phát sinh từ sự chênh lệch về thời điểm đáo hạn (đối với công cụ cố định) và thời điểm tái định giá (đối với công cụ thả nổi) giữa tài sản nợ và tài sản có [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-choudhry-principles-banking#^choudhry-irrbb-4]].

#### Kênh truyền dẫn đến NII:
- Khi ngân hàng ở trạng thái **Nhạy cảm tài sản (Asset-sensitive, $\text{GAP} > 0$)**: Khối lượng tài sản định giá lại lớn hơn nợ phải trả. Lãi suất thị trường tăng sẽ giúp tài sản tái định giá lên mức lãi suất mới nhanh hơn nợ, làm tăng thu nhập lãi và mở rộng NIM [[src-choudhry-principles-banking#^choudhry-irrbb-5]] [[src-tata-bank-alm#^tata-nii-6]]. Ngược lại, khi lãi suất giảm, NII sẽ sụt giảm nhanh chóng.
- Khi ngân hàng ở trạng thái **Nhạy cảm nợ (Liability-sensitive, $\text{GAP} < 0$)**: Lãi suất thị trường tăng sẽ đẩy chi phí trả lãi của các khoản tiền gửi ngắn hạn tăng ngay lập tức, trong khi danh mục cho vay kỳ hạn dài chưa tái định giá, bóp nghẹt NIM và bào mòn NII [[src-choudhry-principles-banking#^choudhry-irrbb-5]].
- **Hiệu ứng trễ thời gian (Timing Asymmetry)** trong mô phỏng NII 36 tháng của Fidelio Tata, kịch bản lãi suất giảm 100 bp:
  - Tiền gửi kỳ hạn tái định giá sau 3 tháng nên hưởng lợi rất nhanh từ lãi suất giảm, tiết kiệm đáng kể chi phí lãi [[src-tata-bank-alm#^tata-nii-6]]. Cho vay thế chấp chưa tái định giá trong một năm nữa, nên thu nhập lãi giảm muộn hơn [[src-tata-bank-alm#^tata-nii-7]].
  - Ngân hàng mô hình chịu rủi ro NII giảm đáng kể trong giai đoạn từ năm thứ nhất đến năm thứ hai [[src-tata-bank-alm#^tata-nii-14]]. NII theo giai đoạn: baseline 3.750 / 3.639 / 7.002 / 14.124 / 13.956, tổng 3 năm 42.471; kịch bản sốc 3.750 / 4.014 / 7.248 / 13.116 / 13.956, tổng 3 năm 42.084 [[src-tata-bank-alm#^tata-nii-13]].
  - *Diễn giải:* cộng theo năm từ hai bảng trên, NII kịch bản sốc so với baseline cao hơn khoảng 0.62 ở năm 1 (15.012 so với 14.391), thấp hơn khoảng 1.01 ở năm 2 (13.116 so với 14.124) và bằng nhau ở năm 3.

#### Kênh truyền dẫn đến EVE:
- Dòng tiền tương lai được chiết khấu theo toàn bộ đường cong lãi suất phi rủi ro giao ngay [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- Khi đường cong dịch chuyển song song hướng lên (+200 bps): Nếu ngân hàng có thời lượng tài sản lớn hơn thời lượng nợ ($D^*_A > D^*_L \cdot \frac{L}{A}$), hiện giá tài sản giảm mạnh hơn hiện giá nợ, gây tổn thất vốn kinh tế nghiêm trọng [[src-tata-bank-alm#^tata-dgap-2]].
- Khi đường cong biến dạng phi song song (**Yield Curve Risk** — Flattener / Steepener / Twist) [[src-choudhry-principles-banking#^choudhry-irrbb-4]]:
  - Kịch bản **Dốc hóa (Steepener)**: Lãi suất ngắn hạn giảm, dài hạn tăng. EVE chịu tổn thất nặng nề ở các tài sản kỳ hạn dài (như trái phiếu chính phủ 10–20 năm), trong khi nợ ngắn hạn hầu như không giảm giá trị hiện tại.
  - Kịch bản **Phẳng hóa (Flattener)**: Lãi suất ngắn hạn tăng mạnh, dài hạn giữ nguyên hoặc giảm. Nợ ngắn hạn bị sụt giảm giá trị hiện tại nhẹ, nhưng chi phí dòng tiền chiết khấu ngắn hạn bị bóp méo.

---

### 2.2. Rủi Ro Cơ Sở (Basis Risk)

Basis risk phát sinh khi các công cụ tài sản và công nợ có cùng kỳ hạn tái định giá nhưng được tham chiếu theo các chỉ số lãi suất cơ sở khác nhau, hoặc cùng một chỉ số nhưng có độ nhạy điều chỉnh biên độ khác nhau [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-choudhry-principles-banking#^choudhry-irrbb-4]].

#### Kênh truyền dẫn đến NII:
- **Tenor Basis**: Lệch pha giữa các kỳ hạn của cùng một chỉ số cơ sở (ví dụ: Tài sản nhận lãi suất Euribor 3 tháng, trong khi nợ trả lãi suất Euribor 1 tháng hoặc Euribor 6 tháng). Khi chênh lệch giữa Euribor 3M và 1M co hẹp bất thường trên thị trường liên ngân hàng, thu nhập lãi thu được không đủ bù đắp chi phí vốn, làm NII sụt giảm dù kỳ hạn danh nghĩa bằng nhau [[src-choudhry-principles-banking#^choudhry-irrbb-4]].
- **Benchmark / Index Basis**: Tài sản tham chiếu theo lãi suất thị trường (như SOFR, Euribor hoặc Lãi suất liên ngân hàng), trong khi nợ phải trả là tiền gửi khách hàng tham chiếu theo Lãi suất cơ sở điều hành của ngân hàng (Administered Rate) hoặc lãi suất điều hành của Ngân hàng Trung ương.
- **Hệ số truyền dẫn bất đối xứng (Pass-through Beta $\beta$)**:
  $$\Delta r_L = \beta_L \cdot \Delta r_{\text{market}}, \quad \Delta r_A = \beta_A \cdot \Delta r_{\text{market}}$$
  - Khi lãi suất thị trường tăng nhanh, nếu áp lực cạnh tranh buộc ngân hàng phải tăng lãi suất tiền gửi với $\beta_L \to 1,0$ trong khi lãi suất cho vay thương mại bị ràng buộc bởi hợp đồng nên chỉ tăng với $\beta_A = 0,6$, biên độ chênh lệch bị thu hẹp $\Delta(\text{Spread}) = (\beta_A - \beta_L)\Delta r < 0$, trực tiếp làm suy giảm NII.

#### Kênh truyền dẫn đến EVE:
- Trong mô hình chiết khấu EVE, các tài sản và công nợ thả nổi dựa trên các chỉ số cơ sở khác nhau bắt buộc phải được dự phóng dòng tiền tương lai theo các đường cong kỳ hạn riêng biệt (*dual-curve / multi-curve framework*) và chiết khấu về hiện giá bằng đường cong OIS/phi rủi ro chuẩn.
- Sự giãn rộng chênh lệch cơ sở (*basis spread widening*) giữa hai đường cong làm biến dạng hiện giá tương đối giữa tài sản và công nợ qua toàn bộ vòng đời hợp đồng, tác động trực tiếp đến EVE.

---

### 2.3. Rủi Ro Quyền Chọn (Option Risk: Automatic & Behavioral)

Option risk phát sinh từ các quyền chọn rõ ràng (*explicit options*) hoặc quyền chọn ngầm định (*embedded options*) được tích hợp trong các hợp đồng tài chính của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u02-2]] [[src-choudhry-principles-banking#^choudhry-irrbb-4]].

```
                                +-----------------------------+
                                |      RỦI RO QUYỀN CHỌN      |
                                +-----------------------------+
                                               |
                   +---------------------------+---------------------------+
                   |                                                       |
        [QUYỀN CHỌN TỰ ĐỘNG]                                    [QUYỀN CHỌN HÀNH VI]
        (Automatic Options)                                     (Behavioral Options)
        - Trần / Sàn lãi suất (Caps/Floors)                    - Trả nợ trước hạn (Prepayment / CPR)
        - Swaptions, Bond Calls                                 - Rút tiền gửi kỳ hạn trước hạn (TDRR)
        - Kích hoạt theo thuật toán giá                         - Hành vi tiền gửi không kỳ hạn (NMDs)
        - Tạo ra độ lồi phi tuyến                              - Rút vốn cam kết hạn mức (Pipeline Risk)
```

#### A. Quyền chọn tự động (Automatic Options)
- **Cơ chế truyền dẫn đến NII**:
  - **Sàn lãi suất tiền gửi (Deposit Floor)**: Khi lãi suất thị trường giảm sâu xuống mức cận 0%, ngân hàng không thể hạ lãi suất tiền gửi xuống dưới sàn, trong khi lợi suất tài sản tiếp tục lao dốc theo thị trường, khiến NIM bị bóp nghẹt [[src-choudhry-principles-banking#^choudhry-irrbb-7]].
  - **Trần lãi suất cho vay (Loan Cap)**: Khi lãi suất tăng vượt mức strike của cap, ngân hàng bị chặn mức trần thu nhập lãi, trong khi chi phí huy động vốn vẫn tiếp tục leo thang, làm NII sụt giảm mạnh so với kịch bản tuyến tính [[src-choudhry-principles-banking#^choudhry-irrbb-7]].
- **Cơ chế truyền dẫn đến EVE**:
  - Gây ra hiện tượng **Độ lồi âm (Negative Convexity)**. Giá trị của quyền chọn ngầm biến thiên phi tuyến tính theo công thức Black-76 hoặc Bachelier. Ngân hàng bán quyền chọn ngầm (short option) cho khách hàng sẽ phải chịu mức sụt giảm EVE theo gia tốc bậc hai $\frac{1}{2} C \cdot (\Delta y)^2$ khi lãi suất biến động mạnh.

#### B. Quyền chọn hành vi (Behavioral Options)
1. **Quyền trả nợ trước hạn (Prepayment Risk / CPR)**:
   - *Tác động đến NII*: Khi lãi suất giảm sâu, người vay thế chấp thực hiện quyền tái tài trợ khoản vay với lãi suất thấp hơn. Ngân hàng nhận lại dòng tiền hoàn vốn gốc sớm và buộc phải tái đầu tư vào tài sản mới với lợi suất thấp, làm thu nhập lãi suy giảm dài hạn [[src-bcbs-irrbb-2016#^irrbb-p05-3]].
   - *Tác động đến EVE*: Khi lãi suất giảm, giá trị hiện tại của khoản cho vay thông thường sẽ tăng lên; tuy nhiên, do khách hàng trả nợ trước hạn, thời lượng tài sản bị rút ngắn đột ngột, hạn chế tiềm năng tăng giá trị của tài sản (hiện tượng *price compression / negative convexity*).
2. **Quyền rút tiền gửi kỳ hạn trước hạn (Early Withdrawal / TDRR)**:
   - *Tác động đến NII & EVE*: Khi lãi suất thị trường tăng cao, người gửi tiền chấp nhận mất một phần tiền lãi phạt để rút tiền trước hạn và chuyển sang gửi tiết kiệm với lãi suất mới cao hơn [[src-bcbs-irrbb-2016#^irrbb-p05-3]]. Ngân hàng mất đi nguồn vốn rẻ dài hạn và phải tái tài trợ với chi phí lãi cao hơn, vừa làm giảm NII tức thì vừa làm tăng giá trị hiện tại của nghĩa vụ nợ, làm giảm EVE.
3. **Tiền gửi không kỳ hạn (Non-Maturity Deposits — NMDs)**:
   - Khách hàng có quyền rút tiền bất kỳ lúc nào mà không cần báo trước. Khi lãi suất thị trường tăng, ngân hàng đối mặt với hiện tượng khách hàng rút tiền chuyển sang các kênh đầu tư khác (*deposit beta expansion / run-off acceleration*). Ngân hàng phải phân tích cơ sở khách hàng để xác định tỷ lệ tiền gửi lõi (*core deposits*) ổn định [[src-bcbs-irrbb-2016#^irrbb-p05-2]].
4. **Rủi ro cam kết tín dụng chưa giải ngân (Pipeline Risk)**:
   - Ngân hàng phát hành cam kết cho vay với lãi suất cố định. Khi lãi suất thị trường tăng vọt, khách hàng ồ ạt giải ngân để chốt mức lãi suất rẻ, buộc ngân hàng phải tài trợ các tài sản lợi suất thấp bằng nguồn vốn mới giá đắt, gây tổn thất kép cho cả NII và EVE [[src-choudhry-principles-banking#^choudhry-irrbb-6]].

---

### 2.4. Rủi Ro Chênh Lệch Tín Dụng Sổ Ngân Hàng (CSRBB)

Chuẩn mực Basel d368 tách biệt rạch ròi CSRBB khỏi IRRBB thuần túy: CSRBB là rủi ro phát sinh từ sự thay đổi của chênh lệch tín dụng (*credit spread*) đối với các công cụ nhạy cảm lãi suất trong sổ ngân hàng, độc lập với rủi ro vỡ nợ (*credit risk jump-to-default*) và rủi ro lãi suất phi rủi ro [[src-bcbs-irrbb-2016#^irrbb-u02-3]].

#### Kênh truyền dẫn trực tiếp đến EVE và Vốn CET1:
- Danh mục chứng khoán đầu tư sẵn sàng để bán (FVOCI / AFS) phải được đánh giá lại theo giá thị trường (Mark-to-Market) [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
- Khi rủi ro thị trường gia tăng, biên chênh lệch tín dụng của trái phiếu chính quyền địa phương, trái phiếu ngân hàng hoặc trái phiếu doanh nghiệp mở rộng (+100 bps credit spread).
- Khoản sụt giảm giá trị hiện tại này ($\Delta\text{PV} \approx - \text{CS01} \times \Delta\text{Spread}$) không chỉ làm giảm EVE mà còn **chảy thẳng vào Vốn tự có Cấp 1 (Common Equity Tier 1 — CET1)** thông qua khoản lỗ chưa thực hiện trong Thu nhập toàn diện khác tích lũy (AOCI). Đây chính là cơ chế truyền dẫn đã phá hủy năng lực vốn của hàng loạt ngân hàng khu vực Mỹ năm 2023 (xem chi tiết tại [[irrbb-csrbb-measurement-and-hedging]]).

#### Kênh truyền dẫn đến NII:
- Tác động gián tiếp: Khi ngân hàng cần phát hành trái phiếu thứ cấp, chứng chỉ tiền gửi hoặc huy động vốn thị trường mới để tài trợ cho bảng cân đối, ngân hàng phải trả biên chênh lệch tín dụng cao hơn, làm tăng chi phí vốn biên và bào mòn NII trong các chu kỳ tái tài trợ tiếp theo.

---

## 3. Xung Đột Mục Tiêu Chiến Lược: Nghịch Lý Giữa EVE Và NII (The Trade-Off Dilemma)

Một phát hiện cốt lõi mang tính quy luật trong quản trị ALM được Fidelio Tata chứng minh là: **Cả hai thước đo EVE và NII đều cần thiết để lượng hóa rủi ro lãi suất; tuy nhiên, EVE và NII thường phản ứng ngược chiều nhau trước các biến động lãi suất** [[src-tata-bank-alm#^tata-nii-11]]. Basel d368 cũng cảnh báo: nếu ngân hàng chỉ triệt tiêu rủi ro giá trị kinh tế bằng cách khớp kỳ hạn tài sản và nợ dài hạn, ngân hàng có thể đối mặt với rủi ro biến động thu nhập nghiêm trọng [[src-bcbs-irrbb-2016#^irrbb-u02-4]].

```
                                 XUNG ĐỘT MỤC TIÊU EVE vs NII
                                               
           LÃI SUẤT TĂNG (+Δy)                               LÃI SUẤT GIẢM (-Δy)
           -------------------                               -------------------
  NII TĂNG      <--- (Asset-Sensitive) --->        NII GIẢM
  (Tái định giá tài sản nhanh hơn nợ)              (Lợi suất tài sản giảm nhanh hơn nợ)
        VS                                               VS
  EVE GIẢM      <--- (Long Duration)   --->        EVE TĂNG
  (Chiết khấu dòng tiền dài hạn sâu hơn)           (Hiện giá dòng tiền tương lai tăng vọt)
```

### 3.1. Nghiên cứu thực nghiệm số học từ Fidelio Tata: Phòng hộ NII bằng Receiver Swap
Các ngân hàng thường cố tránh biến động NII để ổn định thu nhập qua thời gian [[src-tata-bank-alm#^tata-nii-8]]. Một cách để tận dụng việc lãi suất giảm là ký hợp đồng hoán đổi nhận cố định, trả thả nổi (**Receiver Swap**) [[src-tata-bank-alm#^tata-nii-9]].

- **Tác động lên NII**:
  - Swap minh hoạ có kỳ hạn 3 năm, notional EUR 100, chân cố định 4.16%, chân thả nổi ban đầu 3.95% và tái định giá mỗi sáu tháng [[src-tata-bank-alm#^tata-nii-15]].
  - Với hedge, NII kịch bản sốc −100 bp theo giai đoạn là 3.804 / 4.065 / 7.854 / 14.328 / 15.168, tổng 3 năm 45.219. Hedge giúp ổn định NII, đặc biệt giảm mức sụt NII ở giai đoạn 13–24 tháng [[src-tata-bank-alm#^tata-nii-16]].
  - **Caveat của tác giả**: kết quả này "có vẻ quá tốt để là thật" vì NII đã hedge còn cao hơn cả baseline. Nguyên nhân là mô phỏng giữ nguyên lãi suất ngắn hạn hiện tại; nếu lãi suất tăng theo forward rates, lợi ích ngắn hạn của việc nhận cố định cao, trả thả nổi thấp sẽ mất dần [[src-tata-bank-alm#^tata-nii-17]].
- **Tác động ngược chiều lên EVE**:
  - *Diễn giải:* vị thế nhận cố định tương đương việc nắm thêm một tài sản lãi suất cố định, nên làm tăng duration phía tài sản.
  - Trong phân tích giá trị kinh tế, thêm receiver swap làm **repricing gap tăng từ 1.74 lên 3.63** [[src-tata-bank-alm#^tata-nii-10]]. Gap 1.74 nghĩa là EVE giảm 1.74, bằng 3.48% vốn 50, khi lãi suất tăng 1% [[src-tata-bank-alm#^tata-gap-7]].
  - *Diễn giải:* nếu vốn vẫn là 50, gap 3.63 tương ứng EVE giảm khoảng 7.26% vốn cho mỗi 1% lãi suất tăng, tức khoảng gấp đôi trước khi hedge. Hedge ổn định NII khi lãi suất giảm, nhưng làm tăng tổn thất EVE nếu lãi suất tăng. EVE và NII thường phản ứng ngược chiều nhau [[src-tata-bank-alm#^tata-nii-11]].

```
+---------------------------------------------------------------------------------------------------+
|               BẢNG MINH HỌA ĐÁNH ĐỔI EVE vs NII QUA RECEIVER SWAP (FIDELIO TATA 2025)             |
+-----------------------------+-------------------------------+-------------------------------------+
| CHỈ TIÊU ĐO LƯỜNG           | TRƯỚC PHÒNG HỘ (STANDALONE)   | SAU KHI KÝ RECEIVER SWAP            |
+-----------------------------+-------------------------------+-------------------------------------+
| Repricing gap (EVE)         | 1.74                          | 3.63                                |
| EVE giảm khi LS tăng 1%     | 1.74 = 3.48% vốn 50           | 3.63 ≈ 7.26% vốn 50 (diễn giải)     |
| NII 3 năm, sốc -100 bp      | 42.084 (baseline 42.471)      | 45.219                              |
| NII tháng 13-24, sốc -100 bp| 13.116 (baseline 14.124)      | 14.328                              |
+-----------------------------+-------------------------------+-------------------------------------+
```

---

## 4. Ma Trận Truyền Dẫn Tổng Hợp (Master Transmission Matrix)

| Cấu phần rủi ro | Chỉ số đo lường chính | Độ trễ tác động | Cơ chế tác động đến NII | Cơ chế tác động đến EVE | Công cụ phòng hộ / Kiểm soát ALM |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Parallel Gap** | $12\text{M-GAP}$, Duration Gap ($D^*_{\text{gap}}$) | Tức thì đến 12M | Định giá lại tài sản và nợ chênh lệch khối lượng làm đổi dòng tiền ròng. | Chiết khấu toàn bộ dòng tiền tương lai; tổn thất tỷ lệ thuận với Duration Gap. | Lãi suất hoán đổi (IRS), tái cơ cấu kỳ hạn huy động/cho vay. |
| **Yield Curve** | Steepener / Flattener Shock Scenarios | 12M–36M | Thay đổi độ dốc đường cong ảnh hưởng đến biên độ FTP giữa các kỳ hạn tái tài trợ. | Xoay đường cong làm biến dạng hiện giá các dòng tiền ở các bucket khác nhau. | Curve Swaps, kỳ hạn tái đầu tư danh mục trái phiếu đầu tư. |
| **Tenor Basis** | Basis Spread (vd: 3M vs 1M Euribor) | Ngắn hạn (< 3M) | Chênh lệch biên độ giữa lãi suất tài sản và chi phí nợ cùng kỳ hạn làm giảm NIM. | Chiết khấu theo các đường cong cơ sở đa dạng (multi-curve framework). | Basis Swaps (Tenor basis swap). |
| **Benchmark Basis** | Beta điều hành ($\beta_{\text{admin}}$) | 3M–12M | Tốc độ tăng lãi suất tiền gửi nhanh hơn lãi suất cho vay làm co hẹp biên lãi ròng. | Phân kỳ đường cong chiết khấu giữa các chỉ số lãi suất. | Điều chỉnh chính sách FTP, quản trị biên độ lãi suất bán lẻ. |
| **Automatic Option** | Delta, Vega, Gamma (Black-76 / Bachelier) | Tức thì khi chạm Strike | Caps làm chặn trần thu nhập; Floors làm chặn sàn chi phí, gây co hẹp NIM. | Độ lồi âm (Negative Convexity) làm sụt giảm hiện giá phi tuyến tính khi LS sốc mạnh. | Mua đối ứng Interest Rate Caps/Floors, Swaptions. |
| **Prepayment (CPR)** | Tỷ lệ trả nợ trước hạn (CPR / SMM) | Trung hạn (6M–24M) | Hoàn gốc sớm buộc tái đầu tư với lợi suất thấp, suy giảm thu nhập lãi dài hạn. | Rút ngắn thời lượng tài sản khi LS giảm, triệt tiêu tiềm năng tăng giá (Price Cap). | Phí phạt trả nợ trước hạn, cấu trúc lại hợp đồng tín dụng. |
| **Term Deposit (TDRR)** | Tỷ lệ rút trước hạn (TDRR) | Ngắn hạn (1M–6M) | Mất nguồn vốn chi phí thấp, phải tái huy động bằng vốn đắt hơn, làm tăng chi phí lãi. | Nghĩa vụ nợ bị rút ngắn kỳ hạn thực tế, đẩy chi phí chiết khấu lên cao. | Quy định phạt mất toàn bộ lãi khi rút trước hạn. |
| **NMDs Run-off** | Mô hình hóa kỳ hạn NMDs (Core / Non-core) | Liên tục | Tiền gửi không kỳ hạn chuyển dịch sang có kỳ hạn hoặc rút khỏi hệ thống khi LS tăng. | Phá vỡ cấu trúc thời lượng nợ giả định, làm gia tăng khe hở thời lượng ròng. | Phân tích cơ sở khách hàng, xác định tỷ lệ tiền gửi lõi ổn định. |
| **Pipeline Risk** | Tỷ lệ cam kết giải ngân (Drawdown rate) | Ngắn hạn (1M–3M) | Giải ngân vốn cam kết lãi suất thấp trong môi trường lãi suất thị trường đã tăng. | Phát sinh nghĩa vụ tài sản dưới giá thị trường ngay tại thời điểm giải ngân. | Giới hạn thời gian cam kết hạn mức, phòng hộ trước bằng phái sinh. |
| **CSRBB** | CS01, Spread Duration, Mark-to-Market | Tức thì qua AOCI/P&L | Tăng chi phí phát hành công cụ nợ và chứng chỉ tiền gửi dài hạn của chính ngân hàng. | Giảm trực tiếp hiện giá danh mục FVOCI, trừ thẳng vào Vốn tự có Cấp 1 (CET1). | Giới hạn tỷ trọng FVOCI, phòng hộ bằng Credit Default Swaps (CDS). |

---

## 5. Hàm Ý Quản Trị Dành Cho Ủy Ban ALCO

Từ các phân tích chuẩn mực và thực nghiệm, Ủy ban ALCO bắt buộc phải tuân thủ các nguyên tắc cốt lõi sau để điều hành bảng cân đối an toàn và bền vững:

1. **Vận hành Khung Quản Trị Trụ Cột Kép (Dual-Pillar Framework)**:
   - Tuyệt đối không bao giờ được tối ưu hóa đơn lẻ một thước đo thu nhập (NII) mà bỏ qua giá trị kinh tế (EVE), hoặc ngược lại.
   - Thiết lập hệ thống hạn mức kép song hành: Hạn mức $\Delta\text{NII}$ để bảo vệ kế hoạch kinh doanh và cổ tức trong ngắn hạn (12 tháng), kết hợp hạn mức $\Delta\text{EVE} \le 15\%$ Vốn Cấp 1 (theo ngưỡng cảnh báo Outlier của Basel d368) để bảo vệ khả năng thanh toán và giá trị nội tại dài hạn của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
2. **Kiểm Soát Rủi Ro Phòng Hộ Ngược (Hedging Paradox)**:
   - Khi thực hiện các chiến lược phái sinh phòng hộ NII (như Receiver Swap), ALCO bắt buộc phải chạy mô phỏng tác động tràn (*spill-over effect*) đối với khe hở thời lượng và độ nhạy EVE. Tránh bẫy "ổn định thu nhập ngắn hạn nhưng đánh đổi bằng rủi ro phá sản dài hạn khi lãi suất đảo chiều" [[src-tata-bank-alm#^tata-nii-10]].
3. **Hiện Đại Hóa Mô Hình Hành Vi (Behavioral Modeling)**:
   - Không được giả định hành vi khách hàng là tĩnh. Phải liên tục hiệu chuẩn các tỷ lệ trả nợ trước hạn (CPR), rút tiền gửi trước hạn (TDRR) và tỷ lệ chuyển dịch tiền gửi không kỳ hạn (NMDs) theo từng kịch bản sốc lãi suất [[src-bcbs-irrbb-2016#^irrbb-p05-1]]. Áp dụng phương pháp phòng hộ động (dynamic hedging) thay vì các sản phẩm phái sinh swaption đắt đỏ [[src-choudhry-principles-banking#^choudhry-irrbb-8]].
4. **Tích Hợp Hoàn Toàn Vào Hệ Thống Định Giá Chuyển Nhượng Vốn Nội Bộ (FTP)**:
   - Mọi cấu phần rủi ro (kỳ hạn, cơ sở, quyền chọn ngầm) phải được định giá sòng phẳng và chuyển giao về Treasury quản trị tập trung [[src-tata-bank-alm#^tata-ftp-1]].
   - Bộ phận Treasury được bù đắp thù lao thông qua Khoản đóng góp cấu trúc (*Structural Contribution*) để gánh vác rủi ro thanh khoản và rủi ro lãi suất phát sinh từ sự lệch pha kỳ hạn tự nhiên của bảng cân đối ngân hàng [[src-tata-bank-alm#^tata-ftp-1]] [[src-tata-bank-alm#^tata-ftp-2]].

## Bất định
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
