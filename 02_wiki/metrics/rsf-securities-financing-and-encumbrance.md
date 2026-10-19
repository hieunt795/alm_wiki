---
title: "Tài trợ có Bảo đảm và Quản trị Cầm cố Tài sản trong NSFR (Securities Financing and Encumbrance)"
aliases: [Cầm cố tài sản NSFR, Securities Financing and Encumbrance, RSF Repo và Encumbrance]
type: metric
domains: [alm, basel, product]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-bcbs-lcr]]"]
relations:
  - {type: part-of, to: "[[required-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-20]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "-", cite: "[[src-bcbs-nsfr#^nsf30-20]]"}
tags: [nsfr, rsf, repo, encumbrance, collateral, covered-bonds]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

Nghiệp vụ tài trợ có bảo đảm (repo, reverse repo, hoán đổi tài sản bảo đảm) và mức độ cầm cố tài sản ([[asset-encumbrance]]) là các nhân tố có tính quyết định đến mẫu số [[required-stable-funding|RSF]], nhận hệ số **RSF từ 10% đến 100%** tùy thuộc vào thời hạn cầm cố và loại tài sản bảo đảm [[src-bcbs-nsfr#^nsf30-20]] [[src-bcbs-nsfr#^nsf30-27]] [[src-bcbs-nsfr#^nsf30-28]]. Chuẩn mực NSFR thiết lập nguyên tắc nghiêm ngặt rằng: một tài sản thanh khoản cao khi đã bị cầm cố để huy động vốn hoặc phát hành trái phiếu có bảo đảm dài hạn thì không thể dùng để giải quyết các nghĩa vụ thanh khoản khác, do đó bắt buộc phải được tài trợ hoàn toàn bằng nguồn vốn ổn định dài hạn [[src-bcbs-nsfr#^nsf30-20]].

## Công thức & tham số

### 1. Khung Thời gian Cầm cố Tài sản (Encumbrance Time Horizon)
Theo NSF30.20, mức độ yêu cầu nguồn vốn ổn định đối với tài sản nội bảng bị cầm cố được phân loại theo thời gian bị khóa thanh khoản [[src-bcbs-nsfr#^nsf30-20]]:
1. **Cầm cố từ 1 năm trở lên ($\ge 1$ năm)**: Toàn bộ tài sản bị cầm cố từ 1 năm trở lên chịu hệ số **RSF 100%** [[src-bcbs-nsfr#^nsf30-20]].
   - *Hệ quả đặc biệt*: Kể cả khi tài sản cầm cố là Trái phiếu Chính phủ Level 1 (vốn chỉ chịu RSF 5% khi unencumbered [[src-bcbs-nsfr#^nsf30-26]]), nhưng nếu đem đi repo kỳ hạn 13 tháng hoặc đưa vào kho tài sản bảo đảm của chương trình covered bond dài hạn, hệ số RSF vọt ngay lên 100% [[src-bcbs-nsfr#^nsf30-20]].
2. **Cầm cố từ 6 tháng đến dưới 1 năm**:
   - Nếu tài sản đó ở trạng thái unencumbered có $\text{RSF} \le 50\%$ (ví dụ HQLA Level 1 hoặc Level 2A), khi bị cầm cố từ 6 tháng đến dưới 1 năm sẽ bị nâng hệ số lên **RSF 50%** [[src-bcbs-nsfr#^nsf30-20]].
   - Nếu tài sản đó vốn dĩ có $\text{RSF} > 50\%$ (ví dụ cho vay thương mại có RSF 85%), khi bị cầm cố vẫn giữ nguyên mức RSF cao hơn đó [[src-bcbs-nsfr#^nsf30-20]].
3. **Cầm cố dưới 6 tháng ($< 6$ tháng)**: Tài sản tiếp tục nhận hệ số RSF như khi ở trạng thái unencumbered (ví dụ Level 1 vẫn giữ RSF 5%) [[src-bcbs-nsfr#^nsf30-20]].

## Diễn giải

### Cơ chế & drivers

#### 2. Nghiệp vụ Cho vay có Bảo đảm (Reverse Repo) đối với Tổ chức Tài chính
Theo NSF30.27 và NSF30.28, khi ngân hàng thực hiện cho vay có bảo đảm (Reverse Repo) đối với các định chế tài chính với kỳ hạn còn lại dưới 6 tháng [[src-bcbs-nsfr#^nsf30-27]] [[src-bcbs-nsfr#^nsf30-28]]:
- **RSF 10%**: Áp dụng nếu khoản cho vay được bảo đảm bằng tài sản [[level-1-assets]] và ngân hàng có quyền tự do **tái thế chấp (*rehypothecate*)** tài sản bảo đảm đó trong suốt vòng đời của khoản vay [[src-bcbs-nsfr#^nsf30-27]].
- **RSF 15%**: Áp dụng cho tất cả các khoản cho vay đối với định chế tài chính kỳ hạn dưới 6 tháng khác (bao gồm cho vay không bảo đảm, hoặc bảo đảm bằng tài sản Level 2A, Level 2B hoặc non-HQLA) [[src-bcbs-nsfr#^nsf30-28]].

#### 3. Nguyên tắc Ghi nhận Kế toán Gộp và Quyền Sở hữu Hưởng lợi
Theo NSF30.21 và NSF30.22 [[src-bcbs-nsfr#^nsf30-21]] [[src-bcbs-nsfr#^nsf30-22]]:
- **Quyền sở hữu hưởng lợi (Beneficial Ownership)**: Chứng khoán đi vay qua giao dịch reverse repo hoặc collateral swap mà ngân hàng không có quyền sở hữu hưởng lợi sẽ **không được ghi nhận vào tài sản** trên bảng cân đối kế toán, do đó không phát sinh RSF đối với chứng khoán đó [[src-bcbs-nsfr#^nsf30-21]]. Ngược lại, chứng khoán ngân hàng đem cho vay (repo) mà vẫn giữ quyền sở hữu hưởng lợi thì vẫn phải nằm trên bảng cân đối và chịu RSF tương ứng [[src-bcbs-nsfr#^nsf30-21]].
- **Báo cáo trên cơ sở gộp (Gross Basis)**: Các khoản phải thu (RSF) và phải trả (ASF) từ giao dịch repo/reverse repo phải được báo cáo gộp, chỉ được phép bù trừ ròng đối với cùng một đối tác duy nhất nếu thỏa mãn các điều kiện bù trừ thanh toán nghiêm ngặt theo chuẩn mực đòn bẩy LEV30 [[src-bcbs-nsfr#^nsf30-22]].

#### 4. Xử lý Tài sản Tách biệt và Cầm cố Vượt mức (Excess Over-Collateralisation)
- **Tài sản tách biệt ký quỹ khách hàng (NSF99.5)**: Tài sản thuộc sở hữu của ngân hàng nhưng bị tách biệt để bảo vệ vốn khách hàng trong các tài khoản giao dịch ký quỹ (segregated customer accounts) phải được xét theo thời hạn cầm cố để áp hệ số RSF phù hợp [[src-bcbs-nsfr#^nsf99-5]].
- **Cầm cố vượt mức trong Covered Bonds (FAQ NSF30.20)**: Phần tài sản thế chấp vượt mức yêu cầu pháp lý (*excess OC*) nếu nằm trong kho tài sản bảo đảm của chương trình phát hành đơn lẻ và không thể rút ra mà không làm suy giảm xếp hạng tín nhiệm thì vẫn bị coi là tài sản bị cầm cố và chịu **RSF 100%**.

### Phụ thuộc regime
- **Thị trường Tài trợ Ngắn hạn Căng thẳng (Repo Freeze)**:
  - Khi thị trường repo đóng băng, việc tái tài trợ cho các khoản vay reverse repo bị ngưng trệ.
  - Ngân hàng nắm giữ tài sản bảo đảm nhưng không thể thanh lý trên thị trường, rủi ro cầm cố kéo dài buộc ngân hàng phải dự phòng thêm nguồn vốn ổn định dài hạn.

### Bằng chứng thực nghiệm
- Trong cuộc khủng hoảng tài chính toàn cầu 2008, hiện tượng "Run on Repo" xảy ra khi các bên cho vay từ chối tái tục hợp đồng repo qua đêm và nâng haircut lên 50%–100%, biến hàng nghìn tỷ USD tài sản có bảo đảm thành tài sản bị khóa thanh khoản. Đây là cơ sở thực tiễn để Basel thiết lập khung quy định encumbrance chặt chẽ trong NSFR.

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM Treasury & Collateral Management**:
  - Quản trị tài sản bảo đảm tập trung (Centralised Collateral Optimization): Khối Treasury phải giám sát chặt chẽ thời hạn của các hợp đồng repo. Tránh tối đa các hợp đồng repo có kỳ hạn vắt qua mốc 1 năm vì sẽ biến tài sản Level 1 (RSF 5%) thành tài sản chịu RSF 100%.
  - Tận dụng quyền tái thế chấp (Rehypothecation): Khi cấp tín dụng ngắn hạn cho các công ty chứng khoán, Treasury phải yêu cầu tài sản bảo đảm là Trái phiếu Chính phủ Level 1 kèm điều khoản tự do tái thế chấp để giảm hệ số RSF từ 15% xuống 10% [[src-bcbs-nsfr#^nsf30-27]].
- **Thị trường Sản phẩm Phái sinh & Repo (Securities Financing)**:
  - Bàn giao dịch Repo (Repo Desk) không thể hoạt động độc lập mà phải phối hợp với ALM để tính toán chi phí vốn chuyển nhượng nội bộ (FTP) phát sinh từ các khoản phải thu repo.

## Câu hỏi mở
- Thị trường repo tại Việt Nam hiện chủ yếu thực hiện qua kênh OMO với NHNN và giao dịch Outright/Repo Trái phiếu Chính phủ trên HNX. Khi TT50 có hiệu lực, các giao dịch repo OMO kỳ hạn 7–14 ngày của NHNN sẽ được đối xử như thế nào trong mô hình encumbrance của các ngân hàng?
