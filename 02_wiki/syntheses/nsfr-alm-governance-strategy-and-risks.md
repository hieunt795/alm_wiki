---
title: "Phương pháp Quản trị Tác nghiệp, Cơ chế Điều hành ALCO, Chiến lược Tối ưu hóa và Khung Quản lý Rủi ro đối với NSFR tại ALM Treasury"
aliases: [Quản trị NSFR ALM Treasury, Chiến lược và Rủi ro NSFR, ALCO NSFR Governance]
type: synthesis
domains: [alm, basel]
status: active
maturity: draft
origin: query
question: "Khung quản trị tác nghiệp, cơ chế vận hành của ALCO, hệ thống hạn mức, cơ chế định giá Term Liquidity FTP, các chiến lược tối ưu hóa cấu trúc bảng cân đối, và những rủi ro cốt lõi đe dọa sự tuân thủ bền vững của tỷ lệ NSFR tại Khối ALM Treasury là gì?"
as_of: 2026-10-16
sources: ["[[src-bcbs-nsfr]]", "[[src-bcbs-lcr]]"]
relations:
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: measures, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf10-5]]"}

tags: [nsfr, alm-governance, alco, liquidity-ftp, risk-management, balance-sheet-strategy]
updated: 2026-10-16
reviewed:
---

## Câu hỏi
Khung quản trị tác nghiệp, cơ chế vận hành của Hội đồng Quản lý Tài sản - Nợ (ALCO), hệ thống hạn mức kiểm soát, cơ chế định giá điều chuyển vốn nội bộ (Term Liquidity FTP), các chiến lược tối ưu hóa cấu trúc bảng cân đối kế toán, và những rủi ro cốt lõi đe dọa sự tuân thủ bền vững của tỷ lệ [[nsfr]] tại Khối ALM Treasury được xác định và triển khai như thế nào?

