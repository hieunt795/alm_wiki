---
title: Domain Basel
type: nav
domain: basel
updated: 2026-10-21
as_of: 2026-10-20
---

# Domain `basel`: Basel

## Phạm vi
Chuẩn mực BCBS về vốn, thanh khoản, IRRBB, đòn bẩy (`03_meta/taxonomy.md`). Domain này phân biệt `doc_status: consultative` với `final`. Với nghĩa vụ tuân thủ tại VN, Basel chỉ là tham chiếu, xem [[domain-vn-reg]].

## Tóm tắt
*Diễn giải:* wiki đã ingest đủ ba chuẩn mực BCBS: LCR, NSFR và IRRBB (d368). Đã có phần lõi của Leverage Ratio (LEV10–LEV40) và ba chương của Basel Framework: SRP50 (chỉ số giám sát thanh khoản), RBC25 (ranh giới banking book/trading book) và SRP30 (nguyên tắc quản trị rủi ro Pillar 2). Mọi chuẩn mực trong wiki đều là bản final. Mảng vốn (RBC, rủi ro tín dụng, rủi ro thị trường, rủi ro hoạt động) gần như chưa có, vì phần còn lại của Basel Framework chưa ingest.

## Cụm chủ đề

### LCR: thanh khoản ngắn hạn
- Ngân hàng phải giữ đủ [[hqla]] để vượt qua kịch bản stress đáng kể kéo dài 30 ngày [[src-bcbs-lcr#^lcr20-1]]. Kịch bản kết hợp cú sốc riêng của ngân hàng và cú sốc toàn thị trường [[src-bcbs-lcr#^lcr20-2]].
- LCR bắt buộc trên cơ sở hợp nhất cho mọi ngân hàng hoạt động quốc tế [[src-bcbs-lcr#^lcr10-1]], với ngưỡng ≥ 100% [[src-bcbs-lcr#^lcr20-5]].
- Trần Level 2 trong HQLA là 40%, trần Level 2B là 15% [[src-bcbs-lcr#^lcr30-31]]. Haircut Level 2A là 15% [[src-bcbs-lcr#^lcr30-43]].
- Ngân hàng phải unwind các giao dịch repo, reverse repo, collateral swap đáo hạn trong 30 ngày có trao đổi HQLA để tính số dư điều chỉnh [[src-bcbs-lcr#^lcr30-34]].
- Dòng vào bị chặn ở 75% dòng ra [[src-bcbs-lcr#^lcr40-77]]. Run-off của stable retail deposit là 5%, jurisdiction có thể chọn 3% [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-11]].

Node: [[bcbs-lcr]] (regulation) · [[lcr]] · [[hqla]] · [[level-1-assets]] · [[level-2-assets]] · [[hqla-unwinding-mechanism]] · [[net-cash-outflows]] · [[cash-outflows]] · [[cash-inflows]] · [[run-off-rate]] · [[retail-deposit-stability]] · [[operational-deposits]] · [[unsecured-wholesale-funding]] · [[secured-funding]] · [[committed-facilities]] · [[derivatives-and-contingent-outflows]] · [[alternative-liquidity-approaches]] · [[liquidity-transfer-restrictions]].

### NSFR: cơ cấu tài trợ một năm
- NSFR yêu cầu ngân hàng duy trì cơ cấu nguồn vốn ổn định tương ứng với thành phần tài sản và hoạt động ngoại bảng [[src-bcbs-nsfr#^nsf-preamble]]. Chuẩn mực hạn chế phụ thuộc vào nguồn vốn bán buôn ngắn hạn [[src-bcbs-nsfr#^nsf20-1]].
- NSFR phải đạt tối thiểu 100% trên cơ sở liên tục [[src-bcbs-nsfr#^nsf20-2]], báo cáo tối thiểu hằng quý [[src-bcbs-nsfr#^nsf20-3]].
- ASF là phần vốn và nợ dự kiến đáng tin cậy trong khoảng thời gian 1 năm [[src-bcbs-nsfr#^nsf20-2]]. Vốn tự có và nợ có kỳ hạn từ 1 năm nhận ASF 100% [[src-bcbs-nsfr#^nsf30-10]].
- Cho vay thế chấp nhà ở nhận RSF 65%, cho vay thông thường 85%, cho vay dưới 1 năm 50%, NPL 100% [[src-bcbs-nsfr#^nsf30-29]] [[src-bcbs-nsfr#^nsf30-30]] [[src-bcbs-nsfr#^nsf30-31]] [[src-bcbs-nsfr#^nsf30-32]].

Node: [[bcbs-nsfr]] (regulation) · [[nsfr]] · [[available-stable-funding]] · [[required-stable-funding]] · [[asf-capital-and-long-term-liabilities]] · [[asf-retail-and-small-business-deposits]] · [[asf-wholesale-and-operational-funding]] · [[rsf-hqla-and-central-bank-reserves]] · [[rsf-loans-and-credit-exposures]] · [[rsf-securities-financing-and-encumbrance]] · [[rsf-derivatives-and-off-balance-sheet]] · [[interdependent-assets-and-liabilities]] · [[lcr-nsfr-interlinkages]].

### SRP50: chỉ số giám sát thanh khoản
- SRP50 thuộc Trụ cột 2, bổ trợ cho LCR và NSFR [[src-bcbs-framework#^srp50-1]]. SRP50 không thay thế LCR hay NSFR [[src-bcbs-framework#^srp50-2]].

Node: [[liquidity-monitoring-metrics]] · [[contractual-maturity-mismatch]] · [[funding-concentration-risk]] · [[available-unencumbered-assets]] · [[lcr-by-currency]] · [[intraday-liquidity-risk]].

### IRRBB (d368)
- d368 đặt nguyên tắc và phương pháp để nhận diện, đo lường, theo dõi và kiểm soát IRRBB và [[csrbb]] [[src-bcbs-irrbb-2016#^irrbb-u01-1]]. BCBS giữ IRRBB trong Trụ cột 2 nâng cao, kèm công bố theo Trụ cột 3 [[src-bcbs-irrbb-2016#^irrbb-u01-2]].
- Chuẩn mực có hiệu lực từ năm 2018 [[src-bcbs-irrbb-2016#^irrbb-u04-2]].
- Bộ sốc chuẩn hoá có 6 kịch bản, áp dụng cho ΔEVE [[src-bcbs-irrbb-2016#^irrbb-u07-1]]. Sốc áp riêng cho từng đồng tiền chiếm từ 5% tài sản hoặc nợ của sổ ngân hàng trở lên [[src-bcbs-irrbb-2016#^irrbb-u07-2]].
- Supervisor nên (should) áp phép thử outlier, so ΔEVE với 15% Tier 1 [[src-bcbs-irrbb-2016#^irrbb-p12-1]]. Ngân hàng bị xác định là outlier phải được rà soát [[src-bcbs-irrbb-2016#^irrbb-p12-4]].
- Quyền chọn của khách hàng wholesale làm thay đổi dòng tiền phải xếp vào nhóm quyền chọn tự động [[src-bcbs-irrbb-2016#^irrbb-u05-7]].

Node: [[bcbs-irrbb]] (regulation) · [[economic-value-of-equity]] · [[net-interest-income-sensitivity]] · [[standardised-interest-rate-shocks]] · [[irrbb-standardised-framework]] · [[outlier-bank-test]] · [[gap-risk]] · [[basis-risk]] · [[option-risk]] · [[behavioural-options]] · [[non-maturity-deposits]] · [[csrbb]] · [[irrbb-balance-sheet-portfolios]] · [[notional-repricing-cash-flow]] · [[irrbb-management]]. Model: [[duration-gap-model]] · [[economic-value-at-risk]] · [[key-rate-duration]] · [[replicating-portfolio-model]].

### Leverage Ratio
- Leverage Ratio là chuẩn mực phi rủi ro thuộc Trụ cột 1, là backstop cho khuôn khổ vốn dựa trên RWA [[src-bcbs-lev#^lev20-1]]. Ngân hàng phải duy trì tỷ lệ đòn bẩy tối thiểu 3% tại mọi thời điểm [[src-bcbs-lev#^lev20-7]].
- Exposure measure tính theo giá trị kế toán gộp [[src-bcbs-lev#^lev30-1]]. Tài sản bảo đảm và bảo lãnh không được dùng để giảm phơi nhiễm [[src-bcbs-lev#^lev30-2]].

Node: [[leverage-ratio]] · [[leverage-exposure-measure]].

### Banking book / trading book (RBC25), Pillar 2 và resolution
- Internal risk transfer theo RBC25 là bản ghi nội bộ về việc chuyển rủi ro trong banking book, giữa banking book và trading book, hoặc giữa các desk trong trading book [[src-bcbs-framework#^rbc25-18]]. Phiên bản RBC25 đã ingest có hiệu lực từ 01/01/2023 [[src-bcbs-framework#^rbc25-0]].
- Kết quả SREP gồm điểm số và yêu cầu vốn bổ sung riêng cho từng ngân hàng (P2R) [[src-bardaeva-alm#^ch13-1]]. Claim này lấy qua nguồn sách (Bardaeva), không phải văn bản BCBS.
- Theo BRRD, bail-in dùng để bù lỗ hoặc chuyển nợ đủ điều kiện thành vốn, và tổ chức tiếp tục hoạt động [[src-bardaeva-alm#^ch14-5]].

Node: [[regulatory-internal-risk-transfer]] · [[banking-book]] · [[srep]] · [[icaap]] · [[ilaap]] · [[bail-in]] · [[mrel]] · [[recovery-and-resolution-planning]] · [[contingent-convertible-bond]]. [[srep]], [[bail-in]], [[mrel]] dựa trên sách và quy định EU, không trên văn bản BCBS.

### SRP30: quản trị rủi ro Pillar 2
- Yêu cầu vốn Pillar 1 là mức tối thiểu; mọi rủi ro nên được phủ đủ vốn, kể cả qua Pillar 2 vượt mức Pillar 1 [[src-bcbs-framework#^srp30-3]]. ICAAP nên làm trên cơ sở hợp nhất, và ở cấp pháp nhân khi cơ quan giám sát thấy cần [[src-bcbs-framework#^srp30-2]].
- Chức năng quản lý rủi ro và CRO nên độc lập với các mảng kinh doanh, báo cáo trực tiếp CEO và HĐQT [[src-bcbs-framework#^srp30-11]].
- SRP30.22 liệt kê chín tình huống tập trung rủi ro, trong đó có nguồn vốn [[src-bcbs-framework#^srp30-22]].
- Rủi ro danh tiếng có thể dẫn tới hỗ trợ ngầm, phát sinh rủi ro tín dụng, thanh khoản, thị trường, pháp lý [[src-bcbs-framework#^srp30-30]].
- HĐQT đặt liquidity risk tolerance; ngân hàng nên đưa chi phí thanh khoản vào định giá nội bộ và duyệt sản phẩm mới [[src-bcbs-framework#^srp30-50]].

Node: [[firm-wide-risk-management]] · [[reputational-risk]] · [[valuation-governance]] (mới) · cập nhật [[icaap]], [[concentration-risk-management]], [[liquidity-risk-management]], [[risk-appetite]], [[risk-limits]], [[stress-testing]], [[new-product-approval]], [[three-lines-of-defence]], [[srep]].

### BCBS 144: nguyên tắc quản trị rủi ro thanh khoản
- Ngân hàng nên có khung quản trị rủi ro thanh khoản vững chắc, gồm đệm tài sản thanh khoản cao không bị cầm cố, để chịu stress làm mất nguồn vốn có và không có bảo đảm [[src-bcbs-liquidity-principles-2008#^lrm-p01]].
- Stress test định kỳ với kịch bản ngắn hạn và kéo dài, riêng ngân hàng và toàn thị trường, đơn lẻ và kết hợp, để giữ phơi nhiễm trong liquidity risk tolerance [[src-bcbs-liquidity-principles-2008#^lrm-p10]].
- Ban điều hành nên rà soát, cập nhật CFP ít nhất hằng năm để HĐQT phê duyệt [[src-bcbs-liquidity-principles-2008#^lrm-121]].
- Không có chỉ số đơn lẻ nào đo trọn rủi ro thanh khoản; thước đo trong stress làm cơ sở cho hạn mức và chỉ báo sớm [[src-bcbs-liquidity-principles-2008#^lrm-47]]. Dự phóng dòng tiền theo bốn chiều: tài sản và nợ, nhu cầu tiềm tàng ngoại bảng, đồng tiền, đại lý/lưu ký/thanh toán [[src-bcbs-liquidity-principles-2008#^lrm-28]].
- P6–P9: giám sát thanh khoản theo pháp nhân và tính hạn chế chuyển giao [[src-bcbs-liquidity-principles-2008#^lrm-p06]]; đa dạng hoá nguồn và kỳ hạn vốn [[src-bcbs-liquidity-principles-2008#^lrm-p07]]; thanh khoản trong ngày với sáu yếu tố vận hành [[src-bcbs-liquidity-principles-2008#^lrm-80]]; quản lý tài sản bảo đảm, phân biệt bị cầm cố và không bị cầm cố [[src-bcbs-liquidity-principles-2008#^lrm-p09]].
- P12: quy mô đệm tài sản thanh khoản gắn tường minh với nhu cầu thanh khoản trong stress [[src-bcbs-liquidity-principles-2008#^lrm-123]]; đệm là tuyến dự phòng, không phải tuyến đầu [[src-bcbs-liquidity-principles-2008#^lrm-126]].
- HĐQT chịu trách nhiệm cuối cùng nên đặt liquidity risk tolerance [[src-bcbs-liquidity-principles-2008#^lrm-10]]. Chi phí, lợi ích, rủi ro thanh khoản nên được phân bổ tường minh với liquidity charge gán tới trạng thái, danh mục hoặc giao dịch [[src-bcbs-liquidity-principles-2008#^lrm-19]].

Node: [[bcbs-liquidity-principles]] (P1–P12) · cập nhật [[hqla]], [[intraday-liquidity-risk]], [[funding-concentration-risk]], [[asset-encumbrance]], [[liquidity-transfer-restrictions]], [[liquidity-monitoring-metrics]], [[contractual-maturity-mismatch]], [[lcr-by-currency]], [[committed-facilities]], [[non-maturity-deposits]], [[ilaap]], [[liquidity-stress-testing]], [[liquidity-risk-management]], [[risk-appetite]], [[funds-transfer-pricing]], [[new-product-approval]], [[alco]], [[three-lines-of-defence]] · [[contingency-funding-plan]], [[liquidity-transfer-pricing]] (đã áp dụng mục Basel theo duyệt 2026-10-20).

## Basel ↔ VN
Diễn giải: bảng dưới là trạng thái phủ của wiki, không phải claim nguồn.

| Chuẩn Basel | Văn bản VN | Trạng thái |
|---|---|---|
| [[bcbs-irrbb]] | [[tt83-2025]] | Có bảng Basel vs VN trong [[economic-value-of-equity]], [[net-interest-income-sensitivity]] |
| [[bcbs-lcr]] | [[tt50-2026]] | Cột VN đã điền trong [[lcr]], [[hqla]], [[level-1-assets]], [[level-2-assets]], [[net-cash-outflows]] (C2-M5, PL1) |
| [[bcbs-nsfr]] | [[tt50-2026]] | Cột VN đã điền trong [[nsfr]], [[available-stable-funding]], [[required-stable-funding]] (C2-M5, PL2) |
| [[bcbs-liquidity-principles]] | [[tt83-2025]] | Bảng P10 vs Đ48 trong [[liquidity-stress-testing]] |
| SRP30 (Pillar 2) | [[tt83-2025]] | Có bảng Basel vs VN trong [[concentration-risk-management]], [[liquidity-risk-management]], [[firm-wide-risk-management]] |
| LEV | TT14/2025 | Chưa đối chiếu |

## Giao với domain khác
- `alm`: gần như mọi node `basel` cũng gắn `alm`.
- `vn-reg`: xem bảng Basel ↔ VN ở trên và [[domain-vn-reg]].
- `product`: [[interest-rate-swap]], [[interest-rate-cap-floor]], [[swaption]] là công cụ phòng ngừa IRRBB, bảo vệ ΔEVE và ΔNII [[src-bcbs-irrbb-2016#^irrbb-p12-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-5]]. Xem [[domain-product]].

## Lỗ hổng và câu hỏi mở
- `src-bcbs-framework` còn phần lớn unit chưa ingest (vốn, rủi ro tín dụng, thị trường, hoạt động, công bố thông tin; SRP10, SRP20, SRP36 của Pillar 2). `src-bcbs-lev` còn hai unit chưa ingest (`03_meta/sources.yaml`).
- Entity [[bcbs]] vẫn là stub.
- [[leverage-ratio]] có đề xuất cập nhật chờ duyệt: nguồn Lubinska ghi tỷ lệ đòn bẩy là "maximum", ngược với "tối thiểu" trong LEV.
- Wiki chưa có node cho BCBS d578 (2024, cập nhật bộ sốc IRRBB), dù TT83/2025 PL5 dẫn tới văn bản này [[src-tt83-2025-nhnn#^pl5-c2]].

## Thống kê
Diễn giải: thống kê nội bộ wiki, không phải claim nguồn. Đếm mọi node có `basel` trong `domains`, ở bất kỳ vị trí nào, as_of 2026-10-20.

| Type | Số node |
|---|---|
| concept | 44 |
| metric | 34 |
| model | 7 |
| instrument | 4 |
| regulation | 5 |
| entity | 1 |
| source | 8 |
| **Tổng** | **103** (đều draft sau khi hạ bậc 2026-10-20) |
