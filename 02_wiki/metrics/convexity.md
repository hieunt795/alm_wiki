---
title: "Convexity"
aliases: [Convexity, CV, Negative Convexity, Tính lồi, Độ lồi]
type: metric
domains: [product, alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-fixed-income-markets]]"]
relations:
  - {type: input-to, to: "[[duration-gap-model]]"}
tags: [interest-rate-risk, convexity, second-order, negative-convexity, bond]
updated: 2026-10-22
reviewed:
---

## Định nghĩa
Convexity là thước đo rủi ro lãi suất bậc hai: nó đo độ cong của đường giá trị hiện tại theo lợi suất. Convexity cũng là chỉ báo sai số khi dùng modified duration ([[duration]]) [[src-choudhry-fixed-income-markets#^ch2-15]].

## Công thức
*Diễn giải (tái dựng, chưa đối chiếu bản gốc):* công thức (2.21)–(2.25) bị mất khi convert. Nguồn nói convexity adjustment nhân convexity với một nửa, vì số hạng thứ hai của khai triển Taylor có hệ số 1/2 [[src-choudhry-fixed-income-markets#^ch2-16]]. Dựng lại:

$$
\frac{\Delta P}{P} \approx -MD \cdot \Delta r + \frac{1}{2} \cdot CV \cdot (\Delta r)^2
$$
  [[src-choudhry-fixed-income-markets#^ch2-16]]

Kiểm bằng ví dụ của nguồn:

| Ví dụ | Đầu vào | Kết quả tái dựng | Nguồn ghi | Nguồn |
|---|---|---|---|---|
| 2.7A, trái phiếu 5% ngang giá, +200 bp | MD 2,639; CV 9,57 | MD: −5,278; convexity: ½ × 9,57 × 0,02² × 100 = +0,1914 | xấp xỉ MD −5,278, đánh giá cao mức giảm 0,1914 | [[src-choudhry-fixed-income-markets#^ch2-17]] |
| 2.7B, trái phiếu 5% 2009, +200 bp | MD 7,64498; CV 100 | MD: −15,28996%; convexity ½ × 100 × 0,02² = +2,0% | convexity 1,92462%; ròng −13,36534%; thực tế −13,92% | [[src-choudhry-fixed-income-markets#^ch2-18]] |
| 2.7, cùng trái phiếu, −150 bp | MD 7,64498 | MD: +11,46747% | MD + convexity +12,55007%; thực tế +10,98843% | [[src-choudhry-fixed-income-markets#^ch2-19]] |
| 2.8, cùng trái phiếu, +300 bp | MD 7,64498 | MD: −22,93494% | MD + convexity −18,60454%; thực tế −19,9477% | [[src-choudhry-fixed-income-markets#^ch2-20]] |

*Diễn giải:* ví dụ 2.7A khớp công thức tái dựng. Ví dụ 2.7B ghi CV = 100 nhưng convexity effect 1,92462% ứng với CV khoảng 96,23. Các số ròng của 2.7B (−13,36534%), −150 bp (+12,55007%) và 2.8 (−18,60454%) đều nhất quán với CV khoảng 96,23. Chưa đối chiếu bản PDF để xác định nguyên nhân.

## Diễn giải
**Tính chất (trái phiếu vanilla):**

| Tính chất | Nguồn |
|---|---|
| Convexity đồng biến với độ phân tán dòng tiền và với duration | [[src-choudhry-fixed-income-markets#^ch2-15]] |
| Giá trị convexity luôn dương; thay đổi giá do convexity dương cả khi lợi suất tăng lẫn giảm | [[src-choudhry-fixed-income-markets#^ch2-16]] |
| Tăng theo bình phương kỳ hạn; giảm khi coupon và lợi suất tăng | [[src-choudhry-fixed-income-markets#^ch2-21]] |
| Lợi suất giảm làm convexity tăng (tính chất của convexity dương) | [[src-choudhry-fixed-income-markets#^ch2-21]] |
| Vanilla gần như luôn có convexity dương; convexity âm (đường giá/lợi suất lõm) phổ biến nhất ở callable bond | [[src-choudhry-fixed-income-markets#^ch2-22]] |

**Khi nào convexity có ích.** Convexity chỉ hiệu quả với thay đổi lợi suất lớn: với −150 bp, MD đơn lẻ lại gần giá thực tế hơn [[src-choudhry-fixed-income-markets#^ch2-19]]. Với +300 bp, MD cộng convexity vẫn gần hơn MD đơn lẻ; sai số còn lại vì convexity cũng thay đổi theo lợi suất [[src-choudhry-fixed-income-markets#^ch2-20]].

## Basel vs VN
| Tham số | Basel | VN | Điều khoản | Hiệu lực |
|---|---|---|---|---|
| Convexity là chỉ tiêu bắt buộc | Không ghi nhận trong nguồn đã ingest [cần nguồn] | Phần TT83/2025 đã ingest không quy định convexity [cần nguồn] | — | — |

## Ứng dụng trong ALM
- *Diễn giải:* sốc chuẩn hoá IRRBB có biên độ hàng trăm bp ([[standardised-interest-rate-shocks]]), là vùng mà nguồn nói xấp xỉ duration sai đáng kể [[src-choudhry-fixed-income-markets#^ch2-14]]. Vì vậy ΔE theo [[duration-gap-model]] cần số hạng convexity, hoặc thay bằng định giá lại toàn bộ như ΔEVE ([[economic-value-of-equity]]). Cạnh `input-to` [[duration-gap-model]] là suy luận này, không có cite.
- *Diễn giải:* callable bond là trường hợp convexity âm phổ biến nhất [[src-choudhry-fixed-income-markets#^ch2-22]]. Khoản vay có quyền trả nợ trước hạn mang cấu trúc tương tự từ phía ngân hàng cho vay; xem [[behavioural-options]], [[option-risk]]. Nguồn ch2 không nói trực tiếp về khoản vay ngân hàng.

## Nhầm lẫn thường gặp
- **Luôn cộng convexity là chính xác hơn.** Với −150 bp ở ví dụ của nguồn, MD đơn lẻ gần thực tế hơn MD cộng convexity [[src-choudhry-fixed-income-markets#^ch2-19]].
- **Coi convexity là hằng số.** Convexity thay đổi theo lợi suất, nên với sốc rất lớn sai số vẫn còn [[src-choudhry-fixed-income-markets#^ch2-20]].
