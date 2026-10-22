---
title: Quản trị Rủi ro Mô hình trong ALM (Model Risk Management)
aliases: [model-risk-management, MRM, rủi ro mô hình ALM, quản trị rủi ro mô hình]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: draft
updated: 2026-10-19
sources: ["[[src-tt83-2025-nhnn]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: limits, to: "[[balance-sheet-optimisation-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u05-12]]"}
  - {type: limits, to: "[[replicating-portfolio-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u05-13]]"}
---

# Quản trị Rủi ro Mô hình trong ALM (Model Risk Management)

## 1. Bản chất và Định nghĩa Mô hình trong ALM

Theo hướng dẫn giám sát của Cục Dự trữ Liên bang Mỹ và Văn phòng Kiểm soát Tiền tệ (OCC, FED 2011-2012 / SR 11-7) được Beata Lubinska viện dẫn, mô hình (model) được định nghĩa là một thuật toán định lượng, hệ thống hoặc phương pháp tiếp cận áp dụng các lý thuyết, kỹ thuật và giả định mang tính thống kê, kinh tế, tài chính hoặc toán học để xử lý dữ liệu đầu vào thành các ước lượng định lượng [[src-lubinska-alm-optimisation#^lubinska-u05-13]].

Một mô hình ALM hoàn chỉnh bao gồm tối thiểu ba cấu phần cơ bản [[src-lubinska-alm-optimisation#^lubinska-u05-13]]:
1. **Dữ liệu đầu vào (Inputs)**: Tập hợp dữ liệu lịch sử, tham số thị trường, giả định hành vi (như tỷ lệ trả nợ trước hạn CPR, tỷ lệ rút tiền gửi sớm TDRR, tỷ lệ tái tục) và các giả thiết vận hành đưa vào mô hình.
2. **Phương pháp chuyển đổi (Transformation Method)**: Thuật toán định lượng hoặc các chuỗi tính toán chuyển hóa dữ liệu đầu vào thành các ước lượng (ví dụ: thuật toán điểm trong KKT trong [[balance-sheet-optimisation-model]], kỹ thuật hồi quy đồng tích hợp trong [[replicating-portfolio-model]], hoặc phương trình phân rã thời lượng trong [[duration-gap-model]]).
3. **Cấu phần báo cáo (Reporting Component)**: Hệ thống tổng hợp và chuyển đổi các kết quả ước lượng định lượng thành thông tin quản trị kinh doanh hữu ích phục vụ việc ra quyết định của Ủy ban ALCO ([[alco]]) và Hội đồng Quản trị.

Rủi ro mô hình (Model Risk) được định nghĩa là nguy cơ phát sinh các hệ quả bất lợi bắt nguồn từ việc đưa ra quyết định dựa trên các kết quả đầu ra hoặc báo cáo mô hình bị sai lệch, khiếm khuyết hoặc bị sử dụng sai mục đích [[src-lubinska-alm-optimisation#^lubinska-u05-15]]. Trong lĩnh vực ALM, rủi ro mô hình có thể dẫn đến việc Ban điều hành định giá sai chi phí vốn [[ftp-pricing-methodology]], tính toán thiếu đệm thanh khoản HQLA [[hqla]], đánh giá thấp mức độ sụt giảm [[economic-value-of-equity|$\Delta\text{EVE}$]] hoặc thu nhập lãi thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]], từ đó đối mặt với các tổn thất tài chính và biện pháp can thiệp giám sát.

---

## 2. Ba Nguồn Phát sinh Rủi ro Mô hình Cơ bản

Theo phân loại của Beata Lubinska, rủi ro mô hình trong các định chế tài chính phát sinh từ 3 nhóm nguyên nhân cốt lõi [[src-lubinska-alm-optimisation#^lubinska-u05-14]]:

```
                     ┌─────────────────────────────────────────┐
                     │          RỦI RO MÔ HÌNH (MRM)           │
                     └────────────────────┬────────────────────┘
                                          │
         ┌────────────────────────────────┼────────────────────────────────┐
         ▼                                ▼                                ▼
┌──────────────────┐            ┌──────────────────┐            ┌──────────────────┐
│   Khiếm khuyết   │            │  Bất định và Sai │            │  Sử dụng Sai     │
│     Dữ liệu      │            │   số Mô hình     │            │    Mục đích      │
└────────┬─────────┘            └────────┬─────────┘            └────────┬─────────┘
         │                               │                               │
  - Thiếu độ sâu LS               - Giả định sai lệch             - Dùng ngoài phạm vi
  - Lỗi nạp dữ liệu               - Đơn giản hoá quá mức          - Không tái hiệu chuẩn
  - Cỡ mẫu không đủ               - Lỗi cấu trúc thuật toán       - Lạm dụng tự động hoá
```

1. **Khiếm khuyết dữ liệu (Data deficiencies)**:
   - Thiếu hụt cả về tính sẵn có (availability) và chất lượng (quality) của dữ liệu.
   - Các lỗi nhập liệu thủ công hoặc lỗi đường truyền (data feeding errors).
   - Thiếu chiều sâu dữ liệu lịch sử qua các chu kỳ kinh tế (historical depth).
   - Quy mô mẫu quan sát không đủ lớn để bảo đảm ý nghĩa thống kê của các ước lượng tham số.

2. **Bất định ước lượng và sai số mô hình (Estimation uncertainty or model error)**:
   - Các giả định nền tảng bị khiếm khuyết, thiên lệch hoặc không còn phù hợp với điều kiện thị trường thay đổi (flawed assumptions).
   - Đơn giản hóa quá mức các mối quan hệ phi tuyến (ví dụ: dùng mô hình tuyến tính đơn giản để ước lượng hành vi trả nợ trước hạn vốn có tính lồi âm phức tạp [[src-lubinska-alm-optimisation#^lubinska-u04-11]]).
   - Sai số thiết kế trong cấu trúc thuật toán hoặc công thức định giá.

3. **Sử dụng sai mục đích (Model misuse)**:
   - Áp dụng mô hình cho các sản phẩm, thị trường hoặc mục đích khác với phạm vi thiết kế ban đầu mà không có kiểm định thích ứng.
   - Mô hình bị bỏ quên, không được tái hiệu chuẩn (recalibration) định kỳ theo biến động của môi trường vĩ mô và lãi suất.
   - Ban điều hành phụ thuộc thụ động vào các kết quả tự động hóa mà thiếu sự đánh giá phê phán từ chuyên môn thực tế.

---

## 3. Nguyên lý Tinh gọn trong Mô hình hóa (Parsimony Principle)

Một nguyên tắc chỉ đạo được Beata Lubinska nhấn mạnh trong xây dựng mô hình ALM là **Nguyên lý Tinh gọn (Parsimony Principle)**: *Mô hình càng tinh gọn càng tốt* [[src-lubinska-alm-optimisation#^lubinska-u05-12]].

Quan điểm này không cổ súy cho việc áp dụng các mô hình thô sơ (rudimentary models) không phản ánh được bản chất rủi ro. Thay vào đó, nguyên lý tinh gọn khẳng định rằng:
- Việc gia tăng độ phức tạp và tinh vi không cần thiết (unnecessary model sophistication) sẽ làm tăng cấp số nhân rủi ro mô hình.
- Mô hình quá phức tạp tạo ra "hộp đen" toán học, làm gia tăng rào cản trong công tác vận hành, hiệu chuẩn tham số và gây khó khăn cho việc kiểm định độc lập.
- Khả năng bị cơ quan giám sát chất vấn và nguy cơ bị phạt vốn Trụ cột 2 (capital add-on) tỷ lệ thuận với mức độ phức tạp không thể giải trình của mô hình [[src-lubinska-alm-optimisation#^lubinska-u05-12]].

---

## 4. Khung Kiểm định và Quản trị Rủi ro Mô hình (Model Validation Framework)

### 4.1. Nguyên tắc Phản biện Hiệu quả (Effective Challenge)
Theo chuẩn mực giám sát quốc tế, nền tảng cốt tử của khung Quản trị Rủi ro Mô hình (Model Risk Management - MRM) là cơ chế **"Phản biện hiệu quả" (Effective Challenge)** [[src-lubinska-alm-optimisation#^lubinska-u05-15]].

Phản biện hiệu quả được định nghĩa là sự phân tích mang tính phê phán khách quan được thực hiện bởi các nhân sự:
- **Độc lập** hoàn toàn với bộ phận phát triển và sở hữu mô hình (Model Developers / Owners).
- **Có năng lực chuyên môn định lượng** và **am hiểu sâu sắc mảng kinh doanh** mà mô hình được ứng dụng.
- Có thẩm quyền nhận diện các hạn chế cốt lõi của mô hình, phát hiện các giả định bất hợp lý và yêu cầu các điều chỉnh bắt buộc trước khi đưa vào ứng dụng thực tiễn.

### 4.2. Bốn Trụ cột Kiểm định Mô hình Độc lập
Quy trình kiểm định mô hình toàn diện (Model Validation) được phân tách thành 4 trụ cột nghiệp vụ [[src-lubinska-alm-optimisation#^lubinska-u05-15]]:

| Trụ cột kiểm định | Nội dung kiểm tra | Mục tiêu giám sát |
|---|---|---|
| **1. Kiểm định Kết quả Đầu ra (Outcome Assessment)** | Đánh giá kết quả ước lượng của mô hình so với diễn biến thực tế phát sinh (backtesting, benchmarking, stress testing). | Xác nhận nghiệm mô hình nằm trong khoảng kỳ vọng hợp lý của hoạt động kinh doanh. |
| **2. Kiểm định Giả định (Assumptions Assessment)** | Rà soát toàn bộ các giả thiết kinh tế, hành vi khách hàng (CPR, TDRR, CASA core ratio) và các điều kiện biên. | Bảo đảm các giả định được áp dụng phù hợp với mục tiêu mô hình và bối cảnh thị trường hiện hành. |
| **3. Kiểm định Phương pháp luận (Methodology Assessment)** | Thẩm định cơ sở lý thuyết toán học, tính vững của thuật toán (convergence của thuật toán điểm trong, tính ổn định của ma trận hiệp phương sai). | Xác nhận phương pháp tiếp cận là chuẩn mực, không có lỗi logic hoặc sai số xấp xỉ nghiêm trọng. |
| **4. Kiểm định Quy trình Dữ liệu (Data Feeding Assessment)** | Kiểm tra tính đầy đủ, độ chính xác, quy trình thu thập dữ liệu và các rủi ro vận hành trong khâu nạp dữ liệu. | Triệt tiêu nguy cơ "rác vào, rác ra" (garbage in, garbage out) trong quá trình nạp dữ liệu tự động. |

### 4.3. Vai trò Giám sát của Kiểm toán Nội bộ và Hội đồng Quản trị
- **Hội đồng Quản trị (Board of Directors)**: Chịu trách nhiệm tối cao trong việc phê duyệt Khung Quản trị Rủi ro Mô hình (MRM Framework), xác định khẩu vị rủi ro mô hình (xem [[risk-appetite]]) và phê duyệt chính sách phân định vai trò sở hữu, kiểm soát và tuân thủ [[src-lubinska-alm-optimisation#^lubinska-u05-15]].
- **Kiểm toán Nội bộ (Internal Audit)**: Thực hiện đánh giá độc lập định kỳ đối với toàn bộ quy trình kiểm định mô hình, thẩm tra tính khách quan và mức độ độc lập thực chất của đơn vị kiểm định mô hình, đồng thời rà soát mức độ tuân thủ quy chế vận hành mô hình trên toàn hàng [[src-lubinska-alm-optimisation#^lubinska-u05-15]].

### 4.4. Bài Học Thực Nghiệm: Rủi Ro Mô Hình Tiềm Ẩn và Bất Đối Xứng Hành Vi (Bank Case Studies)
Nghiên cứu điển hình của Beata Lubinska (2020) tại hai ngân hàng thực tế cung cấp các bài học cốt tử cho công tác MRM [[src-lubinska-alm-optimisation#^lubinska-u06-10]] [[src-lubinska-alm-optimisation#^lubinska-u06-12]]:
- **Rủi ro mô hình tiềm ẩn từ cấu trúc nợ ngắn hạn (Bank 2 Case Study)**: Tại Ngân hàng 2 (quy mô USD 549 tỷ), trên cơ sở hợp đồng, **100% nợ phải trả có kỳ hạn bình quân dưới 1 năm** [[src-lubinska-alm-optimisation#^lubinska-u06-12]]. Cấu trúc này đưa một **rủi ro mô hình tiềm ẩn trọng yếu (material embedded model risk)** vào sổ ngân hàng, vì toàn bộ tính bền vững thanh khoản và rủi ro lãi suất phụ thuộc hoàn toàn vào các giả định và kết quả của mô hình đặc tính hóa tiền gửi không kỳ hạn (CASA kỳ hạn hợp đồng 1 ngày nhưng được mô hình hóa có kỳ hạn kinh tế dài hạn) [[src-lubinska-alm-optimisation#^lubinska-u06-12]].
- **Bất đối xứng độ nhạy hành vi (Liability vs Asset Sensitivity)**: Kết quả tối ưu hóa chứng minh mô hình nhạy cảm cao hơn đáng kể với các giả định hành vi bên nợ phải trả (độ biến động và độ nhạy lãi suất CASA) so với bên tài sản (tỷ lệ trả nợ trước hạn CPR) [[src-lubinska-alm-optimisation#^lubinska-u06-10]]. Do đó, đơn vị kiểm định độc lập phải ưu tiên tài nguyên và tần suất kiểm tra cao nhất cho các mô hình tiền gửi hành vi.
- **Hiệu ứng quy mô và giảm chấn đa dạng hóa (Bank Size Diversification Effect)**: Tại các ngân hàng quốc tế quy mô lớn, danh mục tài sản và nguồn vốn đa dạng hóa cao giúp làm suy giảm và hấp thụ (*subdued*) tác động của các giả định hành vi đơn lẻ, khiến mô hình phản ứng chậm hơn trước thay đổi tham số so với các ngân hàng nhỏ [[src-lubinska-alm-optimisation#^lubinska-u06-14]].

---

## 5. Mối Quan hệ với các Cấu phần ALM trong Vault

```
                             ┌─────────────────────────────┐
                             │    model-risk-management    │
                             └──────────────┬──────────────┘
                                            │ limits
                     ┌──────────────────────┴──────────────────────┐
                     ▼                                             ▼
       ┌───────────────────────────┐                 ┌───────────────────────────┐
       │balance-sheet-optimisation │                 │ replicating-portfolio-   │
       │          -model           │                 │           model           │
       └───────────────────────────┘                 └───────────────────────────┘
```

- [[balance-sheet-optimisation-model]]: Mô hình tối ưu hóa phi tuyến chịu sự ràng buộc chặt chẽ của MRM: yêu cầu tuân thủ nguyên lý tinh gọn, thẩm định tính hội tụ của hàm phạt logarit trong MATLAB `fmincon`, và kiểm tra độ nhạy của nghiệm trước các thay đổi giả định về kịch bản lãi suất và thanh khoản [[src-lubinska-alm-optimisation#^lubinska-u05-12]].
- [[replicating-portfolio-model]]: Mô hình danh mục sao chép tiền gửi không kỳ hạn NMDs đòi hỏi kiểm định thường xuyên về tính dừng của chuỗi dữ liệu, kiểm tra hiện tượng dịch chuyển tham số co-integration và backtest mức độ biến động [[net-interest-margin|NIM]].
- [[behavioural-options]]: Mô hình hóa hành vi khách hàng (Prepayment CPR, Early Redemption TDRR) là một trong những nguồn rủi ro mô hình lớn nhất trong ALM do tính bất đối xứng và chi phối bởi biến số nhân khẩu học xã hội.

---

## Góc nhìn VN
- **Hiệu lực**: quản lý rủi ro mô hình theo Mục 8 Chương III bắt buộc chậm nhất từ 01/01/2028 [[src-tt83-2025-nhnn#^d74-3]]. Riêng mô hình dùng trong phương pháp xếp hạng nội bộ: áp dụng từ 01/07/2026 nếu ngân hàng đã chuyển đổi sang phương pháp này trước ngày đó, hoặc từ ngày bắt đầu chuyển đổi nếu chuyển đổi từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-3]]. Ngân hàng áp dụng sớm trước 01/01/2028 phải thông báo NHNN trong 10 ngày kể từ ngày thực hiện [[src-tt83-2025-nhnn#^d74-5]].
- TT83/2025 định nghĩa mô hình là phương pháp, hệ thống, cách tiếp cận định lượng xử lý dữ liệu đầu vào thành kết quả đầu ra; rủi ro mô hình là rủi ro do lỗi mô hình khi xây dựng, triển khai hoặc do dùng mô hình không phù hợp; vòng đời mô hình tối thiểu gồm xây dựng, triển khai, sử dụng, theo dõi giám sát, kiểm định [[src-tt83-2025-nhnn#^d3-24]].
- **Xếp hạng mô hình**: ngân hàng xác định danh mục mô hình, định kỳ xếp hạng rủi ro cao, trung bình, thấp theo tính trọng yếu, độ phức tạp, mục đích, chất lượng; mô hình dùng trong phương pháp xếp hạng nội bộ là rủi ro cao [[src-tt83-2025-nhnn#^d56-1]]. Mục 8 áp dụng tối thiểu cho mô hình rủi ro cao [[src-tt83-2025-nhnn#^d56-2]].
- **Vòng đời**: xây dựng (mục đích, phạm vi, chất lượng dữ liệu); triển khai thống nhất với bản đã duyệt, kể cả UAT; sử dụng đúng mục đích, kiểm soát ghi đè (override) đầu vào và đầu ra; theo dõi hiệu quả [[src-tt83-2025-nhnn#^d56-4]]; kiểm định trước khi dùng, khi thay đổi trọng yếu và tối thiểu hằng năm [[src-tt83-2025-nhnn#^d56-4d]]. Xem [[model-validation]].
- **Mô hình mua ngoài và hồ sơ**: yêu cầu bên bán cung cấp thông tin; lập hồ sơ cho mô hình rủi ro cao, kể cả đã điều chỉnh, đã ngừng [[src-tt83-2025-nhnn#^d56-5]].
- **Ba tuyến bảo vệ riêng**: tuyến 1 xây dựng, triển khai, sử dụng mô hình; tuyến 2 kiểm định mô hình và xây dựng chính sách; tuyến 3 kiểm toán nội bộ [[src-tt83-2025-nhnn#^d56-7]]. Xem [[three-lines-of-defence]].
- **Nhận dạng và báo cáo**: xác định nguyên nhân phát sinh rủi ro mô hình, có biện pháp khắc phục [[src-tt83-2025-nhnn#^d57-1]]; báo cáo nội bộ tối thiểu hằng năm [[src-tt83-2025-nhnn#^d58-1]].
- **Mô hình giá (rủi ro thị trường)**: nếu dùng mark to model, mô hình phải đánh giá đầy đủ yếu tố ảnh hưởng giá trị, dùng dữ liệu thị trường từ nguồn tin cậy được đánh giá độc lập, và được rà soát tối thiểu hằng năm hoặc đột xuất [[src-tt83-2025-nhnn#^d36-1c]]. Xem [[market-risk-management]].

## Xem Thêm
- [[balance-sheet-optimisation-model]]
- [[replicating-portfolio-model]]
- [[behavioural-options]]
- [[non-maturity-deposits]]
- [[src-lubinska-alm-optimisation]]
