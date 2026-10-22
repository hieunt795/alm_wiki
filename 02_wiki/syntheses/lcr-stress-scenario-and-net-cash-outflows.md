---
title: "LCR: kịch bản stress 30 ngày và dòng tiền ra ròng"
aliases: [LCR stress scenario and net cash outflows, Kịch bản stress 30 ngày và dòng tiền ra ròng LCR, Cơ chế hình thành mẫu số LCR]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Rủi ro thanh khoản ngắn hạn được hình thành, đo lường và kiểm soát thông qua LCR như thế nào (Basel III và Thông tư 50/2026/TT-NHNN)? · Bản chất kịch bản stress 30 ngày và cơ chế hình thành Net Cash Outflows từ cash outflows, cash inflows, runoff rates, inflow rates và 75% inflow cap."
as_of: 2026-10-22
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]", "[[src-tt83-2025-nhnn]]", "[[src-bardaeva-alm]]", "[[src-choudhry-principles-banking]]"]
relations: []
tags: [lcr, liquidity, stress-test, net-cash-outflows, run-off, inflow-cap, research]
updated: 2026-10-22
reviewed:
---

## Câu hỏi
Thuộc bộ "Liquidity Risk — LCR & HQLA" (7 câu). Cụm này trả lời:
- **Q1.** Rủi ro thanh khoản ngắn hạn được hình thành, đo lường và kiểm soát thông qua LCR như thế nào (Basel III và Thông tư 50/2026/TT-NHNN)?
- **Q2.** Bản chất kịch bản stress 30 ngày và cơ chế hình thành Net Cash Outflows từ cash outflows, cash inflows, runoff rates, inflow rates và 75% inflow cap.

Các cụm còn lại: HQLA và đặc điểm từng nguồn vốn (Q3–Q4) ở [[lcr-hqla-and-funding-run-off-characteristics]]; mô hình, tác động biên và biện pháp ALM (Q5, Q7) ở [[lcr-model-marginal-impact-and-alm-levers]]; đánh đổi HQLA – NIM – IRRBB (Q6) ở [[lcr-hqla-buffer-tradeoffs]].

Node dùng: [[lcr]], [[net-cash-outflows]], [[cash-outflows]], [[cash-inflows]], [[run-off-rate]], [[tt50-2026]], đều ở maturity `draft`. BCBS LCR có hiệu lực từ 15/12/2019. TT50/2026 có hiệu lực từ 01/10/2026, nhưng LCR chỉ áp dụng từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]].

