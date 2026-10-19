---
title: "Key Risk Indicators"
aliases: [Key Risk Indicators, KRI, Chỉ số rủi ro chính, Early Warning Indicators, EWI, Chỉ tiêu cảnh báo sớm]
type: concept
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[risk-appetite]]", cite: "[[src-choudhry-principles-banking#^choudhry-rmf-1]]"}
tags: [governance, risk-appetite, escalation]
updated: 2026-10-19
reviewed:
---

## Ý chính
Key risk indicators (KRI) là thước đo giúp đánh giá ngân hàng có đang hoạt động trong giới hạn khẩu vị rủi ro đã nêu hay không, ví dụ tỷ lệ vốn, hạn mức phơi nhiễm lớn, rủi ro tập trung, LCR [[src-choudhry-principles-banking#^choudhry-kri-1]]. RAS gồm KRI, các chỉ số rủi ro bổ sung và early warning indicators (EWI) [[src-choudhry-principles-banking#^choudhry-rmf-1]]. Xem [[risk-appetite]].

## Cơ chế & drivers

### Phân tầng chỉ số (Choudhry, khung UK)
| Loại | Trong RAS? | Đặc điểm | Nguồn |
|---|---|---|---|
| Tier 1 KRI | Có | Đánh giá tuân thủ khẩu vị rủi ro; red ở Tier 1 tự động được coi là vi phạm khẩu vị rủi ro | [[src-choudhry-principles-banking#^choudhry-kri-1]] [[src-choudhry-principles-banking#^choudhry-kri-9]] |
| Tier 2 KRI | Có | Như Tier 1, nhưng vi phạm red không tự động kích hoạt Recovery Plan hay Liquidity Contingency Plan | [[src-choudhry-principles-banking#^choudhry-kri-2]] |
| Tier 3 risk metrics | Không | Liệt kê trong chính sách; phân tích driver của KRI | [[src-choudhry-principles-banking#^choudhry-kri-3]] |
| EWI | Không | Chỉ báo vấn đề tương lai; nội bộ (Exco tác động được) hoặc bên ngoài (ví dụ lãi suất cơ bản của NHTW) | [[src-choudhry-principles-banking#^choudhry-kri-4]] |
| KPI | Chỉ khi cũng là KRI | Đo mục tiêu chiến lược và ngân sách: lợi nhuận, RoC, cost of funds | [[src-choudhry-principles-banking#^choudhry-kri-5]] |
| Recovery Plan Indicator (RPI) | Có (là Tier 1) | Tier 1 KRI được Board chọn để quyết định kích hoạt Recovery Plan | [[src-choudhry-principles-banking#^choudhry-kri-10]] |

Ngân hàng mẫu của Choudhry đặt mọi ngưỡng khẩu vị rủi ro cao hơn hạn mức quy định [[src-choudhry-principles-banking#^choudhry-kri-1]].

### Hiệu chỉnh và vận hành
- Mỗi KRI được hiệu chỉnh bốn mức màu (RAYG); Choudhry khuyến nghị thêm "yellow" giữa green và amber để ban điều hành có thời gian xử lý trước khi phải leo thang [[src-choudhry-principles-banking#^choudhry-kri-6]] [[src-choudhry-principles-banking#^choudhry-rmf-8]].
- Mỗi KRI có chủ sở hữu; KRI phải do người hoặc bộ phận độc lập với chủ sở hữu tạo ra hoặc kiểm định; chỉ số tháng phải có trong 10 ngày làm việc sau cuối tháng [[src-choudhry-principles-banking#^choudhry-kri-7]].

### Leo thang khi vi phạm
| Mức | Hành động | Thời hạn | Nguồn |
|---|---|---|---|
| Amber | Chủ sở hữu xác định nguyên nhân, cách khắc phục, thời gian và chi phí; báo Exco và [[alco]]; người nhận có thể triệu tập họp ALCO khẩn | Chậm nhất 48 giờ | [[src-choudhry-principles-banking#^choudhry-kri-8]] |
| Red | Báo Board Risk sub-committee ngay; CRO triệu tập họp Exco bất thường; trình kế hoạch khắc phục | Ngay khi phát hiện | [[src-choudhry-principles-banking#^choudhry-kri-9]] |
| Red (CEO) | CEO trao đổi với Chủ tịch Board và Board Risk committee về họp khẩn | Trong 24 giờ | [[src-choudhry-principles-banking#^choudhry-kri-9]] |
| RPI | Board kích hoạt Recovery Plan theo đề nghị của Board Risk committee khi có vi phạm (thực tế hoặc dự báo) so với hạn mức quy định | | [[src-choudhry-principles-banking#^choudhry-kri-10]] |

### Với IRRBB
- Risk register mẫu ghi khẩu vị rủi ro lãi suất bằng hạn mức chênh lệch tái định giá [[src-choudhry-principles-banking#^choudhry-rmf-5]].
- *Diễn giải:* hạn mức ΔEVE và ΔNII trong [[irrbb-management]] có thể vận hành như Tier 1 hoặc Tier 2 KRI với bốn mức màu; nguồn không nói ngân hàng nên xếp IRRBB vào tầng nào.

## Phụ thuộc regime
- Một ngân hàng có hạn mức cho một mảng kinh doanh nhưng vị thế thực tế vượt hạn mức 75% (The Times, 30/3/2022) [[src-choudhry-principles-banking#^choudhry-rmf-15]].

## Góc nhìn theo domain
- **VN**: TT83/2025 yêu cầu theo dõi, kiểm soát IRRBB có cảnh báo sớm khi gần vượt hạn mức và biện pháp xử lý kịp thời khi vượt [[src-tt83-2025-nhnn#^d54-4c]]; với thanh khoản, phải có chỉ tiêu cảnh báo sớm [[src-tt83-2025-nhnn#^d47-3]]. Hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]].
- **Basel**: [cần nguồn].

*Diễn giải:* TT83 yêu cầu cơ chế cảnh báo sớm nhưng phần đã ingest không quy định số mức màu hay thời hạn leo thang; khung 4 màu, 48 giờ, 24 giờ của Choudhry là thông lệ UK, không phải yêu cầu của NHNN.

## Bằng chứng thực nghiệm
- [[src-choudhry-principles-banking#^choudhry-rmf-15]] (vượt hạn mức 75%).

## Câu hỏi mở
- Figure 18.7, 18.8 (thang hiệu chỉnh và ma trận leo thang) là ảnh trong raw, chưa trích được.
