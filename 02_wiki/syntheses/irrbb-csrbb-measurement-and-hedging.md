---
title: "Đo lường và Phòng hộ Rủi ro Chênh lệch Tín dụng Sổ Ngân hàng (CSRBB)"
aliases: [CSRBB Measurement and Hedging, Khung đo lường CSRBB và tác động CET1, CS01 and Spread Duration]
type: synthesis
domains: [alm, basel, vn-reg]
status: active
maturity: draft
origin: research
question: "Rủi ro chênh lệch tín dụng trên sổ ngân hàng (Credit Spread Risk in the Banking Book - CSRBB): Khung đo lường CS01, Spread Duration và tác động lên vốn tự có cấp 1 CET1 đối với danh mục trái phiếu FVOCI/AFS."
as_of: 2026-10-19
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-tt83-2025-nhnn]]"]
relations: []
tags: [csrbb, credit-spread, spread-duration, cs01, fvoci, afs, htm, cet1, tier-1-capital, basel, irrbb]
updated: 2026-10-19
reviewed:
---

## Câu hỏi

- Q1: Bản chất CSRBB là gì và ranh giới bóc tách giữa IRRBB, CSRBB và Rủi ro tín dụng Trụ cột 1 (Annex 1 Par 1.2–1.3 BCBS d368)?
- Q2: Khung đo lường định lượng CSRBB: Công thức và ý nghĩa của Spread Duration, CS01 và phân tích độ nhạy?
- Q3: Cơ chế truyền dẫn kế toán và tác động xói mòn Vốn cấp 1 CET1 đối với danh mục trái phiếu FVOCI/AFS so với HTM?
- Q4: Kỹ thuật phòng ngừa rủi ro CSRBB: Hợp đồng hoán đổi rủi ro tín dụng (CDS), hạn mức CS01/Spread Duration và tối ưu hóa danh mục trái phiếu HQLA?
- Q5: So sánh chuẩn mực Basel (BCBS d368 Nguyên tắc 1 & 15, EBA Guidelines on CSRBB) và quy định pháp lý của NHNN (TT 83/2025/TT-NHNN, TT 41/2016/TT-NHNN)?

## Kết luận

