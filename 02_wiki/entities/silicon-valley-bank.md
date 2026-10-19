---
title: "Silicon Valley Bank"
aliases: [Silicon Valley Bank, SVB, Ngân hàng Silicon Valley, SVB collapse]
type: entity
domains: [alm]
status: active
maturity: draft
sources: ["[[src-tata-bank-alm]]"]
relations: []
tags: [case-study, irrbb, duration-gap, non-maturity-deposits, bank-failure]
updated: 2026-10-19
reviewed:
---

## Vai trò
Silicon Valley Bank (SVB) là ngân hàng Mỹ sụp đổ ngày 10/3/2023 và bị cơ quan quản lý tiếp quản [[src-tata-bank-alm#^tata-svb-1]]. Với ALM, đây là ví dụ điển hình về IRRBB và rủi ro thanh khoản: tài sản có duration dài được tài trợ bằng tiền gửi ngắn hạn, tập trung và không được bảo hiểm [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-4]].

## Công cụ / chính sách
**Bảng cân đối cuối 2022.**

| Chỉ tiêu | Giá trị | Nguồn |
|---|---|---|
| Vốn chủ sở hữu / tổng tài sản | khoảng 5,7% (12/212 tỷ USD) | [[src-tata-bank-alm#^tata-svb-5]] |
| Lỗ chưa thực hiện trong sổ HTM | 15,2 tỷ USD (sổ 95 tỷ USD, duration 6,25 năm, ứng với lãi suất tăng 2,7%) | [[src-tata-bank-alm#^tata-svb-5]] |
| Lỗ ước tính thêm trong sổ AFS | khoảng 1,7 tỷ USD | [[src-tata-bank-alm#^tata-svb-5]] |
| NII 2022 | 4,5 tỷ USD; thu nhập lãi 2,73%, chi phí lãi 0,57%, NIM 2,15% | [[src-tata-bank-alm#^tata-svb-6]] |
| Tiền gửi không được FDIC bảo hiểm (cuối 2021) | 166 tỷ USD, hơn 88% tiền gửi không kỳ hạn, tăng 87% trong một năm | [[src-tata-bank-alm#^tata-svb-4]] |
| Tiền gửi của start-up và VC "gửi tạm" | khoảng 45% tiền gửi | [[src-tata-bank-alm#^tata-svb-7]] |

**Phòng ngừa.** Cuối 2021 chỉ 15,3 tỷ USD (khoảng 12,3%) trong danh mục trái phiếu khoảng 124 tỷ USD được phòng ngừa bằng swap trả cố định. Nửa đầu 2022 khoảng 11 tỷ USD swap bị tất toán để làm đẹp P&L ngắn hạn; cuối 2022 chỉ còn 0,5 tỷ USD (0,4% danh mục) [[src-tata-bank-alm#^tata-svb-3]].

**Góc nhìn ba thước đo** — NII cho thấy ngân hàng lành mạnh [[src-tata-bank-alm#^tata-svb-6]], nhưng:
- *Kế toán:* sổ HTM ghi theo giá vốn phân bổ theo GAAP che lỗ chưa thực hiện đủ xoá sạch vốn chủ sở hữu [[src-tata-bank-alm#^tata-svb-5]].
- *Duration gap:* kể cả giả định duration tiền gửi gửi tạm 1 năm, gap khoảng 3 năm, tương ứng lỗ khoảng 12,5 tỷ USD (hơn 100% vốn) với cú sốc tăng 200 bp [[src-tata-bank-alm#^tata-svb-7]]. Xem [[duration-gap-model]].
- *Outlier test:* để lỗ EVE dưới 15% vốn, duration tiền gửi phải trên 3,7 năm, một giả định rất bất hợp lý [[src-tata-bank-alm#^tata-svb-7]]. Xem [[outlier-bank-test]].

*Diễn giải (kiểm số):* 209 tỷ × 2% × 3 năm ≈ 12,5 tỷ USD; và 4,1 − (15% × 12)/(209 × 2%) ≈ 4,1 − 0,43 ≈ 3,7 năm, khớp hai con số nguồn đưa ra [[src-tata-bank-alm#^tata-svb-7]].

**Giả định hành vi.** Duration [[non-maturity-deposits]] phải mô hình hoá theo hành vi rút tiền. Tiền gửi SVB tập trung vào doanh nghiệp công nghệ, khoa học sự sống và PE/VC; lượng tiền gửi tạm phụ thuộc hai kênh lãi suất có quan hệ nhân quả khác nhau [[src-tata-bank-alm#^tata-svb-8]]. Tháng 4/2022, SVB tăng giả định duration tiền gửi: rủi ro hiển thị trên mô hình giảm nhưng rủi ro thực không đổi, và giả định không có cơ sở do tiền gửi tăng nhanh, thiếu dữ liệu lịch sử, lãi suất tăng nhanh rút ngắn duration và khách hàng đặc thù [[src-tata-bank-alm#^tata-svb-9]].

## Timeline

| Thời điểm | Sự kiện | Nguồn |
|---|---|---|
| 29/4/2022 – 27/12/2022 | Không có CRO trong 8 tháng | [[src-tata-bank-alm#^tata-svb-3]] |
| Nửa đầu 2022 | Tất toán khoảng 11 tỷ USD swap phòng ngừa | [[src-tata-bank-alm#^tata-svb-3]] |
| 4/2022 | Tăng giả định duration tiền gửi | [[src-tata-bank-alm#^tata-svb-9]] |
| 2022 | Hoạt động VC giảm mạnh; lãi suất tăng nhanh | [[src-tata-bank-alm#^tata-svb-2]] |
| 8/3/2023 | Báo lỗ 1,8 tỷ USD khi bán 21 tỷ USD chứng khoán | [[src-tata-bank-alm#^tata-svb-1]] |
| Q1/2023 | Nhà đầu tư tìm cách rút 42 tỷ USD trong một ngày | [[src-tata-bank-alm#^tata-svb-7]] |
| 10/3/2023 | Sụp đổ, bị cơ quan quản lý tiếp quản | [[src-tata-bank-alm#^tata-svb-1]] |

## Liên quan ALM
**Bài học theo nguồn** [[src-tata-bank-alm#^tata-svb-10]]:
- kế toán có thể tách lỗ chưa thực hiện khỏi thu nhập ròng, nên ALM thận trọng càng quan trọng;
- quản trị rủi ro lãi suất là bắt buộc;
- giả định duration của NMD tương quan cao từ một nhóm nhỏ người gửi phải bị chất vấn; giám sát viên đã thấy thiếu sót IRRBB qua các đợt CAMELS 2020–2022 nhưng không ra kết luận giám sát;
- chênh lệch kỳ hạn lớn không phòng ngừa là nguy cơ lớn.

*Diễn giải:* đối chiếu TT83/2025, ba điểm yếu của SVB chạm đúng các yêu cầu đã có trong wiki:
- thay đổi giả định mô hình hành vi phải qua kiểm định độc lập, tách khỏi bên xây dựng và sử dụng ([[model-validation]], [[three-lines-of-defence]]);
- danh mục dự trữ thanh khoản thuộc sổ ngân hàng nên lỗ giá trị kinh tế của nó đi vào ΔEVE, không bị che bởi phân loại kế toán ([[banking-book]], [[economic-value-of-equity]]);
- kịch bản stress thanh khoản phải xét mức độ tập trung của huy động vốn ([[liquidity-stress-testing]], [[funding-concentration-risk]]).

Xem thêm [[behavioural-options]] về trả trước khi lãi suất tăng nhanh.
