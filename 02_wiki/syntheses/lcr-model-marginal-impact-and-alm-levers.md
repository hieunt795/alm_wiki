---
title: "LCR: mô hình tính, tác động biên và biện pháp ALM"
aliases: [LCR model marginal impact and ALM levers, Mô hình LCR và tác động biên, Marginal liquidity impact LCR, Biện pháp cải thiện LCR]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Phân tích tác động biên của các quyết định huy động, cho vay, đầu tư và giao dịch liên ngân hàng đến LCR. · Xây dựng mô hình tính LCR, phân rã các yếu tố biến động, xác định marginal liquidity impact và các biện pháp ALM có thể sử dụng để cải thiện LCR."
as_of: 2026-10-22
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-ftp-transmission-analysis]]"]
relations: []
tags: [lcr, marginal-impact, model, decomposition, alm, ftp, research]
updated: 2026-10-22
reviewed:
---

## Câu hỏi
Thuộc bộ "Liquidity Risk — LCR & HQLA" (7 câu). Cụm này trả lời:
- **Q5.** Phân tích tác động biên của các quyết định huy động, cho vay, đầu tư và giao dịch liên ngân hàng đến LCR.
- **Q7.** Xây dựng mô hình tính LCR, phân rã các yếu tố biến động, xác định marginal liquidity impact và các biện pháp ALM có thể sử dụng để cải thiện LCR.

Công thức và hệ số dùng ở đây lấy từ [[lcr-stress-scenario-and-net-cash-outflows]] (Q1–Q2) và [[lcr-hqla-and-funding-run-off-characteristics]] (Q3–Q4). Chi phí của các biện pháp (NIM, IRRBB) nằm ở [[lcr-hqla-buffer-tradeoffs]] (Q6).

**Giới hạn nguồn.** Chưa nguồn nào đã ingest trình bày phương pháp "marginal LCR impact" hay phân rã biến động LCR. Công thức tác động biên và bảng quyết định dưới đây là số học của synthesis, dựng trên hệ số có cite. Bảng cân đối ví dụ là giả định của wiki.

