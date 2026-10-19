---
title: "Phương pháp luận định giá điều chuyển vốn nội bộ (FTP) — Tài liệu tư vấn NHTM"
aliases: [src-vab-ftp, VAB FTP Methodology, Phuong phap luan FTP VAB]
type: source
source_id: src-vab-ftp
domains: [alm]
status: active
maturity: draft
tier: T4
doc_status: draft
issuer: "Tư vấn (theo tên file: EY)"
published: 2021-10-01
raw: "01_sources/alm/VAB - Phương pháp luận FTP/VAB - Phương pháp luận FTP.md"
units_done: [preamble, u01, u02, u03, u04, u05, u06, u07]
updated: 2026-10-16
---

## Thông tin nguồn
- Tiêu đề: *Báo cáo Tư vấn Phương pháp luận và Hỗ trợ Triển khai Hệ thống Định giá Điều chuyển Vốn Nội bộ FTP* (tài liệu tư vấn giữa EY Việt Nam và NHTMCP Việt Á - VietABank).
- Tier: T4 (tài liệu tư vấn nghiệp vụ ngân hàng thực chiến chuyên sâu tại Việt Nam).
- File raw: `01_sources/alm/VAB - Phương pháp luận FTP/VAB - Phương pháp luận FTP.md` (2.118 dòng).
- Units covered:
  - `preamble`: Phần mở đầu (lines 1–12).
  - `u01`: Tổng quan dự án, vai trò FTP trong quản trị thanh khoản & ALM (lines 13–344).
  - `u02`: Phương pháp xác định cấu phần đường cong lãi suất VOF & COF, chi phí dự trữ bắt buộc, bảo hiểm tiền gửi, phần bù thanh khoản kỳ hạn TLP (lines 345–648).
  - `u03`: Định giá sản phẩm không xác định kỳ hạn — Non-term Redemption Curve cho tiền gửi CASA (lines 649–953).
  - `u04`: Giá mua bán vốn cho các sản phẩm có quyền chọn ẩn — Prepayment & TDRR (lines 954–1255).

## Tóm tắt Nội dung và Khẳng định Then chốt

### 1. Vai trò và Mục tiêu của Hệ thống FTP trong NHTM
FTP là nền tảng quản trị sống còn của ngân hàng thương mại, giúp điều phối toàn bộ bảng cân đối tài sản - nợ:

> "Một trong những nền tảng quan trọng nhất để hướng tới yếu tố hiệu quả trong hoạt động của các NH TMCP được hỗ trợ bởi cơ chế định giá điều chuyển vốn nội bộ (Funds Transfer Pricing - FTP)."
> — VAB FTP ^vab-ftp-1
Hệ thống FTP đáp ứng cùng lúc 4 mục tiêu lớn:

> "Việc triển khai dự án FTP sẽ giúp Ngân hàng nâng cao hiệu quả của việc điều hành Bảng cân đối kế toán (BCĐKT) cũng như đáp ứng được các mục tiêu tổng thể bao gồm: Quản lý lợi nhuận, quản lý BCĐKT, quản lý rủi ro thanh khoản &amp; rủi ro lãi suất trên sổ ngân hàng và định hướng hoạt động kinh doanh."
> — VAB FTP ^vab-ftp-2
> "Báo cáo này nhằm mục đích cung cấp các hướng dẫn chi tiết trong việc tiến hành định giá điều chuyển vốn nội bộ, tuân thủ quy định của Pháp luật và phù hợp tiêu chuẩn của Basel."
> — VAB FTP ^vab-ftp-3
FTP phân bổ và bù đắp rủi ro thanh khoản và rủi ro lãi suất giữa các đơn vị kinh doanh và Trung tâm Quản lý Vốn (CFU/ALM):

> "Phản ánh các rủi ro mà Bộ phận FTP cần phải quản lý, trong đó bao gồm rủi ro thanh khoản và rủi ro lãi suất sổ ngân hàng."
> — VAB FTP ^vab-ftp-4
> "Để đáp ứng các vấn đề trên, lãi suất FTP phải phản ánh đầy đủ các chi phí vốn đầu vào (lãi suất huy động vốn, chi phí bảo hiểm tiền gửi, chi phí quản lý huy động vốn), chi phí quản lý rủi ro thanh khoản, rủi ro lãi suất."
> — VAB FTP ^vab-ftp-5
---