## Kết luận
- **Q1.** LCR giả định rủi ro thanh khoản ngắn hạn phát sinh từ một kịch bản stress kết hợp cú sốc riêng của ngân hàng và cú sốc toàn thị trường. Kịch bản này gồm rút tiền gửi, mất wholesale funding và secured funding, hạ bậc tín nhiệm, biến động thị trường, rút hạn mức và nghĩa vụ ngoài hợp đồng [[src-bcbs-lcr#^lcr20-2]]. LCR đo rủi ro đó bằng tỷ số HQLA / total net cash outflows trong 30 ngày [[src-bcbs-lcr#^lcr20-1]] [[src-bcbs-lcr#^lcr20-4]]. Ngưỡng kiểm soát của Basel là ≥ 100% liên tục khi không có stress; trong stress ngân hàng được dùng HQLA và xuống dưới ngưỡng [[src-bcbs-lcr#^lcr20-5]].
- **Q1 (VN).** TT50 dùng tên "tỷ lệ khả năng chi trả" và cùng công thức HQLA đủ điều kiện / dòng tiền ra ròng 30 ngày [[src-tt50-2026-nhnn#^d16-1]]. Ngưỡng áp cho LCR quy VNĐ riêng lẻ theo lộ trình: 50% từ 01/10/2028, tăng 10 điểm mỗi năm, 100% từ 01/10/2033 [[src-tt50-2026-nhnn#^d16-1c]]. Trước mốc 01/10/2028, ngân hàng tuân thủ tỷ lệ khả năng chi trả 30 ngày theo TT22/2019 [[src-tt50-2026-nhnn#^d13-4]]. Wiki chưa có nguồn TT22 [cần nguồn]. Khác Basel, TT50 coi LCR dưới ngưỡng là vi phạm và gắn với biện pháp tự xử lý, báo cáo hằng ngày, xử phạt hành chính [[src-tt50-2026-nhnn#^d17-2]] [[src-tt50-2026-nhnn#^d17-2a]].
- **Q2.** Mẫu số = tổng dòng ra − min(tổng dòng vào; 75% tổng dòng ra). Dòng ra bằng số dư nhân run-off rate hoặc drawdown rate; dòng vào bằng số dư phải thu nhân inflow rate [[src-bcbs-lcr#^lcr40-1]]. TT50 dùng cùng công thức, gọi hai hệ số là "hệ số rút tiền" và "hệ số thu tiền" [[src-tt50-2026-nhnn#^d21-2]]. Vì trần 75%, HQLA tối thiểu luôn bằng 25% tổng dòng ra gộp [[src-bcbs-lcr#^lcr40-77]].

## Cơ chế

### Q1 — Hình thành, đo lường, kiểm soát

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[bcbs-lcr]] | governs | [[lcr]] | | [[src-bcbs-lcr#^lcr10-1]] |
| [[tt50-2026]] | governs | [[lcr]] | | [[src-tt50-2026-nhnn#^d16-1]] |
| [[hqla]] | input-to | [[lcr]] | | [[src-bcbs-lcr#^lcr20-1]] |
| [[net-cash-outflows]] | input-to | [[lcr]] | | [[src-bcbs-lcr#^lcr20-1]] |
| [[hqla]] | drives | [[lcr]] | + | [[src-bcbs-lcr#^lcr20-1]] |
| [[run-off-rate]] | input-to | [[liquidity-stress-testing]] | | [[src-tt83-2025-nhnn#^d48-3]] |

**Hình thành.** Kịch bản LCR gồm bảy cú sốc xảy ra cùng lúc [[src-bcbs-lcr#^lcr20-2]]:
- rút một phần tiền gửi bán lẻ;
- mất một phần wholesale funding không bảo đảm;
- mất secured funding ngắn hạn;
- hạ bậc tín nhiệm tới 3 notch;
- biến động thị trường;
- khách hàng rút hạn mức tín dụng và hạn mức thanh khoản chưa giải ngân;
- ngân hàng mua lại nợ hoặc thực hiện nghĩa vụ ngoài hợp đồng để giảm rủi ro uy tín.

Mục tiêu của LCR là đủ HQLA để vượt qua kịch bản stress đáng kể kéo dài 30 ngày dương lịch [[src-bcbs-lcr#^lcr20-1]]. Mỗi cú sốc được lượng hoá bằng một hệ số trong LCR40 (xem Q2).

**Đo lường.**

$$
\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Total net cash outflows}_{30d}}
$$
[[src-bcbs-lcr#^lcr20-4]] [[src-tt50-2026-nhnn#^d16-1]]

TT50 tách ba loại LCR: LCR quy VNĐ (VNĐ và ngoại tệ quy đổi), LCR VNĐ, LCR ngoại tệ trọng yếu [[src-tt50-2026-nhnn#^d16-1]]. Ngân hàng phải báo cáo NHNN LCR riêng lẻ quy VNĐ và LCR VNĐ; LCR hợp nhất và LCR ngoại tệ trọng yếu quản lý theo quy định nội bộ [[src-tt50-2026-nhnn#^d16-2]]. Basel áp LCR trên cơ sở hợp nhất cho ngân hàng hoạt động quốc tế [[src-bcbs-lcr#^lcr10-1]], và yêu cầu theo dõi nhu cầu thanh khoản theo từng đồng tiền trọng yếu, không giả định các đồng tiền chuyển đổi được trong stress [[src-bcbs-lcr#^lcr10-9]].

**Kiểm soát.** Bảng dưới so sánh các lớp kiểm soát của hai khung.

| Lớp kiểm soát | Basel | VN (TT50, TT83) |
|---|---|---|
| Ngưỡng | ≥ 100% liên tục [[src-bcbs-lcr#^lcr20-5]] | LCR quy VNĐ riêng lẻ 50% → 100% (01/10/2028 → 01/10/2033) [[src-tt50-2026-nhnn#^d16-1c]] |
| Theo dõi | Báo cáo ít nhất hằng tháng, có năng lực tăng lên hằng tuần, hằng ngày khi stress [[src-bcbs-lcr#^lcr20-7]] | Bộ phận tại trụ sở chính theo dõi LCR hằng ngày, do Tổng giám đốc hoặc Phó Tổng giám đốc được uỷ quyền phụ trách [[src-tt50-2026-nhnn#^d17-1]] |
| Khi dưới ngưỡng | Ngân hàng phải thông báo ngay [[src-bcbs-lcr#^lcr20-8]]; supervisor nên cho phép phản ứng có phân biệt [[src-bcbs-lcr#^lcr20-6]] | Ngân hàng phải ngay lập tức dùng biện pháp tự xử lý; từ 10% giá trị HQLA đủ điều kiện trở lên thì NHNN giám sát tăng cường; báo cáo hằng ngày [[src-tt50-2026-nhnn#^d17-2]] |
| Ngưỡng cảnh báo sâu hơn | [cần nguồn] | Nguy cơ mất khả năng chi trả khi HQLA đủ điều kiện < 90% mức phải đáp ứng trong 30 ngày liên tục [[src-tt50-2026-nhnn#^d18-1]] |
| Ràng buộc khi hỗ trợ ngân hàng khác | [cần nguồn] | Chỉ được cho vay, ký cam kết không thể huỷ ngang với TCTD khác để bù thiếu hụt nếu sau đó vẫn bảo đảm LCR [[src-tt50-2026-nhnn#^d17-3]] |
| Stress test nội bộ | LCR chỉ là yêu cầu giám sát tối thiểu [[src-bcbs-lcr#^lcr20-3]] | Tối thiểu 3 kịch bản: đặc thù, toàn hệ thống, hỗn hợp [[src-tt83-2025-nhnn#^d48-2]] |

*Diễn giải:* LCR kiểm soát rủi ro thanh khoản ngắn hạn theo hai bước. Bước thứ nhất là chuẩn hoá cú sốc thành hệ số do cơ quan quản lý ấn định. Bước thứ hai là buộc ngân hàng giữ trước một lượng HQLA đủ bù dòng ra ròng. Stress test nội bộ theo TT83 Đ48 bổ sung phần giả định hành vi của chính ngân hàng: run-off thực tế, mức tập trung, khả năng mất khách gửi tiền quan trọng [[src-tt83-2025-nhnn#^d48-3]].

### Q2 — Kịch bản 30 ngày và Net Cash Outflows

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[run-off-rate]] | input-to | [[net-cash-outflows]] | | [[src-bcbs-lcr#^lcr40-1]] |
| [[cash-outflows]] | input-to | [[net-cash-outflows]] | | [[src-bcbs-lcr#^lcr40-1]] |
| [[cash-inflows]] | input-to | [[net-cash-outflows]] | | [[src-bcbs-lcr#^lcr40-1]] |
| [[cash-outflows]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr20-1]] |
| [[cash-inflows]] | drives | [[lcr]] | + | [[src-bcbs-lcr#^lcr20-1]] |
| [[run-off-rate]] | drives | [[lcr]] | − | [[src-bcbs-lcr#^lcr40-1]] |
| [[tt50-2026]] | governs | [[net-cash-outflows]] | | [[src-tt50-2026-nhnn#^d21-2]] |

**Công thức.**

$$
\text{NCO} = \sum_i O_i \cdot r_i - \min\Big(\sum_j I_j \cdot q_j,\; 0{,}75 \sum_i O_i \cdot r_i\Big)
$$
[[src-bcbs-lcr#^lcr40-1]] [[src-tt50-2026-nhnn#^d21-2]]

Trong đó $O_i$ là số dư nghĩa vụ nợ và cam kết ngoại bảng của nhóm $i$, $r_i$ là run-off rate (TT50: hệ số rút tiền), $I_j$ là số dư phải thu của nhóm $j$, $q_j$ là inflow rate (TT50: hệ số thu tiền).

**Nguyên tắc tính.**
- Chỉ tính dòng tiền trong 30 ngày [[src-tt50-2026-nhnn#^d21-3]].
- Không đếm trùng: tài sản đã tính vào HQLA thì dòng vào của nó không được tính ở mẫu số [[src-bcbs-lcr#^lcr40-4]] [[src-tt50-2026-nhnn#^d21-3]].
- Khoản mục thuộc nhiều nhóm dòng ra thì dùng hệ số rút tiền cao nhất [[src-tt50-2026-nhnn#^d21-3]].
- Nguồn vốn có kỳ hạn còn lại trên 30 ngày không tính vào dòng ra khi khách hàng không có quyền rút trong 30 ngày [[src-bcbs-lcr#^lcr40-16]] [[src-tt50-2026-nhnn#^pl1-b1]]. Basel cũng loại trừ trường hợp rút trước hạn chịu phạt lớn hơn rõ rệt so với mất lãi [[src-bcbs-lcr#^lcr40-16]]; TT50 loại trừ tiền gửi bán lẻ VNĐ rút trước hạn chỉ hưởng tối đa lãi suất không kỳ hạn thấp nhất [[src-tt50-2026-nhnn#^pl1-b1]].
- Không xác định được thời hạn thì TT50 tính vào dòng ra của ngày tiếp theo [[src-tt50-2026-nhnn#^pl1-b1]].
- Biểu mẫu TT50 chia mỗi đầu mục dòng ra, dòng vào theo 4 khung thời gian: ngày tiếp theo, ngày 2–7, ngày 8–14, ngày 15–30 [[src-tt50-2026-nhnn#^pl1-b7]] [[src-tt50-2026-nhnn#^pl1-c7]].

**Dòng ra theo bảy cú sốc.** Mỗi cú sốc của LCR20.2 ứng với một nhóm hệ số dòng ra. Chi tiết theo từng nguồn vốn ở cụm Q3–Q4.

| Cú sốc LCR20.2 | Basel | VN (TT50 PL1 Phần B) |
|---|---|---|
| Rút tiền gửi bán lẻ | stable 5% (jurisdiction có thể 3%), less stable ≥ 10% [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-11]] [[src-bcbs-lcr#^lcr40-13]] | ổn định 5%, kém ổn định 10% [[src-tt50-2026-nhnn#^pl1-b2]] |
| Mất wholesale funding không bảo đảm | operational 25%, DN phi tài chính và khu vực công 40% (20% nếu được bảo hiểm toàn bộ), tổ chức tài chính 100% [[src-bcbs-lcr#^lcr40-26]] [[src-bcbs-lcr#^lcr40-40]] [[src-bcbs-lcr#^lcr40-41]] [[src-bcbs-lcr#^lcr40-42]] | tiền gửi hoạt động 25%, DN phi tài chính và khu vực công 40%, nguồn khác 100% [[src-tt50-2026-nhnn#^pl1-b3]] |
| Mất secured funding ngắn hạn | bảo đảm bằng Level 1 hoặc với NHTW 0%, Level 2 bằng haircut, giao dịch khác 100% [[src-bcbs-lcr#^lcr40-47]] [[src-bcbs-lcr#^lcr40-48]] | HQLA cấp 1 hoặc với NHNN 0%, cấp 2A 15%, cấp 2B khác 50%, tài sản tài chính khác 100% [[src-tt50-2026-nhnn#^pl1-b3-3]] |
| Hạ bậc tín nhiệm tới 3 notch | 100% tài sản bảo đảm hoặc dòng tiền phát sinh [[src-bcbs-lcr#^lcr40-51]] | 100% phần phải thực hiện khi bị hạ tối đa 3 bậc [[src-tt50-2026-nhnn#^pl1-b4-21]] |
| Biến động thị trường | look-back 24 tháng, dòng tài sản bảo đảm ròng lớn nhất trong 30 ngày [[src-bcbs-lcr#^lcr40-56]]; tài sản bảo đảm không phải Level 1 cộng 20% [[src-bcbs-lcr#^lcr40-52]] | lookback 24 tháng; ký quỹ bằng tài sản không phải HQLA cấp 1 tính thêm 20% [[src-tt50-2026-nhnn#^pl1-b4]] |
| Rút hạn mức chưa giải ngân | bán lẻ/SME 5%; DN phi tài chính 10% (tín dụng) / 30% (thanh khoản); ngân hàng 40%; định chế tài chính khác 40% / 100% [[src-bcbs-lcr#^lcr40-64]] | cá nhân và DNNVV 5%/5%; DN phi tài chính 10%/30%; TCTD 40%/40%; tổ chức tài chính khác 40%/100% [[src-tt50-2026-nhnn#^pl1-b5]] |
| Nghĩa vụ ngoài hợp đồng, uy tín | run-off do supervisor quốc gia quyết định [[src-bcbs-lcr#^lcr40-67]] | tài trợ thương mại 3%; bảo lãnh 5%; nghĩa vụ phi hợp đồng do ngân hàng xác định từ dữ liệu lịch sử [[src-tt50-2026-nhnn#^pl1-b5-3]] |

**Dòng vào.**
- Chỉ tính dòng vào theo hợp đồng từ khoản phải thu đang performing; không tính dòng vào tiềm tàng, kể cả hạn mức từ NHTW [[src-bcbs-lcr#^lcr40-75]]. TT50 chỉ ghi nhận khoản phải đòi nợ nhóm 1 và không vỡ nợ, không tính dòng vào mang tính điều kiện kể cả cam kết từ NHNN [[src-tt50-2026-nhnn#^pl1-c1]].
- Hạn mức ngân hàng được tổ chức khác cấp: inflow 0% [[src-bcbs-lcr#^lcr40-82]] [[src-tt50-2026-nhnn#^pl1-c3]].

| Đối tác / tài sản | Basel | VN (TT50 PL1 Phần C) |
|---|---|---|
| Bán lẻ, SME | 50% [[src-bcbs-lcr#^lcr40-86]] | 50% [[src-tt50-2026-nhnn#^pl1-c4-5]] |
| DN phi tài chính, khu vực công | 50% [[src-bcbs-lcr#^lcr40-87]] | 50% [[src-tt50-2026-nhnn#^pl1-c4-6b]] |
| Tổ chức tài chính, NHTW | 100% [[src-bcbs-lcr#^lcr40-87]] | 100% [[src-tt50-2026-nhnn#^pl1-c4-6a]] |
| Chứng khoán không phải HQLA đáo hạn trong 30 ngày | 100% [[src-bcbs-lcr#^lcr40-88]] | 100% [[src-tt50-2026-nhnn#^pl1-c4-7]] |
| Tiền gửi operational đặt tại tổ chức khác | 0% [[src-bcbs-lcr#^lcr40-89]] | 0% [[src-tt50-2026-nhnn#^pl1-c4-8a]] |
| Reverse repo bảo đảm bằng Level 1 / Level 2A / non-HQLA | 0% / 15% / 100% [[src-bcbs-lcr#^lcr40-78]] | cấp 1 0%, cấp 2A 15%, RMBS 25%, cấp 2B khác 50%, tài sản tài chính khác 100% [[src-tt50-2026-nhnn#^pl1-c2]] |
| Phái sinh ròng | 100% [[src-bcbs-lcr#^lcr40-91]] | 100% [[src-tt50-2026-nhnn#^pl1-c5-1]] |
| Dư nợ hạn mức quay vòng | khoản vay hiện hữu giả định được roll-over [[src-bcbs-lcr#^lcr40-84b]] | không tính dòng vào [[src-tt50-2026-nhnn#^pl1-c4-4]] |

**Trần 75%.** Trần dòng vào bằng 75% tổng dòng ra, nên HQLA tối thiểu bằng 25% tổng dòng ra [[src-bcbs-lcr#^lcr40-77]] [[src-tt50-2026-nhnn#^d21-2]]. Ví dụ Bardaeva Table 5.1 dùng trần này để tính đệm thanh khoản cho LCR mục tiêu 110% [[src-bardaeva-alm#^ch5-2]].

*Diễn giải:* trần tạo hai chế độ cho mẫu số.
- Khi dòng vào có trọng số dưới 75% dòng ra, mỗi đồng dòng vào thêm làm NCO giảm đúng một đồng.
- Khi dòng vào vượt 75% dòng ra, NCO cố định ở 25% dòng ra; dòng vào thêm không cải thiện LCR, còn mỗi đồng dòng ra thêm chỉ làm NCO tăng 0,25 đồng.

Ví dụ Bardaeva có dòng ra 100 và dòng vào 90, nên rơi vào chế độ thứ hai: NCO = 100 − 75 = 25.

**Bất đối xứng của giả định.** Ba cặp giả định không đối xứng giữa dòng vào và dòng ra:
- Dòng vào từ bán lẻ và DN phi tài chính chỉ tính 50% vì ngân hàng được giả định tiếp tục cho vay [[src-bcbs-lcr#^lcr40-86]] [[src-bcbs-lcr#^lcr40-83]]. Phía nợ, tiền gửi bán lẻ chỉ chịu run-off 5–10%.
- Liên ngân hàng: vay từ tổ chức tài chính chịu run-off 100% [[src-bcbs-lcr#^lcr40-42]], cho vay tổ chức tài chính có inflow 100% [[src-bcbs-lcr#^lcr40-87]].
- Operational deposits: bên nhận chịu run-off 25% [[src-bcbs-lcr#^lcr40-26]], bên gửi tính inflow 0% [[src-bcbs-lcr#^lcr40-31]].

*Diễn giải:* các cặp giả định trên phản ánh cách nhìn thận trọng của LCR: ngân hàng được giả định vẫn phải phục vụ khách hàng (franchise) và không dựa được vào khoản tiền gửi vận hành của chính mình. Liên ngân hàng là nhóm duy nhất hai chiều đều tính 100%, nên vay và cho vay liên ngân hàng ngắn hạn gần như bù trừ nhau trong NCO cho tới khi chạm trần 75% (ngoài wiki, chưa có nguồn).

## Bằng chứng ủng hộ
- Khung kịch bản, công thức và hệ số của Basel (T2, final) và TT50 (T1) khớp nhau ở trần 75%, công thức NCO, khung 30 ngày [[src-bcbs-lcr#^lcr40-1]] [[src-tt50-2026-nhnn#^d21-2]].
- Choudhry ghi nhận quy mô LAB (HQLA) ngày nay trước hết do LCR và mức LCR tối thiểu ngân hàng tự đặt trên 100% quyết định [[src-choudhry-principles-banking#^choudhry-lab-3]].

## Bằng chứng trái chiều
Không ghi nhận trong nguồn đã ingest. Khác biệt Basel – VN ở mục Hàm ý là khác biệt jurisdiction, không phải conflict.

## Phụ thuộc regime
- **Stress so với bình thường.** Basel cho phép LCR dưới 100% trong stress như cách dùng HQLA hợp lệ [[src-bcbs-lcr#^lcr20-5]]; TT50 coi đó là vi phạm cần tự xử lý và báo cáo [[src-tt50-2026-nhnn#^d17-2]].
- **Chế độ trần dòng vào.** Ngân hàng có dòng vào ngắn hạn lớn (ví dụ cho vay liên ngân hàng) dễ rơi vào chế độ NCO = 25% dòng ra (xem Q2).
- **Đồng tiền.** Tiền gửi ngoại tệ thuộc nhóm kém ổn định trong TT50 [[src-tt50-2026-nhnn#^pl1-b2]]; Basel để supervisor quyết định run-off ngoại tệ [[src-bcbs-lcr#^lcr40-15]].

## Hàm ý ALM / quy định
- **Nghĩa vụ NHNN (căn cứ).** Từ 01/10/2028, ngân hàng phải áp dụng LCR và NSFR theo lộ trình [[src-tt50-2026-nhnn#^d13-1]]. Ngưỡng chỉ áp cho LCR quy VNĐ riêng lẻ [[src-tt50-2026-nhnn#^d16-1c]]. LCR VNĐ cũng phải quản lý và báo cáo [[src-tt50-2026-nhnn#^d16-2]].
- **Basel (tham chiếu).** Ngưỡng 100% hợp nhất, báo cáo hằng tháng [[src-bcbs-lcr#^lcr20-5]] [[src-bcbs-lcr#^lcr20-7]]. Tại VN, khung Basel không phải nghĩa vụ.
- **Giai đoạn 01/10/2026 – 30/09/2028.** Nghĩa vụ là các tỷ lệ của TT22/2019 [[src-tt50-2026-nhnn#^d13-4]]; ngân hàng có thể đăng ký áp dụng LCR sớm [[src-tt50-2026-nhnn#^d13-2]].
- *Diễn giải:* với ALCO, hai đầu mục cần theo dõi ngay là LCR VNĐ và LCR quy VNĐ, vì ngưỡng pháp định chỉ đặt cho LCR quy VNĐ trong khi tiền gửi ngoại tệ luôn chịu hệ số 10%. Biểu tính `04_models/lcr-tt50-2026.xlsx` dựng theo Bảng 3, 6, 8 của TT50 (số liệu minh hoạ).

## Bất định
- Tỷ lệ khả năng chi trả 30 ngày theo TT22/2019 (nghĩa vụ hiện hành trước 01/10/2028): wiki chưa có nguồn. Cần `/register` TT22/2019.
- TT50 không mô tả kịch bản stress bằng lời như LCR20.2. Việc ghép bảy cú sốc với đầu mục TT50 trong bảng Q2 là diễn giải của synthesis.
- Taxonomy chỉ có regime theo lãi suất và stress, nên hai chế độ trần dòng vào chưa ghi được vào cạnh `cash-inflows —drives(+)→ lcr`.
