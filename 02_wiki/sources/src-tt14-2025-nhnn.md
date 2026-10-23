---
title: "Thông tư 14/2025/TT-NHNN — Tỷ lệ an toàn vốn đối với NHTM, CN NHNNg"
aliases: []
type: source
source_id: src-tt14-2025-nhnn
domains: [vn-reg, basel, alm]
status: active
maturity: draft
tier: T1
doc_status: final
issuer: SBV
published: 2025-06-30
effective: 2025-09-15
raw: 01_sources/alm/TT14_2025_SBV/14_2025_TT-NHNN.md
units_done: [preamble, C1, C4, C5, PL1, PL3]
updated: 2026-10-23
---

## Thông tin nguồn
- Issuer: Ngân hàng Nhà nước Việt Nam (NHNN), Thống đốc ban hành; số 14/2025/TT-NHNN, ký ngày 30/06/2025.
- Tier T1, `doc_status: final`.
- Hiệu lực: 15/09/2025 (Đ82). Ngân hàng bắt buộc áp dụng từ 01/01/2030, trừ Chương III (Đ7.1). Từ 01/01/2030 bãi bỏ TT41/2016, khoản 2 Điều 1 TT26/2022 và TT22/2023 (theo `notes` trong registry, Đ82 chưa ingest).
- Raw: `01_sources/alm/TT14_2025_SBV/14_2025_TT-NHNN.md` (4.218 dòng); bản gốc pdf và docx cùng thư mục.
- Conversion: ok (xem `03_meta/sources.yaml`).
- Node regulation tương ứng: [[tt14-2025]].
- Đã ingest 6/27 unit: preamble, C1 (Điều 1–7), C4 (Điều 70–72), C5 (Điều 73–74), PL1 (Phụ lục I: cấu phần vốn tự có), PL3 (Phụ lục III: chỉ số kinh doanh).

## Tóm tắt
- C1 là Chương I (Điều 1–7): phạm vi, định nghĩa, quản lý tỷ lệ an toàn vốn, dữ liệu và công nghệ thông tin, ba tỷ lệ an toàn vốn, vốn tự có, lộ trình áp dụng.
- Ba tỷ lệ (vốn lõi cấp 1, vốn cấp 1, an toàn vốn) có chung mẫu số RWA + 12,5 × (K_OR + K_MR); mức tối thiểu 4,5%, 6%, 8%.
- Bộ đệm bảo toàn vốn (CCB) tăng dần 0,625% → 2,5% trong 4 năm; bộ đệm phản chu kỳ (CCyB) 0%–2,5% do Thống đốc quyết định.
- Ngân hàng bắt buộc áp dụng từ 01/01/2030, trừ phương pháp xếp hạng nội bộ (IRB); được đăng ký áp dụng sớm phương pháp tiêu chuẩn hoặc IRB.
- Đ2 định nghĩa sổ ngân hàng, sổ kinh doanh, rủi ro thị trường và tham số IRB (PD, LGD, EAD, M).
- C4 (Đ70–72): K_OR = BIC × ILM; BIC theo ba nhóm hệ số biên 12% / 15% / 18% (ngưỡng 600 và 18.000 tỷ đồng); ILM = 1 khi BI ≤ 600 tỷ đồng hoặc chuỗi tổn thất dưới 05 năm; LC = 15 lần tổn thất ròng bình quân năm; ngưỡng thu thập tổn thất 12 triệu đồng.
- C5 (Đ73–74): quy định nội bộ về sổ kinh doanh và sổ ngân hàng, quy tắc chuyển sổ một chiều (chỉ từ sổ kinh doanh sang sổ ngân hàng), K_MR = K_IRR + K_ER + K_FXR + K_CMR + K_OPT, ngưỡng 2% vốn tự có cho K_FXR và K_OPT.
- PL1 (Phụ lục I): vốn tự có C = A + B; vốn lõi cấp 1 = A11 − A12 (10 khoản cộng, 8 khoản trừ); vốn bổ sung vốn cấp 1 theo 13 điều kiện (trigger 5,125%); vốn cấp 2 gồm nợ thứ cấp (khấu trừ 20% mỗi năm trong 05 năm cuối), 80% dự phòng chung (trần 1,25%), dự phòng vượt EL của IRB (trần 0,6%); khác biệt hợp nhất và chi nhánh ngân hàng nước ngoài.
- PL3 (Phụ lục III): ILDC = min(|thu nhập lãi − chi phí lãi|; 2,25% × tài sản tạo lãi) + thu nhập góp vốn; SC = max + max; FC = tổng ba giá trị tuyệt đối; bốn khoản loại trừ khỏi BI; cách lấy trung bình 3 năm; ví dụ khung thời gian LC theo số quý (38 và 20 quý). Ví dụ ILDC ghi "2,25 lần" trong khi công thức ghi 2,25%.
- Cách tính từng cấu phần K_MR nằm ở Phụ lục IV; chưa ingest.

## Key claims

### preamble — Phần mở đầu

- Thông tư số 14/2025/TT-NHNN ngày 30/06/2025 của NHNN quy định tỷ lệ an toàn vốn đối với ngân hàng thương mại, chi nhánh ngân hàng nước ngoài.
  > "Số: 14/2025/TT-NHNN"
  > "Hà Nội, ngày 30 tháng 6 năm 2025"
  > "QUY ĐỊNH TỶ LỆ AN TOÀN VỐN ĐỐI VỚI NGÂN HÀNG THƯƠNG MẠI, CHI NHÁNH NGÂN HÀNG NƯỚC NGOÀI"
  > — Phần mở đầu ^pre-1

### C1 — Quy định chung (Đ1–7)

#### Đ1 — Phạm vi và đối tượng

- Thông tư quy định tỷ lệ an toàn vốn đối với ngân hàng thương mại và chi nhánh ngân hàng nước ngoài (gọi chung là ngân hàng).
  > "1. Thông tư này quy định tỷ lệ an toàn vốn đối với ngân hàng thương mại, chi nhánh ngân hàng nước ngoài."
  > "2. Đối tượng áp dụng bao gồm ngân hàng thương mại, chi nhánh ngân hàng nước ngoài (sau đây viết tắt là ngân hàng)."
  > — Đ1.1–2 ^d1-1

- Thông tư không áp dụng cho ngân hàng thương mại được kiểm soát đặc biệt và ngân hàng thương mại được can thiệp sớm thực hiện lộ trình tuân thủ tỷ lệ an toàn vốn theo văn bản chấp thuận của NHNN.
  > "3. Thông tư này không áp dụng đối với các ngân hàng thương mại sau đây:"
  > "a) Ngân hàng thương mại được kiểm soát đặc biệt;"
  > "b) Ngân hàng thương mại được can thiệp sớm thực hiện lộ trình tuân thủ tỷ lệ an toàn vốn theo văn bản chấp thuận của Ngân hàng Nhà nước Việt Nam (sau đây viết tắt là Ngân hàng Nhà nước) quy định tại điểm a khoản 1 Điều 159 Luật Các tổ chức tín dụng."
  > — Đ1.3 ^d1-3

#### Đ2 — Giải thích từ ngữ

- Nợ thứ cấp là khoản nợ mà chủ nợ đồng ý nhận thanh toán sau các nghĩa vụ, chủ nợ có bảo đảm và không bảo đảm khác khi đơn vị vay nợ bị phá sản, giải thể.
  > "5. Nợ thứ cấp là khoản nợ mà chủ nợ đồng ý thỏa thuận nhận thanh toán sau các nghĩa vụ, chủ nợ có bảo đảm và không bảo đảm khác khi đơn vị vay nợ bị phá sản, giải thể."
  > — Đ2.5 ^d2-5

- Repo là giao dịch bán và chuyển giao quyền sở hữu tài sản tài chính kèm cam kết mua lại sau thời gian xác định với giá xác định. Reverse repo là giao dịch ngược lại, gồm cả giao dịch mua có kỳ hạn công cụ chuyển nhượng, giấy tờ có giá khác theo quy định của NHNN về hoạt động chiết khấu.
  > "9. Giao dịch mua lại (Repurchase Agreement - Repo) là giao dịch trong đó một bên bán và chuyển giao quyền sở hữu tài sản tài chính cho một bên khác, đồng thời cam kết sẽ mua lại và nhận lại quyền sở hữu tài sản tài chính đó sau một thời gian xác định với một mức giá xác định."
  > "10. Giao dịch mua lại đảo ngược (Reverse Repo) là giao dịch trong đó một bên mua và nhận chuyển giao quyền sở hữu tài sản tài chính từ một bên khác, đồng thời cam kết sẽ bán lại và chuyển giao quyền sở hữu tài sản tài chính đó sau một thời gian xác định với một mức giá xác định, bao gồm cả giao dịch mua có kỳ hạn công cụ chuyển nhượng, giấy tờ có giá khác theo quy định của Ngân hàng Nhà nước về hoạt động chiết khấu công cụ chuyển nhượng, giấy tờ có giá khác."
  > — Đ2.9–10 ^d2-9

- Công cụ bổ sung vốn cấp 1 là công cụ tài chính do ngân hàng thương mại phát hành đáp ứng đầy đủ các điều kiện tại Phụ lục I.
  > "17. Công cụ bổ sung vốn cấp 1 là công cụ tài chính do ngân hàng thương mại phát hành đáp ứng đầy đủ các điều kiện tại Phụ lục I kèm theo Thông tư này."
  > — Đ2.17 ^d2-17

- Rủi ro tín dụng gồm rủi ro tín dụng khách hàng (khách hàng không thực hiện hoặc không có khả năng thực hiện nghĩa vụ trả nợ theo hợp đồng hoặc thỏa thuận) và rủi ro tín dụng đối tác (đối tác không thực hiện hoặc không có khả năng thực hiện nghĩa vụ thanh toán của các giao dịch quy định tại Đ8.4).
  > "18. Rủi ro tín dụng bao gồm:"
  > "a) Rủi ro tín dụng khách hàng là rủi ro do khách hàng không thực hiện hoặc không có khả năng thực hiện một phần hoặc toàn bộ nghĩa vụ trả nợ theo hợp đồng hoặc thỏa thuận với ngân hàng;"
  > "b) Rủi ro tín dụng đối tác là rủi ro do đối tác không thực hiện hoặc không có khả năng thực hiện một phần hoặc toàn bộ nghĩa vụ thanh toán trước hoặc khi đến hạn của các giao dịch quy định tại khoản 4 Điều 8 Thông tư này."
  > — Đ2.18 ^d2-18

- Rủi ro thị trường là rủi ro do biến động bất lợi của lãi suất, tỷ giá, giá vàng, giá chứng khoán và giá hàng hoá trên thị trường.
  > "19. Rủi ro thị trường là rủi ro do biến động bất lợi của lãi suất, tỷ giá, giá vàng, giá chứng khoán và giá hàng hoá trên thị trường. Rủi ro thị trường bao gồm:"
  > — Đ2.19 ^d2-19

- Rủi ro lãi suất trong rủi ro thị trường là rủi ro do biến động bất lợi của lãi suất thị trường đối với giá trị của giấy tờ có giá, công cụ tài chính có lãi suất, sản phẩm phái sinh lãi suất trên sổ kinh doanh.
  > "a) Rủi ro lãi suất là rủi ro do biến động bất lợi của lãi suất trên thị trường đối với giá trị của giấy tờ có giá, công cụ tài chính có lãi suất, sản phẩm phái sinh lãi suất trên sổ kinh doanh của ngân hàng;"
  > — Đ2.19a ^d2-19a

- Rủi ro hoạt động là rủi ro do quy trình nội bộ không đầy đủ hoặc có sai sót, do con người, do lỗi hoặc sự cố hệ thống, hoặc do yếu tố bên ngoài gây tổn thất tài chính hoặc tác động tiêu cực phi tài chính (gồm rủi ro pháp lý); không gồm rủi ro danh tiếng và rủi ro chiến lược.
  > "20. Rủi ro hoạt động là rủi ro do các quy trình nội bộ quy định không đầy đủ hoặc có sai sót, do con người, do các lỗi, sự cố của hệ thống hoặc do các yếu tố bên ngoài làm tổn thất về tài chính, tác động tiêu cực phi tài chính đối với ngân hàng (bao gồm cả rủi ro pháp lý). Rủi ro hoạt động không bao gồm:"
  > "a) Rủi ro danh tiếng;"
  > "b) Rủi ro chiến lược."
  > — Đ2.20 ^d2-20

- Giao dịch tự doanh là giao dịch mua, bán, trao đổi do ngân hàng hoặc công ty con của ngân hàng thương mại thực hiện trong thời hạn không quá 01 năm để thu lợi từ chênh lệch giá thị trường đối với các công cụ tài chính.
  > "23. Giao dịch tự doanh là giao dịch mua, bán, trao đổi do ngân hàng, công ty con của ngân hàng thương mại thực hiện theo quy định của pháp luật trong thời hạn không quá 01 năm để thu lợi từ chênh lệch giá thị trường cho ngân hàng đối với các công cụ tài chính, bao gồm:"
  > — Đ2.23 ^d2-23

- Sổ kinh doanh ghi nhận trạng thái của giao dịch tự doanh; giao dịch để bảo lãnh phát hành công cụ tài chính; giao dịch phái sinh phòng ngừa rủi ro cho giao dịch tự doanh; giao dịch mua bán ngoại tệ, tài sản tài chính phục vụ khách hàng, đối tác và giao dịch đối ứng.
  > "24. Sổ kinh doanh là danh mục ghi nhận các trạng thái của:"
  > "a) Giao dịch tự doanh;"
  > "b) Giao dịch để thực hiện nghiệp vụ bảo lãnh phát hành công cụ tài chính;"
  > "c) Giao dịch sản phẩm phái sinh để phòng ngừa rủi ro của các giao dịch tự doanh của ngân hàng;"
  > "d) Giao dịch mua bán ngoại tệ, tài sản tài chính để phục vụ nhu cầu của khách hàng, đối tác và các giao dịch để đối ứng với các giao dịch này."
  > — Đ2.24 ^d2-24

- Sổ ngân hàng ghi nhận trạng thái của repo và reverse repo; phái sinh phòng ngừa cho khoản mục của Báo cáo tình hình tài chính (kể cả ngoại bảng) trừ giao dịch đã vào sổ kinh doanh; mua bán tài sản tài chính để dự trữ khả năng thanh khoản; mọi giao dịch còn lại không thuộc sổ kinh doanh.
  > "25. Sổ ngân hàng là danh mục ghi nhận trạng thái của:"
  > "a) Giao dịch mua lại và giao dịch mua lại đảo ngược;"
  > "b) Giao dịch sản phẩm phái sinh để phòng ngừa rủi ro cho các khoản mục của Báo cáo tình hình tài chính (bao gồm cả các khoản mục ngoại bảng) của ngân hàng, trừ các giao dịch đã phân loại vào sổ kinh doanh của ngân hàng quy định tại điểm a và điểm c khoản 24 Điều này;"
  > "c) Giao dịch mua bán tài sản tài chính với mục đích dự trữ khả năng thanh khoản;"
  > "d) Các giao dịch còn lại không thuộc sổ kinh doanh của ngân hàng."
  > — Đ2.25 ^d2-25

- Phương pháp tiêu chuẩn cho rủi ro tín dụng tính tài sản có rủi ro tín dụng theo Chương II; phương pháp xếp hạng nội bộ (IRB) cho rủi ro tín dụng khách hàng theo Chương III, gồm IRB cơ bản và IRB nâng cao.
  > "27. Phương pháp tiêu chuẩn cho rủi ro tín dụng là phương pháp để tính tài sản có rủi ro tín dụng quy định tại Chương II Thông tư này."
  > "28. Phương pháp xếp hạng nội bộ (Internal rating-based approach - IRB) cho rủi ro tín dụng khách hàng là phương pháp để tính tài sản có rủi ro tín dụng khách hàng quy định tại Chương III Thông tư này. Phương pháp xếp hạng nội bộ bao gồm phương pháp xếp hạng nội bộ cơ bản và phương pháp xếp hạng nội bộ nâng cao."
  > — Đ2.27–28 ^d2-27

