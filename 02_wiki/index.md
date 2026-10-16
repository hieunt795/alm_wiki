---
title: Index
type: nav
updated: 2026-10-16
---

# Index

Catalog mọi node trong wiki. LLM đọc file này **đầu tiên** khi query và cập nhật nó sau mỗi lần ingest.
Mỗi dòng có dạng `[[id]] — tóm tắt một dòng · domains · maturity`.

## Metrics
- [[lcr]] — HQLA / total net cash outflows 30 ngày stress, ≥ 100%; bảng Basel vs VN (cột VN chờ TT50) · alm, basel, vn-reg · draft
- [[hqla]] — tử số LCR: tài sản thanh khoản cao unencumbered, phân cấp Level 1 và Level 2 (trần 40%), công thức unwinding và yêu cầu vận hành · alm, basel, vn-reg · canonical
- [[level-1-assets]] — thành phần cao nhất của HQLA: tiền mặt, dự trữ NHTW, nợ chính phủ 0% RW, không trần, haircut 0% · alm, basel, vn-reg · draft
- [[level-2-assets]] — thành phần bổ sung của HQLA: Level 2A (haircut 15%), Level 2B (haircut 25–50%, trần 15%), trần tổng 40% · alm, basel, vn-reg · draft
- [[net-cash-outflows]] — mẫu số LCR: dòng ra − min(dòng vào, 75% dòng ra); bảng run-off/inflow theo nhóm · alm, basel · draft
- [[cash-outflows]] — tổng dòng tiền ra kỳ vọng 30 ngày: cấu trúc 5 trụ cột (bán lẻ, bán buôn không BĐ, repo, phái sinh/add-on, cam kết ngoại bảng) và ma trận tham số Basel · alm, basel · draft
- [[retail-deposit-stability]] — stable (5%/3%) vs less stable (≥ 10%); tiêu chí bảo hiểm tiền gửi hiệu quả; tiền gửi có kỳ hạn > 30 ngày · alm, basel · draft
- [[unsecured-wholesale-funding]] — nguồn vốn từ pháp nhân không bảo đảm: SME như bán lẻ, DN 40%/20%, tổ chức tài chính 100% · alm, basel · draft
- [[operational-deposits]] — tiền gửi clearing/custody/cash management: 25%, điều kiện phụ thuộc thực chất, loại trừ excess balance · alm, basel · draft
- [[secured-funding]] — repo/collateral swap: dòng ra theo tài sản bảo đảm L1 0% → 100% · alm, basel, product · draft
- [[derivatives-and-contingent-outflows]] — nhu cầu thanh khoản phái sinh (bù trừ song phương, ITM options, 3-notch downgrade, non-L1 add-on +20%, look-back 24M), ABCP/conduits và nghĩa vụ tiềm tàng · alm, basel, product · draft
- [[cash-inflows]] — dòng tiền vào theo hợp đồng: trần 75%, phân loại theo đối tác (50% bán lẻ/DN, 100% tài chính), không tính dòng vào tiềm tàng · alm, basel · draft
- [[nsfr]] — ASF / RSF 1 năm, ≥ 100%; bảng Basel vs VN (cột VN chờ TT50) · alm, basel, vn-reg · draft
- [[available-stable-funding]] — tử số NSFR: cấu trúc 5 tầng hệ số ASF (100%, 95%, 90%, 50%, 0%), kỳ hạn nợ và quyền chọn call · alm, basel, vn-reg · canonical
- [[asf-capital-and-long-term-liabilities]] — cấu phần vốn tự có và nợ $\ge 1$ năm trong NSFR (ASF 100%), xử lý quyền chọn call option và cắt lát dòng tiền · alm, basel, vn-reg · draft
- [[asf-retail-and-small-business-deposits]] — tiền gửi bán lẻ và SME trong NSFR: stable (95%) vs less stable (90%), tiền gửi không kỳ hạn và giả định bám dính hành vi · alm, basel, vn-reg · draft
- [[asf-wholesale-and-operational-funding]] — nguồn vốn bán buôn và tiền gửi operational: doanh nghiệp phi tài chính 50%, operational deposits 50%, vốn liên ngân hàng $< 6$M bị triệt tiêu về 0% · alm, basel, vn-reg · draft
- [[required-stable-funding]] — mẫu số NSFR: cấu trúc 8 tầng hệ số RSF (0% đến 100%), cầm cố tài sản và cam kết ngoại bảng 5% · alm, basel, vn-reg · canonical
- [[rsf-hqla-and-central-bank-reserves]] — tài sản thanh khoản cao và dự trữ NHTW trong NSFR: tiền mặt/dự trữ 0%, Level 1 5%, Level 2A 15%, Level 2B 50%, miễn trừ trần và yêu cầu vận hành LCR · alm, basel, vn-reg · draft
- [[rsf-loans-and-credit-exposures]] — danh mục cho vay khách hàng và tín dụng trong NSFR: thế chấp nhà ở 65%, cho vay thông thường 85%, nợ ngắn hạn 50% (roll-over), NPL 100% · alm, basel, vn-reg · draft
- [[rsf-securities-financing-and-encumbrance]] — tài trợ có bảo đảm và quản trị cầm cố tài sản: repo/reverse repo, khung thời gian cầm cố $\ge 1$Y 100%, 6M–1Y HQLA 50%, nguyên tắc báo cáo gộp · alm, basel, product · draft
- [[rsf-derivatives-and-off-balance-sheet]] — phái sinh và cam kết ngoại bảng trong NSFR: ký quỹ ban đầu 85%, tài sản phái sinh ròng 100%, add-on nợ phái sinh gộp 5%–20%, cam kết ngoại bảng 5% · alm, basel, product · draft
- [[economic-value-of-equity]] — biến động giá trị hiện tại thuần của toàn bộ dòng tiền sổ ngân hàng dưới 6 kịch bản sốc lãi suất chuẩn hoá (run-off horizon) · alm, basel · canonical
- [[net-interest-income-sensitivity]] — độ nhạy thu nhập lãi thuần 12 tháng liên tục dưới các kịch bản sốc lãi suất (constant/dynamic balance sheet) · alm, basel · canonical
- [[outlier-bank-test]] — phép thử ngoại lai giám sát Trụ cột 2: ngưỡng cảnh báo max ΔEVE > 15% Vốn cấp 1 (Tier 1 Capital) và các biện pháp can thiệp bắt buộc · basel, alm · canonical

