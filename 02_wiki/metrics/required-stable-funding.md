---
title: "Required Stable Funding (RSF)"
aliases: [RSF, Nguồn vốn ổn định cần thiết, Required Stable Funding]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: canonical
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "-", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
tags: [liquidity, nsfr, assets, funding-requirement]
updated: 2026-10-16
reviewed:
---

## Định nghĩa chuẩn mực

**Required Stable Funding (RSF)** là mẫu số của tỷ lệ [[nsfr]], đại diện cho tổng lượng vốn ổn định tối thiểu mà ngân hàng bắt buộc phải duy trì để tài trợ cho danh mục tài sản nội bảng và các cam kết cấp vốn ngoại bảng trong khoảng thời gian một năm [[src-bcbs-nsfr#^nsf20-2]] [[src-bcbs-nsfr#^nsf30-3]].

Hệ số RSF áp dụng cho từng loại tài sản được hiệu chỉnh dựa trên 4 đặc tính rủi ro thanh khoản cốt lõi [[src-bcbs-nsfr#^nsf30-3]] [[src-bcbs-nsfr#^nsf30-15]]:
1. **Mức độ thanh khoản của tài sản (Asset Liquidity Profile)**: Khả năng chuyển hóa thành tiền mặt thông qua bán đứt hoặc thế chấp vay repo trên thị trường mà không bị chiết khấu giá trị nghiêm trọng.
2. **Kỳ hạn hợp đồng còn lại (Residual Maturity)**: Tài sản có kỳ hạn dài hơn đòi hỏi nguồn tài trợ ổn định dài hơn.
3. **Chất lượng tín dụng (Credit Quality)**: Tài sản có trọng số rủi ro tín dụng (Risk Weight theo chuẩn CRE20) thấp hơn đòi hỏi ít vốn ổn định hơn.
4. **Mức độ cầm cố (Encumbrance Status)**: Tài sản bị cầm cố trong thời gian dài không thể dùng để tạo thanh khoản và phải chịu hệ số RSF tối đa 100%.

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

## Basel vs VN

| Tham số / Khoản mục | Chuẩn mực Basel (BCBS) | Việt Nam (TT50/2026/TT-NHNN) | Căn cứ Điều khoản | Ghi chú & Lộ trình |
|---|---|---|---|---|
| Tiền mặt & Dự trữ NHTW | RSF 0% | *[Chờ đối chiếu TT50]* | NSF30.25 / TT50 PL1 | Bắt buộc từ 01/10/2028 |
| Trái phiếu Chính phủ Level 1 | RSF 5% | *[Chờ đối chiếu TT50]* | NSF30.26 / TT50 PL1 | Bắt buộc từ 01/10/2028 |
| Cho vay thế chấp nhà ở RW $\le 35\%$ | RSF 65% | *[Chờ đối chiếu TT50]* | NSF30.30 / TT50 PL1 | Bắt buộc từ 01/10/2028 |
| Cho vay doanh nghiệp $\ge 1$Y | RSF 85% | *[Chờ đối chiếu TT50]* | NSF30.31 / TT50 PL1 | Bắt buộc từ 01/10/2028 |
| Tài sản cầm cố $\ge 1$Y | RSF 100% | *[Chờ đối chiếu TT50]* | NSF30.32 / TT50 PL1 | Bắt buộc từ 01/10/2028 |
| Add-on nợ phái sinh gộp | 5%–20% (National discretion) | *[Chờ đối chiếu TT50]* | NSF30.32 / TT50 PL1 | Bắt buộc từ 01/10/2028 |
| Hạn mức cam kết ngoại bảng | RSF 5% phần chưa rút | *[Chờ đối chiếu TT50]* | NSF30.34 / TT50 PL1 | Bắt buộc từ 01/10/2028 |

---

## Ứng dụng trong ALM

1. **Cơ sở Tính toán Phí Điều chuyển Vốn Nội bộ (Term Liquidity FTP)**:
   - RSF là biến số trực tiếp nhân với Term Funding Spread để xác định mức phí tài trợ cấu trúc:
     $$\text{FTP Charge}(\text{Asset}) = \text{Base Cost} + \Big(\text{RSF Factor} \times \text{Term Funding Spread}(\text{Tenor})\Big)$$
   - Khoản vay doanh nghiệp dài hạn (RSF 85%) sẽ phải trả phí thanh khoản cao hơn 70% so với khoản đầu tư vào Level 2A (RSF 15%).
2. **Quản trị Tài sản Thế chấp và Cầm cố (Collateral Optimization)**:
   - Treasury tuyệt đối tránh cầm cố trái phiếu chính phủ Level 1 với kỳ hạn $\ge 1$ năm, vì hành vi này sẽ kích hoạt hệ số RSF vọt từ 5% lên 100%, gây tiêu hao 95% vốn ổn định của danh mục [[src-bcbs-nsfr#^nsf30-20]] [[src-bcbs-nsfr#^nsf30-26]].
3. **Cân đối Danh mục Tín dụng và NIM**:
   - Khi tăng trưởng tín dụng trung dài hạn, mẫu số RSF mở rộng liên tục, buộc Treasury phải phát hành trái phiếu dài hạn (ASF 100%) có chi phí cao, làm co hẹp biên lãi thuần NIM nếu không điều phối nhịp nhàng với ALCO.

---

## Nhầm lẫn thường gặp

1. **Nhầm lẫn giữa RSF 5% của HQLA Level 1 và Haircut 0% của LCR**: Trong LCR, tài sản Level 1 được tính 100% giá trị (haircut 0%). Nhưng trong NSFR, tài sản Level 1 vẫn phải chịu RSF 5% để dự phòng chi phí vận hành và rủi ro thanh khoản tiềm tàng.
2. **Bỏ qua Ràng buộc Encumbrance**: Nhiều ngân hàng phân loại trái phiếu chính phủ đem đi repo kỳ hạn 1 năm vào nhóm RSF 5%. Quy định Basel ấn định: bất kỳ tài sản nào cầm cố $\ge 1$ năm đều phải chịu RSF 100% [[src-bcbs-nsfr#^nsf30-20]].
3. **Đếm trùng hoặc Bỏ quên Cam kết Ngoại bảng**: Phần hạn mức cam kết tín dụng chưa rút phải chịu RSF 5%, nếu ngân hàng cấp hạn mức ảo quá lớn cho khách hàng mà không giải ngân, mẫu số RSF vẫn bị phình to làm giảm tỷ lệ NSFR [[src-bcbs-nsfr#^nsf30-34]].

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO.
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[asset-encumbrance]]; đề xuất link ở lần nhắc đầu encumbrance.
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM.