- Trong IRB cơ bản (FIRB), ngân hàng tự ước tính PD và dùng các tham số rủi ro khác theo Thông tư đối với khoản phải đòi doanh nghiệp và khoản mua lại khoản phải thu doanh nghiệp. Trong IRB nâng cao (AIRB), ngân hàng tự ước tính PD, LGD, EAD đối với khoản phải đòi bán lẻ và khoản mua lại khoản phải thu bán lẻ.
  > "29. Phương pháp xếp hạng nội bộ cơ bản (Foundation internal rating - based approach - FIRB) là phương pháp xếp hạng nội bộ trong đó ngân hàng phải tự đưa ra ước tính về xác suất vỡ nợ (PD). Ngân hàng phải sử dụng các tham số rủi ro liên quan khác theo quy định tại Thông tư này đối với khoản phải đòi doanh nghiệp và khoản mua lại khoản phải thu doanh nghiệp."
  > "30. Phương pháp xếp hạng nội bộ nâng cao (Advanced internal rating-based approach - AIRB) là phương pháp xếp hạng nội bộ trong đó ngân hàng phải tự đưa ra ước tính về xác suất vỡ nợ (PD), tỷ lệ tổn thất khi khách hàng vỡ nợ (LGD), giá trị khoản phải đòi tại thời điểm khách hàng vỡ nợ (EAD) đối với khoản phải đòi bán lẻ và khoản mua lại khoản phải thu bán lẻ."
  > — Đ2.29–30 ^d2-29

- Tham số IRB: EL là phần tổn thất ngân hàng dự kiến sẽ xảy ra; M là thời hạn còn lại của khoản phải đòi dùng để tính tài sản có rủi ro tín dụng khách hàng; LGD là tỷ lệ giữa giá trị tổn thất và EAD; PD là khả năng khách hàng vỡ nợ; EAD là giá trị khoản phải đòi hoặc giá trị dự kiến tại thời điểm khách hàng vỡ nợ, tính bằng đồng Việt Nam.
  > "31. Tổn thất dự kiến (Expected losses - EL) là phần tổn thất mà ngân hàng dự kiến sẽ xảy ra."
  > "32. Thời hạn hiệu lực của khoản phải đòi (Effective Maturity - M) là thời hạn còn lại của khoản phải đòi được dùng để tính tài sản có rủi ro tín dụng khách hàng."
  > "33. Tỷ lệ tổn thất khi khách hàng vỡ nợ (Loss given default - LGD) là tỷ lệ giữa giá trị tổn thất và giá trị khoản phải đòi tại thời điểm khách hàng vỡ nợ. LGD có đơn vị đo lường là số thập phân hoặc phần trăm."
  > "34. Xác suất vỡ nợ (Probability of default - PD) là khả năng khách hàng sẽ vỡ nợ. PD có đơn vị đo lường là số thập phân hoặc phần trăm."
  > "35. Giá trị khoản phải đòi tại thời điểm khách hàng vỡ nợ (Exposure at default - EAD) là giá trị khoản phải đòi hoặc giá trị khoản phải đòi dự kiến tại thời điểm khách hàng vỡ nợ. EAD có đơn vị đo lường là đồng Việt Nam."
  > — Đ2.31–35 ^d2-31

#### Đ3 — Cơ cấu tổ chức và hoạt động quản lý tỷ lệ an toàn vốn

- Hội đồng quản trị, Hội đồng thành viên (ngân hàng thương mại) hoặc Tổng giám đốc (Giám đốc) (chi nhánh ngân hàng nước ngoài) ban hành quy định nội bộ về tuân thủ tỷ lệ an toàn vốn tối thiểu, phù hợp với nhu cầu, đặc điểm, mức độ rủi ro, chu kỳ kinh doanh, khả năng thích ứng với rủi ro và chiến lược kinh doanh; đồng thời giám sát Tổng giám đốc (Giám đốc) (đối với ngân hàng thương mại) trong việc quản lý tỷ lệ an toàn vốn.
  > "a) Hội đồng quản trị, Hội đồng thành viên (đối với ngân hàng thương mại) hoặc Tổng giám đốc (Giám đốc) (đối với chi nhánh ngân hàng nước ngoài) thực hiện:"
  > "(i) Ban hành quy định nội bộ về tuân thủ tỷ lệ an toàn vốn tối thiểu của ngân hàng phù hợp với nhu cầu, đặc điểm, mức độ rủi ro trong hoạt động, chu kỳ kinh doanh, khả năng thích ứng với rủi ro và chiến lược kinh doanh của ngân hàng; phù hợp với Thông tư này và quy định của pháp luật liên quan;"
  > "(ii) Giám sát đối với Tổng giám đốc (Giám đốc) (đối với ngân hàng thương mại) trong việc thực hiện quản lý tỷ lệ an toàn vốn;"
  > — Đ3.1a ^d3-1a

- Tổng giám đốc (Giám đốc) xây dựng và trình ban hành quy định nội bộ, quản lý tỷ lệ an toàn vốn bảo đảm tuân thủ quy định nội bộ, và giám sát các cá nhân, bộ phận thực hiện chức năng quản lý tỷ lệ an toàn vốn.
  > "b) Tổng giám đốc (Giám đốc) thực hiện:"
  > "(i) Xây dựng và trình Hội đồng quản trị, Hội đồng thành viên (đối với ngân hàng thương mại) ban hành quy định nội bộ về tuân thủ tỷ lệ an toàn vốn tối thiểu;"
  > "(ii) Quản lý tỷ lệ an toàn vốn đảm bảo tuân thủ quy định nội bộ;"
  > "(iii) Giám sát đối với các cá nhân, bộ phận thực hiện chức năng quản lý tỷ lệ an toàn vốn;"
  > — Đ3.1b ^d3-1b

- Ngân hàng phải có cá nhân, bộ phận thực hiện chức năng quản lý tỷ lệ an toàn vốn, trình Tổng giám đốc (Giám đốc) để báo cáo Hội đồng quản trị, Hội đồng thành viên theo quy định nội bộ.
  > "c) Có cá nhân, bộ phận thực hiện chức năng quản lý tỷ lệ an toàn vốn, trình Tổng giám đốc (Giám đốc) để báo cáo Hội đồng quản trị, Hội đồng thành viên (đối với ngân hàng thương mại) hoặc trình Tổng giám đốc (Giám đốc) (đối với chi nhánh ngân hàng nước ngoài) theo quy định nội bộ về tuân thủ tỷ lệ an toàn vốn tối thiểu của ngân hàng phù hợp với Thông tư này và quy định của pháp luật liên quan."
  > — Đ3.1c ^d3-1c

- Ban Kiểm soát của ngân hàng thương mại phải giám sát việc chấp hành quy định về tỷ lệ an toàn vốn. Kiểm toán nội bộ rà soát, đánh giá độc lập, khách quan về tính thích hợp và sự tuân thủ quy định nội bộ về quản lý tỷ lệ an toàn vốn.
  > "2. Ban Kiểm soát của ngân hàng thương mại phải giám sát việc chấp hành các quy định về tỷ lệ an toàn vốn tại Thông tư này."
  > "3. Kiểm toán nội bộ của ngân hàng thực hiện rà soát, đánh giá độc lập, khách quan về tính thích hợp và sự tuân thủ quy định nội bộ về quản lý tỷ lệ an toàn vốn của ngân hàng."
  > — Đ3.2–3 ^d3-2

#### Đ4 — Dữ liệu và hệ thống công nghệ thông tin

- Ngân hàng phải có dữ liệu đầy đủ và hệ thống công nghệ thông tin phù hợp để tính tỷ lệ an toàn vốn.
  > "1. Ngân hàng phải có dữ liệu đầy đủ và hệ thống công nghệ thông tin phù hợp để tính tỷ lệ an toàn vốn theo quy định tại Thông tư này."
  > — Đ4.1 ^d4-1

- Yêu cầu tối thiểu về dữ liệu: có cơ cấu tổ chức, quy trình, công cụ bảo đảm chất lượng và tính đầy đủ; có quy trình thu thập, đối chiếu, lưu trữ, truy cập, bổ sung, dự phòng, sao lưu và tiêu hủy dữ liệu; đáp ứng yêu cầu báo cáo, thống kê của NHNN.
  > "2. Ngân hàng phải tổ chức thu thập và quản lý dữ liệu đảm bảo các yêu cầu tối thiểu sau đây:"
  > "a) Có cơ cấu tổ chức, chức năng, nhiệm vụ của các cá nhân, bộ phận; quy trình; công cụ để quản lý dữ liệu đảm bảo các yêu cầu chất lượng và tính đầy đủ của dữ liệu;"
  > "b) Có quy trình thu thập, đối chiếu dữ liệu (nội bộ, bên ngoài), lưu trữ, truy cập, bổ sung, dự phòng, sao lưu và tiêu hủy dữ liệu để tính tỷ lệ an toàn vốn theo quy định tại Thông tư này;"
  > "c) Đáp ứng yêu cầu theo quy định nội bộ của ngân hàng và quy định của Ngân hàng Nhà nước về chế độ báo cáo, thống kê."
  > — Đ4.2 ^d4-2

- Yêu cầu tối thiểu về hệ thống công nghệ thông tin: kết nối, quản lý tập trung toàn hệ thống; có công cụ kết nối với hệ thống khác để tính vốn tự có, tổng tài sản có rủi ro tín dụng, vốn yêu cầu cho từng loại rủi ro và tỷ lệ an toàn vốn; có quy trình rà soát, kiểm tra, dự phòng, xử lý sự cố, bảo trì định kỳ.
  > "3. Hệ thống công nghệ thông tin phải đảm bảo các yêu cầu tối thiểu sau đây:"
  > "a) Kết nối, quản lý tập trung toàn hệ thống, đảm bảo bảo mật, an toàn và hiệu quả khi tính tỷ lệ an toàn vốn theo quy định tại Thông tư này;"
  > "b) Có công cụ được kết nối với các hệ thống khác để tính vốn tự có, tổng tài sản có rủi ro tín dụng, vốn yêu cầu cho từng loại rủi ro và tỷ lệ an toàn vốn đảm bảo chính xác, kịp thời;"
  > "c) Có quy trình rà soát, kiểm tra, dự phòng, xử lý sự cố, bảo trì định kỳ, thường xuyên;"
  > — Đ4.3 ^d4-3

#### Đ5 — Tỷ lệ an toàn vốn

- Công thức tỷ lệ vốn lõi cấp 1: vốn lõi cấp 1 chia cho RWA cộng 12,5 lần tổng K_OR và K_MR.
  > "a) Công thức xác định tỷ lệ vốn lõi cấp 1:"
  > "\text{Tỷ lệ vốn lõi cấp 1} = \frac{\text{Vốn lõi cấp 1}}{RWA + 12,5 \times (K_{OR} + K_{MR})}"
  > — Đ5.1a ^d5-1a

- Công thức tỷ lệ vốn cấp 1: vốn cấp 1 chia cho cùng mẫu số.
  > "b) Công thức xác định tỷ lệ vốn cấp 1:"
  > "\text{Tỷ lệ vốn cấp 1} = \frac{\text{Vốn cấp 1}}{RWA + 12,5 \times (K_{OR} + K_{MR})}"
  > — Đ5.1b ^d5-1b

- Công thức tỷ lệ an toàn vốn: vốn tự có chia cho cùng mẫu số.
  > "c) Công thức xác định tỷ lệ an toàn vốn:"
  > "\text{Tỷ lệ an toàn vốn} = \frac{\text{Vốn tự có}}{RWA + 12,5 \times (K_{OR} + K_{MR})}"
  > — Đ5.1c ^d5-1c

- Vốn lõi cấp 1, vốn cấp 1, vốn tự có theo Phụ lục I. RWA là tổng tài sản có rủi ro tín dụng; K_OR là vốn yêu cầu cho rủi ro hoạt động; K_MR là vốn yêu cầu cho rủi ro thị trường.
  > "Trong đó:"
  > "Vốn lõi cấp 1, vốn cấp 1, vốn tự có theo quy định tại Phụ lục I kèm theo Thông tư này;"
  > "RWA: Tổng tài sản có rủi ro tín dụng (Risk weighted assets);"
  > "K<sub>OR</sub>: Vốn yêu cầu cho rủi ro hoạt động (Operational risk capital requirements);"
  > "K<sub>MR</sub>: Vốn yêu cầu cho rủi ro thị trường (Market risk capital requirements)."
  > — Đ5.1 ^d5-1d

- Ngân hàng thương mại không có công ty con và chi nhánh ngân hàng nước ngoài phải duy trì tỷ lệ riêng lẻ; ngân hàng thương mại có công ty con phải duy trì cả tỷ lệ riêng lẻ và hợp nhất.
  > "a) Ngân hàng thương mại không có công ty con, chi nhánh ngân hàng nước ngoài phải duy trì tỷ lệ an toàn vốn riêng lẻ;"
  > "b) Ngân hàng thương mại có công ty con phải duy trì tỷ lệ an toàn vốn riêng lẻ và tỷ lệ an toàn vốn hợp nhất;"
  > — Đ5.2ab ^d5-2ab

- Khi tính tỷ lệ hợp nhất: không hợp nhất công ty con hoạt động theo Luật Kinh doanh bảo hiểm; RWA, K_OR, K_MR tính trên số liệu của ngân hàng thương mại và công ty con; ngân hàng thương mại phải dùng phương pháp tiêu chuẩn để tính tài sản có rủi ro tín dụng của công ty con.
  > "c) Khi tính tỷ lệ an toàn vốn hợp nhất:"
  > "(i) Trường hợp ngân hàng thương mại có công ty con là doanh nghiệp hoạt động theo Luật Kinh doanh bảo hiểm, ngân hàng thương mại không hợp nhất công ty con này theo nguyên tắc hợp nhất của pháp luật về kế toán và báo cáo tài chính đối với tổ chức tín dụng;"
  > "Trong đó, ngân hàng thương mại phải áp dụng phương pháp tiêu chuẩn để tính tài sản có rủi ro tín dụng của công ty con."
  > — Đ5.2c ^d5-2c

- Ngân hàng thương mại không có công ty con và chi nhánh ngân hàng nước ngoài phải duy trì tỷ lệ riêng lẻ tối thiểu: vốn lõi cấp 1 4,5%, vốn cấp 1 6%, an toàn vốn 8%.
  > "3. Ngân hàng thương mại không có công ty con, chi nhánh ngân hàng nước ngoài phải duy trì các tỷ lệ an toàn vốn riêng lẻ sau đây:"
  > "a) Tỷ lệ vốn lõi cấp 1 tối thiểu là 4,5%;"
  > "b) Tỷ lệ vốn cấp 1 tối thiểu là 6%;"
  > "c) Tỷ lệ an toàn vốn tối thiểu là 8%."
  > — Đ5.3 ^d5-3

- Ngân hàng thương mại có công ty con phải duy trì tỷ lệ riêng lẻ và hợp nhất với cùng mức tối thiểu: 4,5%, 6%, 8%.
  > "4. Ngân hàng thương mại có công ty con phải duy trì tỷ lệ an toàn vốn riêng lẻ và tỷ lệ an toàn vốn hợp nhất sau đây:"
  > "a) Tỷ lệ vốn lõi cấp 1 tối thiểu là 4,5%;"
  > "b) Tỷ lệ vốn cấp 1 tối thiểu là 6%;"
  > "c) Tỷ lệ an toàn vốn tối thiểu là 8%."
  > — Đ5.4 ^d5-4

- Tỷ lệ bộ đệm bảo toàn vốn (CCB) là phần tỷ lệ vốn lõi cấp 1 còn lại sau khi ngân hàng đáp ứng đầy đủ các tỷ lệ an toàn vốn (vốn lõi cấp 1, vốn cấp 1, an toàn vốn). Ngân hàng thực hiện CCB ngoài các tỷ lệ bắt buộc tại Đ5.3 và Đ5.4.
  > "5. Ngoài các tỷ lệ bắt buộc phải thực hiện theo quy định tại khoản 3 và khoản 4 Điều này, ngân hàng thực hiện tỷ lệ bộ đệm bảo toàn vốn (Capital conservation buffer - CCB) theo quy định như sau:"
  > "a) Tỷ lệ bộ đệm bảo toàn vốn (CCB) là phần tỷ lệ vốn lõi cấp 1 còn lại sau khi ngân hàng đáp ứng đầy đủ các tỷ lệ an toàn vốn (bao gồm tỷ lệ vốn lõi cấp 1, tỷ lệ vốn cấp 1 và tỷ lệ an toàn vốn);"
  > — Đ5.5a ^d5-5a

