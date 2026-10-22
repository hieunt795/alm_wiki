---
title: HQLA unwinding mechanism
aliases: [HQLA unwinding, Cơ chế unwind HQLA, Unwinding mechanism, Hoàn trả HQLA]
type: concept
domains: [alm, basel, vn-reg]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt50-2026-nhnn]]"]
relations:
  - {type: part-of, to: "[[hqla]]", cite: "[[src-bcbs-lcr#^lcr30-34]]"}
  - {type: limits, to: "[[level-2-assets]]", cite: "[[src-bcbs-lcr#^lcr30-37]]"}
  - {type: input-to, to: "[[lcr]]", cite: "[[src-bcbs-lcr#^lcr30-34]]"}
tags: [liquidity, hqla, unwinding, repo]
updated: 2026-10-22
reviewed:
---

## Ý chính
Cơ chế unwind HQLA là quy trình toán học bắt buộc theo chuẩn mực Basel III (LCR30.34–30.39) nhằm giả định **hoàn trả (unwind)** toàn bộ các giao dịch tài trợ có bảo đảm ngắn hạn (secured funding), cho vay có bảo đảm ngắn hạn (secured lending) và hoán đổi tài sản bảo đảm (collateral swap) đáo hạn trong vòng **30 ngày dương lịch** có liên quan đến việc trao đổi [[hqla]] [[src-bcbs-lcr#^lcr30-34]]. Mục đích cốt lõi của unwind là triệt tiêu hành vi "làm đẹp số liệu" (window-dressing) hoặc thao túng cơ cấu danh mục thanh khoản nhân tạo ngay trước ngày báo cáo, đảm bảo các mức trần tỷ trọng (trần 40% của [[level-2-assets]] và trần 15% của Level 2B) được xác định trên cấu trúc bảng cân đối thực chất [[src-bcbs-lcr#^lcr30-34]] [[src-bcbs-lcr#^lcr30-37]].

## Cơ chế & drivers

### 1. Tại sao Basel bắt buộc phải Unwind?
Trần 40% và 15% tính sau khi unwind giao dịch đáo hạn trong 30 ngày có trao đổi HQLA [[src-bcbs-lcr#^lcr30-34]]. *Diễn giải:* nếu các mức trần chỉ được tính trên số dư sổ sách tại thời điểm báo cáo (unadjusted stock), một ngân hàng đang nắm giữ tỷ trọng tài sản Level 2 quá lớn có thể dễ dàng lách trần bằng các giao dịch repo ngắn hạn trước ngày chốt số liệu:
- **Kịch bản lách luật**: *Diễn giải:* ví dụ giả định. Giả sử ngân hàng có 90 triệu Level 2A và chỉ có 10 triệu Level 1. Theo quy định, Level 2 tối đa bằng $\frac{2}{3}$ Level 1 (tức chỉ được công nhận $6.67$ triệu), ngân hàng sẽ bị loại bỏ hơn 83 triệu tài sản khỏi HQLA. Để né tránh, ngay trước ngày báo cáo, ngân hàng đem 60 triệu Level 2A đi repo kỳ hạn 7 ngày để vay 51 triệu tiền mặt (Level 1, sau haircut 15%). Tại ngày báo cáo, trên sổ sách ngân hàng chỉ còn 30 triệu Level 2A và có tới 61 triệu Level 1 ($10 + 51$). Khi đó, tỷ lệ Level 2 / Level 1 chỉ còn $30 / 61 \approx 49\%$, né được hầu hết khoản khấu trừ trần!
- **Hệ quả thực tế**: *Diễn giải:* chỉ 7 ngày sau đó, khi hợp đồng repo đáo hạn, ngân hàng bắt buộc phải hoàn trả 51 triệu tiền mặt để chuộc lại 60 triệu Level 2A, đưa ngân hàng quay trở lại trạng thái thiếu hụt nghiêm trọng thanh khoản cấp 1.
- **Giải pháp của Basel**: Buộc ngân hàng phải giả định đảo ngược toàn bộ các giao dịch ngắn hạn $\le 30$ ngày về trạng thái ban đầu, khiến Adjusted Level 1 quay về 10 triệu và Adjusted Level 2A quay về 90 triệu, vô hiệu hóa hoàn toàn thủ thuật trên [[src-bcbs-lcr#^lcr30-34]].

### 2. Phạm vi giao dịch chịu sự điều chỉnh của Unwind (LCR30.34, LCR30.37)
Mọi giao dịch thỏa mãn đồng thời hai điều kiện:
1. **Kỳ hạn hợp đồng**: Có ngày đáo hạn hợp đồng còn lại trong vòng **$\le 30$ ngày dương lịch** kể từ ngày báo cáo [[src-bcbs-lcr#^lcr30-37]].
2. **Loại nghiệp vụ**: Có liên quan đến việc trao đổi tài sản HQLA lấy tiền mặt hoặc lấy một tài sản HQLA khác [[src-bcbs-lcr#^lcr30-34]]:
   [[src-bcbs-lcr#^lcr30-37]]
   - **Huy động vốn có bảo đảm ngắn hạn (Secured Funding / Repo)**: Cầm cố HQLA để vay tiền mặt hoặc tài sản khác.
   - **Cho vay có bảo đảm ngắn hạn (Secured Lending / Reverse Repo)**: Cho vay tiền mặt để nhận tài sản HQLA làm bảo đảm.
   - **Hoán đổi tài sản bảo đảm ngắn hạn (Collateral Swaps)**: Hoán đổi trực tiếp giữa các lớp tài sản HQLA khác nhau (ví dụ đưa Level 2 nhận về Level 1).
- **Quy tắc giải tỏa chuỗi tái thế chấp (Rehypothecation Chaining Rule - LCR30.37)**: Trường hợp tài sản bảo đảm nhận được từ giao dịch cho vay có bảo đảm (reverse repo) thỏa mãn các điều kiện vận hành nhưng ngân hàng đã đem tái thế chấp (rehypothecated) vào một giao dịch huy động vốn ngắn hạn (repo), thì **cả hai giao dịch (cả 2 chặng) đều bắt buộc phải được unwind đồng thời** [[src-bcbs-lcr#^lcr30-37]].

### 3. Tác động của từng nghiệp vụ lên Số dư Điều chỉnh (Adjusted Amounts)

Tất cả các tài sản phải được áp dụng mức **haircut tương ứng trước khi đưa vào công thức tính trần** (Level 1: 0%, Level 2A: 15%, RMBS Level 2B: 25%, Level 2B khác: 50%) [[src-bcbs-lcr#^lcr30-41]] [[src-bcbs-lcr#^lcr30-43]] [[src-bcbs-lcr#^lcr30-45]]. *Diễn giải:* bảng dưới là cách wiki suy ra tác động của từng nghiệp vụ từ định nghĩa adjusted amount [[src-bcbs-lcr#^lcr30-37]].

| Nghiệp vụ đáo hạn $\le 30$ ngày | Bản chất khi Unwind (Đảo ngược giao dịch) | Tác động lên Adjusted Level 1 | Tác động lên Adjusted Level 2A | Tác động lên Adjusted Level 2B |
|---|---|---|---|---|
| **Repo bằng Level 1** (vay tiền mặt, thế chấp L1) | Trả lại tiền mặt, nhận lại tài sản Level 1 | **0** *(− tiền mặt L1, + tài sản L1)* | Không đổi | Không đổi |
| **Repo bằng Level 2A** (vay tiền mặt, thế chấp L2A) | Trả lại tiền mặt, nhận lại tài sản Level 2A | **Giảm** *(− tiền mặt Level 1)* | **Tăng** *(+ L2A nhận về sau haircut 15%)* | Không đổi |
| **Repo bằng Level 2B** (vay tiền mặt, thế chấp L2B) | Trả lại tiền mặt, nhận lại tài sản Level 2B | **Giảm** *(− tiền mặt Level 1)* | Không đổi | **Tăng** *(+ L2B nhận về sau haircut)* |
| **Reverse Repo nhận Level 1** (cho vay tiền, giữ L1) | Nhận lại tiền mặt, hoàn trả tài sản Level 1 | **0** *(+ tiền mặt L1, − tài sản L1)* | Không đổi | Không đổi |
| **Reverse Repo nhận Level 2A** (cho vay tiền, giữ L2A) | Nhận lại tiền mặt, hoàn trả tài sản Level 2A | **Tăng** *(+ tiền mặt Level 1)* | **Giảm** *(− L2A hoàn trả sau haircut 15%)* | Không đổi |
| **Reverse Repo nhận Level 2B** (cho vay tiền, giữ L2B) | Nhận lại tiền mặt, hoàn trả tài sản Level 2B | **Tăng** *(+ tiền mặt Level 1)* | Không đổi | **Giảm** *(− L2B hoàn trả sau haircut)* |
| **Collateral Swap** (hoán đổi L2A lấy L1) | Hoàn trả L1, nhận lại L2A | **Giảm** *(− L1 hoàn trả)* | **Tăng** *(+ L2A nhận lại)* | Không đổi |
| **Collateral Swap** (hoán đổi L2B lấy L2A) | Hoàn trả L2A, nhận lại L2B | Không đổi | **Giảm** *(− L2A hoàn trả)* | **Tăng** *(+ L2B nhận lại)* |

#### Công thức toán học tính số dư điều chỉnh (LCR30.37)
$$\text{Adjusted L1} = \text{L1 unencumbered hiện có} + \text{L1 repo chuộc về} - \text{L1 rev repo trả lại} + \text{L1 swap nhận về} - \text{L1 swap hoàn trả}$$
$$\text{Adjusted L2A} = \text{L2A unencumbered} + \text{L2A repo chuộc về} - \text{L2A rev repo trả lại} + \text{L2A swap nhận về} - \text{L2A swap hoàn trả}$$
$$\text{Adjusted L2B} = \text{L2B unencumbered} + \text{L2B repo chuộc về} - \text{L2B rev repo trả lại} + \text{L2B swap nhận về} - \text{L2B swap hoàn trả}$$
[[src-bcbs-lcr#^lcr30-37]]
*(Trong đó toàn bộ giá trị Level 2A và Level 2B đều đã trừ mức haircut tương ứng [[src-bcbs-lcr#^lcr30-34]]. *Diễn giải:* ba công thức trên là cách wiki viết lại định nghĩa adjusted amount.)*

### 4. Thuật toán hai bước tính toán khoản khấu trừ Trần (Cap Adjustments - LCR30.38, LCR30.39)

Theo LCR30.38–30.39 [[src-bcbs-lcr#^lcr30-37]], sau khi tính được bộ ba $\text{Adjusted L1}$, $\text{Adjusted L2A}$, $\text{Adjusted L2B}$, ngân hàng tính toán 2 khoản khấu trừ:

#### Bước 1: Tính khoản khấu trừ vượt trần 15% của Level 2B ($\text{Adjustment}_{15\%}$)
$$\text{Adjustment}_{15\%} = \max\left(\text{Adjusted L2B} - \frac{15}{85}(\text{Adjusted L1} + \text{Adjusted L2A}),\;\; \text{Adjusted L2B} - \frac{15}{60}\text{Adjusted L1},\;\; 0\right)$$
[[src-bcbs-lcr#^lcr30-34]] [[src-bcbs-lcr#^lcr30-37]]
- *Diễn giải:* **Ý nghĩa hệ số $\frac{15}{85}$**: Khi trần tổng thể 40% chưa chạm, Level 2B tối đa chiếm 15% tổng HQLA, đồng nghĩa $85\%$ còn lại là $(\text{Level 1} + \text{Level 2A})$. Tỷ lệ trần Level 2B so với phần còn lại là $\frac{15\%}{85\%} = \frac{15}{85}$.
- *Diễn giải:* **Ý nghĩa hệ số $\frac{15}{60} = \frac{1}{4}$**: Khi trần tổng thể 40% bị chạm, Level 1 bắt buộc phải chiếm ít nhất 60% tổng HQLA. Do đó, Level 2B tối đa chỉ được bằng $\frac{15\%}{60\%} = \frac{1}{4}$ giá trị của Level 1 điều chỉnh [[src-bcbs-lcr#^lcr30-34]].

#### Bước 2: Tính khoản khấu trừ vượt trần 40% tổng Level 2 ($\text{Adjustment}_{40\%}$)
$$\text{Adjustment}_{40\%} = \max\left(\big(\text{Adjusted L2A} + \text{Adjusted L2B} - \text{Adjustment}_{15\%}\big) - \frac{2}{3}\text{Adjusted L1},\;\; 0\right)$$
[[src-bcbs-lcr#^lcr30-34]] [[src-bcbs-lcr#^lcr30-37]]
- *Diễn giải:* **Ý nghĩa hệ số $\frac{2}{3}$**: Level 2 tối đa chiếm 40% tổng HQLA thì Level 1 tối thiểu chiếm 60%. Tỷ lệ tối đa của tổng Level 2 so với Level 1 là $\frac{40\%}{60\%} = \frac{2}{3}$ [[src-bcbs-lcr#^lcr30-34]].

#### Bước 3: Xác định Giá trị HQLA cuối cùng đưa vào tử số LCR
$$\text{Stock of HQLA} = \text{Level 1} + \text{Level 2A} + \text{Level 2B} - \text{Adjustment}_{15\%} - \text{Adjustment}_{40\%}$$
[[src-bcbs-lcr#^lcr30-34]] [[src-bcbs-lcr#^lcr30-37]]
*(Lưu ý: Các giá trị $\text{Level 1}, \text{Level 2A}, \text{Level 2B}$ ở công thức cuối là giá trị danh mục **trước khi unwind** (unencumbered stock tại ngày báo cáo sau haircut), nhưng bị trừ đi các khoản khấu trừ $\text{Adjustment}$ được tính từ danh mục sau unwind)* [[src-bcbs-lcr#^lcr30-37]].

### 5. Thẩm quyền mở rộng của Giám sát quốc gia (Footnote 5 LCR30.35)
Cơ quan giám sát quốc gia có quyền yêu cầu ngân hàng phải tính toán các mức trần 15% và 40% trên cả **cơ sở chưa điều chỉnh (unadjusted basis)** bên cạnh cơ sở điều chỉnh sau unwind [cần nguồn: chú thích LCR30.35 chưa có claim trong src-bcbs-lcr]. Nếu áp dụng tùy chọn này, khoản khấu trừ áp dụng cho ngân hàng sẽ là giá trị lớn nhất:
$$\text{Adjustment}_{15\%\text{ Final}} = \max\left(\text{Adjustment}_{15\%\text{ Adjusted}},\; \text{Adjustment}_{15\%\text{ Unadjusted}}\right)$$
$$\text{Adjustment}_{40\%\text{ Final}} = \max\left(\text{Adjustment}_{40\%\text{ Adjusted}},\; \text{Adjustment}_{40\%\text{ Unadjusted}}\right)$$
[cần nguồn: chú thích LCR30.35 chưa có claim trong src-bcbs-lcr]

---

### 6. Bốn kịch bản số học minh họa chi tiết
*Diễn giải:* bốn kịch bản dưới đây dùng số giả định, áp công thức LCR30.34–30.39 [[src-bcbs-lcr#^lcr30-34]] [[src-bcbs-lcr#^lcr30-37]].

#### Kịch bản 1: Danh mục cân bằng, không vượt trần
- **Dữ liệu tại ngày báo cáo**: $\text{L1} = 100$, $\text{L2A} = 30$, $\text{L2B} = 10$. Không có giao dịch repo/swap ngắn hạn đáo hạn trong 30 ngày.
- **Unwind**: $\text{Adjusted L1} = 100$, $\text{Adjusted L2A} = 30$, $\text{Adjusted L2B} = 10$.
- **Kiểm tra trần 15%**:
  $$\text{Ngưỡng 1} = \frac{15}{85}(100 + 30) = 22.94 > 10 \implies \text{Adjustment}_{15\%} = 0$$
- **Kiểm tra trần 40%**:
  $$\text{Ngưỡng tổng L2} = \frac{2}{3}(100) = 66.67 > (30 + 10 = 40) \implies \text{Adjustment}_{40\%} = 0$$
- **Stock of HQLA** $= 100 + 30 + 10 = 140$ (công nhận 100%).

#### Kịch bản 2: Vô hiệu hóa hành vi Window-Dressing
- **Danh mục gốc**: Ngân hàng có $\text{L1} = 10$, $\text{L2A} = 90$, $\text{L2B} = 0$.
- **Giao dịch trước kỳ**: Ngân hàng đem 60 L2A đi repo lấy 51 tiền mặt L1, đáo hạn sau 7 ngày.
- **Tại ngày báo cáo (chưa unwind)**: $\text{L1} = 61$ ($10 + 51$), $\text{L2A} = 30$ ($90 - 60$), $\text{L2B} = 0$.
  - *Nếu không unwind*: Trần 40% $= \frac{2}{3}(61) = 40.67 > 30 \implies$ Ngân hàng không bị trừ đồng nào! HQLA $= 61 + 30 = 91$.
- **Thực hiện Unwind theo chuẩn Basel**:
  - Hoàn trả 51 tiền mặt L1: $\text{Adjusted L1} = 61 - 51 = 10$.
  - Nhận lại 60 L2A: $\text{Adjusted L2A} = 30 + 60 = 90$.
  - Mức trần Level 2 tối đa $= \frac{2}{3} \times 10 = 6.67$.
  - Khoản khấu trừ trần $\text{Adjustment}_{40\%} = 90 - 6.67 = 83.33$.
- **Stock of HQLA thực tế**:
  $$\text{Stock of HQLA} = (61 + 30) - 83.33 = 7.67$$
  *Kết luận*: Cơ chế unwind đã vô hiệu hóa hoàn toàn thủ thuật repo, giáng một đòn trừng phạt khấu trừ 83.33 triệu, phản ánh đúng thực chất ngân hàng chỉ có 10 triệu Level 1 để bảo trợ cho 90 triệu Level 2.

#### Kịch bản 3: Chạm trần đơn lẻ Level 2B (Trần 40% chưa chạm)
- **Dữ liệu sau unwind**: $\text{Adjusted L1} = 100$, $\text{Adjusted L2A} = 20$, $\text{Adjusted L2B} = 35$.
- **Kiểm tra trần 15%**:
  - Ngưỡng theo công thức: $\frac{15}{85}(100 + 20) = 21.18$.
  - Do $\text{Adjusted L2B} = 35 > 21.18 \implies \text{Adjustment}_{15\%} = 35 - 21.18 = 13.82$.
  - Level 2B còn lại sau trừ trần $= 35 - 13.82 = 21.18$.
- **Kiểm tra trần 40%**:
  - Tổng Level 2 còn lại $= 20 + 21.18 = 41.18$.
  - Ngưỡng 40%: $\frac{2}{3}(100) = 66.67 > 41.18 \implies \text{Adjustment}_{40\%} = 0$.
- **Khoản bị loại bỏ khỏi HQLA**: 13.82.

#### Kịch bản 4: Chạm đồng thời cả hai mức trần 40% và 15% (Binding 40% Cap)
- **Dữ liệu sau unwind**: $\text{Adjusted L1} = 100$, $\text{Adjusted L2A} = 60$, $\text{Adjusted L2B} = 30$.
- **Kiểm tra trần 15%**:
  - Nhánh 1: $\text{L2B} - \frac{15}{85}(100 + 60) = 30 - 28.24 = 1.76$.
  - Nhánh 2 (khi trần 40% bị chạm, áp dụng hệ số 15/60):
    $$\text{L2B} - \frac{15}{60}(\text{L1}) = 30 - \frac{1}{4}(100) = 30 - 25 = 5.00$$
  - Vì $\max(1.76,\; 5.00,\; 0) = 5.00 \implies \text{Adjustment}_{15\%} = 5.00$.
  - Level 2B sau trừ trần $= 30 - 5.00 = 25.00$ (đúng bằng $\frac{1}{4}$ Level 1).
- **Kiểm tra trần 40%**:
  - Tổng Level 2 sau khi trừ $\text{Adjustment}_{15\%} = 60 + 25.00 = 85.00$.
  - Ngưỡng trần 40%: $\frac{2}{3}(100) = 66.67$.
  - $\text{Adjustment}_{40\%} = 85.00 - 66.67 = 18.33$.
- **Tổng khoản khấu trừ bị loại bỏ**:
  $$\text{Adjustment}_{\text{Total}} = \text{Adjustment}_{15\%} + \text{Adjustment}_{40\%} = 5.00 + 18.33 = 23.33$$
- **HQLA được công nhận** $= 100 + 60 + 30 - 23.33 = 166.67$.
  *(Kiểm tra lại cơ cấu: Level 1 = 100 (60% tổng HQLA), Level 2 = 66.67 (40% tổng HQLA), Level 2B = 25.00 (15% tổng HQLA). Cả 2 trần đều chạm chính xác tuyệt đối)*.

---

## Phụ thuộc regime
- **Regime bình thường**: *Diễn giải:* (ngoài wiki, chưa có nguồn) bộ phận ALM Treasury nên chạy mô hình mô phỏng Unwind hàng ngày (daily unwind simulation) để dự báo số dư $\text{Adjusted L1}$ tại ngày chốt báo cáo. Các hợp đồng repo/swap ngắn hạn phải được lên kế hoạch kỳ hạn lệch pha để tránh việc dòng tiền hoàn trả dồn cục làm sụt giảm Adjusted Level 1.
- **Regime stress thanh khoản**:
  - *Diễn giải:* (ngoài wiki, chưa có nguồn) khi thị trường xảy ra khủng hoảng, các đối tác trên thị trường repo thường từ chối gia hạn (roll-over) các hợp đồng cho vay có bảo đảm, buộc các giao dịch phải đáo hạn thực tế.
  - *Diễn giải:* quá trình unwind tự nhiên trên thị trường có thể khiến ngân hàng mất đi lượng tiền mặt dự trữ, kéo theo sự sụt giảm nhanh chóng của Adjusted Level 1 và kích hoạt các khoản khấu trừ trần $Adjustment_{40\%}$ theo hàm số phi tuyến.

## Góc nhìn theo domain
- **Basel**: *Diễn giải:* cơ chế Unwind thể hiện triết lý giám sát thực chất (substance over form), ngăn ngừa mọi nghiệp vụ kinh doanh chênh lệch quy định (regulatory arbitrage) thông qua thị trường repo ngắn hạn [[src-bcbs-lcr#^lcr30-34]].
- **ALM Treasury**:
  - *Mỏ neo Adjusted Level 1*: *Diễn giải:* Adjusted Level 1 chính là "chìa khóa" mở rộng dung lượng cho toàn bộ danh mục tài sản sinh lời Level 2. Mỗi 1 đồng Adjusted Level 1 bị sụt giảm kéo theo sự sụt giảm $0.67$ đồng hạn mức Level 2 được phép ghi nhận, do trần Level 2 bằng 2/3 Level 1 điều chỉnh [[src-bcbs-lcr#^lcr30-34]].
  - *Phối hợp giữa Money Market Desk và ALM Desk*: *Diễn giải:* Money Market Desk khi thực hiện nghiệp vụ repo/reverse repo ngắn hạn phục vụ thanh khoản trong ngày phải luôn kiểm tra hạn mức tác động lên Adjusted HQLA để không làm vi phạm tỷ lệ LCR của ngân hàng.
- **VN**: [[tt50-2026|TT50/2026]] áp dụng unwinding giống Basel: giá trị điều chỉnh của tài sản cấp 1, 2A, 2B là giá trị sau khi đảo ngược các giao dịch có bảo đảm, repo, reverse repo đáo hạn trong 30 ngày; trần tính qua KĐC15% (hệ số 15/85, 15/60) và KĐC40% (2/3 cấp 1) [[src-tt50-2026-nhnn#^pl1-a1]].
  - Quy tắc hai chặng: tài sản nhận từ cấp tín dụng có bảo đảm hoặc repo/reverse repo trong 30 ngày mà ngân hàng thế chấp lại hoặc dùng bảo đảm cho nghĩa vụ với đối tác khác đáo hạn trong 30 ngày thì ngân hàng phải đảo ngược cả 2 giao dịch [[src-tt50-2026-nhnn#^pl1-a1-1b]].
  - Không có giao dịch cần đảo ngược thì KĐC.L1, KĐC.L2A, KĐC.L2B bằng Level 1, Level 2A, Level 2B [[src-tt50-2026-nhnn#^pl1-a1-1b]].
  - Ví dụ của TT50: ngân hàng có 100 tỷ đồng tiền mặt, đã repo một tài sản cấp 2A với cam kết mua lại trong 30 ngày giá 40 tỷ đồng. Sau đảo ngược, ngân hàng có 60 tỷ đồng tiền mặt và 40 tỷ đồng tài sản cấp 2A; KĐC.L1 = 60, KĐC.L2A = 40 × 85% = 34 tỷ đồng. Nếu tài sản cấp 2A không đáp ứng yêu cầu vận hành thì KĐC.L2A = 0 [[src-tt50-2026-nhnn#^pl1-a1-vd]].
  - Cột (2) Bảng 3 của TT50 là giá trị điều chỉnh sau đảo ngược; cột (5) = cột (2) × hệ số thanh khoản [[src-tt50-2026-nhnn#^pl1-a5]].
  - *Diễn giải:* quy tắc hai chặng của TT50 tương ứng rehypothecation chaining rule ở LCR30.37. Phần A PL1 TT50 không có tùy chọn tính trần song song trên cơ sở chưa điều chỉnh như mục 5 ở trên.

## Bằng chứng thực nghiệm
- Trong cuộc khủng hoảng tài chính 2008, sự sụp đổ của Bear Stearns và Lehman Brothers bắt nguồn trực tiếp từ việc các định chế này phụ thuộc quá lớn vào các giao dịch repo qua đêm và ngắn hạn để tài trợ cho các tài sản kém thanh khoản. Khi đối tác từ chối roll-over repo, toàn bộ cấu trúc thanh khoản bị "unwind cưỡng bức" trong vòng vài ngày, dẫn đến vỡ nợ ngay lập tức. Đây chính là bằng chứng thực nghiệm thôi thúc Basel đưa ra nguyên tắc Unwind trong LCR30 [[src-bcbs-lcr#^lcr30-34]].

## Câu hỏi mở
- Các hệ thống ALM / Core Banking tại các ngân hàng thương mại Việt Nam hiện nay đã có module tự động tính toán unwinding theo thời gian thực (real-time unwind simulation) cho danh mục repo/reverse repo chưa, hay vẫn thực hiện thủ công vào cuối kỳ báo cáo?
