---
title: "Structural Hedging (IRRBB)"
aliases: [Structural Hedging, Structural balance sheet hedging, Phòng ngừa cấu trúc IRRBB, Macro hedge IRRBB, Natural hedge, Phòng ngừa tự nhiên]
type: concept
domains: [alm, product]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]", "[[src-bardaeva-alm]]"]
relations:
  - {type: hedges, to: "[[gap-risk]]", cite: "[[src-choudhry-principles-banking#^choudhry-cs-17]]"}
tags: [irrbb, hedging, macro-hedge, natural-hedge, interest-rate-swap, hedge-accounting]
updated: 2026-10-22
reviewed:
---

## Ý chính
IRRBB không phải vị thế rủi ro mà ngân hàng tự chọn. Nó là sản phẩm phụ của chênh lệch tái định giá giữa cho vay và huy động, và chênh lệch này thường do khách hàng tạo ra [[src-choudhry-principles-banking#^choudhry-cs-13]]. Ngân hàng phòng ngừa IRRBB để giảm biến động NII và [[net-interest-margin|NIM]] [[src-choudhry-principles-banking#^choudhry-cs-14]].

Structural hedging là cách phòng ngừa ở mức bảng cân đối, theo phần ròng tài sản trừ nợ. Ngân hàng tận dụng các cặp tài sản – nợ đã tự phòng ngừa cho nhau, và chỉ ra thị trường để phòng ngừa phần ròng còn lại [[src-choudhry-principles-banking#^choudhry-cs-17]].

## Cơ chế & drivers
**Nguồn gốc của IRRBB cần phòng ngừa** [[src-choudhry-principles-banking#^choudhry-cs-13]]:
- tài sản lãi suất cố định được tài trợ bằng nợ thả nổi;
- tài sản thả nổi được tài trợ bằng nợ thả nổi theo một chỉ số khác;
- tiền gửi có kỳ hạn lãi suất cố định chỉ tái định giá khi đáo hạn;
- swap và FRA tái định giá 3 tháng, trong khi tiền gửi không kỳ hạn tái định giá theo một lãi suất cơ bản ngắn hạn khác;
- tài khoản giao dịch không nhạy lãi suất;
- số dư ròng không nhạy lãi suất, gồm cả vốn chủ sở hữu.

Năm nguồn IRRBB theo Choudhry là gap, yield curve, basis, run-off và option [[src-choudhry-principles-banking#^choudhry-cs-12]]. Xem [[gap-risk]], [[basis-risk]], [[option-risk]].

**Macro hedge.** Trong thực tế, ngân hàng phòng ngừa IRRBB ở mức macro. Ví dụ, ngân hàng không làm một IRS cho từng khoản vay thế chấp lãi suất cố định, mà gom số dư phát sinh trong tháng rồi vào một pool IRS cuối tháng. Vì vậy ngân hàng thường không áp được [[hedge-accounting]], và phải chịu biến động P&L mark-to-market của macro hedge bằng phái sinh [[src-choudhry-principles-banking#^choudhry-cs-14]]. Xem [[interest-rate-swap]].

**Hai cách phòng ngừa** (case study 5, một ngân hàng thương mại EU):

| Cách | Nội dung | Hệ quả | Nguồn |
|---|---|---|---|
| Chính thống | Phòng ngừa riêng từng phía khi rủi ro phát sinh và luôn dùng phái sinh. Tài sản cố định dùng IRS trả cố định, nợ cố định dùng IRS nhận cố định | Thiếu góc nhìn "strategic ALM" cho cả hai phía; không giảm thiểu việc dùng phái sinh, trong khi chi phí tài sản bảo đảm không phải lúc nào cũng minh bạch | [[src-choudhry-principles-banking#^choudhry-cs-16]] |
| Structural, theo phần ròng | Khớp tài sản và nợ có tenor hành vi tương tự; chỉ phòng ngừa phần ròng ra thị trường; ưu tiên sản phẩm tiền mặt | Hiệu quả vận hành tốt hơn, chi phí phòng ngừa thấp hơn, biến động P&L MTM giảm | [[src-choudhry-principles-banking#^choudhry-cs-17]] [[src-choudhry-principles-banking#^choudhry-cs-18]] |

**Các cặp natural hedge** [[src-choudhry-principles-banking#^choudhry-cs-17]]:
- vay lãi suất cố định với tiền gửi lãi suất cố định;
- vay thả nổi với tiền gửi thả nổi;
- vay thế chấp thả nổi với NIBL có tenor hành vi tương tự;
- vay thế chấp cố định với tiền gửi cố định.

**Công cụ phòng ngừa (Choudhry Ch6).**
- Phòng ngừa tốt nhất cho một giao dịch là giao dịch đối ứng chính xác. Cách này không phải lúc nào cũng làm được hoặc nên làm, vì ăn vào biên lợi nhuận, nhưng giảm basis risk [[src-choudhry-principles-banking#^choudhry-hedge-3]].
- Trong phần lớn trường hợp, FRA, futures và swap là đủ; trong một số trường hợp, ALM desk có thể muốn dùng option [[src-choudhry-principles-banking#^choudhry-hedge-19]]. Xem [[forward-rate-agreement]], [[interest-rate-futures]], [[interest-rate-swap]], [[interest-rate-cap-floor]].
- Hedge ratio theo PVBP giả định đường cong dịch chuyển song song, nên tạo sai số phòng ngừa đáng kể theo thời gian; khắc phục bằng dynamic hedging [[src-choudhry-principles-banking#^choudhry-hedge-14]].
- Khi cho vay cố định được tài trợ bằng tiền gửi bám theo lãi suất cơ bản, ngân hàng có thể dùng OIS để phòng ngừa NII [[src-choudhry-principles-banking#^choudhry-hedge-18]]. Xem [[overnight-index-swap]].

**Phòng ngừa EAR bằng option (ví dụ 6.12).** Ngân hàng bán lẻ giả định có bảng cân đối 200 triệu USD và gap tức thời −80. Lãi suất +1% song song làm NII giảm 800.000 USD, tức EAR khoảng 7,8% [[src-choudhry-principles-banking#^choudhry-hedge-21]]. Các cách xử lý:

| Cách | Tác động | Nguồn |
|---|---|---|
| Sản phẩm tiền mặt: giảm nợ thả nổi, tăng tài sản thả nổi | Không làm được ngay | [[src-choudhry-principles-banking#^choudhry-hedge-22]] |
| Mua cap notional 80 triệu USD, strike 3%, 1 năm | Loại bỏ hoàn toàn EAR; chi phí 5bp NIM | [[src-choudhry-principles-banking#^choudhry-hedge-23]] [[src-choudhry-principles-banking#^choudhry-hedge-24]] |
| Cap strike 4% (out-of-the-money) | Phí thấp hơn, còn lại một phần EAR | [[src-choudhry-principles-banking#^choudhry-hedge-23]] |
| Swap hoặc FRA | Loại bỏ biến động thu nhập cả hai chiều, không giữ lợi khi lãi suất giảm | [[src-choudhry-principles-banking#^choudhry-hedge-24]] |

Ngân hàng asset-sensitive làm ngược lại: mua floor [[src-choudhry-principles-banking#^choudhry-hedge-25]].

**Dùng sản phẩm tiền mặt thay phái sinh.** Khi có thể, nên dùng sản phẩm tiền mặt thay vì phái sinh, ví dụ để giữ hạn mức swap hoặc giảm nhu cầu vốn cho tài sản bảo đảm [[src-choudhry-principles-banking#^choudhry-cs-17]].

## Phụ thuộc regime
- Hiệu quả của natural hedge phụ thuộc vào việc khớp tenor **hành vi**, không phải tenor hợp đồng [[src-choudhry-principles-banking#^choudhry-cs-17]]. Xem [[non-maturity-deposits]], [[behavioural-options]].
- *Diễn giải:* khi lãi suất tăng nhanh, tenor hành vi của NIBL có thể rút ngắn, như trường hợp SVB ([[silicon-valley-bank]]). Khi đó cặp "vay thế chấp thả nổi – NIBL" không còn khớp, và phần ròng cần phòng ngừa thay đổi. Nguồn không bàn trường hợp này (ngoài wiki, chưa có nguồn).

## Góc nhìn theo domain
- **ALM**: ngân hàng trong case study báo cáo IRRBB bằng cả [[duration|modified duration]] (DV01) và VaR [[src-choudhry-principles-banking#^choudhry-cs-15]]. Repricing gap của một ngân hàng thương mại Anh cho thấy:
  - gap −60.537 triệu GBP ở dải O/N–3 tháng [[src-choudhry-principles-banking#^choudhry-cs-15]];
  - gap luỹ kế quay về 0 sau phần không nhạy lãi suất (10.700 triệu GBP) [[src-choudhry-principles-banking#^choudhry-cs-15]].

  Xem [[repricing-gap-analysis]], [[pv01]].
- **ALM (Bardaeva, T4)**:
  - Công cụ quản lý IRRBB gồm phòng ngừa bằng phái sinh, đầu tư equity, công cụ không nhạy lãi suất, dự báo lãi suất và kế hoạch bảng cân đối [[src-bardaeva-alm#^ch11-18]].
  - Thị trường bất định với kỳ hạn huy động tối đa 1 năm cho tài sản dài hạn đòi hỏi dùng IRS (thường kèm phái sinh FX) để phòng ngừa IRR [[src-bardaeva-alm#^ch12-13]].
  - Ở thị trường không phòng ngừa được mọi rủi ro, Group Treasury tối thiểu hoá vị thế với rủi ro phòng ngừa được và kiểm soát chặt rủi ro không phòng ngừa được [[src-bardaeva-alm#^ch12-2]] [[src-bardaeva-alm#^ch12-15]]. Xem [[irrbb-management]].
- **Product**: theo chính sách của ngân hàng trong case study, IRS là công cụ phòng ngừa chính [[src-choudhry-principles-banking#^choudhry-cs-16]]. Xem [[interest-rate-swap]].
- **Basel/VN**: phần d368 và TT83/2025 đã ingest không quy định cách phòng ngừa theo phần ròng hay theo từng giao dịch [cần nguồn]. Theo TT83/2025, giao dịch phái sinh phòng ngừa rủi ro cho các khoản mục của báo cáo tình hình tài chính, kể cả ngoại bảng, được ghi nhận vào sổ ngân hàng [[src-tt83-2025-nhnn#^d3-33]]. Xem [[banking-book]]. *Diễn giải:* việc chọn giữa structural hedging và phòng ngừa riêng từng giao dịch là quyết định của ALCO ([[alco]]).

## Bằng chứng thực nghiệm
- Case study 5 (ngân hàng thương mại EU): sau khi chuyển sang phòng ngừa theo phần ròng, ngân hàng cải thiện đáng kể hiệu quả vận hành, giảm chi phí phòng ngừa và giảm biến động P&L MTM [[src-choudhry-principles-banking#^choudhry-cs-18]]. Thay đổi bắt đầu khi CFO và Treasurer nghe tác giả trình bày về "Strategic ALM" ([[strategic-alm]]) và mời trình bày lại tại ALCO [[src-choudhry-principles-banking#^choudhry-cs-17]]. Bằng chứng này từ một nguồn T4, tác giả là người tư vấn trực tiếp cho case.

## Câu hỏi mở
- Nguồn không định lượng mức giảm chi phí phòng ngừa [cần nguồn].
- Hedge accounting: đã có node [[hedge-accounting]]. Tiêu chí áp dụng gồm kiểm tra hiệu quả hồi tố trong khoảng 80–125% [[src-choudhry-principles-banking#^choudhry-hacc-3]], và có phân biệt micro với macro hedge accounting [[src-choudhry-principles-banking#^choudhry-hacc-4]]. Chi tiết portfolio fair value hedge cho macro hedge vẫn chưa có nguồn [cần nguồn].