- Ngân hàng chỉ được phân chia phần lợi nhuận còn lại do ngân hàng tự quyết định bằng tiền mặt khi duy trì việc đáp ứng toàn bộ các tỷ lệ theo bảng dưới (tính từ năm thứ nhất).
  > "b) Ngân hàng chỉ được phân chia phần lợi nhuận còn lại do ngân hàng tự quyết định theo quy định của pháp luật về chế độ tài chính bằng tiền mặt khi duy trì việc đáp ứng toàn bộ các tỷ lệ theo các năm như sau:"
  >
  > | Tỷ lệ | Năm thứ nhất | Năm thứ hai | Năm thứ ba | Năm thứ tư trở đi |
  > |---|---|---|---|---|
  > | CCB | 0,625% | 1,25% | 1,875% | 2,5% |
  > | Vốn lõi cấp 1 (bao gồm CCB) | 5,125% | 5,75% | 6,375% | 7% |
  > | Vốn cấp 1 (bao gồm CCB) | 6,625% | 7,25% | 7,875% | 8,5% |
  > | CAR (bao gồm CCB) | 8,625% | 9,25% | 9,875% | 10,5% |
  >
  > — Đ5.5b, Bảng 1 ^d5-5b

- Năm thứ nhất của bảng CCB là năm ngân hàng bắt đầu áp dụng phương pháp tiêu chuẩn đã đăng ký, năm ngân hàng được NHNN chấp thuận áp dụng IRB, hoặc năm 2030 đối với các trường hợp còn lại.
  > "Trong đó năm thứ nhất:"
  > "(i) Là năm ngân hàng bắt đầu áp dụng phương pháp tiêu chuẩn đã đăng ký theo quy định tại điểm b khoản 2 Điều 7 Thông tư này;"
  > "(ii) Là năm ngân hàng được Ngân hàng Nhà nước chấp thuận áp dụng phương pháp xếp hạng nội bộ quy định tại điểm c khoản 3 Điều 7 Thông tư này;"
  > "(iii) Là năm 2030 đối với các trường hợp còn lại."
  > — Đ5.5b ^d5-5c

- Tỷ lệ bộ đệm vốn phản chu kỳ (CCyB) là phần tỷ lệ vốn lõi cấp 1 còn lại sau khi ngân hàng đáp ứng đầy đủ các tỷ lệ an toàn vốn và CCB (nếu có). Thống đốc NHNN quyết định tỷ lệ CCyB cụ thể trong khoảng từ 0% đến 2,5% khi cần thiết trong từng thời kỳ.
  > "a) Tỷ lệ bộ đệm vốn phản chu kỳ là phần tỷ lệ vốn lõi cấp 1 còn lại sau khi ngân hàng đáp ứng đầy đủ các tỷ lệ an toàn vốn (bao gồm tỷ lệ vốn lõi cấp 1, tỷ lệ vốn cấp 1, tỷ lệ an toàn vốn và CCB (nếu có));"
  > "b) Thống đốc Ngân hàng Nhà nước quyết định áp dụng tỷ lệ CCyB cụ thể trong khoảng từ 0% đến 2,5% khi cần thiết trong từng thời kỳ."
  > — Đ5.6 ^d5-6

- Với khoản mục bằng ngoại tệ và vàng, ngân hàng quy đổi sang đồng Việt Nam khi tính tỷ lệ an toàn vốn. Ngày báo cáo không phải ngày làm việc thì dùng tỷ giá và giá vàng của ngày làm việc liền trước.
  > "7. Đối với các khoản mục bằng ngoại tệ và vàng, ngân hàng quy đổi sang đồng Việt Nam khi tính tỷ lệ an toàn vốn như sau:"
  > "d) Trường hợp ngày báo cáo không phải là ngày làm việc, ngân hàng áp dụng tỷ giá và giá vàng của ngày làm việc liền trước."
  > — Đ5.7 ^d5-7

- NHNN có thể căn cứ kết quả thanh tra, kiểm tra, giám sát để yêu cầu ngân hàng duy trì tỷ lệ an toàn vốn cao hơn mức quy định, và quyết định áp tỷ lệ bộ đệm vốn đối với ngân hàng thương mại có tầm quan trọng hệ thống trong từng thời kỳ.
  > "8. Căn cứ kết quả thanh tra, kiểm tra, giám sát đối với ngân hàng, trong trường hợp cần thiết để bảo đảm an toàn trong hoạt động của ngân hàng, tùy theo tính chất, mức độ rủi ro, Ngân hàng Nhà nước xem xét:"
  > "a) Yêu cầu ngân hàng duy trì tỷ lệ an toàn vốn cao hơn so với mức quy định tại Thông tư này;"
  > "b) Quyết định áp dụng tỷ lệ bộ đệm vốn đối với ngân hàng thương mại có tầm quan trọng hệ thống trong từng thời kỳ."
  > — Đ5.8 ^d5-8

#### Đ6 — Vốn tự có

- Vốn tự có là cơ sở để tính tỷ lệ an toàn vốn; gồm tổng vốn cấp 1 (vốn lõi cấp 1 và vốn bổ sung vốn cấp 1) và vốn cấp 2 theo Phụ lục I.
  > "1. Vốn tự có của ngân hàng là cơ sở để tính tỷ lệ an toàn vốn theo quy định tại Thông tư này."
  > "2. Vốn tự có bao gồm tổng vốn cấp 1 (bao gồm cả vốn lõi cấp 1 và vốn bổ sung vốn cấp 1) và vốn cấp 2 quy định tại Phụ lục I kèm theo Thông tư này."
  > — Đ6.1–2 ^d6-1

#### Đ7 — Áp dụng quy định về tỷ lệ an toàn vốn

- Kể từ 01/01/2030, ngân hàng phải áp dụng Thông tư, trừ quy định tại Chương III (IRB).
  > "1. Kể từ ngày 01 tháng 01 năm 2030, ngân hàng phải áp dụng quy định tại Thông tư này, trừ quy định tại Chương III Thông tư này."
  > — Đ7.1 ^d7-1

- Ngân hàng có khả năng thực hiện phương pháp tiêu chuẩn trước 01/01/2030 được gửi văn bản đăng ký cho NHNN, nêu thời điểm bắt đầu áp dụng và kèm báo cáo của Hội đồng quản trị, Hội đồng thành viên hoặc Tổng Giám đốc (Giám đốc) đánh giá việc tuân thủ.
  > "a) Kể từ ngày Thông tư này có hiệu lực, ngân hàng có khả năng thực hiện phương pháp tiêu chuẩn cho rủi ro tín dụng quy định tại Chương II Thông tư này trước thời hạn quy định tại khoản 1 Điều này được gửi văn bản đăng ký áp dụng cho Ngân hàng Nhà nước, trong đó đăng ký thời điểm bắt đầu áp dụng phương pháp tiêu chuẩn kèm báo cáo của Hội đồng quản trị, Hội đồng thành viên của ngân hàng thương mại, Tổng Giám đốc (Giám đốc) của chi nhánh ngân hàng nước ngoài đánh giá việc tuân thủ các quy định liên quan đến phương pháp tiêu chuẩn tại Thông tư này;"
  > — Đ7.2a ^d7-2a

- Từ thời điểm bắt đầu áp dụng phương pháp tiêu chuẩn đã đăng ký, ngân hàng phải thực hiện phương pháp tiêu chuẩn và các quy định khác của Thông tư (trừ Chương III) và dừng thực hiện các Thông tư quy định tại điểm a, b, c khoản 3 Điều 82.
  > "b) Ngân hàng phải thực hiện phương pháp tiêu chuẩn cho rủi ro tín dụng và các quy định khác tại Thông tư này, trừ quy định tại Chương III Thông tư này từ thời điểm bắt đầu áp dụng phương pháp tiêu chuẩn đã đăng ký và dừng thực hiện các Thông tư quy định tại điểm a, b và c khoản 3 Điều 82 Thông tư này."
  > — Đ7.2b ^d7-2b

- Ngân hàng có khả năng thực hiện IRB được gửi văn bản đăng ký cho NHNN kèm Kế hoạch triển khai theo Phụ lục VII và thực hiện giai đoạn chuyển đổi theo Điều 32.
  > "a) Kể từ ngày Thông tư này có hiệu lực, ngân hàng có khả năng thực hiện phương pháp xếp hạng nội bộ cho rủi ro tín dụng quy định tại Chương III Thông tư này:"
  > "(i) Được gửi văn bản đăng ký cho Ngân hàng Nhà nước kèm Kế hoạch triển khai áp dụng phương pháp xếp hạng nội bộ theo quy định tại Phụ lục VII kèm theo Thông tư này;"
  > "(ii) Thực hiện quy định về giai đoạn chuyển đổi sang phương pháp xếp hạng nội bộ tại Điều 32 Thông tư này;"
  > — Đ7.3a ^d7-3a

- Ngân hàng được đề nghị NHNN chấp thuận áp dụng IRB (Đ33) khi đáp ứng cả hai điều kiện: tối thiểu 02 năm kể từ ngày gửi văn bản đăng ký; và có 02 năm liên tục liền kề trước thời điểm nộp hồ sơ được tổ chức kiểm toán độc lập và Hội đồng quản trị, Hội đồng thành viên hoặc Tổng Giám đốc (Giám đốc) đánh giá đã tuân thủ các yêu cầu IRB.
  > "b) Ngân hàng được đề nghị Ngân hàng Nhà nước chấp thuận áp dụng phương pháp xếp hạng nội bộ theo quy định tại Điều 33 Thông tư này khi đáp ứng đầy đủ các điều kiện sau:"
  > "(i) Sau thời gian tối thiểu 02 năm kể từ ngày ngân hàng có văn bản đăng ký gửi Ngân hàng Nhà nước nêu tại điểm a(i) khoản này;"
  > "(ii) Có 02 năm liên tục liền kề trước thời điểm nộp hồ sơ đề nghị Ngân hàng Nhà nước chấp thuận được tổ chức kiểm toán độc lập và Hội đồng quản trị, Hội đồng thành viên của ngân hàng thương mại, Tổng Giám đốc (Giám đốc) của chi nhánh ngân hàng nước ngoài đánh giá đã tuân thủ các yêu cầu liên quan đến phương pháp xếp hạng nội bộ theo quy định tại Thông tư này (bao gồm cả hệ thống xếp hạng tín dụng nội bộ, hệ thống, công cụ tính vốn phục vụ phương pháp xếp hạng nội bộ, tỷ lệ bao phủ, tỷ lệ sàn đầu ra) phù hợp với phạm vi đề nghị chấp thuận;"
  > — Đ7.3b ^d7-3b

- Kể từ ngày được NHNN chấp thuận, ngân hàng áp dụng chính thức IRB; không phải tuân thủ mức tối thiểu về tỷ lệ an toàn vốn tính theo phương pháp tiêu chuẩn tại Chương II; và dừng thực hiện các Thông tư tại điểm a, b, c khoản 3 Điều 82 nếu được chấp thuận trước 01/01/2030.
  > "c) Kể từ ngày được Ngân hàng Nhà nước chấp thuận, ngân hàng thực hiện như sau:"
  > "(i) Áp dụng chính thức phương pháp xếp hạng nội bộ để tính tài sản có rủi ro tín dụng và các quy định khác tại Thông tư này;"
  > "(ii) Không phải tuân thủ mức tối thiểu về tỷ lệ an toàn vốn được tính theo phương pháp tiêu chuẩn quy định tại Chương II Thông tư này;"
  > "(iii) Dừng thực hiện các Thông tư quy định tại điểm a, b và c khoản 3 Điều 82 Thông tư này trong trường hợp ngân hàng được Ngân hàng Nhà nước chấp thuận trước ngày 01 tháng 01 năm 2030."
  > — Đ7.3c ^d7-3c

### C4 — Vốn yêu cầu cho rủi ro hoạt động (Đ70–72)

#### Đ70 — Vốn yêu cầu cho rủi ro hoạt động

- Vốn yêu cầu cho rủi ro hoạt động (K_OR) bằng BIC nhân ILM; BIC là cấu phần chỉ số kinh doanh, ILM là hệ số tổn thất nội bộ.
  > "1. Vốn yêu cầu cho rủi ro hoạt động (K<sub>OR</sub>) được xác định bằng công thức:"
  > "K<sub>OR</sub> = BIC x ILM"
  > "BIC: Cấu phần chỉ số kinh doanh (Business indicator component);"
  > "ILM: Hệ số tổn thất nội bộ (Internal loss multiplier)."
  > — Đ70.1 ^d70-1

- BIC bằng tổng của BI theo từng nhóm nhân hệ số biên α của nhóm đó, với ba nhóm.
  > "2. Cấu phần chỉ số kinh doanh (BIC) được xác định theo công thức sau:"
  > "BIC = \sum_{i=1}^{3} BI_{i} \times \alpha_{i}"
  > — Đ70.2 ^d70-2

- Phân nhóm BI và hệ số biên α: nhóm 1 BI ≤ 600 tỷ đồng, α 12%; nhóm 2 từ trên 600 đến 18.000 tỷ đồng, α 15%; nhóm 3 trên 18.000 tỷ đồng, α 18%.
  > "a) Việc phân nhóm chỉ số kinh doanh và xác định hệ số biên (α<sub>i</sub>) được xác định theo bảng sau:"
  >
  > | Nhóm (i) | Khoảng giá trị (tỷ đồng) | Hệ số biên α<sub>i</sub> (%) |
  > |---|---|---|
  > | 1 | ≤ 600 | 12 |
  > | 2 | 600 < BI ≤ 18000 | 15 |
  > | 3 | >18000 | 18 |
  >
  > — Đ70.2a, Bảng 17 ^d70-2a

- Ví dụ của nguồn: BI là 20.000 tỷ đồng thì BIC = 600×12% + (18.000−600)×15% + (20.000−18.000)×18% = 3.042 tỷ đồng.
  > "Ví dụ: BI có giá trị là 20.000 tỷ đồng, thì BIC = 600×12% + (18.000-600)×15% + (20.000-18.000)×18% = 3.042 tỷ đồng;"
  > — Đ70.2a ^d70-2a-vd

- Chỉ số kinh doanh BI bằng ILDC cộng SC cộng FC: cấu phần lãi, cấu phần dịch vụ, cấu phần tài chính.
  > "BI = ILDC + SC + FC"
  > "BI: Chỉ số kinh doanh (Business indicator);"
  > "ILDC: Cấu phần lãi (Interest, leases and dividend component);"
  > "SC: Cấu phần dịch vụ (Services component);"
  > "FC: Cấu phần tài chính (Financial component)."
  > — Đ70.2b(i) ^d70-2b

- ILDC, SC, FC là giá trị trung bình của 03 năm tính đến thời điểm tính vốn yêu cầu cho rủi ro hoạt động, của các cấu phần chi tiết theo Phụ lục III.
  > "(ii) Các cấu phần của công thức trên (ILDC, SC, FC) được xác định bằng giá trị trung bình của 03 năm tính đến thời điểm tính vốn yêu cầu cho rủi ro hoạt động của các cấu phần chi tiết theo hướng dẫn tại Phụ lục III kèm theo Thông tư này."
  > — Đ70.2b(ii) ^d70-2b2

- Công thức ILM: logarit tự nhiên của (e − 1 + (LC/BIC) mũ 0,8), trong đó LC là cấu phần tổn thất.
  > "3. Hệ số tổn thất nội bộ (ILM) được xác định như sau:"
  > "ILM = \ln \left( \exp(1) - 1 + \left( \frac{LC}{BIC} \right)^{0,8} \right)"
  > "Trong đó: LC là cấu phần tổn thất (Loss component);"
  > — Đ70.3a ^d70-3a

