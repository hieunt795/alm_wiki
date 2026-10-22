---
title: "Các thành phần liên kết và kênh truyền dẫn tương tác giữa LCR và NSFR"
aliases: [LCR-NSFR interlinkages, Liên kết LCR và NSFR, LCR-NSFR transmission channels, Tương tác thanh khoản kép]
type: concept
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of: 2026-10-16
sources: ["[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-bcbs-irrbb-2016]]"]
relations:
  - {type: part-of, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: part-of, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr20-1]]"}
  - {type: drives, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
tags: [liquidity, lcr, nsfr, balance-sheet, transmission-channels, alm-strategy, irrbb]
updated: 2026-10-22
reviewed:
---

## Ý chính

Bảng cân đối kế toán của ngân hàng thương mại là một **chỉnh thể hữu cơ duy nhất (*single unified balance sheet*)**. Chuẩn mực Basel thiết lập hai thước đo thanh khoản bổ trợ cho nhau: [[lcr]] phòng thủ trước cú sốc rút vốn cấp tính trong **30 ngày dương lịch**, trong khi [[nsfr]] thiết lập kỷ luật cấu trúc nguồn vốn tài trợ tài sản trong **khoảng thời gian 1 năm** [[src-bcbs-lcr#^lcr10-1]] [[src-bcbs-nsfr#^nsf10-1]].

Các thành phần liên kết giữa LCR và NSFR (*LCR-NSFR Interlinkages*) là các kênh truyền dẫn kinh tế và kỹ thuật mà qua đó, một giao dịch huy động vốn, giải ngân tín dụng, đầu tư chứng khoán hoặc cam kết ngoại bảng của ngân hàng sẽ **đồng thời tác động lên cả hai chỉ số**. Các kênh này tạo ra sự đánh đổi phức tạp: nhiều hành động cải thiện LCR lại làm suy giảm NSFR, hoặc ngược lại, đòi hỏi ALM Treasury phải nhận diện chính xác từng điểm giao thoa để quản trị bảng cân đối một cách nhất quán [[src-bcbs-lcr#^lcr20-1]] [[src-bcbs-nsfr#^nsf20-2]].

---

## Bảy Kênh Truyền dẫn và Thành phần Liên kết Cốt lõi

```
+---------------------------------------------------------------------------------------+
|                    BẢNG CÂN ĐỐI KẾ TOÁN VÀ CÁC KÊNH TRUYỀN DẪN LCR - NSFR             |
+---------------------------------------------------------------------------------------+
                                           |
    +-------------------+------------------+------------------+-------------------+
    |                   |                  |                  |                   |
    v                   v                  v                  v                   v
+---------------+ +---------------+ +---------------+ +---------------+ +---------------+
|  KÊNH 1       | |  KÊNH 2       | |  KÊNH 3       | |  KÊNH 4       | |  KÊNH 5       |
|  Đòn bẩy kép  | | Trừng phạt kép| |   Vùng mù     | | Cạm bẫy cầm cố| | Bất đối xứng  |
|  Level 1 TPCP | | Vốn liên NH   | | Kỳ hạn 6-12M  | | Repo >= 1 năm | | Trần HQLA L2  |
| (L1: HQLA 100%| (Vay < 6M:      | (Outflow 30D = 0| (LCR không đổi| (LCR: Trần 40%|
|  RSF chỉ 5%)  |  LCR out 100%,  |  nhưng NSFR mất |  nhưng RSF vọt  |  NSFR: Tính hết |
|               |  ASF = 0%)      |  50% giá trị)   |  lên 100%!)     |  không trần)    |
+---------------+ +---------------+ +---------------+ +---------------+ +---------------+
                                           |
                               +-----------+-----------+
                               |                       |
                               v                       v
                      +-----------------+     +-----------------+
                      |  KÊNH 6         |     |  KÊNH 7         |
                      |  Đánh thuế kép  |     |  Thác trôi      |
                      |  Ngoại bảng     |     |  Kỳ hạn nợ      |
                      | (LCR drawdown   |     | (3Y -> 1Y: -50% |
                      |  + NSFR RSF 5%) |     |  6M -> 30D: out)|
                      +-----------------+     +-----------------+
```

### 1. Kênh Đòn bẩy Kép của Trái phiếu Chính phủ Level 1 (Dual Leverage)
- **Cơ chế liên kết**:
  - Trong LCR: Trái phiếu chính phủ 0% RW thuộc [[level-1-assets]] được tính **100% vào HQLA**, không bị áp dụng tỷ lệ chiết khấu (haircut 0%) và không bị giới hạn trần định lượng [[src-bcbs-lcr#^lcr30-41]].
  - Trong NSFR: Cũng chính lô trái phiếu đó, khi ở trạng thái tự do (*unencumbered*), chỉ chịu hệ số [[rsf-hqla-and-central-bank-reserves|RSF]] bằng **5%** [[src-bcbs-nsfr#^nsf30-26]].
- **Hệ quả ALM Treasury**:
  - Đây là tài sản có tính thanh khoản và đòn bẩy vốn cao nhất toàn hệ thống. Cứ mỗi 100 tỷ VND đầu tư vào TPCP Level 1, ngân hàng bổ sung trọn vẹn 100 tỷ VND vào tử số LCR, nhưng chỉ tiêu tốn vỏn vẹn 5 tỷ VND nguồn vốn ổn định (RSF) ở mẫu số NSFR.
  - Tận dụng kênh này, Treasury có thể gia tăng mạnh mẽ đệm an toàn LCR mà không gây áp lực huy động nợ dài hạn tốn kém trong NSFR.

---

### 2. Kênh Trừng phạt Kép của Nguồn vốn Liên ngân hàng Ngắn hạn (Double Penalty)
- **Cơ chế liên kết**:
  - Trong LCR: Nguồn vốn vay mượn không bảo đảm từ các định chế tài chính khác có kỳ hạn $\le 30$ ngày bị áp tỷ lệ rút vốn ([[run-off-rate]]) tuyệt đối **100%** [[src-bcbs-lcr#^lcr40-42]].
  - Trong NSFR: Mọi khoản nợ huy động từ các định chế tài chính và NHTW có kỳ hạn còn lại $< 6$ tháng bị gán hệ số [[asf-wholesale-and-operational-funding|ASF]] bằng **0%** [[src-bcbs-nsfr#^nsf30-14]].
- **Hệ quả ALM Treasury**:
  - Mô hình kinh doanh truyền thống: "Vay ngắn hạn liên ngân hàng để tài trợ danh mục tín dụng trung dài hạn" bị cả hai chuẩn mực trừng phạt triệt để.
  - Nếu Treasury vay liên ngân hàng 3 tháng để mua trái phiếu hoặc giải ngân:
    * Khi bước vào 30 ngày cuối, khoản vay giáng đòn trực diện vào LCR (dòng ra 100%).
    * Trong toàn bộ 3 tháng đó, khoản vay không đóng góp bất kỳ đồng nào vào ASF của NSFR ($\text{ASF} = 0\%$), trong khi tài sản giải ngân lại phát sinh RSF từ 5% đến 85%, kéo tụt tỷ lệ NSFR tức thì.

---

### 3. Kênh "Vùng Mù" Kỳ hạn 6 đến 12 tháng (The 6–12 Month Tenor Mismatch)
- **Cơ chế liên kết**:
  - Trong LCR: Khoảng thời gian kiểm tra sức chịu tải chỉ kéo dài đúng 30 ngày. Do đó, một khoản tiền gửi bán buôn doanh nghiệp hoặc định chế tài chính có kỳ hạn 9 tháng hoàn toàn nằm ngoài chân trời stress, **không phát sinh bất kỳ dòng tiền ra nào trong LCR** (outflow = 0%).
  - Trong NSFR: Vì kỳ hạn còn lại dưới 1 năm, khoản vốn này bị tụt hệ số xuống nhóm **$\text{ASF} = 50\%$** (nếu là doanh nghiệp phi tài chính hoặc định chế tài chính có kỳ hạn 6M–1Y) [[src-bcbs-nsfr#^nsf30-13]].
- **Hệ quả ALM Treasury**:
  - Tạo ra "bẫy tối ưu hóa cục bộ": Nếu Treasury chỉ nhìn vào LCR, họ sẽ có xu hướng huy động vốn bán buôn kỳ hạn 6–9 tháng (vừa tránh được dòng ra LCR 30 ngày, vừa có chi phí lãi suất rẻ hơn phát hành trái phiếu dài hạn $\ge 1$ năm).
  - Tuy nhiên, hành động này làm thất thoát 50% giá trị nguồn vốn ổn định trong NSFR. Ngân hàng phải trả chi phí lãi suất bán buôn nhưng chỉ tài trợ được một nửa tài sản dài hạn tương ứng.

---

### 4. Kênh Truyền dẫn Cầm cố Tài sản Dài hạn (Collateral Encumbrance Transmission)
- **Cơ chế liên kết**:
  - Trong LCR: Ngân hàng đem trái phiếu Level 1 đi cầm cố (repo) để huy động vốn với kỳ hạn 1 năm. Giao dịch này không tạo ra dòng tiền ra LCR trong 30 ngày tới.
  - Trong NSFR: Chuẩn mực NSF30.20 quy định: Bất kỳ tài sản nào trên bảng cân đối kế toán bị cầm cố (*encumbered*, xem [[asset-encumbrance]]) từ 1 năm trở lên đều phải chịu hệ số **$\text{RSF} = 100\%$**, bất kể tài sản gốc trước khi cầm cố là tiền mặt hay Trái phiếu Chính phủ [[src-bcbs-nsfr#^nsf30-20]].
- **Hệ quả ALM Treasury**:
  - Khoản vốn huy động về có kỳ hạn 1 năm chỉ nhận được $\text{ASF} = 100\%$ [[src-bcbs-nsfr#^nsf30-10]].
  - Kết quả: Khoản tài trợ nhận về (ASF 100%) chỉ vừa khít bù đắp cho mức tăng vọt RSF của tài sản bị cầm cố (RSF nhảy từ 5% lên 100%). Giao dịch repo dài hạn không tạo ra bất kỳ thặng dư NSFR ròng nào, đồng thời **tước đoạt vĩnh viễn tư cách HQLA** của lô trái phiếu đó trong LCR (vì tài sản đã bị encumbered).

---

### 5. Kênh Bất Đối xứng Trần HQLA (HQLA Cap Asymmetry)
- **Cơ chế liên kết**:
  - Trong LCR: Tài sản [[level-2-assets]] bị áp trần định lượng nghiêm ngặt sau khi thực hiện cơ chế unwinding: Level 2A và 2B cộng lại không được vượt quá **40% tổng HQLA**, và Level 2B không được vượt quá **15% tổng HQLA** [[src-bcbs-lcr#^lcr30-37]]. Phần vượt trần bị loại khỏi tử số LCR.
  - Trong NSFR: Toàn bộ danh mục Level 2A nhận hệ số $\text{RSF} = 15\%$, và Level 2B nhận $\text{RSF} = 50\%$ **mà không chịu bất kỳ giới hạn trần hay điều kiện vận hành nào** của LCR (Footnote 12 NSF30) [[src-bcbs-nsfr#^nsf30-28]] [[src-bcbs-nsfr#^nsf30-29]].
- **Hệ quả ALM Treasury**:
  - Nếu ngân hàng nắm giữ danh mục trái phiếu doanh nghiệp Level 2A vượt quá trần 40% của LCR: Phần trái phiếu vượt trần đóng góp bằng 0 vào tử số LCR, nhưng vẫn tiếp tục tiêu tốn 15% RSF trong NSFR.
  - Đây là vùng tổn thất thanh khoản biên (*deadweight liquidity loss*): Treasury gánh chịu chi phí nguồn vốn ổn định mà không thu lại được giá trị tuân thủ thanh khoản ngắn hạn.

---

### 6. Kênh Đánh thuế Kép trên Cam kết Ngoại bảng (Off-Balance Sheet Double Tax)
- **Cơ chế liên kết**:
  - Trong LCR: Phần hạn mức tín dụng và thanh khoản cam kết chưa giải ngân (*undrawn committed facilities*) chịu tỷ lệ rút vốn từ **5% đến 100%** (trong đó hạn mức thanh khoản cấp cho doanh nghiệp chịu 30%, cấp cho định chế tài chính chịu 100%) [[src-bcbs-lcr#^lcr40-64]].
  - Trong NSFR: Mọi cam kết tín dụng và thanh khoản không thể hủy ngang hoặc chỉ hủy ngang có điều kiện đều bị đánh thuế đồng loạt **$\text{RSF} = 5\%$** trên giá trị chưa rút [[src-bcbs-nsfr#^nsf30-34]].
- **Hệ quả ALM Treasury**:
  - Việc cấp hạn mức cho khách hàng lớn không chỉ tạo ra rủi ro thanh khoản cấp tính trong 30 ngày (làm phình to mẫu số LCR) mà còn ngốn trực tiếp nguồn vốn dài hạn trong NSFR ngay cả khi khách hàng chưa rút một đồng nào.

---

### 7. Kênh Thác Trôi Kỳ hạn (Maturity Roll-down Cascade)
- **Bản chất động học**:
  - Một khoản nợ phát hành kỳ hạn 3 năm (ví dụ Trái phiếu ngân hàng 1.000 tỷ VND) chuyển dịch trạng thái theo thời gian và tạo ra 3 làn sóng tác động liên tiếp:

```
Nợ phát hành 3Y (1.000 tỷ)
  | 
  |-- Khi t > 1Y:       ASF = 100% (NSFR), LCR outflow = 0. Vận hành ổn định.
  |
  |-- Khi t = 365 ngày: ASF tụt từ 100% xuống 50% [[src-bcbs-nsfr#^nsf30-13]]. 
  |                     -> Mất ngay 500 tỷ ASF. Cú sốc cấu trúc lần 1!
  |
  |-- Khi t = 180 ngày: ASF tụt từ 50% xuống 0% (nếu là nợ tổ chức TC) [[src-bcbs-nsfr#^nsf30-14]].
  |                     -> Mất tiếp 500 tỷ ASF còn lại. Cú sốc cấu trúc lần 2!
  |
  +-- Khi t = 30 ngày:  LCR Outflow kích hoạt 100% [[src-bcbs-lcr#^lcr40-42]].
                        -> Đòi hỏi phải có ngay 1.000 tỷ HQLA để bù đắp. Cú sốc cấp tính lần 3!
```

---

## Ma trận Tác động Song song giữa LCR và NSFR

| Khoản mục Bảng cân đối | Tác động lên LCR (30 ngày) | Tác động lên NSFR (1 năm) | Đánh giá Tương tác ALM | Căn cứ Chuẩn mực |
|---|---|---|---|---|
| **Trái phiếu Chính phủ Level 1** | Tăng HQLA 100% (haircut 0%) | Tăng RSF 5% | **Đòn bẩy kép tối ưu**: Cải thiện LCR cực mạnh, ngốn rất ít RSF | [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-nsfr#^nsf30-26]] |
| **Trái phiếu Doanh nghiệp Level 2A** | Tăng HQLA 85% (haircut 15%, trần 40%) | Tăng RSF 15% | Cải thiện cả hai nhưng bị chặn bởi trần unwinding của LCR | [[src-bcbs-lcr#^lcr30-43]] [[src-bcbs-nsfr#^nsf30-28]] |
| **Cho vay Doanh nghiệp Dài hạn** | Dòng vào = 0% (do kỳ hạn $> 30$ ngày) | Tăng RSF 85% | **Bất lợi thanh khoản**: Không tạo dòng tiền ngắn hạn, ngốn nguồn vốn ổn định | [[src-bcbs-lcr#^lcr40-87]] [[src-bcbs-nsfr#^nsf30-31]] |
| **Cho vay Doanh nghiệp Ngắn hạn** | Dòng vào 50% (tái cấp 50%) | Tăng RSF 50% (giả định roll-over) | Cân bằng đối xứng: Cả hai chỉ số đều giả định tỷ lệ tái tục 50% | [[src-bcbs-lcr#^lcr40-87]] [[src-bcbs-nsfr#^nsf30-13]] |
| **Tiền gửi Bán lẻ Stable (CASA)** | Dòng ra chỉ 5% (hoặc 3%) | Nhận ASF 95% | **Nguồn vốn vàng**: Tối ưu hóa đồng thời cả LCR và NSFR | [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-nsfr#^nsf30-11]] |
| **Vốn Bán buôn DN 6 – 12 tháng** | Dòng ra 0% (kỳ hạn $> 30$ ngày) | Nhận ASF 50% (mất 50%) | **Vùng mù kỳ hạn**: Có lợi cho LCR nhưng gây thiệt hại 50% cho NSFR | [[src-bcbs-lcr#^lcr40-1]] [[src-bcbs-nsfr#^nsf30-13]] |
| **Vay Liên ngân hàng $< 6$ tháng** | Dòng ra 100% (nếu $\le 30$ ngày) | Nhận ASF 0% | **Trừng phạt kép**: Phá vỡ tính an toàn của cả hai chỉ số | [[src-bcbs-lcr#^lcr40-42]] [[src-bcbs-nsfr#^nsf30-14]] |
| **Repo TPCP kỳ hạn $\ge 1$ năm** | Dòng ra 0% | RSF của TPCP vọt lên 100% | **Cạm bẫy cầm cố**: Mất HQLA trong LCR, triệt tiêu đòn bẩy trong NSFR | [[src-bcbs-lcr#^lcr30-24]] [[src-bcbs-nsfr#^nsf30-20]] |
| **Cam kết Tín dụng Ngoại bảng** | Dòng ra 5% – 10% | Tăng RSF 5% trên số dư chưa rút | Đánh thuế kép lên mẫu số của cả hai chỉ số | [[src-bcbs-lcr#^lcr40-64]] [[src-bcbs-nsfr#^nsf30-34]] |

---

## Mở rộng sang Rủi ro Lãi suất (IRRBB): Kênh dẫn truyền Thời lượng (Duration Channel)

*Diễn giải:* (ngoài wiki, chưa có nguồn) chưa nguồn đã ingest nào nói trực tiếp LCR/NSFR tác động lên [[economic-value-of-equity]] hay [[net-interest-income-sensitivity]]; hai kênh dưới đây ghép tham số LCR/NSFR với kịch bản sốc IRRBB, mỗi tham số cite riêng. Khi tích hợp thêm chuẩn mực [[bcbs-irrbb]] (d368), tương tác giữa LCR và NSFR mở rộng sang hai kênh dẫn truyền rủi ro thị trường sống còn:

### 8. Kênh 8: "Cạm bẫy Thời lượng" của Đệm HQLA (The HQLA Duration Trap)
- **Đòn bẩy thanh khoản nhưng rủi ro vốn**: Trái phiếu Chính phủ Level 1 unencumbered mang lại lợi ích thanh khoản tối thượng: đóng góp 100% vào HQLA của [[lcr]] [[src-bcbs-lcr#^lcr30-41]] và chỉ tiêu tốn 5% RSF trong [[nsfr]] [[src-bcbs-nsfr#^nsf30-26]]. Do đó, các ngân hàng thường có xu hướng nắm giữ quy mô lớn TPCP dài hạn (kỳ hạn 5–15 năm) để tối đa hoá đồng thời cả LCR và NSFR.
- **Cú sốc EVE**: Tuy nhiên, việc nắm giữ TPCP dài hạn tạo ra thời lượng (duration) rất lớn. Khi lãi suất thị trường tăng vọt theo kịch bản sốc song song (+200 bps USD/EUR) hoặc dốc lên (steepener) theo Annex 2 [[src-bcbs-irrbb-2016#^irrbb-u07-1]], giá trị thị trường của danh mục HQLA sụt giảm sâu sắc. Nếu tài sản hạch toán FVTOCI/AFS, khoản lỗ chưa thực hiện sẽ trực tiếp làm xói mòn Vốn cấp 1 (Tier 1 Capital), đẩy ngân hàng vào nguy cơ vi phạm phép thử ngoại lai [[outlier-bank-test|Outlier Bank Test ($\max \Delta\text{EVE} > 15\%$ Tier 1 Capital)]] [[src-bcbs-irrbb-2016#^irrbb-p12-1]].

### 9. Kênh 9: Chuyển đổi Kỳ hạn NSFR là Cội nguồn của Khe hở Tái định giá ([[gap-risk]])
- Hoạt động trung gian ngân hàng cố hữu là lấy ngắn nuôi dài: tài trợ tài sản dài hạn (RSF 65%–85%) bằng tiền gửi bán lẻ và tiền gửi doanh nghiệp ngắn hạn.
- Sự chênh lệch kỳ hạn này vừa là nguyên nhân kéo giảm tỷ lệ [[nsfr]], vừa tạo ra một khe hở tái định giá âm khổng lồ trong ngắn hạn. Khi lãi suất ngắn hạn tăng nhanh (Short rate shock up) [[src-bcbs-irrbb-2016#^irrbb-u07-1]], chi phí trả lãi huy động tăng vọt trong khi tài sản chưa kịp tái định giá, bóp nghẹt thu nhập lãi thuần [[net-interest-income-sensitivity|$\Delta\text{NII}$]] và làm bốc hơi giá trị kinh tế [[economic-value-of-equity|$\Delta\text{EVE}$]].

---

## Ý nghĩa Chiến lược đối với ALM Treasury

Việc thấu hiểu các kênh liên kết trên là tiền đề bắt buộc để Khối Nguồn vốn & ALM chuyển dịch từ lối tư duy "quản trị chỉ số đơn lẻ" sang **Chiến lược Quản trị Thanh khoản và Bảng cân đối Tổng hợp (*Integrated Balance Sheet Strategy*)**:

1. **Điều phối Cấu trúc Bảng cân đối Đa mục tiêu**: Không thể giải bài toán thanh khoản một cách độc lập; việc mua sắm tài sản hay cấu trúc nguồn vốn phải được tối ưu hóa đồng thời trên không gian ràng buộc của cả LCR, NSFR và IRRBB.
2. **Thiết kế Mô hình Term Liquidity FTP Toàn diện**: Biểu phí điều chuyển vốn nội bộ phải phản ánh đầy đủ cả chi phí đệm thanh khoản ngắn hạn (phí LCR), chi phí kỳ hạn vốn cấu trúc (phí RSF/thưởng ASF), và phần bù rủi ro lãi suất (IRRBB duration charge).
3. **Quản trị Tài sản Bảo đảm Phân tầng (Collateral Waterfall)**: Thiết lập quy tắc ưu tiên cầm cố tài sản có RSF cao (như bất động sản, nợ doanh nghiệp) để bảo vệ trạng thái *unencumbered* cho Trái phiếu Chính phủ Level 1 nhằm duy trì đòn bẩy kép tối ưu, đồng thời thực hiện hoán đổi lãi suất (IRS) để phòng ngừa rủi ro thời lượng.

