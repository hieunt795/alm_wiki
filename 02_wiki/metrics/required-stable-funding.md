---
title: "Required Stable Funding (RSF)"
aliases: [RSF, Nguồn vốn ổn định cần thiết, Required Stable Funding]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "-", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
tags: [liquidity, nsfr, assets, funding-requirement]
updated: 2026-10-21
reviewed:
---

## Định nghĩa chuẩn mực

**Required Stable Funding (RSF)** là mẫu số của tỷ lệ [[nsfr]], đại diện cho tổng lượng vốn ổn định tối thiểu mà ngân hàng bắt buộc phải duy trì để tài trợ cho danh mục tài sản nội bảng và các cam kết cấp vốn ngoại bảng trong khoảng thời gian một năm [[src-bcbs-nsfr#^nsf20-2]] [[src-bcbs-nsfr#^nsf30-3]].

Hệ số RSF áp dụng cho từng loại tài sản được hiệu chỉnh dựa trên 4 đặc tính rủi ro thanh khoản cốt lõi [[src-bcbs-nsfr#^nsf30-3]] [[src-bcbs-nsfr#^nsf30-15]]:
1. **Mức độ thanh khoản của tài sản (Asset Liquidity Profile)**: Khả năng chuyển hóa thành tiền mặt thông qua bán đứt hoặc thế chấp vay repo trên thị trường mà không bị chiết khấu giá trị nghiêm trọng.
2. **Kỳ hạn hợp đồng còn lại (Residual Maturity)**: Tài sản có kỳ hạn dài hơn đòi hỏi nguồn tài trợ ổn định dài hơn.
3. **Chất lượng tín dụng (Credit Quality)**: Tài sản có trọng số rủi ro tín dụng (Risk Weight theo chuẩn CRE20) thấp hơn đòi hỏi ít vốn ổn định hơn.
4. **Mức độ cầm cố (Encumbrance Status)**: Tài sản [[asset-encumbrance|bị cầm cố]] trong thời gian dài không thể dùng để tạo thanh khoản và phải chịu hệ số RSF tối đa 100%.

---

## Công thức xác định

Theo Chuẩn mực Basel (NSF30.15, NSF99.2), tổng nguồn vốn ổn định cần thiết được xác định bằng tổng giá trị ghi sổ của tài sản nội bảng và giá trị danh nghĩa của cam kết ngoại bảng nhân với hệ số RSF tương ứng [[src-bcbs-nsfr#^nsf30-15]] [[src-bcbs-nsfr#^nsf99-2]]:

$$
\text{RSF} = \sum_{i} \text{Asset Carrying Amount}_i \times \text{RSF Factor}_i + \sum_{j} \text{OBS Notional Amount}_j \times \text{RSF Factor}_j
$$

Khai triển theo 8 tầng hệ số giám sát:

$$
\text{RSF} = 0.00 \times A_{0\%} + 0.05 \times A_{5\%} + 0.10 \times A_{10\%} + 0.15 \times A_{15\%} + 0.50 \times A_{50\%} + 0.65 \times A_{65\%} + 0.85 \times A_{85\%} + 1.00 \times A_{100\%} + \text{OBS}_{\text{RSF}}
$$

Trong đó $\text{Asset Carrying Amount}_i$ là giá trị ghi sổ kế toán sau khi trừ đi các khoản dự phòng rủi ro cụ thể theo chuẩn mực kế toán [[src-bcbs-nsfr#^nsf30-15]].

---

## Diễn giải & Cơ chế Phân tầng 8 Nhóm Hệ số RSF

Basel thiết lập ma trận 8 bậc hệ số RSF tăng dần theo mức độ kém thanh khoản của tài sản [[src-bcbs-nsfr#^nsf30-15]]:

| Hệ số RSF | Cấu phần tài sản nội bảng và ngoại bảng | Căn cứ chuẩn mực |
|:---:|---|---|
| **0%** | - Tiền mặt, tiền xu sẵn sàng để thanh toán [[src-bcbs-nsfr#^nsf30-25]].<br>- Toàn bộ dự trữ tại Ngân hàng Trung ương (cả dự trữ bắt buộc và vượt mức) [[src-bcbs-nsfr#^nsf30-25]].<br>- Các khoản khiếu nại đối với NHTW có kỳ hạn còn lại $< 6$ tháng [[src-bcbs-nsfr#^nsf30-25]].<br>- Các khoản phải thu ngày giao dịch (trade date receivables) [[src-bcbs-nsfr#^nsf30-25]]. | NSF30.25 |
| **5%** | - Tài sản [[level-1-assets]] unencumbered theo chuẩn LCR30.41 (trừ tiền mặt và dự trữ NHTW nhận 0%), gồm trái phiếu chính phủ 0% RW, nợ công phát hành bằng ngoại tệ [[src-bcbs-nsfr#^nsf30-26]]. | NSF30.26 |
| **10%** | - Các khoản cho vay unencumbered đối với định chế tài chính kỳ hạn $< 6$ tháng có bảo đảm bằng tài sản Level 1 mà ngân hàng có quyền tự do tái thế chấp [[src-bcbs-nsfr#^nsf30-27]]. | NSF30.27 |
| **15%** | - Tài sản [[level-2-assets\|Level 2A]] unencumbered (chứng khoán 20% RW, trái phiếu DN/covered bonds từ AA- trở lên) [[src-bcbs-nsfr#^nsf30-28]].<br>- Các khoản cho vay unencumbered khác đối với định chế tài chính kỳ hạn $< 6$ tháng [[src-bcbs-nsfr#^nsf30-28]]. | NSF30.28 |
| **50%** | - Tài sản Level 2B unencumbered (RMBS AA, trái phiếu DN BBB- đến A+, cổ phiếu lớn phi tài chính) [[src-bcbs-nsfr#^nsf30-29]].<br>- Bất kỳ tài sản [[hqla]] nào bị cầm cố từ **6 tháng đến dưới 1 năm** [[src-bcbs-nsfr#^nsf30-29]].<br>- Cho vay định chế tài chính và NHTW kỳ hạn từ **6 tháng đến dưới 1 năm** [[src-bcbs-nsfr#^nsf30-29]].<br>- Tiền gửi vận hành ([[operational-deposits]]) gửi tại định chế tài chính khác [[src-bcbs-nsfr#^nsf30-29]].<br>- Tất cả các khoản cho vay non-HQLA khác kỳ hạn $< 1$ năm (cho vay DN phi tài chính, bán lẻ, SME, chính phủ) [[src-bcbs-nsfr#^nsf30-29]]. | NSF30.29 |
| **65%** | - Cho vay thế chấp nhà ở unencumbered kỳ hạn $\ge 1$ năm có trọng số rủi ro $\text{RW} \le 35\%$ theo phương pháp Chuẩn hóa CRE20 [[src-bcbs-nsfr#^nsf30-30]].<br>- Các khoản cho vay unencumbered khác kỳ hạn $\ge 1$ năm có $\text{RW} \le 35\%$ (trừ cho vay tổ chức tài chính) [[src-bcbs-nsfr#^nsf30-30]]. | NSF30.30 |
| **85%** | - Tiền mặt hoặc chứng khoán ký quỹ ban đầu (*initial margin*) cho phái sinh và đóng góp quỹ vỡ nợ của CCP [[src-bcbs-nsfr#^nsf30-31]].<br>- Các khoản cho vay unencumbered đủ tiêu chuẩn kỳ hạn $\ge 1$ năm có $\text{RW} > 35\%$ (trừ định chế tài chính) [[src-bcbs-nsfr#^nsf30-31]].<br>- Chứng khoán không phải HQLA kỳ hạn $\ge 1$ năm và cổ phiếu niêm yết trên sàn giao dịch [[src-bcbs-nsfr#^nsf30-31]].<br>- Hàng hóa giao dịch thực thể, bao gồm vàng [[src-bcbs-nsfr#^nsf30-31]]. | NSF30.31 |
| **100%** | - Toàn bộ tài sản bị **cầm cố từ 1 năm trở lên** [[src-bcbs-nsfr#^nsf30-32]].<br>- Tài sản phái sinh ròng NSFR (nếu tài sản phái sinh lớn hơn nợ phái sinh) [[src-bcbs-nsfr#^nsf30-32]].<br>- **5% đến 20%** (theo quyết định quốc gia) của tổng nợ phái sinh gộp [[src-bcbs-nsfr#^nsf30-32]].<br>- Nợ xấu (Non-performing loans - NPLs quá hạn $> 90$ ngày) [[src-bcbs-nsfr#^nsf30-32]].<br>- Cho vay định chế tài chính kỳ hạn $\ge 1$ năm [[src-bcbs-nsfr#^nsf30-32]].<br>- Cổ phiếu chưa niêm yết, tài sản cố định, các khoản khấu trừ vốn quy định [[src-bcbs-nsfr#^nsf30-32]]. | NSF30.32 |

### Các Quy tắc Kỹ thuật Đặc thù

#### 1. Khung Quản trị Cầm cố Tài sản (Encumbrance Framework)
Tài sản bị cầm cố để bảo đảm nghĩa vụ nợ (repo, phát hành covered bonds, ký quỹ phái sinh) bị hạn chế chuyển hóa thành tiền mặt [[src-bcbs-nsfr#^nsf30-20]]:
- **Cầm cố $\ge 1$ năm**: Nhận hệ số RSF $100\%$, bất kể tài sản gốc là trái phiếu chính phủ Level 1 hay tiền mặt [[src-bcbs-nsfr#^nsf30-20]].
- **Cầm cố từ 6 tháng đến dưới 1 năm**: Nhận hệ số RSF tối thiểu $50\%$ (đối với HQLA) [[src-bcbs-nsfr#^nsf30-20]].
- **Cầm cố dưới 6 tháng**: Nhận hệ số RSF tương đương như tài sản unencumbered [[src-bcbs-nsfr#^nsf30-20]].

#### 2. Xử lý Phái sinh trong Mẫu số RSF
- **Tài sản phái sinh ròng**: Xác định bằng chi phí thay thế dương (replacement cost) trừ đi khoản variation margin bằng tiền mặt nhận về đủ điều kiện [[src-bcbs-nsfr#^nsf30-23]]. Phần chênh lệch ròng này nhận hệ số **RSF 100%** [[src-bcbs-nsfr#^nsf30-32]].
- **Phụ phí rủi ro nợ phái sinh gộp (Derivative Liabilities Add-on)**: Ngân hàng phải trích lập thêm nguồn vốn ổn định bằng **5% đến 20% tổng nợ phái sinh gộp** (tính trước khi trừ variation margin đã đặt cọc) nhân với hệ số RSF 100% [[src-bcbs-nsfr#^nsf30-32]].

#### 3. Cam kết Ngoại bảng (Off-balance Sheet)
- Hạn mức tín dụng và thanh khoản chưa rút không thể hủy ngang hoặc chỉ hủy ngang có điều kiện (*irrevocable/conditionally revocable*) chịu hệ số **RSF 5%** trên giá trị chưa rút [[src-bcbs-nsfr#^nsf30-34]].

---

## Theo TT50/2026: giải trình từng đầu mục RSF

### Công thức và nguyên tắc chung
$$\text{RSF} = \sum_{i} \text{Giá trị thành phần}_i \times \text{Hệ số RSF}_i$$
[[src-tt50-2026-nhnn#^d24-1]]

- **Phạm vi:** toàn bộ tài sản trên báo cáo tài chính, cam kết ngoại bảng và các phần giá trị khác được phân loại vào Bảng 10 PL2 [[src-tt50-2026-nhnn#^pl2-b1]].
- **Giá trị:** giá trị ghi sổ sau dự phòng cụ thể, hao mòn và các khoản giảm trừ khác theo kế toán [[src-tt50-2026-nhnn#^pl2-b1-2]]. Ngoại lệ: tài sản phái sinh NSFR tính theo Đ25, tài sản thuộc cặp phụ thuộc tính theo Đ26 [[src-tt50-2026-nhnn#^pl2-b1-2]]. Cam kết ngoại bảng tính phần hạn mức chưa sử dụng; khoản phải đòi vỡ nợ xác định theo TT14/2025 [[src-tt50-2026-nhnn#^pl2-b1]].
- **Thứ tự phân loại:** tài sản xếp vào khoản đầu tiên phù hợp, từ trên xuống. Mọi tài sản từ A.4 đến A.20 là tài sản không bị ràng buộc [[src-tt50-2026-nhnn#^pl2-b2]]. *Diễn giải:* tài sản bị ràng buộc rơi vào A.3 trước khi xét tới A.8 (HQLA) hay A.18 (cho vay). Trái phiếu Chính phủ đem repo một năm vì vậy nhận 100%, không phải 5%.
- **Hiệu lực:** NSFR áp dụng từ 01/10/2028 theo lộ trình 90%, 95%, 100% [[src-tt50-2026-nhnn#^d13-1]] [[src-tt50-2026-nhnn#^d22-2]].

### Bước 1: xác định kỳ hạn (Đ24.3–24.6)
Kỳ hạn của tài sản là khoảng thời gian từ ngày tính NSFR đến thời điểm **muộn nhất** phải thực hiện nghĩa vụ [[src-tt50-2026-nhnn#^d24-1]].

| Tình huống | Kỳ hạn dùng để phân loại | Căn cứ |
|---|---|---|
| Không bên nào có quyền gia hạn | Thời điểm đến hạn theo thoả thuận | [[src-tt50-2026-nhnn#^d24-1]] |
| Khách hàng có quyền gia hạn | Thời điểm muộn nhất khách hàng được gia hạn | [[src-tt50-2026-nhnn#^d24-3c]] |
| Ngân hàng được cơ cấu lại thời hạn trả nợ theo pháp luật có quy định thời gian tối đa | Gồm cả thời gian cơ cấu lại tối đa theo pháp luật | [[src-tt50-2026-nhnn#^d24-3c]] |
| Ngân hàng được cơ cấu lại theo thoả thuận | Thời hạn còn lại gồm cả thời gian đã cơ cấu; chưa cơ cấu thì theo thời điểm đến hạn | [[src-tt50-2026-nhnn#^d24-3c]] |
| Cả ngân hàng và khách hàng có quyền gia hạn | Thời điểm muộn hơn | [[src-tt50-2026-nhnn#^d24-3c]] |
| Ngân hàng có quyền bán lại, rút trước hạn; khách hàng có quyền trả nợ sớm | Giả định không bên nào thực hiện quyền | [[src-tt50-2026-nhnn#^d24-3c]] |
| Khoản vay trả nhiều kỳ | Tách từng phần trả nợ theo thời điểm trả | [[src-tt50-2026-nhnn#^d24-5]] |
| Tài sản bị ràng buộc | Hệ số theo thời gian bị ràng buộc còn lại | [[src-tt50-2026-nhnn#^d24-1]] |
| Đã đặt lệnh mua, bán chưa quyết toán (trừ phái sinh, repo) | Tài sản đã mua tính vào RSF, tài sản đã bán loại ra | [[src-tt50-2026-nhnn#^d24-6]] |

*Diễn giải:* phía tài sản chọn kỳ hạn **dài nhất có thể xảy ra**, ngược với phía ASF chọn kỳ hạn ngắn nhất [[available-stable-funding]]. Quyền trả nợ trước hạn của khách hàng không được tính, vì ngân hàng không kiểm soát được việc đó. Quyền cơ cấu lại nợ của ngân hàng thì được tính, vì khi khách hàng gặp khó khăn ngân hàng thường phải gia hạn. Basel có nguyên tắc tương tự: giả định nhà đầu tư thực hiện quyền gia hạn [[src-bcbs-nsfr#^nsf30-17]].

### Bước 2: phân loại Bảng 10
Hệ số theo cột: không kỳ hạn / dưới 6 tháng / 6 tháng – dưới 1 năm / từ 1 năm / không xác định kỳ hạn.

| Khoản | Đầu mục | KKH | < 6T | 6T–1N | ≥ 1N | KXĐ | Căn cứ |
|---|---|---|---|---|---|---|---|
| A.1 | Khoản phải đòi vỡ nợ | 100% | | | | | [[src-tt50-2026-nhnn#^pl2-b2-1]] |
| A.2 | Tài sản ký quỹ ban đầu cho phái sinh | 85%* | 85%* | 85%* | 100% | 100% | [[src-tt50-2026-nhnn#^pl2-b2-1]] |
| A.3 | Tài sản bị ràng buộc | Như không bị ràng buộc | | 50% hoặc cao hơn | 100% | 100% | [[src-tt50-2026-nhnn#^pl2-b2-1]] |
| A.4 | Tài sản thuộc cặp phụ thuộc | 0% | 0% | 0% | 0% | | [[src-tt50-2026-nhnn#^pl2-b2-1]] |
| A.5 | Tài sản phái sinh NSFR ròng | 100% | | | | | [[src-tt50-2026-nhnn#^pl2-b2-1]] |
| A.6 | Trade date receivables | 0% | | | | | [[src-tt50-2026-nhnn#^pl2-b2-1]] |
| A.7 | Khoản giảm trừ khỏi vốn tự có (một số mục TT14, TT41) | | 100% | 100% | 100% | 100% | [[src-tt50-2026-nhnn#^pl2-b2-1]] |
| A.8.1–8.2 | Tiền mặt, tiền gửi dự trữ bắt buộc (cả phần vượt) | 0% | | | | | [[src-tt50-2026-nhnn#^pl2-b2-8]] |
| A.8.3 | HQLA do NHNN phát hành, còn dưới 6 tháng | 0% | 0% | | | | [[src-tt50-2026-nhnn#^pl2-b2-8]] |
| A.8.4 | HQLA cấp 1 khác | | 5% | 5% | 5% | 5% | [[src-tt50-2026-nhnn#^pl2-b2-8]] |
| A.8.5 | HQLA cấp 2A | | 15% | 15% | 15% | 15% | [[src-tt50-2026-nhnn#^pl2-b2-8]] |
| A.8.6 | HQLA cấp 2B | | 50% | 50% | 50% | 50% | [[src-tt50-2026-nhnn#^pl2-b2-8]] |
| A.9 | Phải đòi Chính phủ, KBNN, UBND cấp tỉnh, BHTG, BHXH, PSE nước ngoài | | 50% | 50% | 65% | | [[src-tt50-2026-nhnn#^pl2-b2-9]] |
| A.10.1–10.2 | Phải đòi NHNN; NHTW nước ngoài hệ số rủi ro ≤ 35% | 0% | 0% | 50% | 65% | | [[src-tt50-2026-nhnn#^pl2-b2-9]] |
| A.10.3 | Phải đòi NHTW nước ngoài khác | 0% | 0% | 50% | 85% | | [[src-tt50-2026-nhnn#^pl2-b2-9]] |
| A.11.1 | Cổ phiếu niêm yết | | | | | 85% | [[src-tt50-2026-nhnn#^pl2-b2-9]] |
| A.11.2 | Trái phiếu niêm yết | | 50% | 50% | 85% | | [[src-tt50-2026-nhnn#^pl2-b2-9]] |
| A.11.3 | Chứng khoán khác | | 50% | 50% | 100% | 100% | [[src-tt50-2026-nhnn#^pl2-b2-9]] |
| A.12 | Hàng hoá giao dịch trên sàn, gồm vàng | | | | | 85% | [[src-tt50-2026-nhnn#^pl2-b2-9]] |
| A.13 | Tài sản cố định | | | | | 100% | [[src-tt50-2026-nhnn#^pl2-b2-9]] |
| A.14.1 | Cấp tín dụng tổ chức tài chính, bảo đảm HQLA cấp 1 tái thế chấp được | | 10% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-b2-14]] |
| A.14.2 | Cấp tín dụng khác cho tổ chức tài chính | | 15% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-b2-14]] |
| A.15.1 | Tiền gửi hoạt động tại TCTD khác | 50% | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-b2-14]] |
| A.15.2 | Tiền gửi tại TCTD, chi nhánh NHNNg, TCTD nước ngoài | 15% | 15% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-b2-14]] |
| A.15.3 | Tiền gửi khác | 50% | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-b2-14]] |
| A.16.1 | Phải đòi bất động sản không đủ tiêu chuẩn (TT14) | | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-b2-16]] |
| A.16.2.1 / A.17.1 | Thế chấp nhà ở, hệ số rủi ro ≤ 35% | | 50% | 50% | 65% | | [[src-tt50-2026-nhnn#^pl2-b2-16]] |
| A.16.2.2 / A.17.2 | Bất động sản khác, hệ số rủi ro > 35% | | 50% | 50% | 85% | | [[src-tt50-2026-nhnn#^pl2-b2-16]] |
| A.18.x.1 | Bán lẻ, DNNVV, DN, tổ chức khác: hệ số rủi ro ≤ 35% | | 50% | 50% | 65% | | [[src-tt50-2026-nhnn#^pl2-b2-16]] |
| A.18.x.2 | Như trên: hệ số rủi ro > 35% | | 50% | 50% | 85% | | [[src-tt50-2026-nhnn#^pl2-b2-16]] |
| A.19 | Tài sản khác xác định được kỳ hạn | | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-b2-19]] |
| A.20 | Tài sản khác không xác định được kỳ hạn | | | | | 100% | [[src-tt50-2026-nhnn#^pl2-b2-19]] |
| B.1 | 10% tổng nợ phái sinh, trước khi trừ ký quỹ biến động đã nộp | 100% | | | | | [[src-tt50-2026-nhnn#^pl2-b2-19]] |
| B.2 | Tài sản dự kiến nhận về tại ngày giao dịch | Như Mục A | | | | | [[src-tt50-2026-nhnn#^pl2-b2-19]] |
| B.3 | Khoản giảm trừ khỏi vốn tự có khác | 100% | | | | | [[src-tt50-2026-nhnn#^pl2-b2-19]] |
| C.1 | Hạn mức cam kết, nghĩa vụ giải ngân chưa sử dụng | 5% | | | | | [[src-tt50-2026-nhnn#^pl2-b2-19]] |
| C.2 | Nghĩa vụ nợ tiềm ẩn khác | 0% | | | | | [[src-tt50-2026-nhnn#^pl2-b2-19]] |

\* A.2: 85%, hoặc hệ số cao hơn nếu tài sản ký quỹ thuộc trường hợp có RSF trên 85% [[src-tt50-2026-nhnn#^pl2-b2-1]]. A.3: hệ số theo Đ24.4, chi tiết ở khoản A.3 dưới đây.

### Bước 3: giải trình từng đầu mục

**A.1, khoản phải đòi vỡ nợ.** 100% [[src-tt50-2026-nhnn#^pl2-b2-1]], xác định theo TT14/2025 cho mọi ngân hàng, kể cả ngân hàng đang áp dụng TT41/2016 [[src-tt50-2026-nhnn#^pl2-b1]]. Basel: nợ xấu 100% [[src-bcbs-nsfr#^nsf30-32]]. *Diễn giải:* khoản vỡ nợ không thu hồi được trong một năm và không dùng làm tài sản bảo đảm được, nên phải tài trợ toàn bộ bằng nguồn ổn định.

**A.2, ký quỹ ban đầu cho phái sinh.** 85% dưới 1 năm, 100% từ 1 năm và khi không xác định kỳ hạn; tài sản ký quỹ vốn có RSF trên 85% thì giữ hệ số cao hơn [[src-tt50-2026-nhnn#^pl2-b2-1]]. Basel: 85% [[src-bcbs-nsfr#^nsf30-31]]. *Diễn giải:* tài sản đã ký quỹ ban đầu bị khoá trong suốt thời gian giữ vị thế phái sinh. Chi tiết: [[rsf-derivatives-and-off-balance-sheet]].

**A.3, tài sản bị ràng buộc.** Ràng buộc còn từ 1 năm: 100%. Từ 6 tháng tới dưới 1 năm: 50% nếu tài sản khi không bị ràng buộc có RSF tới 50%, giữ hệ số cao hơn nếu trên 50%. Dưới 6 tháng: như khi không bị ràng buộc [[src-tt50-2026-nhnn#^d24-1]]. Tài sản mà khách hàng có quyền thay đổi thời gian ràng buộc cũng xếp vào A.3 [[src-tt50-2026-nhnn#^pl2-b2-1]]. Basel giống [[src-bcbs-nsfr#^nsf30-20]]. Chi tiết: [[rsf-securities-financing-and-encumbrance]], [[asset-encumbrance]].

**A.4, tài sản thuộc cặp phụ thuộc.** 0% ở mọi kỳ hạn, đi cặp với nợ tương ứng nhận ASF 0% [[src-tt50-2026-nhnn#^pl2-b2-1]] [[src-tt50-2026-nhnn#^d26-1]]. NHNN có quyền yêu cầu ngừng áp [[src-tt50-2026-nhnn#^d26-3]]. Xem [[interdependent-assets-and-liabilities]].

**A.5 và B.1, phái sinh.** Tài sản phái sinh NSFR ròng (phần vượt nợ phái sinh NSFR) nhận 100% [[src-tt50-2026-nhnn#^d25-5]]. Cộng thêm 10% tổng nợ phái sinh trước khi trừ ký quỹ biến động đã nộp, hệ số 100% [[src-tt50-2026-nhnn#^pl2-b2-19]]. Basel để quốc gia chọn trong 5%–20% [[src-bcbs-nsfr#^nsf30-32]]. *Diễn giải:* B.1 tính cả khi ngân hàng đang ở vị thế tài sản phái sinh ròng, để có nguồn ổn định cho biến động giá trị phái sinh trong tương lai.

**A.6 và B.2, giao dịch chờ quyết toán.** Khoản phải thu tại ngày giao dịch từ việc bán công cụ tài chính, ngoại tệ, hàng hoá nhận 0% [[src-tt50-2026-nhnn#^pl2-b2-1]]. Tài sản dự kiến nhận về từ việc mua nhận hệ số như tài sản đó trên bảng cân đối [[src-tt50-2026-nhnn#^pl2-b2-19]] [[src-tt50-2026-nhnn#^d24-6]]. *Diễn giải:* RSF đo theo ngày giao dịch, không theo ngày thanh toán. Mua trái phiếu doanh nghiệp hôm nay làm RSF tăng ngay, dù tiền chưa chuyển.

**A.7 và B.3, khoản giảm trừ khỏi vốn tự có.** 100% [[src-tt50-2026-nhnn#^pl2-b2-1]] [[src-tt50-2026-nhnn#^pl2-b2-19]]. *Diễn giải:* tài sản đã bị trừ khỏi vốn tự có được coi như không có giá trị thanh khoản, nên phải tài trợ hoàn toàn bằng nguồn ổn định. Danh mục cụ thể nằm ở các mục của Phụ lục I TT14/2025 và TT41/2016 [cần nguồn: TT14/2025 chưa register].

**A.8, HQLA không bị ràng buộc.** Tiền mặt, tiền gửi dự trữ bắt buộc kể cả phần vượt: 0%. HQLA do NHNN phát hành còn dưới 6 tháng (tín phiếu NHNN): 0%. HQLA cấp 1 khác: 5%; cấp 2A: 15%; cấp 2B: 50%, áp như nhau ở mọi cột kỳ hạn [[src-tt50-2026-nhnn#^pl2-b2-8]]. Basel: 0%, 5%, 15%, 50% [[src-bcbs-nsfr#^nsf30-25]] [[src-bcbs-nsfr#^nsf30-26]] [[src-bcbs-nsfr#^nsf30-28]] [[src-bcbs-nsfr#^nsf30-29]]. *Diễn giải:* trái phiếu Chính phủ nằm ở A.8.4 (5%), không ở A.9 (65%), vì A.8 đứng trước. Phân loại cấp 1, 2A, 2B lấy theo PL I của LCR ([[src-tt50-2026-nhnn#^pl1-a2]]), nên một tài sản bị loại khỏi HQLA thì RSF nhảy từ 5–15% lên 50–100%. Chi tiết: [[rsf-hqla-and-central-bank-reserves]].

**A.9–A.10, Chính phủ và NHTW (không phải HQLA).** Phải đòi Chính phủ, KBNN, UBND cấp tỉnh, BHTG, BHXH: 50% dưới 1 năm, 65% từ 1 năm, không phân biệt hệ số rủi ro. Phải đòi NHNN, NHTW nước ngoài có hệ số rủi ro tới 35%: 0% dưới 6 tháng, 50% từ 6 tháng, 65% từ 1 năm; NHTW nước ngoài khác 85% từ 1 năm [[src-tt50-2026-nhnn#^pl2-b2-9]]. *Diễn giải:* A.9 gồm các khoản cho vay, tạm ứng Chính phủ, KBNN không phải chứng khoán HQLA. Basel cho 65% chỉ khi hệ số rủi ro tới 35% [[src-bcbs-nsfr#^nsf30-30]].

**A.11–A.13, chứng khoán non-HQLA, hàng hoá, tài sản cố định.** Cổ phiếu niêm yết 85%; trái phiếu niêm yết 50% dưới 1 năm, 85% từ 1 năm; chứng khoán khác 100% từ 1 năm; hàng hoá trên sàn, gồm vàng, 85%; tài sản cố định 100% [[src-tt50-2026-nhnn#^pl2-b2-9]]. Basel: chứng khoán non-HQLA từ 1 năm và cổ phiếu niêm yết 85% [[src-bcbs-nsfr#^nsf30-31]]. *Diễn giải:* TT50 phân biệt chứng khoán niêm yết (85%) với chưa niêm yết (100%), vì chứng khoán chưa niêm yết khó bán hoặc khó dùng làm tài sản bảo đảm.

**A.14–A.15, tổ chức tài chính.** Cấp tín dụng cho tổ chức tài chính dưới 6 tháng: 10% nếu bảo đảm bằng HQLA cấp 1 và ngân hàng được tái thế chấp suốt thời hạn, 15% nếu không. Từ 6 tháng: 50%; từ 1 năm: 100%. Tiền gửi tại TCTD khác: 15% không kỳ hạn và dưới 6 tháng; tiền gửi hoạt động 50% [[src-tt50-2026-nhnn#^pl2-b2-14]]. Basel: 10%, 15%, 50%, 100% [[src-bcbs-nsfr#^nsf30-27]] [[src-bcbs-nsfr#^nsf30-28]] [[src-bcbs-nsfr#^nsf30-29]] [[src-bcbs-nsfr#^nsf30-32]]. *Diễn giải:* hệ số thấp cho liên ngân hàng ngắn hạn phản ánh việc ngân hàng có thể không tái tục khi cần tiền. Liên ngân hàng từ 1 năm nhận 100% để hạn chế tài trợ dài hạn đan chéo giữa các ngân hàng. Chi tiết: [[rsf-loans-and-credit-exposures]].

**A.16–A.17, bất động sản.** Ngân hàng áp TT14/2025 dùng khoản 16 (đủ, không đủ tiêu chuẩn); ngân hàng áp TT41/2016 dùng khoản 17 [[src-tt50-2026-nhnn#^pl2-b2-16]]. Thế chấp nhà ở hệ số rủi ro tới 35%: 65% từ 1 năm; bất động sản khác trên 35%: 85%; bất động sản không đủ tiêu chuẩn: 100% từ 1 năm. Dưới 1 năm đều 50% [[src-tt50-2026-nhnn#^pl2-b2-16]]. Basel: 65%, 85% [[src-bcbs-nsfr#^nsf30-30]] [[src-bcbs-nsfr#^nsf30-31]].

**A.18, cấp tín dụng cho khách hàng khác.** Bán lẻ, DNNVV đủ điều kiện, doanh nghiệp không phải tổ chức tài chính, tổ chức khác: 50% dưới 1 năm; từ 1 năm 65% nếu hệ số rủi ro tới 35%, 85% nếu trên 35% [[src-tt50-2026-nhnn#^pl2-b2-16]]. Hệ số rủi ro theo thông tư về tỷ lệ an toàn vốn ngân hàng đang áp dụng [[src-tt50-2026-nhnn#^pl2-b2-16]]. *Diễn giải:* hầu hết cho vay doanh nghiệp, tiêu dùng tại VN có hệ số rủi ro trên 35%, nên phần dư nợ từ 1 năm nhận 85%. Đây thường là cấu phần RSF lớn nhất. Kỳ hạn dùng để phân loại tính cả thời gian cơ cấu lại nợ tối đa theo pháp luật [[src-tt50-2026-nhnn#^d24-3c]].

**A.19–A.20, tài sản khác.** Có kỳ hạn: 50% dưới 1 năm, 100% từ 1 năm; không xác định kỳ hạn: 100% [[src-tt50-2026-nhnn#^pl2-b2-19]]. *Diễn giải:* khoản mục chưa phân loại được mặc định nhận hệ số cao nhất.

**C, cam kết ngoại bảng.** Hạn mức cam kết và nghĩa vụ giải ngân, thanh toán theo khoản 1, 2, 3.3 Mục V Phần B PL I: 5% phần chưa sử dụng; nghĩa vụ nợ tiềm ẩn khác (khoản 3.2): 0% [[src-tt50-2026-nhnn#^pl2-b2-19]]. Basel: 5% cho hạn mức không thể huỷ ngang hoặc huỷ ngang có điều kiện; nghĩa vụ khác theo quyết định quốc gia [[src-bcbs-nsfr#^nsf30-34]]. Xem [[committed-facilities]].

### Ví dụ minh hoạ
*Diễn giải:* số giả định, đơn vị tỷ đồng, cùng ngân hàng với ví dụ ASF trong [[available-stable-funding]] (tổng tài sản 1.000, ASF 725,5).

| Đầu mục | Khoản | Kỳ hạn | Số dư | Hệ số | RSF |
|---|---|---|---|---|---|
| Tiền mặt | A.8.1 | KKH | 10 | 0% | 0 |
| Tiền gửi dự trữ bắt buộc tại NHNN | A.8.2 | KKH | 30 | 0% | 0 |
| Tín phiếu NHNN | A.8.3 | < 6T | 20 | 0% | 0 |
| Trái phiếu Chính phủ (HQLA cấp 1) | A.8.4 | ≥ 1N | 120 | 5% | 6 |
| Trái phiếu HQLA cấp 2A | A.8.5 | ≥ 1N | 20 | 15% | 3 |
| Trái phiếu Chính phủ repo kỳ hạn 13 tháng | A.3 | ≥ 1N | 20 | 100% | 20 |
| Tiền gửi tại TCTD khác | A.15.2 | < 6T | 60 | 15% | 9 |
| Cho vay tổ chức tài chính không bảo đảm | A.14.2 | < 6T | 30 | 15% | 4,5 |
| Cho vay bán lẻ, doanh nghiệp | A.18 | < 1N | 250 | 50% | 125 |
| Thế chấp nhà ở, hệ số rủi ro ≤ 35% | A.16.2.1 | ≥ 1N | 150 | 65% | 97,5 |
| Cho vay doanh nghiệp, hệ số rủi ro > 35% | A.18.3.2 | ≥ 1N | 200 | 85% | 170 |
| Khoản phải đòi vỡ nợ | A.1 | — | 15 | 100% | 15 |
| Cổ phiếu niêm yết | A.11.1 | KXĐ | 10 | 85% | 8,5 |
| Tài sản cố định | A.13 | KXĐ | 25 | 100% | 25 |
| Tài sản khác | A.20 | KXĐ | 40 | 100% | 40 |
| **Tổng tài sản** | | | **1.000** | | **523,5** |
| Hạn mức cam kết chưa sử dụng | C.1 | — | 100 | 5% | 5 |
| 10% tổng nợ phái sinh (tổng nợ phái sinh 30) | B.1 | — | 3 | 100% | 3 |
| **RSF** | | | | | **531,5** |

NSFR = 725,5 / 531,5 = 136,5%, trên mức 100% [[src-tt50-2026-nhnn#^d22-2]]. Cho vay doanh nghiệp từ 1 năm (170) và cho vay dưới 1 năm (125) chiếm 56% RSF. Kéo dài 100 tỷ đồng cho vay doanh nghiệp từ dưới 1 năm lên từ 1 năm (hệ số rủi ro trên 35%) làm RSF tăng 35, từ 50% lên 85%. Đem thêm 100 tỷ đồng trái phiếu Chính phủ đi repo 13 tháng làm RSF tăng 95, từ 5% lên 100%.

---

## Basel vs VN

| Tham số / Khoản mục | Chuẩn mực Basel (BCBS) | Việt Nam ([[tt50-2026\|TT50/2026/TT-NHNN]]) | Căn cứ Điều khoản | Ghi chú & Lộ trình |
|---|---|---|---|---|
| Tiền mặt & Dự trữ NHTW | RSF 0% | Tiền mặt, tiền gửi dự trữ bắt buộc (cả phần vượt) tại NHNN: 0% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.25 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Trái phiếu Chính phủ Level 1 | RSF 5% | HQLA cấp 1 (trừ tiền mặt, DTBB, HQLA NHNN phát hành < 6 tháng): 5% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.26 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Cho vay thế chấp nhà ở RW $\le 35\%$ | RSF 65% | ≥ 1 năm: 65%; < 1 năm: 50% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.30 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Cho vay doanh nghiệp $\ge 1$Y | RSF 85% | RW > 35%: 85%; RW ≤ 35%: 65% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.31 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Tài sản cầm cố $\ge 1$Y | RSF 100% | Bị ràng buộc ≥ 1 năm: 100% [[src-tt50-2026-nhnn#^pl2-b2]] [[src-tt50-2026-nhnn#^d24-1]] | NSF30.32 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Add-on nợ phái sinh gộp | 5%–20% (National discretion) | 10% tổng nợ phái sinh (trước khi trừ ký quỹ biến động đã nộp), hệ số 100% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.32 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Hạn mức cam kết ngoại bảng | RSF 5% phần chưa rút | 5% phần hạn mức chưa sử dụng; nghĩa vụ nợ tiềm ẩn khác 0% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.34 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |

Khác biệt (TT50 PL2): khoản phải đòi Chính phủ, KBNN, UBND cấp tỉnh, BHTG, BHXH nhận RSF 50% dưới 1 năm và 65% từ 1 năm trở lên [[src-tt50-2026-nhnn#^pl2-b2]]; tiền gửi tại TCTD khác dưới 6 tháng nhận 15% [[src-tt50-2026-nhnn#^pl2-b2]]. Add-on nợ phái sinh được ấn định 10% tổng nợ phái sinh [[src-tt50-2026-nhnn#^pl2-b2]]. Kỳ hạn RSF tính tới thời điểm muộn nhất; khoản vay được cơ cấu lại thời hạn theo pháp luật tính cả thời gian cơ cấu lại tối đa [[src-tt50-2026-nhnn#^d24-3c]]. Tài sản đã đặt lệnh mua chưa quyết toán vẫn vào RSF [[src-tt50-2026-nhnn#^d24-6]]. Khoản giảm trừ khỏi vốn tự có nhận 100% [[src-tt50-2026-nhnn#^pl2-b2-1]]. Chi tiết theo nhóm: [[rsf-hqla-and-central-bank-reserves]], [[rsf-loans-and-credit-exposures]], [[rsf-securities-financing-and-encumbrance]], [[rsf-derivatives-and-off-balance-sheet]].

---

## Ứng dụng trong ALM

1. **Cơ sở Tính toán Phí Điều chuyển Vốn Nội bộ (Term Liquidity FTP)**:
   - RSF là biến số trực tiếp nhân với Term Funding Spread để xác định mức phí tài trợ cấu trúc:
     $$\text{FTP Charge}(\text{Asset}) = \text{Base Cost} + \Big(\text{RSF Factor} \times \text{Term Funding Spread}(\text{Tenor})\Big)$$
   - Khoản vay doanh nghiệp dài hạn (RSF 85%) sẽ phải trả phí thanh khoản cao hơn 70% so với khoản đầu tư vào Level 2A (RSF 15%).
2. **Quản trị Tài sản Thế chấp và Cầm cố (Collateral Optimization)**:
   - Treasury tuyệt đối tránh cầm cố trái phiếu chính phủ Level 1 với kỳ hạn $\ge 1$ năm, vì hành vi này sẽ kích hoạt hệ số RSF vọt từ 5% lên 100%, gây tiêu hao 95% vốn ổn định của danh mục [[src-bcbs-nsfr#^nsf30-20]] [[src-bcbs-nsfr#^nsf30-26]].
3. **Cân đối Danh mục Tín dụng và NIM**:
   - Khi tăng trưởng tín dụng trung dài hạn, mẫu số RSF mở rộng liên tục, buộc Treasury phải phát hành trái phiếu dài hạn (ASF 100%) có chi phí cao, làm co hẹp biên lãi thuần [[net-interest-margin|NIM]] nếu không điều phối nhịp nhàng với [[alco|ALCO]].

---

## Nhầm lẫn thường gặp

1. **Nhầm lẫn giữa RSF 5% của HQLA Level 1 và Haircut 0% của LCR**: Trong LCR, tài sản Level 1 được tính 100% giá trị (haircut 0%). Nhưng trong NSFR, tài sản Level 1 vẫn phải chịu RSF 5% để dự phòng chi phí vận hành và rủi ro thanh khoản tiềm tàng.
2. **Bỏ qua Ràng buộc Encumbrance**: Nhiều ngân hàng phân loại trái phiếu chính phủ đem đi repo kỳ hạn 1 năm vào nhóm RSF 5%. Quy định Basel ấn định: bất kỳ tài sản nào cầm cố $\ge 1$ năm đều phải chịu RSF 100% [[src-bcbs-nsfr#^nsf30-20]].
3. **Đếm trùng hoặc Bỏ quên Cam kết Ngoại bảng**: Phần hạn mức cam kết tín dụng chưa rút phải chịu RSF 5%, nếu ngân hàng cấp hạn mức ảo quá lớn cho khách hàng mà không giải ngân, mẫu số RSF vẫn bị phình to làm giảm tỷ lệ NSFR [[src-bcbs-nsfr#^nsf30-34]].

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
