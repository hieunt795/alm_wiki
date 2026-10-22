---
title: "COF — Chi phí vốn và Giá bán vốn FTP cho tài sản (Cost of Funds)"
aliases: [Cost of Funds, COF, Chi phí vốn, Giá bán vốn FTP, Biểu giá bán vốn cho tài sản tín dụng]
type: metric
domains: [alm, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-vab-ftp]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-clip-ldr-credit-turnover-bottleneck]]"]
relations:
  - {type: part-of, to: "[[funds-transfer-pricing]]", cite: "[[src-vab-ftp#^vab-ftp-7]]"}
  - {type: input-to, to: "[[loan-pricing]]", cite: "[[src-choudhry-principles-banking#^choudhry-strat-16]]"}
  - {type: input-to, to: "[[net-interest-margin]]", cite: "[[src-choudhry-principles-banking#^choudhry-nim-12]]"}
tags: [ftp, metric, cost-of-funds, alm]
updated: 2026-10-19
reviewed:
---

## Định nghĩa

Cost of Funds (COF — Chi phí vốn) trong quản trị ngân hàng mang bản chất kép tùy thuộc vào giác độ tiếp cận [[src-vab-ftp#^vab-ftp-21]] [[src-choudhry-principles-banking#^choudhry-kri-7]]:

1. **Trong cơ chế định giá điều chuyển vốn nội bộ (FTP)**: COF là mức lãi suất mà các Đơn vị Kinh doanh (ĐVKD) sử dụng vốn (cho vay, đầu tư) phải trả cho Đơn vị Quản trị Vốn Tập trung (Central Funding Unit — CFU / Treasury) khi CFU bán vốn để ĐVKD tài trợ cho các tài sản có [[src-vab-ftp#^vab-ftp-21]]. COF phản ánh toàn diện chi phí vốn biên tế để tài trợ tài sản, bao gồm lãi suất thị trường cơ sở, chi phí thanh khoản và các chi phí tuân thủ pháp lệnh của cơ quan quản lý [[src-vab-ftp#^vab-ftp-7]].
2. **Trong quản trị tài chính và tối ưu hóa bảng cân đối ALM tổng thể**: Cost of Funds (Chi phí huy động vốn bình quân toàn hàng) là một chỉ số hiệu suất trọng yếu (KPI) đo lường việc đạt mục tiêu chiến lược và ngân sách tài chính của ngân hàng [[src-choudhry-principles-banking#^choudhry-kri-7]], đồng thời đóng vai trò là hàm mục tiêu tối thiểu hóa trong bài toán tối ưu hóa cấu trúc sổ ngân hàng (Banking Book Optimisation) có ràng buộc [[src-lubinska-alm-optimisation#^lubinska-u07-1]] [[src-lubinska-alm-optimisation#^lubinska-u07-2]].

## Công thức

### 1. Cấu trúc Biểu giá Bán vốn FTP cho Tài sản (COF)

Theo phương pháp luận điều chuyển vốn hai chiều tại các ngân hàng thương mại Việt Nam, Biểu giá bán vốn COF áp dụng cho tài sản tín dụng được cấu thành từ 7 thành phần [[src-vab-ftp#^vab-ftp-7]]:

$$
\text{COF} = \text{Base Curve} + \text{Margin} + \text{Chi phí DTBB} + \text{Chi phí BHTG} + \text{Liquidity Premium} + \text{Term Liquidity Premium} + \text{ALCO Adjust}
$$
[[src-vab-ftp#^vab-ftp-7]]

Trong đó:
- **Lãi suất FTP cơ sở (Base Curve)**:
  - Đối với VND: Xây dựng dựa trên lãi suất huy động bình quân toàn hàng của các khoản phát sinh trong 3 tháng liền kề trước thời điểm tính [[src-vab-ftp#^vab-ftp-28]].
  - Đối với USD: Xây dựng theo lãi suất tham chiếu của thị trường quốc tế [[src-vab-ftp#^vab-ftp-29]].
  - Các kỳ hạn không chuẩn: Được tính toán bằng phương pháp nội suy hoặc ngoại suy trực tiếp từ thang kỳ hạn chuẩn [[src-vab-ftp#^vab-ftp-31]].
  - Đối với khoản vay lãi suất cố định: Lãi suất cơ sở tương ứng với kỳ hạn gốc (ngày đáo hạn trừ ngày giải ngân) căn cứ theo biểu lãi suất tại ngày giải ngân [[src-vab-ftp#^vab-ftp-32]].
- **Hỗ trợ huy động (Margin)**: Cấu phần điều phối lợi ích giữa đơn vị cho vay và đơn vị huy động vốn [[src-vab-ftp#^vab-ftp-7]] [[src-vab-ftp#^vab-ftp-25]].
- **Chi phí Bảo hiểm Tiền gửi (Deposit Insurance Cost)**: Mức phí BHTG luật định (0,15%/năm tính trên số dư tiền gửi cá nhân VND) được phân bổ đều vào giá bán vốn COF tính trên toàn bộ tài sản sinh lời thuộc diện FTP [[src-vab-ftp#^vab-ftp-8]]:
$$
\text{Tỷ lệ Chi phí BHTG} = \frac{\text{Tổng Chi phí BHTG thực tế 3 tháng quy đổi năm}}{\text{Bình quân Tổng tài sản bị tính FTP}}
$$
[[src-vab-ftp#^vab-ftp-8]]
- **Chi phí Dự trữ Bắt buộc (Statutory Reserved Cost)**: Chi phí cơ hội do duy trì tỷ lệ DTBB tại NHNN với lãi suất thấp hoặc 0% (cost of negative carry), được phân bổ vào COF [[src-vab-ftp#^vab-ftp-9]]:
$$
\text{Tỷ lệ Chi phí DTBB} = \frac{\text{Số dư DTBB bình quân} \times (\text{VOF bình quân} - \text{Lãi suất tiền gửi DTBB tại NHNN})}{\text{Bình quân Tổng tài sản bị tính FTP}}
$$
[[src-vab-ftp#^vab-ftp-9]]
- **Phần bù cho tài sản thanh khoản (Liquidity Buffer Premium)**: Chi phí duy trì danh mục tài sản thanh khoản theo quy định Thông tư 22/2019/TT-NHNN, quy định nội bộ hoặc LCR [[src-vab-ftp#^vab-ftp-10]]:
$$
\text{Liquidity Premium} = \frac{\text{Số dư bình quân TSTK} \times (\text{VOF bình quân} - \text{Lãi suất bình quân TSTK})}{\text{Bình quân Tổng tài sản bị tính FTP}}
$$
[[src-vab-ftp#^vab-ftp-10]]
- **Phần bù thanh khoản kỳ hạn (Term Liquidity Premium — TLP)**: Phản ánh chi phí thanh khoản dài hạn, áp dụng cho khoản vay lãi suất thả nổi [[src-vab-ftp#^vab-ftp-11]] [[src-vab-ftp#^vab-ftp-12]] [[src-vab-ftp#^vab-ftp-23]]:
$$
\text{TLP} = \text{Lãi suất kỳ hạn gốc} - \text{Lãi suất kỳ hạn tái định giá}
$$
[[src-vab-ftp#^vab-ftp-33]]
  Đối với khoản vay trả nợ định kỳ hoặc có dòng tiền phức tạp, áp dụng kỳ hạn hiệu lực (duration) [[src-vab-ftp#^vab-ftp-20]] [[src-vab-ftp#^vab-ftp-34]]:
$$
\text{TLP} = \text{Lãi suất kỳ hạn hiệu lực} - \text{Lãi suất kỳ hạn tái định giá}
$$
[[src-vab-ftp#^vab-ftp-34]]
- **Điều chỉnh của ALCO (ALCO Adjust)**: Quyết định điều chỉnh định hướng của Hội đồng ALCO đối với từng loại tài sản có trong từng thời kỳ [[src-vab-ftp#^vab-ftp-7]].

### 2. Chi phí vốn kế toán bình quân (Accounting Cost of Funds)

Ở cấp độ báo cáo tài chính tổng thể, COF được tính bằng tỷ lệ phần trăm giữa tổng chi phí trả lãi và tổng nguồn vốn nợ chịu lãi:

$$
\text{COF (Kế toán)} = \frac{\text{Tổng chi phí lãi và các chi phí tương đương}}{\text{Số dư bình quân các khoản nợ phải trả chịu lãi}}
$$
*Diễn giải:* (công thức kế toán tài chính phổ quát).

## Diễn giải

- **Cơ chế tập trung vốn và chuyển giao chi phí tại Treasury (CFU)**:
  - CFU mua vốn từ đơn vị huy động theo Biểu giá mua vốn (Value of Funds — VOF) và tập trung toàn bộ rủi ro thanh khoản, rủi ro kỳ hạn về trung tâm [[src-vab-ftp#^vab-ftp-6]] [[src-vab-ftp#^vab-ftp-22]].
  - Khi bán vốn cho các đơn vị kinh doanh tín dụng, CFU kết chuyển toàn bộ các chi phí tuân thủ pháp lệnh (DTBB, BHTG, đệm thanh khoản HQLA) vào giá bán vốn COF [[src-vab-ftp#^vab-ftp-7]]. Nhờ cơ chế này, đơn vị kinh doanh cho vay nhận thức đầy đủ mọi gánh nặng chi phí phát sinh từ việc giải ngân một đồng tài sản, ngăn ngừa hiện tượng báo lãi ảo và tăng trưởng quy mô kém chất lượng do định giá vốn quá rẻ [[src-choudhry-principles-banking#^choudhry-gov-12]].
- **Xử lý quyền chọn ẩn và cam kết ngoại bảng**:
  - *Khoản vay có quyền chọn trả nợ trước hạn (Prepayment Option)*: Khi khách hàng trả nợ trước hạn, ngân hàng chịu tổn thất do xáo trộn thanh khoản và rủi ro tái đầu tư. Lãi suất COF cơ sở được xác định dựa trên kỳ hạn hiệu lực tính toán từ mô hình hành vi (MHHV) trả nợ trước hạn thay vì kỳ hạn hợp đồng pháp lý [[src-vab-ftp#^vab-ftp-19]] [[src-vab-ftp#^vab-ftp-20]].
  - *Hạn mức cam kết tín dụng chưa sử dụng*: Đối với phần cam kết trong hạn mức chưa sử dụng của thẻ tín dụng, thấu chi hoặc khoản vay chưa xác định lịch giải ngân, giá bán vốn FTP được áp dụng dựa trên phần bù rủi ro thanh khoản tiềm tàng [[src-vab-ftp#^vab-ftp-35]].

- **Chi phí huy động và chi phí vốn kinh tế**: Nguyễn Khánh (T5, 22/9/2026) cho rằng chi phí huy động chỉ là một thành phần. Chi phí vốn kinh tế còn phụ thuộc vào cách ngân hàng sử dụng và tái tuần hoàn bảng cân đối; khi tài sản không quay vòng, nguồn vốn đắt hơn về mặt kinh tế [[src-clip-ldr-credit-turnover-bottleneck#^p7]]. Xem [[credit-turnover]].

## Basel vs VN

| Tiêu chí | Basel (BCBS) | Việt Nam (NHNN & VAB) | Điều khoản / Nguồn | Hiệu lực |
|---|---|---|---|---|
| Khung pháp lý về FTP | Nguyên tắc Pillar 2 (SRP30, IRRBB d368 Nguyên tắc 8/12): yêu cầu ngân hàng phải có khung phân bổ chi phí thanh khoản và rủi ro lãi suất vào giá sản phẩm | Tự chủ quản trị nội bộ; Thông tư 13/2018/TT-NHNN và Thông tư 83/2025/TT-NHNN quy định trách nhiệm của bộ phận ALM và Hội đồng ALCO trong kiểm soát định giá và thanh khoản | TT83 Đ25.3, Đ6.4.b [[src-tt83-2025-nhnn#^d6-4b]]; [src-vab-ftp](file:///d:/AI/202610%20ALM%20wiki/02_wiki/sources/src-vab-ftp.md) | Hiện hành (TT83 từ 01/07/2026) |
| Chi phí Bảo hiểm Tiền gửi | Phụ thuộc luật định từng quốc gia (FDIC tại Mỹ, DGS tại EU; nhiều chuẩn mực không tính BHTG vào FTP) | Phí BHTG cố định 0,15%/năm trên số dư tiền gửi cá nhân VND, phân bổ toàn bộ vào COF tính trên tài sản có | [[src-vab-ftp#^vab-ftp-8]] | Hiện hành |
| Chi phí Dự trữ Bắt buộc | Dự trữ bắt buộc tại NHTW được tính trong tài sản HQLA của LCR | Tiền gửi DTBB tại NHNN hưởng lãi suất thấp, chi phí cơ hội (negative carry) kết chuyển trực tiếp vào COF | [[src-vab-ftp#^vab-ftp-9]] | Hiện hành |
| Chi phí đệm thanh khoản | Tính qua chi phí duy trì tài sản HQLA cho LCR và NSFR | Kết hợp chi phí đệm thanh khoản theo Thông tư 22/2019/TT-NHNN và LCR vào cấu phần COF | [[src-vab-ftp#^vab-ftp-10]] | Hiện hành |

## Ứng dụng trong ALM

1. **Định giá sản phẩm cho vay (Loan Pricing) và bảo vệ NIM**:
   COF đóng vai trò là sàn chi phí vốn tối thiểu bắt buộc đối với mọi quyết định cấp tín dụng. Lãi suất cho vay (Lending Rate) tối thiểu được xác lập theo công thức bù đắp chi phí:
   $$
   \text{Lending Rate} = \text{COF} + \text{Credit Spread (EL + UL)} + \text{Operating Costs} + \text{Target Profit Margin (ROE / Hurdle Rate)}
   $$
   [[src-choudhry-principles-banking#^choudhry-strat-16]]
   Nếu COF không tính đúng phần bù thanh khoản kỳ hạn (TLP) hoặc bỏ sót các chi phí tuân thủ (DTBB, BHTG), ngân hàng sẽ cho vay dưới giá thành kinh tế thực tế, làm xói mòn trực tiếp biên lãi thuần (NIM) [[src-choudhry-principles-banking#^choudhry-nim-12]].
2. **Hàm mục tiêu trong tối ưu hóa cấu trúc sổ ngân hàng**:
   Trong các mô hình tối ưu hóa bảng cân đối ALM định lượng, bài toán phân bổ nguồn lực được tách thành hai mục tiêu: tối đa hóa thu nhập tài sản có và tối thiểu hóa chi phí vốn (minimisation of funding costs) bên tài sản nợ, dưới các ràng buộc hạn mức nội bộ và tỷ lệ an toàn thanh khoản pháp định (LCR, NSFR, IRRBB) [[src-lubinska-alm-optimisation#^lubinska-u07-1]] [[src-lubinska-alm-optimisation#^lubinska-u07-2]].
3. **Công cụ điều phối chiến lược của ALCO**:
   Hội đồng ALCO sử dụng cấu phần Margin và ALCO Adjust trong COF như một công cụ điều tiết chính sách: tăng giá COF để kìm hãm các phân khúc tín dụng rủi ro cao hoặc kỳ hạn quá dài làm căng thẳng thanh khoản, và giảm COF để trợ giá, thúc đẩy các gói tín dụng mục tiêu [[src-vab-ftp#^vab-ftp-7]].

## Nhầm lẫn thường gặp

- **Đồng nhất COF kế toán bình quân với COF trong FTP**:
  - *COF kế toán* là tỷ lệ chi phí trả lãi bình quân gia quyền của toàn bộ bảng cân đối trong quá khứ (backward-looking).
  - *COF trong FTP* là mức giá bán vốn biên tế (marginal cost of funds) cho từng khoản giải ngân cụ thể theo kỳ hạn, loại tiền tệ và rủi ro thanh khoản tại thời điểm giao dịch. Dùng COF kế toán bình quân để định giá khoản vay dài hạn thả nổi sẽ bỏ sót phần bù thanh khoản kỳ hạn (TLP), dẫn tới hiện tượng định giá thiếu chi phí và tích tụ rủi ro thanh khoản âm ỉ.
- **Nhầm lẫn giữa COF và VOF**:
  - *VOF (Value of Funds)* là giá mua vốn nội bộ CFU trả cho các đơn vị huy động nguồn vốn.
  - *COF (Cost of Funds)* là giá bán vốn nội bộ CFU thu từ các đơn vị sử dụng vốn để tài trợ tài sản.
- **Bỏ qua phần bù thanh khoản kỳ hạn (TLP) cho khoản vay thả nổi**:
  Quan niệm sai lầm cho rằng khoản vay thả nổi tái định giá lãi suất 3 tháng một lần chỉ cần chịu COF kỳ hạn 3 tháng. Thực tế ngân hàng cam kết thanh khoản gốc cho khách hàng trong suốt kỳ hạn hợp đồng (ví dụ 5 năm), do đó COF bắt buộc phải cộng thêm TLP để bù đắp chênh lệch chi phí thanh khoản giữa kỳ hạn gốc 5 năm và kỳ hạn tái định giá 3 tháng [[src-vab-ftp#^vab-ftp-12]] [[src-vab-ftp#^vab-ftp-33]].

## Khái niệm và Liên kết
- [[ftp-pricing-methodology]]: Phương pháp luận định giá VOF và COF toàn diện.
- [[funds-transfer-pricing]]: Tổng quan cơ chế định giá điều chuyển vốn nội bộ.

