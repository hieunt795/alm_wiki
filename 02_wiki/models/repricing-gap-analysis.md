---
title: "Repricing Gap Analysis"
aliases: [Repricing Gap Analysis, Maturity Gap Analysis, Phân tích khe hở tái định giá, Khe hở kỳ hạn lãi suất, Refixing Gap Analysis, Incremental Gap]
type: model
domains: [alm]
status: active
maturity: draft
sources: ["[[src-lubinska-alm-optimisation]]", "[[src-choudhry-principles-banking]]", "[[src-bardaeva-alm]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u02-30]]"}
  - {type: input-to, to: "[[net-interest-income-sensitivity]]", cite: "[[src-lubinska-alm-optimisation#^lubinska-u02-23]]"}
tags: [irrbb, nii, maturity-gap, repricing-gap, refixing-gap, static-model]
updated: 2026-10-20
reviewed:
---

## Mục tiêu
Maturity gap (khe hở kỳ hạn) / Repricing gap (khe hở tái định giá) là kỹ thuật cổ điển và trực quan nhất để đo lường IRRBB, ra đời và phát triển mạnh mẽ trong giai đoạn 1973–1986 ("kỷ nguyên rủi ro tối thiểu" — *minimum risk ALM concept*) sau khi hệ thống Bretton Woods sụp đổ và các cuộc khủng hoảng dầu mỏ khiến lãi suất biến động dữ dội [[src-bardaeva-alm#^ch2-1]] (xem [[alm-evolution]]).

Về nguyên tắc vận hành, Bardaeva (Box 2.1) làm rõ sự khác biệt bản chất giữa khe hở thanh khoản và khe hở lãi suất:
- **Liquidity Gap**: Luôn được ưu tiên duy trì ở trạng thái dương ($GAP > 0$) tại mọi thời điểm để đảm bảo an toàn khả năng chi trả của ngân hàng.
- **Interest Rate Gap**: Lý tưởng nhất nên được duy trì quanh mức 0 ($GAP \approx 0$) hoặc nằm trong các hạn mức khẩu vị rủi ro (*RAS limits*) đã thiết lập để bảo vệ thu nhập lãi thuần [[src-bardaeva-alm#^ch2-2]].

Kỹ thuật này phân tài sản, nợ và vị thế ngoại bảng nhạy lãi suất vào các dải thời gian định trước:
- khoản lãi suất cố định xếp theo kỳ hạn;
- khoản lãi suất thả nổi xếp theo thời gian đến lần tái định giá kế tiếp;
- khoản không có kỳ tái định giá xác định, như tiền gửi không kỳ hạn, và khoản có kỳ hạn thực khác hợp đồng, như vay có quyền trả trước, được phân bổ theo đánh giá và kinh nghiệm của ngân hàng [[src-lubinska-alm-optimisation#^lubinska-u02-22]].

Theo nguyên tắc tương xứng, ngân hàng càng lớn thì phương pháp đo IRRBB càng phải phức tạp [[src-lubinska-alm-optimisation#^lubinska-u02-22]]. Repricing gap đo và kiểm soát [[gap-risk]] theo từng dải và từng đồng tiền trọng yếu [[src-lubinska-alm-optimisation#^lubinska-u02-30]]. Mô hình đứng ở góc nhìn thu nhập, bổ sung cho góc nhìn giá trị kinh tế ([[economic-value-of-equity]]) [[src-lubinska-alm-optimisation#^lubinska-u02-20]].

## Công thức
Repricing gap của một dải bằng tài sản nhạy lãi suất trừ nợ nhạy lãi suất trong dải đó. Nhân gap với thay đổi lãi suất giả định cho xấp xỉ thay đổi NII [[src-lubinska-alm-optimisation#^lubinska-u02-23]]. Các thành phần [[src-lubinska-alm-optimisation#^lubinska-u02-25]]:
- RSA là tài sản nhạy lãi suất, ví dụ khoản vay cố định hoặc thả nổi;
- RSL là nợ nhạy lãi suất, ví dụ vốn bán buôn hoặc tiền gửi không kỳ hạn;
- gapping period (GP) là kỳ phân tích, ví dụ 1 năm.

*Diễn giải (tái dựng, chưa đối chiếu bản gốc):* raw bị mất công thức (`formula-not-decoded`). Dựng lại từ lời văn của nguồn:

$$
\Delta NII = GAP \times \Delta i, \qquad GAP = RSA - RSL
$$

Incremental gap cộng các gap theo trọng số thời gian, tức thời gian từ điểm giữa dải đến cuối gapping period [[src-lubinska-alm-optimisation#^lubinska-u02-28]]. Dựng lại, với $T$ là độ dài gapping period và $t_k$ là điểm giữa dải $k$:

$$
\Delta NII \approx \Delta i \sum_{k} GAP_k \, (T - t_k)
$$

**Dấu của gap** [[src-lubinska-alm-optimisation#^lubinska-u02-26]]:

| GAP | Rủi ro | Lãi suất tăng | Lãi suất giảm | Nguồn |
|---|---|---|---|---|
| > 0 | Tái đầu tư | Lãi | Lỗ | [[src-lubinska-alm-optimisation#^lubinska-u02-26]] |
| < 0 | Tái cấp vốn | Lỗ | Lãi | [[src-lubinska-alm-optimisation#^lubinska-u02-26]] |
| = 0 | Miễn nhiễm | — | — | [[src-lubinska-alm-optimisation#^lubinska-u02-26]] |

## Inputs & giả định
**Các biến thể** của phương pháp:

| Biến thể | Đặc điểm | Dùng cho | Nguồn |
|---|---|---|---|
| Maturity gap cơ bản | Đặt dòng tiền ở điểm giữa dải; không biết dòng tiền gắn với yếu tố rủi ro nào | Ước tính nhanh | [[src-lubinska-alm-optimisation#^lubinska-u02-34]] |
| Advanced repricing gap | Đặt dòng tiền ở ngày rủi ro chính xác; tách dòng đáo hạn (tái đầu tư theo lãi suất forward) khỏi dòng refixing; bắt được indexation không hoàn hảo | Đo ΔNII theo từng yếu tố rủi ro | [[src-lubinska-alm-optimisation#^lubinska-u02-34]] |
| Refixing gap | Thể hiện mọi ngày refixing trong gapping period theo từng chỉ số (EURIBOR 3M, LIBOR 1M…); vị thế run-off | Đặt chiến lược phòng ngừa | [[src-lubinska-alm-optimisation#^lubinska-u02-37]] |
| Flow approach | Dòng tiền với khoản cố định, dư nợ tại ngày tái định giá với khoản thả nổi | Tính ΔNII | [[src-lubinska-alm-optimisation#^lubinska-u02-35]] |
| Stock analysis | Dư nợ của từng khoản | Phơi nhiễm theo dải và phòng ngừa | [[src-lubinska-alm-optimisation#^lubinska-u02-35]] |

**Indexation không hoàn hảo** phát sinh khi [[src-lubinska-alm-optimisation#^lubinska-u02-34]]:
- kỳ fixing khác kỳ trả lãi;
- có spread tài chính;
- trọng số của chỉ số khác 1;
- dùng chỉ số bình quân.

**Repricing gap chỉ "thấy" ngày rủi ro đầu tiên.** Ví dụ, một khoản nợ EURIBOR 3M tái định giá vào các tháng 1, 4, 7 và 10/2019. Nếu phân tích tại 12/2018 thì repricing gap chỉ hiện lần tái định giá tháng 1 [[src-lubinska-alm-optimisation#^lubinska-u02-36]]. Refixing gap khắc phục điểm này [[src-lubinska-alm-optimisation#^lubinska-u02-37]].

**Độ lớn cú sốc.** Cú sốc dựa trên kinh nghiệm, mô phỏng và đánh giá của ban điều hành. Nguồn ghi rằng hướng dẫn quy định hiện hành yêu cầu sốc song song ±200 bp [[src-lubinska-alm-optimisation#^lubinska-u02-23]]. Khi so sánh hai phương pháp, nguồn dùng sốc 200 bp nhưng nói có thể chọn mức khác [[src-lubinska-alm-optimisation#^lubinska-u02-34]].

*Diễn giải:* d368 hiệu chỉnh cú sốc theo từng đồng tiền, nên mức 200 bp ở đây nên hiểu là mức của EUR trong bối cảnh EU của nguồn T4. Đây không phải chuẩn chung. Xem [[irrbb-standardised-shocks-eve-and-nii-measurement]].

**Giả định của gap analysis theo Choudhry** [[src-choudhry-principles-banking#^choudhry-irr-7]]:
- lãi suất dịch chuyển song song; thực tế không song song, gây basis risk giữa tài sản ngắn và dài hạn;
- tái định giá xảy ra ở giữa time bucket;
- mọi khoản trả nợ đúng hạn; thực tế một số người vay trả sớm.

**Xếp bucket NMD.** NMD đáo hạn qua đêm nhưng có thể có behavioural tenor dài. Có ba cách xếp [[src-choudhry-principles-banking#^choudhry-lgap-7]]:

| Cách xếp | Hệ quả | Nguồn |
|---|---|---|
| Bucket ngắn nhất (O/N–1 tuần) | Phổ biến nhất; gap và hồ sơ thanh khoản biến động mạnh | [[src-choudhry-principles-banking#^choudhry-lgap-7]] |
| Bucket dài nhất (> 12 tháng) | Hợp lý vì hành vi thống kê thường dài hạn | [[src-choudhry-principles-banking#^choudhry-lgap-7]] |
| Tách core (bucket dài) và unstable (bucket ngắn) | Số dư core phải được phân tích định kỳ | [[src-choudhry-principles-banking#^choudhry-lgap-7]] |

Xem [[non-maturity-deposits]].

## Calibration
Không có tham số calibration riêng. Chất lượng mô hình phụ thuộc vào cách phân bổ khoản hành vi vào dải, và nguồn dẫn sang các phương pháp thống kê ở Chương 3 [[src-lubinska-alm-optimisation#^lubinska-u02-22]]. Xem [[non-maturity-deposits]], [[behavioural-options]].

- Theo Choudhry, quy trình ALCO phổ biến là trình bày hằng tháng, so sánh NII thực tế với dự báo dưới dạng gap report theo bucket và sản phẩm. Phân tích kịch bản thường giả định sổ không đổi trong một tháng, điều nguồn gọi là không thực tế [[src-choudhry-principles-banking#^choudhry-irr-3]].

## Output & usage
- Regulatory: theo Final Report của EBA (19/7/2018), maturity gap làm trên Excel không còn phù hợp. Mô phỏng NII phải phục vụ nhiều mục đích [[src-lubinska-alm-optimisation#^lubinska-u02-33]]:
  - stress test của EBA có giả định về giá, tầm thời gian và thay đổi cấu trúc sổ;
  - thước đo nội bộ dùng sổ không đổi, trong đó khoản đáo hạn được thay bằng khoản cùng đặc điểm.
- Management: hai chiến lược [[src-lubinska-alm-optimisation#^lubinska-u02-26]]:
  - miễn nhiễm: giữ GAP gần 0;
  - GAP định hướng: điều chỉnh dấu của gap theo kỳ vọng lãi suất.
- Ví dụ refixing gap của nguồn: nợ ròng EUR 1 tỷ theo EURIBOR 6M refixing vào tháng 10 tạo rủi ro tập trung trong một tháng. Ngân hàng phòng ngừa bằng cách mua [[forward-rate-agreement|FRA]] để khoá lãi suất [[src-lubinska-alm-optimisation#^lubinska-u02-37]].
- Ví dụ maturity gap: tổng GAP ngắn hạn 500MM, ngân hàng nhạy tài sản nên NII 12 tháng tăng khi lãi suất tăng. Ở phần trung–dài hạn ngân hàng ở vị thế nợ ròng, nên lãi suất tăng làm EVE tăng [[src-lubinska-alm-optimisation#^lubinska-u02-27]].
- Việc tách thành phần lãi suất, thanh khoản và biên thương mại bằng FTP là điều kiện để phân bổ thu nhập lãi giữa bộ phận bán hàng và Treasury [[src-lubinska-alm-optimisation#^lubinska-u02-33]]. Xem [[funds-transfer-pricing]].

- Gap management giả định ALM manager dự báo đúng lãi suất và có thể đổi cấu trúc sổ dễ dàng; thực tế khó đổi cấu trúc bảng cân đối trong thời gian ngắn [[src-choudhry-principles-banking#^choudhry-lgap-10]].

## Hạn chế & validation
Maturity gap tĩnh có bốn hạn chế [[src-lubinska-alm-optimisation#^lubinska-u02-24]]:
- chỉ xét giao dịch hiện có, không có nghiệp vụ mới;
- coi mọi giao dịch trong cùng dải có cùng hồ sơ rủi ro;
- chỉ ước tính được dịch chuyển lãi suất đồng đều;
- giả định khoản đáo hạn được tái đầu tư hoặc tái cấp vốn mà không đổi cấu trúc.

Một số hạn chế khắc phục được bằng mô-đun mô phỏng NII [[src-lubinska-alm-optimisation#^lubinska-u02-24]]. Refixing gap cũng là phương pháp tĩnh: không xét nghiệp vụ mới, hành vi khách hàng với khoản có quyền chọn nhúng, hay biến động lãi suất tương lai; tác động lên NII tính theo đường forward [[src-lubinska-alm-optimisation#^lubinska-u02-37]].

*Diễn giải:* [[repricing-balance-sheet]] là bước chuyển bảng cân đối kế toán sang lịch tái định giá. Repricing gap analysis là phép đo chạy trên lịch đó. Kết quả gap đưa vào [[net-interest-income-sensitivity]] khi dùng giả định bảng cân đối không đổi.

- **Điểm yếu theo Choudhry**: không tính tăng trưởng hay thay đổi cơ cấu tài sản–nợ; không xét time value of money; time period đặt tuỳ ý. Dù vậy gap analysis vẫn được dùng rộng rãi, vì dữ liệu sẵn có từ báo cáo quy định, dễ tính và dễ giải thích cho lãnh đạo [[src-choudhry-principles-banking#^choudhry-irr-8]].