### 2. Cấu Trúc Biểu Giá Mua Vốn (VOF) và Giá Bán Vốn (COF)
Cơ chế FTP của ngân hàng được phân định thành hai biểu giá hai chiều:

#### Biểu giá mua vốn áp dụng cho nguồn huy động (VOF — Value of Funds):
> "VOF bao gồm các cấu phần sau:"
> — VAB FTP ^vab-ftp-6
- Lãi suất FTP cơ sở (Base curve) theo kỳ hạn huy động.
- Hỗ trợ huy động (Margin) do ALCO điều hành để thúc đẩy tăng trưởng tiền gửi.
- Điều chỉnh của ALCO cho tài sản nợ (ALCO adjust).

$$\text{VOF} = \text{Base Curve} + \text{Margin} + \text{ALCO Adjust}$$

#### Biểu giá bán vốn áp dụng cho tài sản tín dụng (COF — Cost of Funds):
> "COF bao gồm các cấu phần sau:"
> — VAB FTP ^vab-ftp-7
- Lãi suất FTP cơ sở (Base curve).
- Hỗ trợ huy động (Margin) — chuyển giao lợi ích giữa đơn vị cho vay và đơn vị huy động.
- Chi phí dự trữ bắt buộc (Statutory Reserved cost).
- Chi phí bảo hiểm tiền gửi (Deposit insurance cost).
- Phần bù cho tài sản thanh khoản (Liquidity premium).
- Phần bù thanh khoản kỳ hạn (Term liquidity premium).
- Điều chỉnh ALCO cho tài sản có (ALCO adjust).

$$\text{COF} = \text{Base Curve} + \text{Margin} + \text{Chi phí DTBB} + \text{Chi phí BHTG} + \text{Liquidity Premium} + \text{Term Liquidity Premium} + \text{ALCO Adjust}$$

---

### 3. Phương Pháp Định Lượng Chi Phí Tuân Thủ Pháp Định NHNN

#### Chi phí Bảo hiểm Tiền gửi (Deposit Insurance Cost):
Ngân hàng phải nộp phí bảo hiểm tiền gửi định kỳ cho tổ chức BHTG Việt Nam (mức luật định là 0,15%/năm tính trên số dư tiền gửi cá nhân bằng VND):

> "Là số tiền mà Ngân hàng phải thanh toán cho tổ chức BHTG theo quy định của NHNN trong từng thời kỳ (hiện tại là 0.15% năm tính trên số dư của các loại tiền gửi VND của KHCN)."
> — VAB FTP ^vab-ftp-8
Cấu phần này không trừ vào thu nhập của đơn vị huy động mà được **phân bổ đều vào giá bán vốn COF** tính trên toàn bộ tài sản sinh lời thuộc diện áp dụng FTP:
$$\text{Tỷ lệ Chi phí BHTG} = \frac{\text{Tổng Chi phí BHTG thực tế 3 tháng quy đổi năm}}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

#### Chi phí Dự trữ Bắt buộc (Statutory Reserved Cost):
Ngân hàng Nhà nước yêu cầu duy trì tỷ lệ dự trữ bắt buộc tiền mặt tại tài khoản NHNN:

