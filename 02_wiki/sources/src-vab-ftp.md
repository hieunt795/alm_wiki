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
updated: 2026-10-21
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

- Tài sản thanh khoản (TSTK) trong công thức phần bù là tài sản thanh khoản cao giữ làm đệm, danh mục theo Phụ lục 3 TT22/2019; số dư bình quân TSTK lấy số dư hàng ngày theo yêu cầu NHNN về đệm thanh khoản, không gồm repo và cho vay cầm cố, bình quân 3 tháng liền trước.
  > "TSTK: Là tài sản có tính thanh khoản cao Ngân hàng nắm giữ nhằm mục đích duy trì đệm thanh khoản. Chi tiết sản phẩm tuân thủ Phụ lục 3, Thông tư 22/2019/TT-NHNN."
  > "Số dư bình quân TSTK: là bình quân số dư tài sản thanh khoản hàng ngày theo yêu cầu bởi NHNN về chỉ số đệm thanh khoản (không bao gồm các khoản repo, cho vay cầm cố) trong 3 tháng liền trước thời điểm lập báo cáo."
  > — Mục 4 phần bù TSTK, giải thích ký hiệu ^vab-ftp-43

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

- Khi chưa áp dụng mô hình hành vi: phần KKH có khả năng bị rút không thấp hơn 15% số dư bình quân tiền gửi KKH 30 ngày liền kề, theo quy định NHNN mà chú thích (2) dẫn tới điểm 2 phần III Phụ lục 3 TT22/2019; a% không nhỏ hơn 15%; phần còn lại nhận VOF kỳ hạn 2 tháng hoặc theo ALCO.
  > "Nguyên tắc xác định số dư bình quân tiền gửi KKH duy trì và có khả năng bị rút ra theo quy định của NHNN (không thấp hơn 15% số dư bình quân tiền gửi KKH của khách hàng trong 30 ngày liền kề ngày tính toán)"
  > "a%: tỷ lệ rút ra của tiền gửi KKH (không nhỏ hơn 15%)."
  > "VOF CKH TT1: Lãi suất VOF kỳ hạn 2 tháng hoặc theo phê duyệt của ALCO trong từng thời kỳ."
  > "Quy định tại điểm 2 phần III Phụ lục 3, Thông tư 22/2019/TT-NHNN."
  > — Mục 6.1.c.i, chú thích (2) ^vab-ftp-44

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

- Danh mục thông tin đầu vào của đường cong cơ sở (bổ sung cho ^vab-ftp-24): VND dùng lãi suất huy động tiền gửi VND thực tế bình quân 3 tháng liền kề, đã gồm chi phí huy động; USD/ngoại tệ trọng yếu dùng lãi suất tham chiếu thị trường: đường cong LIBOR/SIBOR hoặc công cụ thay thế như SOFR, và đường cong lãi suất hoán đổi USD. Không có VNIBOR, OMO hay lợi suất TPCP trong danh mục.
  > "Lãi suất huy động tiền gửi VND thực tế bình quân trong 3 tháng liền kề thời điểm tính toán. Đã bao gồm các chi phí huy động phát sinh."
  > "Dùng lãi suất tham chiếu của thị trường, dữ liệu đầu vào yêu cầu bao gồm:"
  > "Đường cong LIBOR/SIBOR/Các công cụ thay thế tương đương như lãi suất SOFR (Lãi suất qua đêm có đảm bảo)."
  > "Đường cong lãi suất hoán đổi USD"
  > — PL02 mục 1.a Bước 1 ^vab-ftp-41

- Hoàn thiện đường cong cơ sở: VND nội suy/ngoại suy tuyến tính cho kỳ hạn thiếu thông số; USD lấy bình quân lãi suất tham chiếu 3 tháng liền kề trên từng kỳ hạn.
  > "Đối với các kỳ hạn tham chiếu chưa đầy đủ thông số, Ngân hàng sẽ tiến hành nội suy/ngoại suy tuyến tính sử dụng công cụ Excel"
  > "Tính bình quân lãi suất tham chiếu trong 3 tháng liền kề thời điểm tính toán trên từng kỳ hạn."
  > — PL02 mục 1.a Bước 2 ^vab-ftp-42
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
### u06–u07 (bổ sung 2026-10-21) — Minh hoạ phần bù TSTK và TLP, PL03 phần bù thanh khoản tiềm tàng, PL05–PL06 quy trình vận hành FTP TT1/TT2, MB04 đầu vào đường cong TT2

- Minh hoạ phần bù tài sản thanh khoản: bước 1 thu thập số dư hằng ngày và lãi suất của từng loại tài sản thanh khoản (không gồm repo, cho vay cầm cố); bước 2 tính phần bù theo công thức số dư bình quân TSTK × (VOF bình quân − LSBQ.TSTK) chia tổng tài sản bị tính FTP. Kết quả minh hoạ để trống `(0.00)`, chi tiết ở file Excel.
  > "Bước 1. Thu thập thông tin:"
  > "Loại tài sản thanh khoản (không bao gồm khoản repo, cho vay cầm cố)"
  > "Bước 2. Tính toán phần bù cho tài sản thanh khoản"
  > "Số dư bình quân TSTK × (VOF bình quân - LSBQ.TSTK)"
  > "Tổng tài sản bị tính FTP"
  > — PL02 mục 5.b ^vab-ftp-45

- Phần bù thanh khoản kỳ hạn tính theo 2 bước: (1) dùng đường cong FTP cơ sở để hoàn thiện đường lãi suất giả định cho các kỳ tái định giá; (2) tính phần bù cho mọi kỳ hạn bằng lãi suất kỳ hạn gốc trừ lãi suất kỳ tái định giá, tức chênh lệch lãi suất giữa 2 kỳ đáo hạn.
  > "Bước 1. Sử dụng đường cong lãi suất FTP cơ sở để hoàn thiện đường lãi suất giả định cho các kỳ tái định giá"
  > "Bước 2. Xác định phần bù kỳ hạn cho tất cả các kỳ hạn: Phần bù kỳ hạn cho các sản phẩm lãi suất thả nổi được tính theo công thức: Phần bù thanh khoản kỳ hạn = Lãi suất của kỳ hạn gốc - Lãi suất của kỳ hạn tái định lại lãi suất"
  > "Để tính phần bù kỳ hạn cho các sản phẩm lãi suất thả nổi, Ngân hàng sẽ tính chênh lệch lãi suất giữa 2 kỳ đáo hạn."
  > — PL02 mục 6.a–6.b ^vab-ftp-46

- Minh hoạ TLP (số liệu minh hoạ, %). Bước 1, lãi suất giả định theo kỳ tái định giá (bảng nguồn lặp cùng giá trị trên mọi kỳ đáo hạn ≥ kỳ tái định giá; chép giá trị của mỗi dòng):

| Kỳ tái định giá | NM | 7D | 14D | 21D | 1M | 2M | 3M | … | 24M | 36M | 48M | 60M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lãi suất giả định | 2.02 | 2.24 | 2.44 | 2.46 | 2.70 | 2.92 | 3.22 | 4.68 (dòng "…") | 4.81 | 4.92 | 4.98 | 5.10 |

  Bước 2, ma trận TLP (dòng: kỳ tái định giá; cột: kỳ đáo hạn), trích các dòng có trong raw:

| Kỳ tái định giá | NM | 7D | 14D | 21D | 1M | 2M | 3M | … | 24M | 36M | 48M | 60M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NM | 0.00 | 0.22 | 0.42 | 0.44 | 0.68 | 0.90 | 1.20 | … | 2.79 | 2.90 | 2.96 | 3.08 |
| 7D | | 0.00 | 0.20 | 0.22 | 0.46 | 0.68 | 0.98 | … | 2.57 | 2.68 | 2.74 | 2.86 |
| 1M | | | | | 0.00 | 0.22 | 0.52 | … | 2.11 | 2.22 | 2.28 | 2.40 |
| 3M | | | | | | | 0.00 | … | 1.59 | 1.70 | 1.76 | 1.88 |
| 24M | | | | | | | | … | 0.00 | 0.11 | 0.18 | 0.29 |
| 48M | | | | | | | | … | | | 0.00 | 0.11 |

  > "Bước 1. Hoàn thiện đường lãi suất giả định"
  > "Chi tiết tham khảo file excel sheet 'Term\_liquidity\_pre\_VND', 'Term\_liquidity\_pre\_USD'"
  > — PL02 mục 6.b ^vab-ftp-47

- Phần bù rủi ro thanh khoản tiềm tàng (cấu phần FTP đặc biệt), minh hoạ với hạn mức chưa giải ngân của thẻ tín dụng: hạn mức 100.000.000, dư nợ 20.000.000, CCF 10% theo Điều 10 TT41, tỷ lệ dự trữ thanh khoản 10%, VOF bình quân theo kỳ hạn 6,5%, lợi suất tài sản thanh khoản 5%. Chi phí duy trì tài sản thanh khoản 1,5%; hạn mức khả dụng 80.000.000; phần bù 12.000.
  > "Bước 1. Thu thập thông tin: Minh họa trường hợp Ngân hàng cho khách hàng vay thẻ tín dụng:"
  > "Bước 2. Tính toán phần bù rủi ro thanh khoản tiềm tàng theo công thức tại Điều 5 mục 2 quy định này."
  > — PL03 mục 1 ^vab-ftp-48

| Khoản mục | Giá trị | Ghi chú |
|---|---|---|
| Hệ số chuyển đổi tín dụng (CCF) - Theo Điều 10 TT41 | 10% | |
| Tỷ lệ dự trữ thanh khoản | 10% | |
| Chi phí huy động tài sản thanh khoản (VOF bình quân theo kỳ hạn) | 6.5% | |
| Lợi suất tài sản thanh khoản tạo ra | 5% | |
| Chi phí duy trì tài sản thanh khoản | 1.5% | = 6.5% - 5% |
| Hạn mức khả dụng | 80,000,000 | = 100 - 20 |
| Phần bù rủi ro thanh khoản tiềm tàng | 12,000 | = 80 × 10% × 10% × 1.5% |

