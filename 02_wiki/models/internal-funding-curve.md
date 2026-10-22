---
title: "Internal funding curve"
aliases: [Internal Funding Curve, Internal yield curve, Internal COF curve, Internal cost of funds curve, Đường cong vốn nội bộ, Đường cong lợi suất nội bộ, Đường cong chi phí vốn nội bộ]
type: model
domains: [alm, product]
status: active
maturity: draft
sources: ["[[src-choudhry-principles-banking]]", "[[src-vab-ftp]]", "[[src-bardaeva-alm]]"]
relations:
  - {type: input-to, to: "[[funds-transfer-pricing]]", cite: "[[src-choudhry-principles-banking#^choudhry-ifc-9]]"}
  - {type: input-to, to: "[[loan-pricing]]", cite: "[[src-choudhry-principles-banking#^choudhry-ifc-10]]"}
  - {type: input-to, to: "[[raroc]]", cite: "[[src-choudhry-principles-banking#^choudhry-ifc-1]]"}
tags: [ftp, ftp-curve, internal-curve, cost-of-funds, tlp, yield-curve, model]
updated: 2026-10-21
reviewed:
---

## Mục tiêu

- Internal funding curve (internal cost of funds curve, COF curve) là đường cong lãi suất nội bộ mà ngân hàng dùng để định giá và quản trị rủi ro. Đường cong này dẫn dắt phân bổ nguồn lực, định giá giao dịch của business line, dựng hedge và phân tích RAROC [[src-choudhry-principles-banking#^choudhry-ifc-1]].
- Choudhry coi việc chọn phương pháp dựng đường cong là một quyết định quản trị rủi ro quan trọng. Ngân hàng nên nêu quy trình dựng COF curve trong một văn bản chính sách chính thức [[src-choudhry-principles-banking#^choudhry-ifc-1]].
- Đường cong nội bộ là công cụ quản trị rủi ro của Treasury. Thay đổi lãi suất tác động trực tiếp lên NII, và một đường cong chính xác, công bằng là điều kiện cho định giá và [[funds-transfer-pricing]] [[src-choudhry-principles-banking#^choudhry-ifc-9]].

## Công thức

**Quy trình 4 bước theo no-arbitrage (Choudhry).** Logic no-arbitrage yêu cầu rút đường cong định giá rủi ro của ngân hàng từ giá thị trường, vì giá thị trường quyết định lãi suất ngân hàng huy động được. Ngân hàng nên dùng COF curve của chính mình khi định giá sản phẩm khách hàng [[src-choudhry-principles-banking#^choudhry-ifc-2]]. Thông lệ tốt là nội suy trên lợi suất nợ đã phát hành của chính ngân hàng để rút discount function [[src-choudhry-principles-banking#^choudhry-ifc-3]]. Quy trình [[src-choudhry-principles-banking#^choudhry-ifc-4]]:
1. Fit phương pháp đã chọn vào dữ liệu thị trường [[src-choudhry-principles-banking#^choudhry-ifc-4]].
2. Rút risky yield curve của ngân hàng. Đây là đường cong xác định coupon cố định của trái phiếu ngân hàng phát hành ngang giá [[src-choudhry-principles-banking#^choudhry-ifc-4]].
3. Dùng discount function liên tục từ bước 2 để dựng par-par asset swap curve [[src-choudhry-principles-banking#^choudhry-ifc-4]].
4. Lấy đường cong này làm TLP curve hàm ý thị trường (term liquidity premium trên swap rate), tức spread của FRN ngân hàng phát hành ngang giá [[src-choudhry-principles-banking#^choudhry-ifc-4]].

TLP curve ở bước 4 là baseline pricing curve của ngân hàng và là gốc để dựng mọi cross-currency funding curve [[src-choudhry-principles-banking#^choudhry-ifc-4]]. TLP curve là đường cong unsecured [[src-choudhry-principles-banking#^choudhry-ifc-5]].

**Bốn cách dựng FTP curve.** Ban đầu chỉ có market, cost và mixed approach. Marginal approach được bổ sung sau, do hướng dẫn của cơ quan quản lý [[src-choudhry-principles-banking#^choudhry-ifc-16]].

| Cách | Cấu tạo | Ưu điểm | Hạn chế | Nguồn |
|---|---|---|---|---|
| Cost | Dựa trên lãi suất huy động đã trả | Áp được khi thị trường ổn định, cấu trúc nợ đa dạng theo kỳ hạn | Phụ thuộc lãi suất quá khứ, phản ứng trễ; đường cong méo do các kỳ hạn huy động ở thời điểm khác nhau; khi thừa nguồn không điều tiết được khối lượng tiền gửi | [[src-choudhry-principles-banking#^choudhry-ifc-17]] |
| Market | Lãi suất đặt vốn hoặc vay thay thế trên thị trường | Khách quan, minh bạch; có FTP rate cả ở kỳ hạn không có khoản mục; đường cong trơn | Chỉ báo thị trường tiền tệ biến động mạnh; thiếu chỉ báo trung dài hạn; giao dịch trái phiếu chính phủ ít; thiếu dữ liệu cho mô hình hoá | [[src-choudhry-principles-banking#^choudhry-ifc-18]] |
| Mixed | Market curve trộn với đường cong chi phí thực tế của nợ, theo tỷ trọng nguồn vốn ổn định từng bucket (3 bước) | Phản ánh cơ cấu nợ theo kỳ hạn | [cần nguồn] | [[src-choudhry-principles-banking#^choudhry-ifc-19]] |
| Marginal | Cấu phần thị trường cho chi phí vốn ngắn hạn cơ sở + spread riêng của ngân hàng phản ánh chi phí thanh khoản theo kỳ hạn | Bám mức lãi suất thị trường, phản ứng khá nhanh, có FTP rate ở kỳ hạn không có nợ | Chủ quan; giảm được khi core liabilities đa dạng | [[src-choudhry-principles-banking#^choudhry-ifc-20]] |

Core liabilities dùng cho marginal approach phải thoả 3 tiêu chí: khối lượng nhạy với lãi suất, đủ lớn so với nhu cầu tài trợ, cấu trúc từng nguồn ổn định [[src-choudhry-principles-banking#^choudhry-ifc-20]].

*Diễn giải:* hai khái niệm "term liquidity premium" trong Choudhry khác nhau. Ở lý thuyết đường cong, đó là phần bù thanh khoản chung của thị trường cho kỳ hạn dài ([[term-structure-theories]]). Ở internal funding curve, đó là spread riêng của ngân hàng trên swap rate. Node [[liquidity-transfer-pricing]] dùng nghĩa thứ hai.

## Inputs & giả định

- **Loại đường cong dựng được**: swap curve, implied yield curve, zero-coupon yield curve. Chỉ dùng lãi suất cùng lớp tổ chức phát hành hoặc cùng mức thanh khoản. Sau khủng hoảng 2007–2008, vanilla IRS curve không còn dùng làm lãi suất tham chiếu; thay vào đó dùng OIS curve dựa trên swap có tài sản bảo đảm [[src-choudhry-principles-banking#^choudhry-ifc-12]]. Xem [[overnight-index-swap]].
- **Đầu vào khi thiếu thị trường thứ cấp**: phương pháp nội suy trên nợ của chính ngân hàng cần trái phiếu ngân hàng có thị trường thứ cấp thanh khoản; không có thì dùng proxy [[src-choudhry-principles-banking#^choudhry-ifc-3]].
- **Synthetic curve cho thị trường mới nổi**: khi thiếu swap và trái phiếu kỳ hạn dài, giải pháp tối ưu là dựng synthetic yield curve từ công thức implied yield và FX forward (có thể là NDF). Đầu vào: IRS của thị trường phát triển (ví dụ USD) theo kỳ hạn, FX spot và FX forward của nội tệ so với ngoại tệ mạnh [[src-choudhry-principles-banking#^choudhry-ifc-13]]. Công thức bị mất khi convert nên không trích.
- **Phương pháp tham số**: ngân hàng trung ương dựng zero-coupon curve từ trái phiếu chính phủ bằng spline hoặc Nelson–Siegel, Svensson. Dựng từ trái phiếu ngân hàng ngang hàng: OLS không dựng được đoạn dài nếu thiếu lãi suất tham chiếu; Nelson–Siegel cần đoán tham số ban đầu [[src-choudhry-principles-banking#^choudhry-ifc-14]].
- **Chân trời**: ngân hàng dựng đường cong discount factor cho mọi kỳ hạn, dài ít nhất bằng kỳ hạn dài nhất của sản phẩm trên bảng cân đối; ví dụ OIS zero curve EUR, USD, GBP dựng bằng bootstrapping trên €STER, SOFR, SONIA [[src-choudhry-principles-banking#^choudhry-ifc-23]].
- **Nguyên tắc EBA (CEBS 2010)**: 4 nguyên tắc nên tuân thủ [[src-choudhry-principles-banking#^choudhry-ifc-15]]:
  - transfer price phản ánh điều kiện thị trường gần đây và kỳ vọng gần;
  - giá nội bộ khớp giá giao dịch wholesale khi có;
  - điều chỉnh trên base curve phản ánh đặc thù tổ chức hoặc công cụ;
  - giá nội bộ phản ánh marginal cost of funding.
- Ngân hàng chỉ huy động từ tiền gửi khách hàng và không phát hành vốn wholesale có thể nới một phần các nguyên tắc trên [[src-choudhry-principles-banking#^choudhry-ifc-15]].

## Calibration

- **Làm trơn**: cơ quan quản lý lo ngại đường cong vốn công khai lệch giá thị trường. Ngân hàng nên có quy trình làm trơn, dùng trung bình trượt 14 hoặc 30 ngày; khi biến động cực mạnh có thể đổi sang 60 ngày. Quyết định này thuộc cấp cao, thực tế là [[alco]] hoặc tiểu ban ALCO [[src-choudhry-principles-banking#^choudhry-ifc-6]].
- **Syndicated loan**: ngân hàng có thể đặt TLP cho khoản vay ở mức trung bình trượt 3 tháng, cập nhật hằng quý, do thời gian thu xếp dài [[src-choudhry-principles-banking#^choudhry-ifc-7]].
- **Ngoại suy và độ lệch**: mô hình ngoại suy khi kỳ hạn dài nhất của trái phiếu đã phát hành ngắn hơn kỳ hạn cần dựng. Một điểm kỳ hạn được lệch khỏi giá hàm ý thị trường quá dung sai trong quy trình nếu có business case cụ thể [[src-choudhry-principles-banking#^choudhry-ifc-5]].
- **Theo quy mô ngân hàng (Table 4.1)** [[src-choudhry-principles-banking#^choudhry-ifc-21]]:

| | Thị phần lớn | Thị phần nhỏ | Nguồn |
|---|---|---|---|
| Giải pháp | Đường cong phản ánh mọi yêu cầu quản lý và quyền chọn của sản phẩm; cần mô hình và IT riêng cho sản phẩm không kỳ hạn; mô hình thống kê cho optionality | Học theo ngân hàng lớn; mô hình dựa trên giả định có căn cứ do thiếu dữ liệu; tính tay từng giao dịch, minh bạch | [[src-choudhry-principles-banking#^choudhry-ifc-21]] |

- **Theo thị trường (Table 4.2)** [[src-choudhry-principles-banking#^choudhry-ifc-22]]:

| | Thị trường phát triển | Thị trường mới nổi | Nguồn |
|---|---|---|---|
| Môi trường | Thừa thanh khoản, lãi suất thấp hoặc âm; khách hàng gắn bó trọn đời với ngân hàng | Lạm phát cao, lãi suất cao, biến động mạnh; xã hội lo âu, niềm tin vào ngân hàng thấp | [[src-choudhry-principles-banking#^choudhry-ifc-22]] |
| Giải pháp | Nhiều khả năng dựng đường cong; áp được cho sản phẩm có quyền chọn ẩn; tài khoản tiết kiệm bán lẻ làm core liabilities; dùng được mô hình hành vi | Khả năng hạn chế; dùng cách đơn giản (implied yield curve và FX forward); có thể bỏ tách liquidity cost và base cost; tính tới biến động thị trường cao | [[src-choudhry-principles-banking#^choudhry-ifc-22]] |

## Output & usage
- Regulatory: PRA và EBA, khi rà soát chính sách FTP, nhấn mạnh cần một đường cong định giá nhất quán cho mọi business line, duy trì bám giá thị trường [[src-choudhry-principles-banking#^choudhry-ifc-8]]. Case study 1 của Choudhry: năm 2010, cơ quan quản lý Anh nêu rủi ro đường cong vốn công khai lệch giá thị trường và chênh lệch lãi suất nội bộ giữa Group và wholesale banking, vì ALM desk của mảng wholesale không dựng đường cong bằng phương pháp nội suy thông lệ tốt [[src-choudhry-principles-banking#^choudhry-cs-1]]. Group Treasury xử lý bằng một quy trình trung lập, thông qua ALCO [[src-choudhry-principles-banking#^choudhry-cs-2]].
- Management:
  - **Khoản vay**: đường cong cho FTP rate theo kỳ hạn và đồng tiền của khoản vay. FTP rate là giá tham chiếu cho giao dịch mới và là cơ sở tính gross margin, net margin (sau expected loss và dự phòng) và SVA [[src-choudhry-principles-banking#^choudhry-ifc-10]]. Xem [[loan-pricing]].
  - **Tiền gửi**: FTP rate theo nhu cầu thanh khoản từng kỳ hạn tác động tới quyết định huy động. Tiền gửi mới nên được gán FTP rate để tính gross margin (FTP rate trừ lãi suất tiền gửi). Loại tiền gửi cung cấp lượng vốn về lý thuyết không giới hạn có thể dùng để xác định FTP curve tương lai. Tác động lan sang P&L, CAR, RoE và CoC [[src-choudhry-principles-banking#^choudhry-ifc-11]].
  - Ở thị trường kém phát triển, Bardaeva cũng ghi khả năng dựng đường cong nội bộ hạn chế và có thể áp cách đơn giản hơn [[src-bardaeva-alm#^ch14-16]].

## Hạn chế & validation

- Cách nội suy trên nợ của chính ngân hàng cần thị trường thứ cấp thanh khoản [[src-choudhry-principles-banking#^choudhry-ifc-3]].
- Hạn chế của từng cách dựng: xem bảng ở mục Công thức.
- Công thức implied yield của synthetic curve chưa có trong wiki do lỗi convert [cần nguồn].

*Diễn giải (góc nhìn VN):* phương pháp luận FTP của VAB dựng đường cong cơ sở VND từ lãi suất huy động tiền gửi VND thực tế bình quân 3 tháng liền kề [[src-vab-ftp#^vab-ftp-41]], nội suy hoặc ngoại suy tuyến tính cho kỳ hạn thiếu thông số [[src-vab-ftp#^vab-ftp-42]]. Theo phân loại của Choudhry, cách này gần cost approach, có trung bình trượt 3 tháng tương tự quy trình làm trơn. Đường cong USD của VAB dùng lãi suất tham chiếu thị trường (SOFR, đường cong IRS USD) [[src-vab-ftp#^vab-ftp-41]], gần market approach. Đường cong thị trường 2 của VAB tính hằng ngày từ mid-rate của các ngân hàng TMCP tham chiếu hoặc từ VNIBOR [[src-vab-ftp#^vab-ftp-52]], cũng gần market approach. Ngân hàng VN không có trái phiếu phát hành với thị trường thứ cấp thanh khoản thì không áp được quy trình no-arbitrage 4 bước, và rơi vào nhóm "thị trường mới nổi" của Table 4.2.
