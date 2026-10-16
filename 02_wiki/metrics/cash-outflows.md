---
title: Total expected cash outflows (LCR)
aliases: [Cash outflows, Dòng tiền ra kỳ vọng, LCR cash outflows, Total cash outflows, Dòng tiền ra LCR]
type: metric
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of: 2026-10-16
sources: ["[[src-bcbs-lcr]]"]
relations:
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: input-to, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
tags: [liquidity, cash-outflow, run-off, stress-test]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

**Total expected cash outflows** (Tổng dòng tiền ra kỳ vọng) là cấu phần lớn nhất và mang tính quyết định trong mẫu số [[net-cash-outflows]] của tỷ lệ [[lcr]], đại diện cho tổng quy mô các dòng tiền mặt mà ngân hàng phải chi trả hoặc bị rút ra trong kịch bản kiểm tra sức chịu tải thanh khoản nghiêm ngặt kéo dài 30 ngày dương lịch [[src-bcbs-lcr#^lcr20-1]] [[src-bcbs-lcr#^lcr40-1]].

Khác với dòng tiền vào ([[cash-inflows]]) được khống chế bởi trần khấu trừ 75%, dòng tiền ra phản ánh các nghĩa vụ nợ nội bảng và cam kết ngoại bảng phải thực hiện theo tỷ lệ rút vốn ([[run-off-rate]]) hoặc tỷ lệ giải ngân (*drawdown rate*) do chuẩn mực Basel quy định cho từng danh mục đối tác và cấu trúc sản phẩm [[src-bcbs-lcr#^lcr40-1]].

Quy mô dòng tiền ra gộp là căn cứ trực tiếp để thiết lập quy mô tối thiểu bắt buộc của kho tài sản thanh khoản cao ([[hqla]]), bởi vì ngay cả khi ngân hàng có dòng tiền vào dồi dào, mẫu số LCR vẫn bị chặn dưới bởi **$25\% \times \text{Total Cash Outflows}$** [[src-bcbs-lcr#^lcr40-77]].

---

## Công thức & tham số

### Nguyên lý Xác định và Phạm vi Tính toán

#### 1. Công thức Toán học Tổng quát
Dòng tiền ra gộp được tính bằng tổng tích số giữa số dư phơi nhiễm và tỷ lệ rút vốn/giải ngân tương ứng:

$$
\text{Total Cash Outflows} = \sum_{i} B_i^{\text{out}} \times r_i^{\text{out}}
$$

Trong đó:
- $B_i^{\text{out}}$: Số dư nợ gốc, vốn huy động hoặc hạn mức cam kết cấp vốn ngoại bảng thuộc danh mục dòng ra $i$ đến hạn hoặc có thể bị rút trong 30 ngày [[src-bcbs-lcr#^lcr40-1]].
- $r_i^{\text{out}}$: Tỷ lệ rút vốn (*run-off factor*) hoặc tỷ lệ rút vốn hạn mức (*drawdown rate*) áp dụng cho danh mục $i$.
- **Bao gồm lãi dự kiến trả**: Dòng tiền ra trong phạm vi 30 ngày phải bao gồm cả lãi dự kiến phải trả theo hợp đồng (footnote của LCR40.1).

#### 2. Nguyên tắc Thời hạn và Quyền chọn Rút vốn (LCR40.20 - 40.21)
- **Kỳ hạn hợp đồng sớm nhất (*Earliest Contractual Maturity*)**: Tất cả các khoản nợ có kỳ hạn đáo hạn trong vòng 30 ngày hoặc có thể bị gọi vốn trong 30 ngày đều phải đưa vào tính toán [[src-bcbs-lcr#^lcr40-20]].
- **Quyền chọn của bên cấp vốn (*Investor Put Options*)**: Mọi khoản nợ có quyền chọn cho phép nhà đầu tư đòi tiền trước hạn trong vòng 30 ngày đều phải giả định bên cấp vốn sẽ thực hiện quyền chọn rút vốn ở thời điểm sớm nhất [[src-bcbs-lcr#^lcr40-20]].
- **Quyền chọn của ngân hàng và Rủi ro Uy tín (*Bank Call Options & Reputational Triggers*)**: Nếu công cụ nợ có quyền chọn mua lại trước hạn (*call option*) do ngân hàng nắm giữ, nhưng thị trường tài chính kỳ vọng ngân hàng sẽ mua lại trước ngày đáo hạn pháp lý, ngân hàng và cơ quan thanh tra bắt buộc phải giả định quyền chọn sẽ được thực hiện và tính dòng ra tương ứng [[src-bcbs-lcr#^lcr40-20]].
- **Thời hạn thông báo vượt 30 ngày**: Nguồn vốn có điều khoản yêu cầu bên cấp vốn phải gửi thông báo trước (*notice period*) vượt quá 30 ngày thì không bị tính vào dòng tiền ra 30 ngày [[src-bcbs-lcr#^lcr40-20]].

#### 3. Nguyên tắc Chống Đếm Trùng Nghĩa vụ (No Double-Counting Principle - LCR40.4)
Nếu một khoản mục có khả năng bị phân loại vào nhiều danh mục dòng ra khác nhau (ví dụ: hạn mức thanh khoản cam kết cấp cho một đơn vị phát hành thương phiếu nhằm mục đích bảo đảm cho chính khoản giấy tờ có giá đáo hạn trong 30 ngày), ngân hàng chỉ phải tính toán dòng tiền ra tối đa theo hợp đồng đối với sản phẩm đó, không bị cộng dồn hai lần nghĩa vụ [[src-bcbs-lcr#^lcr40-4]].

---

### Bảng Ma trận Tham số Dòng tiền ra Chuẩn mực (Basel Benchmark Matrix)

| STT | Danh mục Dòng tiền ra Gộp | Run-off / Drawdown | Điều kiện chuẩn mực | Căn cứ Block-ID |
|:---:|---|:---:|---|---|
| **1** | Tiền gửi bán lẻ Stable (chuẩn) | **5%** | BHTG hiệu quả VÀ có quan hệ giao dịch/nhận lương | [[src-bcbs-lcr#^lcr40-7]] |
| **2** | Tiền gửi bán lẻ Stable (ưu đãi) | **3%** | Quỹ BHTG prefunding, chi trả $\le 7$ ngày, stress test $< 3\%$ | [[src-bcbs-lcr#^lcr40-11]] |
| **3** | Tiền gửi bán lẻ Less Stable | **$\ge 10\%$** | Không bảo hiểm toàn bộ, số dư lớn, HNW, internet, ngoại tệ | [[src-bcbs-lcr#^lcr40-13]] |
| **4** | Tiền gửi bán lẻ có kỳ hạn $> 30$ ngày | **0%** | Không có quyền rút hoặc phạt nặng hơn mất lãi | [[src-bcbs-lcr#^lcr40-16]] |
| **5** | Tiền gửi SME ($< 1$M EUR) | **5% / $\ge 10\%$** | Áp dụng khung phân loại bán lẻ (tính gộp trên cơ sở hợp nhất) | [[src-bcbs-lcr#^lcr40-22]] |
| **6** | Tiền gửi Operational (Clearing, Custody, Cash Mgmt) | **25%** | Phụ thuộc thực chất, thông báo $\ge 30$ ngày / chi phí chuyển đổi cao | [[src-bcbs-lcr#^lcr40-26]] |
| **7** | Tiền gửi Operational (được bảo hiểm toàn bộ) | **5%** | Phần số dư operational được BHTG bảo hiểm toàn bộ | [[src-bcbs-lcr#^lcr40-36]] |
| **8** | Số dư thặng dư ngoài Operational (*Excess Balance*) | **40% / 100%** | Phần số dư vượt quá nhu cầu thanh toán/vận hành | [[src-bcbs-lcr#^lcr40-29]] |
| **9** | Tiền gửi trong mạng lưới ngân hàng hợp tác xã | **25%** | Dự trữ bắt buộc hoặc nhiệm vụ chung, có quỹ bảo vệ tương hỗ | [[src-bcbs-lcr#^lcr40-37]] |
| **10** | DN phi tài chính, Sovereign, CB, PSE, MDB | **40%** | Tiền gửi không có quan hệ operational | [[src-bcbs-lcr#^lcr40-40]] |
| **11** | DN phi tài chính / Sovereign (bảo hiểm toàn bộ) | **20%** | Được bảo hiểm toàn bộ bởi BHTG hoặc chính phủ bảo lãnh | [[src-bcbs-lcr#^lcr40-41]] |
| **12** | Tổ chức tài chính (Banks, Broker-dealers, Funds) | **100%** | Toàn bộ tiền gửi và phơi nhiễm không có quan hệ operational | [[src-bcbs-lcr#^lcr40-42]] |
| **13** | Giấy tờ nợ ngân hàng tự phát hành đáo hạn $\le 30$D | **100%** | Trừ khi có điều khoản pháp lý cấm chuyển nhượng phi bán lẻ | [[src-bcbs-lcr#^lcr40-43]] |
| **14** | Repo bảo đảm bằng Level 1 hoặc với NHTW | **0%** | Thanh khoản tuyệt đối của tài sản Level 1 | [[src-bcbs-lcr#^lcr40-47]] |
| **15** | Repo bảo đảm bằng Level 2A | **15%** | Tương đương haircut tối thiểu của Level 2A | [[src-bcbs-lcr#^lcr40-48]] |
| **16** | Repo với Sovereign, PSE trong nước (TSBĐ khác L1/2A) | **25%** | Tổ chức công quyền trong nước ít rút vốn repo khi stress | [[src-bcbs-lcr#^lcr40-47]] |
| **17** | Repo bảo đảm bằng Level 2B RMBS | **25%** | Tương đương haircut tối thiểu RMBS Level 2B | [[src-bcbs-lcr#^lcr40-48]] |
| **18** | Repo bảo đảm bằng Level 2B khác | **50%** | Tương đương haircut tối thiểu Level 2B khác | [[src-bcbs-lcr#^lcr40-48]] |
| **19** | Repo bảo đảm bằng Non-HQLA | **100%** | Thị trường repo tài sản rủi ro đóng băng hoàn toàn khi stress | [[src-bcbs-lcr#^lcr40-48]] |
| **20** | Phái sinh ròng theo hợp đồng netting | **100%** | Tính theo từng master netting agreement, options ITM thực hiện | [[src-bcbs-lcr#^lcr40-49]] |
| **21** | Kích hoạt hạ 3 bậc tín nhiệm (*Downgrade Triggers*) | **100%** | Toàn bộ TSBĐ và tiền mặt phải nộp thêm khi bị hạ 3 notch | [[src-bcbs-lcr#^lcr40-51]] |
| **22** | TSBĐ Non-Level 1 đã ký quỹ phái sinh | **+20%** | Khoản phạt bổ sung 20% giá trị TSBĐ vào yêu cầu HQLA | [[src-bcbs-lcr#^lcr40-52]] |
| **23** | Biến động định giá thị trường (*Look-back approach*) | **Max 30D ròng** | Dòng ký quỹ ròng 30 ngày lớn nhất trong 24 tháng gần nhất | [[src-bcbs-lcr#^lcr40-56]] |
| **24** | Hạn mức tín dụng cam kết cấp cho Bán lẻ / SME | **5%** | Credit facilities chưa rút | [[src-bcbs-lcr#^lcr40-64]] |
| **25** | Hạn mức tín dụng cấp cho DN phi tài chính / Chính phủ | **10%** | Credit facilities chưa rút (vốn lưu động xoay vòng) | [[src-bcbs-lcr#^lcr40-64]] |
| **26** | Hạn mức thanh khoản cấp cho DN phi tài chính / Chính phủ | **30%** | Liquidity facilities chưa rút (backstop cho phát hành nợ) | [[src-bcbs-lcr#^lcr40-64]] |
| **27** | Hạn mức tín dụng & thanh khoản cấp cho Ngân hàng | **40%** | Cam kết cấp vốn cho ngân hàng thương mại | [[src-bcbs-lcr#^lcr40-64]] |
| **28** | Hạn mức thanh khoản cấp cho Định chế tài chính khác | **100%** | Cam kết thanh khoản cho công ty chứng khoán, bảo hiểm | [[src-bcbs-lcr#^lcr40-64]] |
| **29** | Hạn mức cấp cho SPE, Conduits, SPVs, Hedge funds | **100%** | Toàn bộ credit và liquidity facilities chưa giải ngân | [[src-bcbs-lcr#^lcr40-64]] |
| **30** | Nghĩa vụ tài trợ thương mại (*Trade finance*) | **$\le 5\%$** | L/C, bảo lãnh thương mại gắn với luân chuyển hàng hóa thực | [[src-bcbs-lcr#^lcr40-71]] |

---

## Diễn giải

### Cấu trúc 5 Trụ cột Toàn diện của Dòng tiền ra

Chuẩn mực LCR40 phân chia toàn bộ nguồn vốn nợ và cam kết ngoại bảng thành 5 trụ cột cấu thành:

```
+-------------------------------------------------------------------------------+
|             TỔNG DÒNG TIỀN RA KỲ VỌNG TRONG 30 NGÀY (TOTAL CASH OUTFLOWS)      |
+-------------------------------------------------------------------------------+
                                         |
     +-----------------+-----------------+-----------------+-----------------+
     |                 |                 |                 |                 |
     v                 v                 v                 v                 v
+----------------+ +----------------+ +----------------+ +----------------+ +----------------+
|  TRỤ CỘT 1     | |  TRỤ CỘT 2     | |  TRỤ CỘT 3     | |  TRỤ CỘT 4     | |  TRỤ CỘT 5     |
| Tiền gửi bán lẻ| | Nguồn vốn bán  | | Nguồn vốn có   | | Phái sinh &    | | Hạn mức cam kết|
| & SME cá nhân  | | buôn không BĐ  | | bảo đảm (Repo) | | Nhu cầu bổ sung| | & Nghĩa vụ TT  |
| (5% / >= 10%)  | | (20% -> 100%)  | | (0% -> 100%)   | | (100% / Add-on)| | (5% -> 100%)   |
+----------------+ +----------------+ +----------------+ +----------------+ +----------------+
```

#### Trụ cột 1: Tiền gửi Bán lẻ và Doanh nghiệp Nhỏ (LCR40.5 - 40.18)
Quy định chi tiết cơ chế phân loại tại [[retail-deposit-stability]]:
1. **Đối tượng áp dụng**: Tiền gửi của thể nhân (*natural persons*) [[src-bcbs-lcr#^lcr40-5]] và khách hàng doanh nghiệp nhỏ (SME) có tổng vốn huy động dưới 1 triệu EUR được quản lý rủi ro như danh mục bán lẻ [[src-bcbs-lcr#^lcr40-22]] [[src-bcbs-lcr#^lcr40-23]].
2. **Tiền gửi ổn định (Stable deposits: 5% hoặc 3%)**:
   - Mức chuẩn 5%: Phải thỏa mãn đồng thời hai điều kiện: (1) Được bảo hiểm toàn bộ bởi hệ thống bảo hiểm tiền gửi hiệu quả (*effective deposit insurance scheme*) hoặc bảo lãnh công quyền; VÀ (2) Người gửi có quan hệ giao dịch khác với ngân hàng hoặc tiền gửi nằm trong tài khoản thanh toán giao dịch (nhận lương tự động) [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-8]].
   - Mức ưu đãi 3%: Quỹ bảo hiểm tiền gửi có cơ chế trích lập trước (*prefunding*), có bảo lãnh thanh khoản từ chính phủ và chi trả trong vòng 7 ngày làm việc; ngân hàng phải chứng minh tỷ lệ rút tiền lịch sử dưới 3% khi có stress [[src-bcbs-lcr#^lcr40-11]] [[src-bcbs-lcr#^lcr40-12]].
   - **Quy tắc hạn mức bảo hiểm**: "Bảo hiểm toàn bộ" áp dụng cho phần số dư nằm trong hạn mức bảo hiểm; phần số dư vượt quá hạn mức lập tức bị tách sang nhóm *less stable* [[src-bcbs-lcr#^lcr40-7]].
3. **Tiền gửi kém ổn định (Less stable deposits: $\ge 10\%$)**:
   - Bao gồm tiền gửi vượt hạn mức bảo hiểm, tiền gửi giá trị lớn, khách hàng cá nhân giàu có (HNW), tiền gửi qua internet và tiền gửi ngoại tệ [[src-bcbs-lcr#^lcr40-13]] [[src-bcbs-lcr#^lcr40-15]].
   - Ngân hàng không phân loại được mặc định xếp 100% vào *less stable* [[src-bcbs-lcr#^lcr40-14]].
4. **Tiền gửi có kỳ hạn $> 30$ ngày**:
   - Loại khỏi dòng ra (run-off 0%) nếu khách hàng không có quyền rút trước hạn hoặc việc rút trước hạn bị phạt lớn hơn đáng kể so với việc mất lãi [[src-bcbs-lcr#^lcr40-16]].
   - **Quy tắc lây lan (*Contagion Rule*)**: Nếu ngân hàng cho phép khách hàng rút tiền gửi có kỳ hạn mà không áp dụng chế tài phạt nghiêm ngặt, cơ quan giám sát sẽ coi **toàn bộ nhóm tiền gửi có kỳ hạn đó** là tiền gửi không kỳ hạn và áp run-off ngay lập tức [[src-bcbs-lcr#^lcr40-17]].
5. **Các quy tắc FAQ bổ sung**:
   - *Tiền gửi cầm cố (Pledged deposits - FAQ1 LCR40.5)*: Được loại trừ khỏi dòng ra nếu bảo đảm cho khoản vay có kỳ hạn $> 30$ ngày, có hợp đồng cấm rút trước hạn và số tiền loại trừ không vượt quá dư nợ vay.
   - *Tiền gửi kim loại quý (Precious metals - FAQ2 LCR40.5)*: Run-off 0% nếu hợp đồng cho phép thanh toán hiện vật và ngân hàng tự cung ứng đủ từ kho kim loại quý của chính mình.

---

#### Trụ cột 2: Nguồn vốn Bán buôn Không Bảo đảm (LCR40.19 - 40.44)
Quy định chi tiết cơ chế phân loại tại [[unsecured-wholesale-funding]] và [[operational-deposits]]:
1. **Khái niệm**: Các khoản nợ và nghĩa vụ huy động từ pháp nhân (công ty, liên doanh, hợp danh, chính phủ, định chế tài chính) không có tài sản bảo đảm cụ thể [[src-bcbs-lcr#^lcr40-19]].
2. **Tiền gửi vận hành (Operational deposits: 25%)**:
   - Phát sinh từ dịch vụ thanh toán bù trừ (*clearing*), lưu ký chứng khoán (*custody*) và quản lý dòng tiền (*cash management*) [[src-bcbs-lcr#^lcr40-26]].
   - Điều kiện: Khách hàng phụ thuộc thực chất vào ngân hàng, hợp đồng ràng buộc có thời hạn thông báo hủy hợp đồng $\ge 30$ ngày hoặc chi phí chuyển đổi (*switching costs*) rất lớn [[src-bcbs-lcr#^lcr40-27]].
   - **Bóc tách số dư thặng dư (*Excess Balance*)**: Phần số dư vượt quá nhu cầu vận hành thực tế phải chuyển sang nhóm non-operational (run-off 40% hoặc 100%) [[src-bcbs-lcr#^lcr40-29]] [[src-bcbs-lcr#^lcr40-30]].
   - Loại trừ hoàn toàn dịch vụ tài khoản ngân hàng đại lý (*correspondent banking*) và môi giới khách hàng tổ chức (*prime brokerage*) (áp run-off 100%) [[src-bcbs-lcr#^lcr40-32]].
3. **Mạng lưới ngân hàng hợp tác xã (25%)**:
   - Tiền gửi của các ngân hàng thành viên tại định chế trung ương của mạng lưới phục vụ yêu cầu dự trữ luật định hoặc nhiệm vụ chung, có quỹ bảo vệ tương hỗ [[src-bcbs-lcr#^lcr40-37]] [[src-bcbs-lcr#^lcr40-39]].
4. **Doanh nghiệp phi tài chính, Sovereign, NHTW, PSE, MDB (40% / 20%)**:
   - Tiền gửi thông thường không phục vụ hoạt động operational: run-off **40%** [[src-bcbs-lcr#^lcr40-40]].
   - Giảm xuống **20%** nếu toàn bộ số dư được quỹ BHTG hiệu quả hoặc chính phủ bảo lãnh toàn bộ [[src-bcbs-lcr#^lcr40-41]].
5. **Định chế tài chính và các pháp nhân khác (100%)**:
   - Ngân hàng thương mại, công ty chứng khoán, công ty bảo hiểm, quỹ đầu tư tín thác (*fiduciaries*), công ty liên kết và SPV/conduit chịu run-off tuyệt đối **100%** [[src-bcbs-lcr#^lcr40-42]].
6. **Giấy tờ nợ ngân hàng tự phát hành (100%)**:
   - Mọi trái phiếu, kỳ phiếu, chứng chỉ tiền gửi đáo hạn trong vòng 30 ngày phải chịu run-off 100%, trừ khi có điều khoản pháp lý ràng buộc cấm chuyển nhượng và chỉ được nắm giữ bởi khách hàng bán lẻ [[src-bcbs-lcr#^lcr40-43]].

---

#### Trụ cột 3: Nguồn vốn Có Bảo đảm (Secured Funding - LCR40.45 - 40.48)
Quy định chi tiết cơ chế phân loại tại [[secured-funding]]:
1. **Bản chất**: Trong stress, khả năng tái cấp vốn cho các giao dịch repo, hoán đổi tài sản bảo đảm (*collateral swaps*) và cho mượn chứng khoán **hoàn toàn phụ thuộc vào chất lượng thanh khoản của tài sản bảo đảm**, không phụ thuộc vào uy tín của đối tác [[src-bcbs-lcr#^lcr40-46]]:
   - Bảo đảm bằng **Level 1 assets** hoặc giao dịch với **Ngân hàng Trung ương**: Dòng ra **0%** [[src-bcbs-lcr#^lcr40-47]] [[src-bcbs-lcr#^lcr40-48]].
   - Bảo đảm bằng **Level 2A assets**: Dòng ra **15%** (bằng mức chiết khấu tối thiểu) [[src-bcbs-lcr#^lcr40-48]].
   - Giao dịch với Sovereign trong nước, PSE (RW $\le 20\%$), MDB bảo đảm bằng tài sản khác L1/L2A: Dòng ra **25%** [[src-bcbs-lcr#^lcr40-47]].
   - Bảo đảm bằng **Level 2B RMBS đủ điều kiện**: Dòng ra **25%** [[src-bcbs-lcr#^lcr40-48]].
   - Bảo đảm bằng **Level 2B khác**: Dòng ra **50%** [[src-bcbs-lcr#^lcr40-48]].
   - Bảo đảm bằng **Tài sản không phải HQLA (Non-HQLA)**: Dòng ra **100%** [[src-bcbs-lcr#^lcr40-48]].
2. **Quy tắc phân bổ nhóm tài sản hỗn hợp (*Collateral Pool Waterfall*)**: Nếu một nhóm tài sản bảo đảm hỗn hợp được cầm cố cho các nghĩa vụ khác nhau mà không thể tách bạch, tài sản có chất lượng thanh khoản thấp nhất phải được ưu tiên phân bổ cho nghĩa vụ có kỳ hạn dài nhất trước [[src-bcbs-lcr#^lcr40-48]].

---

#### Trụ cột 4: Phái sinh và Nhu cầu Bổ sung (LCR40.49 - 40.58)
Quy định chi tiết cơ chế phân loại tại [[derivatives-and-contingent-outflows]]:
1. **Dòng ra phái sinh ròng (100%)**: Tính bù trừ thu/chi theo từng đối tác nếu có thỏa thuận bù trừ song phương (*valid master netting agreement*); các quyền chọn *in-the-money* giả định bị thực hiện theo quy tắc bên có lợi nhất [[src-bcbs-lcr#^lcr40-49]].
2. **Kích hoạt hạ bậc tín nhiệm (*Downgrade Triggers: 100%*)**: Tính 100% tiền mặt hoặc tài sản bảo đảm bổ sung mà ngân hàng bị buộc phải nộp theo hợp đồng khi bị các tổ chức xếp hạng quốc tế hạ bậc tín nhiệm dài hạn tới **3 notch** [[src-bcbs-lcr#^lcr40-51]].
3. **Phạt ký quỹ tài sản Non-Level 1 (+20%)**: Nếu ngân hàng đã đặt cọc tài sản bảo đảm non-L1 cho đối tác, ngân hàng phải bổ sung **20%** giá trị tài sản đó vào dòng ra HQLA yêu cầu để bù đắp rủi ro sụt giá tài sản thế chấp [[src-bcbs-lcr#^lcr40-52]].
4. **Tài sản bảo đảm thặng dư không tách biệt (100%)**: Toàn bộ TSBĐ do đối tác nộp thừa mà đối tác có quyền rút về bất kỳ lúc nào [[src-bcbs-lcr#^lcr40-53]].
5. **Quyền thay thế TSBĐ (*Collateral Substitution: 100%*)**: Đối tác có quyền hoán đổi rút tài sản HQLA về và thay bằng non-HQLA mà không cần ngân hàng phê duyệt [[src-bcbs-lcr#^lcr40-55]].
6. **Biến động định giá thị trường phái sinh (*Look-back approach*)**: Bắt buộc tính dòng ra bằng dòng tài sản bảo đảm ròng 30 ngày lớn nhất từng xảy ra trong **24 tháng** gần nhất [[src-bcbs-lcr#^lcr40-56]].
7. **Chứng khoán hóa và Conduits tự tài trợ (100%)**: Trái phiếu có bảo đảm (covered bonds), ABS tự phát hành đáo hạn $\le 30$ ngày và toàn bộ nhu cầu tài trợ cho các phương tiện đầu tư cấu trúc (ABCP/conduits/SIVs) [[src-bcbs-lcr#^lcr40-57]] [[src-bcbs-lcr#^lcr40-58]].

---

#### Trụ cột 5: Hạn mức Cam kết và Nghĩa vụ Tiềm tàng (LCR40.59 - 40.74)
Quy định chi tiết cơ chế phân loại tại [[committed-facilities]]:
1. **Tỷ lệ giải ngân trên phần hạn mức chưa rút (*Undrawn Drawdown Rate*)**:
   - Phân biệt giữa **Hạn mức Tín dụng (*Credit Facility*)** (tài trợ vốn lưu động thông thường) và **Hạn mức Thanh khoản (*Liquidity Facility*)** (cam kết hỗ trợ tái tài trợ khi khách hàng không đảo được nợ trên thị trường nợ) [[src-bcbs-lcr#^lcr40-61]].

| Đối tượng nhận cam kết | Credit Facility | Liquidity Facility | Căn cứ chuẩn mực |
|---|---|---|---|
| **Bán lẻ và Doanh nghiệp nhỏ (SME)** | **5%** | **5%** | [[src-bcbs-lcr#^lcr40-64]] |
| **Doanh nghiệp phi tài chính, Sovereign, PSE, MDB** | **10%** | **30%** | [[src-bcbs-lcr#^lcr40-64]] |
| **Ngân hàng thương mại chịu giám sát an toàn** | **40%** | **40%** | [[src-bcbs-lcr#^lcr40-64]] |
| **Định chế tài chính khác (chứng khoán, bảo hiểm, quỹ)** | **40%** | **100%** | [[src-bcbs-lcr#^lcr40-64]] |
| **Pháp nhân cấu trúc (SPEs, Conduits, SPVs, Hedge funds)** | **100%** | **100%** | [[src-bcbs-lcr#^lcr40-62]] [[src-bcbs-lcr#^lcr40-64]] |

2. **Nghĩa vụ cấp vốn hợp đồng khác**:
   - Nghĩa vụ cấp vốn cho tổ chức tài chính & NHTW trong 30 ngày: Dòng ra **100%** [[src-bcbs-lcr#^lcr40-65]].
   - Nghĩa vụ cấp vốn cho bán lẻ và DN phi tài chính: Phần cam kết vượt quá 50% dòng vào từ nhóm đó tính dòng ra **100%** [[src-bcbs-lcr#^lcr40-66]].
   - Tài trợ thương mại (*Trade finance*): Thường $\le 5\%$ do cơ quan quản lý quốc gia quy định [[src-bcbs-lcr#^lcr40-71]].
   - Nghĩa vụ tiềm tàng phi hợp đồng do rủi ro uy tín (*reputational concerns*): Bảo trợ quỹ đầu tư, sản phẩm cấu trúc [[src-bcbs-lcr#^lcr40-68]] [[src-bcbs-lcr#^lcr40-70]].
   - Dòng ra hợp đồng khác: **100%** (không bao gồm chi phí hoạt động nội bộ như tiền lương nhân viên hay thuê văn phòng) [[src-bcbs-lcr#^lcr40-74]].

---

### Logic Giả định Hành vi Giám sát (Supervisory Behavioral Hypotheses)

Khung dòng tiền ra của LCR được xây dựng trên 3 giả định kinh tế vĩ mô then chốt:

1. **Phân tầng Tốc độ Tháo chạy theo Mức độ Tinh vi của Chủ nợ (*Information Asymmetry & Sophistication Ladder*)**:
   - Khách hàng bán lẻ được bảo hiểm có chi phí giám sát cao và phản ứng chậm với tin tức thị trường (run-off 5%).
   - Các định chế tài chính chuyên nghiệp vận hành mô hình quản lý vốn tự động và luôn là bên tháo chạy đầu tiên khi có tin đồn (*first-mover advantage*), dẫn đến run-off bắt buộc là **100%**.
2. **Khái niệm Khóa cứng Vận hành (*Operational Interlocking*)**:
   - Các dòng tiền gắn liền với hệ sinh thái vận hành (trả lương, bù trừ séc, thanh toán chứng khoán) có chi phí chuyển đổi rất cao trong ngắn hạn. Do đó, Basel công nhận tỷ lệ bám dính cao hơn đáng kể (run-off 25% so với 40%–100%).
3. **Phòng thủ Đa tầng trước Hiệu ứng Sụt giảm Tín nhiệm (*Multi-tier Anti-cliff Defense*)**:
   - Không chỉ tính các dòng tiền theo hợp đồng hiện tại, Basel bắt buộc tính trước chi phí ký quỹ khi bị hạ 3 bậc tín nhiệm (LCR40.51) và biến động thị trường lịch sử 24 tháng (LCR40.56) nhằm ngăn ngừa tình trạng ngân hàng bị cạn kiệt thanh khoản tức thì khi bước vào khủng hoảng.

---

## Basel vs VN

### Bất định & Hàm ý Triển khai tại Việt Nam

- **Quy định tại Thông tư 50/2026/TT-NHNN**:
  - Phụ lục 1 (PL1) của TT50 quy định chi tiết bảng tỷ lệ rút tiền đối với các loại tiền gửi và cam kết ngoại bảng tại các ngân hàng thương mại Việt Nam `[chờ đối chiếu: src-tt50-2026-nhnn]`.
  - Các vấn đề cần làm rõ khi đối chiếu TT50:
    1. *Hạn mức bảo hiểm tiền gửi tại Việt Nam*: Mức bảo hiểm tối đa hiện hành (125 triệu VND/người gửi) tác động như thế nào đến việc phân tách số dư stable vs less stable theo tinh thần LCR40.7.
    2. *Tỷ lệ rút tiền đối với tiền gửi của Kho bạc Nhà nước và Doanh nghiệp Nhà nước*: Có được xếp vào nhóm Sovereign/PSE (40% / 20%) hay có cơ chế đặc thù riêng.
    3. *Hạn mức thấu chi cá nhân và cam kết cấp tín dụng*: Tỷ lệ drawdown áp dụng trong điều kiện thanh khoản hệ thống ngân hàng Việt Nam.

## Ứng dụng trong ALM

### Ứng dụng Quản trị tại ALM Treasury

Khối ALM Treasury chủ động tác động vào các cấu phần dòng tiền ra thông qua các đòn bẩy chiến lược:

1. **Chiến lược Chuyển dịch Cơ cấu Nguồn vốn (*Liability Restructuring*)**:
   - Thay thế các khoản tiền gửi bán buôn doanh nghiệp lớn ngắn hạn (run-off 40%) bằng tiền gửi thanh toán bán lẻ gắn tài khoản lương (run-off 5%) hoặc tiền gửi dịch vụ quản lý tiền mặt doanh nghiệp (run-off 25%).
   - Hạn chế phát hành chứng chỉ tiền gửi ngắn hạn cho các định chế tài chính (run-off 100%).
2. **Quản trị Tối ưu Hợp đồng Cam kết Ngoại bảng**:
   - Tách bạch rõ ràng hợp đồng hạn mức tín dụng (*Credit Facility*, drawdown 10%) với hạn mức thanh khoản (*Liquidity Facility*, drawdown 30%) trong các hợp đồng tài trợ doanh nghiệp lớn [[src-bcbs-lcr#^lcr40-61]].
   - Rà soát và thu hồi các hạn mức cam kết chưa rút không hoạt động (*dormant credit lines*) để giảm trực tiếp mẫu số dòng ra.
3. **Tối ưu hóa Tài sản Ký quỹ Phái sinh**:
   - Ưu tiên sử dụng Trái phiếu Chính phủ Level 1 để ký quỹ trong các hợp đồng ISDA/CSA nhằm tránh bị phạt cộng thêm **20%** yêu cầu HQLA đối với tài sản non-L1 [[src-bcbs-lcr#^lcr40-52]].
4. **San bằng Thang Đáo hạn (*Maturity Ladder Smoothing*)**:
   - Tránh việc tập trung khối lượng lớn nợ bán buôn hoặc trái phiếu đáo hạn dồn dập vào cùng một khung thời gian 30 ngày.

---

## Nhầm lẫn thường gặp

### Cạm bẫy Thực tiễn và Nhầm lẫn Thường gặp

- ❌ **Cạm bẫy Bù trừ Tự ý (*Unauthorized Netting Pitfall*)**: Bù trừ khoản tiền gửi thanh toán của một doanh nghiệp với hạn mức cho vay ngắn hạn của chính doanh nghiệp đó trên bảng cân đối.
  - *Thực tế*: LCR nghiêm cấm bù trừ dòng ra và dòng vào ngoại trừ các hợp đồng phái sinh có thỏa thuận bù trừ song phương (*valid master netting agreement*) [[src-bcbs-lcr#^lcr40-49]].
- ❌ **Cạm bẫy Rút Tiết kiệm Trước hạn (*Contagion Rule Trap*)**: Chi nhánh ngân hàng linh hoạt cho phép khách hàng VIP rút tiền gửi tiết kiệm có kỳ hạn 6 tháng trước hạn mà chỉ trừ một phần lãi nhỏ.
  - *Thực tế*: Theo LCR40.17, hành vi này có thể khiến cơ quan thanh tra phán quyết rằng biện pháp phạt không đủ tính răn đe và buộc ngân hàng xếp **toàn bộ danh mục tiền gửi có kỳ hạn** sang tiền gửi không kỳ hạn, khiến dòng tiền ra vọt tăng đột biến.
- ❌ **Hiểu nhầm về Nguồn vốn SME**: Cho rằng mọi doanh nghiệp vừa và nhỏ đều được áp hệ số rút vốn bán lẻ (5%–10%).
  - *Thực tế*: Theo LCR40.23, chỉ các SME có tổng vốn huy động dưới 1 triệu EUR (tính gộp trên cơ sở tập đoàn hợp nhất) và được quản lý theo quy trình bán lẻ mới được hưởng cơ chế này.
- ❌ **Ảo tưởng về Hạn mức Cam kết Huỷ ngang có Điều kiện**: Cho rằng hợp đồng ghi "ngân hàng có quyền đơn phương hủy hạn mức" thì không phải tính dòng ra.
  - *Thực tế*: Theo LCR40.59, chuẩn mực tính toán dòng ra cho cả các hạn mức cam kết không hủy ngang và hạn mức hủy ngang có điều kiện (*committed or conditionally cancellable*).

---
