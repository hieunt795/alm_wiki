---
title: "Concentration Risk Management"
aliases: [Concentration Risk Management, Quản lý rủi ro tập trung, Concentration risk, Rủi ro tập trung]
type: concept
domains: [vn-reg, alm]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]"]
relations: []
tags: [concentration-risk, limits, governance]
updated: 2026-10-19
reviewed:
---

## Ý chính
Theo [[tt83-2025]], rủi ro tập trung là rủi ro phát sinh khi ngân hàng tập trung hoạt động kinh doanh vào một khách hàng, một khách hàng và người có liên quan, hoặc một số khách hàng, đối tác, sản phẩm, giao dịch, ngành kinh tế, ở mức có tác động đáng kể tới thu nhập và trạng thái rủi ro [[src-tt83-2025-nhnn#^d3-21]]. Đây là một rủi ro trọng yếu [[src-tt83-2025-nhnn#^d3-13]].

Chiến lược quản lý rủi ro tập trung áp dụng tối thiểu cho hai hoạt động: cấp tín dụng và giao dịch tự doanh [[src-tt83-2025-nhnn#^d50-1]].

## Cơ chế & drivers
**Chiến lược** tối thiểu gồm [[src-tt83-2025-nhnn#^d50-2]]:
- cấp tín dụng:
  - nguyên tắc đặt hạn mức tập trung theo sản phẩm, khách hàng, ngành kinh tế;
  - tiêu chí xác định người có liên quan;
  - nguyên tắc xác định mức độ đa dạng và mức độ tương tác giữa sản phẩm, ngành;
- giao dịch tự doanh:
  - nguyên tắc đặt hạn mức theo đối tác, sản phẩm;
  - tiêu chí xác định danh mục áp hạn mức.

**Hạn mức tối thiểu** (Đ50.3). Xem [[risk-limits]].

| Hoạt động | Hạn mức | Mẫu số | Nguồn |
|---|---|---|---|
| Cấp tín dụng | Một khách hàng; một khách hàng và người có liên quan | Vốn tự có và tổng dư nợ | [[src-tt83-2025-nhnn#^d50-3]] |
| Cấp tín dụng | Theo sản phẩm, ngành kinh tế | Tổng dư nợ | [[src-tt83-2025-nhnn#^d50-3]] |
| Giao dịch tự doanh | Theo đối tác, sản phẩm | Tổng số dư giao dịch tự doanh | [[src-tt83-2025-nhnn#^d50-3]] |

**Nhận dạng và đo lường.**
- Nhận dạng gồm khoản mục nội bảng, ngoại bảng và cả khoản mục chưa được hạch toán theo pháp luật kế toán [[src-tt83-2025-nhnn#^d51-1]].
- Đo lường dựa trên mức độ tác động tới thu nhập của từng hoạt động có rủi ro tập trung [[src-tt83-2025-nhnn#^d51-2]].
- Theo dõi dư nợ và số dư tự doanh so với hạn mức; cảnh báo sớm khi gần vượt; xử lý kịp thời khi vượt [[src-tt83-2025-nhnn#^d51-2]].

**Báo cáo nội bộ.** Tối thiểu 06 tháng hoặc đột xuất. Nội dung gồm cơ cấu tín dụng theo sản phẩm, loại khách hàng, ngành; cơ cấu danh mục tự doanh theo đối tác, sản phẩm; tình hình thực hiện hạn mức và lý do vượt [[src-tt83-2025-nhnn#^d52-1]].

**Vốn.** Tài sản tính theo rủi ro tập trung ($RWA_{COR}$) là một cấu phần của $RWA^*_E$ khi tính [[economic-capital]] [[src-tt83-2025-nhnn#^pl6-1b]]. Trong stress test vốn, giả định chất lượng tín dụng tác động lên tài sản tính theo rủi ro tập trung [[src-tt83-2025-nhnn#^d60-1]].

Tài sản tính theo rủi ro tập trung của hoạt động cấp tín dụng do ngân hàng tự xây dựng phương pháp, nhưng không thấp hơn mức sàn [[src-tt83-2025-nhnn#^pl6-1d]]:

$$
RWA^{1*}_{COR} = \max(E_i - A \times C;\ 0) + \max(E_j - B \times C;\ 0)
$$
[[src-tt83-2025-nhnn#^pl6-1d]]

trong đó $E_i$ là dư nợ cấp tín dụng với một khách hàng, $E_j$ là dư nợ với một khách hàng và người có liên quan (không gồm khoản có hệ số rủi ro 0% và khoản đã trừ khỏi vốn tự có), $C$ là vốn tự có [[src-tt83-2025-nhnn#^pl6-1d]]. Phần tự doanh ($RWA^2_{COR}$) theo phương pháp ngân hàng tự xây dựng [[src-tt83-2025-nhnn#^pl6-1d]].

| Từ | A (một khách hàng, % vốn tự có) | B (khách hàng và người có liên quan, % vốn tự có) | Nguồn |
|---|---|---|---|
| 01/07/2026 | 8,7 | 16,8 | [[src-tt83-2025-nhnn#^pl6-1d]] |
| 01/01/2027 | 8 | 15,2 | [[src-tt83-2025-nhnn#^pl6-1d]] |
| 01/01/2028 | 7,3 | 13,6 | [[src-tt83-2025-nhnn#^pl6-1d]] |
| 01/01/2029 | 6,5 | 12 | [[src-tt83-2025-nhnn#^pl6-1d]] |

*Diễn giải:* phần dư nợ vượt A% (hoặc B%) vốn tự có bị tính toàn bộ vào $RWA_{COR}$, nên ngưỡng giảm dần theo lộ trình làm tăng vốn kinh tế của danh mục tập trung, kể cả khi chưa chạm giới hạn cấp tín dụng pháp định.

## Phụ thuộc regime
Không ghi nhận trong nguồn đã ingest.

## Góc nhìn theo domain
- **VN**: TT83/2025 Đ50–52, hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]].
- **Basel**: phần đã ingest chỉ có chuẩn giám sát tập trung **nguồn vốn** (SRP50), xem [[funding-concentration-risk]]. Wiki chưa có chuẩn Basel về large exposures [cần nguồn].
- **Khác biệt phạm vi**: Đ50.1 áp chiến lược tập trung cho cấp tín dụng và tự doanh [[src-tt83-2025-nhnn#^d50-1]], không nêu nguồn vốn. Ở TT83, tập trung nguồn vốn chỉ xuất hiện như một yếu tố rủi ro phải phân tích trong kịch bản kiểm tra sức chịu đựng thanh khoản [[src-tt83-2025-nhnn#^d48-3]]. Xem [[liquidity-stress-testing]].
- **ALM**: *Diễn giải:*
  - Ngân hàng tại VN không có nghĩa vụ đặt hạn mức tập trung nguồn vốn theo Đ50. Nếu ALCO muốn kiểm soát tập trung người gửi tiền, căn cứ gần nhất là hạn mức nội bộ cho rủi ro thanh khoản theo Đ45.3 [[src-tt83-2025-nhnn#^d45-3]], với chỉ số SRP50 làm tham chiếu.
  - Hạn mức tập trung tín dụng có mẫu số là vốn tự có [[src-tt83-2025-nhnn#^d50-3]], nên khi vốn tự có giảm (ví dụ do lỗ), mức sử dụng hạn mức tăng dù dư nợ không đổi.

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
- Giới hạn cấp tín dụng pháp định cho một khách hàng và người có liên quan nằm ở Luật Các TCTD [cần nguồn].
- TT83 không nêu phương pháp đo "mức độ tương tác" giữa sản phẩm, ngành (Đ50.2.a.iii); để quy định nội bộ.
