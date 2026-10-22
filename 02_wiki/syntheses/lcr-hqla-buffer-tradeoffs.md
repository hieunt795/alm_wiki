---
title: "LCR: đánh đổi giữa quy mô HQLA, chi phí đệm, NIM và rủi ro lãi suất"
aliases: [HQLA buffer trade-offs, Đánh đổi quy mô HQLA và NIM, Liquidity buffer cost và khả năng sử dụng HQLA]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Đánh giá xung đột giữa quy mô HQLA, liquidity buffer cost, NII/NIM, interest rate risk và khả năng sử dụng HQLA trong stress."
as_of: 2026-10-22
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]", "[[src-tt83-2025-nhnn]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-bcbs-liquidity-principles-2008]]"]
relations: []
tags: [lcr, hqla, buffer-cost, negative-carry, nim, irrbb, buffer-usability, research]
updated: 2026-10-22
reviewed:
---

## Câu hỏi
Thuộc bộ "Liquidity Risk — LCR & HQLA" (7 câu). Cụm này trả lời:
- **Q6.** Đánh giá xung đột giữa quy mô HQLA, liquidity buffer cost, NII/NIM, interest rate risk và khả năng sử dụng HQLA trong stress.

Tham số HQLA (Q3) ở [[lcr-hqla-and-funding-run-off-characteristics]]; tác động biên và biện pháp (Q5, Q7) ở [[lcr-model-marginal-impact-and-alm-levers]].

Node dùng, đều ở maturity `draft`: [[hqla]], [[level-1-assets]], [[net-interest-margin]], [[liquidity-transfer-pricing]], [[lcr]], [[government-bond-holding-ratio]], [[banking-book]].

