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
sources: ["[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]"]
relations: []
tags: [governance, treasury, conflict-of-interest]
updated: 2026-10-19
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

Bardaeva xếp nhiệm vụ ALM thành bốn nhóm: ALM risk management, BS structure targeting, price benchmarking và resources allocation. Nhóm ALM risk management dài hạn gồm interest rate risk management, interest rate gap modelling, balance sheet hedging, determining metrics and limits [[src-bardaeva-alm#^ch10-5]].

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
