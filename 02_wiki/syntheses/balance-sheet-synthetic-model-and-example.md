---
title: "Bảng cân đối giả định: phương pháp và ví dụ định lượng"
aliases: [Bảng cân đối giả định, Synthetic Balance Sheet, Synthetic balance sheet model and worked example, Mô phỏng bảng cân đối]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Phương pháp xây dựng Synthetic Balance Sheet để mô phỏng dòng tiền, rủi ro, lợi nhuận và các giới hạn an toàn. · Xây dựng một bảng cân đối giả định, chứng minh bằng công thức và ví dụ định lượng cách một thay đổi trong tài sản hoặc nguồn vốn tác động đồng thời đến lợi nhuận và rủi ro."
as_of: 2026-10-22
sources: ["[[src-lubinska-alm-optimisation]]", "[[src-choudhry-principles-banking]]", "[[src-tata-bank-alm]]", "[[src-bcbs-irrbb-2016]]", "[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-bcbs-lev]]", "[[src-bcbs-framework]]", "[[src-tt83-2025-nhnn]]", "[[src-tt50-2026-nhnn]]"]
relations: []
tags: [synthetic-balance-sheet, simulation, nii, eve, lcr, nsfr, leverage, worked-example, research]
updated: 2026-10-22
reviewed:
---

## Câu hỏi
Thuộc bộ "Balance Sheet Fundamentals & Risk Transmission" (6 câu). Cụm này trả lời:
- **Q5.** Phương pháp xây dựng Synthetic Balance Sheet để mô phỏng dòng tiền, rủi ro, lợi nhuận và các giới hạn an toàn.
- **Q6.** Xây dựng một bảng cân đối giả định, chứng minh bằng công thức và ví dụ định lượng cách một thay đổi trong tài sản hoặc nguồn vốn tác động đồng thời đến lợi nhuận và rủi ro.

Nền: [[balance-sheet-structure-and-transformation]] (Q1–Q2), [[balance-sheet-gaps-and-risk-transmission]] (Q3–Q4).

