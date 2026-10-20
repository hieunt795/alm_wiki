---
title: "Tỷ Lệ Đòn Bẩy (Leverage Ratio — LR)"
aliases: [Leverage Ratio, LR, Basel III Leverage Ratio, Tỷ lệ đòn bẩy Basel, Tỷ lệ đòn bẩy tối thiểu 3%]
type: metric
domains: [basel, alm, vn-reg]
status: active
maturity: draft
scope: entity
unit: "%"
target: ">= 3.0%"
formula: "Leverage Ratio = (Tier 1 Capital / Total Exposure Measure) * 100%"
sources: ["[[src-bcbs-lev]]", "[[src-lubinska-alm-optimisation]]", "[[src-choudhry-principles-banking]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: measures, to: "[[leverage-exposure-measure]]", cite: "[[src-bcbs-lev#^lev20-3]]"}
tags: [leverage-ratio, basel-iii, pillar-1, capital, exposure-measure, alco, metric]
updated: 2026-10-20
reviewed:
---

## 1. Định nghĩa Chuẩn mực

Tỷ lệ Đòn bẩy (Leverage Ratio — LR) là một chuẩn mực định lượng phi rủi ro (non-risk-based) thuộc Trụ cột 1 của Basel III, đóng vai trò là "chốt chặn an toàn" (backstop measure) bổ trợ cho khuôn khổ an toàn vốn dựa trên trọng số rủi ro (Risk-Weighted Assets — RWA) [[src-bcbs-lev#^lev20-1]]. 

Mục tiêu cốt lõi của chỉ số này là:
1. Hạn chế sự tích tụ đòn bẩy quá mức trong toàn bộ hệ thống ngân hàng, ngăn chặn các chu kỳ bùng nổ tín dụng ảo và triệt tiêu vòng xoáy giảm đòn bẩy hỗn loạn (destabilising deleveraging spiral) có thể phá hủy thanh khoản thị trường và làm suy sụp nền kinh tế thực [[src-bcbs-lev#^lev20-1]].
2. Khắc phục khiếm khuyết nội tại của các mô hình xếp hạng tín nhiệm nội bộ (IRB) — nơi các ngân hàng có xu hướng tối ưu hóa toán học và hạ thấp nhân tạo hệ số rủi ro RWA để giảm thiểu vốn tự có bắt buộc [[src-bcbs-lev#^lev20-1]].

Các ngân hàng phải duy trì tỷ lệ đòn bẩy tối thiểu **3% tại mọi thời điểm** [[src-bcbs-lev#^lev20-7]].

---

## 2. Công thức và Thước đo Cấu thành

Theo quy định tại LEV20.3, tỷ lệ đòn bẩy được tính toán bằng Vốn cấp 1 chia cho Tổng quy mô phơi nhiễm [[src-bcbs-lev#^lev20-3]]:

$$\text{Leverage Ratio} = \frac{\text{Tier 1 Capital}}{\text{Total Exposure Measure}} \ge 3.0\%$$

```
                                 Tier 1 Capital (CET1 + AT1)
Leverage Ratio = ------------------------------------------------------------- >= 3.0%
                 On-Balance + Derivatives (SA-CCR) + SFTs (Gross+E*) + OBS (CCF)
```

### A. Thước đo Vốn (Tử số — Capital Measure)
- Tử số là **Vốn cấp 1 (Tier 1 Capital)** gồm Vốn cấp 1 phổ thông (CET1) và Vốn cấp 1 bổ sung (AT1) theo định nghĩa tại CAP10 [[src-bcbs-lev#^lev20-4]].
- Không sử dụng Vốn cấp 2 (Tier 2 Capital) vì đòn bẩy đòi hỏi khả năng hấp thụ tổn thất ngay trong trạng thái hoạt động liên tục (going-concern loss absorbency).

### B. Thước đo Quy mô Phơi nhiễm (Mẫu số — Exposure Measure)
Tổng quy mô phơi nhiễm là tổng của 4 cấu phần phơi nhiễm [[src-bcbs-lev#^lev20-5]]:
1. **Phơi nhiễm nội bảng (On-balance sheet exposures)**: Toàn bộ tài sản kế toán gộp, trừ các khoản khấu trừ Vốn cấp 1 và dự phòng rủi ro cụ thể [[src-bcbs-lev#^lev30-8]] [[src-bcbs-lev#^lev30-9]].
2. **Phơi nhiễm phái sinh (Derivative exposures)**: Đo lường theo SA-CCR với hệ số mở rộng $\alpha = 1.4$: $\text{Exposure} = 1.4 \times (\text{RC} + \text{PFE})$ [[src-bcbs-lev#^lev30-14]].
3. **Phơi nhiễm giao dịch tài trợ chứng khoán (SFT exposures)**: Tài sản SFTs kế toán gộp (hạn chế tối đa bù trừ nợ) cộng thêm phơi nhiễm rủi ro đối tác hiện tại $E^*$ [[src-bcbs-lev#^lev30-36]] [[src-bcbs-lev#^lev30-37]].
4. **Khoản mục cam kết ngoại bảng (Off-balance sheet items)**: Quy đổi bằng cách nhân giá trị danh nghĩa chưa rút với hệ số chuyển đổi tín dụng CCF (10%–100%) [[src-bcbs-lev#^lev30-47]].

Chi tiết kỹ thuật đo lường từng cấu phần được phân tích chuyên sâu tại [[leverage-exposure-measure]].

---

## 3. Phần Đệm Tỷ Lệ Đòn Bẩy Cho Các Ngân Hàng G-SIB

Đối với các ngân hàng có tầm quan trọng hệ thống toàn cầu (G-SIBs), Basel áp dụng thêm **Phần đệm Tỷ lệ Đòn bẩy (Leverage Ratio Buffer)** [[src-bcbs-lev#^lev40-1]]:
- Mức đệm được ấn định bằng **50% mức đệm vốn rủi ro bổ sung** (higher loss-absorbency requirement) [[src-bcbs-lev#^lev40-2]].
  - *Ví dụ*: Một ngân hàng G-SIB thuộc Nhóm 1 chịu đệm vốn bổ sung 1.0% RWA thì phải duy trì đệm đòn bẩy thêm $0.5\%$, nâng tổng yêu cầu tỷ lệ đòn bẩy lên $3.5\%$.
- Phần đệm này phải được đáp ứng hoàn toàn bằng **Vốn cấp 1 (Tier 1 Capital)** [[src-bcbs-lev#^lev40-1]].
- Nếu tỷ lệ đòn bẩy rơi vào khoảng đệm, ngân hàng sẽ bị áp dụng chế tài tự động giới hạn phân phối lợi nhuận (cổ tức, thưởng nhân sự cấp cao, mua lại cổ phiếu) theo 5 bậc thang tương tự như đệm bảo toàn vốn [[src-bcbs-lev#^lev40-4]].

---

## 4. Bảng So Sánh Chuẩn Mực: Basel III vs Việt Nam

| Cấu phần | Chuẩn mực Basel III (BCBS LEV) | Quy định Việt Nam | Ghi chú & Lộ trình ALM |
| :--- | :--- | :--- | :--- |
| **Ngưỡng tối thiểu** | $\ge 3.0\%$ liên tục [[src-bcbs-lev#^lev20-7]] | Chưa có ngưỡng cố định: Thống đốc quyết định việc áp dụng LEV, gồm ngưỡng tối thiểu và chế độ báo cáo, khi cần thiết trong từng thời kỳ; ngoài thời gian đó ngân hàng quản lý theo quy định nội bộ [[src-tt50-2026-nhnn#^d8-1]] | Basel coi đây là chốt chặn cứng thuộc Trụ cột 1. |
| **Đệm bổ sung G-SIB** | $+50\%$ mức đệm rủi ro (tổng 3.5%–4.25%) [[src-bcbs-lev#^lev40-2]] | `[chưa áp dụng]` | Việt Nam chưa phân loại ngân hàng G-SIB theo chuẩn BIS. |
| **Tử số (Capital)** | Tier 1 Capital (CET1 + AT1) [[src-bcbs-lev#^lev20-4]] | LEV = Vốn cấp 1 / EM × 100%; Vốn cấp 1 theo quy định tỷ lệ an toàn vốn ngân hàng đang áp dụng; EM theo Phụ lục III TT50 [[src-tt50-2026-nhnn#^d8-1]] | Chuẩn Việt Nam thường tập trung vào Vốn tự có tổng hợp (CAR). |
| **Phái sinh** | SA-CCR: $1.4 \times (\text{RC} + \text{PFE})$ [[src-bcbs-lev#^lev30-14]] | `[cần nguồn]` | Tính toán giá trị thị trường và ký quỹ tiền mặt. |
| **Tài sản bảo đảm** | Cấm dùng TSBĐ giảm quy mô phơi nhiễm [[src-bcbs-lev#^lev30-2]] | `[cần nguồn]` | Nguyên tắc phi rủi ro triệt để của Basel. |
| **Cam kết ngoại bảng** | CCF 10%, 20%, 40%, 50%, 100% [[src-bcbs-lev#^lev30-49]] | `[cần nguồn: chờ TT14/2025]` | Hạn mức chưa rút vẫn tính vào đòn bẩy. |

---

## 5. Tương Tác Giữa Tỷ Lệ Đòn Bẩy và Bảng Cân Đối ALM (LCR — NSFR — IRRBB)

Tỷ lệ Đòn bẩy không vận hành độc lập mà tạo nên một thế kiềng ba chân cân não trong điều hành [[alco|ALCO]] và quản trị Bảng Cân đối Kế toán Tổng hợp [[synthetic-balance-sheet-liquidity-risk]]:

```
                 +------------------------------------------+
                 |            VỐN CẤP 1 (TIER 1)            |
                 +------------------------------------------+
                                      |
                +---------------------+---------------------+
                |                                           |
                v                                           v
    [ RỦI RO THANH KHOẢN ]                      [ TỶ LỆ ĐÒN BẨY (LR) ]
    Tích lũy tài sản HQLA                       Mọi tài sản nội bảng (kể cả HQLA
    (Level 1, RW = 0%) để                       rủi ro 0%) đều tính 100% vào mẫu
    đẩy chỉ số LCR >= 100%                      số -> Làm suy giảm chỉ số LR!
                |                                           |
                +---------------------+---------------------+
                                      |
                                      v
                        [ MÂU THUẪN ĐIỀU HÀNH ALCO ]
                        HQLA càng cao -> LCR càng an toàn
                        nhưng LR càng chịu áp lực giảm!
```

1. **Nghịch lý Dự trữ Thanh khoản (HQLA Paradox)**: 
   - Để cải thiện [[lcr|LCR $\ge 100\%$]], Treasury phải mua thêm Trái phiếu Chính phủ (Level 1 Assets) và gửi tiền tại NHTW. Các tài sản này có rủi ro tín dụng bằng 0 (RWA = 0%), không làm suy giảm tỷ lệ an toàn vốn CAR.
   - Tuy nhiên, trong Tỷ lệ Đòn bẩy, Trái phiếu Chính phủ và Tiền gửi NHTW vẫn bị tính trọn vẹn 100% vào mẫu số phơi nhiễm nội bảng [[src-bcbs-lev#^lev30-8]]. Do đó, **tăng dự trữ thanh khoản để đạt LCR sẽ trực tiếp đẩy phơi nhiễm tăng lên và kéo tụt Tỷ lệ Đòn bẩy LR**.
2. **Chi phí Đòn bẩy của Hoạt động Repo (SFT Leverage Drag)**:
   - Nghiệp vụ Repo đảo (Reverse Repo) vừa làm tăng tài sản vừa tạo phơi nhiễm đối tác $E^*$. Dù là tài trợ có bảo đảm tuyệt đối, SFT vẫn làm phình to mẫu số Exposure Measure, đòi hỏi ALCO phải giám sát chặt chẽ biên lợi nhuận ròng.
3. **Giới hạn Mở rộng Bảng Cân đối (Balance Sheet Capacity Ceiling)**:
   - Với mức sàn $\text{LR} \ge 3\%$, tối đa một đồng Vốn cấp 1 chỉ có thể tài trợ cho $33.33$ đồng quy mô phơi nhiễm tổng hợp ($1 / 0.03 \approx 33.33$). Mọi chiến lược tăng trưởng tín dụng hay tăng đệm thanh khoản đều bị chặn lại bởi giới hạn trần này.

4. **Hạn mức nội bộ và chiến lược (Choudhry, T4)**:
   - Choudhry đề xuất dùng mức 3% của Basel III làm cận trên và đặt hạn mức leverage nội bộ chặt hơn, như biện pháp macro-prudential trong pha mở rộng [[src-choudhry-principles-banking#^choudhry-strat-23]]. Leverage ratio (Assets/Capital) là một KPI trong Table 15.1 [[src-choudhry-principles-banking#^choudhry-strat-28]]. Xem [[bank-strategic-plan]].
   - *Diễn giải:* "cận trên" ở đây theo nghĩa giới hạn đòn bẩy (tài sản/vốn ≤ 33,3 lần), tương đương tỷ lệ vốn/phơi nhiễm ≥ 3%.

---

## 6. Nhầm Lẫn Thường Gặp

- **Nhầm lẫn 1: Cho rằng tài sản rủi ro 0% (như TPCP hay tiền gửi NHTW) được loại trừ khỏi Tỷ lệ Đòn bẩy.**
  - *Thực tế*: Nguyên tắc cốt tử của LEV là phi rủi ro (non-risk-based). Toàn bộ tài sản nội bảng đều bị tính 100% vào mẫu số [[src-bcbs-lev#^lev30-8]], trừ trường hợp cơ quan giám sát kích hoạt quyền quyết định quốc gia tạm thời miễn trừ dự trữ NHTW trong khủng hoảng đặc biệt đi kèm tăng tỷ lệ tối thiểu [[src-bcbs-lev#^lev30-7]].
- **Nhầm lẫn 2: Nghĩ rằng có thể dùng tài sản bảo đảm (TSBĐ) nhận về để bù trừ làm giảm phơi nhiễm phái sinh hoặc cho vay.**
  - *Thực tế*: Điều LEV30.2 nghiêm cấm triệt để việc dùng TSBĐ để khấu trừ phơi nhiễm [[src-bcbs-lev#^lev30-2]]. Khoản bù trừ duy nhất được chấp nhận đối với phái sinh là ký quỹ biến đổi bằng tiền mặt (Cash Variation Margin) đáp ứng đầy đủ điều kiện thanh toán hàng ngày [[src-bcbs-lev#^lev30-24]].
- **Nhầm lẫn 3: Đánh đồng Tỷ lệ Đòn bẩy với Tỷ lệ Đòn bẩy Tài chính Kế toán thông thường (Tổng Tài sản / Vốn chủ).**
  - *Thực tế*: Tỷ lệ Đòn bẩy Basel phức tạp hơn nhiều vì mẫu số bao quát cả giá trị danh nghĩa quy đổi của các công cụ phái sinh (theo SA-CCR với hệ số 1.4), các giao dịch SFTs và các cam kết tín dụng ngoại bảng chưa giải ngân (CCF 10%–100%) [[src-bcbs-lev#^lev20-5]] [[src-bcbs-lev#^lev30-47]].

- **Nhầm lẫn 4: Cho rằng 3% là mức tối đa.**
  - *Thực tế*: LEV20 đặt tỷ lệ đòn bẩy tối thiểu 3% [[src-bcbs-lev#^lev20-7]]. Một nguồn T4 (Lubinska) ghi Basel III/CRR yêu cầu "a maximum of 3%" [[src-lubinska-alm-optimisation#^lubinska-u02-13]]; đây là diễn đạt lệch của nguồn T4, căn cứ là chuẩn BCBS (T2).

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
