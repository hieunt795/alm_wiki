---
title: "Loan-to-Deposit Ratio"
aliases: [Loan-to-Deposit Ratio, Loan-deposit ratio, LDR, LTD ratio, Tỷ lệ dư nợ cho vay so với tổng tiền gửi, Customer funding gap]
type: metric
domains: [alm, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: input-to, to: "[[bank-strategic-plan]]", cite: "[[src-choudhry-principles-banking#^choudhry-strat-28]]"}
tags: [liquidity, funding, kpi, strategy]
updated: 2026-10-21
reviewed:
---

## Định nghĩa
Loan-to-deposit ratio (LDR) so cho vay khách hàng với tiền gửi khách hàng. Choudhry đo customer funding gap bằng cho vay khách hàng trừ tiền gửi khách hàng, và gọi tỷ lệ tương ứng là "loan to deposit" (LTD) ratio [[src-choudhry-principles-banking#^choudhry-strat-25]]. Loan-deposit ratio là một KPI trong Table 15.1, bộ KPI mà strategic plan và budget nên có [[src-choudhry-principles-banking#^choudhry-strat-28]].

## Công thức
### Theo TT50/2026 (VN)

$$\text{LDR} = \frac{L}{D} \times 100\%$$
[[src-tt50-2026-nhnn#^d12-1]]

LDR tính theo VNĐ, gồm VNĐ và ngoại tệ quy đổi [[src-tt50-2026-nhnn#^d12-1]]. Ngoại tệ quy đổi theo tỷ giá hạch toán nếu ngày tính không phải ngày làm việc cuối tháng, quý, năm. Ngày làm việc cuối kỳ dùng tỷ giá lập Bảng cân đối tài khoản kế toán (ngân hàng hạch toán bằng VNĐ) hoặc tỷ giá chuyển đổi báo cáo tài chính (ngân hàng hạch toán bằng ngoại tệ). Ngày chốt số liệu không phải ngày làm việc thì dùng tỷ giá ngày làm việc liền trước [[src-tt50-2026-nhnn#^d3-14]].

**L, tử số (Đ12.2–3)**: xem [[ldr-total-loans]]. L cộng dư nợ gốc nội bảng từ cho vay cá nhân, tổ chức và uỷ thác cho TCTD khác cho vay [[src-tt50-2026-nhnn#^d12-2]]; trừ cho vay TCTD tại VN và vay tái cấp vốn NHNN không nhằm hỗ trợ thanh khoản [[src-tt50-2026-nhnn#^d12-1]]. Bảng phân loại nghiệp vụ tín dụng (cho vay vào L, cấp tín dụng khác trừ khỏi D) nằm ở node này.

**D, mẫu số (Đ12.4–5)**: xem [[ldr-total-deposits]], gồm giải trình từng đầu mục và ví dụ số.

| Chiều | Nhóm đầu mục | Căn cứ |
|---|---|---|
| + | Tiền gửi tổ chức và cá nhân, trừ tiền gửi TCTD, ký quỹ, vốn chuyên dùng, KBNN không kỳ hạn và 80% KBNN có kỳ hạn | [[src-tt50-2026-nhnn#^d12-4a]] [[src-tt50-2026-nhnn#^d12-4]] |
| + | Trái phiếu Vốn cấp 2 phát hành trong nước, vốn uỷ thác chịu rủi ro, chênh lệch dương liên ngân hàng, vay nước ngoài | [[src-tt50-2026-nhnn#^d12-4]] [[src-tt50-2026-nhnn#^d12-4d]] |
| + | Vốn chủ sở hữu ròng, lợi nhuận chưa phân phối điều chỉnh lãi dự thu, dự trả, chênh lệch tỷ giá vốn | [[src-tt50-2026-nhnn#^d12-4d]] |
| − | Cấp tín dụng khác không phải cho vay, đầu tư trái phiếu doanh nghiệp, uỷ thác cấp tín dụng khác | [[src-tt50-2026-nhnn#^d12-5]] [[src-tt50-2026-nhnn#^d12-4]] |

*Diễn giải:* D của TT50 không phải "tiền gửi khách hàng" theo nghĩa của Choudhry. D gồm cả nguồn vốn dài hạn (trái phiếu Vốn cấp 2, vay nước ngoài, vốn chủ sở hữu ròng) và phần nhận ròng liên ngân hàng. D trừ đi các khoản sử dụng vốn có tính chất tín dụng ngoài cho vay. L thì loại cho vay liên ngân hàng. Vì vậy LDR của TT50 không so được trực tiếp với customer LDR trong báo cáo quốc tế. Biểu `04_models/lcr-tt50-2026.xlsx` chưa có sheet LDR.

### Theo Choudhry
*Diễn giải (tái dựng, chưa đối chiếu bản gốc):* nguồn chỉ nêu funding gap bằng lời và không ghi công thức tỷ lệ. Dạng thông dụng:

$$LDR = \frac{\text{Customer loans}}{\text{Customer deposits}}$$
[[src-choudhry-principles-banking#^choudhry-strat-25]]

$$\text{Funding gap} = \text{Customer loans} - \text{Customer deposits}$$
[[src-choudhry-principles-banking#^choudhry-strat-25]]

LDR trên 100% tương đương funding gap dương, tức phần cho vay vượt tiền gửi phải tài trợ bằng nguồn khác.

## Diễn giải
| Ví dụ trong nguồn | Giá trị | Nguồn |
|---|---|---|
| Corporate banking của Europe Arab Bank, 2008 | LDR gần 180% | [[src-choudhry-principles-banking#^choudhry-cs-3]] |
| Private Banking của Europe Arab Bank | LDR khoảng 60% | [[src-choudhry-principles-banking#^choudhry-cs-3]] |
| Tập đoàn ngân hàng thương mại châu Âu (case study 6) | LDR dưới 100% | [[src-choudhry-principles-banking#^choudhry-cs-19]] |
| Mục tiêu ví dụ trong liquidity strategy | LDR 95% | [[src-choudhry-principles-banking#^choudhry-liq-15]] |
| Bốn ngân hàng lớn UK, 1997–2009 (Figure 15.4, dữ liệu ECB) | Funding gap gộp tăng, LTD xấu đi đồng loạt | [[src-choudhry-principles-banking#^choudhry-strat-25]] |

Choudhry dùng Figure 15.4 làm ví dụ cho "herd mentality": các ngân hàng cùng đi một hướng khi một trào lưu bị nhầm là best practice [[src-choudhry-principles-banking#^choudhry-strat-25]]. Phụ thuộc quá mức vào wholesale funding nằm trong danh sách dấu hiệu cảnh báo của strategic plan [[src-choudhry-principles-banking#^choudhry-strat-26]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Tên và vai trò | Không có chỉ tiêu LDR trong chuẩn BCBS đã ingest [cần nguồn] | "Tỷ lệ dư nợ cho vay so với tổng tiền gửi"; ngân hàng đặt hạn mức bảo đảm tuân thủ tỷ lệ này [[src-tt83-2025-nhnn#^d45-3]] | TT83 Đ45.3 | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Công thức VN | — | LDR = L / D × 100%, theo VNĐ gồm ngoại tệ quy đổi [[src-tt50-2026-nhnn#^d12-1]]; cấu phần L và D xem mục Công thức [[src-tt50-2026-nhnn#^d12-2]] [[src-tt50-2026-nhnn#^d12-5]] | TT50 Đ12.1–5, Đ3.14 | |
| Ngưỡng tối đa | — | 95% [[src-tt50-2026-nhnn#^d12-6]] | TT50 Đ12.6 | Từ khi áp dụng LCR/NSFR (Đ13.5) [[src-tt50-2026-nhnn#^d12-6]] |
| Báo cáo | — | Từ khi bắt đầu áp dụng LDR, báo cáo NHNN theo chế độ báo cáo thống kê [[src-tt50-2026-nhnn#^d12-8]] | TT50 Đ12.8 | Từ khi áp dụng LCR/NSFR [[src-tt50-2026-nhnn#^d13-5]] |
| Công bố thông tin | — | LDR thuộc nội dung định lượng phải công bố, cùng LCR, NSFR riêng lẻ [[src-tt50-2026-nhnn#^pl4-3]] | TT50 PL4.3 | |
| Chuyển tiếp | — | Trước khi áp dụng LCR/NSFR: tuân thủ LDR theo TT22/2019 [[src-tt50-2026-nhnn#^d13-4]]. Sau đó: tuân thủ LDR theo Đ12 TT50; áp dụng ngưỡng 100% cho cả LCR và NSFR thì LDR chỉ phải báo cáo [[src-tt50-2026-nhnn#^d13-5]]. NHTM đang thực hiện Đ23.3 TT41/2016 không phải tuân thủ Mục 4 (LDR) TT50 cho đến khi kết thúc việc thực hiện đó [[src-tt50-2026-nhnn#^d37-1]] | TT50 Đ13.4–5, Đ37.2 | 01/10/2026 [[src-tt50-2026-nhnn#^d37-1]] |

*Diễn giải:* Basel III đo funding ổn định bằng [[nsfr]], có trọng số theo hành vi và kỳ hạn. LDR là tỷ lệ thô, không phân biệt tiền gửi bán lẻ ổn định với tiền gửi wholesale.

## Ứng dụng trong ALM
- Strategic plan nên đặt mục tiêu dài hạn cho một số KPI trong Table 15.1, trong đó có loan-deposit ratio và wholesale funding ratio, cho toàn ngân hàng và từng mảng Treasury, Corporate Banking, Retail Banking [[src-choudhry-principles-banking#^choudhry-strat-28]]. Xem [[bank-strategic-plan]].
- Fitch dùng customer loans/customer deposits làm một trong 5 tỷ lệ funding cấu trúc để so sánh ngân hàng [[src-choudhry-principles-banking#^choudhry-peer-6]].
- Northern Rock tăng cho vay vượt nền tiền gửi và tài trợ phần dư bằng wholesale và securitisation [[src-choudhry-principles-banking#^choudhry-gov-8]]. Xem [[bank-corporate-governance]].
- Cho vay ở nước ngoài không có nền tiền gửi khách hàng tại chỗ phụ thuộc nhiều hơn vào thị trường và đối tác wholesale, nên ngân hàng dễ tổn thương hơn khi thị trường đi xuống [[src-choudhry-principles-banking#^choudhry-strat-17]].
- *Diễn giải:* LDR theo mảng (180% so với 60% ở EAB) cho thấy mỗi mảng chỉ nhìn một phía bảng cân đối. [[funds-transfer-pricing]] là công cụ chuyển chi phí funding của funding gap về mảng tạo ra nó.

## Nhầm lẫn thường gặp
- *Diễn giải:* LDR dưới 100% không có nghĩa là ngân hàng an toàn thanh khoản. Tỷ lệ này không phản ánh độ ổn định của tiền gửi hay lượng tài sản thanh khoản; xem [[lcr]], [[nsfr]].
