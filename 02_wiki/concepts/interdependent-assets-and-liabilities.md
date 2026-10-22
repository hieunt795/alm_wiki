---
title: "Tài sản và nợ phụ thuộc lẫn nhau (Interdependent Assets and Liabilities)"
aliases: [Interdependent Assets and Liabilities, Tài sản và nợ phụ thuộc lẫn nhau, Interdependent items]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from: 2018-01-01
valid_to:
as_of:
sources: ["[[src-bcbs-nsfr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[available-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-35]]"}
  - {type: part-of, to: "[[required-stable-funding]]", cite: "[[src-bcbs-nsfr#^nsf30-35]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-nsfr#^nsf30-35]]"}
tags: [liquidity, nsfr, pass-through, regulatory-relief]
updated: 2026-10-21
reviewed:
---

## Ý chính
Tài sản và nợ phụ thuộc lẫn nhau (*Interdependent Assets and Liabilities*) là cơ chế giám sát ngoại lệ có giới hạn trong chuẩn mực [[nsfr]], cho phép cơ quan giám sát điều chỉnh hệ số [[available-stable-funding|ASF]] và [[required-stable-funding|RSF]] của một cặp tài sản và nợ phải trả về đồng thời **0%** [[src-bcbs-nsfr#^nsf30-35]]. Cơ chế này áp dụng khi các điều khoản hợp đồng ràng buộc chặt chẽ đến mức nợ không thể đến hạn trước khi tài sản tất toán, và dòng tiền từ tài sản chỉ được dùng duy nhất để trả nợ tương ứng [[src-bcbs-nsfr#^nsf30-35]].

## Cơ chế & drivers

### 1. Bốn điều kiện tiên quyết (NSF30.35)
Để được phê duyệt áp dụng cơ chế interdependent, ngân hàng phải chứng minh cặp tài sản và nợ thỏa mãn đồng thời cả 4 điều kiện khắt khe [[src-bcbs-nsfr#^nsf30-35]]:
1. **Xác định rõ ràng (Clearly identifiable)**: Các khoản mục tài sản và nợ phụ thuộc lẫn nhau phải được bóc tách và định danh riêng biệt trên sổ sách hợp đồng.
2. **Trùng khớp kỳ hạn và giá trị gốc (Matching maturity and principal)**: Kỳ hạn đáo hạn và số tiền gốc của khoản nợ phải trả và tài sản tương ứng phải hoàn toàn trùng khớp nhau.
3. **Vai trò kênh dẫn vốn thuần túy (Pass-through unit)**: Ngân hàng chỉ đóng vai trò là một đơn vị trung chuyển thuần túy để dẫn nguồn vốn nhận được vào tài sản tương ứng, không chịu rủi ro chuyển hóa kỳ hạn ([[maturity-transformation]]).
4. **Đối tác độc lập (Different counterparties)**: Các bên đối tác của khoản nợ và khoản tài sản không được phép là cùng một thực thể.

### 2. Các nguyên tắc giám sát bổ sung
- **Không áp dụng cho phái sinh**: Chuẩn mực nêu rõ cơ chế này không áp dụng cho các giao dịch phái sinh do phái sinh hiếm khi thỏa mãn được đầy đủ các điều kiện ràng buộc hợp đồng khắt khe của NSF30.35 [[src-bcbs-nsfr#^nsf30-35]].
- **Ngăn ngừa khuyến khích lệch lạc (Perverse incentives)**: Cơ quan giám sát trước khi phê duyệt phải cân nhắc liệu việc cho phép áp dụng cơ chế này có tạo ra các khuyến khích lệch lạc hoặc hệ quả ngoài ý muốn đối với hoạt động của tổ chức tín dụng hay không [[src-bcbs-nsfr#^nsf30-36]].
- **Yêu cầu minh bạch quốc gia**: Các trường hợp giám sát viên thực hiện quyền quyết định áp dụng cơ chế này phải được quy định minh bạch, rõ ràng và công khai trong văn bản pháp quy của từng quốc gia [[src-bcbs-nsfr#^nsf30-37]].

## Phụ thuộc regime
- **Mô hình tài trợ dự án đặc thù**: Cơ chế interdependent thường áp dụng cho các chương trình tài trợ dự án nhà ở xã hội có trợ cấp của chính phủ, các khoản vay hợp vốn do ngân hàng phát triển quốc tế cấp vốn thông qua ngân hàng thương mại, hoặc các chương trình cho vay chuyển tiếp (*on-lending*) từ nguồn vốn ODA.

## Góc nhìn theo domain
- **ALM Treasury**:
  - Khi một cặp tài sản - nợ được công nhận là interdependent ($\text{ASF} = 0\%, \text{RSF} = 0\%$), ngân hàng được giải phóng hoàn toàn khỏi áp lực phải huy động nguồn vốn ổn định bổ sung để tài trợ cho tài sản dài hạn đó.
  - Loại trừ hoàn toàn rủi ro tái tài trợ (*refinancing risk*) ra khỏi bảng tính toán NSFR.
- **VN (TT50/2026 Đ26)**:
  - Điều kiện gồm: nguồn vốn chỉ dùng cho tài sản cụ thể, kỳ hạn và số tiền gốc khớp hoàn toàn, không phải phái sinh [[src-tt50-2026-nhnn#^d26-1]]; nợ không phải thanh toán khi tài sản chưa thu hồi được, đối tác hai vế không là cùng một chủ thể, đối tác không được đổi nội dung thoả thuận, ngân hàng chỉ là trung gian pass-through [[src-tt50-2026-nhnn#^d26-1b]].
  - Ngân hàng tự đánh giá từng cặp và được áp ASF, RSF 0% [[src-tt50-2026-nhnn#^d26-1]] [[src-tt50-2026-nhnn#^pl2-a2-2]] [[src-tt50-2026-nhnn#^pl2-b2-1]]. NHNN có quyền yêu cầu ngừng áp 0% và tính riêng từng vế khi cặp không thoả điều kiện hoặc không phản ánh đủ rủi ro [[src-tt50-2026-nhnn#^d26-3]].
  - *Diễn giải:* Basel để supervisor quyết định áp dụng [[src-bcbs-nsfr#^nsf30-35]]; TT50 để ngân hàng tự áp và NHNN kiểm tra sau.
- **Basel Framework**:
  - Thể hiện sự linh hoạt có kiểm soát của BCBS: Nhận diện thực tế rằng một số giao dịch pass-through không làm phát sinh rủi ro thanh khoản cấu trúc cho bảng cân đối kế toán.

## Bằng chứng thực nghiệm
- Tại Liên minh Châu Âu (EU - quy định CRR II), cơ chế interdependent được áp dụng phổ biến cho các khoản vay nhà ở có trợ cấp (*promotional loans*) do các ngân hàng phát triển công (như KfW tại Đức) cấp vốn và các ngân hàng thương mại đóng vai trò kênh phân phối trung gian.

## Câu hỏi mở
- Tại Việt Nam, các khoản vay ủy thác đầu tư hoặc các chương trình cho vay lại nguồn vốn ODA của Chính phủ (Bộ Tài chính) thông qua các NHTM có được NHNN công nhận là tài sản - nợ phụ thuộc lẫn nhau theo cơ chế này hay không?