- ILM bằng 1 khi BI ≤ 600 tỷ đồng, hoặc BI > 600 tỷ đồng và chuỗi dữ liệu tổn thất không đủ độ dài 05 năm.
  > "b) ILM được xác định bằng 1 khi chỉ số kinh doanh của ngân hàng thuộc một trong các điều kiện sau:"
  > "(i) Có BI ≤ 600 tỷ đồng;"
  > "(ii) Có BI > 600 tỷ đồng và có chuỗi dữ liệu tổn thất để đo lường rủi ro hoạt động không đủ độ dài 05 năm;"
  > — Đ70.3b ^d70-3b

- Để tính LC, ngân hàng không thuộc các trường hợp ILM bằng 1, và dữ liệu tổn thất phải đáp ứng Đ71 và Đ72.
  > "c) Để tính cấu phần tổn thất (LC), ngân hàng phải đảm bảo các yêu cầu sau:"
  > "(i) Ngân hàng không thuộc các trường hợp quy định tại điểm b khoản này;"
  > "(iii) Dữ liệu tổn thất hoạt động để tính LC phải đảm bảo các yêu cầu quy định tại Điều 71 và Điều 72 Thông tư này;"
  > — Đ70.3c(i), (iii) ^d70-3c

- Khung thời gian tính LC: chuỗi dữ liệu từ 10 năm trở lên thì dùng 10 năm trở lại đây; chuỗi từ 05 đến dưới 10 năm thì dùng độ dài thực, phần dư từ 06 tháng trở lên làm tròn thành 01 năm.
  > "Đối với chuỗi dữ liệu tổn thất hoạt động có độ dài từ 10 năm trở lên, ngân hàng sử dụng khung thời gian tính là 10 năm trở lại đây;"
  > "Đối với chuỗi dữ liệu tổn thất hoạt động có độ dài từ 05 đến dưới 10 năm, ngân hàng sử dụng độ dài thực của dữ liệu tổn thất hoạt động làm khung thời gian tính. Trường hợp phần dư tính theo năm của độ dài dữ liệu từ 06 tháng trở lên sẽ được tính tròn là 01 năm;"
  > — Đ70.3c(ii) ^d70-3c2

- Ngân hàng thương mại có công ty con được dùng LC tính trên dữ liệu tổn thất riêng lẻ (không gồm công ty con) khi tính tỷ lệ an toàn vốn hợp nhất.
  > "(iv) Ngân hàng thương mại có công ty con được sử dụng LC tính trên dữ liệu tổn thất riêng lẻ (không bao gồm công ty con) khi tính tỷ lệ an toàn vốn hợp nhất;"
  > — Đ70.3c(iv) ^d70-3c4

- Cách xác định LC: tổn thất ròng theo quý bằng tổn thất ghi nhận trừ thu hồi cùng quý; tổn thất ròng theo năm bằng cộng dồn 04 quý liên tiếp; tổn thất ròng trung bình năm bằng tổng các năm trong khung thời gian chia cho số năm; LC bằng 15 lần giá trị trung bình đó.
  > "Ngân hàng thu thập dữ liệu và xác định giá trị tổn thất hoạt động ròng theo quý bằng cách lấy giá trị tổn thất hoạt động ghi nhận trong quý trừ đi giá trị thu hồi được ghi nhận trong cùng quý đó;"
  > "Ngân hàng xác định giá trị tổn thất hoạt động ròng theo năm bằng cách cộng dồn giá trị tổn thất ròng theo quý của 04 quý liên tiếp;"
  > "Ngân hàng xác định giá trị tổn thất hoạt động ròng trung bình năm của khung thời gian tính bằng cách lấy tổng giá trị tổn thất hoạt động ròng theo năm của các năm trong khung thời gian tính chia cho tổng số năm tính;"
  > "LC bằng 15 lần giá trị tổn thất hoạt động ròng trung bình năm của khung thời gian tính."
  > — Đ70.3c(v) ^d70-3c5

#### Đ71 — Dữ liệu tổn thất hoạt động

- Ngân hàng phải thu thập tất cả dữ liệu tổn thất hoạt động có giá trị tổn thất ròng của một sự kiện trong khung thời gian tính từ 12 triệu đồng trở lên.
  > "1. Ngân hàng phải thu thập tất cả các dữ liệu tổn thất hoạt động có giá trị tổn thất hoạt động ròng của một sự kiện trong khung thời gian tính từ 12 triệu đồng trở lên."
  > — Đ71.1 ^d71-1

- Tổn thất ròng của một sự kiện bằng tổng tổn thất ghi nhận trừ các khoản thu hồi đã nhận (kể cả bảo hiểm chi trả); ngân hàng phải dùng giá trị theo ngày hạch toán.
  > "2. Giá trị tổn thất hoạt động ròng của một sự kiện tổn thất được xác định bằng tổng các giá trị tổn thất hoạt động được ghi nhận trừ đi các khoản thu hồi đã được nhận (bao gồm cả khoản được bảo hiểm chi trả) của sự kiện tổn thất đó. Ngân hàng phải sử dụng các giá trị tính theo ngày hạch toán."
  > — Đ71.2 ^d71-2

- Tổng tổn thất hoạt động gồm bốn loại: chi phí ghi vào báo cáo kết quả hoạt động và write-downs; chi phí hậu quả (pháp lý, tư vấn, sửa chữa, thay thế); tổn thất đang chờ xử lý trên tài khoản tạm thời; tổn thất thời gian khi chưa ghi nhận kéo dài hơn 01 năm và làm phát sinh rủi ro pháp lý.
  > "a) Khoản chi phí ghi nhận trực tiếp vào các khoản mục báo cáo kết quả hoạt động và phần giá trị ghi giảm (write-downs) của tài sản do phát sinh sự kiện rủi ro hoạt động của ngân hàng gây ra;"
  > "b) Chi phí phát sinh do hậu quả của sự kiện tổn thất hoạt động bao gồm cả chi phí bên ngoài có mối liên hệ trực tiếp tới sự kiện rủi ro hoạt động"
  > "c) Tổn thất phát sinh từ sự kiện rủi ro hoạt động với tác động tài chính cụ thể, được ghi nhận vào tài khoản tạm thời và chưa được phản ánh trong báo cáo kết quả hoạt động (tổn thất đang chờ xử lý);"
  > "Thời gian chưa thực hiện ghi nhận sự kiện rủi ro hoạt động kéo dài hơn 01 năm và làm phát sinh rủi ro pháp lý (tổn thất thời gian)."
  > — Đ71.3 ^d71-3

- Ba khoản loại trừ khi tính tổng mức tổn thất: chi phí hợp đồng bảo trì chung cho tài sản cố định hữu hình; chi phí tăng cường kinh doanh sau tổn thất (nâng cấp, cải tiến, sáng kiến, cải tiến đánh giá rủi ro); chi phí mua bảo hiểm rủi ro hoạt động.
  > "4. Các cấu phần sau phải loại trừ khi tính tổng mức tổn thất:"
  > "a) Chi phí của hợp đồng bảo trì chung cho tài sản cố định hữu hình;"
  > "b) Chi phí để tăng cường kinh doanh sau các tổn thất rủi ro hoạt động: nâng cấp, cải tiến, các sáng kiến và cải tiến đánh giá rủi ro;"
  > "c) Chi phí mua bảo hiểm rủi ro hoạt động."
  > — Đ71.4 ^d71-4

#### Đ72 — Thu thập và xử lý dữ liệu tổn thất hoạt động

- Ngân hàng phải ban hành đầy đủ quy định nội bộ về quy trình xác định, thu thập, xử lý thông tin tổn thất. Kiểm toán nội bộ phải rà soát quy trình trước khi dữ liệu được dùng tính vốn; kiểm toán nội bộ hoặc kiểm toán độc lập định kỳ xem xét, đánh giá dữ liệu.
  > "1. Ngân hàng phải ban hành đầy đủ quy định nội bộ về quy trình xác định, thu thập và xử lý thông tin tổn thất hoạt động. Quy trình này phải được bộ phận kiểm toán nội bộ rà soát trước khi dữ liệu tổn thất được sử dụng trong tính vốn cho rủi ro hoạt động và được bộ phận kiểm toán nội bộ hoặc kiểm toán độc lập định kỳ xem xét, đánh giá dữ liệu tổn thất."
  > — Đ72.1 ^d72-1

- Dữ liệu tổn thất phải liên kết với các hoạt động kinh doanh hiện tại, hệ thống thông tin, dữ liệu và quy trình quản lý rủi ro của ngân hàng.
  > "2. Dữ liệu tổn thất phải liên kết với các hoạt động kinh doanh hiện tại, hệ thống thông tin, dữ liệu và quy trình quản lý rủi ro của ngân hàng."
  > — Đ72.2 ^d72-2

- Hoạt động làm phát sinh đồng thời rủi ro tín dụng và rủi ro hoạt động thì ngân hàng không phải thu thập dữ liệu tổn thất đó. Hoạt động làm phát sinh đồng thời rủi ro thị trường và rủi ro hoạt động thì ngân hàng phải thu thập.
  > "3. Trường hợp các hoạt động của ngân hàng làm phát sinh đồng thời rủi ro tín dụng và rủi ro hoạt động thì ngân hàng không phải thu thập dữ liệu tổn thất hoạt động này."
  > "4. Trường hợp các hoạt động của ngân hàng làm phát sinh đồng thời rủi ro thị trường và rủi ro hoạt động thì ngân hàng phải thu thập dữ liệu tổn thất hoạt động này."
  > — Đ72.3–4 ^d72-3

- Thông tin cần thu thập gồm ba ngày tham chiếu (ngày xảy ra sự kiện là ngày bắt đầu diễn ra; ngày ghi nhận là ngày ngân hàng nhận biết; ngày hạch toán là ngày các tổn thất được ghi vào lãi, lỗ, hoặc ngày ghi vào tài khoản chờ xử lý), tổng giá trị tổn thất, các khoản thu hồi, và mô tả nguyên nhân cùng yếu tố tác động.
  > "(i) Ngày xảy ra sự kiện là ngày bắt đầu diễn ra;"
  > "(ii) Ngày ghi nhận sự kiện là ngày ngân hàng nhận biết về sự kiện;"
  > "(iii) Ngày hạch toán là ngày hoặc các ngày xảy ra sự kiện tổn thất dẫn đến tổn thất được ghi nhận trong các khoản mục lãi, lỗ của ngân hàng. Đối với trường hợp tổn thất chờ xử lý, ngày hạch toán là ngày ghi nhận vào tài khoản chờ xử lý;"
  > "b) Tổng giá trị tổn thất hoạt động;"
  > "c) Các khoản thu hồi của tổn thất hoạt động;"
  > "d) Mô tả các nguyên nhân và các yếu tố tác động đến sự kiện tổn thất."
  > — Đ72.5 ^d72-5

- Ngân hàng dùng ngày hạch toán để xây dựng bộ dữ liệu tổn thất; với tổn thất từ sự kiện pháp lý thì phải dùng ngày chậm nhất là ngày hạch toán.
  > "6. Ngân hàng sử dụng ngày hạch toán để xây dựng bộ dữ liệu tổn thất. Đối với những tổn thất phát sinh từ các sự kiện pháp lý, ngân hàng phải sử dụng ngày chậm nhất là ngày hạch toán để ghi nhận tổn thất."
  > — Đ72.6 ^d72-6

- Tổn thất do cùng một sự kiện hoặc các sự kiện theo thời gian đã hạch toán cho một số năm thì phân bổ dữ liệu theo các năm tương ứng, phù hợp với nguyên tắc kế toán.
  > "7. Các khoản tổn thất do cùng một sự kiện rủi ro hoạt động hoặc do các sự kiện rủi ro hoạt động theo thời gian và đã được hạch toán cho một số năm thì phân bổ dữ liệu tổn thất theo các năm tương ứng, phù hợp với nguyên tắc kế toán."
  > — Đ72.7 ^d72-7

- Khi ngân hàng mua lại doanh nghiệp thành công ty con, sáp nhập hoặc hợp nhất, phạm vi tổn thất và các cấu phần BI để tính vốn phải gồm các doanh nghiệp đó, kể cả thời gian trước khi mua lại, sáp nhập, hợp nhất.
  > "8. Đối với trường hợp ngân hàng có hoạt động mua lại doanh nghiệp để trở thành công ty con và sáp nhập, hợp nhất, phạm vi tổn thất và các cấu phần của chỉ số kinh doanh được sử dụng để tính yêu cầu về vốn cho rủi ro hoạt động phải bao gồm các doanh nghiệp được mua lại, bị sáp nhập, bị hợp nhất, bao gồm cả khoảng thời gian trước khi được mua lại, bị sáp nhập, bị hợp nhất theo quy định tại Chương này."
  > — Đ72.8 ^d72-8

### C5 — Vốn yêu cầu cho rủi ro thị trường (Đ73–74)

#### Đ73 — Quy định nội bộ về trạng thái rủi ro thị trường

- Để xác định vốn yêu cầu cho rủi ro thị trường, ngân hàng phải có quy định nội bộ đảm bảo tối thiểu các nội dung tại Đ73.1.
  > "1. Để xác định vốn yêu cầu cho rủi ro thị trường, ngân hàng phải có quy định nội bộ đảm bảo tối thiểu các nội dung sau:"
  > — Đ73.1 ^d73-1

- Quy định nội bộ phải nêu điều kiện, tiêu chí xác định khoản mục thuộc sổ kinh doanh, bảo đảm phân biệt giao dịch trên sổ kinh doanh và sổ ngân hàng, và việc chuyển khoản mục giữa hai sổ.
  > "a) Các điều kiện, tiêu chí xác định các khoản mục thuộc phạm vi sổ kinh doanh để tính các trạng thái rủi ro trên sổ kinh doanh, đảm bảo phân biệt các giao dịch trên sổ kinh doanh và sổ ngân hàng và việc chuyển các khoản mục giữa sổ kinh doanh và sổ ngân hàng;"
  > — Đ73.1a ^d73-1a

- Dữ liệu giao dịch phải được ghi nhận chính xác, đầy đủ, kịp thời vào hệ thống cơ sở dữ liệu quản lý rủi ro và hệ thống sổ sách kế toán; phải xác định được bộ phận kinh doanh trực tiếp thực hiện giao dịch.
  > "b) Dữ liệu về giao dịch phải được ghi nhận chính xác, đầy đủ và kịp thời vào hệ thống cơ sở dữ liệu quản lý rủi ro và hệ thống sổ sách kế toán của ngân hàng;"
  > "c) Xác định được bộ phận kinh doanh trực tiếp thực hiện giao dịch;"
  > — Đ73.1b–c ^d73-1b

- Quy định nội bộ phải có trách nhiệm của kiểm toán nội bộ rà soát, đánh giá định kỳ các khoản mục trên sổ kinh doanh và sổ ngân hàng.
  > "d) Có quy định về trách nhiệm bộ phận kiểm toán nội bộ phải định kỳ rà soát, đánh giá các khoản mục trên sổ kinh doanh và sổ ngân hàng;"
  > — Đ73.1d ^d73-1d

- Quy định nội bộ phải có chiến lược tự doanh cho từng loại tiền tệ, công cụ tài chính, sản phẩm phái sinh, bảo đảm không bị hạn chế về mua, bán hoặc có khả năng phòng ngừa được rủi ro.
  > "đ) Có chiến lược tự doanh đối với từng loại tiền tệ, công cụ tài chính, sản phẩm phái sinh, đảm bảo không bị hạn chế về mua, bán hoặc có khả năng phòng ngừa được rủi ro;"
  > — Đ73.1đ ^d73-1dd

- Hạn mức rủi ro thị trường phải được rà soát, đánh giá tối thiểu định kỳ hằng năm hoặc khi có thay đổi lớn ảnh hưởng tới trạng thái rủi ro thị trường.
  > "e) Các hạn mức rủi ro thị trường theo quy định của Ngân hàng Nhà nước về hệ thống kiểm soát nội bộ của ngân hàng phải được rà soát, đánh giá tối thiểu định kỳ hàng năm hoặc vào thời điểm có thay đổi lớn ảnh hưởng tới trạng thái rủi ro thị trường;"
  > — Đ73.1e ^d73-1e

