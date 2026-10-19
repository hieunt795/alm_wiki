---
title: "Chuẩn mực BCBS IRRBB (Interest Rate Risk in the Banking Book)"
aliases: [BCBS IRRBB, Basel IRRBB, Chuẩn mực rủi ro lãi suất trên sổ ngân hàng, BCBS d368]
type: regulation
domains: [basel, alm]
status: active
maturity: canonical
issuer: BCBS
number: d368
jurisdiction: INTL
doc_status: final
issued: 2016-04-21
valid_from: 2018-01-01
valid_to:
supersedes: []
superseded_by:
amends: []
implements: []
sources: ["[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: governs, to: "[[economic-value-of-equity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u01-4]]"}
  - {type: governs, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u01-4]]"}
  - {type: governs, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: governs, to: "[[basis-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: governs, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-2]]"}
  - {type: governs, to: "[[non-maturity-deposits]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-4]]"}
  - {type: governs, to: "[[behavioural-options]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-5]]"}
  - {type: governs, to: "[[csrbb]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u02-3]]"}
  - {type: governs, to: "[[outlier-bank-test]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
tags: [basel, irrbb, pillar-2, eve, nii, interest-rate-risk]
updated: 2026-10-18
reviewed:
---

## Mục đích & phạm vi
Chuẩn mực IRRBB 2016 (văn bản Standards d368 của [[bcbs]]) thiết lập các nguyên tắc và phương pháp luận cập nhật nhằm nhận diện, đo lường, theo dõi và kiểm soát rủi ro lãi suất trên sổ ngân hàng (IRRBB) và rủi ro chênh lệch tín dụng trên sổ ngân hàng ([[csrbb]]) [[src-bcbs-irrbb-2016#^irrbb-u01-1]] [[src-bcbs-irrbb-2016#^irrbb-p01-1]].

Về vị trí pháp lý trong cấu trúc Basel, BCBS đã chính thức quyết định duy trì IRRBB trong **Trụ cột 2 nâng cao (Enhanced Pillar 2 - Supervisory Review Process)** kết hợp với nghĩa vụ công bố thông tin minh bạch theo **Trụ cột 3 (Pillar 3 - Market Discipline)** [[src-bcbs-irrbb-2016#^irrbb-u01-2]]. Đề xuất đưa IRRBB thành yêu cầu vốn tối thiểu Trụ cột 1 (Pillar 1 minimum capital charge) đã bị bác bỏ do tính chất không đồng nhất (heterogeneity) của danh mục tài sản và nợ sổ ngân hàng giữa các tổ chức tín dụng; một công thức chuẩn hoá cứng nhắc sẽ không thể phản ánh chính xác độ nhạy rủi ro và các đặc tính hành vi đặc thù [[src-bcbs-irrbb-2016#^irrbb-u01-2]].

Về phạm vi áp dụng, chuẩn mực bắt buộc áp dụng trên cơ sở hợp nhất cho tất cả các ngân hàng hoạt động quốc tế lớn; các cơ quan giám sát quốc gia có quyền quyết định áp dụng cho các ngân hàng nội địa nhằm duy trì bình đẳng cạnh tranh [[src-bcbs-irrbb-2016#^irrbb-u04-1]]. Chuẩn mực có hiệu lực từ năm 2018 (công bố số liệu năm tài chính 2017) [[src-bcbs-irrbb-2016#^irrbb-u04-2]].

## Cấu trúc 12 Nguyên tắc IRRBB

Chuẩn mực bao gồm 12 nguyên tắc cốt lõi chia thành 2 nhóm chủ thể:

### Nhóm nguyên tắc dành cho Ngân hàng (Principles 1–9)
1. **Nguyên tắc 1 — Nhận diện & Kiểm soát**: IRRBB là rủi ro trọng yếu đối với mọi ngân hàng, phát sinh từ hoạt động trung gian tài chính tạo ra chênh lệch kỳ hạn và chênh lệch lãi suất; ngân hàng phải nhận diện, đo lường, theo dõi và kiểm soát chặt chẽ cả IRRBB và CSRBB [[src-bcbs-irrbb-2016#^irrbb-p01-1]].
2. **Nguyên tắc 2 — Quản trị & ALCO**: Hội đồng Quản trị chịu trách nhiệm cao nhất về chiến lược, chính sách và khẩu vị rủi ro IRRBB; có thể ủy quyền cho Ban điều hành hoặc Hội đồng Quản lý Tài sản - Nợ (ALCO) [[src-bcbs-irrbb-2016#^irrbb-p02-1]]. Báo cáo IRRBB phải gửi lên HĐQT tối thiểu bán niên [[src-bcbs-irrbb-2016#^irrbb-p02-2]]. Khối quản trị rủi ro IRRBB phải độc lập với các đơn vị kinh doanh chấp nhận rủi ro [[src-bcbs-irrbb-2016#^irrbb-p02-3]].
3. **Nguyên tắc 3 — Khẩu vị rủi ro & Hạn mức**: Khẩu vị rủi ro phải được định lượng đồng thời qua cả hai lăng kính: giá trị kinh tế ([[economic-value-of-equity|$\Delta\text{EVE}$]]) và thu nhập ([[net-interest-income-sensitivity|$\Delta\text{NII}$]]), kèm hệ thống hạn mức cụ thể cho từng loại rủi ro (gap, basis, options) [[src-bcbs-irrbb-2016#^irrbb-p03-1]].
4. **Nguyên tắc 4 — Đo lường & Kịch bản sốc**: Phải sử dụng đồng thời thước đo giá trị kinh tế (horizon run-off đến khi đáo hạn hết dòng tiền) và thước đo thu nhập (horizon ngắn-trung hạn 1–3 năm, giả định constant/dynamic balance sheet) [[src-bcbs-irrbb-2016#^irrbb-p04-1]] [[src-bcbs-irrbb-2016#^irrbb-p04-2]]. Hệ thống IMS phải chạy được 6 kịch bản sốc chuẩn hoá tại Annex 2, kịch bản ICAAP nội bộ, và stress testing ngược (reverse stress test) [[src-bcbs-irrbb-2016#^irrbb-p04-3]].
5. **Nguyên tắc 5 — Giả định hành vi**: Phải mô hình hoá và kiểm định nghiêm ngặt các giả định hành vi về tiền gửi không kỳ hạn (NMDs), tỷ lệ trả nợ trước hạn (prepayment CPR), và tỷ lệ rút tiền gửi có kỳ hạn sớm (early redemption TDRR) [[src-bcbs-irrbb-2016#^irrbb-p05-1]].
6. **Nguyên tắc 6 — Hệ thống dữ liệu & Kiểm định mô hình độc lập**: Quy trình quản trị rủi ro mô hình phải có chức năng kiểm định độc lập (independent validation) tách biệt với nhóm phát triển mô hình, bao gồm 3 cấu phần: đánh giá tính vững chắc lý luận, giám sát liên tục, và phân tích kết quả/kiểm định ngược (backtesting) [[src-bcbs-irrbb-2016#^irrbb-p06-1]] [[src-bcbs-irrbb-2016#^irrbb-p06-2]]. Kiểm toán nội bộ rà soát hàng năm [[src-bcbs-irrbb-2016#^irrbb-p06-3]].
7. **Nguyên tắc 7 — Báo cáo nội bộ**: Định kỳ báo cáo HĐQT và ALCO về phơi lượng rủi ro gộp, mức độ tuân thủ hạn mức, kết quả stress test và đánh giá chiến lược phòng ngừa rủi ro [[src-bcbs-irrbb-2016#^irrbb-p07-1]].
8. **Nguyên tắc 8 — Công bố thông tin Trụ cột 3**: Bắt buộc công bố định kỳ hàng năm theo Bảng A (thông tin định tính) và Bảng B (thông tin định lượng: $\Delta\text{EVE}$ và $\Delta\text{NII}$ dưới 6 kịch bản sốc) [[src-bcbs-irrbb-2016#^irrbb-p08-1]].
9. **Nguyên tắc 9 — Đánh giá an toàn vốn nội bộ (ICAAP)**: Ngân hàng phải tự tính toán và nắm giữ vốn tự có đủ để bù đắp rủi ro giá trị kinh tế EVE và trích lập bộ đệm vốn (capital buffers) cho rủi ro suy giảm thu nhập tương lai NII [[src-bcbs-irrbb-2016#^irrbb-p09-1]] [[src-bcbs-irrbb-2016#^irrbb-p09-2]].

### Nhóm nguyên tắc dành cho Cơ quan Giám sát (Principles 10–12)
10. **Nguyên tắc 10 — Thu thập thông tin giám sát**: Cơ quan giám sát định kỳ thu thập dữ liệu về khe hở tái định giá, mô hình NMDs, quyền chọn tự động, $\Delta\text{EVE}$ và $\Delta\text{NII}$ để so sánh ngang hàng (peer comparison) [[src-bcbs-irrbb-2016#^irrbb-p10-1]].
11. **Nguyên tắc 11 — Đánh giá giám sát chuyên sâu**: Cơ quan giám sát sử dụng cán bộ chuyên trách để đánh giá hệ thống IMS của ngân hàng; có quyền yêu cầu ngân hàng áp dụng Khuôn khổ chuẩn hoá (Standardised Framework) nếu IMS không đạt yêu cầu [[src-bcbs-irrbb-2016#^irrbb-p11-1]] [[src-bcbs-irrbb-2016#^irrbb-p11-2]].
12. **Nguyên tắc 12 — Ngân hàng ngoại lai (Outlier Bank Test)**: Cơ quan giám sát phải công bố tiêu chí xác định ngân hàng ngoại lai và nên (should) áp dụng ít nhất một phép thử so sánh $\Delta\text{EVE}$ cực đại dưới 6 kịch bản sốc với **15% Vốn cấp 1 (Tier 1 Capital)** [[src-bcbs-irrbb-2016#^irrbb-p12-1]]. Khi rà soát kết luận quản trị IRRBB không đầy đủ hoặc rủi ro quá mức, cơ quan giám sát phải yêu cầu một hoặc nhiều biện pháp: giảm phơi lượng, tăng vốn, đặt ràng buộc lên tham số nội bộ, cải thiện khung quản trị rủi ro [[src-bcbs-irrbb-2016#^irrbb-p12-3]].

## Các ngưỡng định lượng và quy chuẩn kỹ thuật

| Tiêu chuẩn | Đối tượng | Quy định kỹ thuật | Căn cứ d368 |
|---|---|---|---|
| [[outlier-bank-test\|Outlier Bank Test]] | Ngân hàng chịu rủi ro quá mức | $\max_{i=1..6} \Delta\text{EVE}_i > 15\% \text{ Tier 1 Capital}$ | Nguyên tắc 12 [[src-bcbs-irrbb-2016#^irrbb-p12-1]] |
| [[economic-value-of-equity\|$\Delta\text{EVE}$]] | Biến động giá trị kinh tế | Run-off balance sheet, loại bỏ vốn chủ sở hữu, chiết khấu risk-free | Nguyên tắc 8 [[src-bcbs-irrbb-2016#^irrbb-p08-2]] |
| [[net-interest-income-sensitivity\|$\Delta\text{NII}$]] | Biến động thu nhập thuần từ lãi | Constant balance sheet, chân trời 12 tháng liên tục, gồm commercial margin | Nguyên tắc 8 [[src-bcbs-irrbb-2016#^irrbb-p08-3]] |
| Phân bổ dải kỳ hạn | Dòng tiền tái định giá | 19 dải kỳ hạn chuẩn hoá (Overnight đến $> 20$ năm) | Section IV [[src-bcbs-irrbb-2016#^irrbb-u05-2]] |
| [[notional-repricing-cash-flow\|Notional repricing cash flow]] | Dòng tiền tái định giá | Hoàn trả gốc, tái định giá gốc, thanh toán lãi; ngày của mỗi khoản là repricing date | Section IV par 102 [[src-bcbs-irrbb-2016#^irrbb-u05-9]] |
| Công cụ lãi suất thả nổi | Floating rate instruments | Giả định tái định giá toàn bộ tại first reset date; trừ phần spread không tái định giá | Section IV par 104 [[src-bcbs-irrbb-2016#^irrbb-u05-12]] |
| [[non-maturity-deposits\|Trần tiền gửi lõi (Core NMDs)]] | Tiền gửi không kỳ hạn bán lẻ giao dịch | Tối đa 90% số dư; kỳ hạn bình quân tối đa 5 năm | Section IV Table 2 [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| [[non-maturity-deposits\|Trần tiền gửi lõi (Core NMDs)]] | Tiền gửi không kỳ hạn bán lẻ phi giao dịch | Tối đa 70% số dư; kỳ hạn bình quân tối đa 4,5 năm | Section IV Table 2 [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| [[non-maturity-deposits\|Trần tiền gửi lõi (Core NMDs)]] | Tiền gửi không kỳ hạn bán buôn | Tối đa 50% số dư; kỳ hạn bình quân tối đa 4 năm | Section IV Table 2 [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| [[non-maturity-deposits\|Tiền gửi NMDs phi lõi]] | Non-core deposits | Bắt buộc phân bổ 100% vào dải kỳ hạn qua đêm (overnight) | Section IV [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| [[behavioural-options\|Hệ số nhân trả nợ trước hạn $\gamma_i$]] | Prepayment CPR scalar | 0.8 khi lãi suất tăng; 1.2 khi lãi suất giảm | Section IV Table 3 [[src-bcbs-irrbb-2016#^irrbb-u05-5]] |
| [[behavioural-options\|Hệ số co giãn rút tiền gửi sớm $u_i$]] | Early redemption TDRR scalar | 1.2 khi lãi suất tăng; 0.8 khi lãi suất giảm | Section IV Table 4 [[src-bcbs-irrbb-2016#^irrbb-u05-6]] |
| Quyền chọn tự động $KAO_{i,c}$ | Automatic interest rate options | Định giá lại toàn bộ với mức tăng độ biến động ngầm định 25% | Section IV [[src-bcbs-irrbb-2016#^irrbb-u05-7]] |
| 6 Kịch bản sốc lãi suất | Toàn bộ tiền tệ trọng yếu | Sàn tuyệt đối 100 bps; trần Short 500 bps, Parallel 400 bps, Long 300 bps | Annex 2 [[src-bcbs-irrbb-2016#^irrbb-u07-4]] |

## Mối liên hệ tương hỗ với Thanh khoản (LCR & NSFR)
Chuẩn mực IRRBB liên kết mật thiết với các chỉ số thanh khoản Basel:
- **Thời lượng (Duration) của đệm HQLA trong [[lcr]]**: Nắm giữ trái phiếu chính phủ Level 1 dài hạn để tối đa hoá tỷ lệ LCR mà không phòng ngừa rủi ro lãi suất sẽ tạo ra tổn thất $\Delta\text{EVE}$ nặng nề khi đường cong dịch chuyển tăng song song hoặc dốc lên.
- **Chênh lệch kỳ hạn trong [[nsfr]]**: Hoạt động chuyển đổi kỳ hạn (maturity transformation) — sử dụng nguồn vốn ngắn hạn (ASF thấp) tài trợ cho tài sản sinh lời trung-dài hạn (RSF cao) — vừa là nguyên nhân làm giảm tỷ lệ NSFR, vừa là cội nguồn phát sinh rủi ro khe hở tái định giá ([[gap-risk]]) làm tổn thương $\Delta\text{EVE}$ và $\Delta\text{NII}$.
- Xem phân tích chi tiết tại [[irrbb-five-tier-architecture]], [[irrbb-alm-governance-strategy-and-tradeoffs]], [[integrated-alm-liquidity-strategy]] và [[hqla-decomposition-and-tradeoffs]].

## Đề xuất cập nhật
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đề xuất thêm dòng vào bảng yêu cầu (sau dòng 69): | Notional repricing cash flow | Hoàn trả gốc, tái định giá gốc, thanh toán lãi; ngày của mỗi khoản là repricing date | par 102 [[src-bcbs-irrbb-2016#^irrbb-u05-9]] | và | Công cụ thả nổi | Tái định giá toàn bộ tại first reset date | par 104 [[src-bcbs-irrbb-2016#^irrbb-u05-12]] |. → đã áp [2026-10-18]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; dòng bảng "Notional repricing cash flow" đề xuất ở trên nên link tới node này. → đã áp [2026-10-18]
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 60 "phép thử tối thiểu bắt buộc là so sánh … 15% Vốn cấp 1": đề xuất "cơ quan giám sát phải công bố tiêu chí và nên (should) áp dụng ít nhất một phép thử so max ∆EVE dưới 6 kịch bản với 15% Tier 1" ([[src-bcbs-irrbb-2016#^irrbb-p12-1]]). "Khi vi phạm, ngân hàng bị áp dụng chế tài": đề xuất "khi rà soát kết luận quản trị yếu kém hoặc rủi ro quá mức, cơ quan giám sát phải yêu cầu một hoặc nhiều biện pháp" ([[src-bcbs-irrbb-2016#^irrbb-p12-3]]). → đã áp [2026-10-18]
