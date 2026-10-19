---
title: "Mô Hình Bảng Cân Đối Tái Định Giá (Repricing Balance Sheet)"
aliases: [Repricing Balance Sheet, Bảng cân đối tái định giá, Repricing Schedule, Thang tái định giá lãi suất, Repricing Gap Schedule]
type: model
domains: [alm, basel, vn-reg]
status: active
maturity: draft
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-tata-bank-alm#^tata-gap-1]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u02-23]]"}
  - {type: input-to, to: "[[economic-value-of-equity]]", cite: "[[src-tata-bank-alm#^tata-gap-3]]"}
  - {type: input-to, to: "[[irrbb-standardised-framework]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: input-to, to: "[[duration-gap-model]]", cite: "[[src-tata-bank-alm#^tata-dgap-1]]"}
  - {type: input-to, to: "[[balance-sheet-optimisation-model]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u04-13]]"}
tags: [irrbb, model, repricing-balance-sheet, repricing-gap, cash-flow-slotting, reset-date, time-bands, alm]
updated: 2026-10-19
reviewed:
---

## Mục tiêu
Repricing balance sheet (lịch tái định giá) phân bổ tài sản, nợ và khoản mục ngoại bảng nhạy lãi suất vào các dải kỳ hạn. Khoản lãi suất cố định xếp theo ngày đáo hạn; khoản thả nổi xếp theo thời gian còn lại tới ngày tái định giá tiếp theo [[src-tata-bank-alm#^tata-gap-1]]. Đây là đầu vào của repricing gap analysis [[src-tata-bank-alm#^tata-gap-1]].

Theo BCBS, ngày của mỗi khoản trả gốc, tái định giá gốc hay trả lãi đều là repricing date của khoản đó [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Vì vậy lịch tái định giá nhìn bảng cân đối theo thời điểm lãi suất đổi, không theo kỳ hạn hợp đồng. Xem [[notional-repricing-cash-flow]].

Mô hình phục vụ ba phép đo:

| Phép đo | Cách dùng lịch tái định giá | Nguồn |
|---|---|---|
| Repricing gap theo dải | RSA trừ RSL của mỗi dải | [[src-lubinska-alm-optimisation#^lubinska-u02-23]] |
| ΔNII | Gap nhân thay đổi lãi suất giả định, xấp xỉ thay đổi NII trong gapping period | [[src-lubinska-alm-optimisation#^lubinska-u02-25]] |
| ΔEVE | Gap ròng mỗi dải nhân mức giảm giá trị theo modified duration, cộng dồn thành total repricing gap | [[src-tata-bank-alm#^tata-gap-3]] |
| ΔEVE chuẩn hoá (Basel) | Stage 2 của khung năm giai đoạn: slot dòng tiền vào dải kỳ hạn | [[src-bcbs-irrbb-2016#^irrbb-u05-1]] |

Tại Việt Nam, [[tt83-2025]] yêu cầu chiến lược IRRBB tối thiểu có nguyên tắc quản lý theo trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile). Chỉ số này là chênh lệch giữa tài sản và nợ nhạy lãi suất, gồm cả ngoại bảng, theo thời điểm ấn định lãi suất mới hoặc thời điểm định giá lại [[src-tt83-2025-nhnn#^d53-1a1]]. Báo cáo nội bộ IRRBB, tối thiểu hằng quý, phải gồm trạng thái này [[src-tt83-2025-nhnn#^d55-1]].

## Công thức
Repricing gap của dải $k$ bằng tài sản nhạy lãi suất trừ nợ nhạy lãi suất. RSA gồm khoản vay cố định hoặc thả nổi; RSL gồm vốn bán buôn và tiền gửi không kỳ hạn [[src-lubinska-alm-optimisation#^lubinska-u02-23]] [[src-lubinska-alm-optimisation#^lubinska-u02-25]]:

$$\text{GAP}_k = \text{RSA}_k - \text{RSL}_k$$
[[src-lubinska-alm-optimisation#^lubinska-u02-25]]

*Diễn giải:* khoản mục ngoại bảng (chân swap) được cộng vào RSA hoặc RSL của dải tương ứng, vì lịch tái định giá gồm cả ngoại bảng [[src-tata-bank-alm#^tata-gap-1]] [[src-tt83-2025-nhnn#^d53-1a1]]. Khe hở luỹ kế $\text{CGAP}_K = \sum_{k \le K} \text{GAP}_k$ là cách trình bày của wiki, nguồn không nêu công thức này.

**Dấu của gap.** Gap dương (nhiều tài sản tái định giá hơn nợ) là asset sensitive, hưởng lợi khi lãi suất tăng; gap âm là liability sensitive, thua lỗ khi lãi suất tăng [[src-choudhry-principles-banking#^choudhry-irrbb-5]].

**ΔNII theo gap.** ΔNII bằng thay đổi lãi suất nhân GAP trong gapping period, ví dụ 1 năm [[src-lubinska-alm-optimisation#^lubinska-u02-25]]. Phương pháp incremental gap gán trọng số thời gian từ điểm giữa dải tới cuối gapping period [[src-lubinska-alm-optimisation#^lubinska-u02-28]]. Tata gọi đây là earning gap: periodic earning gap bằng net repricing gap × 1% × phần còn lại của năm đầu tính từ điểm giữa dải, chia 12 [[src-tata-bank-alm#^tata-egap-1]]:

$$\Delta\text{NII}_{12M} = \sum_{k} \text{GAP}_k \cdot \Delta r \cdot \frac{12 - t_k}{12}$$
[[src-tata-bank-alm#^tata-egap-1]]

với $t_k$ là điểm giữa dải $k$ tính theo tháng, chỉ gồm các dải trong 12 tháng đầu.

**ΔEVE theo gap.** Nhân mỗi gap ròng với mức giảm giá trị kinh tế (%) khi lãi suất tăng 1%, dựa trên modified duration $D^*_k$ của tài sản và nợ trong dải, rồi cộng dồn [[src-tata-bank-alm#^tata-gap-3]]:

$$\Delta\text{EVE} \approx - \sum_{k} \text{GAP}_k \cdot D^*_k \cdot \Delta y$$
[[src-tata-bank-alm#^tata-gap-3]]

Với khung chuẩn hoá của BCBS, dòng tiền ròng mỗi dải được chiết khấu theo kịch bản sốc thay vì nhân duration. Xem [[irrbb-standardised-framework]].

**Các biến thể của gap** (chi tiết ở [[repricing-gap-analysis]]):

| Biến thể | Đặc điểm | Nguồn |
|---|---|---|
| Maturity gap | Đơn giản nhất: xếp theo kỳ hạn (cố định) hoặc thời gian tới lần tái định giá kế tiếp (thả nổi) | [[src-lubinska-alm-optimisation#^lubinska-u02-22]] |
| Maturity gap cơ bản và advanced repricing gap | Cơ bản đặt dòng tiền ở điểm giữa dải; nâng cao đặt ở đúng ngày rủi ro | [[src-lubinska-alm-optimisation#^lubinska-u02-34]] |
| Flow approach và stock analysis | Flow (dòng tiền khoản cố định, dư nợ tại ngày tái định giá khoản thả nổi) để tính ΔNII; stock (dư nợ từng khoản) để tính phơi nhiễm theo dải và phòng ngừa | [[src-lubinska-alm-optimisation#^lubinska-u02-35]] |
| Repricing gap 12 tháng | Chia theo tháng, nhưng chỉ "thấy" ngày rủi ro đầu tiên của khoản thả nổi | [[src-lubinska-alm-optimisation#^lubinska-u02-36]] |
| Refixing gap | Mọi ngày refixing trong gapping period theo từng yếu tố rủi ro (EURIBOR 3M, LIBOR 1M…); công cụ cơ bản để đặt chiến lược phòng ngừa | [[src-lubinska-alm-optimisation#^lubinska-u02-37]] |

## Inputs & giả định
**Phạm vi.**
- Sổ ngân hàng gồm mọi giao dịch, vị thế dài hạn liên quan đến hoạt động kinh doanh khách hàng và việc tài trợ cho chúng, kể cả vốn chủ sở hữu [[src-tata-bank-alm#^tata-scope-1]]. Sổ kinh doanh gồm vị thế nắm giữ để bán lại ngắn hạn, hưởng lợi từ biến động giá ngắn hạn, arbitrage hoặc phòng ngừa rủi ro [[src-tata-bank-alm#^tata-scope-2]]. Xem [[banking-book]].
- Chỉ công cụ nhạy lãi suất được đưa vào tính IRRBB [[src-tata-bank-alm#^tata-scope-3]]. Công cụ nhạy lãi suất là tài sản, nợ và ngoại bảng trong sổ ngân hàng, trừ tài sản bị trừ khỏi CET1 như bất động sản, tài sản vô hình và đầu tư cổ phần sổ ngân hàng [[src-tata-bank-alm#^tata-scope-4]].
- Khi tính độ nhạy NII, vị thế không nhạy lãi suất (bất động sản, đầu tư cổ phần, tài sản vô hình, vốn chủ sở hữu kế toán) bị loại [[src-tata-bank-alm#^tata-nii-5]]. Trong khung BCBS, dòng tiền của nợ được tính trừ CET1 [[src-bcbs-irrbb-2016#^irrbb-u05-2]], và vốn chủ sở hữu bị loại khỏi tính ΔEVE công bố [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- Ngoại bảng gồm phái sinh dùng phòng ngừa vi mô, ví dụ asset swap đổi khoản vay cố định 5 năm sang thả nổi [[src-tata-bank-alm#^tata-scope-5]]. Cam kết cho vay, nhận tiền gửi ở lãi suất cố định tạo pipeline risk [[src-choudhry-principles-banking#^choudhry-irrbb-6]].
- *Diễn giải:* danh mục cụ thể (cho vay khách hàng, liên ngân hàng, tiền gửi NHTW, giấy tờ có giá phát hành) là cách wiki liệt kê theo nhóm sản phẩm, nguồn không đưa danh sách đầy đủ.

**Quy tắc slot theo loại lãi suất:**

| Trường hợp | Quy tắc | Nguồn |
|---|---|---|
| Lãi suất cố định | Mọi coupon và khoản trả gốc nên xếp theo contractual maturity | [[src-bcbs-irrbb-2016#^irrbb-u05-13]] |
| Lãi suất thả nổi, phần gốc | Giả định tái định giá toàn bộ tại first reset date | [[src-bcbs-irrbb-2016#^irrbb-u05-12]] |
| Lãi suất thả nổi, cách biểu diễn | Chuỗi coupon tới next reset date cộng một dòng par notional tại dải chứa ngày đó | [[src-bcbs-irrbb-2016#^irrbb-u05-14]] |
| Spread không tái định giá | Phải slot tới contractual maturity, kể cả khi gốc đã tái định giá | [[src-bcbs-irrbb-2016#^irrbb-u05-11]] |
| Commercial margin | Ngân hàng được chọn trừ hay giữ, với phương pháp thận trọng và minh bạch | [[src-bcbs-irrbb-2016#^irrbb-u05-15]] |

Lý do kinh tế: sau khi reset theo lãi suất thị trường, công cụ giao dịch lại ở mệnh giá, nên rủi ro lãi suất chỉ tính tới next reset date [[src-tata-bank-alm#^tata-gap-2]].

**Dải kỳ hạn.** BCBS dùng 19 dải kỳ hạn chuẩn hoặc điểm giữa của các dải [[src-bcbs-irrbb-2016#^irrbb-u05-2]], từ qua đêm tới trên 20 năm [[src-bcbs-irrbb-2016#^irrbb-u05-25]]. Mọi dòng tiền được phân bổ theo từng đồng tiền, tuỳ khả năng chuẩn hoá của vị thế [[src-bcbs-irrbb-2016#^irrbb-u05-16]]. *Diễn giải:* lịch nội bộ thường gộp ít dải hơn để dễ đọc, ví dụ 8 dải trong ngân hàng mô hình của Tata (<1 tới 48–60 tháng) [[src-tata-bank-alm#^tata-gap-6]].

**Vị thế hành vi:**

| Vị thế | Xử lý | Nguồn |
|---|---|---|
| NMD (BCBS) | Phần phi lõi coi là qua đêm, đặt vào dải ngắn nhất; phần lõi slot theo quy trình của ngân hàng, trong trần kỳ hạn bình quân: bán lẻ giao dịch 5 năm, bán lẻ phi giao dịch 4,5 năm, bán buôn 4 năm | [[src-bcbs-irrbb-2016#^irrbb-u05-4]] |
| NMD (thực hành) | Ba cách: dải ngắn nhất (phổ biến nhất, gap biến động mạnh); dải dài nhất; tách core/unstable | [[src-choudhry-principles-banking#^choudhry-lgap-7]] |
| NMD (báo cáo EU) | Góc nhìn hợp đồng xếp NMD vào dải ngắn nhất, không áp hành vi; góc nhìn hành vi phải nhất quán với dòng tiền đã mô hình hoá | [[src-tata-bank-alm#^tata-rep-2]] |
| Cho vay trả nợ trước hạn | CPR nhân hệ số 0,8 khi lãi suất tăng, 1,2 khi lãi suất giảm | [[src-bcbs-irrbb-2016#^irrbb-u05-5]] |
| Tiền gửi có kỳ hạn rút trước hạn | TDRR nhân hệ số 1,2 khi lãi suất tăng, 0,8 khi lãi suất giảm | [[src-bcbs-irrbb-2016#^irrbb-u05-6]] |

Xem [[non-maturity-deposits]], [[behavioural-options]].

**Phản ứng của lãi suất sản phẩm.** Khi lãi suất chung đổi, lãi suất sản phẩm giữ nguyên (cố định, không chịu lãi), đổi bằng mức thay đổi benchmark (gắn SONIA hoặc Base Rate), hoặc đổi nhiều hơn hay ít hơn (thẻ tín dụng, tài khoản lãi thấp cũ) [[src-choudhry-principles-banking#^choudhry-nim-3]]. *Diễn giải:* nhóm thứ ba không khớp giả định "tái định giá 100% tại ngày reset" của lịch tái định giá; cần xử lý bằng hệ số pass-through hoặc tách basis risk.

**Basel vs VN:**

| Tham số | Basel (d368) | VN (TT83/2025 PL5) | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Dòng tiền | Trả gốc, tái định giá gốc, trả lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]] | Khoản trả gốc; khoản gốc được định giá lại; khoản trả lãi trên phần gốc chưa hoàn trả hoặc chưa định giá lại [[src-tt83-2025-nhnn#^pl5-a1-1c]] | par 102; PL5.A.I.1.c | 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] |
| Dải kỳ hạn | 19 dải hoặc điểm giữa [[src-bcbs-irrbb-2016#^irrbb-u05-2]] | 19 thang kỳ hạn theo ngày định giá lại hoặc điểm giữa; phân bổ vào điểm giữa thì chia dòng tiền giữa hai điểm giữa liền kề [[src-tt83-2025-nhnn#^pl5-a2-0]] [[src-tt83-2025-nhnn#^pl5-a2-t1]] | par 101; PL5.A.II | 01/07/2026 |
| Cố định | Theo contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-13]] | Dòng tiền trả gốc, lãi vào thang có ngày trả gốc, lãi [[src-tt83-2025-nhnn#^pl5-a2-1]] | par 106; PL5.A.II.1.b | 01/07/2026 |
| Thả nổi | Toàn bộ gốc tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]] | Gốc, lãi định kỳ tới ngày định giá lại gần nhất; gốc còn lại vào thang có ngày đó [[src-tt83-2025-nhnn#^pl5-a2-1]] | par 104; PL5.A.II.1.b | 01/07/2026 |
| NMD | Trần lõi và kỳ hạn bình quân theo Table 2 [[src-bcbs-irrbb-2016#^irrbb-u05-4]] | NMD lõi xác định từ NMD ổn định, phân bổ đáp ứng Bảng 2 [[src-tt83-2025-nhnn#^pl5-a2-3a2]] | par 114–115; PL5.A.II.3.a | 01/07/2026 |
| Thời điểm không xác định | [cần nguồn] | Ngân hàng được dùng giả định do cấp có thẩm quyền phê duyệt [[src-tt83-2025-nhnn#^d54-4a]] | Đ54.4.a | 01/07/2026 |

Khác biệt: PL5 không quy định phần spread không tái định giá và lựa chọn trừ hay giữ commercial margin. Chi tiết ở [[notional-repricing-cash-flow]].

## Calibration
- Cú sốc dùng với repricing gap dựa vào kinh nghiệm, mô phỏng và đánh giá của ban điều hành; Lubinska ghi hướng dẫn quy định yêu cầu sốc song song ±200 bp cho phân tích này [[src-lubinska-alm-optimisation#^lubinska-u02-23]].
- Chu kỳ tái định giá của sản phẩm có thể là ước tính bình quân. Ví dụ Tata xếp mortgage kỳ hạn 60 tháng vào chu kỳ tái định giá 12 tháng, tài khoản tiết kiệm 36 tháng vào chu kỳ 6 tháng [[src-tata-bank-alm#^tata-gap-5]].
- Tại VN, khi không xác định được thời điểm ấn định lãi suất mới, giả định phải được cấp có thẩm quyền phê duyệt [[src-tt83-2025-nhnn#^d54-4a]].
- Tham số hành vi (tỷ lệ lõi NMD, CPR, TDRR) theo các node [[non-maturity-deposits]], [[behavioural-options]].

## Output & usage
**Ví dụ 1: ngân hàng mô hình của Tata** (tổng tài sản 500, vốn 50, không ghi đơn vị tiền tệ) [[src-tata-bank-alm#^tata-gap-4]]:

| Khoản mục | Quy mô | Kỳ hạn hợp đồng (tháng) | Chu kỳ tái định giá (tháng) | Nguồn |
|---|---|---|---|---|
| Bonds | 50 | 60 | 60 | [[src-tata-bank-alm#^tata-gap-4]] [[src-tata-bank-alm#^tata-gap-5]] |
| Loans | 300 | 6 | 6 | [[src-tata-bank-alm#^tata-gap-4]] [[src-tata-bank-alm#^tata-gap-5]] |
| Mortgages | 150 | 60 | 12 | [[src-tata-bank-alm#^tata-gap-4]] [[src-tata-bank-alm#^tata-gap-5]] |
| Term deposits | 150 | 3 | 3 | [[src-tata-bank-alm#^tata-gap-4]] [[src-tata-bank-alm#^tata-gap-5]] |
| Savings accounts | 200 | 36 | 6 | [[src-tata-bank-alm#^tata-gap-4]] [[src-tata-bank-alm#^tata-gap-5]] |
| Interbank deposits | 100 | 24 | 24 | [[src-tata-bank-alm#^tata-gap-4]] [[src-tata-bank-alm#^tata-gap-5]] |
| Equity | 50 | — | không phân bổ | [[src-tata-bank-alm#^tata-gap-4]] [[src-tata-bank-alm#^tata-gap-6]] |

| Dải (tháng) | <1 | 1–3 | 3–6 | 6–12 | 12–24 | 24–36 | 36–48 | 48–60 | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| Σ Tài sản | 0 | 0 | 300 | 150 | 0 | 0 | 0 | 50 | [[src-tata-bank-alm#^tata-gap-6]] |
| Σ Nợ | 0 | 150 | 200 | 0 | 100 | 0 | 0 | 0 | [[src-tata-bank-alm#^tata-gap-6]] |
| Net repricing gap | 0 | −150 | 100 | 150 | −100 | 0 | 0 | 50 | [[src-tata-bank-alm#^tata-gap-6]] |
| Periodic earning gap (1%) | 0 | −1,25 | 0,625 | 0,375 | | | | | [[src-tata-bank-alm#^tata-egap-1]] |

- **Góc EVE:** total repricing gap bằng 1,74, tức EVE giảm 1,74 khi lãi suất tăng 1%, tương đương 3,48% vốn cho mỗi 100 bp [[src-tata-bank-alm#^tata-gap-7]].
- **Góc NII năm đầu:** total earning gap bằng −0,25, tức NII năm đầu giảm 0,25 cho mỗi 1% lãi suất tăng song song [[src-tata-bank-alm#^tata-egap-2]].
- *Diễn giải:* khe hở luỹ kế tới 12 tháng (wiki tự cộng: −150 + 100 + 150 = +100) dương, nhưng NII năm đầu vẫn giảm khi lãi suất tăng. Khe hở âm ở dải 1–3 tháng chịu tác động gần trọn năm, còn khe hở dương ở dải 6–12 tháng chỉ chịu khoảng một phần tư năm. Vì vậy dấu của khe hở luỹ kế không đủ để kết luận chiều biến động NII.
- **Thêm swap:** receiver swap 3 năm, notional EUR 100, chân cố định 4,16%, chân thả nổi ban đầu 3,95% tái định giá 6 tháng [[src-tata-bank-alm#^tata-nii-15]], làm repricing gap phía giá trị kinh tế tăng từ 1,74 lên 3,63 [[src-tata-bank-alm#^tata-nii-10]]. *Diễn giải:* theo quy tắc reset date, chân nhận cố định rơi vào dải 24–36 tháng (RSA), chân trả thả nổi rơi vào dải 3–6 tháng (RSL).

**Ví dụ 2: gap report giản lược của Choudhry** (ngân hàng bán lẻ giả định, 200 triệu USD): RSA 20, RSL 100, gap tức thời −80, RSA/RSL 20%. Lãi suất +1% song song làm NII giảm 800.000 USD, tương đương EAR khoảng 7,8% [[src-choudhry-principles-banking#^choudhry-hedge-21]]. Xem [[structural-hedging]].

**Bất đối xứng thời điểm.** Mô phỏng NII 36 tháng của Tata: khi lãi suất giảm, tiền gửi kỳ hạn tái định giá sau 3 tháng nên tiết kiệm chi phí lãi sớm [[src-tata-bank-alm#^tata-nii-6]], còn mortgage không tái định giá trong năm tiếp theo nên thu nhập lãi giảm muộn hơn [[src-tata-bank-alm#^tata-nii-7]].

**Sử dụng trong quản trị:**
- ALCO thường nhận trình bày hằng tháng, so sánh NII thực tế với dự báo dưới dạng gap report theo bucket và sản phẩm [[src-choudhry-principles-banking#^choudhry-irr-3]]. Xem [[alco]].
- Trang MI "Basis Risk" phân loại tài sản và nợ theo cơ sở lãi suất (cố định theo kỳ, administered, Bank Base Rate, không chịu lãi) [[src-choudhry-principles-banking#^choudhry-alco-19]]. Xem [[basis-risk]].
- Refixing gap là công cụ cơ bản để đặt chiến lược phòng ngừa, ví dụ mua FRA cho nợ ròng refixing tập trung trong một tháng [[src-lubinska-alm-optimisation#^lubinska-u02-37]]. Xem [[forward-rate-agreement]].
- Đầu vào cho [[balance-sheet-optimisation-model]] và [[duration-gap-model]].

Phân tích theo câu hỏi: [[irrbb-principal-and-interest-cash-flows]], [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-transmission-mechanisms-to-nii-and-eve]], [[irrbb-commercial-margins-and-discount-curves]], [[irrbb-basis-risk-measurement-and-hedging]].

## Hạn chế & validation
| Hạn chế | Nội dung | Nguồn |
|---|---|---|
| Dịch chuyển song song | Gap analysis giả định lãi suất dịch chuyển song song; thực tế không song song, gây basis risk giữa tài sản ngắn và dài hạn | [[src-choudhry-principles-banking#^choudhry-irr-7]] |
| Basis risk | Tài sản và funding định giá theo hai lãi suất khác nhau (ví dụ prime rate và Libor) nên spread biến động, dù cùng dải | [[src-choudhry-principles-banking#^choudhry-irr-5]] [[src-choudhry-principles-banking#^choudhry-irrbb-4]] |
| Tái định giá giữa dải | Giả định tái định giá ở điểm giữa time bucket | [[src-choudhry-principles-banking#^choudhry-irr-7]] |
| Intra-bucket mismatch | Dòng tiền khác ngày trong cùng dải được coi là khớp hoàn toàn; BCBS giảm rủi ro này bằng 19 dải | [[src-bcbs-irrbb-2016#^irrbb-u05-22]] |
| Cùng hồ sơ rủi ro trong dải | Mọi giao dịch trong cùng dải được coi là có cùng hồ sơ rủi ro | [[src-lubinska-alm-optimisation#^lubinska-u02-24]] |
| Tĩnh | Chỉ xét giao dịch hiện có, không có nghiệp vụ mới; giả định tái đầu tư không đổi cấu trúc | [[src-lubinska-alm-optimisation#^lubinska-u02-24]] |
| Time value of money | Gap analysis không xét giá trị thời gian của tiền; time period đặt tuỳ ý | [[src-choudhry-principles-banking#^choudhry-irr-8]] |
| Hành vi | Bỏ qua prepayment và quyền chọn nếu chỉ dùng lịch hợp đồng | [[src-choudhry-principles-banking#^choudhry-irr-7]] |

Một số hạn chế khắc phục được bằng mô-đun mô phỏng NII [[src-lubinska-alm-optimisation#^lubinska-u02-24]]. Dù vậy gap analysis vẫn được dùng rộng rãi vì dữ liệu sẵn có từ báo cáo quy định, dễ tính và dễ giải thích cho lãnh đạo [[src-choudhry-principles-banking#^choudhry-irr-8]].

*Diễn giải:* kiểm định lịch tái định giá nên đối chiếu tổng số dư phân bổ với bảng cân đối kế toán (sau loại trừ), và kiểm tra giả định hành vi bằng backtest. Xem [[model-validation]].
