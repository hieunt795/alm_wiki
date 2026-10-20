---
title: Domain Product
type: nav
domain: product
updated: 2026-10-20
as_of: 2026-10-20
---

# Domain `product`: Financial Product

## Phạm vi
Fixed income, swap, derivatives, sản phẩm tiền gửi/cho vay (`03_meta/taxonomy.md`).

## Tóm tắt
*Diễn giải:* wiki nhìn sản phẩm tài chính từ phía ALM: công cụ nào dùng để phòng ngừa IRRBB, sản phẩm khách hàng nào sinh quyền chọn hành vi, và sản phẩm được định giá nội bộ qua FTP ra sao. Phần lớn claim đến từ Choudhry (T4), BCBS d368 (T2) và tài liệu tư vấn FTP (T4). Wiki chưa có node nào về fixed income như một thị trường (trái phiếu, đường cong lợi suất, định giá), vì các sách fixed income đã đăng ký nhưng chưa ingest.

## Cụm chủ đề

### Phái sinh lãi suất dùng để phòng ngừa
- IRS trao đổi dòng tiền lãi suất tương lai trên một notional, không chuyển giao gốc [[src-bcbs-irrbb-2016#^irrbb-u06-4]]. Payer swap rút ngắn thời lượng tài sản, phòng ngừa tổn thất $\Delta\text{EVE}$ khi lãi suất tăng [[src-bcbs-irrbb-2016#^irrbb-u05-8]].
- OIS trả cố định đổi lấy lãi suất qua đêm. Swap thông thường trả cố định đổi lấy khoản thả nổi hằng quý hoặc nửa năm [[src-choudhry-principles-banking#^choudhry-hedge-15]].
- Cross-currency swap có trao đổi gốc, khác với IRS [[src-choudhry-principles-banking#^choudhry-fxs-2]].
- FRA là hợp đồng ngoại bảng: bên mua vay danh nghĩa, bên bán cho vay danh nghĩa ở lãi suất cố định cho một kỳ bắt đầu trong tương lai [[src-choudhry-principles-banking#^choudhry-hedge-8]]. Short-term interest-rate futures cũng là công cụ ngoại bảng, không có khoản tiền thực tế được gửi [[src-choudhry-principles-banking#^choudhry-hedge-5]].
- Cap, floor và swaption là quyền chọn lãi suất. Người nắm giữ thực thi khi quyền chọn in-the-money [[src-bcbs-irrbb-2016#^irrbb-u02-2]]. Quyền chọn có thể là phái sinh độc lập hoặc nhúng trong sản phẩm tín dụng và tiền gửi [[src-bcbs-irrbb-2016#^irrbb-u05-3]].
- PV01 là thay đổi giá trị hiện tại khi đường lãi suất của một đồng tiền dịch 1 bp [[src-lubinska-alm-optimisation#^lubinska-u02-43]].

Node: [[interest-rate-swap]] (canonical) · [[overnight-index-swap]] (draft) · [[cross-currency-swap]] (draft) · [[forward-rate-agreement]] (draft) · [[interest-rate-futures]] (draft) · [[interest-rate-cap-floor]] (canonical) · [[swaption]] (canonical) · [[pv01]] (draft) · [[key-rate-duration]] (model, canonical).

### Tiền gửi, cho vay và quyền chọn hành vi
- NMD là khoản nợ mà người gửi có quyền rút bất kỳ lúc nào, không có ngày đáo hạn hay kỳ tái định giá theo hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u06-6]]. Giả định NMD là nợ qua đêm hay nợ dài hạn tác động lên cả $\Delta\text{EVE}$ và $\Delta\text{NII}$ [[src-bcbs-irrbb-2016#^irrbb-p05-2]].
- Quyền chọn hành vi là điều khoản nhúng trong hợp đồng, cho khách hàng quyền thay đổi thời điểm và quy mô dòng tiền hoàn trả hoặc rút tiền gửi [[src-tata-bank-alm#^tata-opt-1]]. Theo Basel, quyền chọn của khách hàng wholesale làm thay đổi dòng tiền phải xếp vào nhóm quyền chọn tự động [[src-bcbs-irrbb-2016#^irrbb-u05-7]].
- Theo Choudhry, lãi suất cho vay đặt bằng spread trên chi phí funding. Spread là hàm của RoE mục tiêu, credit spread bù tổn thất dự kiến và spread bù chi phí vận hành [[src-choudhry-principles-banking#^choudhry-lp-5]].

Node: [[non-maturity-deposits]] (canonical) · [[behavioural-options]] (canonical) · [[option-risk]] (canonical) · [[basis-risk]] (canonical) · [[loan-pricing]] (draft) · [[effective-interest-rate]] (draft) · [[expected-credit-loss]] (draft) · [[net-interest-margin]] (draft).

### FTP: định giá sản phẩm nội bộ
- FTP là hệ thống giá điều chuyển nội bộ giữa Treasury và đơn vị kinh doanh, thanh toán trên cơ sở trùng khớp kỳ hạn theo một đường cong FTP [[src-choudhry-principles-banking#^choudhry-ftp-6]].
- Theo Choudhry, FTP không phải phòng ngừa rủi ro ra bên ngoài, cũng không phải điều chuyển vốn nội bộ. FTP là chuyển giao rủi ro nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-10]].

Node: [[funds-transfer-pricing]] · [[liquidity-transfer-pricing]] (canonical) · [[internal-risk-transfer]] (canonical) · [[cost-of-funds]] · [[ftp-pricing-methodology]] (model) · [[ftp-transmission-mechanism]]. Synthesis FTP (đều canonical trừ khi ghi khác): [[ftp-nature-and-balance-sheet-management]], [[ftp-risk-and-cost-components]], [[ftp-curve-construction-methodology]], [[ftp-portfolio-and-bucket-allocation]], [[ftp-cost-benefit-allocation-principles]], [[ftp-final-rate-determination]], [[ftp-economic-cost-and-incentive-validation]], [[ftp-balance-sheet-optimization]] (draft). Chi tiết ở [[domain-alm]].

### Funding có bảo đảm, chứng khoán hoá và vốn lai
- Securitisation chuyển tài sản có dòng tiền dự đoán được thành chứng khoán giao dịch được, thường qua một SPV [[src-choudhry-principles-banking#^choudhry-sec-1]].
- Tài sản dùng làm tài sản bảo đảm trong repo, hoặc làm pool cho ABS và covered bond, đều bị encumber [[src-choudhry-principles-banking#^choudhry-enc-2]]. Choudhry coi asset encumbrance là chỉ số "gone concern" [[src-choudhry-principles-banking#^choudhry-enc-6]].
- CoCo bond tự chuyển thành cổ phần khi tỷ lệ Tier 1 của tổ chức phát hành giảm xuống một mức định trước [[src-choudhry-principles-banking#^choudhry-coco-4]].

Node: [[securitisation]] · [[asset-encumbrance]] · [[contingent-convertible-bond]] · [[secured-funding]] · [[rsf-securities-financing-and-encumbrance]] · [[derivatives-and-contingent-outflows]] · [[rsf-derivatives-and-off-balance-sheet]] (đều draft).

### Kế toán và phòng ngừa cấu trúc
- Hedge accounting xử lý vấn đề khoản vay hoặc tiền gửi không được fair value hằng ngày, trong khi phái sinh phòng ngừa thì có, khiến P&L biến động [[src-choudhry-principles-banking#^choudhry-hacc-1]].
- Structural hedging phòng ngừa theo phần ròng tài sản trừ nợ: ngân hàng tận dụng các cặp tài sản – nợ đã tự phòng ngừa cho nhau và chỉ ra thị trường cho phần ròng còn lại [[src-choudhry-principles-banking#^choudhry-cs-17]].

Node: [[hedge-accounting]] · [[structural-hedging]] · [[valuation-governance]] (đều draft).

- Theo Basel SRP30, khi không có giá minh bạch từ thị trường thanh khoản, định giá phải dựa vào mô hình, giá đại diện và phán đoán chuyên gia [[src-bcbs-framework#^srp30-38]].

## Giao với domain khác
- `alm`: gần như mọi node `product` cũng gắn `alm`. Sản phẩm là đối tượng, ALM là góc nhìn quản trị. Xem [[domain-alm]].
- `basel`: d368 quy định cách xử lý quyền chọn tự động (KAO) và quyền chọn hành vi trong đo IRRBB [[src-bcbs-irrbb-2016#^irrbb-u05-7]]. Xem [[irrbb-standardised-framework]], [[domain-basel]].
- `vn-reg`: [[new-product-approval]] theo TT83/2025 Đ21. Xem [[domain-vn-reg]].
- `macro`: sàn 0% trên tiền gửi khi lãi suất âm [[src-tata-bank-alm#^tata-neg-2]], xem [[negative-interest-rates]] và [[domain-macro]].

## Lỗ hổng và câu hỏi mở
- Nguồn `product` đã đăng ký nhưng chưa ingest: `src-choudhry-fixed-income-markets`, `src-choudhry-yield-curve`, `col-during-fixed-income` (`03_meta/sources.yaml`).
- Chưa có node về trái phiếu (chính phủ, doanh nghiệp), repo như sản phẩm, FX swap, sản phẩm tiền gửi/cho vay đặc thù VN [cần nguồn].
- Phần lớn instrument viết theo thị trường UK/EU (SONIA, €STR, short sterling). Thị trường phái sinh lãi suất VN chưa có trong wiki [cần nguồn].

## Thống kê
Diễn giải: thống kê nội bộ wiki, không phải claim nguồn. Đếm mọi node có `product` trong `domains`, ở bất kỳ vị trí nào, as_of 2026-10-20.

| Type | Số node |
|---|---|
| concept | 15 |
| instrument | 8 |
| metric | 9 |
| model | 2 |
| synthesis | 11 |
| source | 2 |
| **Tổng** | **47** (canonical 18, draft 29) |
