---
title: "Kế Hoạch Tài Trợ Dự Phòng (Contingency Funding Plan — CFP)"
aliases: [Contingency Funding Plan, CFP, Kế hoạch tài trợ dự phòng, Quản trị khủng hoảng thanh khoản, Liquidity Contingency Plan, LCP]
type: concept
domains: [alm]
status: active
maturity: canonical
sources: ["[[src-choudhry-principles-banking]]", "[[src-bcbs-framework]]"]
relations:
  - {type: drives, to: "[[hqla]]", cite: "[[src-choudhry-principles-banking#^choudhry-cfp-8]]"}
tags: [liquidity, cfp, crisis-management, alco, ewi, lab, stress-testing, concept]
updated: 2026-10-17
reviewed:
---

## 1. Định vị Chiến Lược và Bản Chất Cốt Tử

Kế hoạch Tài trợ Dự phòng (Contingency Funding Plan — CFP, tại một số khu vực pháp lý như Vương quốc Anh còn gọi là Liquidity Contingency Plan — LCP) là **cấu phần tối quan trọng nhất** trong toàn bộ hệ thống quản trị rủi ro thanh khoản của ngân hàng [[src-choudhry-principles-banking#^choudhry-cfp-1]].

Giáo sư Moorad Choudhry chỉ rõ: các cuộc khủng hoảng thanh khoản cực đoan hiếm khi xuất hiện trong đời sống thường nhật của một ngân hàng, nhưng khi xảy ra, chúng diễn biến với tốc độ hủy diệt chỉ trong vài ngày hoặc vài giờ [[src-choudhry-principles-banking#^choudhry-cfp-1]]. Hầu hết nhân viên và cấp quản lý đều không có kinh nghiệm thực chiến để đối phó với một cuộc tháo chạy tiền gửi quy mô lớn hoặc tình trạng thị trường liên ngân hàng đóng băng. CFP đóng vai trò là "Cẩm nang Tác chiến Khủng hoảng" (Crisis Playbook) quy định chi tiết ngân hàng phải hành động chính xác như thế nào, ai là người ra quyết định, và các nguồn vốn khẩn cấp nào sẽ được khai thông [[src-choudhry-principles-banking#^choudhry-cfp-2]].

---

## 2. Các Trụ Cột Cấu Thành Một CFP Thực Chiến

Một bản CFP khả thi và chuẩn mực theo Choudhry và BCBS phải bao gồm đầy đủ 6 cấu phần bắt buộc [[src-choudhry-principles-banking#^choudhry-cfp-2]] [[src-choudhry-principles-banking#^choudhry-cfp-3]]:

```
+---------------------------------------------------------------------------------------------------+
|                        KIẾN TRÚC KẾ HOẠCH TÀI TRỢ DỰ PHÒNG (CFP)                                  |
+---------------------------------+---------------------------------+-------------------------------+
|  1. CHỈ BÁO CẢNH BÁO SỚM (EWIs) |  2. KHUNG QUẢN TRỊ KHỦNG HOẢNG  |  3. DANH MỤC HÀNH ĐỘNG VỐN     |
|  - Rút tiền gửi bất thường      |  - Crisis Management Team (CMT) |  - Menu of Funding Measures   |
|  - CDS spread nới rộng          |  - Phân quyền ALCO / BOD        |  - Repo, Bán TP, Thu hồi HM   |
|  - Tắc nghẽn thanh toán RTGS    |  - Họp hàng ngày / thời gian thực| - Tái cấp vốn NHTW           |
+---------------------------------+---------------------------------+-------------------------------+
|  4. CHIẾN LƯỢC TRUYỀN THÔNG     |  5. BẢO ĐẢM THANH TOÁN INTRADAY |  6. HỆ THỐNG BÁO CÁO MI       |
|  - Trấn an người gửi tiền       |  - Ưu tiên dòng tiền RTGS       |  - Daily Liquidity Dashboard  |
|  - Thông cáo báo chí, cổ đông   |  - Tránh bị đình chỉ hệ thống   |  - Dự báo dòng tiền 30-90D    |
|  - Làm việc với Cơ quan QL      |  - Thấu chi khẩn cấp NHTW       |  - Báo cáo trực tiếp CEO/BOD  |
+---------------------------------------------------------------------------------------------------+
```

### A. Hệ thống Chỉ báo Cảnh báo Sớm (Early Warning Indicators — EWIs)
Hệ thống EWIs đóng vai trò phát hiện sớm các mầm mống suy thoái thanh khoản trước khi các chỉ số định lượng như [[lcr|LCR]] hay [[nsfr|NSFR]] chạm đáy. EWIs được chia làm 2 nhóm:
1. **Chỉ báo nội tại ngân hàng (Idiosyncratic EWIs)**:
   - Tốc độ sụt giảm tiền gửi bán lẻ và bán buôn vượt ngưỡng lịch sử (ví dụ $> 3\%$ trong 48 giờ).
   - Tỷ lệ rút tiền từ các tài khoản doanh nghiệp lớn hoặc tiền gửi không kỳ hạn CASA.
   - Chi phí phát hành chứng chỉ tiền gửi (CDs) hoặc Trái phiếu ngân hàng tăng vọt so với các ngân hàng đồng hạng.
   - Tổ chức xếp hạng tín nhiệm đưa ngân hàng vào diện theo dõi hạ bậc (Rating Downgrade Watch).
   - Tắc nghẽn dòng tiền trong ngày, thường xuyên phải sử dụng hạn mức thấu chi RTGS cuối ngày [[intraday-liquidity-risk]].
2. **Chỉ báo toàn thị trường (Systemic / Market-wide EWIs)**:
   - Chênh lệch Libor/SOFR-OIS hoặc lãi suất liên ngân hàng VND (ON/1W) nới rộng đột biến.
   - Thị trường Repo liên ngân hàng đối với tài sản phi chính phủ đóng băng.
   - Biến động tỷ giá hối đoái và căng thẳng thanh khoản ngoại tệ USD/VND.

### B. Ba Cấp Độ Cảnh Báo và Kích Hoạt CFP
Hội đồng ALCO quản trị CFP qua mô hình đèn tín hiệu 3 màu:
- **Cấp độ 1 — Xanh (Green — Normal / Business as Usual)**: Thanh khoản vận hành bình thường, LCR $\ge 110\%$, NSFR $\ge 105\%$, các EWIs nằm trong dải dung sai.
- **Cấp độ 2 — Vàng (Amber — Heightened Alert)**: Xuất hiện 2–3 chỉ báo EWI vượt ngưỡng cảnh báo (ví dụ dòng tiền rút bất thường trong 3 ngày liên tiếp). ALCO triệu tập họp bất thường, tăng tần suất theo dõi dòng tiền lên hàng ngày, rà soát kho tài sản khả dụng [[available-unencumbered-assets]] và chuẩn bị sẵn các hợp đồng repo.
- **Cấp độ 3 — Đỏ (Red — Crisis Invoked)**: Kích nổ khủng hoảng. LCR suy giảm nhanh về sát ngưỡng 100%, ngân hàng bị cắt hạn mức tín dụng liên ngân hàng hoặc bị hạ bậc tín nhiệm. Kích hoạt toàn diện CFP [[src-choudhry-principles-banking#^choudhry-cfp-4]].

---

## 3. Danh Mục Các Hành Động Quản Trị Khắc Phục (Management Action List)

Khi CFP được kích hoạt, Hội đồng Quản trị Khủng hoảng (Crisis Management Team — CMT do Tổng Giám đốc / Trưởng ALCO dẫn dắt) sẽ kích hoạt danh mục các hành động can thiệp theo thứ tự ưu tiên nhằm tạo dòng tiền vào khẩn cấp [[src-choudhry-principles-banking#^choudhry-cfp-3]]:

| Tuyến Nghiệp vụ | Hành động Can thiệp Cụ thể | Thời gian Triển khai | Tác động Tiêu cực Tiềm ẩn | Dòng Tiền Kỳ vọng |
| :--- | :--- | :---: | :--- | :---: |
| **Tín dụng Doanh nghiệp** | Thu hồi hoặc đóng băng các hạn mức cam kết tín dụng chưa rút đối với đối tác có dấu hiệu suy yếu [[src-choudhry-principles-banking#^choudhry-cfp-3]] | 24–48h | Tổn hại nghiêm trọng uy tín thương quyền ngân hàng | Rất cao |
| **Kinh doanh Vốn (Treasury)** | Mở rộng quy mô Repo toàn bộ Trái phiếu Chính phủ và giấy tờ có giá đủ điều kiện [[available-unencumbered-assets]] | Trong ngày | Tăng chi phí lãi vay, cạn kiệt tài sản unencumbered | Rất cao |
| **Danh mục Đầu tư** | Bán đứt danh mục trái phiếu sẵn sàng để bán (AFS/FVTOCI) | 1–3 ngày | Chấp nhận lỗ P&L từ bán giải chấp tài sản | Cao |
| **Phái sinh & Tiền tệ** | Đóng vị thế tự doanh có lãi (cash settle ITM positions), ngừng mở mới vị thế phái sinh rủi ro | 24–48h | Mất cơ hội kinh doanh | Trung bình |
| **Cửa sổ Tái cấp vốn NHTW** | Kích hoạt vay tái cấp vốn qua đêm hoặc cầm cố hồ sơ tín dụng đủ chuẩn tại Ngân hàng Trung ương | Trong ngày | Tín hiệu tiêu cực nếu bị rò rỉ thông tin ra thị trường | Tối thượng |

---

## 4. Tương Tác Giữa CFP và Quy Mô Đệm Thanh Khoản (LAB / HQLA)

Một phát hiện mang tính đột phá của Giáo sư Choudhry và cơ quan giám sát tài chính quốc tế là **mối quan hệ đánh đổi trực tiếp giữa chất lượng của CFP và Quy mô Đệm Tài sản Thanh khoản (Liquidity Asset Buffer — LAB / HQLA)** [[src-choudhry-principles-banking#^choudhry-cfp-7]] [[src-choudhry-principles-banking#^choudhry-cfp-8]]:

$$\text{Required LAB} = \text{Stressed Net Cash Outflows} - \text{Credible Stressed Management Actions}$$

```
    KỊCH BẢN KHÔNG CÓ CFP CHUẨN MỰC           KỊCH BẢN CÓ CFP KHẢ THI & ĐƯỢC PHÊ DUYỆT
+---------------------------------------+   +---------------------------------------+
|  Tổng dòng tiền ra kịch bản Stress    |   |  Tổng dòng tiền ra kịch bản Stress    |
|  (30 - 90 ngày)                       |   |  (30 - 90 ngày)                       |
|  [ ================================ ] |   |  [ ================================ ] |
|                                       |   |                                       |
|  Ngân hàng BẮT BUỘC phải nắm giữ      |   |  Bù trừ: Hành động Quản trị CFP       |
|  100% tài sản HQLA thanh khoản cao    |   |  (Repo, thu hồi HM, bán tài sản...)   |
|  [ ================================ ] |   |  [ ------------------ ]               |
|                                       |   |                                       |
|  Hậu quả: Chi phí cơ hội vốn rất lớn, |   |  Quy mô Đệm HQLA bắt buộc GIẢM XUỐNG! |
|  NIM bị bào mòn nặng nề!              |   |  [ ============== ]                   |
|                                       |   |  Giải phóng vốn cho tín dụng sinh lời!|
+---------------------------------------+   +---------------------------------------+
```

1. **Cơ chế Bù trừ Dòng tiền Quản trị (Management Action Offsetting)**:
   - Nếu ngân hàng chứng minh được bằng văn bản, dữ liệu lịch sử và quy trình thực nghiệm rằng các hành động trong CFP có độ khả thi cao trong thời gian khủng hoảng, cơ quan giám sát cho phép khấu trừ dòng tiền tạo ra từ CFP vào tổng dòng tiền ra stress [[src-choudhry-principles-banking#^choudhry-cfp-7]].
2. **Giải phóng Năng lực Tài trợ (Freeing up Funding Capacity)**:
   - Nhờ có CFP vững chắc, ngân hàng không cần phải "chôn" một lượng vốn khổng lồ vào các tài sản có lợi suất thấp như tiền gửi NHTW hay TPCP ngắn hạn. Ngân hàng có thể duy trì quy mô [[hqla|HQLA]] ở mức tối ưu hợp lý, chuyển hóa nguồn lực sang các khoản cho vay khách hàng sinh lời cao hơn, cải thiện trực tiếp tỷ lệ thu nhập lãi thuần [[synthetic-balance-sheet-liquidity-risk|NIM]] [[src-choudhry-principles-banking#^choudhry-cfp-8]].
3. **Gia tăng Niềm tin Thị trường (Stakeholder Confidence)**:
   - Một bản CFP được phê duyệt và diễn tập định kỳ tác động tích cực tức thì đến đánh giá tín nhiệm của các tổ chức xếp hạng (Moody's, S&P, Fitch), giúp ngân hàng duy trì hạn mức tín dụng và giảm thiểu phần bù rủi ro huy động vốn [[src-choudhry-principles-banking#^choudhry-cfp-9]].
