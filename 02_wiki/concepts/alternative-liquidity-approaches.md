---
title: Alternative liquidity approaches
aliases: [Alternative liquidity approaches, ALA, Phương pháp thanh khoản thay thế]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]"]
relations:
  - {type: part-of, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr31-1]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr31-1]]"}
tags: [liquidity, hqla, ala, clf, foreign-currency, level-2a]
updated: 2026-10-15
reviewed:
---

## Ý chính
Phương pháp thanh khoản thay thế (Alternative Liquidity Approaches - ALA) là cơ chế đặc thù của Basel III (chương LCR31) dành riêng cho các khu vực pháp lý có sự thiếu hụt mang tính cơ cấu (structural shortfall) về nguồn cung [[level-1-assets]] (hoặc cả Level 1 và [[level-2-assets]]) bằng đồng nội tệ so với tổng nhu cầu thanh khoản của hệ thống ngân hàng [[src-bcbs-lcr#^lcr31-1]]. Basel đưa ra 3 lựa chọn thay thế (Options) nhằm đảm bảo ngân hàng vẫn có đủ tài sản dự phòng thanh khoản mà không bóp méo thị trường nợ chính phủ nội địa [[src-bcbs-lcr#^lcr31-3]].

## Cơ chế & drivers

### Ba lựa chọn thanh khoản thay thế (Three Options)
1. **Option 1 — Hạn mức thanh khoản cam kết từ NHTW có thu phí (Committed Liquidity Facility - CLF)**:
   - Ngân hàng ký thỏa thuận hợp đồng hạn mức thanh khoản cam kết riêng biệt với NHTW (hoàn toàn tách biệt với các cơ chế cho vay thường trực qua đêm hoặc tái cấp vốn thông thường) [[src-bcbs-lcr#^lcr31-12]].
   - **Điều kiện hợp đồng**: Kỳ hạn thỏa thuận tối thiểu phải nằm ngoài cửa sổ 30 ngày của LCR; không thể hủy ngang trước hạn; và tuyệt đối không đòi hỏi quyết định thẩm định tín dụng bổ sung từ NHTW khi giải ngân (no ex post credit decision) [[src-bcbs-lcr#^lcr31-12]].
   - **Cơ chế phí triệt tiêu chênh lệch lợi suất (Yield-neutral fee)**: Ngân hàng phải trả phí cam kết liên tục trên toàn bộ hạn mức (bất kể có rút vốn hay không) [[src-bcbs-lcr#^lcr31-12]]. Mức phí được tính toán sao cho lợi suất ròng của tài sản thế chấp (sau khi trừ phí) không cao hơn lợi suất danh mục Level 1/Level 2 chuẩn, nhằm loại bỏ động cơ tìm kiếm lợi nhuận (yield arbitrage) [[src-bcbs-lcr#^lcr31-12]].
2. **Option 2 — Sử dụng HQLA ngoại tệ bù đắp thanh khoản nội tệ (Foreign currency HQLA for domestic needs)**:
   - Cho phép các ngân hàng thiếu hụt HQLA nội tệ được nắm giữ HQLA bằng ngoại tệ tự do chuyển đổi để bù đắp dòng tiền ra ròng bằng đồng nội tệ [[src-bcbs-lcr#^lcr31-13]]. Vị thế bất cân xứng kỳ hạn đồng tiền (currency mismatch) phát sinh phải được kiểm soát chặt chẽ trong hạn mức của supervisor [[src-bcbs-lcr#^lcr31-13]].
   - **Haircut rủi ro tỷ giá (FX Haircut)**: Áp dụng mức haircut tối thiểu 8% đối với các ngoại tệ chủ chốt (thị phần giao dịch toàn cầu ≥ 10%) [[src-bcbs-lcr#^lcr31-14]]. Đối với các ngoại tệ khác, áp dụng haircut cao hơn căn cứ theo biến động tỷ giá lịch sử (chuỗi 10 năm) [[src-bcbs-lcr#^lcr31-14]]. Nếu đồng nội tệ được neo tỷ giá chính thức hiệu quả (peg mechanism), mức haircut có thể được hạ thấp tương ứng [[src-bcbs-lcr#^lcr31-14]].
   - **Ngưỡng miễn trừ (Supervisory threshold)**: Haircut chỉ bắt buộc áp dụng đối với phần HQLA ngoại tệ vượt ngưỡng do cơ quan giám sát quy định (ngưỡng tối đa 25% tổng net cash outflows nội tệ) [[src-bcbs-lcr#^lcr31-14]].
3. **Option 3 — Sử dụng bổ sung tài sản Level 2A với haircut cao hơn (Additional Level 2A assets)**:
   - Áp dụng khi quốc gia thiếu hụt Level 1 nhưng có nguồn cung dồi dào về tài sản Level 2A chất lượng cao [[src-bcbs-lcr#^lcr31-17]].
   - **Haircut phạt bổ sung (Penalty haircut)**: Toàn bộ lượng Level 2A bổ sung vượt mức trần 40% phải chịu haircut tối thiểu 20% (cao hơn 5% so với mức chuẩn 15% của Level 2A trong trần) [[src-bcbs-lcr#^lcr31-17]].
   - **Tuyệt đối tuân thủ trần Level 2B**: Tài sản Level 2B vẫn chịu sự khống chế nghiêm ngặt ở mức tối đa 15% tổng danh mục HQLA, không được nới lỏng trong mọi trường hợp [[src-bcbs-lcr#^lcr31-17]].

### Giới hạn tổng thể & Nguyên tắc quản trị (Limits & Governance)
- **Hạn mức trần sử dụng ALA**: Supervisor phải đặt ra một tỷ lệ trần tối đa cho tổng tài sản HQLA hình thành từ các lựa chọn ALA (ví dụ tối đa 80% tổng HQLA yêu cầu), buộc mọi ngân hàng phải duy trì tỷ lệ tối thiểu còn lại (ví dụ ít nhất 20%) bằng tài sản Level 1 nội tệ thực tế [[src-bcbs-lcr#^lcr31-4]].
- **Ưu tiên giảm rủi ro thanh khoản**: Ngân hàng phải chứng minh đã nỗ lực tối đa trong việc gom tài sản Level 1, Level 2 và chủ động thu hẹp rủi ro thanh khoản (giảm dòng tiền ra ròng) trước khi xin phê duyệt áp dụng ALA [[src-bcbs-lcr#^lcr31-10]].
- **Ba nguyên tắc đánh giá điều kiện đủ (Qualifying Principles)** [[src-bcbs-lcr#^lcr31-20]]:
  * *Principle 1 (Thiếu hụt mang tính cơ cấu)*: Phải chứng minh sự thiếu hụt Level 1 nội tệ xuất phát từ các yếu tố cơ cấu kéo dài trong trung hạn (3–5 năm) như chính sách tài khóa thặng dư triền miên, quy mô nợ chính phủ quá thấp hoặc đặc thù cơ chế tỷ giá [[src-bcbs-lcr#^lcr31-20]].
  * *Principle 2 (Năng lực kiểm soát rủi ro)*: Quốc gia phải có tiềm lực tài chính để bảo trợ các cam kết CLF của NHTW, hệ thống giám sát rủi ro tỷ giá cho Option 2 và tiêu chuẩn khắt khe cho Option 3 [[src-bcbs-lcr#^lcr31-20]].
  * *Principle 3 (Nghĩa vụ giám sát & Rà soát 5 năm)*: Quốc gia phải công khai khung chính sách, thực hiện rà soát tự đánh giá định kỳ tối đa 5 năm một lần và chấp nhận quy trình bình duyệt độc lập (peer review) từ Basel [[src-bcbs-lcr#^lcr31-20]] [[src-bcbs-lcr#^lcr31-58]].

## Tác động ALM
*Diễn giải:*
- **Giải quyết bài toán "Crowding Out" trái phiếu chính phủ**: Tại các quốc gia có tỷ lệ nợ công thấp (như Australia, Na Uy), nếu bắt buộc mọi ngân hàng phải gom TPCP để đạt 100% LCR, hệ thống ngân hàng sẽ thâu tóm toàn bộ lượng trái phiếu đang lưu hành, làm tê liệt tính thanh khoản của thị trường nợ thứ cấp. Cơ chế CLF (Option 1) của NHTW Úc (Reserve Bank of Australia - RBA) là ví dụ thực tiễn điển hình giúp hệ thống ngân hàng tuân thủ LCR mà không làm méo mó thị trường nợ chính phủ.
- **Tối ưu hóa bảng cân đối & chi phí vốn**: Haircut phạt (20% cho Level 2A) hoặc phí cam kết của CLF trực tiếp làm giảm hiệu quả sinh lời của danh mục thanh khoản. ALM Desk phải so sánh chi phí cơ hội giữa việc trả phí CLF, nắm giữ Level 2A chịu haircut lớn, hay sử dụng ngoại tệ (Option 2) kèm chi phí phòng ngừa rủi ro tỷ giá (cross-currency / FX swap).

## Phụ thuộc regime
- **Regime bình thường**: Các ngân hàng áp dụng Option 2 có thể hoán đổi ngoại tệ ra nội tệ dễ dàng trên thị trường FX swap với chi phí basis thấp.
- **Regime stress**: Khả năng tiếp cận thị trường FX swap có thể bị suy giảm nghiêm trọng hoặc chi phí hoán đổi ngoại tệ tăng vọt, trong khi tỷ giá biến động bất lợi làm sụt giảm giá trị thanh khoản quy đổi của danh mục HQLA ngoại tệ. Mức sàn haircut 8% và trần tỷ lệ sử dụng được thiết kế nhằm hạn chế tối đa nguy cơ tổn thất này [[src-bcbs-lcr#^lcr31-14]].

## Góc nhìn theo domain
- **Basel**: Chuẩn hóa cơ chế van an toàn (escape valve) tại LCR31, tránh việc các quốc gia tự ý hạ thấp tiêu chuẩn HQLA khi thiếu hụt tài sản công [[src-bcbs-lcr#^lcr31-1]] [[src-bcbs-lcr#^lcr31-20]].
- **VN**: Thị trường trái phiếu chính phủ và trái phiếu doanh nghiệp tại Việt Nam có quy mô và tính thanh khoản chưa cao so với tổng tài sản của hệ thống ngân hàng. Khi xây dựng lộ trình áp dụng LCR đầy đủ theo Basel III tại Việt Nam, các nguyên tắc của ALA (đặc biệt là cơ chế tái cấp vốn cam kết từ NHNN tương tự Option 1 hoặc cho phép sử dụng trái phiếu ngoại tệ theo Option 2) là những bài học thể chế có giá trị tham chiếu rất lớn.

## Câu hỏi mở
- Khi triển khai LCR tại Việt Nam, NHNN có thể xem xét áp dụng cơ chế tương tự Option 1 (CLF có thu phí dựa trên tài sản thế chấp là nợ tiêu chuẩn/trái phiếu doanh nghiệp) để giải tỏa áp lực thiếu hụt TPCP cho các NHTM hay không?
