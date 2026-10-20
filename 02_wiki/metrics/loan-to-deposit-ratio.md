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
updated: 2026-10-20
reviewed:
---

## Định nghĩa
Loan-to-deposit ratio (LDR) so cho vay khách hàng với tiền gửi khách hàng. Choudhry đo customer funding gap bằng cho vay khách hàng trừ tiền gửi khách hàng, và gọi tỷ lệ tương ứng là "loan to deposit" (LTD) ratio [[src-choudhry-principles-banking#^choudhry-strat-25]]. Loan-deposit ratio là một KPI trong Table 15.1, bộ KPI mà strategic plan và budget nên có [[src-choudhry-principles-banking#^choudhry-strat-28]].

## Công thức
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
| Công thức VN | — | LDR = L / D × 100%, theo VNĐ gồm ngoại tệ quy đổi; L trừ cho vay TCTD khác và vay tái cấp vốn NHNN không nhằm hỗ trợ thanh khoản [[src-tt50-2026-nhnn#^d12-1]]; D gồm tiền gửi tổ chức và cá nhân (trừ tiền gửi TCTD, ký quỹ, KBNN không kỳ hạn và 80% KBNN có kỳ hạn), trái phiếu đủ điều kiện Vốn cấp 2, vay nước ngoài, vốn chủ sở hữu…, trừ đầu tư trái phiếu doanh nghiệp [[src-tt50-2026-nhnn#^d12-4]] | TT50 Đ12.1–5 | |
| Ngưỡng tối đa | — | 95% [[src-tt50-2026-nhnn#^d12-6]] | TT50 Đ12.6 | Từ khi áp dụng LCR/NSFR (Đ13.5) [[src-tt50-2026-nhnn#^d12-6]] |
| Chuyển tiếp | — | Trước khi áp dụng LCR/NSFR: tuân thủ LDR theo TT22/2019 [[src-tt50-2026-nhnn#^d13-4]]. Sau đó: tuân thủ LDR theo Đ12 TT50; áp dụng ngưỡng 100% cho cả LCR và NSFR thì LDR chỉ phải báo cáo [[src-tt50-2026-nhnn#^d13-5]] | TT50 Đ13.4–5 | 01/10/2026 [[src-tt50-2026-nhnn#^d37-1]] |

*Diễn giải:* Basel III đo funding ổn định bằng [[nsfr]], có trọng số theo hành vi và kỳ hạn. LDR là tỷ lệ thô, không phân biệt tiền gửi bán lẻ ổn định với tiền gửi wholesale.

## Ứng dụng trong ALM
- Strategic plan nên đặt mục tiêu dài hạn cho một số KPI trong Table 15.1, trong đó có loan-deposit ratio và wholesale funding ratio, cho toàn ngân hàng và từng mảng Treasury, Corporate Banking, Retail Banking [[src-choudhry-principles-banking#^choudhry-strat-28]]. Xem [[bank-strategic-plan]].
- Fitch dùng customer loans/customer deposits làm một trong 5 tỷ lệ funding cấu trúc để so sánh ngân hàng [[src-choudhry-principles-banking#^choudhry-peer-6]].
- Northern Rock tăng cho vay vượt nền tiền gửi và tài trợ phần dư bằng wholesale và securitisation [[src-choudhry-principles-banking#^choudhry-gov-8]]. Xem [[bank-corporate-governance]].
- Cho vay ở nước ngoài không có nền tiền gửi khách hàng tại chỗ phụ thuộc nhiều hơn vào thị trường và đối tác wholesale, nên ngân hàng dễ tổn thương hơn khi thị trường đi xuống [[src-choudhry-principles-banking#^choudhry-strat-17]].
- *Diễn giải:* LDR theo mảng (180% so với 60% ở EAB) cho thấy mỗi mảng chỉ nhìn một phía bảng cân đối. [[funds-transfer-pricing]] là công cụ chuyển chi phí funding của funding gap về mảng tạo ra nó.

## Nhầm lẫn thường gặp
- *Diễn giải:* LDR dưới 100% không có nghĩa là ngân hàng an toàn thanh khoản. Tỷ lệ này không phản ánh độ ổn định của tiền gửi hay lượng tài sản thanh khoản; xem [[lcr]], [[nsfr]].