- [[lcr-by-currency]] — tỷ lệ LCR theo từng ngoại tệ trọng yếu (≥ 5% nợ), đo lường rủi ro lệch pha cơ cấu tiền tệ và nguy cơ đóng băng FX Swap · alm, basel · canonical
- [[contractual-maturity-mismatch]] — thang chênh lệch kỳ hạn theo hợp đồng (Maturity Ladder) 13 dải kỳ hạn, phân tích khoảng trống thanh khoản thuần túy pháp lý không rollover · alm, basel · canonical
- [[available-unencumbered-assets]] — tài sản không bị phong tỏa khả dụng làm đệm thanh khoản thứ cấp: 2 kênh huy động (Repo và NHTW) và 2 tầng haircut · alm, basel · canonical
- [[leverage-ratio]] — Vốn cấp 1 / Tổng quy mô phơi nhiễm (Exposure Measure) ≥ 3.0%; chốt chặn phi rủi ro Trụ cột 1 và đệm G-SIB · basel, alm, vn-reg · canonical
- [[leverage-exposure-measure]] — quy mô phơi nhiễm tỷ lệ đòn bẩy LEV30: giá trị tài sản nội bảng gộp, SA-CCR phái sinh α=1.4, SFTs và hệ số CCF ngoại bảng (10%–100%) · basel, alm · canonical

