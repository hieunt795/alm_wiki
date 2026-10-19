---
title: "Định Giá Điều Chuyển Thanh Khoản Nội Bộ (Liquidity Transfer Pricing — Liquidity FTP)"
aliases: [Liquidity Transfer Pricing, Liquidity FTP, FTP Thanh khoản, Định giá điều chuyển thanh khoản, Phí thanh khoản nội bộ, Term Liquidity Premium, TLP]
type: concept
domains: [alm, product]
status: active
maturity: canonical
sources: ["[[src-choudhry-principles-banking]]", "[[src-ftp-transmission-analysis]]", "[[src-vab-ftp]]"]
relations:
  - {type: priced-by, to: "[[lcr]]", cite: "[[src-choudhry-principles-banking#^choudhry-ftp-15]]"}
  - {type: priced-by, to: "[[nsfr]]", cite: "[[src-choudhry-principles-banking#^choudhry-ftp-14]]"}
  - {type: input-to, to: "[[ftp-transmission-mechanism]]", cite: "[[src-ftp-transmission-analysis#^ftp-trans-2]]"}
  - {type: input-to, to: "[[ftp-pricing-methodology]]", cite: "[[src-vab-ftp#^vab-ftp-5]]"}
  - {type: part-of, to: "[[funds-transfer-pricing]]", cite: "[[src-choudhry-principles-banking#^choudhry-ftp-14]]"}
tags: [ftp, liquidity-ftp, alm, treasury, term-liquidity-premium, lcr, nsfr, alco, pricing, concept]
updated: 2026-10-17
reviewed:
---

## 1. Bản Chất và Cuộc Cách Mạng Tư Duy về FTP

