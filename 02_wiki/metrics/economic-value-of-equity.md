---
title: "Economic Value of Equity (EVE)"
aliases: [EVE, Giá trị kinh tế của vốn chủ sở hữu, ΔEVE, Delta EVE]
type: metric
domains: [alm, basel]
status: active
maturity: canonical
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]"]
relations:
  - {type: measures, to: "[[gap-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: measures, to: "[[option-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-1]]"}
  - {type: measures, to: "[[basis-risk]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-4]]"}
  - {type: input-to, to: "[[outlier-bank-test]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-p12-1]]"}
tags: [irrbb, eve, economic-value, pillar-2, outlier-test, run-off]
updated: 2026-10-16
reviewed:
---

## Định nghĩa
Giá trị kinh tế của vốn chủ sở hữu (Economic Value of Equity - EVE) là giá trị hiện tại thuần (NPV) của toàn bộ dòng tiền dự kiến trong tương lai từ các tài sản, nợ phải trả và các vị thế ngoại bảng nhạy cảm với lãi suất trên sổ ngân hàng, loại trừ vốn chủ sở hữu kế toán [[src-bcbs-irrbb-2016#^irrbb-p08-2]] [[src-bcbs-irrbb-2016#^irrbb-u06-5]].

Chỉ số biến động giá trị kinh tế ($\Delta\text{EVE}$) đo lường mức độ sụt giảm giá trị kinh tế của ngân hàng khi chịu tác động của các kịch bản sốc lãi suất chuẩn hoá so với kịch bản cơ sở theo đường cong lợi suất hiện hành [[src-bcbs-irrbb-2016#^irrbb-u01-4]] [[src-bcbs-irrbb-2016#^irrbb-u05-8]]:
- **Lăng kính dài hạn (Run-off Horizon)**: $\Delta\text{EVE}$ đánh giá tác động trên toàn bộ vòng đời còn lại của tất cả các công cụ tài chính hiện hữu cho đến khi chạy hết dòng tiền (run-off), không tính đến các giao dịch kinh doanh mới trong tương lai [[src-bcbs-irrbb-2016#^irrbb-p04-2]].
- **Thước đo an toàn vốn của Cơ quan giám sát**: Cơ quan giám sát Basel sử dụng $\Delta\text{EVE}$ làm thước đo chuẩn mực để đánh giá mức độ đủ vốn Trụ cột 2 và kiểm tra ngưỡng ngân hàng ngoại lai qua phép thử [[outlier-bank-test|Outlier Bank Test]] [[src-bcbs-irrbb-2016#^irrbb-u02-4]] [[src-bcbs-irrbb-2016#^irrbb-p12-1]].
- **Nguyên tắc Reset Date theo Fidelio Tata**: Rủi ro lãi suất đối với giá trị kinh tế chỉ được tính đến ngày tái định giá tiếp theo (*next reset date*) chứ không phải ngày đáo hạn theo hợp đồng, bởi vì khi một công cụ được thiết lập lại theo lãi suất thị trường, nó sẽ giao dịch lại theo giá ngang mệnh giá (*par*) [[src-tata-bank-alm#^tata-gap-2]]. Đối với các công cụ có dòng tiền phụ thuộc vào mức lãi suất (như quyền chọn trả nợ trước hạn hay công cụ thả nổi), dự phóng dòng tiền bắt buộc phải được điều chỉnh tương ứng [[src-tata-bank-alm#^tata-ev-3]].

## Công thức tính toán chuẩn hoá

Theo Khuôn khổ chuẩn hoá của [[bcbs-irrbb]], với mỗi đồng tiền trọng yếu $c$ và kịch bản sốc lãi suất $i \in \{1..6\}$, biến động giá trị kinh tế $\Delta\text{EVE}_{i,c}$ được xác định qua 4 bước:

### 1. Chiết khấu dòng tiền tái định giá thuần
Dòng tiền tái định giá thuần $CF_{i,c}(k)$ tại dải kỳ hạn $k$ (hoặc điểm giữa $t_k$) được chiết khấu theo hệ số chiết khấu liên tục:

$$
DF_{i,c}(t_k) = \exp\left(-R_{i,c}(t_k) \cdot t_k\right)
$$

Trong đó $R_{i,c}(t_k)$ là lãi suất phi rủi ro sau sốc tại kỳ hạn $t_k$.

### 2. Giá trị kinh tế không bao gồm quyền chọn tự động ($\text{EVE}^{\text{nao}}$)

$$
\text{EVE}_{i,c}^{\text{nao}} = \sum_{k=1}^{K} CF_{i,c}(t_k) \cdot DF_{i,c}(t_k)
$$

### 3. Tổn thất EVE từng kịch bản và loại tiền tệ kèm add-on quyền chọn tự động

$$
\Delta\text{EVE}_{i,c} = \text{EVE}_{0,c}^{\text{nao}} - \text{EVE}_{i,c}^{\text{nao}} + \text{KAO}_{i,c}
$$

Trong đó:
- $\text{EVE}_{0,c}^{\text{nao}}$ là giá trị kinh tế theo đường cong lãi suất cơ sở ban đầu.
- $\text{KAO}_{i,c}$ là phần bù rủi ro quyền chọn lãi suất tự động (automatic interest rate options add-on) được định giá lại toàn bộ dưới kịch bản sốc lãi suất kết hợp mức tăng 25% độ biến động ngầm định [[src-bcbs-irrbb-2016#^irrbb-u05-7]].

### 4. Tổng hợp đa tiền tệ và Thước đo rủi ro EVE cực đại
Theo quy chuẩn Basel d368, tổng hợp tổn thất trên tất cả các đồng tiền trọng yếu với nguyên tắc thận trọng không bù trừ lãi từ đồng tiền khác nếu tổng thể đồng tiền đó sinh lời ($\Delta\text{EVE}_{i,c} > 0$ đại diện cho tổn thất):

$$
\Delta\text{EVE}_i = \max\left(0; \sum_{c: \Delta\text{EVE}_{i,c} > 0} \Delta\text{EVE}_{i,c}\right)
$$

Thước đo rủi ro EVE chuẩn hoá tổng thể là mức tổn thất lớn nhất trong 6 kịch bản sốc:

$$
\text{Standardised EVE risk measure} = \max_{i \in \{1..6\}} \Delta\text{EVE}_i
$$

## Quy chuẩn công bố Trụ cột 3 (Nguyên tắc 8)

Khi tính toán $\Delta\text{EVE}$ phục vụ công bố thông tin theo Bảng B [[src-bcbs-irrbb-2016#^irrbb-p08-1]], ngân hàng phải tuân thủ nghiêm ngặt các nguyên tắc:
1. **Loại trừ vốn chủ sở hữu**: Vốn chủ sở hữu không được gán lãi suất hay kỳ hạn mà bị loại bỏ hoàn toàn khỏi tính toán; tỷ lệ sụt giảm được so sánh trực tiếp với quy mô vốn tự có [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
2. **Dòng tiền toàn diện**: Bao gồm tất cả tài sản sinh lời, nợ phải trả và các cam kết ngoại bảng chịu lãi suất; loại trừ tài sản cố định và các khoản đầu tư vốn bị trừ khỏi vốn CET1 [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
3. **Đường cong chiết khấu**: Sử dụng lãi suất phi rủi ro (risk-free zero coupon rate, ví dụ đường cong OIS hoặc swap có bảo đảm); nếu dòng tiền tính cả biên thương mại (commercial margin) thì lãi suất chiết khấu cũng phải cộng thêm biên tương ứng [[src-bcbs-irrbb-2016#^irrbb-p08-2]].
4. **Giả định bảng cân đối**: Bắt buộc sử dụng giả định bảng cân đối run-off [[src-bcbs-irrbb-2016#^irrbb-p08-2]].

## So sánh với Thước đo Thu nhập ($\Delta\text{NII}$)

| Đặc tính so sánh | Thước đo Giá trị kinh tế ($\Delta\text{EVE}$) | Thước đo Thu nhập ($\Delta\text{NII}$) |
|---|---|---|
| **Mục tiêu đo lường** | Biến động giá trị thị trường nội tại của vốn chủ sở hữu [[src-bcbs-irrbb-2016#^irrbb-u06-5]] | Biến động lợi nhuận từ lãi trong kỳ kế toán [[src-bcbs-irrbb-2016#^irrbb-u06-5]] |
| **Đường chân trời** | Dài hạn — Run-off horizon đến khi tài sản/nợ cuối cùng đáo hạn [[src-bcbs-irrbb-2016#^irrbb-p04-2]] | Ngắn-trung hạn — 12 tháng (công bố) hoặc 1–3 năm [[src-bcbs-irrbb-2016#^irrbb-p08-3]] |
| **Giả định bảng cân đối** | Run-off balance sheet (không tái đầu tư) [[src-bcbs-irrbb-2016#^irrbb-p08-2]] | Constant balance sheet (tái đầu tư thay thế tương đương) hoặc Dynamic [[src-bcbs-irrbb-2016#^irrbb-p08-3]] |
| **Đối xử với Vốn chủ sở hữu** | Loại bỏ khỏi dòng tiền chiết khấu [[src-bcbs-irrbb-2016#^irrbb-p08-2]] | Vốn chủ sở hữu tạo ra thu nhập cơ sở (endowment return) [[src-bcbs-irrbb-2016#^irrbb-u06-6]] |
| **Cơ chế chiết khấu** | Chiết khấu dòng tiền theo đường cong phi rủi ro [[src-bcbs-irrbb-2016#^irrbb-p08-2]] | Không chiết khấu (tính toán số học chênh lệch thu nhập) [[src-bcbs-irrbb-2016#^irrbb-u06-5]] |
| **Trọng tâm quản trị** | Cơ quan giám sát (Pillar 2 capital adequacy & Outlier test) [[src-bcbs-irrbb-2016#^irrbb-u02-4]] | Ban điều hành & ALCO (kế hoạch tài chính, cổ tức, P&L) [[src-bcbs-irrbb-2016#^irrbb-u02-4]] |

## Mối liên kết chiến lược với Đệm HQLA và NSFR
- **Thời lượng HQLA**: Danh mục trái phiếu chính phủ Level 1 trong [[lcr]] có thời lượng bình quân lớn (ví dụ duration 5–7 năm) sẽ tạo ra mức nhạy cảm lãi suất cực lớn ($\text{PV01}$ cao). Khi chịu cú sốc tăng lãi suất song song (+200 bps USD/EUR), danh mục HQLA sẽ sụt giảm giá trị thị trường sâu sắc, kéo giảm nghiêm trọng $\Delta\text{EVE}$ và đẩy ngân hàng vào nguy cơ vi phạm ngưỡng ngoại lai 15% Tier 1 Capital.
- **Tài trợ chênh lệch kỳ hạn trong NSFR**: Một ngân hàng duy trì tài sản dài hạn (RSF 85%–100%) tài trợ bởi tiền gửi ngắn hạn sẽ chịu chênh lệch kỳ hạn âm lớn, khiến EVE cực kỳ tổn thương trước các cú sốc tăng dốc đường cong (steepener) hoặc tăng song song.
- **Mô hình định lượng và công cụ phòng ngừa liên quan**:
  - [[duration-gap-model|Mô hình Chênh lệch Thời lượng (Duration Gap Model)]]: Phân tích độ nhạy tổng thể và phương trình miễn nhiễm vốn tự có.
  - [[key-rate-duration|Thời lượng Lãi suất Từng Kỳ hạn (Key Rate Duration - KRD)]]: Phân rã độ nhạy trên 19 dải kỳ hạn để đo lường rủi ro xoay trục đường cong.
  - [[economic-value-at-risk|Giá trị Kinh tế Chịu Rủi ro (EVaR)]]: Đo lường tổn thất EVE tối đa theo phương pháp phân phối xác suất và mô phỏng Monte Carlo.
  - [[interest-rate-swap|Hợp đồng Hoán đổi Lãi suất (IRS)]]: Công cụ tái cân bằng thời lượng và phòng ngừa tổn thất EVE chủ lực.
- Xem chi tiết tại [[integrated-alm-liquidity-strategy]], [[irrbb-alm-governance-strategy-and-tradeoffs]].