## Kết luận
- **Trục điều phối chiến lược dài hạn**: Chuẩn mực Net Stable Funding Ratio ([[nsfr]]) không phải là một chỉ số tuân thủ pháp định tĩnh mà là **trục điều phối chiến lược (strategic orchestrator)** cho toàn bộ cấu trúc bảng cân đối kế toán của ngân hàng trong khoảng thời gian một năm [[src-bcbs-nsfr#^nsf20-1]] [[src-bcbs-nsfr#^nsf20-2]].
- **Hệ thống Quản trị Đa tầng tại ALCO**: Quản trị NSFR đòi hỏi ALCO phải vận hành hệ thống hạn mức cảnh báo sớm 3 tầng (*Traffic-Light Limits*), kết hợp với quy trình đánh giá an toàn thanh khoản nội bộ dài hạn (ILAAP) và kế hoạch tài trợ vốn có cấu trúc (*Structural Funding Plan*) [[src-bcbs-nsfr#^nsf10-5]] [[src-bcbs-nsfr#^nsf20-3]].
- **Cơ chế Định giá Vốn Nội bộ (Term Liquidity FTP)**: Là công cụ kinh tế hữu hiệu nhất để biến các quy định định tính của Basel thành hành vi kinh doanh cụ thể: Áp phí thanh khoản cấu trúc lên các khoản tài sản có [[required-stable-funding|RSF]] cao (65%–85%), đồng thời trả thưởng thanh khoản ổn định cho các khoản tiền gửi bán lẻ cốt lõi có [[available-stable-funding|ASF]] cao (90%–95%) [[src-bcbs-nsfr#^nsf30-11]] [[src-bcbs-nsfr#^nsf30-30]].
- **Bốn Chiến lược Tối ưu hóa Thực chiến**: Bao gồm (1) San bằng thang kỳ hạn nợ phát hành (*funding ladder smoothing*) nhằm xóa bỏ hiệu ứng vực thẳm kỳ hạn trôi (*cliff-edge rollovers*); (2) Tối ưu hóa danh mục tài sản bảo đảm (*collateral optimization*) ngăn ngừa bẫy cầm cố dài hạn; (3) Khai thác đòn bẩy kép của Trái phiếu Chính phủ Level 1 (HQLA 100% trong LCR nhưng chỉ ngốn RSF 5% trong NSFR); và (4) Tái cấu trúc hợp đồng hạn mức ngoại bảng.
- **Bốn Rủi ro Trọng yếu đe dọa NSFR**: Gồm rủi ro tái tài trợ kỳ hạn khi thị trường vốn đóng băng, rủi ro rút tiền kỹ thuật số làm sụp đổ giả định bám dính của tiền gửi cá nhân, rủi ro biến động ký quỹ phái sinh (Margin Calls), và rủi ro hạ bậc tín nhiệm (Downgrade Triggers).

## Cơ chế Vận hành và Quản trị ALCO

```
+-------------------------------------------------------------------------------+
|             KHUNG QUẢN TRỊ TÁC NGHIỆP NSFR TẠI ALM TREASURY VÀ ALCO           |
+-------------------------------------------------------------------------------+
                                        |
       +--------------------------------+--------------------------------+
       |                                                                 |
       v                                                                 v
+-------------------------------+                               +-------------------------------+
|      HỆ THỐNG HẠN MỨC         |                               |     CƠ CHẾ ĐỊNH GIÁ NỘI BỘ    |
|    ĐÈN TÍN HIỆU 3 TẦNG        |                               |       TERM LIQUIDITY FTP      |
+-------------------------------+                               +-------------------------------+
| - Green: NSFR >= 110% - 115%  |                               | - Áp phí RSF vào tài sản dài  |
|   (Vận hành an toàn)          |                               |   hạn (cho vay BĐS, DN).      |
| - Amber: 103% <= NSFR < 110%  |                               | - Thưởng ASF cho tiền gửi cốt |
|   (Cảnh báo sớm, hạn chế cho  |                               |   lõi bán lẻ (CASA, Term).    |
|   vay dài hạn mới)            |                               | - Triệt tiêu NIM của các gói  |
| - Red: 100% <= NSFR < 103%    |                               |   tín dụng ngắn hạn dựa vào   |
|   (Kích hoạt Structural CFP)  |                               |   vốn vay liên ngân hàng.     |
+-------------------------------+                               +-------------------------------+
                                        |
                                        v
+-------------------------------------------------------------------------------+
|             KẾ HOẠCH TÀI TRỢ CẤU TRÚC VÀ BẬC THANG PHÁT HÀNH NỢ (ILAAP)       |
|  - Dự báo động bảng cân đối kế toán theo chu kỳ 12 tháng.                    |
|  - Chia nhỏ các đợt phát hành trái phiếu dài hạn so le đều đặn các năm.        |
|  - Giám sát rào cản chuyển giao thanh khoản giữa các công ty con (Ring-fence). |
+-------------------------------------------------------------------------------+
```

### 1. Hệ thống Hạn mức Đèn tín hiệu 3 tầng (Traffic-Light Limit Framework)
Treasury không bao giờ vận hành NSFR ở sát mức sàn quy định $100\%$, vì một sự sụt giảm số dư tiền gửi bán buôn hoặc việc chuyển nhóm nợ xấu có thể đẩy tỷ lệ vi phạm ngưỡng pháp lý ngay lập tức [[src-bcbs-nsfr#^nsf20-2]] [[src-bcbs-nsfr#^nsf30-32]]. Hội đồng ALCO thiết lập 3 tầng đệm an toàn:
1. **Tầng Xanh (Green - Target Operating Zone: $\text{NSFR} \ge 110\%\text{–}115\%$)**:
   - Vùng hoạt động bình thường, các khối kinh doanh được phép giải ngân và phát triển tài sản tín dụng trung dài hạn theo kế hoạch kinh doanh đã phê duyệt.
2. **Tầng Vàng (Amber - Early Warning Zone: $103\% \le \text{NSFR} < 110\%$)**:
   - Vùng cảnh báo sớm. Kích hoạt quyền can thiệp của Giám đốc ALM:
     - Tăng phí Term Liquidity FTP đối với các khoản vay trung dài hạn mới để hãm tốc độ tăng trưởng mẫu số RSF.
     - Yêu cầu Khối Nguồn vốn tăng cường phát hành trái phiếu hoặc chứng chỉ tiền gửi kỳ hạn $\ge 1$ năm để bổ sung ASF 100% [[src-bcbs-nsfr#^nsf30-10]].
     - Tạm dừng các giao dịch repo tài sản HQLA có kỳ hạn trên 6 tháng nhằm tránh làm tăng hệ số RSF lên 50% hoặc 100% [[src-bcbs-nsfr#^nsf30-20]].
3. **Tầng Đỏ (Red - Recovery Zone: $100\% \le \text{NSFR} < 103\%$)**:
   - Vùng khẩn cấp. Hội đồng ALCO triệu tập phiên bất thường, kích hoạt Kế hoạch Tài trợ Dự phòng Vốn (Structural CFP):
     - Đóng băng toàn bộ hạn mức giải ngân tín dụng mới có kỳ hạn trên 1 năm.
     - Thực hiện hoán đổi danh mục tài sản: chuyển dịch các tài sản chịu RSF 85% sang tài sản Level 1 (RSF 5%) hoặc thanh lý tài sản unencumbered [[src-bcbs-nsfr#^nsf30-26]] [[src-bcbs-nsfr#^nsf30-31]].
     - Tăng lãi suất huy động tiền gửi cá nhân dài hạn nhằm hút dòng vốn ASF 95%–100% từ thị trường dân cư [[src-bcbs-nsfr#^nsf30-10]] [[src-bcbs-nsfr#^nsf30-11]].
4. **Vùng Vi phạm (Breach: $\text{NSFR} < 100\%$)**:
   - Ngân hàng lập tức phải báo cáo chính thức bằng văn bản cho Cơ quan Giám sát (NHNN / BCBS) nêu rõ nguyên nhân và đệ trình Kế hoạch Phục hồi Thanh khoản cấu trúc có cam kết thời hạn theo quy định [[src-bcbs-nsfr#^nsf20-2]] [[src-bcbs-nsfr#^nsf20-3]].

### 2. Cơ chế Định giá Điều chuyển Vốn Nội bộ (Term Liquidity FTP)
Cơ chế FTP là "cây gậy và củ cà rốt" của Treasury để định hướng bảng cân đối kế toán:
- **Biểu phí Phạt Tài sản (RSF Charge)**: Mỗi đồng tài sản được giải ngân sẽ bị ALM Treasury khấu trừ phí tài trợ vốn dài hạn:
  $$\text{FTP Charge}(\text{Asset}) = \text{Base Cost} + \Big(\text{RSF Factor} \times \text{Term Funding Spread}(\text{Tenor})\Big)$$
  - Ví dụ: Khoản cho vay doanh nghiệp dài hạn có $\text{RSF} = 85\%$ sẽ chịu phí thanh khoản cấu trúc bằng $85\% \times \text{Spread Trái phiếu 3 năm}$ [[src-bcbs-nsfr#^nsf30-31]].
  - Khoản cho vay mua nhà ở xã hội có $\text{RSF} = 65\%$ chỉ chịu phí bằng $65\% \times \text{Spread}$ [[src-bcbs-nsfr#^nsf30-30]].
  - Khoản đầu tư Trái phiếu Chính phủ Level 1 chỉ chịu phí bằng $5\% \times \text{Spread}$ [[src-bcbs-nsfr#^nsf30-26]].
- **Biểu thưởng Nguồn vốn (ASF Credit)**: Mỗi đồng tiền gửi huy động được sẽ được Treasury trả thưởng thanh khoản ổn định:
  - Tiền gửi bán lẻ stable (ASF 95%): Nhận thưởng tối đa nhờ giúp ngân hàng giảm thiểu chi phí phát hành trái phiếu quốc tế [[src-bcbs-nsfr#^nsf30-11]].
  - Tiền gửi liên ngân hàng $< 6$ tháng: Hưởng $\text{ASF Credit} = 0\%$, triệt tiêu hoàn toàn động lực của các chi nhánh huy động vốn liên ngân hàng ngắn hạn để báo cáo tăng trưởng tài sản [[src-bcbs-nsfr#^nsf30-14]].

---

## Bốn Chiến lược Tối ưu hóa Thực chiến tại ALM Treasury

### 1. Chiến lược San bằng Thang Kỳ hạn Nợ (Funding Ladder Smoothing)
- **Bản chất vấn đề**: Một khoản nợ dài hạn 1.000 tỷ VND phát hành kỳ hạn 3 năm (ASF 100%) khi trôi qua mốc 365 ngày sẽ bị tụt hệ số xuống 50% (mất 500 tỷ ASF), và khi chạm mốc 180 ngày sẽ tụt tiếp về 0% (mất tiếp 500 tỷ ASF) [[src-bcbs-nsfr#^nsf30-10]] [[src-bcbs-nsfr#^nsf30-13]] [[src-bcbs-nsfr#^nsf30-14]]. Hiện tượng này tạo ra các "hố đen" sụt giảm NSFR định kỳ.
- **Giải pháp Treasury**:
  - Thực hiện chiến lược chia nhỏ và phát hành so le (*laddering*): Thay vì phát hành 1 lô trái phiếu lớn 5.000 tỷ VND kỳ hạn 5 năm, Treasury phát hành chia đều thành các lô 1.000 tỷ VND với các kỳ hạn 2 năm, 3 năm, 4 năm, 5 năm.
  - Tái phát hành cuốn chiếu sớm (*Pre-funding rollover*): Bắt đầu kế hoạch phát hành lô trái phiếu mới để thay thế ngay khi khoản nợ cũ bước vào khoảng thời gian còn lại 15 tháng (trước khi trôi vào bucket 1 năm), triệt tiêu hoàn toàn cú sốc giảm tỷ lệ NSFR.

### 2. Quản trị Tài sản Thế chấp và Khung Cầm cố (Collateral & Encumbrance Optimization)
- **Bản chất vấn đề**: Đem tài sản đi cầm cố dài hạn $\ge 1$ năm sẽ biến một tài sản Level 1 (RSF 5%) thành tài sản chịu **RSF 100%** [[src-bcbs-nsfr#^nsf30-20]] [[src-bcbs-nsfr#^nsf30-26]].
- **Giải pháp Treasury**:
  - Phân bổ tài sản bảo đảm phân tầng (*Collateral Waterfall*): Khi cần huy động vốn có bảo đảm hoặc phát hành covered bonds dài hạn, Treasury luôn ưu tiên cầm cố các tài sản vốn dĩ đã có hệ số RSF cao sẵn (như các khoản vay thế chấp nhà ở có RSF 65% hoặc các khoản vay thương mại có RSF 85%) [[src-bcbs-nsfr#^nsf30-30]] [[src-bcbs-nsfr#^nsf30-31]].
  - Tuyệt đối bảo tồn trạng thái unencumbered cho Trái phiếu Chính phủ Level 1 để giữ mức RSF ở mức 5% [[src-bcbs-nsfr#^nsf30-26]].
  - Kiểm soát các điều khoản repo: Chỉ ký các hợp đồng repo có kỳ hạn dưới 6 tháng để bảo đảm tài sản Level 1 không bị nâng hệ số RSF lên 50% hoặc 100% [[src-bcbs-nsfr#^nsf30-20]].

### 3. Ma trận Tối ưu hóa Đồng thời LCR – NSFR (Đòn bẩy kép của Level 1)
- **Bản chất vấn đề**: Nhiều tài sản mang lại lợi suất cao nhưng ngốn quá nhiều nguồn vốn ổn định (RSF), trong khi một số tài sản cải thiện LCR nhưng lại không giúp ích cho NSFR.
- **Giải pháp Treasury**:
  - Khai thác tối đa Trái phiếu Chính phủ Level 1: Được tính 100% vào tử số LCR, đồng thời chỉ chịu $\text{RSF} = 5\%$ trong NSFR [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-nsfr#^nsf30-26]]. Đây là tài sản duy nhất mang lại hiệu quả đòn bẩy kép cho cả hai chỉ số thanh khoản của Basel.
  - Hạn chế nắm giữ tài sản Level 2B vượt mức: Level 2B bị chiết khấu tới 50% trong LCR và chịu tới 50% RSF trong NSFR [[src-bcbs-lcr#^lcr30-45]] [[src-bcbs-nsfr#^nsf30-29]]. Treasury chỉ nắm giữ Level 2B khi biên lợi suất tín dụng (*credit spread*) đủ lớn để bù đắp chi phí vốn ổn định phát sinh.

### 4. Tái cấu trúc Hạn mức Cam kết Ngoại bảng
- **Bản chất vấn đề**: Các hạn mức thanh khoản (Liquidity Facilities) cấp cho khách hàng vừa chịu rủi ro rút vốn cấp tính 30%–100% trong LCR [[src-bcbs-lcr#^lcr40-64]], vừa bị đánh thuế 5% RSF trên phần chưa rút trong NSFR [[src-bcbs-nsfr#^nsf30-34]].
- **Giải pháp Treasury**:
  - Hướng dẫn các khối kinh doanh tái cấu trúc hợp đồng tín dụng thành Hạn mức Vốn lưu động thông thường (*Credit Facilities*): Giảm tỷ lệ dòng ra LCR xuống còn 10% [[src-bcbs-lcr#^lcr40-64]].
  - Thu hồi các hạn mức cam kết cấp cho khách hàng không hoạt động hoặc không có giao dịch thực tế (*dormant commitments*) để giảm trực tiếp mẫu số RSF ngoại bảng [[src-bcbs-nsfr#^nsf30-34]].

---

## Bốn Rủi ro Trọng yếu đe dọa NSFR và Biện pháp Phòng ngừa

### 1. Rủi ro Tái tài trợ Kỳ hạn (Refinancing / Rollover Risk)
- **Bản chất rủi ro**: Ngân hàng phụ thuộc vào việc phát hành trái phiếu dài hạn để duy trì ASF 100%. Khi thị trường tài chính xảy ra khủng hoảng niềm tin hoặc suy thoái kinh tế, thị trường trái phiếu sơ cấp đóng băng. Các lô trái phiếu cũ đến hạn không thể tái phát hành, làm suy sụp tỷ lệ NSFR.
- **Biện pháp phòng ngừa**: Duy trì tỷ trọng tiền gửi bán lẻ cốt lõi (ASF 90%–95%) làm bệ đỡ vững chắc chiếm tối thiểu 60% tổng cơ cấu ASF; đa dạng hóa thị trường phát hành nợ sang các đồng tiền và nhà đầu tư khác nhau.

### 2. Rủi ro Rút tiền Kỹ thuật số (Digital Bank Run Risk)
- **Bản chất rủi ro**: Giả định của Basel gán cho tiền gửi bán lẻ không kỳ hạn hệ số ASF $90\%\text{–}95\%$ dựa trên tiền đề rằng người gửi tiền cá nhân có tính bám dính cao [[src-bcbs-nsfr#^nsf30-2]] [[src-bcbs-nsfr#^nsf30-11]]. Tuy nhiên, trong kỷ nguyên số, các ứng dụng Mobile Banking cho phép hàng chục nghìn khách hàng rút tiền đồng loạt trong vòng vài giờ khi có tin đồn lan truyền trên mạng xã hội.
- **Biện pháp phòng ngừa**: ALM Treasury phải tự xây dựng kịch bản Stress Test nội bộ với giả định suy giảm mạnh của tiền gửi bán lẻ (giả định ASF chỉ đạt 70%–80%) và xây dựng Kế hoạch Tài trợ Dự phòng khẩn cấp.

### 3. Rủi ro Biến động Ký quỹ và Giá trị Thị trường Phái sinh
- **Bản chất rủi ro**: Khi tỷ giá hoặc lãi suất biến động mạnh, các hợp đồng phái sinh bị thua lỗ định giá thị trường. Ngân hàng bị các đối tác và CCP gọi ký quỹ bổ sung (*margin calls*). Toàn bộ tiền mặt và chứng khoán đem ký quỹ ban đầu bị khóa vào hệ số **RSF 85%** [[src-bcbs-nsfr#^nsf30-31]], đồng thời tổng nợ phái sinh gộp tăng cao kéo theo khoản phạt add-on tăng vọt [[src-bcbs-nsfr#^nsf30-32]], làm phình to mẫu số RSF.
- **Biện pháp phòng ngừa**: Bàn giao dịch phái sinh phải thiết lập hạn mức dung sai rủi ro phơi bày phái sinh ròng; ký kết các phụ lục CSA cho phép sử dụng đa dạng tài sản bảo đảm và thiết lập ngưỡng chuyển tiền ký quỹ hợp lý.

### 4. Rủi ro Hạ bậc Tín nhiệm (Credit Downgrade Trigger Risk)
- **Bản chất rủi ro**: Khi ngân hàng bị các tổ chức xếp hạng tín nhiệm quốc tế (Moody's, S&P, Fitch) hạ bậc tín nhiệm:
  - Chi phí phát hành trái phiếu mới tăng vọt, triệt tiêu khả năng huy động vốn dài hạn (ASF 100%).
  - Các hợp đồng phái sinh và tài trợ có bảo đảm kích hoạt điều khoản cam kết phụ (*rating triggers*), buộc ngân hàng phải đặt cọc thêm tài sản bảo đảm, đẩy các tài sản unencumbered sang trạng thái encumbered (nâng RSF lên 100%) [[src-bcbs-nsfr#^nsf30-20]].
- **Biện pháp phòng ngừa**: Treasury luôn tính toán trước tác động của kịch bản hạ 1–3 bậc tín nhiệm lên mẫu số RSF trong quy trình ILAAP hàng năm.

---

## Bằng chứng Thực nghiệm & Bài học Điển hình

### 1. Thất bại Thanh khoản Cấu trúc của Silicon Valley Bank (SVB - 2023)
- SVB là ví dụ kinh điển về việc vi phạm nguyên lý cấu trúc của NSFR:
  - Về phía tài sản: SVB đầu tư ồ ạt hơn 120 tỷ USD vào danh mục chứng khoán nợ và trái phiếu thế chấp nhà ở dài hạn (HTM/AFS) có kỳ hạn 10–30 năm (tương ứng với các tài sản chịu RSF 65%–85% trong NSFR).
  - Về phía nguồn vốn: Thay vì tài trợ bằng nợ dài hạn (ASF 100%) hoặc tiền gửi bán lẻ được bảo hiểm (ASF 95%), SVB lại tài trợ danh mục trên bằng tiền gửi không kỳ hạn của các doanh nghiệp công nghệ và quỹ đầu tư mạo hiểm (vốn chỉ nhận ASF 50% hoặc 0% nếu là định chế tài chính) [[src-bcbs-nsfr#^nsf30-13]] [[src-bcbs-nsfr#^nsf30-14]].
  - Kết quả: Khi lãi suất tăng, giá trị thị trường của danh mục trái phiếu bốc hơi, người gửi tiền bán buôn rút hàng chục tỷ USD trong 48 giờ. Bảng cân đối của SVB sụp đổ hoàn toàn do sự chênh lệch kỳ hạn cấu trúc cực đoan. Nếu SVB bị bắt buộc tuân thủ chuẩn mực NSFR từ trước, ngân hàng này đã không thể mở rộng quy mô danh mục tài sản dài hạn mà không phát hành nợ dài hạn tương ứng.

---

## Bất định & Hàm ý Triển khai tại Việt Nam

- **Lộ trình Tuân thủ theo Thông tư 50/2026/TT-NHNN**:
  - Điều 13.1 của TT50 quy định thời hạn bắt buộc áp dụng tỷ lệ NSFR đối với các ngân hàng thương mại Việt Nam bắt đầu từ ngày **01/10/2028**.
  - Các NHTM Việt Nam đang đứng trước bài toán chuyển dịch lớn:
    1. *Chuẩn hóa Hệ thống Dữ liệu Hợp đồng*: Bóc tách chính xác kỳ hạn còn lại, điều khoản call option và các khoản phạt rút tiền trước hạn của tiền gửi dân cư [[src-bcbs-nsfr#^nsf30-7]] [[src-bcbs-nsfr#^nsf30-10]].
    2. *Tách bạch Nguồn vốn Doanh nghiệp và Định chế Tài chính*: Phân loại chuẩn xác tiền gửi của các công ty bảo hiểm, chứng khoán, quỹ đầu tư (để áp đúng ASF 0% nếu kỳ hạn $< 6$ tháng) với tiền gửi của doanh nghiệp sản xuất kinh doanh thông thường (ASF 50%) [[src-bcbs-nsfr#^nsf30-13]] [[src-bcbs-nsfr#^nsf30-14]].
    3. *Hiệu chỉnh Mô hình FTP Nội bộ*: Chuyển đổi từ mô hình FTP thanh khoản ngắn hạn đơn thuần sang mô hình Term Liquidity FTP đa kỳ hạn, đưa hệ số RSF vào công thức tính toán lợi nhuận sau điều chỉnh rủi ro (RAROC) của từng chi nhánh và từng sản phẩm tín dụng.
