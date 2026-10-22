---
title: "Net Stable Funding Ratio (NSFR)"
aliases: [NSFR, Tỷ lệ nguồn vốn ổn định ròng, Net Stable Funding Ratio]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: measures, to: "[[available-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: measures, to: "[[required-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: limits, to: "[[available-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: limits, to: "[[balance-sheet-optimisation-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u04-12]]"}
  - {type: drives, to: "[[net-interest-margin]]", direction: "-", cite: "[[src-lubinska-alm-optimisation#^lubinska-u02-18]]"}
tags: [liquidity, structural-funding, long-term, basel]
updated: 2026-10-22
reviewed:
---

## Định nghĩa
NSFR đo lường mức độ lành mạnh và an toàn của cơ cấu tài trợ trong khoảng thời gian một năm [[src-bcbs-nsfr#^nsf20-2]]. Tỷ lệ này yêu cầu ngân hàng phải duy trì nguồn vốn ổn định tương ứng với mức độ kém thanh khoản của tài sản và các cam kết tài trợ ngoại bảng, nhằm hạn chế sự phụ thuộc quá mức vào nguồn vốn bán buôn ngắn hạn và giảm thiểu nguy cơ đổ vỡ có tính hệ thống [[src-bcbs-nsfr#^nsf20-1]].

## Công thức

$$
\text{NSFR} = \frac{\text{Available Stable Funding (ASF)}}{\text{Required Stable Funding (RSF)}} \geq 100\%
$$

Trong đó:
- **Tử số — [[available-stable-funding|Available Stable Funding (ASF)]]**: Tổng giá trị ghi sổ của vốn tự có và nợ phải trả nhân hệ số ổn định tương ứng ($\text{ASF}\% \in \{100\%, 95\%, 90\%, 50\%, 0\%\}$) [[src-bcbs-nsfr#^nsf30-6]] [[src-bcbs-nsfr#^nsf99-1]]:
  - [[asf-capital-and-long-term-liabilities]]: Vốn tự có và nợ dài hạn $\ge 1$ năm (ASF 100%) [[src-bcbs-nsfr#^nsf30-10]].
  - [[asf-retail-and-small-business-deposits]]: Tiền gửi bán lẻ và SME (ASF 90%–95%) [[src-bcbs-nsfr#^nsf30-11]] [[src-bcbs-nsfr#^nsf30-12]].
  - [[asf-wholesale-and-operational-funding]]: Nguồn vốn doanh nghiệp phi tài chính và operational deposits (ASF 50%), nguồn vốn liên ngân hàng $< 6$M (ASF 0%) [[src-bcbs-nsfr#^nsf30-13]] [[src-bcbs-nsfr#^nsf30-14]].
  $$\text{ASF} = \sum_{i} \text{Carrying Value}_i \times \text{ASF Factor}_i$$
- **Mẫu số — [[required-stable-funding|Required Stable Funding (RSF)]]**: Tổng giá trị ghi sổ của tài sản nội bảng và cam kết ngoại bảng nhân hệ số yêu cầu ($\text{RSF}\% \in \{0\%, 5\%, 10\%, 15\%, 50\%, 65\%, 85\%, 100\%\}$) [[src-bcbs-nsfr#^nsf30-15]] [[src-bcbs-nsfr#^nsf99-2]]:
  - [[rsf-hqla-and-central-bank-reserves]]: Tiền mặt/dự trữ (RSF 0%), Level 1 (RSF 5%), Level 2A (RSF 15%), Level 2B (RSF 50%) [[src-bcbs-nsfr#^nsf30-25]] [[src-bcbs-nsfr#^nsf30-26]] [[src-bcbs-nsfr#^nsf30-28]] [[src-bcbs-nsfr#^nsf30-29]].
  - [[rsf-loans-and-credit-exposures]]: Cho vay thế chấp nhà ở (RSF 65%), cho vay thông thường (RSF 85%), cho vay $< 1$ năm (RSF 50%), NPLs (RSF 100%) [[src-bcbs-nsfr#^nsf30-29]] [[src-bcbs-nsfr#^nsf30-30]] [[src-bcbs-nsfr#^nsf30-31]] [[src-bcbs-nsfr#^nsf30-32]].
  - [[rsf-securities-financing-and-encumbrance]]: Cho vay có bảo đảm repo (RSF 10%–15%), khung thời gian cầm cố tài sản $\ge 1$Y (RSF 100%) [[src-bcbs-nsfr#^nsf30-20]] [[src-bcbs-nsfr#^nsf30-27]].
  - [[rsf-derivatives-and-off-balance-sheet]]: Ký quỹ phái sinh ban đầu (RSF 85%), tài sản phái sinh ròng (RSF 100%), add-on nợ phái sinh gộp (RSF 100%), cam kết ngoại bảng (RSF 5%) [[src-bcbs-nsfr#^nsf30-31]] [[src-bcbs-nsfr#^nsf30-32]] [[src-bcbs-nsfr#^nsf30-34]].
  $$\text{RSF} = \sum_{j} \text{Asset Carrying Value}_j \times \text{RSF Factor}_j + \sum_{k} \text{OBS Exposure}_k \times \text{RSF Factor}_k$$

## Diễn giải
- **Horizon thời gian 1 năm**: Khác với [[lcr]] tập trung vào kịch bản căng thẳng thanh khoản cấp tính 30 ngày (*acute stress survival horizon*), NSFR thiết lập một cấu trúc tài trợ bền vững kéo dài 1 năm (*structural funding profile*) trong điều kiện bình thường và căng thẳng kéo dài [[src-bcbs-nsfr#^nsf20-2]].
- **Ngưỡng tuân thủ liên tục**: Tỷ lệ NSFR nên đạt tối thiểu $100\%$ trên cơ sở liên tục (*on an ongoing basis*) [[src-bcbs-nsfr#^nsf20-2]].
- **Tần suất báo cáo**: Ngân hàng phải báo cáo chỉ số NSFR tối thiểu hàng quý cho cơ quan quản lý [[src-bcbs-nsfr#^nsf20-3]].
- **Giả định hành vi thận trọng**:
  - Đối với nợ phải trả: Giả định nhà đầu tư sẽ thực hiện quyền chọn mua lại (*call options*) ở ngày sớm nhất có thể [[src-bcbs-nsfr#^nsf30-7]].
  - Đối với tài sản: Giả định khách hàng sẽ thực hiện quyền chọn gia hạn kỳ hạn hợp đồng [[src-bcbs-nsfr#^nsf30-17]].
  - Tái cấp tín dụng: Basel giả định ngân hàng buộc phải tái cấp một tỷ lệ đáng kể các khoản cho vay đến hạn để bảo vệ thương quyền và quan hệ khách hàng [[src-bcbs-nsfr#^nsf30-3]].
- **Tài sản bị cầm cố (*Encumbered Assets*)**: Mức độ cầm cố quyết định trực tiếp hệ số RSF. Tài sản cầm cố $\ge 1$ năm chịu RSF $100\%$; HQLA cầm cố từ 6 tháng đến dưới 1 năm chịu RSF $50\%$ [[src-bcbs-nsfr#^nsf30-20]].
- **Ngoại lệ tài sản và nợ phụ thuộc nhau**: Trường hợp đặc biệt khi tài sản và nợ gắn kết theo hợp đồng không thể tách rời (như dự án pass-through), giám sát viên có thể cho phép áp dụng đồng thời $\text{ASF} = 0\%$ và $\text{RSF} = 0\%$ theo [[interdependent-assets-and-liabilities]] [[src-bcbs-nsfr#^nsf30-35]].

## Basel vs VN

| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Ngưỡng tối thiểu | $\ge 100\%$ liên tục [[src-bcbs-nsfr#^nsf20-2]] | NSFR riêng lẻ 90% (01/10/2028), 95% (01/10/2029), 100% từ 01/10/2030 [[src-tt50-2026-nhnn#^d22-2]] | NSF20.2 / TT50 Đ22.2 | Basel: 01/01/2018; VN: theo lộ trình |
| Horizon đánh giá | 1 năm [[src-bcbs-nsfr#^nsf20-2]] | [cần nguồn] | NSF20.2 / TT50 Đ13 | |
| Tần suất báo cáo | Tối thiểu hàng quý [[src-bcbs-nsfr#^nsf20-3]] | [cần nguồn] | NSF20.3 | |
| Phạm vi áp dụng | Hợp nhất (consolidated) [[src-bcbs-nsfr#^nsf10-4]] | Riêng lẻ phải báo cáo; hợp nhất theo quy định nội bộ [[src-tt50-2026-nhnn#^d22-3]] | NSF10.4 / TT50 Đ22.3–4 | |
| Nợ liên ngân hàng $< 6$ tháng | ASF 0% [[src-bcbs-nsfr#^nsf30-14]] | TCTD, chi nhánh NHNNg: ASF 0% [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.14 | |
| Tiền gửi bán lẻ stable | ASF 95% [[src-bcbs-nsfr#^nsf30-11]] | ASF 95%; có kỳ hạn ≥ 1 năm không được rút trước hạn: 100% [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.11 | |
| Tiền gửi bán lẻ less stable | ASF 90% [[src-bcbs-nsfr#^nsf30-12]] | ASF 90%; có kỳ hạn ≥ 1 năm không được rút trước hạn: 100% [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.12 | |
| Tiền gửi DN phi tài chính $< 1$ năm | ASF 50% [[src-bcbs-nsfr#^nsf30-13]] | ASF 50% [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.13 | |
| Tài sản Level 1 unencumbered | RSF 5% [[src-bcbs-nsfr#^nsf30-26]] | RSF 5% (tiền mặt, DTBB tại NHNN: 0%) [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.26 | |
| Tài sản Level 2A unencumbered | RSF 15% [[src-bcbs-nsfr#^nsf30-28]] | RSF 15% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.28 | |
| Tài sản Level 2B unencumbered | RSF 50% [[src-bcbs-nsfr#^nsf30-29]] | RSF 50% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.29 | |
| Vay nhà ở unencumbered $\ge 1$ năm (RW $\le 35\%$) | RSF 65% [[src-bcbs-nsfr#^nsf30-30]] | RSF 65% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.30 | |
| Cho vay unencumbered $\ge 1$ năm (RW $> 35\%$) | RSF 85% [[src-bcbs-nsfr#^nsf30-31]] | RSF 85% [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.31 | |
| Cam kết tín dụng/thanh khoản ngoại bảng | RSF 5% phần chưa rút [[src-bcbs-nsfr#^nsf30-34]] | RSF 5% phần chưa sử dụng [[src-tt50-2026-nhnn#^pl2-b2]] | NSF30.34 | |

*Ghi chú:* NSFR = ASF / RSF × 100% theo Đ22.1 [[src-tt50-2026-nhnn#^d22-1]]; ngân hàng áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]]. Hệ số ASF/RSF theo khoản mục lấy từ TT50 Phụ lục II. Khoản phải đòi repo tính vào RSF, khoản phải trả repo tính vào ASF, tách biệt [[src-tt50-2026-nhnn#^d22-5]]. Xem [[tt50-2026]].

## Ứng dụng trong ALM
*Diễn giải:*
Trong thực tiễn điều hành tại ALCO ([[alco]]) và ALM Treasury, NSFR tạo thành khuôn khổ định hình cấu trúc bảng cân đối kế toán dài hạn:
- **Cặp bài trùng với LCR (Tối ưu hóa đa mục tiêu)**:
  - Nếu Treasury nắm giữ danh mục [[hqla]] bằng trái phiếu chính phủ Level 1, tài sản này vừa giúp tối ưu hóa tử số của [[lcr]] (nhận giá trị 100% không bị chiết khấu), vừa chỉ đòi hỏi mức vốn ổn định tối thiểu trong NSFR ($\text{RSF} = 5\%$) [[src-bcbs-nsfr#^nsf30-26]].
  - Ngược lại, nếu ngân hàng tài trợ danh mục HQLA bằng nguồn vốn liên ngân hàng ngắn hạn ($< 30$ ngày), LCR bị triệt tiêu vì dòng tiền ra tăng tương ứng, đồng thời nguồn vốn này nhận $\text{ASF} = 0\%$ trong NSFR, khiến NSFR sụt giảm mạnh [[src-bcbs-nsfr#^nsf30-14]].
- **Định giá chuyển nhượng vốn nội bộ (Term Liquidity FTP)**:
  - NSFR buộc ALM Treasury phải áp phí thanh khoản kỳ hạn (*Term Liquidity Premium*) đối với các khoản tín dụng trung dài hạn ($\ge 1$ năm), vì các khoản vay này đòi hỏi từ 65% đến 85% nguồn vốn ổn định có chi phí cao.
  - Đồng thời, Treasury thực hiện trả thưởng thanh khoản (*Stable Funding Incentive*) cho các đơn vị kinh doanh huy động được tiền gửi bán lẻ cốt lõi ($\text{ASF} = 90\%\text{–}95\%$) hoặc phát hành nợ dài hạn ($\text{ASF} = 100\%$).
- **Chiến lược quản trị cấu trúc kỳ hạn (Tenor Structuring)**:
  - Ngân hàng phải chủ động kiểm soát "vực thẳm kỳ hạn" (*cliff-edge maturity*): Khi một khoản nợ bán buôn lớn trôi từ kỳ hạn trên 1 năm xuống dưới 1 năm, hệ số ASF giảm đột ngột từ $100\%$ xuống $50\%$ (hoặc từ $50\%$ xuống $0\%$ khi kỳ hạn còn lại dưới 6 tháng), tạo ra áp lực sụt giảm NSFR tức thì [[src-bcbs-nsfr#^nsf30-10]] [[src-bcbs-nsfr#^nsf30-13]] [[src-bcbs-nsfr#^nsf30-14]].
- **Thang kỳ hạn hợp đồng**: xem [[contractual-maturity-mismatch]].
- **Rủi ro thanh khoản cấu trúc**: xem [[structural-liquidity-risk]].

## Nhầm lẫn thường gặp
- **NSFR không phải là "tỷ lệ cấp tín dụng trên huy động (LDR)"**: [[loan-to-deposit-ratio|LDR]] là tỷ lệ thô giữa tổng dư nợ cho vay trên tổng tiền gửi. NSFR là mô hình phân rã đa chiều gán trọng số hành vi và tính thanh khoản cho mọi tài sản, nợ và ngoại bảng.
- **Nguồn vốn liên ngân hàng không được coi là nguồn vốn ổn định**: Nguồn vốn vay mượn từ các định chế tài chính và NHTW có kỳ hạn dưới 6 tháng bị ấn định $\text{ASF} = 0\%$, bất kể ngân hàng có uy tín tín dụng cao đến đâu [[src-bcbs-nsfr#^nsf30-14]].
- **Tài sản ngắn hạn vẫn đòi hỏi nguồn vốn ổn định**: Một khoản cho vay doanh nghiệp có kỳ hạn dưới 1 năm vẫn phải chịu $\text{RSF} = 50\%$ do giả định hành vi ngân hàng phải tái cấp vốn (*roll-over*) để giữ chân khách hàng [[src-bcbs-nsfr#^nsf30-3]] [[src-bcbs-nsfr#^nsf30-29]].