## Concepts
- [[run-off-rate]] — tỷ lệ giả định rút/không tái tục trong stress 30 ngày; mức sàn Basel theo loại nguồn vốn · alm, basel · draft
- [[committed-facilities]] — drawdown rate theo đối tượng và loại hạn mức (5% → 100%) · alm, basel · draft
- [[hqla-unwinding-mechanism]] — cơ chế hoàn trả giả định các giao dịch repo/swap ngắn hạn ≤ 30 ngày để tính trần 40% và 15% của HQLA, triệt tiêu window-dressing · alm, basel · draft
- [[liquidity-transfer-restrictions]] — rào cản chuyển giao thanh khoản (ring-fencing) trong tập đoàn: loại trừ HQLA thặng dư không thể điều chuyển khỏi LCR hợp nhất · alm, basel, vn-reg · draft
- [[alternative-liquidity-approaches]] — phương pháp thanh khoản thay thế (ALA): Option 1 (CLF có phí), Option 2 (HQLA ngoại tệ), Option 3 (Level 2A vượt trần) cho quốc gia thiếu Level 1 nội tệ · alm, basel, vn-reg · draft
- [[interdependent-assets-and-liabilities]] — cơ chế tài sản và nợ phụ thuộc lẫn nhau: ASF = 0% và RSF = 0% theo 4 tiêu chí khắt khe · alm, basel, vn-reg · draft
- [[lcr-nsfr-interlinkages]] — các thành phần liên kết và 7 kênh truyền dẫn tương tác giữa LCR và NSFR trên bảng cân đối kế toán · alm, basel · draft
- [[liquidity-monitoring-metrics]] — khuôn khổ bộ chỉ số giám sát thanh khoản bổ trợ Basel SRP50: 5 công cụ cốt lõi và quản trị thanh khoản trong ngày · basel, alm · canonical
- [[funding-concentration-risk]] — rủi ro tập trung nguồn vốn bán buôn theo chuẩn SRP50: ngưỡng đối tác (>1%), sản phẩm/công cụ (>1%) và 5 dải kỳ hạn · alm, basel · canonical
- [[intraday-liquidity-risk]] — quản trị rủi ro thanh khoản trong ngày theo BCBS SRP50 / BCBS 248: 7 công cụ giám sát, tỷ lệ thông lượng throughput và 4 kịch bản stress · alm, basel · canonical
- [[gap-risk]] — rủi ro chênh lệch cấu trúc kỳ hạn và thời điểm tái định giá lãi suất: dịch chuyển song song vs phi song song/xoay trục đường cong · alm, basel · canonical
- [[basis-risk]] — rủi ro chênh lệch giữa các chỉ số lãi suất tham chiếu khác nhau của các công cụ có cùng kỳ hạn tái định giá · alm, product, basel · canonical
- [[option-risk]] — rủi ro quyền chọn tự động (caps/floors/swaptions - add-on KAO) và quyền chọn hành vi (prepayment CPR, early redemption TDRR, NMD core deposits) · alm, product, basel · canonical
- [[non-maturity-deposits]] — mô hình hoá tiền gửi không kỳ hạn trong IRRBB: phân tách tiền gửi lõi (core) và phi lõi, trần Table 2 và kỹ thuật Replicating Portfolio · alm, product, basel · canonical
- [[behavioural-options]] — quyền chọn hành vi trong IRRBB: rủi ro trả nợ trước hạn (prepayment CPR, hệ số $\gamma_i$), rút tiền gửi có kỳ hạn sớm (TDRR, hệ số $u_i$) và tính lồi âm · alm, product, basel · canonical
- [[standardised-interest-rate-shocks]] — 6 kịch bản sốc lãi suất chuẩn hoá Basel: sốc song song, sốc xoay trục đường cong (Steepener/Flattener), sàn 100 bps và trần biên độ · alm, basel · canonical
- [[csrbb]] — rủi ro chênh lệch tín dụng trên sổ ngân hàng: phân định ranh giới với IRRBB, biến động market credit spread và liquidity spread · alm, basel · canonical
- [[irrbb-balance-sheet-portfolios]] — cấu phần danh mục bảng cân đối chịu rủi ro IRRBB: phạm vi bao gồm/loại trừ (CET1, cổ phiếu, TSCĐ), 3 nhóm vị thế chuẩn hoá, phân loại kế toán HTM/AFS/FVTPL và quy tắc slotting 19 dải kỳ hạn · alm, basel · canonical
- [[contingency-funding-plan]] — kế hoạch tài trợ dự phòng (CFP): quản trị khủng hoảng thanh khoản, chỉ báo sớm EWIs 3 cấp độ (Green/Amber/Red), menu hành động vốn khẩn cấp và cơ chế giảm đệm LAB · alm · canonical
- [[liquidity-transfer-pricing]] — định giá điều chuyển thanh khoản nội bộ (Liquidity FTP): cấu trúc lãi suất 4 tầng (Base, TLP, Buffer carry, Regulatory), nguyên tắc Matched-Maturity và Marginality · alm, product · canonical
- [[ftp-transmission-mechanism]] — cơ chế truyền dẫn FTP đến các yếu tố rủi ro: vai trò hệ thống điều khiển trung tâm (unified control mechanism), 3 kênh truyền dẫn (Thanh khoản LCR/NSFR, Lãi suất IRRBB, Tín dụng & Vốn RAROC) và vòng phản hồi cân bằng động · alm, product · draft
- [[internal-risk-transfer]] — cơ chế chuyển giao rủi ro nội bộ qua FTP: mô hình hai lớp hợp đồng, ma trận phân định rủi ro BU vs CFU, cơ chế hồ điều tiết trung tâm (netting & pooling), bóc tách 3 nguồn lợi nhuận NIM và động lực bảo hiểm trong kịch bản sốc lãi suất · alm, product · canonical