- **Q1 (Bản chất và Ranh giới)**: CSRBB là rủi ro phát sinh từ các biến động của chênh lệch lợi suất tín dụng (credit spread) đối với các công cụ chịu rủi ro tín dụng trên sổ ngân hàng mà không được giải thích bởi IRRBB hay rủi ro vỡ nợ đột ngột (jump-to-default) [[src-bcbs-irrbb-2016#^irrbb-u02-3]]. Chuẩn mực Basel chia tách lãi suất thành 5 thành phần: Lãi suất phi rủi ro và Spread thời lượng thuộc phạm vi IRRBB; Spread thanh khoản thị trường và Spread tín dụng thị trường chung thuộc phạm vi CSRBB; trong khi Spread tín dụng đặc thù thuộc phạm vi Rủi ro tín dụng Trụ cột 1 [[src-bcbs-irrbb-2016#^irrbb-u06-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- **Q2 (Khung Đo lường CS01 & Spread Duration)**: Trong thực tế ngân hàng của Moorad Choudhry, CSRBB áp dụng rõ ràng và trọng yếu nhất đối với danh mục trái phiếu (Eurobonds) hạch toán theo giá trị hợp lý [[src-choudhry-principles-banking#^choudhry-irrbb-9]] [[src-choudhry-principles-banking#^choudhry-irrbb-13]]. Thước đo độ nhạy cốt lõi là CS01 (biến động giá trị hiện tại theo 1 điểm cơ bản dịch chuyển credit spread) và Spread Duration (độ co giãn phần trăm của giá trái phiếu theo credit spread).
- **Q3 (Truyền dẫn Kế toán sang Vốn cấp 1 CET1)**: Tài sản ghi nhận theo giá trị phân bổ (Amortised cost / HTM) không chịu điều chỉnh thị giá tức thời; ngược lại, danh mục ghi nhận theo giá trị hợp lý (FVOCI/AFS) phản ánh ngay các khoản lỗ chưa thực hiện vào Thu nhập toàn diện khác tích lũy (AOCI), trừ thẳng vào Vốn tự có Cấp 1 CET1 và làm xói mòn tỷ lệ an toàn vốn CAR [[src-bcbs-irrbb-2016#^irrbb-u06-1]] [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
- **Q4 (Kỹ thuật Phòng ngừa Rủi ro)**: Khi phơi nhiễm CSRBB vượt khẩu vị rủi ro, ngân hàng phải áp dụng các kỹ thuật miễn nhiễm rủi ro qua phòng hộ tự nhiên, hạn mức CS01/Spread Duration, phân bổ tối ưu giữa HTM và FVOCI, chuyển dịch cơ cấu HQLA sang tài sản Level 1, hoặc sử dụng công cụ phái sinh tín dụng (CDS) [[src-choudhry-principles-banking#^choudhry-irrbb-12]].
- **Q5 (Khung Quy định Basel vs NHNN)**: Basel d368 (Nguyên tắc 1) yêu cầu giám sát độc lập CSRBB trong Trụ cột 2/ICAAP [[src-bcbs-irrbb-2016#^irrbb-p01-1]]. Tại Việt Nam, C3-M7 và Phụ lục V của [[tt83-2025]] chỉ dùng repricing gap, ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-1a1]] [[src-tt83-2025-nhnn#^d53-1a2]]; hai phần này không nhắc CSRBB, CS01 hay vốn riêng cho CSRBB. Các phần khác của TT83 (C3-M3 rủi ro thị trường, C3-M9 ICAAP) và TT41/2016 chưa có trong wiki `[cần nguồn: src-tt83-2025-nhnn C3-M3, C3-M9]`.

## Cơ chế

### Q1 — Bản chất và Phân định Ranh giới IRRBB vs CSRBB vs Credit Risk

Chuẩn mực BCBS d368 (Annex 1) thiết lập nguyên tắc bóc tách cấu trúc lãi suất của mọi công cụ tài chính thành 5 thành phần để phân định thẩm quyền quản trị giữa IRRBB, CSRBB và Rủi ro tín dụng Trụ cột 1 [[src-bcbs-irrbb-2016#^irrbb-u06-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]]:

| Thành phần Lãi suất | Bản chất Kinh tế | Khuôn khổ Quản trị | Căn cứ Quy định |
|---|---|---|---|
| **1. Lãi suất phi rủi ro (Risk-free rate)** | Lợi suất tài trợ phi rủi ro thị trường (đường cong OIS/TPCP). | Thuộc phạm vi **IRRBB** | [[src-bcbs-irrbb-2016#^irrbb-u06-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]] |
| **2. Spread thời lượng thị trường (Market duration spread)** | Phần bù kỳ hạn cho việc cam kết vốn dài hạn trên thị trường. | Thuộc phạm vi **IRRBB** | [[src-bcbs-irrbb-2016#^irrbb-u06-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]] |
| **3. Spread thanh khoản thị trường (Market liquidity spread)** | Phần bù cho tính kém thanh khoản chung của phân khúc tài sản. | Thuộc phạm vi **CSRBB** | [[src-bcbs-irrbb-2016#^irrbb-u06-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]] |
| **4. Spread tín dụng thị trường chung (General market credit spread)** | Phần bù rủi ro tín dụng bình quân theo ngành/nhóm xếp hạng. | Thuộc phạm vi **CSRBB** | [[src-bcbs-irrbb-2016#^irrbb-u06-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]] |
| **5. Spread tín dụng đặc thù (Idiosyncratic credit spread)** | Phần bù rủi ro vi mô gắn liền với khả năng vỡ nợ của con nợ. | Thuộc **Credit Risk (Pillar 1)** | [[src-bcbs-irrbb-2016#^irrbb-u02-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-2]] |

Ranh giới cốt lõi:
- **IRRBB** hấp thu biến động của lãi suất phi rủi ro, spread thời lượng thị trường, lãi suất tham chiếu và biên tài trợ nội bộ [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- **CSRBB** tích hợp biến động của **spread thanh khoản thị trường** và **spread tín dụng thị trường chung** [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- **Rủi ro tín dụng Trụ cột 1** bao hàm rủi ro tín dụng đặc thù của con nợ và rủi ro vỡ nợ đột ngột (jump-to-default risk), vốn đã được dự phòng và tính toán trong yêu cầu an toàn vốn tối thiểu [[src-bcbs-irrbb-2016#^irrbb-u02-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-2]].

### Q2 — Khung Đo lường Định lượng: Spread Duration, CS01 và Phân tích Độ nhạy

Theo Moorad Choudhry (*The Principles of Banking*, Ch. 7), rủi ro CSRBB áp dụng rõ nhất cho danh mục trái phiếu và được đo lường cho mục đích EVE bằng thước đo tương đương **CS01** [[src-choudhry-principles-banking#^choudhry-irrbb-9]] [[src-choudhry-principles-banking#^choudhry-irrbb-13]].

*Diễn giải:* (ngoài wiki, chưa có nguồn) Cơ chế định lượng của Spread Duration và CS01 dựa trên mô hình định giá trái phiếu với lợi suất chiết khấu $y = r_{\text{rf}} + s$ (trong đó $r_{\text{rf}}$ là lãi suất phi rủi ro và $s$ là credit spread):

1. **Spread Duration (Thời lượng Chênh lệch Tín dụng — SD)**: Đo lường phần trăm thay đổi giá trị tài sản khi credit spread dịch chuyển:
$$\text{SD} = - \frac{1}{P} \frac{\partial P}{\partial s} \approx \frac{P_- - P_+}{2 \cdot P_0 \cdot \Delta s}$$
Đối với trái phiếu lãi suất cố định thông thường, $\text{SD}$ xấp xỉ bằng Modified Duration ($\text{MD}$). Tuy nhiên, đối với trái phiếu lãi suất thả nổi (Floating Rate Notes — FRN), trong khi $\text{MD}$ chỉ phản ánh thời gian tới kỳ tái định giá kế tiếp (thường từ 1 đến 3 tháng), thì $\text{SD}$ lại phản ánh toàn bộ kỳ hạn còn lại của trái phiếu đến ngày đáo hạn gốc.

2. **CS01 (Credit Spread 01 / Spread DV01)** ([[cs01]]): Mức biến động bằng tiền tuyệt đối của giá trị hiện tại (PV) khi credit spread dịch chuyển song song 1 điểm cơ bản ($\Delta s = 1\text{ bp} = 0.0001$):
$$\text{CS01} = - \frac{\partial P}{\partial s} \times 0.0001 = \text{SD} \times P \times 0.0001$$
Choudhry khẳng định CS01 là thước đo tiệm cận nhất với lăng kính EVE đối với danh mục trái phiếu [[src-choudhry-principles-banking#^choudhry-irrbb-9]].

3. **Phân rã Biến động Giá trị Hiện tại ($\Delta\text{PV}$)**:
$$\Delta P \approx - \text{CS01} \times \Delta s_{\text{bps}} + \frac{1}{2} \text{SC} \times P \times (\Delta s)^2$$
(với $\text{SC}$ là Spread Convexity). Khi spread nới rộng mạnh, độ lồi chênh lệch tín dụng giúp giảm nhẹ mức tổn thất thực tế.

| Thước đo | Ký hiệu | Đối tượng Rủi ro | Kỳ hạn chiết khấu đối với FRN | Kênh tác động |
|---|---|---|---|---|
| **PV01 / DV01** | $\text{DV01}$ | Rủi ro Lãi suất Phi rủi ro (IRRBB) | Đến ngày tái định giá kế tiếp (Next Repricing Date) | EVE / P&L |
| **CS01** | $\text{CS01}$ | Rủi ro Credit Spread Thị trường (CSRBB) | Đến ngày đáo hạn hợp đồng (Maturity Date) | EVE / AOCI / CET1 |

### Q3 — Kênh Truyền dẫn Kế toán và Tác động Xói mòn Vốn cấp 1 CET1 (FVOCI vs HTM)

Chuẩn mực BCBS d368 (Annex 1 Par 1.2) chỉ rõ sự khác biệt giữa hai mô hình kế toán đối với bảng cân đối [[src-bcbs-irrbb-2016#^irrbb-u06-1]]:

1. **Mô hình Giá trị Phân bổ (Amortised Cost / HTM)**:
- Áp dụng cho các khoản tín dụng và trái phiếu giữ đến ngày đáo hạn (Hold to Collect).
- Biến động của credit spread thị trường không làm thay đổi giá trị ghi sổ của tài sản; ngân hàng không ghi nhận lỗ đánh giá lại hàng kỳ [[src-bcbs-irrbb-2016#^irrbb-u06-1]]. Tổn thất chỉ phát sinh khi có sự kiện suy giảm tín dụng (impairment) dẫn tới trích lập dự phòng rủi ro.

2. **Mô hình Giá trị Hợp lý qua OCI (FVOCI / AFS)**:
- Áp dụng cho danh mục trái phiếu đầu tư sẵn sàng để bán hoặc danh mục Eurobonds của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u06-1]] [[src-choudhry-principles-banking#^choudhry-irrbb-9]].
- Khi credit spread thị trường giãn rộng (spread widening), giá trị thị trường của trái phiếu sụt giảm ngay lập tức; khoản lỗ chưa thực hiện (unrealised loss) được hạch toán thẳng vào mục Thu nhập toàn diện khác tích lũy (Accumulated Other Comprehensive Income — AOCI) thuộc Vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-u06-1]].

3. **Cơ chế Truyền dẫn Xói mòn Vốn Tự có Cấp 1 CET1**:
*Diễn giải:* (ngoài wiki, chưa có nguồn) Theo chuẩn mực Basel III (khi loại bỏ bộ lọc AOCI prudential filter):
$$\Delta\text{AOCI} = \Delta\text{PV}_{\text{FVOCI}} \approx - \sum_{k} \text{CS01}_k \times \Delta s_k$$
Khoản suy giảm AOCI này trừ trực tiếp vào Vốn tự có Cấp 1:
$$\text{CET1}_{\text{post-shock}} = \text{CET1}_{\text{pre-shock}} - |\Delta\text{AOCI}|$$
Tỷ lệ an toàn vốn (CAR) sau sốc credit spread suy giảm theo cơ chế:
$$\text{CAR}_{\text{post-shock}} = \frac{\text{CET1}_{\text{post-shock}} + \text{AT1} + \text{Tier 2}}{\text{RWA}}$$
Khi credit spread giãn rộng 100–200 bps trong khủng hoảng thanh khoản, danh mục FVOCI có thời lượng dài sẽ gây ra khoản lỗ AOCI khổng lồ, trực tiếp đẩy tỷ lệ CAR của ngân hàng xuống dưới ngưỡng tối thiểu, kích hoạt các chế tài can thiệp giám sát.

### Q4 — Kỹ thuật Phòng ngừa Rủi ro CSRBB và Quản trị Danh mục HQLA

Moorad Choudhry nhấn mạnh: nếu tác động căng thẳng lãi suất và credit spread vượt quá khẩu vị rủi ro, ngân hàng bắt buộc phải: (1) Miễn nhiễm rủi ro qua phòng ngừa tự nhiên hoặc phái sinh; (2) Phân bổ thêm Vốn cấp 1; hoặc (3) Loại bỏ rủi ro khỏi bảng cân đối [[src-choudhry-principles-banking#^choudhry-irrbb-12]].

Bốn trụ cột kỹ trị quản trị rủi ro CSRBB tại ALM & Treasury:

1. **Hệ thống Hạn mức CS01 Độc lập**:
ALCO thiết lập hạn mức CS01 tổng thể và chi tiết theo từng phân khúc ngành, xếp hạng tín nhiệm và dải kỳ hạn, độc lập hoàn toàn với hạn mức PV01 của IRRBB.

2. **Cơ cấu Phân loại Kế toán (Accounting Classification Strategy)**:
Chủ động điều phối tỷ trọng phân bổ giữa HTM và FVOCI tại thời điểm ghi nhận ban đầu. Danh mục dự kiến nắm giữ dài hạn để thu dòng tiền được chuyển sang HTM nhằm miễn nhiễm rủi ro xói mòn vốn CET1 do biến động thị giá.

3. **Rủi ro Kép trên Đệm Tài sản Thanh khoản Cao (HQLA)**:
Trong khi tài sản Level 1 (TPCP) miễn nhiễm với CSRBB, các tài sản **Level 2A và Level 2B** (trái phiếu chính quyền địa phương, trái phiếu doanh nghiệp) trong [[hqla]] vừa gánh rủi ro IRRBB vừa chịu rủi ro CSRBB rất lớn [[src-bcbs-irrbb-2016#^irrbb-u06-1]]. Trong khủng hoảng thị trường, credit spread của tài sản Level 2 nới rộng dữ dội, làm sụt giảm hiện giá danh mục thanh khoản ngay thời điểm ngân hàng cần huy động vốn khẩn cấp nhất.

4. **Phòng hộ bằng Phái sinh Tín dụng (Credit Default Swaps — CDS)**:
Trên thị trường quốc tế, ngân hàng mua bảo hiểm CDS (Buy Protection) đối với các danh mục trái phiếu doanh nghiệp chuẩn hoá (CDX / iTraxx) để bù đắp mức suy giảm giá trị khi credit spread thị trường nới rộng [[src-choudhry-principles-banking#^choudhry-irrbb-12]].

### Q5 — So sánh Chuẩn mực Basel vs Quy định của Ngân hàng Nhà nước Việt Nam

| Tiêu chí So sánh | Chuẩn mực Quốc tế (Basel BCBS d368 & EBA) | Quy định Ngân hàng Nhà nước Việt Nam | Căn cứ & Đánh giá |
|---|---|---|---|
| **Cơ sở Pháp lý** | BCBS d368 Nguyên tắc 1; EBA Guidelines on CSRBB (EBA/GL/2022/14). | [[tt83-2025]] (IRRBB: Đ53–55, Phụ lục V); TT41/2016 chưa register. | [[src-bcbs-irrbb-2016#^irrbb-p01-1]] [[src-tt83-2025-nhnn#^d53-1a2]] `[cần nguồn: TT41/2016]` |
| **Phạm vi Đo lường** | Bắt buộc đối với toàn bộ công cụ chịu rủi ro spread trên sổ ngân hàng. | C3-M7 và Phụ lục V không có quy định về CSRBB. | [[src-bcbs-irrbb-2016#^irrbb-u02-3]] [[src-tt83-2025-nhnn#^d53-1a2]] `[cần nguồn: src-tt83-2025-nhnn C3-M3]` |
| **Thước đo Kỹ thuật** | CS01, Spread Duration, VaR Credit Spread, kịch bản sốc spread. | [cần nguồn] (nhận định về TT11/2021 chưa có nguồn trong wiki). | [[src-choudhry-principles-banking#^choudhry-irrbb-9]] `[cần nguồn: TT11/2021]` |
| **Tác động Vốn CET1** | Bỏ bộ lọc AOCI, phản ánh tức thì lỗ chưa thực hiện vào CET1. | Áp dụng chuẩn kế toán VAS, danh mục AFS không đánh giá lại thị trường hàng ngày vào vốn. | [[src-bcbs-irrbb-2016#^irrbb-u06-1]] `[cần nguồn: src-tt41-2016-nhnn]` |
| **Yêu cầu Vốn Trụ cột 2** | Tính vốn bổ sung trong ICAAP nếu phơi nhiễm CSRBB trọng yếu. | C3-M7 không có; ICAAP thuộc C3-M9, PL3 chưa ingest. | [[src-bcbs-irrbb-2016#^irrbb-p01-1]] `[cần nguồn: src-tt83-2025-nhnn C3-M9]` |

## Bằng chứng ủng hộ

- Chuẩn mực BCBS d368 xác định rõ CSRBB là cấu phần không thể tách rời trong giám sát Trụ cột 2 [[src-bcbs-irrbb-2016#^irrbb-p01-1]], đồng thời cung cấp phương pháp luận phân rã 5 thành phần lãi suất tại Annex 1 [[src-bcbs-irrbb-2016#^irrbb-u06-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-3]].
- Moorad Choudhry khẳng định tầm quan trọng thực tiễn của thước đo CS01 đối với danh mục Eurobonds hạch toán FVOCI [[src-choudhry-principles-banking#^choudhry-irrbb-9]] [[src-choudhry-principles-banking#^choudhry-irrbb-13]], và chỉ rõ các phương án hành động bắt buộc khi căng thẳng vượt khẩu vị rủi ro [[src-choudhry-principles-banking#^choudhry-irrbb-12]].
- Hướng dẫn kế toán Annex 1 Par 1.2 của BCBS d368 chứng minh kênh truyền dẫn trực tiếp từ thị giá tài sản FVOCI sang vốn khả dụng của ngân hàng [[src-bcbs-irrbb-2016#^irrbb-u06-1]].

## Bằng chứng trái chiều

- **Phạm vi áp dụng lý thuyết vs thực tiễn**:
  - *Quan điểm BCBS*: Văn bản d368 mở rộng định nghĩa CSRBB cho mọi tài sản và công nợ chịu rủi ro tín dụng trên sổ ngân hàng (bao gồm cả dư nợ cho vay và huy động tiền gửi) [[src-bcbs-irrbb-2016#^irrbb-u02-3]].
  - *Quan điểm Moorad Choudhry*: Giáo sư Choudhry cho rằng định chế Basel chỉ dành 4 dòng tóm lược về CSRBB và việc áp dụng CSRBB cho toàn bộ bảng cân đối là thiếu thực tế; trong điều hành ngân hàng thực chiến, CSRBB chủ yếu và trọng yếu nhất đối với danh mục trái phiếu (Eurobonds) hạch toán theo giá trị hợp lý [[src-choudhry-principles-banking#^choudhry-irrbb-9]].

## Phụ thuộc regime

- **Regime Thị trường Bình thường vs Khủng hoảng Thanh khoản (Flight-to-Quality)**:
  - Trong điều kiện bình thường, biến động credit spread của trái phiếu doanh nghiệp tương đối ổn định, CS01 duy trì ở mức an toàn.
  - Trong khủng hoảng thị trường hoặc suy thoái kinh tế, hiện tượng tháo chạy tìm nơi trú ẩn an toàn (Flight-to-Quality) diễn ra: Lãi suất phi rủi ro của TPCP giảm mạnh, nhưng credit spread của trái phiếu doanh nghiệp (Level 2B) bị nới rộng dữ dội, khiến danh mục FVOCI sụt giảm giá trị kép.
- **Regime Pháp lý và Chuẩn mực Kế toán**:
  - Dưới IFRS 9 và chuẩn mực Basel III quốc tế: Lỗ chưa thực hiện từ FVOCI trừ thẳng vào CET1 mà không có bộ lọc an toàn, tạo ra biến động vốn dữ dội.
  - Dưới VAS và môi trường pháp lý hiện hành tại Việt Nam: Phần lớn trái phiếu được hạch toán theo giá gốc/phân bổ, hạn chế tác động biến động thị giá tức thời lên vốn tự có nhưng tiềm ẩn rủi ro tích tụ suy giảm giá trị khi thoái vốn.

## Hàm ý ALM / quy định

- **Hàm ý cho ALCO và Treasury**:
  1. *Phân tách hạn mức kép*: ALCO không được gộp chung rủi ro lãi suất và rủi ro tín dụng; bắt buộc phải phê duyệt hệ thống hạn mức độc lập giữa PV01 (IRRBB) và CS01 (CSRBB).
  2. *Bóc tách trong cơ chế FTP*: Bàn ALM cần chuyển giao rủi ro credit spread thị trường từ các đơn vị kinh doanh về cuốn sổ trung tâm (CFU) thông qua phụ phí thanh khoản và rủi ro tín dụng thị trường, đảm bảo biên thương mại của chi nhánh được miễn nhiễm.
  3. *Tối ưu hóa đệm HQLA*: Cần giới hạn tỷ trọng tài sản Level 2A và Level 2B trong đệm thanh khoản; ưu tiên nắm giữ Trái phiếu Chính phủ Việt Nam (Level 1) để triệt tiêu phơi nhiễm CSRBB cho mục đích an toàn thanh khoản.
- *Diễn giải:* (ngoài wiki, chưa có nguồn) Đối với các NHTM Việt Nam, trong lộ trình chuyển đổi áp dụng IFRS 9 và Thông tư sửa đổi Thông tư 41, khối Quản trị rủi ro cần chủ động xây dựng mô hình tính toán CS01 và kịch bản sốc nới rộng spread đối với danh mục trái phiếu doanh nghiệp và trái phiếu TCTD để chủ động đệm vốn trước khi cơ quan giám sát ban hành hướng dẫn chính thức.

## Bất định

- Khung quy định CSRBB của NHNN: C3-M7 và PL5 không có (đã ingest [2026-10-19]); cần kiểm C3-M3 (rủi ro thị trường), C3-M9 (ICAAP), PL3 `[cần nguồn: src-tt83-2025-nhnn C3-M3, C3-M9]`.
- Quy chế áp dụng bộ lọc thận trọng (Prudential Filter) đối với khoản lỗ/lãi chưa thực hiện trong danh mục AFS/FVOCI khi tính Vốn cấp 1 theo Thông tư 41/2016/TT-NHNN `[cần nguồn: src-tt41-2016-nhnn]`.
- Mức độ thanh khoản và công cụ phái sinh tín dụng (CDS nội địa) trên thị trường tài chính Việt Nam còn hạn chế, khiến việc phòng ngừa rủi ro CSRBB bằng phái sinh khó khả thi trên thực tế.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1: đã có node [[risk-appetite]], [[risk-limits]], [[stress-testing]]; stress test IRRBB tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]]; cần rà lại chỗ nhắc khẩu vị rủi ro / hạn mức.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN.
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M3: đã có node [[market-risk-management]]; C3-M3 (Đ35–37) cũng không có quy định về credit spread; cần rà lại Q5.