## Kết luận
- **Quy mô HQLA ↔ NII/NIM.** HQLA thường có lợi suất thấp hơn chi phí vốn dài hạn dùng để tài trợ nó. Trong ví dụ ChoudWest của Choudhry, tăng đệm £1,5bn với net cost of carry 3% làm NII giảm £45m và NIM giảm 0,50 điểm % [[src-choudhry-principles-banking#^choudhry-nim-5]]. Resti (2011), do Lubinska dẫn, cho rằng LCR và NSFR làm giảm lợi nhuận ngân hàng vì phải kéo dài kỳ hạn huy động và giữ đệm HQLA [[src-lubinska-alm-optimisation#^lubinska-u02-18]].
- **Buffer cost.** BCBS 144 yêu cầu chi phí thanh khoản được đưa vào định giá nội bộ và duyệt sản phẩm mới, để mỗi mảng chịu đúng rủi ro thanh khoản mình tạo ra [[src-bcbs-liquidity-principles-2008#^lrm-p04]]. Choudhry gán chi phí đó cho đơn vị tạo tài sản qua FTP [[src-choudhry-principles-banking#^choudhry-ftp-15]].
- **HQLA ↔ rủi ro lãi suất.** Level 1 và Level 2A được đo theo current market value [[src-bcbs-lcr#^lcr30-40]] [[src-bcbs-lcr#^lcr30-43]]. Supervisor có thể đặt haircut cho Level 1 dựa trên độ nhạy lãi suất [[src-bcbs-lcr#^lcr30-40]]; NHNN có quyền tương tự với cả ba cấp [[src-tt50-2026-nhnn#^pl1-a2-2]]. Bằng chứng về chiều tác động lên IRR chưa thống nhất: một nghiên cứu ngân hàng nhỏ Ý thấy điều chỉnh thanh khoản theo Basel III đồng thời giảm IRR [[src-lubinska-alm-optimisation#^lubinska-u02-18]]. Wiki chưa có nguồn định lượng tác động của danh mục HQLA lên EVE [cần nguồn].
- **Khả năng sử dụng trong stress.** Basel cho phép dùng HQLA và xuống dưới 100% trong stress [[src-bcbs-lcr#^lcr20-5]]. TT50 coi LCR dưới ngưỡng là vi phạm, kèm biện pháp tự xử lý, báo cáo hằng ngày và xử phạt hành chính [[src-tt50-2026-nhnn#^d17-2]] [[src-tt50-2026-nhnn#^d17-2a]]. Khác biệt này làm phần HQLA thực sự dùng được ở VN là phần vượt ngưỡng lộ trình.

## Cơ chế

### Q6 — Bốn xung đột quanh danh mục HQLA

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[hqla]] | drives | [[lcr]] | + | [[src-bcbs-lcr#^lcr20-1]] |
| [[hqla]] | drives | [[net-interest-margin]] | − | [[src-choudhry-principles-banking#^choudhry-nim-5]] |
| [[liquidity-transfer-pricing]] | priced-by | [[lcr]] | | [[src-choudhry-principles-banking#^choudhry-ftp-15]] |
| [[government-bond-holding-ratio]] | limits | [[government-bond-holdings]] | | [[src-tt50-2026-nhnn#^d28-1]] |
| [[hqla]] | drives | [[economic-value-of-equity]] | | [cần nguồn] |

**1. Quy mô HQLA và NII/NIM (negative carry).**
- Ví dụ ChoudWest, kịch bản 2: tài sản trong đệm có lợi suất 4,5%, thấp hơn chi phí vốn dài hạn 7,5%, nên net cost of carry là 3%. Tài sản sinh lãi tăng £1,5bn lên £17,5bn; NII giảm £45m còn £416m; NIM giảm 0,50 điểm % còn 2,38% [[src-choudhry-principles-banking#^choudhry-nim-5]].
- *Diễn giải:* NIM chịu hai tác động cùng chiều: tử số NII giảm vì carry âm, mẫu số tài sản sinh lãi tăng vì đệm được tài trợ thêm. Nếu đệm được tạo bằng cách đổi tài sản có sẵn (không tăng bảng cân đối), chỉ còn tác động carry.
- Choudhry: quy mô HQLA book tối thiểu do khẩu vị rủi ro stress thanh khoản trong RAS và stress test ILAAP quyết định, có LCR và Survival Days làm hướng dẫn [[src-choudhry-principles-banking#^choudhry-tig-2]]. Quy mô LAB trước hết do LCR và mức LCR tối thiểu ngân hàng tự đặt trên 100% quyết định [[src-choudhry-principles-banking#^choudhry-lab-3]].

**2. Liquidity buffer cost và phân bổ.**
- BCBS 144 P4: chi phí, lợi ích, rủi ro thanh khoản nên vào định giá nội bộ, đo hiệu quả và duyệt sản phẩm mới [[src-bcbs-liquidity-principles-2008#^lrm-p04]]. Phân bổ nên xét thời gian nắm giữ dự kiến, thanh khoản thị trường của tài sản, và lợi ích của nguồn vốn ổn định như một số loại tiền gửi bán lẻ [[src-bcbs-liquidity-principles-2008#^lrm-19b]]. Chi phí nên được định lượng có xét điều kiện stress [[src-bcbs-liquidity-principles-2008#^lrm-20]].
- Choudhry CS6: số dư rút ngay chịu chi phí đệm dòng ra LCR cao nhất nên có giá trị thấp nhất với ngân hàng [[src-choudhry-principles-banking#^choudhry-cs-20]].
- *Diễn giải:* chi phí đệm của một sản phẩm nợ xấp xỉ bằng (run-off rate × net cost of carry) trên mỗi đồng số dư. Với run-off 40% và carry 3%, chi phí xấp xỉ 1,2%/năm; với 5% thì xấp xỉ 0,15%/năm (số học từ hệ số [[src-tt50-2026-nhnn#^pl1-b3]], [[src-tt50-2026-nhnn#^pl1-b2]] và carry của ví dụ ChoudWest; không phải số liệu VN).

**3. HQLA và rủi ro lãi suất.**
- HQLA phải ít nhạy với lãi suất và rủi ro thị trường [[src-bcbs-lcr#^lcr30-6]]. Level 1 và Level 2A đo theo current market value [[src-bcbs-lcr#^lcr30-40]] [[src-bcbs-lcr#^lcr30-43]]; TT50 lấy số dư theo giá thị trường hoặc mark-to-model [[src-tt50-2026-nhnn#^pl1-a5]].
- Ngân hàng được phòng ngừa rủi ro thị trường của HQLA mà vẫn tính vào stock; giá trị phải trừ chi phí đóng phòng ngừa trước hạn [[src-bcbs-lcr#^lcr30-19]] [[src-tt50-2026-nhnn#^d20-2dd]].
- Tại VN, giao dịch mua bán tài sản tài chính để dự trữ thanh khoản thuộc sổ ngân hàng [[src-tt83-2025-nhnn#^d3-33]]. Vì vậy danh mục này nằm trong phạm vi IRRBB ([[banking-book]]).
- Bằng chứng trái chiều: Baldan, Zen và Rebonato (do Lubinska dẫn) thấy điều chỉnh thanh khoản theo Basel III đồng thời giảm IRR ở một ngân hàng nhỏ Ý giai đoạn 2009–2010 [[src-lubinska-alm-optimisation#^lubinska-u02-18]].
- *Diễn giải:* hướng tác động lên IRRBB tuỳ cách tạo đệm. Kéo dài kỳ hạn huy động để tài trợ HQLA ngắn hạn làm giảm mismatch. Mua trái phiếu chính phủ dài hạn cố định để tăng lợi suất đệm làm tăng duration của tài sản. Wiki chưa có nguồn định lượng hai trường hợp này (ngoài wiki, chưa có nguồn).

**4. Khả năng sử dụng HQLA trong stress.**
- Basel: ngưỡng ≥ 100% áp liên tục khi không có stress; khi stress, dùng HQLA và xuống dưới mức tối thiểu là "entirely appropriate" [[src-bcbs-lcr#^lcr20-5]]. Supervisor nên cho phép phản ứng có phân biệt [[src-bcbs-lcr#^lcr20-6]], xét nguyên nhân, cú sốc riêng hay toàn thị trường, quy mô và thời gian giảm [[src-bcbs-lcr#^lcr20-6b]].
- BCBS 144 P12: đệm tài sản thanh khoản cao không bị cầm cố là bảo hiểm trước nhiều kịch bản stress [[src-bcbs-liquidity-principles-2008#^lrm-p12]].
- Định kỳ monetise một phần danh mục để kiểm tra khả năng tiếp cận thị trường và giảm rủi ro phát tín hiệu tiêu cực khi stress [[src-bcbs-lcr#^lcr30-15]] [[src-choudhry-principles-banking#^choudhry-lab-4]].
- VN: vi phạm LCR quy VNĐ riêng lẻ kéo theo biện pháp tự xử lý ngay, giám sát tăng cường khi dùng biện pháp từ 10% giá trị HQLA đủ điều kiện trở lên, báo cáo hằng ngày [[src-tt50-2026-nhnn#^d17-2]], xử phạt vi phạm hành chính [[src-tt50-2026-nhnn#^d17-2a]]. HQLA đủ điều kiện dưới 90% mức phải đáp ứng trong 30 ngày liên tục là nguy cơ mất khả năng chi trả [[src-tt50-2026-nhnn#^d18-1]].
- *Diễn giải:* LCR20.5 coi đệm là để dùng. TT50 biến ngưỡng thành sàn phải giữ, nên ngân hàng VN có động cơ duy trì đệm trên ngưỡng, và chỉ phần trên ngưỡng mới thực sự dùng được mà không vi phạm. Khoảng đệm này là chi phí carry cộng thêm, do khác biệt quy định tạo ra.

**Ràng buộc riêng của VN với danh mục cấp 1.** Ngân hàng chỉ được mua, nắm giữ, đầu tư TPCP và trái phiếu được Chính phủ bảo lãnh tối đa 30% Tổng Nợ phải trả bình quân tháng liền kề trước [[src-tt50-2026-nhnn#^d28-1]]. Đây cũng là các tài sản cấp 1 [[src-tt50-2026-nhnn#^pl1-a2]]. *Diễn giải:* phần HQLA vượt trần này chỉ có thể là tiền mặt và tiền gửi NHNN, thường có lợi suất thấp hơn TPCP, nên chi phí carry tăng khi LCR mục tiêu cao (ngoài wiki, chưa có nguồn về lợi suất).

## Bằng chứng ủng hộ
- Choudhry (T4) có ví dụ số về tác động âm của đệm lên NII và NIM [[src-choudhry-principles-banking#^choudhry-nim-5]]. Resti (2011), do Lubinska (T4) dẫn, đưa ra nhận định cùng chiều [[src-lubinska-alm-optimisation#^lubinska-u02-18]].
- BCBS 144 (T2) yêu cầu phân bổ chi phí thanh khoản tường minh [[src-bcbs-liquidity-principles-2008#^lrm-p04]] [[src-bcbs-liquidity-principles-2008#^lrm-19]].

## Bằng chứng trái chiều
- Về IRR: điều chỉnh thanh khoản theo Basel III đồng thời giảm IRR ở một ngân hàng nhỏ Ý [[src-lubinska-alm-optimisation#^lubinska-u02-18]]. Bằng chứng này đi ngược giả định "HQLA làm tăng duration" và chỉ dựa trên một nghiên cứu được dẫn lại (T4, nguồn thứ cấp).
- Các bằng chứng về NIM đều là ví dụ minh hoạ hoặc nhận định, không có dữ liệu ngân hàng VN.

## Phụ thuộc regime
- **Lãi suất tăng (rising_rate).** HQLA đo theo market value nên giá trái phiếu giảm làm giảm tử số [[src-bcbs-lcr#^lcr30-40]]; chiều tác động lên carry tuỳ tốc độ tái định giá của nguồn vốn [cần nguồn].
- **Stress.** Basel cho dùng đệm [[src-bcbs-lcr#^lcr20-5]]; TT50 coi dưới ngưỡng là vi phạm [[src-tt50-2026-nhnn#^d17-2]].
- **Lộ trình VN.** Ngưỡng 50% năm 2028 tăng lên 100% năm 2033 [[src-tt50-2026-nhnn#^d16-1c]], nên chi phí carry để giữ đúng ngưỡng tăng dần theo năm.

## Hàm ý ALM / quy định
- **Nghĩa vụ NHNN.** Ngưỡng LCR theo lộ trình, xử lý vi phạm Đ17, trần 30% TPCP Đ28. Basel LCR20.5–20.6 là tham chiếu; tại VN, dùng HQLA xuống dưới ngưỡng không được coi là hợp lệ như trong Basel.
- *Diễn giải:* ALCO cần đặt LCR mục tiêu nội bộ trên ngưỡng lộ trình, với khoảng đệm đủ hấp thụ biến động hằng ngày. Chi phí của khoảng đệm này nên được phân bổ qua FTP theo run-off rate của từng sản phẩm nợ ([[liquidity-transfer-pricing]]). Mức đệm cụ thể chưa có nguồn.
- *Diễn giải:* khi chọn tài sản cho đệm, ALCO đánh đổi giữa lợi suất (giảm carry) và độ nhạy giá (rủi ro LCR và EVE khi lãi suất tăng). Phòng ngừa bằng phái sinh được phép mà HQLA vẫn được tính [[src-tt50-2026-nhnn#^d20-2dd]].

## Bất định
- Tác động định lượng của danh mục HQLA lên EVE/ΔNII: chưa có cạnh `hqla → economic-value-of-equity` có nguồn. Có thể tìm trong nguồn IRRBB đã ingest khi có đoạn về danh mục đầu tư thanh khoản.
- Lợi suất tiền gửi NHNN so với TPCP và chi phí vốn ở VN: chưa có nguồn số liệu (cần `as_of`).
- Mức LCR mục tiêu nội bộ thông dụng: chưa có nguồn. Node [[lcr]] có bảng ngưỡng 4 tầng trong đoạn *Diễn giải* nhưng không có citation, nên không dùng ở đây.
