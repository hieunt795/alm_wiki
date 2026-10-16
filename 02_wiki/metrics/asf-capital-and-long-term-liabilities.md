---
title: "Vốn tự có và Nợ dài hạn trong NSFR (Capital and Long-Term Liabilities)"
aliases: [Vốn tự có và nợ dài hạn NSFR, Capital and Long-Term Liabilities, ASF 100%]
type: metric
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]"]
relations:
  - {type: part-of, to: "[[available-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-10]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf20-2]]"}
  - {type: drives, to: "[[nsfr]]", direction: "+", cite: "[[src-bcbs-nsfr#^nsf30-10]]"}
tags: [nsfr, asf, capital, long-term-debt, funding-stability]
updated: 2026-10-16
reviewed:
---

## Định nghĩa

Vốn tự có và các khoản nợ dài hạn có kỳ hạn còn lại từ 1 năm trở lên là cấu phần ổn định cao nhất trong tử số [[available-stable-funding|ASF]], được gán hệ số **ASF 100%** [[src-bcbs-nsfr#^nsf30-10]] [[src-bcbs-nsfr#^nsf99-1]]. Cấu phần này đóng vai trò là nguồn vốn nền tảng cho phép ngân hàng tài trợ các tài sản kém thanh khoản dài hạn và duy trì hoạt động cấp tín dụng cho nền kinh tế mà không chịu rủi ro tái tài trợ ngắn hạn [[src-bcbs-nsfr#^nsf20-1]] [[src-bcbs-nsfr#^nsf30-3]].

## Công thức & tham số

### 1. Phạm vi các công cụ nhận hệ số ASF 100%
Theo NSF30.10, các công cụ đủ điều kiện nhận hệ số ASF 100% bao gồm 4 nhóm chính [[src-bcbs-nsfr#^nsf30-10]]:
1. **Vốn tự có quy định (Regulatory Capital)**: Toàn bộ vốn tự có trước khi áp dụng các khoản khấu trừ giám sát theo chuẩn CAP10, nhưng **loại trừ** phần công cụ Vốn cấp 2 (Tier 2) có kỳ hạn còn lại dưới 1 năm [[src-bcbs-nsfr#^nsf30-10]].
2. **Các công cụ vốn khác có kỳ hạn $\ge 1$ năm**: Các công cụ vốn không nằm trong mục (1) nhưng có kỳ hạn hiệu lực còn lại từ 1 năm trở lên, loại trừ các công cụ có quyền chọn rút ngắn kỳ hạn xuống dưới 1 năm [[src-bcbs-nsfr#^nsf30-10]].
3. **Các khoản vay nợ và trái phiếu kỳ hạn $\ge 1$ năm**: Toàn bộ các khoản vay mượn có bảo đảm và không bảo đảm (bao gồm tiền gửi có kỳ hạn) có kỳ hạn hiệu lực còn lại từ 1 năm trở lên [[src-bcbs-nsfr#^nsf30-10]].
4. **Tiền gửi bán lẻ có kỳ hạn $\ge 1$ năm**: Các khoản tiền gửi của khách hàng cá nhân có kỳ hạn còn lại trên 1 năm và hợp đồng có điều khoản phạt rút trước hạn đáng kể (*significant penalty*) [[src-bcbs-nsfr#^nsf30-10]].

## Diễn giải

### Cơ chế & drivers

#### 2. Nguyên tắc xử lý Quyền chọn Mua lại (Call Options)
- **Giả định thực hiện quyền chọn sớm nhất**: Khi xác định kỳ hạn nợ hoặc công cụ vốn có quyền chọn mua lại (*call option*), ngân hàng bắt buộc phải giả định nhà đầu tư sẽ thực hiện quyền chọn ở ngày đầu tiên có thể [[src-bcbs-nsfr#^nsf30-7]].
- **Kỳ vọng thị trường và rủi ro uy tín**: Đối với các khoản nợ có quyền chọn mua lại thuộc quyền quyết định của ngân hàng (như trái phiếu thứ cấp có điều khoản call tại năm thứ 5 của kỳ hạn 10 năm), nếu thị trường kỳ vọng ngân hàng sẽ thực hiện quyền mua lại để tái phát hành, ngân hàng và cơ quan giám sát phải giả định hành vi mua lại đó và tính kỳ hạn kết thúc tại ngày call date [[src-bcbs-nsfr#^nsf30-7]]. Nếu khoảng cách tới call date $< 1$ năm, công cụ đó không được nhận hệ số ASF 100% [[src-bcbs-nsfr#^nsf30-7]].
- **Cấu trúc Soft-Bullet**: Quyền chọn của ngân hàng về việc gia hạn kỳ hạn nợ (ví dụ trong các cấu trúc trái phiếu có bảo đảm soft-bullet) nhìn chung phải giả định là không được thực hiện nếu việc gia hạn có thể gây tổn hại đến uy tín phát hành của ngân hàng trên thị trường vốn [[src-bcbs-nsfr#^nsf30-7]].

#### 3. Cơ chế Cắt lát Dòng tiền (Cash Flow Slicing)
- Đối với các khoản nợ có kỳ hạn dài, Basel quy định không được gán toàn bộ số dư danh nghĩa vào nhóm 100% nếu có các dòng tiền thanh toán gốc/lãi diễn ra trong vòng 1 năm [[src-bcbs-nsfr#^nsf30-7]] [[src-bcbs-nsfr#^nsf30-10]]:
  - Dòng tiền đáo hạn sau 1 năm: Nhận hệ số **ASF 100%** [[src-bcbs-nsfr#^nsf30-10]].
  - Dòng tiền đáo hạn từ 6 tháng đến dưới 1 năm: Nhận hệ số **ASF 50%** (nếu từ định chế tài chính) [[src-bcbs-nsfr#^nsf30-13]].
  - Dòng tiền đáo hạn dưới 6 tháng: Nhận hệ số **ASF 0%** (nếu từ định chế tài chính) [[src-bcbs-nsfr#^nsf30-14]].

### Phụ thuộc regime
- **Môi trường Lãi suất Thấp vs Lãi suất Cao**:
  - Khi lãi suất thấp và thanh khoản dồi dào, các ngân hàng dễ dàng phát hành nợ dài hạn 3–5 năm với chi phí thấp để khóa nguồn ASF 100%.
  - Khi lãi suất tăng mạnh và thị trường trái phiếu thắt chặt, chi phí phát hành nợ mới tăng vọt, tạo áp lực lớn lên chi phí duy trì NSFR của ALM Treasury.

### Bằng chứng thực nghiệm
- **Khủng hoảng Ngân hàng Châu Âu 2011–2012**: Các ngân hàng tại Tây Ban Nha và Ý bị đóng băng thị trường phát hành trái phiếu quốc tế dài hạn, khiến tỷ trọng nợ có ASF 100% sụt giảm liên tục, đẩy các ngân hàng này vào khủng hoảng thanh khoản cấu trúc và buộc NHTW Châu Âu (ECB) phải can thiệp bằng các gói cho vay tái cấp vốn dài hạn (LTRO 3 năm).

## Ứng dụng trong ALM

### Góc nhìn theo domain
- **ALM Treasury**:
  - Quản trị cấu trúc bậc thang phát hành nợ (Debt Issuance Ladder): Treasury phải lập kế hoạch phát hành so le đều đặn theo từng năm để tránh việc các đợt phát hành lớn cùng trôi vào bucket dưới 1 năm tại cùng một thời điểm.
  - Phân bổ chi phí vốn dài hạn vào hệ thống FTP: Trái phiếu phát hành kỳ hạn $\ge 1$ năm chịu chi phí huy động cao hơn tiền gửi ngắn hạn; khoản chênh lệch này được Treasury kết chuyển thành phí thanh khoản kỳ hạn áp lên các mảng tín dụng trung dài hạn.
- **Basel**:
  - Đảm bảo vốn tự có (Tier 1 và Tier 2) không chỉ phục vụ hấp thụ tổn thất tín dụng theo Pillar 1 CAR mà còn đóng vai trò là "mỏ neo" thanh khoản dài hạn bảo vệ bảng cân đối kế toán [[src-bcbs-nsfr#^nsf20-1]].

## Câu hỏi mở
- Các công cụ nợ có điều khoản tự động chuyển đổi thành vốn cổ phần (CoCos - Contingent Convertibles) khi gặp stress sẽ được phản ánh như thế nào trong mô hình dự báo ASF tương lai?
- Tại Việt Nam, trái phiếu chuyển đổi và trái phiếu thứ cấp đủ điều kiện tính vào Vốn cấp 2 của các NHTM có được áp dụng trọn vẹn hệ số ASF 100% trước 1 năm đáo hạn hay không?