## Instruments
- [[interest-rate-swap]] — IRS: hợp đồng hoán đổi lãi suất cố định/thả nổi (Payer/Receiver), OIS, Basis swap, công cụ phòng ngừa chênh lệch thời lượng và DV01 · product, alm, basel · canonical
- [[interest-rate-cap-floor]] — Caps, Floors, Collars: quyền chọn lãi suất tự động, định giá Black-76, phòng ngừa rủi ro phi tuyến và phụ trội vốn KAO trong Basel d368 · product, alm, basel · canonical
- [[swaption]] — quyền chọn hoán đổi lãi suất (Payer/Receiver Swaption, kiểu Bermudan): công cụ phòng ngừa rủi ro trả nợ trước hạn (prepayment) và rủi ro pipeline tín dụng thế chấp · product, alm, basel · canonical

## Models
- [[duration-gap-model]] — mô hình chênh lệch thời lượng bảng cân đối (DGAP): Macaulay, Modified, Effective Duration, phương trình biến động vốn và hiệu chỉnh tính lồi · alm, basel · canonical
- [[key-rate-duration]] — thời lượng lãi suất từng kỳ hạn (KRD): phân rã độ nhạy đường cong trên 19 dải kỳ hạn Basel, nhận diện rủi ro xoay trục (Steepener/Flattener) và cánh bướm · alm, basel, product · canonical
- [[replicating-portfolio-model]] — mô hình danh mục tái lập NMDs: kỹ thuật lát cắt bình quân trượt (moving average tranches), hồi quy đồng tích hợp, tối ưu hoá NIM và trần Table 2 Basel · alm, basel · canonical
- [[economic-value-at-risk]] — giá trị kinh tế chịu rủi ro (EVaR): lượng hoá mức sụt giảm EVE tối đa qua 3 phương pháp (Delta-normal, mô phỏng lịch sử, Monte Carlo) và giới hạn rủi ro đuôi · alm, basel · canonical
- [[ftp-pricing-methodology]] — phương pháp luận định giá điều chuyển vốn nội bộ (FTP): kiến trúc hai chiều VOF và COF, chi phí dự trữ bắt buộc, bảo hiểm tiền gửi BHTG, phần bù đệm thanh khoản, Term Liquidity Premium (TLP), đường cong hoàn trả CASA và định giá quyền chọn ẩn (Prepayment/TDRR) · alm, product · draft
- [[irrbb-standardised-framework]] — khuôn khổ chuẩn hoá đo lường $\Delta\text{EVE}$ (Section IV d368): quy trình 5 giai đoạn, 19 dải kỳ hạn, add-on quyền chọn tự động $\text{KAO}$ và tổng hợp đa tiền tệ · alm, basel · canonical

## Regulations
- [[bcbs-lcr]] — chuẩn mực LCR của BCBS (Basel Framework, effective 15/12/2019) · basel, alm · draft
- [[bcbs-nsfr]] — chuẩn mực NSFR của BCBS (Basel Framework, effective 15/12/2019) · basel, alm · draft
- [[bcbs-irrbb]] — chuẩn mực quản trị và giám sát rủi ro lãi suất trên sổ ngân hàng của BCBS (Standards d368, effective 2018) · basel, alm · canonical

## Entities
- [[bcbs]] — Basel Committee on Banking Supervision; *stub* · basel · draft