## Kết luận
- **Q5.** Tác động biên của một quyết định lên LCR bằng $(\Delta\text{HQLA} - \text{LCR}\cdot\Delta\text{NCO}) / \text{NCO}$. Vì vậy cùng một giao dịch có thể cho dấu khác nhau tuỳ LCR đang trên hay dưới 100%, và tuỳ trần dòng vào 75% có bị chạm không [[src-bcbs-lcr#^lcr40-77]]. Các quyết định có tác động lớn nhất trong ví dụ là: giải ngân cho vay kỳ hạn > 30 ngày bằng HQLA (giảm tử số 1:1), cấp hạn mức cam kết (tăng mẫu số theo drawdown rate) [[src-tt50-2026-nhnn#^pl1-b5]], và huy động vốn không được rút trong 30 ngày rồi giữ HQLA (tăng tử số, mẫu số không đổi) [[src-tt50-2026-nhnn#^pl1-b1]]. Vay và cho vay liên ngân hàng ≤ 30 ngày cùng hệ số 100% hai chiều [[src-tt50-2026-nhnn#^pl1-b3]] [[src-tt50-2026-nhnn#^pl1-c4-6a]], nên trung tính với NCO khi trần chưa chạm.
- **Q7.** Mô hình LCR gồm bốn khối: dữ liệu vị thế theo khung thời gian đến hạn, bảng phân loại và hệ số, khối HQLA (unwinding và trần), khối NCO (trần 75%). TT50 cung cấp sẵn biểu mẫu cho ba khối cuối: Bảng 3, Bảng 6, Bảng 8 [[src-tt50-2026-nhnn#^pl1-a5]] [[src-tt50-2026-nhnn#^pl1-b7]] [[src-tt50-2026-nhnn#^pl1-c7]]. Phân rã biến động là yêu cầu có nguồn: khi vi phạm, báo cáo ngày đầu phải nêu nguyên nhân và mức độ của từng cấu phần [[src-tt50-2026-nhnn#^d17-2b]]; Basel yêu cầu nêu các yếu tố làm LCR giảm [[src-bcbs-lcr#^lcr20-6b]]. Biện pháp ALM đi theo bốn đòn bẩy: tăng HQLA, kéo dài và làm ổn định nguồn vốn, giảm cam kết ngoại bảng có drawdown cao, và định giá chi phí thanh khoản vào FTP [[src-choudhry-principles-banking#^choudhry-cs-21]] [[src-choudhry-principles-banking#^choudhry-ftp-15]].

## Cơ chế

### Q5 — Tác động biên của từng loại quyết định

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[hqla]] | drives | [[lcr]] | + | [[src-bcbs-lcr#^lcr20-1]] |
| [[cash-outflows]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr20-1]] |
| [[cash-inflows]] | drives | [[lcr]] | + | [[src-bcbs-lcr#^lcr20-1]] |
| [[unsecured-wholesale-funding]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-20]] |
| [[committed-facilities]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-64]] |
| [[secured-funding]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-46]] |

**Công thức tác động biên.** Từ $\text{LCR} = H/N$ với $N = O - \min(I, 0{,}75\,O)$ [[src-bcbs-lcr#^lcr40-1]] [[src-tt50-2026-nhnn#^d21-2]]:

*Diễn giải (số học của synthesis):*

$$
\Delta\text{LCR} \approx \frac{\Delta H - \text{LCR}\cdot\Delta N}{N}
$$

Khi trần chưa chạm ($I < 0{,}75\,O$): $\Delta N = \sum_i r_i\,\Delta O_i - \sum_j q_j\,\Delta I_j$. Khi trần đã chạm: $\Delta N = 0{,}25 \sum_i r_i\,\Delta O_i$ và dòng vào thêm không có tác dụng. Hệ quả:
- Một quyết định tăng $H$ và $N$ cùng một lượng làm LCR hội tụ về 100%: giảm LCR nếu LCR đang > 100%, tăng nếu đang < 100%.
- Hệ số $r_i$, $q_j$ quyết định độ lớn; haircut quyết định phần $\Delta H$ của tài sản Level 2.

**Bảng cân đối ví dụ (giả định, tỷ đồng, hệ số theo TT50).**

| Khoản mục | Số dư | Hệ số | Giá trị LCR | Nguồn hệ số |
|---|---|---|---|---|
| Tiền mặt, tiền gửi NHNN, TPCP (cấp 1) | 80 | 100% | 80 | [[src-tt50-2026-nhnn#^pl1-a2]] |
| Trái phiếu DN phi tài chính AA− (cấp 2A) | 20 | 85% | 17 | [[src-tt50-2026-nhnn#^pl1-a3]] |
| Trái phiếu DN phi tài chính BBB− (cấp 2B) | 10 | 50% | 5 | [[src-tt50-2026-nhnn#^pl1-a4]] |
| **HQLA đủ điều kiện** (chưa chạm trần) | | | **102** | [[src-tt50-2026-nhnn#^pl1-a1]] |
| Tiền gửi bán lẻ ổn định | 300 | 5% | 15 | [[src-tt50-2026-nhnn#^pl1-b2]] |
| Tiền gửi bán lẻ kém ổn định | 200 | 10% | 20 | [[src-tt50-2026-nhnn#^pl1-b2]] |
| Tiền gửi DN phi tài chính | 150 | 40% | 60 | [[src-tt50-2026-nhnn#^pl1-b3]] |
| Tiền gửi hoạt động | 40 | 25% | 10 | [[src-tt50-2026-nhnn#^pl1-b3]] |
| Vay, tiền gửi của TCTD ≤ 30 ngày | 60 | 100% | 60 | [[src-tt50-2026-nhnn#^pl1-b3-25]] |
| Hạn mức tín dụng chưa giải ngân, DN phi tài chính | 100 | 10% | 10 | [[src-tt50-2026-nhnn#^pl1-b5]] |
| Bảo lãnh | 50 | 5% | 2,5 | [[src-tt50-2026-nhnn#^pl1-b5-3]] |
| **Tổng dòng tiền ra** | | | **177,5** | |
| Thu nợ bán lẻ đến hạn trong 30 ngày | 20 | 50% | 10 | [[src-tt50-2026-nhnn#^pl1-c4-5]] |
| Thu nợ DN phi tài chính đến hạn | 40 | 50% | 20 | [[src-tt50-2026-nhnn#^pl1-c4-6b]] |
| Cho vay, tiền gửi tại TCTD ≤ 30 ngày | 50 | 100% | 50 | [[src-tt50-2026-nhnn#^pl1-c4-6a]] |
| **Tổng dòng tiền vào** (trần 75% = 133,1, chưa chạm) | | | **80** | [[src-tt50-2026-nhnn#^d21-2]] |

*Diễn giải (số học):* NCO = 177,5 − 80 = 97,5; LCR = 102 / 97,5 = 104,62%.

**Tác động của từng quyết định (mỗi quyết định 10 tỷ đồng, tính lại toàn bộ).**

| # | Quyết định | ΔHQLA | ΔNCO | LCR sau | ΔLCR (điểm %) | Hệ số chi phối |
|---|---|---|---|---|---|---|
| D1 | Huy động tiền gửi bán lẻ ổn định, giữ tại NHNN | +10 | +0,5 | 114,29% | +9,67 | 5% [[src-tt50-2026-nhnn#^pl1-b2]] |
| D2 | Huy động tiền gửi bán lẻ ổn định, cho vay khách hàng kỳ hạn > 30 ngày | 0 | +0,5 | 104,08% | −0,53 | 5% [[src-tt50-2026-nhnn#^pl1-b2]] |
| D3 | Vay liên ngân hàng ≤ 30 ngày, giữ tại NHNN | +10 | +10 | 104,19% | −0,43 | 100% [[src-tt50-2026-nhnn#^pl1-b3-25]] |
| D4 | Vay liên ngân hàng ≤ 30 ngày, cho vay liên ngân hàng ≤ 30 ngày | 0 | 0 | 104,62% | 0 | 100% / 100% [[src-tt50-2026-nhnn#^pl1-c4-6a]] |
| D5 | Rút tiền gửi NHNN cho vay liên ngân hàng ≤ 30 ngày | −10 | −10 | 105,14% | +0,53 | 100% [[src-tt50-2026-nhnn#^pl1-c4-6a]] |
| D6 | Dùng HQLA giải ngân cho vay DN kỳ hạn > 30 ngày | −10 | 0 | 94,36% | −10,26 | dòng vào chỉ tính khoản đến hạn trong 30 ngày [[src-tt50-2026-nhnn#^pl1-c1-1]] |
| D7 | Dùng tiền mua trái phiếu DN AA− (cấp 2A) | −1,5 | 0 | 103,08% | −1,54 | 85% [[src-tt50-2026-nhnn#^pl1-a3]] |
| D8 | Dùng tiền mua TPCP (cấp 1) | 0 | 0 | 104,62% | 0 | 100% [[src-tt50-2026-nhnn#^pl1-a2]] |
| D9 | Cấp thêm 100 tỷ đồng hạn mức tín dụng cho DN, chưa giải ngân | 0 | +10 | 94,88% | −9,73 | 10% [[src-tt50-2026-nhnn#^pl1-b5]] |
| D10 | Huy động tiền gửi DN kỳ hạn > 30 ngày, không được rút trước hạn, giữ tại NHNN | +10 | 0 | 114,87% | +10,26 | ngoài phạm vi dòng ra [[src-tt50-2026-nhnn#^pl1-b1]] |
| D11 | Chuyển tiền gửi bán lẻ kém ổn định sang ổn định | 0 | −0,5 | 105,15% | +0,54 | 10% → 5% [[src-tt50-2026-nhnn#^pl1-b2-2]] |
| D12 | Huy động tiền gửi DN phi tài chính ≤ 30 ngày, giữ tại NHNN | +10 | +4 | 110,34% | +5,73 | 40% [[src-tt50-2026-nhnn#^pl1-b3-24]] |

*Diễn giải:*
- **Huy động.** Giá trị LCR của một đồng huy động bằng $(1 - \text{LCR}\cdot r)$ nếu được giữ dưới dạng cấp 1. Với LCR 104,62%, tiền gửi bán lẻ ổn định giữ lại 0,95 đồng, tiền gửi DN 0,58 đồng, vay liên ngân hàng ngắn hạn −0,05 đồng (D1, D12, D3).
- **Cho vay.** Giải ngân bằng HQLA làm giảm tử số 1:1; dòng thu nợ chỉ bù 50% và chỉ cho phần đến hạn trong 30 ngày (D6) [[src-tt50-2026-nhnn#^pl1-c4-5]] [[src-tt50-2026-nhnn#^pl1-c4-6b]]. Hạn mức chưa giải ngân cũng tốn LCR trước khi giải ngân (D9).
- **Đầu tư.** Chuyển tiền sang cấp 1 trung tính (D8). Chuyển sang cấp 2 mất phần haircut, và mất toàn bộ phần vượt trần 40%/15% (D7) [[src-tt50-2026-nhnn#^pl1-a1]].
- **Liên ngân hàng.** D4 trung tính khi trần chưa chạm. Nếu ngân hàng đã chạm trần 75% (ví dụ dòng vào 140 thay vì 80, LCR 229,86%), D4 làm NCO tăng 2,5 và LCR giảm còn 217,60%. D5 tăng LCR khi LCR > 100% và trần chưa chạm, nhưng làm giảm HQLA tuyệt đối. Khi LCR dưới ngưỡng, TT50 chỉ cho cho vay TCTD khác nếu sau đó vẫn bảo đảm LCR [[src-tt50-2026-nhnn#^d17-3]].

### Q7 — Mô hình tính LCR và phân rã biến động

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[hqla-unwinding-mechanism]] | input-to | [[lcr]] | | [[src-bcbs-lcr#^lcr30-34]] |
| [[run-off-rate]] | input-to | [[net-cash-outflows]] | | [[src-bcbs-lcr#^lcr40-1]] |
| [[net-cash-outflows]] | input-to | [[lcr]] | | [[src-bcbs-lcr#^lcr20-1]] |
| [[lcr]] | limits | [[balance-sheet-optimisation-model]] | | [[src-lubinska-alm-optimisation#^lubinska-u04-12]] |
| [[liquidity-transfer-pricing]] | priced-by | [[lcr]] | | [[src-choudhry-principles-banking#^choudhry-ftp-15]] |

**Kiến trúc mô hình.**
1. **Dữ liệu vị thế.** Mỗi nghĩa vụ, cam kết và khoản phải thu xếp vào 4 khung thời gian: ngày tiếp theo, ngày 2–7, ngày 8–14, ngày 15–30 [[src-tt50-2026-nhnn#^pl1-b7]] [[src-tt50-2026-nhnn#^pl1-c7]]. Khoản phải thu lấy ngày trả muộn nhất theo hợp đồng [[src-bcbs-lcr#^lcr40-84]] [[src-tt50-2026-nhnn#^pl1-c4-1]]; khoản có nhiều kỳ trả nợ căn cứ thời hạn từng kỳ [[src-tt50-2026-nhnn#^pl1-c1-5]].
2. **Phân loại và hệ số.** Gán từng khoản mục vào đầu mục Bảng 6, Bảng 8; khoản mục thuộc nhiều nhóm dòng ra dùng hệ số cao nhất [[src-tt50-2026-nhnn#^d21-3]]. Hệ số lấy từ PL1 Phần B, C (bảng ở [[lcr-stress-scenario-and-net-cash-outflows]]).
3. **Khối HQLA.** Số dư theo giá thị trường hoặc mark-to-model, cột giá trị sau unwinding, nhân hệ số thanh khoản; tính KĐC15%, KĐC40% [[src-tt50-2026-nhnn#^pl1-a5]] [[src-tt50-2026-nhnn#^pl1-a1]]. Chỉ đưa vào tài sản đạt yêu cầu vận hành Đ20.2 [[src-tt50-2026-nhnn#^d20-1]].
4. **Khối NCO và kết quả.** NCO = dòng ra − min(dòng vào; 75% dòng ra) [[src-tt50-2026-nhnn#^d21-2]]; so với ngưỡng lộ trình [[src-tt50-2026-nhnn#^d16-1c]] và ngưỡng 90% của Đ18.1 [[src-tt50-2026-nhnn#^d18-1]].

Ba loại LCR (quy VNĐ, VNĐ, ngoại tệ trọng yếu) chạy cùng mô hình trên tập dữ liệu khác nhau [[src-tt50-2026-nhnn#^d16-1]]. Biểu tính `04_models/lcr-tt50-2026.xlsx` dựng theo đúng bốn khối này, gồm các sheet HQLA, DongTienRa, DongTienVao, ThamSo, KetQua (số liệu minh hoạ).

**Phân rã biến động.** Yêu cầu nguồn: báo cáo ngày đầu vi phạm phải nêu nguyên nhân (căng thẳng riêng hay toàn thị trường) và mức độ của từng cấu phần [[src-tt50-2026-nhnn#^d17-2b]]; Basel yêu cầu ngân hàng trình các yếu tố làm LCR giảm dưới 100% [[src-bcbs-lcr#^lcr20-6b]].

*Diễn giải (phương pháp của synthesis, chưa có nguồn):*

$$
\text{LCR}_1 - \text{LCR}_0 = \frac{H_1 - H_0}{N_1} - \text{LCR}_0 \cdot \frac{N_1 - N_0}{N_1}
$$

Tách tiếp hai số hạng:
- $\Delta H$ = Δ khối lượng theo cấp + Δ giá thị trường (Level 1, 2A đo theo current market value [[src-bcbs-lcr#^lcr30-40]] [[src-bcbs-lcr#^lcr30-43]]) + Δ hệ số do NHNN điều chỉnh [[src-tt50-2026-nhnn#^pl1-a2-2]] − Δ KĐC15%, KĐC40% − tài sản ra khỏi danh mục vì mất chuẩn hoặc bị ràng buộc.
- $\Delta N = \sum_i r_i \Delta O_i$ (khối lượng) $+ \sum_i O_i \Delta r_i$ (tái phân loại, ví dụ tiền gửi ổn định sang kém ổn định) $- \Delta I_{\text{được tính}}$ (gồm thay đổi do trần 75%).

Ví dụ: áp đồng thời D1 và D9 lên bảng cân đối mẫu, LCR đi từ 104,62% xuống 103,70%. Phân rã: HQLA +9,26 điểm %; NCO −10,17 điểm %, trong đó hạn mức tín dụng chiếm +10 trên ΔNCO = +10,5.

### Biện pháp ALM cải thiện LCR

| Đòn bẩy | Biện pháp | Cơ chế (hệ số) | Nguồn |
|---|---|---|---|
| Tử số | Giữ phần thặng dư huy động dưới dạng cấp 1 thay vì cấp 2 | cấp 1 100%, không trần [[src-tt50-2026-nhnn#^pl1-a2]] | D7, D8 |
| Tử số | Tránh để cấp 2/2B vượt trần | phần vượt bị loại qua KĐC40%, KĐC15% [[src-tt50-2026-nhnn#^pl1-a1]] | |
| Tử số | Giải phóng tài sản bị ràng buộc | tài sản ràng buộc một phần coi là bị ràng buộc [[src-tt50-2026-nhnn#^d20-2]] | |
| Nguồn vốn | Kéo dài kỳ hạn, hạn chế quyền rút trước hạn trong 30 ngày | nguồn vốn kỳ hạn còn lại > 30 ngày không có quyền rút không tính dòng ra [[src-tt50-2026-nhnn#^pl1-b1]] | D10 |
| Nguồn vốn | Sản phẩm "LCR-friendly": tài khoản báo trước 35 ngày, tiền gửi kỳ hạn dài hơn, chuyển sang tài khoản giao dịch | [[src-choudhry-principles-banking#^choudhry-cs-21]] | |
| Nguồn vốn | Chuyển tiền gửi bán lẻ sang nhóm ổn định (quan hệ vay trung dài hạn hoặc tài khoản thanh toán hoạt động) | 10% → 5% [[src-tt50-2026-nhnn#^pl1-b2-2]] | D11 |
| Nguồn vốn | Phân loại tiền gửi hoạt động đủ điều kiện | 40% → 25% [[src-tt50-2026-nhnn#^pl1-b3]] | |
| Nguồn vốn | Thay vay liên ngân hàng không bảo đảm bằng repo cấp 1 | 100% → 0% [[src-tt50-2026-nhnn#^pl1-b3-3]] | |
| Ngoại bảng | Thiết kế hạn mức huỷ ngang vô điều kiện thay vì cam kết | 0% thay vì 10–100% [[src-tt50-2026-nhnn#^pl1-b5-3]] | D9 |
| Dòng vào | Cấu trúc lịch trả nợ để có khoản đến hạn trong 30 ngày | chỉ tính dòng vào theo thoả thuận, nợ nhóm 1 [[src-tt50-2026-nhnn#^pl1-c1-1]] | hiệu quả dừng ở trần 75% |
| Định giá | Thu chi phí thanh khoản của tài sản qua FTP | đơn vị tạo tài sản gây áp lực thanh khoản phải trả chi phí đó qua FTP [[src-choudhry-principles-banking#^choudhry-ftp-15]]; LCR thấp thì tăng spread FTP các tenor O/N–30 ngày [[src-ftp-transmission-analysis#^ftp-trans-8]] (T5) | |
| Ra quyết định | Tối ưu bảng cân đối với LCR là ràng buộc bất đẳng thức | [[src-lubinska-alm-optimisation#^lubinska-u04-12]] | [[balance-sheet-optimisation-model]] |
| Khi vi phạm (VN) | Vay TCTD khác, cam kết không thể huỷ ngang | biện pháp tự xử lý bắt buộc [[src-tt50-2026-nhnn#^d17-2]] | |

## Bằng chứng ủng hộ
- Choudhry CS6: rà soát tiền gửi cho thấy khoảng 12% số dư rút ngay chịu chi phí đệm dòng ra LCR cao nhất. Treasury đưa lên ALCO chiến lược tiền gửi theo hiệu quả vốn và độ nhạy lãi suất [[src-choudhry-principles-banking#^choudhry-cs-20]], với khuyến nghị chuyển sang sản phẩm "LCR-friendly" [[src-choudhry-principles-banking#^choudhry-cs-21]].
- Lubinska đặt các tỷ lệ thanh khoản ngắn hạn làm ràng buộc trong bài toán tối ưu sổ ngân hàng [[src-lubinska-alm-optimisation#^lubinska-u04-12]].

## Bằng chứng trái chiều
Không ghi nhận trong nguồn đã ingest. Công thức tác động biên chưa được nguồn nào kiểm chứng hay phản bác.

## Phụ thuộc regime
- **LCR trên hay dưới 100%.** Quyết định tăng HQLA và NCO cùng lượng (D3) làm giảm LCR khi LCR > 100%, tăng khi LCR < 100% (số học).
- **Trần dòng vào.** Ngân hàng có dòng vào ngắn hạn lớn chạm trần 75%; khi đó cải thiện dòng vào không có tác dụng [[src-tt50-2026-nhnn#^d21-2]].
- **Stress.** Trong stress, Basel coi việc dùng HQLA là hợp lệ [[src-bcbs-lcr#^lcr20-5]]; TT50 yêu cầu biện pháp tự xử lý ngay [[src-tt50-2026-nhnn#^d17-2]]. Biện pháp cấu trúc (kỳ hạn, phân loại tiền gửi) cần thời gian; biện pháp khi vi phạm là vay và cam kết từ TCTD khác.

## Hàm ý ALM / quy định
- **Nghĩa vụ NHNN.** Hệ số trong bảng quyết định là hệ số TT50, áp dụng cho LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]]. Báo cáo vi phạm phải định lượng mức độ của từng cấu phần [[src-tt50-2026-nhnn#^d17-2b]], nên mô hình cần lưu được đóng góp theo đầu mục giữa hai ngày.
- **Basel (tham chiếu).** Run-off bán lẻ stable có thể là 3% tại jurisdiction có quỹ bảo hiểm prefunded [[src-bcbs-lcr#^lcr40-11]]; tại VN, TT50 áp 5% [[src-tt50-2026-nhnn#^pl1-b2]].
- *Diễn giải:* ALCO có thể dùng $(1 - \text{LCR}\cdot r)$ làm "giá trị LCR" của mỗi đồng huy động, và $(1 - q\cdot\text{LCR})$ làm "chi phí LCR" của mỗi đồng HQLA chuyển sang tài sản có dòng thu trong 30 ngày với inflow rate $q$, để so sánh sản phẩm. Kết hợp với chi phí huy động thì ra chi phí biên của một điểm LCR. Phần này cần nguồn phương pháp trước khi dùng làm chính sách.

## Bất định
- Phương pháp tác động biên và phân rã biến động: chưa có nguồn. Cần `/register` tài liệu về quản trị LCR hoặc liquidity attribution.
- Bảng cân đối ví dụ dùng số giả định; cột "Giá trị LCR" không phản ánh ngân hàng thực nào.
- Choudhry u27 (danh mục file kèm sách) có nhắc LCR; chưa rõ có mô hình tính hay không.
- Nguồn [[src-ftp-transmission-analysis]] là T5; quy tắc tăng spread FTP theo LCR mới chỉ có một nguồn.
