---
title: "Reverse Stress Testing"
aliases: [Reverse Stress Testing, RST, Kiểm tra sức chịu đựng ngược]
type: concept
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[stress-testing]]", cite: "[[src-tt83-2025-nhnn#^d23-3]]"}
  - {type: input-to, to: "[[recovery-and-resolution-planning]]", cite: "[[src-choudhry-principles-banking#^choudhry-rst-9]]"}
tags: [stress-test, recovery, risk-appetite]
updated: 2026-10-19
reviewed:
---

## Ý chính
Reverse stress testing (RST) phân tích các kịch bản làm mô hình kinh doanh của ngân hàng không còn khả thi [[src-choudhry-principles-banking#^choudhry-rst-1]]. RST khác stress test thông thường ở hai điểm [[src-choudhry-principles-banking#^choudhry-rst-1]]:
- **hướng**: bắt đầu từ kết cục rồi dựng ngược kịch bản dẫn tới kết cục đó;
- **mức nghiêm trọng**: đi sâu vào đuôi phân phối, thường tới mức "break the bank".

Theo [[tt83-2025]], kiểm tra sức chịu đựng ngược là một trong ba phương pháp cho rủi ro tín dụng và thị trường: giả định trường hợp bất lợi nghiêm trọng (như vi phạm tỷ lệ an toàn vốn tối thiểu), rồi tìm sự kiện, yếu tố dẫn tới [[src-tt83-2025-nhnn#^d23-3]].

## Cơ chế & drivers

### Sáu bước (Choudhry)
| Bước | Nội dung | Nguồn |
|---|---|---|
| 1. Failure points | Định nghĩa điểm thất bại theo ba góc: lợi nhuận, vốn, thanh khoản, xét riêng từng chiều | [[src-choudhry-principles-banking#^choudhry-rst-3]] |
| 2. Vulnerability analysis | Lập risk inventory, phân loại theo loại failure và time horizon | [[src-choudhry-principles-banking#^choudhry-rst-4]] |
| 3. Generic storyboards | Dựng tám nhóm storyboard từ phân loại ở bước 2 | [[src-choudhry-principles-banking#^choudhry-rst-4]] |
| 4. Scenario design | Hiệu chỉnh từng khối của storyboard; có thể nhưng không bắt buộc dựa vào kịch bản lịch sử hay kịch bản quy định | [[src-choudhry-principles-banking#^choudhry-rst-5]] |
| 5. Plausibility & management actions | Kiểm tra tính hợp lý, back-test với stress đã xảy ra; xác suất quá cao thì ngân hàng phải có biện pháp giảm thiểu | [[src-choudhry-principles-banking#^choudhry-rst-6]] |
| 6. Monitoring & reporting | Theo dõi qua chỉ báo gắn với yếu tố rủi ro; xác suất tăng thì đề xuất biện pháp và leo thang; báo cáo ít nhất hằng năm | [[src-choudhry-principles-banking#^choudhry-rst-7]] |

Ở bước 5, không nhất thiết luôn có management action khả dụng, vì kịch bản RST rất nghiêm trọng [[src-choudhry-principles-banking#^choudhry-rst-6]].

### Ma trận kịch bản (Figure 20.19)
| | Liquidity failure | Capital failure | Capital induced liquidity failure | Earnings failure |
|---|---|---|---|---|
| Instantaneous | 1a: sự kiện rủi ro nghiêm trọng gây mất thanh khoản | 2a: vốn cạn đột ngột | 3a: vốn suy giảm đột ngột làm nghi ngờ khả năng tồn tại, dẫn tới mất thanh khoản | 4a: thay đổi đột ngột làm PTI âm kéo dài |
| Bleeding out | 1b: chuỗi sự kiện rủi ro gây mất thanh khoản | 2b: vốn cạn dần, hạn mức thanh khoản khẩn cấp vẫn còn | 3b: vốn suy giảm liên tục dẫn tới mất thanh khoản | 4b: thay đổi liên tục làm PTI âm |

Nguồn bảng: [[src-choudhry-principles-banking#^choudhry-rst-8]].

### Biến thể
- RST theo từng độ nhạy, ví dụ: dòng ra bất ngờ của tiền gửi không kỳ hạn lớn cỡ nào thì gây lỗ do phải đóng hedge không còn khớp [[src-choudhry-principles-banking#^choudhry-rst-10]]. Xem [[non-maturity-deposits]].
- "Mild RST": hạ ngưỡng lỗ xuống vài triệu USD để thảo luận kịch bản không làm ngân hàng sụp nhưng thử mức chấp nhận rủi ro của Board với một danh mục [[src-choudhry-principles-banking#^choudhry-rst-11]]. Xem [[risk-appetite]].

## Phụ thuộc regime
- Ở một số jurisdiction, cơ quan quản lý yêu cầu ít nhất một RST trong ICAAP, và trong ILAAP nếu có [[src-choudhry-principles-banking#^choudhry-rst-2]]. Mục lục ICAAP mẫu và mục lục ILAAP Choudhry khuyến nghị đều có RST [[src-choudhry-principles-banking#^choudhry-icaap-6]] [[src-choudhry-principles-banking#^choudhry-ilaap-12]].
- **VN**: phương pháp tại TT83/2025 Đ23.3 áp cho rủi ro tín dụng và thị trường; ngân hàng chọn tối thiểu một trong ba phương pháp [[src-tt83-2025-nhnn#^d23-3]]. Kiểm tra sức chịu đựng tín dụng, thị trường áp dụng chậm nhất từ 01/01/2028 [[src-tt83-2025-nhnn#^d74-2]].

## Góc nhìn theo domain
- **Recovery planning**: RST có thể xem là trường hợp đặc biệt của recovery planning, hoặc giúp xác định điểm kích hoạt resolution planning [[src-choudhry-principles-banking#^choudhry-rst-9]]. Liquidity Contingency Plan và Recovery Plan dùng stress "extreme" dưới dạng reverse stress [[src-choudhry-principles-banking#^choudhry-rmf-10]]. Xem [[recovery-and-resolution-planning]].
- **ICAAP**: RST dùng để back-test độ phù hợp và độ nghiêm trọng của bộ kịch bản hiện có [[src-choudhry-principles-banking#^choudhry-rst-9]]. Xem [[icaap]], [[ilaap]].
- **Quản trị**: Stress Testing Policy do Executive Risk Committee sở hữu bao gồm Reverse Stress Testing Policy [[src-choudhry-principles-banking#^choudhry-rmf-7]].
- **Basel**: [cần nguồn].

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Figure 20.18 (sáu bước) và Figure 20.20 (building blocks) chỉ có dạng ảnh trong raw.
- *Diễn giải:* TT83 Đ23.3 cho phép chọn một trong ba phương pháp, nên RST không bắt buộc tại VN nếu ngân hàng chọn độ nhạy hoặc kịch bản; cần đối chiếu Đ60 (vốn) xem có yêu cầu riêng.
