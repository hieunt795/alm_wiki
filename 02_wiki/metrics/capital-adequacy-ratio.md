---
title: "Capital Adequacy Ratio"
aliases: [Capital Adequacy Ratio, CAR, Tỷ lệ an toàn vốn, Tỷ lệ vốn lõi cấp 1, Tỷ lệ vốn cấp 1, CET1 ratio, Tier 1 ratio]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2025-09-15
valid_to:
as_of:
sources: ["[[src-tt14-2025-nhnn]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[target-capital]]", cite: "[[src-tt83-2025-nhnn#^pl6-2]]"}
tags: [capital, car, tt14]
updated: 2026-10-23
reviewed:
---

## Định nghĩa
TT14/2025 quy định ba tỷ lệ an toàn vốn: tỷ lệ vốn lõi cấp 1, tỷ lệ vốn cấp 1 và tỷ lệ an toàn vốn (CAR). Ba tỷ lệ có chung mẫu số, và khác nhau ở tử số là vốn lõi cấp 1, vốn cấp 1 hoặc [[own-funds]] [[src-tt14-2025-nhnn#^d5-1a]] [[src-tt14-2025-nhnn#^d5-1b]] [[src-tt14-2025-nhnn#^d5-1c]].

Thông tư áp dụng cho ngân hàng thương mại và chi nhánh ngân hàng nước ngoài [[src-tt14-2025-nhnn#^d1-1]]. Ngân hàng thương mại được kiểm soát đặc biệt, và ngân hàng thương mại được can thiệp sớm thực hiện lộ trình tuân thủ theo văn bản chấp thuận của NHNN, nằm ngoài phạm vi áp dụng [[src-tt14-2025-nhnn#^d1-3]].

## Công thức
$$
\text{Tỷ lệ vốn lõi cấp 1} = \frac{\text{Vốn lõi cấp 1}}{RWA + 12{,}5 \times (K_{OR} + K_{MR})}
$$
[[src-tt14-2025-nhnn#^d5-1a]]

$$
\text{Tỷ lệ vốn cấp 1} = \frac{\text{Vốn cấp 1}}{RWA + 12{,}5 \times (K_{OR} + K_{MR})}
$$
[[src-tt14-2025-nhnn#^d5-1b]]

$$
\text{Tỷ lệ an toàn vốn} = \frac{\text{Vốn tự có}}{RWA + 12{,}5 \times (K_{OR} + K_{MR})}
$$
[[src-tt14-2025-nhnn#^d5-1c]]

| Ký hiệu | Ý nghĩa | Nguồn |
|---|---|---|
| Vốn lõi cấp 1, vốn cấp 1, vốn tự có | Theo Phụ lục I của TT14/2025: [[common-equity-tier-1-capital]], vốn cấp 1 ([[additional-tier-1-capital]]), [[own-funds]] | [[src-tt14-2025-nhnn#^d5-1d]] |
| RWA | Tổng tài sản có rủi ro tín dụng (Risk weighted assets) | [[src-tt14-2025-nhnn#^d5-1d]] |
| $K_{OR}$ | Vốn yêu cầu cho rủi ro hoạt động (xem [[operational-risk-capital-requirement]]) | [[src-tt14-2025-nhnn#^d5-1d]] |
| $K_{MR}$ | Vốn yêu cầu cho rủi ro thị trường (xem [[market-risk-capital-requirement]]) | [[src-tt14-2025-nhnn#^d5-1d]] |

## Diễn giải
**Mức tối thiểu.** Ngân hàng thương mại không có công ty con và chi nhánh ngân hàng nước ngoài duy trì ba tỷ lệ riêng lẻ [[src-tt14-2025-nhnn#^d5-3]]. Ngân hàng thương mại có công ty con duy trì ba tỷ lệ ở cả hai cấp, riêng lẻ và hợp nhất [[src-tt14-2025-nhnn#^d5-4]].

| Tỷ lệ | Mức tối thiểu | Cộng CCB đầy đủ (năm thứ tư trở đi) | Nguồn |
|---|---|---|---|
| Vốn lõi cấp 1 | 4,5% | 7% | [[src-tt14-2025-nhnn#^d5-3]] [[src-tt14-2025-nhnn#^d5-5b]] |
| Vốn cấp 1 | 6% | 8,5% | [[src-tt14-2025-nhnn#^d5-3]] [[src-tt14-2025-nhnn#^d5-5b]] |
| An toàn vốn (CAR) | 8% | 10,5% | [[src-tt14-2025-nhnn#^d5-3]] [[src-tt14-2025-nhnn#^d5-5b]] |

**Cấu phần của mẫu số.** Mẫu số gồm RWA cộng 12,5 lần tổng $K_{OR}$ và $K_{MR}$ [[src-tt14-2025-nhnn#^d5-1d]]. $K_{OR}$ bằng BIC × ILM [[src-tt14-2025-nhnn#^d70-1]]. $K_{MR}$ gồm $K_{IRR}$, $K_{ER}$, $K_{FXR}$, $K_{CMR}$, $K_{OPT}$ [[src-tt14-2025-nhnn#^d74-1]]. Rủi ro lãi suất thuộc rủi ro thị trường là rủi ro đối với giấy tờ có giá, công cụ tài chính có lãi suất và phái sinh lãi suất trên sổ kinh doanh [[src-tt14-2025-nhnn#^d2-19a]]. Phân loại hai sổ xem [[banking-book]].

**Hợp nhất.** Ngân hàng thương mại không hợp nhất công ty con hoạt động theo Luật Kinh doanh bảo hiểm khi tính tỷ lệ hợp nhất [[src-tt14-2025-nhnn#^d5-2c]]. Ngân hàng thương mại phải dùng phương pháp tiêu chuẩn để tính tài sản có rủi ro tín dụng của công ty con [[src-tt14-2025-nhnn#^d5-2c]].

**Bộ đệm và yêu cầu bổ sung.** Ngân hàng thực hiện thêm [[capital-conservation-buffer]] và [[countercyclical-capital-buffer]] [[src-tt14-2025-nhnn#^d5-5a]] [[src-tt14-2025-nhnn#^d5-6]]. NHNN có thể yêu cầu tỷ lệ cao hơn mức quy định, và quyết định tỷ lệ bộ đệm vốn đối với ngân hàng thương mại có tầm quan trọng hệ thống [[src-tt14-2025-nhnn#^d5-8]].

**Quy đổi ngoại tệ, vàng.** Khoản mục bằng ngoại tệ và vàng được quy đổi sang đồng Việt Nam khi tính tỷ lệ. Ngày báo cáo không phải ngày làm việc thì dùng tỷ giá và giá vàng của ngày làm việc liền trước [[src-tt14-2025-nhnn#^d5-7]].

**Lộ trình áp dụng** [[src-tt14-2025-nhnn#^d7-1]]:
- Ngân hàng phải áp dụng Thông tư từ 01/01/2030, trừ Chương III (IRB).
- Ngân hàng có khả năng thực hiện phương pháp tiêu chuẩn sớm hơn được đăng ký với NHNN thời điểm bắt đầu áp dụng [[src-tt14-2025-nhnn#^d7-2a]].
- Từ thời điểm đó, ngân hàng thực hiện phương pháp tiêu chuẩn cùng các quy định khác của Thông tư, trừ Chương III, và dừng thực hiện các thông tư tại Đ82.3 điểm a, b, c [[src-tt14-2025-nhnn#^d7-2b]].
- IRB cần đăng ký kèm kế hoạch triển khai, rồi được NHNN chấp thuận. Điều kiện chấp thuận gồm tối thiểu 02 năm kể từ ngày đăng ký, và 02 năm liên tục liền kề trước khi nộp hồ sơ được kiểm toán độc lập và Hội đồng quản trị, Hội đồng thành viên hoặc Tổng Giám đốc (Giám đốc) đánh giá đã tuân thủ [[src-tt14-2025-nhnn#^d7-3a]] [[src-tt14-2025-nhnn#^d7-3b]].
- Sau khi được chấp thuận, ngân hàng không phải tuân thủ mức tối thiểu tính theo phương pháp tiêu chuẩn [[src-tt14-2025-nhnn#^d7-3c]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Tỷ lệ vốn lõi cấp 1 tối thiểu | [cần nguồn] (CAP, RBC20 chưa ingest) | 4,5% [[src-tt14-2025-nhnn#^d5-3]] | Đ5.3a, Đ5.4a | Bắt buộc từ 01/01/2030, đăng ký sớm theo Đ7 [[src-tt14-2025-nhnn#^d7-1]] |
| Tỷ lệ vốn cấp 1 tối thiểu | [cần nguồn] | 6% [[src-tt14-2025-nhnn#^d5-3]] | Đ5.3b, Đ5.4b | Như trên |
| Tỷ lệ an toàn vốn tối thiểu | [cần nguồn] | 8% [[src-tt14-2025-nhnn#^d5-3]] | Đ5.3c, Đ5.4c | Như trên |
| Mẫu số | [cần nguồn] | RWA + 12,5 × ($K_{OR}$ + $K_{MR}$) [[src-tt14-2025-nhnn#^d5-1d]] | Đ5.1 | Như trên |
| Bộ đệm bảo toàn vốn | [cần nguồn] (RBC30 chưa ingest) | Lộ trình 0,625% → 2,5% ([[capital-conservation-buffer]]) | Đ5.5 | Năm thứ nhất theo Đ5.5b |
| Bộ đệm phản chu kỳ | [cần nguồn] | 0%–2,5% do Thống đốc quyết định ([[countercyclical-capital-buffer]]) | Đ5.6 | Theo từng thời kỳ |
| Thước đo vốn của [[leverage-ratio]] | Tier 1 = CET1 + AT1 theo CAP10 [[src-bcbs-lev#^lev20-4]] | Vốn cấp 1 theo quy định tỷ lệ an toàn vốn đang áp dụng [[src-tt50-2026-nhnn#^d8-1]] | Đ5.1b | Như trên |

## Ứng dụng trong ALM
*Diễn giải:* mẫu số của Đ5.1 chỉ có ba cấu phần: RWA, $K_{OR}$, $K_{MR}$ [[src-tt14-2025-nhnn#^d5-1d]]. Rủi ro lãi suất thuộc $K_{MR}$ gắn với sổ kinh doanh [[src-tt14-2025-nhnn#^d2-19a]]. IRRBB trên sổ ngân hàng không có cấu phần riêng ở mẫu số này. Vốn cho IRRBB được ngân hàng xét trong [[icaap]] qua [[rwa-irrbb]] và [[economic-capital]] theo TT83/2025.

*Diễn giải:* vốn tự có để đáp ứng tỷ lệ an toàn vốn là $C_R$ trong [[target-capital]] [[src-tt83-2025-nhnn#^pl6-2]]. Vì vậy ba tỷ lệ tối thiểu và CCB là sàn của [[capital-plan]].

*Diễn giải:* CAR là tỷ số của vốn trên tài sản tính theo rủi ro nên mỗi quyết định tăng RWA (tăng cho vay hệ số rủi ro cao) hoặc tăng vốn tự có đều đổi tỷ lệ. [[capital-adequacy-management]] mô tả vai trò quản trị.

## Nhầm lẫn thường gặp
- Ba tỷ lệ có chung mẫu số. Tử số khác nhau, nên một ngân hàng có thể đạt CAR 8% nhưng vẫn thiếu tỷ lệ vốn lõi cấp 1 tối thiểu 4,5% [[src-tt14-2025-nhnn#^d5-3]].
- CCB là phần tỷ lệ vốn lõi cấp 1 còn lại sau khi đáp ứng đủ ba tỷ lệ, tính ngoài các mức tối thiểu [[src-tt14-2025-nhnn#^d5-5a]].
- *Diễn giải:* hạn mức liên quan đến vốn tự có ở TT50/2026 (giới hạn cấp tín dụng, LDR) không phải tỷ lệ an toàn vốn, xem [[total-credit-outstanding]].
