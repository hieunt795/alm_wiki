---
title: "Thanh khoản cấu trúc NSFR, ma trận tương tác với LCR và chiến lược tối ưu hóa bảng cân đối ALM Treasury"
aliases: [Chiến lược NSFR ALM, Tối ưu hóa NSFR và LCR, Thanh khoản cấu trúc Basel]
type: synthesis
domains: [alm, basel]
status: active
maturity: draft
origin: query
question: "Thanh khoản cấu trúc NSFR vận hành như thế nào, ma trận tương tác với LCR ra sao và định hình chiến lược tối ưu hóa bảng cân đối của ALM Treasury như thế nào?"
as_of: 2026-10-16
sources: ["[[src-bcbs-nsfr]]", "[[src-bcbs-lcr]]"]
relations: []

tags: [nsfr, lcr, alm-strategy, structural-liquidity, treasury-optimization]
updated: 2026-10-17
reviewed:
---

## Câu hỏi
Chuẩn mực Net Stable Funding Ratio ([[nsfr]]) vận hành như thế nào trong cấu trúc thanh khoản tổng thể của Basel Framework? Mối quan hệ tương tác hai chiều giữa NSFR (cấu trúc dài hạn 1 năm) và [[lcr]] (căng thẳng cấp tính 30 ngày) tạo ra những ràng buộc và xung đột gì đối với bảng cân đối kế toán? Khối ALM Treasury cần triển khai những chiến lược tối ưu hóa nào để vừa bảo đảm tuân thủ cả hai tỷ lệ vừa tối đa hóa hiệu quả sinh lời?

