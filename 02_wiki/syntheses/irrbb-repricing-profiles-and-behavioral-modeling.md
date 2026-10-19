---
title: "Xác Định Repricing Profile và Khung Ứng Dụng Behavioral Modeling trong IRRBB"
aliases: [IRRBB Repricing Profiles and Behavioral Modeling, Cơ chế xác định Repricing Profile, Behavioral Modeling in IRRBB, Contractual vs Reset vs Behavioral Maturity]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Repricing profile của từng portfolio được xác định theo contractual maturity, next repricing date hay behavioral maturity? Khi nào cần áp dụng Behavioral Modeling theo chuẩn mực BCBS d368 và phân tích của Fidelio Tata?"
as_of: 2026-10-19
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-tt83-2025-nhnn]]"]
relations: []
tags: [irrbb, repricing-profile, behavioral-modeling, contractual-maturity, reset-date, nmd, prepayment, replicating-portfolio, synthesis]
updated: 2026-10-19
reviewed:
---

## Câu hỏi

- **Q1**: Repricing profile của từng portfolio được xác định theo contractual maturity, next repricing date hay behavioral maturity?
- **Q2**: Khi nào cần áp dụng Behavioral Modeling?

## Kết luận

1. **Về cơ chế xác định Repricing Profile (Q1)**:
   - Repricing profile không ấn định theo một phương pháp duy nhất cho toàn bộ bảng cân đối, mà phân bổ theo bản chất nhạy cảm lãi suất và đặc tính sản phẩm [[src-tata-bank-alm#^tata-gap-1]]:
     - **Contractual Maturity**: Dành cho tài sản/nợ lãi suất cố định thuần túy không có quyền chọn nhúng (hoặc có chi phí phạt phá vỡ hợp đồng đủ lớn triệt tiêu động cơ khách hàng) [[src-tata-bank-alm#^tata-gap-1]]. Dòng tiền phân bổ theo lịch đáo hạn pháp lý hoặc lịch trả nợ danh nghĩa.
     - **Next Repricing Date / Reset Date**: Dành cho tài sản/nợ lãi suất thả nổi định kỳ neo theo chỉ số tham chiếu [[src-tata-bank-alm#^tata-gap-1]]. Ngay tại ngày reset date, công cụ quay về giao dịch ngang mệnh giá ($PV = Par$), triệt tiêu rủi ro giá trị kinh tế của kỳ hạn gốc [[src-tata-bank-alm#^tata-gap-2]]; do đó bắt buộc phải slot vào dải kỳ hạn chứa ngày reset kế tiếp, không được slot theo ngày đáo hạn hợp đồng [[src-tata-bank-alm#^tata-gap-2]].
     - **Behavioral Maturity**: Dành cho các sản phẩm không có kỳ hạn hợp đồng (NMDs/CASA) hoặc có kỳ hạn hợp đồng nhưng chứa quyền chọn hành vi của khách hàng (prepayment, rút trước hạn, pipeline) [[src-tata-bank-alm#^tata-nmd-1]] [[src-tata-bank-alm#^tata-opt-3]]. Dòng tiền phân bổ dựa trên mô hình danh mục sao chép hoặc tỷ lệ suy giảm dòng tiền [[src-tata-bank-alm#^tata-nmd-3]].
2. **Về các trường hợp bắt buộc áp dụng Behavioral Modeling (Q2)**:
   - Ngân hàng bắt buộc áp dụng mô hình hành vi khi danh mục chứa **quyền chọn hành vi (behavioral options)** của khách hàng bán lẻ và doanh nghiệp nhỏ, nơi quyết định thực hiện quyền chịu chi phối bởi các yếu tố phi tài chính và nhân khẩu học [[src-tata-bank-alm#^tata-opt-1]] [[src-tata-bank-alm#^tata-opt-4]] [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
   - Năm trường hợp bắt buộc gồm: (1) Tiền gửi không kỳ hạn và thanh toán (NMDs/CASA) qua phân tách Core/Non-core và mô hình Replicating Portfolio [[src-bcbs-irrbb-2016#^irrbb-u05-4]] [[src-tata-bank-alm#^tata-nmd-3]]; (2) Cho vay cố định chịu rủi ro trả nợ trước hạn (Prepayment CPR) [[src-bcbs-irrbb-2016#^irrbb-u05-5]] [[src-tata-bank-alm#^tata-opt-3]]; (3) Tiền gửi có kỳ hạn chịu rủi ro rút trước hạn (Early redemption TDRR) [[src-bcbs-irrbb-2016#^irrbb-u05-6]]; (4) Rủi ro giải ngân đường ống cam kết cho vay (Pipeline risk) [cần nguồn]; (5) Tiền gửi lãi suất điều hành phi tuyến (Administered rate deposits & Deposit Beta) [cần nguồn].
   - *Lưu ý quy định tại Việt Nam*: [[tt83-2025]] (hiệu lực 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]]) là căn cứ. Phụ lục V dùng cùng 19 thang [[src-tt83-2025-nhnn#^pl5-a2-t1]], cùng trần NMDs lõi [[src-tt83-2025-nhnn#^pl5-a2-3a]] và cùng hệ số $\gamma_i$, $u_i$ [[src-tt83-2025-nhnn#^pl5-a2-3b]] [[src-tt83-2025-nhnn#^pl5-a2-3c]] như d368. Quản lý rủi ro mô hình hành vi thuộc C3-M8 `[cần nguồn: src-tt83-2025-nhnn C3-M8]`.

---

## 1. Bản Chất Và Vai Trò Của Repricing Profile Trong Quản Trị IRRBB

Trong quản trị rủi ro lãi suất trên sổ ngân hàng ([[bcbs-irrbb|IRRBB]]), Bảng cân đối định giá lại ([[repricing-balance-sheet|Repricing Schedule]]) là nền tảng kỹ thuật bắt buộc để lượng hóa cả biến động giá trị kinh tế ([[economic-value-of-equity|∆EVE]]) và biến động thu nhập lãi thuần ([[net-interest-income-sensitivity|∆NII]]) [[src-bcbs-irrbb-2016#^irrbb-u05-1]].

Repricing Profile biểu diễn lịch trình phân bổ toàn bộ dòng tiền gốc và lãi (notional cash flows) phát sinh từ các tài sản, nợ phải trả và cam kết ngoại bảng nhạy cảm với lãi suất vào các dải kỳ hạn chuẩn hóa (time bands/buckets) [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. Điểm mấu chốt quyết định độ chính xác của mô hình là xác định chính xác thời điểm mà dòng tiền đó **nhạy cảm với sự thay đổi của lãi suất thị trường**.

Việc xác định Repricing Profile được phân bổ theo ba phương pháp căn bản:

```
                          ┌────────────────────────────────────────────────────────┐
                          │   CƠ CHẾ PHÂN BỔ REPRICING PROFILE TRÊN BẢNG ALM      │
                          └──────────────────────────┬─────────────────────────────┘
                                                     │
         ┌───────────────────────────────────────────┼───────────────────────────────────────────┐
         ▼                                           ▼                                           ▼
┌──────────────────────────────┐            ┌──────────────────────────────┐            ┌──────────────────────────────┐
│     CONTRACTUAL MATURITY     │            │      NEXT REPRICING DATE     │            │     BEHAVIORAL MATURITY      │
├──────────────────────────────┤            ├──────────────────────────────┤            ├──────────────────────────────┤
│ • Lãi suất cố định thuần túy │            │ • Lãi suất thả nổi định kỳ   │            │ • Sản phẩm chứa quyền chọn   │
│ • Không có quyền chọn nhúng  │            │ • Neo theo chỉ số tham chiếu │            │   hành vi của khách hàng     │
│ • Slot theo lịch đáo hạn     │            │ • Ngang mệnh giá tại Reset   │            │ • Ước tính bằng mô hình      │
│   hoặc hoàn trả danh nghĩa   │            │ • Slot vào ngày Reset kế tiếp│            │   thống kê / kinh tế lượng   │
└──────────────────────────────┘            └──────────────────────────────┘            └──────────────────────────────┘
```

---

## 2. So Sánh Ba Cơ Chế Xác Định Repricing Profile

| Tiêu chí | Contractual Maturity (Kỳ hạn hợp đồng) | Next Repricing Date / Reset Date (Ngày định giá lại kế tiếp) | Behavioral Maturity (Kỳ hạn hành vi) |
| :--- | :--- | :--- | :--- |
| **Bản chất kinh tế** | Dòng tiền gốc được hoàn trả toàn bộ hoặc từng phần theo lịch trình pháp lý cố định, chấm dứt cam kết lãi suất cố định ban đầu. | Thời điểm mà lãi suất hợp đồng được cập nhật theo lãi suất thị trường hiện hành; **công cụ quay về giao dịch ngang mệnh giá (*par*)**, triệt tiêu rủi ro định giá của kỳ hạn gốc [[src-tata-bank-alm#^tata-gap-2]]. | Dòng tiền thực tế phát sinh sớm hơn hoặc muộn hơn kỳ hạn hợp đồng do khách hàng thực hiện quyền chọn hành vi; kỳ hạn kỳ vọng bị co ngắn hoặc kéo dài so với hợp đồng [[src-tata-bank-alm#^tata-opt-3]]. |
| **Điều kiện áp dụng** | Công cụ có lãi suất cố định thuần túy (fixed-rate bullet hoặc amortising) và không chứa quyền chọn nhúng (hoặc chi phí phạt phá vỡ hợp đồng đủ lớn để triệt tiêu động cơ thực hiện quyền chọn). | Công cụ có lãi suất thả nổi định kỳ (floating-rate), neo theo một chỉ số tham chiếu lãi suất minh bạch trên thị trường tiền tệ (SOFR, Euribor 1M/3M/6M) [[src-tata-bank-alm#^tata-gap-1]]. | Sản phẩm có kỳ hạn hành vi khác biệt với kỳ hạn hợp đồng hoặc hoàn toàn không có kỳ hạn hợp đồng xác định [[src-tata-bank-alm#^tata-nmd-1]]. |
| **Phân bổ vào Time Bands** | Dòng tiền được slot vào dải kỳ hạn tương ứng với ngày đáo hạn cuối cùng hoặc từng đợt trả nợ gốc/lãi danh nghĩa [[src-tata-bank-alm#^tata-gap-1]]. | Toàn bộ số dư danh nghĩa (hoặc dòng tiền gốc chịu thả nổi) được slot vào dải kỳ hạn chứa **ngày tái xác định lãi suất kế tiếp** [[src-tata-bank-alm#^tata-gap-1]] [[src-tata-bank-alm#^tata-gap-2]]. | Số dư danh nghĩa được phân rã thành các dòng tiền ảo và phân bổ vào các dải kỳ hạn dựa trên mô hình danh mục sao chép hoặc tỷ lệ suy giảm dòng tiền [[src-tata-bank-alm#^tata-nmd-3]]. |
| **Danh mục áp dụng điển hình** | • Trái phiếu Chính phủ / Doanh nghiệp cố định không quyền chọn mua lại (*bullet*).<br>• Khoản vay doanh nghiệp lớn lãi suất cố định có điều khoản bồi hoàn chi phí tài chính (*breakage costs/make-whole*).<br>• Tiền gửi bán buôn kỳ hạn cố định không được rút trước hạn. | • Cho vay doanh nghiệp / bán lẻ thả nổi định kỳ.<br>• Tiền gửi và vay liên ngân hàng thả nổi.<br>• Trái phiếu thả nổi (FRNs).<br>• Chân thả nổi của hợp đồng hoán đổi lãi suất (IRS floating leg). | • Tiền gửi không kỳ hạn và tiền gửi thanh toán ([[non-maturity-deposits|NMDs / CASA]]).<br>• Cho vay thế chấp mua nhà cố định có quyền trả nợ trước hạn (Prepayment).<br>• Tiền gửi có kỳ hạn cho phép rút sớm (Early redemption).<br>• Cam kết tín dụng (Pipeline risk). |

### Cơ Chế Reset Date Triệt Tiêu Rủi Ro Định Giá (Fidelio Tata)

Theo Fidelio Tata (2025), sai lầm phổ biến trong ALM là nhầm lẫn giữa kỳ hạn hoàn trả gốc của hợp đồng và kỳ hạn nhạy cảm lãi suất [[src-tata-bank-alm#^tata-gap-1]].

Đối với một khoản vay thế chấp hoặc tín dụng doanh nghiệp có kỳ hạn 10 năm nhưng lãi suất thả nổi điều chỉnh 3 tháng một lần theo Euribor 3M:
* Khoản vay này **không** mang rủi ro lãi suất của một tài sản 10 năm [[src-tata-bank-alm#^tata-gap-2]].
* Ngay tại ngày Reset Date, lãi suất của khoản vay được cập nhật bằng lãi suất thị trường hiện hành. Về mặt định giá chiết khấu dòng tiền, giá trị hiện tại của khoản vay quay về đúng mệnh giá danh nghĩa ($PV = Par$) [[src-tata-bank-alm#^tata-gap-2]].
* Do đó, rủi ro biến động giá trị kinh tế của khoản vay chỉ tồn tại trong khoảng thời gian từ hiện tại cho đến ngày Reset Date kế tiếp. Trong Repricing Schedule, khoản vay này bắt buộc phải được slot vào dải kỳ hạn 1–3 tháng (hoặc dải chứa ngày reset kế tiếp), hoàn toàn không được slot vào dải 10 năm [[src-tata-bank-alm#^tata-gap-1]] [[src-tata-bank-alm#^tata-gap-2]].

---

## 3. Khung Ứng Dụng Behavioral Modeling: Năm Trường Hợp Bắt Buộc

Ủy ban Basel ([[bcbs-irrbb|BCBS d368]]) và Fidelio Tata chỉ rõ: Việc áp dụng máy móc kỳ hạn hợp đồng danh nghĩa cho các danh mục chứa quyền chọn hành vi của khách hàng sẽ làm biến dạng nghiêm trọng thước đo [[economic-value-of-equity|∆EVE]] và [[net-interest-income-sensitivity|∆NII]]. Ngân hàng bắt buộc phải ứng dụng mô hình hóa hành vi (Behavioral Modeling) trong năm trường hợp sau:

### 3.1. Tiền Gửi Không Kỳ Hạn Và Thanh Toán (Non-Maturity Deposits - NMDs / CASA)

* **Xung đột thực tế**: Về mặt pháp lý hợp đồng, khách hàng có quyền rút tiền bất kỳ lúc nào mà không cần báo trước (kỳ hạn hợp đồng danh nghĩa là **qua đêm / overnight**). Tuy nhiên, về mặt hành vi kinh tế, phần lớn người gửi tiền duy trì một số dư ổn định để phục vụ giao dịch và tích lũy dài hạn.
* **Hậu quả nếu không mô hình hóa**: Nếu slot 100% CASA vào dải qua đêm, ngân hàng sẽ ghi nhận một khe hở tái định giá âm nghiêm trọng trong ngắn hạn ($\text{Gap} < 0$), dẫn đến quyết định phòng ngừa rủi ro sai lệch bằng cách mua các công cụ cố định ngắn hạn, làm triệt tiêu biên lãi ròng.
* **Quy trình mô hình hóa bắt buộc**:
  1. **Phân tách cấu trúc**:
     * **Tiền gửi phi lõi (Non-core deposits)**: Phần số dư biến động theo mùa vụ hoặc dòng tiền ngắn hạn của khách hàng $\rightarrow$ Bắt buộc phân bổ vào dải **qua đêm (Overnight)** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
     * **Tiền gửi lõi (Core deposits)**: Phần số dư ổn định bền vững qua nhiều chu kỳ lãi suất $\rightarrow$ Phân bổ vào các dải kỳ hạn trung và dài hạn.
  2. **Kỹ thuật Replicating Portfolio Model**:
     * Xây dựng danh mục đầu tư mô phỏng bao gồm các công cụ thanh khoản có kỳ hạn khác nhau sao cho diễn biến khối lượng và lợi suất của danh mục tái lập xấp xỉ sát thực tế hành vi kỳ vọng của sản phẩm phi kỳ hạn [[src-tata-bank-alm#^tata-nmd-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
     * Ước tính tỷ lệ rút vốn tự nhiên ([[run-off-rate|Run-off rate]]) để đo lường mức độ suy giảm số dư theo thời gian [[src-tata-bank-alm#^tata-nmd-2]].
  3. **Trần quy chuẩn giám sát theo Basel d368 (Table 2)** [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:
     * **Retail Transactional (Bán lẻ - Tài khoản giao dịch)**: Trần tiền gửi lõi tối đa **90%**; trần kỳ hạn bình quân gia quyền tối đa **5 năm** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
     * **Retail Non-transactional (Bán lẻ - Tài khoản phi giao dịch)**: Trần tiền gửi lõi tối đa **70%**; trần kỳ hạn bình quân gia quyền tối đa **4,5 năm** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
     * **Wholesale (Tiền gửi bán buôn)**: Trần tiền gửi lõi tối đa **50%**; trần kỳ hạn bình quân gia quyền tối đa **4 năm** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].

### 3.2. Cho Vay Lãi Suất Cố Định Chịu Rủi Ro Trả Nợ Trước Hạn (Prepayment Risk / Contraction Risk)

* **Xung đột thực tế**: Các khoản cho vay mua nhà thế chấp (mortgages) hoặc cho vay tiêu dùng dài hạn có lãi suất cố định. Hợp đồng cho phép người vay trả nợ trước hạn toàn bộ hoặc từng phần [[src-tata-bank-alm#^tata-opt-2]].
* **Cơ chế rủi ro**:
  * Khi **lãi suất thị trường giảm**: Khách hàng có động cơ tài chính mạnh mẽ để tái tài trợ (refinancing) ở mức lãi suất thấp hơn $\rightarrow$ Tốc độ trả trước tăng vọt $\rightarrow$ Dòng tiền vốn gốc bị hoàn trả sớm về ngân hàng và phải tái đầu tư vào môi trường lãi suất thấp (**Contraction Risk**) [[src-tata-bank-alm#^tata-opt-3]].
  * Khi **lãi suất thị trường tăng**: Khách hàng giữ chặt khoản vay lãi suất rẻ $\rightarrow$ Tốc độ trả trước sụt giảm $\rightarrow$ Kéo dài kỳ hạn thực tế của tài sản sinh lời thấp (**Extension Risk**).
  * Hiện tượng này tạo ra **độ lồi âm (*negative convexity*)**, làm sụt giảm nghiêm trọng giá trị kinh tế của ngân hàng (EVE).
* **Quy chuẩn mô hình hóa**:
  * Ước tính tỷ lệ trả nợ trước hạn có điều kiện (Conditional Prepayment Rate - CPR).
  * Theo chuẩn hóa Basel d368, tốc độ trả trước CPR được điều chỉnh theo hệ số nhân kịch bản $\gamma_i$: hệ số $\gamma_i = 1.2$ khi lãi suất giảm (tăng tốc trả trước) và $\gamma_i = 0.8$ khi lãi suất tăng (chậm trả trước) [[src-bcbs-irrbb-2016#^irrbb-u05-5]].

### 3.3. Tiền Gửi Có Kỳ Hạn Chịu Rủi Ro Rút Trước Hạn (Early Redemption Risk)

* **Xung đột thực tế**: Tiền gửi tiết kiệm có kỳ hạn cố định (ví dụ 12–24 tháng). Khách hàng có quyền tất toán trước ngày đáo hạn pháp lý và chịu phạt mất một phần tiền lãi tích lũy [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
* **Cơ chế rủi ro**: Khi lãi suất thị trường tăng vọt, phần chênh lệch lợi suất từ sản phẩm tiền gửi mới vượt qua chi phí phạt mất lãi $\rightarrow$ Khách hàng rút trước hạn để chuyển tiền sang kỳ hạn mới lãi suất cao hơn $\rightarrow$ Ngân hàng mất nguồn vốn chi phí rẻ, buộc phải huy động bù đắp ở mức chi phí vốn tăng cao.
* **Quy chuẩn mô hình hóa**:
  * Ước tính tỷ lệ rút tiền gửi có kỳ hạn trước hạn (Term Deposit Redemption Rate - TDRR).
  * Basel d368 quy định hệ số điều chỉnh kịch bản $u_i$: hệ số $u_i = 1.2$ khi lãi suất tăng (người gửi tiền đẩy mạnh rút trước hạn) và $u_i = 0.8$ khi lãi suất giảm [[src-bcbs-irrbb-2016#^irrbb-u05-6]].

### 3.4. Rủi Ro Đường Ống Cam Kết Cho Vay (Pipeline Risk / Loan Commitments)

* **Xung đột thực tế**: Ngân hàng ký cam kết cấp tín dụng hoặc khóa lãi suất cho vay cố định (rate-lock commitment) trong vòng 30 đến 90 ngày trước khi tiến hành giải ngân thực tế.
* **Cơ chế rủi ro**:
  * Nếu **lãi suất tăng**: Khách hàng tranh thủ giải ngân tối đa hạn mức đã khóa lãi suất rẻ $\rightarrow$ Tỷ lệ giải ngân thực tế (*Drawdown / Take-up rate*) tăng tiệm cận 100%.
  * Nếu **lãi suất giảm**: Khách hàng từ bỏ cam kết để tiếp cận các khoản vay rẻ hơn từ đối thủ $\rightarrow$ Tỷ lệ giải ngân thực tế sụt giảm mạnh.
* **Mô hình hóa**: Phải xây dựng hàm xác suất giải ngân động phụ thuộc vào chênh lệch giữa lãi suất cam kết và lãi suất thị trường hiện hành [cần nguồn].

### 3.5. Lãi Suất Tiền Gửi Điều Hành (Administered Rate Deposits & Deposit Beta)

* **Xung đột thực tế**: Các sản phẩm tiền gửi tiết kiệm có lãi suất do ngân hàng tự niêm yết (administered rates). Ngân hàng có quyền quyết định thời điểm và biên độ điều chỉnh lãi suất này thay vì tự động điều chỉnh theo chỉ số chuẩn như SOFR/Euribor.
* **Cơ chế rủi ro**: Tốc độ và biên độ điều chỉnh lãi suất huy động niêm yết thường có độ trễ và không dịch chuyển 1:1 với lãi suất thị trường.
* **Mô hình hóa**:
  * Ước tính hệ số truyền dẫn lãi suất (Deposit Beta / Pass-through Rate - PTR) [cần nguồn]:
    $$\beta = \frac{\Delta r_{\text{deposit}}}{\Delta r_{\text{market}}}$$
  * Mô hình hóa tính chất bất đối xứng: Ngân hàng có xu hướng tăng lãi suất huy động chậm khi thị trường tăng, nhưng giảm lãi suất huy động nhanh khi thị trường giảm (hoặc ngược lại tùy áp lực cạnh tranh thị phần).

---

## 4. Phân Định Bản Chất: Automatic Options Vs Behavioral Options (Fidelio Tata & Basel d368)

Mô hình hóa hành vi chỉ áp dụng cho quyền chọn hành vi, tuyệt đối không được áp dụng lẫn lộn với quyền chọn tự động [[src-tata-bank-alm#^tata-opt-1]].

```
                                  ┌──────────────────────────────────────────────┐
                                  │      PHÂN LOẠI QUYỀN CHỌN LÃI SUẤT           │
                                  └──────────────────────┬───────────────────────┘
                                                         │
                    ┌────────────────────────────────────┴────────────────────────────────────┐
                    ▼                                                                         ▼
     ┌──────────────────────────────┐                                          ┌──────────────────────────────┐
     │      AUTOMATIC OPTIONS       │                                          │      BEHAVIORAL OPTIONS      │
     ├──────────────────────────────┤                                          ├──────────────────────────────┤
     │ • Caps, Floors, Swaptions    │                                          │ • Prepayment, Early Exit,    │
     │ • Thực thi hoàn toàn duy lý  │                                          │   CASA Core Profile          │
     │ • 100% In-the-money          │                                          │ • Chịu chi phối nhân khẩu học│
     │ • Định giá: Black-76, HW     │                                          │ • Có thể phi lý tài chính    │
     │ • Bóc tách khỏi dòng tiền gốc│                                          │ • Co ngắn kỳ hạn kỳ vọng     │
     └──────────────────────────────┘                                          └──────────────────────────────┘
```

| Đặc điểm | Automatic Options (Quyền chọn tự động) | Behavioral Options (Quyền chọn hành vi) |
| :--- | :--- | :--- |
| **Công cụ đại diện** | Lãi suất trần (Caps), lãi suất sàn (Floors), quyền chọn hoán đổi (Swaptions) [[src-tata-bank-alm#^tata-opt-1]]. | Trả nợ trước hạn (Prepayment), rút tiền gửi sớm (Early redemption), số dư CASA [[src-tata-bank-alm#^tata-opt-2]]. |
| **Tính duy lý kinh tế** | **Hoàn toàn duy lý tài chính (*100% rational*)**: Quyền chọn luôn được thực thi ngay khi rơi vào trạng thái có lãi (*in-the-money*) và không bao giờ thực hiện khi lỗ (*out-of-the-money*) [[src-tata-bank-alm#^tata-opt-4]]. | **Chi phối bởi các yếu tố phi tài chính và nhân khẩu học (*demographic factors*)**: Tử vong, ly hôn, chuyển nhà, mất việc làm [[src-tata-bank-alm#^tata-opt-4]]. |
| **Hành vi phi tối ưu** | Không bao giờ xảy ra [[src-tata-bank-alm#^tata-opt-4]]. | **Có thể thực thi ngay cả khi out-of-the-money** (ví dụ bán nhà tất toán khoản vay lãi suất rẻ sau ly hôn), hoặc không thực thi dù in-the-money (do lười biếng, thiếu thông tin) [[src-tata-bank-alm#^tata-opt-4]]. |
| **Xử lý trong Bảng cân đối định giá lại** | **Bóc tách hoàn toàn khỏi dòng tiền cơ sở**: Quyền chọn tự động được định giá riêng biệt bằng mô hình Black-76 hoặc Hull-White để tính cấu phần gia tăng rủi ro $\text{KAO}_{i,c}$ [[src-bcbs-irrbb-2016#^irrbb-u05-3]] [[src-bcbs-irrbb-2016#^irrbb-u05-7]]. | **Tích hợp trực tiếp vào lịch dòng tiền**: Điều chỉnh kỳ hạn và khối lượng dòng tiền tái định giá trong từng dải kỳ hạn [[src-tata-bank-alm#^tata-opt-3]]. |
| **Ranh giới Retail vs Wholesale theo Basel d368** | Áp dụng bắt buộc cho mọi nhóm khách hàng [[src-bcbs-irrbb-2016#^irrbb-u05-3]]. | **Chỉ áp dụng mô hình hành vi cho Retail và Small Business**. Với khách hàng Wholesale (doanh nghiệp lớn, định chế tài chính), mọi quyền chọn nhúng bắt buộc phải xử lý theo **Automatic Option Logic** (giả định khách hàng thực hiện quyền chọn theo kịch bản gây bất lợi tài chính lớn nhất cho ngân hàng) [[src-bcbs-irrbb-2016#^irrbb-u05-4]]. |

---

## 5. Ma Trận Phân Bổ Repricing Profile Cho Toàn Bộ Bảng Cân Đối ALM

Dưới đây là ma trận chuẩn hóa phân loại toàn bộ các khoản mục nội bảng và ngoại bảng vào 3 cơ chế xác định Repricing Profile:

| Nhóm danh mục | Khoản mục cụ thể | Cơ chế Repricing Profile áp dụng | Căn cứ kỹ thuật & Lưu ý mô hình |
| :--- | :--- | :--- | :--- |
| **Tài sản (Assets)** | Cho vay thế chấp mua nhà lãi suất cố định | **Behavioral Maturity** | Mô hình hóa tốc độ trả nợ trước hạn (CPR). Co ngắn kỳ hạn thực tế khi lãi suất giảm [[src-tata-bank-alm#^tata-opt-3]]. |
| | Cho vay mua nhà / tiêu dùng thả nổi | **Next Repricing Date** | Slot vào ngày Reset Date kế tiếp theo chỉ số tham chiếu [[src-tata-bank-alm#^tata-gap-1]] [[src-tata-bank-alm#^tata-opt-2]]. |
| | Cho vay doanh nghiệp lớn cố định có phí phạt phá vỡ | **Contractual Maturity** | Phí phạt triệt tiêu động cơ trả trước $\rightarrow$ Slot theo lịch hoàn trả hợp đồng [[src-tata-bank-alm#^tata-gap-1]]. |
| | Cho vay doanh nghiệp thả nổi định kỳ | **Next Repricing Date** | Slot vào ngày Reset Date kế tiếp (1M, 3M, 6M) [[src-tata-bank-alm#^tata-gap-1]] [[src-tata-bank-alm#^tata-gap-2]]. |
| | Trái phiếu Chính phủ / Doanh nghiệp cố định | **Contractual Maturity** | Slot theo ngày đáo hạn gốc hoặc dòng coupon/gốc định kỳ [[src-tata-bank-alm#^tata-gap-1]]. |
| | Trái phiếu thả nổi (FRNs) | **Next Repricing Date** | Slot vào ngày coupon reset kế tiếp [[src-tata-bank-alm#^tata-gap-2]]. |
| | Tài sản cố định, Bất động sản, Vốn góp | **Loại trừ khỏi IRRBB** | Không nhạy cảm lãi suất, được loại trừ khỏi phân tích NII/EVE [[src-tata-bank-alm#^tata-nii-5]]. |
| **Nợ phải trả (Liabilities)** | Tiền gửi không kỳ hạn & thanh toán (CASA) | **Behavioral Maturity** | Tách Non-core (Overnight) và Core (Replicating Portfolio tối đa 5 năm) [[src-bcbs-irrbb-2016#^irrbb-u05-4]]. |
| | Tiền gửi tiết kiệm kỳ hạn bán lẻ có quyền rút sớm | **Behavioral Maturity** | Mô hình hóa tỷ lệ rút trước hạn (TDRR) theo chênh lệch lãi suất [[src-bcbs-irrbb-2016#^irrbb-u05-6]]. |
| | Tiền gửi kỳ hạn bán buôn khóa chặt | **Contractual Maturity** | Không cho phép rút trước $\rightarrow$ Slot theo ngày đáo hạn hợp đồng [[src-tata-bank-alm#^tata-gap-1]]. |
| | Tiền gửi kỳ hạn bán buôn có quyền rút trước | **Tương đương Automatic** | Giả định rút ngay tại cơ hội đầu tiên gây bất lợi nhất cho ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u05-4]]. |
| | Vay liên ngân hàng thả nổi | **Next Repricing Date** | Slot theo chu kỳ điều chỉnh lãi suất kế tiếp [[src-tata-bank-alm#^tata-gap-2]]. |
| | Giấy tờ có giá cố định do ngân hàng phát hành | **Contractual Maturity** | Slot theo ngày đáo hạn hoặc lịch mua lại bắt buộc [[src-tata-bank-alm#^tata-gap-1]]. |
| | Vốn chủ sở hữu kế toán (Accounting Equity) | **Loại trừ khỏi IRRBB** | EVE đo lường giá trị kinh tế của vốn nên vốn kế toán được loại trừ khỏi dòng tiền chiết khấu [[src-tata-bank-alm#^tata-nii-5]]. |
| **Ngoại bảng (Off-Balance Sheet)** | Hợp đồng hoán đổi lãi suất (IRS) - Chân nhận cố định | **Contractual Maturity** | Slot toàn bộ dòng tiền nhận cố định theo kỳ hạn hợp đồng hoán đổi [[src-tata-bank-alm#^tata-nii-15]]. |
| | Hợp đồng hoán đổi lãi suất (IRS) - Chân trả thả nổi | **Next Repricing Date** | Slot số dư danh nghĩa vào ngày reset thả nổi kế tiếp [[src-tata-bank-alm#^tata-nii-15]]. |
| | Cam kết cấp tín dụng / Khóa lãi suất (Rate-lock) | **Behavioral Maturity** | Mô hình hóa tỷ lệ giải ngân thực tế (Take-up rate) động theo lãi suất [cần nguồn]. |
| | Quyền chọn trần/sàn lãi suất (Caps/Floors nhúng) | **Automatic Option** | Bóc tách riêng để định giá phi tuyến ($\text{KAO}_{i,c}$), không đưa vào slotting [[src-bcbs-irrbb-2016#^irrbb-u05-3]]. |

---

## 6. Khuyến Nghị Chiến Lược Cho Ủy Ban Quản Lý Tài Sản Nợ - Tài Sản Có (ALCO)

1. **Quản trị rủi ro mô hình hành vi (Behavioral Model Risk)**:
   * Giả định hành vi khách hàng là nguồn gốc rủi ro mô hình lớn nhất trong IRRBB hiện đại. Khi lãi suất đảo chiều từ mức thấp lịch sử sang mức cao kỷ lục, các giả định về độ bám dính của CASA hoặc tốc độ trả nợ trước hạn CPR thường bị gãy đổ cấu trúc (*structural break*).
   * ALCO phải yêu cầu bộ phận Quản lý rủi ro thực hiện kiểm định ngược (**Backtesting**) định kỳ hàng quý giữa hành vi rút vốn thực tế và giả định mô hình.
2. **Kỷ luật áp dụng trần quy định (Regulatory Caps)**:
   * Tuyệt đối tuân thủ các trần tỷ lệ tiền gửi lõi (Core caps) và trần kỳ hạn bình quân gia quyền của Basel d368 (Table 2) [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
   * Ngăn chặn hiện tượng ban điều hành lạc quan quá mức về tính ổn định của CASA để giả định kỳ hạn bình quân kéo dài 7–10 năm nhằm che giấu rủi ro sụt giảm [[economic-value-of-equity|∆EVE]].
3. **Phòng ngừa rủi ro kết hợp (Dynamic Hedging)**:
   * Do quyền chọn hành vi không thể phòng hộ hoàn hảo bằng các công cụ phái sinh chuẩn hóa (swaptions) vì tính chất phi duy lý nhân khẩu học [[src-tata-bank-alm#^tata-opt-4]], ALCO cần kết hợp giữa phòng hộ phái sinh vĩ mô và điều chỉnh chính sách định giá chuyển vốn nội bộ ([[ftp-pricing-methodology|FTP]]) nhằm định hướng hành vi khách hàng ở cấp độ bán lẻ.

---

## Bằng chứng ủng hộ

- **Ủy ban Basel (BCBS d368)**: Khung chuẩn hóa quy định bắt buộc phải ánh xạ dòng tiền tái định giá danh nghĩa vào 19 dải kỳ hạn chuẩn hóa hoặc điểm giữa dải kỳ hạn [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. Đồng thời, chuẩn mực thiết lập các trần giám sát nghiêm ngặt cho tiền gửi không kỳ hạn (Table 2) [[src-bcbs-irrbb-2016#^irrbb-u05-4]], hệ số nhân kịch bản $\gamma_i$ cho tỷ lệ trả trước CPR [[src-bcbs-irrbb-2016#^irrbb-u05-5]], và hệ số $u_i$ cho tỷ lệ rút tiền gửi sớm TDRR [[src-bcbs-irrbb-2016#^irrbb-u05-6]].
- **Fidelio Tata (2025)**: Phân tích cơ sở toán học chứng minh rằng tại ngày tái định giá (reset date), giá trị hiện tại của công cụ thả nổi quay về ngang mệnh giá ($PV = Par$), do đó rủi ro lãi suất chỉ tồn tại đến ngày reset date tiếp theo chứ không phải ngày đáo hạn hợp đồng [[src-tata-bank-alm#^tata-gap-2]]. Đồng thời, Tata chỉ rõ bản chất quyền chọn hành vi chịu tác động phi lý tài chính do nhân khẩu học [[src-tata-bank-alm#^tata-opt-4]], đòi hỏi phải tích hợp trực tiếp vào lịch dòng tiền thay vì bóc tách định giá như quyền chọn tự động [[src-tata-bank-alm#^tata-opt-3]].

---

## Bằng chứng trái chiều

- Không ghi nhận mâu thuẫn giữa BCBS d368 và Fidelio Tata về nguyên lý phân bổ kỳ hạn và phân loại rủi ro quyền chọn.
- Khác biệt nằm ở phạm vi ứng dụng: Basel d368 đặt ra các trần tham số giám sát cố định thận trọng (Table 2: trần core 50%–90%, trần kỳ hạn 4–5 năm) [[src-bcbs-irrbb-2016#^irrbb-u05-4]], trong khi giáo trình của Tata khuyến khích ngân hàng sử dụng mô hình tối ưu hóa thống kê nội bộ (Replicating Portfolio) để phản ánh sát nhất chu kỳ kinh doanh thực tế [[src-tata-bank-alm#^tata-nmd-3]].

---

## Phụ thuộc regime

- **Môi trường lãi suất thấp và ổn định**: Tiền gửi không kỳ hạn (CASA) có xu hướng bám dính cao do chênh lệch lãi suất với tiền gửi kỳ hạn không đáng kể. Tỷ lệ trả trước CPR đối với các khoản vay cố định cũ tăng cao khi khách hàng tái tài trợ [[src-tata-bank-alm#^tata-opt-3]].
- **Môi trường lãi suất tăng nhanh và biến động mạnh (Regime shift)**: Khách hàng có xu hướng dịch chuyển mạnh số dư CASA sang tiền gửi có kỳ hạn hoặc rút vốn trước hạn để tái đầu tư với lãi suất cao hơn [[src-bcbs-irrbb-2016#^irrbb-u05-6]]. Các tham số bám dính ước tính trong giai đoạn bình thường dễ bị gãy đổ cấu trúc (*structural break*), gây rủi ro mô hình nghiêm trọng cho ALCO.

---

## Hàm ý ALM / quy định

- **Hàm ý cho ALCO và Treasury**:
  - Không thể triệt tiêu đồng thời cả rủi ro giá trị kinh tế (EVE) và rủi ro thu nhập (NII). Nếu điều chỉnh bảng cân đối sang thả nổi ngắn hạn theo reset date để triệt tiêu $\Delta\text{EVE}$, ngân hàng sẽ gánh chịu biến động thu nhập lãi thuần $\Delta\text{NII}$ nghiêm trọng khi lãi suất thị trường thay đổi [[src-bcbs-irrbb-2016#^irrbb-u02-4]].
  - ALCO cần kết hợp phòng ngừa rủi ro phái sinh vĩ mô với chính sách định giá chuyển vốn nội bộ ([[ftp-pricing-methodology|FTP]]) nhằm phản ánh chi phí quyền chọn hành vi (Prepayment/CASA Core) vào biểu lãi suất kinh doanh bán lẻ.
- **Quy định pháp lý tại Việt Nam**:
  - [[tt83-2025]] có hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]]. Chiến lược IRRBB phải gồm nguyên tắc quản lý theo trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile), tức chênh lệch tài sản và nợ phải trả nhạy cảm với lãi suất theo thời điểm ấn định lãi suất mới hoặc định giá lại [[src-tt83-2025-nhnn#^d53-1a1]].
  - Khi không xác định được thời gian đáo hạn hoặc thời điểm ấn định lãi suất mới, ngân hàng có thể dùng giả định; giả định phải được cấp có thẩm quyền phê duyệt [[src-tt83-2025-nhnn#^d54-4a]]. Giả định và thay đổi giả định cần được ghi nhận, lưu trữ [[src-tt83-2025-nhnn#^d54-3d]].
  - NMDs phân loại theo cá nhân (giao dịch / không giao dịch) và tổ chức; NMDs lõi trong trần 90%/5 năm, 70%/4,5 năm, 50%/4 năm [[src-tt83-2025-nhnn#^pl5-a2-3a]]. Quản lý rủi ro mô hình thuộc C3-M8 `[cần nguồn: src-tt83-2025-nhnn C3-M8]`.
  - *Diễn giải:* Các quy định của BCBS d368 hiện là chuẩn mực tham chiếu quốc tế; khi áp dụng tại Việt Nam, ngân hàng cần tuân thủ các quy định bắt buộc của NHNN trước khi áp dụng các thông lệ nâng cao của Basel.

---

## Bất định

- Dải kỳ hạn [[src-tt83-2025-nhnn#^pl5-a2-t1]], trần CASA lõi [[src-tt83-2025-nhnn#^pl5-a2-3a]] và yêu cầu repricing gap profile [[src-tt83-2025-nhnn#^d53-1a1]] đã có nguồn NHNN [2026-10-19]. Còn thiếu: tiêu chuẩn mô hình hành vi (C3-M8) `[cần nguồn: src-tt83-2025-nhnn C3-M8]`.
- Mức độ nhạy cảm của rủi ro đường ống cam kết cho vay (Pipeline risk) và hệ số Deposit Beta trên thị trường ngân hàng Việt Nam phụ thuộc vào cấu trúc cạnh tranh và trần lãi suất huy động của NHNN từng thời kỳ.

---
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại các đoạn về dòng tiền tái định giá và citation par 101–106.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.

## Liên Kết Quan Hệ
- **Đầu vào cho**: [[repricing-balance-sheet]], [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[irrbb-standardised-shocks-eve-and-nii-measurement]]
- **Khái niệm thành phần**: [[non-maturity-deposits]], [[behavioural-options]], [[option-risk]], [[gap-risk]], [[run-off-rate]]
- **Mô hình triển khai**: [[replicating-portfolio-model]], [[duration-gap-model]]
- **Chuẩn mực giám sát**: [[bcbs-irrbb]], [[standardised-interest-rate-shocks]]
- **Nguồn trích dẫn**: [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]]

