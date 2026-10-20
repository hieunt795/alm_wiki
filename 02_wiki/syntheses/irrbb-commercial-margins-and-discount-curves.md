---
title: "Phương Pháp Luận Bóc Tách Biên Thương Mại và Lựa Chọn Đường Cong Chiết Khấu EVE (Deduct vs Include)"
aliases: [IRRBB Commercial Margin Unbundling and Discount Curves, Phuong phap boc tach bien thuong mai va duong cong chiet khau EVE, Commercial Margins Deduct vs Include]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Phương pháp luận bóc tách Biên thương mại (Commercial Margin Unbundling) và lựa chọn đường cong chiết khấu dòng tiền EVE (Deduct vs Include)"
as_of: 2026-10-19
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tata-bank-alm]]", "[[src-tt83-2025-nhnn]]"]
relations: []
tags: [irrbb, commercial-margin, discount-curve, eve, nii, deduct-margin, include-margin, csrbb, basel, synthesis]
updated: 2026-10-19
reviewed:
---

## Câu hỏi

1. **Q1 (Bản chất kinh tế của Biên thương mại)**: Biên thương mại (Commercial Margin / Customer Spread) trong sổ ngân hàng được định nghĩa như thế nào? Vì sao hệ thống FTP bắt buộc phải bóc tách rạch ròi giữa rủi ro chuyển đổi kỳ hạn (Maturity Transformation) và thương quyền khách hàng (Customer Franchise) theo BCBS d368 và Moorad Choudhry?
2. **Q2 (Phương pháp Khấu trừ Biên thương mại — Deduct Approach)**: Cơ chế kỹ thuật bóc tách biên thương mại khỏi dòng tiền tái định giá danh nghĩa (Par 102–103 BCBS d368): Dòng tiền được chiết khấu theo đường cong phi rủi ro (Risk-free Curve) ra sao, ưu điểm về tính miễn nhiễm rủi ro tín dụng và giới hạn trong việc phản ánh giá trị kinh tế của vốn?
3. **Q3 (Phương pháp Giữ lại Biên thương mại — Include Approach)**: Cơ chế giữ lại biên thương mại trong dòng tiền dự phóng: Yêu cầu bắt buộc về đường cong chiết khấu (Risk-free Curve + Commercial Spread) theo Nguyên tắc 8 BCBS d368 để tránh làm biến dạng giá trị kinh tế?
4. **Q4 (Nguyên tắc Nhất quán Xuyên suốt và Ranh giới CSRBB)**: Yêu cầu nhất quán toàn diện giữa tài sản và nợ (Internal consistency across assets and liabilities): Nguy cơ méo mó khi áp dụng bất đối xứng và ranh giới phân định với rủi ro chênh lệch tín dụng trên sổ ngân hàng (CSRBB)?
5. **Q5 (Khung Quy định: Basel vs Ngân hàng Nhà nước Việt Nam)**: Chuẩn mực BCBS d368 và Thông tư 83/2025/TT-NHNN (C3-M7, PL5) quy định như thế nào về quyền lựa chọn giữa Deduct và Include? Đâu là khoảng trống pháp lý tại Việt Nam?

## Kết luận

Synthesis `draft`, dựa trên source note `draft` của BCBS d368 (2016), Choudhry và Tata; cột VN chưa có nguồn NHNN.

