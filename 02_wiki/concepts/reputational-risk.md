---
title: "Reputational Risk"
aliases: [Reputational Risk, Rủi ro danh tiếng, Rủi ro uy tín, Implicit support, Hỗ trợ ngầm]
type: concept
domains: [basel, alm]
status: active
maturity: draft
valid_from: 2019-12-15
valid_to:
as_of:
sources: ["[[src-bcbs-framework]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: input-to, to: "[[icaap]]", cite: "[[src-bcbs-framework#^srp30-30]]"}
  - {type: input-to, to: "[[contingency-funding-plan]]", cite: "[[src-bcbs-framework#^srp30-30]]"}
  - {type: input-to, to: "[[stress-testing]]", cite: "[[src-bcbs-framework#^srp30-34]]"}
tags: [reputational-risk, pillar-2, liquidity]
updated: 2026-10-20
reviewed:
---

## Ý chính
Theo SRP30, rủi ro danh tiếng là rủi ro phát sinh từ nhận thức tiêu cực của khách hàng, đối tác, cổ đông, nhà đầu tư, chủ nợ, nhà phân tích hoặc cơ quan quản lý. Nhận thức đó ảnh hưởng tới khả năng duy trì hoặc thiết lập quan hệ kinh doanh và khả năng tiếp cận nguồn vốn, ví dụ qua thị trường liên ngân hàng hay thị trường chứng khoán hoá [[src-bcbs-framework#^srp30-29]].

Rủi ro danh tiếng có thể dẫn tới hỗ trợ ngầm (implicit support), từ đó phát sinh rủi ro tín dụng, thanh khoản, thị trường và pháp lý, ảnh hưởng tới thu nhập, thanh khoản và vốn [[src-bcbs-framework#^srp30-30]]. SRP30.8 xếp rủi ro danh tiếng vào nhóm rủi ro trọng yếu mà quy trình quản trị rủi ro toàn hàng nên bao gồm, cùng rủi ro pháp lý và chiến lược [[src-bcbs-framework#^srp30-8]].

## Cơ chế & drivers
**Nguồn rủi ro.** Ngân hàng nên nhận diện nguồn rủi ro danh tiếng: các mảng kinh doanh, nợ phải trả, hoạt động liên kết, vehicle ngoại bảng và thị trường hoạt động [[src-bcbs-framework#^srp30-30]]. Ví dụ theo SRP30.32 [[src-bcbs-framework#^srp30-32]]:
- bảo trợ cấu trúc chứng khoán hoá như ABCP conduit và SIV, bán khoản tín dụng cho trust chứng khoán hoá;
- bảo trợ quỹ thị trường tiền tệ, hedge fund nội bộ, REIT.

**Hỗ trợ ngầm khi stress.** Trước biến động 2007, nhiều ngân hàng không nhận ra rủi ro danh tiếng của vehicle ngoại bảng. Khi stress, một số ngân hàng đã hỗ trợ vượt nghĩa vụ hợp đồng cho các cấu trúc chứng khoán hoá và vehicle do mình bảo trợ [[src-bcbs-framework#^srp30-31]]. Xem [[securitisation]].

**Kênh nợ phải trả.** Niềm tin thị trường và khả năng huy động vốn gắn với danh tiếng. Để tránh tổn hại uy tín, ngân hàng có thể gọi (mua lại) nợ trước hạn dù làm xấu hồ sơ thanh khoản. Điều này đặc biệt đúng với nợ là cấu phần vốn quy định như nợ hybrid hoặc nợ thứ cấp, khi đó vị thế vốn cũng bị ảnh hưởng [[src-bcbs-framework#^srp30-33]]. Xem [[contingent-convertible-bond]].

**Kênh thanh khoản.** Ngân hàng nên xét tác động của rủi ro danh tiếng lên vị thế thanh khoản tổng thể: tài sản có thể tăng và nguồn vốn có thể bị hạn chế khi đối tác mất niềm tin [[src-bcbs-framework#^srp30-36]].

**Đo lường.**
- Ngân hàng nên đo mức hỗ trợ có thể phải cung cấp (kể cả hỗ trợ ngầm cho chứng khoán hoá) hoặc tổn thất khi thị trường bất lợi. Một cách làm là đưa kịch bản rủi ro danh tiếng vào stress test định kỳ [[src-bcbs-framework#^srp30-35]].
- Quy trình stress testing nên tính đến rủi ro danh tiếng và hiệu ứng vòng hai [[src-bcbs-framework#^srp30-34]]. Xem [[stress-testing]].
- Rủi ro này nên được xử lý trong [[icaap]] và kế hoạch dự phòng thanh khoản [[src-bcbs-framework#^srp30-30]]. Xem [[contingency-funding-plan]].

**Sản phẩm mới.** Ngân hàng nên có chính sách nhận diện nguồn rủi ro danh tiếng khi vào thị trường, sản phẩm hoặc mảng hoạt động mới [[src-bcbs-framework#^srp30-34]]. Xem [[new-product-approval]].

## Phụ thuộc regime
- Hỗ trợ ngầm cho vehicle ngoại bảng bộc lộ khi stress, như giai đoạn 2007 [[src-bcbs-framework#^srp30-31]].

## Góc nhìn theo domain
- **Basel**: SRP30.29–30.36, Pillar 2, phiên bản hiệu lực từ 15/12/2019 [[src-bcbs-framework#^srp30-0]].
- **VN**:
  - Danh sách rủi ro trọng yếu tối thiểu của TT83/2025 gồm tín dụng, thị trường, hoạt động, thanh khoản, tập trung, IRRBB và rủi ro khác theo quy định nội bộ [[src-tt83-2025-nhnn#^d3-13]], không nêu đích danh rủi ro danh tiếng.
  - TT83 đề cập danh tiếng ở hai chỗ: nhận dạng rủi ro thanh khoản phải tính cả rủi ro thanh khoản phát sinh từ rủi ro danh tiếng [[src-tt83-2025-nhnn#^d47-1]]; hạn mức rủi ro hoạt động gồm hạn mức tổn thất phi tài chính, kể cả uy tín, danh tiếng [[src-tt83-2025-nhnn#^d38-2]].
- **ALM**: *Diễn giải:*
  - Kênh nợ phải trả ở SRP30.33 có nghĩa là quyền gọi nợ trước hạn của ngân hàng (call option trên nợ thứ cấp, công cụ vốn) có thể bị thực hiện vì lý do danh tiếng, không theo tính kinh tế. Giả định kỳ hạn hành vi của các khoản nợ này trong gap thanh khoản và IRRBB nên xét kịch bản gọi sớm.
  - Kênh thanh khoản ở SRP30.36 tác động cả hai phía bảng cân đối: rút tiền gửi tăng dòng ra, trong khi hỗ trợ ngầm và cam kết ngoại bảng làm tài sản tăng. Đây là kịch bản đặc thù ngân hàng (idiosyncratic) trong [[liquidity-stress-testing]].

## Bằng chứng thực nghiệm
- Biến động 2007: một số ngân hàng hỗ trợ vượt nghĩa vụ hợp đồng cho cấu trúc chứng khoán hoá và vehicle ngoại bảng do mình bảo trợ [[src-bcbs-framework#^srp30-31]].

## Câu hỏi mở
- SRP30 không đưa phương pháp định lượng cụ thể cho rủi ro danh tiếng; chỉ gợi ý so sánh trạng thái nội bảng với mức phơi nhiễm ngoại bảng tối đa [[src-bcbs-framework#^srp30-35]].
- Phần CRE40–CRE45 về implicit support trong khung chứng khoán hoá chưa ingest [cần nguồn: src-bcbs-framework CRE40].