- Quy trình quản lý trạng thái rủi ro thị trường phải đáp ứng đầy đủ các điều kiện: nhận diện, đo lường, theo dõi, kiểm soát chặt chẽ; có bộ phận riêng thực hiện giao dịch tự doanh và bộ phận quản lý, hạch toán theo dõi; báo cáo trạng thái rủi ro cho các cấp thẩm quyền.
  > "g) Quy trình quản lý trạng thái rủi ro thị trường phải đảm bảo đáp ứng đầy đủ các điều kiện sau:"
  > "(i) Các trạng thái rủi ro thị trường được nhận diện, đo lường, theo dõi và kiểm soát chặt chẽ;"
  > "(ii) Có bộ phận riêng để thực hiện các giao dịch tự doanh, trong đó các giao dịch viên có quyền tự chủ thực hiện các giao dịch trong phạm vi các hạn mức và chiến lược tự doanh; có bộ phận quản lý, hạch toán theo dõi các giao dịch tự doanh và các khoản mục trên sổ kinh doanh;"
  > "(iii) Các trạng thái rủi ro và kết quả đo lường rủi ro phải được báo cáo cho các cấp thẩm quyền theo quy định về quản lý rủi ro của ngân hàng;"
  > — Đ73.1g(i)–(iii) ^d73-1g

- Mọi trạng thái tài chính trên sổ kinh doanh phải được đo lường và định giá theo giá thị trường hoặc dữ liệu thị trường ít nhất 01 lần trên 01 ngày làm việc. Dữ liệu thị trường đầu vào phải được thu thập tối đa từ nguồn phù hợp với thị trường và thường xuyên được rà soát về tính phù hợp.
  > "(iv) Tất cả các trạng thái tài chính trên sổ kinh doanh phải được đo lường và định giá theo giá thị trường hoặc dữ liệu thị trường ít nhất 01 lần trên 01 ngày làm việc để xác định mức lỗ, lãi và trạng thái rủi ro thị trường;"
  > "(v) Các dữ liệu thị trường đầu vào phải được thu thập tối đa từ nguồn phù hợp với thị trường và thường xuyên được rà soát, đánh giá về tính phù hợp của các dữ liệu thị trường đầu vào;"
  > — Đ73.1g(iv)–(v) ^d73-1g2

- Phương pháp đo lường rủi ro thị trường phải mô tả đầy đủ giả định và tham số, và được rà soát, đánh giá hằng năm và khi có thay đổi bất thường. Quy trình giám sát trạng thái rủi ro và tuân thủ hạn mức theo chiến lược tự doanh là nội dung bắt buộc.
  > "h) Các phương pháp đo lường rủi ro thị trường (trong đó mô tả đầy đủ các giả định và các tham số được sử dụng), các phương pháp đo lường rủi ro thị trường phải được rà soát, đánh giá hàng năm và khi có thay đổi bất thường ảnh hưởng tới trạng thái rủi ro thị trường;"
  > "i) Quy trình giám sát các trạng thái rủi ro và việc tuân thủ các hạn mức rủi ro thị trường theo chiến lược tự doanh của ngân hàng;"
  > — Đ73.1h–i ^d73-1h

- Nguyên tắc, cách tính vốn yêu cầu cho rủi ro thị trường phải đáp ứng Phụ lục IV.
  > "k) Nguyên tắc, cách tính vốn yêu cầu cho rủi ro thị trường đáp ứng quy định tại Phụ lục IV kèm theo Thông tư này."
  > — Đ73.1k ^d73-1k

- Giao dịch trên sổ kinh doanh và sổ ngân hàng phải được phản ánh trên hệ thống sổ sách kế toán và đối chiếu với số liệu ghi nhận của bộ phận kinh doanh.
  > "a) Giao dịch trên sổ kinh doanh và sổ ngân hàng phải được phản ánh trên hệ thống sổ sách kế toán và phải được đối chiếu với số liệu ghi nhận của bộ phận kinh doanh (nhật ký giao dịch hoặc hình thức ghi nhận khác);"
  > — Đ73.2a ^d73-2a

- Ngân hàng chỉ được phép phân loại lại và chuyển khoản mục từ sổ kinh doanh sang sổ ngân hàng khi khoản mục không còn đáp ứng điều kiện, tiêu chí theo quy định nội bộ tại Đ73.1a. Ngân hàng không được chuyển công cụ tài chính từ sổ ngân hàng sang sổ kinh doanh.
  > "b) Ngân hàng chỉ được phép phân loại lại và chuyển khoản mục từ sổ kinh doanh sang sổ ngân hàng khi khoản mục đó không còn đáp ứng được điều kiện, tiêu chí theo quy định nội bộ của ngân hàng tại điểm a khoản 1 Điều này;"
  > "c) Ngân hàng không được chuyển các công cụ tài chính từ sổ ngân hàng sang sổ kinh doanh."
  > — Đ73.2b–c ^d73-2b

- Việc ban hành, sửa đổi, bổ sung quy định nội bộ phải được các cấp có thẩm quyền của ngân hàng phê duyệt, và được kiểm toán nội bộ rà soát tối thiểu định kỳ hằng năm.
  > "3. Việc ban hành, sửa đổi, bổ sung quy định nội bộ tại khoản 1 Điều này phải được các cấp có thẩm quyền của ngân hàng phê duyệt. Quy định nội bộ này phải được kiểm toán nội bộ rà soát tối thiểu định kỳ hàng năm theo quy định của Ngân hàng Nhà nước về hệ thống kiểm soát nội bộ của ngân hàng."
  > — Đ73.3 ^d73-3

- Ngân hàng gửi quy định nội bộ cho NHNN (qua Cục Quản lý, giám sát tổ chức tín dụng hoặc NHNN chi nhánh Khu vực) để giám sát trước khi thực hiện; khi cần thiết, NHNN có ý kiến bằng văn bản để ngân hàng sửa đổi, bổ sung.
  > "4. Ngân hàng gửi quy định tại khoản 1 Điều này cho Ngân hàng Nhà nước (qua Cục Quản lý, giám sát tổ chức tín dụng hoặc Ngân hàng Nhà nước chi nhánh Khu vực) để giám sát trước khi thực hiện. Trường hợp cần thiết, Ngân hàng Nhà nước (Cục Quản lý, giám sát tổ chức tín dụng hoặc Ngân hàng Nhà nước chi nhánh Khu vực) có ý kiến bằng văn bản gửi ngân hàng để sửa đổi, bổ sung quy định này."
  > — Đ73.4 ^d73-4

#### Đ74 — Vốn yêu cầu cho rủi ro thị trường

- Vốn yêu cầu cho rủi ro thị trường (K_MR) là tổng của năm cấu phần: K_IRR (rủi ro lãi suất), K_ER (rủi ro giá cổ phiếu), K_FXR (rủi ro ngoại hối gồm vàng), K_CMR (rủi ro giá hàng hoá), K_OPT (giao dịch quyền chọn); bốn cấu phần đầu không gồm giao dịch quyền chọn.
  > "1. Vốn yêu cầu cho rủi ro thị trường (K<sub>MR</sub>) được xác định theo công thức sau:"
  > "K<sub>MR</sub> = K<sub>IRR</sub>+ K<sub>ER</sub> + K<sub>FXR</sub> + K<sub>CMR</sub> + K<sub>OPT</sub>"
  > "K<sub>IRR</sub>: Vốn yêu cầu cho rủi ro lãi suất, trừ giao dịch quyền chọn;"
  > "K<sub>ER</sub>: Vốn yêu cầu cho rủi ro giá cổ phiếu, trừ giao dịch quyền chọn;"
  > "K<sub>FXR</sub>: Vốn yêu cầu cho rủi ro ngoại hối (bao gồm cả vàng), trừ giao dịch quyền chọn;"
  > "K<sub>CMR</sub>: Vốn yêu cầu cho rủi ro giá hàng hóa, trừ giao dịch quyền chọn;"
  > "K<sub>OPT</sub>: Vốn yêu cầu cho giao dịch quyền chọn."
  > — Đ74.1 ^d74-1

- K_IRR gồm hai thành phần (K_IRR^SR và K_IRR^GR), tính theo hướng dẫn tại Phụ lục IV.
  > "2. Vốn yêu cầu cho rủi ro lãi suất (K<sub>IRR</sub>) được xác định theo công thức sau:"
  > "Trong đó, vốn yêu cầu cho rủi ro lãi suất được tính theo hướng dẫn tại Phụ lục IV kèm theo Thông tư này."
  > — Đ74.2 ^d74-2

- K_ER gồm hai thành phần (K_ER^SR và K_ER^GR), tính theo hướng dẫn tại Phụ lục IV.
  > "3. Vốn yêu cầu cho rủi ro giá cổ phiếu (K<sub>ER</sub>) xác định theo công thức như sau:"
  > "Trong đó, vốn yêu cầu cho rủi ro giá cổ phiếu được tính theo hướng dẫn tại Phụ lục IV kèm theo Thông tư này."
  > — Đ74.3 ^d74-3

- K_FXR chỉ áp dụng khi tổng giá trị trạng thái ngoại hối ròng (gồm vàng) của ngân hàng lớn hơn 2% vốn tự có; K_FXR và tổng trạng thái ngoại hối ròng tính theo Phụ lục IV.
  > "4. Vốn yêu cầu cho rủi ro ngoại hối (K<sub>FXR</sub>) chỉ áp dụng đối với trường hợp tổng giá trị trạng thái ngoại hối ròng (bao gồm cả vàng) của ngân hàng lớn hơn 2% vốn tự có của ngân hàng. Vốn yêu cầu cho rủi ro ngoại hối và tổng trạng thái ngoại hối ròng (bao gồm cả vàng) được tính theo hướng dẫn tại Phụ lục IV kèm theo Thông tư này."
  > — Đ74.4 ^d74-4

- K_CMR tính theo hướng dẫn tại Phụ lục IV.
  > "5. Vốn yêu cầu cho rủi ro giá hàng hóa (K<sub>CMR</sub>) được tính theo hướng dẫn tại Phụ lục IV kèm theo Thông tư này."
  > — Đ74.5 ^d74-5

- K_OPT chỉ áp dụng khi tổng giá trị các giao dịch quyền chọn lớn hơn 2% vốn tự có; tính theo Phụ lục IV.
  > "6. Vốn yêu cầu cho giao dịch quyền chọn (K<sub>OPT</sub>) chỉ áp dụng khi tổng giá trị các giao dịch quyền chọn lớn hơn 2% vốn tự có của ngân hàng. Vốn yêu cầu cho giao dịch quyền chọn (K<sub>OPT</sub>) được tính theo hướng dẫn tại Phụ lục IV kèm theo Thông tư này."
  > — Đ74.6 ^d74-6

### PL1 — Phụ lục I: Cấu phần và cách xác định vốn tự có

#### A.I — Vốn tự có riêng lẻ của ngân hàng thương mại (Bảng 18)

- Vốn tự có (C) bằng vốn cấp 1 (A) cộng vốn cấp 2 (B). Vốn cấp 1 (A) bằng vốn lõi cấp 1 (A1) cộng vốn bổ sung vốn cấp 1 (A2). Vốn lõi cấp 1 (A1) bằng vốn lõi cấp 1 chưa giảm trừ (A11) trừ các khoản giảm trừ (A12).
  > "VỐN CẤP 1 (A) = A1 + A2"
  > "Vốn lõi cấp 1(A1) = A11 - A12"
  > "VỐN TỰ CÓ (C) = (A) + (B)"
  > — PL1.A.I ^pl1-a-struct

- Vốn lõi cấp 1 chưa giảm trừ (A11) là tổng mười khoản mục (1)–(10): vốn điều lệ (vốn đã góp), quỹ dự trữ bổ sung vốn điều lệ, quỹ đầu tư phát triển, quỹ dự phòng tài chính, các quỹ khác trích từ lợi nhuận sau thuế (không gồm quỹ khen thưởng, phúc lợi, quỹ thưởng ban điều hành), vốn đầu tư xây dựng cơ bản và mua sắm tài sản cố định, vốn khác, lợi nhuận chưa phân phối, thặng dư vốn cổ phần của cổ phần phổ thông, chênh lệch tỷ giá hối đoái.
  > "Vốn lõi cấp 1 chưa giảm trừ (A11)= ∑(1) ÷ (10)"
  > "Vốn điều lệ (vốn đã góp)"
  > "Quỹ dự trữ bổ sung vốn điều lệ"
  > "Quỹ đầu tư phát triển"
  > "Quỹ dự phòng tài chính"
  > "Các quỹ khác được trích từ lợi nhuận sau thuế thu nhập doanh nghiệp theo quy định của pháp luật (không bao gồm quỹ khen thưởng, phúc lợi, quỹ thưởng ban điều hành)"
  > "Vốn đầu tư xây dựng cơ bản, mua sắm tài sản cố định"
  > "Lợi nhuận chưa phân phối"
  > "Thặng dư vốn cổ phần của cổ phần phổ thông"
  > "Chênh lệch tỷ giá hối đoái"
  > — PL1.A.I (1)–(10) ^pl1-a11

- Thặng dư vốn cổ phần tính vào vốn lõi cấp 1 bằng số liệu thặng dư vốn cổ phần trên Báo cáo tình hình tài chính nhân với tỷ trọng cổ phần phổ thông trên tổng số cổ phần.
  > "Lấy số liệu Thặng dư vốn cổ phần trên Báo cáo tình hình tài chính (được lập theo số liệu Bảng cân đối tài khoản kế toán) nhân với tỷ trọng của cổ phần phổ thông trên tổng số cổ phần."
  > — PL1.A.I (9) ^pl1-a11-9

- Với ngân hàng được chấp thuận hoãn, giãn trích lập dự phòng rủi ro, lợi nhuận chưa phân phối phải trừ đi chênh lệch dương giữa số dự phòng rủi ro phải trích theo quy định và số dự phòng đã trích.
  > "Đối với ngân hàng được chấp thuận hoãn, giãn trích lập dự phòng rủi ro, lợi nhuận chưa phân phối phải trừ đi chênh lệch dương giữa số dự phòng rủi ro phải trích theo quy định của pháp luật về mức trích, phương pháp trích lập dự phòng rủi ro và việc sử dụng dự phòng để xử lý rủi ro trong hoạt động của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài và trường hợp tổ chức tín dụng phân bổ lãi phải thu phải thoái so với số dự phòng rủi ro đã trích."
  > — PL1.A.I (8) ^pl1-a11-8

- Các khoản giảm trừ khỏi vốn lõi cấp 1 (A12) là tổng tám khoản mục (11)–(18). Bốn khoản đầu: tài sản cố định vô hình (không gồm quyền sử dụng đất), tài sản thuế thu nhập hoãn lại, lỗ lũy kế, cổ phiếu quỹ ứng với cổ phần phổ thông.
  > "Các khoản giảm trừ khỏi Vốn lõi cấp 1 (A12) = ∑(11) ÷ (18)"
  > "Các tài sản cố định vô hình (không bao gồm quyền sử dụng đất)"
  > "Tài sản thuế thu nhập hoãn lại"
  > "Lỗ lũy kế"
  > "Cổ phiếu quỹ ứng với cổ phần phổ thông"
  > — PL1.A.I (11)–(14) ^pl1-a12

- Phần chênh lệch dương của tổng mức tổn thất dự kiến so với dự phòng rủi ro của danh mục áp dụng IRB (chỉ tính cho danh mục theo khoản 1 Đ62): trừ 50% vào vốn lõi cấp 1 và 50% còn lại vào vốn cấp 2 trong 02 năm kể từ ngày được NHNN chấp thuận IRB; từ năm thứ ba trở đi trừ toàn bộ vào vốn lõi cấp 1.
  > "Phần chênh lệch dương của tổng mức tổn thất dự kiến so với dự phòng rủi ro của danh mục tài sản được áp dụng phương pháp xếp hạng nội bộ"
  > "Chỉ tính chênh lệch cho danh mục tài sản áp dụng phương pháp xếp hạng nội bộ theo quy định tại khoản 1 Điều 62 Thông tư này;"
  > "Ngân hàng thương mại trừ 50% phần chênh lệch vào vốn lõi cấp 1 và 50% phần chênh lệch còn lại vào vốn cấp 2 trong 02 năm kể từ ngày được Ngân hàng Nhà nước chấp thuận áp dụng phương pháp xếp hạng nội bộ. Kể từ năm thứ ba trở đi, ngân hàng thương mại trừ toàn bộ phần chênh lệch vào vốn lõi cấp 1."
  > — PL1.A.I (15) ^pl1-a12-15

