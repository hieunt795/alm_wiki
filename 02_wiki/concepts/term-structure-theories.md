---
title: "Lý thuyết cấu trúc kỳ hạn lãi suất"
aliases: [Term Structure Theories, Yield Curve Theories, Lý thuyết đường cong lợi suất, Liquidity Preference Theory, Expectations Hypothesis, Segmented Markets Theory, Combined Theory]
type: concept
domains: [macro, product, alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations: []
tags: [yield-curve, term-structure, liquidity-premium, expectations-hypothesis, inverted-curve, concept]
updated: 2026-10-21
reviewed:
---

## Ý chính

- Lý thuyết cấu trúc kỳ hạn giải thích hình dạng đường cong lợi suất. Choudhry trình bày bốn cách giải thích: expectations hypothesis, liquidity preference theory, segmented markets theory và combined theory [[src-choudhry-principles-banking#^choudhry-ytc-2]] [[src-choudhry-principles-banking#^choudhry-ytc-3]] [[src-choudhry-principles-banking#^choudhry-ytc-4]].
- **Expectations hypothesis**: forward rate bằng spot rate kỳ vọng trong tương lai [[src-choudhry-principles-banking#^choudhry-ytc-2]].
- **Liquidity preference theory**: người đi vay muốn vay dài, người cho vay muốn cho vay ngắn. Vì vậy người cho vay phải được bù một premium cho việc mất thanh khoản, và đường cong hầu như luôn dốc lên [[src-choudhry-principles-banking#^choudhry-ytc-1]]. Forward rate có thể chứa liquidity premium [[src-choudhry-principles-banking#^choudhry-ytc-2]].
- **Segmented markets theory**: hoạt động tập trung ở từng phân khúc kỳ hạn không liên hệ nhau; cung cầu từng phân khúc tạo "bướu" trên đường cong [[src-choudhry-principles-banking#^choudhry-ytc-3]].
- **Combined theory**: forward rate bằng spot rate kỳ vọng cộng liquidity premium đã định lượng; lý thuyết này nhất quán với đường cong đảo ngược [[src-choudhry-principles-banking#^choudhry-ytc-4]].

## Cơ chế & drivers

- **Liquidity premium** là phần bù đòi hỏi khi nắm giữ công cụ kém thanh khoản hơn. Choudhry ghi phần bù này khó định lượng và biến động theo thời gian [[src-choudhry-principles-banking#^choudhry-ytc-2]].
- **Ngân hàng ở đầu ngắn**: theo segmented markets theory, ngân hàng tập trung hoạt động ở đầu ngắn đường cong vì quản lý tiền mặt hằng ngày và yêu cầu thanh khoản. Giả thuyết này giải thích được một số đặc điểm của đường cong dốc lên nhưng tự nó chưa đủ [[src-choudhry-principles-banking#^choudhry-ytc-3]].
- **Chính sách tiền tệ**: độ dốc đường cong, thường đo bằng lợi suất 10 năm trừ lãi suất 3 tháng, là thước đo mức thắt chặt của chính sách tiền tệ [[src-choudhry-principles-banking#^choudhry-ytc-5]].
- **Nợ công**: quy mô nợ công mà thị trường cảm nhận ảnh hưởng lợi suất trái phiếu; nợ tăng có thể đẩy lợi suất tăng trên mọi kỳ hạn [[src-choudhry-principles-banking#^choudhry-ytc-8]].
- **Đường cong benchmark**: ở nước không có thị trường swap thanh khoản, benchmark là đường cong trái phiếu chính phủ. Nơi có thị trường swap thanh khoản, swap rate được coi là lãi suất "phi rủi ro" và đường cong swap là benchmark định giá [[src-choudhry-principles-banking#^choudhry-ytc-9]]. Ở các nền kinh tế phát triển, đường cong swap thường được dùng để dự báo lãi suất ngắn hạn [[src-choudhry-principles-banking#^choudhry-ytc-8]].

## Phụ thuộc regime

- **Đường cong đảo ngược**: ở Mỹ, mọi cuộc suy thoái từ 1955 trừ một đều có đường cong Treasury đảo ngược đi trước. Cách giải thích thông thường là thị trường kỳ vọng kinh tế chậm lại hoặc suy thoái [[src-choudhry-principles-banking#^choudhry-ytc-5]].
- **Đường cong phẳng**: quyết định mua hay bán trái phiếu dài hạn nên dựa vào quan điểm về lãi suất dài hạn tương lai, không dựa vào hình dạng đường cong [[src-choudhry-principles-banking#^choudhry-ytc-6]].
- **Lãi suất về 0 (Covid-19, Anh)**: từ 16/3/2020 đến 25/5/2020, đường cong gilt ở đoạn 2–5 năm không chỉ đảo ngược mà xuống âm [[src-choudhry-principles-banking#^choudhry-ytc-7]]:

| UK gilt (%) | 6M | 1Y | 2Y | 5Y | 10Y | 30Y | Nguồn |
|---|---|---|---|---|---|---|---|
| 16/3/2020 | 0.42 | 0.34 | 0.29 | 0.36 | 0.42 | 0.86 | [[src-choudhry-principles-banking#^choudhry-ytc-7]] |
| 25/5/2020 | 0.13 | 0.03 | -0.04 | -0.02 | 0.18 | 0.58 | [[src-choudhry-principles-banking#^choudhry-ytc-7]] |
| 22/2/2021 | 0.02 | 0.01 | 0.08 | 0.29 | 0.7 | 1.27 | [[src-choudhry-principles-banking#^choudhry-ytc-7]] |

## Góc nhìn theo domain

- **Macro**: độ dốc và đảo ngược đường cong là chỉ báo chính sách tiền tệ và chu kỳ [[src-choudhry-principles-banking#^choudhry-ytc-5]].
- **Product**: ngân hàng dùng đường cong lợi suất để định giá sản phẩm, cùng với so sánh lãi suất ngân hàng ngang hàng và cung cầu [[src-choudhry-principles-banking#^choudhry-ytc-9]]. Đường cong nội bộ dùng cho định giá: [[internal-funding-curve]].
- **ALM**: cấu trúc kỳ hạn lãi suất là một trong bốn khái niệm định nghĩa ALM truyền thống; hình dạng đường cong phụ thuộc kỳ vọng lãi suất, liquidity preference và cung cầu [[src-choudhry-principles-banking#^choudhry-almb-4]]. Xem [[alm-evolution]].

*Diễn giải:* "term liquidity premium" ở đây là phần bù chung của thị trường cho kỳ hạn dài. TLP trong [[liquidity-transfer-pricing]] là spread riêng của ngân hàng trên swap rate ([[internal-funding-curve]]). Hai khái niệm trùng tên nhưng khác đối tượng đo.

## Bằng chứng thực nghiệm

- Đường cong gilt Anh xuống âm ở đoạn 2–5 năm tháng 5/2020 [[src-choudhry-principles-banking#^choudhry-ytc-7]].

## Câu hỏi mở

- Công thức của expectations hypothesis, liquidity preference và combined theory (phương trình 4.3–4.5) bị mất khi convert; chưa có trong wiki.
- Chưa có nguồn về hình dạng đường cong lợi suất trái phiếu Chính phủ VN và quan hệ với chính sách NHNN [cần nguồn].
