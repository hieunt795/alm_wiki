---
title: "Phương Pháp Xây Dựng Danh Mục Sao Chép (Replicating Portfolio) Cho CASA và Kỹ Thuật Phòng Ngừa IRS"
aliases: [CASA Replicating Portfolio and IRS Hedging, Danh mục sao chép CASA và phòng hộ IRS, Replicating Portfolio Model in ALM, Hedging IRRBB with IRS, CASA Duration and Swaps]
type: synthesis
domains: [alm, product, basel]
status: active
maturity: draft
origin: research
question: "Phương pháp xây dựng đường cong hoàn trả danh mục sao chép (Replicating Portfolio) cho tiền gửi CASA và kỹ thuật phòng ngừa rủi ro (Hedging) bằng IRS được triển khai như thế nào theo chuẩn mực BCBS d368, Moorad Choudhry và Fidelio Tata?"
as_of: 2026-10-17
sources: ["[[src-bcbs-irrbb-2016]]", "[[src-tata-bank-alm]]", "[[src-choudhry-principles-banking]]", "[[src-lubinska-alm-optimisation]]"]
relations:
  - {type: drives, to: "[[replicating-portfolio-model]]", cite: "[[src-tata-bank-alm#^tata-nmd-3]]"}
  - {type: drives, to: "[[interest-rate-swap]]", cite: "[[src-tata-bank-alm#^tata-nii-15]]"}
  - {type: input-to, to: "[[non-maturity-deposits]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u05-4]]"}
  - {type: input-to, to: "[[duration-gap-model]]", cite: "[[src-tata-bank-alm#^tata-dgap-1]]"}
  - {type: drives, to: "[[ftp-curve-construction-methodology]]", cite: "[[src-choudhry-principles-banking#^choudhry-ftp-2]]"}
tags: [irrbb, casa, nmd, replicating-portfolio, irs, interest-rate-swap, duration-gap, dv01, ftp, hedging, synthesis]
updated: 2026-10-17
reviewed:
---

## Câu hỏi

- **Q1**: Phương pháp xây dựng đường cong hoàn trả danh mục sao chép (Replicating Portfolio Model) cho tiền gửi CASA được thực hiện như thế nào (kỹ thuật phân tách Core/Non-core, lát cắt bình quân trượt moving-average tranches, tối ưu hóa biên lãi và ràng buộc trần Table 2 Basel d368)?
- **Q2**: Kỹ thuật phòng ngừa rủi ro lãi suất (Hedging) bằng Hợp đồng hoán đổi lãi suất (IRS) được triển khai như thế nào (Receiver vs Payer Swap, phòng hộ Duration Gap và DV01, quy tắc slotting hai chân swap theo reset date)?
- **Q3**: Tương tác giữa mô hình Replicating Portfolio CASA và chiến lược hedging IRS trong việc cân đối mâu thuẫn đánh đổi giữa EVE và NII, đồng thời truyền dẫn qua hệ thống FTP tại ALCO?

---

## Kết luận