- Các khoản góp vốn, mua cổ phần tại tổ chức tín dụng khác, công ty con của tổ chức tín dụng và doanh nghiệp hoạt động trong lĩnh vực ngân hàng, bảo hiểm, chứng khoán là khoản giảm trừ khỏi vốn lõi cấp 1. Cách xác định lấy số liệu góp vốn, đầu tư dài hạn và phần chứng khoán vốn trong chứng khoán sẵn sàng để bán của các đối tượng đó.
  > "Các khoản góp vốn, mua cổ phần tại tổ chức tín dụng khác, công ty con của tổ chức tín dụng và doanh nghiệp hoạt động trong lĩnh vực ngân hàng, bảo hiểm, chứng khoán"
  > "Lấy số liệu các khoản Góp vốn, đầu tư dài hạn và Chứng khoán sẵn sàng để bán phần chứng khoán vốn của các đối tượng là các tổ chức tín dụng khác, công ty con của tổ chức tín dụng khác, doanh nghiệp hoạt động trong lĩnh vực ngân hàng, bảo hiểm, chứng khoán trên Báo cáo tình hình tài chính hợp nhất được lập theo số liệu Bảng cân đối tài khoản kế toán."
  > — PL1.A.I (16) ^pl1-a12-16

- Phần chênh lệch dương giữa tài sản cố định vô hình là quyền sử dụng đất (N1) và 15% của A11 sau khi trừ các khoản (11) đến (16) (N2) là khoản giảm trừ; lấy giá trị N1 − N2 khi lớn hơn 0.
  > "Phần chênh lệch dương giữa Tài sản cố định vô hình là quyền sử dụng đất và 15% của A11 sau khi trừ đi các khoản phải trừ từ (11) đến (16)"
  > "N1 = Tài sản cố định vô hình là Quyền sử dụng đất"
  > "N2 = 15% * [(A11) - ∑(11)÷(16)];"
  > "Lấy giá trị N1 - N2 > 0"
  > — PL1.A.I (17) ^pl1-a12-17

- Khoản giảm trừ cuối cùng của A12 là phần bù cho giá trị âm của vốn bổ sung vốn cấp 1: trường hợp A2 < 0 thì lấy giá trị giảm trừ (ô công thức trong raw bị cụt sau "là").
  > "Phần bù cho giá trị âm của Vốn bổ sung vốn cấp 1"
  > "Trường hợp A2<0, lấy giá trị giảm trừ là"
  > — PL1.A.I (18) ^pl1-a12-18

- Vốn bổ sung vốn cấp 1 (A2) bằng A21 trừ A22. A21 là tổng của (19) công cụ bổ sung vốn cấp 1 do chính ngân hàng thương mại phát hành, đáp ứng đủ điều kiện Mục III, và (20) thặng dư vốn cổ phần của các công cụ đó (số liệu thặng dư vốn cổ phần nhân với tỷ trọng các loại cổ phần không phải cổ phần phổ thông, đáp ứng điều kiện Mục III, trên tổng số cổ phần).
  > "Vốn bổ sung vốn cấp 1 (A2)= A21 - A22"
  > "Vốn bổ sung vốn cấp 1 chưa giảm trừ (A21) =∑(19) ÷ (20)"
  > "Công cụ bổ sung vốn cấp 1 do chính ngân hàng thương mại phát hành"
  > "Lấy giá trị các công cụ bổ sung vốn cấp 1 đáp ứng đầy đủ các điều kiện quy định tại Mục III Phần này"
  > "Thặng dư vốn cổ phần của các công cụ bổ sung vốn cấp 1"
  > — PL1.A.I (19)–(20) ^pl1-a21

- A22 là tổng của (21) mua lại công cụ bổ sung vốn cấp 1 do chính ngân hàng phát hành (cổ phiếu quỹ theo tỷ trọng các loại cổ phần đủ điều kiện Mục III, cộng giá trị công cụ không phải cổ phiếu mà ngân hàng mua lại) và (22) phần bù cho giá trị âm của vốn cấp 2: trường hợp B < 0 thì lấy giá trị giảm trừ là |B|.
  > "Các khoản giảm trừ khỏi Vốn bổ sung vốn cấp 1 (A22)= ∑(21)÷ (22)"
  > "Mua lại công cụ bổ sung vốn cấp 1 do chính ngân hàng thương mại phát hành"
  > "Phần bù cho giá trị âm của Vốn cấp 2"
  > "Trường hợp B<0, lấy giá trị giảm trừ là │B│"
  > — PL1.A.I (21)–(22) ^pl1-a22

- Vốn cấp 2 (B) bằng B1 trừ B2. B1 là tổng ba khoản mục (23)–(25); B2 là tổng bốn khoản mục (26)–(29).
  > "VỐN CẤP 2 (B) = B1 - B2"
  > "Vốn cấp 2 chưa giảm trừ (B1)= ∑(23) ÷ (25)"
  > "Các khoản giảm trừ khỏi Vốn cấp 2 (B2)= ∑(26) ÷ (29)"
  > — PL1.A.I ^pl1-b-struct

- Nợ thứ cấp tính vào vốn cấp 2 phải do ngân hàng phát hành, ký kết và đáp ứng sáu điều kiện: (i) kỳ hạn ban đầu từ 05 năm trở lên; (ii) không được đảm bảo bằng tài sản của chính ngân hàng; (iii) ngân hàng được trả nợ trước hạn nếu sau đó vẫn đảm bảo các tỷ lệ, giới hạn bảo đảm an toàn và báo cáo NHNN để giám sát; (iv) ngân hàng được ngừng trả lãi và chuyển lãi lũy kế sang năm sau nếu việc trả lãi làm kết quả kinh doanh trong năm bị lỗ; (v) khi thanh lý, chủ sở hữu chỉ được thanh toán sau tất cả các chủ nợ khác; (vi) lãi suất cố định hoặc công thức lãi suất xác định trước và ghi rõ trong hợp đồng.
  > "Nợ thứ cấp do ngân hàng phát hành, ký kết đáp ứng đầy đủ các điều kiện sau:"
  > "(i) Có kỳ hạn ban đầu từ 05 năm trở lên;"
  > "(ii) Không được đảm bảo bằng tài sản của chính ngân hàng;"
  > "(iii) Ngân hàng được trả nợ trước thời gian đáo hạn với điều kiện sau khi thực hiện vẫn đảm bảo các tỷ lệ, giới hạn bảo đảm an toàn theo quy định và báo cáo Ngân hàng Nhà nước (Cục Quản lý, giám sát tổ chức tín dụng hoặc Ngân hàng Nhà nước chi nhánh Khu vực theo đối tượng giám sát) để giám sát;"
  > "(iv) Ngân hàng được ngừng trả lãi và chuyển lãi lũy kế sang năm tiếp theo nếu việc trả lãi dẫn đến kết quả kinh doanh trong năm bị lỗ;"
  > "(v) Trong trường hợp thanh lý ngân hàng, người sở hữu khoản nợ thứ cấp chỉ được thanh toán sau khi ngân hàng đã thanh toán cho tất cả các chủ nợ khác;"
  > "(vi) Lãi suất cố định hoặc công thức tính lãi suất được xác định trước và ghi rõ trong hợp đồng, tài liệu phát hành."
  > — PL1.A.I (23) ^pl1-b-sd-cond

- Với lãi suất cố định, việc điều chỉnh tăng lãi suất chỉ được thực hiện sau 05 năm kể từ ngày phát hành, ký kết hợp đồng và chỉ được thay đổi 01 lần trong suốt thời hạn. Với lãi suất theo công thức, công thức không được thay đổi và chỉ được thay đổi biên độ (nếu có) 01 lần sau 05 năm kể từ ngày phát hành, ký kết hợp đồng.
  > "Đối với lãi suất cố định, việc điều chỉnh tăng lãi suất chỉ được thực hiện sau 05 năm kể từ ngày phát hành, ký kết hợp đồng và chỉ được thay đổi 01 lần trong suốt thời hạn của nợ thứ cấp."
  > "Đối với lãi suất tính theo công thức, công thức không được thay đổi và chỉ được thay đổi biên độ trong công thức (nếu có) 01 lần sau 05 năm kể từ ngày phát hành, ký kết hợp đồng."
  > — PL1.A.I (23) ^pl1-b-sd-rate

- Giá trị nợ thứ cấp tính vào vốn cấp 2: toàn bộ nếu thời hạn còn lại trên 05 năm; bắt đầu từ năm thứ năm trước khi đến hạn thanh toán, mỗi năm tại ngày đầu tiên của năm (tính theo ngày phát hành), giá trị tính vào vốn cấp 2 bị khấu trừ 20% của tổng mệnh giá.
  > "Tại thời điểm xác định giá trị, nếu thời hạn còn lại của nợ thứ cấp trên 05 năm, toàn bộ giá trị nợ thứ cấp được tính vào vốn cấp 2."
  > "Bắt đầu từ năm thứ năm trước khi đến hạn thanh toán, mỗi năm tại ngày đầu tiên của năm (tính theo ngày phát hành), giá trị nợ thứ cấp được tính vào vốn cấp 2 sẽ phải được khấu trừ 20% của tổng mệnh giá."
  > — PL1.A.I (23) ^pl1-b-sd-amort

- Khoản mục (24) là 80% dự phòng chung cho các danh mục áp dụng phương pháp tiêu chuẩn khi tính tài sản có rủi ro tín dụng khách hàng; lấy 80% tổng các khoản mục Dự phòng chung trên Báo cáo tình hình tài chính.
  > "80% dự phòng chung theo quy định về mức trích, phương pháp trích dự phòng rủi ro và sử dụng dự phòng để xử lý rủi ro cho các danh mục được áp dụng phương pháp tiêu chuẩn khi tính tài sản có rủi ro tín dụng khách hàng"
  > "Lấy 80% tổng các khoản mục Dự phòng chung trên Báo cáo tình hình tài chính được lập theo số liệu Bảng cân đối tài khoản kế toán."
  > — PL1.A.I (24) ^pl1-b-gp

- Khoản mục (25) là phần chênh lệch dương giữa dự phòng rủi ro và tổn thất dự kiến của danh mục áp dụng IRB khi tính tài sản có rủi ro tín dụng khách hàng; chỉ áp dụng cho danh mục theo khoản 2 Đ62.
  > "Phần chênh lệch dương giữa dự phòng rủi ro và tổn thất dự kiến cho danh mục được áp dụng phương pháp xếp hạng nội bộ khi tính tài sản có rủi ro tín dụng khách hàng"
  > "Chỉ áp dụng cho danh mục tài sản được áp dụng phương pháp xếp hạng nội bộ khi tính tài sản có rủi ro tín dụng khách hàng theo quy định tại khoản 2 Điều 62 Thông tư này."
  > — PL1.A.I (25) ^pl1-b-irb

- Khoản giảm trừ (26) là phần chênh lệch dương giữa khoản mục (24) và 1,25% Tổng tài sản có rủi ro tín dụng khách hàng của danh mục áp dụng phương pháp tiêu chuẩn. Khoản giảm trừ (27) là phần chênh lệch dương giữa khoản mục (25) và 0,6% Tổng tài sản có rủi ro tín dụng khách hàng của danh mục áp dụng IRB.
  > "Phần giá trị chênh lệch dương giữa khoản mục (24) và 1,25% “Tổng tài sản có rủi ro tín dụng khách hàng” của danh mục được áp dụng phương pháp tiêu chuẩn khi tính tài sản có rủi ro tín dụng khách hàng quy định tại Thông tư này"
  > "Phần chênh lệch dương giữa khoản mục (25) và 0,6% “Tổng tài sản có rủi ro tín dụng khách hàng” của danh mục được áp dụng phương pháp xếp hạng nội bộ khi tính tài sản có rủi ro tín dụng khách hàng quy định tại Thông tư này"
  > — PL1.A.I (26)–(27) ^pl1-b2-cap

- Khoản giảm trừ (28) là 50% phần chênh lệch dương của tổng mức tổn thất dự kiến so với trích lập dự phòng của danh mục IRB; chỉ áp dụng trong vòng 02 năm kể từ ngày được NHNN chấp thuận IRB, từ năm thứ ba trở đi không áp dụng.
  > "50% phần chênh lệch dương của tổng mức tổn thất dự kiến so với dự phòng rủi ro của danh mục các tài sản được áp dụng phương pháp xếp hạng tín dụng nội bộ"
  > "Chỉ áp dụng trong vòng 02 năm kể từ ngày được Ngân hàng Nhà nước chấp thuận áp dụng phương pháp xếp hạng nội bộ theo quy định tại khoản 1 Điều 62 Thông tư này. Kể từ năm thứ ba trở đi, không áp dụng khoản mục này."
  > — PL1.A.I (28) ^pl1-b2-28

- Khoản giảm trừ (29) là khoản mua, đầu tư nợ thứ cấp của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác phát hành đáp ứng điều kiện tính vào vốn cấp 2 của đơn vị đó (không gồm nợ thứ cấp nhận làm tài sản bảo đảm, chiết khấu, tái chiết khấu của khách hàng). Từ năm thứ năm trước khi đến hạn thanh toán, mỗi năm tại ngày đầu tiên của năm giá trị khoản mua, đầu tư bị khấu trừ 20% của tổng giá mua.
  > "Mua, đầu tư nợ thứ cấp của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác phát hành đáp ứng đầy đủ các điều kiện để tính vào vốn cấp 2 của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài đó (không bao gồm nợ thứ cấp nhận làm tài sản bảo đảm, chiết khấu, tái chiết khấu của khách hàng)"
  > "Bắt đầu từ năm thứ năm trước khi đến hạn thanh toán, mỗi năm tại ngày đầu tiên của năm (tính theo ngày phát hành), giá trị khoản mua, đầu tư nợ thứ cấp của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài khác phát hành đáp ứng đầy đủ các điều kiện để tính vào vốn cấp 2 của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài đó sẽ được khấu trừ 20% của tổng giá mua."
  > — PL1.A.I (29) ^pl1-b2-29

#### A.II — Vốn tự có hợp nhất (Bảng 19)

- Vốn tự có hợp nhất lấy từ Báo cáo tình hình tài chính hợp nhất, trong đó không hợp nhất công ty con là doanh nghiệp hoạt động theo Luật kinh doanh bảo hiểm. Khi báo cáo hợp nhất không có khoản mục cụ thể, ngân hàng phải xây dựng số liệu thống kê từ các bảng cân đối tài khoản kế toán riêng lẻ của các đối tượng hợp nhất.
  > "a. Vốn tự có hợp nhất được xác định theo các cấu phần quy định tại điểm 2 dưới đây, lấy từ Báo cáo tình hình tài chính, trong đó không hợp nhất công ty con là doanh nghiệp hoạt động theo Luật kinh doanh bảo hiểm."
  > "b. Trường hợp Báo cáo tình hình tài chính hợp nhất nêu tại điểm a không có các khoản mục cụ thể để tính vốn lõi cấp 1 hợp nhất, vốn bổ sung vốn cấp 1 hợp nhất và vốn cấp 2 hợp nhất, thì ngân hàng phải xây dựng số liệu thống kê từ các bảng cân đối tài khoản kế toán riêng lẻ của các đối tượng hợp nhất để đảm bảo việc tính toán đầy đủ, chính xác các khoản mục Vốn tự có."
  > — PL1.A.II.1 ^pl1-ii-1

