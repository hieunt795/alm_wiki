---
title: Domain VN Regulator
type: nav
domain: vn-reg
updated: 2026-10-22
as_of: 2026-10-22
---

# Domain `vn-reg`: VN Regulator

## Phạm vi
Luật các TCTD, Nghị định, Thông tư NHNN (`03_meta/taxonomy.md`). Domain này theo dõi sửa đổi, thay thế và hết hiệu lực. Với nghĩa vụ tuân thủ tại VN, quy định NHNN là căn cứ, Basel chỉ là tham chiếu.

## Tóm tắt
Wiki hiện có một văn bản NHNN đã ingest đủ: [[tt83-2025]] về hệ thống kiểm soát nội bộ (20/20 unit, hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]]). Hai thông tư còn lại trong registry là TT50/2026 (giới hạn, tỷ lệ an toàn, gồm LCR/NSFR) và TT14/2025 (tỷ lệ an toàn vốn), chưa ingest unit nào. Vì vậy cột VN trong bảng Basel vs VN của [[lcr]] và [[nsfr]] vẫn là `[cần nguồn]`. Phần IRRBB, ICAAP và quản trị rủi ro thì đã có đối chiếu Basel vs VN.

## Cụm chủ đề

### TT83/2025: khung kiểm soát nội bộ
- TT83/2025 quy định hệ thống kiểm soát nội bộ của ngân hàng thương mại và chi nhánh ngân hàng nước ngoài [[src-tt83-2025-nhnn#^d2-1]]. Hệ thống tổ chức qua ba nhóm hoạt động: hoạt động kiểm soát (Chương II), quản lý rủi ro (Chương III), kiểm toán nội bộ (Chương IV) [[src-tt83-2025-nhnn#^d7-1]].
- Rủi ro trọng yếu gồm tín dụng, thị trường, hoạt động, thanh khoản, tập trung, IRRBB, và rủi ro khác theo quy định nội bộ [[src-tt83-2025-nhnn#^d3-13]].
- Hệ thống kiểm soát nội bộ có 3 tuyến bảo vệ độc lập [[src-tt83-2025-nhnn#^d4-2]].
- Từ 01/07/2026, TT83/2025 bãi bỏ TT13/2018/TT-NHNN, TT40/2018/TT-NHNN và Điều 3 TT09/2024/TT-NHNN [[src-tt83-2025-nhnn#^d74-6]].

Node: [[tt83-2025]] (regulation, draft) · [[three-lines-of-defence]] · [[risk-appetite]] · [[risk-limits]] · [[new-product-approval]] · [[stress-testing]] · [[reverse-stress-testing]] · [[key-risk-indicators]].

### Quản trị và hội đồng
- ALCO là hội đồng giúp việc Tổng giám đốc về quản lý tài sản và nợ phải trả, tham mưu các nội dung tại Đ25.3 [[src-tt83-2025-nhnn#^d6-4b]].
- Hội đồng quản lý vốn tham mưu Tổng giám đốc về ICAAP, họp tối thiểu 6 tháng một lần [[src-tt83-2025-nhnn#^d6-4c]].
- Khẩu vị rủi ro thể hiện bằng các tỷ lệ và chỉ tiêu tại Đ19.2.a [[src-tt83-2025-nhnn#^d3-10]]. Hạn mức rủi ro phải phù hợp với khẩu vị rủi ro [[src-tt83-2025-nhnn#^d20-2]].

Node: [[alco]] · [[bank-corporate-governance]].

### IRRBB theo TT83/2025 (C3-M7, Phụ lục V)
- TT83/2025 định nghĩa IRRBB là rủi ro do lãi suất biến động bất lợi tác động tới trạng thái sổ ngân hàng, ảnh hưởng tới vốn và thu nhập. IRRBB gồm gap risk, basis risk, option risk [[src-tt83-2025-nhnn#^d3-22]].
- Chiến lược IRRBB tối thiểu có nguyên tắc quản lý theo trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile) [[src-tt83-2025-nhnn#^d53-1a1]]. Báo cáo nội bộ IRRBB lập tối thiểu hằng quý [[src-tt83-2025-nhnn#^d55-1]].
- ΔEVE là mức thay đổi giá trị hiện tại ròng giữa dòng tiền vào của tài sản và dòng tiền ra của nợ phải trả nhạy cảm với lãi suất [[src-tt83-2025-nhnn#^pl5-a-0]]. ΔNII là mức thay đổi thu nhập lãi thuần do thay đổi lãi suất [[src-tt83-2025-nhnn#^pl5-b1]].
- Lộ trình: từ 01/07/2026 đến 31/12/2027, ngân hàng được dùng ΔNII hoặc ΔEVE [[src-tt83-2025-nhnn#^d74-4a]], và phải dùng cả hai chậm nhất từ 01/01/2028 [[src-tt83-2025-nhnn#^d74-4b]].
- Sổ ngân hàng gồm repo/reverse repo, phái sinh phòng ngừa, tài sản tài chính dự trữ thanh khoản, và giao dịch còn lại không thuộc sổ kinh doanh [[src-tt83-2025-nhnn#^d3-33]].

Node: [[irrbb-management]] · [[banking-book]] · [[repricing-balance-sheet]] (model) · [[gap-risk]] · [[economic-value-of-equity]] · [[net-interest-income-sensitivity]] · [[standardised-interest-rate-shocks]] · [[irrbb-standardised-framework]] · [[notional-repricing-cash-flow]] · [[behavioural-options]] · [[non-maturity-deposits]].

### ICAAP và vốn kinh tế
- ICAAP thực hiện tối thiểu hằng năm và đột xuất [[src-tt83-2025-nhnn#^d59-1]]. Ngân hàng thương mại được kiểm soát đặc biệt không phải thực hiện ICAAP [[src-tt83-2025-nhnn#^d1-1]].
- Vốn kinh tế là mức vốn ngân hàng tự xác định để bù đắp các rủi ro trọng yếu và bảo đảm tỷ lệ an toàn vốn trong kịch bản bất lợi [[src-tt83-2025-nhnn#^d3-7]].
- Chậm nhất từ 01/01/2028, ngân hàng phải tính $RWA_{IRRBB}$ theo chỉ tiêu ΔEVE [[src-tt83-2025-nhnn#^pl6-1c]].
- Vốn tự có dự kiến không đáp ứng vốn mục tiêu thì kế hoạch vốn phải có phương án tăng vốn [[src-tt83-2025-nhnn#^d61-1]].

Node: [[icaap]] · [[capital-plan]] · [[economic-capital]] · [[rwa-irrbb]] · [[target-capital]] · [[projected-own-funds]] · [[raroc]].

### Thanh khoản
- Rủi ro thanh khoản là rủi ro ngân hàng không thực hiện được nghĩa vụ tài chính khi đến hạn, hoặc thực hiện được nhưng với chi phí cao hơn bình quân thị trường [[src-tt83-2025-nhnn#^d3-20]].
- Ngân hàng phải đưa chi phí thanh khoản và rủi ro thanh khoản vào định giá vốn nội bộ và đánh giá kết quả kinh doanh của hoạt động trọng yếu [[src-tt83-2025-nhnn#^d45-1b]].
- LCR/NSFR VN theo [[tt50-2026]]: áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]]; LCR quy VNĐ riêng lẻ 50% năm thứ nhất, 100% từ 01/10/2033 [[src-tt50-2026-nhnn#^d16-1c]]; NSFR 90%, 95%, 100% từ 01/10/2030 [[src-tt50-2026-nhnn#^d22-2]]. HQLA gồm tài sản cấp 1 (hệ số 100%), cấp 2A (85%), cấp 2B (75% hoặc 50% theo loại) [[src-tt50-2026-nhnn#^pl1-a2]] [[src-tt50-2026-nhnn#^pl1-a3]] [[src-tt50-2026-nhnn#^pl1-a4]]; NHNN có quyền yêu cầu hệ số thấp hơn [[src-tt50-2026-nhnn#^pl1-a2-2]] hoặc không cho tính tài sản vào cấp 2B [[src-tt50-2026-nhnn#^pl1-a4-1]].
- NSFR theo TT50: kỳ hạn RSF tính tới thời điểm muộn nhất, khoản vay được cơ cấu lại thời hạn theo pháp luật tính cả thời gian cơ cấu lại tối đa [[src-tt50-2026-nhnn#^d24-3c]]; RSF tính thêm 10% tổng nợ phái sinh với hệ số 100% [[src-tt50-2026-nhnn#^pl2-b2-19]]; cặp tài sản – nợ phụ thuộc do ngân hàng tự áp ASF, RSF 0%, NHNN có quyền yêu cầu ngừng [[src-tt50-2026-nhnn#^d26-3]].
- Ngân hàng được mua, nắm giữ, đầu tư TPCP, trái phiếu được Chính phủ bảo lãnh tối đa 30% Tổng Nợ phải trả bình quân của tháng liền kề trước [[src-tt50-2026-nhnn#^d28-1]].

Node: [[liquidity-risk-management]] · [[liquidity-stress-testing]] · [[lcr]] · [[nsfr]] · [[structural-liquidity-risk]] · [[loan-to-deposit-ratio]] ([[ldr-total-loans]], [[ldr-total-deposits]]) · [[government-bond-holding-ratio]] ([[government-bond-holdings]], [[average-total-liabilities]]) · [[hqla]] · [[level-1-assets]] · [[level-2-assets]] · [[committed-facilities]] · [[hqla-unwinding-mechanism]] cùng các cấu phần ASF/RSF/HQLA gắn `vn-reg` chờ cột VN.

### Các rủi ro khác và mô hình
Node: [[credit-risk-management]] · [[market-risk-management]] · [[operational-risk-management]] · [[concentration-risk-management]] · [[interbank-cross-shareholding]] · [[real-value-of-charter-capital]] · [[capital-shortfall-remediation]] · [[supervisory-discretion-tt50]] · [[total-credit-outstanding]] · [[model-validation]] · [[model-risk-management]] · [[firm-wide-risk-management]]. Kiểm định mô hình thuộc tuyến bảo vệ thứ hai, tách khỏi tuyến 1 là bên xây dựng và sử dụng mô hình [[src-tt83-2025-nhnn#^d56-7]].

### Node có góc nhìn VN theo TT83 (duyệt đề xuất 2026-10-20)
Diễn giải: danh sách điều hướng, không phải claim nguồn. Các node sau (khi đó canonical, nay đã hạ về draft) đã được thêm mục hoặc dòng VN theo TT83/2025 khi user duyệt các đề xuất tồn đọng: [[basis-risk]], [[gap-risk]], [[option-risk]], [[behavioural-options]], [[non-maturity-deposits]], [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[bcbs-irrbb]], [[csrbb]], [[hqla]], [[funding-concentration-risk]], [[contingency-funding-plan]], [[intraday-liquidity-risk]], [[irrbb-balance-sheet-portfolios]].

## Basel ↔ VN
Diễn giải: bảng dưới là trạng thái phủ của wiki, không phải claim nguồn. Claim Basel vs VN có citation nằm trong node được dẫn.

| Chủ đề | Chuẩn Basel | Văn bản VN | Trạng thái trong wiki |
|---|---|---|---|
| IRRBB | [[bcbs-irrbb]] (d368) | [[tt83-2025]] C3-M7, PL5 | Có bảng Basel vs VN trong [[economic-value-of-equity]], [[net-interest-income-sensitivity]] |
| ICAAP / Pillar 2 | SRP30 ([[srep]]) | [[tt83-2025]] C3-M9, PL3, PL6 | [[icaap]] có mục Basel SRP30; bảng Basel vs VN trong [[concentration-risk-management]], [[liquidity-risk-management]], [[firm-wide-risk-management]] |
| LCR | [[bcbs-lcr]] | [[tt50-2026]] C2-M5, PL1 | Ngưỡng, phạm vi, trần dòng vào, hệ số thanh khoản, hệ số rút tiền, hệ số thu tiền đã điền trong [[lcr]], [[hqla]], [[net-cash-outflows]], [[cash-outflows]], [[cash-inflows]]; bảng Basel vs VN cấp tài sản trong [[level-1-assets]], [[level-2-assets]] |
| NSFR | [[bcbs-nsfr]] | [[tt50-2026]] C2-M5, PL2 | Ngưỡng, phạm vi, hệ số ASF/RSF đã điền trong [[nsfr]], [[available-stable-funding]], [[required-stable-funding]] |
| Công bố thông tin thanh khoản | BCBS 144 P13 (chưa ingest) | [[tt50-2026]] Đ27, PL4 | Nội dung công bố tối thiểu: chính sách, khẩu vị, cơ cấu tổ chức [[src-tt50-2026-nhnn#^pl4-1]]; LCR, NSFR riêng lẻ, LDR, LEV [[src-tt50-2026-nhnn#^pl4-3]] |
| Vốn, đòn bẩy | LEV, RBC | TT14/2025 | Chưa ingest TT14 |

Khác biệt đã ghi nhận ở IRRBB: TT83/2025 chiết khấu theo lãi suất phi rủi ro [[src-tt83-2025-nhnn#^pl5-a3-2]], để ngân hàng tự đo $KAO_{i,c}$ [[src-tt83-2025-nhnn#^pl5-a4]], và C3-M7, PL5 không có phép thử outlier [cần nguồn]. Ở rủi ro tập trung: TT83 Đ50.1 áp cho cấp tín dụng và tự doanh [[src-tt83-2025-nhnn#^d50-1]], còn Basel SRP30.22 liệt kê cả nguồn vốn [[src-bcbs-framework#^srp30-22]].

*Diễn giải:* quan hệ `implements: [[bcbs-irrbb]]` của [[tt83-2025]] là suy luận của wiki, dựa trên việc Phụ lục V dùng cùng cấu trúc, thuật ngữ và tham số với Section IV của d368 (xem [[tt83-2025]]).

## Giao với domain khác
- `alm`: gần như mọi node `vn-reg` cũng gắn `alm`, vì TT83/2025 quy định trực tiếp cách ngân hàng quản trị IRRBB, thanh khoản và vốn. Xem [[domain-alm]].
- `basel`: 70 node gắn cả `basel` và `vn-reg` (Diễn giải: đếm từ frontmatter). Xem [[domain-basel]].
- `product`: [[new-product-approval]] (TT83/2025 Đ21). Xem [[domain-product]].

## Lỗ hổng và câu hỏi mở
- `src-tt50-2026-nhnn` đã ingest 7/14 unit (C1, C2-M2, C2-M4, C2-M5, PL1, PL2, PL4); `src-tt14-2025-nhnn` chưa ingest unit nào. Unit TT50 còn lại có giá trị ALM: `C2-M3`, `PL3`.
- Wiki chưa có node cho Luật các TCTD, các văn bản bị TT83/2025 bãi bỏ (TT13/2018, TT40/2018), quy định dự trữ bắt buộc, bảo hiểm tiền gửi [cần nguồn].
- Câu hỏi mở trong [[overview]], xem [[lcr]] và [[nsfr]]: TT50/2026 nội luật hoá LCR/NSFR của Basel tới mức nào, tham số nào khác Basel?
- Câu hỏi mở trong [[overview]], xem [[retail-deposit-stability]]: bảo hiểm tiền gửi VN có đáp ứng tiêu chí "effective deposit insurance scheme" không?

## Thống kê
Diễn giải: thống kê nội bộ wiki, không phải claim nguồn. Đếm mọi node có `vn-reg` trong `domains`, ở bất kỳ vị trí nào, as_of 2026-10-22.

| Type | Số node |
|---|---|
| concept | 43 |
| metric | 41 |
| model | 2 |
| regulation | 2 |
| source | 2 |
| synthesis | 10 |
| **Tổng** | **100** (đều draft) |
