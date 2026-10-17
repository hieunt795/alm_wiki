---
title: "Phương Pháp Luận Bóc Tách Biên Thương Mại và Lựa Chọn Đường Cong Chiết Khấu EVE (Deduct vs Include)"
aliases: [IRRBB Commercial Margin Unbundling and Discount Curves, Phuong phap boc tach bien thuong mai va duong cong chiet khau EVE, Commercial Margins Deduct vs Include]
type: synthesis
domains: [alm, basel]
status: active
maturity: draft
origin: research
question: "Phương pháp luận bóc tách Biên thương mại (Commercial Margin Unbundling) và lựa chọn đường cong chiết khấu dòng tiền EVE (Deduct vs Include)"
as_of: 2026-10-17
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tata-bank-alm]]"]
relations: []
tags: [irrbb, commercial-margin, discount-curve, eve, nii, deduct-margin, include-margin, csrbb, basel, synthesis]
updated: 2026-10-17
reviewed:
---

## Câu hỏi

1. **Q1 (Bản chất kinh tế của Biên thương mại)**: Biên thương mại (Commercial Margin / Customer Spread) trong sổ ngân hàng được định nghĩa như thế nào? Vì sao hệ thống FTP bắt buộc phải bóc tách rạch ròi giữa rủi ro chuyển đổi kỳ hạn (Maturity Transformation) và thương quyền khách hàng (Customer Franchise) theo BCBS d368 và Moorad Choudhry?
2. **Q2 (Phương pháp Khấu trừ Biên thương mại — Deduct Approach)**: Cơ chế kỹ thuật bóc tách biên thương mại khỏi dòng tiền tái định giá danh nghĩa (Par 102–103 BCBS d368): Dòng tiền được chiết khấu theo đường cong phi rủi ro (Risk-free Curve) ra sao, ưu điểm về tính miễn nhiễm rủi ro tín dụng và giới hạn trong việc phản ánh giá trị kinh tế của vốn?
3. **Q3 (Phương pháp Giữ lại Biên thương mại — Include Approach)**: Cơ chế giữ lại biên thương mại trong dòng tiền dự phóng: Yêu cầu bắt buộc về đường cong chiết khấu (Risk-free Curve + Commercial Spread) theo Nguyên tắc 8 BCBS d368 để tránh làm biến dạng giá trị kinh tế?
4. **Q4 (Nguyên tắc Nhất quán Xuyên suốt và Ranh giới CSRBB)**: Yêu cầu nhất quán toàn diện giữa tài sản và nợ (Internal consistency across assets and liabilities): Nguy cơ méo mó khi áp dụng bất đối xứng và ranh giới phân định với rủi ro chênh lệch tín dụng trên sổ ngân hàng (CSRBB)?
5. **Q5 (Khung Quy định: Basel vs Ngân hàng Nhà nước Việt Nam)**: Chuẩn mực BCBS d368 và Thông tư 83/2025/TT-NHNN (C3-M7, PL5) quy định như thế nào về quyền lựa chọn giữa Deduct và Include? Đâu là khoảng trống pháp lý tại Việt Nam?

## Kết luận

