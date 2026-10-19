---
title: Liquidity transfer restrictions
aliases: [Liquidity transfer restrictions, Ring-fencing, Rào cản chuyển giao thanh khoản, Hạn chế chuyển giao thanh khoản]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: limits, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr30-24]]"}
  - {type: limits, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr10-8]]"}
tags: [liquidity, ring-fencing, cross-border, consolidated-lcr]
updated: 2026-10-15
reviewed:
---

## Ý chính
Rào cản chuyển giao thanh khoản (liquidity transfer restrictions / ring-fencing) là các hạn chế pháp lý, quy chế quản lý hoặc kiểm soát ngoại hối ngăn cản việc tự do điều chuyển [[hqla]] và dòng vốn giữa các pháp nhân trong cùng một tập đoàn ngân hàng xuyên biên giới [[src-bcbs-lcr#^lcr10-7]]. Nguyên tắc cốt lõi của [[lcr]] hợp nhất là **không được ghi nhận thanh khoản thặng dư** (no excess liquidity recognised) nếu có nghi ngờ hợp lý về tính sẵn sàng điều chuyển của nguồn vốn đó [[src-bcbs-lcr#^lcr10-7]].

## Cơ chế & drivers

### Xử lý HQLA của thực thể chịu hạn chế trong LCR hợp nhất
Khi một pháp nhân hoặc chi nhánh trong tập đoàn hoạt động tại khu vực pháp lý có rào cản chuyển giao thanh khoản (ví dụ kiểm soát ngoại hối, không chuyển đổi tự do đồng nội tệ, hoặc quy định khoanh vùng bảo vệ người gửi tiền nội địa — ring-fencing):
- **Khống chế mức ghi nhận**: HQLA đủ điều kiện do thực thể đó nắm giữ chỉ được đưa vào [[lcr]] hợp nhất **tối đa bằng tổng dòng tiền ra ròng (total net cash outflows)** của chính thực thể đó [[src-bcbs-lcr#^lcr10-7]].
- **Loại trừ thặng dư (Surplus exclusion)**: Bất kỳ lượng HQLA nào vượt quá dòng tiền ra ròng cục bộ (HQLA surplus) nếu không thể chuyển giao tự do về công ty mẹ hoặc các thực thể khác trong tập đoàn thì **bắt buộc phải loại bỏ hoàn toàn** khỏi tử số LCR hợp nhất [[src-bcbs-lcr#^lcr10-7]] [[src-bcbs-lcr#^lcr30-27]].
- **Phạm vi hạn chế cần tính toán**: Bị giới hạn ở các rào cản hiện hữu theo luật định, quy định của cơ quan giám sát có thẩm quyền [[src-bcbs-lcr#^lcr10-8]]. Tập đoàn phải duy trì quy trình định kỳ rà soát các rào cản chuyển giao và lượng hóa tác động thanh khoản toàn diện [[src-bcbs-lcr#^lcr10-3]] [[src-bcbs-lcr#^lcr10-8]].

### Rủi ro không thể chuyển đổi tiền tệ trong stress
- Dù LCR được tính toán và báo cáo bằng một đồng tiền báo cáo chung ở cấp hợp nhất, ngân hàng và cơ quan thanh tra không được phép giả định các đồng tiền sẽ duy trì khả năng chuyển đổi hoặc chuyển giao tự do trong thời kỳ khủng hoảng [[src-bcbs-lcr#^lcr10-9]].
- Cơ cấu đồng tiền của danh mục HQLA bắt buộc phải tương thích với phân bổ nhu cầu dòng tiền ra theo từng đồng tiền trọng yếu [[src-bcbs-lcr#^lcr10-9]] [[src-bcbs-lcr#^lcr30-27]].

### Intra-group lending (Choudhry, UK)
- Intra-group lending (IGL) là yếu tố đáng kể của rủi ro thanh khoản trong tập đoàn; chính sách IGL phải tuân thủ quy định của mọi jurisdiction mà ngân hàng hoạt động [[src-choudhry-principles-banking#^choudhry-igl-1]].
- Ở UK, IGL thường được quản lý trong khung large exposure, giới hạn tổng IGL ở 25% capital base của ngân hàng cho vay. Ví dụ ngân hàng có vốn €500 triệu thì hạn mức IGL tổng là €125 triệu [[src-choudhry-principles-banking#^choudhry-igl-2]].
- Ngân hàng có thể lập "Integrated Group": không giới hạn phơi nhiễm, trọng số rủi ro 0%. Đối tác không đạt tiêu chí thuộc non-integrated group, tổng phơi nhiễm phải trong 25% [[src-choudhry-principles-banking#^choudhry-igl-2]].
- Mọi yêu cầu IGL mới phải được thành viên điều hành của công ty vay và [[alm-operating-model|Group Treasury]]/Group ALCO phê duyệt trước giao dịch [[src-choudhry-principles-banking#^choudhry-igl-3]].
- Choudhry khuyến nghị mọi pháp nhân và địa bàn "stand alone" về thanh khoản và funding, mỗi nơi có kế hoạch dự phòng riêng [[src-choudhry-principles-banking#^choudhry-liq-10]]. FSA PS 09/16 yêu cầu ngân hàng UK có thể "stand alone" [[src-choudhry-principles-banking#^choudhry-liq-4]].

## Tác động ALM
*Diễn giải:*
- **Bẫy thanh khoản cục bộ (Liquidity Trap)**: Trong một tập đoàn ngân hàng đa quốc gia, công ty con tại nước A có thể đạt LCR solo rất cao (ví dụ 250%), nhưng lượng HQLA thặng dư này bị "mắc kẹt" tại nước A do ring-fencing. Khi ngân hàng mẹ hoặc công ty con tại nước B gặp khủng hoảng rút tiền, thặng dư tại nước A không thể bù đắp được, khiến LCR hợp nhất thực tế thấp hơn nhiều so với phép cộng cơ học số dư bảng cân đối kế toán.
- **Tối ưu hóa mô hình Treasury (Centralised vs Decentralised)**: ALM phải cân đối giữa việc tập trung hóa nguồn vốn tại hội sở chính (để tối ưu chi phí vốn và FTP) với yêu cầu duy trì lớp đệm thanh khoản độc lập tại từng thực thể sở tại nhằm tuân thủ quy định ring-fencing của nước chủ nhà (Host jurisdiction).

## Phụ thuộc regime
- **Regime bình thường**: Các giao dịch hoán đổi ngoại tệ (FX swaps) và thị trường liên ngân hàng xuyên biên giới vận hành thông suốt, dòng vốn nội bộ có thể chu chuyển tương đối dễ dàng.
- **Regime stress**: Cơ quan giám sát tại các nước sở tại (Host) thường có xu hướng lập tức siết chặt ring-fencing, phong tỏa dòng kiều hối hoặc hạn chế chuyển ngoại tệ về công ty mẹ để bảo vệ quyền lợi người gửi tiền trong nước, khiến rào cản chuyển giao thanh khoản trở nên gay gắt đột biến [[src-bcbs-lcr#^lcr10-7]] [[src-bcbs-lcr#^lcr10-9]].

## Góc nhìn theo domain
- **Basel**: Chuẩn hóa nguyên tắc thận trọng tại LCR10.7–10.9 và LCR30.21, yêu cầu loại bỏ hoàn toàn "thanh khoản ảo" trên báo cáo hợp nhất [[src-bcbs-lcr#^lcr10-1]] [[src-bcbs-lcr#^lcr10-7]].
- **VN**: Pháp lệnh Ngoại hối và các quy định của NHNN về quản lý dòng vốn xuyên biên giới thiết lập cơ chế kiểm soát chuyển tiền ra nước ngoài đối với các chi nhánh ngân hàng nước ngoài tại Việt Nam.

## Câu hỏi mở
- Khi tính LCR hợp nhất cho một NHTM Việt Nam có ngân hàng con tại Lào/Campuchia, cơ chế loại trừ thặng dư HQLA theo quy định của NHNN (TT50/2026) được hướng dẫn chi tiết như thế nào?