## Kết luận
- **Q5.** Nguồn đã ingest không dùng thuật ngữ "synthetic balance sheet" [cần nguồn]. Phương pháp có nguồn được ghép từ ba khối: lịch tái định giá và lịch kỳ hạn hợp đồng để sinh dòng tiền [[src-tata-bank-alm#^tata-gap-1]] [[src-bcbs-framework#^srp50-7]]; kế hoạch khối lượng, biên lãi và kịch bản lãi suất để sinh NII [[src-tata-bank-alm#^tata-niip-3]] [[src-tata-bank-alm#^tata-niip-4]]; và bài toán tối ưu với hạn mức NII, thanh khoản làm ràng buộc bất đẳng thức [[src-lubinska-alm-optimisation#^lubinska-u04-12]]. Giả định bảng cân đối phải khớp mục đích: run-off cho ΔEVE, constant cho ΔNII [[src-bcbs-irrbb-2016#^irrbb-p08-2]] [[src-bcbs-irrbb-2016#^irrbb-p08-3]]. Kế hoạch ALM phải dự phóng cả LCR, NSFR và yêu cầu vốn [[src-tata-bank-alm#^tata-niip-6]].
- **Q6.** Ví dụ dưới đây dùng bảng cân đối 1.000 tỷ đồng, số dư và lãi suất do wiki giả định, tham số quy định có nguồn. Tăng 100 tỷ cho vay cố định dài hạn, tài trợ bằng vay liên ngân hàng dưới 30 ngày, làm NII tăng 4,0 tỷ và NIM tăng 0,04 điểm %. Cùng lúc, LCR giảm từ 108,7% xuống 70,4%, NSFR từ 140,9% xuống 122,5%, LEV từ 8,0% xuống 7,3%. ΔNII khi lãi suất +200 bp xấu đi từ −5,1 tỷ xuống −7,0 tỷ, và ΔE theo duration gap xấu đi từ −26,9 tỷ xuống −30,8 tỷ. CAR không tính được vì thiếu nguồn TT14 [cần nguồn].

## Cơ chế

### Q5 — Phương pháp xây dựng bảng cân đối giả định

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[irrbb-balance-sheet-portfolios]] | input-to | [[repricing-balance-sheet]] | | [[src-tata-bank-alm#^tata-gap-1]] |
| [[repricing-balance-sheet]] | input-to | [[balance-sheet-optimisation-model]] | | [[src-lubinska-alm-optimisation#^lubinska-u04-13]] |
| [[repricing-balance-sheet]] | input-to | [[duration-gap-model]] | | [[src-tata-bank-alm#^tata-dgap-1]] |
| [[repricing-balance-sheet]] | input-to | [[net-interest-income-sensitivity]] | | [[src-lubinska-alm-optimisation#^lubinska-u02-23]] |
| [[nii-planning]] | input-to | [[net-interest-income-sensitivity]] | | [[src-tata-bank-alm#^tata-nii-3]] |
| [[contractual-maturity-mismatch]] | input-to | [[lcr]] | | [[src-bcbs-framework#^srp50-2]] |
| [[lcr]] | limits | [[balance-sheet-optimisation-model]] | | [[src-lubinska-alm-optimisation#^lubinska-u04-12]] |
| [[nsfr]] | limits | [[balance-sheet-optimisation-model]] | | [[src-lubinska-alm-optimisation#^lubinska-u04-12]] |
| [[net-interest-income-sensitivity]] | input-to | [[balance-sheet-optimisation-model]] | | [[src-lubinska-alm-optimisation#^lubinska-u04-12]] |

**Các bước** (mỗi bước có nguồn cho nội dung; thứ tự là cách wiki sắp xếp):

| Bước | Nội dung | Nguồn |
|---|---|---|
| 1. Phân nhóm vị thế | Xếp vị thế nhạy lãi suất vào ba nhóm theo khả năng chuẩn hoá dòng tiền, theo từng đồng tiền | [[src-bcbs-irrbb-2016#^irrbb-u05-1]] |
| 2. Lịch tái định giá | Khoản cố định theo ngày đáo hạn, khoản thả nổi theo thời gian tới lần tái định giá kế tiếp | [[src-tata-bank-alm#^tata-gap-1]] |
| 3. Lịch kỳ hạn hợp đồng | Dòng tiền vào/ra theo hợp đồng của nội bảng và ngoại bảng, 13 dải; không tái tục nợ, không tài sản mới | [[src-bcbs-framework#^srp50-7]] [[src-bcbs-framework#^srp50-9]] |
| 4. Giả định hành vi | NMD core/non-core có trần; CPR và TDRR nhân hệ số theo kịch bản | [[src-bcbs-irrbb-2016#^irrbb-u05-4]] [[src-bcbs-irrbb-2016#^irrbb-u05-5]] [[src-bcbs-irrbb-2016#^irrbb-u05-6]] |
| 5. Kế hoạch khối lượng | Lập theo từng mảng vì run-off khác nhau; run-off là hàm của lãi suất và hành vi; cộng nghiệp vụ mới | [[src-tata-bank-alm#^tata-niip-4]] |
| 6. Kế hoạch biên lãi | Theo từng mảng, có margin compression; nếu dùng margin-beta thì biên đổi theo kịch bản | [[src-tata-bank-alm#^tata-niip-5]] |
| 7. Kịch bản lãi suất | Kịch bản cơ sở theo lãi suất spot hoặc forward; khối lượng và biên nhất quán với từng kịch bản | [[src-tata-bank-alm#^tata-niip-3]] |
| 8. Sốc chuẩn hoá | Sáu kịch bản cho EVE, hai kịch bản song song cho NII | [[src-bcbs-irrbb-2016#^irrbb-u07-1]] |
| 9. Kịch bản thanh khoản | Đặc thù ngân hàng, toàn hệ thống, hỗn hợp | [[src-tt83-2025-nhnn#^d48-2]] |
| 10. Ràng buộc và tối ưu | Hạn mức NII và tỷ lệ thanh khoản là bất đẳng thức; hai hàm mục tiêu: tối đa thu nhập tài sản, tối thiểu chi phí vốn | [[src-lubinska-alm-optimisation#^lubinska-u04-12]] [[src-lubinska-alm-optimisation#^lubinska-u04-13]] |

**Giả định bảng cân đối theo mục đích.**

| Mục đích | Giả định | Nguồn |
|---|---|---|
| ΔEVE | Run-off balance sheet; loại vốn chủ sở hữu | [[src-bcbs-irrbb-2016#^irrbb-p08-2]] |
| ΔNII (Basel) | Constant balance sheet, khoản đáo hạn thay bằng khoản cùng số dư, kỳ tái định giá, spread; rolling 12 tháng | [[src-bcbs-irrbb-2016#^irrbb-p08-3]] |
| ΔNII (VN) | 01 năm, constant balance sheet | [[src-tt83-2025-nhnn#^pl5-b2]] |
| Kế hoạch ALM | Khối lượng theo phân khúc hành vi lãi suất, kỳ hạn nghiệp vụ mới; dự phóng EVE, NII, LCR, NSFR, yêu cầu vốn | [[src-tata-bank-alm#^tata-niip-6]] |
| Tối ưu (Lubinska) | Constant balance sheet, tái tục khoản đáo hạn hoặc tái định giá | [[src-lubinska-alm-optimisation#^lubinska-u04-13]] |

**Cấp độ dữ liệu.** Mô hình bottom-up dùng thuộc tính từng tài sản, nợ (số dư, biên trên reference rate, lịch trả nợ, kỳ hạn) cộng dự báo reference rate và nghiệp vụ mới; sốc lãi suất rồi tính lại để có độ nhạy NII [[src-choudhry-principles-banking#^choudhry-nim-13]]. Thách thức chính là luồng dữ liệu cấp tài khoản và chất lượng dữ liệu [[src-choudhry-principles-banking#^choudhry-nim-13]]. Sai số của dự báo NII cơ sở phần lớn triệt tiêu khi lấy hiệu số giữa kịch bản sốc và kịch bản cơ sở [[src-tata-bank-alm#^tata-nii-3]].

**Giới hạn an toàn đưa vào mô hình.**
- VN (T1): hạn mức ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-2]]; LCR quy VNĐ riêng lẻ theo lộ trình 50% → 100% [[src-tt50-2026-nhnn#^d16-1c]]; NSFR 90% → 100% [[src-tt50-2026-nhnn#^d22-2]]; LEV chưa có ngưỡng [[src-tt50-2026-nhnn#^d8-1]].
- Basel (T2, tham chiếu): LCR ≥ 100% [[src-bcbs-lcr#^lcr20-5]], NSFR ≥ 100% [[src-bcbs-nsfr#^nsf20-2]], LEV ≥ 3% [[src-bcbs-lev#^lev20-7]].
- Nội bộ (ví dụ của nguồn T4): trần tập trung 80% cho mỗi nguồn vốn [[src-lubinska-alm-optimisation#^lubinska-u05-11]].

**Phương pháp giải.** Hàm tuyến tính dùng linear programming (simplex); phi tuyến dùng Lagrange multiplier; phi tuyến nhiều biến với ràng buộc bất đẳng thức dùng interior-point [[src-choudhry-principles-banking#^choudhry-opt-3]] [[src-choudhry-principles-banking#^choudhry-opt-4]]. Choudhry đối lập cách quản lý tích hợp thanh khoản và IRRBB với cách quản lý silo phổ biến [[src-choudhry-principles-banking#^choudhry-opt-6]]. Chi tiết: [[balance-sheet-optimisation-model]].

**Kiểm định.** Độ phức tạp không cần thiết làm tăng rủi ro mô hình [[src-lubinska-alm-optimisation#^lubinska-u05-12]]; mô hình phải qua effective challenge [[src-lubinska-alm-optimisation#^lubinska-u05-15]]. Xem [[model-risk-management]].

### Q6 — Bảng cân đối giả định và ví dụ định lượng

**Bảng cân đối cơ sở** (đơn vị: tỷ đồng). Cột số dư, lãi suất và duration là **giả định của wiki**, không phải số liệu của nguồn. Cột hệ số quy định có nguồn ở bảng tham số kế tiếp.

| Khoản mục | Số dư | Lãi suất | $D_{mod}$ (năm) | Tái định giá trong 12 tháng | HQLA / run-off | ASF / RSF |
|---|---|---|---|---|---|---|
| Tiền mặt, tiền gửi DTBB tại NHNN | 40 | 0% | 0 | Không nhạy lãi suất | Không tính HQLA (giả định thận trọng) | RSF 0% |
| TPCP VNĐ | 200 | 4,0% | 3,0 | Không (cố định > 1 năm) | HQLA cấp 1 | RSF 5% |
| Cho vay DN ngắn hạn, thả nổi 3 tháng | 260 | 8,0% | 0,2 | Dải 1–3 tháng | Không có dòng vào 30 ngày (giả định) | RSF 50% |
| Cho vay trung dài hạn cố định ≥ 1 năm (giả định RW > 35%) | 500 | 9,0% | 2,0 | Không | — | RSF 85% |
| **Tổng tài sản** | **1.000** | | | | | |
| Tiền gửi bán lẻ ổn định, kỳ hạn ≤ 12 tháng | 440 | 4,0% | 0,4 | Dải 3–12 tháng | Run-off 5% | ASF 95% |
| Tiền gửi bán lẻ kém ổn định, kỳ hạn ≤ 12 tháng | 220 | 4,5% | 0,4 | Dải 3–12 tháng | Run-off 10% | ASF 90% |
| Tiền gửi DN phi tài chính < 1 năm, không operational | 200 | 4,5% | 0,2 | Dải 1–3 tháng | Run-off 40% | ASF 50% |
| Vay liên ngân hàng, đáo hạn ≤ 30 ngày | 60 | 5,0% | 0,05 | Dải 0–1 tháng | Run-off 100% | ASF 0% |
| Vốn chủ sở hữu (= Vốn cấp 1, giả định) | 80 | — | — | — | — | ASF 100% |
| **Tổng nguồn vốn** | **1.000** | | | | | |

**Tham số quy định dùng trong ví dụ:**

| Tham số | Giá trị | Nguồn |
|---|---|---|
| TPCP VNĐ là HQLA cấp 1 | Cấp 1 | [[src-tt50-2026-nhnn#^pl1-a2]] |
| Run-off tiền gửi bán lẻ ổn định / kém ổn định | 5% / 10% | [[src-tt50-2026-nhnn#^pl1-b2]] |
| Run-off vốn DN phi tài chính không operational (Basel) | 40% | [[src-bcbs-lcr#^lcr40-40]] |
| Run-off vốn không đảm bảo từ ngân hàng (Basel) | 100% | [[src-bcbs-lcr#^lcr40-42]] |
| Dòng tiền ra ròng: dòng ra trừ min(dòng vào, 75% dòng ra) | | [[src-tt50-2026-nhnn#^d16-1]] [[src-bcbs-lcr#^lcr40-1]] |
| ASF vốn và nợ ≥ 1 năm | 100% | [[src-bcbs-nsfr#^nsf30-10]] |
| ASF tiền gửi bán lẻ ổn định / kém ổn định | 95% / 90% | [[src-bcbs-nsfr#^nsf30-11]] [[src-bcbs-nsfr#^nsf30-12]] |
| ASF nguồn vốn DN phi tài chính < 1 năm | 50% | [[src-bcbs-nsfr#^nsf30-13]] |
| ASF nguồn vốn từ TCTD < 6 tháng | 0% | [[src-bcbs-nsfr#^nsf30-14]] |
| RSF tiền gửi DTBB tại NHNN | 0% | [[src-tt50-2026-nhnn#^pl2-b2]] |
| RSF tài sản cấp 1 | 5% | [[src-bcbs-nsfr#^nsf30-26]] |
| RSF tài sản non-HQLA < 1 năm (cho vay DN) | 50% | [[src-bcbs-nsfr#^nsf30-29]] |
| RSF cho vay ≥ 1 năm, RW > 35% | 85% | [[src-bcbs-nsfr#^nsf30-31]] |
| Sốc song song | ±200 bp | [[src-lubinska-alm-optimisation#^lubinska-u02-23]] |

Hệ số ASF/RSF của TT50 PL2 trùng các hệ số Basel trên cho từng dòng đã đối chiếu ở node [[nsfr]]. Hai run-off 40% và 100% là của Basel; synthesis này chưa đối chiếu dòng tương ứng của TT50 PL1.

**Công thức** (đều có nguồn ở node tương ứng):

$$
\text{NII} = \sum_a r_a A_a - \sum_l r_l L_l, \qquad \text{NIM} = \frac{\text{NII}}{\text{Tài sản sinh lãi}}
$$
[[src-choudhry-principles-banking#^choudhry-nim-2]]

$$
\Delta\text{NII}_{12M} = \sum_{k} \text{GAP}_k \cdot \Delta r \cdot \frac{12 - t_k}{12}
$$
[[src-tata-bank-alm#^tata-egap-1]]

$$
DGAP = D_A - \frac{L}{A} D_L, \qquad \Delta E \approx -DGAP \times A \times \Delta y
$$
[[src-lubinska-alm-optimisation#^lubinska-u02-45]] [[src-lubinska-alm-optimisation#^lubinska-u02-47]]

$$
\text{LCR} = \frac{\text{HQLA}}{\text{Dòng tiền ra ròng 30 ngày}}, \qquad \text{NSFR} = \frac{\text{ASF}}{\text{RSF}}, \qquad \text{LEV} = \frac{\text{Vốn cấp 1}}{\text{EM}}
$$
[[src-tt50-2026-nhnn#^d16-1]] [[src-tt50-2026-nhnn#^d22-1]] [[src-tt50-2026-nhnn#^d8-1]]

**Chứng minh tác động biên.** *Diễn giải:* thay các công thức trên với một thay đổi $\Delta A_j$ của tài sản $j$ tài trợ bằng $\Delta L_k = \Delta A_j$ của nguồn $k$ cho các vi phân sau. Đây là đại số trên công thức có nguồn, không phải công thức của nguồn (ngoài wiki, chưa có nguồn):

$$
\begin{aligned}
\Delta\text{NII} &= (r_j - r_k)\,\Delta A_j \\
\Delta(\text{NIM}) &> 0 \iff r_j - r_k > \text{NIM} \quad (\text{khi } j \text{ sinh lãi}) \\
\text{LCR}' &= \frac{\text{HQLA} + h_j \Delta A_j}{\text{NCO} + o_k \Delta L_k} \\
\text{NSFR}' &= \frac{\text{ASF} + a_k \Delta L_k}{\text{RSF} + s_j \Delta A_j} \\
\text{LEV}' &= \frac{\text{Vốn cấp 1}}{\text{EM} + \Delta A_j} \\
\Delta(\Delta E) &\approx -(D_j - D_k)\,\Delta A_j\,\Delta y
\end{aligned}
$$

với $h_j$ là hệ số HQLA của tài sản $j$ (0 nếu không phải HQLA), $o_k$ là run-off của nguồn $k$ nếu đến hạn trong 30 ngày, $a_k$ và $s_j$ là hệ số ASF, RSF. Khi không có dòng vào, NCO bằng dòng ra. Bốn chỉ số rủi ro xấu đi cùng lúc khi $h_j = 0$, $o_k > 0$, $s_j \times \text{NSFR} > a_k$ và $D_j > D_k$ (LEV luôn giảm khi tài sản tăng mà Vốn cấp 1 không đổi), trong khi NII tăng khi $r_j > r_k$. Đó là trường hợp trong kịch bản dưới.

**Kịch bản:** tăng 100 tỷ cho vay cố định trung dài hạn (9,0%, $D_{mod}$ 2,0, RSF 85%), tài trợ bằng 100 tỷ vay liên ngân hàng ≤ 30 ngày (5,0%, run-off 100%, ASF 0%). Vốn cấp 1 giữ nguyên 80 tỷ. Không có dòng vào trong 30 ngày.

| Chỉ số | Cơ sở | Sau thay đổi | Thay đổi | Cách tính |
|---|---|---|---|---|
| Thu nhập lãi | 73,8 | 82,8 | +9,0 | $100 \times 9\%$ |
| Chi phí lãi | 39,5 | 44,5 | +5,0 | $100 \times 5\%$ |
| **NII** | **34,3** | **38,3** | **+4,0** | $(9\% - 5\%) \times 100$ |
| Tài sản sinh lãi | 960 | 1.060 | +100 | Trừ tiền mặt, DTBB (lãi suất 0%) |
| **NIM** | **3,57%** | **3,61%** | **+0,04 điểm %** | $r_j - r_k = 4\% > \text{NIM}$ |
| HQLA | 200 | 200 | 0 | TPCP |
| Dòng ra 30 ngày | 184 | 284 | +100 | $22 + 22 + 80 + 60$ → $+100 \times 100\%$ |
| **LCR** | **108,7%** | **70,4%** | **−38,3 điểm %** | |
| ASF | 796 | 796 | 0 | ASF 0% cho vay liên ngân hàng |
| RSF | 565 | 650 | +85 | $100 \times 85\%$ |
| **NSFR** | **140,9%** | **122,5%** | **−18,4 điểm %** | |
| EM | 1.000 | 1.100 | +100 | Tài sản nội bảng theo giá trị kế toán |
| **LEV** | **8,0%** | **7,3%** | **−0,7 điểm %** | |
| Repricing gap 0–1 tháng | −60 | −160 | −100 | Vay liên ngân hàng |
| Repricing gap 1–3 tháng | +60 | +60 | 0 | 260 − 200 |
| Repricing gap 3–12 tháng | −660 | −660 | 0 | Tiền gửi bán lẻ |
| **ΔNII (+200 bp)** | **−5,1** | **−7,0** | **−1,9** | Trọng số $(12 - t_k)/12$, $t_k$ = 0,5; 2; 7,5 tháng |
| ΔNII / NII | −14,9% | −18,3% | | |
| $D_A$ | 1,65 | 1,68 | | Bình quân theo số dư |
| $\frac{L}{A} D_L$ | 0,307 | 0,284 | | |
| DGAP | 1,345 | 1,400 | +0,055 | |
| **ΔE (+200 bp)** | **−26,9** | **−30,8** | **−3,9** | $-DGAP \times A \times 2\%$ |
| ΔE / Vốn cấp 1 | −33,6% | −38,5% | | |
| CAR | [cần nguồn] | [cần nguồn] | | Thiếu hệ số rủi ro TT14 C2-M2 |

Kiểm tra bằng công thức biên: $\Delta(\Delta E) \approx -(2{,}0 - 0{,}05) \times 100 \times 2\% = -3{,}9$, khớp bảng.

**Đọc kết quả theo ngưỡng.**
- LCR 70,4% vẫn trên ngưỡng 50% năm đầu của lộ trình TT50 nhưng dưới 100% áp từ 01/10/2033 [[src-tt50-2026-nhnn#^d16-1c]]; Basel yêu cầu 100% [[src-bcbs-lcr#^lcr20-5]].
- NSFR 122,5% vẫn trên 100% của cả TT50 và Basel [[src-tt50-2026-nhnn#^d22-2]] [[src-bcbs-nsfr#^nsf20-2]].
- LEV 7,3% trên mức 3% của Basel [[src-bcbs-lev#^lev20-7]]; VN chưa có ngưỡng [[src-tt50-2026-nhnn#^d8-1]].
- ΔE vượt 15% Vốn cấp 1 ngay ở cơ sở, mức Basel dùng cho phép thử outlier [[src-bcbs-irrbb-2016#^irrbb-p12-1]]. TT83 không có phép thử này, ngân hàng chỉ phải có hạn mức nội bộ [[src-tt83-2025-nhnn#^d53-2]].

*Diễn giải:* kịch bản cho thấy cùng một quyết định tài trợ tạo +4,0 tỷ NII nhưng đẩy LCR qua ngưỡng 100%, giảm NSFR, LEV và làm ΔNII, ΔE xấu đi. Nếu tài trợ bằng tiền gửi bán lẻ ổn định thay vì liên ngân hàng, công thức biên cho thấy dòng ra 30 ngày chỉ tăng 5 tỷ và ASF tăng 95 tỷ, đổi lại NII tăng ít hơn nếu lãi suất tiền gửi cao hơn (ngoài wiki, chưa có nguồn).

## Bằng chứng ủng hộ
- Khung tối ưu có nguồn T4 hai tác giả (Lubinska, Choudhry Ch5 đồng tác giả Lubinska) [[src-lubinska-alm-optimisation#^lubinska-u04-13]] [[src-choudhry-principles-banking#^choudhry-opt-2]].
- Quy trình kế hoạch NII có nguồn T4 (Tata) [[src-tata-bank-alm#^tata-niip-3]].
- Tham số LCR, NSFR, LEV có nguồn T1/T2. Ví dụ tương tự trong nguồn: case ChoudWest tăng đệm thanh khoản làm NII giảm £45m, NIM giảm 0,50 điểm % [[src-choudhry-principles-banking#^choudhry-nim-5]].

## Bằng chứng trái chiều
- Công thức gap và DGAP là xấp xỉ: DGAP bỏ qua trả nợ trước hạn và chỉ đúng với sốc nhỏ, song song [[src-lubinska-alm-optimisation#^lubinska-u02-48]]; gap analysis giả định tái định giá ở giữa dải và dịch chuyển song song [[src-choudhry-principles-banking#^choudhry-irr-7]]. ΔEVE chuẩn hoá chiết khấu dòng tiền theo kịch bản thay vì nhân duration [[src-bcbs-irrbb-2016#^irrbb-u05-1]].
- Ví dụ giả định truyền dẫn lãi suất đầy đủ vào tiền gửi. Bằng chứng mà Tata dẫn cho thấy biên lãi chỉ biến động khoảng 19 bp cho mỗi 100 bp lãi suất ngắn hạn [[src-tata-bank-alm#^tata-niip-5]], nên ΔNII thực tế có thể khác.

## Phụ thuộc regime
- Kịch bản lãi suất tăng làm ΔNII âm vì gap 12 tháng âm; lãi suất giảm cho chiều ngược lại theo cùng công thức [[src-tata-bank-alm#^tata-egap-1]].
- Trong stress thanh khoản, TT83 yêu cầu ba kịch bản [[src-tt83-2025-nhnn#^d48-2]]; run-off trong ví dụ là tham số chuẩn của LCR, không phải kịch bản nội bộ.

## Hàm ý ALM / quy định
- **Nghĩa vụ NHNN (T1):** báo cáo IRRBB nội bộ hằng quý gồm repricing gap profile [[src-tt83-2025-nhnn#^d55-1]]; hạn mức ΔNII, ΔEVE [[src-tt83-2025-nhnn#^d53-2]]; LCR, NSFR theo lộ trình TT50 từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]].
- **Chưa có nguồn NHNN trong wiki** về CAR (TT14), về ngưỡng LEV, và về mô hình mô phỏng bảng cân đối như một yêu cầu riêng.
- *Diễn giải:* một bảng cân đối giả định đơn giản như trên đã đủ để ALCO thấy đánh đổi giữa NII và bốn chỉ số rủi ro trước khi duyệt kế hoạch tăng trưởng. Biểu `04_models/lcr-tt50-2026.xlsx` có thể mở rộng thêm sheet NSFR, LEV và gap theo cấu trúc này (ngoài wiki, chưa có nguồn).

## Bất định
- **CAR** [cần nguồn]: cần `/ingest src-tt14-2025-nhnn C1` (định nghĩa, ngưỡng) và `C2-M2` (hệ số rủi ro tín dụng). Sau khi có, thêm dòng CAR vào bảng kịch bản: cho vay mới 100 tỷ làm RWA tăng theo hệ số rủi ro của khoản vay.
- **Thuật ngữ "synthetic balance sheet"** không có trong nguồn đã ingest. Node [[contractual-maturity-mismatch]] mục 4 dùng thuật ngữ này nhưng không có citation.
- **Run-off TT50 cho tiền gửi DN và vay liên ngân hàng** chưa đối chiếu; ví dụ dùng LCR40.40 và LCR40.42 của Basel.
- **Giả định của ví dụ:** tiền mặt, DTBB không tính HQLA; không có dòng vào 30 ngày; toàn bộ tiền gửi bán lẻ là có kỳ hạn ≤ 12 tháng (không mô hình NMD core); giá trị thị trường bằng giá trị sổ sách; truyền dẫn lãi suất đầy đủ.
- Ràng buộc LDR 80%, ΔNII 4%, CAR 10,5% ghi ở [[balance-sheet-optimisation-model]] cite Lubinska u05-6 đến u05-11, nhưng synthesis này chỉ verify được trần tập trung 80% [[src-lubinska-alm-optimisation#^lubinska-u05-11]]. Các con số còn lại cần rà bằng `python tools/citations.py --node balance-sheet-optimisation-model`.
