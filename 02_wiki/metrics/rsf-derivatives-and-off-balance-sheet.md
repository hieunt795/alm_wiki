---
title: "Phái sinh và Cam kết Ngoại bảng trong NSFR (Derivatives and Off-Balance Sheet Exposures)"
aliases: [Phái sinh trong NSFR, Derivatives and Off-Balance Sheet NSFR, RSF Phái sinh và Ngoại bảng]
type: metric
domains: [alm, basel, product]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[required-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-31]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "-", cite: "[[src-bcbs-nsfr#^nsf30-32]]"}
tags: [nsfr, rsf, derivatives, initial-margin, ccp, off-balance-sheet, commitments]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

Nghiệp vụ phái sinh và các cam kết thanh khoản ngoại bảng là các cấu phần tạo ra nhu cầu nguồn vốn ổn định tiềm tàng đáng kể trong mẫu số [[required-stable-funding|RSF]], nhận hệ số **RSF từ 5% đến 100%** [[src-bcbs-nsfr#^nsf30-4]] [[src-bcbs-nsfr#^nsf30-31]] [[src-bcbs-nsfr#^nsf30-32]] [[src-bcbs-nsfr#^nsf30-34]]. Dù các hoạt động này không phát sinh nhu cầu tài trợ tiền mặt trực tiếp tức thì trên sổ sách, chúng tiềm ẩn nguy cơ rút cạn nguồn vốn thanh khoản của ngân hàng trong vòng 1 năm khi đối tác rút hạn mức tín dụng hoặc khi thị trường phái sinh biến động đòi hỏi ký quỹ bổ sung [[src-bcbs-nsfr#^nsf30-4]].

## Công thức & tham số

### Cơ chế & drivers

#### 1. Cơ chế Đo lường Phái sinh trong RSF
Chuẩn mực NSFR thiết lập 3 tầng đo lường đối với danh mục phái sinh:

##### A. Tài sản Phái sinh Ròng (Net Derivative Assets - RSF 100%)
- **Xác định Tài sản Phái sinh NSFR**: Đo lường bằng chi phí thay thế dương (*positive replacement cost*) sau khi áp dụng bù trừ song phương đủ điều kiện theo CRE52.7 [[src-bcbs-nsfr#^nsf30-23]].
- **Điều kiện bù trừ tài sản bảo đảm (Variation Margin)**: Tài sản bảo đảm nhận về **không được phép bù trừ** vào chi phí thay thế dương, trừ khi nhận dưới dạng **ký quỹ biến đổi bằng tiền mặt (cash variation margin)** thỏa mãn đầy đủ các điều kiện khắt khe của chuẩn mực đòn bẩy LEV30 (được trao đổi hàng ngày và coi như khoản thanh toán trước) [[src-bcbs-nsfr#^nsf30-24]].
- **Hệ số RSF**: Nếu sau khi bù trừ, tổng tài sản phái sinh NSFR lớn hơn tổng nợ phái sinh NSFR, phần chênh lệch ròng này chịu hệ số **RSF 100%** [[src-bcbs-nsfr#^nsf30-32]].

##### B. Ký quỹ Ban đầu và Đóng góp Quỹ Vỡ nợ CCP (RSF 85%)
- Tiền mặt, chứng khoán hoặc bất kỳ tài sản nào ngân hàng đặt cọc dưới dạng **Ký quỹ Ban đầu (*Initial Margin*)** cho các hợp đồng phái sinh hoặc đóng góp vào **Quỹ Dự phòng Vỡ nợ (*Default Fund*)** của Trung tâm Bù trừ Đối tác Trung tâm (CCP) đều phải chịu hệ số **RSF 85%** (bất kể tài sản đó được ghi nhận nội bảng hay ngoại bảng) [[src-bcbs-nsfr#^nsf30-31]].
- *Ngoại lệ*: Nếu tài sản đem ký quỹ vốn dĩ có hệ số RSF cao hơn (ví dụ cổ phiếu chưa niêm yết có RSF 100%), tài sản đó sẽ giữ nguyên hệ số cao hơn [[src-bcbs-nsfr#^nsf30-31]].

##### C. Khoản Cộng thêm Nợ Phái sinh Gộp (Derivative Liabilities Add-on - RSF 100%)
- Theo NSF30.32(5), ngân hàng phải tính thêm vào mẫu số RSF một khoản tương đương **5% đến 20% (theo quyết định của cơ quan giám sát quốc gia) của tổng Nợ Phái sinh Gộp (*Gross Derivative Liabilities*)** nhân với hệ số **RSF 100%** [[src-bcbs-nsfr#^nsf30-32]].
- **Đặc điểm kỹ thuật cốt lõi**:
  - Nợ phái sinh gộp được tính bằng tổng chi phí thay thế âm **trước khi trừ đi tài sản bảo đảm variation margin đã đặt cọc** (FAQ NSF30.32) [[src-bcbs-nsfr#^nsf30-32]].
  - Khoản cộng thêm này áp dụng cho mọi trường hợp, **kể cả khi ngân hàng đang ở vị thế tài sản phái sinh ròng** (FAQ NSF30.32).
  - Áp dụng cả đối với các hợp đồng phái sinh có cấu trúc thanh toán hàng ngày (*Settled-to-Market*) (FAQ NSF30.32).
  - *Ý nghĩa ALM*: Khoản đệm này buộc ngân hàng phải dự phòng nguồn vốn ổn định cho rủi ro biến động định giá phái sinh trong tương lai (*potential future exposure*).

```
+-------------------------------------------------------------------------+
|                  CƠ CẤU YÊU CẦU NGUỒN VỐN CHO PHÁI SINH TRONG NSFR       |
+-------------------------------------------------------------------------+
| Cấu phần phái sinh                      | Hệ số RSF | Cơ chế tính toán   |
|-----------------------------------------|:---------:|--------------------|
| Tài sản phái sinh ròng (Net Assets)     |   100%    | NSF30.23 & 30.32   |
| Ký quỹ ban đầu (Initial Margin) & CCP   |    85%    | NSF30.31           |
| Nợ phái sinh gộp (5%–20% Gross Liab.)   |   100%    | NSF30.32(5)        |
+-------------------------------------------------------------------------+
```

#### 2. Cam kết Ngoại bảng (Off-Balance Sheet Commitments)
Theo NSF30.34 và Bảng 3 NSF99.3 [[src-bcbs-nsfr#^nsf30-34]] [[src-bcbs-nsfr#^nsf99-3]]:
- **Hạn mức Cam kết Tín dụng và Thanh khoản Chưa rút**: Phần giá trị chưa giải ngân của các hạn mức không thể hủy ngang hoặc chỉ có thể hủy ngang có điều kiện (*irrevocable and conditionally revocable credit and liquidity facilities*) cấp cho bất kỳ khách hàng nào đều chịu hệ số **RSF 5%** [[src-bcbs-nsfr#^nsf30-34]].
- **Các Nghĩa vụ Tài trợ Tiềm tàng Khác**: Áp dụng hệ số RSF theo quyết định của cơ quan quản lý quốc gia, bao gồm:
  - Hạn mức tín dụng có thể hủy ngang vô điều kiện (*unconditionally revocable*).
  - Nghĩa vụ liên quan đến tài trợ thương mại (Trade finance: bảo lãnh thanh toán, thư tín dụng L/C).
  - Nghĩa vụ phi hợp đồng: yêu cầu mua lại thương phiếu hoặc hỗ trợ thanh khoản cho các công ty liên kết đặc biệt (SPEs, Conduits, SIVs) hoặc các quỹ đầu tư duy trì NAV cố định.

## Diễn giải

### Phụ thuộc regime
- **Khi Thị trường Tài chính Biến động Mạnh (High Market Volatility)**:
  - Giá trị thị trường của các hợp đồng phái sinh (IRS, FX Swaps, Commodity Swaps) biến động dữ dội, kích hoạt các đợt gọi ký quỹ bổ sung (Margin Calls).
  - Khoản tiền mặt và tài sản bị hút vào ký quỹ ban đầu (RSF 85%) tăng vọt, đồng thời tổng nợ phái sinh gộp tăng cao làm gia tăng khoản phạt add-on (RSF 100%), gây áp lực suy giảm tỷ lệ NSFR tức thì.

### Bằng chứng thực nghiệm
- Trong sự kiện "Dash for Cash" vào tháng 3/2020 khi đại dịch Covid bùng phát, các ngân hàng toàn cầu phải đối mặt với các đợt gọi ký quỹ phái sinh kỷ lục từ các CCP (hơn 300 tỷ USD trên toàn cầu), làm tăng vọt mẫu số RSF đối với các khoản ký quỹ ban đầu và chứng minh tính cần thiết của các hệ số RSF 85% và khoản cộng thêm 5%–20%.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM Treasury & Trading Desk**:
  - Tối ưu hóa hợp đồng CSA (Credit Support Annex): Khối Treasury phải đàm phán các điều khoản CSA tiêu chuẩn hóa để đủ điều kiện bù trừ song phương ròng theo CRE52.7, và sử dụng tiền mặt làm variation margin để được khấu trừ vào tài sản phái sinh theo LEV30 [[src-bcbs-nsfr#^nsf30-24]].
  - Kiểm soát quy mô hạn mức cam kết cấp cho khách hàng: Dù khách hàng chưa rút vốn, mỗi 1.000 tỷ VND hạn mức cam kết cấp ra vẫn ngốn của ngân hàng 50 tỷ VND nguồn vốn ổn định dài hạn (RSF 5%). Treasury phải áp phí thanh khoản duy trì hạn mức (*Commitment Liquidity Fee*) lên các khối kinh doanh.
- **Quản lý Rủi ro Thị trường & Đối tác**:
  - Theo dõi sát sao mức độ phơi bày phái sinh với các đối tác lớn để ngăn ngừa rủi ro vỡ nợ dây chuyền và tổn thất thanh khoản ký quỹ.

## Câu hỏi mở
- Tại Việt Nam, hoạt động phái sinh tiền tệ (FX Swap, Cross-Currency Swap) và phái sinh lãi suất (IRS) chủ yếu giao dịch OTC song phương chưa qua CCP. Cơ quan thanh tra NHNN sẽ áp dụng tỷ lệ trích nợ phái sinh gộp ở mức sàn 5% hay nâng lên mức trần 20%?