1. **Về mô hình Replicating Portfolio cho CASA (Q1)**:
   - Do tiền gửi không kỳ hạn (CASA/NMDs) không có ngày đáo hạn hợp đồng nhưng số dư tổng thể có tính bám dính dài hạn [[src-tata-bank-alm#^tata-nmd-1]], ngân hàng mô phỏng đặc tính kinh tế của CASA bằng một danh mục đầu tư tái lập gồm các công cụ thanh khoản có kỳ hạn cố định [[src-tata-bank-alm#^tata-nmd-3]] [[src-bcbs-irrbb-2016#^irrbb-u06-6]].
   - Quy trình kỹ thuật gồm 3 bước: (1) Phân tách Non-core (phân bổ dải qua đêm) và Core deposits [[src-bcbs-irrbb-2016#^irrbb-u05-4]]; (2) Chia nhỏ số dư Core thành các lát cắt bình quân trượt (*moving-average tranches*) tái đầu tư định kỳ vào các công cụ cố định kỳ hạn $M$ năm [[src-tata-bank-alm#^tata-nmd-3]]; (3) Tối ưu hóa tỷ trọng các lát cắt để cực tiểu hóa phương sai biên lãi thuần $\min \text{Var}(r_{\text{rep}} - r_{\text{dep}})$ hoặc tối đa hóa độ ổn định NIM [[src-tata-bank-alm#^tata-nmd-3]].
   - Mô hình phải tuân thủ nghiêm ngặt các trần giám sát cố định tại Bảng 2 Basel d368 (Bán lẻ giao dịch trần core 90%, kỳ hạn tối đa 5 năm; Bán buôn trần core 50%, kỳ hạn tối đa 4 năm) [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
2. **Về kỹ thuật phòng ngừa rủi ro bằng IRS (Q2)**:
   - Hợp đồng hoán đổi lãi suất ([[interest-rate-swap|IRS]]) là công cụ chủ lực để điều chỉnh khe hở thời lượng (Duration Gap) và độ nhạy DV01 của sổ ngân hàng [[src-choudhry-principles-banking#^choudhry-irrbb-8]] [[src-tata-bank-alm#^tata-nii-15]]:
     - **Receiver Swap (Nhận cố định, Trả thả nổi)**: Sử dụng khi ngân hàng nhạy cảm tài sản ($\text{GAP} > 0$ hoặc $\text{DGAP} > 0$), bảo vệ thu nhập NII khi lãi suất thị trường giảm nhưng làm gia tăng mức độ tổn thất EVE khi lãi suất tăng [[src-tata-bank-alm#^tata-nii-10]] [[src-tata-bank-alm#^tata-nii-16]].
     - **Payer Swap (Trả cố định, Nhận thả nổi)**: Sử dụng khi ngân hàng nhạy cảm nợ ($\text{GAP} < 0$ hoặc $\text{DGAP} < 0$), bảo vệ thu nhập NII và giá trị vốn EVE khi lãi suất tăng [[src-tata-bank-alm#^tata-nii-17]].
   - **Quy tắc Slotting của Fidelio Tata**: Chân cố định của IRS được slot theo kỳ hạn hợp đồng (hoặc lịch hoàn trả gốc), trong khi chân thả nổi bắt buộc phải slot vào dải kỳ hạn chứa ngày Reset Date kế tiếp (do giá trị hiện tại quay về ngang mệnh giá $PV = Par$ tại ngày reset) [[src-tata-bank-alm#^tata-gap-2]] [[src-tata-bank-alm#^tata-nii-15]].
3. **Về tương tác hệ thống và truyền dẫn FTP tại ALCO (Q3)**:
   - Lợi suất hoàn trả của danh mục sao chép ($r_{\text{rep}}$) đóng vai trò là đường cong FTP chuẩn (VOF) cho sản phẩm CASA, giúp chuyển giao toàn bộ rủi ro lãi suất từ mạng lưới chi nhánh về Treasury CFU [[src-choudhry-principles-banking#^choudhry-ftp-1]] [[src-choudhry-principles-banking#^choudhry-ftp-2]].
   - Sau khi tiếp nhận vị thế thời lượng ngầm định của CASA, Treasury thực hiện phòng hộ động (*dynamic hedging*) trên thị trường liên ngân hàng bằng IRS để đưa Duration Gap toàn hàng về mức mục tiêu theo khẩu vị rủi ro của ALCO, cân bằng hài hòa giữa rủi ro giá trị vốn ($\Delta\text{EVE}$) và rủi ro thu nhập ($\Delta\text{NII}$) [[src-choudhry-principles-banking#^choudhry-irrbb-3]] [[src-choudhry-principles-banking#^choudhry-irrbb-8]].
   - *Lưu ý tuân thủ tại Việt Nam*: Hiện wiki chưa có nguồn văn bản quy định của NHNN về quản lý rủi ro mô hình sao chép và điều kiện phái sinh phòng ngừa IRRBB (chờ ingest `src-tt83-2025-nhnn` unit `PL5`, `C3-M8` và `C3-M7`).

---

## Cơ chế

### Q1 — Phương pháp xây dựng đường cong hoàn trả danh mục sao chép (Replicating Portfolio) cho CASA

Mô hình danh mục sao chép chuyển hóa đặc tính phi kỳ hạn của tiền gửi CASA thành một cấu trúc dòng tiền có kỳ hạn xác định thông qua 3 giai đoạn kỹ thuật [[src-tata-bank-alm#^tata-nmd-3]]:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    QUY TRÌNH XÂY DỰNG REPLICATING PORTFOLIO CHO TIỀN GỬI CASA                   │
└────────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                 │
  ┌──────────────────────────────┼──────────────────────────────┐
  ▼                              ▼                              ▼
┌──────────────────────────────┐┌──────────────────────────────┐┌──────────────────────────────┐
│  BƯỚC 1: PHÂN TÁCH SỐ DƯ     ││ BƯỚC 2: THIẾT KẾ TRANCHES    ││ BƯỚC 3: TỐI ƯU HÓA TỶ TRỌNG  │
├──────────────────────────────┤├──────────────────────────────┤├──────────────────────────────┤
│• Non-core: Biến động ngắn hạn││• Lát cắt bình quân trượt     ││• Cực tiểu hóa sai phân NIM   │
│  $\rightarrow$ Slot qua đêm (Overnight)  ││  (Moving-Average Tranches)   ││  $\min \text{Var}(r_{\text{rep}} - r_{\text{dep}})$   │
│• Core: Ổn định qua chu kỳ    ││• Đầu tư luân phiên vào trái  ││• Ràng buộc trần Table 2 BCBS │
│  $\rightarrow$ Đưa vào mô hình sao chép ││  phiếu/swap cố định kỳ hạn M ││• Ước tính tỷ lệ Run-off      │
└──────────────────────────────┘└──────────────────────────────┘└──────────────────────────────┘
```

1. **Phân tách cấu trúc Số dư (Core vs Non-core)**:
   - Phân tích chuỗi thời gian số dư tiền gửi lịch sử để bóc tách:
     - **Tiền gửi phi lõi (*Non-core deposits*)**: Phần số dư biến động theo mùa vụ $\rightarrow$ Bắt buộc phân bổ vào dải kỳ hạn **qua đêm (Overnight)** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
     - **Tiền gửi lõi (*Core deposits*)**: Phần số dư duy trì ổn định bền vững ngay cả trong môi trường lãi suất biến động [[src-tata-bank-alm#^tata-nmd-1]].
2. **Kỹ thuật Lát cắt bình quân trượt (Moving-Average Tranches)**:
   - Giả định danh mục sao chép đầu tư số dư Core vào các công cụ lãi suất cố định kỳ hạn $M$ năm, được chia thành $N$ lát cắt tái đầu tư cuốn chiếu theo tháng ($N = 12 \times M$) [[src-tata-bank-alm#^tata-nmd-3]]:
     $$r_{\text{rep},t}(M) = \frac{1}{N} \sum_{i=0}^{N-1} R_{\text{market}, t-i}(M)$$
   - Lợi suất hoàn trả của danh mục sao chép là bình quân trượt của lãi suất thị trường kỳ hạn $M$ trong quá khứ, giúp làm mượt biến động lãi suất và tạo ra thu nhập ổn định cho ngân hàng [[src-tata-bank-alm#^tata-nmd-3]].
3. **Thuật toán Tối ưu hóa (Optimization Engine)**:
   - Thiết lập hàm mục tiêu giải bài toán danh mục tối ưu:
     $$\min_{w_1, \dots, w_K} \text{Var}\left( \sum_{k=1}^K w_k \cdot r_{\text{rep},t}(M_k) - r_{\text{dep},t} \right) \quad \text{với } \sum w_k = 1, \, w_k \ge 0$$
   - Trong đó $r_{\text{dep},t}$ là lãi suất thực trả cho khách hàng gửi tiền CASA, và $w_k$ là tỷ trọng phân bổ vào các dải kỳ hạn $M_k$ (vd: 1Y, 2Y, 3Y, 5Y) [[src-tata-bank-alm#^tata-nmd-3]].
4. **Ràng buộc trần giám sát Basel d368 (Table 2)** [[src-bcbs-irrbb-2016#^irrbb-u05-4]]:
   - Bán lẻ - Tài khoản giao dịch: Trần Core tối đa **90%**, kỳ hạn bình quân gia quyền ($\text{WAM}$) tối đa **5 năm** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
   - Bán lẻ - Tài khoản phi giao dịch: Trần Core tối đa **70%**, kỳ hạn bình quân gia quyền tối đa **4,5 năm** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
   - Tiền gửi bán buôn: Trần Core tối đa **50%**, kỳ hạn bình quân gia quyền tối đa **4 năm** [[src-bcbs-irrbb-2016#^irrbb-u05-4]].

---

### Q2 — Kỹ thuật phòng ngừa rủi ro (Hedging) bằng Hợp đồng hoán đổi lãi suất (IRS)

Hợp đồng hoán đổi lãi suất cố định/thả nổi (IRS) là công cụ ngoại bảng linh hoạt nhất để ALM điều chỉnh Duration Gap và DV01 mà không cần thay đổi quy mô bảng cân đối kế toán [[src-choudhry-principles-banking#^choudhry-irrbb-8]] [[src-tata-bank-alm#^tata-nii-15]]:

| Tiêu chí | Receiver Swap (Nhận Cố định / Trả Thả nổi) | Payer Swap (Trả Cố định / Nhận Thả nổi) |
| :--- | :--- | :--- |
| **Cơ chế dòng tiền** | Nhận dòng tiền cố định $R_{\text{fixed}}$, trả lãi suất thả nổi thị trường $R_{\text{floating}}$ [[src-tata-bank-alm#^tata-nii-15]]. | Trả dòng tiền cố định $R_{\text{fixed}}$, nhận lãi suất thả nổi thị trường $R_{\text{floating}}$ [[src-tata-bank-alm#^tata-nii-17]]. |
| **Tác động lên Duration Gap** | **Tăng thời lượng tài sản**, làm dịch chuyển $\text{DGAP}$ theo chiều dương ($\Delta\text{DGAP} > 0$) [[src-tata-bank-alm#^tata-nii-10]]. | **Giảm thời lượng tài sản**, làm dịch chuyển $\text{DGAP}$ theo chiều âm ($\Delta\text{DGAP} < 0$) [[src-tata-bank-alm#^tata-nii-17]]. |
| **Trạng thái bảng cân đối áp dụng** | Áp dụng khi ngân hàng **nhạy cảm tài sản ($\text{GAP} > 0$)**, phòng ngừa rủi ro lãi suất thị trường giảm [[src-choudhry-principles-banking#^choudhry-irrbb-5]]. | Áp dụng khi ngân hàng **nhạy cảm nợ ($\text{GAP} < 0$)**, phòng ngừa rủi ro lãi suất thị trường tăng [[src-choudhry-principles-banking#^choudhry-irrbb-5]]. |
| **Tác động lên NII** | Bảo vệ và gia tăng NII khi lãi suất giảm; nhưng làm suy giảm NII khi lãi suất tăng (do chân thả nổi phải trả tăng chi phí) [[src-tata-bank-alm#^tata-nii-16]]. | Bảo vệ NII khi lãi suất tăng (chân thả nổi nhận về bù đắp chi phí huy động tăng); nhưng cố định chi phí khi lãi suất giảm [[src-tata-bank-alm#^tata-nii-17]]. |
| **Tác động lên EVE** | Khi lãi suất tăng, giá trị hiện tại của chân nhận cố định giảm mạnh $\rightarrow$ Làm suy giảm thêm $\Delta\text{EVE}$ [[src-tata-bank-alm#^tata-nii-10]]. | Khi lãi suất tăng, giá trị hiện tại của nghĩa vụ trả cố định giảm $\rightarrow$ Tạo ra khoản lãi giá trị hiện tại bù đắp suy giảm $\Delta\text{EVE}$ [[src-tata-bank-alm#^tata-nii-17]]. |

#### 1. Công thức xác định Quy mô phòng hộ (Hedge Sizing) qua DV01 và Duration Gap:
Để triệt tiêu hoàn toàn khe hở thời lượng bảng cân đối ($\text{DGAP} = 0$), quy mô danh nghĩa của vị thế IRS cần thiết lập ($N_{\text{IRS}}$) được tính toán theo công thức [[src-tata-bank-alm#^tata-dgap-1]] [[src-tata-bank-alm#^tata-dgap-2]]:
$$N_{\text{IRS}} = - \frac{\text{DGAP} \cdot \text{PV}(A)}{D^*_{\text{fixed}} - D^*_{\text{floating}}} = - \frac{\Delta\text{EVE} / \Delta y}{\text{DV01}_{\text{IRS}} \times 10^4}$$
Trong đó $D^*_{\text{fixed}}$ là thời lượng hiệu chỉnh của chân cố định và $D^*_{\text{floating}}$ là thời lượng đến ngày reset kế tiếp của chân thả nổi [[src-tata-bank-alm#^tata-gap-2]].

#### 2. Quy tắc Slotting IRS trên Repricing Schedule (Fidelio Tata):
- **Chân cố định (Fixed Leg)**: Phân bổ toàn bộ các dòng tiền coupon và gốc danh nghĩa vào các dải kỳ hạn theo đúng lịch hợp đồng đáo hạn [[src-tata-bank-alm#^tata-nii-15]].
- **Chân thả nổi (Floating Leg)**: Toàn bộ số dư danh nghĩa bắt buộc slot vào dải kỳ hạn chứa **ngày định giá lại tiếp theo (*next reset date*)**, vì tại ngày reset, chân thả nổi giao dịch lại ngang mệnh giá ($PV = Par$) [[src-tata-bank-alm#^tata-gap-2]] [[src-tata-bank-alm#^tata-nii-15]].

---

### Q3 — Tương tác hệ thống: Từ Mô hình CASA đến Chiến lược Phòng hộ IRS và Truyền dẫn FTP

Trong kiến trúc điều hành ALM hiện đại, mô hình Replicating Portfolio và công cụ IRS liên kết chặt chẽ qua cơ chế định giá chuyển vốn nội bộ ([[ftp-pricing-methodology|FTP]]) [[src-choudhry-principles-banking#^choudhry-ftp-1]]:

```
+───────────────────────────────────────────────────────────────────────────────────────────────────+
│                    CHUỖI TRUYỀN DẪN VÀ PHÒNG HỘ RỦI RO LÃI SUẤT TỔNG THỂ                         │
+───────────────────────────────────────────────────────────────────────────────────────────────────+
│                                                                                                   │
│  [ Khách hàng gửi CASA ]                                                                          │
│            │  (Tiền gửi không kỳ hạn, lãi suất thấp, bám dính hành vi)                            │
│            ▼                                                                                      │
│  [ Mô hình Replicating Portfolio ] ──(Table 2 Caps)──> Xác lập Đường cong Hoàn trả CASA           │
│            │                                                    │                                 │
│            │                                                    ▼                                 │
│            │                                           [ Hệ thống FTP VOF ]                       │
│            │                                           (Trả lãi suất kỳ hạn 3–5Y cho Chi nhánh,   │
│            │                                            khóa biên lợi nhuận thương mại)           │
│            ▼                                                    │                                 │
│  [ Chuyển giao Rủi ro Thời lượng về Treasury ] <────────────────┘                                 │
│            │                                                                                      │
│            ▼                                                                                      │
│  [ Tổng hợp Duration Gap Toàn Ngân Hàng ]                                                         │
│            │                                                                                      │
│            ▼                                                                                      │
│  [ Thị trường Phái sinh Liên ngân hàng ] <─── Thực thi IRS (Receiver/Payer) để Macro-Hedge         │
│            │                                                                                      │
│            ▼                                                                                      │
│  [ Cân bằng Đánh đổi EVE vs NII theo Khẩu vị ALCO ]                                               │
│                                                                                                   │
+───────────────────────────────────────────────────────────────────────────────────────────────────+
```

1. **Khóa biên lợi nhuận cho mạng lưới kinh doanh qua FTP**:
   - Replicating Portfolio rate cho phép Treasury trả cho chi nhánh một mức lãi suất FTP cố định dài hạn (tương đương kỳ hạn 3–5 năm) đối với nguồn vốn CASA [[src-choudhry-principles-banking#^choudhry-ftp-2]]. Chi nhánh hoàn toàn miễn nhiễm với rủi ro thị trường và tập trung tối đa vào việc phát triển số dư huy động [[src-choudhry-principles-banking#^choudhry-ftp-1]].
2. **Tập trung rủi ro và Macro-Hedging tại Treasury**:
   - Toàn bộ rủi ro biến động lãi suất và rủi ro thời lượng của CASA được chuyển giao về Treasury CFU [[src-choudhry-principles-banking#^choudhry-ftp-1]].
   - Thay vì phòng hộ vi mô từng khoản tiền gửi, Treasury tổng hợp vị thế ròng của toàn bộ bảng cân đối và thực hiện **phòng hộ vĩ mô động (*dynamic macro-hedging*)** bằng các hợp đồng IRS trên thị trường phái sinh liên ngân hàng [[src-choudhry-principles-banking#^choudhry-irrbb-8]].
3. **Giải quyết Mâu thuẫn Đánh đổi giữa EVE và NII tại ALCO**:
   - ALCO sử dụng danh mục sao chép để ổn định thu nhập $\Delta\text{NII}$ qua chu kỳ kinh tế [[src-tata-bank-alm#^tata-nmd-3]], đồng thời sử dụng IRS có chọn lọc để kiểm soát rủi ro sụt giảm giá trị kinh tế $\Delta\text{EVE}$, ngăn chặn nguy cơ vi phạm ngưỡng ngoại lai 15% Vốn cấp 1 [[src-bcbs-irrbb-2016#^irrbb-p12-1]] [[src-choudhry-principles-banking#^choudhry-irrbb-3]].

---

## Bằng chứng ủng hộ

- **Fidelio Tata (2025)**: Thiết lập nền tảng giải tích của Replicating Portfolio Model nhằm tối ưu hóa biên lãi thuần [[src-tata-bank-alm#^tata-nmd-3]], công thức Duration Gap lượng hóa biến động vốn [[src-tata-bank-alm#^tata-dgap-1]], và cơ chế định giá lại tại Reset Date triệt tiêu rủi ro giá trị kinh tế của chân thả nổi IRS [[src-tata-bank-alm#^tata-gap-2]] [[src-tata-bank-alm#^tata-nii-15]].
- **Basel Committee on Banking Supervision (BCBS d368)**: Hướng dẫn kỹ thuật mô hình hóa sản phẩm phi kỳ hạn (footnote 38 Annex 1) [[src-bcbs-irrbb-2016#^irrbb-u06-6]] và thiết lập hệ thống trần Table 2 khống chế tỷ lệ Core và kỳ hạn bình quân nhằm bảo vệ tính thận trọng giám sát [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
- **Moorad Choudhry**: Khẳng định sự ưu việt của kỹ thuật phòng hộ động (*dynamic hedging*) bằng IRS thay vì dùng các công cụ swaptions đắt đỏ [[src-choudhry-principles-banking#^choudhry-irrbb-8]], đồng thời xác lập vai trò trung tâm của FTP trong việc chuyển giao rủi ro lãi suất từ mạng lưới về Treasury [[src-choudhry-principles-banking#^choudhry-ftp-1]].
- **Beata Lubinska**: Nhấn mạnh tầm quan trọng của Quản trị rủi ro mô hình (Model Risk Management - MRM theo chuẩn SR 11-7) đối với các giả định hành vi khách hàng trong Replicating Portfolio [[src-lubinska-alm-optimisation#^lubinska-u05-13]] [[src-lubinska-alm-optimisation#^lubinska-u05-14]].

---

## Bằng chứng trái chiều

- **Xung đột giữa Tối ưu hóa Thống kê Nội bộ và Trần Giám sát Thận trọng**:
  - Mô hình kinh tế lượng nội bộ dựa trên chuỗi số liệu lịch sử có thể ước tính tỷ lệ tiền gửi lõi Core lên tới 95% và kỳ hạn bình quân kéo dài 7–10 năm.
  - Tuy nhiên, Basel d368 (Table 2) áp đặt trần cứng tối đa **5 năm** cho bán lẻ và **4 năm** cho bán buôn [[src-bcbs-irrbb-2016#^irrbb-u05-4]].
  - *Diễn giải:* Nếu ALM phòng ngừa rủi ro thời lượng theo mô hình nội bộ 7–10 năm (mua receiver swap kỳ hạn dài), khi báo cáo thanh tra giám sát theo chuẩn chuẩn hóa d368, ngân hàng sẽ bị coi là thừa thời lượng nghiêm trọng, làm tăng vọt mức sụt giảm $\Delta\text{EVE}$ dưới kịch bản sốc lãi suất tăng và đối mặt nguy cơ vi phạm ngưỡng ngoại lai 15% Vốn cấp 1 [[src-bcbs-irrbb-2016#^irrbb-p12-1]].

---

## Phụ thuộc regime

- **Môi trường chuyển dịch lãi suất tăng nhanh và đột ngột (Regime Shift)**:
  - Khi lãi suất tăng vọt từ mức thấp lịch sử, giả định bám dính của CASA bị gãy đổ cấu trúc (*structural break*); khách hàng đẩy mạnh chuyển dịch tiền gửi sang kỳ hạn cố định để tìm kiếm lợi suất cao.
  - Nếu Treasury đã thực hiện phòng hộ bằng Receiver Swap quy mô lớn dựa trên giả định CASA dài hạn cũ, ngân hàng sẽ rơi vào trạng thái "Over-hedged": vừa chịu chi phí trả thả nổi của swap tăng vọt, vừa mất số dư CASA chi phí rẻ, gây tổn thất nặng nề cho cả NII và EVE.

---

## Hàm ý ALM / quy định

- **Hàm ý cho ALCO và Treasury**:
  - ALCO bắt buộc phải yêu cầu kiểm định ngược (**Backtesting**) và phân tích độ nhạy (*Sensitivity Stress Testing*) định kỳ hàng quý đối với các tham số mô hình Replicating Portfolio [[src-lubinska-alm-optimisation#^lubinska-u05-15]].

  - Kết hợp linh hoạt giữa phòng hộ bằng phái sinh (IRS) trên thị trường tài chính và phòng hộ tự nhiên (Organic Hedging) thông qua việc điều chỉnh biểu lãi suất huy động và cơ chế FTP thương mại.
- **Quy định pháp lý tại Việt Nam**:
  - *Chưa có nguồn quy định NHNN trong wiki*: Hiện tại wiki chưa ingest văn bản pháp quy của NHNN quy định về tiêu chuẩn kiểm định mô hình sao chép tiền gửi CASA và điều kiện phòng ngừa rủi ro lãi suất sổ ngân hàng bằng IRS.
  - Chuẩn mực pháp lý chính thức dự kiến là **Thông tư 83/2025/TT-NHNN** (có hiệu lực từ 01/07/2026), trong đó quy định thẩm quyền quản trị IRRBB tại Chương 3 Mục 7 (`C3-M7`), quản lý rủi ro mô hình tại Mục 8 (`C3-M8`) và hướng dẫn kỹ thuật tại Phụ lục 5 (`PL5`).
  - *Diễn giải:* Tại Việt Nam, thị trường hoán đổi lãi suất IRS liên ngân hàng bằng VND có thanh khoản tập trung chủ yếu ở kỳ hạn ngắn ($\le 5$ năm). Ngân hàng cần tuân thủ các quy định về tỷ lệ an toàn và hạn mức phái sinh của NHNN trước khi triển khai các cấu trúc phòng hộ phức tạp.

---

## Bất định

- Quy định cụ thể của NHNN về các trần tham số bám dính CASA và điều kiện kế toán phòng ngừa rủi ro (Hedge Accounting) cho các giao dịch IRS sổ ngân hàng tại Việt Nam hiện `[cần nguồn]` (chờ ingest `src-tt83-2025-nhnn` unit `C3-M7`, `C3-M8` và `PL5`).
- Mức độ thanh khoản thực tế và rủi ro cơ sở (Basis Risk) giữa lãi suất thả nổi liên ngân hàng (VND O/N, 1M, 3M) và lãi suất huy động bán lẻ tại thị trường Việt Nam.

---

## Liên Kết Quan Hệ
- **Đầu vào từ**: [[non-maturity-deposits]], [[behavioural-options]], [[repricing-balance-sheet]]
- **Mô hình định lượng**: [[replicating-portfolio-model]], [[duration-gap-model]], [[key-rate-duration]]
- **Công cụ phòng ngừa**: [[interest-rate-swap]], [[swaption]], [[interest-rate-cap-floor]]
- **Truyền dẫn & Quản trị**: [[ftp-curve-construction-methodology]], [[ftp-pricing-methodology]], [[irrbb-alm-governance-strategy-and-tradeoffs]]
- **Chuẩn mực giám sát**: [[bcbs-irrbb]], [[outlier-bank-test]]
- **Nguồn trích dẫn**: [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]], [[src-choudhry-principles-banking]], [[src-lubinska-alm-optimisation]]