Theo định nghĩa của Giáo sư Moorad Choudhry, **Funds Transfer Pricing (FTP) không phải là việc phòng ngừa rủi ro ra bên ngoài thị trường, cũng không phải là việc điều chuyển vật lý các dòng tiền tệ; bản chất cốt tử của FTP là cơ chế chuyển giao rủi ro nội bộ (Internal Transfer of Risk)** [[src-choudhry-principles-banking#^choudhry-ftp-10]].

Trước cuộc khủng hoảng tài chính 2007–2008, ngành ngân hàng toàn cầu chủ yếu vận hành hệ thống **Classic Interest-Rate FTP (FTP Lãi suất Đơn thuần)**. Trong mô hình cổ điển này:
- Toàn bộ ngân hàng áp dụng một đường cong lãi suất phi rủi ro duy nhất (Libor/Euribor flat).
- Các đơn vị kinh doanh thoải mái cho vay các khoản tín dụng trung dài hạn 5–10 năm mà chỉ bị tính phí huy động vốn ngắn hạn, với niềm tin ngây thơ rằng Treasury luôn có thể tái tài trợ (rollover) nguồn vốn không giới hạn trên thị trường liên ngân hàng.

Cuộc khủng hoảng 2008 đã vạch trần lỗ hổng chết người này khi thị trường bán buôn đóng băng, chênh lệch tín dụng và thanh khoản nới rộng kỷ lục [[src-choudhry-principles-banking#^choudhry-ftp-14]]. Sự ra đời của **Liquidity Transfer Pricing (Liquidity FTP)** là một bước tiến mang tính cách mạng: **buộc mọi đơn vị kinh doanh tạo ra tài sản dài hạn phải gánh chịu đầy đủ chi phí thanh khoản và chi phí tuân thủ quy định mà tài sản đó gây ra cho toàn bộ bảng cân đối** [[src-choudhry-principles-banking#^choudhry-ftp-15]].

---

## 2. Bốn Tầng Cấu Thành Lãi Suất Điều Chuyển Vốn Nội Bộ

Hệ thống Liquidity FTP hiện đại bóc tách một mức lãi suất FTP tổng hợp thành 4 tầng chi phí độc lập và minh bạch [[src-choudhry-principles-banking#^choudhry-ftp-6]] [[src-choudhry-principles-banking#^choudhry-ftp-14]]:

$$\text{FTP Rate} = \text{Base Rate} + \text{Term Liquidity Premium (TLP)} + \text{Contingent Liquidity Charge} + \text{Regulatory Cost}$$

```
+---------------------------------------------------------------------------------------------------+
|                        CẤU TRÚC ĐA TẦNG CỦA LÃI SUẤT ĐIỀU CHUYỂN VỐN (FTP)                        |
+---------------------------------------------------------------------------------------------------+
|  1. BASE INTEREST RATE (Lãi suất Cơ sở Lãi suất Phi Rủi ro)                                        |
|     - Neo theo đường cong OIS / RFR / Swap Curve tương ứng với kỳ hạn định giá lại (Repricing)    |
+---------------------------------------------------------------------------------------------------+
|  2. TERM LIQUIDITY PREMIUM — TLP (Phần bù Rủi ro Thanh khoản Có kỳ hạn)                          |
|     - Chi phí khóa nguồn vốn dài hạn trên thị trường vốn (Bond Spread / Wholesale Cost)           |
|     - Tính theo kỳ hạn đáo hạn hợp đồng thực tế (Contractual Maturity Tenor)                      |
+---------------------------------------------------------------------------------------------------+
|  3. CONTINGENT LIQUIDITY CHARGE / BUFFER COST (Chi phí Dự trữ Đệm Thanh khoản LCR)               |
|     - Phí gánh khoản lỗ âm (Negative Carry) của việc nắm giữ tài sản HQLA (TPCP, dự trữ NHTW)     |
|     - Thu từ các tài sản làm tăng mẫu số dòng tiền ra hoặc các cam kết ngoại bảng                 |
+---------------------------------------------------------------------------------------------------+
|  4. REGULATORY COST CHARGE (Chi phí Tuân thủ Tỷ lệ Cấu trúc NSFR & Đòn bẩy LEV)                   |
|     - Phạt các tài sản có hệ số RSF cao (cho vay dài hạn chịu RSF 85%-100%)                       |
|     - Thưởng (Credit) cho nguồn tiền gửi ổn định có hệ số ASF cao (CASA lõi ASF 95%, nợ >1Y 100%) |
+---------------------------------------------------------------------------------------------------+
```

### A. Lãi suất Cơ sở (Base Rate)
- Đo lường chi phí vốn phi rủi ro thuần túy, phản ánh rủi ro thị trường và lãi suất tham chiếu.
- Được xác định theo kỳ hạn tái định giá (Repricing Tenor) qua đường cong hoán đổi lãi suất qua đêm (OIS) hoặc Trái phiếu Chính phủ.

### B. Phần bù Thanh khoản Có kỳ hạn (Term Liquidity Premium — TLP)
- Đo lường chi phí thực tế mà Treasury phải trả để huy động được một đồng vốn có kỳ hạn tương ứng trên thị trường tài chính bán buôn (chênh lệch giữa lãi suất phát hành trái phiếu ngân hàng/chứng chỉ tiền gửi và Base Rate) [[src-choudhry-principles-banking#^choudhry-ftp-15]].
- Triệt tiêu hoàn toàn thói quen "ăn xổi" của các chi nhánh khi đem nguồn vốn ngắn hạn đi cho vay kỳ hạn 10 năm mà không hạch toán chi phí bảo hiểm kỳ hạn.

### C. Chi phí Đệm Thanh khoản Khẩn cấp (Contingent Liquidity Charge / LCR Buffer Cost)
- Để tài trợ an toàn cho một khoản vay tín dụng hoặc cam kết cấp hạn mức, ngân hàng bắt buộc phải duy trì một lượng [[hqla|Tài sản thanh khoản cao HQLA]] để bảo đảm [[lcr|LCR $\ge 100\%$]].
- Tài sản HQLA (như TPCP hay tiền gửi NHTW) thường có lợi suất thấp hơn chi phí huy động vốn của ngân hàng, tạo ra một khoản **lỗ mang vác âm (negative carry)**. 
- Khoản lỗ mang vác này không thể để Treasury tự gánh chịu làm méo mó kết quả kinh doanh, mà phải được tính toán và phân bổ trực tiếp vào chi phí FTP đầu vào của các khoản vay tín dụng gây ra rủi ro thanh khoản đó [[src-choudhry-principles-banking#^choudhry-ftp-15]].

### D. Chi phí Ràng buộc Cấu trúc (Regulatory Charge / NSFR & Leverage)
- **Tài sản Có (Cho vay)**: Khoản vay dài hạn $\ge 1$ năm chịu hệ số $\text{RSF} = 85\% - 100\%$ [[required-stable-funding]], buộc ngân hàng phải phát hành nợ dài hạn tốn kém. Đơn vị kinh doanh phải trả thêm phụ phí NSFR tương ứng.
- **Tài sản Nợ (Huy động tiền gửi)**: Các khoản tiền gửi CASA ổn định được bảo hiểm nhận hệ số $\text{ASF} = 95\%$ [[available-stable-funding]], giúp ngân hàng giảm thiểu nhu cầu nợ dài hạn. Do đó, đơn vị kinh doanh huy động được CASA sẽ được Treasury **thưởng thêm lãi suất (Liquidity Credit)**, khuyến khích tối đa hóa nguồn vốn bền vững.

---

## 3. Hai Nguyên Tắc Vàng Trong Điều Hành FTP

Giáo sư Choudhry chỉ rõ hệ thống FTP chỉ vận hành chuẩn xác khi tuân thủ nghiêm ngặt 2 nguyên tắc nền tảng [[src-choudhry-principles-banking#^choudhry-ftp-11]] [[src-choudhry-principles-banking#^choudhry-ftp-12]]:

### A. Nguyên Tắc Trùng Khớp Kỳ Hạn (Matched-Maturity Principle)
- Mọi hợp đồng khách hàng phát sinh đều được đối ứng với một mức giá điều chuyển nội bộ có **cùng kỳ hạn, cùng đồng tiền và cùng cơ sở lãi suất** [[src-choudhry-principles-banking#^choudhry-ftp-6]] [[src-choudhry-principles-banking#^choudhry-ftp-11]].
- Mức giá FTP này được **chốt cứng (locked-in) trong suốt vòng đời hợp đồng**, giúp cố định hoàn toàn Biên thương mại (Commercial Margin) cho Đơn vị Kinh doanh [[src-choudhry-principles-banking#^choudhry-ftp-7]] [[src-choudhry-principles-banking#^choudhry-ftp-8]]. Chi nhánh không phải lo lắng về việc lãi suất thị trường tăng hay giảm trong tương lai.

### B. Nguyên Tắc Cận Biên (Marginality Principle)
- Chi phí của các nguồn vốn đã huy động trong quá khứ (lãi suất bình quân gia quyền lịch sử — blended pool rate / WACF) **hoàn toàn không có giá trị** trong việc định giá các hợp đồng tín dụng mới [[src-choudhry-principles-banking#^choudhry-ftp-12]].
- Mọi khoản vay mới và tiền gửi mới bắt buộc phải được định giá dựa trên **chi phí cơ hội cận biên trên thị trường vốn tại chính thời điểm giao dịch phát sinh** (ex-ante marginal opportunity cost) [[src-choudhry-principles-banking#^choudhry-ftp-12]]. 
- Điều này ngăn chặn triệt để hiện tượng "trợ cấp chéo" (cross-subsidisation) nguy hiểm — nơi các khoản vay mới kém hiệu quả được bao cấp bởi các nguồn tiền gửi rẻ huy động từ nhiều năm trước [[src-choudhry-principles-banking#^choudhry-ftp-9]].

---

## 4. Tách Bạch Ba Nguồn Lợi Nhuận Của Ngân Hàng

Nhờ hệ thống FTP, toàn bộ Thặng dư Lãi ròng (Net Interest Margin — NIM) của ngân hàng được phân rã thành 3 cấu phần độc lập và minh bạch [[src-choudhry-principles-banking#^choudhry-ftp-13]]:

```
                +-------------------------------------------------------+
                |     TỔNG THẶNG DƯ LÃI RÒNG CỦA NGÂN HÀNG (TOTAL NIM)  |
                +-------------------------------------------------------+
                                           |
         +---------------------------------+---------------------------------+
         |                                 |                                 |
         v                                 v                                 v
[ BIÊN THƯƠNG MẠI CHO VAY ]       [ BIÊN TREASURY / ALM ]       [ BIÊN THƯƠNG MẠI TIỀN GỬI ]
   (Asset Commercial Margin)       (Treasury Mismatch Margin)     (Liability Commercial Margin)
       Lãi suất Cho vay              Lãi suất FTP Cho vay              Lãi suất FTP Tiền gửi
             TRỪ                               TRỪ                              TRỪ
     Lãi suất FTP Cho vay            Lãi suất FTP Tiền gửi              Lãi suất Tiền gửi
         (Cố định)                      (Chịu Rủi ro ALM)                    (Cố định)
```

1. **Biên Thương mại Cho vay (Asset Commercial Margin)**: Thể hiện năng lực của khối kinh doanh tín dụng trong việc đàm phán giá với khách hàng cao hơn chi phí thị trường vốn. Hoàn toàn phi rủi ro thị trường đối với đơn vị kinh doanh.
2. **Biên Thương mại Huy động (Liability Commercial Margin)**: Thể hiện giá trị thương quyền khách hàng và mạng lưới chi nhánh trong việc thu hút tiền gửi rẻ hơn chi phí đi vay bán buôn.
3. **Biên Quản trị Vốn (Treasury Margin)**: Là kết quả P&L thuần túy từ hoạt động quản trị chênh lệch kỳ hạn và vị thế thanh khoản tập trung tại Treasury. Mức lợi nhuận này phản ánh chính sách chấp nhận rủi ro (Risk Appetite) của ALCO và khả năng điều hành các công cụ phái sinh [[interest-rate-swap]] để bảo vệ giá trị kinh tế [[economic-value-of-equity|EVE]].

---

## 5. Mở Rộng Cơ Chế Truyền Dẫn và Phương Pháp Luận Định Giá Thực Chiến

Trong thực tế triển khai tại các Ngân hàng Thương mại Việt Nam và các mô hình ALM tối ưu hóa hiện đại:
- **Cơ chế truyền dẫn rủi ro đa chiều**: FTP không chỉ truyền dẫn rủi ro thanh khoản mà còn liên kết đồng thời đến rủi ro lãi suất (IRRBB) và rủi ro tín dụng / chi phí phân bổ vốn (RAROC). Xem chi tiết tại [[ftp-transmission-mechanism]] [[src-ftp-transmission-analysis#^ftp-trans-2]].
- **Phương pháp luận định giá chi tiết**: Cơ chế phân định biểu giá mua vốn VOF (Base curve + Margin + ALCO adjust) và biểu giá bán vốn COF (kèm chi phí dự trữ bắt buộc, bảo hiểm tiền gửi BHTG, đệm thanh khoản và đường cong hoàn trả Non-term Redemption Curve cho tiền gửi CASA). Xem chi tiết tại [[ftp-pricing-methodology]] [[src-vab-ftp#^vab-ftp-6]] [[src-vab-ftp#^vab-ftp-7]].
- **Động cơ tối ưu hóa bảng cân đối ALM**: Tích hợp các ràng buộc pháp định LCR, NSFR, LEV, CAR và hạn mức IRRBB vào bài toán tối ưu hóa NII / RAROC toàn ngân hàng. Xem chi tiết tại [[ftp-balance-sheet-optimization]] [[src-ftp-transmission-analysis#^ftp-trans-1]].

## Khái niệm và Liên kết
- [[ftp-transmission-mechanism]]: Cơ chế truyền dẫn FTP đến các yếu tố rủi ro.
- [[ftp-pricing-methodology]]: Phương pháp luận định giá VOF và COF thực chiến tại NHTM.
- [[ftp-balance-sheet-optimization]]: Tối ưu hóa bảng cân đối ALM toàn diện qua FTP.
- [[internal-risk-transfer]]: Cơ chế chuyển giao rủi ro nội bộ qua FTP.
- [[ftp-nature-and-balance-sheet-management]]: Bản chất, mục tiêu của FTP và các vấn đề cốt tử giải quyết trong quản trị bảng cân đối.
- [[synthetic-balance-sheet-liquidity-risk]]: Bảng cân đối thanh khoản tổng hợp.
- [[practical-alm-liquidity-governance]]: Khung quản trị thanh khoản thực chiến theo Choudhry.
- [[lcr]]: Tỷ lệ đảm bảo khả năng thanh khoản ngắn hạn.
- [[nsfr]]: Tỷ lệ nguồn vốn ổn định ròng dài hạn.

## Đề xuất cập nhật
- [2026-10-19] ingest src-tt83-2025-nhnn PL6 — chờ user duyệt: đã có node [[raroc]] (lợi nhuận trước thuế / vốn kinh tế theo TT83 PL6.III); đề xuất link ở lần nhắc đầu RAROC.
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO.