- Quy trình FTP thị trường 1 (PL05): định kỳ hằng quý hoặc khi thị trường biến động lớn, Bộ phận quản lý FTP đề xuất cập nhật biểu lãi suất FTP và yêu cầu dữ liệu đầu vào (MB02). Khối CNTT chiết xuất dữ liệu cho FTP thông thường; khối kinh doanh lập đề xuất FTP đặc biệt/ngoại lệ.
  > "Định kỳ hàng quý hoặc khi có biến động lớn trên thị trường, Bộ phận quản lý FTP đề xuất cập nhật biểu lãi suất FTP, cung cấp danh sách dữ liệu đầu vào yêu cầu Khối CNTT, Khối Kinh doanh và các đơn vị liên quan khác cung cấp."
  > "Khối CNTT chiết xuất dữ liệu tính lãi suất FTP cơ sở, chuyển cho Bộ phận quản lý FTP."
  > "Khối kinh doanh/các đơn vị liên quan lập đề xuất áp dụng chính sách FTP đặc biệt/ngoại lệ (các chính sách FTP ngoại lệ, các trường hợp điều chỉnh thu nhập/chi phí FTP, các cấu phần FTP đặc biệt cho khách hàng, chương trình thúc đẩy, sản phẩm đặc thù, …) chuyển cho Bộ phận quản lý FTP."
  > — PL05 mục II bước 1–2 ^vab-ftp-49

- PL05 tiếp: Trưởng bộ phận quản lý FTP kiểm soát, rà soát; trình ALCO tham mưu đến TGĐ phê duyệt và ban hành biểu lãi suất FTP TT1; TGĐ (hoặc người được uỷ quyền) ký phê duyệt hoặc trả lại để điều chỉnh. Bước 3 và 5 ghi ban hành "Giải pháp FTP hàng tháng", trong khi cột thời gian ghi "Hàng quý/khi có yêu cầu".
  > "Trình ALCO tham mưu đến TGĐ phê duyệt và ban hành Biểu lãi suất FTP TT1."
  > "Nếu đồng ý, ký phê duyệt ban hành Giải pháp FTP hàng tháng."
  > "Hàng quý/khi có yêu cầu"
  > — PL05 mục II bước 3–5 ^vab-ftp-50

- PL05 tiếp: Khối CNTT/Bộ phận quản lý FTP cập nhật biểu đã phê duyệt lên hệ thống quản lý vốn nội bộ; khối kinh doanh thực hiện và rà soát giao dịch mua bán vốn nội bộ; cấp kiểm soát của Bộ phận quản lý FTP kiểm tra số tiền, loại tiền, kỳ hạn, lãi suất và xác nhận giao dịch; Bộ phận kế toán tổng hợp, lưu trữ hồ sơ giao dịch giữa CFU và đơn vị kinh doanh.
  > "Khối CNTT/Bộ phận quản lý FTP, định kỳ cập nhật biểu lãi suất FTP TT1 đã được phê duyệt lên hệ thống quản lý vốn nội bộ."
  > "Cấp kiểm soát bộ phận quản lý FTP chịu trách nhiệm kiểm tra số tiền, loại tiền, kỳ hạn, lãi suất mua bán vốn và thực hiện xác nhận giao dịch mua bán vốn nội bộ."
  > "Tổng hợp và lưu trữ hồ sơ giao dịch điều chuyển vốn nội bộ giữa CFU và các đơn vị kinh doanh."
  > — PL05 mục II bước 6–9 ^vab-ftp-51

- Quy trình điều chuyển vốn nội bộ trên thị trường 2 (PL06): hằng ngày Khối QL&KDV cung cấp lãi suất thị trường; Bộ phận quản lý FTP tính biểu FTP TT2 hằng ngày từ 9 giờ đến 10 giờ. Phương pháp 1: bình quân lãi suất chào gửi và chào nhận (mid-rate) của các ngân hàng TMCP tham chiếu. Phương pháp 2: xác nhận mức VNIBOR áp dụng theo cơ chế đã được TGĐ phê duyệt.
  > "Hàng ngày, các Bộ phận liên quan thuộc Khối QL&KDV thu thập và kịp thời cung cấp thông tin lãi suất thị trường cho Bộ phận quản lý FTP thông qua công cụ: skype, mail,….."
  > "Hàng ngày từ 9 giờ đến 10 giờ/khi có yêu cầu"
  > "Trường hợp Ngân hàng áp dụng phương pháp 1 xác định lãi suất cơ sở: Dựa trên bình quân lãi suất chào gửi và chào nhận (mid-rate) của các NH TMCP tham chiếu:"
  > "Trường hợp Ngân hàng áp dụng phương pháp 2 xác định lãi suất cơ sở: Dựa trên lãi suất VNIBOR:"
  > — PL06 mục II bước 1–2 ^vab-ftp-52

- PL06 tiếp: Trưởng bộ phận quản lý FTP rà soát, trình ALCO tham mưu TGĐ phê duyệt ban hành; TGĐ phê duyệt biểu lãi suất FTP nội bộ giữa CFU và Khối QL&KDV hằng ngày. Giao dịch trước khi ban hành biểu mới áp dụng biểu có hiệu lực ngày làm việc liền trước; giao dịch trong ngày áp dụng biểu có hiệu lực tại ngày giao dịch.
  > "Trưởng bộ phận quản lý FTP kiểm soát, rà soát biểu lãi suất FTP TT2, thông qua trưởng bộ phận quản lý FTP cho ý kiến, sau đó trình ALCO tham mưu TGĐ phê duyệt ban hành."
  > "Nếu đồng ý, ký phê duyệt ban hành Biểu lãi suất FTP nội bộ giữa CFU và K.QL&KDV hàng ngày."
  > "Với các giao dịch mua bán trước khi ban hành biểu điều chuyển vốn mới: Áp dụng biểu có hiệu lực vào ngày làm việc liền kề trước."
  > — PL06 mục II bước 3–5 ^vab-ftp-53

- MB04 (đầu vào đường cong lãi suất liên ngân hàng TT2): danh sách ngân hàng tham chiếu (để trống trong mẫu), danh sách kỳ hạn tham chiếu ON, 7D, 14D, 21D, 1M, 2M, 3M, 6M và tiếp theo; dữ liệu hằng ngày gồm BID và OFFER của từng ngân hàng tham chiếu theo từng kỳ hạn.
  > "BIỂU DỮ LIỆU ĐẦU VÀO PHỤC VỤ XÂY DỰNG ĐƯỜNG CONG LÃI SUẤT THỊ TRƯỜNG LIÊN NGÂN HÀNG (TT2)"
  > "(Tương tự cho các thang kỳ hạn tiếp theo)"
  > — MB04 ^vab-ftp-54

#### Ghi chú convert u06–u07 (bổ sung)
- Công thức phần bù TSTK (dòng 1578–1584) bị vỡ thành 3 dòng rời, kết quả minh hoạ `(0.00)`; giá trị phân số dựng lại đã có ở ^vab-ftp-43.
- Bảng TLP (dòng 1603–1653) bị tách 4 mảnh do ngắt trang; dòng "…" che các kỳ tái định giá giữa 3M và 24M.
- PL05 bước 3 dính chữ (`TrìnhALCOthammưuđếnTGĐphêduyệtvàban hành`); PL05 bước 4 ghi "biểu lãi suất FTP TT2" trong quy trình TT1 (nghi lỗi soạn thảo).

### u04 (bổ sung 2026-10-21) — Điều 7.2 Nostro/Vostro, Điều 9 đường cong FTP thị trường 2, Điều 10 cơ chế FTP khối QL&KDV, Điều 11 phát hành GTCG

- Tiền gửi không kỳ hạn tại TCTD khác (Nostro, kể cả tiền gửi tại NHNN) thuộc danh mục tài sản thanh khoản cao, đã được tính chi phí TSTK nên không mua bán vốn FTP với CFU.
  > "Tiền gửi KKH tại các TCTD khác thuộc danh mục tài sản thanh khoản cao của Ngân hàng và đã được tính chi phí TSTK cao nên không áp dụng mua bán vốn FTP với CFU."
  > — Đ7.2.a ^vab-ftp-55

- Vostro (tiền gửi KKH của TCTD khác mở tại ĐVKD): VOF cơ sở lấy theo lãi suất VOF cơ sở TT2 kỳ hạn qua đêm (ON), cố định suốt giao dịch; phần bù thanh khoản kỳ hạn bằng 0.
  > "Áp dụng cho các khoản TG KKH của các TCTD khác mở tại các ĐVKD."
  > "Cách xác định lãi suất VOF cơ sở: Lãi suất VOF cơ sở TT2 tương ứng với kỳ hạn qua đêm (ON)."
  > "Lãi suất VOF cơ sở này được áp dụng cố định trong suốt thời gian của giao dịch."
  > "Phần bù thanh khoản kỳ hạn = 0: Áp dụng trong suốt thời hạn giao dịch."
  > — Đ7.2.b ^vab-ftp-56

