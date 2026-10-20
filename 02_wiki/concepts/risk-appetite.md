---
title: "Risk Appetite"
aliases: [Risk Appetite, Khẩu vị rủi ro, Risk Appetite Statement]
type: concept
domains: [alm, vn-reg, basel]
status: active
maturity: draft
valid_from: 2026-07-01
valid_to:
as_of:
sources: ["[[src-tt83-2025-nhnn]]", "[[src-bcbs-framework]]", "[[src-bcbs-liquidity-principles-2008]]", "[[src-bcbs-irrbb-2016]]", "[[src-choudhry-principles-banking]]", "[[src-bardaeva-alm]]"]
relations:
  - {type: input-to, to: "[[risk-limits]]", cite: "[[src-tt83-2025-nhnn#^d20-2]]"}
  - {type: limits, to: "[[bank-strategic-plan]]", cite: "[[src-choudhry-principles-banking#^choudhry-strat-11]]"}
tags: [governance, risk-appetite, internal-control]
updated: 2026-10-20
reviewed:
---

## Ý chính
Khẩu vị rủi ro là mức độ rủi ro ngân hàng sẵn sàng chấp nhận khi thực hiện chiến lược kinh doanh, thể hiện bằng các tỷ lệ và chỉ tiêu tại Đ19.2.a [[src-tt83-2025-nhnn#^d3-10]]. Theo [[tt83-2025]], chính sách quản lý rủi ro tối thiểu gồm khẩu vị rủi ro, danh sách rủi ro trọng yếu và chiến lược quản lý từng rủi ro trọng yếu [[src-tt83-2025-nhnn#^d19-2]]. Hạn mức rủi ro phải phù hợp với khẩu vị rủi ro [[src-tt83-2025-nhnn#^d20-2]]; xem [[risk-limits]].

## Cơ chế & drivers
**Cấu phần khẩu vị rủi ro theo TT83/2025** [[src-tt83-2025-nhnn#^d19-2]]:

| Cấu phần | Nội dung | Nguồn |
|---|---|---|
| Vốn | Tỷ lệ an toàn vốn mục tiêu; là $CAR_{Target}$ trong công thức [[economic-capital]] [[src-tt83-2025-nhnn#^pl6-1a]] | [[src-tt83-2025-nhnn#^d19-2]] |
| Thu nhập | ROE; [[raroc]] (lợi nhuận trước thuế / vốn kinh tế [[src-tt83-2025-nhnn#^pl6-iii]]) | [[src-tt83-2025-nhnn#^d19-2]] |
| Định tính | Chỉ tiêu và mức độ chấp nhận rủi ro khác theo quy định nội bộ | [[src-tt83-2025-nhnn#^d19-2]] |

**Rủi ro trọng yếu.** Danh sách rủi ro trọng yếu tối thiểu gồm tín dụng, thị trường, hoạt động, thanh khoản, tập trung, IRRBB [[src-tt83-2025-nhnn#^d3-13]].

**Báo cáo NHNN.** Báo cáo ICAAP hằng năm trình bày khẩu vị rủi ro với chỉ tiêu $CAR_{target}$, ROE, RAROC cho năm $t_0$ đến $t_0+3$ [[src-tt83-2025-nhnn#^pl3-2]]. Xem [[icaap]].

**Ban hành và chu kỳ.**
- Chính sách quản lý rủi ro của ngân hàng thương mại do HĐQT hoặc HĐTV ban hành [[src-tt83-2025-nhnn#^d19-1]].
- Chính sách lập cho 3–5 năm, đánh giá ít nhất mỗi năm một lần và đột xuất khi môi trường kinh doanh hay pháp lý thay đổi [[src-tt83-2025-nhnn#^d19-3]].
- Chính sách phải phù hợp với mức vốn tự có và nguồn tăng vốn tự có, có tính kế thừa qua các chu kỳ kinh tế [[src-tt83-2025-nhnn#^d19-3]].

**Liên kết với ICAAP.** ICAAP phải duy trì tỷ lệ an toàn vốn mục tiêu ở kịch bản bình thường và bất lợi, và phù hợp khẩu vị rủi ro [[src-tt83-2025-nhnn#^d59-1]]. Rà soát ICAAP đánh giá sự phù hợp giữa khẩu vị rủi ro và kế hoạch kinh doanh [[src-tt83-2025-nhnn#^d62-1]]. Xem [[icaap]].

**Với IRRBB (Basel).**
- d368 yêu cầu khẩu vị rủi ro IRRBB được thể hiện theo cả giá trị kinh tế và thu nhập, và hạn mức chính sách phải giữ IRRBB nhất quán với khẩu vị đó [[src-bcbs-irrbb-2016#^irrbb-p03-1]].
- Risk appetite statement nên được governing body phê duyệt và thực thi qua risk appetite framework; chính sách IRRBB rà soát ít nhất hằng năm [[src-bcbs-irrbb-2016#^irrbb-p03-2]].

**RAS theo Choudhry (T4).**
- RAS là tuyên bố rõ ràng về khẩu vị và mức chịu đựng rủi ro bảng cân đối của Board, gồm chỉ số và hạn mức định tính, định lượng. Choudhry gọi đây là văn bản quan trọng nhất cần Board phê duyệt [[src-choudhry-principles-banking#^choudhry-salm-9]].
- Với mỗi chỉ số, ngân hàng đặt "macro-tolerance" toàn ngân hàng rồi chia cho từng khối kinh doanh. Ngân hàng giao dịch đa tiền tệ thêm hạn mức FX; ngân hàng dùng nhiều funding có bảo đảm thêm hạn mức [[asset-encumbrance]] [[src-choudhry-principles-banking#^choudhry-salm-10]].
- RAS cần rà soát và phê duyệt định kỳ, thường hằng năm hoặc khi đổi mô hình kinh doanh, và cập nhật khi dự báo hoặc xảy ra stress thị trường [[src-choudhry-principles-banking#^choudhry-salm-11]].
- Board RAS xác định KRI và KPI mà ngân hàng muốn tối ưu, là bước đầu của quy trình [[strategic-alm]] [[src-choudhry-principles-banking#^choudhry-salm-1]].

**RAS trong quản trị IRRBB (Bardaeva, T4).**
- Ngân hàng nên nêu trong khung khẩu vị rủi ro các ngưỡng kích hoạt phục hồi (recovery triggers) [[src-bardaeva-alm#^ch14-2]]. Xem [[recovery-and-resolution-planning]].
- Sau khi đo tác động, ngân hàng quyết định quản lý những tác động không phù hợp RAS [[src-bardaeva-alm#^ch11-18]]. Xem [[irrbb-management]].
- Amber zone của khẩu vị rủi ro được đặt ở các hội đồng cấp dưới; với rủi ro ALM là [[alco]] [[src-bardaeva-alm#^ch11-20]].

**Risk taxonomy và risk register (Choudhry, T4).**
- RAS được phản ánh trong các văn bản chính sách; RAS gồm KRI, các chỉ số rủi ro bổ sung và EWI [[src-choudhry-principles-banking#^choudhry-rmf-1]]. Xem [[key-risk-indicators]].
- ALCO phê duyệt danh sách loại rủi ro trọng yếu; danh sách được rà soát hằng năm qua MIRA, kết quả là Risk Taxonomy ba cấp, đầu vào của ICAAP và ILAAP [[src-choudhry-principles-banking#^choudhry-rmf-2]] [[src-choudhry-principles-banking#^choudhry-rmf-3]].
- Risk register mẫu: khẩu vị rủi ro lãi suất là hạn mức chênh lệch tái định giá; khẩu vị thanh khoản là chịu được stress riêng của ngân hàng trong 90 ngày [[src-choudhry-principles-banking#^choudhry-rmf-5]].
- RAS mẫu đặt mục tiêu tài chính theo tổng thu nhập, NII, lợi nhuận ròng, RARoC và RoRWA [[src-choudhry-principles-banking#^choudhry-rmf-14]]. Mọi ngưỡng khẩu vị rủi ro được đặt cao hơn hạn mức quy định [[src-choudhry-principles-banking#^choudhry-kri-1]].
- Dưới ICAAP, khẩu vị rủi ro nên được định lượng cả theo biến động vốn và lợi nhuận, không chỉ theo hạn mức [[src-choudhry-principles-banking#^choudhry-icaap-3]].
- Survival period tối thiểu là một thành phần của Liquidity Risk Appetite Statement [[src-choudhry-principles-banking#^choudhry-ilaap-5]]; ILAAP nên nêu khẩu vị rủi ro theo thời gian và loại stress cần vượt qua [[src-choudhry-principles-banking#^choudhry-ilaap-11]]. Xem [[cash-flow-survival-period]].
- "Mild RST" hạ ngưỡng lỗ để thử mức chấp nhận rủi ro của Board với một danh mục [[src-choudhry-principles-banking#^choudhry-rst-11]]. Xem [[reverse-stress-testing]].

**Risk appetite và strategic plan (Choudhry, T4).**
- Kỳ vọng của cổ đông, khách hàng, cơ quan quản lý là đầu vào để xây risk appetite; risk appetite là lớp phủ lên strategic plan [[src-choudhry-principles-banking#^choudhry-strat-8]].
- Risk appetite chịu tác động của: khẩu vị của Board và cổ đông với biến động kết quả và mức sinh lời; vốn hấp thụ lỗ và yêu cầu quy định; cấu trúc funding và hồ sơ thanh khoản; vị thế danh tiếng và thị trường; độ vững vận hành và năng lực quản lý [[src-choudhry-principles-banking#^choudhry-strat-11]].
- Strategic plan phải được đánh giá theo khung risk appetite Board đã duyệt [[src-choudhry-principles-banking#^choudhry-strat-11]]. Mục tiêu return on capital nên tương xứng mức ngại rủi ro trong RAS [[src-choudhry-principles-banking#^choudhry-strat-14]]. Xem [[bank-strategic-plan]].

## Phụ thuộc regime
- Bardaeva nêu Finance có KPI ngân sách nên khi kết quả kém kế hoạch có động cơ tăng khẩu vị rủi ro để kiếm thêm từ gap kỳ hạn/tiền tệ [[src-bardaeva-alm#^ch11-12]]; xung đột lợi ích trong ALM tăng trong suy thoái và khủng hoảng [[src-bardaeva-alm#^ch11-23]].

## Góc nhìn theo domain
- **VN**: TT83/2025 chỉ định đích danh chỉ tiêu khẩu vị rủi ro (CAR mục tiêu, ROE, RAROC) [[src-tt83-2025-nhnn#^d19-2]], có hiệu lực từ 01/07/2026 [[src-tt83-2025-nhnn#^d74-1]].
- **Basel**: d368 không nêu chỉ tiêu cụ thể, chỉ yêu cầu khẩu vị theo cả economic value và earnings [[src-bcbs-irrbb-2016#^irrbb-p03-1]].
- **Basel (SRP30, Pillar 2)**:
  - Cơ quan giám sát nên xác định ngân hàng có khung quản trị rủi ro toàn hàng cho phép định nghĩa khẩu vị rủi ro và nhận diện mọi rủi ro trọng yếu [[src-bcbs-framework#^srp30-5]]. Xem [[firm-wide-risk-management]].
  - HĐQT và ban điều hành chịu trách nhiệm xác định khẩu vị rủi ro và bảo đảm có hạn mức thận trọng toàn hàng nhất quán với khẩu vị và năng lực chấp nhận rủi ro [[src-bcbs-framework#^srp30-8]].
  - Chức năng quản lý rủi ro nên báo cáo HĐQT và ban điều hành về vi phạm hạn mức khẩu vị rủi ro [[src-bcbs-framework#^srp30-11]].
  - Với thanh khoản, HĐQT đặt liquidity risk tolerance [[src-bcbs-framework#^srp30-50]].
- **Basel (BCBS 144 Principle 2, liquidity risk tolerance)**:
  - Ngân hàng nên đặt liquidity risk tolerance theo mục tiêu kinh doanh, định hướng chiến lược và khẩu vị rủi ro tổng thể. HĐQT chịu trách nhiệm cuối cùng nên đặt tolerance [[src-bcbs-liquidity-principles-2008#^lrm-10]].
  - Tolerance xác định mức rủi ro thanh khoản ngân hàng sẵn sàng chấp nhận, phản ánh tình hình tài chính và năng lực funding, và nên giúp ngân hàng chịu được stress kéo dài [[src-bcbs-liquidity-principles-2008#^lrm-10]].
  - Tolerance có thể diễn đạt định tính hoặc định lượng, ví dụ bằng mức rủi ro thanh khoản funding chưa giảm thiểu trong điều kiện thường và stress. Cơ quan giám sát đánh giá tính phù hợp của tolerance [[src-bcbs-liquidity-principles-2008#^lrm-10b]]. Xem [[bcbs-liquidity-principles]].
  - Stress test thanh khoản bảo đảm phơi nhiễm nằm trong tolerance [[src-bcbs-liquidity-principles-2008#^lrm-p10]]. Xem [[liquidity-stress-testing]].
  - *Diễn giải:* TT83/2025 giao HĐQT, HĐTV ban hành chính sách quản lý rủi ro có khẩu vị rủi ro [[src-tt83-2025-nhnn#^d19-1]] [[src-tt83-2025-nhnn#^d19-2]], khớp với SRP30.8 về chủ thể. SRP30 không nêu chỉ tiêu cụ thể như CAR mục tiêu, ROE, RAROC của TT83.
- **ALM**: *Diễn giải:* với IRRBB, khẩu vị theo "economic value" của Basel tương ứng ΔEVE, theo "earnings" tương ứng ΔNII. TT83 đặt hạn mức cho cả hai chỉ tiêu [[src-tt83-2025-nhnn#^d53-2]], nhưng Đ19 không yêu cầu đưa ΔEVE hay ΔNII vào khẩu vị rủi ro.

## Bằng chứng thực nghiệm
Không ghi nhận trong nguồn đã ingest.

## Câu hỏi mở
