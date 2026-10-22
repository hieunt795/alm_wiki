---
title: "Các loại gap và truyền dẫn rủi ro bảng cân đối"
aliases: [Các loại gap và truyền dẫn rủi ro bảng cân đối, Balance Sheet Gaps and Risk Transmission, Truyền dẫn từ bảng cân đối tới NII EVE LCR NSFR LEV]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Mối quan hệ giữa Asset–Liability Mismatch, Funding Gap, Repricing Gap, Duration Gap, Liquidity Gap và Capital Consumption. · Cơ chế truyền dẫn từ thay đổi quy mô, kỳ hạn, lãi suất và cơ cấu bảng cân đối đến NII, EVE, LCR, NSFR, CAR và LEV."
as_of: 2026-10-22
sources: ["[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-bardaeva-alm]]", "[[src-bcbs-irrbb-2016]]", "[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-bcbs-lev]]", "[[src-bcbs-framework]]", "[[src-tt83-2025-nhnn]]", "[[src-tt50-2026-nhnn]]", "[[src-tata-bank-alm]]"]
relations: []
tags: [gap, repricing-gap, duration-gap, liquidity-gap, funding-gap, nii, eve, lcr, nsfr, leverage, capital, research]
updated: 2026-10-22
reviewed:
---

## Câu hỏi
Thuộc bộ "Balance Sheet Fundamentals & Risk Transmission" (6 câu). Cụm này trả lời:
- **Q3.** Mối quan hệ giữa Asset–Liability Mismatch, Funding Gap, Repricing Gap, Duration Gap, Liquidity Gap và Capital Consumption.
- **Q4.** Cơ chế truyền dẫn từ thay đổi quy mô, kỳ hạn, lãi suất và cơ cấu bảng cân đối đến NII, EVE, LCR, NSFR, CAR và LEV.

Nền về cấu trúc bảng cân đối và maturity transformation (Q1–Q2): [[balance-sheet-structure-and-transformation]]. Ví dụ định lượng (Q5–Q6): [[balance-sheet-synthetic-model-and-example]].

