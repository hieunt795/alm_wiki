---
title: "LDR Total Deposits (D)"
aliases: [LDR Total Deposits, Tổng tiền gửi trong LDR, Mẫu số LDR, LDR denominator]
type: metric
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2026-10-01
valid_to:
as_of:
sources: ["[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[loan-to-deposit-ratio]]", cite: "[[src-tt50-2026-nhnn#^d12-1]]"}
tags: [liquidity, funding, vn-regulation, ldr]
updated: 2026-10-21
reviewed:
---

## Định nghĩa
D là mẫu số của [[loan-to-deposit-ratio]] theo TT50/2026: tổng tiền gửi xác định tại Đ12.5, tức tổng các khoản ở Đ12.4 trừ đi các khoản ở Đ12.5 [[src-tt50-2026-nhnn#^d12-5]]. D tính theo VNĐ, gồm ngoại tệ quy đổi theo tỷ giá Đ3.14 [[src-tt50-2026-nhnn#^d12-1]] [[src-tt50-2026-nhnn#^d3-14]]. Tử số tương ứng là [[ldr-total-loans]].

## Công thức
*Diễn giải:* viết gọn từ lời văn Đ12.4–5.

$$D = (a + b + c + d + \text{đ} + e + g + h + i) - (5a + 5b + 5c)$$
[[src-tt50-2026-nhnn#^d12-4]] [[src-tt50-2026-nhnn#^d12-5]]

| Mã | Chiều | Đầu mục | Căn cứ |
|---|---|---|---|
| a | + | Tiền gửi của tổ chức, sau loại trừ (i)–(iv) | [[src-tt50-2026-nhnn#^d12-4a]] [[src-tt50-2026-nhnn#^d12-4]] |
| b | + | Tiền gửi của cá nhân, trừ ký quỹ và tiền gửi vốn chuyên dùng | [[src-tt50-2026-nhnn#^d12-4a]] |
| c | + | Trái phiếu phát hành trong nước đủ điều kiện Vốn cấp 2 | [[src-tt50-2026-nhnn#^d12-4]] |
| d | + | Vốn uỷ thác cấp tín dụng đã nhận và chịu rủi ro | [[src-tt50-2026-nhnn#^d12-4d]] |
| đ | + | Chênh lệch dương nhận từ TCTD trừ cấp cho TCTD | [[src-tt50-2026-nhnn#^d12-4]] |
| e | + | Vay nước ngoài, kể cả trái phiếu quốc tế | [[src-tt50-2026-nhnn#^d12-4]] [[src-tt50-2026-nhnn#^d12-4d]] |
| g | + | Vốn chủ sở hữu ròng (vốn, quỹ, thặng dư trừ lỗ luỹ kế, tài sản cố định, góp vốn, cổ phiếu quỹ) | [[src-tt50-2026-nhnn#^d12-4d]] |
| h | + | Lợi nhuận chưa phân phối trừ lãi, phí phải thu cộng lãi, phí phải trả | [[src-tt50-2026-nhnn#^d12-4d]] |
| i | + | Chênh lệch tỷ giá đánh giá lại vốn chủ sở hữu gốc ngoại tệ | [[src-tt50-2026-nhnn#^d12-4d]] |
| 5a | − | Cấp tín dụng khác không phải cho vay với khách hàng không phải TCTD | [[src-tt50-2026-nhnn#^d12-5]] |
| 5b | − | Đầu tư trái phiếu doanh nghiệp (có ngoại lệ) | [[src-tt50-2026-nhnn#^d12-4]] |
| 5c | − | Uỷ thác cho TCTD cấp tín dụng khác không phải cho vay | [[src-tt50-2026-nhnn#^d12-5]] |

## Giải trình từng đầu mục
Mỗi đầu mục gồm: lời văn TT50 (có citation), cách cùng khoản mục được xử lý trong LCR, NSFR của TT50 (có citation), và lý do cộng hoặc trừ dưới nhãn *Diễn giải*. TT50 không nêu lý do của từng đầu mục; phần "vì sao" là suy luận.

### Đ12.4.a — Tiền gửi của tổ chức
**Lời văn.** Cộng số dư tiền gửi của tổ chức, trừ bốn loại [[src-tt50-2026-nhnn#^d12-4a]] [[src-tt50-2026-nhnn#^d12-4]]:

| Loại trừ | Mức loại trừ | Căn cứ | Đối chiếu LCR, NSFR | Vì sao loại (*Diễn giải*) |
|---|---|---|---|---|
| (i) Tiền gửi của TCTD, chi nhánh NHNNg khác | 100% | [[src-tt50-2026-nhnn#^d12-4a]] | NSFR: nguồn từ TCTD có ASF 0% nếu không kỳ hạn hoặc dưới 6 tháng [[src-tt50-2026-nhnn#^pl2-a2]] | Không bỏ hẳn: tiền gửi TCTD quay lại qua đầu mục đ dưới dạng ròng. Loại ở đây để tránh tính gộp phần liên ngân hàng hai chiều |
| (ii) Tiền ký quỹ và tiền gửi vốn chuyên dùng | 100% | [[src-tt50-2026-nhnn#^d12-4a]] | — | Gắn với nghĩa vụ hoặc mục đích cụ thể (ký quỹ L/C, bảo lãnh; vốn dự án), nên không phải nguồn tự do để cho vay |
| (iii) Tiền gửi không kỳ hạn của KBNN | 100% | [[src-tt50-2026-nhnn#^d12-4a]] | LCR: nguồn từ KBNN có hệ số rút tiền 40% [[src-tt50-2026-nhnn#^pl1-b3-24]] | Biến động theo thu chi ngân sách, không ổn định |
| (iv) Tiền gửi có kỳ hạn của KBNN | 80%, hoặc tỷ lệ khác do Thống đốc quyết định | [[src-tt50-2026-nhnn#^d12-4]] | NSFR: tiền gửi KBNN có ASF 50% nếu dưới 1 năm, 100% nếu từ 1 năm [[src-tt50-2026-nhnn#^pl2-a2]] | Chỉ 20% được tính. Tỷ lệ do Thống đốc điều chỉnh nên đây là công cụ chính sách: tăng tỷ lệ tính vào D làm LDR toàn hệ thống giảm |

Phần còn lại (doanh nghiệp, tổ chức khác không phải TCTD, KBNN có kỳ hạn sau loại trừ) tính 100% số dư, không phân biệt kỳ hạn [[src-tt50-2026-nhnn#^d12-4a]].

*Diễn giải:* LCR áp hệ số rút tiền 40% cho nguồn vốn doanh nghiệp không phải tiền gửi hoạt động [[src-tt50-2026-nhnn#^pl1-b3-24]], còn D tính đủ 100%. D vì vậy coi tiền gửi doanh nghiệp ổn định ngang tiền gửi cá nhân, trái với giả định stress của LCR.

### Đ12.4.b — Tiền gửi của cá nhân
**Lời văn.** Cộng số dư tiền gửi của cá nhân, trừ tiền ký quỹ và tiền gửi vốn chuyên dùng [[src-tt50-2026-nhnn#^d12-4a]].

**Đối chiếu.** LCR: tiền gửi bán lẻ ổn định có hệ số rút tiền 5%, kém ổn định 10% [[src-tt50-2026-nhnn#^pl1-b2-2]] [[src-tt50-2026-nhnn#^pl1-b2-3]]. NSFR: ASF 95% (ổn định) hoặc 90% (kém ổn định) [[src-tt50-2026-nhnn#^pl2-a2]].

*Diễn giải:* đây là đầu mục khớp nhất giữa D và hai tỷ lệ Basel. Tiền gửi cá nhân là nguồn ổn định nhất trong D nhưng D không phân biệt ổn định và kém ổn định.

### Đ12.4.c — Trái phiếu Vốn cấp 2 phát hành trong nước
**Lời văn.** Cộng số dư trái phiếu do ngân hàng phát hành trong nước đủ điều kiện tính vào Vốn cấp 2 theo quy định tỷ lệ an toàn vốn ngân hàng đang áp dụng [[src-tt50-2026-nhnn#^d12-4]].

**Đối chiếu.** NSFR: Vốn cấp 2 có ASF 100% nếu kỳ hạn còn lại từ 1 năm, 50% nếu từ 6 tháng đến dưới 1 năm, 0% nếu dưới 6 tháng [[src-tt50-2026-nhnn#^pl2-a2]].

*Diễn giải:*
- Điều kiện "đủ điều kiện tính vào Vốn cấp 2" bảo đảm đây là nợ dài hạn, thứ cấp. D tính toàn bộ số dư, không giảm theo kỳ hạn còn lại như NSFR.
- Trái phiếu thường (không phải Vốn cấp 2) và chứng chỉ tiền gửi phát hành trong nước không có trong danh sách Đ12.4. Theo lời văn thì không tính vào D [cần nguồn: hướng dẫn báo cáo NHNN].
- TT50 định nghĩa tiền gửi là số dư gốc từ hoạt động nhận tiền gửi theo Luật Các TCTD [[src-tt50-2026-nhnn#^d3-2]], và liệt kê chứng chỉ tiền gửi là một loại giấy tờ có giá [[src-tt50-2026-nhnn#^d3-3]]. Chứng chỉ tiền gửi có thuộc "tiền gửi" ở Đ12.4 hay không phụ thuộc định nghĩa nhận tiền gửi của Luật Các TCTD [cần nguồn: Luật Các TCTD]. Trái phiếu phát hành ra thị trường quốc tế thì tính qua đầu mục e.

### Đ12.4.d — Vốn uỷ thác cấp tín dụng
**Lời văn.** Cộng nguồn vốn uỷ thác cấp tín dụng của Chính phủ, cá nhân và tổ chức khác (kể cả TCTD) mà ngân hàng đã nhận và chịu rủi ro khi cấp tín dụng [[src-tt50-2026-nhnn#^d12-4d]].

*Diễn giải:* đầu mục này đối xứng với L. Cho vay từ vốn nhận uỷ thác mà ngân hàng chịu rủi ro được tính vào L [[src-tt50-2026-nhnn#^d12-2]], nên nguồn vốn tài trợ khoản đó cũng vào D. Vốn uỷ thác mà ngân hàng không chịu rủi ro không thuộc cả hai vế.

### Đ12.4.đ — Chênh lệch dương liên ngân hàng
**Lời văn.** Cộng chênh lệch dương giữa số dư được cấp tín dụng, nhận tiền gửi từ TCTD, chi nhánh NHNNg khác và số dư cấp tín dụng, gửi tiền tại TCTD, chi nhánh NHNNg khác [[src-tt50-2026-nhnn#^d12-4]].

*Diễn giải:*
- Chỉ tính khi ngân hàng là bên vay ròng trên liên ngân hàng; bên cho vay ròng thì đầu mục này bằng 0, không âm.
- Kết hợp với loại trừ (i) ở a và loại cho vay TCTD khỏi L [[src-tt50-2026-nhnn#^d12-1]], liên ngân hàng chỉ đi vào LDR một lần, ở dạng ròng.
- Đầu mục này có thể làm LDR giảm nhờ vay liên ngân hàng ngắn hạn. Vay qua đêm từ TCTD khác cuối kỳ làm tăng đ, nên tăng D. NSFR thì cho nguồn TCTD dưới 6 tháng ASF 0% [[src-tt50-2026-nhnn#^pl2-a2]].

### Đ12.4.e — Vay nước ngoài
**Lời văn.** Cộng nguồn vay nước ngoài, kể cả trái phiếu phát hành ra thị trường quốc tế. Với chi nhánh NHNNg, gồm cả vay từ ngân hàng mẹ và chi nhánh của ngân hàng mẹ ở nước ngoài [[src-tt50-2026-nhnn#^d12-4]] [[src-tt50-2026-nhnn#^d12-4d]].

*Diễn giải:* TT50 không đặt điều kiện kỳ hạn cho vay nước ngoài. Khoản vay ngắn hạn từ ngân hàng nước ngoài vẫn được tính đủ vào D, trong khi nếu vay từ TCTD trong nước thì chỉ vào phần chênh lệch ròng ở đ. Hai nguồn liên ngân hàng tương tự nhau vì vậy được xử lý khác nhau.

### Đ12.4.g — Vốn chủ sở hữu ròng
**Lời văn.** Cộng vốn điều lệ, vốn được cấp, quỹ dự trữ bổ sung vốn điều lệ, quỹ đầu tư phát triển, quỹ dự phòng tài chính và thặng dư vốn cổ phần. Trừ lỗ luỹ kế, nguyên giá tài sản cố định, giá trị góp vốn, mua cổ phần và tiền mua cổ phiếu quỹ [[src-tt50-2026-nhnn#^d12-4d]].

*Diễn giải:* đây là phần vốn tự do (free capital): vốn chủ sở hữu chưa bị giữ trong tài sản không cho vay được (tài sản cố định, góp vốn, cổ phiếu quỹ). Trừ nguyên giá chứ không phải giá trị còn lại, nên khấu hao tài sản cố định không làm D tăng. NSFR cho Vốn cấp 1 ASF 100% [[src-tt50-2026-nhnn#^pl2-a2]] nhưng không trừ tài sản cố định ở vế nguồn.

### Đ12.4.h — Lợi nhuận chưa phân phối
**Lời văn.** Cộng lợi nhuận chưa phân phối, trừ lãi, phí phải thu, cộng lãi, phí phải trả [[src-tt50-2026-nhnn#^d12-4d]].

*Diễn giải:* điều chỉnh từ dồn tích sang tiền. Lãi phải thu đã ghi nhận vào lợi nhuận nhưng chưa thu được tiền, nên phải trừ. Lãi phải trả đã ghi nhận chi phí nhưng tiền vẫn còn ở ngân hàng, nên cộng lại. Đầu mục này có thể âm nếu lãi phải thu lớn.

### Đ12.4.i — Chênh lệch tỷ giá vốn chủ sở hữu
**Lời văn.** Cộng chênh lệch tỷ giá do đánh giá lại vốn chủ sở hữu gốc ngoại tệ, ghi nhận khi chuyển đổi báo cáo tài chính lập bằng ngoại tệ ra VNĐ [[src-tt50-2026-nhnn#^d12-4d]].

*Diễn giải:* chỉ phát sinh ở ngân hàng hạch toán bằng ngoại tệ (thường là chi nhánh NHNNg), để vốn quy đổi nhất quán với tỷ giá Đ3.14.b(ii) [[src-tt50-2026-nhnn#^d3-14]].

### Đ12.5.a — Trừ cấp tín dụng khác không phải cho vay
**Lời văn.** Trừ dư nợ gốc nội bảng mà ngân hàng chịu rủi ro từ cấp tín dụng khác không phải cho vay, kể cả nợ trả thay theo cam kết ngoại bảng và cấp tín dụng từ vốn nhận uỷ thác, đối với cá nhân, tổ chức không phải TCTD, chi nhánh NHNNg tại VN [[src-tt50-2026-nhnn#^d12-5]]. Các nghiệp vụ cấp tín dụng ngoài cho vay được liệt kê ở Đ9.3.a: chiết khấu, tái chiết khấu, cho thuê tài chính, bao thanh toán [[src-tt50-2026-nhnn#^d9-3]].

*Diễn giải:* các khoản này dùng vốn như cho vay nhưng không nằm trong L. Trừ ở mẫu số tương đương coi chúng đã dùng hết phần nguồn tương ứng, nên LDR đo cho vay so với nguồn còn lại sau khi tài trợ cấp tín dụng khác. Bảo lãnh, L/C chỉ bị trừ khi đã trả thay. Chi tiết phân loại xem [[ldr-total-loans]].

### Đ12.5.b — Trừ đầu tư trái phiếu doanh nghiệp
**Lời văn.** Trừ số dư đầu tư trái phiếu doanh nghiệp, không gồm trái phiếu do TCTD khác tại VN phát hành và trái phiếu đặc biệt của VAMC [[src-tt50-2026-nhnn#^d12-4]]. Đầu tư trái phiếu doanh nghiệp gồm mua, nắm giữ hoặc uỷ thác mua; không gồm nhận làm tài sản bảo đảm và chiết khấu, tái chiết khấu [[src-tt50-2026-nhnn#^d3-4]].

*Diễn giải:*
- Trái phiếu doanh nghiệp là rủi ro tín dụng tương tự cho vay, nên bị trừ như 5a.
- Trái phiếu do TCTD khác phát hành không bị trừ, nhất quán với cách liên ngân hàng bị loại khỏi cả L và a(i).
- Trái phiếu đặc biệt VAMC không bị trừ vì nó là kết quả của bán nợ xấu chứ không phải quyết định đầu tư.
- Trái phiếu Chính phủ và tín phiếu NHNN không bị trừ. Vì vậy đầu tư vào HQLA không làm LDR tăng.

### Đ12.5.c — Trừ uỷ thác cấp tín dụng khác
**Lời văn.** Trừ dư nợ gốc nội bảng từ khoản uỷ thác cho TCTD, chi nhánh NHNNg thực hiện cấp tín dụng khác không phải cho vay [[src-tt50-2026-nhnn#^d12-5]].

*Diễn giải:* đối xứng với Đ12.2.b. Uỷ thác cho TCTD khác cho vay thì vào L [[src-tt50-2026-nhnn#^d12-2]]; uỷ thác cấp tín dụng khác thì trừ khỏi D, như cấp tín dụng khác tự làm.

### Không có trong D
*Diễn giải:* theo lời văn Đ12.4, các nguồn sau không được liệt kê nên không tính vào D [cần nguồn: hướng dẫn báo cáo NHNN để xác nhận]:
- vay NHNN (tái cấp vốn, cầm cố, nghiệp vụ thị trường mở). Riêng tái cấp vốn không nhằm hỗ trợ thanh khoản thì đã trừ khỏi L [[src-tt50-2026-nhnn#^d12-1]];
- chứng chỉ tiền gửi, trái phiếu không đủ điều kiện Vốn cấp 2 phát hành trong nước;
- tiền gửi của TCTD ở phần không vượt chênh lệch dương liên ngân hàng;
- nợ phải trả khác (phải trả nội bộ, thuế, dự phòng).

## Ví dụ minh hoạ
*Diễn giải:* số giả định, đơn vị tỷ đồng.

| Đầu mục | Số dư | Tính vào D | Ghi chú |
|---|---|---|---|
| a. Tiền gửi doanh nghiệp | 400, trong đó ký quỹ 20 | 380 | trừ ký quỹ |
| a(iii). KBNN không kỳ hạn | 30 | 0 | loại 100% |
| a(iv). KBNN có kỳ hạn | 50 | 10 | loại 80% |
| a(i). Tiền gửi TCTD | 60 | 0 | đi vào đ |
| b. Tiền gửi cá nhân | 500, trong đó ký quỹ 5 | 495 | |
| c. Trái phiếu Vốn cấp 2 trong nước | 20 | 20 | |
| d. Vốn nhận uỷ thác chịu rủi ro | 10 | 10 | |
| đ. Nhận từ TCTD (tiền gửi 60 + vay 40) trừ gửi, cho vay TCTD 70 | 100 − 70 | 30 | |
| e. Vay nước ngoài | 30 | 30 | |
| g. Vốn 60 + quỹ 10 + thặng dư 5 − TSCĐ 15 − góp vốn 5 | 55 | 55 | |
| h. LNCPP 12 − lãi phải thu 8 + lãi phải trả 6 | 10 | 10 | |
| 5a. Chiết khấu, bao thanh toán | 25 | −25 | |
| 5b. Trái phiếu doanh nghiệp | 15 | −15 | |
| **D** | | **1.000** | |

Tiền gửi khách hàng theo nghĩa thông thường trong ví dụ là 400 + 500 + 30 + 50 = 980. D bằng 1.000 nhưng có cơ cấu khác: loại 95 (ký quỹ 25, KBNN 70), cộng 155 từ nguồn ngoài tiền gửi khách hàng (trái phiếu, uỷ thác, liên ngân hàng ròng, vay nước ngoài, vốn, lợi nhuận), trừ 40 cấp tín dụng khác và trái phiếu doanh nghiệp.

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Chỉ tiêu tương ứng | Không có LDR trong chuẩn BCBS đã ingest; NSFR đo nguồn ổn định bằng ASF có trọng số [cần nguồn] | D theo Đ12.4–5 [[src-tt50-2026-nhnn#^d12-4]] [[src-tt50-2026-nhnn#^d12-5]] | TT50 Đ12.4–5 | Từ khi áp dụng LCR/NSFR [[src-tt50-2026-nhnn#^d12-6]] |
| Trọng số theo độ ổn định | ASF 0–100% theo đối tác, kỳ hạn [cần nguồn: src-bcbs-nsfr] | 100% cho đầu mục được tính; loại 100% hoặc 80% cho đầu mục bị loại; không xét kỳ hạn [[src-tt50-2026-nhnn#^d12-4a]] [[src-tt50-2026-nhnn#^d12-4]] | TT50 Đ12.4 | |

## Ứng dụng trong ALM
- *Diễn giải:* các đòn bẩy làm tăng D gồm phát hành trái phiếu Vốn cấp 2 trong nước, vay nước ngoài, vay ròng liên ngân hàng cuối kỳ, giữ lợi nhuận. Các đòn bẩy làm giảm D gồm tăng chiết khấu, bao thanh toán, cho thuê tài chính và đầu tư trái phiếu doanh nghiệp. ALCO cần theo dõi D theo từng đầu mục chứ không chỉ theo tổng tiền gửi khách hàng.
- *Diễn giải:* D tính số dư cuối ngày, nên dễ bị tối ưu cuối kỳ bằng vay liên ngân hàng ngắn hạn (đầu mục đ). Đây là khác biệt lớn với [[nsfr]], nơi nguồn TCTD dưới 6 tháng có ASF 0% [[src-tt50-2026-nhnn#^pl2-a2]].

## Nhầm lẫn thường gặp
- *Diễn giải:* D không phải "tổng tiền gửi khách hàng" trên báo cáo tài chính. Hai số có thể gần nhau nhưng thành phần khác nhau (xem ví dụ).
- *Diễn giải:* tiền gửi KBNN có kỳ hạn không bị loại hết mà vẫn tính 20%; tiền gửi KBNN không kỳ hạn mới bị loại toàn bộ.
