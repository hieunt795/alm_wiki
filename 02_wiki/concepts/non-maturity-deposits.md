---
title: "Non-Maturity Deposits (NMDs — Tiền gửi không kỳ hạn trong IRRBB)"
aliases: [NMDs, Tiền gửi không kỳ hạn, Non-Maturity Deposits, Core Deposits, Replicating Portfolio]
type: concept
domains: [alm, product, basel, vn-reg]
status: active
maturity: canonical
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-lubinska-alm-optimisation]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-4]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-6]]"}
  - {type: hedges, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-6]]"}
  - {type: input-to, to: "[[repricing-balance-sheet]]", cite: "[[src-tata-bank-alm#^tata-gap-1]]"}
tags: [irrbb, nmd, core-deposits, replicating-portfolio, behavioural-modelling, basel]
updated: 2026-10-19
reviewed:
---

## Định nghĩa & Bản chất Kinh tế
Tiền gửi không kỳ hạn (Non-Maturity Deposits - NMDs) là các khoản nợ phải trả của ngân hàng mà người gửi tiền có quyền rút ra bất kỳ lúc nào mà không có ngày đáo hạn hay kỳ tái định giá theo hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u06-6]]. Theo Tiến sĩ Fidelio Tata, sản phẩm phi kỳ hạn được định nghĩa là các vị thế mà **kỳ hạn hành vi (behavioral maturity) khác biệt với kỳ hạn hợp đồng (contractual maturity)** hoặc không có kỳ hạn hợp đồng xác định [[src-tata-bank-alm#^tata-nmd-1]]. NMDs bao gồm tiền gửi thanh toán (current accounts/CASA), tiền gửi tiết kiệm không kỳ hạn và các tài khoản vãng lai.

Dưới góc độ quản trị ALM, NMDs mang đặc tính kép:
1. **Hợp đồng pháp lý ngắn hạn**: Theo hợp đồng, tiền gửi có thể rút ngay trong ngày ($\text{Tenor} = 0$, kỳ hạn qua đêm).
2. **Hành vi thực tế dài hạn và ổn định**: Trong điều kiện kinh doanh bình thường, phần lớn người gửi tiền duy trì số dư tối thiểu để chi tiêu hoặc giao dịch thường xuyên. Các khoản rút ra được bù đắp bởi các khoản gửi vào mới từ khách hàng khác, tạo nên một cơ số tiền gửi bám dính (*sticky core balance*) ổn định và có chi phí vốn cực thấp [[src-bcbs-irrbb-2016#^irrbb-u06-6]]. Quá trình suy giảm tiền gửi trong các tài khoản hiện hữu theo thời gian được đo lường bằng tỷ lệ rút vốn tự nhiên (*run-off rate*) [[src-tata-bank-alm#^tata-nmd-2]].

Việc giả định NMDs là nợ qua đêm (overnight) hay là nợ dài hạn có tác động mang tính quyết định lên mức phơi lượng rủi ro lãi suất của ngân hàng dưới cả hai thước đo [[economic-value-of-equity|$\Delta\text{EVE}$]] và [[net-interest-income-sensitivity|$\Delta\text{NII}$]] [[src-bcbs-irrbb-2016#^irrbb-p05-2]] [[src-tata-bank-alm#^tata-opt-3]]. Do đó, các ngân hàng sử dụng [[replicating-portfolio-model|Mô hình danh mục tái lập (Replicating Portfolio Model)]] để xấp xỉ kỳ hạn và diễn biến lãi suất thực tế của NMDs bằng một danh mục công cụ tài chính thanh khoản có kỳ hạn xác định [[src-tata-bank-alm#^tata-nmd-3]].

## Phân đoạn và Quy chuẩn Basel (d368 Section IV)

Chuẩn mực [[bcbs-irrbb]] quy định quy trình chuẩn hoá 2 bước để xử lý NMDs:

### Bước 1: Phân đoạn khách hàng (Customer Segmentation)
NMDs bắt buộc phải được chia tách thành các phân khúc độc lập [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:
- **Tiền gửi Bán lẻ Giao dịch (Retail / Transactional)**: Tiền gửi của cá nhân hoặc doanh nghiệp nhỏ (dư nợ $< 1$ triệu EUR) được sử dụng để giao dịch định kỳ (như tài khoản nhận lương, thanh toán hoá đơn thường xuyên) hoặc tài khoản không hưởng lãi.
- **Tiền gửi Bán lẻ Phi giao dịch (Retail / Non-transactional)**: Tiền gửi của cá nhân mang tính chất tiết kiệm, không phát sinh giao dịch chi tiêu hàng ngày thường xuyên.
- **Tiền gửi Bán buôn (Wholesale)**: Tiền gửi không kỳ hạn từ các định chế tài chính, doanh nghiệp lớn, công ty hợp danh.

### Bước 2: Tách Tiền gửi Ổn định và Tiền gửi Lõi (Core vs Non-Core Deposits)
Dựa trên chuỗi số liệu quan sát biến động số dư trong **tối thiểu 10 năm lịch sử** [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:
- **Tiền gửi Ổn định (Stable NMDs)**: Phần số dư có xác suất rất cao sẽ không bị rút ra trong các điều kiện thị trường biến động.
- **Tiền gửi Lõi (Core Deposits)**: Là tỷ lệ tiền gửi ổn định mà ngân hàng đánh giá là **không có khả năng tái định giá ngay cả khi môi trường lãi suất thị trường thay đổi đáng kể** (tức là lãi suất trả cho khách hàng hầu như không tăng ngay cả khi lãi suất điều hành tăng mạnh) [[src-bcbs-irrbb-2016#^irrbb-p05-2]]. Phân tích biến động số dư bóc tách tiền gửi thành phần lõi (core) duy trì dưới hầu hết điều kiện và phần phi lõi (non-core) biến động ngắn hạn theo yếu tố đặc thù hoặc vĩ mô [[src-lubinska-alm-optimisation#^lubinska-u04-5]].
- **Tiền gửi Phi lõi (Non-Core Deposits)**: Toàn bộ phần số dư còn lại ngoài tiền gửi lõi.

### Phương pháp Định lượng Core vs Non-Core theo Beata Lubinska
Beata Lubinska (2020) tổng kết hai phương pháp lượng hóa thực tế tại các ngân hàng Châu Âu [[src-lubinska-alm-optimisation#^lubinska-u04-5]]:
1. **Mô hình Tăng trưởng Hàm Mũ (Exponential Fit Model)**:
   - Số dư tiền gửi được khớp theo đường cong tăng trưởng hàm mũ. Để đảm bảo độ thận trọng, đường xu hướng được hạ thấp một biên độ bằng $3.1$ lần độ lệch chuẩn ($3.1\sigma$), tương ứng mức độ tin cậy 99.9% theo phân phối chuẩn [[src-lubinska-alm-optimisation#^lubinska-u04-6]].
   - Biên độ này bảo đảm xác suất tổng số dư rơi xuống dưới mức lõi chỉ xảy ra $0.1\%$ thời gian (tương đương 1 tháng trong mỗi 83 năm) [[src-lubinska-alm-optimisation#^lubinska-u04-6]].
   - Tỷ lệ lõi (%) được chuyển hóa thành số dư tiền tệ tuyệt đối: nếu số dư đang giảm thì nhân với số dư tháng gần nhất; nếu số dư đang tăng thì nhân với số dư bình quân 12 tháng để duy trì tính thận trọng.
2. **Mô hình Biến động Tháng (Monthly Volatility Model)**:
   - Tính toán chuỗi tỷ lệ biến động số dư tương đối hàng tháng và sắp xếp theo thứ tự giảm dần. Mức sụt giảm số dư tồi tệ nhất ở phân vị thứ 95 (95th percentile worst decline over 1 month) được chọn đại diện cho dòng tiền rút ra trong 1 tháng tại mức tin cậy 95% [[src-lubinska-alm-optimisation#^lubinska-u04-7]].
   - Tỷ lệ phi lõi (non-core %) được quy năm bằng cách nhân độ biến động tháng với căn bậc hai của 12: $\text{Non-core} \% = \text{MV} \times \sqrt{12}$. Tỷ lệ tiền gửi lõi là phần bù còn lại: $\text{Core} \% = 100\% - \text{Non-core} \%$ [[src-lubinska-alm-optimisation#^lubinska-u04-7]].
3. **Cấu trúc Hồ sơ Lãi suất CASA trong FTP**:
   - Hồ sơ lãi suất CASA luôn bao gồm hai cấu phần: phần biến động được mô hình hóa tái định giá trên cơ sở qua đêm (O/N) theo chuẩn BCBS d368, và phần ổn định được coi là nhạy cảm theo thị trường hoặc phần lõi phi nhạy cảm lãi suất đóng vai trò nguồn vốn dài hạn lãi suất 0% [[src-lubinska-alm-optimisation#^lubinska-u04-1]].

## Bảng Trần Khống chế Chuẩn hoá của Basel (Table 2)

Nhằm ngăn chặn các ngân hàng lạm dụng giả định mô hình hành vi (tự ý kéo dài kỳ hạn NMDs để che giấu rủi ro EVE), Chuẩn mực Basel d368 thiết lập các trần khống chế nghiêm ngặt [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:

| Phân loại NMDs | Trần Tỷ lệ Tiền gửi Lõi (Cap on Core %) | Trần Kỳ hạn Bình quân của Tiền gửi Lõi (Cap on Average Maturity) | Xử lý Dòng tiền Tái định giá |
|---|---|---|---|
| **Bán lẻ / Giao dịch (Retail Transactional)** | **$\le 90\%$** tổng số dư | **$\le 5,0$ năm** | Phân bổ vào 19 dải kỳ hạn sao cho kỳ hạn bình quân $\le 5$ năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| **Bán lẻ / Phi giao dịch (Retail Non-transactional)** | **$\le 70\%$** tổng số dư | **$\le 4,5$ năm** | Phân bổ vào 19 dải kỳ hạn sao cho kỳ hạn bình quân $\le 4,5$ năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| **Bán buôn (Wholesale Deposits)** | **$\le 50\%$** tổng số dư | **$\le 4,0$ năm** | Phân bổ vào 19 dải kỳ hạn sao cho kỳ hạn bình quân $\le 4$ năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| **Tiền gửi Phi lõi (Non-Core Deposits)** | Phần thặng dư ($10\% - 50\%$) | **Qua đêm (Overnight)** | **Bắt buộc phân bổ 100% vào dải kỳ hạn qua đêm (k = 1)** [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |

## Kỹ thuật Quản trị: Danh mục Tái lập (Replicating Portfolio)

Để quản lý rủi ro biến động thu nhập từ nguồn NMDs lõi mà không gây bất ổn cho bảng cân đối, ALM Treasury sử dụng [[replicating-portfolio-model|Mô hình Danh mục Tái lập (Replicating Portfolio Model)]] [[src-bcbs-irrbb-2016#^irrbb-u06-6]]:
- **Cơ chế hoạt động**: Treasury xây dựng một danh mục tài sản đầu tư cố định dài hạn (ví dụ trái phiếu chính phủ hoặc hợp đồng [[interest-rate-swap|Receiver IRS]]) đầu tư cuốn chiếu đều đặn. 
- **Ví dụ chuẩn Basel**: Tái đầu tư $1/60$ tổng danh mục mỗi tháng vào trái phiếu cố định kỳ hạn 5 năm. Danh mục này sẽ tạo ra một cấu trúc kỳ hạn bình quân ổn định là **2,5 năm**, và mang lại mức lợi suất bằng trung bình trượt (*moving average*) của lãi suất 5 năm trong 60 tháng qua [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
- **Hóa giải mâu thuẫn**: Danh mục tái lập triệt tiêu hoàn toàn sự biến động của thu nhập lãi thuần $\Delta\text{NII}$ trước các biến động lãi suất ngắn hạn, biến nguồn NMDs thành một bệ đỡ thu nhập ổn định (*endowment return*). Chi tiết thuật toán tối ưu hóa xem tại [[replicating-portfolio-model]].

## Đánh đổi ALM và Rủi ro Thanh khoản
1. **Rủi ro EVE khi kéo dài thời lượng NMDs**: Nếu Treasury gán kỳ hạn hành vi cho NMDs quá dài (ví dụ tối đa 5 năm) để đầu tư vào tài sản dài hạn, khi xảy ra cú sốc tăng lãi suất đột ngột, giá trị kinh tế của danh mục tài sản sẽ sụt giảm mạnh, trong khi NMDs trên thực tế có thể bị rút ra nhanh hơn mô hình dự tính (hiện tượng *deposit run* như Silicon Valley Bank năm 2023).
2. **Deposit Beta và Độ nhạy Lãi suất**: Trong môi trường lãi suất cao kéo dài, khách hàng dần nhận thức về chi phí cơ hội và chuyển dịch từ CASA sang tiền gửi có kỳ hạn hoặc quỹ thị trường tiền tệ, làm xói mòn tỷ lệ tiền gửi lõi và đè bẹp tỷ lệ thu nhập lãi thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]].
3. **Mối liên hệ với [[nsfr]]**: Tiền gửi NMDs bán lẻ stable được nhận hệ số ASF lên tới 95%, cung cấp nguồn vốn ổn định dài hạn giá rẻ để tài trợ cho tài sản sinh lời.
4. **Bất đối xứng độ nhạy hành vi trong tối ưu hóa ALM**: Nghiên cứu thực nghiệm của Beata Lubinska (2020) chỉ ra rằng độ nhạy của bảng cân đối và chi phí huy động vốn trước các giả định hành vi bên nợ phải trả (độ biến động và độ nhạy lãi suất CASA) cao hơn đáng kể so với các giả định hành vi bên tài sản (tỷ lệ trả nợ trước hạn CPR) [[src-lubinska-alm-optimisation#^lubinska-u06-10]].
5. **Rủi ro mô hình tiềm ẩn (Embedded Model Risk) và Hiệu ứng Quy mô**: Tại các ngân hàng có 100% nợ phải trả hợp đồng kỳ hạn dưới 1 năm (như Ngân hàng 2 của Lubinska), bảng cân đối chịu rủi ro mô hình tiềm ẩn trọng yếu từ mô hình đặc tính hóa CASA [[src-lubinska-alm-optimisation#^lubinska-u06-12]]. Tuy nhiên, ở các ngân hàng lớn với cơ cấu huy động và tài sản đa dạng hóa cao, tác động của biến động giả định CASA đơn lẻ có xu hướng suy giảm và được hấp thụ tốt hơn so với ngân hàng nhỏ [[src-lubinska-alm-optimisation#^lubinska-u06-14]].
- Xem thêm tại [[option-risk]], [[gap-risk]], [[economic-value-of-equity]], [[integrated-alm-liquidity-strategy]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[balance-sheet-optimisation-model]], [[model-risk-management]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Phân loại | Retail transactional, retail non-transactional, wholesale [[src-bcbs-irrbb-2016#^irrbb-u05-4]] | Tiền gửi cá nhân (tài khoản giao dịch / không giao dịch), tiền gửi tổ chức [[src-tt83-2025-nhnn#^pl5-a2-3a]] | d368 par 114; TT83 PL5.A.II.3.a | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Trần lõi, kỳ hạn TB — giao dịch cá nhân | 90%, 5 năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] | 90%, 5 năm [[src-tt83-2025-nhnn#^pl5-a2-3a]] | Table 2; TT83 Bảng 2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Trần lõi, kỳ hạn TB — không giao dịch cá nhân | 70%, 4,5 năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] | 70%, 4,5 năm [[src-tt83-2025-nhnn#^pl5-a2-3a]] | Table 2; TT83 Bảng 2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Trần lõi, kỳ hạn TB — tổ chức | 50%, 4 năm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] | 50%, 4 năm [[src-tt83-2025-nhnn#^pl5-a2-3a]] | Table 2; TT83 Bảng 2 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| NMDs không lõi | Thang qua đêm [[src-bcbs-irrbb-2016#^irrbb-u05-4]] | Thang qua đêm [[src-tt83-2025-nhnn#^pl5-a2-3a]] | d368 par 114; TT83 PL5.A.II.3.a(iii) | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |

Khác biệt: [[tt83-2025]] dùng nhãn "cá nhân / tổ chức" thay "retail / wholesale"; giá trị trần giống d368.

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 — user duyệt [2026-10-19]: thêm dòng VN. PL5 phân loại NMDs thành tiền gửi cá nhân (tài khoản giao dịch / không giao dịch) và tiền gửi tổ chức; tách NMDs ổn định bằng dữ liệu lịch sử, NMDs lõi lấy từ phần ổn định; trần Bảng 2 là 90%/5 năm, 70%/4,5 năm, 50%/4 năm (giống Table 2 d368); NMDs không lõi vào thang qua đêm [[src-tt83-2025-nhnn#^pl5-a2-3a]]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 (bổ sung) — chờ user duyệt: thêm vào dòng VN hoặc dòng "Khác biệt": PL5 định nghĩa NMDs ổn định là NMDs có khả năng cao khách hàng sẽ duy trì; NMDs lõi lấy từ phần ổn định; NMDs không lõi là phần còn lại; NMDs lõi được phân bổ sao cho đáp ứng Bảng 2 [[src-tt83-2025-nhnn#^pl5-a2-3a2]].
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M8 — chờ user duyệt: thêm góc nhìn VN: mô hình NMD lõi là mô hình theo TT83 Đ3.23 [[src-tt83-2025-nhnn#^d3-24]]; nếu ngân hàng xếp hạng rủi ro cao [[src-tt83-2025-nhnn#^d56-1]] thì phải kiểm định trước khi dùng, khi thay đổi trọng yếu và tối thiểu hằng năm [[src-tt83-2025-nhnn#^d56-4d]]; link [[model-validation]].