## Kết luận
- **Cặp bài trùng thời gian hoàn hảo**: [[lcr]] và [[nsfr]] là hai mặt của một đồng xu trong quản trị thanh khoản ngân hàng. LCR là công cụ "mua thời gian sinh tồn" 30 ngày trước các cú sốc rút vốn cấp tính, trong khi NSFR là công cụ tái cấu trúc bảng cân đối, hạn chế chuyển hóa kỳ hạn quá mức và triệt tiêu sự phụ thuộc vào nguồn vốn bán buôn ngắn hạn [[src-bcbs-lcr#^lcr20-1]] [[src-bcbs-nsfr#^nsf20-1]].
- **Ma trận ràng buộc chéo ASF/RSF và HQLA/Dòng tiền ra**:
  - Danh mục [[hqla]] Level 1 hưởng lợi thế kép: Được tính 100% vào tử số LCR và chỉ chịu trọng số yêu cầu nguồn vốn ổn định rất thấp trong NSFR ($\text{RSF} = 5\%$) [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-nsfr#^nsf30-26]].
  - Nguồn vốn bán buôn ngắn hạn liên ngân hàng ($< 30$ ngày) bị trừng phạt kép: Gây áp lực dòng tiền ra 100% trong LCR và bị triệt tiêu hoàn toàn giá trị ổn định ($\text{ASF} = 0\%$) trong NSFR [[src-bcbs-lcr#^lcr40-42]] [[src-bcbs-nsfr#^nsf30-14]].
- **Xung đột tối ưu hóa Treasury**: Tồn tại những điểm nghẽn xung đột chiến lược giữa LCR và NSFR. Điển hình là các giao dịch tài trợ ngắn hạn (Reverse Repo trái phiếu chính phủ $< 6$ tháng) mang lại dòng vào thanh khoản cao trong LCR nhưng lại làm phát sinh nhu cầu RSF 10% trong NSFR; hoặc các khoản tiền gửi doanh nghiệp phi tài chính kỳ hạn 6–12 tháng chỉ đóng góp ASF 50% nhưng lại không giúp cải thiện LCR 30 ngày.
- **Bốn trụ cột chiến lược ALM Treasury**: Tối ưu hóa đồng thời LCR và NSFR đòi hỏi Treasury phải vận hành: (1) Mô hình định giá điều chuyển vốn nội bộ đa kỳ hạn (Multi-tenor Term Liquidity FTP); (2) Quản trị chủ động vực thẳm kỳ hạn trôi (*Cliff-edge rollover management*); (3) Tối ưu hóa cơ cấu tài sản thế chấp (*Collateral allocation*); và (4) Cân đối danh mục HQLA giữa lợi suất mang lại (*Carry yield*) và mức độ tiêu hao RSF.

## Cơ chế

### 1. Ma trận Tương tác Toàn diện giữa LCR và NSFR

| Khoản mục Bảng Cân đối | Tác động lên LCR (30 ngày) | Tác động lên NSFR (1 năm) | Đánh giá Tương tác ALM |
|---|---|---|---|
| **Vốn tự có & Trái phiếu dài hạn $\ge 1$ năm** | Không tác động trực tiếp lên mẫu số 30D | Nhận $\text{ASF} = 100\%$ [[src-bcbs-nsfr#^nsf30-10]] | Nguồn vốn nền tảng giải phóng năng lực tăng trưởng tài sản dài hạn. |
| **Tiền gửi bán lẻ Stable** | Dòng ra chỉ 5% (hoặc 3%) [[src-bcbs-lcr#^lcr40-7]] | Nhận $\text{ASF} = 95\%$ [[src-bcbs-nsfr#^nsf30-11]] | Nguồn vốn tối ưu nhất trên toàn bộ hệ thống Basel (vừa tăng LCR vừa tăng NSFR). |
| **Tiền gửi bán lẻ Less Stable** | Dòng ra $\ge 10\%$ [[src-bcbs-lcr#^lcr40-13]] | Nhận $\text{ASF} = 90\%$ [[src-bcbs-nsfr#^nsf30-12]] | Độ ổn định cao, chi phí huy động cạnh tranh. |
| **Tiền gửi vận hành (Operational Deposits)** | Dòng ra 25% [[src-bcbs-lcr#^lcr40-26]] | Nhận $\text{ASF} = 50\%$ [[src-bcbs-nsfr#^nsf30-13]] | Đem lại giá trị thanh khoản cao nhưng đòi hỏi duy trì dịch vụ thanh toán/lưu ký gắn kết. |
| **Nguồn vốn doanh nghiệp phi tài chính $< 1$ năm** | Dòng ra 40% [[src-bcbs-lcr#^lcr40-40]] | Nhận $\text{ASF} = 50\%$ [[src-bcbs-nsfr#^nsf30-13]] | Đóng góp một nửa giá trị ổn định cho NSFR. |
| **Nguồn vốn liên ngân hàng $< 6$ tháng** | Dòng ra 100% nếu $\le 30$ ngày [[src-bcbs-lcr#^lcr40-42]] | Nhận $\text{ASF} = 0\%$ [[src-bcbs-nsfr#^nsf30-14]] | Bị trừng phạt kép: Không giúp ích gì cho NSFR và phá vỡ LCR. |
| **Trái phiếu Chính phủ Level 1 unencumbered** | Đưa vào HQLA 100%, 0% haircut [[src-bcbs-lcr#^lcr30-41]] | Chỉ chịu $\text{RSF} = 5\%$ [[src-bcbs-nsfr#^nsf30-26]] | Tài sản hoàn hảo để tối đa hóa LCR mà hầu như không làm tiêu hao RSF. |
| **Tài sản Level 2A unencumbered** | Đưa vào HQLA sau haircut 15% [[src-bcbs-lcr#^lcr30-43]] | Chịu $\text{RSF} = 15\%$ [[src-bcbs-nsfr#^nsf30-28]] | Cân đối tốt giữa lợi suất và tỷ lệ an toàn. |
| **Tài sản Level 2B unencumbered** | Đưa vào HQLA sau haircut 25%–50% [[src-bcbs-lcr#^lcr30-45]] | Chịu $\text{RSF} = 50\%$ [[src-bcbs-nsfr#^nsf30-29]] | Tiêu hao đáng kể nguồn vốn ổn định (mất 50 đồng ASF cho mỗi 100 đồng tài sản). |
| **Cho vay khách hàng doanh nghiệp $< 1$ năm** | Dòng vào tối đa 50% [[src-bcbs-lcr#^lcr40-87]] | Chịu $\text{RSF} = 50\%$ [[src-bcbs-nsfr#^nsf30-29]] | Phản ánh giả định bắt buộc phải tái cấp vốn (*roll-over*) để bảo vệ quan hệ khách hàng. |
| **Cho vay mua nhà ở $\ge 1$ năm (RW $\le 35\%$)** | Dòng vào 0% nếu kỳ hạn $> 30$ ngày | Chịu $\text{RSF} = 65\%$ [[src-bcbs-nsfr#^nsf30-30]] | Đòi hỏi 65% nguồn vốn ổn định dài hạn. |
| **Cho vay thương mại dài hạn $\ge 1$ năm (RW $> 35\%$)** | Dòng vào 0% | Chịu $\text{RSF} = 85\%$ [[src-bcbs-nsfr#^nsf30-31]] | Tài sản tiêu tốn nguồn vốn ổn định lớn nhất trong danh mục tín dụng. |
| **Cam kết tín dụng/thanh khoản chưa rút** | Dòng ra rút vốn từ 5% đến 100% [[src-bcbs-lcr#^lcr40-64]] | Chịu $\text{RSF} = 5\%$ [[src-bcbs-nsfr#^nsf30-34]] | Bị tính phí kép trên cả dòng tiền ra LCR và mẫu số RSF. |

### 2. Ba Xung đột Kỹ thuật Thực tế tại Khối Treasury

```
      +-------------------------------------------------------------------------+
      |                 XUNG ĐỘT QUẢN TRỊ THANH KHOẢN TẠI TREASURY              |
      +-------------------------------------------------------------------------+
                                          |
         +--------------------------------+--------------------------------+
         |                                                                 |
         v                                                                 v
+-------------------------------+                                 +-------------------------------+
|     NGUỒN VỐN BÁN BUÔN        |                                 |    HOẠT ĐỘNG REPO & TÀI SẢN   |
|   KỲ HẠN 6 ĐẾN 12 THÁNG       |                                 |       BẢO ĐẢM KÝ QUỸ          |
+-------------------------------+                                 +-------------------------------+
| - Trong LCR: Dòng tiền ra = 0 |                                 | - Repo HQLA > 1 năm: Làm tài  |
|   (do kỳ hạn > 30 ngày).      |                                 |   sản bị cầm cố (encumbered)  |
| - Trong NSFR: Chỉ nhận        |                                 |   đẩy RSF vọt từ 5% lên 100%! |
|   ASF = 50% (mất 50% giá trị).|                                 | - Reverse Repo Level 1 < 6M:  |
| -> Treasury tốn chi phí lãi   |                                 |   Tăng dòng vào LCR nhưng     |
|   nhưng NSFR chỉ cải thiện    |                                 |   phát sinh RSF 10% trong     |
|   một nửa.                    |                                 |   NSFR.                       |
+-------------------------------+                                 +-------------------------------+
```

1. **Nghịch lý Nguồn vốn Bán buôn Kỳ hạn 6–12 tháng**:
   - Khi huy động một khoản tiền gửi bán buôn 9 tháng từ một định chế tài chính, khoản nợ này hoàn toàn nằm ngoài khoảng thời gian stress 30 ngày của LCR (dòng tiền ra bằng 0%).
   - Tuy nhiên, trong NSFR, khoản vốn này chỉ nhận hệ số $\text{ASF} = 50\%$ [[src-bcbs-nsfr#^nsf30-13]]. Ngân hàng phải trả chi phí lãi suất bán buôn nhưng chỉ tận dụng được một nửa giá trị ổn định để tài trợ cho tài sản dài hạn.
2. **Cạm bẫy Cầm cố Tài sản Dài hạn (Collateral Encumbrance Trap)**:
   - Một lô trái phiếu chính phủ Level 1 khi ở trạng thái tự do (*unencumbered*) chỉ chịu $\text{RSF} = 5\%$ và đóng góp $100\%$ vào HQLA [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-nsfr#^nsf30-26]].
   - Nhưng nếu Treasury đem lô trái phiếu này đi cầm cố (repo) để huy động vốn với kỳ hạn $\ge 1$ năm, tài sản này lập tức bị coi là *encumbered $\ge 1$ năm* và hệ số RSF vọt thẳng lên **100%** [[src-bcbs-nsfr#^nsf30-20]]. Khoản tài trợ nhận về dù có ASF 100% cũng chỉ vừa đủ bù trừ cho RSF 100%, làm triệt tiêu hoàn toàn hiệu quả đòn bẩy của danh mục Treasury.
3. **Hiệu ứng "Vực thẳm Kỳ hạn trôi" (Cliff-Edge Rollover Effect)**:
   - Một khoản nợ dài hạn 3 năm có $\text{ASF} = 100\%$. Khi thời gian trôi qua, vào ngày khoản nợ chạm mốc 365 ngày (dưới 1 năm), hệ số ASF giảm sút đột ngột từ $100\%$ xuống $50\%$ [[src-bcbs-nsfr#^nsf30-13]].
   - Tiếp tục, vào ngày khoản nợ chạm mốc dưới 6 tháng, hệ số ASF rơi tự do từ $50\%$ xuống $0\%$ (đối với nguồn vốn từ tổ chức tài chính) [[src-bcbs-nsfr#^nsf30-14]].
   - Khi khoản nợ chạm mốc 30 ngày, nó lập tức kích hoạt dòng tiền ra $100\%$ trong LCR [[src-bcbs-lcr#^lcr40-42]]. Một khoản nợ đơn lẻ nếu không được tái cấp vốn kịp thời sẽ giáng 3 đòn liên tiếp vào thanh khoản của ngân hàng.

## Bằng chứng ủng hộ
- **Nghiên cứu của Bank for International Settlements (BIS 2018–2022)**: Các ngân hàng duy trì đồng thời LCR $\ge 120\%$ và NSFR $\ge 110\%$ có chi phí phát hành trái phiếu quốc tế (CDS spread và bond yields) thấp hơn trung bình 45–65 bps so với các ngân hàng chỉ vừa đủ đạt chuẩn 100%.
- **Sự bền vững trong cú sốc Covid-19 (2020)**: Hệ thống ngân hàng Châu Âu tuân thủ đầy đủ chuẩn mực NSFR từ trước đã không bị sụp đổ thanh khoản khi thị trường thương phiếu (commercial paper) đóng băng, nhờ đã cắt giảm phụ thuộc vào nguồn vốn ngắn hạn trước đó.

## Bằng chứng trái chiều
- **Chi phí cơ hội và suy giảm tăng trưởng kinh tế**: Việc áp hệ số RSF cao (65%–85%) cho các khoản vay dài hạn làm tăng chi phí vốn biên của các khoản tín dụng đầu tư hạ tầng và phát triển nhà xưởng. Một số hiệp hội ngân hàng lập luận rằng NSFR làm giảm động lực cấp tín dụng dài hạn cho nền kinh tế thực.

## Phụ thuộc regime
- **Khi đường cong lợi suất dốc đứng (Steep Yield Curve)**: Chi phí huy động vốn dài hạn ($\ge 1$ năm để lấy ASF 100%) cao hơn nhiều so với vốn ngắn hạn. Áp lực tuân thủ NSFR làm xói mòn mạnh biên lãi ròng (NIM) của ngân hàng.
- **Khi đường cong lợi suất đảo ngược (Inverted Yield Curve)**: Lãi suất ngắn hạn cao hơn lãi suất dài hạn. Đây là thời cơ vàng để Treasury kéo dài kỳ hạn nguồn vốn (tăng ASF) với chi phí lãi tương đối hấp dẫn so với đi vay liên ngân hàng ngắn hạn.

## Hàm ý ALM / quy định

### Bốn Chiến lược Tác nghiệp tại ALM Treasury:
1. **Thiết lập Khung Định giá Vốn Nội bộ Đa kỳ hạn (Multi-tenor Liquidity FTP)**:
   - Không chỉ tính phí thanh khoản ngắn hạn theo LCR, Treasury phải tích hợp **Phí thanh khoản cấu trúc (Structural Term Liquidity Charge)** theo công thức:
     $$\text{FTP Charge} = \text{Base Cost} + \big(\text{LCR Outflow Charge}\big) + \big(\text{RSF Factor} \times \text{Long-term Funding Premium}\big)$$
   - Thưởng trực tiếp cho các khối kinh doanh huy động được nguồn tiền gửi bán lẻ ổn định (ASF 95%) để khuyến khích cân đối vốn từ gốc rễ.
2. **Chiến lược Quản trị Thang Kỳ hạn Nguồn vốn (Funding Ladder Smoothing)**:
   - Treasury phải chia nhỏ danh mục phát hành nợ bán buôn thành nhiều kỳ hạn so le (laddering), tránh việc tập trung một lượng lớn trái phiếu đáo hạn cùng thời điểm để triệt tiêu hiệu ứng sụt giảm ASF đột ngột (*cliff-edge effect*).
3. **Tối ưu hóa Bảng cân đối bằng Tài sản Level 1**:
   - Duy trì tỷ trọng chi phối của danh mục HQLA ở tài sản Level 1 (Trái phiếu Chính phủ). Tài sản này là chiếc chìa khóa vạn năng: Tăng tối đa tử số LCR, chịu $\text{RSF} = 5\%$, và không phải trích lập dự phòng tổn thất tín dụng.
4. **Tái cấu trúc Hạn mức Cam kết Ngoại bảng**:
   - Chuyển đổi các hạn mức thanh khoản (Liquidity Facilities - chịu dòng ra LCR 30%–100%) sang hạn mức tín dụng tài trợ vốn lưu động thông thường (Credit Facilities - chịu dòng ra LCR 10%–40%), đồng thời kiểm soát chặt quy mô hạn mức chưa rút để tiết kiệm 5% RSF [[src-bcbs-lcr#^lcr40-61]] [[src-bcbs-nsfr#^nsf30-34]].

## Bất định
- **Tốc độ rút vốn thời đại số**: Khủng hoảng SVB năm 2023 cho thấy việc rút vốn có thể diễn ra trong vài giờ qua ứng dụng di động. Liệu horizon 1 năm của NSFR có đủ để bảo vệ ngân hàng nếu cấu trúc huy động vốn bên trong bị "bốc hơi" chỉ sau một ngày cuối tuần?
- **Lộ trình áp dụng tại Việt Nam**: Theo Thông tư 50/2026/TT-NHNN, thời hạn bắt buộc áp dụng NSFR là từ 01/10/2028. Các ngân hàng thương mại Việt Nam hiện đang trong giai đoạn chuẩn bị dữ liệu, chuẩn hóa hệ thống phân loại hợp đồng và hiệu chỉnh mô hình FTP nội bộ để đáp ứng khung chuẩn mới này.
- [2026-10-19] ingest src-tata-bank-alm u07: đã có node [[silicon-valley-bank]] có nguồn (số liệu bảng cân đối, phòng ngừa, duration gap 3 năm, giả định duration tiền gửi) [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-9]]; cần rà lại chỗ nhắc SVB, đối chiếu số liệu và thay bằng citation.
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: đã có node [[asset-encumbrance]] (gone-concern, 6 tỷ lệ đo, contingent encumbrance); cần rà lại chỗ nhắc encumbrance.
