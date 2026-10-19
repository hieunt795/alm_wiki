---
title: Domain ALM
type: nav
domain: alm
updated: 2026-10-19
as_of: 2026-10-19
---

# Domain `alm`: ALM

## Phạm vi
IRRBB, thanh khoản (LCR/NSFR), FTP, hành vi khách hàng, balance sheet management (`03_meta/taxonomy.md`).

## Tóm tắt
*Diễn giải:* `alm` là domain trung tâm của wiki: gần như mọi node đều gắn `alm`, kể cả node có domain chính là `basel`, `vn-reg` hay `product`. Wiki phủ dày nhất ở ba mảng: IRRBB (d368 đã ingest đủ, kèm TT83/2025 và các sách Tata, Bardaeva, Lubinska), thanh khoản (LCR, NSFR, SRP50, ILAAP, CFP) và FTP (tài liệu tư vấn FTP, Choudhry, Lubinska). Mảng vốn và lợi nhuận điều chỉnh rủi ro mỏng hơn, chủ yếu dựa trên TT83/2025 PL6 và Choudhry. Phần lớn node ở mức draft. Node canonical tập trung ở IRRBB, NSFR/HQLA và FTP.

## Cụm chủ đề

### IRRBB: đo lường và quản trị
- IRRBB là rủi ro hiện tại hoặc tiềm năng đối với vốn và thu nhập do biến động bất lợi của lãi suất tác động lên vị thế trên sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u02-1]]. BCBS d368 chia IRRBB thành gap risk, basis risk và option risk [[src-bcbs-irrbb-2016#^irrbb-u02-2]].
- EVE là NPV của toàn bộ dòng tiền nhạy lãi suất trên sổ ngân hàng, loại trừ vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. ΔNII đo biến động thu nhập lãi thuần dự kiến trong một khoảng thời gian xác định dưới kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- Giả định NMD là nợ qua đêm hay nợ dài hạn tác động lên cả ΔEVE và ΔNII [[src-bcbs-irrbb-2016#^irrbb-p05-2]]. Replicating portfolio gán kỳ hạn hành vi cho NMD và vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
- Theo Bardaeva, Risk lập báo cáo phân tích rủi ro rồi chuyển cho ALM [[src-bardaeva-alm#^ch11-22]]. ALM đề xuất công cụ quản lý. Trading Desk thực hiện giao dịch sau khi hội đồng có thẩm quyền phê duyệt [[src-bardaeva-alm#^ch11-4]].
- Theo Choudhry, IRRBB là sản phẩm phụ của chênh lệch tái định giá giữa cho vay và huy động, thường do khách hàng tạo ra [[src-choudhry-principles-banking#^choudhry-cs-13]].
- SVB sụp đổ ngày 10/3/2023 [[src-tata-bank-alm#^tata-svb-1]]. Cuối 2022, SVB chỉ còn 0,5 tỷ USD swap phòng ngừa, tức 0,4% danh mục trái phiếu [[src-tata-bank-alm#^tata-svb-3]].

Node chính: [[irrbb-management]] · [[gap-risk]] · [[basis-risk]] · [[option-risk]] · [[csrbb]] · [[economic-value-of-equity]] · [[net-interest-income-sensitivity]] · [[standardised-interest-rate-shocks]] · [[outlier-bank-test]] · [[irrbb-standardised-framework]] · [[non-maturity-deposits]] · [[behavioural-options]] · [[irrbb-balance-sheet-portfolios]] (đều canonical) · [[repricing-balance-sheet]] · [[repricing-gap-analysis]] · [[notional-repricing-cash-flow]] · [[structural-hedging]] · [[pv01]] · [[cs01]] (stub) · [[silicon-valley-bank]]. Model: [[duration-gap-model]] · [[economic-value-at-risk]] · [[key-rate-duration]] · [[replicating-portfolio-model]] (canonical).

Synthesis `irrbb-*`: [[irrbb-five-tier-architecture]] và [[irrbb-alm-governance-strategy-and-tradeoffs]] (canonical) · [[irrbb-transmission-mechanisms-to-nii-and-eve]] · [[irrbb-standardised-shocks-eve-and-nii-measurement]] · [[irrbb-basis-risk-measurement-and-hedging]] · [[irrbb-csrbb-measurement-and-hedging]] · [[irrbb-casa-replicating-portfolio-and-irs-hedging]] · [[irrbb-repricing-profiles-and-behavioral-modeling]] · [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] · [[irrbb-principal-and-interest-cash-flows]] · [[irrbb-commercial-margins-and-discount-curves]] · [[irrbb-liquidity-hqla-and-ftp-interaction]].

### NII và NIM
- NII planning là dự phóng thu nhập lãi thuần cho các kỳ tương lai, khác với tính NII kỳ đã qua để báo cáo [[src-tata-bank-alm#^tata-niip-1]]. Kế hoạch hằng năm tối thiểu gồm khối lượng và biên lãi kỳ vọng của từng mảng, cùng môi trường lãi suất kỳ vọng [[src-tata-bank-alm#^tata-niip-3]].
- NIM là NII chia một thước đo tài sản bình quân [[src-choudhry-principles-banking#^choudhry-nim-14]].

Node: [[nii-planning]] · [[net-interest-margin]] · [[negative-interest-rates]] · [[effective-interest-rate]]. Synthesis: [[nii-nature-repricing-mechanisms-and-planning]] · [[nii-shocks-regulation-hedging-and-alco-tradeoffs]].

### Thanh khoản: LCR, NSFR, giám sát và dự phòng
- LCR yêu cầu đủ HQLA để vượt qua kịch bản stress đáng kể kéo dài 30 ngày [[src-bcbs-lcr#^lcr20-1]]. NSFR đo cơ cấu tài trợ trong khoảng thời gian một năm [[src-bcbs-nsfr#^nsf20-2]]. Chi tiết chuẩn mực ở [[domain-basel]].
- Theo TT83/2025, ngân hàng phải đưa chi phí và rủi ro thanh khoản vào định giá vốn nội bộ [[src-tt83-2025-nhnn#^d45-1b]].
- ILAAP là quy trình ngân hàng tự đánh giá mức đủ thanh khoản: chạy liquidity stress test, so với khẩu vị rủi ro thanh khoản, rồi ghi thành tài liệu để Board phê duyệt [[src-choudhry-principles-banking#^choudhry-ilaap-1]]. Cash-flow survival period là output chính của liquidity stress testing [[src-choudhry-principles-banking#^choudhry-ilaap-5]].
- Choudhry coi CFP là cấu phần quan trọng nhất của quản trị rủi ro thanh khoản, vì khủng hoảng thanh khoản cực đoan hiếm khi xảy ra [[src-choudhry-principles-banking#^choudhry-cfp-1]].
- Choudhry gọi tỷ lệ giữa cho vay và tiền gửi khách hàng là LTD ratio [[src-choudhry-principles-banking#^choudhry-strat-25]].

Node: [[lcr]] · [[nsfr]] · [[hqla]] (canonical) · [[liquidity-risk-management]] · [[liquidity-stress-testing]] · [[ilaap]] · [[cash-flow-survival-period]] · [[contingency-funding-plan]] (canonical) · [[intraday-liquidity-risk]] (canonical) · [[liquidity-monitoring-metrics]] (canonical) · [[asset-encumbrance]] · [[loan-to-deposit-ratio]] · [[lcr-nsfr-interlinkages]]. Cấu phần LCR/NSFR: xem [[domain-basel]].

Synthesis: [[basel-liquidity-monitoring-framework]] · [[synthetic-balance-sheet-liquidity-risk]] · [[practical-alm-liquidity-governance]] (canonical) · [[hqla-decomposition-and-tradeoffs]] · [[integrated-alm-liquidity-strategy]] · [[lcr-economic-significance-and-alm-governance]] · [[lcr-net-cash-outflows-mechanics]] · [[nsfr-alm-governance-strategy-and-risks]] · [[nsfr-structural-liquidity-and-alm-strategy]].

### FTP
- Theo Choudhry, FTP là chuyển giao rủi ro nội bộ, không phải phòng ngừa ra bên ngoài hay điều chuyển vốn [[src-choudhry-principles-banking#^choudhry-ftp-10]]. Khoản chuyển vốn nội bộ được thanh toán trên cơ sở trùng khớp kỳ hạn theo một đường cong FTP [[src-choudhry-principles-banking#^choudhry-ftp-6]].
- Trong FTP, COF là lãi suất đơn vị kinh doanh sử dụng vốn trả cho đơn vị quản trị vốn tập trung [[src-vab-ftp#^vab-ftp-21]].
- Liquidity FTP buộc đơn vị tạo tài sản dài hạn gánh đủ chi phí thanh khoản và chi phí tuân thủ mà tài sản đó gây ra [[src-choudhry-principles-banking#^choudhry-ftp-15]].

Node: [[funds-transfer-pricing]] · [[liquidity-transfer-pricing]] (canonical) · [[internal-risk-transfer]] (canonical) · [[cost-of-funds]] · [[ftp-pricing-methodology]] · [[ftp-transmission-mechanism]] · [[loan-pricing]]. Bảy synthesis FTP canonical và [[ftp-balance-sheet-optimization]]: xem [[domain-product]].

### Vốn, ICAAP và lợi nhuận điều chỉnh rủi ro
- Theo TT83/2025, vốn kinh tế là mức vốn ngân hàng tự xác định để bù đắp các rủi ro trọng yếu và bảo đảm tỷ lệ an toàn vốn trong kịch bản bất lợi [[src-tt83-2025-nhnn#^d3-7]].
- RAROC là một chỉ tiêu thu nhập trong khẩu vị rủi ro, cùng với ROE [[src-tt83-2025-nhnn#^d19-2]].
- Expected loss xác định từ PD và LGD [[src-choudhry-principles-banking#^choudhry-crd-2]].

Node: [[icaap]] · [[capital-plan]] · [[economic-capital]] · [[rwa-irrbb]] · [[target-capital]] · [[projected-own-funds]] · [[raroc]] · [[expected-loss]] · [[expected-credit-loss]] · [[shareholder-value-added]] · [[mrel]] · [[bail-in]] · [[recovery-and-resolution-planning]] · [[srep]] · [[leverage-ratio]] (canonical).

### Quản trị, tổ chức và mô hình
- Theo TT83/2025, ALCO giúp việc Tổng giám đốc về quản lý tài sản và nợ phải trả [[src-tt83-2025-nhnn#^d6-4b]]. Choudhry coi ALCO là diễn đàn quan trọng nhất trong mọi ngân hàng [[src-choudhry-principles-banking#^choudhry-alco-1]].
- Strategic ALM là chiến lược kinh doanh toàn ngân hàng dẫn dắt bởi cân nhắc ALM bảng cân đối. Theo Choudhry, cách làm này phải chủ động, từ trên xuống và có Board phê duyệt [[src-choudhry-principles-banking#^choudhry-salm-7]].
- Theo Bardaeva, không bàn Treasury/ALM nào chịu được toàn bộ nhiệm vụ ALM, vì một bộ phận không thể vừa đặt hạn mức vị thế vừa giao dịch cho vị thế đó [[src-bardaeva-alm#^ch10-1]].
- Theo Lubinska, bài toán tối ưu hoá sổ ngân hàng hầu như luôn là bài toán phi tuyến với ràng buộc bất đẳng thức [[src-lubinska-alm-optimisation#^lubinska-u04-12]].
- Rủi ro khí hậu tác động lên thu nhập và vốn qua bốn kênh: tín dụng đối tác, huy động vốn, đầu tư và quy định [[src-tata-bank-alm#^tata-fut-4]].

Node: [[alco]] · [[strategic-alm]] · [[alm-operating-model]] · [[bank-strategic-plan]] · [[bank-corporate-governance]] · [[risk-appetite]] · [[risk-limits]] · [[key-risk-indicators]] · [[three-lines-of-defence]] · [[stress-testing]] · [[reverse-stress-testing]] · [[model-risk-management]] · [[model-validation]] · [[new-product-approval]] · [[hedge-accounting]] · [[climate-risk]] · [[credit-risk-management]] · [[market-risk-management]] · [[operational-risk-management]] · [[concentration-risk-management]]. Model: [[balance-sheet-optimisation-model]].

## Giao với domain khác
- `basel`: chuẩn mực LCR, NSFR, IRRBB, LEV là ràng buộc của bài toán ALM. Xem [[domain-basel]].
- `vn-reg`: TT83/2025 quy định cách ngân hàng VN quản trị IRRBB, thanh khoản, ICAAP. Xem [[domain-vn-reg]].
- `product`: phái sinh phòng ngừa, sản phẩm tiền gửi/cho vay, FTP. Xem [[domain-product]].
- `macro`: lãi suất âm và sàn 0% trên tiền gửi bán lẻ [[src-tata-bank-alm#^tata-neg-2]]. Xem [[domain-macro]].

## Lỗ hổng và câu hỏi mở
- Nguồn ALM còn unit chưa ingest: `src-choudhry-principles-banking`, `src-tata-bank-alm`, `src-bardaeva-alm`, `src-lubinska-alm-optimisation` (`03_meta/sources.yaml`).
- Cột VN cho LCR/NSFR chờ ingest TT50/2026. Xem [[domain-vn-reg]].
- [[cs01]] và [[bcbs]] là stub.
- Wiki chưa có node cho tỷ lệ an toàn vốn (CAR) theo TT14/2025 [cần nguồn].

## Thống kê
Diễn giải: thống kê nội bộ wiki, không phải claim nguồn. Đếm mọi node có `alm` trong `domains`, ở bất kỳ vị trí nào, as_of 2026-10-19.

| Type | Số node |
|---|---|
| concept | 60 |
| metric | 47 |
| model | 9 |
| instrument | 7 |
| regulation | 4 |
| entity | 1 |
| synthesis | 31 |
| source | 12 |
| **Tổng** | **171** (canonical 46, draft 125) |
