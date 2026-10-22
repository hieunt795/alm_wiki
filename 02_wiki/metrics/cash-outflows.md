---
title: Total expected cash outflows (LCR)
aliases: [Cash outflows, Dòng tiền ra kỳ vọng, LCR cash outflows, Total cash outflows, Dòng tiền ra LCR]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of: 2026-10-20
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: input-to, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
tags: [liquidity, cash-outflow, run-off, stress-test]
updated: 2026-10-22
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
- **Bao gồm lãi dự kiến trả**: Dòng tiền ra trong phạm vi 30 ngày phải bao gồm cả lãi dự kiến phải trả theo hợp đồng (chú thích của LCR40.1) [cần nguồn: chú thích LCR40.1 chưa có claim trong src-bcbs-lcr].

#### 2. Nguyên tắc Thời hạn và Quyền chọn Rút vốn (LCR40.20 - 40.21)
- **Kỳ hạn hợp đồng sớm nhất (*Earliest Contractual Maturity*)**: Tất cả các khoản nợ có kỳ hạn đáo hạn trong vòng 30 ngày hoặc có thể bị gọi vốn trong 30 ngày đều phải đưa vào tính toán [[src-bcbs-lcr#^lcr40-20]].
- **Quyền chọn của bên cấp vốn (*Investor Put Options*)**: Mọi khoản nợ có quyền chọn cho phép nhà đầu tư đòi tiền trước hạn trong vòng 30 ngày đều phải giả định bên cấp vốn sẽ thực hiện quyền chọn rút vốn ở thời điểm sớm nhất [[src-bcbs-lcr#^lcr40-20]].
- **Quyền chọn của ngân hàng và [[reputational-risk|Rủi ro Uy tín]] (*Bank Call Options & Reputational Triggers*)**: Nếu công cụ nợ có quyền chọn mua lại trước hạn (*call option*) do ngân hàng nắm giữ, nhưng thị trường tài chính kỳ vọng ngân hàng sẽ mua lại trước ngày đáo hạn pháp lý, ngân hàng và cơ quan thanh tra bắt buộc phải giả định quyền chọn sẽ được thực hiện và tính dòng ra tương ứng [[src-bcbs-lcr#^lcr40-20]].
- **Thời hạn báo trước vượt 30 ngày**: vốn bán buôn mà bên cấp vốn có quyền đòi nhưng phải tuân thời hạn báo trước theo hợp đồng vượt 30 ngày thì không tính vào dòng ra [[src-bcbs-lcr#^lcr40-21]]. TT50 có quy định tương ứng: nguồn vốn có quyền rút trước hạn với thời gian thông báo trên 30 ngày mà khách hàng chưa thông báo rút thì không tính [[src-tt50-2026-nhnn#^pl1-b1-4a]].

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
| **30** | Nghĩa vụ tài trợ thương mại (*Trade finance*) | **$\le 5\%$** | L/C, bảo lãnh thương mại gắn với luân chuyển hàng hóa thực | [[src-bcbs-lcr#^lcr40-71]] [[src-bcbs-lcr#^lcr40-71b]] |

---

## Diễn giải

### Cấu trúc 5 Trụ cột Toàn diện của Dòng tiền ra

*Diễn giải:* cách gom LCR40 thành 5 trụ cột dưới đây là của wiki, không phải của chuẩn mực. Tham số từng trụ cột cite ở các mục bên dưới.

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

#### Trụ cột 1: Tiền gửi Bán lẻ và Doanh nghiệp Nhỏ (LCR40.5 – 40.18, 40.22 – 40.23)
Quy định chi tiết cơ chế phân loại tại [[retail-deposit-stability]]:

##### 1.1. Tiền gửi bán lẻ ổn định chuẩn (Stable retail deposits — 5%)
- **Phạm vi và Điều kiện quy chuẩn**: Áp dụng cho tiền gửi của thể nhân (*natural persons*) [[src-bcbs-lcr#^lcr40-5]] thỏa mãn đồng thời hai điều kiện: (1) Được bảo hiểm toàn bộ bởi hệ thống bảo hiểm tiền gửi hiệu quả (*effective deposit insurance scheme*) hoặc bảo lãnh công quyền tương đương; VÀ (2) Người gửi tiền có quan hệ giao dịch khác với ngân hàng, hoặc tiền gửi nằm trong tài khoản thanh toán giao dịch (ví dụ tài khoản nhận lương tự động) [[src-bcbs-lcr#^lcr40-7]]. Hệ thống BHTG hiệu quả phải thỏa mãn 4 tiêu chí: có khả năng chi trả nhanh, phạm vi bảo hiểm rõ ràng, nhận thức công chúng cao, và tổ chức BHTG có quyền lực pháp lý, độc lập vận hành và minh bạch [[src-bcbs-lcr#^lcr40-8]]. Chỉ có bảo hiểm tiền gửi mà không có quan hệ giao dịch thì không đủ điều kiện xếp vào nhóm ổn định [[src-bcbs-lcr#^lcr40-10]]. "Bảo hiểm toàn bộ" chỉ áp dụng cho phần số dư nằm trong hạn mức bảo hiểm; phần vượt hạn mức bị tách sang nhóm kém ổn định [[src-bcbs-lcr#^lcr40-7]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Hệ số rút vốn 5% dựa trên hiện tượng "tính ỳ hành vi" (*behavioral inertia*) của cá nhân nhỏ lẻ. Khi tin tức xấu lan truyền, việc tiền gửi được nhà nước bảo lãnh hoàn toàn làm triệt tiêu động cơ kinh tế thúc đẩy người dân tháo chạy rút tiền (*no incentive to run*). Việc gắn với tài khoản nhận lương hay thanh toán hóa đơn sinh hoạt định kỳ tạo ra chi phí chuyển đổi (*switching costs*) rất cao; người gửi tiền không thể đóng tài khoản ngay trong 30 ngày mà không gây gián đoạn nghiêm trọng tới đời sống hàng ngày.
- *Hàm ý ALM:* Khối ALM và Bán lẻ cần phối hợp thiết kế các gói sản phẩm tiền gửi gắn liền với tài khoản chi lương và ngân hàng giao dịch chính (*primary transactional bank*) để tối đa hóa phần số dư hưởng hệ số 5%, giúp tiết giảm chi phí duy trì đệm HQLA.

##### 1.2. Tiền gửi bán lẻ ổn định ưu đãi (Stable retail deposits with pre-funded scheme — 3%)
- **Phạm vi và Điều kiện quy chuẩn**: Cơ quan giám sát quốc gia có quyền lựa chọn áp dụng hệ số rút vốn ưu đãi 3% nếu hệ thống BHTG đáp ứng thêm các tiêu chuẩn nghiêm ngặt: quỹ BHTG có cơ chế tích lũy trước (*prefunded*) bằng phí thu từ các thành viên; có quyền tiếp cận nguồn hỗ trợ thanh khoản công từ chính phủ khi stress; cam kết thời gian chi trả bồi thường cho người gửi tiền không quá 7 ngày làm việc [[src-bcbs-lcr#^lcr40-11]]; và ngân hàng phải cung cấp bằng chứng chứng minh tỷ lệ rút vốn thực tế của nhóm tiền gửi ổn định trong toàn hệ thống ngân hàng dưới 3% qua các cuộc khủng hoảng lịch sử [[src-bcbs-lcr#^lcr40-12]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Ngưỡng chi trả trong vòng 7 ngày là then chốt. Sự sợ hãi lớn nhất của người gửi tiền cá nhân không phải là mất toàn bộ vốn (do đã có BHTG), mà là rủi ro bị "đóng băng thanh khoản" kéo dài hàng tháng trong thời gian thanh lý ngân hàng, khiến họ không có tiền chi tiêu. Cam kết chi trả $\le 7$ ngày loại bỏ hoàn toàn rủi ro này, biến tiền gửi thành một công cụ gần như không chịu rủi ro thanh khoản.

##### 1.3. Tiền gửi bán lẻ kém ổn định (Less stable retail deposits — $\ge 10\%$)
- **Phạm vi và Điều kiện quy chuẩn**: Áp dụng hệ số rút vốn tối thiểu 10% [[src-bcbs-lcr#^lcr40-13]]. Supervisor quốc gia có trách nhiệm phân chia thành các nhóm với hệ số rút vốn cao hơn (15%, 20% hoặc cao hơn), bao gồm: phần tiền gửi vượt hạn mức BHTG, tiền gửi số dư lớn, tiền gửi của khách hàng cá nhân giàu có hoặc am hiểu tài chính (HNW), tiền gửi có thể rút nhanh qua kênh số hoặc internet banking, và tiền gửi bằng ngoại tệ [[src-bcbs-lcr#^lcr40-13]] [[src-bcbs-lcr#^lcr40-15]]. Nếu ngân hàng không đủ dữ liệu để chứng minh điều kiện phân loại vào nhóm ổn định, bắt buộc phải xếp toàn bộ 100% số dư vào nhóm kém ổn định [[src-bcbs-lcr#^lcr40-14]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:*
  - *Phần vượt hạn mức BHTG*: Chịu rủi ro mất vốn trực tiếp khi ngân hàng phá sản, do đó có động lực kinh tế mạnh nhất để rút tiền ngay khi xuất hiện dấu hiệu bất an.
  - *Khách hàng HNW*: Có quan hệ với nhiều ngân hàng, theo dõi sát sao thị trường và thường xuyên dịch chuyển dòng vốn lớn nhằm bảo toàn tài sản hoặc săn tìm lợi suất.
  - *Kênh internet/digital banking*: Giảm chi phí giao dịch rút tiền xuống mức gần bằng 0; người gửi tiền có thể chuyển dịch dòng vốn chỉ bằng vài thao tác trên ứng dụng di động trong vài giây.
  - *Tiền gửi ngoại tệ*: Phản ánh tâm lý phòng hộ biến động kinh tế vĩ mô hoặc đầu cơ tỷ giá, dễ bị rút ra khỏi ngân hàng nội địa để chuyển ra nước ngoài hoặc găm giữ tiền mặt.

##### 1.4. Tiền gửi bán lẻ có kỳ hạn $> 30$ ngày (Term deposits — 0%) và Quy tắc Lây lan (*Contagion Rule*)
- **Phạm vi và Điều kiện quy chuẩn**: Được loại trừ hoàn toàn khỏi dòng tiền ra (run-off 0%) nếu hợp đồng quy định người gửi tiền không có quyền rút vốn trước hạn trong 30 ngày, HOẶC việc rút vốn trước hạn phải chịu chế tài phạt tài chính đáng kể vượt quá mức mất lãi thuần túy [[src-bcbs-lcr#^lcr40-16]].
- **Quy tắc lây lan (Contagion Rule)**: Nếu ngân hàng cho phép khách hàng rút tiền gửi có kỳ hạn mà không áp dụng chế tài phạt nghiêm ngặt (hoặc chỉ phạt tượng trưng), cơ quan giám sát bắt buộc phải coi **toàn bộ nhóm tiền gửi có kỳ hạn đó** là tiền gửi không kỳ hạn và áp run-off ngay lập tức [[src-bcbs-lcr#^lcr40-17]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Chế tài phạt thiệt hại tài chính nặng (như khấu trừ vào nợ gốc hoặc tịch thu toàn bộ lợi tức tích lũy) tạo ra rào cản kinh tế thực tế ngăn người gửi tiền phá vỡ hợp đồng. Quy tắc lây lan nhằm triệt tiêu "rủi ro đạo đức" (*moral hazard*): ngăn ngân hàng nhượng bộ ngầm cho các khách hàng VIP rút tiền sớm để duy trì mối quan hệ kinh doanh, đẩy rủi ro thiếu hụt thanh khoản lên toàn bộ hệ thống.

##### 1.5. Tiền gửi Doanh nghiệp nhỏ (Small Business Customers / SME — 5% / $\ge 10\%$)
- **Phạm vi và Điều kiện quy chuẩn**: Áp dụng cơ chế phân loại và hệ số rút vốn tương tự như tiền gửi bán lẻ (5% ổn định, $\ge 10\%$ kém ổn định) nếu tổng số dư vốn huy động từ một khách hàng SME nhỏ hơn 1 triệu EUR (tính gộp trên cơ sở tập đoàn hợp nhất) và được ngân hàng quản lý rủi ro nhất quán theo danh mục bán lẻ [[src-bcbs-lcr#^lcr40-22]] [[src-bcbs-lcr#^lcr40-23]]. Ngân hàng không có dư nợ với khách hàng để dùng định nghĩa SME theo CRE30 vẫn có thể xếp tiền gửi vào nhóm này nếu tổng vốn huy động dưới 1 triệu EUR và được quản lý như tiền gửi bán lẻ [[src-bcbs-lcr#^lcr40-24]]. Tiền gửi có kỳ hạn của SME xử lý như tiền gửi có kỳ hạn bán lẻ [[src-bcbs-lcr#^lcr40-25]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Các doanh nghiệp siêu nhỏ và hộ kinh doanh không có phòng Treasury chuyên nghiệp; dòng tiền của họ gắn liền với vòng quay vốn lưu động buôn bán nhỏ lẻ, có độ phân tán cao và hành vi rút vốn mang tính ổn định tương đồng với khách hàng cá nhân.

##### 1.6. Tiền gửi cầm cố & Kim loại quý (Pledged deposits & Precious metals — FAQ LCR40.5)
- *Tiền gửi cầm cố (Pledged deposits)*: chỉ được loại khỏi dòng ra khi đủ ba điều kiện: khoản vay không đáo hạn trong 30 ngày; hợp đồng cầm cố có hiệu lực pháp lý cấm rút trước khi khoản vay tất toán; số loại trừ không vượt dư nợ (phần đã giải ngân). Tiền gửi cầm cố cho hạn mức chưa giải ngân thì áp tỷ lệ dòng ra cao hơn giữa hạn mức và tiền gửi [[src-bcbs-lcr#^lcr40-5-faq1]]. TT50 không tính vào dòng ra nguồn vốn mà khách hàng không có quyền rút trước hạn trong hơn 30 ngày, kể cả khi tài sản tài chính của khách hàng đang bị ràng buộc [[src-tt50-2026-nhnn#^pl1-b1-4a]].
- *Tiền gửi kim loại quý (Precious metals)*: mặc định xử lý như tiền gửi bán lẻ hoặc vốn bán buôn không bảo đảm tuỳ loại đối tác. Jurisdiction **có thể** cho phép giả định không có dòng ra nếu tiền gửi thanh toán bằng hiện vật và ngân hàng tự cung ứng được từ kho của mình, hoặc hợp đồng cho ngân hàng quyền chọn hình thức thanh toán [[src-bcbs-lcr#^lcr40-5-faq2]]. TT50: [cần nguồn].

---

#### Trụ cột 2: Nguồn vốn Bán buôn Không Bảo đảm (Unsecured Wholesale Funding - LCR40.19 – 40.44)
Quy định chi tiết cơ chế phân loại tại [[unsecured-wholesale-funding]] và [[operational-deposits]]:

##### 2.1. Tiền gửi vận hành (Operational Deposits — 25% / 5% nếu có BHTG)
- **Phạm vi và Điều kiện quy chuẩn**: Áp dụng hệ số 25% cho các khoản tiền gửi phát sinh trực tiếp từ việc cung cấp dịch vụ bù trừ (*clearing* - LCR40.33), lưu ký chứng khoán (*custody* - LCR40.34) và quản lý dòng tiền (*cash management* - LCR40.35) [[src-bcbs-lcr#^lcr40-26]].
- **Điều kiện ràng buộc**: Khách hàng phải có sự phụ thuộc thực chất (*substantive dependency*); hợp đồng phải có điều khoản yêu cầu thời hạn thông báo hủy $\ge 30$ ngày hoặc việc hủy hợp đồng khiến khách hàng phải chịu chi phí chuyển đổi (*switching costs*) rất lớn [[src-bcbs-lcr#^lcr40-27]]. Tiền gửi phải nằm trong tài khoản chuyên biệt, không được định giá lãi suất cao nhằm mục đích khuyến khích tích lũy số dư đầu cơ [[src-bcbs-lcr#^lcr40-28]].
- **Bóc tách số dư thặng dư (Excess Balance)**: Phần số dư vượt quá nhu cầu vận hành thực tế không được hưởng hệ số 25% mà phải chuyển sang nhóm non-operational (run-off 40% hoặc 100%) [[src-bcbs-lcr#^lcr40-29]]. Nếu ngân hàng không xây dựng được phương pháp định lượng excess balance được supervisor chấp thuận, toàn bộ khoản tiền gửi bắt buộc bị coi là non-operational [[src-bcbs-lcr#^lcr40-29]] [[src-bcbs-lcr#^lcr40-30]].
- **Loại trừ tuyệt đối**: Dịch vụ tài khoản ngân hàng đại lý (*correspondent banking*) và môi giới khách hàng tổ chức (*prime brokerage*) bị cấm áp dụng tỷ lệ operational, phải chịu run-off 100% [[src-bcbs-lcr#^lcr40-32]].
- **Quy tắc đối ứng**: Phần số dư operational được BHTG bảo hiểm toàn bộ được hưởng run-off 5% [[src-bcbs-lcr#^lcr40-36]]. Phía bên gửi tiền bắt buộc phải ghi nhận dòng vào (inflow) 0% để đảm bảo tính cân đối hệ thống [[src-bcbs-lcr#^lcr40-31]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Tiền gửi vận hành là mạch máu nuôi dưỡng hoạt động giao dịch hàng ngày của doanh nghiệp. Để chuyển tài khoản chi trả lương cho hàng chục ngàn công nhân hay chuyển hệ thống bù trừ thanh toán sang ngân hàng khác, doanh nghiệp phải mất nhiều tháng chuẩn bị kỹ thuật và pháp lý. Do đó, dòng tiền này bị "khóa cứng" trong ngắn hạn. Ngược lại, phần thặng dư (*excess balance*) thực chất là tiền nhàn rỗi đầu tư ngắn hạn, rất dễ tháo chạy nên bị loại trừ. Dịch vụ correspondent banking và prime brokerage là các hoạt động thanh khoản bán buôn liên ngân hàng nhạy cảm cao độ, không có tính gắn kết vận hành bền vững nên phải áp run-off 100%.

##### 2.2. Tiền gửi trong mạng lưới ngân hàng hợp tác xã (Institutional networks of cooperative banks — 25%)
- **Phạm vi và Điều kiện quy chuẩn**: Tiền gửi của các ngân hàng thành viên tại định chế trung ương của mạng lưới nhằm đáp ứng dự trữ pháp định tối thiểu hoặc chia sẻ nhiệm vụ chung theo quy chế pháp lý, với điều kiện mạng lưới có cơ chế bảo vệ tương hỗ chống mất khả năng thanh khoản và thanh toán [[src-bcbs-lcr#^lcr40-37]]. Bên gửi tiền ghi nhận inflow 0% [[src-bcbs-lcr#^lcr40-38]]. Hoạt động correspondent banking bị loại trừ và phải chịu run-off 100% [[src-bcbs-lcr#^lcr40-39]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Bảo vệ mô hình liên kết tín dụng hợp tác xã (như hệ thống Raiffeisen/Volksbanken tại Đức hay Credit Agricole tại Pháp). Sự gắn kết về mặt thể chế và quỹ tương hỗ đảm bảo các ngân hàng thành viên không rút vốn khỏi ngân hàng mẹ trung ương khi có khủng hoảng.

##### 2.3. Tiền gửi của Doanh nghiệp phi tài chính, Sovereign, NHTW, PSE, MDB (40% / 20%)
- **Phạm vi và Điều kiện quy chuẩn**: Tiền gửi không có quan hệ vận hành (non-operational) từ doanh nghiệp sản xuất, thương mại phi tài chính, chính phủ, NHTW, ngân hàng phát triển đa phương (MDB) và tổ chức công quyền (PSE) chịu run-off 40% [[src-bcbs-lcr#^lcr40-40]]. Run-off giảm xuống 20% nếu toàn bộ số dư được BHTG hoặc chính phủ bảo lãnh toàn bộ [[src-bcbs-lcr#^lcr40-41]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Giám đốc tài chính (CFO) của các doanh nghiệp lớn có trách nhiệm bảo toàn thanh khoản doanh nghiệp; khi ngân hàng đối tác gặp trục trặc, họ sẽ rút các khoản tiền gửi ngắn hạn để chuyển sang ngân hàng an toàn hơn (*flight-to-quality*). Tuy nhiên, doanh nghiệp phi tài chính vẫn phải duy trì các khoản tiền thanh toán chi phí nguyên vật liệu, thuế và vận hành chuỗi cung ứng, nên tỷ lệ rút vốn dừng ở mức 40% thay vì rút sạch 100%.

##### 2.4. Tiền gửi của Tổ chức tài chính và Pháp nhân khác (100%)
- **Phạm vi và Điều kiện quy chuẩn**: Toàn bộ tiền gửi không bảo đảm và phơi nhiễm nợ ngắn hạn đáo hạn $\le 30$ ngày từ các ngân hàng thương mại, công ty chứng khoán, bảo hiểm, quỹ đầu tư, quỹ tín thác (*fiduciaries*), công ty liên kết và các thực thể SPV/conduit chịu run-off tuyệt đối 100% [[src-bcbs-lcr#^lcr40-42]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Các định chế tài chính là nhóm chủ nợ am hiểu thị trường nhất, sử dụng hệ thống tự động để giám sát tín dụng liên ngân hàng. Họ là những bên rút vốn đầu tiên (*first-mover advantage*) vì không muốn chịu rủi ro vỡ nợ của đối tác. Thị trường vay mượn tín chấp giữa các tổ chức tài chính lập tức đóng băng hoàn toàn khi khủng hoảng nổ ra.

##### 2.5. Giấy tờ có giá do ngân hàng tự phát hành đáo hạn $\le 30$ ngày (100%)
- **Phạm vi và Điều kiện quy chuẩn**: Mọi trái phiếu, kỳ phiếu, chứng chỉ tiền gửi do ngân hàng phát hành có kỳ hạn đáo hạn trong vòng 30 ngày chịu run-off 100%, trừ khi chứng minh được chỉ bán trên thị trường bán lẻ và nằm trong tài khoản bán lẻ [[src-bcbs-lcr#^lcr40-43]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Khác với tiền gửi quan hệ, giấy tờ nợ bán buôn lưu hành trên thị trường thứ cấp hoàn toàn vô danh và mang tính giao dịch thuần túy. Khi đáo hạn, ngân hàng không thể phát hành giấy tờ mới để đảo nợ (*refinancing market closure*), buộc phải chi trả toàn bộ 100% bằng tiền mặt.

---

#### Trụ cột 3: Nguồn vốn Có Bảo đảm (Secured Funding - LCR40.45 – 40.48)
Quy định chi tiết cơ chế phân loại tại [[secured-funding]]:

##### 3.1. Bản chất và Nguyên lý Chiết khấu Chất lượng Tài sản (Collateral Quality Trumps Counterparty Credit)
- **Bản chất**: Nguồn vốn có bảo đảm là các khoản nợ được bảo đảm bằng quyền pháp lý cụ thể đối với tài sản của ngân hàng đi vay khi phá sản [[src-bcbs-lcr#^lcr40-45]]. Trong kịch bản stress, khả năng gia hạn (*rollover*) các hợp đồng repo, reverse repo, hoán đổi tài sản bảo đảm (*collateral swaps*) và cho mượn chứng khoán để khách hàng bán khống (*customer short positions*) phụ thuộc hoàn toàn vào phẩm cấp của tài sản bảo đảm, không phụ thuộc vào uy tín tín nhiệm của bên vay [[src-bcbs-lcr#^lcr40-46]].
- **Thang bậc dòng ra theo tài sản bảo đảm (LCR40.48)**:
  - *Bảo đảm bằng Level 1 hoặc giao dịch với NHTW trong nước (Dòng ra 0%)* [[src-bcbs-lcr#^lcr40-47]] [[src-bcbs-lcr#^lcr40-48]]: Trái phiếu chính phủ tối cao và các giao dịch với NHTW duy trì thanh khoản tuyệt đối; bên cho vay sẵn sàng rollover 100% giao dịch repo.
  - *Bảo đảm bằng Level 2A (Dòng ra 15%)* [[src-bcbs-lcr#^lcr40-48]]: Phản ánh mức haircut chuẩn mực 15% của tài sản Level 2A; đối tác repo yêu cầu tăng mức ký quỹ hoặc giảm quy mô giải ngân tương ứng.
  - *Giao dịch với Sovereign, PSE trong nước (RW $\le 20\%$), MDB bằng tài sản ngoài L1/L2A (Dòng ra 25%)* [[src-bcbs-lcr#^lcr40-47]]: Cơ quan nhà nước không rút vốn ồ ạt vì mục tiêu ổn định kinh tế vĩ mô.
  - *Bảo đảm bằng Level 2B RMBS đủ điều kiện (Dòng ra 25%)* [[src-bcbs-lcr#^lcr40-48]]: Phản ánh mức chiết khấu định giá của chứng khoán hóa nợ mua nhà chất lượng cao.
  - *Bảo đảm bằng Level 2B khác (Dòng ra 50%)* [[src-bcbs-lcr#^lcr40-48]]: Trái phiếu doanh nghiệp BBB- và cổ phiếu thuộc rổ chỉ số lớn chịu mức sụt giá sâu khi thị trường hoảng loạn.
  - *Bảo đảm bằng Non-HQLA (Dòng ra 100%)* [[src-bcbs-lcr#^lcr40-48]]: Thị trường repo đối với các tài sản rủi ro (trái phiếu lợi suất cao, cổ phiếu rác, khoản vay tín chấp) đóng băng hoàn toàn; đối tác từ chối gia hạn hợp đồng và yêu cầu hoàn trả 100% tiền mặt.
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Kịch bản LCR phản ánh chính xác cơ chế sụp đổ của các ngân hàng đầu tư năm 2008: tài trợ cho danh mục tài sản rủi ro phi HQLA bằng hợp đồng repo ngắn hạn qua đêm; khi thị trường tài sản rủi ro suy giảm, bên cho vay repo từ chối rollover hoặc nâng haircut lên 100%, gây ra cuộc khủng hoảng thanh khoản tức thì.

##### 3.2. Quy tắc Phân bổ Thác Tài sản Hỗn hợp (Collateral Pool Waterfall Principle)
- **Quy chuẩn Basel**: LCR40.48 không nêu quy tắc phân bổ tài sản bảo đảm hỗn hợp cho từng giao dịch nguồn vốn có bảo đảm [cần nguồn]. Quy tắc gần nhất là chú thích 3 LCR30.16: pool tài sản cầm cố không chỉ định chứng khoán cụ thể thì ngân hàng có thể giả định tài sản bị ràng buộc theo thứ tự thanh khoản tăng dần (non-HQLA trước, rồi Level 2B, 2A, cuối cùng Level 1) khi xác định phần còn lại tính vào HQLA [[src-bcbs-lcr#^lcr30-16b]].
- **TT50**: tài sản có hệ số rút tiền cao nhất được sử dụng trước cho giao dịch ngắn nhất [[src-tt50-2026-nhnn#^pl1-b3-3]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Nguyên tắc này ép các khoản nợ đáo hạn trong 30 ngày phải gánh các tài sản bảo đảm có phẩm cấp thấp hơn (hoặc non-HQLA), dẫn đến tỷ lệ dòng ra tính toán cao hơn, bảo đảm tính thận trọng tối đa trong quản trị rủi ro.

---

#### Trụ cột 4: Phái sinh và Nhu cầu Bổ sung (LCR40.49 – 40.58)
Quy định chi tiết cơ chế phân loại tại [[derivatives-and-contingent-outflows]]:

##### 4.1. Dòng tiền ra phái sinh ròng (Net derivative cash outflows — 100%)
- **Phạm vi và Quy chuẩn**: Tính bù trừ dòng tiền thu và chi theo từng đối tác nếu có thỏa thuận bù trừ song phương (*master netting agreement*) có hiệu lực pháp lý; mọi quyền chọn đáo hạn $\le 30$ ngày (kể cả quyền chọn kiểu Mỹ đáo hạn sau 30 ngày) mà đối tác đang có lãi (*in the money*) đều bắt buộc giả định bị thực hiện [[src-bcbs-lcr#^lcr40-49]]. Dòng ra được tính ròng với HQLA nhận về nếu ngân hàng có quyền pháp lý và năng lực vận hành tái sử dụng tài sản đó [[src-bcbs-lcr#^lcr40-50]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Giao dịch phái sinh có độ đòn bẩy cao; khi giá thị trường biến động bất lợi, các khoản thanh toán bù trừ hoặc đóng vị thế lỗ đòi hỏi ngân hàng phải chi trả ngay lập tức bằng tiền mặt mà không có độ trễ thương lượng.

##### 4.2. Kích hoạt hạ bậc tín nhiệm (Downgrade Triggers — 100%)
- **Phạm vi và Quy chuẩn**: Ngân hàng phải tính toán toàn bộ lượng tiền mặt hoặc tài sản bảo đảm bổ sung mà ngân hàng bắt buộc phải nộp theo hợp đồng khi bị các tổ chức xếp hạng tín nhiệm quốc tế hạ bậc tín nhiệm dài hạn tới **3 bậc** (up to and including a 3-notch downgrade) [[src-bcbs-lcr#^lcr40-51]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Phòng ngừa hiện tượng "vách đá thanh khoản" (*liquidity cliff*). Nhiều ngân hàng phá sản không phải do mất vốn điều lệ mà do các điều khoản kích hoạt hạ bậc tín nhiệm trong phụ lục bảo đảm tín dụng (CSA) buộc ngân hàng phải nộp thêm hàng tỷ USD ký quỹ trong vòng 24–48 giờ, làm cạn kiệt thanh khoản tức thì.

##### 4.3. Phạt ký quỹ bằng tài sản không phải Cấp 1 (Non-Level 1 posted collateral — +20%)
- **Phạm vi và Quy chuẩn**: Trường hợp ngân hàng đã ký quỹ tài sản Level 2 hoặc Non-HQLA cho đối tác, ngân hàng phải tính thêm một khoản phạt bằng **20%** giá trị thị trường của các tài sản đó vào HQLA yêu cầu [[src-bcbs-lcr#^lcr40-52]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Bù đắp rủi ro tài sản ký quỹ bị sụt giá hoặc bị đối tác tăng tỷ lệ chiết khấu haircut trong thời kỳ khủng hoảng, buộc ngân hàng phải bổ sung thêm tài sản ký quỹ mới.

##### 4.4. Tài sản bảo đảm thặng dư không tách biệt (Excess non-segregated collateral — 100%)
- **Phạm vi và Quy chuẩn**: Tính 100% dòng ra đối với phần TSBĐ mà đối tác đã nộp thừa cho ngân hàng mà đối tác có quyền rút về theo hợp đồng bất kỳ lúc nào [[src-bcbs-lcr#^lcr40-53]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Trong thời kỳ bình thường, đối tác để tài sản thừa lại ngân hàng vì chi phí giao dịch; nhưng khi ngân hàng gặp nguy cơ rủi ro, đối tác sẽ rà soát và rút toàn bộ phần tài sản thừa về két của họ để tự vệ.

##### 4.5. Tài sản bảo đảm theo hợp đồng chưa bị đòi (Contractually required uncalled collateral — 100%)
- **Phạm vi và Quy chuẩn**: Tính 100% dòng ra đối với tài sản bảo đảm mà theo điều khoản hợp đồng ngân hàng có nghĩa vụ phải nộp nhưng đối tác chưa phát lệnh đòi nộp (*uncalled margin calls*) [[src-bcbs-lcr#^lcr40-54]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Độ trễ vận hành tạm thời của đối tác sẽ biến mất ngay khi ngân hàng có tin đồn tiêu cực; đối tác sẽ phát lệnh margin call ngay lập tức.

##### 4.6. Rủi ro thay thế tài sản bảo đảm (Collateral Substitution Risk — 100% hoặc chênh lệch haircut)
- **Phạm vi và Quy chuẩn**: Nếu hợp đồng cho phép đối tác thay thế TSBĐ mà không cần ngân hàng đồng ý, ngân hàng phải tính 100% dòng ra đối với phần HQLA có thể bị thay bằng tài sản non-HQLA; hoặc tính dòng ra bằng chênh lệch haircut nếu thay bằng HQLA có bậc thanh khoản thấp hơn [[src-bcbs-lcr#^lcr40-55]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Trong khủng hoảng, đối tác sẽ hành động theo lợi ích của họ: rút tài sản có tính thanh khoản cao nhất (như TPCP Level 1) về và nộp thay bằng các tài sản kém thanh khoản hơn, làm hao hụt trực tiếp kho HQLA của ngân hàng.

##### 4.7. Biến động định giá thị trường phái sinh (Market Valuation Changes — 24-month Look-back Approach)
- **Phạm vi và Quy chuẩn**: Dòng ra phát sinh từ biến động giá trị thị trường của danh mục phái sinh được tính bằng dòng ký quỹ ròng 30 ngày lớn nhất trong vòng **24 tháng** gần nhất [[src-bcbs-lcr#^lcr40-56]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Phương pháp hồi quy lịch sử 24 tháng (*look-back approach*) loại bỏ các giả định mô hình hóa chủ quan, định lượng quy mô dòng tiền ký quỹ đỉnh điểm mà ngân hàng từng phải chi trả trên thực tế khi thị trường biến động dữ dội.

##### 4.8. Công cụ nợ cấu trúc tự phát hành & ABCP Conduits/SIVs (100%)
- **Phạm vi và Quy chuẩn**: Trái phiếu có bảo đảm (covered bonds) và ABS do chính ngân hàng phát hành đáo hạn $\le 30$ ngày chịu dòng ra 100% [[src-bcbs-lcr#^lcr40-57]]. Mất nguồn vốn từ ABCP, conduits, SIV: tính 100% công cụ nợ ngắn hạn đáo hạn và 100% tài sản có thể bị trả lại qua quyền chọn bán thanh khoản (*liquidity puts*) [[src-bcbs-lcr#^lcr40-58]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Ngăn chặn rủi ro từ hệ thống ngân hàng bóng đêm (*shadow banking*). Trong cuộc khủng hoảng tài chính toàn cầu, khi thị trường thương phiếu ABCP đóng băng, các cấu trúc ngoại bảng đổ vỡ và ngân hàng tài trợ buộc phải đưa toàn bộ tài sản và nợ về lại bảng cân đối để bảo toàn uy tín thương hiệu.

---

#### Trụ cột 5: Hạn mức Cam kết và Nghĩa vụ Tiềm tàng (LCR40.59 – 40.74)
Quy định chi tiết cơ chế phân loại tại [[committed-facilities]]:

##### 5.1. Phân biệt bản chất: Credit Facility vs Liquidity Facility (LCR40.61)
- **Credit Facility (Hạn mức Tín dụng)**: Hạn mức cam kết nhằm tài trợ nhu cầu kinh doanh và vốn lưu động thông thường của khách hàng (ví dụ: hạn mức thấu chi, cho vay xoay vòng) [[src-bcbs-lcr#^lcr40-61]].
- **Liquidity Facility (Hạn mức Thanh khoản)**: Hạn mức cam kết đặc biệt, đóng vai trò bảo đảm hỗ trợ tái tài trợ khi khách hàng không thể đảo nợ trên thị trường tài chính (ví dụ: bảo đảm cho chương trình thương phiếu doanh nghiệp CP) [[src-bcbs-lcr#^lcr40-61]].
- **Quy tắc xếp loại SPE/Quỹ**: Mọi hạn mức cấp cho hedge funds, MMFs, SPEs, conduits bắt buộc phải phân loại là liquidity facility và chịu tỷ lệ rút vốn 100% [[src-bcbs-lcr#^lcr40-62]].
- **Giả định dư nợ không hoàn trả**: Toàn bộ số tiền đã giả định rút ra được coi là dư nợ duy trì liên tục và không được hoàn trả trong 30 ngày, bất kể kỳ hạn hợp đồng [[src-bcbs-lcr#^lcr40-59]]. Cho phép trừ ròng với HQLA hợp lệ đã đặt cọc nếu ngân hàng có quyền tái sử dụng hợp pháp [[src-bcbs-lcr#^lcr40-60]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Hạn mức thanh khoản có xác suất rút vốn cao hơn nhiều so với hạn mức tín dụng; khi thị trường nợ đóng băng, bên phát hành nợ bắt buộc phải kích hoạt 100% hạn mức thanh khoản để trả nợ cho các trái chủ nhằm tránh vỡ nợ kỹ thuật.

##### 5.2. Ma trận Tỷ lệ Rút vốn Hạn mức Chưa giải ngân (Drawdown Rates — LCR40.64)
- *Bán lẻ & SME cá nhân: 5% (cả Credit và Liquidity)* [[src-bcbs-lcr#^lcr40-64]]: Người tiêu dùng và hộ kinh doanh rút hạn mức thẻ tín dụng hoặc thấu chi ở mức vừa phải để chi tiêu thiết yếu.
- *Doanh nghiệp phi tài chính, Sovereign, NHTW, PSE, MDB*:
  - Credit Facility: **10%** [[src-bcbs-lcr#^lcr40-64]]. Doanh nghiệp rút một phần hạn mức để tăng dự trữ tiền mặt phòng thủ (*precautionary cash hoarding*).
  - Liquidity Facility: **30%** [[src-bcbs-lcr#^lcr40-64]]. Dự kiến khoảng 30% doanh nghiệp gặp khó khăn khi phát hành thương phiếu mới và phải kích hoạt hạn mức thanh khoản backstop từ ngân hàng.
- *Ngân hàng thương mại chịu giám sát: 40% (cả Credit và Liquidity)* [[src-bcbs-lcr#^lcr40-64]]: Các ngân hàng đối tác gặp khó khăn thanh khoản liên ngân hàng sẽ chủ động rút hạn mức cam kết lẫn nhau.
- *Định chế tài chính khác (công ty chứng khoán, bảo hiểm, quỹ): Credit 40% / Liquidity 100%* [[src-bcbs-lcr#^lcr40-64]]: Các công ty chứng khoán và quỹ không có cửa sổ tái cấp vốn trực tiếp từ NHTW; khi thị trường repo đóng băng, họ sẽ rút cạn kiệt 100% hạn mức thanh khoản ngân hàng đã cam kết.
- *Pháp nhân cấu trúc (SPEs, Conduits, SPVs, Hedge funds): 100% (cả Credit và Liquidity)* [[src-bcbs-lcr#^lcr40-62]] [[src-bcbs-lcr#^lcr40-64]]: Các thực thể đòn bẩy tài chính cấu trúc này không có nguồn thu ổn định và sẽ rút sạch toàn bộ hạn mức khi thị trường biến động.

##### 5.3. Nghĩa vụ cấp vốn hợp đồng khác (Contractual Lending Obligations — LCR40.65, 40.66)
- *Tổ chức tài chính & NHTW*: Mọi nghĩa vụ theo hợp đồng cấp vốn cho các định chế tài chính và NHTW trong 30 ngày chưa phản ánh ở nơi khác phải tính dòng ra **100%** [[src-bcbs-lcr#^lcr40-65]].
- *Khách bán lẻ và Doanh nghiệp phi tài chính*: Phần cam kết cấp vốn theo hợp đồng vượt quá 50% tổng dòng vào hợp đồng từ chính nhóm khách hàng đó phải tính dòng ra **100%** [[src-bcbs-lcr#^lcr40-66]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Ngân hàng không thể đơn phương hủy bỏ các hợp đồng cấp vốn đã ký kết với các định chế tài chính khác mà không bị kiện ra tòa hoặc hủy hoại uy tín thanh toán trên thị trường.

##### 5.4. Nghĩa vụ tài trợ tiềm tàng phi hợp đồng và Rủi ro Uy tín (Reputational Triggers — LCR40.68 – 40.70)
- **Phạm vi và Quy chuẩn**: Áp dụng cho các nghĩa vụ tiềm tàng phi hợp đồng phát sinh từ việc ngân hàng liên kết tên tuổi hoặc bảo trợ cho các sản phẩm đầu tư, quỹ thị trường tiền tệ (MMFs), hoặc liên doanh không hợp nhất [[src-bcbs-lcr#^lcr40-68]] [[src-bcbs-lcr#^lcr40-70]]. Một số nghĩa vụ phụ thuộc vào sự kiện tín dụng hoặc thị trường (ví dụ chứng chỉ cấu trúc autocallable note) [[src-bcbs-lcr#^lcr40-69]]. Tỷ lệ rút vốn do supervisor quốc gia quy định [[src-bcbs-lcr#^lcr40-67]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Dù không có ràng buộc pháp lý bằng hợp đồng, ngân hàng thường phải tự nguyện can thiệp bơm vốn (*step-in support*) để cứu các sản phẩm đầu tư mang thương hiệu của mình nhằm bảo vệ uy tín. Nếu ngân hàng để mặc cho các quỹ đầu tư liên kết sụp đổ, người gửi tiền sẽ mất niềm tin và làn sóng tháo chạy sẽ lan sang chính ngân hàng mẹ.

##### 5.5. Tài trợ thương mại (Trade Finance — LCR40.71) & Bảo lãnh hợp đồng
- **Phạm vi và Quy chuẩn**: Các nghĩa vụ tiềm tàng phát sinh từ công cụ tài trợ thương mại (như L/C thư tín dụng chứng từ, bảo lãnh nhận hàng) áp dụng tỷ lệ rút vốn tương đối thấp ($\le 5\%$, do cơ quan quản lý quốc gia ấn định) [[src-bcbs-lcr#^lcr40-71]]. Công cụ tài trợ thương mại gồm thư tín dụng chứng từ thương mại, nhờ thu kèm chứng từ và nhờ thu trơn, hối phiếu nhập khẩu, xuất khẩu, và bảo lãnh gắn trực tiếp với tài trợ thương mại như bảo lãnh nhận hàng [[src-bcbs-lcr#^lcr40-71b]]. Cam kết cho vay xuất nhập khẩu trực tiếp cho doanh nghiệp phi tài chính không thuộc nhóm này, áp tỷ lệ rút của LCR40.64 [[src-bcbs-lcr#^lcr40-72]]. Danh mục nghĩa vụ tiềm tàng khác gồm hạn mức hủy ngang vô điều kiện, bảo lãnh dự thầu, vị thế bán khống bù trừ nội bộ bằng tài sản khách hàng khác (run-off tối thiểu 50%) [[src-bcbs-lcr#^lcr40-73]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* L/C và bảo lãnh thương mại gắn liền với dòng lưu chuyển hàng hóa thực tế và có bộ chứng từ đối ứng chặt chẽ. Khách hàng chỉ yêu cầu ngân hàng thanh toán khi có sự vi phạm hợp đồng hoặc đối tác giao hàng thực tế, xác suất phát sinh nghĩa vụ bồi thường đồng loạt trong 30 ngày là rất thấp.

##### 5.6. Dòng tiền ra hợp đồng khác: 100% (LCR40.74)
- **Phạm vi và Quy chuẩn**: Mọi dòng tiền ra theo hợp đồng khác trong 30 ngày chịu hệ số 100%; dòng ra liên quan chi phí hoạt động không thuộc chuẩn mực này [[src-bcbs-lcr#^lcr40-74]].
- **FAQ LCR40.74**: giao dịch đã khớp chưa thanh toán gồm cả open và failed trades nếu dự kiến thanh toán trong 30 ngày. Tài sản Level 1, 2 cho mượn không bảo đảm và sẽ hoàn trả trong 30 ngày không tính vào HQLA của cả hai bên; bên đi mượn đã tái sử dụng tài sản thì có dòng ra hợp đồng khác [[src-bcbs-lcr#^lcr40-74-faq]].
- *Diễn giải — Ý nghĩa kinh tế & giám sát:* Đảm bảo tính bao quát tuyệt đối: mọi cam kết dòng tiền mặt rời khỏi ngân hàng đều phải được dự phòng bằng HQLA, không bỏ sót bất kỳ nghĩa vụ pháp lý nào.

---

### Khung Pháp lý Dòng tiền ra theo TT50/2026/TT-NHNN (Phần B Phụ lục I)

Dòng tiền ra LCR tại Việt Nam được quy định tại Đ21.2 và Phần B Phụ lục I TT50/2026 [[src-tt50-2026-nhnn#^d21-2]]. TT50 có hiệu lực từ 01/10/2026 [[src-tt50-2026-nhnn#^d37-1]]; LCR áp dụng từ 01/10/2028 theo lộ trình [[src-tt50-2026-nhnn#^d13-1]].

#### Danh mục dòng tiền ra theo Bảng 6 TT50

Bảng 6 phân mỗi đầu mục theo 4 khung thời gian đến hạn: Ngày tiếp theo; ngày 2–7; ngày 8–14; ngày 15–30. Giá trị theo mức độ rủi ro = tổng 4 khung × hệ số rút tiền [[src-tt50-2026-nhnn#^pl1-b7]].

| Mục Bảng 6 | Đầu mục | Hệ số rút tiền | Điều kiện chính | Nguồn |
|---|---|---|---|---|
| 1.1 | Tiền gửi bán lẻ ổn định | 5% | Được BHTG bảo hiểm hoàn toàn và khách hàng có nợ vay trung, dài hạn hoặc có tài khoản thanh toán phát sinh giao dịch trong 6 tháng | [[src-tt50-2026-nhnn#^pl1-b2-2]] |
| 1.2 | Tiền gửi bán lẻ kém ổn định | 10% | Không đủ điều kiện ổn định; gồm phần vượt giới hạn bảo hiểm và mọi tiền gửi ngoại tệ | [[src-tt50-2026-nhnn#^pl1-b2-3]] [[src-tt50-2026-nhnn#^pl1-b2-1]] [[src-tt50-2026-nhnn#^pl1-b2-2]] |
| 2.1.1 / 2.1.2 | Tiền gửi DNNVV đủ điều kiện ổn định / kém ổn định | 5% / 10% | Không phải tổ chức tài chính; là DNNVV theo luật; tiền gửi bình quân tháng liền kề tại ngân hàng ≤ 30 tỷ đồng | [[src-tt50-2026-nhnn#^pl1-b3-22]] |
| 2.2 | Tiền gửi hoạt động | 25% | Từ thanh toán bù trừ, lưu ký, quản lý tiền mặt; điều kiện tại III.2.3.b–c | [[src-tt50-2026-nhnn#^pl1-b3-23a]] [[src-tt50-2026-nhnn#^pl1-b3-23c]] [[src-tt50-2026-nhnn#^pl1-b3-23d]] |
| 2.3 | Nguồn vốn từ doanh nghiệp, Chính phủ, NHNN, NHTW, PSE nước ngoài, KBNN, UBND cấp tỉnh, ngân hàng chính sách, BHTG, BHXH, tổ chức tài chính quốc tế | 40% | Không gồm tiền gửi hoạt động; doanh nghiệp không phải DNNVV đủ điều kiện, không phải tổ chức tài chính | [[src-tt50-2026-nhnn#^pl1-b3-24]] |
| 2.4 | Nguồn vốn không có bảo đảm khác | 100% | Không thuộc 2.2–2.4 Mục III | [[src-tt50-2026-nhnn#^pl1-b3-25]] |
| 3.1 | Có bảo đảm bằng HQLA cấp 1 hoặc giao dịch với NHNN | 0% | | [[src-tt50-2026-nhnn#^pl1-b3-3]] |
| 3.2 | Có bảo đảm bằng HQLA cấp 2A | 15% | | [[src-tt50-2026-nhnn#^pl1-b3-3]] |
| 3.3 | Có bảo đảm bằng tài sản tài chính khác với Chính phủ, KBNN, UBND cấp tỉnh, ngân hàng chính sách, VAMC, DATC, BHTG, BHXH, tổ chức tài chính quốc tế | 25% | | [[src-tt50-2026-nhnn#^pl1-b3-3]] |
| 3.4 | Có bảo đảm bằng RMBS cấp 2B | 25% | | [[src-tt50-2026-nhnn#^pl1-b3-3]] |
| 3.5 | Có bảo đảm bằng HQLA cấp 2B khác | 50% | | [[src-tt50-2026-nhnn#^pl1-b3-3]] |
| 3.6 | Có bảo đảm bằng tài sản tài chính khác | 100% | | [[src-tt50-2026-nhnn#^pl1-b3-3]] |
| 4.1 | Thay đổi giá trị tài sản bảo đảm không phải HQLA cấp 1 | 20% | Tính trên giá trị danh nghĩa × hệ số thanh khoản (cấp 2 theo Phần A; tài sản khác 25%), sau khi trừ tài sản bảo đảm nhận được | [[src-tt50-2026-nhnn#^pl1-b4-22]] |
| 4.2 | Hạ bậc xếp hạng tín nhiệm | 100% | Hạ tối đa 3 bậc, kể cả ngân hàng mẹ của chi nhánh NHNNg | [[src-tt50-2026-nhnn#^pl1-b4-21]] |
| 4.3 / 4.4 | Tài sản bảo đảm dư thừa đối tác có quyền thu hồi / ký quỹ chưa bị yêu cầu | 100% | | [[src-tt50-2026-nhnn#^pl1-b4-23]] |
| 4.5 | Thay đổi định giá thị trường | 100% | Có bù trừ: dòng ký quỹ ròng 30 ngày lớn nhất trong 24 tháng, ở cấp độ danh mục | [[src-tt50-2026-nhnn#^pl1-b4-25]] |
| 5.1.1 | Hạn mức cam kết: bán lẻ, DNNVV | 5% | Không thể huỷ ngang hoặc huỷ ngang có điều kiện | [[src-tt50-2026-nhnn#^pl1-b5]] [[src-tt50-2026-nhnn#^pl1-b5-1]] |
| 5.1.2 | Hạn mức cam kết: doanh nghiệp không phải tổ chức tài chính | 10% tín dụng / 30% thanh khoản | | [[src-tt50-2026-nhnn#^pl1-b5]] |
| 5.1.3 | Hạn mức cam kết: Chính phủ, NHTW, PSE, KBNN, UBND cấp tỉnh, BHTG, tổ chức tài chính quốc tế | 10% / 30% (Bảng 5; ô Bảng 6 để trống) | | [[src-tt50-2026-nhnn#^pl1-b5]] [[src-tt50-2026-nhnn#^pl1-b7]] |
| 5.1.4 | Hạn mức cam kết: TCTD, chi nhánh NHNNg | 40% | | [[src-tt50-2026-nhnn#^pl1-b5]] |
| 5.1.5 | Hạn mức cam kết: tổ chức tài chính khác (công ty chứng khoán, bảo hiểm, quản lý quỹ) | 40% tín dụng / 100% thanh khoản | | [[src-tt50-2026-nhnn#^pl1-b5]] [[src-tt50-2026-nhnn#^pl1-b7]] |
| 5.1.6 | Hạn mức cam kết: đối tượng khác | 100% | | [[src-tt50-2026-nhnn#^pl1-b5]] |
| 5.2.1 | Nghĩa vụ giải ngân trong 30 ngày cho tổ chức tài chính, kể cả NHNN | 100% | | [[src-tt50-2026-nhnn#^pl1-b5-2]] |
| 5.2.2 | Nghĩa vụ giải ngân trong 30 ngày cho cá nhân, tổ chức khác | 100% phần vượt | Chỉ phần chênh lệch dương khi tổng nghĩa vụ vượt 50% dòng tiền vào 30 ngày từ các nhóm này | [[src-tt50-2026-nhnn#^pl1-b5-2]] |
| 5.3.1 | Nghĩa vụ tiềm ẩn theo hợp đồng | 0% / 3% / 5% | 0%: hạn mức huỷ ngang vô điều kiện, cam kết cung cấp cam kết ngoại bảng khác; 3%: tài trợ thương mại; 5%: bảo lãnh ngân hàng, dự thầu, thực hiện hợp đồng, autocallable notes | [[src-tt50-2026-nhnn#^pl1-b5-31]] |
| 5.3.2 / 5.3.3 | Nghĩa vụ tiềm ẩn phi hợp đồng / cam kết ngoại bảng khác | Ngân hàng xác định | Dựa trên dữ liệu lịch sử | [[src-tt50-2026-nhnn#^pl1-b5-31]] |
| 5.3.4 | Nghĩa vụ tiềm ẩn đã bị kích hoạt, phải thanh toán trong 30 ngày | 100% | | [[src-tt50-2026-nhnn#^pl1-b5-31]] |
| 6 | Dòng tiền ra ròng từ phái sinh | 100% | Bù trừ theo đối tác khi có thỏa thuận bù trừ đủ điều kiện | [[src-tt50-2026-nhnn#^pl1-b4-1]] |
| 7 | Dòng tiền ra theo thỏa thuận khác | 100% | Mọi nghĩa vụ trong 30 ngày không thuộc Mục II–V | [[src-tt50-2026-nhnn#^pl1-b6]] |

#### 1. Nguyên tắc thời hạn (Mục I Phần B)
- Tổng dòng tiền ra là tổng dòng tiền từ nghĩa vụ đến hạn, nghĩa vụ thực hiện cam kết hoặc dự kiến phát sinh trong 30 ngày tiếp theo; nghĩa vụ quá hạn (kể cả lãi, lãi quá hạn, lãi phạt) tính vào Ngày tiếp theo [[src-tt50-2026-nhnn#^pl1-b1-1]]. Nghĩa vụ không xác định được thời hạn cũng tính vào Ngày tiếp theo [[src-tt50-2026-nhnn#^pl1-b1]].
- Nguồn vốn kỳ hạn còn lại trên 30 ngày **không** tính vào dòng tiền ra khi [[src-tt50-2026-nhnn#^pl1-b1-4a]]:
  1. khách hàng không có quyền rút trước hạn trong hơn 30 ngày, kể cả khi tài sản tài chính của khách hàng bị ràng buộc;
  2. khách hàng có quyền rút nhưng phải báo trước hơn 30 ngày và chưa báo, hoặc ngày rút dự kiến còn hơn 30 ngày;
  3. tiền gửi bán lẻ VNĐ (kể cả tiền gửi bán buôn xác định như bán lẻ) rút trước hạn chỉ được lãi tối đa bằng lãi suất không kỳ hạn VNĐ thấp nhất và không hưởng lợi ích khác;
  4. nguồn vốn bán buôn có quyền rút khi ngân hàng vi phạm nghĩa vụ nhưng khách hàng chưa thông báo rút.
- Nguồn vốn kỳ hạn còn lại trên 30 ngày **phải** tính khi: khách hàng có quyền rút trong 30 ngày; không đủ thông tin để phân loại vào các trường hợp trên; ngân hàng đã thông báo mua lại, thanh toán trước hạn trong 30 ngày; ngân hàng vi phạm thanh toán sớm theo kết luận thanh tra (tính toàn bộ vào Ngày tiếp theo) [[src-tt50-2026-nhnn#^pl1-b1-4b]].
- *Diễn giải:* điều kiện 3 thay cho tiêu chí phạt rút trước hạn của Basel LCR40.16; mức phạt TT50 dùng là mất phần chênh lệch so với lãi suất không kỳ hạn VNĐ thấp nhất.

#### 2. Tiền gửi bán lẻ và DNNVV (Mục II, khoản 2.2 Mục III)
- Khách hàng bán lẻ là cá nhân, tổ hợp tác, hộ kinh doanh, không gồm doanh nghiệp tư nhân và tổ chức không có tư cách pháp nhân; tiền gửi bán lẻ ngoại tệ là kém ổn định [[src-tt50-2026-nhnn#^pl1-b2-1]].
- "Bảo hiểm hoàn toàn" là 100% số tiền thuộc giới hạn bảo hiểm tiền gửi; phần vượt giới hạn là kém ổn định [[src-tt50-2026-nhnn#^pl1-b2-2]]. TT50 không nêu con số giới hạn bảo hiểm [cần nguồn: văn bản về hạn mức chi trả bảo hiểm tiền gửi].
- Khi kiểm tra sức chịu đựng, ngân hàng phải chia tiền gửi kém ổn định thành nhóm rủi ro tương đồng với hệ số khác nhau theo quy định nội bộ [[src-tt50-2026-nhnn#^pl1-b2-3]].
- DNNVV: số dư bình quân là tổng số dư cuối mỗi ngày của tháng liền kề chia số ngày; không có thông tin xác định DNNVV thì không được phân loại vào DNNVV [[src-tt50-2026-nhnn#^pl1-b3-22]].

#### 3. Nguồn vốn bán buôn không có bảo đảm (khoản 2 Mục III)
- Nguồn vốn bán buôn là nợ phải trả huy động từ pháp nhân, doanh nghiệp tư nhân, công ty hợp danh, tổ chức không có tư cách pháp nhân và nguồn không phải tiền gửi bán lẻ; nghĩa vụ phái sinh không thuộc nhóm không có bảo đảm [[src-tt50-2026-nhnn#^pl1-b3-1]].
- **Tiền gửi hoạt động (25%)** [[src-tt50-2026-nhnn#^pl1-b3-23a]]:
  - ngân hàng có thể áp hệ số trên 25% khi tiền gửi tập trung vào ít khách hàng;
  - phần được bảo hiểm hoàn toàn áp hệ số như bán lẻ ổn định;
  - tiền ngân hàng đặt tại ngân hàng khác cho các hoạt động này có hệ số thu tiền 0%.
- Phạm vi hoạt động được liệt kê: thanh toán bù trừ (truyền tải, đối soát lệnh; thấu chi trong ngày, tài trợ qua đêm; xác định vị thế), lưu ký (thanh toán chứng khoán, xử lý tài sản bảo đảm, nhận cổ tức…), quản lý tiền mặt (chuyển tiền, tổng hợp quỹ, bảng lương, kiểm soát giải ngân) [[src-tt50-2026-nhnn#^pl1-b3-23b]].
- Điều kiện thỏa thuận [[src-tt50-2026-nhnn#^pl1-b3-23c]]: khách hàng bắt buộc dùng dịch vụ cho nhu cầu 30 ngày; chấm dứt phải báo trước trên 30 ngày, hoặc chi phí chuyển đổi tối thiểu bằng toàn bộ tiền lãi và 10% gốc; không phải tiền gửi ngân hàng đại lý.
- Điều kiện khoản tiền gửi [[src-tt50-2026-nhnn#^pl1-b3-23d]]: không phải tiền huy động chỉ để hưởng lãi; giữ trong tài khoản cụ thể với lãi suất không kỳ hạn thấp nhất; có mức tối thiểu thỏa thuận. Phần vượt mức không được áp 25%; không xác định được phần vượt thì toàn bộ không được áp 25%.
- **40%**: danh sách đối tượng tại mục 2.3 Bảng 6 ở trên [[src-tt50-2026-nhnn#^pl1-b3-24]]. **100%**: nguồn vốn không có bảo đảm khác [[src-tt50-2026-nhnn#^pl1-b3-25]].

#### 4. Nguồn vốn bán buôn có bảo đảm (khoản 3 Mục III, Bảng 4)
- Là nguồn vốn được thế chấp bằng tài sản tài chính thuộc sở hữu ngân hàng (kể cả repo), kể cả khi phá sản hoặc thanh lý; với NHNN thì tài sản bảo đảm theo quy định NHNN. Hệ số Bảng 4 áp cho nguồn vốn đang được bảo đảm tại thời điểm tính LCR [[src-tt50-2026-nhnn#^pl1-b3-31]].
- Thế chấp chung không tách bạch được giữa giao dịch trên 30 ngày và trong 30 ngày: tài sản có hệ số rút tiền cao nhất dùng trước cho giao dịch đáo hạn ngắn nhất [[src-tt50-2026-nhnn#^pl1-b3-3]].

#### 5. Phái sinh và yêu cầu bổ sung (Mục IV)
- Dòng tiền phái sinh tính theo thỏa thuận, bù trừ ròng theo đối tác chỉ khi có thỏa thuận bù trừ hai bên đủ điều kiện; với LCR quy VNĐ, phái sinh ngoại hối thanh toán toàn bộ trong cùng ngày được bù trừ dù không có thỏa thuận bù trừ; quyền chọn có thể thực hiện trong 30 ngày giả định được thực hiện khi có lợi cho người mua [[src-tt50-2026-nhnn#^pl1-b4-1]].
- Cheapest to deliver: giả định giao tài sản thanh khoản thấp nhất, áp hệ số HQLA hoặc 25% với tài sản không phải HQLA, đối xứng cho dòng vào và dòng ra [[src-tt50-2026-nhnn#^pl1-b4-14]].
- Tài khoản ký quỹ riêng biệt chỉ được bù trừ trong chính tài khoản đó [[src-tt50-2026-nhnn#^pl1-b4-22]].
- Lookback 24 tháng tính ở cấp độ danh mục, nhưng ngân hàng phải theo dõi dòng ký quỹ ròng ở cấp độ đối tác theo quy định nội bộ [[src-tt50-2026-nhnn#^pl1-b4-25]].

#### 6. Cam kết ngoại bảng và nghĩa vụ tiềm ẩn (Mục V, Bảng 5)
- Giá trị hạn mức cam kết là phần chưa sử dụng, trừ tiền mặt khách hàng ký quỹ hoặc HQLA khách hàng đã chuyển quyền sở hữu (sau hệ số, nếu chưa tính vào HQLA). Hạn mức thanh khoản là cam kết thanh toán nghĩa vụ nợ hiện tại của khách hàng đáo hạn trong 30 ngày; phần không dùng cho nghĩa vụ hiện tại coi là hạn mức tín dụng. Hạn mức tín dụng gồm thẻ tín dụng và hạn mức cấp tín dụng, trừ bảo lãnh [[src-tt50-2026-nhnn#^pl1-b5-1]].
- Tài trợ thương mại (3%) là nhờ thu chứng từ, nhờ thu hoá đơn xuất nhập khẩu, bảo lãnh vận chuyển; nghĩa vụ phi hợp đồng là hỗ trợ tài chính để bảo vệ uy tín hoặc duy trì hoạt động liên doanh, góp vốn, đầu tư [[src-tt50-2026-nhnn#^pl1-b5-31]].

*Diễn giải:* Bảng 6 để trống ô hệ số mục 5.1.3, trong khi Bảng 5 điểm c ghi 10% / 30%. Bảng 6 chỉ là biểu mẫu dẫn chiếu khoản 1.5c Mục V, nên khi lập biểu tính nên dùng hệ số Bảng 5.

---

### Logic Giả định Hành vi Giám sát (Supervisory Behavioral Hypotheses)

*Diễn giải:* (ngoài wiki, chưa có nguồn) ba giả định hành vi dưới đây là cách wiki giải thích thang run-off; nguồn đã ingest không nêu lý do này. Chỉ các tham số có cite.

1. **Phân tầng Tốc độ Tháo chạy theo Mức độ Tinh vi của Chủ nợ (*Information Asymmetry & Sophistication Ladder*)**:
   - Khách hàng bán lẻ được bảo hiểm có chi phí giám sát cao và phản ứng chậm với tin tức thị trường (run-off 5% [[src-bcbs-lcr#^lcr40-7]]).
   - Các định chế tài chính chuyên nghiệp vận hành mô hình quản lý vốn tự động và luôn là bên tháo chạy đầu tiên khi có tin đồn (*first-mover advantage*), dẫn đến run-off bắt buộc là **100%** [[src-bcbs-lcr#^lcr40-42]].
2. **Khái niệm Khóa cứng Vận hành (*Operational Interlocking*)**:
   - Các dòng tiền gắn liền với hệ sinh thái vận hành (trả lương, bù trừ séc, thanh toán chứng khoán) có chi phí chuyển đổi rất cao trong ngắn hạn. Do đó, Basel công nhận tỷ lệ bám dính cao hơn đáng kể (run-off 25% [[src-bcbs-lcr#^lcr40-26]] so với 40% [[src-bcbs-lcr#^lcr40-40]] – 100% [[src-bcbs-lcr#^lcr40-42]]).
3. **Phòng thủ Đa tầng trước Hiệu ứng Sụt giảm Tín nhiệm (*Multi-tier Anti-cliff Defense*)**:
   - Không chỉ tính các dòng tiền theo hợp đồng hiện tại, Basel bắt buộc tính trước chi phí ký quỹ khi bị hạ 3 bậc tín nhiệm (LCR40.51) [[src-bcbs-lcr#^lcr40-51]] và biến động thị trường lịch sử 24 tháng (LCR40.56) [[src-bcbs-lcr#^lcr40-56]] nhằm ngăn ngừa tình trạng ngân hàng bị cạn kiệt thanh khoản tức thì khi bước vào khủng hoảng.

---

## Basel vs VN

| Nhóm cấu phần | Tham số Basel (LCR40) | Tham số VN (TT50/2026/TT-NHNN) | Điều khoản TT50 | Hiệu lực |
|---|---|---|---|---|
| **Bán lẻ ổn định** | 5% (hoặc 3% nếu BHTG có prefunding & chi trả $\le 7$ ngày) [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-11]] | 5% (BHTG bảo hiểm hoàn toàn VÀ có nợ vay trung dài hạn HOẶC có TKTT giao dịch trong 6 tháng gần nhất) [[src-tt50-2026-nhnn#^pl1-b2-2]] | PL1.B.II.2.1 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Bán lẻ kém ổn định** | $\ge 10\%$ (do supervisor lập bucket; không xác định được ổn định thì vào đây) [[src-bcbs-lcr#^lcr40-13]] [[src-bcbs-lcr#^lcr40-14]] | 10% (phần vượt giới hạn bảo hiểm và toàn bộ tiền gửi ngoại tệ) [[src-tt50-2026-nhnn#^pl1-b2-2]] [[src-tt50-2026-nhnn#^pl1-b2-1]] [[src-tt50-2026-nhnn#^pl1-b2-3]] | PL1.B.II.3 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Tiền gửi có kỳ hạn $> 30$ ngày** | 0% (người gửi không có quyền rút trong 30 ngày, hoặc rút sớm bị phạt nặng hơn mất lãi) [[src-bcbs-lcr#^lcr40-16]] | 0% (không có quyền rút trong 30 ngày, HOẶC rút trước hạn chỉ hưởng lãi suất không kỳ hạn VNĐ thấp nhất và không có lợi ích khác) [[src-tt50-2026-nhnn#^pl1-b1-4a]] | PL1.B.I.4.a | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Doanh nghiệp nhỏ (SME)** | Áp như bán lẻ (5% / $\ge 10\%$) nếu tổng tiền gửi $< 1$ triệu EUR và quản lý như bán lẻ [[src-bcbs-lcr#^lcr40-22]] | Áp như bán lẻ (5% / 10%) nếu tiền gửi bình quân tháng liền kề tại ngân hàng $\le 30$ tỷ đồng [[src-tt50-2026-nhnn#^pl1-b3-22]] | PL1.B.III.2.2 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Tiền gửi hoạt động (Operational)** | 25% (Clearing, custody, cash management; switching cost cao); phần bảo hiểm toàn bộ 5% [[src-bcbs-lcr#^lcr40-26]] [[src-bcbs-lcr#^lcr40-36]] | 25% (chỉ phần không vượt mức yêu cầu; chi phí chuyển đổi tối thiểu toàn bộ lãi + 10% gốc; không xác định được phần vượt thì không được áp 25%; phần được bảo hiểm hoàn toàn như bán lẻ ổn định) [[src-tt50-2026-nhnn#^pl1-b3-23a]] [[src-tt50-2026-nhnn#^pl1-b3-23c]] [[src-tt50-2026-nhnn#^pl1-b3-23d]] | PL1.B.III.2.3 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **DN phi tài chính, Sovereign, KBNN, PSE** | 40% (20% nếu bảo hiểm toàn bộ hoặc CP bảo lãnh) [[src-bcbs-lcr#^lcr40-40]] [[src-bcbs-lcr#^lcr40-41]] | 40% (DN không phải DNNVV đủ điều kiện, không phải tổ chức tài chính; Chính phủ, NHNN, NHTW, PSE nước ngoài, KBNN, UBND cấp tỉnh, ngân hàng chính sách, BHTG, BHXH, tổ chức tài chính quốc tế) [[src-tt50-2026-nhnn#^pl1-b3-24]] | PL1.B.III.2.4 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Tổ chức tài chính & nợ bán buôn khác** | 100% [[src-bcbs-lcr#^lcr40-42]] [[src-bcbs-lcr#^lcr40-43]] | 100% (nguồn vốn không có bảo đảm khác, không thuộc khoản 2.2–2.4) [[src-tt50-2026-nhnn#^pl1-b3-25]] | PL1.B.III.2.5 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Repo bảo đảm bằng HQLA cấp 1 / với NHTW** | 0% [[src-bcbs-lcr#^lcr40-47]] | 0% (HQLA cấp 1 hoặc giao dịch với NHNN) [[src-tt50-2026-nhnn#^pl1-b3-3]] | PL1.B.III.3.2.2 (Bảng 4) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Repo bảo đảm bằng HQLA cấp 2A** | 15% [[src-bcbs-lcr#^lcr40-48]] | 15% [[src-tt50-2026-nhnn#^pl1-b3-3]] | PL1.B.III.3.2.2 (Bảng 4) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Repo TSBĐ khác với Chính phủ, PSE, KBNN** | 25% [[src-bcbs-lcr#^lcr40-47]] | 25% (Chính phủ, KBNN, UBND, ngân hàng chính sách, VAMC, DATC, BHTG, BHXH) [[src-tt50-2026-nhnn#^pl1-b3-3]] | PL1.B.III.3.2.2 (Bảng 4) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Repo bảo đảm bằng RMBS cấp 2B** | 25% [[src-bcbs-lcr#^lcr40-48]] | 25% [[src-tt50-2026-nhnn#^pl1-b3-3]] | PL1.B.III.3.2.2 (Bảng 4) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Repo bảo đảm bằng Cấp 2B khác / Non-HQLA** | Cấp 2B khác 50%; Non-HQLA 100% [[src-bcbs-lcr#^lcr40-48]] | Cấp 2B khác 50%; Tài sản tài chính khác 100% [[src-tt50-2026-nhnn#^pl1-b3-3]] | PL1.B.III.3.2.2 (Bảng 4) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Phân bổ TSBĐ thế chấp thác (Collateral Waterfall)** | [cần nguồn: claim LCR40.48 không nêu quy tắc phân bổ]; LCR30.16 chú thích 3 có thứ tự ràng buộc pool khi tính HQLA [[src-bcbs-lcr#^lcr30-16b]] | Tài sản có hệ số rút tiền cao nhất sử dụng trước cho giao dịch ngắn nhất [[src-tt50-2026-nhnn#^pl1-b3-3]] | PL1.B.III.3.2.1.b | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Phái sinh ròng & Hạ bậc tín nhiệm** | Phái sinh ròng 100%; Hạ 3 bậc tín nhiệm 100% [[src-bcbs-lcr#^lcr40-49]] [[src-bcbs-lcr#^lcr40-51]] | Phái sinh ròng 100% (FX cùng ngày được bù trừ ròng); Hạ tối đa 3 bậc tín nhiệm 100% [[src-tt50-2026-nhnn#^pl1-b4-1]] [[src-tt50-2026-nhnn#^pl1-b4-21]] | PL1.B.IV.1, 2.1 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **TSBĐ phái sinh không phải Cấp 1** | Phạt thêm 20% vào HQLA yêu cầu [[src-bcbs-lcr#^lcr40-52]] | Tính thêm 20% giá trị TSBĐ vào dòng tiền ra [[src-tt50-2026-nhnn#^pl1-b4-22]] | PL1.B.IV.2.2 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Biến động định giá thị trường phái sinh** | Dòng collateral ròng 30 ngày lớn nhất trong 24 tháng [[src-bcbs-lcr#^lcr40-56]] | Dòng ký quỹ ròng 30 ngày lớn nhất trong 24 tháng [[src-tt50-2026-nhnn#^pl1-b4-25]] | PL1.B.IV.2.5 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Cam kết tín dụng / thanh khoản Bán lẻ & SME** | Tín dụng 5% / Thanh khoản 5% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 5% / Thanh khoản 5% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Cam kết tín dụng / thanh khoản DN phi tài chính** | Tín dụng 10% / Thanh khoản 30% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 10% / Thanh khoản 30% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Cam kết tín dụng / thanh khoản TCTD** | Tín dụng 40% / Thanh khoản 40% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 40% / Thanh khoản 40% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Cam kết với Định chế tài chính khác** | Tín dụng 40% / Thanh khoản 100% [[src-bcbs-lcr#^lcr40-64]] | Tín dụng 40% / Thanh khoản 100% [[src-tt50-2026-nhnn#^pl1-b5]] | PL1.B.V.1 (Bảng 5) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Giải ngân hợp đồng cho cá nhân & DN phi tài chính** | Vượt quá 50% dòng vào tính 100% [[src-bcbs-lcr#^lcr40-66]] | Phần vượt 50% dòng vào tính 100% [[src-tt50-2026-nhnn#^pl1-b5-2]] | PL1.B.V.2.2 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Cam kết hủy ngang vô điều kiện** | Supervisor quyết định (thường 0%) [[src-bcbs-lcr#^lcr40-64]] | 0%, gồm cả cam kết cung cấp một cam kết ngoại bảng khác [[src-tt50-2026-nhnn#^pl1-b5-31]] | PL1.B.V.3.1.a(i), (iv) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Tài trợ thương mại (Trade finance)** | $\le 5\%$ (quốc gia ấn định) [[src-bcbs-lcr#^lcr40-71]] | 3% [[src-tt50-2026-nhnn#^pl1-b5-31]] | PL1.B.V.3.1.a(ii) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Bảo lãnh ngân hàng, bảo lãnh dự thầu, Autocallable** | Thường $\le 5\%$ do supervisor ấn định [[src-bcbs-lcr#^lcr40-73]] | 5% [[src-tt50-2026-nhnn#^pl1-b5-31]] | PL1.B.V.3.1.a(iii), (v) | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |
| **Dòng tiền ra hợp đồng khác** | 100% (loại trừ chi phí vận hành) [[src-bcbs-lcr#^lcr40-74]] | 100% [[src-tt50-2026-nhnn#^pl1-b6]] | PL1.B.VI.1–2 | LCR từ 01/10/2028 [[src-tt50-2026-nhnn#^d13-1]] |

*Điểm khác biệt trọng yếu giữa Basel và TT50/2026*:
1. **Tiền gửi bán lẻ ổn định**: Basel cho phép áp mức ưu đãi 3% nếu hệ thống bảo hiểm có prefunding và chi trả trong vòng 7 ngày [[src-bcbs-lcr#^lcr40-11]]; TT50 không áp dụng mức 3% mà ấn định mức sàn 5%. Điều kiện ổn định của TT50 gắn chặt với tiêu chí có nợ vay trung dài hạn hoặc tài khoản thanh toán giao dịch thường xuyên 6 tháng, đồng thời phần vượt giới hạn bảo hiểm tiền gửi và toàn bộ tiền gửi ngoại tệ là kém ổn định (10%) [[src-tt50-2026-nhnn#^pl1-b2-2]] [[src-tt50-2026-nhnn#^pl1-b2-1]].
2. **Quyền rút tiền gửi trước hạn**: TT50 quy định cơ chế chế tài rõ ràng: tiền gửi bán lẻ VNĐ có quyền rút trước hạn vẫn được loại trừ khỏi dòng tiền ra 30 ngày nếu rút trước hạn chỉ được hưởng tối đa lãi suất không kỳ hạn VNĐ thấp nhất và không có lợi ích khác [[src-tt50-2026-nhnn#^pl1-b1]].
3. **Ngưỡng quy mô SME**: Basel quy định ngưỡng 1 triệu EUR trên cơ sở tập đoàn hợp nhất [[src-bcbs-lcr#^lcr40-22]]; TT50 quy định ngưỡng tiền gửi bình quân tháng liền kề tại chính ngân hàng không quá 30 tỷ đồng [[src-tt50-2026-nhnn#^pl1-b3-22]].
4. **Chi phí chuyển đổi tiền gửi hoạt động**: TT50 định lượng cụ thể chi phí chuyển đổi đáng kể trong thỏa thuận tối thiểu bằng toàn bộ tiền lãi và 10% phần số tiền gốc [[src-tt50-2026-nhnn#^pl1-b3-23c]], tạo tiêu chuẩn kiểm tra pháp lý rõ ràng hơn so với nguyên tắc định tính chung của Basel LCR40.27.
5. **Ký quỹ TSBĐ non-Level 1**: Basel phạt cộng thêm 20% vào giá trị HQLA yêu cầu [[src-bcbs-lcr#^lcr40-52]]; TT50 quy định tính thêm 20% giá trị tài sản bảo đảm trực tiếp vào mẫu số dòng tiền ra [[src-tt50-2026-nhnn#^pl1-b4-22]].
6. **Tài trợ thương mại và cam kết ngoại bảng**: Basel để mở thẩm quyền quốc gia ($\le 5\%$); TT50 quy định dứt khoát 3% cho tài trợ thương mại và 5% cho bảo lãnh thực hiện hợp đồng/dự thầu. Hạn mức cam kết hủy ngang vô điều kiện và cam kết cung cấp một cam kết ngoại bảng khác được hưởng hệ số 0% [[src-tt50-2026-nhnn#^pl1-b5-31]].
7. **Hiệu lực**: TT50/2026 có hiệu lực từ 01/10/2026 [[src-tt50-2026-nhnn#^d37-1]]; LCR áp dụng từ 01/10/2028 theo lộ trình [[src-tt50-2026-nhnn#^d13-1]].

## Ứng dụng trong ALM

### Ứng dụng Quản trị tại ALM Treasury

*Diễn giải:* các đòn bẩy dưới đây là đề xuất của wiki; chỉ tham số có cite.

1. **Chiến lược Chuyển dịch Cơ cấu Nguồn vốn (*Liability Restructuring*)**:
   - Thay thế các khoản tiền gửi bán buôn doanh nghiệp lớn ngắn hạn (run-off 40% [[src-bcbs-lcr#^lcr40-40]]) bằng tiền gửi thanh toán bán lẻ gắn tài khoản lương (run-off 5% nếu đủ điều kiện stable [[src-bcbs-lcr#^lcr40-7]]) hoặc tiền gửi dịch vụ quản lý tiền mặt doanh nghiệp (run-off 25% [[src-bcbs-lcr#^lcr40-26]]).
   - Hạn chế phát hành chứng chỉ tiền gửi ngắn hạn cho các định chế tài chính (run-off 100% [[src-bcbs-lcr#^lcr40-42]] [[src-bcbs-lcr#^lcr40-43]]).
2. **Quản trị Tối ưu Hợp đồng Cam kết Ngoại bảng**:
   - Tách bạch rõ ràng hợp đồng hạn mức tín dụng (*Credit Facility*, drawdown 10%) với hạn mức thanh khoản (*Liquidity Facility*, drawdown 30%) trong các hợp đồng tài trợ doanh nghiệp lớn [[src-bcbs-lcr#^lcr40-61]] [[src-bcbs-lcr#^lcr40-64]].
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
  - *Thực tế*: Theo LCR40.17 [[src-bcbs-lcr#^lcr40-17]], hành vi này có thể khiến cơ quan thanh tra phán quyết rằng biện pháp phạt không đủ tính răn đe và buộc ngân hàng xếp **toàn bộ danh mục tiền gửi có kỳ hạn** sang tiền gửi không kỳ hạn. *Diễn giải:* dòng tiền ra vì vậy tăng.
- ❌ **Hiểu nhầm về Nguồn vốn SME**: Cho rằng mọi doanh nghiệp vừa và nhỏ đều được áp hệ số rút vốn bán lẻ (5%–10%).
  - *Thực tế*: Theo LCR40.22–40.23, chỉ các SME có tổng vốn huy động dưới 1 triệu EUR (tính gộp trên cơ sở hợp nhất) mới được xử lý như tiền gửi bán lẻ [[src-bcbs-lcr#^lcr40-22]] [[src-bcbs-lcr#^lcr40-23]].
- ❌ **Ảo tưởng về Hạn mức Cam kết Huỷ ngang có Điều kiện**: Cho rằng hợp đồng ghi "ngân hàng có quyền đơn phương hủy hạn mức" thì không phải tính dòng ra.
  - *Thực tế*: Theo LCR40.59 [[src-bcbs-lcr#^lcr40-59]], chuẩn mực tính toán dòng ra cho cả các hạn mức cam kết không hủy ngang và hạn mức hủy ngang có điều kiện (*committed or conditionally cancellable*).

---

## Đọc thêm
- [[lcr]] — Tỷ lệ khả năng chi trả thanh khoản tổng thể.
- [[net-cash-outflows]] — Dòng tiền ra ròng (mẫu số của LCR).
- [[cash-inflows]] — Tổng dòng tiền vào kỳ vọng 30 ngày và trần 75%.
- [[run-off-rate]] — Khái niệm và nguyên lý xác định tỷ lệ rút vốn trong stress test.
- [[retail-deposit-stability]] — Tiền gửi bán lẻ và cơ chế phân loại ổn định vs kém ổn định.
- [[unsecured-wholesale-funding]] — Nguồn vốn bán buôn không có bảo đảm.
- [[secured-funding]] — Nguồn vốn có bảo đảm (giao dịch Repo).
- [[operational-deposits]] — Tiền gửi hoạt động gắn liền với nghiệp vụ thanh toán, lưu ký, bù trừ.
- [[committed-facilities]] — Hạn mức tín dụng và hạn mức thanh khoản cam kết ngoại bảng.
- [[derivatives-and-contingent-outflows]] — Dòng ra phái sinh và nghĩa vụ tài trợ tiềm tàng.
- [[tt50-2026]] — Thông tư 50/2026/TT-NHNN của Ngân hàng Nhà nước Việt Nam.