## Syntheses
- [[hqla-decomposition-and-tradeoffs]] — phân tích tổng hợp các thành phần HQLA, thuật toán unwinding và trần kép, cùng các đánh đổi chiến lược ALM Treasury (carry, IRRBB, NSFR, Leverage Ratio) · alm, basel · draft
- [[lcr-net-cash-outflows-mechanics]] — phân rã chuyên sâu mẫu số LCR (TNCO), các giả định hành vi bất đối xứng (franchise preservation, operational lock-in), trần 75% và chiến lược ALM Treasury · alm, basel · draft
- [[lcr-economic-significance-and-alm-governance]] — ý nghĩa kinh tế, nghịch lý sử dụng đệm HQLA (buffer usability paradox) và phương pháp quản trị LCR của ALM Treasury (ILAAP, hạn mức traffic-light, Liquidity FTP, LCR ngoại tệ, CFP, SRP50) · alm, basel · draft
- [[nsfr-structural-liquidity-and-alm-strategy]] — thanh khoản cấu trúc NSFR, ma trận tương tác với LCR, các xung đột kỹ thuật và chiến lược tối ưu hóa bảng cân đối ALM Treasury · alm, basel · draft
- [[nsfr-alm-governance-strategy-and-risks]] — phương pháp quản trị tác nghiệp, cơ chế điều hành ALCO, hệ thống hạn mức 3 tầng, Term Liquidity FTP, 4 chiến lược tối ưu hóa và 4 rủi ro trọng yếu đối với NSFR tại Treasury · alm, basel · draft
- [[integrated-alm-liquidity-strategy]] — chiến lược quản trị thanh khoản và bảng cân đối kế toán tổng hợp LCR – NSFR: mô hình tối ưu hóa tuyến tính, cơ chế định giá FTP tích hợp, thác phân bổ tài sản bảo đảm và ma trận điều hành ALCO · alm, basel · draft
- [[irrbb-alm-governance-strategy-and-tradeoffs]] — chiến lược quản trị ALM toàn diện đối với IRRBB: giải quyết mâu thuẫn EVE vs NII, kiểm soát cạm bẫy thời lượng HQLA, hạn mức ALCO 4 tầng và cơ chế IRRBB FTP · alm, basel · canonical
- [[irrbb-five-tier-architecture]] — bản thiết kế kiến trúc toàn diện 5 tầng của IRRBB: từ 5 thành phần lãi suất (T1), hai lăng kính EVE/NII (T2), mô hình định lượng DGAP/KRD/Replicating (T3), công cụ phái sinh IRS/Caps/Swaptions (T4) đến cơ chế truyền dẫn FTP (T5) và 4 thách thức thực chiến · alm, basel · canonical
- [[synthetic-balance-sheet-liquidity-risk]] — mô hình bảng cân đối kế toán tổng hợp quản trị rủi ro thanh khoản LCR – NSFR: quy hoạch tuyến tính đa ràng buộc, thiết kế chi tiết TSN - TSC quy mô 100k tỷ, kiểm chứng giải tích LCR 114% và NSFR 115%, cùng 4 quy luật cân đối động lực học · alm, basel, product · canonical
- [[basel-liquidity-monitoring-framework]] — kiến trúc giám sát thanh khoản đa tầng Basel III: tích hợp chuẩn mực định lượng bắt buộc LCR – NSFR với Bộ 5 công cụ giám sát SRP50 (thang kỳ hạn hợp đồng, tập trung nguồn vốn, tài sản sạch unencumbered, LCR ngoại tệ, thanh khoản trong ngày) · alm, basel · canonical
- [[practical-alm-liquidity-governance]] — khung điều hành quản trị thanh khoản thực chiến: tích hợp Synthetic Balance Sheet, quy định pháp lệnh (LCR/NSFR/LEV/SRP50), Liquidity FTP và Kế hoạch tài trợ dự phòng CFP · alm, basel · canonical
- [[ftp-balance-sheet-optimization]] — hệ thống FTP: động cơ điều khiển và tối ưu hóa bảng cân đối ALM toàn diện, giải bài toán tối ưu NII/RAROC dưới đa ràng buộc pháp định (LCR, NSFR, LEV, CAR, IRRBB) và quy trình điều hành của ALCO · alm, product · draft
- [[ftp-nature-and-balance-sheet-management]] — bản chất, mục tiêu của FTP và các vấn đề cốt tử giải quyết trong quản trị bảng cân đối: ranh giới giữa thương quyền khách hàng và chuyển đổi kỳ hạn, 4 mục tiêu chiến lược và 5 vấn nạn ALM kinh điển được hóa giải · alm, product · canonical
- [[ftp-risk-and-cost-components]] — các cấu phần rủi ro và chi phí trong định giá FTP: bóc tách 4 trụ cột Funding Cost, Liquidity Risk (TLP, đệm HQLA, DTBB, BHTG), IRRBB (Gap, Basis, Yield Curve) và Optionality (Prepayment, Early Withdrawal, Core CASA, Caps/Floors) · alm, product · canonical
- [[ftp-curve-construction-methodology]] — phương pháp luận xây dựng đường cong FTP theo không gian 3 chiều: cấu trúc kỳ hạn chuẩn O/N–10Y và nội suy tuyến tính, tách biệt độc lập theo đồng tiền (VND vs USD SOFR/IRS/FX Swap CIP) và ma trận định giá chi tiết theo loại sản phẩm (VOF huy động, COF cho vay, WAL trả định kỳ, TLP thả nổi, CASA phi kỳ hạn, cam kết ngoại bảng) · alm, product · canonical
- [[ftp-portfolio-and-bucket-allocation]] — phương pháp phân bổ giao dịch và sản phẩm vào các danh mục và thang kỳ hạn FTP: phân định Banking Book TT1 vs Trading Book TT2, danh mục loại trừ HQLA/VCSH, 7 tiêu chí kỹ trị phân bổ bucket (cố định vs thả nổi TLP, WAL trả định kỳ, CASA Core/Non-core, đồng tiền, ưu đãi, trạng thái tín dụng, ngoại bảng/quyền chọn) và ma trận quy tắc ánh xạ chi tiết · alm, product · canonical
- [[ftp-cost-benefit-allocation-principles]] — nguyên tắc phân bổ chi phí và lợi ích của từng FTP portfolio cho các đơn vị kinh doanh và sản phẩm: bóc tách 3 khối biên lợi nhuận (biên thương mại huy động, biên thương mại tín dụng, biên Treasury mismatch), 6 nguyên tắc kỹ trị cốt lõi, cơ chế phân bổ đệm HQLA negative carry, phí cam kết ngoại bảng và khung báo cáo NII/NIM 5 cấp độ · alm, product · canonical
- [[ftp-final-rate-determination]] — xác định mức lãi suất FTP rate cuối cùng cho từng giao dịch và sản phẩm: tích hợp 4 chiều (kỳ hạn hợp đồng/WAL, repricing profile cố định/thả nổi/ưu đãi, đặc tính thanh khoản TLP/HQLA/DTBB/BHTG/ngoại bảng, quyền chọn ẩn prepayment/CASA/early withdrawal/caps/floors) và công thức tính chi tiết 8 nhóm sản phẩm · alm, product · canonical
- [[ftp-economic-cost-and-incentive-validation]] — kiểm tra tính phản ánh economic cost và cơ chế định hướng incentive của hệ thống FTP: khung kiểm định kép (marginality, phân rã chi phí, Treasury residual P&L, backtest hành vi, quy tắc PRA phân tách True Cost vs Management Overlays, miễn nhiễm biên thương mại, chống gaming và quản trị ALCO 3 tuyến phòng thủ) · alm, product · canonical

