---
title: Domain Macro
type: nav
domain: macro
updated: 2026-10-21
as_of: 2026-10-21
---

# Domain `macro`: Macroeconomic

## Phạm vi
Chính sách tiền tệ, lãi suất, lạm phát, thanh khoản hệ thống. Mọi claim định lượng của domain này phải có `as_of` ([[overview]], `03_meta/taxonomy.md`).

## Tóm tắt
Domain có 3 node, đều draft. [[term-structure-theories]] là node đầu tiên nhận `macro` làm domain chính (lý thuyết đường cong lợi suất theo Choudhry Ch4). [[negative-interest-rates]] và [[credit-turnover]] gắn `macro` nhưng viết từ góc nhìn ALM. Các nguồn macro chuyên biệt đã đăng ký trong registry nhưng chưa unit nào được ingest (xem mục Lỗ hổng).

## Cụm chủ đề

### Lãi suất âm và sàn 0%
- Ngày 5/6/2014, ECB hạ lãi suất deposit facility xuống −0,10% [[src-tata-bank-alm#^tata-neg-1]]. Ngày 6/7/2020, toàn bộ đường cong trái phiếu chính phủ Đức và đường cong EUR OIS nằm dưới 0,00%, tới kỳ hạn 30 và 40 năm [[src-choudhry-principles-banking#^choudhry-neg-1]].
- Trước giai đoạn này, giả định mô hình phần lớn coi lãi suất bị chặn dưới ở 0, ví dụ giả định phân phối log-normal [[src-tata-bank-alm#^tata-neg-1]].
- Với ALM, vấn đề chính là sàn 0% trên tiền gửi bán lẻ. Khi có sàn, lãi suất thực trả là $\max(r_I \pm x;\ 0\%)$ thay vì $r_I \pm x$ [[src-tata-bank-alm#^tata-neg-2]]. Sàn 0% là một quyền chọn nhúng: gần như không có giá trị khi lãi suất cao, nhưng at the money hoặc in the money khi lãi suất thấp hay âm [[src-tata-bank-alm#^tata-neg-2]].
- NIRP làm giảm biên trung gian, vì lợi suất tài sản giảm trong khi phần lớn chi phí vốn không đổi [[src-tata-bank-alm#^tata-neg-4]].
- Ở Đức giai đoạn 1999–2021, tỷ trọng tiền gửi không kỳ hạn tăng từ 7,9% lên 29,3% [[src-tata-bank-alm#^tata-prac-1]].
- Dữ liệu hành vi của thời kỳ lãi suất âm không dùng để backtest cho thời kỳ lãi suất dương, và ngược lại [[src-tata-bank-alm#^tata-beh-2]].

Node: [[negative-interest-rates]] (concept, draft).

*Diễn giải:* toàn bộ claim trên đến từ hai sách ALM (T4) và nói về hệ quả của chính sách tiền tệ lên bảng cân đối ngân hàng. Wiki chưa có claim nào về bản thân cơ chế chính sách tiền tệ (truyền dẫn, công cụ NHTW, lạm phát).

### Hấp thụ tín dụng và lãi suất cho vay tại VN
- Nguyễn Khánh (T5, 22/9/2026) cho rằng một bộ phận doanh nghiệp không chấp nhận vay VND ở mức 9–10%, nên tín dụng không hình thành dù ngân hàng có thanh khoản [[src-clip-ldr-credit-turnover-bottleneck#^p2]].
- Theo tác giả, thanh khoản ở thị trường 2 chỉ thành tín dụng khi đi qua chuỗi tiền gửi liên ngân hàng → cho vay ngắn hạn → vốn lưu động → deposit ngắn → cho vay mới dài [[src-clip-ldr-credit-turnover-bottleneck#^p3]].
- Nới LDR giải quyết giới hạn bảng cân đối ngân hàng, không giải quyết giới hạn hấp thụ vốn của nền kinh tế [[src-clip-ldr-credit-turnover-bottleneck#^p4]].
- Vòng quay tín dụng ngắn hạn thấp làm chi phí vốn kinh tế tăng, nên lãi suất cho vay dài hạn khó giảm [[src-clip-ldr-credit-turnover-bottleneck#^p7]].

Node: [[credit-turnover]] (concept, draft).

### Đường cong lợi suất
- Liquidity preference theory: người cho vay phải được bù premium cho việc mất thanh khoản, nên đường cong hầu như luôn dốc lên [[src-choudhry-principles-banking#^choudhry-ytc-1]].
- Độ dốc đường cong, thường đo bằng lợi suất 10 năm trừ lãi suất 3 tháng, là thước đo mức thắt chặt của chính sách tiền tệ. Ở Mỹ, mọi cuộc suy thoái từ 1955 trừ một đều có đường cong Treasury đảo ngược đi trước [[src-choudhry-principles-banking#^choudhry-ytc-5]].
- Quy mô nợ công mà thị trường cảm nhận ảnh hưởng lợi suất trái phiếu; nợ tăng có thể đẩy lợi suất tăng trên mọi kỳ hạn [[src-choudhry-principles-banking#^choudhry-ytc-8]].

Node: [[term-structure-theories]] (concept, draft).

## Giao với domain khác
- `alm`, `product`: [[term-structure-theories]] là nền cho [[internal-funding-curve]] (đường cong FTP). Xem [[domain-alm]].
- `alm`: [[credit-turnover]] tác động lên [[cost-of-funds]] và [[loan-pricing]]. Xem [[domain-alm]].
- `alm`: [[negative-interest-rates]] tác động lên [[non-maturity-deposits]], [[behavioural-options]], [[nii-planning]], [[net-interest-margin]]. Xem [[domain-alm]].
- `product`: sàn 0% là quyền chọn nhúng [[src-tata-bank-alm#^tata-neg-2]], liên quan [[interest-rate-cap-floor]]; NMD được hedge bằng [[interest-rate-swap]]. Xem [[domain-product]].
- `vn-reg`: phần TT83/2025 đã ingest không đề cập lãi suất âm hay sàn 0% [cần nguồn]. Xem [[domain-vn-reg]].

## Lỗ hổng và câu hỏi mở
- Các nguồn `macro` đã đăng ký nhưng chưa ingest unit nào (`03_meta/sources.yaml`): `src-bindseil-mpo`, `src-cargill-financial-system`, `src-imf-macro-accounting`, `src-modern-money-mechanics`, `src-friedman-capitalism-freedom`, `src-choudhry-yield-curve`, `src-choudhry-fixed-income-markets`, `col-during-fixed-income`. `col-clippings` mới ingest 1/90 bài.
- Chưa có node về: cơ chế điều hành chính sách tiền tệ của NHNN (OMO, tái cấp vốn, dự trữ bắt buộc), lãi suất điều hành, thanh khoản hệ thống, lạm phát [cần nguồn]. Đường cong lợi suất mới có lý thuyết chung (Choudhry Ch4), chưa có dữ liệu đường cong VN [cần nguồn].
- Câu hỏi mở trong [[overview]], xem [[alternative-liquidity-approaches]]: cơ chế OMO/tái cấp vốn của NHNN có thể phát triển thành cơ chế CLF (Option 1) theo Basel LCR31 không?
- Quy định VN về lãi suất tiền gửi âm chưa có trong wiki [cần nguồn].

## Thống kê
Diễn giải: thống kê nội bộ wiki, không phải claim nguồn. Đếm mọi node có `macro` trong `domains`, ở bất kỳ vị trí nào, as_of 2026-10-21.

| Type | Số node | Maturity |
|---|---|---|
| concept | 3 | draft 3 |
| **Tổng** | **3** | |