- Phương án 1 dùng mid-rate của tối thiểu 3 đến 6 NH TMCP cùng peer (cùng mức xếp hạng tín nhiệm) trên thị trường liên ngân hàng. Tiêu chí ưu tiên: tương đương quy mô tài sản; tương đương xếp hạng tín nhiệm (tham khảo Moody's, S&P, Fitch); giao dịch thường xuyên với VietABank; tương đương chiến lược bán lẻ/bán buôn. ALCO rà soát, thông qua danh sách tối thiểu 1 năm/1 lần, trên đề xuất của Khối QL&KDV và ý kiến Phòng ALM.
  > "Phương án 1: Dựa trên bình quân lãi suất chào gửi và chào nhận (mid-rate) của các NH TMCP tham chiếu làm cơ sở để xác định cơ chế giá."
  > "Các NH TMCP tham chiếu lãi suất bao gồm: tối thiểu 3 đến 6 NH TMCP có cùng mức độ xếp hạng tín nhiệm (cùng Peer) với VietABank trên thị trường liên ngân hàng."
  > "Các ngân hàng có tương đương về quy mô tài sản;"
  > "Các ngân hàng tương đương về mức độ xếp hạng tín nhiệm trên thị trường"
  > "Các ngân hàng có giao dịch thường xuyên với VietABank (active) để đảm bảo tính sát thực tế của lãi suất và kỳ hạn mà các đối tác đang cung cấp cho VietABank"
  > "Tham  chiếu  chung  tổng  thể  Ngân  hàng  mức  độ  tương  đương VietABank về chiến lược kinh doanh bán lẻ/bán buôn."
  > "Danh sách các ngân hàng cùng mức độ xếp hạng tín nhiệm được sử dụng làm tham chiếu cần được ALCO rà soát và thông qua trong từng giai đoạn (rà soát tối thiểu 1 năm/1 lần) trên đề xuất của Khối QL&amp;KDV và đóng góp ý kiến của Phòng ALM (Khối Tài chính)."
  > — Đ9.1.a ^vab-ftp-57

- Nguyên tắc chung của phương án 1: kỳ hạn thiếu thông số thì nội suy/ngoại suy theo chênh lệch lãi suất giữa các kỳ hạn; giá của một ngân hàng peer (giá không thực hiện giao dịch) lệch quá ±15% so với bình quân các ngân hàng còn lại bị coi là outlier và loại khỏi bình quân; sau khi xác định lãi suất TT2, CFU được cộng trừ một biên độ đã được ALCO thông qua.
  > "Đối với kỳ hạn tham chiếu chưa đầy đủ thông số: Ngân hàng sẽ tiến hành nội suy/ngoại suy dựa trên lãi suất tham chiếu của kỳ hạn đã có, tiến hành nội/ngoại suy lãi suất cho các kỳ hạn còn lại dựa trên biên độ chênh lệch lãi suất giữa các kỳ hạn."
  > "Trong trường hợp lãi suất thu thập được của một trong số các ngân hàng cùng Peer (giá không thực hiện giao dịch) vượt ngưỡng trên/dưới 15% giá bình quân của các ngân hàng còn lại trong nhóm cùng Peer thì thông tin giá đó sẽ được xem là dữ liệu ngoại lai (outlier) và loại bỏ ra khi tính bình quân."
  > "Sau khi xác định ra lãi suất TT2 thì CFU được quyền cộng trừ thêm 1 biên độ đã được ALCO thông qua điều chỉnh để phù hợp hóa đường cong, hạn chế mức độ sai lệch của các lãi suất tham chiếu thu thập được."
  > — Đ9.2.a ^vab-ftp-58

- Phương án 2: lãi suất mua bán vốn TT2 bằng VNIBOR kỳ hạn 1 tuần.
  > "Phương án 2: Dựa trên lãi suất VNIBOR làm cơ sở để xác định cơ chế giá mua/bán vốn trên Thị trường 2."
  > "Lãi suất mua bán vốn TT2 được xác định bằng lãi suất VNIBOR kỳ hạn 1 tuần."
  > — Đ9.2.b ^vab-ftp-59

- Cơ chế FTP khối QL&KDV, phương án 1: áp cho trạng thái ròng của từng desk kinh doanh; các desk mua bán vốn trực tiếp với CFU; lãi suất TT2 theo kỳ hạn của nhu cầu cân đối vốn từng desk; cố định trong thời gian giao dịch.
  > "Áp dụng cho trạng thái ròng của từng bộ phận kinh doanh (Desk kinh doanh) trực thuộc khối QL&amp;KDV phục vụ cho mục đích kinh doanh. Các bộ phận kinh doanh sẽ mua bán vốn trực tiếp với với bộ phận quản lý FTP (CFU)."
  > "Lãi suất mua bán vốn TT2 tương ứng với kỳ hạn theo nhu cầu cân đối vốn của từng bộ phận kinh doanh thuộc khối QL&amp;KDV và Bộ phận quản lý FTP."
  > "Thời hạn hiệu lực của lãi suất mua bán vốn TT2: áp dụng cố định trong thời gian giao dịch."
  > — Đ10.1 ^vab-ftp-60

- Cơ chế FTP khối QL&KDV, phương án 2: áp cho trạng thái ròng của cả khối; bộ phận điều hoà vốn (MM) đại diện khối mua bán phần thặng dư/thiếu hụt ròng với CFU; ngân hàng cần hạn mức thanh khoản 30 ngày cho trạng thái ròng của khối, nếu chưa có thì theo dõi định kỳ (hằng ngày/hằng tuần) tuân thủ chỉ số khả năng chi trả 30 ngày của NHNN; lãi suất là VNIBOR 1 tuần, cố định trong kỳ hạn giao dịch.
  > "Áp dụng cho trạng thái ròng của cả khối QL&amp;KDV (bao gồm tất cả các đơn vị kinh doanh của khối) phục vụ cho mục đích kinh doanh. Trong đó, bộ phận điều hòa vốn (MM) đại diện cho Khối QL&amp;KDV thực hiện mua bán vốn phần thặng dư/thiếu hụt vốn ròng của cả Khối với bộ phận quản lý FTP (CFU)."
  > "Để có thể áp dụng cơ chế này, Ngân hàng cần thiết lập hạn mức thanh khoản 30 ngày cho trạng thái ròng của khối QL&amp;KDV."
  > "Trường hợp Ngân hàng chưa thiết lập hạn mức thanh khoản 30 ngày cho trạng thái ròng của khối QL&amp;KDV, Ngân hàng theo dõi định kỳ việc tuân thủ chỉ số thanh khoản về khả năng chi trả 30 ngày để đảm bảo tuân thủ quy định của NHNN. Tần suất theo dõi dựa trên tình hình thanh khoản thực tế của Ngân hàng, định kỳ hàng ngày/hàng tuần."
  > "Lãi suất mua bán vốn TT2 áp dụng là lãi suất VNIBOR kỳ hạn 1 tuần."
  > "Thời hạn hiệu lực của lãi suất mua bán vốn TT2: áp dụng cố định trong kỳ hạn giao dịch"
  > — Đ10.2 ^vab-ftp-61

- Phát hành GTCG do Khối QL&KDV thực hiện: nếu phát hành theo yêu cầu ALCO, ghi nhận tại book Hội sở để phục vụ sổ ngân hàng thì không áp dụng mua bán vốn nội bộ, khối có thể được trả phí hoa hồng tương đương một khoản "Điều chỉnh ALCO"; nếu phát hành trên TT2, ghi nhận cho Khối QL&KDV thì áp dụng như GTCG trên TT1 tại Điều 6.1.
  > "Khối QL&amp;KDV phát hành GTCG theo yêu cầu của ALCO (ghi nhận phát hành GTCG tại book của Hội sở) nhằm mục đích phục vụ cho Sổ ngân hàng."
  > "Không áp dụng cơ chế mua bán vốn nội bộ."
  > "Khối QL&amp;KDV có thể được trả một mức phí hoa hồng tương đương một khoản 'Điều chỉnh ALCO' phù hợp với chiến lược, mục tiêu, định hướng quản lý của ALCO trong từng thời kỳ."
  > "Phát hành GTCG trên TT2 (ghi nhận cho Khối QL&amp;KDV) thì cơ chế mua bán vốn được áp dụng tương tự như cơ chế áp dụng cho việc phát hành GTCG trên TT1 của các Khối Kinh doanh được đề cập tại Điều 6.1."
  > — Đ11 ^vab-ftp-62

### u02 (bổ sung 2026-10-21, nhóm 1) — Điều chỉnh ALCO, tần suất rà soát cấu phần FTP, chi phí vốn chủ sở hữu, phần bù rủi ro thanh khoản tiềm tàng

- Điều chỉnh ALCO cho tài sản nợ: CFU cộng thêm vào giá FTP mua vốn một mức điều chỉnh được ALCO thông qua, để điều tiết hành vi đơn vị kinh doanh theo chiến lược huy động từng thời kỳ (kỳ hạn, loại tiền, khối, đối tượng khách hàng); áp cho tất cả sản phẩm trong quy định.
  > "Nhằm thực hiện chức năng điều tiết hành vi của các đơn vị kinh doanh theo định hướng mong muốn của hội đồng ALCO, CFU cộng thêm 1 mức điều chỉnh được ALCO thông qua vào giá FTP mua vốn."
  > "Điều chỉnh ALCO được áp dụng cho các điều chỉnh về chiến lược huy động của từng thời kỳ về: kỳ hạn, loại tiền, khối, đối tượng khách hàng."
  > "Mức điều chỉnh ALCO này được áp dụng cho tất cả các sản phẩm được đề cập tại quy định này."
  > — Đ4.2.3 ^vab-ftp-63

- Điều chỉnh ALCO cho cho vay: COF được cộng/trừ một mức điều chỉnh chung phục vụ chiến lược cho vay từng thời kỳ (loại tiền, kỳ hạn, sản phẩm); có thể khớp hoặc không khớp với điều chỉnh ALCO cho tài sản nợ, tuỳ mục tiêu chiến lược. Chương trình/sản phẩm ưu đãi cụ thể do ALCO xem xét trên tờ trình riêng.
  > "Tương tự như lãi suất mua vốn, COF cũng được cộng/trừ một mức điều chỉnh chung để phục vụ cho các chiến lược về cho vay của từng thời kỳ: loại tiền, kỳ hạn hoặc sản phẩm."
  > "Đối với các chương trình/sản phẩm ưu đãi cụ thể, ALCO sẽ tiến hành xem xét, thông qua, tham mưu theo chức năng nhiệm vụ được quy định trong Chính sách trên các tờ trình/đề xuất cụ thể."
  > "Điều chỉnh ALCO cho Tài sản Có có thể khớp với Điều chỉnh ALCO cho Tài sản Nợ hoặc không, phụ thuộc vào mục tiêu chiến lược của ngân hàng."
  > — Đ4.3.5 ^vab-ftp-64

- Tần suất rà soát các cấu phần FTP: lãi suất FTP cơ sở, chi phí BHTG, chi phí DTBB, phần bù TSTK, TLP và điều chỉnh ALCO rà soát hằng quý; hỗ trợ huy động rà soát hằng năm hoặc khi kế hoạch kinh doanh thay đổi. Mọi cấu phần bắt buộc, trừ điều chỉnh ALCO (tuỳ quyết định của ALCO).
  > "Cấu phần giá FTP, phương pháp luận FTP, tần suất cập nhật và cơ sở tính toán được trình bày trong bảng dưới đây."
  > — Đ4.4 ^vab-ftp-65

| STT | Cấu phần đường cong FTP | Phương pháp tính toán FTP | Tần suất rà soát | Yêu cầu áp dụng |
|---|---|---|---|---|
| 1 | Lãi suất FTP cơ sở | Đường cong FTP (cấu trúc kỳ hạn) | Hàng quý | Bắt buộc |
| 2 | Hỗ trợ huy động | Phần bù cộng vào đường cong FTP | Hàng năm hoặc khi có thay đổi về kế hoạch kinh doanh | Bắt buộc |
| 3 | Chi phí bảo hiểm tiền gửi | Phần bù cộng vào đường cong FTP | Hàng quý | Bắt buộc |
| 4 | Chi phí dự trữ bắt buộc | Phần bù cộng vào đường cong FTP | Hàng quý | Bắt buộc |
| 5 | Phần bù cho tài sản thanh khoản | Phần bù cộng vào đường cong FTP | Hàng quý | Bắt buộc |
| 6 | Phần bù thanh khoản kỳ hạn | Đường cong FTP (cấu trúc kỳ hạn) | Hàng quý | Bắt buộc |
| 7 | Mức điều chỉnh ALCO cho tài sản nợ và tài sản có | Phần bù cộng vào đường cong FTP | Hàng quý | Không bắt buộc, phụ thuộc vào quyết định của ALCO |

- Vốn chủ sở hữu tài trợ các khoản mục dài hạn, không sinh lãi (tài sản cố định, tài sản khác, đầu tư vào công ty con, công ty liên kết). Khi có thặng dư VCSH và chưa áp khung RAROC: chi phí VCSH tính trên phần thặng dư theo VOF bình quân TT1; thặng dư = VCSH trừ tài sản cố định, lãi phải thu, tài sản có khác, phí phải trả, nợ phải trả khác. Không có thặng dư thì không tính chi phí VCSH.
  > "VCSH được sử dụng để tài trợ cho các khoản mục đầu tư dài hạn và không sinh lãi /theo định hướng của Ngân hàng ví dụ như: Tài sản Cố định, Tài sản khác, Đầu tư vào công ty con, công ty liên kết, v.v."
  > "Trường hợp Ngân hàng chưa áp dụng khung quản lý tỷ lệ phần trăm giữa tổng lợi nhuận trước thuế so với Vốn kinh tế RAROC, chi phí VCSH được tính toán dựa trên phần thặng dư VCSH và được xác định theo lãi suất VOF bình quân của TT1."
  > "Khoản mục tài sản khác được khấu trừ ra khỏi VCSH để tính phần thặng dư cuối cùng bao gồm:"
  > "Trường hợp Ngân hàng không có thặng dư Vốn chủ sở hữu: Không áp dụng tính toán chi phí Vốn chủ sở hữu."
  > — Đ5.1 ^vab-ftp-66

- Khi đã áp khung RAROC, hiệu quả đơn vị kinh doanh đánh giá trên lợi nhuận kinh tế: tính kỳ hạn hiệu lực WAT bình quân gia quyền của danh mục khoản vay mới trong kỳ (công thức bị mất khi convert); COF của danh mục nội suy theo WAT trên biểu FTP, riêng cho từng loại tiền; chi phí VCSH = (ROE% − COF%) × vốn RAROC dự kiến × WAT/365.
  > "Trường hợp Ngân hàng đã áp dụng khung RAROC, hiệu quả hoạt động của các bộ phận kinh doanh cần được đánh giá dựa trên cơ sở lợi nhuận kinh tế."
  > "Với n là số lượng khoản vay phát sinh mới trong kỳ tính FTP thuộc danh mục của ĐVKD"
  > "COF (%) =  Interp (WAT, cột tham chiếu kỳ hạn của biểu FTP, cột tham chiếu lãi suất của biểu FTP)"
  > "Lãi suất COF được tính riêng cho từng loại tiền tệ."
  > "Chi phí VCSH = (𝑅𝑂𝐸%  -  𝐶𝑂𝐹%) × 𝑣ố𝑛 𝑅𝐴𝑅𝑂𝐶 𝑑ự 𝑘𝑖ế𝑛 × 𝑊𝐴𝑇/365"
  > "Vốn RAROC dự kiến: Vốn RAROC dự kiến được phân bổ cho từng ĐVKD theo kế hoạch của Ngân hàng."
  > — Đ5.1.b.ii ^vab-ftp-67

- Giá FTP bán vốn cho phần hạn mức chưa sử dụng của thẻ tín dụng, thấu chi và cho vay hạn mức bằng phần bù rủi ro thanh khoản tiềm tàng. Nguồn dẫn BIS (12/2011) về định giá chuyển vốn rủi ro thanh khoản.
  > "Giá FTP bán vốn cho phần hạn mức chưa sử dụng của khoản mục thẻ tín dụng, thấu chi, và cho vay hạn mức bằng chính phần bù rủi ro thanh khoản tiềm tàng."
  > "Ngân hàng thanh toán quốc tế (BIS) đã ban hành văn bản về Định giá chuyển vốn rủi ro thanh khoản tháng 12 năm 2011."
  > — Đ5.2.b ^vab-ftp-68

- Công thức phần bù rủi ro thanh khoản tiềm tàng: có mô hình hành vi về tỷ lệ giải ngân thì = C × P% × tỷ lệ dự trữ thanh khoản × chi phí duy trì TSTK; không có mô hình hành vi thì = C × CCF × tỷ lệ dự trữ thanh khoản × chi phí duy trì TSTK. C là tổng số dư cam kết/hạn mức chưa sử dụng; tỷ lệ dự trữ thanh khoản là đệm thanh khoản thực tế; P% là tỷ lệ giải ngân trên hạn mức chưa giải ngân; CCF theo Điều 10 TT41/2016. Chi phí duy trì TSTK dựa trên VOF bình quân TT1 và lãi suất bình quân TSTK (công thức bị mất khi convert).
  > "Phần bù rủi ro thanh khoản tiềm tàng (Contingent Liquidity charge) = C × P% × Tỷ lệ dự trữ thanh khoản × Chi phí duy trì TSTK"
  > "C × CCF × Tỷ lệ dự trữ thanh khoản × Chi phí duy trì TSTK"
  > "C (Commitment remains): Tổng số dư chưa được sử dụng của các cam kết tiềm tàng (tổng số dư các khoản mục cam kết/hạn mức chưa sử dụng);"
  > "Tỷ lệ dự trữ thanh khoản: là đệm thanh khoản (tỷ lệ dự trữ thanh khoản) thực tế của Ngân hàng;"
  > "P%: Tỷ lệ giải ngân/Tổng hạn mức chưa giải ngân;"
  > "CCF (Credit conversion factor): Hệ số chuyển đổi tín dụng, được xác định theo quy định tại Điều 10 Thông tư 41/2016/TT-NHNN"
  > "Lãi suất bình quân TSTK: là bình quân lãi suất tài sản thanh khoản cao đang được hưởng khi được nắm giữ làm đệm thanh khoản."
  > — Đ5.2.b ^vab-ftp-69

#### Ghi chú convert u02 (bổ sung nhóm 1)
- Công thức WAT (dòng 558) và chi phí duy trì TSTK (dòng 610) mất (`<!-- formula-not-decoded -->`).
- Công thức phần bù tiềm tàng cho trường hợp không có mô hình hành vi bị đẩy xuống dòng 634, nằm lẫn trong mục Điều 6.1.b (tiền gửi), dưới dạng heading.

### u02–u03 (bổ sung 2026-10-21, nhóm 2) — Ma trận sản phẩm: kỳ hiệu lực, tiền gửi TT1, cho vay W.A cố định, quá hạn, gia hạn, sản phẩm ưu đãi, trái phiếu doanh nghiệp

- Với sản phẩm có gốc trả định kỳ, phần bù thanh khoản kỳ hạn dùng lãi suất của kỳ hiệu lực, được định nghĩa là kỳ hạn đã chiết khấu về hiện tại của các dòng lịch trả.
  > "Sản phẩm có số dư gốc trả định kỳ:"
  > "Lãi suất của kỳ hiệu lực"
  > "(là kỳ hạn đã được chiết khấu về hiện tại của các dòng lịch trả)"
  > — Đ4.3.4.b ^vab-ftp-70

- Tiền gửi TT1 gốc trả cuối kỳ (cố định hoặc thả nổi): VOF cơ sở theo kỳ hạn gốc, căn cứ biểu tại ngày phát sinh, cố định suốt thời gian gửi; TLP bằng 0; hỗ trợ huy động theo mục 2.2 Điều 4. VOF cho kỳ hạn ngoài thang chuẩn được nội suy/ngoại suy từ thang chuẩn (MB01). ALCO có thể đổi phương pháp định giá VOF cho từng sản phẩm tiền gửi.
  > "Lãi suất VOF cơ sở tương ứng với kỳ hạn gốc của khoản tiền gửi căn cứ vào biểu lãi suất VOF cơ sở tương ứng tại ngày phát sinh."
  > "Lãi suất VOF cơ sở được áp dụng cố định trong suốt thời gian gửi tiền."
  > "Phần bù thanh khoản kỳ hạn = 0 : Áp dụng trong suốt thời hạn gửi tiền."
  > "Giá mua vốn áp dụng cho các tài sản nợ (VOF) đối với các kỳ hạn không theo thang kỳ hạn chuẩn của biểu ban hành thì được tính nội suy/ngoại suy trực tiếp từ thang kỳ hạn chuẩn."
  > "Hội đồng ALCO có thể quyết định việc thay đổi phương pháp định giá VOF đối với từng sản phẩm tiền gửi"
  > — Đ6.1.a–b ^vab-ftp-71

- Tiền gửi gửi góp: VOF cơ sở = lãi suất huy động gửi góp theo kỳ hạn cộng chênh lệch giữa VOF và lãi suất huy động của tiền gửi gốc trả cuối kỳ cùng kỳ hạn; cố định suốt thời gian gửi; TLP bằng 0.
  > "Lãi suất VOF cơ sở áp dụng tương ứng lãi suất huy động khách hàng theo kỳ hạn gửi cộng mức chênh lệch giữa giá VOF và lãi suất huy động khách hàng cùng kỳ hạn của sản phẩm tiền gửi gốc trả cuối kỳ"
  > "Khách hàng làm hợp đồng tiền gửi 12 tháng, số tiền 120 triệu, gửi góp mỗi tháng 10 triệu."
  > — Đ6.1.c ^vab-ftp-72

- Cho vay gốc trả định kỳ, lãi suất cố định (W.A): COF cơ sở theo kỳ hạn hiệu lực trên biểu tại ngày giải ngân, áp suốt thời gian cho vay; kỳ hạn hiệu lực tính bằng bình quân gia quyền (thời lượng) theo lịch trả gốc (công thức mất khi convert; N số kỳ trả gốc, Pi gốc trả lần i, Ti từ ngày giải ngân tới ngày trả gốc lần i); TLP bằng 0.
  > "Cách xác định lãi suất COF cơ sở : Tương ứng với kỳ hạn hiệu lực căn cứ vào biểu lãi suất COF cơ sở tương ứng tại ngày giải ngân."
  > "Cách xác định kỳ hạn hiệu lực : Áp dụng phương pháp Bình quân gia quyền (Weighted Average) để tính kỳ hạn bình quân (thời lượng) của khoản vay theo công thức như sau:"
  > "Pi: Số dư gốc được thanh toán trong lần i."
  > "Phần bù thanh khoản kỳ hạn = 0 : Áp dụng trong suốt thời hạn cho vay."
  > — Đ6.2.d ^vab-ftp-73

- Cho vay quá hạn: COF cơ sở theo kỳ hạn của khoản vay thông thường trước khi chuyển quá hạn, trên số dư tại thời điểm quá hạn, cố định suốt thời gian quá hạn; sản phẩm ưu đãi quá hạn trong kỳ ưu đãi xử lý như sản phẩm tiêu chuẩn; TLP theo tính chất dòng tiền của khoản vay trước khi quá hạn.
  > "Đối với sản phẩm tiêu chuẩn: Lãi suất COF cơ sở tương ứng với kỳ hạn khoản cho vay thông thường trước khi chuyển thành nợ quá hạn trên số dư hiện tại tại thời điểm quá hạn."
  > "Lãi suất COF cơ sở được áp dụng cố định trong suốt thời gian quá hạn."
  > "Phần bù thanh khoản kỳ hạn :  được xác định theo tính chất dòng tiền của sản phẩm (tương tự như cách xác định của sản phẩm cho vay thông thường trước khi bị chuyển sang nợ quá hạn)"
  > — Đ6.2.g ^vab-ftp-74

- Cho vay gia hạn: COF cơ sở theo kỳ hạn gốc mới (kỳ hạn gốc trước gia hạn cộng thời gian gia hạn) hoặc theo kỳ điều chỉnh lãi suất, tuỳ tính chất dòng tiền; áp suốt thời gian gia hạn hoặc đến ngày điều chỉnh lãi suất tiếp theo; TLP theo tính chất dòng tiền.
  > "Lãi suất COF cơ sở tương ứng với kỳ hạn gia hạn được tham chiếu theo kỳ hạn gốc mới hoặc kỳ điều chỉnh lãi suất (tùy vào tính chất dòng tiền của sản phẩm trước khi gia hạn), trong đó kỳ hạn gốc mới bằng tổng kỳ hạn gốc trước khi gia hạn cộng thời gian gia hạn thêm."
  > "Phần bù thanh khoản kỳ hạn :  Áp dụng theo loại tính chất dòng tiền của sản phẩm. (tương tự như cách xác định của sản phẩm cho vay thông thường)"
  > — Đ6.2.h ^vab-ftp-75

- Cho vay không tiêu chuẩn (có ưu đãi), gốc trả cuối kỳ, lãi suất cố định, hai phương án. Phương án 1 giữ kỳ hạn gốc, chỉ đổi FTP khi hết ưu đãi (ví dụ 5 năm, ưu đãi năm đầu: năm đầu lấy giá hợp đồng 5 năm có kỳ điều chỉnh 12 tháng, 4 năm sau lấy giá 5 năm). Phương án 2 chia thành cấu phần kỳ ưu đãi và ngoài ưu đãi (năm đầu lấy giá 1 năm, 4 năm sau lấy giá 4 năm). TLP bằng 0.
  > "Phương án 1: Chỉ thay đổi lãi suất FTP (tại thời điểm kết thúc ưu đãi), giữ nguyên kỳ hạn gốc."
  > "o 1 năm đầu: lãi suất FTP lấy theo giá của hợp đồng kỳ hạn 5 năm có kỳ điều chỉnh lãi suất 12 tháng"
  > "o 4 năm còn lại : lãi suất FTP lấy theo giá của hợp đồng kỳ hạn 5 năm."
  > "Phương án 2: Chia nhỏ sản phẩm thành các cấu phần riêng lẻ (kỳ ưu đãi và kỳ ngoài ưu đãi) và xác định lãi suất FTP của các cấu phần nhỏ đó."
  > "o 1 năm đầu (trong kỳ ưu đãi): lãi suất FTP lấy theo giá của kỳ hạn 1 năm."
  > "o 4 năm còn lại (ngoài kỳ ưu đãi): lãi suất FTP lấy theo giá của kỳ hạn 4 năm."
  > — Đ6.2.i ^vab-ftp-76

- Trái phiếu doanh nghiệp: giữ đến đáo hạn thì COF cơ sở như khoản vay gốc trả cuối kỳ (cố định hoặc thả nổi). Nắm giữ để kinh doanh hoặc AFS thì COF cơ sở TT1 theo kỳ hạn từ mô hình hành vi, áp suốt thời hạn đầu tư; chưa có mô hình hành vi thì áp như cho vay cố định/thả nổi với kỳ hạn theo quy tắc phân tách sổ kinh doanh của TT41/2016 (thường dưới 1 năm).
  > "Trái phiếu doanh nghiệp lãi suất cố định: lãi suất COF cơ sở áp dụng cho sản phẩm này sẽ tương tự như lãi suất COF cơ sở TT1 áp dụng cho một khoản cho vay có gốc trả cuối kỳ và lãi suất cố định được mô tả ở khoản b điều này."
  > "Đối với trái phiếu doanh nghiệp nắm giữ nhằm mục đích kinh doanh (Trading) hoặc sẵn sàng để bán (AFS ) : lãi suất COF cơ sở của sản phẩm này được xác định theo lãi suất COF cơ sở của TT1 tương ứng với kỳ hạn được tính ra từ mô hình hành vi, áp dụng trong suốt thời hạn đầu tư."
  > "Trong trường hợp Ngân hàng chưa có MHHV(MÔ HÌNH HÀNH VI), Ngân hàng áp dụng cơ chế FTP cho các sản phẩm này tương tự như với các sản phẩm cho vay lãi suất cố định/thả nổi, với kỳ hạn được lấy theo quy tắc phân tách sổ Kinh doanh của Thông tư 41/2016/TT-NHNN (thông thường là dưới 1 năm)."
  > — Đ6.2.m ^vab-ftp-77

#### Ghi chú convert (nhóm 2)
- Công thức TLP cho sản phẩm trả gốc cuối kỳ/định kỳ (dòng 482–501) vỡ thành mảnh rời; công thức chính đã có ở ^vab-ftp-33, ^vab-ftp-34.
- Công thức kỳ hạn hiệu lực W.A (dòng 748) và cho kỳ sau ưu đãi (dòng 938) mất.
- Ví dụ gửi góp (dòng 645) mất dấu trừ: "(VOF tiền gửi gốc trả cuối kỳ 12M lãi suất tiền gửi gốc trả cuối kỳ 12M)".

### u01, u02, u05 (bổ sung 2026-10-21, nhóm 3) — Phạm vi, căn cứ, hỗ trợ huy động, tổng tài sản bị tính FTP, minh hoạ đường cong cơ sở, hỗ trợ huy động, BHTG, DTBB

- Phạm vi: quy định điều chỉnh điều chuyển vốn nội bộ giữa CFU và các đơn vị kinh doanh trên toàn hệ thống, áp cho cả thị trường 1 và thị trường 2. Văn bản liên quan gồm TT13/2018 (kiểm soát nội bộ), TT22/2019 (giới hạn, tỷ lệ an toàn), TT24/2014 (bảo hiểm tiền gửi), TT30/2019 (dự trữ bắt buộc).
  > "Quy định này điều chỉnh hoạt động điều chuyển vốn nội bộ giữa trung tâm vốn ('CFU') và các đơn vị kinh doanh trên toàn hệ thống VietABank."
  > "Quy định này áp dụng cho tất cả các giao dịch điều chuyển vốn giữa Hội sở và các đơn vị kinh doanh (áp dụng cho cả thị trường 1 và thị trường 2)."
  > "Thông tư 13/2018/TT-NHNN của Ngân hàng Nhà nước Việt Nam quy định về hệ thống kiểm soát nội bộ của ngân hàng thương mại, chi nhánh ngân hàng nước ngoài."
  > "Thông tư 22/2019/TT-NHNN của Ngân hàng Nhà nước Việt Nam quy định các giới hạn, tỷ lệ bảo đảm an toàn trong hoạt động của ngân hàng, chi nhánh ngân hàng nước ngoài."
  > "Thông tư 30/2019/TT-NHNN của Ngân hàng Nhà nước Việt Nam quy định về thực hiện dự trữ bắt buộc của các tổ chức tín dụng"
  > — Đ1.2, Đ2 ^vab-ftp-78

- Lãi suất FTP cơ sở của ngoại tệ khác xác định theo phương pháp của USD.
  > "Dựa trên thực trạng thông tin của ngân hàng thì lãi suất FTP cơ sở của các loại ngoại tệ khác được xác định theo phương pháp xác định lãi suất FTP cơ sở đối với USD."
  > — Đ4.2.1.iii ^vab-ftp-79

- Hỗ trợ huy động: phần ALCO dùng để tạo động lực cho đơn vị huy động vốn; chi tiết theo loại tiền và kỳ hạn tuỳ mức chi tiết của kế hoạch kinh doanh; tính vào đầu năm (có thể điều chỉnh bán niên hoặc hằng quý khi kế hoạch thay đổi); tính riêng cho từng loại tiền. Đầu vào NII vay gửi: NII kế hoạch từ cho vay và tiền gửi (gồm trái phiếu doanh nghiệp), tổng chi phí quản lý của hoạt động cho vay và tiền gửi, chi phí dự phòng rủi ro tín dụng năm kế hoạch.
  > "Hỗ trợ huy động là phần Hội đồng ALCO muốn tạo động lực cho các đơn vị kinh doanh thông qua việc tính cho các đơn vị huy động vốn một mức lợi nhuận nhất định"
  > "Việc xác định hỗ trợ huy động cho các loại tiền tệ khác nhau và các kỳ hạn khác nhau được áp dụng dựa vào mức độ chi tiết của kế hoạch kinh doanh có thể phân bổ."
  > "Chi phí này được tính toán vào đầu năm (hoặc có thể điều chỉnh bán niên/hàng quý trong trường hợp có thay đổi về kế hoạch kinh doanh)."
  > "Chi phí này được tính riêng biệt cho từng loại tiền tệ."
  > "NII kế hoạch: Thu nhập lãi thuần kế hoạch từ hoạt động cho vay và tiền gửi của toàn ngân hàng theo kế hoạch năm dữ liệu tính (bao gồm trái phiếu doanh nghiệp);"
  > "Chi phí dự phòng rủi ro tín dụng năm kế hoạch: Chi phí dự phòng rủi ro tín dụng theo kế hoạch của năm dữ liệu tính năm kế hoạch, bao gồm chi phí dự phòng rủi ro chung và dự phòng cụ thể."
  > — Đ4.2.2 ^vab-ftp-80

- Tổng tài sản bị tính FTP = tổng tài sản − tài sản thanh khoản − tài sản ghi nhận cho Khối QL&KDV − tài sản có khác; dùng bình quân 3 tháng liền kề. Lý do loại trừ: TSTK đã phân bổ vào COF qua phần bù TSTK; tài sản Khối QL&KDV mua bán theo cơ chế TT2; tài sản có khác (gồm tài sản cố định) được tài trợ bằng VCSH.
  > "Bình quân Tổng tài sản bị tính FTP: được xác định bằng bình quân số dư tổng tài sản bị tính FTP trong 3 tháng liền kề thời điểm tính."
  > "Tổng tài sản bị tính FTP =  Tổng tài sản -Tài sản thanh khoản -Tài sản ghi nhận cho Khối QL&amp;KDV -Tài sản có khác"
  > "Tài sản thanh khoản cao do đã được phân bổ vào giá bán vốn COF qua cấu phần Phần bù cho tài sản thanh khoản, do đó cần loại trừ khỏi Tổng tài sản bị tính FTP."
  > "Tài sản ghi nhận cho Khối QL&amp;KDV được mua bán theo cơ chế FTP cho thị trường 2,"
  > "Tài sản có khác không được mua bán qua cơ chế FTP mà được tài trợ bởi VCSH, do"
  > "Tài sản có khác: Bao gồm tài sản cố định và các tài sản có khác."
  > — Đ4.3.1.b ^vab-ftp-81

- Minh hoạ đường cong cơ sở. VND: lãi suất huy động thực tế bình quân theo kỳ hạn dùng làm lãi suất giả định. USD: LIBOR bình quân 3 tháng cho kỳ ngắn, IRS bình quân 3 tháng cho 12M trở lên; kỳ 14D, 21D không có dữ liệu được gán 0.10 (bằng 7D); từ 24M lấy theo IRS.
  > "Bước 1. Thu thập bảng Lãi suất huy động thực tế bình quân của Ngân hàng"
  > "Chi tiết tham khảo file excel sheet 'Base\_curve\_VND', 'Base\_curve\_USD'."
  > — PL02 mục 1.b ^vab-ftp-82

| Lãi suất (%) | NM | 7D | 14D | 21D | 1M | 2M | 3M | … | 12M | 24M | 36M | 48M | 60M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VND lãi suất huy động thực tế bình quân = lãi suất giả định | 2.02 | 2.24 | 2.44 | 2.46 | 2.70 | 2.92 | 3.22 | … | 4.53 | 2.72 | 2.83 | 2.96 | 3.08 |
| USD LIBOR bình quân 3 tháng | 0.08 | 0.10 | | | 0.15 | 0.18 | 0.23 | … | 0.36 | | | | |
| USD IRS bình quân 3 tháng | | | | | | | | | 0.22 | 0.24 | 0.27 | 0.32 | 0.40 |
| USD lãi suất giả định | 0.08 | 0.10 | 0.10 | 0.10 | 0.15 | 0.18 | 0.23 | … | 0.36 | 0.24 | 0.27 | 0.32 | 0.40 |

- Minh hoạ hỗ trợ huy động (năm kế hoạch 2020): NII kế hoạch 23,7 tỷ; chi phí hoạt động huy động 5,64 tỷ và cho vay 4,23 tỷ; dự phòng 8,1 tỷ; cơ cấu NIM huy động/cho vay 50%/50%; số dư huy động bình quân 701 tỷ, dư nợ bình quân 664,8 tỷ. NII vay gửi = 5,73 tỷ. Công thức tỷ lệ NIM vay gửi và hỗ trợ huy động bị mất khi convert.
  > "Năm kế hoạch"
  > "Bước 2. Tính toán hỗ trợ huy động"
  > "- (5,640,000,000 + 4,230,000,000)"
  > — PL02 mục 2.b ^vab-ftp-83

| Thông tin | Giá trị |
|---|---|
| Thu nhập lãi thuần toàn hàng NII kế hoạch từ tiền gửi và cho vay | 23,700,000,000 |
| Tổng chi phí hoạt động của huy động vốn năm kế hoạch | 5,640,000,000 |
| Tổng chi phí hoạt động của cho vay năm kế hoạch | 4,230,000,000 |
| Chi phí dự phòng rủi ro tín dụng năm kế hoạch | 8,100,000,000 |
| Cơ cấu NIM cho huy động (n1) / cho vay (n2) | 50% / 50% |
| Số dư huy động vốn bình quân | 701,000,000,000 |
| Dư nợ bình quân | 664,800,000,000 |
| NII vay gửi | 5,730,000,000 |

- Minh hoạ chi phí BHTG: đầu vào là chi phí BHTG thực tế cuối tháng 3 tháng liền kề và tổng tài sản bị tính FTP 3 tháng liền kề. Tổng 3 tháng 85.424.439.251; quy đổi năm ×4 = 341.697.757.003; chia "bình quân tổng tài sản tính FTP" 643.285.217.739.938, ra 0,05%. Bảng dữ liệu tính tài sản tính FTP = tổng tài sản − tài sản TT2 của Khối QL&KDV − tài sản thanh khoản cao.
  > "Chi phí bảo hiểm tiền gửi thực tế phải trả cuối tháng của Ngân hàng trong 3 tháng liền kề trước thời điểm tính toán"
  > "= 85,424,439,251 × 4"
  > "= 341,697,757,003/643,285,217,739,938"
  > — PL02 mục 3 ^vab-ftp-84

| Chỉ mục | Giá trị | Ghi chú |
|---|---|---|
| Tổng chi phí BHTG cho VND (3 tháng gần nhất) | 85,424,439,251 | |
| Quy đổi cả năm | 341,697,757,003 | = 85,424,439,251 × 4 |
| Bình quân tổng tài sản tính FTP | 643,285,217,739,938 | |
| Chi phí BHTG (%) | 0.05% | = 341,697,757,003/643,285,217,739,938 |
| Ví dụ dòng 31/12/2019: Tổng tài sản / Tài sản TT2 / TSTK / Tài sản tính FTP | 643,285,217,739,938 / 614,233,544,561 / 6,303,075,979,333 / 636,367,908,216,044 | |

- Minh hoạ chi phí DTBB: đầu vào là số dư DTBB tối thiểu VND theo yêu cầu NHNN 3 tháng liền kề và tổng tài sản bị tính FTP. Yêu cầu DTBB bình quân 13.100.233.516.399; lãi suất DTBB "-"; lãi suất FTP mua vốn bình quân 4,17; bình quân tổng tài sản VND bị tính FTP 677.919.886.993.106; chi phí DTBB ghi 0,00%.
  > "Chi phí dự trữ bắt buộc tối thiểu theo yêu cầu của NHNN trong 3 tháng liền kề trước thời điểm tính"
  > "Bước 2. Tính toán chi phí dự trữ bắt buộc"
  > — PL02 mục 4 ^vab-ftp-85

| Yêu cầu DTBB bình quân | Lãi suất DTBB | Lãi suất FTP mua vốn bình quân | Bình quân tổng tài sản VND bị tính FTP | Chi phí DTBB |
|---|---|---|---|---|
| 13,100,233,516,399 | - | 4.17 | 677,919,886,993,106 | 0.00% |

#### Ghi chú convert (nhóm 3)
- Công thức tỷ lệ NIM vay gửi và hỗ trợ huy động (dòng 317, 321, 1450, 1454) mất.
- Bảng đường cong VND (dòng 1367): 12M 4.53 rồi 24M 2.72 — giảm đột ngột, khác giá trị 24M = 4.81 ở ví dụ TLP (dòng 1622); nghi số liệu minh hoạ không nhất quán.

### u03 (bổ sung 2026-10-21, nhóm 4) — Cho vay lãi suất thả nổi (Đ6.2.c, e) và sản phẩm ưu đãi (Đ6.2.j, k, l)

- Cho vay trả gốc cuối kỳ, lãi suất thả nổi: COF cơ sở theo kỳ hạn tái định giá trên biểu của đồng tiền và sản phẩm tại ngày giải ngân hoặc ngày điều chỉnh lãi suất, áp đến ngày điều chỉnh lãi suất tiếp theo; TLP theo kỳ hạn gốc và tần suất điều chỉnh lãi suất, bằng lãi suất kỳ hạn gốc trừ lãi suất kỳ tái định giá, áp đến ngày điều chỉnh lãi suất tiếp theo.
  > "Cách xác định lãi suất COF cơ sở : Tương ứng với kỳ hạn tái định giá của khoản cho vay căn cứ vào biểu lãi suất COF cơ sở áp dụng cho đồng tiền và sản phẩm cho vay tương ứng tại ngày giải ngân hoặc ngày điều chỉnh lãi suất."
  > "Lãi suất COF cơ sở được áp dụng đến ngày điều chỉnh lãi suất tiếp theo của hợp đồng tín dụng."
  > "Phần bù thanh khoản kỳ hạn : Được xác định tương ứng với kỳ hạn gốc (bằng ngày đáo hạn trừ ngày giải ngân) và tần suất điều chỉnh lãi suất của khoản cho vay tương ứng tại ngày giải ngân hoặc ngày điều chỉnh lãi suất gần nhất."
  > "Phần bù thanh khoản kỳ hạn được áp dụng đến ngày điều chỉnh lãi suất tiếp theo."
  > — Đ6.2.c ^vab-ftp-86

- Cho vay trả gốc định kỳ, lãi suất thả nổi: COF cơ sở theo kỳ tái định giá tại ngày giải ngân hoặc ngày điều chỉnh lãi suất, áp đến ngày điều chỉnh lãi suất tiếp theo; TLP theo kỳ hạn hiệu lực (bình quân gia quyền) và tần suất điều chỉnh, bằng lãi suất kỳ hạn hiệu lực trừ lãi suất kỳ tái định giá. Công thức kỳ hạn hiệu lực bị mất khi convert.
  > "Cách xác định lãi suất COF cơ sở : Tương ứng với kỳ hạn tái định lại lãi suất của khoản cho vay tương ứng tại ngày giải ngân hoặc ngày điều chỉnh lãi suất."
  > "Được xác định tương ứng với kỳ hạn hiệu lực (được xác định theo phương pháp bình quân gia quyền - Weighted Average) và tần suất điều chỉnh lãi suất của khoản cho vay"
  > "Phần bù thanh khoản kỳ hạn = Lãi suất của kỳ hạn hiệu lực - Lãi suất của kỳ hạn tái định lại lãi suất"
  > — Đ6.2.e ^vab-ftp-87

- Cho vay ưu đãi, trả gốc cuối kỳ, lãi suất thả nổi. Ví dụ hợp đồng 5 năm, cố định 1 năm đầu, 4 năm sau thả nổi 3 tháng/lần. Phương án 1 giữ kỳ hạn gốc, chỉ đổi kỳ điều chỉnh: năm đầu giá kỳ hạn 5 năm kỳ điều chỉnh 12 tháng, 4 năm sau giá kỳ hạn 5 năm kỳ điều chỉnh 3 tháng. Phương án 2 tách cấu phần: năm đầu giá kỳ hạn 1 năm, 4 năm sau giá kỳ hạn 4 năm kỳ điều chỉnh 3 tháng. Trong kỳ ưu đãi: COF theo kỳ ưu đãi tại ngày giải ngân, cố định, TLP bằng 0. Ngoài kỳ ưu đãi: COF theo kỳ tái định giá tại ngày sau ngày kết thúc ưu đãi; TLP bằng lãi suất kỳ hạn gốc sau ưu đãi (ngày đáo hạn trừ ngày kết thúc ưu đãi) trừ lãi suất kỳ tái định giá.
  > "Phương án 1: Chỉ xác định lại kỳ điều chỉnh lãi suất FTP, giữ nguyên kỳ hạn gốc. Ví dụ: Hợp đồng trả gốc cuối kỳ 5 năm cố định lãi suất trong 1 năm đầu, 4 năm còn lại thả nổi 3 tháng/lần."
  > "o 4 năm còn lại: lãi suất FTP lấy theo giá của hợp đồng kỳ hạn 5 năm kỳ điều chỉnh lãi suất 3 tháng."
  > "o 4 năm còn lại (ngoài kỳ ưu đãi) : lãi suất FTP lấy theo giá của hợp đồng kỳ hạn 4 năm kỳ điều chỉnh lãi suất 3 tháng/lần ."
  > "o Lãi suất COF cơ sở : Tương ứng với kỳ hạn tái định lại lãi suất của khoản cho vay căn cứ vào biểu lãi suất COF cơ sở tương ứng tại ngày sau ngày kết thúc ưu đãi."
  > "Phần bù thanh khoản kỳ hạn = Lãi suất của kỳ hạn gốc sau ưu đãi (ngày đáo hạn - ngày kết thúc ưu đãi) - Lãi suất của kỳ hạn tái định lại lãi suất"
  > — Đ6.2.j ^vab-ftp-88

- Cho vay ưu đãi, trả gốc định kỳ, lãi suất cố định. Phương án 1 giữ kỳ hạn hiệu lực tính theo kỳ gốc, chỉ đổi lãi suất FTP khi hết ưu đãi (ví dụ 5 năm: năm đầu giá kỳ hiệu lực của 5 năm có kỳ điều chỉnh 12 tháng, 4 năm sau giá kỳ hiệu lực của 5 năm). Phương án 2 tách cấu phần (năm đầu giá kỳ hạn 1 năm, 4 năm sau giá kỳ hiệu lực của 4 năm). Ngoài kỳ ưu đãi: COF theo kỳ hạn hiệu lực sau ưu đãi, tính bình quân gia quyền với Ti đo từ ngày hết hạn ưu đãi, cố định đến ngày đáo hạn; TLP bằng 0.
  > "Phương án 1: Chỉ thay đổi lãi suất FTP (tại thời điểm kết thúc ưu đãi), giữ nguyên kỳ hạn hiệu lực được tính dựa vào kỳ gốc."
  > "o 4 năm còn lại (ngoài ưu đãi): lãi suất FTP lấy theo giá của hợp đồng kỳ hạn hiệu lực được tính dựa vào 4 năm."
  > "o Lãi suất COF cơ sở : Tương ứng với kỳ hạn hiệu lực sau ưu đãi, được căn cứ vào biểu lãi suất COF cơ sở tương ứng tại ngày sau ngày kết thúc ưu đãi."
  > "Ti: Kỳ hạn của mỗi dòng tiền gốc được thanh toán trong lần i = ngày thanh toán gốc lần i trừ ( ̶ ) ngày hết hạn ưu đãi."
  > "o Thời hạn hiệu lực của lãi suất COF cơ sở: lãi suất COF cơ sở được hệ thống xác định cố định từ ngày kết thúc ưu đãi đến ngày đáo hạn của khoản cho vay."
  > — Đ6.2.k ^vab-ftp-89

- Cho vay ưu đãi, trả gốc định kỳ, lãi suất thả nổi. Phương án 1 giữ kỳ hạn hiệu lực tính theo kỳ gốc, chỉ đổi kỳ điều chỉnh (năm đầu: kỳ hiệu lực của 5 năm, kỳ điều chỉnh 12 tháng; 4 năm sau: kỳ điều chỉnh 3 tháng). Phương án 2 tách cấu phần (năm đầu kỳ hạn 1 năm; 4 năm sau kỳ hiệu lực của 4 năm, kỳ điều chỉnh 3 tháng). Ngoài kỳ ưu đãi: COF theo kỳ tái định giá tại ngày sau ngày kết thúc ưu đãi, áp đến ngày điều chỉnh tiếp theo; TLP bằng lãi suất kỳ hạn hiệu lực tính từ khoảng thời gian sau ưu đãi trừ lãi suất kỳ tái định giá.
  > "o 4 năm còn lại: lãi suất FTP lấy theo giá của hợp đồng kỳ hạn hiệu lực được tính dựa vào 5 năm có kỳ điều chỉnh lãi suất là 3 tháng."
  > "o 4 năm còn lại (ngoài ưu đãi): lãi suất FTP lấy theo giá của hợp đồng kỳ hạn hiệu lực được tính dựa vào 4 năm có kỳ điều chỉnh lãi suất là 3 tháng."
  > "o Lãi suất COF cơ sở : Tương ứng với kỳ hạn tái định giá của khoản cho vay tương ứng tại ngày sau ngày kết thúc ưu đãi."
  > "Phần bù thanh khoản kỳ hạn = Lãi suất của kỳ hạn hiệu lực được tính từ khoản thời gian sau ưu đãi - Lãi suất của kỳ hạn tái định lại lãi suất"
  > — Đ6.2.l ^vab-ftp-90

#### Ghi chú convert (nhóm 4)
- Công thức kỳ hạn hiệu lực W.A ở Đ6.2.e (dòng 773), Đ6.2.k (dòng 901) và Đ6.2.l (sau dòng 934) mất (`<!-- formula-not-decoded -->`); hình minh hoạ ở dòng 734, 765, 857, 883, 912 không convert.
- Dòng 739 (Đ6.2.c) và 916 (Đ6.2.l) bị gắn số thứ tự lạ "4." và "3." trước nội dung.

### u04 (bổ sung 2026-10-21, nhóm 5) — Đ7.3 cổ phiếu chiến lược, Đ7.4 tài sản khác, Điều 8 thay đổi giá mua bán vốn

- Cổ phiếu đầu tư dài hạn (chiến lược): VAB dẫn Luật 47/2010 Điều 103, TCTD không được kinh doanh cổ phiếu, chỉ nắm giữ để đầu tư dài hạn. COF cơ sở TT1 theo kỳ hạn nắm giữ dự kiến theo chiến lược ban đầu; chưa xác định được thì theo kỳ hạn nhận cổ tức hằng năm (≥ 1 năm) hoặc theo thông lệ đưa vào dải kỳ hạn trên 5 năm (≥ 5 năm); cố định suốt thời gian giao dịch.
  > "Hiện tại theo quy định của NHNN, các TCTD không được phép kinh doanh Cổ phiếu (Theo Luật Ngân hàng 47/2010/QH12 ngày 16/06/2010 - Điều 103 về Góp vốn mua cổ phần) mà chỉ"
  > "Cách xác định lãi suất COF cơ sở: Lãi suất COF cơ sở TT1 tương ứng với kỳ hạn nắm giữ danh mục dự kiến theo chiến lược kinh doanh đã đặt ra ban đầu Hoặc trong trường hợp chưa xác định được kỳ hạn dự kiến thì áp dụng 1 trong 2 phương án sau:"
  > "Theo kỳ hạn nhận cổ tức hàng năm (≥ 1 năm);"
  > "Theo thông lệ sẽ đưa vào dải kỳ hạn  trên 5 năm (≥ 5 năm) đối với các khoản mục đầu tư góp vốn mang tính chiến lược/dài hạn."
  > "Lãi suất COF cơ sở được áp dụng cố định trong suốt thời gian giao dịch"
  > — Đ7.3 ^vab-ftp-91

- Tài sản nợ và tài sản có khác: VAB áp cách tiếp cận mua bán một phần bảng cân đối nên không tính FTP cho khoản mục này; khoản mục được tài trợ bằng VCSH. Nếu muốn tính FTP thì chuyển sang mua bán toàn bộ bảng cân đối: lấy % số dư theo thang kỳ hạn của báo cáo gap thanh khoản nhân lãi suất FTP từng thang rồi cộng lại.
  > "Ngân hàng áp dụng phương pháp tiếp cận mua bán một phần bảng cân đối kế toán, do đó không tính FTP cho khoản mục này."
  > "Khoản mục này được tài trợ bởi nguồn VCSH, do đó, phần thặng dư của VCSH sau khi được khấu trừ khoản mục tài sản khác sẽ được tính FTP."
  > "Nói cách khác, Ngân hàng (1) xác định % số dư ở từng thang kỳ hạn của khoản mục tài sản khác, sau đó (2) Ngân hàng lấy % số dư tại từng thang kỳ hạn (ở (1)) nhân với lãi suất FTP tương ứng với thang kỳ hạn đó."
  > — Đ7.4 ^vab-ftp-92

- Tiền gửi đổi tần suất xác định lãi suất (ví dụ 3 tháng/lần sang 6 tháng/lần): vào ngày thay đổi, hệ thống FTP tính lại VOF theo tần suất mới và lãi suất VOF cơ sở, phần bù thanh khoản tại ngày điều chỉnh; VOF mới áp từ ngày thay đổi.
  > "Trong trường hợp thay đổi tần suất xác định lãi suất (ví dụ từ thay đổi 3 tháng/lần thành 6 tháng/lần), vào ngày thay đổi tần suất xác định lãi suất, hệ thống FTP sẽ tính lại giá VOF của khoản tiền gửi căn cứ vào:"
  > "Lãi suất VOF mới sẽ được áp dụng từ ngày thay đổi tần suất xác định lãi suất."
  > — Đ8.1.a–b ^vab-ftp-93

- Điều chỉnh thủ công giá mua vốn và giá bán vốn: ngoài các trường hợp đã nêu, ALCO xem xét cho phép điều chỉnh khi có sai sót tính toán/hạch toán FTP, khi luật, quy định hoặc biến động thị trường làm giá biến động trên dưới ±0.2% so với giá FTP hiện tại, hoặc trường hợp khác do ALCO xác định. Mức biến động xác định theo quan sát lịch sử và phương pháp chuyên gia.
  > "Ngoài các trường hợp nêu tại mục 1 Điều này, ALCO sẽ xem xét cho phép điều chỉnh giá mua vốn nếu:"
  > "Do sự thay đổi của luật, quy định hoặc biến động thị trường dẫn tới sự biến động lớn trên dưới +/- 0.2% 1 so với giá FTP hiện tại."
  > "Ngoài các trường hợp nêu tại mục 2 Điều này, ALCO sẽ xem xét cho phép điều chỉnh giá bán vốn nếu:"
  > "1 Mức biến động được xác định dựa trên quan sát lịch sử và phương pháp chuyên gia theo thông lệ áp dụng trên thị trường."
  > — Đ8.1.c, Đ8.2.f ^vab-ftp-94

- Tiền gửi có kỳ hạn tái tục trên TT1: VOF cơ sở theo phương án không áp dụng mô hình hành vi, xác định như tiền gửi phát sinh mới, dùng biểu cập nhật tại thời điểm tái tục; cố định suốt thời gian gửi.
  > "Cách xác định lãi suất VOF cơ sở: Được xác định theo phương án không áp dụng MHHV(MÔ HÌNH HÀNH VI):"
  > "Biểu lãi suất VOF áp dụng là biểu lãi suất mới cập nhật tại thời điểm tái tục."
  > — Đ8.1.d ^vab-ftp-95

- Khoản vay đổi tần suất xác định lãi suất hoặc đổi lịch thanh toán gốc (sản phẩm trả gốc định kỳ, cố định): hệ thống FTP tính lại COF vào ngày thay đổi, căn cứ tần suất mới hoặc lịch trả nợ mới và lãi suất COF cơ sở (cùng phần bù thanh khoản kỳ hạn khi đổi tần suất); COF mới áp từ ngày điều chỉnh.
  > "Trong trường hợp thay đổi tần suất xác định lãi suất, vào ngày thay đổi tần suất xác định lãi suất, hệ thống FTP sẽ tính lại giá COF của khoản cho vay căn cứ vào:"
  > "Lãi suất COF cơ sở, phần bù thanh khoản kỳ hạn tại ngày điều chỉnh tần suất xác định lãi suất."
  > "Lãi suất COF được áp dụng từ ngày điều chỉnh thay đổi lịch thanh toán gốc."
  > — Đ8.2.a–b ^vab-ftp-96

- Khoản vay đổi loại hình lãi suất (cố định sang thả nổi hoặc ngược lại), cơ cấu lại đồng tiền nhận nợ, hoặc đổi hình thức trả gốc (một lần sang trả dần hoặc ngược lại): COF mới xác định tại thời điểm thay đổi căn cứ loại hình lãi suất hoặc hình thức trả gốc mới, lịch trả nợ, tần suất xác định lãi suất, lãi suất COF cơ sở và TLP tại ngày thay đổi; đổi đồng tiền thì chấm dứt COF trên tài khoản cũ và tính COF trên tài khoản đồng tiền mới. COF mới áp từ ngày thay đổi.
  > "Trong trường hợp khoản cho vay được điều chỉnh thay đổi loại hình lãi suất (ví dụ từ cố định sang thả nổi hoặc ngược lại), giá COF mới sẽ được xác định tại thời điểm thay đổi phù hợp với đối tượng khách hàng, loại đồng tiền và sản phẩm cho vay căn cứ vào:"
  > "Lãi suất COF cơ sở, phần bù thanh khoản kỳ hạn tại ngày thay đổi loại hình lãi suất. Hệ thống sẽ áp giá COF mới kể từ ngày thay đổi loại hình lãi suất."
  > "Trong trường hợp cơ cấu lại đồng tiền nhận nợ, việc tính toán giá COF đối với khoản cho vay bằng đồng tiền cũ (trên tài khoản cho vay cũ) sẽ chấm dứt và chuyển sang tính toán giá COF đối với khoản cho vay bằng đồng tiền mới (trên tài khoản cho vay mới)."
  > "Hệ thống sẽ áp giá COF mới kể từ ngày thay đổi hình thức trả gốc."
  > — Đ8.2.c–e ^vab-ftp-97

### u06–u07 (bổ sung 2026-10-21, nhóm 6) — Điều 15 kỳ tính FTP, Phụ lục 04 khung báo cáo NII/NIM hằng ngày và giải thích chu kỳ tính phí PL03

- Kỳ tính FTP (Điều 15): Tùy thuộc vào quy trình vận hành FTP mà kỳ tính FTP được xác định theo 1 trong 2 phương án: (1) Từ ngày 25 của tháng trước đến hết ngày 25 của tháng hiện tại; hoặc (2) Từ đầu tháng đến cuối tháng.
  > "Tùy thuộc vào quy trình vận hành FTP mà kỳ tính FTP được xác định theo một trong hai phương án sau:"
  > "1. Từ ngày 25 của tháng trước đến hết ngày 25 của tháng hiện tại;"
  > "2. Từ đầu tháng đến cuối tháng"
  > — Đ15 ^vab-ftp-98

- Khung báo cáo FTP (PL04): Báo cáo tổng hợp NII/NIM cấp đơn vị kinh doanh và cấp độ cụm chi nhánh được lập với tần suất hằng ngày cho tất cả các loại tiền tệ, cung cấp thông tin so sánh NIM, giá trị FTP ròng và NII. Do đó, chi phí FTP (bao gồm phần bù rủi ro thanh khoản tiềm tàng) được trích dồn hằng ngày (daily accrual) vào kết quả kinh doanh của ĐVKD.
  > "Báo cáo tổng hợp NII/NIM - Cấp đơn vị kinh doanh"
  > "Cung cấp thông tin so sánh NIM theo các cấp độ đơn vị kinh doanh"
  > "Các tham số trong báo cáo tổng hợp được nêu ra như dưới đây: Đơn vị kinh doanh, giá trị FTP, thu nhập lãi/chi phí lãi, giá trị NII và NIM"
  > "Hàng ngày"
  > — PL04 mục I.1 ^vab-ftp-99

#### Ghi chú convert (nhóm 5)
- Dòng 1016–1017 (Đ7.3) bị gắn số thứ tự "3." và "4." trước gạch đầu dòng; dòng 1036 gắn nhãn "b." vào câu thuộc mục a; chú thích "1" của ngưỡng ±0.2% dính vào câu ở dòng 1046.

## Khái niệm và Liên kết
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ giữa BU và CFU.
- [[ftp-pricing-methodology]]: Phân tích chuyên sâu phương pháp luận định giá VOF/COF và phụ phí tuân thủ ngân hàng.
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn điều tiết rủi ro thanh khoản, lãi suất và tín dụng của FTP.
- [[liquidity-transfer-pricing]]: Cơ chế định giá điều chuyển thanh khoản tổng quát theo Moorad Choudhry.
- [[lcr]]: Đệm tài sản thanh khoản chất lượng cao theo chuẩn mực quốc tế.

## Node bị ảnh hưởng
- u01, u02, u05 bổ sung nhóm 3 [2026-10-21]: cập nhật [[ftp-pricing-methodology]] (draft).
- u02–u03 bổ sung nhóm 2 [2026-10-21]: cập nhật [[ftp-pricing-methodology]] (draft).
- u02 bổ sung nhóm 1 [2026-10-21]: cập nhật [[ftp-pricing-methodology]], [[funds-transfer-pricing]] (draft).
- u04 bổ sung [2026-10-21]: cập nhật [[ftp-pricing-methodology]], [[alm-operating-model]] (draft); đánh dấu `ftp-curve-construction-methodology` (synthesis).
- u06–u07 bổ sung [2026-10-21]: cập nhật [[ftp-pricing-methodology]], [[alco]], [[alm-operating-model]], [[internal-funding-curve]] (draft); đánh dấu `ftp-curve-construction-methodology` (synthesis).
- u06–u07 bổ sung nhóm 6 [2026-10-21]: cập nhật [[ftp-pricing-methodology]].

## Mâu thuẫn ghi nhận
- Nội bộ nguồn, minh hoạ PL02: đường cong VND 24M = 2.72 (^vab-ftp-82) khác 24M = 4.81 ở ví dụ TLP (^vab-ftp-47); ví dụ BHTG dùng tổng tài sản ngày đầu làm "bình quân tổng tài sản tính FTP" và không trừ tài sản có khác, khác định nghĩa ^vab-ftp-81 (^vab-ftp-84); ví dụ DTBB ghi 0.00% dù đầu vào cho khoảng 0.08% (^vab-ftp-85). Ghi ở [[ftp-pricing-methodology]].
- Nội bộ nguồn, PL05: cột thời gian ghi biểu FTP TT1 cập nhật "Hàng quý/khi có yêu cầu", bước 3 và 5 ghi ban hành "Giải pháp FTP hàng tháng" (^vab-ftp-49, ^vab-ftp-50). Ghi callout ở [[ftp-pricing-methodology]].