## Kết luận
- **Q3.** Các loại gap đều là cách đo cùng một mismatch tài sản – nợ theo những chiều khác nhau. Choudhry gọi chung là ALM gap, gồm liquidity gap (chênh lệch kỳ hạn) và interest-rate gap (chênh lệch cơ sở lãi suất) [[src-choudhry-principles-banking#^choudhry-almb-7]]. Repricing gap đo tác động lên NII trong gapping period [[src-lubinska-alm-optimisation#^lubinska-u02-23]]; duration gap đo tác động lên giá trị vốn [[src-lubinska-alm-optimisation#^lubinska-u02-45]]; funding gap đo phần cho vay khách hàng vượt tiền gửi khách hàng [[src-choudhry-principles-banking#^choudhry-strat-25]]. Hai gap có mục tiêu ngược nhau: liquidity gap nên luôn dương, interest-rate gap nên quanh 0 [[src-bardaeva-alm#^ch2-2]]. "Capital consumption" không có trong nguồn đã ingest; chuỗi có nguồn gần nhất là ΔEVE → $RWA_{IRRBB}$ → vốn kinh tế theo TT83 [[src-tt83-2025-nhnn#^pl6-1c]].
- **Q4.** Mỗi chỉ số phản ứng với một chiều khác nhau của thay đổi bảng cân đối: ΔNII theo repricing gap nhân thay đổi lãi suất [[src-lubinska-alm-optimisation#^lubinska-u02-23]]; ΔEVE theo duration gap [[src-lubinska-alm-optimisation#^lubinska-u02-47]]; LCR theo HQLA và dòng ra ròng 30 ngày [[src-bcbs-lcr#^lcr20-1]]; NSFR theo ASF/RSF [[src-bcbs-nsfr#^nsf20-2]]; LEV theo Vốn cấp 1 chia quy mô phơi nhiễm [[src-bcbs-lev#^lev20-3]]. Vì vậy một thay đổi có thể cải thiện chỉ số này và làm xấu chỉ số khác, như tăng đệm thanh khoản làm giảm NII và NIM [[src-choudhry-principles-banking#^choudhry-nim-5]]. CAR chưa phân tích được vì wiki thiếu định nghĩa và hệ số rủi ro của TT14 [cần nguồn].

## Cơ chế

### Q3 — Quan hệ giữa các loại gap

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[repricing-gap-analysis]] | measures | [[gap-risk]] | | [[src-lubinska-alm-optimisation#^lubinska-u02-30]] |
| [[repricing-gap-analysis]] | input-to | [[net-interest-income-sensitivity]] | | [[src-lubinska-alm-optimisation#^lubinska-u02-23]] |
| [[duration-gap-model]] | measures | [[gap-risk]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-7]] |
| [[duration-gap-model]] | input-to | [[economic-value-of-equity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-5]] |
| [[repricing-balance-sheet]] | input-to | [[duration-gap-model]] | | [[src-tata-bank-alm#^tata-dgap-1]] |
| [[contractual-maturity-mismatch]] | input-to | [[lcr]] | | [[src-bcbs-framework#^srp50-2]] |
| [[contractual-maturity-mismatch]] | input-to | [[nsfr]] | | [[src-bcbs-framework#^srp50-2]] |
| [[economic-value-of-equity]] | input-to | [[rwa-irrbb]] | | [[src-tt83-2025-nhnn#^pl6-1c]] |
| [[rwa-irrbb]] | part-of | [[economic-capital]] | | [[src-tt83-2025-nhnn#^pl6-1b]] |

Không có cạnh nối trực tiếp [[repricing-gap-analysis]] với [[duration-gap-model]] (cùng đầu vào là [[repricing-balance-sheet]], khác tầm thời gian), và không có cạnh nối [[loan-to-deposit-ratio]] với [[lcr]] hay [[nsfr]] [cần nguồn].

**Bản đồ các loại gap** (mỗi dòng có nguồn riêng):

| Gap | Đo cái gì | Công thức / dấu | Nguồn |
|---|---|---|---|
| ALM gap (asset–liability mismatch) | Chênh lệch kỳ hạn và chênh lệch cơ sở lãi suất giữa tài sản và nợ | Gồm liquidity gap và interest-rate gap | [[src-choudhry-principles-banking#^choudhry-almb-7]] |
| Liquidity gap | Chênh lệch kỳ hạn tài sản – nợ tại từng điểm của cấu trúc kỳ hạn; mỗi điểm có gap là một funding gap risk | Static / dynamic / marginal gap | [[src-choudhry-principles-banking#^choudhry-lgap-1]] [[src-choudhry-principles-banking#^choudhry-lgap-3]] |
| Contractual maturity mismatch | Dòng tiền vào/ra theo hợp đồng của nội bảng và ngoại bảng, xếp theo kỳ hạn hợp đồng còn lại | Thang 13 dải, không tái tục nợ | [[src-bcbs-framework#^srp50-6]] [[src-bcbs-framework#^srp50-7]] [[src-bcbs-framework#^srp50-9]] |
| Funding gap (customer) | Phần cho vay khách hàng không được tiền gửi khách hàng tài trợ | Cho vay KH − tiền gửi KH; tỷ lệ tương ứng là LTD | [[src-choudhry-principles-banking#^choudhry-strat-25]] |
| Repricing gap | Tài sản nhạy lãi suất trừ nợ nhạy lãi suất trong một dải | $GAP>0$: rủi ro tái đầu tư; $GAP<0$: rủi ro tái cấp vốn | [[src-lubinska-alm-optimisation#^lubinska-u02-23]] [[src-lubinska-alm-optimisation#^lubinska-u02-26]] |
| Duration gap | Độ nhạy giá trị vốn | $DGAP = D_A - w D_L$, $w = L/A$ | [[src-lubinska-alm-optimisation#^lubinska-u02-45]] |

Repricing gap và ΔNII:

$$
\Delta NII \approx GAP \times \Delta i, \qquad GAP = RSA - RSL
$$
[[src-lubinska-alm-optimisation#^lubinska-u02-23]]

Công thức trên do [[repricing-gap-analysis]] dựng lại từ lời văn của nguồn vì raw mất công thức; xem ghi chú ở node đó.

Duration gap và giá trị vốn: ví dụ của Lubinska với DGAP 1 năm, tổng tài sản 1.000 euro, lãi suất tăng 200 bp cho giá trị thị trường của vốn giảm 20 euro, tức $1000 \times 2\%$ [[src-lubinska-alm-optimisation#^lubinska-u02-47]]. Ví dụ miễn nhiễm: $D_A$ 4,17 năm, $D_L$ 1 năm, tỷ lệ nợ/tài sản 0,9 cho DGAP 3,27 năm [[src-lubinska-alm-optimisation#^lubinska-u02-46]].

$$
\Delta E \approx -DGAP \times A \times \Delta y
$$
[[src-lubinska-alm-optimisation#^lubinska-u02-47]]

**Hai gap lãi suất nói khác nhau về cùng bảng cân đối.** Ngân hàng trong ví dụ của Lubinska có tổng repricing gap ngắn hạn 500MM, nên nhạy tài sản và NII 12 tháng tăng khi lãi suất tăng. Ở phần trung–dài hạn, ngân hàng lại ở vị thế nợ ròng, nên lãi suất tăng làm EVE tăng; khác biệt giữa hai thước đo là tầm thời gian [[src-lubinska-alm-optimisation#^lubinska-u02-27]]. Basel cảnh báo cùng điều: chỉ triệt rủi ro EV bằng cách khớp tái định giá ngoài kỳ hạn ngắn có thể làm thu nhập biến động [[src-bcbs-irrbb-2016#^irrbb-u02-4]].

**Liquidity gap khác interest-rate gap về mục tiêu.** Liquidity gap nên dương ở mọi thời điểm; interest-rate gap lý tưởng là quanh 0 hoặc trong hạn mức của risk appetite statement [[src-bardaeva-alm#^ch2-2]]. Nhu cầu funding tương lai (liquidity gap âm) cũng là nguồn rủi ro lãi suất, vì ngân hàng không biết lãi suất sẽ phải trả [[src-choudhry-principles-banking#^choudhry-almb-9]].

**Capital consumption** [cần nguồn cho thuật ngữ]. Chuỗi có nguồn theo TT83:

$$
C_E = RWA^*_E \times CAR_{Target} + \Delta RWA_B \times CAR_R
$$
[[src-tt83-2025-nhnn#^pl6-1a]]

- $RWA_{IRRBB}$ là một cấu phần của $RWA^*_E$ [[src-tt83-2025-nhnn#^pl6-1b]], và chậm nhất từ 01/01/2028 phải tính theo ΔEVE [[src-tt83-2025-nhnn#^pl6-1c]]. Xem [[rwa-irrbb]], [[economic-capital]].
- Basel: vốn cho IRRBB xét trong ICAAP theo rủi ro giá trị kinh tế [[src-bcbs-irrbb-2016#^irrbb-p09-2]].
- PL6 không nêu cách quy đổi ΔEVE thành RWA [cần nguồn].

*Diễn giải:* như vậy duration gap là gap duy nhất có đường nối có nguồn tới vốn (DGAP → ΔEVE → $RWA_{IRRBB}$ → $C_E$). Funding gap và liquidity gap chỉ nối tới vốn qua CAR của rủi ro tín dụng, phần này chưa có nguồn (ngoài wiki, chưa có nguồn).

### Q4 — Truyền dẫn tới NII, EVE, LCR, NSFR, CAR, LEV

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[gap-risk]] | drives | [[net-interest-margin]] | − · rising_rate | [[src-choudhry-principles-banking#^choudhry-hedge-1]] |
| [[gap-risk]] | input-to | [[net-interest-income-sensitivity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-4]] |
| [[gap-risk]] | input-to | [[economic-value-of-equity]] | | [[src-bcbs-irrbb-2016#^irrbb-u06-4]] |
| [[behavioural-options]] | drives | [[economic-value-of-equity]] | − · falling_rate | [[src-bcbs-irrbb-2016#^irrbb-u05-5]] |
| [[hqla]] | drives | [[lcr]] | + | [[src-bcbs-lcr#^lcr20-1]] |
| [[hqla]] | drives | [[net-interest-margin]] | − | [[src-choudhry-principles-banking#^choudhry-nim-5]] |
| [[run-off-rate]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-1]] |
| [[committed-facilities]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-64]] |
| [[available-stable-funding]] | drives | [[nsfr]] | + | [[src-bcbs-nsfr#^nsf20-2]] |
| [[required-stable-funding]] | drives | [[nsfr]] | − | [[src-bcbs-nsfr#^nsf20-2]] |
| [[rsf-loans-and-credit-exposures]] | drives | [[nsfr]] | − | [[src-bcbs-nsfr#^nsf30-31]] |
| [[leverage-exposure-measure]] | drives | [[leverage-ratio]] | − | [[src-bcbs-lev#^lev20-3]] |
| [[economic-value-of-equity]] | input-to | [[rwa-irrbb]] | | [[src-tt83-2025-nhnn#^pl6-1c]] |
| [[hqla]] | drives | [[leverage-ratio]] | − | *Diễn giải:* (ngoài wiki, chưa có nguồn); qua EM, xem dưới |
| tài sản có rủi ro tín dụng | drives | CAR | − | [cần nguồn] (TT14 C1, C2-M2) |

**Công thức các chỉ số đích:**

| Chỉ số | Công thức | Ngưỡng VN | Nguồn |
|---|---|---|---|
| NII, NIM | NII = thu nhập lãi − chi phí lãi; NIM = NII / tài sản sinh lãi | Không có | [[src-choudhry-principles-banking#^choudhry-nim-2]] |
| ΔNII | 1 năm, constant balance sheet, sốc song song tăng và giảm | Phải có hạn mức nội bộ | [[src-tt83-2025-nhnn#^pl5-b2]] [[src-tt83-2025-nhnn#^pl5-b3]] [[src-tt83-2025-nhnn#^d53-2]] |
| ΔEVE | Thay đổi PV ròng của dòng tiền tài sản và nợ nhạy lãi suất | Phải có hạn mức nội bộ | [[src-tt83-2025-nhnn#^pl5-a-0]] [[src-tt83-2025-nhnn#^d53-2]] |
| LCR | HQLA / dòng tiền ra ròng 30 ngày | LCR quy VNĐ riêng lẻ 50% từ 01/10/2028, lên 100% từ 01/10/2033 | [[src-tt50-2026-nhnn#^d16-1]] [[src-tt50-2026-nhnn#^d16-1c]] |
| NSFR | ASF / RSF | 90% từ 01/10/2028, 95% từ 01/10/2029, 100% từ 01/10/2030 | [[src-tt50-2026-nhnn#^d22-1]] [[src-tt50-2026-nhnn#^d22-2]] |
| LEV | Vốn cấp 1 / EM | Không có ngưỡng cố định; Thống đốc quyết định khi cần | [[src-tt50-2026-nhnn#^d8-1]] |
| CAR | [cần nguồn] | [cần nguồn] | TT14 C1 chưa ingest |

Dòng tiền ra ròng là dòng ra kỳ vọng trừ dòng vào kỳ vọng trong 30 ngày stress; dòng vào bị chặn ở 75% dòng ra [[src-bcbs-lcr#^lcr40-1]]. EM gồm mọi tài sản trên Báo cáo tình hình tài chính và cam kết ngoại bảng, tính theo giá trị kế toán, không bù trừ tài sản với nợ [[src-tt50-2026-nhnn#^pl3-1]] [[src-tt50-2026-nhnn#^pl3-3]].

**Ma trận truyền dẫn.** Mỗi ô có nguồn cho tham số; chiều tổng hợp là suy luận từ công thức.

| Thay đổi | NII / NIM | ΔEVE | LCR | NSFR | LEV |
|---|---|---|---|---|---|
| **Quy mô:** tăng tài sản tài trợ bằng nợ mới | NII có thể tăng trong khi NIM giảm, nếu nghiệp vụ mới kém sinh lời hơn [[src-choudhry-principles-banking#^choudhry-nim-8]] | Phụ thuộc DGAP của phần tăng thêm [[src-lubinska-alm-optimisation#^lubinska-u02-45]] | Phụ thuộc run-off của nợ mới và HQLA tạo ra [[src-bcbs-lcr#^lcr40-1]] | ASF của nợ mới so với RSF của tài sản mới [[src-bcbs-nsfr#^nsf20-2]] | EM tăng theo giá trị kế toán của tài sản mới [[src-tt50-2026-nhnn#^pl3-3]] |
| **Kỳ hạn tài sản:** cho vay kéo dài từ dưới 1 năm lên từ 1 năm | Theo repricing gap của dải mới [[src-lubinska-alm-optimisation#^lubinska-u02-23]] | $D_A$ tăng làm DGAP tăng [[src-lubinska-alm-optimisation#^lubinska-u02-45]] | Ít tác động trực tiếp *Diễn giải* | RSF tăng: cho vay từ 1 năm RW > 35% chịu 85% [[src-bcbs-nsfr#^nsf30-31]] | Không đổi nếu số dư không đổi *Diễn giải* |
| **Kỳ hạn nợ:** kéo dài nợ lên từ 1 năm | Chi phí funding cao hơn *Diễn giải* | $D_L$ tăng làm DGAP giảm [[src-lubinska-alm-optimisation#^lubinska-u02-46]] | Dòng ra 30 ngày giảm khi nợ không đến hạn trong kỳ [[src-bcbs-lcr#^lcr40-1]] | ASF 100% cho nợ từ 1 năm [[src-bcbs-nsfr#^nsf30-10]] | Không đổi |
| **Lãi suất:** sốc song song | $\Delta NII \approx GAP \times \Delta i$ [[src-lubinska-alm-optimisation#^lubinska-u02-23]] | $\Delta E \approx -DGAP \times A \times \Delta y$ [[src-lubinska-alm-optimisation#^lubinska-u02-47]] | [cần nguồn] cho kênh giá HQLA | Không phụ thuộc trực tiếp *Diễn giải* | Không phụ thuộc trực tiếp *Diễn giải* |
| **Cơ cấu:** thêm đệm HQLA £1,5bn (case ChoudWest) | NII −£45m, NIM −0,50 điểm % [[src-choudhry-principles-banking#^choudhry-nim-5]] | Phụ thuộc duration của HQLA *Diễn giải* | Tử số tăng [[src-bcbs-lcr#^lcr20-1]] | RSF thấp: Level 1 chịu 5% [[src-bcbs-nsfr#^nsf30-26]] | EM tăng [[src-tt50-2026-nhnn#^pl3-1]] |
| **Cơ cấu:** thay tiền gửi bán lẻ ổn định bằng vay liên ngân hàng dưới 6 tháng | [cần nguồn] cho chênh lệch lãi suất | Phụ thuộc kỳ tái định giá *Diễn giải* | Run-off bán lẻ ổn định 5% [[src-bcbs-lcr#^lcr40-7]] so với 100% cho vốn không đảm bảo từ ngân hàng đến hạn trong 30 ngày [[src-bcbs-lcr#^lcr40-42]] [[src-bcbs-lcr#^lcr40-20]] | ASF 95% [[src-bcbs-nsfr#^nsf30-11]] xuống 0% [[src-bcbs-nsfr#^nsf30-14]] | Không đổi |
| **Ngoại bảng:** tăng cam kết tín dụng chưa rút | Không đổi đến khi giải ngân *Diễn giải* | Có, nếu cam kết có lãi suất cố định *Diễn giải* | Dòng ra theo drawdown rate [[src-bcbs-lcr#^lcr40-64]] | RSF 5% phần chưa rút [[src-bcbs-nsfr#^nsf30-34]] | $E_{off} \times CCF$ [[src-tt50-2026-nhnn#^pl3-9]] |

*Diễn giải:* ô ghi "*Diễn giải*" là suy luận từ công thức của chỉ số, không phải claim của nguồn (ngoài wiki, chưa có nguồn).

**Truyền dẫn lãi suất qua hành vi.** Tốc độ trả trước tăng khi lãi suất giảm và giảm khi lãi suất tăng [[src-bcbs-irrbb-2016#^irrbb-u05-5]]; tỷ lệ rút tiền gửi có kỳ hạn trước hạn đổi theo kịch bản [[src-bcbs-irrbb-2016#^irrbb-u05-6]]. Khối lượng cũng phản ứng: trong 2021–2023 lãi suất tăng làm tiền gửi không kỳ hạn của MFI Đức giảm từ 29,3% xuống 26,1% tổng tài sản [[src-tata-bank-alm#^tata-prac-2]]. Biên lãi cũng đổi theo lãi suất: Cruz-García và cộng sự ước tính biên biến động khoảng 19 bp cho mỗi 100 bp lãi suất ngắn hạn [[src-tata-bank-alm#^tata-niip-5]]. Vì vậy công thức gap tĩnh ở trên đánh giá thấp truyền dẫn trong kịch bản lãi suất lớn.

**CAR** [cần nguồn]. Wiki chưa có định nghĩa CAR, ngưỡng tối thiểu và hệ số rủi ro tín dụng theo TT14/2025. Hai điểm có nguồn:
- $CAR_R$ là tỷ lệ an toàn vốn theo quy định NHNN và là một tham số của vốn kinh tế [[src-tt83-2025-nhnn#^pl6-1a]];
- Vốn cấp 1 của LEV xác định theo quy định tỷ lệ an toàn vốn mà ngân hàng đang áp dụng [[src-tt50-2026-nhnn#^d8-1]], nên lợi nhuận giữ lại từ NII là kênh nối NII với cả CAR và LEV *Diễn giải* (ngoài wiki, chưa có nguồn).

## Bằng chứng ủng hộ
- Công thức repricing gap và duration gap có nguồn T4 (Lubinska), ví dụ số cụ thể [[src-lubinska-alm-optimisation#^lubinska-u02-46]] [[src-lubinska-alm-optimisation#^lubinska-u02-47]]. Giả định của gap analysis (dịch chuyển song song, tái định giá ở giữa dải, không trả trước) do Choudhry nêu [[src-choudhry-principles-banking#^choudhry-irr-7]].
- Công thức LCR, NSFR, LEV và hệ số ASF/RSF, run-off có nguồn T2 (BCBS) và T1 (TT50).
- Chuỗi ΔEVE → $RWA_{IRRBB}$ → vốn kinh tế có nguồn T1 (TT83 PL6).

## Bằng chứng trái chiều
- Repricing gap và duration gap có thể cho chiều ngược nhau trên cùng bảng cân đối [[src-lubinska-alm-optimisation#^lubinska-u02-27]]; không phải mâu thuẫn giữa nguồn mà là khác tầm thời gian.
- DGAP bỏ qua trả nợ trước hạn và chỉ đúng với sốc nhỏ, song song [[src-lubinska-alm-optimisation#^lubinska-u02-48]]. Gap management giả định có thể đổi cấu trúc sổ dễ dàng, điều Choudhry nói khó làm trong ngắn hạn [[src-choudhry-principles-banking#^choudhry-lgap-10]].
- Node [[lcr-nsfr-interlinkages]] có hai cạnh `drives` tới [[economic-value-of-equity]] và [[net-interest-income-sensitivity]] nhưng cite [[src-bcbs-irrbb-2016#^irrbb-p12-1]] và [[src-bcbs-irrbb-2016#^irrbb-u02-4]], hai đoạn không nói về LCR hay NSFR. Synthesis này không dùng hai cạnh đó.

## Phụ thuộc regime
- **Lãi suất tăng:** gap âm (liability sensitive) làm NII giảm [[src-choudhry-principles-banking#^choudhry-irrbb-5]]; DGAP dương làm giá trị vốn giảm [[src-lubinska-alm-optimisation#^lubinska-u02-47]]. Trả trước giảm [[src-bcbs-irrbb-2016#^irrbb-u05-5]].
- **Lãi suất giảm:** trả trước tăng làm EVE giảm [[src-bcbs-irrbb-2016#^irrbb-u05-5]]; gap dương làm NII giảm [[src-lubinska-alm-optimisation#^lubinska-u02-26]].
- **Stress thanh khoản:** LCR dùng kịch bản 30 ngày kết hợp cú sốc riêng và cú sốc toàn thị trường [[src-bcbs-lcr#^lcr20-2]]; NSFR đo trong tầm 1 năm [[src-bcbs-nsfr#^nsf20-2]].
- **Jurisdiction:** VN áp LCR, NSFR riêng lẻ với lộ trình từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]]; LEV chưa có ngưỡng [[src-tt50-2026-nhnn#^d8-1]]; IRRBB dùng ΔNII hoặc ΔEVE đến hết 2027 và cả hai chậm nhất từ 01/01/2028 [[src-tt83-2025-nhnn#^d74-4a]] [[src-tt83-2025-nhnn#^d74-4b]].

## Hàm ý ALM / quy định
- **Nghĩa vụ NHNN (T1):** hạn mức ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-2]]; chiến lược IRRBB gồm nguyên tắc quản lý theo repricing gap profile [[src-tt83-2025-nhnn#^d53-1a1]]; LCR và NSFR theo lộ trình TT50; $RWA_{IRRBB}$ trong vốn kinh tế ICAAP [[src-tt83-2025-nhnn#^pl6-1c]].
- **Tham chiếu Basel (T2):** ngưỡng 100% cho LCR, NSFR [[src-bcbs-lcr#^lcr20-5]] [[src-bcbs-nsfr#^nsf20-2]] và 3% cho LEV [[src-bcbs-lev#^lev20-7]] không phải nghĩa vụ tại VN; phép thử outlier 15% Tier 1 không có trong TT83 [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
- **Chưa có nguồn NHNN trong wiki** về CAR (TT14/2025) và về ngưỡng funding gap.
- *Diễn giải:* ALCO nên đánh giá mọi đề xuất thay đổi bảng cân đối trên cả năm chỉ số cùng lúc theo ma trận ở trên, vì cải thiện một chỉ số thường đổi bằng chỉ số khác. Ví dụ đệm HQLA cải thiện LCR nhưng giảm NII, NIM và LEV (ngoài wiki, chưa có nguồn).

## Bất định
- **CAR** [cần nguồn]: cần `/ingest src-tt14-2025-nhnn C1` (định nghĩa, ngưỡng) và `C2-M2` (hệ số rủi ro). Gỡ Q3 (capital consumption), Q4 (CAR).
- **Capital consumption:** thuật ngữ không có trong nguồn; phần trên dùng chuỗi vốn kinh tế TT83.
- **Kênh giá HQLA → LCR:** node [[lcr]] nêu HQLA định giá theo giá thị trường (LCR30.40) nhưng câu đó không có citation. Cần rà bằng `python tools/citations.py --node lcr`.
- **LDR và LCR/NSFR:** không có cạnh nối [[loan-to-deposit-ratio]] với chỉ số thanh khoản; chưa có nguồn.
- **Cạnh `gap-risk` và `duration-gap-model` —drives(−, rising_rate)→ `economic-value-of-equity`** cite [[src-bcbs-irrbb-2016#^irrbb-u07-1]], đoạn chỉ liệt kê sáu kịch bản sốc. Chiều tác động ở synthesis này dùng [[src-lubinska-alm-optimisation#^lubinska-u02-47]] thay thế. Đề xuất /lint.
- Bảng truyền dẫn giả định khoản vay liên ngân hàng dưới 6 tháng đến hạn trong 30 ngày; nếu đến hạn sau 30 ngày thì không có dòng ra LCR [[src-bcbs-lcr#^lcr40-20]].
