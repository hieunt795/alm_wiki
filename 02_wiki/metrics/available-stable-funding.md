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
updated: 2026-10-20
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

## Basel vs VN

| Tham số / Khoản mục | Chuẩn mực Basel (BCBS) | Việt Nam ([[tt50-2026\|TT50/2026/TT-NHNN]]) | Căn cứ Điều khoản | Ghi chú & Lộ trình |
|---|---|---|---|---|
| Tiền gửi bán lẻ stable | ASF 95% (có bảo hiểm hiệu quả) | 95% (không kỳ hạn; có kỳ hạn < 1 năm); có kỳ hạn ≥ 1 năm: 100% nếu không được rút trước hạn, 95% nếu được rút trước hạn [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.11 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Tiền gửi bán lẻ less stable | ASF 90% | 90% (không kỳ hạn; có kỳ hạn < 1 năm); có kỳ hạn ≥ 1 năm: 100% nếu không được rút trước hạn, 90% nếu được rút trước hạn [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.12 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Nguồn vốn bán buôn DN $< 1$Y | ASF 50% | DN phi tài chính: 50% (tiền gửi hoạt động và không hoạt động, < 1 năm) [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.13 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Vốn liên ngân hàng $< 6$M | ASF 0% (triệt tiêu hoàn toàn) | TCTD, chi nhánh NHNNg: 0% (không kỳ hạn và < 6 tháng) [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.14 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Vốn liên ngân hàng 6M–1Y | ASF 50% | TCTD, chi nhánh NHNNg: 50% [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.13 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |
| Vốn tự có & nợ $\ge 1$Y | ASF 100% | Vốn cấp 1: 100%; vốn cấp 2 và nợ ≥ 1 năm: 100% [[src-tt50-2026-nhnn#^pl2-a2]] | NSF30.10 / TT50 PL2 | NSFR áp dụng từ 01/10/2028 |

Khác biệt (TT50 PL2): tiền gửi bán lẻ và DNNVV có kỳ hạn từ 1 năm trở lên nhưng được rút trước hạn chỉ nhận 95% (ổn định) hoặc 90% (kém ổn định), trong khi Basel cho nợ có kỳ hạn hiệu lực ≥ 1 năm hệ số 100% [[src-tt50-2026-nhnn#^pl2-a2]]. Nguồn huy động từ NHNN không phải tiền gửi hoạt động nhận 0% dưới 6 tháng, 50% từ 6 tháng tới dưới 1 năm [[src-tt50-2026-nhnn#^pl2-a2]].

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
