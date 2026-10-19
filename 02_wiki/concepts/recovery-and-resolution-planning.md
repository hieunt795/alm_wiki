---
title: "Recovery and Resolution Planning"
aliases: [Recovery and Resolution Planning, RRP, Recovery plan, Resolution plan, Kế hoạch phục hồi và xử lý]
type: concept
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]"]
relations: []
tags: [recovery, resolution, brrd, crisis]
updated: 2026-10-19
reviewed:
---

## Ý chính
Recovery and resolution planning (RRP) gồm hai kế hoạch cho hai giai đoạn ngoài going concern.
- **Recovery plan** do ngân hàng tự lập: ngưỡng kích hoạt (recovery triggers) đặt trong khung khẩu vị rủi ro, biện pháp phục hồi (recovery options), quy trình leo thang (kể cả thông báo cơ quan giám sát) và cách thực hiện biện pháp. Recovery plan không dựa vào hỗ trợ của nhà nước [[src-bardaeva-alm#^ch14-2]].
- **Resolution plan** do cơ quan có thẩm quyền lập, thường với sự hỗ trợ của ngân hàng. Cơ quan xử lý quyết định chiến lược xử lý; ngân hàng chuẩn bị triển khai biện pháp [[src-bardaeva-alm#^ch14-3]].

## Cơ chế & drivers

### Các giai đoạn
Bardaeva liệt kê bốn giai đoạn: going concern, phục hồi do ngân hàng chủ động, phục hồi và/hoặc xử lý do cơ quan có thẩm quyền chủ động, xử lý có dùng nguồn bên ngoài [[src-bardaeva-alm#^ch14-1]].

### Chiến lược xử lý
| Lựa chọn | Khi nào | Nguồn |
|---|---|---|
| Thanh lý thông thường (ordinary insolvency) | Không có chức năng trọng yếu, không đe doạ ổn định tài chính; không có yêu cầu MREL bổ sung ngoài vốn tự có | [[src-bardaeva-alm#^ch14-4]] [[src-bardaeva-alm#^ch16-8]] |
| Resolution theo BRRD | Chức năng trọng yếu cho nền kinh tế hoặc ổn định thị trường bị đe doạ | [[src-bardaeva-alm#^ch14-4]] |

Tổ chức nhỏ và đơn giản nhất, không có chức năng trọng yếu hay liên kết với nền kinh tế, thanh lý thông thường khi vỡ nợ [[src-bardaeva-alm#^ch14-7]].

### Công cụ resolution theo BRRD [[src-bardaeva-alm#^ch14-5]]
| Công cụ | Nội dung |
|---|---|
| Sale of business | Bán một phần bảng cân đối cho nhà đầu tư, thanh lý phần còn lại |
| Bridge institution | Chuyển một phần bảng cân đối sang pháp nhân mới, thanh lý phần còn lại |
| Asset separation | Chuyển tài sản và nợ sang "bad bank", phần lõi tiếp tục hoạt động |
| [[bail-in]] | Bù lỗ hoặc chuyển nợ đủ điều kiện thành vốn, tổ chức tiếp tục hoạt động |

### Khả năng xử lý (resolvability)
Ngân hàng cần đủ công cụ [[mrel]] cho nhu cầu hấp thụ lỗ và tái cấp vốn, và nên có bail-in playbook [[src-bardaeva-alm#^ch14-6]].

### Vai trò ALM
- Mỗi mảng ALM (thanh khoản và funding, vốn, IRRBB, FTP) nên có kế hoạch hành động định sẵn theo mức độ nghiêm trọng của khủng hoảng [[src-bardaeva-alm#^ch15-1]].
- Biện pháp phục hồi nên được đánh giá lại liên tục, xem ngân hàng đã dùng biện pháp nào khi duy trì thanh khoản, vốn hay kết quả tài chính [[src-bardaeva-alm#^ch15-9]].
- Khi add-on resolution vượt thặng dư vốn, ALM huy động nguồn đủ chuẩn MREL [[src-bardaeva-alm#^ch16-9]].
- Thứ tự hành động thanh khoản trong khủng hoảng nằm ở [[contingency-funding-plan]]; kế hoạch hành động vốn nằm ở [[capital-plan]].

### Recovery Plan Indicators (Choudhry, T4)
- Board chọn một số Tier 1 KRI làm Recovery Plan Indicators (RPI); Board kích hoạt Recovery Plan theo đề nghị của Board Risk committee khi có vi phạm thực tế hoặc dự báo so với hạn mức quy định [[src-choudhry-principles-banking#^choudhry-kri-10]]. Xem [[key-risk-indicators]].
- Vi phạm red của Tier 2 KRI không tự động kích hoạt Recovery Plan hay Liquidity Contingency Plan [[src-choudhry-principles-banking#^choudhry-kri-2]].
- Liquidity Contingency Plan là phần rủi ro thanh khoản của Recovery Plan; cả hai dùng stress "extreme" dưới dạng reverse stress [[src-choudhry-principles-banking#^choudhry-rmf-10]].
- ICAAP, ILAAP, recovery planning và resolution planning được làm tích hợp trong cùng RMF [[src-choudhry-principles-banking#^choudhry-rmf-9]].

### Choudhry (T4): FSB Key Attributes và nội dung kế hoạch
- Recovery planning là quy trình "going concern": ngân hàng chứng minh hành động khả thi trong stress cao độ để đưa KRI về green. Resolution plan là quy trình "gone concern", áp dụng khi ngân hàng đã bị coi là thất bại [[src-choudhry-principles-banking#^choudhry-rrp-18]].
- Recovery planning có thể xem là phần mở rộng của [[icaap]] và [[ilaap]] dưới stress nghiêm trọng hơn [[src-choudhry-principles-banking#^choudhry-rrp-1]]. [[reverse-stress-testing]] có thể xem là trường hợp đặc biệt của recovery planning [[src-choudhry-principles-banking#^choudhry-rst-9]].
- Mục đích RRP là xử lý ngân hàng sắp đổ vỡ hoặc đã tới point of non-viability, tránh bail-out "too big to fail" [[src-choudhry-principles-banking#^choudhry-rrp-2]]. FSB Key Attributes (2011) đặt mục tiêu xử lý không gây gián đoạn hệ thống, không để người nộp thuế chịu lỗ [[src-choudhry-principles-banking#^choudhry-rrp-5]].
- Quyền của cơ quan xử lý gồm vượt quyền cổ đông, lập bridge institution, [[bail-in]], tạm hoãn quyền chấm dứt sớm [[src-choudhry-principles-banking#^choudhry-rrp-6]]. Cơ chế bảo vệ gồm thứ tự chủ nợ và "no creditor worse off" [[src-choudhry-principles-banking#^choudhry-rrp-7]]. Resolvability assessment bắt buộc ít nhất với G-SIFI [[src-choudhry-principles-banking#^choudhry-rrp-8]].

| Kế hoạch | Nội dung nên có | Nguồn |
|---|---|---|
| Recovery plan | Phương án cho stress đặc thù và toàn thị trường, cho thiếu hụt vốn và áp lực thanh khoản; quy trình thực hiện kịp thời | [[src-choudhry-principles-banking#^choudhry-rrp-9]] |
| Resolution plan | Chức năng trọng yếu, phương án xử lý, rào cản và biện pháp tháo gỡ, bảo vệ người gửi tiền được bảo hiểm, phương án thoát | [[src-choudhry-principles-banking#^choudhry-rrp-10]] |
| Cả hai | Early warning triggers, hành động chuẩn bị, trở ngại trọng yếu, phân định trách nhiệm; cập nhật ít nhất hằng năm | [[src-choudhry-principles-banking#^choudhry-rrp-17]] [[src-choudhry-principles-banking#^choudhry-rrp-10]] |

- Ch15 mô tả recovery plan là phản ứng với sự kiện tác động mạnh lên vốn khi ngân hàng vẫn solvent, có thể gồm cắt giảm chi phí và bán tài sản hay mảng phi cốt lõi, và phải xử lý hệ quả thanh khoản, tín dụng. Resolution plan thuộc về Regulator ngang với ngân hàng, xét các bước khi recovery không còn khả thi [[src-choudhry-principles-banking#^choudhry-strat-30]]. Xem [[bank-strategic-plan]].
- Kế hoạch không công bố ra thị trường và xác định chức năng kinh tế trọng yếu như thanh toán, quyết toán, nhận tiền gửi [[src-choudhry-principles-banking#^choudhry-rrp-4]].

## Phụ thuộc regime
- Kết quả stress test cho phơi nhiễm với khủng hoảng phi tài chính có thể được đưa vào biện pháp phục hồi [[src-bardaeva-alm#^ch16-7]].

## Góc nhìn theo domain
- **EU**: khung BRRD và MREL theo Bardaeva (T4); wiki chưa có văn bản gốc BRRD hay FSB Key Attributes [cần nguồn]. Theo Choudhry, cách tiếp cận EU áp cho mọi tổ chức, ba trụ cột: chuẩn bị và phòng ngừa, can thiệp sớm, xử lý [[src-choudhry-principles-banking#^choudhry-rrp-11]]; resolution planning do cơ quan có thẩm quyền làm và sở hữu [[src-choudhry-principles-banking#^choudhry-rrp-12]].
- **US**: Dodd-Frank áp cho G-SIFI và tổ chức có bảng cân đối trên 50 tỷ USD; FDIC là cơ quan xử lý; ưu tiên single point of entry [[src-choudhry-principles-banking#^choudhry-rrp-13]]. Recovery plan không bắt buộc ở US [[src-choudhry-principles-banking#^choudhry-rrp-11]].
- **UK**: mọi ngân hàng phải nộp recovery plan [[src-choudhry-principles-banking#^choudhry-rrp-3]]; RRP tách khỏi ICAAP, khác US nơi CCAR gồm cả RRP [[src-choudhry-principles-banking#^choudhry-icaap-16]].
- **VN**: wiki chưa có nguồn NHNN về phương án phục hồi, xử lý [cần nguồn].

## Bằng chứng thực nghiệm
[cần nguồn]

## Câu hỏi mở
- Figure 21.2 (creditor waterfall) và Figure 21.3 (bail-in bằng số) chỉ có dạng ảnh; số liệu lấy từ lời văn.