## Sources
- [[src-bcbs-lcr]] — BCBS LCR (T2, final); hoàn thành 8/8 units (toàn bộ chuẩn mực Basel LCR) · basel, alm
- [[src-bcbs-nsfr]] — BCBS NSFR (T2, final); hoàn thành 5/5 units (toàn bộ chuẩn mực Basel NSFR) · basel, alm
- [[src-bcbs-irrbb-2016]] — BCBS Standards d368 (T2, final); hoàn thành 8/8 units (toàn bộ chuẩn mực IRRBB 2016) · basel, alm
- [[src-bcbs-framework]] — The Basel Framework Consolidated (T2, final); hoàn thành unit SRP50 (Liquidity Monitoring Metrics) · basel, alm
- [[src-bcbs-lev]] — BCBS LEV Leverage Ratio (T2, final); hoàn thành 4 units (LEV10, LEV20, LEV30, LEV40) · basel, alm
- [[src-choudhry-principles-banking]] — The Principles of Banking — Moorad Choudhry (T4, final); hoàn thành 2 units (u16 CFP, u17 FTP & Liquidity FTP) · alm, product
- [[src-lubinska-alm-optimisation]] — Asset Liability Management Optimisation — Beata Lubinska (T4, final); hoàn thành unit u03 (Chapter 2: FTP, Target Operating Model, Incentive Overlays, PRA Review) · alm, product
- [[src-ftp-transmission-analysis]] — Cơ chế truyền dẫn FTP đến các risk factors — Lubinska ALM Optimisation framework (T5, draft); hoàn thành 1/1 unit (u01) · alm
- [[src-vab-ftp]] — Phương pháp luận định giá điều chuyển vốn nội bộ (FTP) — Báo cáo tư vấn NHTM EY (T4, draft); hoàn thành 5 units (preamble, u01, u02, u03, u04) · alm

