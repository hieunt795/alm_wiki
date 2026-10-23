---
title: "Bản chất, mục tiêu của FTP và vấn đề FTP giải quyết trong quản trị bảng cân đối"
aliases: [FTP: bản chất, mục tiêu và vấn đề giải quyết, FTP purpose and balance sheet problems]
type: synthesis
domains: [alm, product, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Bản chất và mục tiêu của Funds Transfer Pricing (FTP) trong ngân hàng là gì? · FTP giải quyết vấn đề gì trong quản trị bảng cân đối?"
as_of: 2026-10-22
sources: ["[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]", "[[src-vab-ftp]]", "[[src-bardaeva-alm]]", "[[src-tata-bank-alm]]", "[[src-bcbs-liquidity-principles-2008]]", "[[src-tt83-2025-nhnn]]"]
relations: []
# relations — synthesis: luôn để trống; synthesis không làm chủ thể hay đích của relation. Quan hệ khai ở node tri thức (chủ thể A); thân bài trình bày chuỗi quan hệ trong `## Cơ chế`. Xem 03_meta/taxonomy.md, mục "Relation"
tags: [ftp, treasury, transfer-pricing, balance-sheet]
updated: 2026-10-22
reviewed:
---

## Câu hỏi

- Q1. Bản chất và mục tiêu của Funds Transfer Pricing (FTP) trong ngân hàng là gì?
- Q2. FTP giải quyết vấn đề gì trong quản trị bảng cân đối?

Một cụm, không có hub. Node nền: [[funds-transfer-pricing]] (draft), [[liquidity-transfer-pricing]] (draft), [[maturity-transformation]] (draft), [[internal-funding-curve]] (draft). Mốc as_of 2026-10-22; TT83/2025 hiệu lực từ 2026-07-01.

## Kết luận

**Q1.** FTP là cơ chế chuyển giao rủi ro nội bộ. Choudhry viết rằng FTP không phải phòng ngừa rủi ro ra bên ngoài và cũng không phải điều chuyển vốn vật lý nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-10]]. Giá điều chuyển là giá giả định, dựa trên một phòng ngừa danh nghĩa cho giao dịch khách hàng [[src-choudhry-principles-banking#^choudhry-ftp-5]]. Hệ thống FTP là ranh giới giữa maturity transformation và customer franchise [[src-choudhry-principles-banking#^choudhry-ftp-3]].

Mục tiêu có hai tầng. Tầng giao dịch: dùng lãi suất thị trường vốn trùng khớp kỳ hạn làm giá điều chuyển để đo năng lực customer franchise của từng đơn vị kinh doanh (BU) [[src-choudhry-principles-banking#^choudhry-ftp-4]], và giữ commercial margin không đổi trước biến động đường cong sau đó [[src-choudhry-principles-banking#^choudhry-ftp-8]]. Tầng ngân hàng: VAB nêu bốn mục tiêu tổng thể là quản lý lợi nhuận, quản lý bảng cân đối, quản lý rủi ro thanh khoản và lãi suất sổ ngân hàng, và định hướng hoạt động kinh doanh [[src-vab-ftp#^vab-ftp-2]].

**Q2.** FTP giải quyết ba vấn đề của bảng cân đối, và có giới hạn ở vấn đề thứ tư.

1. Lợi nhuận của BU lẫn với lợi nhuận từ chênh lệch kỳ hạn. FTP tách kết quả giao dịch thành customer contribution và risk contribution [[src-lubinska-alm-optimisation#^lubinska-u01-11]], nên giá giao dịch khách hàng và commercial margin không bị trợ cấp chéo bằng P&L kỳ vọng chưa thực hiện từ vị thế chênh lệch kỳ hạn [[src-choudhry-principles-banking#^choudhry-ftp-9]].
2. Rủi ro lãi suất và rủi ro funding nằm rải ở BU. FTP gỡ hai rủi ro này khỏi BU và chuyển về ALM quản lý tập trung [[src-lubinska-alm-optimisation#^lubinska-u01-7]].
3. Chi phí thanh khoản không được gán cho mảng tạo ra nó. Liquidity FTP bắt BU tạo tài sản gây áp lực thanh khoản phải chịu chi phí tìm nguồn đó qua phí FTP [[src-choudhry-principles-banking#^choudhry-ftp-15]].
4. Giới hạn: một số rủi ro không chuyển ra thị trường được, do FTP thiết lập sai hoặc thị trường phái sinh kém thanh khoản; rủi ro tín dụng theo định nghĩa không chuyển về ALM [[src-lubinska-alm-optimisation#^lubinska-u01-8]].

Lubinska còn xếp FTP vào công cụ quản lý bảng cân đối để thực thi chiến lược: khung FTP vững cho phép steering và control cần thiết để đạt mục tiêu bảng cân đối [[src-lubinska-alm-optimisation#^lubinska-u01-11]].

## Cơ chế

### Chuỗi quan hệ quanh FTP (Q1, Q2)

| Từ | Quan hệ | Tới | Chiều · regime | Nguồn |
|---|---|---|---|---|
| [[internal-funding-curve]] | input-to | [[funds-transfer-pricing]] | — | [[src-choudhry-principles-banking#^choudhry-ifc-9]] |
| [[liquidity-transfer-pricing]] | part-of | [[funds-transfer-pricing]] | — | [[src-choudhry-principles-banking#^choudhry-ftp-14]] |
| [[maturity-transformation]] | priced-by | [[liquidity-transfer-pricing]] | — | [[src-choudhry-principles-banking#^choudhry-ftp-15]] |
| [[bcbs-liquidity-principles]] | governs | [[funds-transfer-pricing]] | — | [[src-bcbs-liquidity-principles-2008#^lrm-19]] |
| [[funds-transfer-pricing]] | input-to | [[net-interest-margin]] | — | [[src-vab-ftp#^vab-ftp-40]] |

Chưa có cạnh từ [[funds-transfer-pricing]] tới [[gap-risk]] hay [[liquidity-cost-risk]] trong `relations` [cần nguồn]. Nguồn nói FTP chuyển rủi ro lãi suất và funding về ALM [[src-lubinska-alm-optimisation#^lubinska-u01-7]], nhưng chưa ai khai thành cạnh.

### FTP là ranh giới giữa hai nguồn lợi nhuận (Q1, Q2)

- Maturity transformation là việc tạo lợi nhuận rủi ro từ chênh lệch kỳ hạn có chủ đích hoặc không giữa tài sản và nợ [[src-choudhry-principles-banking#^choudhry-ftp-1]]. Customer franchise là năng lực bán sản phẩm cho khách hàng ở lãi suất khác lãi suất thị trường vốn [[src-choudhry-principles-banking#^choudhry-ftp-2]].
- Sự tách "rủi ro" khỏi "phi rủi ro" là một hệ quả quan trọng của hệ thống FTP [[src-choudhry-principles-banking#^choudhry-ftp-13]].
- Trong ví dụ của Lubinska, asset centre lãi 2,69%, liability centre lỗ 0,68% (chi phí vốn bên ngoài cao hơn FTP rate) và ALM lãi 0,99% từ chuyển hoá kỳ hạn và lãi suất [[src-lubinska-alm-optimisation#^lubinska-u01-16]].

### Matched-maturity và commercial margin (Q1)

- Việc chuyển vốn giữa Treasury và BU thanh toán trên cơ sở trùng khớp kỳ hạn theo một đường cong FTP được chọn phù hợp [[src-choudhry-principles-banking#^choudhry-ftp-6]]. Commercial margin là chênh lệch giữa lãi suất khách hàng và lãi suất FTP [[src-choudhry-principles-banking#^choudhry-ftp-7]].
- Lãi suất FTP cố định trên cơ sở trùng khớp (cùng kỳ hạn, đồng tiền, cơ sở lãi suất) với lãi suất khách hàng, nên commercial margin không đổi trước thay đổi đường cong FTP hay tỷ giá về sau [[src-choudhry-principles-banking#^choudhry-ftp-8]]. Lubinska nêu cùng ý: customer margin không đổi suốt vòng đời sản phẩm [[src-lubinska-alm-optimisation#^lubinska-u01-15]].
- Marginality principle: chi phí đã phát sinh của nguồn vốn hiện có không liên quan tới định giá khoản vay mới [[src-choudhry-principles-banking#^choudhry-ftp-12]].

### Liquidity FTP và chi phí thanh khoản (Q2)

- Chênh lệch chi phí huy động của ngân hàng nới rộng đã dẫn tới việc mở rộng FTP lãi suất cổ điển bằng tầng liquidity FTP [[src-choudhry-principles-banking#^choudhry-ftp-14]].
- Case Europe Arab Bank: FTP Libor-flat tạo điều kiện cho rủi ro thanh khoản dư thừa và lợi nhuận mảng kinh doanh cao một cách giả tạo khi ngân hàng huy động cao hơn Libor [[src-choudhry-principles-banking#^choudhry-cs-3]]. Chế độ FTP có liquidity premium từ 1/1/2010 chuyển thêm thu nhập về mảng tạo nguồn vốn và buộc corporate banking định giá khoản vay chính xác hơn [[src-choudhry-principles-banking#^choudhry-cs-4]].
- UBS 2008: ban lãnh đạo không phát hiện lỗi trong cơ chế funding nội bộ, cho phép mảng structured credit ghi lợi nhuận ảo; Choudhry kết luận giá chuyển vốn phải phản ánh đúng vị thế rủi ro thanh khoản của từng mảng [[src-choudhry-principles-banking#^choudhry-gov-12]].

### Vận hành: ai quyết định và dùng để lái bảng cân đối (Q2)

- ALM xác định nguyên tắc định giá điều chuyển, dựng đường cong FTP nội bộ và quy tắc lãi suất khách hàng tối thiểu [[src-bardaeva-alm#^ch11-5]]. Nguyên tắc gán kỳ hạn trên đường cong không được do đơn vị thực hiện giao dịch quyết định [[src-bardaeva-alm#^ch11-11]].
- Bardaeva: để khuyến khích huy động và hạn chế cho vay, đường cong FTP phải được định giá lại và/hoặc áp steering margin; độ dốc đường cong FTP điều chỉnh tác động bất lợi của chuyển hoá kỳ hạn lên NII [[src-bardaeva-alm#^ch15-8]].

## Bằng chứng ủng hộ

- Ba nguồn T4 độc lập (Choudhry, Lubinska, Bardaeva) cùng mô tả FTP là cơ chế tách khách hàng khỏi rủi ro và đặt rủi ro về ALM/Treasury. Tài liệu VAB (T4, `doc_status: draft`, tư vấn) lặp lại các mục tiêu này cho bối cảnh ngân hàng Việt Nam [[src-vab-ftp#^vab-ftp-2]].
- Basel (T2): BCBS 144 P4 nêu ngân hàng nên đưa chi phí, lợi ích, rủi ro thanh khoản vào định giá nội bộ, đo lường hiệu quả và duyệt sản phẩm mới, để động cơ chấp nhận rủi ro của từng mảng khớp với rủi ro thanh khoản chúng tạo ra cho toàn ngân hàng [[src-bcbs-liquidity-principles-2008#^lrm-p04]]. Chi phí nên được phân bổ tường minh, với liquidity charge gán cho trạng thái, danh mục hoặc giao dịch [[src-bcbs-liquidity-principles-2008#^lrm-19]].

## Bằng chứng trái chiều

- Không ghi nhận nguồn nào bác bỏ mục đích của FTP.
- Mandate của Treasury làm giá FTP khác nhau. Treasury là cost centre thì lãi suất chuyển giao thường bằng COF nội bộ, có thể cộng spread bù chi phí vận hành; là profit centre thì còn kiếm P&L từ rủi ro lãi suất phát sinh khi funding ở đầu ngắn đường cong [[src-choudhry-principles-banking#^choudhry-mo-3]]. Tata mô tả cùng lựa chọn cho ALM: profit centre hoặc cost centre, và cost centre chuyển chi phí vào chi phí chung của đơn vị kinh doanh [[src-tata-bank-alm#^tata-prac-4]]. Đây là khác biệt về thiết kế, không phải conflict.

## Phụ thuộc regime

- Khi chi phí huy động nới rộng, FTP lãi suất cổ điển không đủ và cần thêm tầng liquidity FTP [[src-choudhry-principles-banking#^choudhry-ftp-14]]. Với ngân hàng huy động cao hơn Libor, FTP Libor-flat làm lợi nhuận mảng sai lệch [[src-choudhry-principles-banking#^choudhry-cs-3]].
- Nguồn đã ingest chưa phân tích hành vi của FTP theo chiều lãi suất tăng hay giảm. [cần nguồn]

## Hàm ý ALM / quy định

- **Nghĩa vụ tại VN (T1).** TT83/2025/TT-NHNN (hiệu lực 2026-07-01) có hai yêu cầu liên quan FTP và cả hai đều gián tiếp: ngân hàng phải xác định chi phí đáp ứng nhu cầu thanh khoản và rủi ro thanh khoản trong định giá vốn nội bộ, và trong đánh giá kết quả kinh doanh các hoạt động trọng yếu, cả nội bảng và ngoại bảng [[src-tt83-2025-nhnn#^d45-1b]]; chiến lược phải có nguyên tắc xác định chi phí bù đắp rủi ro tín dụng trong tính lãi suất, định giá sản phẩm tín dụng theo mức độ rủi ro của khách hàng [[src-tt83-2025-nhnn#^d26-2c]]. Wiki chưa có quy định NHNN nào đặt yêu cầu cho cả hệ thống FTP (cấu phần lãi suất, kỳ hạn, vốn).
- **Tham chiếu Basel (không phải nghĩa vụ tại VN).** BCBS 144 P4 chỉ nói phần thanh khoản [[src-bcbs-liquidity-principles-2008#^lrm-p04]]. Wiki chưa có chuẩn BCBS về FTP cho cấu phần lãi suất, tín dụng. [cần nguồn]
- **Tài liệu VN.** VAB đặt mục tiêu hướng dẫn định giá điều chuyển vốn tuân thủ pháp luật và phù hợp tiêu chuẩn Basel [[src-vab-ftp#^vab-ftp-3]], và yêu cầu lãi suất FTP phản ánh đủ chi phí vốn đầu vào, chi phí quản lý rủi ro thanh khoản và rủi ro lãi suất [[src-vab-ftp#^vab-ftp-5]]. Đây là tài liệu tư vấn T4 bản draft, không phải quy định.
- *Diễn giải:* nếu hai yêu cầu TT83 ở trên là phần duy nhất của nghĩa vụ NHNN về FTP, thì thiết kế đường cong, kỳ hạn và chuyển giao rủi ro lãi suất là quyết định thiết kế nội bộ của ngân hàng, tham chiếu Choudhry/Lubinska/VAB. ALCO là nơi duyệt các quyết định này (xem [[alco]]). (ngoài wiki, chưa có nguồn)

## Bất định

- [cần nguồn] Quy định NHNN riêng về hệ thống FTP. Chưa thấy trong wiki; `src-tt14-2025-nhnn` có 0/19 unit ingest nhưng chưa rõ có nội dung FTP.
- Cạnh [[funds-transfer-pricing]] —input-to→ [[net-interest-margin]] cite `^vab-ftp-40` chỉ nói NIM sản phẩm trong tài liệu VAB được tính từ chênh lệch lãi suất khách hàng và giá FTP; chưa đủ để nói FTP ảnh hưởng NIM toàn ngân hàng. Rà lại cạnh ngày 2026-10-22: cạnh đúng ở phạm vi NIM sản phẩm theo VAB.
- Chưa có cạnh từ [[funds-transfer-pricing]] tới [[gap-risk]], [[liquidity-cost-risk]] trong `relations`, dù claim `^lubinska-u01-7` đã có. Gợi ý `/ingest --node funds-transfer-pricing` hoặc đề xuất thêm cạnh khi user duyệt.
- Phần "ba kênh truyền dẫn" của [[ftp-transmission-mechanism]] dựa chủ yếu vào nguồn T5 (`src-ftp-transmission-analysis`), nên không dùng trong cụm này.
- [[internal-risk-transfer]] đã viết lại ngày 2026-10-22 (bỏ ví dụ số tự dựng); cụm này vẫn chỉ dùng ví dụ số của Lubinska có citation.
- [2026-10-22] ingest src-tata-bank-alm (bổ sung 2.3 FTP): [[funds-transfer-pricing]] thêm Tata ^tata-ftp-16/17 (steering) và ^tata-ftp-29 (phạm vi rủi ro); cần rà lại Q2 mục Giới hạn.
- Bước 3 chưa đọc raw: mọi claim lấy từ source note đã ingest, trích nguyên văn đã khớp lint.
