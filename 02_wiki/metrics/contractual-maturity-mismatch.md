---
title: "Contractual Maturity Mismatch — Thang Chênh Lệch Kỳ Hạn Hợp Đồng (Basel SRP50)"
aliases: [Contractual Maturity Mismatch, Maturity Ladder, Thang kỳ hạn thanh khoản, Khe hở kỳ hạn hợp đồng, Liquidity Maturity Gap, Thang dòng tiền hợp đồng]
type: metric
domains: [basel, alm]
status: active
maturity: draft
sources: ["[[src-bcbs-framework]]", "[[src-bcbs-lcr]]", "[[src-bcbs-nsfr]]", "[[src-choudhry-principles-banking]]"]
relations:
  - {type: part-of, to: "[[bcbs]]", cite: "[[src-bcbs-framework#^srp50-1]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
  - {type: input-to, to: "[[nsfr]]", cite: "[[src-bcbs-framework#^srp50-2]]"}
  - {type: governs, to: "[[cash-inflows]]", cite: "[[src-bcbs-framework#^srp50-6]]"}
  - {type: governs, to: "[[cash-outflows]]", cite: "[[src-bcbs-framework#^srp50-6]]"}
tags: [liquidity, maturity-mismatch, maturity-ladder, contractual-cash-flows, liquidity-gap, srp50, basel]
updated: 2026-10-20
reviewed:
---

## Định nghĩa

### Tóm tắt Cấp cao (Executive Summary)

Trong khung giám sát thanh khoản của Ủy ban Basel (**BCBS SRP50**), **Chênh lệch kỳ hạn theo hợp đồng (Contractual Maturity Mismatch / Maturity Ladder)** là công cụ đo lường nền tảng phản ánh khoảng cách giữa dòng tiền vào và dòng tiền ra theo hợp đồng tại từng dải kỳ hạn xác định [[src-bcbs-framework#^srp50-6]]. 

Nếu như [[lcr]] kiểm tra khả năng sinh tồn trong kịch bản stress 30 ngày và [[nsfr]] giám sát cân bằng cấu trúc tài trợ 1 năm, thì Contractual Maturity Mismatch phơi bày **mức độ phụ thuộc thực chất của ngân hàng vào hoạt động chuyển đổi kỳ hạn (maturity transformation)** và chỉ ra lượng thanh khoản tiềm năng ngân hàng phải huy động nếu toàn bộ các nghĩa vụ dòng tiền ra phát sinh tại thời điểm sớm nhất có thể theo hợp đồng [[src-bcbs-framework#^srp50-6]].

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│               THANG KỲ HẠN DÒNG TIỀN HỢP ĐỒNG BASEL SRP50 (CONTRACTUAL MATURITY LADDER)          │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Dải kỳ hạn (Time Bands):                                                                        │
│ [Qua đêm] ➔ [7D] ➔ [14D] ➔ [1M] ➔ [2M] ➔ [3M] ➔ [6M] ➔ [9M] ➔ [1Y] ➔ [2Y] ➔ [3Y] ➔ [5Y] ➔ [>5Y] │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ DÒNG TIỀN VÀO HỢP ĐỒNG (Contractual Inflows):                                                   │
│ • Thu hồi nợ gốc, lãi cho vay đến hạn (không giải ngân mới)                                      │
│ • Đáo hạn trái phiếu, thu hồi tiền gửi liên ngân hàng                                           │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ DÒNG TIỀN RA HỢP ĐỒNG (Contractual Outflows):                                                   │
│ • Tất toán tiền gửi kỳ hạn, tiền gửi thanh toán (không tái tục - no rollover)                    │
│ • Đáo hạn nợ bán buôn, trái phiếu ngân hàng, cam kết tài trợ tiềm tàng                          │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ KHOẢNG TRỐNG THANH KHOẢN (LIQUIDITY GAP):                                                       │
│ • Khe hở đơn kỳ:      Gap_t = Inflow_t - Outflow_t                                              │
│ • Khe hở tích lũy:   CumGap_T = ∑_{t=1}^T Gap_t  (Xác định đỉnh thiếu hụt thanh khoản ròng)     │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 1. Bản Chất và Định Nghĩa Chuẩn Mực Basel SRP50

Theo quy định tại **SRP50.6 & SRP50.7**, Contractual Maturity Mismatch được định nghĩa là tập hợp các dòng tiền mặt và dòng chứng khoán vào/ra theo hợp đồng từ toàn bộ các khoản mục nội bảng và ngoại bảng, được phân bổ vào các dải kỳ hạn xác định dựa trên kỳ hạn hợp đồng còn lại (*residual contractual maturity*) [[src-bcbs-framework#^srp50-6]] [[src-bcbs-framework#^srp50-7]].

Khung giám sát chuẩn của Basel khuyến nghị xây dựng thang kỳ hạn trên **13 dải thời gian** [[src-bcbs-framework#^srp50-7]]:
1. Qua đêm (Overnight)
2. 7 ngày (7 days)
3. 14 ngày (14 days)
4. 1 tháng (1 month)
5. 2 tháng (2 months)
6. 3 tháng (3 months)
7. 6 tháng (6 months)
8. 9 tháng (9 months)
9. 1 năm (1 year)
10. 2 năm (2 years)
11. 3 năm (3 years)
12. 5 năm (5 years)
13. Trên 5 năm (Beyond 5 years)

Các công cụ không xác định kỳ hạn đáo hạn cụ thể (*non-defined or open maturity* như vốn chủ sở hữu, nợ xấu NPLs, tiền gửi thanh toán không kỳ hạn) bắt buộc phải được tách riêng và báo cáo độc lập mà không áp đặt bất kỳ giả định chủ quan nào về thời điểm đáo hạn [[src-bcbs-framework#^srp50-7]] [[src-bcbs-framework#^srp50-8]].

---

## Công thức & tham số

### 2. Bốn Giả Định Nghiêm Ngặt của Dòng Tiền Hợp Đồng (SRP50.9)

Khác với các mô hình dự báo kinh doanh thông thường, thang kỳ hạn hợp đồng Basel được thiết lập dựa trên nguyên tắc **thuần túy pháp lý hợp đồng (*pure contractual run-off*)** mà không tính đến hành vi khách hàng [[src-bcbs-framework#^srp50-9]]:

1. **Giả định Không Tái tục Nợ (No Rollover Assumption)**: Toàn bộ các khoản nợ phải trả (tiền gửi có kỳ hạn, vay liên ngân hàng, giấy tờ có giá) được giả định sẽ rút sạch khi đáo hạn hợp đồng, không một khoản nợ nào được quay vòng hoặc gia hạn [[src-bcbs-framework#^srp50-9]].
2. **Giả định Không Phát sinh Tài sản Mới (No New Contracts)**: Ngân hàng giả định ngừng hoàn toàn việc giải ngân các khoản vay mới hoặc mua thêm chứng khoán mới; toàn bộ tài sản chỉ thu hồi gốc và lãi theo đúng lịch trình hợp đồng [[src-bcbs-framework#^srp50-9]].
3. **Theo dõi Dòng Chứng khoán Song hành (Securities Flows)**: Ngân hàng phải ghi nhận toàn bộ dòng luân chuyển chứng khoán song song với dòng tiền mặt, phục vụ việc giám sát kỳ hạn đáo hạn của các hợp đồng hoán đổi tài sản bảo đảm (collateral swaps) và vay mượn chứng khoán không có bảo đảm [[src-bcbs-framework#^srp50-9]].
4. **Bóc tách Tài sản Tái thế chấp (Rehypothecated Collateral)**: Phải báo cáo riêng biệt lượng tài sản bảo đảm của khách hàng mà ngân hàng được quyền tái thế chấp và lượng thực tế đã đem đi tái thế chấp, nhằm phát hiện rủi ro lệch pha kỳ hạn giữa tài sản bảo đảm đi vay và cho vay [[src-bcbs-framework#^srp50-9]].

---

## Diễn giải

### 3. Đối Chiếu: Thang Kỳ Hạn Hợp Đồng vs Thang Kỳ Hạn Hành Vi

Ủy ban Basel phân định rõ ranh giới giữa hai lăng kính thang kỳ hạn [[src-bcbs-framework#^srp50-11]] [[src-bcbs-framework#^srp50-12]]:

| Tiêu chí | Thang Kỳ hạn Hợp đồng (Contractual Mismatch - SRP50) | Thang Kỳ hạn Hành vi (Behavioural / Going-Concern Mismatch) |
|---|---|---|
| **Cơ sở xác định** | Ngày đáo hạn pháp lý ghi trên hợp đồng [[src-bcbs-framework#^srp50-7]] | Mô hình kinh tế lượng phân tích hành vi khách hàng lịch sử [[src-bcbs-framework#^srp50-12]] |
| **Giả định tái tục (Rollover)** | $0\%$ — Không quay vòng nợ [[src-bcbs-framework#^srp50-9]] | Có tính tỷ lệ tái tục tiền gửi tiết kiệm và quay vòng vốn vay lưu động |
| **Tiền gửi không kỳ hạn (CASA)** | Đưa vào dải qua đêm ($T=0$) hoặc báo cáo riêng [[src-bcbs-framework#^srp50-7]] | Tách thành phần phi lõi (ngắn hạn) và phần lõi ổn định 2–5 năm |
| **Trả nợ trước hạn (CPR)** | Không tính trả nợ sớm; thu gốc theo lịch hợp đồng | Ước tính tốc độ trả nợ sớm biến động theo lãi suất thị trường |
| **Mục đích quản trị** | Đo lường mức độ phụ thuộc chuyển đổi kỳ hạn và kiểm tra áp lực thanh khoản tối đa [[src-bcbs-framework#^srp50-6]] | Lập kế hoạch kinh doanh, điều hành thanh khoản hàng ngày và xây dựng kịch bản CFP |

---

### Liên hệ [[bcbs-liquidity-principles|BCBS 144]]: liquidity gap và hạn mức chênh lệch luỹ kế
- Principle 5 yêu cầu dự phóng dòng tiền theo nhiều kịch bản để lập phân tích 'cash flow mismatch' hay 'liquidity gap', tính thặng dư hoặc thiếu hụt ròng luỹ kế trên khung thời gian đánh giá [[src-bcbs-liquidity-principles-2008#^lrm-48]].
- Loại hạn mức phổ biến giới hạn chênh lệch dòng tiền hợp đồng luỹ kế, ví dụ nhu cầu funding ròng luỹ kế tính theo % tổng nợ, theo nhiều kỳ hạn [[src-bcbs-liquidity-principles-2008#^lrm-50]].

*Diễn giải:* BCBS 144 cho phép gap dựa trên giả định hành vi; thang kỳ hạn SRP50 ở trên chỉ dùng dòng tiền hợp đồng.

## Ứng dụng trong ALM

### 4. Ý Nghĩa trong Mô Hình Bảng Cân Đối Tổng Hợp (Synthetic Balance Sheet)

Thang kỳ hạn hợp đồng SRP50 là chiếc cầu nối giải tích giữa:
1. **Dòng Tiền Gốc và Thanh khoản**: Toàn bộ dòng tiền gốc vào và ra được phân bổ vào 13 dải kỳ hạn, cho thấy chính xác **đỉnh thâm hụt thanh khoản ròng lũy kế (Maximum Cumulative Outflow - MCO)**.
2. **Chiến lược Đệm HQLA**: Quy mô đệm [[hqla]] bắt buộc phải đủ lớn để che phủ đỉnh thâm hụt lũy kế trong 30 ngày đầu tiên (tương thích với tử số của [[lcr]]).
3. **Cơ cấu Nguồn vốn Dài hạn**: Khoảng trống thanh khoản âm lớn ở các dải kỳ hạn $>1$ năm cảnh báo ngân hàng đang chuyển đổi kỳ hạn quá mức, buộc [[alco|ALCO]] phải phát hành trái phiếu dài hạn hoặc tăng vốn tự có để bảo đảm chỉ số [[nsfr]].

- **Liquidity gap theo Choudhry (T4)**: liquidity gap là chênh lệch kỳ hạn giữa tài sản và nợ ở từng điểm kỳ hạn; mỗi gap là một phơi nhiễm funding gap risk [[src-choudhry-principles-banking#^choudhry-lgap-1]]. Gap luôn là dynamic gap; marginal (incremental) gap là thay đổi tài sản trừ thay đổi nợ trong kỳ [[src-choudhry-principles-banking#^choudhry-lgap-3]].
- **"ALM Smile" (Choudhry, T4)**: không quá 20% tổng funding ở bucket O/N–1 tuần, tương tự bucket 9–12 tháng [[src-choudhry-principles-banking#^choudhry-lgap-4]]. Ở phạm vi toàn bảng cân đối, Choudhry (2007) đề xuất không quá 20–30% được tài trợ ở kỳ hạn dưới 3 tháng [[src-choudhry-principles-banking#^choudhry-liq-6]].
- *Diễn giải:* các ngưỡng của Choudhry là khuyến nghị thực hành, không phải chuẩn SRP50. SRP50 chỉ yêu cầu báo cáo chênh lệch kỳ hạn hợp đồng, không đặt hạn mức.

---

## 5. Ma trận Liên kết Hệ thống ALM Wiki

* **Chuẩn mực Nguồn**: [[src-bcbs-framework]] (Chương SRP50, claims ^srp50-6 đến ^srp50-12).
* **Các Chỉ số Thanh khoản**: [[lcr]], [[nsfr]], [[cash-inflows]], [[cash-outflows]], [[net-cash-outflows]].
* **Mô hình & Chiến lược**: [[synthetic-balance-sheet-liquidity-risk]], [[integrated-alm-liquidity-strategy]], [[lcr-nsfr-interlinkages]].
* **Khái niệm Liên quan**: [[funding-concentration-risk]], [[available-unencumbered-assets]], [[lcr-by-currency]], [[intraday-liquidity-risk]].

## Đề xuất cập nhật
*Chưa có nội dung cần cập nhật.*