- **Về bản chất kinh tế (Q1)**: Choudhry nêu việc tách chuyển đổi kỳ hạn rủi ro (*risky maturity transformation*) khỏi thương quyền khách hàng phi rủi ro (*risk-free customer franchise*) là một hệ quả của hệ thống FTP [[src-choudhry-principles-banking#^choudhry-ftp-13]]; FTP là cơ chế chuyển giao rủi ro nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-10]]. Định nghĩa commercial margin theo con số cụ thể: [cần nguồn]; các claim đã ingest của d368 dùng thuật ngữ "commercial margins and other spread components" mà không định nghĩa.
- **Về phương pháp Khấu trừ — Deduct Approach (Q2)**: Par 103 cho ngân hàng chọn có trừ commercial margin và spread component khác khỏi notional repricing cash flow hay không, với phương pháp thận trọng và minh bạch [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. Khi đã trừ, dòng tiền nên được chiết khấu bằng risk-free rate [[src-bcbs-irrbb-2016#^irrbb-u05-19]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Về phương pháp Giữ lại — Include Approach (Q3)**: Risk-free rate cộng commercial margin và spread component chỉ được dùng làm lãi suất chiết khấu khi ngân hàng đã đưa các phần này vào dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-19]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Discount factor phải đại diện cho risk-free zero coupon rate; secured interest rate swap curve là một ví dụ được chấp nhận [[src-bcbs-irrbb-2016#^irrbb-u05-19]].
- **Về nguyên tắc nhất quán và ranh giới CSRBB (Q4)**: Wiki chưa có nguồn cho yêu cầu áp cùng một phương pháp trên cả tài sản và nợ: par 103 không nêu yêu cầu này [[src-bcbs-irrbb-2016#^irrbb-u05-15]], và câu trích "applied consistently across all interest rate-sensitive assets and liabilities" ở bản trước không có trong raw d368 `[cần nguồn]`. Về CSRBB, Choudhry chỉ nêu CSRBB tác động lên danh mục trái phiếu FVOCI và đo bằng CS01 [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
- **Về quy định tại Việt Nam (Q5)**: BCBS d368 để ngân hàng chọn Deduct hoặc Include [[src-bcbs-irrbb-2016#^irrbb-u05-15]] và yêu cầu công bố ∆EVE, ∆NII dưới các kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-p08-1]]. Ngân hàng nên công bố đã loại trừ hay đưa commercial margin vào dòng tiền ∆EVE [[src-bcbs-irrbb-2016#^irrbb-p08-4]] và đã chiết khấu bằng risk-free rate hay risk-free rate cộng margin [[src-bcbs-irrbb-2016#^irrbb-p08-5]]; Table A dòng g yêu cầu mô tả hai giả định này [[src-bcbs-irrbb-2016#^irrbb-p08-6]]. Tại Việt Nam, Phụ lục V của [[tt83-2025]] chỉ quy định chiết khấu dòng tiền ΔEVE theo lãi suất phi rủi ro (risk-free rate) [[src-tt83-2025-nhnn#^pl5-a3-2]] và không nói về việc trừ hay giữ commercial margin; C3-M7 và Phụ lục V không có yêu cầu công bố lựa chọn này.

## Cơ chế

### Q1 — Bản chất kinh tế của Biên thương mại: Phân tách Thương quyền vs Chuyển đổi kỳ hạn

Chi tiết FTP ở [[ftp-pricing-methodology]]. *Diễn giải:* lãi suất hợp đồng có thể được tách thành hai phần:

$$\text{Lãi suất Hợp đồng} = \text{Lãi suất Cơ sở Thị trường (Market Base Rate)} + \text{Biên thương mại (Commercial Margin)}$$

Công thức trên là khung phân tích, không chép từ nguồn.

1. **Lãi suất Cơ sở Thị trường (Market Base Rate / Risk-free Transfer Rate)**:
   - Choudhry nêu nguyên tắc trùng khớp kỳ hạn (*matched-maturity principle*) là một thuộc tính của FTP [[src-choudhry-principles-banking#^choudhry-ftp-11]].
   - Phần chuyển đổi kỳ hạn được Choudhry gọi là "risky" maturity transformation [[src-choudhry-principles-banking#^choudhry-ftp-13]]. *Diễn giải:* đây là phần mang IRRBB, được chuyển về Treasury qua FTP.

2. **Biên thương mại (Commercial Margin / Customer Franchise Spread)**:
   - Phần thương quyền khách hàng được Choudhry gọi là "riskfree" customer franchise [[src-choudhry-principles-banking#^choudhry-ftp-13]].
   - FTP không phải là phòng ngừa rủi ro ra bên ngoài, cũng không phải điều chuyển vốn vật lý nội bộ, mà là chuyển giao rủi ro nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-10]].
   - *Diễn giải:* (ngoài wiki, chưa có nguồn) trên tài sản, biên thương mại là phần lãi suất cho vay vượt lãi suất FTP; trên nợ, là phần lãi suất FTP vượt lãi suất huy động.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               PHÂN TÁCH LÃI SUẤT HỢP ĐỒNG TRONG HỆ THỐNG ALM & FTP                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  LÃI SUẤT DANH NGHĨA HỢP ĐỒNG = LÃI SUẤT CƠ SỞ + BIÊN THƯƠNG MẠI                       │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│  LÃI SUẤT CƠ SỞ PHI RỦI RO                │  BIÊN THƯƠNG MẠI CỐ ĐỊNH                   │
│  - Chuyển giao về ALM / Treasury          │  - Để lại cho Khối Kinh doanh              │
│  - Quản trị: Rủi ro Lãi suất (IRRBB)      │  - Phản ánh: Thương quyền khách hàng       │
│  - Biến động theo đường cong thị trường   │  - Bản chất: Cố định theo hợp đồng         │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

### Q2 — Phương pháp Khấu trừ Biên thương mại (Deduct Approach)

Par 103 cho ngân hàng chọn có trừ commercial margin và spread component khác khỏi notional repricing cash flow hay không, với phương pháp thận trọng và minh bạch [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. Lựa chọn này thuộc bước slot dòng tiền; việc chọn lãi suất chiết khấu nằm ở par 132 và par 70 [[src-bcbs-irrbb-2016#^irrbb-u05-19]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

1. **Cơ chế kỹ thuật bóc tách dòng tiền**:
   - Notional repricing cash flow gồm hoàn trả gốc, tái định giá gốc và thanh toán lãi trên phần gốc chưa hoàn trả hay chưa tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-9]]. Với Deduct, phần commercial margin và spread component được trừ khỏi các dòng tiền này [[src-bcbs-irrbb-2016#^irrbb-u05-15]].
   - *Diễn giải:* dòng tiền dự phóng tại kỳ $t$ khi đó có dạng:

     $$\text{CF}_{\text{deduct}}(t) = \text{Principal}(t) + \text{Balance}(t) \cdot r_{\text{risk-free}}(t) \cdot \Delta t$$

   - Dòng hoàn trả gốc và tái định giá gốc không chứa spread nên không bị ảnh hưởng bởi lựa chọn này [[src-bcbs-irrbb-2016#^irrbb-u05-9]].

2. **Lựa chọn đường cong chiết khấu**:
   - Dòng tiền nên được chiết khấu bằng risk-free rate; discount factor phải đại diện cho risk-free zero coupon rate, ví dụ secured interest rate swap curve [[src-bcbs-irrbb-2016#^irrbb-u05-19]] [[src-bcbs-irrbb-2016#^irrbb-p08-5]].
   - Trong khuôn khổ chuẩn hoá, discount factor có dạng liên tục [[src-bcbs-irrbb-2016#^irrbb-u05-18]]:

     $$DF_{i,c}(t_k) = \exp(-R_{i,c}(t_k) \cdot t_k)$$

   - *Diễn giải:* EVE theo Deduct là tổng $\text{CF}_{\text{deduct}}(t_k) \cdot DF(t_k)$ theo các dải; công thức 4 bước của par 132 ở [[irrbb-standardised-shocks-eve-and-nii-measurement]].

3. **Ưu điểm và giới hạn kỹ trị**:
   - *Diễn giải:* (ngoài wiki, chưa có nguồn) Deduct cho dòng tiền chỉ phản ánh phần lãi suất phi rủi ro, nên ∆EVE không lẫn biến động spread khách hàng; đổi lại, EVE không gồm giá trị của biên thương mại tương lai.

### Q3 — Phương pháp Giữ lại Biên thương mại (Include Approach)

Mức độ phổ biến của Include tại các nhóm ngân hàng: [cần nguồn].

1. **Cơ chế kỹ thuật**:
   - Với Include, ngân hàng không trừ commercial margin khỏi notional repricing cash flow [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. *Diễn giải:* dòng tiền dự phóng khi đó có dạng:

     $$\text{CF}_{\text{include}}(t) = \text{Principal}(t) + \text{Balance}(t) \cdot \left(r_{\text{risk-free}}(t) + s_{\text{margin}}\right) \cdot \Delta t$$

   - Với công cụ thả nổi, toàn bộ gốc được slot vào dải chứa first reset date, còn phần spread không tái định giá được slot tới contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-11]] [[src-bcbs-irrbb-2016#^irrbb-u05-12]].
   - Với $\Delta\text{NII}$ công bố, dòng tiền dự kiến nên gồm commercial margin và spread component [[src-bcbs-irrbb-2016#^irrbb-p08-3]].

2. **Lựa chọn đường cong chiết khấu**:
   - Risk-free rate cộng commercial margin và spread component chỉ được dùng khi ngân hàng đã đưa các phần này vào dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-19]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. *Diễn giải:* khi đó lãi suất chiết khấu có dạng:

     $$r_{\text{discount}}(t) = r_{\text{risk-free}}(t) + s_{\text{margin}}(t)$$

   - Footnote 29 vẫn yêu cầu discount factor đại diện cho risk-free zero coupon rate [[src-bcbs-irrbb-2016#^irrbb-u05-19]]. *Diễn giải:* nguồn không giải thích cách hai yêu cầu này cùng áp dụng khi lãi suất chiết khấu đã cộng margin (xem `## Bất định`).

3. **Quy tắc toán học tránh biến dạng hiện giá**:
   - Par 132 và par 70 chỉ cho cộng margin vào lãi suất chiết khấu khi margin đã có trong dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-19]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Giá trị kinh tế là tổng hiện giá dòng tiền chiết khấu theo lãi suất phù hợp với môi trường hiện hành [[src-tata-bank-alm#^tata-ev-1]].
   - *Diễn giải:* (ngoài wiki, chưa có nguồn) dòng tiền có margin chiết khấu bằng risk-free rate sẽ cho hiện giá cao hơn mệnh giá; dòng tiền và lãi suất chiết khấu cùng chứa spread $s$ thì hiện giá ban đầu xấp xỉ mệnh giá.

### Bảng So sánh Đối chiếu Hai Phương pháp Luận

| Tiêu chí | Khấu trừ Biên thương mại (Deduct Margins) | Giữ lại Biên thương mại (Include Margins) |
|---|---|---|
| **Dòng tiền dự phóng $\text{CF}(t)$** | Trừ commercial margin và spread component khỏi notional repricing cash flow [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. | Giữ commercial margin và spread component trong dòng tiền [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. |
| **Đường cong chiết khấu** | Risk-free rate; ví dụ secured interest rate swap curve [[src-bcbs-irrbb-2016#^irrbb-u05-19]]. | Risk-free rate cộng commercial margin và spread component [[src-bcbs-irrbb-2016#^irrbb-u05-19]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. |
| **Mức độ phức tạp mô hình** | [cần nguồn] | [cần nguồn] |
| **Tính nhạy cảm lãi suất ($\Delta\text{EVE}$)** | *Diễn giải:* (ngoài wiki, chưa có nguồn) chỉ phản ánh biến động lãi suất phi rủi ro. | *Diễn giải:* (ngoài wiki, chưa có nguồn) có thể chịu thêm biến động spread nếu spread chiết khấu được cập nhật theo thị trường. |
| **Thích hợp cho danh mục** | [cần nguồn] | [cần nguồn] |

### Q4 — Nguyên tắc Nhất quán Xuyên suốt và Ranh giới CSRBB

1. **Nguyên tắc Nhất quán Toàn diện (Internal Consistency — Principle 8)**:
   - Câu trích "A bank should decide whether to deduct or include commercial margins… The approach should be applied consistently across all interest rate-sensitive assets and liabilities" ở bản trước của synthesis này không có trong raw d368 (đã grep u03, u04, u05 ngày 2026-10-18). Đã bỏ câu trích.
   - Principle 8 trong source note là nguyên tắc **công bố thông tin**: thông tin về mức IRRBB và thực hành đo lường phải được công bố, ngân hàng phải công bố ∆EVE và ∆NII dưới các kịch bản sốc ở Annex 2 [[src-bcbs-irrbb-2016#^irrbb-p08-1]]. Yêu cầu nhất quán Deduct/Include giữa tài sản và nợ: `[cần nguồn]`.
   - *Diễn giải:* (ngoài wiki, chưa có nguồn) nếu ngân hàng trừ margin trên một vế của bảng cân đối mà giữ margin trên vế kia, phần coupon tính vào hai vế sẽ khác bản chất, nên khe hở tái định giá và ∆EVE phản ánh cả chênh lệch phương pháp chứ không chỉ chênh lệch lãi suất.

2. **Ranh giới Tương tác với CSRBB (Credit Spread Risk in the Banking Book)**:
   - Choudhry nêu CSRBB áp cho danh mục trái phiếu Eurobonds hạch toán FVOCI, có giá trị thay đổi theo credit spread ngoài các kịch bản sốc, và được đo bằng CS01 (biến động PV cho 1 bp credit spread) [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
   - *Diễn giải:* (ngoài wiki, chưa có nguồn) nếu ngân hàng chọn Include và cập nhật spread chiết khấu theo thị trường, ∆EVE có thể chứa một phần biến động credit spread, tức chồng lấn với CSRBB. Nguồn đã ingest không nói về quan hệ Include–CSRBB. Chi tiết CSRBB ở [[irrbb-csrbb-measurement-and-hedging]].

### Q5 — Khung Quy định: So sánh Basel d368 vs Ngân hàng Nhà nước Việt Nam

- **Chuẩn mực Basel (BCBS d368)**:
  - Ngân hàng được chọn trừ hay giữ commercial margin trong notional repricing cash flow, với phương pháp thận trọng và minh bạch [[src-bcbs-irrbb-2016#^irrbb-u05-15]]. Ngân hàng phải công bố ∆EVE và ∆NII dưới các kịch bản sốc ở Annex 2 [[src-bcbs-irrbb-2016#^irrbb-p08-1]].
  - Ngân hàng nên (should) công bố đã loại trừ hay đưa commercial margin và spread component vào dòng tiền ∆EVE [[src-bcbs-irrbb-2016#^irrbb-p08-4]].
  - Ngân hàng nên công bố đã chiết khấu dòng tiền bằng risk-free rate hay risk-free rate cộng commercial margin; lựa chọn sau chỉ dùng được khi margin đã có trong dòng tiền [[src-bcbs-irrbb-2016#^irrbb-p08-5]].
  - Table A (công bố định tính, bắt buộc với ngân hàng trong phạm vi Section III) dòng g yêu cầu mô tả việc dòng tiền ∆EVE có gồm commercial margin hay không và lãi suất chiết khấu đã dùng [[src-bcbs-irrbb-2016#^irrbb-p08-6]].
  - Với $\Delta\text{NII}$ công bố, ngân hàng nên đưa commercial margin và spread component vào dòng tiền dự kiến, theo giả định constant balance sheet [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- **Quy định Ngân hàng Nhà nước Việt Nam**:
  - [[tt83-2025]] có hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]] và là căn cứ tại Việt Nam; Basel d368 là tham chiếu. Phụ lục V yêu cầu dòng tiền ròng tại mỗi thang kỳ hạn được chiết khấu theo lãi suất phi rủi ro (risk-free rate) [[src-tt83-2025-nhnn#^pl5-a3-2]]. Phụ lục V không có phương án risk-free cộng margin như par 132 d368 [[src-bcbs-irrbb-2016#^irrbb-u05-19]].
  - Quản trị rủi ro mô hình nằm ở Chương 3 Mục 8; nội dung liên quan tới đường cong chiết khấu chưa kiểm `[cần nguồn: src-tt83-2025-nhnn C3-M8]`.
  - *Khoảng trống pháp lý tại Việt Nam*: định nghĩa dòng tiền trong Phụ lục V gồm trả gốc, định giá lại gốc và trả lãi [[src-tt83-2025-nhnn#^pl5-a1-1c]], nhưng không nói phần lãi có gồm commercial margin hay không. Với ΔNII, Phụ lục V chỉ nêu chân trời 01 năm và constant balance sheet [[src-tt83-2025-nhnn#^pl5-b2]].
  - *Diễn giải:* nếu ngân hàng giữ margin trong dòng tiền ΔEVE nhưng chỉ được chiết khấu bằng risk-free rate theo PL5.A.III.2, ΔEVE sẽ gồm giá trị hiện tại của margin. Cách NHNN xử lý trường hợp này chưa có nguồn.

## Bằng chứng ủng hộ

- **Ủy ban Basel (BCBS d368)**: Par 103 cho phép hai lựa chọn Deduct/Include [[src-bcbs-irrbb-2016#^irrbb-u05-15]]; par 132(2) và footnote 29 gắn lãi suất chiết khấu với lựa chọn đó [[src-bcbs-irrbb-2016#^irrbb-u05-19]]; par 70 nhắc lại quy tắc chiết khấu cho ∆EVE công bố [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Moorad Choudhry (2022)**: Nêu việc tách chuyển đổi kỳ hạn rủi ro khỏi thương quyền khách hàng phi rủi ro là hệ quả của FTP [[src-choudhry-principles-banking#^choudhry-ftp-13]].
- **Fidelio Tata (2025)**: Giá trị kinh tế là tổng hiện giá dòng tiền, chiết khấu bằng lãi suất phù hợp với môi trường lãi suất hiện hành [[src-tata-bank-alm#^tata-ev-1]].

## Bằng chứng trái chiều

- Không ghi nhận nguồn đã ingest nói ngược chiều về lựa chọn Deduct/Include.
- *Diễn giải:* (ngoài wiki, chưa có nguồn) Include đòi hỏi ước tính spread chiết khấu cho từng danh mục; Deduct cho ∆EVE khác với thu nhập kế toán vì bỏ phần biên thương mại. Cả hai nhận định chưa có nguồn.

## Phụ thuộc regime

- **Môi trường Biên tín dụng Thị trường Dãn rộng (Credit Spread Widening)**:
  - *Diễn giải:* (ngoài wiki, chưa có nguồn) với Include, nếu spread chiết khấu được cập nhật theo thị trường, spread dãn rộng làm giảm hiện giá tài sản dù risk-free rate không đổi; với Deduct, ∆EVE không phản ánh biến động này. Danh mục FVOCI chịu CSRBB đo bằng CS01 [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
- **Môi trường Cạnh tranh về Biên lãi thuần (NIM Compression)**:
  - *Diễn giải:* (ngoài wiki, chưa có nguồn) khi biên thương mại của giao dịch mới thu hẹp, ngân hàng dùng Include phải điều chỉnh spread trong dòng tiền và lãi suất chiết khấu, làm EVE thay đổi không do sốc lãi suất.

## Hàm ý ALM / quy định

Chưa có nguồn NHNN trong wiki cho chủ đề này; các điểm dưới đây dựa trên BCBS d368, là tham chiếu chứ không phải nghĩa vụ tại VN.

- **Đối với ALM / Treasury**:
  - *Diễn giải:* hệ thống tính EVE có thể chạy cả hai phương án Deduct và Include để đối chiếu, vì d368 cho phép cả hai [[src-bcbs-irrbb-2016#^irrbb-u05-15]].
  - *Diễn giải:* đường cong chiết khấu nên được xây cùng nguyên tắc matched-maturity với đường cong FTP [[src-choudhry-principles-banking#^choudhry-ftp-11]].
- **Đối với ALCO**:
  - *Diễn giải:* par 103 yêu cầu phương pháp thận trọng và minh bạch [[src-bcbs-irrbb-2016#^irrbb-u05-15]], nên ALCO cần phê duyệt lựa chọn Deduct/Include bằng văn bản.
  - *Diễn giải:* đổi phương pháp giữa các kỳ báo cáo làm ∆EVE không so sánh được với ngưỡng outlier 15% Tier 1 capital [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
- **Đối với Ngân hàng Nhà nước Việt Nam**:
  - *Diễn giải:* (ngoài wiki, chưa có nguồn) cách các NHTM Việt Nam ghi nhận dòng tiền (gộp hay tách margin) chưa có nguồn. Nếu PL5 TT83 không quy định lựa chọn này, dữ liệu IRRBB giữa các ngân hàng có thể không so sánh được.

## Bất định
- **Hướng dẫn kỹ thuật Phụ lục 5 Thông tư 83/2025/TT-NHNN**: đã ingest [2026-10-19]; PL5 không quy định bóc tách hay giữ commercial margin, chỉ quy định chiết khấu theo risk-free rate [[src-tt83-2025-nhnn#^pl5-a3-2]]. Phần còn có thể liên quan: C3-M8 (rủi ro mô hình, đường cong chiết khấu) `[cần nguồn: src-tt83-2025-nhnn C3-M8]`.
- **Claim bỏ sót ở u03 (unit đã `done`)**: raw par 70(b) "Banks should disclose whether they have excluded or included commercial margins and other spread components…" và 70(c) "Banks should disclose whether they have d…" (u03 dòng 260–261), Table B dòng 296. Claim [[src-bcbs-irrbb-2016#^irrbb-p08-2]] lược bỏ hai câu này. Gỡ Q5 (yêu cầu công bố lựa chọn). Đề xuất `/ingest src-bcbs-irrbb-2016 u03`. → đã bổ sung [2026-10-18]: [[src-bcbs-irrbb-2016#^irrbb-p08-4]], [[src-bcbs-irrbb-2016#^irrbb-p08-5]], [[src-bcbs-irrbb-2016#^irrbb-p08-6]] (dòng 296 thuộc Table A, không phải Table B).
- **Yêu cầu nhất quán Deduct/Include giữa tài sản và nợ**: không tìm thấy trong u03, u04, u05 của d368 `[cần nguồn]`. Không có trong TT83 PL5 (đã ingest [2026-10-19]); có thể có trong EBA GL (chưa register).
- **Footnote 29** (và footnote 12 của par 70, cùng nội dung, [[src-bcbs-irrbb-2016#^irrbb-p08-5]]): yêu cầu discount factor "representative of a risk-free zero coupon rate" cùng lúc với lựa chọn risk-free rate cộng margin [[src-bcbs-irrbb-2016#^irrbb-u05-19]]; cách hai yêu cầu cùng áp dụng chưa có nguồn giải thích.
- **Phương pháp bóc tách Biên thương mại trên danh mục cho vay thả nổi**: *Diễn giải:* (ngoài wiki, chưa có nguồn) biên thương mại của khoản vay thả nổi thường cố định theo hợp đồng trong khi chi phí huy động thay đổi; cố định biên khi chiết khấu dòng tiền dài hạn có thể tạo sai số mô hình.
- [2026-10-18] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 91): có claim [[src-bcbs-irrbb-2016#^irrbb-p12-5]] — supervisor nên xét tác động của giả định giữ/trừ commercial margin lên ∆EVE khi đánh giá vốn; cần rà lại Q4, Q5.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M2: đã có node [[credit-risk-management]]; TT83 Đ26.2.c yêu cầu nguyên tắc đưa chi phí bù đắp rủi ro tín dụng vào định giá sản phẩm tín dụng theo mức rủi ro khách hàng [[src-tt83-2025-nhnn#^d26-2c]] (văn bản NHNN đầu tiên trong wiki chạm tới pricing tín dụng); cần rà lại mục Hàm ý ALM / quy định.
