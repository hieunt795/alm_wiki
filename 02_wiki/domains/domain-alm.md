---
title: Domain ALM
type: nav
domain: alm
updated: 2026-10-23
as_of: 2026-10-23
---

# Domain `alm`: ALM

## Phạm vi
IRRBB, thanh khoản (LCR/NSFR), FTP, hành vi khách hàng, balance sheet management (`03_meta/taxonomy.md`).

## Tóm tắt
*Diễn giải:* `alm` là domain trung tâm của wiki: gần như mọi node đều gắn `alm`, kể cả node có domain chính là `basel`, `vn-reg` hay `product`. Wiki phủ dày nhất ở ba mảng: IRRBB (d368 đã ingest đủ, kèm TT83/2025 và các sách Tata, Bardaeva, Lubinska), thanh khoản (LCR, NSFR, SRP50, ILAAP, CFP) và FTP (tài liệu tư vấn FTP, Choudhry, Lubinska). Mảng vốn và lợi nhuận điều chỉnh rủi ro mỏng hơn, chủ yếu dựa trên TT83/2025 PL6 và Choudhry. Toàn bộ node đang ở mức draft (45 node canonical cũ đã hạ bậc ngày 2026-10-20 để rà lại).

## Cụm chủ đề

### IRRBB: đo lường và quản trị
- IRRBB là rủi ro hiện tại hoặc tiềm năng đối với vốn và thu nhập do biến động bất lợi của lãi suất tác động lên vị thế trên sổ ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u02-1]]. BCBS d368 chia IRRBB thành gap risk, basis risk và option risk [[src-bcbs-irrbb-2016#^irrbb-u02-2]].
- EVE là NPV của toàn bộ dòng tiền nhạy lãi suất trên sổ ngân hàng, loại trừ vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. ΔNII đo biến động thu nhập lãi thuần dự kiến trong một khoảng thời gian xác định dưới kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- Giả định NMD là nợ qua đêm hay nợ dài hạn tác động lên cả ΔEVE và ΔNII [[src-bcbs-irrbb-2016#^irrbb-p05-2]]. Replicating portfolio gán kỳ hạn hành vi cho NMD và vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
- Theo Bardaeva, Risk lập báo cáo phân tích rủi ro rồi chuyển cho ALM [[src-bardaeva-alm#^ch11-22]]. ALM đề xuất công cụ quản lý. Trading Desk thực hiện giao dịch sau khi hội đồng có thẩm quyền phê duyệt [[src-bardaeva-alm#^ch11-4]].
- Theo Choudhry, IRRBB là sản phẩm phụ của chênh lệch tái định giá giữa cho vay và huy động, thường do khách hàng tạo ra [[src-choudhry-principles-banking#^choudhry-cs-13]].
- SVB sụp đổ ngày 10/3/2023 [[src-tata-bank-alm#^tata-svb-1]]. Cuối 2022, SVB chỉ còn 0,5 tỷ USD swap phòng ngừa, tức 0,4% danh mục trái phiếu [[src-tata-bank-alm#^tata-svb-3]].

Node chính: [[irrbb-management]] · [[gap-risk]] · [[basis-risk]] · [[option-risk]] · [[csrbb]] · [[economic-value-of-equity]] · [[net-interest-income-sensitivity]] · [[standardised-interest-rate-shocks]] · [[outlier-bank-test]] · [[irrbb-standardised-framework]] · [[non-maturity-deposits]] · [[behavioural-options]] · [[irrbb-balance-sheet-portfolios]] · [[repricing-balance-sheet]] · [[repricing-gap-analysis]] · [[notional-repricing-cash-flow]] · [[structural-hedging]] · [[pv01]] · [[cs01]] (stub) · [[silicon-valley-bank]]. Model: [[duration-gap-model]] · [[economic-value-at-risk]] · [[key-rate-duration]] · [[replicating-portfolio-model]].

### NII và NIM
- NII planning là dự phóng thu nhập lãi thuần cho các kỳ tương lai, khác với tính NII kỳ đã qua để báo cáo [[src-tata-bank-alm#^tata-niip-1]]. Kế hoạch hằng năm tối thiểu gồm khối lượng và biên lãi kỳ vọng của từng mảng, cùng môi trường lãi suất kỳ vọng [[src-tata-bank-alm#^tata-niip-3]].
- NIM là NII chia một thước đo tài sản bình quân [[src-choudhry-principles-banking#^choudhry-nim-14]].

Node: [[nii-planning]] · [[net-interest-margin]] · [[negative-interest-rates]] · [[effective-interest-rate]].

### Thanh khoản: LCR, NSFR, giám sát và dự phòng
- LCR yêu cầu đủ HQLA để vượt qua kịch bản stress đáng kể kéo dài 30 ngày [[src-bcbs-lcr#^lcr20-1]]. NSFR đo cơ cấu tài trợ trong khoảng thời gian một năm [[src-bcbs-nsfr#^nsf20-2]]. Chi tiết chuẩn mực ở [[domain-basel]].
- Theo TT83/2025, ngân hàng phải đưa chi phí và rủi ro thanh khoản vào định giá vốn nội bộ [[src-tt83-2025-nhnn#^d45-1b]].
- ILAAP là quy trình ngân hàng tự đánh giá mức đủ thanh khoản: chạy liquidity stress test, so với khẩu vị rủi ro thanh khoản, rồi ghi thành tài liệu để Board phê duyệt [[src-choudhry-principles-banking#^choudhry-ilaap-1]]. Cash-flow survival period là output chính của liquidity stress testing [[src-choudhry-principles-banking#^choudhry-ilaap-5]].
- Choudhry coi CFP là cấu phần quan trọng nhất của quản trị rủi ro thanh khoản, vì khủng hoảng thanh khoản cực đoan hiếm khi xảy ra [[src-choudhry-principles-banking#^choudhry-cfp-1]].
- Choudhry gọi tỷ lệ giữa cho vay và tiền gửi khách hàng là LTD ratio [[src-choudhry-principles-banking#^choudhry-strat-25]].
- Structural liquidity risk là nguy cơ tổn thất thực tế hoặc chi phí cơ hội khi cơ cấu bảng cân đối dưới tối ưu [[src-lubinska-alm-optimisation#^lubinska-u05-6]]; Lubinska đo bằng structural limit dùng dòng tiền sau 1 năm và vốn cấp 1, thông lệ tốt từ 100% trở lên [[src-lubinska-alm-optimisation#^lubinska-u05-17]] [[src-lubinska-alm-optimisation#^lubinska-u05-18]].

Node: [[lcr]] · [[nsfr]] · [[hqla]] · [[liquidity-risk-management]] · [[liquidity-cost-risk]] · [[structural-liquidity-risk]] · [[liquidity-stress-testing]] · [[ilaap]] · [[bcbs-liquidity-principles]] · [[cash-flow-survival-period]] · [[contingency-funding-plan]] · [[intraday-liquidity-risk]] · [[liquidity-monitoring-metrics]] · [[asset-encumbrance]] · [[loan-to-deposit-ratio]] · [[government-bond-holding-ratio]] ([[government-bond-holdings]], [[average-total-liabilities]]) · [[lcr-nsfr-interlinkages]]. Cấu phần LCR/NSFR: xem [[domain-basel]].

### FTP
- Theo Choudhry, FTP là chuyển giao rủi ro nội bộ, không phải phòng ngừa ra bên ngoài hay điều chuyển vốn [[src-choudhry-principles-banking#^choudhry-ftp-10]]. Khoản chuyển vốn nội bộ được thanh toán trên cơ sở trùng khớp kỳ hạn theo một đường cong FTP [[src-choudhry-principles-banking#^choudhry-ftp-6]].
- Trong FTP, COF là lãi suất đơn vị kinh doanh sử dụng vốn trả cho đơn vị quản trị vốn tập trung [[src-vab-ftp#^vab-ftp-21]].
- Hệ thống FTP là ranh giới giữa maturity transformation và customer franchise [[src-choudhry-principles-banking#^choudhry-ftp-3]]. Maturity transformation tạo đồng thời rủi ro lãi suất và rủi ro thanh khoản [[src-lubinska-alm-optimisation#^lubinska-u02-18]]. Xem [[maturity-transformation]].
- Liquidity FTP buộc đơn vị tạo tài sản dài hạn gánh đủ chi phí thanh khoản và chi phí tuân thủ mà tài sản đó gây ra [[src-choudhry-principles-banking#^choudhry-ftp-15]].
- Lubinska mô tả ALM là "bank within a bank": ALM thu FTP rate của asset centre, ghi có FTP rate cho liability centre, và rủi ro lãi suất, rủi ro funding được tách khỏi BU [[src-lubinska-alm-optimisation#^lubinska-u01-7]]. Rủi ro tín dụng theo định nghĩa không chuyển về ALM [[src-lubinska-alm-optimisation#^lubinska-u01-8]].
- Có 4 cách dựng FTP curve: market, cost, mixed và marginal; marginal được bổ sung sau, do hướng dẫn của cơ quan quản lý [[src-choudhry-principles-banking#^choudhry-ifc-16]]. Ở thị trường mới nổi, đường cong nội bộ có thể dựng từ implied yield curve và FX forward, và có thể bỏ tách liquidity cost và base cost [[src-choudhry-principles-banking#^choudhry-ifc-22]].

Node: [[funds-transfer-pricing]] · [[maturity-transformation]] · [[liquidity-transfer-pricing]] · [[internal-risk-transfer]] · [[cost-of-funds]] · [[ftp-pricing-methodology]] · [[ftp-transmission-mechanism]] · [[internal-funding-curve]] (model) · [[loan-pricing]] · [[credit-turnover]]. Bảy synthesis FTP: xem [[domain-product]].

### Vốn, ICAAP và lợi nhuận điều chỉnh rủi ro
- Theo TT83/2025, vốn kinh tế là mức vốn ngân hàng tự xác định để bù đắp các rủi ro trọng yếu và bảo đảm tỷ lệ an toàn vốn trong kịch bản bất lợi [[src-tt83-2025-nhnn#^d3-7]].
- RAROC là một chỉ tiêu thu nhập trong khẩu vị rủi ro, cùng với ROE [[src-tt83-2025-nhnn#^d19-2]].
- Expected loss xác định từ PD và LGD [[src-choudhry-principles-banking#^choudhry-crd-2]].

Node: [[icaap]] · [[capital-plan]] · [[economic-capital]] · [[rwa-irrbb]] · [[target-capital]] · [[projected-own-funds]] · [[raroc]] · [[expected-loss]] · [[expected-credit-loss]] · [[shareholder-value-added]] · [[mrel]] · [[bail-in]] · [[recovery-and-resolution-planning]] · [[srep]] · [[leverage-ratio]].

### Quản trị, tổ chức và mô hình
- Theo TT83/2025, ALCO giúp việc Tổng giám đốc về quản lý tài sản và nợ phải trả [[src-tt83-2025-nhnn#^d6-4b]]. Choudhry coi ALCO là diễn đàn quan trọng nhất trong mọi ngân hàng [[src-choudhry-principles-banking#^choudhry-alco-1]]. BCBS 144 không gọi tên ALCO; theo P3, ban điều hành xây chiến lược thanh khoản gồm cơ cấu và kỳ hạn tài sản – nợ, HĐQT phê duyệt ít nhất hằng năm [[src-bcbs-liquidity-principles-2008#^lrm-p03]] [[src-bcbs-liquidity-principles-2008#^lrm-11]].
- Strategic ALM là chiến lược kinh doanh toàn ngân hàng dẫn dắt bởi cân nhắc ALM bảng cân đối. Theo Choudhry, cách làm này phải chủ động, từ trên xuống và có Board phê duyệt [[src-choudhry-principles-banking#^choudhry-salm-7]].
- Theo Bardaeva, sự tiến hoá của các khái niệm ALM trải qua 6 giai đoạn từ sau 1950 (Can thiệp tối thiểu → Rủi ro tối thiểu → Công cụ ngoại bảng → Rào cản bảng cân đối → Thời kỳ biên sinh lời thấp → Vượt qua các điểm nghẽn) phản ánh sự thay đổi của môi trường vĩ mô và khung pháp quy [[src-bardaeva-alm#^ch7-1]] [[src-bardaeva-alm#^ch7-6]]. Trong Banking Package mới, sự liên kết toàn diện giữa Vốn, Thanh khoản, IRRBB và MREL khiến ALM chuyển trọng tâm sang giải bài toán tối ưu hoá đa tham số để nhận diện và điều phối các "điểm nghẽn" (bottlenecks) [[src-bardaeva-alm#^ch6-1]] [[src-bardaeva-alm#^ch6-3]]. Khung RAF gồm 4 trụ cột cùng cơ chế đèn tín hiệu 3 màu Green/Amber/Red điều hành bảng cân đối, kích hoạt ERT và kế hoạch phục hồi [[src-bardaeva-alm#^ch8-1]] [[src-bardaeva-alm#^ch8-3]].
- Theo Lubinska, bài toán tối ưu hoá sổ ngân hàng hầu như luôn là bài toán phi tuyến với ràng buộc bất đẳng thức [[src-lubinska-alm-optimisation#^lubinska-u04-12]].
- Rủi ro khí hậu tác động lên thu nhập và vốn qua bốn kênh: tín dụng đối tác, huy động vốn, đầu tư và quy định [[src-tata-bank-alm#^tata-fut-4]].
- Theo Basel SRP30, rủi ro danh tiếng có thể tác động lên nợ phải trả: để tránh tổn hại uy tín, ngân hàng có thể gọi nợ trước hạn dù làm xấu hồ sơ thanh khoản, đặc biệt với nợ hybrid/thứ cấp [[src-bcbs-framework#^srp30-33]].

Node: [[alco]] · [[strategic-alm]] · [[alm-evolution]] · [[alm-operating-model]] · [[bank-strategic-plan]] · [[bank-corporate-governance]] · [[risk-appetite]] · [[risk-limits]] · [[key-risk-indicators]] · [[three-lines-of-defence]] · [[stress-testing]] · [[reverse-stress-testing]] · [[model-risk-management]] · [[model-validation]] · [[new-product-approval]] · [[hedge-accounting]] · [[climate-risk]] · [[credit-risk-management]] · [[market-risk-management]] · [[operational-risk-management]] · [[concentration-risk-management]] · [[firm-wide-risk-management]] · [[reputational-risk]]. Model: [[balance-sheet-optimisation-model]].

## Giao với domain khác
- `basel`: chuẩn mực LCR, NSFR, IRRBB, LEV là ràng buộc của bài toán ALM. Xem [[domain-basel]].
- `vn-reg`: TT83/2025 quy định cách ngân hàng VN quản trị IRRBB, thanh khoản, ICAAP. Xem [[domain-vn-reg]].
- `product`: phái sinh phòng ngừa, sản phẩm tiền gửi/cho vay, FTP. Xem [[domain-product]].
- `macro`: lãi suất âm và sàn 0% trên tiền gửi bán lẻ [[src-tata-bank-alm#^tata-neg-2]]. Xem [[domain-macro]].

## Lỗ hổng và câu hỏi mở
- Nguồn ALM còn unit chưa ingest: `src-choudhry-principles-banking`, `src-tata-bank-alm`, `src-bardaeva-alm`, `src-lubinska-alm-optimisation` (`03_meta/sources.yaml`).
- Cột VN cho LCR/NSFR chờ ingest TT50/2026. Xem [[domain-vn-reg]].
- [[cs01]] và [[bcbs]] là stub.
- Node tỷ lệ an toàn vốn theo TT14/2025 đã có ([[capital-adequacy-ratio]], [[own-funds]], [[capital-conservation-buffer]], [[countercyclical-capital-buffer]], [[capital-adequacy-management]], [[market-risk-capital-requirement]], [[operational-risk-capital-requirement]], [[common-equity-tier-1-capital]], [[additional-tier-1-capital]], [[tier-2-capital]], [[capital-deductions]], [[subordinated-debt]], [[business-indicator]] và ba cấu phần ILDC, SC, FC) cùng khung RWA tín dụng ([[risk-weighted-assets]], [[customer-credit-risk-rwa]], [[counterparty-credit-risk-rwa]], [[exposure-value]], [[specific-provision]], [[credit-conversion-factor]], [[credit-risk-weight]]); bảng hệ số rủi ro tín dụng theo nhóm tài sản đã có ([[credit-risk-weight]], [[loan-to-value]], [[corporate-exposure-risk-weighting]]); xếp hạng độc lập ([[external-credit-rating-use]], [[credit-rating-scale-mapping]]); giảm thiểu rủi ro tín dụng ([[credit-risk-mitigation]], [[eligible-collateral-haircuts]], [[on-balance-sheet-netting]], [[third-party-guarantee-mitigation]], [[credit-derivative-mitigation]]) và rủi ro tín dụng đối tác ([[replacement-cost]], [[potential-future-exposure]], [[add-on-factor]], [[bilateral-netting]], [[settlement-failure-risk-weighting]]); thiếu Phụ lục II [cần nguồn]; khung IRB đã có ([[internal-ratings-based-approach]], [[irb-coverage-ratio]], [[output-floor]], [[irb-approval-process]], [[customer-default-definition]], [[irb-asset-classes]], [[irb-capital-requirement]], [[probability-of-default]], [[loss-given-default]], [[exposure-at-default]], [[asset-correlation]], [[maturity-adjustment]], [[irb-credit-risk-mitigation]], [[irb-retail-parameter-estimation]], [[purchased-receivables-rwa]], [[purchased-receivables-default-risk-rwa]], [[purchased-receivables-dilution-risk-rwa]], [[irb-expected-loss]], [[irb-risk-provisions]], [[el-provision-difference-treatment]], [[irb-rating-system-design]], [[irb-model-governance]], [[irb-rating-operation-and-governance]], [[irb-use-test]], [[irb-parameter-estimation-requirements]], [[irb-model-validation]], [[irb-implementation-plan]], [[capital-adequacy-reporting-and-disclosure]], [[sbv-capital-supervision-responsibilities]]); cách tính từng cấu phần $K_{MR}$ đã có ([[interest-rate-risk-capital-requirement]], [[specific-interest-rate-risk-capital]], [[general-interest-rate-risk-capital]], [[net-weighted-position]], [[vertical-disallowance]], [[horizontal-disallowance]], [[equity-risk-capital-requirement]], [[foreign-exchange-risk-capital-requirement]], [[commodity-risk-capital-requirement]], [[options-risk-capital-requirement]]).

## Thống kê
Diễn giải: thống kê nội bộ wiki, không phải claim nguồn. Đếm mọi node có `alm` trong `domains`, ở bất kỳ vị trí nào, as_of 2026-10-23.

| Type | Số node |
|---|---|
| concept | 75 |
| metric | 72 |
| model | 10 |
| instrument | 8 |
| regulation | 7 |
| entity | 1 |
| source | 16 |
| synthesis | 10 |
| **Tổng** | **199** (đều draft) |