- Cấu trúc vốn tự có hợp nhất giống riêng lẻ: C = A + B, A = A1 + A2, A1 = A11 − A12, B = B1 − B2. Các khoản giảm trừ khỏi vốn lõi cấp 1 hợp nhất (A12) là tổng khoản mục (11)–(19).
  > "VỐN CẤP 1 HỢP NHẤT (A) = A1 + A2"
  > "Vốn lõi cấp 1 hợp nhất (A1) = A11 - A12"
  > "VỐN CẤP 2 HỢP NHẤT (B) = B1 - B2"
  > "VỐN TỰ CÓ HỢP NHẤT (C) = (A) + (B)"
  > "Các khoản giảm trừ khỏi Vốn lõi cấp 1 hợp nhất (A12) = ∑(11) ÷ (19)"
  > — PL1.A.II.2 ^pl1-ii-struct

- Vốn tự có hợp nhất có thêm khoản giảm trừ lợi thế thương mại phát sinh khi hợp nhất kinh doanh, lấy từ Báo cáo tình hình tài chính hợp nhất.
  > "Lợi thế thương mại"
  > "Lấy số liệu Lợi thế thương mại phát sinh khi hợp nhất kinh doanh được xác định theo chuẩn mực kế toán hợp nhất kinh doanh trên Báo cáo tình hình tài chính hợp nhất."
  > — PL1.A.II.2 (11) ^pl1-ii-gw

- Với khoản góp vốn, mua cổ phần tại tổ chức tín dụng khác, công ty con của tổ chức tín dụng và doanh nghiệp ngân hàng, bảo hiểm, chứng khoán, vốn tự có hợp nhất lấy cả phần chứng khoán vốn trong chứng khoán kinh doanh, ngoài góp vốn, đầu tư dài hạn và chứng khoán sẵn sàng để bán.
  > "Lấy số liệu các khoản Góp vốn, đầu tư dài hạn và Chứng khoán sẵn sàng để bán và Chứng khoán kinh doanh phần chứng khoán vốn vào các đối tượng là các tổ chức tín dụng khác, công ty con của tổ chức tín dụng khác, doanh nghiệp hoạt động trong lĩnh vực ngân hàng, bảo hiểm, chứng khoán trên Báo cáo tình hình tài chính hợp nhất được lập theo số liệu Bảng cân đối tài khoản kế toán của các đối tượng hợp nhất."
  > — PL1.A.II.2 (17) ^pl1-ii-17

- Vốn cấp 2 hợp nhất chưa giảm trừ (B1) là tổng bốn khoản mục (24)–(27), trong đó (27) là lợi ích cổ đông không kiểm soát.
  > "Vốn cấp 2 hợp nhất chưa giảm trừ (B1)= ∑(24) ÷ (27)"
  > "Lợi ích cổ đông không kiểm soát"
  > — PL1.A.II.2 (27) ^pl1-ii-mi

- Khoản giảm trừ hợp nhất (28) là phần chênh lệch dương giữa khoản mục (25) và 1,25% Tổng tài sản có rủi ro tín dụng khách hàng của danh mục áp dụng phương pháp tiêu chuẩn; (29) là phần chênh lệch dương giữa khoản mục (26) và 0,6% của danh mục áp dụng IRB. Các trần 1,25% và 0,6% giữ nguyên như riêng lẻ.
  > "Phần giá trị chênh lệch dương giữa khoản mục (25) và 1,25% “Tổng tài sản có rủi ro tín dụng khách hàng” của danh mục được áp dụng phương pháp tiêu chuẩn khi tính tài sản có rủi ro tín dụng khách hàng quy định tại Thông tư này"
  > "Phần chênh lệch dương giữa khoản mục (26) và 0,6% “Tổng tài sản có rủi ro tín dụng khách hàng” của danh mục được áp dụng phương pháp xếp hạng nội bộ khi tính tài sản có rủi ro tín dụng khách hàng quy định tại Thông tư này"
  > — PL1.A.II.2 (28)–(29) ^pl1-ii-caps

#### A.III — Công cụ bổ sung vốn cấp 1

- Công cụ bổ sung vốn cấp 1 do ngân hàng thương mại phát hành phải đã phát hành và được bên mua nộp tiền đầy đủ; có thứ tự thanh toán sau người gửi tiền, chủ nợ có bảo đảm, chủ nợ không có bảo đảm và chủ nợ nợ thứ cấp; không được bảo đảm bằng tài sản hoặc bảo lãnh của ngân hàng phát hành hoặc bên liên quan; không có ngày đáo hạn và không có điều khoản tăng lãi suất hoặc ưu đãi khác cho việc mua lại.
  > "Công cụ bổ sung vốn cấp 1 là công cụ tài chính do ngân hàng thương mại phát hành đáp ứng đầy đủ các điều kiện sau:"
  > "1. Đã phát hành và đã được bên mua nộp tiền thanh toán đầy đủ."
  > "2. Có thứ tự thanh toán sau người gửi tiền, các chủ nợ có bảo đảm, chủ nợ không có bảo đảm và chủ nợ các khoản nợ thứ cấp của ngân hàng thương mại."
  > "3. Không được bảo đảm bằng tài sản hoặc bảo lãnh của ngân hàng thương mại phát hành hoặc của bất kỳ bên liên quan của ngân hàng thương mại phát hành; hoặc không có bất kỳ thỏa thuận nào khác khiến chủ sở hữu của công cụ này có quyền ưu tiên về mặt pháp lý hoặc kinh tế so với các chủ nợ của ngân hàng thương mại."
  > "4. Không có ngày đáo hạn và không có điều khoản tăng lãi suất hoặc các ưu đãi khác cho việc mua lại công cụ này."
  > — PL1.A.III.1–4 ^pl1-iii-1

- Ngân hàng thương mại chỉ được mua lại công cụ theo hợp đồng phát hành sau tối thiểu 05 năm kể từ ngày phát hành, khi đủ ba điều kiện: NHNN chấp thuận việc mua lại và hoàn trả vốn gốc; ngân hàng thay thế công cụ bằng nguồn vốn có chất lượng tương đương hoặc cao hơn, hoặc bảo đảm sau mua lại vẫn tuân thủ các giới hạn, tỷ lệ an toàn; ngân hàng không tạo kỳ vọng chắc chắn về việc mua lại và việc chấp thuận.
  > "5. Công cụ này chỉ được ngân hàng thương mại thực hiện quyền mua lại theo hợp đồng phát hành sau tối thiểu 05 năm kể từ ngày phát hành khi đáp ứng đầy đủ các điều kiện sau:"
  > "a) Việc mua lại và việc hoàn trả phần vốn gốc của công cụ phải được Ngân hàng Nhà nước chấp thuận theo quy định của pháp luật;"
  > "b) Ngân hàng thương mại thay thế công cụ được mua lại bằng nguồn vốn có chất lượng tương đương vốn bổ sung vốn cấp 1 hoặc cao hơn, phù hợp với khả năng sinh lời của ngân hàng thương mại; hoặc ngân hàng thương mại đảm bảo sau khi thực hiện quyền mua lại vẫn tuân thủ các giới hạn, tỷ lệ an toàn theo quy định;"
  > "c) Ngân hàng thương mại không được tạo ra kỳ vọng về việc công cụ này chắc chắn sẽ được ngân hàng thương mại thực hiện quyền mua lại và việc hoàn trả phần vốn gốc của công cụ sẽ được chấp thuận."
  > — PL1.A.III.5 ^pl1-iii-5

- Công cụ phải linh hoạt trong việc hủy bỏ chi trả cổ tức, lãi: hủy bỏ tại bất kỳ thời điểm nào; không bị coi là sự kiện vỡ nợ; được dùng khoản đã hủy để thanh toán nghĩa vụ khác khi đến hạn; không ảnh hưởng toàn bộ hoạt động của ngân hàng, trừ việc phân phối lợi nhuận cho cổ đông phổ thông. Chi trả bằng lợi nhuận chưa phân phối do ngân hàng tự quyết định, và không được điều chỉnh theo xếp hạng tín nhiệm của ngân hàng.
  > "6. Công cụ có tính linh hoạt trong việc hủy bỏ chi trả cổ tức, lãi (coupon), cụ thể:"
  > "a) Việc hủy bỏ chi trả cổ tức, lãi của công cụ có thể được thực hiện tại bất kỳ thời điểm nào;"
  > "b) Việc hủy bỏ các khoản chi trả không được xem là sự kiện vỡ nợ của ngân hàng thương mại;"
  > "c) Được sử dụng khoản cổ tức, lãi đã bị hủy bỏ chi trả để thanh toán các nghĩa vụ khác khi đến hạn;"
  > "d) Việc hủy bỏ chi trả cổ tức, lãi không ảnh hưởng đến toàn bộ hoạt động của ngân hàng thương mại, trừ ảnh hưởng đến việc phân phối lợi nhuận cho cổ đông phổ thông;"
  > "7. Ngân hàng thương mại sử dụng phần lợi nhuận chưa phân phối do ngân hàng thương mại tự quyết định theo quy định pháp luật về chế độ tài chính để chi trả cổ tức, lãi của công cụ này;"
  > "8. Việc chi trả cổ tức, lãi của công cụ này không được có đặc tính điều chỉnh theo xếp hạng tín nhiệm của ngân hàng thương mại;"
  > — PL1.A.III.6–8 ^pl1-iii-6

- Công cụ không làm gia tăng nghĩa vụ nợ vượt quá tổng tài sản của ngân hàng khi kiểm tra báo cáo tình hình tài chính theo pháp luật về phá sản.
  > "9. Không làm gia tăng nghĩa vụ nợ vượt quá tổng tài sản của ngân hàng thương mại trong trường hợp ngân hàng thương mại thực hiện kiểm tra báo cáo tình hình tài chính theo quy định pháp luật về phá sản."
  > — PL1.A.III.9 ^pl1-iii-9

- Công cụ được phân loại là khoản nợ cho mục đích hạch toán và phải có cơ chế bù đắp lỗ khi tỷ lệ vốn lõi cấp 1 thấp hơn 5,125%, chuyển thành vốn lõi cấp 1 theo chuẩn mực kế toán, bằng chuyển đổi nợ thành cổ phần hoặc ghi giảm giá trị gốc. Tổng số tiền ghi giảm giá trị, chuyển đổi tối thiểu phải đủ để đưa tỷ lệ vốn lõi cấp 1 lên 5,125%; nếu không thực hiện được thì phải ghi giảm toàn bộ giá trị gốc.
  > "10. Công cụ này được phân loại là khoản nợ cho mục đích hạch toán và phải có cơ chế bù đắp lỗ khi tỷ lệ vốn lõi cấp 1 thấp hơn 5,125%."
  > "Ngân hàng thương mại phát hành được thực hiện cơ chế bù đắp lỗ bằng việc chuyển đổi công cụ nợ thành cổ phần hoặc ghi giảm giá trị gốc của công cụ nợ."
  > "a) Tổng số tiền ghi giảm giá trị, chuyển đổi tối thiểu phải đủ để đưa tỷ lệ vốn lõi cấp 1 của ngân hàng thương mại lên mức 5,125%;"
  > "b) Nếu không thực hiện được điểm 11a nêu trên, ngân hàng thương mại phải ghi giảm toàn bộ giá trị gốc của công cụ đó."
  > — PL1.A.III.10–11 ^pl1-iii-10

- Ngân hàng thương mại, công ty con, công ty liên kết không được mua công cụ bổ sung vốn cấp 1, và ngân hàng thương mại không được cấp tín dụng để mua công cụ này. Công cụ không có điều khoản cản trở việc tăng vốn của ngân hàng.
  > "12. Ngân hàng thương mại, công ty con, công ty liên kết của ngân hàng thương mại không được mua công cụ bổ sung vốn cấp 1. Ngân hàng thương mại không được cấp tín dụng để mua công cụ này."
  > "13. Không có điều khoản cản trở việc tăng vốn của ngân hàng thương mại, như điều khoản yêu cầu ngân hàng thương mại phát hành phải bồi thường cho chủ sở hữu của công cụ trước đó trong trường hợp một công cụ mới được phát hành với mức giá thấp hơn công cụ trước đó trong một khoảng thời gian xác định kể từ thời điểm phát hành công cụ trước đó."
  > — PL1.A.III.12–13 ^pl1-iii-12

#### B — Vốn tự có của chi nhánh ngân hàng nước ngoài (Bảng 20)

- Chi nhánh ngân hàng nước ngoài căn cứ vào các cấu phần của Phần B, quy định về chế độ tài chính và khoản mục tài sản của mình để xác định vốn tự có. Vốn cấp 1 (A) chỉ gồm vốn lõi cấp 1 (A1); vốn lõi cấp 1 chưa giảm trừ (A11) là tổng chín khoản mục (1)–(9), khoản (1) là vốn đã được cấp; các khoản giảm trừ (A12) là tổng khoản mục (10)–(15). Vốn cấp 2 của chi nhánh có cùng cấu trúc B = B1 − B2, B1 là tổng khoản mục (16)–(18) và B2 là tổng khoản mục (19)–(22).
  > "Chi nhánh ngân hàng nước ngoài căn cứ vào các cấu phần quy định dưới đây, quy định của pháp luật về chế độ tài chính đối với tổ chức tín dụng, chi nhánh ngân hàng nước ngoài và khoản mục tài sản của mình để xác định Vốn tự có cho phù hợp."
  > "VỐN CẤP 1 (A) = A1"
  > "Vốn lõi cấp 1 chưa giảm trừ (A11)= ∑(1) ÷ (9)"
  > "Vốn đã được cấp"
  > "Các khoản giảm trừ khỏi Vốn lõi cấp 1 (A12) = ∑(10) ÷ (15)"
  > "VỐN CẤP 2 (B) = B1 - B2"
  > "Vốn cấp 2 chưa giảm trừ (B1)= ∑(16) ÷(18)"
  > "Các khoản giảm trừ khỏi Vốn cấp 2 (B2)= ∑(19) ÷(22)"
  > — PL1.B ^pl1-br-struct

- Chi nhánh ngân hàng nước ngoài trừ phần chênh lệch dương của tổng mức tổn thất dự kiến so với dự phòng rủi ro của danh mục IRB theo cùng lịch như ngân hàng thương mại: 50% vào vốn lõi cấp 1 và 50% vào vốn cấp 2 trong 02 năm kể từ ngày được NHNN chấp thuận, từ năm thứ ba trừ toàn bộ vào vốn lõi cấp 1.
  > "Chi nhánh ngân hàng nước ngoài trừ 50% phần chênh lệch vào vốn lõi cấp 1 và 50% phần chênh lệch còn lại vào vốn cấp 2 trong 02 năm kể từ ngày được Ngân hàng Nhà nước chấp thuận áp dụng phương pháp xếp hạng nội bộ. Kể từ năm thứ ba trở đi, chi nhánh ngân hàng nước ngoài trừ toàn bộ phần chênh lệch vào vốn lõi cấp 1."
  > — PL1.B (13) ^pl1-br-13

### PL3 — Phụ lục III: Xác định giá trị của chỉ số kinh doanh

#### Công thức các cấu phần BI (Bảng 24)

- ILDC bằng giá trị nhỏ hơn giữa giá trị tuyệt đối của (thu nhập lãi và các khoản thu nhập tương tự trừ chi phí lãi và các chi phí tương tự) và 2,25% tài sản tạo lãi, cộng thu nhập từ góp vốn, mua cổ phần.
  > "min (│Thu nhập lãi và các khoản thu nhập tương tự - Chi phí lãi và các chi phí tương tự│; 2,25%*Tài sản tạo lãi) + Thu nhập từ góp vốn mua cổ phần"
  > — PL3.1 (ILDC) ^pl3-1-ildc

- Tài sản tạo lãi là những tài sản tạo ra thu nhập lãi và các khoản thu nhập tương tự từ Báo cáo tình hình tài chính, gồm sáu khoản: tiền gửi tại NHNN; tiền gửi và cho vay các TCTD khác; chứng khoán kinh doanh; cho vay khách hàng; hoạt động mua nợ; chứng khoán đầu tư.
  > "Tài sản tạo lãi là những tài sản tạo ra thu nhập lãi và các khoản thu nhập tương tự từ Báo cáo tình hình tài chính gồm:"
  > "+ Tiền gửi tại NHNN;"
  > "+ Tiền gửi và cho vay các TCTD khác;"
  > "+ Chứng khoán kinh doanh;"
  > "+ Cho vay khách hàng"
  > "+ Hoạt động mua nợ;"
  > "+ Chứng khoán đầu tư."
  > — PL3.1 (ILDC) ^pl3-1-eaa