> "NHNN yêu cầu các Ngân hàng phải nắm giữ tỷ lệ % tiền gửi nhất định như một khoản dự trữ tiền tại Ngân hàng Nhà nước."
> — VAB FTP ^vab-ftp-9
Khoản tiền gửi này chịu mức lãi suất tiền gửi dự trữ bắt buộc rất thấp từ NHNN (hoặc 0%), tạo ra chi phí cơ hội vốn (cost of negative carry). Chi phí này được phân bổ vào biểu giá bán vốn COF:
$$\text{Tỷ lệ Chi phí DTBB} = \frac{\text{Số dư DTBB bình quân} \times (\text{VOF bình quân} - \text{Lãi suất tiền gửi DTBB tại NHNN})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

---

### 4. Phần Bù Tài Sản Thanh Khoản và Phần Bù Thanh Khoản Kỳ Hạn (TLP)

#### Phần bù cho tài sản thanh khoản (Liquidity Buffer Premium):
Ngân hàng phải nắm giữ một danh mục tài sản có tính thanh khoản cao (trái phiếu chính phủ, tiền gửi NHNN) làm đệm an toàn theo [[src-bcbs-lcr|LCR]] và Thông tư 22/2019/TT-NHNN:

> "Phần bù cho tài sản thanh khoản thể hiện chi phí duy trì danh mục tài sản thanh khoản đáp ứng các yêu cầu về tài sản thanh khoản theo quy định TT22/2019/TT-NHNN, quy định nội bộ và/hoặc theo yêu cầu luật định"
> — VAB FTP ^vab-ftp-10
Chi phí duy trì đệm thanh khoản được xác định bằng chênh lệch âm giữa chi phí huy động bình quân (VOF bình quân) và lợi suất đầu tư tài sản thanh khoản:
$$\text{Liquidity Premium} = \frac{\text{Số dư bình quân TSTK} \times (\text{VOF bình quân} - \text{Lãi suất bình quân TSTK})}{\text{Bình quân Tổng tài sản bị tính FTP}}$$

#### Phần bù thanh khoản kỳ hạn (Term Liquidity Premium — TLP):
Phần bù thanh khoản kỳ hạn bảo đảm rằng các khoản vay dài hạn thả nổi không bị định giá thiếu hụt chi phí thanh khoản dài hạn:

> "Phần bù thanh khoản kỳ hạn phản ánh sự kết hợp giữa rủi ro tín dụng của riêng Ngân hàng và phần bù thanh khoản kỳ hạn phổ biến trong thị trường (chi phí thanh khoản dài hạn)."
> — VAB FTP ^vab-ftp-11
> "Phần bù thanh khoản kỳ hạn chỉ áp dụng cho những khoản vay có lãi suất thả nổi."
> — VAB FTP ^vab-ftp-12
Khoản vay lãi suất thả nổi thường được định kỳ tái định giá lãi suất theo kỳ hạn ngắn (ví dụ lãi suất 3 tháng hoặc 6 tháng), nhưng ngân hàng vẫn phải cam kết thanh khoản gốc cho đến kỳ hạn đáo hạn cuối cùng của khoản vay (ví dụ 5 năm). TLP bù đắp chính xác chênh lệch chi phí thanh khoản giữa kỳ hạn gốc và kỳ hạn tái định giá:
$$\text{TLP} = \text{Lãi suất đường cong FTP kỳ hạn gốc} - \text{Lãi suất đường cong FTP kỳ hạn tái định giá}$$

---

### 5. Định Giá Sản Phẩm Phi Kỳ Hạn — Đường Cong Hoàn Trả Tiền Gửi CASA (Non-term Redemption Curve)
Tiền gửi không kỳ hạn (CASA) có tính chất dòng tiền biến động theo hành vi của khách hàng:

> "Trường hợp áp dụng : Sản phẩm tiền gửi của khách hàng không có kỳ hạn."
> — VAB FTP ^vab-ftp-13
Ngân hàng áp dụng phương pháp danh mục sao chép (replicating portfolio) và đường cong hoàn trả (Redemption Curve) để chia tách CASA thành hai cấu phần: phần không ổn định (non-core / volatile CASA) và phần ổn định (core / sticky CASA):

> "VietABank áp dụng phương pháp Đường cong hoàn trả (Redemtion Curve) để xác định giá VOF dựa trên giá bình quân gia quyền của các thang kỳ hạn tương ứng với tỷ lệ dòng tiền ổn định và dòng tiền không ổn định."
> — VAB FTP ^vab-ftp-14
Công thức tính lãi suất VOF cơ sở cho CASA:

> "FTP Base Curve= FTP Base Curve i × Non-CoreCasa i + FTP Base Curve j(1- Non-corecasa i)"
> — VAB FTP ^vab-ftp-15
> "Non-CoreCasa i: Tỷ lệ tiền gửi CASA không ổn định của các thang kỳ hạn i và được xác định theo kết quả tính toán định kỳ của mô hình hành vi của ngân hàng tại thời điểm liền kề gần nhất."

Đối với trường hợp chưa xây dựng mô hình hành vi thống kê tiên tiến, áp dụng phân bổ theo tỷ lệ quy định thận trọng của NHNN (tỷ lệ rút tiền tối thiểu 15%):

> "VOF = VOFKKH TT1× a% + VOF CKH TT1 × (1- a%)"
> — VAB FTP ^vab-ftp-16
---

### 6. Định Giá Sản Phẩm Chứa Quyền Chọn Ẩn (Embedded Options Pricing)
Các sản phẩm trên bảng cân đối thường đi kèm với quyền chọn ẩn về hành vi tài chính:

> "Giá mua bán vốn áp dụng cho các sản phẩm có quyền chọn ẩn"
> — VAB FTP ^vab-ftp-17
#### Tiền gửi rút trước hạn:
Khách hàng có quyền rút tiền gửi có kỳ hạn trước ngày đáo hạn. Ngân hàng áp dụng cơ chế hồi tố lãi suất và phạt rút vốn trước hạn:

> "Áp dụng chi phí phạt rút trước hạn: Lãi suất VOF cơ sở được xác định dựa trên lãi suất VOF tương ứng KKH thông thường."
> — VAB FTP ^vab-ftp-18
#### Khoản vay trả nợ trước hạn (Prepayment Option):
Khi khách hàng trả nợ trước hạn, ngân hàng bị tổn thất do chi phí tái đầu tư (reinvestment risk) và chi phí thanh khoản bị xáo trộn. Giá COF được điều chỉnh theo kỳ hạn hiệu lực mô hình hóa hành vi thay vì kỳ hạn pháp lý:

> "Lãi suất COF cơ sở được xác định dựa trên Lãi suất COF cơ sở theo kỳ hạn hiệu lực được tính toán từ dòng tiền của MHHV(MÔ HÌNH HÀNH VI) trả trước hạn đối với từng khoản vay trả trước hạn."
> — VAB FTP ^vab-ftp-19
Kỳ hạn hiệu lực của khoản vay được xác định bằng phương pháp bình quân gia quyền:

> "định bằng phương pháp Bình quân gia quyền (Weighted Average) để tính kỳ hạn bình quân (thời lượng) của khoản vay theo công thức như sau:"
> — VAB FTP ^vab-ftp-20
---

### 7. Giải Thích Thuật Ngữ và Quy Trình Vận Hành (Units u05, u06, u07)

#### Định nghĩa cốt lõi về COF và VOF:
> "Là mức lãi suất các ĐVKD phải trả cho CFU khi CFU bán vốn để các ĐVKD sử dụng cho tài sản có"
> — VAB FTP ^vab-ftp-21
> "Là mức lãi suất các ĐVKD được hưởng khi CFU mua tài sản nợ của ĐVKD"
> — VAB FTP ^vab-ftp-22
#### Bản chất phần bù thanh khoản kỳ hạn:
> "Phần bù thanh khoản kỳ hạn phản ánh chi phí thanh khoản dài hạn và là phần bù cấu trúc được cộng vào lãi suất cơ sở."
> — VAB FTP ^vab-ftp-23
#### Đường cong lãi suất cơ sở:
> "Đường cong lãi suất cơ sở được tính toán dựa trên những thông tin sau:"
> — VAB FTP ^vab-ftp-24
#### Cấu phần hỗ trợ huy động (Margin):
> "Là cấu phần đảm bảo bù đắp tất cả các chi phí quản lý của các đơn vị huy động vốn cũng như khuyến khích hoạt động huy động của các đơn vị kinh doanh."
> — VAB FTP ^vab-ftp-25
#### Xây dựng đường cong FTP theo đồng tiền (VND, USD):
> "Do FTP được tính cho các loại tiền tệ nên các cấu phần trong giá FTP cũng được tính độc lập với các loại tiền tệ."
> — VAB FTP ^vab-ftp-26
> "Lãi suất FTP cơ sở được tính riêng biệt cho từng loại tiền tệ."
> — VAB FTP ^vab-ftp-27
> "Lãi suất FTP cơ sở đối với tiền VND được xây dựng dựa trên lãi suất huy động bình quân toàn hàng của các khoản phát sinh trong 3 tháng liền kề trước thời điểm tính."
> — VAB FTP ^vab-ftp-28
> "Lãi suất FTP cơ sở đối với tiền USD được xây dựng theo phương án dùng lãi suất tham chiếu của thị trường."
> — VAB FTP ^vab-ftp-29
#### Xây dựng đường cong FTP theo cấu trúc kỳ hạn và nội suy:
> "Giá mua vốn áp dụng cho các tài sản nợ (VOF) đối với các kỳ hạn không theo thang kỳ hạn chuẩn của biểu ban hành thì được tính nội suy/ngoại suy trực tiếp từ thang kỳ hạn chuẩn."
> — VAB FTP ^vab-ftp-30
> "Giá bán vốn áp dụng cho các tài sản có (COF) đối với các kỳ hạn không theo thang kỳ hạn chuẩn của biểu ban hành thì được tính nội suy/ngoại suy trực tiếp từ thang kỳ hạn chuẩn."
> — VAB FTP ^vab-ftp-31
#### Xây dựng biểu giá theo loại sản phẩm (Cố định, Thả nổi, Trả định kỳ):
> "Lãi suất COF cơ sở tương ứng với kỳ hạn gốc (bằng ngày đáo hạn trừ ngày giải ngân) của khoản cho vay căn cứ vào biểu lãi suất COF cơ sở tương ứng tại ngày giải ngân."
> — VAB FTP ^vab-ftp-32
> "Phần bù thanh khoản kỳ hạn = Lãi suất kỳ hạn gốc - Lãi suất của kỳ hạn tái định lại lãi suất"
> — VAB FTP ^vab-ftp-33
> "Phần bù thanh khoản kỳ hạn = Lãi suất của kỳ hạn hiệu lực - Lãi suất của kỳ hạn tái định lại lãi suất"
> — VAB FTP ^vab-ftp-34
> "FTP bán vốn đối với phần cam kết trong hạn mức chưa được sử dụng của thẻ tín dụng, thẻ thấu chi và các khoản cho vay có lịch giải ngân chưa xác định nhưng lãi suất cố định tại thời điểm ký kết hợp đồng được áp dụng dựa trên phần bù rủi ro thanh khoản tiềm tàng."
> — VAB FTP ^vab-ftp-35
#### Cơ chế FTP Thị trường 2 (Liên ngân hàng / Treasury):
> "Lãi suất FTP cơ sở mua bán vốn với các giao dịch trên thị trường liên ngân hàng (thị trường 2) được thiết lập theo 1 trong 2 phương án:"
> — VAB FTP ^vab-ftp-36
> "Lãi suất mua bán vốn TT2 = Bình quân Lãi suất chào nhận và chào gửi của nhóm NH TMCP cùng Peer (bao gồm 3 đến 6 NH TMCP cùng Peer tại thời điểm tính)"
> — VAB FTP ^vab-ftp-37
#### Khung báo cáo và đo lường hiệu quả NII / NIM (Điều 14 & Phụ lục 01):
> "Lập báo cáo tổng hợp để đánh giá hiệu quả hoạt động của toàn bộ các đơn vị kinh doanh, các sản phẩm và xác định các sản phẩm/đơn vị kinh doanh kém hiệu quả."
> — VAB FTP ^vab-ftp-38
> "Tuy nhiên, đối với từng sản phẩm, khách hàng hoặc đơn vị kinh doanh, NII sẽ được xác định thu nhập lãi (thu nhập lãi cho vay hoặc thu nhập FTP) so với chi phí lãi"
> — VAB FTP ^vab-ftp-39
> "Lãi cận biên ròng NIM trong tài liệu này được xác định dựa trên chênh lệch giữa lãi suất suất cho vay với giá FTP bán vốn đối với Tài sản; và chênh lệch giữa giá FTP mua vốn với lãi suất huy động đối với nợ phải trả"
> — VAB FTP ^vab-ftp-40
## Khái niệm và Liên kết
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU.
- [[ftp-pricing-methodology]]: Phân tích chuyên sâu phương pháp luận định giá VOF/COF và phụ phí tuân thủ ngân hàng.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn điều tiết rủi ro thanh khoản, lãi suất và tín dụng của FTP.
- [[ftp-balance-sheet-optimization]]: Mô hình tối ưu hóa bảng cân đối ALM toàn diện.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản tổng quát theo Moorad Choudhry.
- [[lcr]]: Đệm tài sản thanh khoản chất lượng cao theo chuẩn mực quốc tế.
