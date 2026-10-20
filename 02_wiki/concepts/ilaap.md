---
title: "ILAAP"
aliases: [ILAAP, Internal Liquidity Adequacy Assessment Process, Individual Liquidity Adequacy Assessment, Đánh giá nội bộ về mức đủ thanh khoản]
type: concept
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]", "[[src-bcbs-liquidity-principles-2008]]", "[[src-bcbs-framework]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[liquidity-risk-management]]", cite: "[[src-choudhry-principles-banking#^choudhry-ilaap-7]]"}
tags: [liquidity, stress-test, pillar-2, governance]
updated: 2026-10-20
reviewed:
---

## Ý chính
ILAAP là quy trình ngân hàng tự đánh giá mức đủ thanh khoản: chạy liquidity stress test trên bảng cân đối, so kết quả với khẩu vị rủi ro thanh khoản, rồi ghi thành tài liệu ILAAP để Board phê duyệt [[src-choudhry-principles-banking#^choudhry-ilaap-1]] [[src-choudhry-principles-banking#^choudhry-ilaap-11]]. Ở UK, cơ quan quản lý rà soát tài liệu này qua L-SREP [[src-choudhry-principles-banking#^choudhry-ilaap-13]]. Cặp tương ứng phía vốn là [[icaap]].

## Cơ chế & drivers

### Quy trình liquidity stress testing
| Bước | Nội dung | Nguồn |
|---|---|---|
| Inventory | Cấu trúc và kỳ hạn của bảng cân đối, kể cả ngoại bảng, tại một ngày | [[src-choudhry-principles-banking#^choudhry-ilaap-1]] |
| Kịch bản | Do ngân hàng tự xây (khác LCR dùng kịch bản của cơ quan quản lý), gồm stress đặc thù, thị trường và vĩ mô; nghiêm trọng nhưng hợp lý, tập trung vào điểm yếu chính | [[src-choudhry-principles-banking#^choudhry-ilaap-2]] |
| Giả định | Dựa trên hành vi lịch sử ở điều kiện thường và stress; ít dữ liệu thì chỉ mô hình ở cấp sản phẩm | [[src-choudhry-principles-banking#^choudhry-ilaap-3]] |
| Output | [[cash-flow-survival-period]]; ngưỡng tối thiểu nằm trong Liquidity Risk Appetite Statement | [[src-choudhry-principles-banking#^choudhry-ilaap-5]] |
| Review | Gửi ALCO và Board; survival period ngắn hơn khẩu vị thì cần biện pháp khắc phục | [[src-choudhry-principles-banking#^choudhry-ilaap-7]] |

Nguồn rủi ro cần xét khi lập giả định gồm funding bán lẻ, wholesale có và không có bảo đảm, tập trung funding, intraday, hạ hạng tín nhiệm, chuyển thanh khoản giữa pháp nhân và internalisation risk [[src-choudhry-principles-banking#^choudhry-ilaap-4]].

### Biện pháp khi survival period dưới khẩu vị
Choudhry nêu ba nhóm [[src-choudhry-principles-banking#^choudhry-ilaap-7]]:
- giảm phơi nhiễm với một số sản phẩm và thị trường;
- giảm hạn mức dòng ra hợp đồng, tức giảm maturity transformation;
- rà lại chiến lược xử lý thiếu hụt trong [[contingency-funding-plan]] [[src-choudhry-principles-banking#^choudhry-ilaap-8]].

### Ví dụ ba kịch bản (ngân hàng UK, Figure 20.16)
| Giả định dòng ra | Firm specific | Market wide | Combined | Nguồn |
|---|---|---|---|---|
| Retail, tài khoản rủi ro cao (dòng ra/ngày) | Tuần 1–2: 2,80%; tuần 3–4: 1,26% | Không có | Tuần 1–2: 1,40%; tuần 3–4: 1,13% | [[src-choudhry-principles-banking#^choudhry-ilaap-9]] |
| Retail, quan hệ lâu năm, rủi ro thấp | Tuần 1–2: 0,750%; tuần 3–4: 0,350% | Không có | Tuần 1–2: 0,40%; tuần 3–4: 0,17% | [[src-choudhry-principles-banking#^choudhry-ilaap-9]] |
| Tiền gửi có kỳ hạn qua cash management platform | Rút 100% khi đáo hạn | Rút 100% khi đáo hạn | Rút 100% khi đáo hạn | [[src-choudhry-principles-banking#^choudhry-ilaap-9]] |
| Tiền gửi có kỳ hạn tại chi nhánh | Rút 25% khi đáo hạn | Rút 15% khi đáo hạn | Rút 25% khi đáo hạn | [[src-choudhry-principles-banking#^choudhry-ilaap-9]] |
| Wholesale funding đáo hạn | Không rollover | Không rollover | Không rollover | [[src-choudhry-principles-banking#^choudhry-ilaap-9]] |

Kịch bản firm specific lấy mốc Northern Rock (mất khoảng 15% số dư bán lẻ) và giả định mức rút bằng khoảng một nửa [[src-choudhry-principles-banking#^choudhry-ilaap-10]]. Mức survival trong ví dụ là OLAR 92 ngày, do ngân hàng tự chọn [[src-choudhry-principles-banking#^choudhry-ilaap-6]].

### Nội dung tài liệu ILAAP
- Tài liệu nên có khẩu vị rủi ro nêu thời gian và loại stress cần vượt qua, các kịch bản, kết quả stress test và biện pháp CFP sẽ áp dụng [[src-choudhry-principles-banking#^choudhry-ilaap-11]].
- ILAAP nên được Board phê duyệt, tương xứng với quy mô và độ phức tạp, cập nhật hằng năm hoặc khi mô hình kinh doanh thay đổi [[src-choudhry-principles-banking#^choudhry-ilaap-11]].
- Không có định dạng bắt buộc. Mục lục Choudhry khuyến nghị có Pillar 2 Liquidity, [[reverse-stress-testing]], phụ lục FTP Policy và deposit pricing [[src-choudhry-principles-banking#^choudhry-ilaap-12]].

## Phụ thuộc regime
- **UK (PRA)**: L-SREP rà soát khung IT, quản trị, cơ chế transfer pricing thanh khoản, kiểm soát liquid asset buffer và hệ thống hạn mức nội bộ [[src-choudhry-principles-banking#^choudhry-ilaap-13]]. Sau L-SREP, PRA đưa Individual Liquidity Guidance; hướng dẫn định lượng bao phủ cả rủi ro thanh khoản mà LCR không nắm được [[src-choudhry-principles-banking#^choudhry-ilaap-14]].
- Ở một số jurisdiction, ILAAP phải có ít nhất một reverse stress test [[src-choudhry-principles-banking#^choudhry-rst-2]].

## Góc nhìn theo domain
- **ALM**: ILAAP, ICAAP, recovery planning và resolution planning được làm tích hợp trong cùng RMF [[src-choudhry-principles-banking#^choudhry-rmf-9]]. Risk Taxonomy ba cấp do ALCO phê duyệt là đầu vào của ICAAP và ILAAP [[src-choudhry-principles-banking#^choudhry-rmf-3]].
- **VN**: TT83/2025 yêu cầu kiểm tra sức chịu đựng thanh khoản với 3 kịch bản và lập kế hoạch dự phòng từ kết quả đó [[src-tt83-2025-nhnn#^d48-2]] [[src-tt83-2025-nhnn#^d48-4]]. Xem [[liquidity-stress-testing]]. *Diễn giải:* trong các claim TT83 đã ingest, wiki chưa thấy điều khoản nào gọi tên ILAAP hay yêu cầu tài liệu đánh giá mức đủ thanh khoản riêng như ICAAP (Đ59–63).
- **Basel**: BCBS không có chuẩn mang tên ILAAP. Các thành phần tương ứng nằm trong [[bcbs-liquidity-principles]] (BCBS 144, 9/2008) và SRP30.48–30.52.

| Thành phần ILAAP | Yêu cầu Basel | Nguồn |
|---|---|---|
| Khung quản trị và đệm thanh khoản | Khung quản trị rủi ro thanh khoản vững chắc, đệm tài sản thanh khoản cao không bị cầm cố, chịu được stress làm mất nguồn vốn có và không có bảo đảm | [[src-bcbs-liquidity-principles-2008#^lrm-p01]] |
| Chứng minh mức đủ | Ngân hàng nên chứng minh đệm tương xứng với độ phức tạp hoạt động, mức chênh lệch funding và chiến lược funding; dùng giả định thận trọng | [[src-bcbs-liquidity-principles-2008#^lrm-8b]] |
| Khẩu vị rủi ro | HĐQT đặt liquidity risk tolerance; stress test bảo đảm phơi nhiễm nằm trong tolerance | [[src-bcbs-framework#^srp30-50]] [[src-bcbs-liquidity-principles-2008#^lrm-p10]] |
| Kịch bản | Ngắn hạn và kéo dài, riêng ngân hàng và toàn thị trường, đơn lẻ và kết hợp; theo điểm yếu riêng | [[src-bcbs-liquidity-principles-2008#^lrm-p10]] [[src-bcbs-liquidity-principles-2008#^lrm-98]] |
| Phạm vi | Hợp nhất, pháp nhân, mảng kinh doanh; nhiều kỳ hạn kể cả trong ngày | [[src-bcbs-liquidity-principles-2008#^lrm-95]] |
| Giả định | Thận trọng; 17 giả định minh hoạ (run-off bán lẻ, wholesale, margin call, rating trigger, chuyển thanh khoản giữa pháp nhân, tiếp cận NHTW…) | [[src-bcbs-liquidity-principles-2008#^lrm-103]] |
| Tài liệu và rà soát | Lựa chọn kịch bản, giả định được lập hồ sơ; ban điều hành rà soát; kết quả báo cáo HĐQT và cơ quan giám sát | [[src-bcbs-liquidity-principles-2008#^lrm-108]] |
| Sử dụng kết quả | Đưa vào kế hoạch chiến lược, quản trị rủi ro hằng ngày và hạn mức nội bộ | [[src-bcbs-liquidity-principles-2008#^lrm-108]] |
| Biện pháp khi thiếu | Thiếu hụt dự phóng vượt tolerance thì điều chỉnh vị thế thanh khoản hoặc tăng cường CFP, tham vấn HĐQT | [[src-bcbs-liquidity-principles-2008#^lrm-109]] |
| CFP | CFP chính thức, gắn với kết quả stress test; rà soát ít nhất hằng năm để HĐQT phê duyệt | [[src-bcbs-liquidity-principles-2008#^lrm-112]] [[src-bcbs-liquidity-principles-2008#^lrm-121]] |

- **Basel vs ILAAP kiểu UK**: *Diễn giải:* khác biệt chính giữa Basel và ILAAP kiểu UK ở hình thức. Choudhry mô tả ILAAP là tài liệu do Board phê duyệt và được L-SREP rà soát [[src-choudhry-principles-banking#^choudhry-ilaap-11]] [[src-choudhry-principles-banking#^choudhry-ilaap-13]]. BCBS 144 đặt nội dung tương đương nhưng không yêu cầu một tài liệu tự đánh giá riêng; output được nêu là báo cáo kết quả stress test lên HĐQT và cơ quan giám sát. BCBS 144 cũng không đặt survival period tối thiểu, còn Choudhry dùng [[cash-flow-survival-period]] làm output chính.

## Bằng chứng thực nghiệm
- Ví dụ của Choudhry: survival period tăng từ 49 lên 93 ngày [[src-choudhry-principles-banking#^choudhry-st-20]].

## Câu hỏi mở
- Mục lục ILAAP Figure 20.17 đánh số trùng mục 17 (Reverse Stress Test và ILAAP challenge) trong raw.
