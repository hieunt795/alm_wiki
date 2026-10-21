---
title: "Strategic ALM"
aliases: [Strategic ALM, ALM chiến lược, Proactive balance sheet management, 3D optimisation problem, Bài toán tối ưu 3D]
type: concept
domains: [alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [strategic-alm, balance-sheet-optimisation, risk-appetite, alco, liabilities-strategy]
updated: 2026-10-21
reviewed:
---

## Ý chính
Strategic ALM là cách tiếp cận tích hợp, gắn origination tài sản với huy động nợ và phá bỏ "silo" trong tổ chức. Choudhry định nghĩa đây là chiến lược kinh doanh toàn ngân hàng, dẫn dắt bởi các cân nhắc ALM bảng cân đối. Strategic ALM phải chủ động, từ trên xuống, và chỉ triển khai được khi có Board phê duyệt [[src-choudhry-principles-banking#^choudhry-salm-7]].

Đối lập với strategic ALM là ALM truyền thống, một quá trình "reactive". Khối kinh doanh phát sinh tài sản, nợ theo ngân sách một năm trong silo, rồi Treasury cùng Finance và Risk quản lý rủi ro ALM sau sự việc [[src-choudhry-principles-banking#^choudhry-salm-4]]. Ở Ch5, Choudhry nêu ALM ở mọi ngân hàng luôn là quá trình phản ứng và hiếm khi tích hợp được chính sách origination phía tài sản [[src-choudhry-principles-banking#^choudhry-almb-5]]; cách tiếp cận hiện tại chủ động tác động vào origination để tạo bảng cân đối tối ưu [[src-choudhry-principles-banking#^choudhry-almb-1]]. Bối cảnh lịch sử: [[alm-evolution]].

## Cơ chế & drivers
**Bài toán tối ưu 3D.** Sau Basel III, tối ưu bảng cân đối không còn là tối đa hoá RoC. Bảng cân đối phải đáp ứng nhu cầu cạnh tranh nhưng tương đương của regulator, khách hàng và cổ đông [[src-choudhry-principles-banking#^choudhry-salm-5]]. Ví dụ xung đột:
- tiền gửi doanh nghiệp lớn và NBFI là "non-sticky" theo Basel III nên đắt về thanh khoản, nhưng ngân hàng vẫn phải nhận để phục vụ khách hàng [[src-choudhry-principles-banking#^choudhry-salm-6]];
- NIBL tối đa hoá NII, trong khi Basel III đòi funding dài hạn theo hợp đồng, đắt hơn và bất lợi cho NII [[src-choudhry-principles-banking#^choudhry-salm-6]].

**Các thành phần triển khai:**

| Thành phần | Nội dung | Nguồn |
|---|---|---|
| RAS | Văn bản quan trọng nhất cần Board phê duyệt; có chỉ số và hạn mức định tính, định lượng | [[src-choudhry-principles-banking#^choudhry-salm-9]] |
| ALCO | Ngang hàng ExCo, giám sát Credit Committee, thiết kế và theo dõi EWI ([[key-risk-indicators]]) | [[src-choudhry-principles-banking#^choudhry-salm-12]] |
| Chiến lược nợ | Chiến lược nợ phải trả rõ ràng, tối ưu cơ cấu funding và gắn với origination tài sản | [[src-choudhry-principles-banking#^choudhry-salm-8]] |
| Quy trình ngân sách | ALCO điều hành lập ngân sách; lập kế hoạch tích hợp, lặp tới khi KRI/KPI tối ưu; ALCO và Board phê duyệt | [[src-choudhry-principles-banking#^choudhry-salm-1]] |
| Bộ ba Treasurer, CFO, CRO | Thông qua ALCO, có ảnh hưởng lớn hơn tới origination và định giá khách hàng | [[src-choudhry-principles-banking#^choudhry-salm-3]] |

Xem [[risk-appetite]], [[alco]].

**Funding nhìn cả hai phía.** Chính sách thanh khoản và funding không nên chỉ quan tâm phía nợ. Độ vững của funding phụ thuộc thanh khoản, kỳ hạn, loại tài sản cũng như cơ cấu nợ [[src-choudhry-principles-banking#^choudhry-salm-13]]. Một số hành động chiến lược [[src-choudhry-principles-banking#^choudhry-salm-14]]:
- phía nợ: phân bổ chi phí thanh khoản phù hợp cho các khối kinh doanh qua [[funds-transfer-pricing]];
- phía tài sản: tăng tài sản thanh khoản trong bảng cân đối, cân bằng với ROE;
- hạn chế [[asset-encumbrance]], dù điều này ngược với áp lực huy động có bảo đảm.

## Phụ thuộc regime
Sau khủng hoảng 2007–2008, tối ưu bảng cân đối khó hơn vì vốn và thanh khoản nhiều và đắt hơn, quy định can thiệp sâu hơn, và yêu cầu đối xử công bằng với khách hàng cao hơn [[src-choudhry-principles-banking#^choudhry-alco-10]]. Theo Choudhry, đây là lý do chính để chuyển sang strategic ALM [[src-choudhry-principles-banking#^choudhry-salm-5]].

## Góc nhìn theo domain
- **ALM**: truyền thống, ALM nghĩa là quản lý rủi ro thanh khoản và rủi ro lãi suất. Strategic ALM quản lý toàn bộ tài sản và nợ từ một góc nhìn tích hợp [[src-choudhry-principles-banking#^choudhry-salm-2]]. Choudhry cho rằng ALM nên quản lý cả vốn quy định và chủ động định vị bảng cân đối để tối đa hoá lợi nhuận [[src-choudhry-principles-banking#^choudhry-desk-2]].
- **Mô hình định lượng**: tối ưu hoá bảng cân đối tích hợp thanh khoản và IRRBB, thay vì quản lý silo, là một cách triển khai strategic ALM [[src-choudhry-principles-banking#^choudhry-opt-6]]. Xem [[balance-sheet-optimisation-model]].
- **IRRBB**: case study 5 cho thấy cách phòng ngừa theo phần ròng xuất phát từ việc ALCO tiếp nhận quan điểm "Strategic ALM" [[src-choudhry-principles-banking#^choudhry-cs-17]]. Xem [[structural-hedging]].
- **Strategic plan**: sau khủng hoảng 2008, giới hạn nguồn lực (vốn, funding) dẫn dắt chiến lược thay cho mục tiêu RoE [[src-choudhry-principles-banking#^choudhry-strat-21]]; bảng cân đối và độ vững của nó là trung tâm của strategic plan [[src-choudhry-principles-banking#^choudhry-strat-33]]. Xem [[bank-strategic-plan]].
- **Basel/VN**: phần d368 và TT83/2025 đã ingest không dùng thuật ngữ "strategic ALM" [cần nguồn].

*Diễn giải:* TT83/2025 giao bộ phận ALM quản lý bảng cân đối và đề xuất kế hoạch huy động, sử dụng vốn ([[alco]]). Khung này gần với strategic ALM ở phần kế hoạch, nhưng đặt ALCO dưới Tổng giám đốc thay vì ngang ExCo như Choudhry đề xuất.

## Bằng chứng thực nghiệm
- Ví dụ ChoudWest Bank (giả định) cho thấy cấu trúc funding tối ưu tiết kiệm 0,6 tỷ USD mỗi năm [[src-choudhry-principles-banking#^choudhry-opt-5]].

## Câu hỏi mở
- Nguồn là một tác giả T4; khái niệm "strategic ALM" và "3D optimisation" là thuật ngữ riêng của Choudhry, chưa có nguồn thứ hai đối chiếu.
