---
title: "LDR Total Loans (L)"
aliases: [LDR Total Loans, Tổng dư nợ cho vay trong LDR, Tử số LDR, LDR numerator]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2026-10-01
valid_to:
as_of:
sources: ["[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[loan-to-deposit-ratio]]", cite: "[[src-tt50-2026-nhnn#^d12-1]]"}
tags: [credit, funding, vn-regulation, ldr]
updated: 2026-10-21
reviewed:
---

## Định nghĩa
L là tử số của [[loan-to-deposit-ratio]] theo TT50/2026: tổng dư nợ cho vay xác định tại Đ12.3, tức tổng các khoản ở Đ12.2 trừ đi các khoản ở Đ12.3 [[src-tt50-2026-nhnn#^d12-2]]. L tính theo VNĐ, gồm ngoại tệ quy đổi theo tỷ giá Đ3.14 [[src-tt50-2026-nhnn#^d12-1]] [[src-tt50-2026-nhnn#^d3-14]]. Mẫu số tương ứng là [[ldr-total-deposits]].

## Công thức

| Chiều | Cấu phần | Điều khoản | Căn cứ |
|---|---|---|---|
| + | Dư nợ gốc nội bảng mà ngân hàng chịu rủi ro từ cho vay cá nhân, tổ chức, kể cả cho vay từ vốn nhận uỷ thác | Đ12.2.a | [[src-tt50-2026-nhnn#^d12-2]] |
| + | Dư nợ gốc nội bảng từ khoản uỷ thác cho TCTD, chi nhánh NHNNg khác cho vay | Đ12.2.b | [[src-tt50-2026-nhnn#^d12-2]] |
| − | Dư nợ cho vay TCTD, chi nhánh NHNNg khác tại VN | Đ12.3.a | [[src-tt50-2026-nhnn#^d12-1]] |
| − | Dư vay tái cấp vốn của NHNN không nhằm mục đích hỗ trợ thanh khoản | Đ12.3.b | [[src-tt50-2026-nhnn#^d12-1]] |

## Giải trình từng đầu mục
- **Đ12.2.a, cho vay khách hàng.** Chỉ tính dư nợ gốc, chỉ nội bảng, và chỉ phần ngân hàng chịu rủi ro [[src-tt50-2026-nhnn#^d12-2]]. *Diễn giải:* lãi dự thu, hạn mức chưa giải ngân và cam kết ngoại bảng không vào L. Cho vay từ vốn nhận uỷ thác mà ngân hàng chịu rủi ro vào L, đối xứng với việc vốn uỷ thác đó vào D [[src-tt50-2026-nhnn#^d12-4d]].
- **Đ12.2.b, uỷ thác cho TCTD khác cho vay.** Tính vào L [[src-tt50-2026-nhnn#^d12-2]]. *Diễn giải:* ngân hàng uỷ thác vẫn chịu rủi ro và đã chi vốn, nên coi như cho vay trực tiếp. Uỷ thác cấp tín dụng khác thì trừ khỏi D [[src-tt50-2026-nhnn#^d12-5]].
- **Đ12.3.a, trừ cho vay TCTD tại VN.** [[src-tt50-2026-nhnn#^d12-1]] *Diễn giải:* liên ngân hàng đi vào LDR một lần, ở dạng ròng qua đầu mục đ của D [[src-tt50-2026-nhnn#^d12-4]]. Cho vay TCTD nước ngoài không thuộc khoản trừ này theo lời văn ("tại Việt Nam") [cần nguồn: hướng dẫn báo cáo NHNN].
- **Đ12.3.b, trừ tái cấp vốn NHNN không nhằm hỗ trợ thanh khoản.** [[src-tt50-2026-nhnn#^d12-1]] *Diễn giải:* đây là khoản bên nợ nhưng được trừ ở tử số. Hiệu ứng là phần cho vay tài trợ bằng tái cấp vốn có mục tiêu (chương trình tín dụng chính sách) không làm LDR tăng. Tái cấp vốn hỗ trợ thanh khoản thì không được trừ.

## Phân loại nghiệp vụ tín dụng
Đ12 chỉ gọi tên "hoạt động cho vay" (vào L) và "cấp tín dụng khác không phải là hoạt động cho vay" (trừ khỏi D) [[src-tt50-2026-nhnn#^d12-2]] [[src-tt50-2026-nhnn#^d12-5]]. TT50 không định nghĩa "cho vay" [cần nguồn: Luật Các TCTD, thông tư về hoạt động cho vay]. Danh sách nghiệp vụ dưới đây lấy từ [[total-credit-outstanding]] tại Đ9.3, trong đó cho vay được liệt kê riêng với chiết khấu, tái chiết khấu, cho thuê tài chính, bao thanh toán [[src-tt50-2026-nhnn#^d9-3]].

| Nghiệp vụ | Đ9.3 | Xử lý trong LDR | Căn cứ | Tác động lên LDR (*Diễn giải*) |
|---|---|---|---|---|
| Cho vay cá nhân, tổ chức không phải TCTD, dư nợ gốc nội bảng, kể cả cho vay bằng vốn nhận uỷ thác mà ngân hàng chịu rủi ro | a | Cộng vào L | [[src-tt50-2026-nhnn#^d12-2]] | Tăng L, LDR tăng |
| Uỷ thác cho TCTD, chi nhánh NHNNg khác cho vay | c | Cộng vào L | [[src-tt50-2026-nhnn#^d12-2]] | Như cho vay trực tiếp |
| Cho vay TCTD, chi nhánh NHNNg khác tại VN | a | Trừ khỏi L | [[src-tt50-2026-nhnn#^d12-1]] | Không vào L; nhưng làm giảm chênh lệch dương liên ngân hàng trong D (Đ12.4.đ) [[src-tt50-2026-nhnn#^d12-4]], nên LDR vẫn có thể tăng |
| Vay tái cấp vốn NHNN không nhằm hỗ trợ thanh khoản (bên nợ, không phải nghiệp vụ cấp tín dụng) | — | Trừ khỏi L | [[src-tt50-2026-nhnn#^d12-1]] | Khoản cho vay tài trợ bằng tái cấp vốn mục tiêu không làm tăng LDR |
| Chiết khấu, tái chiết khấu, cho thuê tài chính, bao thanh toán đối với khách hàng không phải TCTD | a | Không vào L; dư nợ gốc nội bảng trừ khỏi D | [[src-tt50-2026-nhnn#^d9-3]] [[src-tt50-2026-nhnn#^d12-5]] | Xếp vào "cấp tín dụng khác" vì Đ9.3.a liệt kê riêng với cho vay; giảm D, LDR tăng |
| Bảo lãnh, phát hành, xác nhận L/C (cam kết ngoại bảng) | b | Không tính khi còn ngoại bảng; nợ trả thay trừ khỏi D | [[src-tt50-2026-nhnn#^d9-3]] [[src-tt50-2026-nhnn#^d12-5]] | Chỉ tác động khi phát sinh trả thay |
| Hạn mức cho vay chưa giải ngân, hạn mức thẻ tín dụng chưa sử dụng | b | Không tính | [[src-tt50-2026-nhnn#^d9-3]] [[src-tt50-2026-nhnn#^d12-2]] | Đ12 chỉ tính dư nợ gốc nội bảng; giải ngân thì vào L |
| Uỷ thác cho TCTD khác cấp tín dụng khác không phải cho vay | c | Trừ khỏi D | [[src-tt50-2026-nhnn#^d12-5]] | Giảm D |
| Đầu tư trái phiếu doanh nghiệp (mua, nắm giữ trực tiếp hoặc uỷ thác mua), trừ trái phiếu do TCTD khác tại VN phát hành và trái phiếu đặc biệt của VAMC | d | Trừ khỏi D | [[src-tt50-2026-nhnn#^d3-4]] [[src-tt50-2026-nhnn#^d12-4]] | Giảm D. Nhận trái phiếu doanh nghiệp làm tài sản bảo đảm không phải đầu tư; chiết khấu trái phiếu doanh nghiệp rơi vào dòng chiết khấu ở trên |
| Bán nợ chưa nhận đủ tiền | đ | Đ12 không nêu | [[src-tt50-2026-nhnn#^d9-3]] | Theo lời văn Đ12 thì không thuộc L và không thuộc khoản trừ D [cần nguồn: hướng dẫn báo cáo NHNN] |
| Mua nợ (đã thanh toán, trừ phần khách hàng đã trả) | e | Đ12 không nêu | [[src-tt50-2026-nhnn#^d9-3]] | Như trên [cần nguồn] |
| Mua hẳn miễn truy đòi bộ chứng từ theo L/C | g | Đ12 không nêu | [[src-tt50-2026-nhnn#^d9-3]] | Như trên [cần nguồn] |
| Dư nợ chương trình, dự án theo quyết định của Chính phủ, Thủ tướng | — | Xem xét theo quyết định đó | [[src-tt50-2026-nhnn#^d1-4]] | Có thể có ngoại lệ riêng cho L hoặc D |

*Diễn giải:* trong cùng một tổng dư nợ cấp tín dụng, LDR nhạy với cách phân loại. Cho vay làm tăng tử số. Chiết khấu, bao thanh toán, cho thuê tài chính và trái phiếu doanh nghiệp làm giảm mẫu số. Khi LDR dưới 100%, chuyển x từ cho vay sang cấp tín dụng khác làm LDR giảm, vì (L − x)/(D − x) < L/D khi L < D. Ví dụ L = 90, D = 100, x = 10 thì LDR từ 90% còn 88,9%. Khi tăng thêm cấp tín dụng khác tài trợ bằng nguồn ngoài D, L giữ nguyên còn D giảm, nên LDR tăng.

## Ví dụ minh hoạ
*Diễn giải:* số giả định, đơn vị tỷ đồng, cùng bảng cân đối với ví dụ trong [[ldr-total-deposits]] (D = 1.000).

| Đầu mục | Số dư | Tính vào L |
|---|---|---|
| 2.a Cho vay khách hàng không phải TCTD | 820 | 820 |
| 2.a Cho vay TCTD trong nước | 40 | 40 |
| 2.b Uỷ thác cho TCTD khác cho vay | 10 | 10 |
| 3.a Trừ cho vay TCTD trong nước | | −40 |
| 3.b Trừ vay tái cấp vốn NHNN không nhằm hỗ trợ thanh khoản | 30 | −30 |
| **L** | | **800** |

LDR = 800 / 1.000 = 80%, dưới ngưỡng 95% [[src-tt50-2026-nhnn#^d12-6]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Chỉ tiêu tương ứng | Không có LDR trong chuẩn BCBS đã ingest [cần nguồn] | L theo Đ12.2–3 [[src-tt50-2026-nhnn#^d12-2]] [[src-tt50-2026-nhnn#^d12-1]] | TT50 Đ12.2–3 | Từ khi áp dụng LCR/NSFR [[src-tt50-2026-nhnn#^d12-6]] |

## Ứng dụng trong ALM
- *Diễn giải:* L chỉ gồm cho vay; tăng trưởng tín dụng qua chiết khấu, bao thanh toán, cho thuê tài chính không làm L tăng nhưng làm D giảm. Hạn mức LDR nội bộ nên được giám sát cùng [[total-credit-outstanding]] để thấy toàn bộ cấp tín dụng.

## Nhầm lẫn thường gặp
- *Diễn giải:* L không bằng "dư nợ cho vay khách hàng" trên báo cáo tài chính: L loại cho vay TCTD, trừ vay tái cấp vốn mục tiêu và cộng uỷ thác cho TCTD khác cho vay.