- SC bằng giá trị lớn hơn giữa thu nhập và chi phí từ hoạt động dịch vụ, cộng giá trị lớn hơn giữa thu nhập và chi phí từ hoạt động khác.
  > "max(Thu nhập từ hoạt động dịch vụ, Chi phí hoạt động dịch vụ) + max (Thu nhập từ hoạt động khác, Chi phí từ hoạt động khác)"
  > — PL3.1 (SC) ^pl3-1-sc

- FC bằng tổng ba giá trị tuyệt đối: lãi/lỗ thuần từ hoạt động kinh doanh ngoại hối (gồm vàng tiêu chuẩn), lãi/lỗ thuần từ mua bán chứng khoán kinh doanh, lãi/lỗ thuần từ mua bán chứng khoán đầu tư.
  > "│Lãi/lỗ thuần từ hoạt động kinh doanh ngoại hối (bao gồm cả vàng tiêu chuẩn)│ + │Lãi/lỗ thuần từ mua bán chứng khoán kinh doanh│ + │Lãi/lỗ thuần từ mua bán, chứng khoán đầu tư│"
  > — PL3.1 (FC) ^pl3-1-fc

- Các cấu phần của BI (ILDC, SC, FC) được xác định qua giá trị trung bình 03 năm gần nhất của các thành phần theo công thức.
  > "Các cấu phần của BI (ILDC, SC, FC) được xác định qua giá trị trung bình 03 năm gần nhất của các thành phần theo công thức."
  > — PL3.1 ^pl3-1-avg

#### Khoản mục không tính vào BI

- Bốn nhóm khoản mục không được tính vào bất cứ cấu phần nào của BI: (a) thu nhập và chi phí từ hoạt động kinh doanh bảo hiểm hoặc tái bảo hiểm (TK716); (b) phí bảo hiểm đã thanh toán và các khoản bồi hoàn từ hợp đồng bảo hiểm hoặc tái bảo hiểm đã mua; (c) thay đổi trong lợi thế thương mại ghi vào Báo cáo kết quả hoạt động; (d) thu nhập từ việc thu hồi chi phí vận hành, gồm thu hồi các khoản thanh toán thay cho khách hàng.
  > "Các khoản mục sau đây không được tính vào bất cứ cấu phần nào của BI:"
  > "a) Thu nhập và chi phí từ hoạt động kinh doanh bảo hiểm hoặc tái bảo hiểm (TK716);"
  > "b) Phí bảo hiểm đã thanh toán và các khoản bồi hoàn/ được thanh toán từ các hợp đồng bảo hiểm hoặc tái bảo hiểm đã mua (Tài khoản 883 - Chi nộp phí bảo hiểm, bảo toàn tiền gửi của khách hàng gồm các khoản chi phí cho công ty bảo hiểm tiền gửi của khách hàng và một phần TK79 ứng với Thu tiền bảo hiểm được bồi thường được hạch toán vào thu nhập sau khi đã bù đắp khoản tổn thất đã mua bảo hiểm);"
  > "c) Thay đổi trong lợi thế thương mại đã được ghi nhận vào Báo cáo KQHĐ (phần Tài khoản 79 hoặc phần Tài khoản 89 ứng với lợi thế thương mại được chuyển nhượng khi thực hiện mua tài sản mà chỉ tính một phần hoặc không tính đến lợi thế thương mại đi kèm);"
  > "d) Thu nhập từ việc thu hồi chi phí vận hành bao gồm thu hồi các khoản thanh toán thay cho khách hàng (phần Tài khoản 79 - Thu nhập khác ứng với thu hồi các khoản chi nộp phạt vi phạm hành chính mà ngân hàng đã trả thay cho khách hàng)."
  > — PL3.2 ^pl3-2

#### Ví dụ xác định BI tại thời điểm 31/10/2024

- Ví dụ ILDC: bước 1 tính trung bình 3 năm của giá trị tuyệt đối của (thu nhập lãi trừ chi phí lãi). Giá trị tuyệt đối theo năm lấy bằng cách cộng dồn giá trị tuyệt đối theo quý của 4 quý liên tiếp; năm 2022 gồm Q4.2021, Q1.2022, Q2.2022 và Q3.2022.
  > "Bước 1: Xác định thành phần giá trị trung bình 3 năm của giá trị tuyệt đối của “Thu nhập lãi và các khoản thu nhập tương tự - Chi phí lãi và các chi phí tương tự” như sau:"
  > "Xác định giá trị tuyệt đối theo năm của “Thu nhập lãi và các khoản thu nhập tương tự - Chi phí lãi và các chi phí tương tự” cho năm 2022 bằng cách cộng dồn số dư cuối kỳ của giá trị tuyệt đối của “Thu nhập lãi và các khoản thu nhập tương tự - Chi phí lãi và các chi phí tương tự” theo quý của 4 quý liên tiếp Q4.2021, Q1.2022, Q2.2022 và Q3.2022."
  > — PL3.3.1 (ILDC, bước 1) ^pl3-3-ildc1

- Ví dụ ILDC: bước 2 tính trung bình 3 năm của tài sản tạo lãi. Giá trị theo năm lấy bằng trung bình số dư tại bốn thời điểm Q4.2021, Q1.2022, Q2.2022 và Q3.2022 (không cộng dồn).
  > "Bước 2: Xác định thành phần giá trị trung bình 3 năm của “Tài sản tạo lãi” như sau:"
  > "Xác định giá trị theo năm của “Tài sản tạo lãi” cho năm 2022 bằng cách lấy giá trị trung bình của số dư cấu phần này tại các thời điểm Q4.2021, Q1.2022, Q2.2022 và Q3.2022;"
  > — PL3.3.1 (ILDC, bước 2) ^pl3-3-ildc2

- Ví dụ ILDC: bước 3 so sánh và chọn giá trị bé hơn giữa trung bình 3 năm của giá trị tuyệt đối của (thu nhập lãi trừ chi phí lãi) và "2,25 lần" giá trị trung bình 3 năm của tài sản tạo lãi. Câu này khác công thức Bảng 24, vốn ghi 2,25% tài sản tạo lãi.
  > "Bước 3: So sánh và chọn giá trị bé hơn giữa giá trị trung bình 3 năm cho giá trị tuyệt đối của “Thu nhập lãi và các khoản thu nhập tương tự - Chi phí lãi và các chi phí tương tự” với 2,25 lần giá trị trung bình 3 năm của “Tài sản tạo lãi”."
  > — PL3.3.1 (ILDC, bước 3) ^pl3-3-ildc3

- Thu nhập từ góp vốn, mua cổ phần tính trung bình 3 năm bằng phương pháp tương tự cách tính trung bình 3 năm của giá trị tuyệt đối của (thu nhập lãi trừ chi phí lãi).
  > "Đối với thành phần “Thu nhập từ góp vốn mua cổ phần, ngân hàng sử dụng phương pháp tương tự như cách xác định giá trị trung bình 3 năm cho thành phần giá trị tuyệt đối của “Thu nhập lãi và các khoản thu nhập tương tự - Chi phí lãi và các chi phí tương tự”."
  > — PL3.3.1 (ILDC) ^pl3-3-div

- Ví dụ SC: giá trị theo năm của thu nhập từ hoạt động dịch vụ lấy bằng cách cộng dồn số dư cuối kỳ của 4 quý liên tiếp. Chi phí hoạt động dịch vụ xác định tương tự; sau đó lấy giá trị lớn hơn giữa hai trung bình 3 năm. Cặp thu nhập và chi phí hoạt động khác xác định tương tự cặp dịch vụ.
  > "Xác định giá trị theo năm của “Thu nhập từ hoạt động dịch vụ” cho năm 2022 bằng cách cộng dồn số dư cuối kỳ của 4 quý Q4.2021, Q1.2022, Q2.2022 và Q3.2022;"
  > "Bước 3: So sánh và lấy giá trị lớn hơn giữa giá trị trung bình 3 năm của “Thu nhập từ hoạt động dịch vụ” và giá trị trung bình 3 năm của “Chi phí hoạt động dịch vụ”."
  > "Đối với thành phần giá trị lớn hơn giữa “Thu nhập từ hoạt động khác” và “Chi phí hoạt động khác” được xác định tương tự như thành phần giá trị lớn hơn giữa “Thu nhập từ hoạt động dịch vụ” và “Chi phí hoạt động dịch vụ”."
  > — PL3.3.1 (SC) ^pl3-3-sc

- Ví dụ FC: giá trị tuyệt đối theo năm của lãi/lỗ thuần ngoại hối (gồm vàng tiêu chuẩn) lấy bằng cách cộng dồn giá trị tuyệt đối theo quý của 4 quý liên tiếp, rồi lấy trung bình 3 năm. Hai thành phần chứng khoán kinh doanh và chứng khoán đầu tư dùng phương pháp tương tự.
  > "Bước 1: Xác định giá trị tuyệt đối theo năm của “Lãi/lỗ thuần từ hoạt động kinh doanh ngoại hối (bao gồm cả vàng tiêu chuẩn)” cho năm 2022 bằng cách cộng dồn số dư cuối kỳ của giá trị tuyệt đối theo quý của 4 quý Q4.2021, Q1.2022, Q2.2022 và Q3.2022"
  > "Sử dụng phương pháp tương tự để xác định giá trị trung bình 3 năm của giá trị tuyệt đối của “Lãi/lỗ thuần từ mua bán chứng khoán kinh doanh” và giá trị trung bình 3 năm của giá trị tuyệt đối của “Lãi/lỗ thuần từ mua bán, chứng khoán đầu tư”"
  > — PL3.3.1 (FC) ^pl3-3-fc

#### Ví dụ xác định LC tại thời điểm 31/10/2024

- Ví dụ LC: ngân hàng thu thập dữ liệu tổn thất hoạt động ròng theo quý, bằng giá trị tổn thất ghi nhận trong quý trừ giá trị thu hồi được ghi nhận trong cùng quý.
  > "Bước 1: Ngân hàng thu thập dữ liệu tổn thất hoạt động ròng theo quý bằng cách lấy giá trị tổn thất hoạt động ghi nhận trong quý trừ đi giá trị thu hồi được ghi nhận trong cùng quý đó;"
  > — PL3.3.2 (bước 1) ^pl3-lc-1

- Khung thời gian tính toán tại tháng 10/2024: 10 năm khi độ dài dữ liệu từ 38 quý liên tiếp trở lên (quý đầu tiên phải trước Q2.2015); từ 05 năm đến dưới 10 năm khi từ 20 đến 37 quý liên tiếp (quý đầu tiên trong khoảng Q3.2015 đến Q4.2019); chưa đủ 05 năm khi dưới 20 quý liên tiếp (quý đầu tiên từ sau Q1.2020).
  > "Ngân hàng có khung thời gian tính toán 10 năm khi có độ dài dữ liệu từ 38 quý liên tiếp trở lên tính đến thời điểm Tháng 10/2024 (dữ liệu theo quý đầu tiên phải trước Q2.2015);"
  > "Ngân hàng có khung thời gian tính toán từ 05 năm đến dưới 10 năm khi có độ dài dữ liệu từ 20 đến 37 quý liên tiếp tính đến thời điểm Tháng 10/2024 (dữ liệu theo quý đầu tiên kể nằm trong khoảng thời gian từ Q3.2015 đến Q4.2019);"
  > "Ngân hàng có khung thời gian tính toán chưa đủ độ dài 05 năm khi có độ dài dữ liệu ít hơn 20 quý liên tiếp tính đến thời điểm Tháng 10/2024 (dữ liệu theo quý đầu tiên là từ sau Q1.2020)."
  > — PL3.3.2 (bước 2) ^pl3-lc-2

- Khung 10 năm: tổn thất ròng năm 2015 (X1) bằng tổng bốn quý Q4.2014, Q1.2015, Q2.2015, Q3.2015; tương tự cho X2 (2016) đến X10 (2024). LC bằng tổng X1 đến X10 chia 10, nhân 15.
  > "Trường hợp ngân hàng có khung thời gian tính toán 10 năm:"
  > "Tính giá trị tổn thất hoạt động ròng năm 2015:"
  > "X1 = X<sub>Q4.2014</sub> + X<sub>Q1.2015</sub> + X<sub>Q2.2015</sub> + X<sub>Q3.2015</sub>"
  > "Tính giá trị tổn thất hoạt động ròng năm 2016 (X2); 2017 (X3)... 2024 (X10)"
  > — PL3.3.2 (bước 3, 10 năm) ^pl3-lc-3

- Khung từ 05 năm đến dưới 10 năm: LC bằng tổng tổn thất ròng theo năm của n năm chia n, nhân 15. n bằng số quý thực tế chia 4; phần thập phân từ 0,5 trở lên làm tròn thành 1.
  > "Trường hợp ngân hàng có khung thời gian tính toán từ 05 năm đến dưới 10 năm:"
  > "Tính giá trị tổn thất hoạt động ròng theo năm của các năm trong khung thời gian tính toán"
  > "Trong đó: n là số năm tính toán, được xác định bằng số quý thực tế chia cho 4 (trường hợp kết quả phép tính có phần thập phân từ 0,5 trở lên được làm tròn thành 1)."
  > — PL3.3.2 (bước 3, 05 đến dưới 10 năm) ^pl3-lc-n

## Node bị ảnh hưởng
- Tạo mới: [[tt14-2025]], [[capital-adequacy-ratio]], [[own-funds]], [[capital-conservation-buffer]], [[countercyclical-capital-buffer]], [[capital-adequacy-management]], [[market-risk-capital-requirement]], [[operational-risk-capital-requirement]], [[business-indicator-component]], [[business-indicator]], [[internal-loss-multiplier]], [[loss-component]], [[operational-loss-data]], [[operational-loss-event-dates]], [[common-equity-tier-1-capital]], [[additional-tier-1-capital]], [[tier-2-capital]], [[capital-deductions]], [[additional-tier-1-instrument-conditions]], [[subordinated-debt]], [[interest-leases-and-dividend-component]], [[services-component]], [[financial-component]], [[interest-earning-assets]].
- Cập nhật: [[banking-book]] (định nghĩa sổ ngân hàng, sổ kinh doanh theo Đ2.23–25; quy tắc chuyển sổ Đ73.2), [[market-risk-management]], [[operational-risk-management]], [[capital-adequacy-ratio]].

## Mâu thuẫn ghi nhận
> [!conflict] ILDC: 2,25% hay 2,25 lần tài sản tạo lãi (PL3)
> - Bảng 24 ghi "min (│Thu nhập lãi và các khoản thu nhập tương tự - Chi phí lãi và các chi phí tương tự│; 2,25%*Tài sản tạo lãi)" [[src-tt14-2025-nhnn#^pl3-1-ildc]].
> - Ví dụ PL3.3.1 ghi "2,25 lần giá trị trung bình 3 năm của Tài sản tạo lãi" [[src-tt14-2025-nhnn#^pl3-3-ildc3]].
> - Hai câu cùng văn bản nói khác nhau về hệ số (2,25% so với 2,25 lần, chênh 100 lần). Giữ cả hai; chưa kết luận. Cần đối chiếu pdf hoặc docx gốc.

Ngoài callout trên, không có. Định nghĩa sổ ngân hàng và sổ kinh doanh tại Đ2.24–25 có cùng cấu trúc bốn nhóm với TT83/2025 Đ3 [[src-tt83-2025-nhnn#^d3-32]] [[src-tt83-2025-nhnn#^d3-33]]; chỉ khác số khoản dẫn chiếu nội bộ (khoản 24 so với khoản 32).

## Ghi chú convert
- Công thức Đ5.1 giữ nguyên dạng LaTeX của raw. Raw ghi K<sub>OR</sub>, K<sub>MR</sub> bằng thẻ HTML; dòng "Trong đó" của claim `^d5-1d` trích dạng đã bỏ thẻ.
- Bảng CCB (Bảng 1) chép lại nguyên giá trị từ raw dòng 331–336.