- **Về bản chất kinh tế (Q1)**: Biên thương mại là phần bù chênh lệch giữa lãi suất hợp đồng thỏa thuận với khách hàng và lãi suất thị trường vốn tại cùng kỳ hạn chuyển giao [[src-choudhry-principles-banking#^choudhry-ftp-13]]. Hệ thống FTP phân tách rạch ròi giữa thương quyền khách hàng phi rủi ro (*risk-free customer franchise*) để lại cho đơn vị kinh doanh và chuyển đổi kỳ hạn mang rủi ro (*risky maturity transformation*) chuyển giao về Treasury quản trị tập trung [[src-choudhry-principles-banking#^choudhry-ftp-13]].
- **Về phương pháp Khấu trừ — Deduct Approach (Q2)**: Ngân hàng bóc tách hoàn toàn biên thương mại và spread tín dụng khỏi dòng tiền; dòng tiền còn lại chỉ thuần túy là lãi suất cơ sở phi rủi ro và nợ gốc [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. Dòng tiền này bắt buộc phải chiết khấu theo đường cong phi rủi ro thuần túy (Risk-free discount curve) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Phương pháp này phản ánh thuần túy rủi ro lãi suất thị trường nhưng bỏ qua lớp đệm thu nhập bảo vệ vốn [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Về phương pháp Giữ lại — Include Approach (Q3)**: Ngân hàng giữ nguyên biên thương mại trong toàn bộ dòng tiền dự phóng [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. Khi đó, theo Nguyên tắc 8 BCBS d368, đường cong chiết khấu bắt buộc phải cộng thêm phần bù biên thương mại và spread tương ứng (Risk-free rate + Commercial margins) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Nếu giữ lại biên thương mại trong dòng tiền nhưng lại chiết khấu bằng đường cong phi rủi ro thấp hơn, giá trị kinh tế của ngân hàng sẽ bị phóng đại ảo [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Về nguyên tắc nhất quán và ranh giới CSRBB (Q4)**: Ngân hàng phải áp dụng một phương pháp thống nhất cho cả tài sản và nợ phải trả, không được khấu trừ biên thương mại trên tài sản nhưng lại giữ lại biên thương mại trên nợ (hoặc ngược lại) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. Khi giữ lại biên thương mại, biến động của spread tín dụng thị trường trên các tài sản sẽ thẩm thấu vào hiện giá, làm mờ ranh giới giữa IRRBB và CSRBB [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
- **Về quy định tại Việt Nam (Q5)**: BCBS d368 cho phép ngân hàng quyền tự quyết lựa chọn Deduct hoặc Include nhưng phải công bố minh bạch tại Trụ cột 3 [[src-bcbs-irrbb-2016#^irrbb-p08-1]]. Tại Việt Nam, Thông tư 83/2025/TT-NHNN điều chỉnh IRRBB tại Chương 3 Mục 7 và Phụ lục 5 nhưng hướng dẫn kỹ thuật chi tiết về việc bắt buộc giữ lại hay cho phép khấu trừ biên thương mại đang ở trạng thái chờ ingest `[cần nguồn: src-tt83-2025-nhnn C3-M7, PL5]`.

## Cơ chế

### Q1 — Bản chất kinh tế của Biên thương mại: Phân tách Thương quyền vs Chuyển đổi kỳ hạn

Trong cơ chế định giá sản phẩm của ngân hàng thương mại, lãi suất danh nghĩa ký kết với khách hàng trên sổ ngân hàng luôn bao gồm hai thành phần độc lập:

$$\text{Lãi suất Hợp đồng} = \text{Lãi suất Cơ sở Thị trường (Market Base Rate)} + \text{Biên thương mại (Commercial Margin)}$$

1. **Lãi suất Cơ sở Thị trường (Market Base Rate / Risk-free Transfer Rate)**:
   - Phản ánh chi phí cơ hội của vốn trên thị trường tiền tệ hoặc thị trường trái phiếu chính phủ có cùng kỳ hạn và cấu trúc dòng tiền theo nguyên tắc Matched-Maturity [[src-choudhry-principles-banking#^choudhry-ftp-11]].
   - Chịu sự chi phối của chính sách tiền tệ và biến động cung cầu vốn vĩ mô; đây là nguồn gốc tạo ra rủi ro lãi suất sổ ngân hàng ([[bcbs-irrbb|IRRBB]]) và rủi ro chuyển đổi kỳ hạn (Maturity Transformation) [[src-choudhry-principles-banking#^choudhry-ftp-13]].

2. **Biên thương mại (Commercial Margin / Customer Franchise Spread)**:
   - Đại diện cho giá trị thương quyền khách hàng (Customer Franchise Value) mà đơn vị kinh doanh (Business Unit) đàm phán được với người vay hoặc người gửi tiền [[src-choudhry-principles-banking#^choudhry-ftp-13]]:
     - Trên tài sản (cho vay): Lãi suất cho vay cao hơn lãi suất thị trường vốn ($\text{Lãi suất cho vay} - \text{FTP Base} > 0$), bù đắp chi phí vận hành, chi phí vốn và rủi ro tín dụng.
     - Trên nợ (tiền gửi): Lãi suất huy động thấp hơn lãi suất thị trường ($\text{FTP Base} - \text{Lãi suất tiền gửi} > 0$), phản ánh thương quyền khai thác nguồn vốn giá rẻ.
   - Theo Giáo sư Moorad Choudhry, hệ thống định giá điều chuyển vốn nội bộ ([[ftp-pricing-methodology|FTP]]) ra đời nhằm mục đích tối thượng là chuyển giao toàn bộ rủi ro chuyển đổi kỳ hạn về Treasury/ALM quản trị tập trung, để lại phần biên thương mại thuần túy phi rủi ro lãi suất cho đơn vị kinh doanh [[src-choudhry-principles-banking#^choudhry-ftp-10]] [[src-choudhry-principles-banking#^choudhry-ftp-13]].

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               PHÂN TÁCH LÃI SUẤT HỢP ĐỒNG TRONG HỆ THỐNG ALM & FTP                     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  LÃI SUẤT DANH NGHĨA HỢP ĐỒNG (VD: Cho vay 10.5% = Base 6.5% + Spread 4.0%)            │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│  LÃI SUẤT CƠ SỞ PHI RỦI RO (6.5%)         │  BIÊN THƯƠNG MẠI CỐ ĐỊNH (4.0%)            │
│  - Chuyển giao về ALM / Treasury          │  - Để lại cho Khối Kinh doanh              │
│  - Quản trị: Rủi ro Lãi suất (IRRBB)      │  - Phản ánh: Thương quyền khách hàng       │
│  - Biến động theo đường cong thị trường   │  - Bản chất: Cố định theo hợp đồng         │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

### Q2 — Phương pháp Khấu trừ Biên thương mại (Deduct Approach)

Theo Đoạn 101–103 và Nguyên tắc 8 của chuẩn mực BCBS d368, ngân hàng được phép áp dụng phương pháp khấu trừ biên thương mại khi lập bảng phân bổ dòng tiền tái định giá danh nghĩa và tính toán giá trị kinh tế [[src-bcbs-irrbb-2016#^irrbb-u05-2]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

1. **Cơ chế kỹ thuật bóc tách dòng tiền**:
   - Toàn bộ cấu phần biên thương mại (commercial margin) và các khoản spread tín dụng được trừ khỏi dòng tiền lãi dự kiến của từng kỳ hạn thanh toán.
   - Dòng tiền dự phóng tại kỳ $t$ chỉ bao gồm:
     $$\text{CF}_{\text{deduct}}(t) = \text{Principal}(t) + \text{Balance}(t) \cdot r_{\text{risk-free}}(t) \cdot \Delta t$$
   - Dòng tiền hoàn trả gốc và dòng nợ gốc tái định giá danh nghĩa giữ nguyên giá trị hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-2]].

2. **Lựa chọn đường cong chiết khấu bắt buộc**:
   - Vì dòng tiền dự phóng đã loại bỏ hoàn toàn biên thương mại, theo Nguyên tắc 8(c), ngân hàng **bắt buộc phải chiết khấu bằng đường cong lãi suất phi rủi ro (Risk-free Discount Curve)** (ví dụ: đường cong OIS, SOFR, hoặc Trái phiếu Chính phủ) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]:
     $$\text{EVE}_{\text{deduct}} = \sum_{t} \frac{\text{CF}_{\text{deduct}}(t)}{\left(1 + r_{\text{risk-free}}(t)\right)^t}$$

3. **Ưu điểm và giới hạn kỹ trị**:
   - *Ưu điểm*: Đo lường thuần túy rủi ro lãi suất thị trường (pure interest rate risk), loại bỏ hoàn toàn nguy cơ biến động spread tín dụng khách hàng gây nhiễu loạn thước đo $\Delta\text{EVE}$ [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
   - *Hạn chế*: Bỏ qua giá trị thương quyền khách hàng (Customer Franchise Value). Trong thực tế, biên thương mại là dòng thu nhập ròng ổn định bảo vệ khả năng hấp thụ tổn thất của ngân hàng; việc khấu trừ biên thương mại có thể làm giảm quy mô giá trị kinh tế cơ sở so với sổ sách kế toán.

### Q3 — Phương pháp Giữ lại Biên thương mại (Include Approach)

Phương pháp giữ lại biên thương mại là phương án phổ biến tại các ngân hàng thương mại có mô hình kinh doanh truyền thống tập trung vào tín dụng bán lẻ và doanh nghiệp vừa và nhỏ [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

1. **Cơ chế kỹ thuật**:
   - Ngân hàng giữ lại toàn bộ các dòng thanh toán lãi danh nghĩa đầy đủ theo hợp đồng (bao gồm cả lãi suất cơ sở và biên thương mại) [[src-bcbs-irrbb-2016#^irrbb-u05-2]]:
     $$\text{CF}_{\text{include}}(t) = \text{Principal}(t) + \text{Balance}(t) \cdot \left(r_{\text{risk-free}}(t) + s_{\text{margin}}\right) \cdot \Delta t$$
   - Đối với công cụ lãi suất thả nổi, phần nợ gốc danh nghĩa quay về mệnh giá tại Reset Date tiếp theo, nhưng phần bù biên thương mại cố định ($s_{\text{margin}}$) vẫn được trải vào các dải kỳ hạn cho đến ngày đáo hạn hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-2]].

2. **Lựa chọn đường cong chiết khấu bắt buộc**:
   - Theo quy định tại Nguyên tắc 8(c) BCBS d368, khi dòng tiền đã bao gồm biên thương mại, **đường cong chiết khấu bắt buộc phải là đường cong phi rủi ro cộng thêm phần bù biên thương mại và spread tương ứng** [[src-bcbs-irrbb-2016#^irrbb-p08-2]]:
     $$r_{\text{discount}}(t) = r_{\text{risk-free}}(t) + s_{\text{margin}}(t)$$
     $$\text{EVE}_{\text{include}} = \sum_{t} \frac{\text{CF}_{\text{include}}(t)}{\left(1 + r_{\text{risk-free}}(t) + s_{\text{margin}}(t)\right)^t}$$

3. **Quy tắc toán học tránh biến dạng hiện giá**:
   - Nếu ngân hàng giữ lại biên thương mại trong dòng tiền tử số ($\text{CF}_{\text{include}}$) nhưng lại sử dụng đường cong phi rủi ro thuần túy ở mẫu số ($r_{\text{risk-free}}$), giá trị kinh tế sẽ bị thổi phồng ảo do dòng biên thương mại tương lai được chiết khấu ở mức lãi suất quá thấp [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
   - *Quy tắc bù trừ giải tích*: Khi tử số có spread $s$ và mẫu số được chiết khấu cộng thêm spread $s$, hiện giá của công cụ tại thời điểm ban đầu được bảo toàn ở mức ngang mệnh giá ($PV = Par$), bảo đảm tính trung thực của báo cáo ALM [[src-tata-bank-alm#^tata-ev-1]].

### Bảng So sánh Đối chiếu Hai Phương pháp Luận

| Tiêu chí | Khấu trừ Biên thương mại (Deduct Margins) | Giữ lại Biên thương mại (Include Margins) |
|---|---|---|
| **Dòng tiền dự phóng $\text{CF}(t)$** | Chỉ gồm gốc và lãi cơ sở phi rủi ro; loại bỏ toàn bộ spread thương mại [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. | Gồm đầy đủ gốc, lãi cơ sở và biên thương mại danh nghĩa theo hợp đồng [[src-bcbs-irrbb-2016#^irrbb-u05-2]]. |
| **Đường cong chiết khấu** | Đường cong phi rủi ro chuẩn (OIS, SOFR, Trái phiếu Chính phủ) [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. | Đường cong phi rủi ro cộng phần bù biên thương mại tương ứng [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. |
| **Mức độ phức tạp mô hình** | Đơn giản hơn: chỉ cần xây dựng một đường cong chiết khấu duy nhất cho toàn bộ bảng cân đối [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. | Phức tạp hơn: phải xây dựng nhiều đường cong chiết khấu theo từng phân khúc sản phẩm và mức xếp hạng tín dụng [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. |
| **Tính nhạy cảm lãi suất ($\Delta\text{EVE}$)** | Phản ánh thuần túy rủi ro lãi suất thị trường; thời lượng nhạy cảm chính xác hơn [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. | Có thể bị ảnh hưởng bởi biến động của spread tín dụng thị trường (CSRBB) [[src-choudhry-principles-banking#^choudhry-irrbb-9]]. |
| **Thích hợp cho danh mục** | Trái phiếu đầu tư, công cụ thị trường vốn, các vị thế phái sinh thanh khoản cao [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. | Khoản cho vay bán lẻ, tín dụng doanh nghiệp nhỏ, tiền gửi giao dịch truyền thống [[src-bcbs-irrbb-2016#^irrbb-p08-2]]. |

### Q4 — Nguyên tắc Nhất quán Xuyên suốt và Ranh giới CSRBB

1. **Nguyên tắc Nhất quán Toàn diện (Internal Consistency — Principle 8)**:
   - Ủy ban Basel quy định ngân hàng không được phép tùy tiện áp dụng lẫn lộn hai phương pháp: *"A bank should decide whether to deduct or include commercial margins... The approach should be applied consistently across all interest rate-sensitive assets and liabilities"* [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
   - *Nguy cơ bất đối xứng*: Nếu ngân hàng khấu trừ biên thương mại đối với tiền gửi (nợ) nhưng lại giữ lại biên thương mại đối với cho vay (tài sản), thời lượng tài sản sẽ bị kéo dài giả tạo trong khi thời lượng nợ bị co ngắn, tạo ra khe hở thời lượng dương nhân tạo ($\text{DGAP} > 0$), dẫn đến sai lệch nghiêm trọng các quyết định phòng ngừa rủi ro của ALCO [[src-tata-bank-alm#^tata-gap-3]].

2. **Ranh giới Tương tác với CSRBB (Credit Spread Risk in the Banking Book)**:
   - Theo Giáo sư Moorad Choudhry, khi ngân hàng áp dụng phương pháp Giữ lại Biên thương mại (Include Approach), sự thay đổi của chênh lệch tín dụng trên thị trường (*credit spread*) sẽ tác động trực tiếp lên giá trị chiết khấu của tài sản sổ ngân hàng [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
   - Hiện tượng này dẫn đến việc đo lường $\Delta\text{EVE}$ bị chồng lấn giữa hai loại rủi ro: rủi ro lãi suất thuần túy (IRRBB) và rủi ro spread tín dụng (CSRBB) [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
   - Ngược lại, phương pháp Khấu trừ (Deduct Approach) thiết lập một ranh giới kỹ trị tuyệt đối: IRRBB chỉ đo lường sự dịch chuyển của đường cong phi rủi ro, còn biến động của biên tín dụng được tách riêng để đo lường bằng độ nhạy CS01 trong khuôn khổ CSRBB [[src-choudhry-principles-banking#^choudhry-irrbb-9]].

### Q5 — Khung Quy định: So sánh Basel d368 vs Ngân hàng Nhà nước Việt Nam

- **Chuẩn mực Basel (BCBS d368)**:
  - Cho phép ngân hàng tự quyết định áp dụng Deduct hoặc Include cho mục đích quản trị nội bộ và tính toán $\Delta\text{EVE}$, nhưng yêu cầu bắt buộc phải công bố công khai phương pháp luận đã chọn trong Bảng A và Bảng B của Trụ cột 3 [[src-bcbs-irrbb-2016#^irrbb-p08-1]] [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
  - Đối với đo lường độ nhạy thu nhập ($\Delta\text{NII}$ 12 tháng), BCBS d368 bắt buộc phải bao gồm đầy đủ biên thương mại và spread trên giả định bảng cân đối không đổi (*constant balance sheet*) [[src-bcbs-irrbb-2016#^irrbb-p08-3]].
- **Quy định Ngân hàng Nhà nước Việt Nam**:
  - Thông tư 83/2025/TT-NHNN (có hiệu lực từ ngày 01/07/2026) điều chỉnh quản trị rủi ro lãi suất trên sổ ngân hàng tại Chương 3 Mục 7 và hướng dẫn đo lường kỹ thuật tại Phụ lục 5 `[cần nguồn: src-tt83-2025-nhnn C3-M7, PL5]`.
  - Quản trị dữ liệu và rủi ro mô hình liên quan đến việc xác định đường cong chiết khấu được quy định tại Chương 3 Mục 8 `[cần nguồn: src-tt83-2025-nhnn C3-M8]`.
  - *Khoảng trống pháp lý tại Việt Nam*: Hướng dẫn chi tiết của NHNN về việc liệu NHTM Việt Nam có được phép bóc tách biên thương mại hay bắt buộc phải giữ lại biên thương mại trong báo cáo khe hở kỳ hạn và đo lường tổn thất vốn hiện vẫn đang ở trạng thái `pending` trong wiki `[cần nguồn: src-tt83-2025-nhnn PL5]`.

## Bằng chứng ủng hộ

- **Ủy ban Basel (BCBS d368)**: Nguyên tắc 8 xác lập cơ sở pháp lý và toán học cho cả hai cách tiếp cận Deduct và Include, quy định rõ nguyên tắc bù trừ đường cong chiết khấu để bảo đảm tính khách quan của chỉ tiêu $\Delta\text{EVE}$ [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Moorad Choudhry (2022)**: Khẳng định nguyên lý tách biệt giữa thương quyền khách hàng và chuyển đổi kỳ hạn trong hệ thống FTP là nền tảng cốt tử giúp ALM đo lường chính xác các dòng tiền rủi ro [[src-choudhry-principles-banking#^choudhry-ftp-13]].
- **Fidelio Tata (2025)**: Chứng minh rằng việc chiết khấu dòng tiền bằng lãi suất phù hợp với bản chất của dòng tiền là yêu cầu bắt buộc để xác định đúng giá trị kinh tế của ngân hàng [[src-tata-bank-alm#^tata-ev-1]].

## Bằng chứng trái chiều

- **Tranh cãi về tính khả thi của Include Approach**: Việc xây dựng đường cong chiết khấu có cộng biên thương mại ($r_{\text{risk-free}} + s_{\text{margin}}$) đòi hỏi ngân hàng phải ước tính spread riêng cho từng danh mục cho vay và tiền gửi. Khi thị trường tài chính biến động mạnh, việc xác định spread chuẩn hóa trở nên thiếu khách quan và dễ bị thao túng để làm đẹp chỉ số EVE [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Xung đột giữa góc nhìn EVE và P&L thực tế**: Phương pháp Deduct bảo đảm tính thuần khiết của rủi ro lãi suất nhưng lại tạo ra độ lệch lớn so với thu nhập P&L thực tế của ngân hàng, vì trên thực tế ngân hàng luôn thu được biên thương mại đầy đủ nếu khách hàng không vỡ nợ [[src-bcbs-irrbb-2016#^irrbb-p08-3]].

## Phụ thuộc regime

- **Môi trường Biên tín dụng Thị trường Dãn rộng (Credit Spread Widening)**:
  - Nếu áp dụng *Include Approach*: Hiện giá của các khoản cho vay sụt giảm mạnh do tỷ suất chiết khấu tăng cao, khuếch đại mức sụt giảm $\Delta\text{EVE}$ ngay cả khi lãi suất phi rủi ro của ngân hàng trung ương không đổi [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
  - Nếu áp dụng *Deduct Approach*: Chỉ số $\Delta\text{EVE}$ hoàn toàn miễn nhiễm trước biến động của biên tín dụng, bảo đảm tính độc lập của chỉ số an toàn Trụ cột 2 [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
- **Môi trường Cạnh tranh Gay gắt về Biên lãi thuần (NIM Compression)**:
  - Khi biên thương mại bị co hẹp do cạnh tranh huy động, ngân hàng áp dụng *Include Approach* phải định kỳ điều chỉnh giảm spread chiết khấu, gây biến động giá trị kinh tế không xuất phát từ cú sốc lãi suất thị trường.

## Hàm ý ALM / quy định

- **Đối với ALM / Treasury**:
  - Khi thiết kế hệ thống tính toán EVE, ALM phải xây dựng module cho phép chạy song song cả hai kịch bản (Deduct và Include) để đối chiếu mức độ nhạy cảm của bảng cân đối trước biến động của biên thương mại.
  - Phải phối hợp chặt chẽ với bàn FTP để bảo đảm đường cong chiết khấu được xây dựng nhất quán với biểu lãi suất điều chuyển vốn nội bộ [[src-choudhry-principles-banking#^choudhry-ftp-11]].
- **Đối với ALCO**:
  - ALCO cần phê duyệt bằng văn bản chính sách lựa chọn phương pháp luận (Deduct vs Include) và giám sát chặt chẽ nguyên tắc nhất quán trên toàn bộ tài sản và nợ [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
  - Tránh hiện tượng thay đổi phương pháp luận giữa các kỳ báo cáo nhằm che giấu việc vi phạm ngưỡng ngoại lai 15% Vốn cấp 1 theo Outlier Bank Test [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
- **Đối với Ngân hàng Nhà nước Việt Nam**:
  - *Diễn giải:* (ngoài wiki, chưa có nguồn) Tại các NHTM Việt Nam, hầu hết các hệ thống Core Banking và ALM hiện nay đều ghi nhận dòng tiền gộp (bao gồm cả biên độ thương mại 3%–4%). Do đó, đại đa số các ngân hàng có xu hướng áp dụng phương pháp Giữ lại (Include Approach). NHNN cần ban hành hướng dẫn kỹ thuật rõ ràng về việc chuẩn hóa đường cong chiết khấu có spread để ngăn ngừa tình trạng mỗi ngân hàng áp dụng một công thức chiết khấu khác nhau làm sai lệch dữ liệu giám sát toàn hệ thống.

## Bất định

- **Hướng dẫn kỹ thuật Phụ lục 5 Thông tư 83/2025/TT-NHNN**: Chi tiết về việc NHNN có bắt buộc NHTM Việt Nam bóc tách biên thương mại hay cho phép duy trì dòng tiền gộp vẫn đang chờ được ingest từ raw text `[cần nguồn: src-tt83-2025-nhnn PL5]`.
- **Phương pháp bóc tách Biên thương mại trên danh mục cho vay thả nổi**: Trên thực tế, biên thương mại của khoản vay thả nổi thường cố định trong suốt vòng đời hợp đồng, nhưng chi phí huy động vốn của ngân hàng lại biến động liên tục; việc cố định biên thương mại khi chiết khấu dòng tiền dài hạn có thể tạo ra sai số mô hình khi chu kỳ thanh khoản thay đổi.
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation và mục spread/commercial margin.
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 103): có claim [[src-bcbs-irrbb-2016#^irrbb-u05-15]] — par 103 cho chọn trừ commercial margin khỏi notional repricing cash flow (Stage 2), tách khỏi việc chọn đường cong chiết khấu ∆EVE ([[src-bcbs-irrbb-2016#^irrbb-p08-2]]); par 103 không có yêu cầu nhất quán cho tài sản và nợ; cần rà lại Q2, Q5 và câu trích 'A bank should decide whether…'.
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại các đoạn về dòng tiền tái định giá và citation par 101–106.
