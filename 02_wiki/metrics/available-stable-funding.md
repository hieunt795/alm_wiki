---
title: "Available Stable Funding (ASF)"
aliases: [ASF, Nguồn vốn ổn định sẵn có, Available Stable Funding]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-tata-bank-alm]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "+", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
tags: [liquidity, nsfr, liabilities, funding-stability]
updated: 2026-10-21
reviewed:
---

## Định nghĩa chuẩn mực

**Available Stable Funding (ASF)** là tử số của tỷ lệ [[nsfr]], đại diện cho tổng quy mô nguồn vốn tự có và nợ phải trả được kỳ vọng sẽ duy trì ổn định, bám dính và đáng tin cậy trong khoảng thời gian một năm dưới các điều kiện hoạt động bình thường và căng thẳng thanh khoản vừa phải [[src-bcbs-nsfr#^nsf20-2]] [[src-bcbs-nsfr#^nsf30-2]].

ASF được đo lường dựa trên hai đặc tính nền tảng của nguồn vốn [[src-bcbs-nsfr#^nsf30-2]] [[src-bcbs-nsfr#^nsf30-5]]:
1. **Kỳ hạn hợp đồng (Funding Tenor)**: Các khoản nợ có kỳ hạn còn lại từ 1 năm trở lên được coi là ổn định hoàn toàn.
2. **Đặc tính hành vi của nhà cung cấp vốn (Funding Provider Propensity)**: Các khoản tiền gửi ngắn hạn hoặc không kỳ hạn từ khách hàng cá nhân và doanh nghiệp nhỏ (SME) có tính bám dính cao hơn đáng kể so với nguồn vốn bán buôn từ các định chế tài chính.

---

## Công thức xác định

Theo Chuẩn mực Basel (NSF30.6, NSF99.1), tổng nguồn vốn ổn định sẵn có được xác định bằng tổng giá trị ghi sổ của từng cấu phần nợ và vốn nhân với hệ số ASF tương ứng [[src-bcbs-nsfr#^nsf30-6]] [[src-bcbs-nsfr#^nsf99-1]]:

$$
\text{ASF} = \sum_{k} \text{Carrying Amount}_k \times \text{ASF Factor}_k
$$

Khai triển theo 5 nhóm hệ số giám sát:

$$
\text{ASF} = 1.00 \times \text{Liab}_{100\%} + 0.95 \times \text{Liab}_{95\%} + 0.90 \times \text{Liab}_{90\%} + 0.50 \times \text{Liab}_{50\%} + 0.00 \times \text{Liab}_{0\%}
$$

Trong đó $\text{Carrying Amount}_k$ là giá trị ghi sổ kế toán (bao gồm cả gốc và lãi dồn tích) của từng công cụ nợ hoặc vốn thuộc nhóm $k$ trước khi áp dụng các bộ lọc quy định [[src-bcbs-nsfr#^nsf30-6]].

---

## Diễn giải & Cơ chế Phân tầng 5 Nhóm Hệ số ASF

Hệ thống Chuẩn mực Basel thiết lập ma trận 5 bậc hệ số ASF giảm dần theo mức độ ổn định của nguồn vốn [[src-bcbs-nsfr#^nsf30-6]]:

| Hệ số ASF | Cấu phần nợ và vốn đủ điều kiện | Căn cứ chuẩn mực |
|:---:|---|---|
| **100%** | - Vốn điều lệ và vốn tự có quy định theo chuẩn CAP10 (trừ công cụ Tier 2 kỳ hạn $< 1$ năm) [[src-bcbs-nsfr#^nsf30-10]].<br>- Các công cụ vốn khác có kỳ hạn còn lại $\ge 1$ năm (không có quyền chọn rút ngắn kỳ hạn) [[src-bcbs-nsfr#^nsf30-10]].<br>- Nợ vay và tiền gửi bán buôn có kỳ hạn còn lại $\ge 1$ năm [[src-bcbs-nsfr#^nsf30-10]].<br>- Tiền gửi bán lẻ có kỳ hạn $\ge 1$ năm có điều khoản phạt nặng nếu rút sớm [[src-bcbs-nsfr#^nsf30-10]]. | NSF30.10 |
| **95%** | - Tiền gửi không kỳ hạn và tiền gửi có kỳ hạn $< 1$ năm thuộc nhóm **stable** của khách hàng bán lẻ và SME (được bảo hiểm tiền gửi hiệu quả chi trả) [[src-bcbs-nsfr#^nsf30-11]]. | NSF30.11 |
| **90%** | - Tiền gửi không kỳ hạn và tiền gửi có kỳ hạn $< 1$ năm thuộc nhóm **less stable** của khách hàng bán lẻ và SME [[src-bcbs-nsfr#^nsf30-12]]. | NSF30.12 |
| **50%** | - Nguồn vốn (có bảo đảm và không bảo đảm) kỳ hạn $< 1$ năm từ doanh nghiệp phi tài chính [[src-bcbs-nsfr#^nsf30-13]].<br>- Tiền gửi vận hành ([[operational-deposits]] theo LCR40.26–36) [[src-bcbs-nsfr#^nsf30-13]].<br>- Nguồn vốn kỳ hạn $< 1$ năm từ chính phủ (Sovereign), cơ quan khu vực công (PSE), ngân hàng phát triển đa phương (MDB) và ngân hàng phát triển quốc gia [[src-bcbs-nsfr#^nsf30-13]].<br>- Nguồn vốn kỳ hạn từ **6 tháng đến dưới 1 năm** từ Ngân hàng Trung ương và các định chế tài chính [[src-bcbs-nsfr#^nsf30-13]]. | NSF30.13 |
| **0%** | - Nguồn vốn kỳ hạn **dưới 6 tháng** từ Ngân hàng Trung ương và các định chế tài chính [[src-bcbs-nsfr#^nsf30-14]].<br>- Các khoản nợ không kỳ hạn xác định (vị thế bán khống short positions, trừ thuế hoãn lại và lợi ích cổ đông thiểu số) [[src-bcbs-nsfr#^nsf30-14]].<br>- Nợ phái sinh ròng NSFR (nếu nợ phái sinh lớn hơn tài sản phái sinh) [[src-bcbs-nsfr#^nsf30-14]].<br>- Các khoản phải trả ngày giao dịch (trade date payables) [[src-bcbs-nsfr#^nsf30-14]]. | NSF30.14 |

### Các Quy tắc Kỹ thuật Trọng yếu

#### 1. Quy tắc Xác định Kỳ hạn và Quyền chọn Mua lại (Call Options)
- **Giả định ngày thực hiện sớm nhất**: Khi xác định kỳ hạn nợ có quyền chọn mua lại (*call option*), ngân hàng phải giả định bên có quyền sẽ thực hiện quyền chọn ở ngày sớm nhất có thể [[src-bcbs-nsfr#^nsf30-7]].
- **Kỳ vọng thị trường và rủi ro uy tín**: Nếu thị trường kỳ vọng ngân hàng sẽ mua lại trái phiếu trước hạn (ví dụ tại ngày call date đầu tiên của trái phiếu thứ cấp Cấp 2), ngân hàng bắt buộc phải tính kỳ hạn nợ kết thúc tại ngày call date đó, khiến khoản nợ không được ghi nhận vào nhóm ASF 100% nếu thời gian đến ngày call date $< 1$ năm [[src-bcbs-nsfr#^nsf30-7]].
- **Cắt lát dòng tiền (Cash flow slicing)**: Đối với nợ dài hạn thanh toán định kỳ, chỉ phần dòng tiền thực sự đáo hạn sau 1 năm mới được nhận hệ số ASF 100%; các dòng tiền gốc và lãi rơi vào khoảng 6 tháng đến dưới 1 năm nhận ASF 50%, và dưới 6 tháng nhận ASF 0% (đối với nguồn vốn từ tổ chức tài chính) [[src-bcbs-nsfr#^nsf30-7]] [[src-bcbs-nsfr#^nsf30-10]].

#### 2. Đối xử Nợ Phái sinh trong ASF
- Nợ phái sinh được đo lường bằng chi phí thay thế âm (replacement cost) sau khi áp dụng bù trừ song phương đủ điều kiện [[src-bcbs-nsfr#^nsf30-8]].
- Tài sản bảo đảm ký quỹ biến đổi (variation margin) đã đặt cọc được trừ khỏi nợ phái sinh [[src-bcbs-nsfr#^nsf30-9]].
- Nếu sau khi bù trừ, tổng nợ phái sinh NSFR lớn hơn tổng tài sản phái sinh NSFR, phần chênh lệch ròng này được xếp vào nhóm **ASF 0%** (không được coi là nguồn vốn ổn định) [[src-bcbs-nsfr#^nsf30-14]].

---

## Theo TT50/2026: giải trình từng đầu mục ASF

### Công thức và nguyên tắc chung
$$\text{ASF} = \sum_{k} \text{Giá trị thành phần}_k \times \text{Hệ số ASF}_k$$
[[src-tt50-2026-nhnn#^d23-1]]

- **Phạm vi:** toàn bộ nợ phải trả và vốn chủ sở hữu trên báo cáo tài chính được phân loại vào Bảng 9 PL2 [[src-tt50-2026-nhnn#^pl2-a1]].
- **Giá trị:** giá trị ghi sổ theo kế toán. Ngoại lệ: nợ phái sinh NSFR tính theo Đ25, nợ thuộc cặp phụ thuộc tính theo Đ26, vốn tự có tính theo TT14/2025 hoặc TT41/2016 [[src-tt50-2026-nhnn#^pl2-a1]].
- **Thứ tự phân loại:** nguồn huy động được xếp vào khoản đầu tiên phù hợp, đi từ trên xuống dưới Bảng 9 [[src-tt50-2026-nhnn#^pl2-a2]]. *Diễn giải:* một khoản nợ thoả hai dòng thì nhận hệ số của dòng ở trên. Ví dụ nợ thuộc cặp phụ thuộc (khoản 2) nhận 0% dù đối tác là khách hàng bán lẻ (khoản 9).
- **Hiệu lực:** NSFR áp dụng từ 01/10/2028 theo lộ trình 90%, 95%, 100% [[src-tt50-2026-nhnn#^d13-1]] [[src-tt50-2026-nhnn#^d22-2]].

### Bước 1: xác định kỳ hạn (Đ23.3)
Kỳ hạn là khoảng thời gian từ ngày tính NSFR đến thời điểm **sớm nhất** phải thực hiện nghĩa vụ [[src-tt50-2026-nhnn#^d23-1]]. Cột kỳ hạn của Bảng 9 (không kỳ hạn, dưới 6 tháng, 6 tháng – dưới 1 năm, từ 1 năm, không xác định) chọn theo kỳ hạn này.

| Tình huống quyền chọn | Kỳ hạn dùng để phân loại | Căn cứ |
|---|---|---|
| Không bên nào có quyền mua lại, rút trước hạn | Thời điểm đến hạn theo thoả thuận | [[src-tt50-2026-nhnn#^d23-1]] |
| Khách hàng có quyền rút trước hạn, bán lại | Thời điểm sớm nhất khách hàng được thực hiện quyền | [[src-tt50-2026-nhnn#^d23-1]] |
| Ngân hàng có quyền mua lại, thanh toán sớm, chưa thông báo | Thời điểm đến hạn | [[src-tt50-2026-nhnn#^d23-3c]] |
| Ngân hàng đã thông báo mua lại, thanh toán sớm | Thời điểm sớm nhất trong thông báo | [[src-tt50-2026-nhnn#^d23-3c]] |
| Cả ngân hàng và khách hàng cùng có quyền | Thời điểm sớm hơn trong hai cách trên | [[src-tt50-2026-nhnn#^d23-3c]] |
| Có quyền gia hạn (cơ cấu lại thời hạn trả nợ, kéo dài kỳ hạn trái phiếu) | Giả định không thực hiện quyền gia hạn | [[src-tt50-2026-nhnn#^d23-1]] |
| Phải thanh toán sớm theo kết luận thanh tra, kiểm tra | Thời hạn phải thanh toán; vi phạm thì toàn bộ số dư còn lại nhận ASF 0% | [[src-tt50-2026-nhnn#^d23-1]] |
| Nguồn vốn trả nhiều kỳ | Tách từng phần trả nợ theo thời điểm trả | [[src-tt50-2026-nhnn#^d23-3g]] |

*Diễn giải:* nguyên tắc chung là chọn kỳ hạn **ngắn nhất có thể xảy ra** cho bên nợ. Mọi quyền làm nguồn vốn rời ngân hàng sớm hơn đều được giả định thực hiện; quyền kéo dài thì giả định không thực hiện. Ngoại lệ là quyền mua lại của ngân hàng: chưa thông báo thì chưa tính. Với RSF, phía tài sản dùng nguyên tắc ngược lại, chọn thời điểm **muộn nhất** [[src-tt50-2026-nhnn#^d24-1]].

### Bước 2: phân loại 14 khoản Bảng 9
Hệ số theo cột: không kỳ hạn / dưới 6 tháng / 6 tháng – dưới 1 năm / từ 1 năm / không xác định kỳ hạn. Ô trống là cột không áp dụng cho khoản đó.

| Khoản | Đầu mục | KKH | < 6T | 6T–1N | ≥ 1N | KXĐ | Căn cứ |
|---|---|---|---|---|---|---|---|
| 1.1 | Vốn cấp 1 | 100% | | | | | [[src-tt50-2026-nhnn#^pl2-a2-1]] |
| 1.2 | Vốn cấp 2 | | 0% | 50% | 100% | 100% | [[src-tt50-2026-nhnn#^pl2-a2-1]] |
| 1.3 | Công cụ vốn chủ sở hữu khác | 0% | 0% | 50% | 100% | 100% | [[src-tt50-2026-nhnn#^pl2-a2-1]] |
| 2 | Nợ thuộc cặp tài sản – nợ phụ thuộc | 0% | 0% | 0% | 0% | | [[src-tt50-2026-nhnn#^pl2-a2-2]] |
| 3 | Nợ phái sinh NSFR ròng | 0% | | | | | [[src-tt50-2026-nhnn#^pl2-a2-2]] |
| 4 | Trade date payables | 0% | | | | | [[src-tt50-2026-nhnn#^pl2-a2-2]] |
| 5 | Thuế thu nhập hoãn lại phải trả | 0% | 0% | 50% | 100% | 0% | [[src-tt50-2026-nhnn#^pl2-a2-2]] |
| 6 | Phát hành trái phiếu | | 0% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 7.1–7.2 | Chính phủ, KBNN, UBND cấp tỉnh, BHTG, BHXH…: tiền gửi | 50% | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 7.3 | Như trên: nguồn khác | | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 8.1 | NHNN, NHTW nước ngoài: tiền gửi hoạt động | 50% | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 8.2–8.3 | NHNN, NHTW nước ngoài: tiền gửi khác, nguồn khác | 0% | 0% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-6]] |
| 9.1 / 10.1 | Bán lẻ, DNNVV: tiền gửi ổn định | 95% | 95% | 95% | 100% hoặc 95% | | [[src-tt50-2026-nhnn#^pl2-a2-9]] |
| 9.2 / 10.2 | Bán lẻ, DNNVV: tiền gửi kém ổn định | 90% | 90% | 90% | 100% hoặc 90% | | [[src-tt50-2026-nhnn#^pl2-a2-9]] |
| 9.3 / 10.3 | Bán lẻ, DNNVV: vốn vay, nợ khác | | 0% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-9]] |
| 11.1 | Tổ chức tài chính: tiền gửi hoạt động | 50% | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-11]] |
| 11.2–11.3 | TCTD, chi nhánh NHNNg, tổ chức tài chính khác | 0% | 0% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-11]] |
| 12 | DN không phải tổ chức tài chính (mọi loại nguồn) | 50% | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-11]] |
| 13.1 | Tổ chức khác: tiền gửi hoạt động | 50% | 50% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-11]] |
| 13.2–13.3 | Tổ chức khác: tiền gửi khác, nguồn khác | 0% | 0% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-11]] |
| 14.1 | Nợ và vốn khác có kỳ hạn | | 0% | 50% | 100% | | [[src-tt50-2026-nhnn#^pl2-a2-11]] |
| 14.2 | Nợ và vốn khác không xác định kỳ hạn, vị thế bán | | | | | 0% | [[src-tt50-2026-nhnn#^pl2-a2-11]] |

Ô "100% hoặc 95%/90%" của khoản 9–10: 100% khi tiền gửi không được rút trước hạn hoặc thuộc điểm a(iii) khoản 4 Mục I Phần B PL I; 95% hoặc 90% khi được rút trước hạn ngoài trường hợp đó [[src-tt50-2026-nhnn#^pl2-a2-9]].

### Bước 3: giải trình từng đầu mục

**Khoản 1, vốn tự có.** Vốn cấp 1 tính theo vốn lõi cấp 1 và vốn bổ sung cấp 1 *chưa giảm trừ* (TT14) hoặc vốn cấp 1 (TT41), trừ một số mục, và nhận 100% không phụ thuộc kỳ hạn [[src-tt50-2026-nhnn#^pl2-a2-1]]. Vốn cấp 2 nhận hệ số theo kỳ hạn còn lại. Nợ thứ cấp không bị khấu trừ dần theo thời hạn như khi tính vốn, dự phòng chung tính đủ 100% số dư, và hệ số ASF nhân trước khi trừ các khoản mục bị trừ [[src-tt50-2026-nhnn#^pl2-a2-1]]. *Diễn giải:* vốn cấp 1 không có nghĩa vụ hoàn trả nên ổn định tuyệt đối. Vốn cấp 2 là nợ, có ngày đáo hạn, nên mất dần tính ổn định khi tới hạn. Basel tương tự: vốn trước khấu trừ nhận 100%, trừ công cụ Tier 2 còn dưới 1 năm [[src-bcbs-nsfr#^nsf30-10]]. Chi tiết: [[asf-capital-and-long-term-liabilities]].

**Khoản 2–5 và 14, nợ phải trả khác.** Nợ thuộc cặp phụ thuộc nhận 0% ở mọi kỳ hạn, vì tài sản tương ứng cũng nhận RSF 0% [[src-tt50-2026-nhnn#^pl2-a2-2]] [[src-tt50-2026-nhnn#^d26-1]]. Nợ phái sinh chỉ vào ASF phần chênh lệch dương so với tài sản phái sinh, với hệ số 0% [[src-tt50-2026-nhnn#^d25-5]]. Trade date payables nhận 0%. Thuế hoãn lại phải trả nhận hệ số theo kỳ hạn, nhưng 0% khi không xác định kỳ hạn [[src-tt50-2026-nhnn#^pl2-a2-2]]. Vị thế bán và nợ không xác định kỳ hạn nhận 0% [[src-tt50-2026-nhnn#^pl2-a2-11]]. *Diễn giải:* đây là các khoản nợ không phải nguồn tài trợ thật sự (cặp phụ thuộc, nợ phái sinh, phải trả thanh toán) hoặc không đo được độ bền. Chi tiết: [[asf-other-liabilities]].

**Khoản 6, phát hành trái phiếu.** 0% dưới 6 tháng, 50% từ 6 tháng tới dưới 1 năm, 100% từ 1 năm [[src-tt50-2026-nhnn#^pl2-a2-6]]. Khoản 6 đứng trên các khoản theo đối tác (7–13), nên trái phiếu được xếp theo kỳ hạn, không theo người nắm giữ. *Diễn giải:* trái phiếu dưới 6 tháng nhận 0% kể cả khi người nắm giữ là cá nhân. Ngân hàng không biết chắc ai nắm giữ trái phiếu khi đáo hạn, nên hệ số gắn với kỳ hạn. TT50 xếp chứng chỉ tiền gửi là một loại giấy tờ có giá, liệt kê tách khỏi trái phiếu [[src-tt50-2026-nhnn#^d3-3]]. Khoản 6 chỉ ghi phát hành trái phiếu [[src-tt50-2026-nhnn#^pl2-a2-6]], và Bảng 9 không có dòng riêng cho chứng chỉ tiền gửi. Hệ số ASF của chứng chỉ tiền gửi vì vậy chưa xác định được từ TT50 [cần nguồn: hướng dẫn phân loại chứng chỉ tiền gửi; định nghĩa nhận tiền gửi trong Luật Các TCTD mà Đ3.2 dẫn chiếu [[src-tt50-2026-nhnn#^d3-2]]].

**Khoản 7, Chính phủ và khu vực công.** Chính phủ, Chính phủ nước ngoài, PSE nước ngoài, tổ chức tài chính quốc tế, KBNN, UBND cấp tỉnh, BHTG, BHXH: tiền gửi (hoạt động hay không) nhận 50% dưới 1 năm, kể cả không kỳ hạn; 100% từ 1 năm [[src-tt50-2026-nhnn#^pl2-a2-6]]. Basel cho Chính phủ, PSE, MDB 50% dưới 1 năm [[src-bcbs-nsfr#^nsf30-13]]. Chi tiết: [[asf-public-sector-and-central-bank-funding]].

**Khoản 8, NHNN và NHTW nước ngoài.** Tiền gửi hoạt động 50% dưới 1 năm; tiền gửi khác và vốn vay 0% dưới 6 tháng, 50% từ 6 tháng tới dưới 1 năm, 100% từ 1 năm [[src-tt50-2026-nhnn#^pl2-a2-6]]. Basel: NHTW dưới 6 tháng 0% [[src-bcbs-nsfr#^nsf30-14]]. *Diễn giải:* vay NHNN qua OMO, tái cấp vốn ngắn hạn không đóng góp vào ASF.

**Khoản 9, bán lẻ.** Khách hàng bán lẻ là cá nhân, tổ hợp tác, hộ kinh doanh [[src-tt50-2026-nhnn#^pl1-b2-1]]. Tiền gửi ổn định là tiền gửi VNĐ được BHTG bảo hiểm toàn bộ và khách hàng có quan hệ (vay trung dài hạn, hoặc tài khoản thanh toán có giao dịch) [[src-tt50-2026-nhnn#^pl1-b2-2]]; còn lại là kém ổn định, và tiền gửi ngoại tệ luôn kém ổn định [[src-tt50-2026-nhnn#^pl1-b2-1]] [[src-tt50-2026-nhnn#^pl1-b2-3]]. Ổn định nhận 95%, kém ổn định 90% ở mọi cột dưới 1 năm [[src-tt50-2026-nhnn#^pl2-a2-9]].
- Tiền gửi có kỳ hạn từ 1 năm nhận **100%** khi không được rút trước hạn, hoặc khi thuộc điểm a(iii): tiền gửi bán lẻ VNĐ mà khi rút trước hạn khách hàng chỉ được lãi suất tối đa bằng lãi suất không kỳ hạn thấp nhất và không hưởng lợi ích khác [[src-tt50-2026-nhnn#^pl2-a2-9]] [[src-tt50-2026-nhnn#^pl1-b1-4a]].
- Được rút trước hạn ngoài điểm a(iii) thì giữ 95% hoặc 90% dù kỳ hạn từ 1 năm [[src-tt50-2026-nhnn#^pl2-a2-9]].
- *Diễn giải:* điểm a(iii) là bản VN của "phạt rút trước hạn đáng kể" trong Basel [[src-bcbs-nsfr#^nsf30-10]]. Hệ quả là sản phẩm tiền gửi có kỳ hạn thiết kế theo a(iii) vừa không tính dòng tiền ra trong LCR [[src-tt50-2026-nhnn#^pl1-b1-4a]], vừa nhận ASF 100% từ 1 năm. Chi tiết: [[asf-retail-and-small-business-deposits]], [[retail-deposit-stability]].
- Vốn vay và nợ khác từ khách hàng bán lẻ (không phải tiền gửi) nhận 0%, 50%, 100% theo kỳ hạn [[src-tt50-2026-nhnn#^pl2-a2-9]].

**Khoản 10, DNNVV đủ điều kiện.** Hệ số giống bán lẻ [[src-tt50-2026-nhnn#^pl2-a2-9]]. DNNVV đủ điều kiện phải không phải tổ chức tài chính, là DNNVV theo pháp luật, và có tổng tiền gửi bình quân tháng liền kề tại ngân hàng không quá 30 tỷ đồng [[src-tt50-2026-nhnn#^pl1-b3-22]]. *Diễn giải:* DNNVV vượt 30 tỷ đồng chuyển sang khoản 12, hệ số giảm từ 95% hoặc 90% xuống 50%.

**Khoản 11, tổ chức tài chính.** Tiền gửi hoạt động 50% dưới 1 năm. TCTD, chi nhánh NHNNg và tổ chức tài chính khác: 0% không kỳ hạn và dưới 6 tháng, 50% từ 6 tháng, 100% từ 1 năm [[src-tt50-2026-nhnn#^pl2-a2-11]]. Basel giống [[src-bcbs-nsfr#^nsf30-14]] [[src-bcbs-nsfr#^nsf30-13]]. *Diễn giải:* nguồn liên ngân hàng ngắn hạn có thể rút ngay khi thị trường căng thẳng, nên không được coi là nguồn ổn định.

**Khoản 12, doanh nghiệp không phải tổ chức tài chính.** Tiền gửi hoạt động, tiền gửi khác và nguồn khác đều 50% dưới 1 năm, 100% từ 1 năm [[src-tt50-2026-nhnn#^pl2-a2-11]]. Basel: 50% [[src-bcbs-nsfr#^nsf30-13]]. Chi tiết: [[asf-wholesale-and-operational-funding]].

**Khoản 13, tổ chức khác.** Tiền gửi hoạt động 50%; tiền gửi khác và nguồn khác 0% dưới 6 tháng, 50% từ 6 tháng [[src-tt50-2026-nhnn#^pl2-a2-11]]. *Diễn giải:* nhóm này chặt hơn doanh nghiệp (khoản 12). Bảng 9 không định nghĩa "tổ chức khác"; nguồn vốn bán buôn trong PL I gồm cả tổ chức không có tư cách pháp nhân [[src-tt50-2026-nhnn#^pl1-b3-1]] [cần nguồn: định nghĩa tổ chức khác].

**Tiền gửi hoạt động (khoản 7.1, 8.1, 11.1, 12.1, 13.1).** Xác định theo khoản 2.3 Mục III Phần B PL I, nhận 50% dưới 1 năm cho mọi nhóm đối tác [[src-tt50-2026-nhnn#^pl2-a2-6]] [[src-tt50-2026-nhnn#^pl2-a2-11]]. Xem [[operational-deposits]].

### Ví dụ minh hoạ
*Diễn giải:* số giả định, đơn vị tỷ đồng, ngân hàng tổng nguồn vốn 1.000.

| Đầu mục | Khoản | Kỳ hạn | Số dư | Hệ số | ASF |
|---|---|---|---|---|---|
| Vốn cấp 1 | 1.1 | — | 80 | 100% | 80 |
| Nợ thứ cấp (vốn cấp 2) | 1.2 | ≥ 1N | 20 | 100% | 20 |
| Nợ thứ cấp (vốn cấp 2) | 1.2 | 8 tháng | 10 | 50% | 5 |
| Trái phiếu phát hành | 6 | ≥ 1N | 30 | 100% | 30 |
| Trái phiếu phát hành | 6 | < 6T | 20 | 0% | 0 |
| Tiền gửi KBNN không kỳ hạn | 7.2 | KKH | 40 | 50% | 20 |
| Vay NHNN qua OMO | 8.3 | < 6T | 30 | 0% | 0 |
| Bán lẻ ổn định không kỳ hạn | 9.1.3 | KKH | 150 | 95% | 142,5 |
| Bán lẻ kém ổn định có kỳ hạn | 9.2.1 | < 1N | 300 | 90% | 270 |
| Bán lẻ có kỳ hạn thuộc điểm a(iii) | 9.1.1 | ≥ 1N | 50 | 100% | 50 |
| DNNVV ổn định không kỳ hạn | 10.1.3 | KKH | 40 | 95% | 38 |
| DN phi tài chính có kỳ hạn | 12.2 | < 1N | 120 | 50% | 60 |
| TCTD gửi | 11.2 | < 6T | 70 | 0% | 0 |
| TCTD gửi | 11.2 | 6T–1N | 20 | 50% | 10 |
| Tổ chức khác, tiền gửi không phải hoạt động | 13.2 | < 6T | 10 | 0% | 0 |
| Nợ phái sinh ròng | 3 | — | 5 | 0% | 0 |
| Nợ khác không xác định kỳ hạn | 14.2 | KXĐ | 5 | 0% | 0 |
| **Tổng** | | | **1.000** | | **725,5** |

ASF bằng 72,55% tổng nguồn vốn. Ba khoản kéo ASF xuống nhiều nhất: nguồn TCTD dưới 6 tháng (70), vay NHNN ngắn hạn (30) và trái phiếu dưới 6 tháng (20) nhận 0%, cộng 120 tỷ đồng mất đi. Chuyển 100 tỷ đồng tiền gửi bán lẻ kém ổn định dưới 1 năm sang sản phẩm có kỳ hạn từ 1 năm thuộc điểm a(iii) tăng ASF thêm 10 (từ 90% lên 100%).

---

## Basel vs VN

| Tham số / Khoản mục | Chuẩn mực Basel (BCBS) | Việt Nam ([[tt50-2026\|TT50/2026/TT-NHNN]]) | Căn cứ Điều khoản | Ghi chú & Lộ trình |
|---|---|---|---|---|
| Tiền gửi bán lẻ stable | ASF 95% (có bảo hiểm hiệu quả) | 95% (không kỳ hạn; có kỳ hạn < 1 năm); có kỳ hạn ≥ 1 năm: 100% nếu không được rút trước hạn, 95% nếu được rút trước hạn [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.11 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Tiền gửi bán lẻ less stable | ASF 90% | 90% (không kỳ hạn; có kỳ hạn < 1 năm); có kỳ hạn ≥ 1 năm: 100% nếu không được rút trước hạn, 90% nếu được rút trước hạn [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.12 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Nguồn vốn bán buôn DN $< 1$Y | ASF 50% | DN phi tài chính: 50% (tiền gửi hoạt động và không hoạt động, < 1 năm) [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.13 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Vốn liên ngân hàng $< 6$M | ASF 0% (triệt tiêu hoàn toàn) | TCTD, chi nhánh NHNNg: 0% (không kỳ hạn và < 6 tháng) [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.14 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Vốn liên ngân hàng 6M–1Y | ASF 50% | TCTD, chi nhánh NHNNg: 50% [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.13 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Vốn tự có & nợ $\ge 1$Y | ASF 100% | Vốn cấp 1: 100%; vốn cấp 2 và nợ ≥ 1 năm: 100% [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.10 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |

Khác biệt (TT50 PL2): tiền gửi bán lẻ và DNNVV có kỳ hạn từ 1 năm trở lên nhưng được rút trước hạn chỉ nhận 95% (ổn định) hoặc 90% (kém ổn định) [[src-tt50-2026-nhnn#^pl2-a2]]. Basel cũng cho 95% hoặc 90% khi rút trước hạn không bị phạt nặng [[src-bcbs-nsfr#^nsf30-11]], nên khác biệt nằm ở tiêu chí ("được rút trước hạn" so với "phạt nặng"), không ở hệ số. Kỳ hạn ASF khi ngân hàng có quyền mua lại: chưa thông báo thì theo đáo hạn, đã thông báo thì theo ngày trong thông báo [[src-tt50-2026-nhnn#^d23-3c]]. Chi tiết theo nhóm: [[asf-capital-and-long-term-liabilities]], [[asf-retail-and-small-business-deposits]], [[asf-wholesale-and-operational-funding]], [[asf-public-sector-and-central-bank-funding]], [[asf-other-liabilities]]. Nguồn huy động từ NHNN không phải tiền gửi hoạt động nhận 0% dưới 6 tháng, 50% từ 6 tháng tới dưới 1 năm [[src-tt50-2026-nhnn#^pl2-a2]].

---

## Ứng dụng trong ALM

1. **Định hình Chiến lược Huy động Nguồn vốn (Funding Strategy)**:
   - ASF là cơ sở để Treasury thiết kế cấu trúc kỳ hạn nợ: ưu tiên phát hành công cụ nợ có kỳ hạn ban đầu trên 2–3 năm để tạo khoảng đệm an toàn trước khi kỳ hạn còn lại trôi về dưới 1 năm.
   - Nhận diện rủi ro "vực thẳm kỳ hạn trôi" (*cliff-edge rollover risk*): khi một khoản nợ liên ngân hàng trôi từ mốc 181 ngày về 179 ngày, hệ số ASF giảm sút tức thì từ 50% về 0%, gây sốc giảm tử số NSFR.
2. **Cơ chế Định giá Điều chuyển Vốn Nội bộ (Term Liquidity FTP)**:
   - Treasury trả thưởng thanh khoản cao (FTP Incentive) cho các chi nhánh huy động tiền gửi cá nhân và SME nhờ hệ số ASF 90%–95%.
   - Phạt chi phí vốn đối với các khoản vốn ngắn hạn liên ngân hàng vì không mang lại giá trị ASF nào cho tỷ lệ NSFR [[src-bcbs-nsfr#^nsf30-14]].
3. **Phòng ngừa Rủi ro Thanh khoản Hệ thống**:
   - Với [[silicon-valley-bank|Silicon Valley Bank]] (SVB), khoảng 45% tiền gửi là tiền của start-up và VC chỉ gửi tạm; trong Q1/2023 nhà đầu tư tìm cách rút 42 tỷ USD trong một ngày [[src-tata-bank-alm#^tata-svb-7]]. Cuối 2021, hơn 88% tiền gửi không được FDIC bảo hiểm [[src-tata-bank-alm#^tata-svb-4]]. NSFR hiệu chuẩn độ ổn định của nguồn nợ theo kỳ hạn và loại nguồn, đối tác [[src-bcbs-nsfr#^nsf30-2]]. *Diễn giải:* tiền gửi bán buôn của doanh nghiệp phi tài chính và quỹ đầu tư như vậy rơi vào nhóm ASF thấp, nên khung ASF phản ánh đúng loại nguồn vốn đã rời SVB; xem [[asf-wholesale-and-operational-funding]].

---

## Nhầm lẫn thường gặp

1. **Nhầm lẫn giữa ASF của NSFR và Run-off của LCR**: Trong LCR, tiền gửi có kỳ hạn $> 30$ ngày nhận dòng ra 0% (rất tốt). Nhưng trong NSFR, nếu khoản tiền gửi đó có kỳ hạn còn lại $< 6$ tháng và từ định chế tài chính, nó nhận ASF 0% (hoàn toàn không có giá trị ổn định).
2. **Nhầm lẫn về Tiền gửi Bán buôn Doanh nghiệp**: Tiền gửi doanh nghiệp kỳ hạn 9 tháng nhận ASF 50% (không phải 0% như liên ngân hàng), vì Basel công nhận doanh nghiệp phi tài chính duy trì tiền gửi phục vụ hoạt động sản xuất kinh doanh thực tế.
3. **Bỏ qua Cắt lát Dòng tiền (Cash Flow Slicing)**: Nhiều ngân hàng tính gộp toàn bộ dư nợ của một khoản vay dài hạn có trả gốc định kỳ vào nhóm ASF 100%. Quy định Basel bắt buộc phải bóc tách các đợt trả nợ gốc rơi vào 12 tháng tới để áp hệ số 50% hoặc 0% [[src-bcbs-nsfr#^nsf30-7]].

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
