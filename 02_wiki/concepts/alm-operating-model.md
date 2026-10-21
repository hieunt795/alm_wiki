---
title: "ALM Operating Model"
aliases: [ALM Operating Model, Treasury Operating Model, Mô hình vận hành ALM, Mô hình vận hành Treasury, Group Treasury]
type: concept
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-vab-ftp]]"]
relations: []
tags: [governance, treasury, conflict-of-interest]
updated: 2026-10-21
reviewed:
---

## Ý chính
ALM operating model là cách tổ chức chức năng ALM/Treasury: nhiệm vụ nào thuộc ALM, ALM báo cáo cho ai, và ALM tách khỏi Risk, Finance, Trading Desk ra sao. Mục đích là tránh xung đột lợi ích. Không bàn Treasury/ALM nào chịu được toàn bộ nhiệm vụ ALM, vì một bộ phận không thể vừa đặt hạn mức vị thế vừa giao dịch cho vị thế đó, vừa dựng đường cong lãi suất nội bộ vừa giao dịch với biên trên đường cong này [[src-bardaeva-alm#^ch10-1]].

## Cơ chế & drivers

### Front office và middle office
| Mô hình | Đặc điểm | Nguồn |
|---|---|---|
| Treasury front office | Loại bỏ chức năng chiến lược và kiểm soát; thường là profit center | [[src-bardaeva-alm#^ch10-3]] |
| ALM middle office | Chủ yếu quản lý bảng cân đối chiến lược; làm chức năng phân tích, cung cấp thông tin cho Ban điều hành | [[src-bardaeva-alm#^ch10-4]] |

Choudhry đặt cùng lựa chọn dưới dạng profit centre (gồm bàn money market) và cost centre "middle office" chỉ đặt chính sách và quản trị [[src-choudhry-principles-banking#^choudhry-opmodel-3]]. Choudhry cũng mô tả ALM desk đi từ cost centre có mục tiêu lợi nhuận bằng 0 tới profit centre tối ưu chính sách funding trong hạn mức [[src-choudhry-principles-banking#^choudhry-desk-1]].

Bardaeva định nghĩa tổng quát ALM là quá trình mô hình hoá bảng cân đối và các khoản mục ngoại bảng, thay đổi khối lượng và cơ cấu của chúng nhằm đạt các mục tiêu kinh doanh trong các môi trường vĩ mô khác nhau, phù hợp với hồ sơ nguồn lực của ngân hàng và tuân thủ các giới hạn rủi ro nội bộ cũng như ràng buộc quy định về thanh khoản, lãi suất (IRR), ngoại hối (FX) và an toàn vốn [[src-bardaeva-alm#^ch9-1]].

Nhiệm vụ ALM được chia thành bốn nhóm chủ đề [[src-bardaeva-alm#^ch9-2]]:
1. **ALM risk management**: quản trị rủi ro lãi suất, tỷ giá và thanh khoản bảo đảm hoạt động trong hạn mức và duy trì thanh khoản bền vững.
2. **BS structure targeting**: điều phối cấu trúc bảng cân đối qua các giao dịch kỳ hạn, tiền tệ và phòng ngừa phù hợp để duy trì an toàn vốn.
3. **Price benchmarking**: cung cấp chuẩn đối chiếu định giá (đường cong FTP và lãi suất sàn cho vay) định hướng động lực kinh doanh.
4. **Resources allocation**: phân bổ thanh khoản, vốn, mức rủi ro và biên lãi suất cho các đơn vị kinh doanh.

Bảng 9.1 phân rã toàn diện nhiệm vụ ALM theo bốn nhóm và ba cấp thời gian [[src-bardaeva-alm#^ch9-3]]:

| Tầm thời gian | ALM risk management | BS structure targeting | Price benchmarking | Resources allocation |
|---|---|---|---|---|
| Ngắn hạn / tác nghiệp | Quản lý đệm thanh khoản; Thanh khoản tác nghiệp; Quản lý tiền mặt và tương đương tiền; Tiền gửi liên ngân hàng; Giao dịch Repo; Mua bán chứng khoán; Thực hiện phái sinh; Quản lý số dư giới hạn FX; Hoạt động hối đoái; Phân tích dòng tiền; Quản lý tài sản bảo đảm; Kiểm soát hạn mức đối tác | Điều phối tỷ lệ an toàn vốn (CAR) | Xây dựng đường cong FTP | Tính toán chi phí thanh khoản |
| Dài hạn / chiến lược (going concern) | Quản trị rủi ro lãi suất; Mô hình hoá khe hở lãi suất; Quản trị rủi ro thanh khoản; Kế hoạch tài trợ dự phòng; Phòng ngừa bảng cân đối; Xác định thước đo và hạn mức | Phát hành nợ; Huy động vốn dài hạn; Chứng khoán hoá; Kế hoạch vốn và nguồn vốn; Xác định cấu trúc vốn | Định giá sản phẩm; Mô hình khả năng sinh lời kinh doanh; Định giá điều chuyển vốn (FTP); Mô hình hoá hành vi; Khớp kỳ hạn | Dự báo NII và NIM; Đặt mục tiêu RoE; So sánh RoRWA; Phát triển chiến lược; Phân bổ vốn và RWA; Xác định chi phí vốn (CoC) |
| Kịch bản khủng hoảng (gone concern) | Thực thi ILAAP; Stress test thanh khoản; Stress test dòng tiền | Thực thi ICAAP; Stress test vốn; Dự báo MREL; Kế hoạch xử lý (Resolution); Kế hoạch phục hồi (Recovery) | *(trống)* | Tính toán và phân bổ vốn kinh tế |

### Ma trận tác động của ALM trên các sản phẩm bảng cân đối
ALM thực thi nhiệm vụ thông qua việc điều phối 6 nhóm sản phẩm bảng cân đối cốt lõi:
- **Cho vay (Loans)**: Tác động đồng thời lên khe hở lãi suất (theo kỳ hạn và loại lãi suất), khe hở thanh khoản, trạng thái ngoại hối mở OCP, an toàn vốn (RWA) và stress testing [[src-bardaeva-alm#^ch9-4]]. Đánh giá hiệu quả khoản vay qua 3 tầng biên lãi: Gross margin (lãi khách hàng trừ FTP rate), Net margin (gross margin trừ EL), và EVA (net margin trừ chi phí vốn CoC) [[src-bardaeva-alm#^ch9-5]].
- **Tiền gửi (Deposits)**: Nguồn vốn nợ chủ lực; các khoản tiền gửi phi kỳ hạn được lượng hoá qua mô hình hành vi; quyết định huy động được định hướng qua đường cong FTP; phân loại nợ đủ điều kiện MREL, nợ thứ cấp (T2) hoặc công cụ vốn tự có bổ sung (T1) [[src-bardaeva-alm#^ch9-6]].
- **Tiền mặt (Cash) và Vốn chủ sở hữu (Equity)**: Tiền mặt đóng vai trò dòng cân đối thanh khoản trong mọi tính toán và ảnh hưởng đến FTP tiền gửi qua dự trữ bắt buộc; Vốn chủ sở hữu là nơi tích luỹ lợi nhuận giữ lại, nền tảng của tỷ lệ an toàn vốn và chỉ tiêu RoE [[src-bardaeva-alm#^ch9-7]].

Chọn mô hình mới là bước đầu: phải xét cả tuyến báo cáo, vì thành viên ban điều hành mà ALM báo cáo có thể phụ trách bộ phận có chức năng xung đột [[src-bardaeva-alm#^ch10-6]].

### ALM trong tam giác Risk–Trading–Finance
Khung quản trị rủi ro bảng cân đối phải xoay quanh một mô hình vận hành bảo đảm tương tác giữa Finance, Treasury (Trading Desk) và Risk [[src-bardaeva-alm#^ch11-1]]. Bardaeva kết luận không thể gộp ALM vào bộ phận nào trong ba bộ phận này [[src-bardaeva-alm#^ch11-2]].

| Gộp ALM vào | Xung đột | Nguồn |
|---|---|---|
| Risk | Đơn vị đánh giá không đánh giá rủi ro khách quan; có động cơ hạ thấp rủi ro để tránh công cụ bất tiện | [[src-bardaeva-alm#^ch11-10]] |
| Trading Desk | Xung đột lớn, không giải được kể cả khi ALM không là profit center; nguyên tắc gán kỳ hạn FTP không được do đơn vị giao dịch quyết định | [[src-bardaeva-alm#^ch11-11]] |
| Finance | KPI ngân sách tạo động cơ tăng khẩu vị rủi ro để kiếm thêm từ gap kỳ hạn/tiền tệ | [[src-bardaeva-alm#^ch11-12]] |

So sánh nhiệm vụ bốn bộ phận [[src-bardaeva-alm#^ch11-3]]:

| ALM | Risk | Trading | Finance |
|---|---|---|---|
| ALM risk management | Risk assessment | Execution of deals | Profitability analysis |
| BS structure targeting | Limiting positions/portfolios | Funding strategy development | Budgeting |
| Price benchmarking | Models validation, stress testing | Quoting of rates | Deviations analysis |
| Resources allocation | Economic capital evaluation | Earning income | Profit calculation |

Cơ chế giảm xung đột gồm RAS, amber zone đặt ở [[alco]], và thành phần ALCO có ALM, Risk, Finance [[src-bardaeva-alm#^ch11-20]]. Đơn vị ALM nên độc lập, trực thuộc CFO hoặc CEO (khi họ có KPI cả về tham số rủi ro), hoặc thuộc đơn vị phụ trách chiến lược dài hạn [[src-bardaeva-alm#^ch11-21]]. Choudhry cũng kết luận ALM desk nên độc lập với các đơn vị vận hành [[src-choudhry-principles-banking#^choudhry-opmodel-2]].

Trong mô hình [[three-lines-of-defence]], ALM/Treasury là tuyến 1, kể cả khi thực hiện giao dịch [[src-bardaeva-alm#^ch11-7]].

### Group Treasury
Group Treasury là ALM desk của cả tập đoàn ngân hàng [[src-bardaeva-alm#^ch12-1]]. Có hai mô hình cơ bản là tập trung và phân tán, kết hợp lại thành mô hình lai [[src-bardaeva-alm#^ch12-16]].

| Mô hình | Hạn mức IR/FX | Nhược điểm | Nguồn |
|---|---|---|---|
| Tập trung | Công ty con quản lý danh mục theo hướng dẫn và hạn mức của Group Treasury | Funding và phân bổ vốn có thể không rẻ nhất; phương pháp trung tâm bỏ sót đặc thù địa phương | [[src-bardaeva-alm#^ch12-17]] [[src-bardaeva-alm#^ch12-18]] |
| Phân tán | Group Treasury đặt hạn mức quốc gia; công ty con tự đặt hạn mức chi tiết | Thiếu quy mô, ít nguồn funding và công cụ phòng ngừa, chi phí cao hơn | [[src-bardaeva-alm#^ch12-19]] [[src-bardaeva-alm#^ch12-20]] |

Ở thị trường địa phương kém phát triển, mô hình tập trung là cần thiết [[src-bardaeva-alm#^ch12-21]]. Group Treasury thiết kế nguyên tắc và mô hình [[funds-transfer-pricing]] cho cả tập đoàn [[src-bardaeva-alm#^ch12-3]].

### ALM thuộc khối thị trường hay phi thị trường (Lubinska)
| Vị trí | Đặc điểm | Nguồn |
|---|---|---|
| Khối thị trường (Financial Markets, Capital Markets, Treasury) | ALCO quyết định định vị rủi ro, ALM tự quản lý vị thế trong hạn mức tác nghiệp; treasurer dự báo lãi suất và dùng directional GAP (không phải trading); ALM có earnings budget, gọi là business unit model | [[src-lubinska-alm-optimisation#^lubinska-u01-10]] |
| Khối phi thị trường (Finance, Risk) | ALM không tự mở vị thế, không được tiếp cận thị trường, giao dịch phải giao cho đơn vị thị trường thực hiện; phổ biến khi chiến lược IRRBB là immunisation | [[src-lubinska-alm-optimisation#^lubinska-u01-10]] |

Hai lựa chọn này tương ứng hai khẩu vị rủi ro mà ALCO đặt: riding the yield curve (tài trợ tài sản cố định bằng nợ thả nổi) hoặc immunisation [[src-lubinska-alm-optimisation#^lubinska-u01-5]].

### Quy trình vận hành FTP tại một NHTM VN (VAB, tài liệu tư vấn T4)
Thị trường 1 (PL05), định kỳ hằng quý hoặc khi thị trường biến động lớn:

| Bước | Việc | Người thực hiện | Nguồn |
|---|---|---|---|
| 1 | Đề xuất cập nhật biểu FTP, yêu cầu dữ liệu đầu vào (MB02) | Bộ phận quản lý FTP | [[src-vab-ftp#^vab-ftp-49]] |
| 2 | Cung cấp dữ liệu: CNTT chiết xuất dữ liệu FTP cơ sở; khối kinh doanh lập đề xuất FTP đặc biệt/ngoại lệ | Khối CNTT, khối kinh doanh | [[src-vab-ftp#^vab-ftp-49]] |
| 3–4 | Tính toán, kiểm soát, rà soát; trình ALCO tham mưu đến TGĐ | Bộ phận quản lý FTP, trưởng bộ phận | [[src-vab-ftp#^vab-ftp-50]] |
| 5 | Phê duyệt hoặc trả lại điều chỉnh | TGĐ/người được uỷ quyền | [[src-vab-ftp#^vab-ftp-50]] |
| 6 | Cập nhật biểu lên hệ thống quản lý vốn nội bộ | Khối CNTT/Bộ phận quản lý FTP | [[src-vab-ftp#^vab-ftp-51]] |
| 7–8 | Thực hiện giao dịch mua bán vốn nội bộ; kiểm tra số tiền, loại tiền, kỳ hạn, lãi suất và xác nhận | Khối kinh doanh; cấp kiểm soát Bộ phận quản lý FTP | [[src-vab-ftp#^vab-ftp-51]] |
| 9 | Tổng hợp, lưu trữ hồ sơ giao dịch giữa CFU và đơn vị kinh doanh | Bộ phận kế toán | [[src-vab-ftp#^vab-ftp-51]] |

Thị trường 2 (PL06), hằng ngày:

| Bước | Việc | Người thực hiện | Nguồn |
|---|---|---|---|
| 1 | Cung cấp lãi suất thị trường | Khối QL&KDV | [[src-vab-ftp#^vab-ftp-52]] |
| 2 | Tính biểu FTP TT2 từ 9 giờ đến 10 giờ (mid-rate ngân hàng tham chiếu) hoặc xác nhận VNIBOR | Bộ phận quản lý FTP | [[src-vab-ftp#^vab-ftp-52]] |
| 3–4 | Rà soát, trình ALCO tham mưu; TGĐ phê duyệt biểu giữa CFU và Khối QL&KDV | Trưởng bộ phận quản lý FTP; TGĐ | [[src-vab-ftp#^vab-ftp-53]] |
| 5 | Giao dịch mua bán vốn nội bộ; giao dịch trước khi có biểu mới dùng biểu ngày làm việc liền trước | Khối QL&KDV | [[src-vab-ftp#^vab-ftp-53]] |

Hai cơ chế giao dịch giữa CFU và Khối QL&KDV: từng desk mua bán vốn trực tiếp với CFU theo kỳ hạn nhu cầu của desk [[src-vab-ftp#^vab-ftp-60]], hoặc bộ phận MM đại diện cả khối mua bán phần thặng dư/thiếu hụt ròng ở VNIBOR 1 tuần, kèm hạn mức thanh khoản 30 ngày cho trạng thái ròng [[src-vab-ftp#^vab-ftp-61]].

*Diễn giải:* trong quy trình VAB, CFU (Bộ phận quản lý FTP) tính và kiểm soát giá, còn quyền phê duyệt thuộc TGĐ qua ALCO. Khối QL&KDV (thị trường 2) chỉ cung cấp dữ liệu và thực hiện giao dịch, tương ứng việc tách front office khỏi bộ phận định giá ở mục trên. Bước 6–9 của PL06 (kiểm soát, xác nhận, lưu hồ sơ) lặp lại cấu trúc PL05, nên không chép.

### Theo quy mô ngân hàng
- Ở ngân hàng nhỏ, thiếu nhân sự thường cản trở phân tách trách nhiệm, dẫn tới mơ hồ trong phân chia chức năng [[src-bardaeva-alm#^ch14-8]].
- Ở ngân hàng thị phần lớn, xung đột lợi ích bị hạn chế và giám sát thận trọng; ở ngân hàng nhỏ, không loại trừ mơ hồ trong phân chia chức năng [[src-bardaeva-alm#^ch14-9]].
- Ngân hàng nhỏ không bị yêu cầu triển khai quy định còn ở giai đoạn tham vấn, nên có thời gian học từ ngân hàng lớn [[src-bardaeva-alm#^ch14-10]] [[src-bardaeva-alm#^ch14-9]].
- Ở thị trường kém phát triển, cũng không loại trừ mơ hồ trong phân chia chức năng [[src-bardaeva-alm#^ch14-16]].

## Phụ thuộc regime
- Xung đột lợi ích trong ALM có xu hướng tăng trong suy thoái và khủng hoảng [[src-bardaeva-alm#^ch11-23]]. Trong khủng hoảng, ALM tham gia mọi mảng: thanh khoản và funding, vốn, IRRBB, FTP [[src-bardaeva-alm#^ch15-1]]. Xem [[recovery-and-resolution-planning]].

## Góc nhìn theo domain
- **ALM**: quản trị IRRBB theo mô hình này được mô tả ở [[irrbb-management]].
- **VN**: [[tt83-2025]] yêu cầu bộ phận đo lường, theo dõi, kiểm soát IRRBB độc lập với bộ phận kinh doanh phát sinh rủi ro [[src-tt83-2025-nhnn#^d54-1b]]. Phần đã ingest không quy định ALM đặt ở khối nào [cần nguồn].

## Bằng chứng thực nghiệm
[cần nguồn]

## Câu hỏi mở
- Table 10.1/10.2 mất phần tô màu khi convert, nên chưa biết ô nào thuộc front office, ô nào thuộc middle office; cần đối chiếu PDF.
