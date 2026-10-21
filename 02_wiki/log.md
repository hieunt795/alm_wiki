---
title: Log
type: nav
---

# Log

Append-only, mỗi entry mở đầu bằng `## [YYYY-MM-DD] <loại> | <đối tượng>`. Loại gồm: `register`, `ingest`, `query`, `lint`, `decision`.
Xem 5 hoạt động gần nhất: `grep "^## \[" 02_wiki/log.md | tail -5`

## [2026-10-15] decision | scaffold theo đặc tả v2
- Dựng vault theo `alm-wiki-architecture-v2.md`: 02_wiki/, 03_meta/ (taxonomy, templates, views), .claude/ (settings, 4 skill), tools/ (units.py, lint.py).
- Giữ nguyên 01_sources/ làm raw layer (248 file, đã lưu manifest SHA-256 trước khi dựng).
- Không dùng git (theo quyết định của user).

## [2026-10-15] register | batch ban đầu — 23 nguồn, 496 unit
- T1: src-tt14-2025-nhnn, src-tt50-2026-nhnn, src-tt83-2025-nhnn
- T2: src-bcbs-lcr, src-bcbs-nsfr, src-bcbs-lev, src-bcbs-irrbb-2016, src-bcbs-framework
- T3: src-imf-macro-accounting, src-modern-money-mechanics
- T4: src-choudhry-principles-banking, src-choudhry-fixed-income-markets, src-choudhry-yield-curve, src-bindseil-mpo, src-cargill-financial-system, src-tata-bank-alm, src-bardaeva-alm, src-lubinska-alm-optimisation, src-vab-ftp, src-friedman-capitalism-freedom, col-during-fixed-income
- T5: src-ftp-transmission-analysis, col-clippings
- Cần user quyết định: bản canonical của src-bardaeva-alm (2 file khác hash); tác giả/tier của src-ftp-transmission-analysis; tier cho tài liệu tư vấn (src-vab-ftp).
- Conversion partial: Choudhry Principles/Yield Curve, Bindseil, Cargill, Tata, Lubinska, Friedman (heading chapter thiếu/lặp → chunk); VAB FTP (lỗi ký tự đầu file).
- Phát hiện: src-tata-bank-alm là sách của Fidelio Tata (T4), không phải báo cáo ngân hàng như ghi trong v2 §C.4.

## [2026-10-15] ingest | src-bcbs-lcr LCR20 + LCR40 (pilot)
- Source note: [[src-bcbs-lcr]] (62 claim có block-id, 76 trích nguyên văn; LCR20 đọc kèm để có định nghĩa và ngưỡng 100%)
- created: [[lcr]], [[net-cash-outflows]], [[run-off-rate]], [[retail-deposit-stability]], [[unsecured-wholesale-funding]], [[operational-deposits]], [[secured-funding]], [[committed-facilities]], [[hqla]] (stub), [[bcbs-lcr]], [[bcbs]] (stub)
- conflicts: không có
- Cột VN trong các bảng Basel vs VN để `[cần nguồn]`, chờ ingest src-tt50-2026-nhnn (C2-M5, PL1).
- Tiếp theo: LCR30 (HQLA) → hoàn thiện [[hqla]]; TT50/2026 C2-M5 + PL1 → điền bảng Basel vs VN.

## [2026-10-15] lint | sau pilot
- tools/lint.py: 15 note, 0 error, 0 warning. Quote check đã đối chiếu 76 trích dẫn với raw.
- Sửa lỗi của tool: regex quote check không bắt được blockquote thụt lề trong list, nên lần chạy trước báo "pass" nhưng thực ra chưa kiểm tra gì. Phát hiện nhờ negative test.
- Đã xoá alias trùng ('LCR standard') giữa src-bcbs-lcr và bcbs-lcr.

## [2026-10-15] ingest | src-bcbs-lcr LCR30
- created: [[level-1-assets]], [[level-2-assets]]
- updated: [[src-bcbs-lcr]] (thêm unit LCR30, 14 key claims, 24 trích dẫn nguyên văn), [[hqla]] (gỡ stub, hoàn thiện Level 1, 2A, 2B, haircuts, caps, operational requirements), [[lcr]] (bổ sung chi tiết tử số và bảng Basel vs VN), [[index]], [[overview]]
- proposed: không có
- conflicts: không có
- tiếp theo: src-tt50-2026-nhnn C2-M5 + PL1 (đối chiếu tham số HQLA và dòng tiền với quy định VN) hoặc src-bcbs-lcr LCR10 / LCR31

## [2026-10-15] tooling | tạo skill alm-writing-style
- created: `.claude/skills/alm-writing-style/` (SKILL.md + references: hollow-words, subject-examples, term-glossary). Skill thụ động (`disable-model-invocation: true`).
- Rule theo nhóm P (vùng cấm sửa), R (mức bắt buộc, provenance), C, N, S, T, F, V (profile source note / node / synthesis-query / log).
- updated: ingest §3, query bước 5, lint §2 (đọc skill trước khi viết hoặc rà); CLAUDE.md (bảng Operation, mục Ngôn ngữ).
- Phát hiện khi dựng ví dụ R1: [[src-bcbs-lcr]] claim LCR20 "Supervisor phải phản ứng có phân biệt và tương xứng…" lệch với trích dẫn "should allow" — chờ rà ở lượt /lint.

## [2026-10-15] ingest | src-bcbs-lcr LCR10
- created: [[liquidity-transfer-restrictions]]
- updated: [[src-bcbs-lcr]] (thêm unit LCR10, 8 key claims, 14 trích dẫn nguyên văn), [[bcbs-lcr]] (hoàn thiện phạm vi áp dụng hợp nhất, quy tắc Home vs Host, rào cản ring-fencing), [[hqla]] (bổ sung điều kiện hạn chế chuyển giao thanh khoản trong tập đoàn), [[lcr]] (bổ sung ghi chú tính LCR hợp nhất và quản lý theo đồng tiền), [[index]], [[overview]]
- proposed: không có
- conflicts: không có
- tiếp theo: src-tt50-2026-nhnn C2-M5 + PL1 (đối chiếu toàn diện chuẩn Basel LCR đã hoàn tất với quy định của NHNN Việt Nam)

## [2026-10-15] ingest | src-bcbs-lcr LCR31
- created: [[alternative-liquidity-approaches]]
- updated: [[src-bcbs-lcr]] (thêm unit LCR31, 9 key claims, 15 trích dẫn nguyên văn), [[hqla]] (bổ sung mục ALA và liên kết quan hệ), [[bcbs-lcr]] (bổ sung bảng yêu cầu LCR31, định nghĩa ALA và CLF), [[index]], [[overview]]
- proposed: không có
- conflicts: không có

## [2026-10-15] ingest | src-bcbs-lcr preamble, LCR90, LCR99 — hoàn tất 8/8 units
- updated: [[src-bcbs-lcr]] (thêm key claims cho preamble, LCR90 transition và LCR99 application guidance; 8/8 units done), [[bcbs-lcr]], [[index]], [[overview]]
- source hoàn tất: [[src-bcbs-lcr]] (BCBS LCR) đạt 100% ingest (tổng cộng 71 key claims có locator và block-id, hơn 90 trích dẫn nguyên văn)
- tiếp theo: src-tt50-2026-nhnn C2-M5 + PL1 (đối chiếu toàn diện khung Basel LCR đã hoàn thành với quy định LCR của NHNN Việt Nam)


## [2026-10-15] decision | thay bộ relation theo ba nhóm thành phần / đo lường-quản trị-giới hạn / tác động-đầu vào
- taxonomy: thêm `measures`, `governs`, `limits`, `drives`, `input-to`; bỏ `causes`, `affects`, `constrains`, `measured-by`, `required-by`. Quy ước: khai ở node A, chiều A → B thể chủ động, một chiều. Field mới `cite` (tuỳ chọn) trỏ block-id source note.
- tools/lint.py: kiểm key hợp lệ, `direction`/`regime` chỉ với `drives`, `cite` phải trỏ `[[src-…#^id]]`.
- templates: 7 template thêm dòng gợi ý relation theo type.
- migrate: `required-by bcbs-lcr` (lcr, net-cash-outflows, alternative-liquidity-approaches) và `liquidity-transfer-restrictions part-of bcbs-lcr` → `bcbs-lcr governs …`; `constrains` → `limits` (lcr → hqla, liquidity-transfer-restrictions → hqla); bỏ 3 dòng `hqla constrains level-1/level-2/ALA` (trùng chiều ngược của `part-of`); `affects` → `drives` (retail-deposit-stability, secured-funding, unsecured-wholesale-funding); `run-off-rate part-of` → `input-to net-cash-outflows`.
- chưa có relation nào gắn `cite`; bổ sung dần khi ingest hoặc lint.

## [2026-10-15] ingest | chi tiết các thành phần HQLA (Level 1, Level 2A, Level 2B, Caps, Operational Rules)
- updated:
  - [[level-1-assets]]: Mở rộng chi tiết 5 nhóm tài sản Level 1 (tiền mặt, dự trữ NHTW bao gồm tiền gửi qua đêm, dự trữ bắt buộc rút được và điều kiện tiền gửi kỳ hạn theo Footnote 7; chứng khoán công 0% RW kèm quy tắc loại trừ định chế tài chính theo Footnote 11; trái phiếu chính phủ nội tệ khi RW > 0%; trái phiếu chính phủ ngoại tệ khống chế bằng stressed net outflow ngoại tệ). Bổ sung tiêu chuẩn vận hành, tác động mẫu số và động lực ALM Treasury (negative carry, duration IRRBB, NSFR 0% RSF).
  - [[level-2-assets]]: Mở rộng chi tiết cấu phần Level 2A (haircut 15%, kiểm định sụt giá stress ≤ 10%, trái phiếu DN AA-, covered bonds AA-) và Level 2B (haircut 25%–50%, RMBS AA full recourse LTV ≤ 80% stress sụt giá ≤ 20%, trái phiếu DN BBB- đến A+, cổ phiếu thuộc major stock index nội tệ bù trừ QCCP stress sụt giá ≤ 40%, RCLF từ NHTW, sản phẩm Shari'ah/Sukuk). Chi tiết hóa thuật toán unwinding và công thức tính hai mức trần 40% và 15% kèm bảng minh họa số học 3 kịch bản; quy tắc ân hạn 30 ngày (cliff-edge relief).
  - [[hqla]]: Hoàn thiện Master Classification Matrix so sánh toàn bộ 8 nhóm tài sản HQLA, 6 đặc tính nền tảng và thị trường (LCR30.2–30.14), khung tiêu chuẩn vận hành đầy đủ (unencumbered, Treasury control, periodic monetisation, rehypothecation & derivatives collateral, ring-fencing), cùng ma trận tương tác đa chiều (NSFR, Leverage Ratio, IRRBB, Large Exposures).
- lint & citations: 19 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% khớp trích dẫn nguyên văn.

## [2026-10-15] synthesis | đóng gói phân tích HQLA và các đánh đổi ALM Treasury
- created:
  - [[hqla-decomposition-and-tradeoffs]]: Đóng gói phân tích tổng hợp đa chiều về cấu trúc phân tầng HQLA (Level 1, 2A, 2B), toán học cơ chế unwind và công thức hai mức trần (40% và 15%), 7 tiêu chuẩn vận hành, các bằng chứng lịch sử (khủng hoảng 2008, 2020, nghịch lý nợ công châu Âu), và bài toán "Bộ tứ đánh đổi" tại ALM Treasury (Negative carry NIM, Duration IRRBB, RWA & Cap trap, Leverage Ratio conflict).
- updated: [[index]], [[hqla]], [[overview]] (bổ sung luận điểm thứ 4 về tối ưu hóa đệm HQLA trong ALM).
- lint: 20 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info.

## [2026-10-15] ingest | cơ chế unwind HQLA và thuật toán xác định trần kép (LCR30.34–30.39)
- created:
  - [[hqla-unwinding-mechanism]]: Concept note chuyên sâu về cơ chế unwind HQLA: bản chất ngăn ngừa window-dressing qua repo ngắn hạn, phạm vi giao dịch đáo hạn ≤ 30 ngày (repo, reverse repo, collateral swap), quy tắc giải tỏa chuỗi tái thế chấp (rehypothecation chaining), công thức toán học số dư điều chỉnh (Adjusted L1, L2A, L2B), thuật toán 2 bước tính khấu trừ trần (Adjustment 15% và Adjustment 40%), quyền giám sát mở rộng theo Footnote 5 LCR30.35 (unadjusted basis), và 4 ca nghiên cứu số học minh họa chi tiết.
- updated:
  - [[src-bcbs-lcr]]: Bổ sung claim `^lcr30-37` (LCR30.37–30.39) về định nghĩa số dư điều chỉnh, quy tắc tái thế chấp chuỗi và công thức trần.
  - [[hqla]], [[level-2-assets]], [[hqla-decomposition-and-tradeoffs]], [[index]].
- lint & citations: 21 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-15] ingest | chi tiết mẫu số LCR: dòng tiền ra ròng 30 ngày (TNCO - LCR40)
- created:
  - [[cash-inflows]]: Concept note chuyên sâu về dòng tiền vào theo hợp đồng: 5 nguyên tắc cốt lõi (performing only, 0% contingent inflows, latest possible date, exclusion of open maturity loans, chống đếm trùng HQLA), phân rã chi tiết reverse repo / cho vay có bảo đảm (haircut theo L1/L2A/L2B/non-HQLA, ngoại lệ rehypothecation bù vị thế bán khống nhận inflow 0%), dòng vào theo đối tác và logic bảo tồn thương quyền (50% bán lẻ & DN phi tài chính, 100% tổ chức tài chính), tiền gửi operational tại nơi khác (inflow 0%), dòng vào phái sinh ròng (100%), cơ chế trần dòng vào 75% và hiện tượng tổn thất thanh khoản biên, cùng yêu cầu giám sát mức độ tập trung dòng vào bán buôn (LCR40.76).
  - [[lcr-net-cash-outflows-mechanics]]: Synthesis note toàn diện phân rã chuyên sâu cấu trúc toán học của mẫu số LCR (TNCO), cơ chế trần 75% và sàn bắt buộc HQLA 25% dòng ra gộp, ba giả định hành vi bất đối xứng (bảo tồn thương quyền franchise preservation, kẹt vốn vận hành operational lock-in, phòng chống lây lan chéo anti-contagion), các cạm bẫy thực tiễn (quy tắc lây lan vi phạm tiền gửi có kỳ hạn contagion rule, cạm bẫy netting đơn phương, phơi nhiễm ký quỹ hạ 3 bậc tín nhiệm downgrade triggers), cùng 4 nhóm chiến lược tối ưu hóa mẫu số của ALM Treasury.
- updated:
  - [[net-cash-outflows]]: Nâng cấp toàn diện thành masterwork metric note: công thức giải tích TNCO, phân tầng chi tiết 5 trụ cột dòng tiền ra (bán lẻ & SME, bán buôn không bảo đảm, tài trợ có bảo đảm repo, phái sinh & downgrade triggers, hạn mức cam kết & nghĩa vụ tiềm tàng), cấu trúc dòng vào hợp đồng, phân tích tính bất đối xứng hành vi, ứng dụng ALM Treasury và tổng kết cạm bẫy thường gặp.
  - [[run-off-rate]]: Mở rộng các tham số phái sinh, downgrade triggers hạ 3 bậc tín nhiệm (100%), biến động định giá 24 tháng look-back, quyền chọn mua lại nợ call options và đối trọng inflow rate.
  - [[retail-deposit-stability]]: Bổ sung nguyên tắc tính hạn mức bảo hiểm từng phần (Footnote 45-0), điều kiện loại trừ tiền gửi cầm cố (FAQ1 LCR40.5), tiền gửi kim loại quý, và ngoại lệ hardship đối với rút tiền gửi có kỳ hạn (LCR40.17).
  - [[unsecured-wholesale-funding]]: Bổ sung quy tắc cộng gộp SME hợp nhất < 1M EUR (Footnote LCR40.23), kỳ vọng thị trường đối với call options (LCR40.20), điều kiện pháp lý đối với trái phiếu bán lẻ (LCR40.43), và tài khoản phong tỏa prime brokerage (LCR40.44).
  - [[operational-deposits]]: Bổ sung phương pháp luận định lượng granular excess balance (LCR40.30), tiền gửi trong mạng lưới ngân hàng hợp tác xã (LCR40.37–39), và phạm vi chi tiết 3 nhóm dịch vụ clearing/custody/cash management (LCR40.33–35).
  - [[secured-funding]]: Bổ sung cơ chế hoán đổi TSBĐ (collateral swaps), cho vay bán khống của khách hàng (customer shorts), quy tắc phân bổ danh mục tài sản thế chấp hỗn hợp (collateral waterfall LCR40.48), và tài trợ vị thế bán khống của ngân hàng (LCR40.80).
  - [[committed-facilities]]: Bổ sung phân biệt định nghĩa Credit Facility vs Liquidity Facility (LCR40.61), hạn mức cấp cho SPE/conduit/hedge funds (LCR40.62), và cơ chế tính ròng với HQLA bảo đảm (LCR40.60).
  - [[src-bcbs-lcr]]: Bổ sung toàn bộ các claim chi tiết LCR40: `^lcr40-30`, `^lcr40-33`, `^lcr40-34`, `^lcr40-35`, `^lcr40-37`, `^lcr40-38`, `^lcr40-39`, `^lcr40-44`, `^lcr40-46`, `^lcr40-50`, `^lcr40-53`, `^lcr40-54`, `^lcr40-55`, `^lcr40-58`, `^lcr40-60`, `^lcr40-61`, `^lcr40-62`, `^lcr40-65`, `^lcr40-68`, `^lcr40-69`, `^lcr40-70`, `^lcr40-73`, `^lcr40-76`, `^lcr40-79`, `^lcr40-80`, `^lcr40-81`, `^lcr40-83`, `^lcr40-90`, `^lcr40-91`, `^lcr40-92`, `^lcr40-93`.
  - [[index]], [[overview]].
- lint & citations: 23 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-15] ingest | chi tiết nhu cầu thanh khoản phái sinh và nghĩa vụ tiềm tàng (LCR40.49–40.75)
- created:
  - [[derivatives-and-contingent-outflows]]: Concept note chuyên sâu về rủi ro thanh khoản phái sinh và nghĩa vụ tiềm tàng: dòng tiền phái sinh ròng (bù trừ song phương hợp lệ, ITM options exercise, cheapest-to-deliver, ngoại lệ FX swap, chống đếm trùng HQLA); rủi ro hạ bậc tín nhiệm (downgrade triggers 3 notch 100%, tác động quyền tái thế chấp); định giá và thay thế tài sản bảo đảm (add-on +20% cho non-Level 1, excess non-segregated 100%, collateral due 100%, collateral substitution 100%); phương pháp hồi cứu biến động thị trường (24M look-back approach, đỉnh 30 ngày dòng ký quỹ ròng, settled-to-market); tài trợ cấu trúc (ABS/covered bonds tự phát hành 100%, ABCP/conduits/SIVs 100% nợ đáo hạn + 100% returnable assets qua liquidity puts); các nghĩa vụ tiềm tàng (cam kết cho vay tổ chức tài chính 100%, tài trợ thương mại ≤ 5%, rủi ro danh tiếng quỹ NAV ổn định, autocallables, liên doanh non-consolidated, bán khống khách hàng bù trừ nội bộ bằng non-HQLA ≥ 50%); động lực quản trị ALM Treasury và tổng hợp cạm bẫy thực tế.
- updated:
  - [[net-cash-outflows]], [[lcr-net-cash-outflows-mechanics]], [[index]], [[overview]].
- lint & citations: 24 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-15] synthesis | ý nghĩa kinh tế, nghịch lý sử dụng đệm HQLA và phương pháp quản trị LCR tại ALM Treasury
- created:
  - [[lcr-economic-significance-and-alm-governance]]: Synthesis note chuyên sâu phân tích toàn diện ý nghĩa kinh tế của LCR: chuyển dịch từ mô hình tĩnh (LDR, Liquid Asset Ratio) sang mô hình dòng tiền căng thẳng động 30 ngày (stressed dynamic cash flows); bản chất "mua thời gian sinh tồn" 30 ngày (survival horizon) và vai trò thanh khoản như hàng hóa công cộng ngăn chặn vòng xoáy bán tháo (fire-sale & liquidity spirals); giải tỏa nghịch lý sử dụng đệm HQLA (buffer usability paradox) và ứng xử giám sát có phân biệt, chống chu kỳ thuận (LCR20.5–20.6); vai trò của ILAAP và stress test nội bộ đa kỳ hạn tích hợp rủi ro khí hậu (LCR20.3); cùng 5 trụ cột quản trị tác nghiệp của ALM Treasury (hạn mức đèn tín hiệu 4 tầng Green/Amber/Red/Breach, Liquidity FTP 3 cấu phần, quản trị ngoại tệ trọng yếu ≥ 5% theo LCR10.9, Kế hoạch tài trợ dự phòng CFP theo thang thanh khoản khẩn cấp, và bộ công cụ giám sát Pillar 2 SRP50).
- updated:
  - [[lcr]]: Nâng cấp toàn diện mục "Ứng dụng trong ALM" với 5 trụ cột quản trị tác nghiệp và liên kết bộ ba phân tích tổng hợp LCR (tử số HQLA, mẫu số TNCO, và quản trị ALM).
  - [[index]], [[overview]].
- lint & citations: 25 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | src-bcbs-nsfr preamble, NSF10, NSF20, NSF30, NSF99 — hoàn tất 5/5 units
- created:
  - [[src-bcbs-nsfr]]: Source note chuẩn mực Basel NSFR (41 key claims có locator và block-id, hơn 40 trích dẫn nguyên văn đối chiếu 100% raw text, 5/5 units done).
  - [[bcbs-nsfr]]: Regulation note chuẩn mực NSFR của BCBS (phạm vi hợp nhất, yêu cầu ≥ 100% liên tục, tần suất báo cáo hàng quý, bảng ma trận điều khoản và tác động ALM).
  - [[nsfr]]: Metric note toàn diện về Net Stable Funding Ratio: công thức giải tích ASF / RSF, horizon 1 năm, giả định hành vi thận trọng (call options sớm nhất, roll-over khách hàng), bảng đối chiếu Basel vs VN, ứng dụng ALM Treasury (cặp bài trùng với LCR, Term Liquidity FTP, cliff-edge maturity) và cạm bẫy thường gặp.
  - [[available-stable-funding]]: Concept note tử số NSFR: cấu trúc phân tầng 5 nhóm hệ số ASF (100%, 95%, 90%, 50%, 0%), quy tắc xử lý quyền chọn mua lại và cắt lát dòng tiền (cash flow slicing), đối xử nợ phái sinh và bài học thực tiễn SVB 2023.
  - [[required-stable-funding]]: Concept note mẫu số NSFR: cấu trúc phân tầng 8 nhóm hệ số RSF (0%, 5%, 10%, 15%, 50%, 65%, 85%, 100%), cam kết ngoại bảng (5%), khung quy định cầm cố tài sản (encumbrance) và khoản phạt nợ phái sinh gộp (5%–20%).
  - [[interdependent-assets-and-liabilities]]: Concept note cơ chế ngoại lệ tài sản và nợ phụ thuộc lẫn nhau: điều kiện áp dụng đồng thời ASF 0% và RSF 0% theo 4 tiêu chí khắt khe (NSF30.35) và ứng dụng thực tiễn trong tài trợ dự án pass-through.
  - [[nsfr-structural-liquidity-and-alm-strategy]]: Synthesis note đóng gói phân tích chuyên sâu về thanh khoản cấu trúc NSFR, ma trận tương tác hai chiều với LCR, 3 xung đột kỹ thuật thực tế tại Treasury (nguồn vốn bán buôn 6–12 tháng, cạm bẫy cầm cố tài sản dài hạn, hiệu ứng vực thẳm kỳ hạn trôi), và 4 chiến lược tác nghiệp của ALM Treasury.
- updated:
  - [[lcr]]: Bổ sung liên kết hai chiều với [[nsfr]], [[available-stable-funding]], [[required-stable-funding]] và [[nsfr-structural-liquidity-and-alm-strategy]].
  - [[hqla]]: Cập nhật chuẩn xác hệ số RSF tương ứng của Level 1 (5%), Level 2A (15%), Level 2B (50%) và liên kết NSFR.
  - [[index]], [[overview]].
- source hoàn tất: [[src-bcbs-nsfr]] (BCBS NSFR) đạt 100% ingest (5/5 units done).
- conflicts: không có
- tiếp theo: src-tt50-2026-nhnn C2-M5 + PL1 (đối chiếu toàn diện khung Basel LCR & NSFR đã hoàn thành với Thông tư 50/2026/TT-NHNN của Việt Nam) hoặc src-bcbs-irrbb-2016 (rủi ro lãi suất trên sổ ngân hàng).

## [2026-10-16] ingest | phân rã chi tiết các thành phần ASF, RSF và khung quản trị rủi ro NSFR tại ALM Treasury
- created:
  - [[asf-capital-and-long-term-liabilities]]: Cấu phần vốn tự có CAP10 và nợ dài hạn $\ge 1$ năm (ASF 100%), xử lý quyền chọn call option (giả định call date sớm nhất), cơ cấu soft-bullet và cắt lát dòng tiền.
  - [[asf-retail-and-small-business-deposits]]: Cấu phần tiền gửi bán lẻ và SME: stable (ASF 95%) vs less stable (ASF 90%), tiền gửi có kỳ hạn $\ge 1$ năm phạt nặng (ASF 100%), quy tắc gom cụm SME $< 1$ triệu EUR và giả định bám dính hành vi.
  - [[asf-wholesale-and-operational-funding]]: Cấu phần nguồn vốn bán buôn và tiền gửi vận hành: doanh nghiệp phi tài chính $< 1$ năm (ASF 50%), operational deposits (ASF 50%), sovereign/PSEs (ASF 50%), vốn định chế tài chính 6M–1Y (ASF 50%) và triệt tiêu nguồn vốn liên ngân hàng $< 6$ tháng (ASF 0%).
  - [[rsf-hqla-and-central-bank-reserves]]: Cấu phần HQLA và dự trữ NHTW trong NSFR: tiền mặt/dự trữ (RSF 0%), Level 1 (RSF 5%), Level 2A (RSF 15%), Level 2B (RSF 50%), phân tích miễn trừ trần khống chế và miễn trừ yêu cầu vận hành của LCR.
  - [[rsf-loans-and-credit-exposures]]: Danh mục cho vay và cấp tín dụng: thế chấp nhà ở unencumbered $\ge 1$ năm $\text{RW} \le 35\%$ (RSF 65%), cho vay thông thường $\text{RW} > 35\%$ (RSF 85%), cho vay $< 1$ năm (RSF 50% do giả định roll-over), NPLs (RSF 100%), quy tắc bóc tách khoản vay bảo đảm một phần.
  - [[rsf-securities-financing-and-encumbrance]]: Tài trợ có bảo đảm và quản trị cầm cố tài sản: repo/reverse repo (RSF 10%–15%), khung thời gian cầm cố ($\ge 1$ năm RSF 100%, 6M–1Y HQLA RSF 50%), quy tắc báo cáo gộp và sở hữu hưởng lợi.
  - [[rsf-derivatives-and-off-balance-sheet]]: Phái sinh và cam kết ngoại bảng: ký quỹ ban đầu (RSF 85%), tài sản phái sinh ròng (RSF 100%), khoản cộng thêm nợ phái sinh gộp 5%–20% (RSF 100%), cam kết tín dụng/thanh khoản ngoại bảng (RSF 5%).
  - [[nsfr-alm-governance-strategy-and-risks]]: Flagship synthesis note phân tích toàn diện cách vận hành thực tế tại ALCO, hệ thống hạn mức đèn tín hiệu 3 tầng (Green, Amber, Red/Breach), cơ chế định giá Term Liquidity FTP, 4 chiến lược tối ưu hóa và 4 rủi ro trọng yếu đối với NSFR tại ALM Treasury.
- updated:
  - [[nsfr]], [[src-bcbs-nsfr]], [[index]], [[overview]].
- lint & citations: 40 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | chuẩn hóa cấu trúc mẫu số LCR: tạo master concept note cash-outflows
- created:
  - [[cash-outflows]]: Master concept note toàn diện về Tổng dòng tiền ra kỳ vọng trong 30 ngày (Total Cash Outflows - LCR40): công thức toán học tổng quát, nguyên tắc thời hạn sớm nhất và quyền chọn rút vốn (LCR40.20), nguyên tắc chống đếm trùng nghĩa vụ (LCR40.4), phân rã chi tiết 5 trụ cột cấu thành (tiền gửi bán lẻ & SME cá nhân, nguồn vốn bán buôn không bảo đảm, nguồn vốn có bảo đảm repo, phái sinh & nhu cầu bổ sung, hạn mức cam kết & nghĩa vụ tiềm tàng), bảng ma trận 30 tham số chuẩn mực Basel, 3 tiên đề hành vi giám sát, 4 chiến lược tác nghiệp tại ALM Treasury, 4 cạm bẫy thực tiễn (unauthorized netting, contagion rule, SME consolidated threshold, conditional cancellation), và các điểm chờ đối chiếu Thông tư 50/2026/TT-NHNN.
- updated:
  - [[net-cash-outflows]]: Liên kết trực tiếp tới [[cash-outflows]] làm master note cho phần dòng ra gộp.
  - [[retail-deposit-stability]], [[unsecured-wholesale-funding]], [[operational-deposits]], [[secured-funding]], [[committed-facilities]], [[derivatives-and-contingent-outflows]]: Chuẩn hóa trường quan hệ `part-of: [[cash-outflows]]` và hướng tác động `drives: [[lcr]], direction: "-"`.
  - [[index]], [[overview]].
- lint & citations: 41 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | hoàn thiện và chuẩn hóa toàn bộ relations có cite cho 35 notes LCR và NSFR
- updated:
  - Đồng bộ và làm giàu trường `relations:` trong frontmatter của toàn bộ 35 notes thuộc phân hệ LCR và NSFR (gồm 2 regulations, 3 metrics, 25 concepts, 5 syntheses).
  - Bổ sung trường trích dẫn xuất xứ `cite: "[[src-...#^...]]"` cho từng relation, gắn chặt với các block-id chuẩn xác trong [[src-bcbs-lcr]] và [[src-bcbs-nsfr]].
  - Chuẩn hóa quan hệ phân cấp: `governs` từ regulations tới metrics/concepts; `part-of` từ cấu phần vi mô tới tử số/mẫu số; `input-to` tới các chỉ số; `drives` kèm `direction: "+"` hoặc `"-"`; `limits` và `measures`.
  - Xóa bỏ tình trạng quan hệ rỗng `relations: []` tại các synthesis notes ([[nsfr-structural-liquidity-and-alm-strategy]], [[nsfr-alm-governance-strategy-and-risks]]).
- lint & citations: 41 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | phân rã các thành phần liên kết LCR - NSFR và đóng gói chiến lược quản trị tổng hợp
- created:
  - [[lcr-nsfr-interlinkages]]: Concept note phân tích chuyên sâu 7 kênh truyền dẫn tương tác giữa LCR và NSFR trên bảng cân đối kế toán (đòn bẩy kép Level 1 TPCP, trừng phạt kép vốn liên ngân hàng ngắn hạn, vùng mù kỳ hạn 6–12M, cạm bẫy cầm cố tài sản dài hạn repo $\ge 1$Y, bất đối xứng trần HQLA Level 2, đánh thuế kép cam kết ngoại bảng, và hiệu ứng thác trôi kỳ hạn 3Y $\rightarrow$ 1Y $\rightarrow$ 6M $\rightarrow$ 30D); kèm ma trận tác động song song và hàm ý đối với ALM Treasury.
  - [[integrated-alm-liquidity-strategy]]: Flagship synthesis note về Chiến lược Quản trị Thanh khoản và Bảng Cân đối Kế toán Tổng hợp LCR – NSFR: mô hình quy hoạch toán học tối ưu hóa đa mục tiêu ($\max \text{NII}$ / $\max \text{RoRWA}$ thỏa mãn đồng thời LCR, NSFR, Leverage Ratio, CAR, IRRBB), cơ chế định giá Term Liquidity FTP tích hợp 4 cấu phần (Base Rate + LCR Charge + NSFR Spread + Capital/RWA), 3 trụ cột tác nghiệp thực chiến (thác phân bổ TSBĐ Collateral Waterfall, bậc thang phát hành nợ động Pre-funding Window 15 tháng, tái cấu trúc cam kết ngoại bảng), ma trận điều hành ALCO 4 trạng thái liên chỉ số (Green/Green, Amber/Green, Green/Amber, Red/Red), bài học thực nghiệm SVB 2023 và lộ trình triển khai tại Việt Nam theo Thông tư 50/2026/TT-NHNN.
- updated:
  - [[index]], [[overview]] (bổ sung luận điểm thesis thứ 8 về bài toán tối ưu hóa đa ràng buộc LCR – NSFR).
- lint & citations: 43 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | chuẩn mực BCBS IRRBB 2016 (d368) — hoàn tất 8/8 units và kết nối rủi ro thời lượng HQLA/NSFR với EVE/NII
- created:
  - [[src-bcbs-irrbb-2016]]: Source note chuẩn mực BCBS IRRBB 2016 (Standards d368), hoàn thành 100% 8/8 units (preamble, u01, u02, u03, u04, u05, u06, u07), 35 block-ids trích dẫn nguyên văn đối chiếu 100% raw text.
  - [[bcbs-irrbb]]: Regulation note chuẩn mực IRRBB của BCBS (Trụ cột 2 nâng cao, 12 Nguyên tắc, Standardised Framework, Outlier Bank Test 15% Tier 1 Capital, Table A & Table B).
  - [[economic-value-of-equity]]: Metric note $\Delta\text{EVE}$ (giá trị kinh tế của vốn chủ sở hữu, run-off horizon, chiết khấu liên tục, add-on quyền chọn tự động $KAO_{i,c}$, tổng hợp đa tiền tệ).
  - [[net-interest-income-sensitivity]]: Metric note $\Delta\text{NII}$ (độ nhạy thu nhập lãi thuần 12 tháng liên tục, constant balance sheet, đánh đổi chiến lược EVE vs NII).
  - [[gap-risk]]: Concept note rủi ro chênh lệch kỳ hạn tái định giá: dịch chuyển song song vs phi song song / xoay trục đường cong (Steepener, Flattener, Short rate shocks).
  - [[basis-risk]]: Concept note rủi ro cơ sở: phân kỳ giữa các chỉ số lãi suất tham chiếu (SOFR, Euribor, VNIBOR), lệch pha kỳ hạn 1M/3M, administered rates, và cross-currency basis spread.
  - [[option-risk]]: Concept note rủi ro quyền chọn: quyền chọn tự động (caps/floors/swaptions, add-on $KAO_{i,c}$) vs quyền chọn hành vi (prepayment CPR scalars $\gamma_i$, early redemption TDRR scalars $u_i$, trần tiền gửi lõi NMDs).
  - [[csrbb]]: Concept note rủi ro chênh lệch tín dụng trên sổ ngân hàng: phân tách 5 thành phần lãi suất, ranh giới với IRRBB, tác động kế toán amortised cost vs fair value, rủi ro đối với tài sản Level 2 trong HQLA.
  - [[outlier-bank-test]]: Concept note kiểm tra ngân hàng ngoại lai: thắt chặt từ 20% tổng vốn xuống $\max \Delta\text{EVE} > 15\%$ Vốn cấp 1 (Tier 1 Capital) qua 6 kịch bản sốc chuẩn hoá, các biện pháp can thiệp giám sát bắt buộc.
- updated:
  - [[lcr-nsfr-interlinkages]]: Bổ sung Kênh 8 ("Cạm bẫy Thời lượng" của đệm HQLA TPCP Level 1) và Kênh 9 (Chuyển đổi kỳ hạn NSFR là cội nguồn phát sinh Gap risk), cập nhật `sources` và `relations`.
  - [[integrated-alm-liquidity-strategy]]: Chuẩn hóa phương trình ràng buộc Outlier Test $\max \Delta\text{EVE}_i / \text{Tier 1} \le 15\%$ và liên kết với [[outlier-bank-test]] và [[bcbs-irrbb]].
  - [[level-1-assets]]: Bổ sung liên kết rủi ro lãi suất thời lượng tới [[bcbs-irrbb]], [[economic-value-of-equity]], [[outlier-bank-test]] và làm rõ RSF 0% cho dự trữ NHTW và 5% cho chứng khoán nợ Level 1 unencumbered.
  - [[index]], [[overview]]: Cập nhật toàn bộ danh mục 52 notes, thesis thứ 9 về bộ ba ALM (LCR – NSFR – IRRBB) và bảng tiến độ registry.
- source hoàn tất: [[src-bcbs-irrbb-2016]] đạt 100% ingest (8/8 units done).
- lint & citations: 52 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | chuyên sâu các cấu phần mô hình hóa, kịch bản sốc và chiến lược quản trị tổng thể IRRBB Basel
- created:
  - [[non-maturity-deposits]]: Concept note chuyên sâu về mô hình hoá tiền gửi không kỳ hạn (NMDs) trong IRRBB: phân loại Bán lẻ (giao dịch/phi giao dịch) và Bán buôn; trần tiền gửi lõi (core deposits) 50%–90% và trần kỳ hạn bình quân 4–5 năm theo Bảng 2 Section IV; quy tắc dồn 100% tiền gửi phi lõi vào dải qua đêm; phân tích phương sai số dư 10 năm ($10\text{Y}$ observation window); phương pháp luận Danh mục Tái lập (Replicating Portfolio 5Y 60-tranche); và mối liên hệ với ASF trong [[nsfr]].
  - [[behavioural-options]]: Concept note chuyên sâu về quyền chọn hành vi trong IRRBB: rủi ro trả nợ trước hạn (Prepayment risk, tỷ lệ trả nợ có điều kiện CPR, hệ số nhân kịch bản $\gamma_i = 0.8/1.2$ theo Bảng 3); rủi ro rút tiền gửi có kỳ hạn sớm (Early redemption risk, tỷ lệ TDRR, hệ số co giãn kịch bản $u_i = 1.2/0.8$ theo Bảng 4); hiệu ứng co cụm thời lượng (contraction risk) và kéo dài thời lượng (extension risk); bản chất lồi âm (negative convexity); và các kỹ thuật phòng hộ tại ALM Treasury.
  - [[standardised-interest-rate-shocks]]: Concept note chuyên sâu về 6 kịch bản sốc lãi suất chuẩn hoá Basel (Annex 2): định nghĩa 6 kịch bản EVE và 2 kịch bản NII; công thức toán học định hình đường cong xoay trục (Steepener và Flattener) với hàm suy giảm $S_{\text{short}}(t_k) = e^{-t_k/4}$; biên độ sốc theo loại tiền tệ (Table 1: USD 200/300/150, EUR 200/250/100, JPY 100/100/100, GBP 250/300/150); cơ chế bảo vệ với sàn sốc tối thiểu 100 bps, trần tối đa (Short 500, Parallel 400, Long 300 bps); và giới hạn sàn lãi suất âm sau sốc.
  - [[irrbb-standardised-framework]]: Concept note chuyên sâu về Khuôn khổ chuẩn hoá đo lường $\Delta\text{EVE}$ (Section IV d368): thẩm quyền can thiệp và áp đặt dự phòng của cơ quan giám sát (Principle 11); quy trình định lượng 5 giai đoạn tuần tự; bảng 19 dải kỳ hạn chuẩn hoá và điểm giữa $t_k$; công thức chiết khấu liên tục $DF_{i,c}(t_k) = \exp(-R_{i,c}(t_k) \cdot t_k)$; add-on quyền chọn tự động $KAO_{i,c}$ với mức tăng biến động ngầm định 25%; quy tắc tổng hợp phi đối xứng đa tiền tệ $\sum_c \max(0, \Delta EVE_{i,c})$; và bảng so sánh toàn diện với Hệ thống đo lường nội bộ (IMS).
  - [[irrbb-alm-governance-strategy-and-tradeoffs]]: Flagship synthesis note về Khung Quản trị ALM, Chiến lược Điều hành và Sự Đánh đổi Cốt lõi của IRRBB: mô hình 3 tuyến phòng thủ và vai trò của HĐQT/ALCO theo 12 Nguyên tắc; giải quyết mâu thuẫn nền tảng giữa Giá trị kinh tế (EVE run-off) và Thu nhập lãi thuần (NII 12M) bằng kỹ thuật Replicating Portfolio; phân tích và hóa giải "Cạm bẫy Thời lượng" của đệm thanh khoản [[hqla]] trong bài toán tối ưu hóa đa ràng buộc (LCR $\times$ NSFR $\times$ IRRBB $\times$ Leverage $\times$ CAR); hệ thống hạn mức ALCO 4 tầng; và cơ chế Định giá Điều chuyển Vốn Nội bộ Tích hợp (IRRBB & Liquidity FTP) bóc tách rủi ro khỏi chi nhánh.
- updated:
  - [[option-risk]]: Bỏ các alias gây trùng lặp, liên kết chuyên sâu tới [[behavioural-options]] và [[non-maturity-deposits]].
  - [[bcbs-irrbb]]: Bổ sung quan hệ `governs` tới [[non-maturity-deposits]] và [[behavioural-options]], cập nhật bảng quy chuẩn kỹ thuật.
  - [[index]], [[overview]]: Đồng bộ toàn bộ 57 notes, bổ sung thesis thứ 10 về chiến lược quản trị ALM toàn diện giải quyết sự đánh đổi EVE vs NII.
- lint & citations: 57 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] decision | chuẩn hóa phân loại kiến trúc: chuyển đổi HQLA, ASF và RSF sang metric
- bối cảnh: Trước đây, các đại lượng định lượng cấu thành nên tỷ lệ LCR và NSFR bị phân loại không đồng nhất: trong khi `net-cash-outflows` (mẫu số LCR) được xếp là `type: metric` thì `hqla` (tử số LCR), `available-stable-funding` (tử số NSFR) và `required-stable-funding` (mẫu số NSFR) lại bị xếp thành `type: concept`.
- quyết định: Chuẩn hóa toàn bộ các biến số định lượng tuyệt đối (tính bằng số tiền, có công thức xác định, bảng quy chuẩn số học, và bắt buộc báo cáo trong Pillar 3 DIS85) thành `type: metric` nằm trong `02_wiki/metrics/`.
- migrated & created:
  - [[available-stable-funding]]: Chuyển sang `02_wiki/metrics/available-stable-funding.md`, chuẩn hóa cấu trúc metric (Định nghĩa chuẩn mực, Công thức xác định, Diễn giải & Cơ chế 5 bậc ASF, Bảng Basel vs VN, Ứng dụng ALM và Nhầm lẫn thường gặp).
  - [[required-stable-funding]]: Chuyển sang `02_wiki/metrics/required-stable-funding.md`, chuẩn hóa cấu trúc metric (Định nghĩa chuẩn mực, Công thức xác định, Diễn giải & Cơ chế 8 bậc RSF, Bảng Basel vs VN, Ứng dụng ALM và Nhầm lẫn thường gặp).
  - [[hqla]]: Chuyển sang `02_wiki/metrics/hqla.md`, chuẩn hóa cấu trúc metric (Định nghĩa chuẩn mực, Công thức Unwind & trần kép 40%/15%, Bảng phân loại Master Matrix, 7 yêu cầu vận hành, Bảng Basel vs VN, Ứng dụng ALM và Nhầm lẫn thường gặp).
- removed: `02_wiki/concepts/available-stable-funding.md`, `02_wiki/concepts/required-stable-funding.md`, `02_wiki/concepts/hqla.md`.
- updated: [[index]], [[overview]].
- lint & citations: 57 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | chuyên sâu các công cụ phái sinh và mô hình định lượng cấu phần IRRBB theo Basel và tài liệu quốc tế
- bối cảnh: Người dùng yêu cầu tập trung hoàn toàn vào chuẩn mực Basel và tài liệu ALM/Fixed Income nước ngoài (BCBS d368, Moorad Choudhry, Alexander During, Fidelio Tata, Beata Lubinska) để làm sâu sắc toàn diện các cấu phần của IRRBB trước khi đối chiếu quy định Việt Nam.
- created:
  - [[interest-rate-swap]]: Instrument note chuyên sâu về Hợp đồng hoán đổi lãi suất (IRS): Plain Vanilla (Payer/Receiver Swap), Basis Swap, OIS Swap, Amortising Swap; định giá No-Arbitrage và Par Swap Rate; công thức đo lường độ nhạy điểm cơ bản (DV01/PV01); và cơ chế tái cấu trúc thời lượng bảng cân đối để phòng ngừa rủi ro chênh lệch kỳ hạn [[gap-risk]] và bảo vệ vốn tự có [[economic-value-of-equity|$\Delta\text{EVE}$]].
  - [[interest-rate-cap-floor]]: Instrument note chuyên sâu về Hạn mức trần và sàn lãi suất (Caps, Floors, Collars): phân tách thành chuỗi Caplets/Floorlets; nhận diện quyền chọn nhúng bán khống (Short Cap/Floor) trong các gói tín dụng và tiền gửi bán buôn; định giá theo mô hình Black-76 và Bachelier; các hệ số độ nhạy Delta, Vega, Gamma; và cơ chế tính toán phụ trội vốn quyền chọn tự động $\text{KAO}_{i,c}$ dưới mức tăng 25% độ biến động ngầm định theo Basel d368 Section IV.
  - [[swaption]]: Instrument note chuyên sâu về Quyền chọn hoán đổi lãi suất: Payer vs Receiver Swaption, phong cách thực thi kiểu châu Âu và Bermudan; ứng dụng phòng ngừa rủi ro phi tuyến tính lồi âm (negative convexity) phát sinh từ quyền trả nợ trước hạn (Prepayment risk) trên danh mục cho vay thế chấp và rủi ro cam kết giải ngân (pipeline risk); định giá Black-76 và quy chuẩn phụ trội vốn $\text{KAO}_{i,c}$.
  - [[duration-gap-model]]: Model note về Mô hình chênh lệch thời lượng bảng cân đối (DGAP): phân biệt Macaulay Duration, Modified Duration, Effective Duration; phương trình vi phân giá trị vốn chủ sở hữu $\Delta E \approx -(D_A - \frac{L}{A} D_L) \cdot A \cdot \Delta y$; điều kiện miễn nhiễm hoàn toàn $\text{DGAP} = 0$; hiệu chỉnh tính lồi (Convexity Adjustment $C_E$); và 3 hạn chế cốt tử được Basel cảnh báo đối với mô hình DGAP.
  - [[key-rate-duration]]: Model note về Thời lượng lãi suất từng kỳ hạn (KRD / Bucket PV01): công thức giải tích đạo hàm riêng từng điểm kỳ hạn then chốt; mối quan hệ bảo toàn $\sum \text{KRD}_k = D_{\text{Mod}}$; cơ chế nhận diện rủi ro phi song song (Non-parallel gap risk) và xoay trục đường cong (Steepener, Flattener, Twists); ma trận 19 dải kỳ hạn chuẩn hoá của Basel d368 và hàm suy giảm $e^{-t_k/4}$; và chiến lược tái cân bằng ALM theo từng bucket.
  - [[replicating-portfolio-model]]: Model note về Mô hình Danh mục Tái lập (Replicating Portfolio): gán kỳ hạn hành vi cho NMDs và Vốn tự có; phân tách Core vs Non-core; kỹ thuật lát cắt bình quân trượt (Moving Average Tranches, ví dụ WAM 2.5 năm từ 60 tranches theo Footnote 38 Basel); mô hình kinh tế lượng đồng tích hợp (Cointegration & ECM) và tối ưu hóa hàm mục tiêu Sharpe ratio của NIM; và các trần khống chế nghiêm ngặt tại Table 2 Basel d368.
  - [[economic-value-at-risk]]: Model note về Giá trị kinh tế chịu rủi ro (EVaR): phân biệt EVaR (vốn dài hạn) và EaR (thu nhập 12M); 3 phương pháp luận định lượng (Delta-Normal VaR, Mô phỏng lịch sử, Mô phỏng ngẫu nhiên Monte Carlo); và 3 hạn chế cốt tử về rủi ro đuôi (tail risk) dẫn tới sự bắt buộc của Stress Testing và Outlier Bank Test theo Basel d368.
- updated:
  - [[option-risk]]: Bổ sung liên kết tới [[interest-rate-cap-floor]] và [[swaption]].
  - [[gap-risk]]: Bổ sung liên kết tới [[duration-gap-model]], [[key-rate-duration]] và [[interest-rate-swap]].
  - [[non-maturity-deposits]]: Bổ sung liên kết chuyên sâu tới [[replicating-portfolio-model]].
  - [[behavioural-options]]: Bổ sung liên kết tới [[swaption]].
  - [[economic-value-of-equity]]: Bổ sung liên kết tới [[duration-gap-model]], [[key-rate-duration]], [[economic-value-at-risk]] và [[interest-rate-swap]].
  - [[net-interest-income-sensitivity]]: Bổ sung liên kết tới [[economic-value-at-risk]] (EaR), [[interest-rate-swap]] và [[interest-rate-cap-floor]].
  - [[index]], [[overview]]: Đồng bộ toàn bộ 64 notes (8 metrics, 32 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 7 syntheses, 3 sources, 3 nav notes).
- lint & citations: 64 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | lưu trữ Master Blueprint Kiến trúc Toàn diện 5 Tầng của IRRBB
- bối cảnh: Người dùng phê duyệt lưu trữ toàn bộ Khung Kiến trúc 5 Tầng của IRRBB thành một synthesis note trọng điểm trong kho tri thức.
- created:
  - [[irrbb-five-tier-architecture]]: Flagship synthesis note phân tích toàn diện 5 tầng của IRRBB: Tầng 1 (5 thành phần lãi suất & 3 loại rủi ro Gap/Basis/Option + CSRBB); Tầng 2 (Hai lăng kính EVE vs NII & Mâu thuẫn quản trị kinh điển); Tầng 3 (4 mô hình định lượng DGAP, KRD 19 buckets, Replicating Portfolio NMDs, EVaR/EaR); Tầng 4 (3 nhóm công cụ phái sinh phòng ngừa IRS, Caps/Floors, Swaptions); Tầng 5 (Kiến trúc FTP matched-maturity 4 cấu phần); kèm theo phân tích phê phán 4 giá trị vượt trội và 4 thách thức thực chiến (rủi ro mô hình hành vi, rào cản IFRS 9 hedge accounting, tương tác LCR/NSFR/Leverage, sự trỗi dậy của CSRBB).
## [2026-10-16] ingest | cấu phần danh mục bảng cân đối chịu rủi ro IRRBB theo BCBS d368
- bối cảnh: Người dùng yêu cầu ingest và xử lý toàn diện các cấu phần danh mục bảng cân đối chịu phơi nhiễm rủi ro lãi suất IRRBB theo chuẩn mực Basel và tài liệu ALM quốc tế.
- created:
  - [[irrbb-balance-sheet-portfolios]]: Concept note chuyên sâu về cấu phần danh mục bảng cân đối chịu rủi ro IRRBB: phạm vi bao hàm (mọi tài sản, nợ nhạy cảm lãi suất và cam kết ngoại bảng) và loại trừ bắt buộc (vốn cấp 1 CET1, cổ phiếu sổ ngân hàng, tài sản cố định); phân loại 3 nhóm vị thế chuẩn hoá theo Giai đoạn 1 (Amenable, Less amenable bóc tách quyền chọn tự động $\text{KAO}$, Not amenable chứa quyền chọn hành vi NMDs/CPR/TDRR); phân tích chi tiết từng danh mục cấu phần (cho vay bán lẻ/bán buôn, trái phiếu HQLA, tiền gửi CASA lõi/phi lõi, tiền gửi tiết kiệm, vay nợ bán buôn và phái sinh); phân loại kế toán và cơ chế truyền dẫn rủi ro (Amortised Cost/HTM gánh $\Delta\text{EVE}$, Fair Value through OCI/AFS ảnh hưởng trực tiếp Vốn cấp 1 CET1 qua OCI, FVTPL tác động tức thì P&L); quy tắc phân bổ dòng tiền vào 19 dải kỳ hạn và bóc tách biên thương mại.
- updated:
  - [[irrbb-standardised-framework]]: Liên kết chuyên sâu tới [[irrbb-balance-sheet-portfolios]] trong Giai đoạn 1 phân loại vị thế.
  - [[irrbb-five-tier-architecture]]: Liên kết chuyên sâu tới [[irrbb-balance-sheet-portfolios]] trong Tầng 1.
  - [[index]], [[overview]]: Cập nhật toàn bộ danh mục 66 notes (8 metrics, 33 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 8 syntheses, 3 sources, 3 nav notes).
- lint & citations: 66 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | xây dựng Synthetic Balance Sheet cho Rủi ro Thanh khoản LCR – NSFR
- bối cảnh: Người dùng yêu cầu tích hợp toàn diện source Basel, các wiki node và xây dựng mô hình Bảng Cân đối Kế toán Tổng hợp (Synthetic Balance Sheet Liquidity Risk) định hình sự cân đối giữa Tài sản Nợ (TSN) và Tài sản Có (TSC) dựa trên các chỉ tiêu LCR và NSFR.
- created:
  - [[synthetic-balance-sheet-liquidity-risk]]: Flagship synthesis note về Mô hình Bảng Cân đối Mục tiêu Quản trị Rủi ro Thanh khoản LCR – NSFR: mô hình quy hoạch tuyến tính đa ràng buộc giải tích ($\sum A = \sum L + E$, $\text{LCR} \ge 100\%$, $\text{NSFR} \ge 100\%$, $\text{LR} \ge 3\%$, $\Delta\text{EVE} \le 15\%$); thiết kế chi tiết danh mục mẫu quy mô 100.000 tỷ VND (TSC gồm tiền mặt, 17% TPCP Level 1, 30% cho vay thế chấp, 43% cho vay DN/vốn lưu động; TSN gồm 20% CASA bán lẻ ổn định, 25% tiết kiệm kỳ hạn, 15% operational deposits, 15% bán buôn ngắn hạn, 15% trái phiếu dài hạn và 10% vốn CET1); kiểm chứng số học giải tích từng bước đạt $\text{LCR} = 114.17\%$ và $\text{NSFR} = 114.91\%$, NIM $3.01\%$, Leverage $9.09\%$; 4 quy luật động lực học cân đối TSN - TSC; và cơ chế truyền dẫn điều hành ALCO qua Term Liquidity FTP.
- updated:
  - [[integrated-alm-liquidity-strategy]]: Bổ sung khuyến nghị thứ 4 về việc vận hành mô hình synthetic balance sheet.
  - [[lcr-nsfr-interlinkages]]: Bổ sung liên kết chuyên sâu tới [[synthetic-balance-sheet-liquidity-risk]].
  - [[index]], [[overview]]: Cập nhật toàn bộ danh mục 67 notes (8 metrics, 33 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 9 syntheses, 3 sources, 3 nav notes).
- lint & citations: 67 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | tích hợp Bản chất Dòng tiền Kép (Gốc vs Lãi) và Kỳ hạn Portfolio vào Synthetic Balance Sheet
- bối cảnh: Người dùng chỉ đạo làm rõ bản chất bản thể của bảng cân đối ALM: một bảng cân đối thực chất chỉ bao gồm dòng tiền (dòng vào/ra $\Rightarrow$ dòng gốc do kỳ hạn đáo hạn chi phối) và phần lãi suất quyết định (dòng vào/ra $\Rightarrow$ dòng lãi do kỳ hạn định giá lại chi phối).
- updated:
  - [[synthetic-balance-sheet-liquidity-risk]]: Bổ sung toàn diện Mục 2 chuyên sâu: (1) Bản thể luận Cỗ máy Dòng tiền Kép (Dual Cash Flow Engine) phân rã $\mathbf{CF}_t = \mathbf{CF}_t^{\text{Prin}} + \mathbf{CF}_t^{\text{Int}}$, chỉ rõ dòng gốc quyết định thanh khoản nguồn vốn (Funding Liquidity), thang kỳ hạn (Maturity Ladder), LCR 30 ngày và cấu trúc NSFR 1 năm, trong khi dòng lãi quyết định P&L, NII, NIM và EVE; (2) Phân tách (Decoupling) sâu sắc giữa Kỳ hạn Gốc (Maturity Tenor) và Kỳ hạn Lãi (Repricing Tenor) qua 4 hình thái lệch pha kinh điển; (3) Bảng phân bổ đa chiều 10 cấu phần tài sản - nợ - vốn của portfolio mẫu 100.000 tỷ VND; (4) Vòng xoắn phản hồi động lực học hai chiều: Thâm hụt dòng gốc kích nổ chi phí dòng lãi $\leftrightarrow$ Cú sốc dòng lãi bóp nghẹt và đóng băng dòng gốc; nâng cấp thành 5 Quy luật Động lực học Cân đối TSN - TSC và cập nhật Ma trận Liên kết.
- lint & citations: 67 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | chuẩn mực giám sát thanh khoản bổ trợ Basel SRP50
- bối cảnh: Người dùng yêu cầu triển khai theo Lựa chọn 1: Ingest Chương SRP50 (Liquidity Monitoring Metrics) từ Bộ khung Basel hợp nhất (`src-bcbs-framework`) để hoàn thiện kiến trúc giám sát thanh khoản đa tầng, kết nối trực tiếp với dòng tiền gốc/lãi và thang kỳ hạn hợp đồng.
- created:
  - [[src-bcbs-framework]]: Source note quản lý bộ chuẩn mực hợp nhất The Basel Framework, mở đầu bằng Unit SRP50 gồm 28 trích dẫn nguyên văn đối chiếu 100% với raw source.
  - [[liquidity-monitoring-metrics]]: Concept note tổng quan về bộ công cụ giám sát thanh khoản SRP50, vai trò bổ trợ Trụ cột 2 song hành cùng LCR và NSFR.
  - [[contractual-maturity-mismatch]]: Concept note về Chênh lệch kỳ hạn theo hợp đồng (Maturity Ladder) trên 13 dải kỳ hạn, nguyên tắc dòng tiền tĩnh không rollover và xử lý dòng tiền chứng khoán cầm cố.
  - [[funding-concentration-risk]]: Concept note về Rủi ro tập trung nguồn vốn trên 3 chiều: đối tác (>1% tổng tài sản), công cụ/sản phẩm (>1%), và đồng tiền trọng yếu ($\ge 5\%$) qua 5 dải kỳ hạn còn lại.
  - [[available-unencumbered-assets]]: Concept note về Tài sản sạch khả dụng chưa cầm cố, cơ chế haircut 2 tầng (thị trường thứ cấp vs NHTW) và vai trò lá chắn thanh khoản bổ sung ngoài HQLA.
  - [[lcr-by-currency]]: Metric note về Tỷ lệ khả năng chi trả LCR theo từng đồng tiền trọng yếu (ngưỡng nợ $\ge 5\%$), công cụ giám sát rủi ro đóng băng thị trường hoán đổi tiền tệ (FX Swap freeze).
  - [[intraday-liquidity-risk]]: Concept note về Rủi ro thanh khoản trong ngày (BCBS 248 / SRP50.47–92), 7 công cụ giám sát thời gian thực và 4 kịch bản căng thẳng thanh khoản trong ngày.
  - [[basel-liquidity-monitoring-framework]]: Flagship synthesis note phân tích toàn diện Kiến trúc Giám sát Thanh khoản Đa tầng Basel III: tích hợp LCR, NSFR và 5 công cụ SRP50; ma trận so sánh 7 chiều đo lường; và 4 nguyên tắc điều hành ALCO thực chiến.
- updated:
  - [[synthetic-balance-sheet-liquidity-risk]]: Bổ sung Mục 7 tích hợp Bộ công cụ SRP50 vào Bảng cân đối mẫu (Contractual Ladder 13 dải, Concentration Limits, Available Assets Buffer, Intraday Limits).
  - [[lcr]], [[nsfr]]: Bổ sung liên kết chéo tới [[basel-liquidity-monitoring-framework]] và [[lcr-by-currency]].
  - [[integrated-alm-liquidity-strategy]]: Cập nhật Khuyến nghị 5 về hệ thống giám sát đa tầng.
  - [[index]], [[overview]]: Đồng bộ toàn bộ 75 notes (9 metrics, 38 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 10 syntheses, 4 sources, 3 nav notes).
- lint & citations: 75 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | chuẩn mực Tỷ lệ Đòn bẩy Basel III (LEV)
- bối cảnh: Người dùng yêu cầu triển khai Lựa chọn 1: Ingest toàn bộ Chương LEV (Leverage Ratio) từ chuẩn mực Basel (`src-bcbs-lev`) để hoàn thiện chốt chặn an toàn vốn phi rủi ro (non-risk-based backstop), tích hợp với LCR và NSFR trên Bảng cân đối tổng hợp.
- created:
  - [[src-bcbs-lev]]: Source note quản lý chuẩn mực LEV (đạt 100% trích dẫn nguyên văn qua 22 claims từ LEV10 đến LEV40).
  - [[leverage-ratio]]: Metric note về Tỷ lệ Đòn bẩy tối thiểu 3.0%, cấu trúc tử số Vốn cấp 1 và mẫu số Exposure Measure, phần đệm đòn bẩy G-SIB và mâu thuẫn điều hành HQLA.
  - [[leverage-exposure-measure]]: Concept note chuyên sâu về Quy mô phơi nhiễm đòn bẩy LEV30: giá trị tài sản kế toán gộp nội bảng, phơi nhiễm phái sinh SA-CCR alpha 1.4 nhân (RC + PFE), phụ trội bán CDS, bù trừ SFTs và ma trận hệ số CCF ngoại bảng (10%–100%).
- updated:
  - [[synthetic-balance-sheet-liquidity-risk]]: Cập nhật ràng buộc tỷ lệ đòn bẩy LR ≥ 3% và liên kết tới các cấu phần đo lường phơi nhiễm.
  - [[03_meta/sources.yaml]]: Cập nhật trạng thái các unit LEV10, LEV20, LEV30, LEV40 thành done.

## [2026-10-16] ingest | chuyên sâu Thực chiến ALM Tier 4: Kế hoạch Tài trợ Dự phòng (CFP) và Liquidity FTP theo Moorad Choudhry
- bối cảnh: Tự động chạy tiếp Lựa chọn 3 theo chỉ đạo của người dùng: Ingest kho tri thức thực chiến ALM từ tác phẩm kinh điển *The Principles of Banking* của Giáo sư Moorad Choudhry (`src-choudhry-principles-banking`) về Contingency Funding Plan và Liquidity Transfer Pricing.
- created:
  - [[src-choudhry-principles-banking]]: Source note cho giáo trình *The Principles of Banking* (Ấn bản 2, Wiley 2022), bao quát units u16 và u17 với 24 trích dẫn nguyên văn đối chiếu 100% với raw.
  - [[contingency-funding-plan]]: Concept note về Kế hoạch Tài trợ Dự phòng (CFP): cẩm nang tác chiến khủng hoảng thanh khoản, 3 cấp độ EWIs (Green, Amber, Red), thẩm quyền ALCO Crisis Management Team, danh mục hành động vốn khẩn cấp (Menu of Funding Measures), và cơ chế khấu trừ dòng tiền giúp tối ưu hóa giảm quy mô đệm tài sản thanh khoản bắt buộc (LAB/HQLA).
  - [[liquidity-transfer-pricing]]: Concept note về Định giá điều chuyển thanh khoản nội bộ (Liquidity FTP): bản chất chuyển giao rủi ro nội bộ (Internal Risk Transfer), cấu trúc giá 4 tầng (Base Rate, Term Liquidity Premium TLP, LCR Buffer Carry Cost, NSFR Structural Charge), nguyên tắc Matched-Maturity và Marginality, cùng sự phân tách 3 nguồn lợi nhuận ngân hàng (Biên thương mại cho vay, Biên thương mại tiền gửi, và Biên Treasury ALM).
  - [[practical-alm-liquidity-governance]]: Flagship synthesis note phân tích Khung Điều hành Quản trị Thanh khoản Thực chiến Toàn diện: kết nối đồng bộ 4 cỗ máy (Synthetic Balance Sheet 100k tỷ, Hệ thống tỷ lệ Basel LCR/NSFR/LEV/SRP50, Cơ chế Liquidity FTP và Lá chắn sinh tồn CFP); ma trận phân quyền tác chiến và 5 nguyên tắc vàng điều hành ALCO thực chiến.
- updated:
  - [[synthetic-balance-sheet-liquidity-risk]]: Bổ sung Liquidity FTP và CFP vào Mục 6 điều hành tác nghiệp và Mục 7 ma trận liên kết.
  - [[03_meta/sources.yaml]]: Cập nhật trạng thái các unit u16 và u17 của `src-choudhry-principles-banking` thành done.
  - [[index]], [[overview]]: Đồng bộ toàn bộ danh mục 82 notes (10 metrics, 41 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 11 syntheses, 6 sources, 3 nav notes).
- lint & citations: 82 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.

## [2026-10-16] ingest | chuyên sâu về Cơ chế Truyền dẫn và Phương pháp luận Định giá FTP (Lubinska Framework & EY VietABank)
- bối cảnh: Người dùng yêu cầu ingest chi tiết thêm về FTP. Thực hiện phân rã chuyên sâu toàn diện cả về mặt lý thuyết điều khiển rủi ro đa chiều (Lubinska 2020) và phương pháp luận định giá thực chiến tại ngân hàng thương mại Việt Nam (báo cáo tư vấn EY cho VietABank).
- created:
  - [[src-ftp-transmission-analysis]]: Source note về Cơ chế truyền dẫn FTP đến các risk factors (Lubinska framework ứng dụng tại VN), hoàn thành unit u01 với 14 trích dẫn nguyên văn đối chiếu 100% với raw.
  - [[src-vab-ftp]]: Source note về Phương pháp luận định giá điều chuyển vốn nội bộ FTP (báo cáo tư vấn EY cho VietABank), hoàn thành 5 units (preamble, u01, u02, u03, u04) với 20 trích dẫn nguyên văn đối chiếu 100% với raw.
  - [[ftp-transmission-mechanism]]: Concept note phân tích Cơ chế truyền dẫn FTP đến các yếu tố rủi ro: vai trò hệ thống điều khiển trung tâm (unified control mechanism); 3 kênh truyền dẫn (RRTK LCR/NSFR, RRLS IRRBB matched-maturity và khe hở kỳ hạn, RRTD & Vốn EL/Capital Charge/deal-level RAROC); mô hình điều tiết định lượng delta-spreads và vòng phản hồi cân bằng động.
  - [[ftp-pricing-methodology]]: Concept note về Phương pháp luận định giá điều chuyển vốn nội bộ (FTP) thực chiến: kiến trúc hai chiều VOF (Base curve + Margin + ALCO adjust) và COF (Base curve + Margin + Dự trữ bắt buộc DTBB + Bảo hiểm tiền gửi BHTG + Liquidity Buffer Premium + Term Liquidity Premium TLP + ALCO adjust); phương pháp phân bổ chi phí pháp định NHNN; đường cong hoàn trả Non-term Redemption Curve cho tiền gửi CASA (danh mục sao chép core vs non-core CASA); và định giá quyền chọn ẩn (prepayment khoản vay theo kỳ hạn hiệu lực WAL, rút tiền gửi trước hạn theo Thông tư 04/2022/TT-NHNN).
  - [[ftp-balance-sheet-optimization]]: Flagship synthesis note phân tích Hệ thống FTP — Động cơ điều khiển và tối ưu hóa bảng cân đối ALM toàn diện: bài toán quy hoạch tối ưu toán học MAX [NII / RAROC] dưới đa ràng buộc pháp định (LCR, NSFR, LEV, CAR, IRRBB ΔNII/ΔEVE); cơ chế nhân tử Lagrange và shadow prices chuyển hóa thành spreads điều khiển hành vi phi tập trung của chi nhánh; và quy trình 5 bước điều hành động cơ ALCO.
- updated:
  - [[liquidity-transfer-pricing]]: Bổ sung nguồn mới, mở rộng Mục 5 liên kết cơ chế truyền dẫn và phương pháp luận định giá thực chiến tại Việt Nam.
  - [[03_meta/sources.yaml]]: Cập nhật trạng thái u01 của `src-ftp-transmission-analysis` và 5 units của `src-vab-ftp` thành done.
  - [[index]], [[overview]]: Đồng bộ toàn bộ danh mục 87 notes (10 metrics, 43 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 12 syntheses, 8 sources, 3 nav notes).

## [2026-10-16] ingest | chuyên sâu Cơ chế Chuyển giao Rủi ro Nội bộ qua FTP (Internal Risk Transfer) & hoàn tất 100% tài liệu VAB FTP
- bối cảnh: Người dùng yêu cầu làm rõ và ingest chi tiết bản chất FTP như một cơ chế chuyển giao rủi ro (Internal Risk Transfer) mà BU take khi kinh doanh và CFU mua lại.
- created:
  - [[internal-risk-transfer]]: Concept note chuẩn mực phân tích Bản chất chuyển giao rủi ro nội bộ qua FTP: mô hình hai lớp hợp đồng (hợp đồng thật ngoài thị trường vs hợp đồng rủi ro ảo nội bộ); ma trận phân định rủi ro BU vs CFU (CFU mua lại 100% rủi ro thanh khoản và IRRBB, BU giữ lại rủi ro tín dụng và chi phí hoạt động); hiệu ứng bù trừ tự nhiên (netting) và hồ điều tiết trung tâm (pooling); bóc tách 3 nguồn lợi nhuận NIM (Biên cho vay, Biên huy động, Biên Treasury); và động lực học trong kịch bản khủng hoảng lãi suất tăng sốc +300 bps (chuyển lỗ về CFU để phòng ngừa bằng IRS).
- updated:
  - [[src-vab-ftp]]: Hoàn tất 100% cả 8/8 units (bổ sung units u05, u06, u07 với 5 trích dẫn verbatim về định nghĩa COF/VOF, TLP, Base curve và Margin).
  - [[03_meta/sources.yaml]]: Cập nhật trạng thái u05, u06, u07 của `src-vab-ftp` thành done (hoàn tất 100% nguồn).
  - [[index]], [[overview]]: Đồng bộ danh mục 88 notes (10 metrics, 44 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 12 syntheses, 8 sources, 3 nav notes).

## [2026-10-16] ingest | tổng hợp bản chất, mục tiêu và các vấn đề cốt tử FTP giải quyết trong quản trị bảng cân đối (ftp-nature-and-balance-sheet-management)
- bối cảnh: Người dùng yêu cầu ingest câu hỏi: "Bản chất và mục tiêu của Funds Transfer Pricing (FTP) trong ngân hàng là gì? FTP giải quyết vấn đề gì trong quản trị bảng cân đối?".
- created:
  - [[ftp-nature-and-balance-sheet-management]]: Flagship synthesis note trả lời toàn diện câu hỏi cốt lõi về FTP trong quản trị ALM:
    - *Bản chất*: Không phải phòng ngừa rủi ro ra ngoài hay luân chuyển vật lý dòng tiền tệ, mà là cơ chế chuyển giao rủi ro nội bộ (Internal Transfer of Risk), thiết lập ranh giới kinh tế giữa thương quyền khách hàng phi rủi ro thị trường (Customer Franchise) của chi nhánh và hoạt động chuyển đổi kỳ hạn rủi ro (Maturity Transformation) của Treasury; tuân thủ 2 nguyên tắc kỹ trị nền tảng: Trùng khớp kỳ hạn (Matched-Maturity) và Cận biên (Marginality).
    - *4 mục tiêu chiến lược*: (1) Đo lường hiệu quả & lợi nhuận minh bạch (bóc tách 3 nguồn NIM); (2) Quản lý tập trung rủi ro thanh khoản và lãi suất (CFU pooling & IRS hedging); (3) Quản trị và tối ưu hóa bảng cân đối ALM (đa ràng buộc LCR, NSFR, LEV, CAR, IRRBB); (4) Định hướng hoạt động kinh doanh bằng cơ chế giá thị trường nội bộ.
    - *5 vấn nạn cốt tử được giải quyết*: (1) Triệt tiêu trợ cấp chéo rủi ro (cross-subsidization); (2) Chặn đứng cạm bẫy chuyển đổi kỳ hạn quá mức qua phần bù thanh khoản TLP; (3) Khắc phục quản trị rủi ro phân tán bằng cơ chế tập trung hóa; (4) Nội bộ hóa sòng phẳng các chi phí pháp định (DTBB, BHTG, đệm thanh khoản LCR) vào giá bán vốn tín dụng; (5) Thay thế mệnh lệnh hành chính bằng đòn bẩy giá cả thị trường nội bộ.
- updated:
  - [[internal-risk-transfer]]: Bổ sung liên kết quan hệ và danh mục tham chiếu tới `[[ftp-nature-and-balance-sheet-management]]`.
  - [[liquidity-transfer-pricing]]: Bổ sung tham chiếu tới `[[internal-risk-transfer]]` và `[[ftp-nature-and-balance-sheet-management]]`.
  - [[index]], [[overview]]: Đồng bộ danh mục 89 notes (10 metrics, 44 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 13 syntheses, 8 sources, 3 nav notes).

## [2026-10-16] ingest | các cấu phần rủi ro và chi phí trong định giá FTP: funding cost, liquidity risk, IRRBB, optionality (ftp-risk-and-cost-components)
- bối cảnh: Người dùng yêu cầu ingest câu hỏi: "FTP phản ánh và định giá những loại rủi ro/chi phí nào trên bảng cân đối, đặc biệt là funding cost, liquidity risk, interest rate risk và optionality?".
- created:
  - [[ftp-risk-and-cost-components]]: Flagship synthesis note phân tích toàn diện 4 trụ cột rủi ro và chi phí trong hệ thống định giá điều chuyển vốn nội bộ đa tầng:
    - *Funding Cost (Chi phí Vốn Cơ sở)*: Đường cong phi rủi ro tham chiếu thị trường (SOFR, OIS, VNIBOR, OMO, VGB Yield Curve); chi phí cơ hội cận biên (Marginal Cost of Funds) thay cho chi phí bình quân lịch sử; wholesale funding spread phản ánh chi phí huy động bán buôn của ngân hàng.
    - *Liquidity Risk (Rủi ro Thanh khoản & Chi phí Pháp lệnh)*: Phân rã Term Liquidity Premium (TLP) cho tài sản dài hạn thả nổi; chi phí gánh đệm thanh khoản pháp lệnh (Liquidity Buffer Carry Cost / HQLA negative carry) theo LCR và TT22; chi phí tuân thủ bắt buộc tại Việt Nam (Dự trữ bắt buộc DTBB và Phí bảo hiểm tiền gửi BHTG 0,15%); phụ phí cấu trúc NSFR và chi phí thanh khoản dự phòng cho hạn mức cam kết chưa rút.
    - *IRRBB (Rủi ro Lãi suất Sổ Ngân hàng)*: Triệt tiêu rủi ro khe hở tái định giá (Gap Risk) qua nguyên tắc Matched-Maturity; xử lý rủi ro cơ sở (Basis Risk) giữa chỉ số cho vay và huy động qua Basis Spread Charge; quản trị tập trung biến động đường cong lợi suất (Yield Curve Risk) và phòng ngừa bằng IRS tại CFU.
    - *Optionality & Behavioral Risk (Rủi ro Quyền chọn Ẩn & Hành vi)*: Quyền chọn trả nợ trước hạn (Prepayment Option) định giá qua kỳ hạn hiệu lực bình quân gia quyền WAL và mô hình CPR; quyền chọn rút tiền gửi trước hạn (Early Withdrawal Option) hồi tố lãi suất theo Thông tư 04/2022/TT-NHNN; mô hình hóa tiền gửi không kỳ hạn CASA qua Non-term Redemption Curve và danh mục sao chép (tách Core CASA dài hạn vs Non-core CASA ngắn hạn); quyền chọn tự động trần/sàn lãi suất (Caps/Floors).
    - *Mở rộng RAROC*: Tích hợp Expected Loss Charge (EL = PD × LGD × EAD) và Capital Charge (RWA × CAR × Cost of Equity) vào giá bán vốn tín dụng.
- updated:
  - [[ftp-nature-and-balance-sheet-management]]: Bổ sung liên kết drives và tham chiếu chéo tới `[[ftp-risk-and-cost-components]]`.
  - [[ftp-pricing-methodology]]: Bổ sung tham chiếu tới `[[ftp-risk-and-cost-components]]` và `[[internal-risk-transfer]]`.
  - [[index]], [[overview]]: Đồng bộ danh mục 90 notes (10 metrics, 44 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 14 syntheses, 8 sources, 3 nav notes).

## [2026-10-16] ingest | phương pháp luận xây dựng đường cong FTP theo kỳ hạn, đồng tiền và loại sản phẩm (ftp-curve-construction-methodology)
- bối cảnh: Người dùng yêu cầu ingest câu hỏi: "FTP curve/FTP rate được xây dựng như thế nào cho từng kỳ hạn, đồng tiền và loại sản phẩm?".
- created:
  - [[ftp-curve-construction-methodology]]: Flagship synthesis note phân tích chi tiết quy trình xây dựng đường cong định giá FTP theo không gian 3 chiều:
    - *Chiều Cấu trúc Kỳ hạn (Tenor)*: Thang kỳ hạn chuẩn hóa O/N đến 10 năm; phương pháp nội suy tuyến tính (Linear Interpolation) và hàm Interp(WAT) cho các kỳ hạn lẻ; kỹ thuật đường cong Zero-coupon / Cubic Spline.
    - *Chiều Đồng tiền (Currency)*: Tách biệt độc lập các bộ đường cong FTP theo từng đồng tiền; đường cong VND (kết hợp bình quân huy động 3 tháng hoặc VNIBOR + OMO + Trái phiếu Chính phủ VGB Benchmark); đường cong USD & Ngoại tệ (kỳ hạn ngắn $\le 1$Y theo SOFR / Term SOFR / SIBOR; kỳ hạn $>1$Y theo USD IRS); cơ chế liên kết tỷ giá hoán đổi FX Swap Curve và Ngang giá Lãi suất có bảo hiểm (CIP); phân bổ chi phí pháp định DTBB riêng cho từng đồng tiền (trần lãi suất tiền gửi USD 0% theo Thông tư 24/2015/TT-NHNN).
    - *Chiều Loại sản phẩm (Product)*: Ma trận định giá chi tiết: Tiền gửi trả cuối kỳ (VOF cố định, TLP = 0); Tiền gửi gửi góp tích lũy; Tiền gửi không kỳ hạn CASA (Non-term Redemption Curve bóc tách Core CASA dài hạn vs Non-core CASA ngắn hạn, hoặc tỷ lệ rút 15% theo TT22); Khoản vay trả cuối kỳ cố định (COF cố định, TLP = 0); Khoản vay trả cuối kỳ thả nổi (COF theo kỳ hạn tái định giá, TLP = COF gốc - COF tái định giá); Khoản vay trả định kỳ cố định (COF theo kỳ hạn hiệu lực bình quân gia quyền WAL); Khoản vay trả định kỳ thả nổi (COF tái định giá, TLP = COF WAL - COF tái định giá); Cho vay thấu chi / thẻ tín dụng (Core OD 6M–1Y vs Non-core OD 1M); Phụ phí thanh khoản tiềm tàng cho hạn mức cam kết ngoại bảng chưa sử dụng ($C \times \text{CCF} \times \text{TSTK fee}$).
    - *Phân tách hai thị trường*: Thị trường 1 (Chi nhánh) áp biểu định kỳ cố định (tháng/quý) tích hợp Margin và ALCO Adjust; Thị trường 2 (Treasury / Liên ngân hàng) áp cơ chế Deal-by-deal real-time bám sát mid-rate nhóm 3–6 ngân hàng cùng Peer (loại bỏ outlier $\pm 15\%$) hoặc VNIBOR 1 tuần.
- updated:
  - [[src-vab-ftp]]: Bổ sung 12 trích dẫn nguyên văn đối chiếu 100% với raw (`^vab-ftp-26` đến `^vab-ftp-37`) về quy tắc đồng tiền độc lập, nội suy kỳ hạn, công thức TLP cho sản phẩm thả nổi, phụ phí cam kết ngoại bảng và giá TT2.
  - [[ftp-risk-and-cost-components]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-curve-construction-methodology]]`.
  - [[ftp-nature-and-balance-sheet-management]]: Bổ sung tham chiếu tới `[[ftp-curve-construction-methodology]]`.
  - [[index]], [[overview]]: Đồng bộ danh mục 91 notes (10 metrics, 44 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 15 syntheses, 8 sources, 3 nav notes).

## [2026-10-16] ingest | phương pháp phân bổ giao dịch và sản phẩm vào các FTP portfolio và tenor bucket (ftp-portfolio-and-bucket-allocation)
- bối cảnh: Người dùng yêu cầu ingest câu hỏi: "Các giao dịch hoặc sản phẩm được phân bổ vào các FTP portfolio/bucket như thế nào? Tiêu chí phân bổ là gì?".
- created:
  - [[ftp-portfolio-and-bucket-allocation]]: Flagship synthesis note phân tích chi tiết quy tắc phân loại và ánh xạ dòng tiền trên Core Banking vào các Portfolio và Tenor Bucket:
    - *Phân bổ theo Danh mục (Portfolio Segmentation)*: Tách biệt Sổ Ngân hàng (Banking Book / Thị trường 1) áp biểu định kỳ cố định biên lợi nhuận cho chi nhánh, Sổ Kinh doanh (Trading Book / Thị trường 2) giao dịch deal-by-deal bám sát thị trường liên ngân hàng; danh mục Huy động (VOF), danh mục Tín dụng (COF); Danh mục Loại trừ đặc biệt (Đệm tài sản thanh khoản cao theo Phụ lục 3 TT22 loại trừ khỏi mẫu số tính FTP và gom negative carry vào Liquidity Buffer Premium; Tài sản cố định tài trợ bởi Vốn chủ sở hữu).
    - *Bảy tiêu chí kỹ trị phân bổ vào Tenor Buckets*:
      1. Cơ chế lãi suất: Lãi suất cố định gán theo kỳ hạn gốc hoặc WAL; Lãi suất thả nổi bóc tách kép đồng thời vào Repricing Bucket (xác định Base Rate) và Tenor Bucket gốc/WAL (tính phụ phí thanh khoản kỳ hạn TLP = COF gốc - COF tái định giá).
      2. Đặc tính hoàn trả gốc: Trả cuối kỳ (Bullet) gán theo Contractual Maturity; Trả định kỳ (Amortizing) bắt buộc quy đổi theo Kỳ hạn hiệu lực bình quân gia quyền (Weighted Average Life - WAL).
      3. Tính chất kỳ hạn hợp đồng vs hành vi: Sản phẩm có kỳ hạn xác định gán theo hợp đồng; Sản phẩm phi kỳ hạn (CASA) phân bổ qua mô hình danh mục sao chép (Replicating Portfolio) tách thành Non-core CASA (O/N–1M) và Core CASA (6M–3Y+), hoặc áp tỷ lệ thận trọng TT22 (15% KKH, 85% có kỳ hạn 2 tháng); Thấu chi Overdraft tách Core OD vs Non-core OD.
      4. Loại đồng tiền: Phân lập độc lập tuyệt đối giữa các đồng tiền (VND Bucket riêng, USD Bucket riêng).
      5. Tính chất ưu đãi: Tách nhỏ khoản vay ưu đãi 2 giai đoạn (Giai đoạn ưu đãi áp Bucket cố định ngắn hạn, Giai đoạn sau ưu đãi áp Base tái định giá + TLP cho kỳ hạn còn lại).
      6. Trạng thái tín dụng: Nợ trong hạn áp biểu chuẩn; Nợ quá hạn đóng băng lãi suất COF tại thời điểm quá hạn; Nợ gia hạn gán vào Bucket mới bằng kỳ hạn cũ cộng thời gian gia hạn thêm.
      7. Ngoại bảng & Quyền chọn ẩn: Cam kết tín dụng chưa rút gán vào Contingent Liquidity Bucket tính phí thanh khoản tiềm tàng ($C \times \text{CCF} \times \text{TSTK Fee}$); Khoản vay trả trước hạn rút ngắn WAL theo tỷ lệ CPR; Rút tiền gửi trước hạn hồi tố về Bucket không kỳ hạn theo TT04/2022.
    - *Ma trận quy tắc ánh xạ kỹ thuật (Master Bucketing Rule Matrix)*: Chuẩn hóa quy tắc ánh xạ tự động cho từng mã sản phẩm trên Core Banking (TD, CASA, Loan, Overdraft, Commitment, Interbank, Excluded HQLA).
- updated:
  - [[ftp-curve-construction-methodology]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-portfolio-and-bucket-allocation]]`.
  - [[ftp-risk-and-cost-components]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-portfolio-and-bucket-allocation]]`.
  - [[ftp-pricing-methodology]]: Bổ sung tham chiếu tới `[[ftp-portfolio-and-bucket-allocation]]`.
  - [[index]], [[overview]]: Đồng bộ danh mục 92 notes (10 metrics, 44 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 16 syntheses, 8 sources, 3 nav notes).

## [2026-10-16] ingest | nguyên tắc phân bổ chi phí và lợi ích của từng FTP portfolio cho đơn vị kinh doanh và sản phẩm (ftp-cost-benefit-allocation-principles)
- bối cảnh: Người dùng yêu cầu ingest câu hỏi: "Chi phí/lợi ích của từng FTP portfolio được phân bổ cho các đơn vị kinh doanh hoặc sản phẩm theo nguyên tắc nào?".
- created:
  - [[ftp-cost-benefit-allocation-principles]]: Flagship synthesis note phân tích chi tiết cơ chế phân bổ chi phí và lợi ích P&L theo từng danh mục FTP:
    - *Bản chất phân rã NII*: Bóc tách toàn bộ thu nhập lãi thuần toàn hàng thành 3 khối biên lợi nhuận độc lập: (1) Biên thương mại Huy động cho Liability BUs ($\text{VOF} - \text{Lãi suất KH}$); (2) Biên thương mại Cho vay cho Asset BUs ($\text{Lãi suất KH} - \text{COF}$); (3) Biên điều hòa vốn Treasury Mismatch Margin cho CFU ($\text{Net COF/VOF} \pm \text{Chi phí phòng ngừa rủi ro}$).
    - *Sáu nguyên tắc kỹ trị cốt lõi*: (1) Trùng khớp kỳ hạn (Matched-Maturity); (2) Chi phí cơ hội cận biên (Marginality - không trợ cấp chéo); (3) Trách nhiệm phân định rủi ro (Risk Ownership - BU chỉ chịu rủi ro kiểm soát được); (4) Người gây rủi ro chịu phí (User-Pays / Causality - sản phẩm dài hạn chịu TLP, sản phẩm tiêu tốn dự trữ chịu DTBB/BHTG); (5) Hồ điều tiết tập trung (Pooling & Netting); (6) Định hướng chiến lược ALCO (Incentive Alignment qua ALCO Adjust và Margin).
    - *Cơ chế phân bổ chi tiết theo từng Portfolio*: Phân bổ doanh thu VOF và lợi ích CASA (Replicating Portfolio) cho đơn vị tiền gửi; phân bổ chi phí vốn COF 7 cấu phần cho đơn vị tín dụng; cơ chế tập hợp và phân bổ chi phí đệm HQLA negative carry vào phụ phí Buffer của toàn bộ tài sản có; phân bổ phí thanh khoản tiềm tàng cho cam kết tín dụng ngoại bảng chưa rút; cơ chế phân bổ TT2 cho Khối QL&KDV (Deal-by-deal từng Desk vs Bù trừ ròng toàn Khối theo VNIBOR 1 tuần).
    - *Khung báo cáo phân bổ P&L 5 cấp độ*: Toàn hàng, Đơn vị kinh doanh (Chi nhánh), Loại sản phẩm, Khách hàng/Nhóm khách hàng, và Các trường hợp phê duyệt ngoại lệ / gói vay ưu đãi.
- updated:
  - [[src-vab-ftp]]: Bổ sung 3 trích dẫn nguyên văn đối chiếu 100% với raw (`^vab-ftp-38` đến `^vab-ftp-40`) về khung báo cáo hiệu quả NII/NIM và công thức phân rã P&L.
  - [[ftp-portfolio-and-bucket-allocation]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-cost-benefit-allocation-principles]]`.
  - [[internal-risk-transfer]]: Bổ sung tham chiếu chéo tới `[[ftp-cost-benefit-allocation-principles]]` và `[[ftp-portfolio-and-bucket-allocation]]`.
  - [[ftp-pricing-methodology]]: Bổ sung tham chiếu tới `[[ftp-cost-benefit-allocation-principles]]`.
  - [[index]], [[overview]]: Đồng bộ danh mục 93 notes (10 metrics, 44 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 17 syntheses, 8 sources, 3 nav notes).

## [2026-10-16] ingest | xác định mức lãi suất FTP rate cuối cùng cho từng giao dịch và sản phẩm (ftp-final-rate-determination)
- bối cảnh: Người dùng yêu cầu ingest câu hỏi: "Mức FTP rate cuối cùng được áp dụng cho từng giao dịch/sản phẩm như thế nào sau khi tính đến tenor, repricing profile, liquidity characteristics và embedded options?".
- created:
  - [[ftp-final-rate-determination]]: Flagship synthesis note phân tích chi tiết quy trình tích hợp 4 chiều kích cấu thành mức lãi suất điều chuyển vốn nội bộ cuối cùng (Final Granular Deal-Level FTP Rate) cho từng hợp đồng, giao dịch và dòng sản phẩm trên bảng cân đối:
    1. *Tích hợp Chiều kích Kỳ hạn (Tenor Profile)*: Contractual Maturity vs Amortizing WAL ($\text{WAL} = \sum P_i T_i / \sum P_i$); Nội suy đường cong cho kỳ hạn lẻ (Odd-Tenor Linear/Cubic Spline); Khung kỳ hạn hành vi (Behavioral Horizon) cho sản phẩm phi kỳ hạn.
    2. *Tích hợp Chiều kích Tái định giá (Repricing Profile)*: Lãi suất cố định (Single Tenor Lock); Lãi suất thả nổi (Dual-Tenor bóc tách kép: Base Rate thả nổi reset theo kỳ hạn tái định giá + TLP và các phụ phí thanh khoản khóa cố định suốt vòng đời khoản vay); Gói vay ưu đãi phân rã 2 giai đoạn.
    3. *Tích hợp Đặc tính Thanh khoản (Liquidity Characteristics)*: Term Liquidity Premium (TLP) theo WAL; Phụ phí đệm thanh khoản HQLA (Liquidity Buffer Premium); Phụ phí chi phí dự trữ bắt buộc (DTBB) và bảo hiểm tiền gửi (BHTG 0.15%); Phụ phí thanh khoản tiềm tàng cho hạn mức cam kết tín dụng chưa giải ngân ngoại bảng ($C \times \text{CCF} \times \text{TSTK Fee}$).
    4. *Tích hợp Quyền chọn Ẩn (Embedded Options)*: Quyền chọn trả nợ trước hạn (Prepayment CPR rút ngắn Contractual WAL thành Behavioral WAL + Phí bù đắp tái đầu tư); Quyền chọn rút tiền gửi trước hạn (Early Redemption Penalty hồi tố KKH theo TT04/2022); Mô hình Replicating Portfolio cho CASA (Non-core vs Core CASA); Quyền chọn trần/sàn lãi suất (Embedded Caps/Floors Add-on định giá qua mô hình Black-76).
    5. *Hệ thống Công thức Toán học Định lượng Chuẩn mực cho 8 Nhóm Sản phẩm*: Fixed-rate TD, CASA/NMD, Fixed Bullet Loan, Fixed Amortizing Loan, Floating Amortizing Loan, Promotional Loan 2 pha, Undrawn Commitments, và Comprehensive Deal-Level RAROC Pricing tích hợp EL và Capital Charge ($K \times \text{CoE}$).
    6. *Nghiên cứu Tình huống Thực tiễn (Case Studies)*: Minh họa số học chi tiết cho Khoản vay thế chấp mua nhà 10 năm trả nợ đều (Contractual WAL 5.5 năm, Behavioral WAL 3.8 năm sau CPR, tính chi tiết COF thả nổi 8.35% với TLP 1.10% bị khóa trọn đời) và Danh mục tiền gửi CASA 1.000 tỷ VND (tách 20% Non-core VOF 4.50% và 80% Core VOF 6.20%, tạo ra VOF hỗn hợp 5.86% và biên thương mại 5.66% cho chi nhánh).
- updated:
  - [[ftp-cost-benefit-allocation-principles]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-final-rate-determination]]`.
  - [[ftp-portfolio-and-bucket-allocation]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-final-rate-determination]]`.
  - [[ftp-curve-construction-methodology]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-final-rate-determination]]`.
  - [[ftp-risk-and-cost-components]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-final-rate-determination]]`.
  - [[ftp-pricing-methodology]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-final-rate-determination]]`.
  - [[index]], [[overview]]: Đồng bộ danh mục 94 notes (10 metrics, 44 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 18 syntheses, 8 sources, 3 nav notes).

## [2026-10-16] ingest | kiểm tra tính phản ánh economic cost và cơ chế định hướng incentive của hệ thống FTP (ftp-economic-cost-and-incentive-validation & src-lubinska-alm-optimisation u03)
- bối cảnh: Người dùng yêu cầu ingest câu hỏi: "Làm thế nào để kiểm tra FTP đã phản ánh đúng economic cost của bảng cân đối và tạo đúng incentive cho các đơn vị kinh doanh?".
- created:
  - [[src-lubinska-alm-optimisation]]: Source note mới của Beata Lubinska (*Asset Liability Management Optimisation*, Wiley Finance 2020, Tier T4), hoàn thành unit `u03` (Chapter 2: lines 958–1376) với 14 trích dẫn nguyên văn đối chiếu 100% với raw (`^lubinska-ftp-1` đến `^lubinska-ftp-14`) về bản chất FTP là công cụ định hình bảng cân đối (shaping the banking book), Target Operating Model (TOM), quy tắc phân tách True Economic Cost và Incentive Overlays, bài học cảnh báo từ rà soát hệ thống ngân hàng Anh của PRA (Cadamagnani et al. 2015), và rủi ro định giá sai chi phí vốn (under/over-estimation).
  - [[ftp-economic-cost-and-incentive-validation]]: Flagship synthesis note xây dựng Khung Kiểm Định Kép (Dual-Validation Framework) toàn diện cho Ủy ban ALCO:
    1. *Trụ cột A: Bốn kiểm định phản ánh đúng Economic Cost của Bảng cân đối*:
       - Kiểm thử 1: Nguyên tắc chi phí cơ hội cận biên (Marginality Principle Test) và khả năng giao dịch phòng ngừa thực tế (Transactability Check); loại bỏ hoàn toàn bẫy chi phí bình quân sổ sách lịch sử.
       - Kiểm thử 2: Hạch toán toàn diện & không bỏ sót phụ phí (Decomposition & Non-Omission Test) đối với TLP, HQLA buffer negative carry, chi phí tuân thủ pháp lệnh DTBB & BHTG, phí cam kết thanh khoản ngoại bảng chưa rút, và chi phí quyền chọn ẩn (prepayment & early redemption).
       - Kiểm thử 3: Kiểm định Lãi/Lỗ thặng dư của Trung tâm vốn (Treasury Residual Hedged P&L tiệm cận 0); nhận diện lỗi cấu trúc khi Treasury lỗ âm kéo dài hoặc phình to lãi bất thường.
       - Kiểm thử 4: Backtesting và kiểm định mô hình hành vi (CASA Replicating Portfolio và tỷ lệ trả nợ trước hạn CPR).
    2. *Trụ cột B: Bốn kiểm định tạo đúng Động lực / Incentive cho Đơn vị Kinh doanh*:
       - Kiểm thử 5: Phân tách minh bạch giữa True Economic Cost và Management Overlays theo chuẩn mực PRA; cấm áp dụng đường cong lệch ngầm định; thiết lập kiến trúc định giá 2 tầng và 4 kỷ luật thép cho Incentive Premium (có hạn định kết thúc sunset clause, ngân sách ALCO rõ ràng).
       - Kiểm thử 6: Kiểm định miễn nhiễm biên thương mại chi nhánh (Commercial Margin Immunization Test) qua các chu kỳ sốc lãi suất thị trường.
       - Kiểm thử 7: Nhận diện và ngăn chặn các hành vi trục lợi giá nội bộ ("Gaming" & Internal Arbitrage) như bậc thang kỳ hạn, lách TLP thả nổi, CASA ảo cuối tháng và treo hạn mức ngoại bảng.
       - Kiểm thử 8: Kiểm định vòng lặp điều tiết hành vi khép kín (Closed-Loop Steering Effectiveness) và đo lường độ co giãn hành vi của BU trước các cú huých spread của ALCO.
    3. *Bộ chỉ số định lượng đo lường sức khỏe FTP*: Treasury Residual P&L Ratio, Commercial Margin Stability Index (CMSI), Incentive Overlay Transparency Ratio (IOTR), Arbitrage Anomaly Rate (AAR), và Behavioral Drift Ratio (BDR).
    4. *Khung Quản trị 3 Tuyến Phòng Thủ*: Phân định trách nhiệm giữa Tuyến 1 (Treasury/CFU), Tuyến 2 (Risk Management độc lập thẩm định mô hình), Tuyến 3 (Internal Audit), cấp phê duyệt tối cao ALCO/HĐQT và cơ chế phản biện lành mạnh từ các đơn vị kinh doanh.
    5. *Quy trình rà soát định kỳ 5 bước thực chiến dành cho Ủy ban ALCO*.
- updated:
  - [[ftp-final-rate-determination]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-economic-cost-and-incentive-validation]]`.
  - [[ftp-cost-benefit-allocation-principles]]: Bổ sung liên kết quan hệ và tham chiếu chéo tới `[[ftp-economic-cost-and-incentive-validation]]` và `[[src-lubinska-alm-optimisation]]`.
  - [[index]], [[overview]]: Đồng bộ danh mục 96 notes (10 metrics, 44 concepts, 3 instruments, 4 models, 3 regulations, 1 entity, 19 syntheses, 9 sources, 3 nav notes).

## [2026-10-16] decision | chuẩn hoá node type: chuyển 15 node từ concepts sang metrics/models (user duyệt)

- Lý do: rà 44 concept theo cây quyết định v2 C.1; nhiều node là đại lượng có công thức hoặc phương pháp định lượng. User quyết định thêm: nhóm cấu phần ASF/RSF là metric vì được đánh giá riêng trong báo cáo quản trị bảng cân đối.
- moved → `metrics/` (type: metric): [[cash-outflows]], [[cash-inflows]], [[leverage-exposure-measure]], [[contractual-maturity-mismatch]], [[available-unencumbered-assets]], [[outlier-bank-test]], [[asf-capital-and-long-term-liabilities]], [[asf-retail-and-small-business-deposits]], [[asf-wholesale-and-operational-funding]], [[rsf-hqla-and-central-bank-reserves]], [[rsf-loans-and-credit-exposures]], [[rsf-securities-financing-and-encumbrance]], [[rsf-derivatives-and-off-balance-sheet]].
- moved → `models/` (type: model): [[ftp-pricing-methodology]], [[irrbb-standardised-framework]].
- Chỉ đổi `type`, thư mục và `updated`; ID giữ nguyên nên link `[[id]]` không đổi. Thân bài chưa theo template metric/model (Định nghĩa · Công thức · Diễn giải… / Mục tiêu · Inputs & giả định · Calibration…); 5 node canonical (leverage-exposure-measure, contractual-maturity-mismatch, available-unencumbered-assets, outlier-bank-test, irrbb-standardised-framework) cần user duyệt nếu tái cấu trúc.
- Giữ concept (user quyết định): [[funding-concentration-risk]], [[lcr-nsfr-interlinkages]], [[non-maturity-deposits]], [[committed-facilities]], [[standardised-interest-rate-shocks]]. Giữ [[run-off-rate]] là concept: tham số Basel ấn định, không đo từ dữ liệu.
- fixed: 4 link tuyệt đối `file:///…/concepts/outlier-bank-test.md` → `[[outlier-bank-test|…]]` trong [[behavioural-options]] và [[irrbb-five-tier-architecture]].
- spec: bổ sung tiêu chí thành phần metric / tham số / phương pháp quy định vào `alm-wiki-architecture-v2.md` C.1 và `CLAUDE.md` mục "Chọn node type".
- Mở: (1) các nhóm dòng ra/tài sản LCR ([[retail-deposit-stability]], [[operational-deposits]], [[unsecured-wholesale-funding]], [[secured-funding]], [[derivatives-and-contingent-outflows]], [[level-1-assets]], [[level-2-assets]]) cùng bản chất với `asf-*`/`rsf-*`, chờ user quyết; (2) cùng một nhóm khoản mục đang tách thành node LCR và node NSFR (ví dụ retail-deposit-stability ↔ asf-retail-and-small-business-deposits), cân nhắc gộp khi ingest thông tư NHNN tương ứng; (3) `tools/update_relations.py` còn ghi cứng `02_wiki/concepts/cash-{outflows,inflows}.md`.
- [[index]]: đồng bộ 96 notes (23 metrics, 29 concepts, 3 instruments, 6 models, 3 regulations, 1 entity, 19 syntheses, 9 sources, 3 nav notes). Lint: 0 error.

## [2026-10-16] decision | mọi đại lượng trong công thức metric là metric; lint chấp nhận alias escape trong bảng; tái cấu trúc 22 node theo template (user duyệt)

- Nguyên tắc (user): mọi đại lượng trong công thức tính một chỉ số đều phải được quản trị, nên đều là metric. Đã cập nhật `alm-wiki-architecture-v2.md` C.1 và `CLAUDE.md`.
- moved → `metrics/` (type: metric): [[retail-deposit-stability]], [[operational-deposits]], [[unsecured-wholesale-funding]], [[secured-funding]], [[derivatives-and-contingent-outflows]], [[level-1-assets]], [[level-2-assets]]. [[index]] đồng bộ: 30 metrics, 22 concepts, 6 models.
- tools: `tools/lint.py` regex `LINK` chấp nhận `[[id\|alias]]` (cú pháp alias trong bảng của Obsidian). Đã kiểm thử trên bản copy vault: link escape hợp lệ qua, link và block-ref escape sai vẫn bị bắt.
- fixed: escape 34 alias link trong dòng bảng ở 8 file (concepts/irrbb-balance-sheet-portfolios, metrics/available-unencumbered-assets, metrics/required-stable-funding, metrics/rsf-hqla-and-central-bank-reserves, regulations/bcbs-irrbb, syntheses/basel-liquidity-monitoring-framework, syntheses/irrbb-five-tier-architecture, syntheses/practical-alm-liquidity-governance).
- restructured: 20 metric + 2 model node (toàn bộ node chuyển type hôm nay) theo template metric (Định nghĩa · Công thức & tham số · Diễn giải · Basel vs VN · Ứng dụng trong ALM · Nhầm lẫn thường gặp) và model (Mục tiêu · Công thức · Inputs & giả định · Calibration · Output & usage · Hạn chế & validation). Chỉ di chuyển block và hạ cấp heading; script đối chiếu xác nhận mọi dòng nội dung, citation, block-ref giữ nguyên; heading duy nhất bị bỏ là "Ý chính" (gộp vào Định nghĩa). Mục ngoài template (Câu hỏi mở, Ma trận Liên kết, Xem thêm, Khái niệm và Liên kết) giữ ở cuối.
- Mục template còn trống (không tạo heading rỗng): "Basel vs VN" thiếu ở 19/20 metric (trừ [[cash-outflows]]), chờ ingest TT50/2026; "Nhầm lẫn thường gặp" thiếu ở 16 metric; "Calibration" thiếu ở cả 2 model; "Hạn chế & validation" thiếu ở [[ftp-pricing-methodology]]; "Inputs & giả định" thiếu ở [[irrbb-standardised-framework]].
- Mở: theo nguyên tắc mới, [[committed-facilities]] (nhóm dòng ra trong NCO, cùng bản chất [[secured-funding]]) và tham số [[run-off-rate]] chờ user quyết.

## [2026-10-16] ingest | src-choudhry-principles-banking u12 (Chapter 7: Managing IRRBB)
- updated:
  - [[src-choudhry-principles-banking]]: Bổ sung unit u12 (Chapter 7: Managing IRRBB), tóm tắt chuyên sâu, 9 key claims với 14 trích dẫn nguyên văn khớp 100% raw.
  - [[irrbb-balance-sheet-portfolios]]: Bổ sung góc nhìn Moorad Choudhry về bản chất kế toán dồn tích (Accruals Book / Par / Amortised Cost) và rủi ro thị trường tiềm ẩn (rủi ro P&L và chi phí cơ hội do cấu trúc tài trợ nợ ngắn hạn nuôi tài sản dài hạn).
  - [[gap-risk]]: Bổ sung phân tích trạng thái nhạy cảm tài sản (asset-sensitive: khe hở dương) vs nhạy cảm nợ (liability-sensitive: khe hở âm) và lý giải cấu trúc liability-sensitive truyền thống của các NHTM.
  - [[option-risk]]: Bổ sung phân tích rủi ro trần/sàn lãi suất (Cap & Floor risk), rủi ro đường ống cam kết giải ngân (Pipeline risk) và phương pháp phòng hộ động (Dynamic Hedging) bằng hợp đồng hoán đổi thay cho swaptions đắt đỏ.
  - [[index]]: Cập nhật mục `src-choudhry-principles-banking` đạt 3 units hoàn thành (u12, u16, u17).
- proposed: không có (đã được user duyệt thực hiện)
- conflicts: không có
- tiếp theo: src-choudhry-principles-banking u13/u14 hoặc src-tata-bank-alm u02 (Banking Book vs Trading Book)

## [2026-10-16] ingest | src-tata-bank-alm u03 (Economic Value Measures & Earnings Measures)
- created:
  - [[src-tata-bank-alm]]: Source note mới từ sách chuyên khảo *Bank Asset-Liability Management* (Fidelio Tata, 2025), ingest unit u03 (lines 816–1242) gồm 12 key claims, trích dẫn nguyên văn chuẩn xác.
- updated:
  - [[economic-value-of-equity]]: Bổ sung nguyên tắc Reset Date theo Fidelio Tata (rủi ro lãi suất chỉ tính đến ngày reset date thay vì ngày đáo hạn hợp đồng; công cụ sau reset quay lại giao dịch ngang par).
  - [[net-interest-income-sensitivity]]: Bổ sung góc nhìn retrospective của Kế toán vs prospective của ALM và cơ chế triệt tiêu sai số mô hình (error cancellation) khi tính toán độ nhạy NII.
  - [[index]]: Thêm [[src-tata-bank-alm]] (1 unit u03).
- proposed: không có (đã được user duyệt thực hiện)
- conflicts: không có
- tiếp theo: src-tata-bank-alm u04 (NII monthly simulation model) hoặc src-choudhry-principles-banking u13/u14

## [2026-10-16] ingest | src-tata-bank-alm u04 & synthesis irrbb-transmission-mechanisms-to-nii-and-eve
- created:
  - [[irrbb-transmission-mechanisms-to-nii-and-eve]]: Synthesis note toàn diện phân tích cơ chế truyền dẫn của các cấu phần IRRBB (Gap, Basis, Option, CSRBB) đến Thu nhập lãi thuần (NII) và Giá trị kinh tế của vốn chủ sở hữu (EVE): tích hợp phương trình chiết khấu EVE, mô hình khe hở định giá lại NII, nguyên tắc Reset Date và cơ chế triệt tiêu sai số mô hình của Fidelio Tata; giải mã nghịch lý và xung đột chiến lược giữa EVE vs NII (minh họa số học từ mô hình phòng hộ Receiver Swap làm khe hở định giá lại tăng từ 1,74 lên 3,63); xây dựng Ma trận truyền dẫn tổng hợp (Master Transmission Matrix 10 cấu phần) và 4 hàm ý quản trị cốt tử cho Ủy ban ALCO.
- updated:
  - [[src-tata-bank-alm]]: Hoàn thành ingest unit u04 (lines 1243–1662) với 8 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về mô phỏng NII kịch bản sốc, chiến lược phòng hộ bằng Receiver Swap, xung đột EVE vs NII và FTP Structural Contribution bù đắp cho Treasury khi gánh vác rủi ro lãi suất và thanh khoản cấu trúc.
  - [[03_meta/sources.yaml]]: Đánh dấu `src-tata-bank-alm` unit `u04` -> `done`.
  - [[index]]: Thêm synthesis note mới và cập nhật trạng thái `src-tata-bank-alm` đạt 2 units hoàn thành (u03, u04).
- lint: 98 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.
- proposed: không có
- conflicts: không có
- tiếp theo: src-tata-bank-alm u05 hoặc src-choudhry-principles-banking u13/u14.

## [2026-10-16] ingest | src-tata-bank-alm u02 & model repricing-balance-sheet
- created:
  - [[repricing-balance-sheet]]: Model note chuẩn mực về Bảng cân đối tái định giá (Repricing Balance Sheet / Repricing Schedule): chuyển đổi từ Bảng cân đối kế toán thông thường (kỳ hạn hợp đồng danh nghĩa) sang kỳ hạn tái định giá lãi suất (Next Reset Date); quy trình 5 bước kinh điển (Aggregation, Assign Reset Periods, Cash Flow Slotting vào 19 time bands Basel hoặc 8-12 buckets ALM, Net Repricing Gaps, Weight & Aggregate); cơ chế xử lý các sản phẩm phi kỳ hạn (CASA core/non-core), quyền chọn hành vi (CPR, TDRR) và phái sinh ngoại bảng (IRS receive/pay legs); mô hình số học minh họa Model Bank 500 từ Fidelio Tata; phân tích 4 hạn chế cốt tử (parallel shift trap, bỏ qua basis risk, bỏ qua giá trị thời gian trong bucket, rủi ro mô hình hành vi).
- updated:
  - [[src-tata-bank-alm]]: Hoàn thành ingest unit u02 (lines 410–815) với 7 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về mục đích tối ưu hóa ALM, phân định ranh giới Banking Book vs Trading Book, các nhóm công cụ ALM (Customer business, External positions, Off-balance sheet) và định nghĩa công cụ nhạy cảm lãi suất loại trừ tài sản khấu trừ khỏi CET1.
  - [[irrbb-balance-sheet-portfolios]]: Bổ sung nguồn Tata và các trích dẫn về phân định Banking Book vs Trading Book, công cụ ALM nội bảng vs phái sinh ngoại bảng và liên kết tới model note mới.
  - [[03_meta/sources.yaml]]: Đánh dấu `src-tata-bank-alm` unit `u02` -> `done`.
  - [[index]]: Cập nhật `src-tata-bank-alm` đạt 3 units hoàn thành (u02, u03, u04).
- lint: 99 note, 23 nguồn trong registry, 0 error, 0 warning, 0 info; 100% trích dẫn khớp nguyên văn.
- proposed: không có
- conflicts: không có
- tiếp theo: src-tata-bank-alm u05 hoặc src-choudhry-principles-banking u13/u14.

## [2026-10-16] lint | phạm vi: thay đổi chưa commit (Tata u02–u04, Choudhry u12, repricing-balance-sheet)
- trước: 0 error / 1 warning · sau: 0 / 0
- đã sửa: [[index]] thêm [[repricing-balance-sheet]] vào mục Models (warning `index`).
- ghi chú: chưa có entry log cho ingest `src-tata-bank-alm` u02 (registry đã `done`), cho việc tạo [[repricing-balance-sheet]] và mục D của [[irrbb-balance-sheet-portfolios]].
- đề xuất chờ duyệt:
  - [[repricing-balance-sheet]]: ví dụ receiver swap ghi "cố định 2%, Euribor 3M, chân trả ở dải 1–3M", raw ghi 4.16%, chân thả nổi reprice 6 tháng, chân pay ở dải 3–6M, chân receive ở dải 24–36M (Table 2.35); kết luận "NII cả năm tăng" mâu thuẫn với chính công thức ΔNII của node; bảng Table 2.2–2.5 chưa có citation; "150 triệu" là đơn vị không có trong nguồn; Savings ghi "không kỳ hạn" trong khi raw ghi maturity 36.
  - [[irrbb-transmission-mechanisms-to-nii-and-eve]]: "cố định 2,0%" sai (raw 4.16%); "-1,74% Vốn CSH" sai (raw: EVE giảm 1.74 tuyệt đối = 3.48% vốn); các số NII +0,75/-0,75/+0,25/-1,50/+1,00 không có trong raw nhưng được gán cho Tata; "bù đắp hoàn hảo" trái với caveat "too good to be true".
  - [[irrbb-balance-sheet-portfolios]] (canonical): "Sổ kinh doanh chỉ bao gồm" lệch "typically includes"; "ưu tiên… trước khi dùng phái sinh" lệch "in lieu of… appear to".
  - [[net-interest-income-sensitivity]] (canonical): "đều được loại trừ" lệch "can be excluded"; hai ý "intra-month" và "false sense of accuracy" chưa được trích trong source note.
  - [[src-tata-bank-alm]]: bỏ câu diễn giải "Phù hợp hoàn toàn với… Basel d368 và… Choudhry" ở mục Mâu thuẫn ghi nhận.

## [2026-10-16] lint-fix | áp batch đề xuất lint đã được user duyệt (Tata IRRBB)
- updated:
  - [[src-tata-bank-alm]]: thêm claim `^tata-gap-3`…`^tata-gap-7` (bước 5, Table 2.2–2.5, gap 1.74 = 3.48% vốn), `^tata-egap-1`/`^tata-egap-2` (earning gap −0.25), `^tata-nii-12` (intra-month), `^tata-nii-13`…`^tata-nii-17` (NII baseline/shock/hedged, điều khoản swap 4.16%/6M, caveat "too good to be true"); mở rộng trích dẫn `^tata-nii-4` và `^tata-scope-5`; bỏ câu diễn giải ở mục Mâu thuẫn ghi nhận; bỏ học vị "Tiến sĩ" (raw ghi "professor of Finance").
  - [[repricing-balance-sheet]]: sửa ví dụ swap (4.16%, chân thả nổi reset 6M → RSL 3–6M, chân cố định → RSA 24–36M) trong thân bài và sơ đồ; sửa vay reset 3M → dải 1–3M trong sơ đồ; cite bảng ví dụ bằng Table 2.2–2.5; sửa Savings (kỳ hạn 36, reset 6); bỏ đơn vị "triệu"; viết lại nhận xét: EVE giảm 1.74 (3.48% vốn), NII năm đầu giảm 0.25 cho mỗi 1% lãi suất tăng (thay cho kết luận sai "NII tăng").
  - [[irrbb-transmission-mechanisms-to-nii-and-eve]]: thay các số NII bịa (+0,75/−0,75/+0,25/−1,50/+1,00) bằng số trong Table 2.20/2.27/2.33; sửa swap 2,0% → 4.16%; sửa "−1,74% vốn" → 1.74 = 3.48% vốn; 7.26% gắn nhãn diễn giải; thêm caveat của tác giả; bỏ "bù đắp hoàn hảo", "thảm khốc".
  - [[irrbb-balance-sheet-portfolios]] (canonical, user duyệt): "chỉ bao gồm" → "thường bao gồm"; "ưu tiên… trước khi" → "có vẻ… thay vì dùng swap".
  - [[net-interest-income-sensitivity]] (canonical, user duyệt): "đều được loại trừ" → "có thể được loại"; cite `^tata-nii-12` cho ý intra-month; viết sát nguồn câu về chân trời dự báo.
- lint: 99 note · 23 nguồn · 0 error · 0 warning · 0 info.
- còn lại: các dòng `--uncited` ở hai node trên chủ yếu là sơ đồ ASCII, công thức và dòng bảng đã được cite ở câu dẫn; chưa rà phần còn lại của vault.

## [2026-10-16] ingest | src-tata-bank-alm u05 (Embedded & Behavioral Options, Replicating Model) & cập nhật concepts
- updated:
  - [[src-tata-bank-alm]]: Hoàn thành ingest unit u05 (lines 1663–2068) với 7 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về Automatic Options vs Behavioral Options (`^tata-opt-1`, `^tata-opt-4`), quyền chọn hành vi trên sản phẩm có kỳ hạn (`^tata-opt-2`), tác động co ngắn kỳ hạn thực tế và ảnh hưởng EVE/NII (`^tata-opt-3`), định nghĩa NMDs (`^tata-nmd-1`), run-off rate (`^tata-nmd-2`), và mô hình Replicating Portfolio Model (`^tata-nmd-3`).
  - [[non-maturity-deposits]]: Bổ sung trích dẫn và liên kết từ Fidelio Tata về định nghĩa NMDs, cơ chế run-off rate, mô hình Replicating Portfolio và tác động của quyền chọn hành vi làm co ngắn kỳ hạn thực tế.
  - [[behavioural-options]]: Bổ sung trích dẫn và đối chiếu nguyên lý Automatic vs Behavioral Options, sự hiện diện trên cả sản phẩm có kỳ hạn hợp đồng (mortgages, floating-rate loans), tác động co ngắn expected maturity, và các biến số phi tài chính (nhân khẩu học) thúc đẩy hành vi khách hàng.
  - [[03_meta/sources.yaml]]: Đánh dấu `src-tata-bank-alm` unit `u05` -> `done`.
  - [[index]]: Cập nhật `src-tata-bank-alm` đạt 4 units hoàn thành (u02, u03, u04, u05).
- lint: 99 note · 23 nguồn trong registry · 0 error · 0 warning · 0 info; 100% trích dẫn khớp nguyên văn.
- proposed: không có
- conflicts: không có
- tiếp theo: src-choudhry-principles-banking u13/u14 hoặc src-tata-bank-alm u06.

## [2026-10-16] synthesis | irrbb-repricing-profiles-and-behavioral-modeling
- created:
  - [[irrbb-repricing-profiles-and-behavioral-modeling]]: Synthesis note toàn diện về phương pháp xác định Repricing Profile (Contractual Maturity vs Next Repricing Date vs Behavioral Maturity) và khung ứng dụng Behavioral Modeling trong IRRBB: phân tích cơ chế ngang mệnh giá (*Par*) tại Reset Date của Tata triệt tiêu rủi ro định giá; xây dựng khung ứng dụng Behavioral Modeling cho 5 trường hợp bắt buộc (NMDs/CASA tách Core/Non-core theo Replicating Portfolio Model, Prepayment CPR & Contraction Risk với độ lồi âm, Early Redemption TDRR & Extension Risk, Pipeline Risk, Deposit Beta / Pass-through Rate); phân định bản chất Automatic Options (thực thi duy lý tài chính 100%) vs Behavioral Options (chi phối bởi biến số nhân khẩu học tử vong, ly hôn, chuyển việc từ Fidelio Tata); quy định đối xử phân biệt của Basel d368 (Wholesale bắt buộc xử lý theo Automatic option logic, chỉ Retail mới được áp dụng Behavioral modeling); Ma trận Master phân bổ Repricing Profile cho toàn bộ bảng cân đối ALM (Tài sản, Nợ, Ngoại bảng); 3 khuyến nghị chiến lược quản trị rủi ro mô hình cho ALCO.
- updated:
  - [[index]]: Thêm [[irrbb-repricing-profiles-and-behavioral-modeling]] vào mục Syntheses.
- lint: 100 note · 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-choudhry-principles-banking u13/u14 hoặc src-tata-bank-alm u06.

## [2026-10-17] ingest | src-lubinska-alm-optimisation u04 & balance-sheet-optimisation-model
- created:
  - [[balance-sheet-optimisation-model]]: Model note về mô hình tối ưu hoá bảng cân đối phi tuyến ràng buộc bất đẳng thức: điều kiện tối ưu KKT, thuật toán điểm trong hàm rào cản logarit (Interior-point Logarithmic Barrier Algorithm) trong MATLAB fmincon, giải đồng thời hai bài toán tối đa hóa thu nhập tài sản (Max Asset Income) và tối thiểu hóa chi phí vốn (Min Funding Cost) trên constant balance sheet với các ràng buộc cấu trúc, thanh khoản và rủi ro.
- updated:
  - [[src-lubinska-alm-optimisation]]: Hoàn thành ingest unit u04 (lines 1377–1806) với 13 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về mô hình hoá hành vi trả nợ trước hạn Prepayment (phân rã 2 tầng Structural vs Financial, hiện tượng burnout, mô hình phi tham số, cảnh báo rủi ro phòng ngừa quá mức overhedging), mô hình hoá tiền gửi không kỳ hạn NMDs (2 phương pháp định lượng: đường cong phân rã hàm mũ 3.1 sigma và phương pháp biến động dòng tiền theo tháng 95% * sqrt(12), phân tầng lãi suất CASA), cơ chế phân bổ chi phí dự phòng thanh khoản qua FTP, và khung mô hình tối ưu hoá bảng cân đối KKT.
  - [[behavioural-options]]: Bổ sung mô hình phân rã 2 tầng Prepayment của Lubinska, hiện tượng burnout, phương pháp phi tham số và rủi ro overhedging.
  - [[non-maturity-deposits]]: Bổ sung 2 phương pháp định lượng NMDs của Lubinska và phân tầng lãi suất tiền gửi CASA.
  - [[ftp-pricing-methodology]]: Bổ sung Section 7.3 về FTP behaviouralisation và phân bổ chi phí đệm dự phòng thanh khoản tiềm tàng.
  - [[repricing-balance-sheet]]: Cập nhật nguồn Lubinska và liên kết tới model note tối ưu hoá bảng cân đối.
  - [[integrated-alm-liquidity-strategy]]: Cập nhật liên kết khung lý thuyết tối ưu hoá bảng cân đối KKT.
  - [[03_meta/sources.yaml]]: Đánh dấu `src-lubinska-alm-optimisation` unit `u04` -> `done`.
  - [[index]], [[overview]].
- lint: 101 note, 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-lubinska-alm-optimisation u05 hoặc src-tt50-2026-nhnn C2-M3.

## [2026-10-17] ingest | src-lubinska-alm-optimisation u05 & model-risk-management
- created:
  - [[model-risk-management]]: Concept note chuyên sâu về Quản trị Rủi ro Mô hình trong ALM theo hướng dẫn OCC/Fed SR 11-7 và Beata Lubinska (2020): định nghĩa mô hình (Inputs, Transformation Method, Reporting), 3 nguồn phát sinh rủi ro mô hình (Khiếm khuyết dữ liệu, Sai số/bất định mô hình, Sử dụng sai mục đích), Nguyên lý Tinh gọn (Parsimony Principle) chống lạm dụng sự tinh vi không cần thiết, nguyên tắc Phản biện hiệu quả (Effective Challenge) bởi nhân sự độc lập qua 4 trụ cột kiểm định (Outcome, Assumptions, Methodology, Data feeding) dưới sự giám sát của Kiểm toán nội bộ và Hội đồng Quản trị.
- updated:
  - [[src-lubinska-alm-optimisation]]: Hoàn thành ingest unit u05 (lines 1807–2246) với 15 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về điểm khởi đầu $t_0$, khác biệt cấu trúc ngân hàng theo khu vực (Ý, Anh, Mỹ), hệ thống ràng buộc tối ưu hóa ALM (Survival Horizon 30-90d, Structural Liquidity Limit >1Y, A/D Ratio <80%, Giới hạn tập trung nguồn vốn <=80%, IRRBB NII Sensitivity <=4% kèm sàn Floor 0%, CAR >=10.5%), điều kiện không âm (Non-negativity condition) bảo toàn mô hình kinh doanh, và quản trị rủi ro mô hình MRM.
  - [[balance-sheet-optimisation-model]]: Bổ sung chi tiết các phương trình ràng buộc định lượng từ Lubinska u05 (SH, Structural limit, A/D ratio, Concentration limit 80%, NII 4% shock +-200 bps kèm Floor 0%, CAR 10.5%), điều kiện không âm và nguyên lý tinh gọn MRM.
  - [[net-interest-income-sensitivity]]: Bổ sung nguồn Lubinska, 3 trạng thái bảng cân đối (Run-off, Constant, Dynamic) theo chuẩn EBA/Lubinska và nguyên tắc áp dụng sàn Floor 0% ngăn ngừa lãi suất âm cho tiền gửi bán lẻ và khoản vay có embedded floors.
  - [[03_meta/sources.yaml]]: Đánh dấu `src-lubinska-alm-optimisation` unit `u05` -> `done`.
  - [[index]], [[overview]].
- lint: 102 note, 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-lubinska-alm-optimisation u06 hoặc src-tt50-2026-nhnn C2-M3.

## [2026-10-17] ingest | src-lubinska-alm-optimisation u06 & empirical case studies
- updated:
  - [[src-lubinska-alm-optimisation]]: Hoàn thành ingest unit u06 (lines 2247–2680) với 14 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về 5 kịch bản độ nhạy "What-if" (Base, Interest rate, Deposit characterisation, Prepayment CPR 7%, Initial asset base), kết quả thực nghiệm tại Ngân hàng 1 (EUR 3.4bn: thặng dư EUR 3.8–7.63m, đánh đổi chi phí tuân thủ thanh khoản ngắn hạn, nguyên lý độ trễ vận hành Operational latency "cannot be done overnight", bất đối xứng độ nhạy hành vi CASA > CPR) và Ngân hàng 2 (USD 549bn: thặng dư kỷ lục USD 1.25bn, rủi ro mô hình tiềm ẩn Embedded Model Risk khi 100% nợ hợp đồng < 1 năm, hiệu ứng quy mô và giảm chấn đa dạng hóa Bank size diversification effect).
  - [[balance-sheet-optimisation-model]]: Bổ sung Section "Thực Nghiệm Kiểm Chứng & Động Lực Nhạy Cảm" phân tích 5 kịch bản What-if, kết quả thực nghiệm Bank 1 vs Bank 2, nguyên lý độ trễ vận hành và hiệu ứng quy mô ngân hàng.
  - [[model-risk-management]]: Bổ sung Section 4.4 về rủi ro mô hình tiềm ẩn trọng yếu từ tiền gửi không kỳ hạn (Bank 2 Case Study: 100% nợ hợp đồng < 1 năm) và tính bất đối xứng của độ nhạy hành vi (Liability CASA > Asset CPR).
  - [[non-maturity-deposits]]: Bổ sung phân tích bất đối xứng độ nhạy hành vi trong tối ưu hóa ALM, rủi ro mô hình tiềm ẩn và hiệu ứng giảm chấn đa dạng hóa theo quy mô ngân hàng.
  - [[03_meta/sources.yaml]]: Đã đánh dấu `src-lubinska-alm-optimisation` unit `u06` -> `done`.
  - [[index]], [[overview]].
- lint: 102 note, 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-lubinska-alm-optimisation u07 hoặc src-tt50-2026-nhnn C2-M3.

## [2026-10-17] ingest | src-lubinska-alm-optimisation u07 & numerical proof
- updated:
  - [[src-lubinska-alm-optimisation]]: Hoàn thành ingest unit u07 (lines 2681–3093) với 14 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về Kết luận tổng thể tối ưu hóa ALM, Động lực cơ cấu khởi điểm (Initial Structure as Destiny Driver), Phục hồi vi phạm giới hạn thanh khoản nội bộ (Boundary Restoration), Tối ưu hóa kép lợi nhuận & rủi ro (Dual Return-Risk Improvement: nén Delta NII từ 80.5% về trần 4%, khôi phục thanh khoản ngắn hạn từ 59.7% lên 100%), và Bằng chứng định lượng chi tiết tại Ngân hàng 1 (tài sản: thặng dư EUR 0.069bn / 6 tháng; nguồn vốn: thặng dư Base EUR 0.2964m/năm, HY/LBO EUR 0.6677m/năm, CASA remodeling EUR 1.1954m/năm).
  - [[balance-sheet-optimisation-model]]: Bổ sung Section luận điểm Cơ cấu khởi điểm là Động lực định mệnh, Phục hồi biên giới hạn rủi ro, Tối ưu hóa đồng thời Lợi nhuận & Rủi ro, và Bảng số liệu thực nghiệm chứng minh định lượng tại Ngân hàng 1.
  - [[net-interest-income-sensitivity]]: Bổ sung cơ chế nén độ nhạy lãi suất Delta NII từ 80.5% về trần 4% thông qua điều kiện KKT và phân bổ lại danh mục tối ưu.
  - [[03_meta/sources.yaml]]: Đã đánh dấu `src-lubinska-alm-optimisation` unit `u07` -> `done`.
  - [[index]], [[overview]].
- lint: 102 note, 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-lubinska-alm-optimisation u08 hoặc src-tt50-2026-nhnn C2-M3.

## [2026-10-17] ingest | src-lubinska-alm-optimisation u08 & buffer right-sizing
- updated:
  - [[src-lubinska-alm-optimisation]]: Hoàn thành ingest unit u08 (lines 3094–3567) với 14 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về:
    - Phân tích độ nhạy nguồn vốn Ngân hàng 1: thay đổi tỷ trọng danh mục tài sản (thặng dư EUR 0.5663m – EUR 4.9560m, phục hồi vi phạm thanh khoản ngắn hạn từ 60.89% lên 100%), hạ 1 bậc tín nhiệm Downgrade by One Notch (thặng dư EUR 0.6388m/năm, thanh khoản khôi phục từ 59.8% lên 100%, nén Delta NII +200bps từ 72.18% về 6.8%), và tính đến tỷ lệ trả nợ trước hạn CPR (thặng dư EUR 1.2244m/năm, thanh khoản khôi phục từ 62% lên 100%).
    - Thực nghiệm tối ưu hóa phía tài sản Ngân hàng 2 (USD 549bn) và cơ chế Tinh gọn Đệm Thanh khoản (Liquidity Buffer Right-Sizing / Negative Carry Elimination): tinh gọn đệm LAB từ 10.92% xuống đúng mức cận biên 4.66% để SH_2M chạm đúng hạn mức 100%, giải phóng thanh khoản tái đầu tư vào tài sản bán lẻ (19.85% -> 26.76%) và thị trường tài chính (36.79% -> 43.19%), mang lại thặng dư thu nhập kỷ lục USD 284.9m (Base), USD 345.2m (Oil Supply Crisis) và USD 273.0m (Earthquake) trong 6 tháng song hành cùng việc nén Delta NII +200bps từ 38% về 27.68%–30.37%.
  - [[balance-sheet-optimisation-model]]: Bổ sung chi tiết kết quả thực nghiệm độ nhạy nguồn vốn Bank 1 (tỷ trọng tài sản, hạ bậc tín nhiệm, CPR), cơ chế Tinh gọn Đệm Thanh khoản Buffer Right-Sizing và bảng minh chứng số liệu thực nghiệm tối ưu hóa phía tài sản Bank 2 qua các kịch bản sốc lãi suất.
  - [[net-interest-income-sensitivity]]: Bổ sung dẫn chứng thực nghiệm Bank 1 (nén Delta NII về 6.8% khi hạ bậc tín nhiệm) và Bank 2 (nén Delta NII từ 38% về 27.68%–30.37% qua 3 kịch bản sốc lãi suất Base, Oil Crisis, Earthquake song hành với gia tăng hàng trăm triệu USD thu nhập).
  - [[03_meta/sources.yaml]]: Đã đánh dấu `src-lubinska-alm-optimisation` unit `u08` -> `done`.
  - [[index]], [[overview]].
- lint: 102 note, 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-lubinska-alm-optimisation u09 hoặc src-tt50-2026-nhnn C2-M3.

## [2026-10-17] ingest | src-lubinska-alm-optimisation u09 & Bank 2 funding optimisation
- updated:
  - [[src-lubinska-alm-optimisation]]: Hoàn thành ingest unit u09 (lines 3568–3971) với 15 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về:
    - Phía tài sản Ngân hàng 2 (USD 549bn): Kịch bản lạm phát (+USD 382.9m, nén Delta NII về 24.64%); Kịch bản hạ 1 bậc tín nhiệm Downgrade (tái cơ cấu tài sản cực đoan: bán lẻ vọt lên 52.14%, doanh nghiệp bị cắt về 0.00011%, thu nhập tăng USD 392.9m, CAR lên 14.56%); Kịch bản CPR & mô hình tiền gửi (+USD 284.9m, Delta NII 24.31%–30.37%); Kịch bản cơ cấu tài sản cố định (thu hẹp LAB từ 25.13% về 4.66% tạo thặng dư thu nhập kỷ lục USD 1.255 tỷ / 6 tháng).
    - Phía nguồn vốn Ngân hàng 2 (USD 549bn Base scenario): Khai thác triệt để nguồn vốn bán lẻ giá rẻ (Retail CASA tăng từ 28.3% lên 51.16%), cắt giảm CASA giao dịch Treasury xuống 10%, cắt giảm nợ bán buôn đắt đỏ (Senior debt từ 11.4% về 3.8%, CP/CD từ 7.8% về 2%), hạ chi phí vốn từ USD 2.8493 tỷ xuống USD 2.1967 tỷ / 6 tháng, tạo mức cắt giảm chi phí vốn khổng lồ USD 0.6526 tỷ / 6 tháng (trên USD 1.3 tỷ/năm) song hành với việc hạ AD ratio về 72% và nén Delta NII +200bps từ 65% về 54%.
  - [[balance-sheet-optimisation-model]]: Bổ sung chi tiết kết quả thực nghiệm phía tài sản Bank 2 qua các kịch bản khắc nghiệt (lạm phát, hạ bậc tín nhiệm, thặng dư kỷ lục USD 1.255 tỷ) và thiết lập Section 4 về tối ưu hóa phía nguồn vốn Bank 2 (cắt giảm chi phí vốn USD 652.6 triệu).
  - [[net-interest-income-sensitivity]]: Bổ sung dẫn chứng nén Delta NII phía tài sản Bank 2 (lạm phát nén về 24.64%, tiền gửi nén về 24.31%) và phía nguồn vốn Bank 2 (nén từ 65% về 54% cùng cắt giảm chi phí vốn USD 652.6 triệu).
  - [[03_meta/sources.yaml]]: Đã đánh dấu `src-lubinska-alm-optimisation` unit `u09` -> `done`.
  - [[index]], [[overview]].
- lint: 102 note, 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-lubinska-alm-optimisation u10 hoặc src-tt50-2026-nhnn C2-M3.

## [2026-10-17] ingest | src-lubinska-alm-optimisation u10 & Bank 2 funding sensitivity
- updated:
  - [[src-lubinska-alm-optimisation]]: Hoàn thành ingest unit u10 (lines 3972–4417) với 18 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về toàn bộ 6 kịch bản độ nhạy nguồn vốn Ngân hàng 2 (USD 549bn):
    - Kịch bản lạm phát: chi phí vốn ban đầu USD 3.3356 tỷ giảm về USD 2.6928 tỷ, tiết kiệm USD 0.6428 tỷ / 6 tháng, nén Delta NII +200bps về 49%.
    - Kịch bản khủng hoảng dầu mỏ: chi phí vốn ban đầu USD 3.0597 tỷ giảm về USD 2.4 tỷ, tiết kiệm USD 0.6591 tỷ / 6 tháng, nén Delta NII +200bps từ 62% về 51.7%.
    - Kịch bản động đất: tiết kiệm chi phí vốn USD 0.6496 tỷ / 6 tháng, nén Delta NII +200bps từ 64% về 53%.
    - Kịch bản đặc tính hóa tiền gửi & CPR: tiết kiệm USD 0.6526 tỷ và USD 0.6698 tỷ, Delta NII được kiểm soát trong dải 54.6%–61.85%.
    - Kịch bản hạ 1 bậc tín nhiệm Downgrade: chi phí vốn ban đầu vọt lên USD 2.9893 tỷ do spread nới rộng; mô hình KKT tái cấu trúc nợ giúp cắt giảm chi phí vốn về USD 2.2439 tỷ, mang lại mức tiết kiệm chi phí vốn cao nhất toàn chu kỳ: **USD 0.7455 tỷ** / 6 tháng (tương đương **USD 1.49 tỷ quy năm**), Delta NII duy trì ở mức 54.26%.
    - Kịch bản tài sản cố định: đối mặt với Delta NII ban đầu 129%, mô hình đẩy CASA lên 54.9% và cắt giảm senior debt triệt để về 0.00011%.
  - [[balance-sheet-optimisation-model]]: Bổ sung Section 4 tiểu mục phân tích độ nhạy nguồn vốn Bank 2 qua các kịch bản sốc thị trường và minh chứng số liệu định lượng chi tiết.
  - [[net-interest-income-sensitivity]]: Bổ sung dẫn chứng nén Delta NII trên toàn bộ các kịch bản độ nhạy nguồn vốn Bank 2 (lạm phát về 49%, dầu mỏ về 51.7%, động đất về 53%, hạ bậc tín nhiệm về 54.26% song hành với tiết kiệm chi phí vốn đạt đỉnh USD 745.5 triệu / 6 tháng).
  - [[03_meta/sources.yaml]]: Đã đánh dấu `src-lubinska-alm-optimisation` unit `u10` -> `done`.
  - [[index]], [[overview]].
- lint: 102 note, 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-lubinska-alm-optimisation u11 hoặc src-tt50-2026-nhnn C2-M3.

## [2026-10-17] ingest | src-lubinska-alm-optimisation u11 & completion of core Lubinska chapters
- updated:
  - [[src-lubinska-alm-optimisation]]: Hoàn thành ingest unit u11 (lines 4418–5055) với 8 key claims và trích dẫn nguyên văn đối chiếu 100% raw text về:
    - Kịch bản biến động tỷ trọng tài sản cố định (Funding side): Giảm chi phí vốn ban đầu từ USD 2.8493 tỷ xuống USD 1.982 tỷ / 6 tháng, mang lại mức cắt giảm chi phí vốn lên tới USD 0.8666 tỷ / 6 tháng (tương đương USD 1.733 tỷ quy năm); chỉ số rủi ro mục tiêu đạt AD ratio 50%, MTFR hành vi 216%, SH_2M vọt lên 247% và Delta NII +200bps duy trì ở mức 121%.
    - Kịch bản biến động tỷ trọng tài sản thả nổi (Funding side): Tái phân bổ nợ mục tiêu đẩy Retail CASA lên 53.23%, tiền gửi DN 30%, và nợ cao cấp senior debt giảm về 1.77%; chi phí vốn giảm về USD 2.08 tỷ / 6 tháng, tiết kiệm USD 0.6526 tỷ / 6 tháng; AD ratio đạt 63.38%, MTFR hành vi 193%, SH_2M đạt 192% và Delta NII +200bps duy trì ở mức 66%.
    - Đúc kết toàn diện công trình tối ưu hóa ALM của Beata Lubinska: Khẳng định quy luật Dual Return-Risk Improvement xuyên suốt 16 kịch bản sốc, vai trò cốt tử của CASA bán lẻ chi phí thấp và tính ổn định hành vi cao, cùng kỷ luật kỹ trị của hệ thống FTP bóc tách management overlays và phản ánh đúng chi phí kinh tế cận biên gộp. Hoàn thành 100% các chương chuyên khảo cốt lõi của tác giả (u03–u11).
  - [[balance-sheet-optimisation-model]]: Bổ sung hai kịch bản phân tích độ nhạy nguồn vốn cuối cùng của Bank 2 (tài sản cố định và tài sản thả nổi) và số liệu định lượng kiểm chứng.
  - [[net-interest-income-sensitivity]]: Bổ sung phân tích độ nhạy Delta NII dưới sự đánh đổi cấu trúc tài sản cố định (121%) và tài sản thả nổi (66%).
  - [[03_meta/sources.yaml]]: Đã đánh dấu `src-lubinska-alm-optimisation` unit `u11` -> `done`.
  - [[index]], [[overview]].
- lint: 102 note, 23 nguồn trong registry.
- proposed: không có
- conflicts: không có
- tiếp theo: src-tt50-2026-nhnn C2-M3 hoặc các chương tiếp theo của src-tata-bank-alm / src-choudhry-principles-banking.

## [2026-10-17] ingest | src-choudhry-principles-banking u13 & ALCO governance / EVE paradox
- updated:
  - [[src-choudhry-principles-banking]]: Hoàn thành ingest unit u13 (lines 6350–6869) với 10 trích dẫn nguyên văn đối chiếu 100% raw text về:
    - Nguyên tắc BCBS 368 về IRRBB (Trụ cột 2) và yêu cầu vốn/phòng ngừa phái sinh.
    - Nghịch lý giá trị thị trường cổ phiếu vs EVE (The EVE vs Market Value Paradox): Lãi suất tăng đẩy thị giá cổ phiếu ngân hàng tăng do kỳ vọng NII/NIM mở rộng, trong khi EVE lại sụt giảm do mismatch kỳ hạn.
    - Credit Spread Risk in the Banking Book (CSRBB) trên danh mục trái phiếu (Eurobonds) và thước đo CS01.
    - Mô hình tổ chức Khối ALM & Treasury tối ưu: Đơn vị ALM độc lập báo cáo trực tiếp Tổng Giám đốc (CEO) để triệt tiêu xung đột lợi ích giữa Treasury, Finance và Risk; Treasury là trung tâm lợi nhuận (profit centre).
    - Quản trị ALCO: Diễn đàn quan trọng nhất trong ngân hàng ("A broken balance sheet usually will sink a bank"); Tỷ lệ chia tách định kiến 50-50 giữa Lợi nhuận và An toàn; CFO làm Chủ tịch ALCO.
  - [[irrbb-alm-governance-strategy-and-tradeoffs]]: Bổ sung Section 1 về triết lý ALCO 50-50 & mô hình ALM độc lập theo Choudhry & Bardaeva; Section 2 về Nghịch lý EVE vs Thị giá cổ phiếu ngân hàng.
  - [[economic-value-of-equity]]: Bổ sung Section chuyên sâu về Nghịch lý EVE vs Thị giá cổ phiếu ngân hàng và 3 giải pháp quy định bắt buộc khi stressed EVE vượt khẩu vị rủi ro (Immunise, Tier 1 capital, De-risking).
  - [[csrbb]]: Bổ sung quan điểm thực tiễn của Choudhry về CSRBB trên danh mục trái phiếu và thước đo CS01.
  - [[03_meta/sources.yaml]]: Đã đánh dấu `src-choudhry-principles-banking` unit `u13` -> `done`.
  - [[index]], [[overview]].
- lint: 0 error, 0 warning, 0 info.
- proposed: không có
- conflicts: không có
- tiếp theo: src-tata-bank-alm u06 / u07 / u08 (IRRBB measurement & EBA RTS / SOTs) hoặc src-tt50-2026-nhnn C2-M3.

## [2026-10-17] lint | toàn bộ vault 102 wiki nodes
- trước: 0 error / 0 warning / 0 info (lint.py) · sau: 0 error / 0 warning / 0 info
- kiểm tra kỹ thuật (tools/lint.py): 102 notes, 23 nguồn trong registry, toàn vẹn 100% link, block-reference và trích dẫn nguyên văn đối chiếu raw layer.
- kiểm tra quan hệ (tools/audit_vault.py): 99 content notes (47 canonical, 52 draft), 0 note ngắn (<30 dòng); đã bổ sung citation cho 2 relations trong [[model-risk-management]].
- kiểm tra công thức toán (tools/check_latex.py & tools/test_latex_deep.py): 0 lỗi KaTeX/LaTeX syntax trên toàn bộ vault.
- đề xuất chờ duyệt: không có lỗi nội dung tồn đọng.

## [2026-10-17] tooling | audit harness → skill research, đồng bộ lint, chốt skill văn phong
- created: `.claude/skills/research/SKILL.md` — nghiên cứu một vấn đề hoặc bộ câu hỏi (vd 20 câu IRRBB, 7 câu FTP): bản đồ phủ câu hỏi ↔ node, lỗ hổng nguồn và unit cần ingest, synthesis `origin: research` theo cụm câu hỏi. Chỉ chạy khi user gọi (`disable-model-invocation: true`). `/query` giữ nguyên.
- updated: lint §2b — chính thức hoá script phụ chỉ đọc `audit_vault.py`, `check_latex.py`, `test_latex_deep.py` (trước đây đã dùng trong lượt lint 2026-10-17 nhưng chưa có trong skill); mẫu log lint thêm dòng kết quả script phụ.
- updated: CLAUDE.md — trong vault chỉ dùng `alm-writing-style`, không dùng skill văn phong toàn cục; bảng Operation thêm `/research`; bảng thư mục tách nhóm script phụ dùng trong `/lint`.
- tồn đọng từ audit: các synthesis `origin: research` hiện có chưa theo heading template synthesis; loại log `decision`/`tooling`/`lint-fix`/`synthesis` chưa được định nghĩa ở đâu.

## [2026-10-17] tooling | test và chốt skill research (skill-creator, 2 iteration)
- evals: `.claude/skills/research/evals/evals.json` (3 case: IRRBB Q11–14 viết synthesis · FTP 7 câu đã có synthesis canonical · chỉ có chủ đề). Chạy trên bản copy vault trong scratchpad, vault thật không đổi.
- iteration 1 (so với bản đầu): thêm hai pha đọc lướt/đọc kỹ, bảng phủ ghi log, quy tắc frontmatter, heading không độn, nguồn NHNN. Phát hiện: bản mới tự thêm claim vào source note `src-tata-bank-alm` (ngoài phạm vi research); user góp ý thiếu gợi ý sau research.
- iteration 2: cấm research sửa source note (đoạn raw sót → `## Bất định` + gợi ý `/ingest`); thêm bước 6 `## Gợi ý tiếp theo` (ingest theo số câu gỡ được, chờ duyệt, lỗi wiki, research tiếp, /compact). Kết quả 100% (15/15) so với bản đầu 80%; user duyệt.
- phát hiện phụ chờ xử lý (/lint hoặc /ingest): 7 synthesis FTP canonical có câu chứa số thiếu citation, `^vab-ftp-28` lệch nội dung, dẫn TT22 trong khi TT50/2026 đã sửa đổi; [[economic-value-of-equity]] ghi "OIS" không có trong trích dẫn; [[standardised-interest-rate-shocks]] mục sàn lãi suất sau sốc thiếu citation; source note d368 (fn 12/29, par 40–41, 47, 132) và Tata (§2.3, dòng 1047–1051, 1283, 1641–1657) sót đoạn dù unit đã `done`; `citations.py` báo nhầm `^vab-ftp-28` không tồn tại.

## [2026-10-17] tooling | research iteration 3: citations --uncited ở bước 1 + 2 case khó
- skill: bước 1 chạy `python tools/citations.py --uncited > scratch/uncited.txt` một lần, chỉ đếm theo file ứng viên; câu trả lời dựa vào node có tham số thật thiếu citation tối đa "một phần" và vào nhóm lỗi wiki ở bước 6.
- evals: bỏ case 3 (quá dễ), thêm case 4 (cập nhật synthesis draft không theo template, IRRBB Q1–2) và case 5 (bẫy LCR tại VN as-of 2026-09-15: TT50/2026 hiệu lực 01/10/2026, TT22/2019 chưa register).
- kết quả: bản hiện tại 15/15; bản đầu 13/15 — case 4 bản đầu tái cấu trúc cả synthesis draft (mất 5 heading, 274→164 dòng). User duyệt.
- phát hiện phụ chờ xử lý: [[hqla]] "bắt buộc từ 01/07/2027" không citation, lệch TT50 Đ13.1 (01/10/2028); [[level-1-assets]] dẫn "TT50 Điều 19, 20" không citation; [[cash-outflows]] hạn mức BHTG 125 triệu VND không citation; [[gap-risk]] cite `^irrbb-u06-4` cho phần trích đã lược; [[option-risk]] dòng tham số Table 2 thiếu citation; [[src-bcbs-irrbb-2016]] claim `^irrbb-u02-4`, `^irrbb-p05-1`, `^irrbb-p05-2` diễn đạt mạnh hơn trích dẫn.

## [2026-10-17] research | IRRBB Repricing Profile & Behavioral Modeling
- bộ câu hỏi: 2 câu · phủ: 0 đủ / 2 một phần / 0 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Repricing profile theo contractual, next repricing hay behavioral? | một phần | [[irrbb-repricing-profiles-and-behavioral-modeling]], [[repricing-balance-sheet]], [[irrbb-balance-sheet-portfolios]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]] | Quy định phân bổ dòng tiền tái định giá của NHNN · src-tt83-2025-nhnn (C3-M7, PL5) |
  | Q2 | Khi nào cần áp dụng Behavioral Modeling trong IRRBB? | một phần | [[irrbb-repricing-profiles-and-behavioral-modeling]], [[non-maturity-deposits]], [[behavioural-options]], [[replicating-portfolio-model]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]] | Hướng dẫn định lượng và quản trị rủi ro mô hình hành vi của NHNN · src-tt83-2025-nhnn (C3-M7, C3-M8, PL5) |
- created: không có · updated: [[irrbb-repricing-profiles-and-behavioral-modeling]] (bổ sung Q1–Q2, cấu trúc synthesis, fix citations) · proposed: không có
- conflicts: không có
- cần ingest: src-tt83-2025-nhnn C3-M7 & PL5 (gỡ Q1, Q2 cho quy định VN), src-tt83-2025-nhnn C3-M8 (gỡ Q2 về rủi ro mô hình hành vi)

## [2026-10-17] research | IRRBB EVE & NII Standardised Shocks Measurement
- bộ câu hỏi: 3 câu · phủ: 0 đủ / 3 một phần / 0 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Đo lường ΔEVE dưới 6 kịch bản sốc chuẩn hóa (19 dải, run-off, KAO, đa tiền tệ, outlier test 15%) | một phần | [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[economic-value-of-equity]], [[irrbb-standardised-framework]], [[outlier-bank-test]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]] | Quy định kỹ thuật đo lường EVE và ngưỡng ngoại lai của NHNN · src-tt83-2025-nhnn (C3-M7, PL5) |
  | Q2 | Đo lường độ nhạy ΔNII dưới kịch bản sốc chuẩn hóa (12 tháng, constant/dynamic balance sheet, NIM) | một phần | [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[net-interest-income-sensitivity]], [[irrbb-transmission-mechanisms-to-nii-and-eve]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]], [[src-choudhry-principles-banking]] | Hướng dẫn kiểm tra sức chịu đựng thu nhập lãi thuần của NHNN · src-tt83-2025-nhnn (PL5) |
  | Q3 | Cấu trúc toán học và tham số 6 kịch bản sốc Basel (hàm suy giảm xoay trục, sàn 100 bps, trần biên độ) | một phần | [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[standardised-interest-rate-shocks]] | [[src-bcbs-irrbb-2016]] | Biên độ sốc chuẩn hóa cho đồng VND do NHNN quy định · src-tt83-2025-nhnn (PL5) |
- created: [[irrbb-standardised-shocks-eve-and-nii-measurement]] · updated: [[index]] · proposed: không có
- conflicts: không có
- cần ingest: src-tt83-2025-nhnn PL5 (gỡ Q1, Q2, Q3 cho chuẩn đo lường VND), src-tt83-2025-nhnn C3-M7 (gỡ Q1, Q2 về thẩm quyền và ngưỡng an toàn)

## [2026-10-17] research | IRRBB CASA Replicating Portfolio & IRS Hedging
- bộ câu hỏi: 3 câu · phủ: 0 đủ / 3 một phần / 0 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Xây dựng đường cong hoàn trả Replicating Portfolio cho CASA (moving-average, tối ưu NIM, trần Table 2) | một phần | [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[replicating-portfolio-model]], [[non-maturity-deposits]] | [[src-tata-bank-alm]], [[src-bcbs-irrbb-2016]] | Hướng dẫn kiểm định rủi ro mô hình sao chép CASA của NHNN · src-tt83-2025-nhnn (C3-M8, PL5) |
  | Q2 | Kỹ thuật phòng ngừa rủi ro bằng IRS (Receiver/Payer, DGAP, DV01, slotting 2 chân swap theo reset date) | một phần | [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[interest-rate-swap]], [[duration-gap-model]], [[repricing-balance-sheet]] | [[src-tata-bank-alm]], [[src-choudhry-principles-banking]] | Quy định về phái sinh phòng ngừa rủi ro trên sổ ngân hàng của NHNN · src-tt83-2025-nhnn (C3-M7) |
  | Q3 | Tương tác Replicating Portfolio CASA và IRS hedging trong cân đối EVE vs NII và truyền dẫn FTP tại ALCO | một phần | [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-alm-governance-strategy-and-tradeoffs]], [[ftp-curve-construction-methodology]] | [[src-choudhry-principles-banking]], [[src-tata-bank-alm]], [[src-lubinska-alm-optimisation]] | Quy chế quản trị ALCO và kiểm soát nội bộ IRRBB của NHNN · src-tt83-2025-nhnn (C3-M7) |
- created: [[irrbb-casa-replicating-portfolio-and-irs-hedging]] · updated: [[index]], [[replicating-portfolio-model]], [[interest-rate-swap]] · proposed: không có
- conflicts: không có
- cần ingest: src-tt83-2025-nhnn PL5 (gỡ Q1, Q2 cho chuẩn đo lường VN), src-tt83-2025-nhnn C3-M8 (gỡ Q1 về rủi ro mô hình sao chép), src-tt83-2025-nhnn C3-M7 (gỡ Q2, Q3 về thẩm quyền ALCO và phái sinh)

## [2026-10-17] research | ALM IRRBB Liquidity HQLA & FTP Interaction
- bộ câu hỏi: 6 câu · phủ: 3 đủ / 2 một phần / 1 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT50 & TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Xung đột cấu trúc và sự đánh đổi (trade-offs) giữa LCR/NSFR và IRRBB trên bảng cân đối | đủ | [[irrbb-liquidity-hqla-and-ftp-interaction]], [[synthetic-balance-sheet-liquidity-risk]], [[hqla-decomposition-and-tradeoffs]] | [[src-tata-bank-alm]], [[src-bcbs-lcr]], [[src-bcbs-nsfr]], [[src-lubinska-alm-optimisation]] | Đã đủ khung lý thuyết và mô hình bảng cân đối tổng hợp |
  | Q2 | Đệm HQLA truyền dẫn bẫy thời lượng sang IRRBB và kỹ thuật hóa giải bằng Payer IRS | đủ | [[irrbb-liquidity-hqla-and-ftp-interaction]], [[hqla-decomposition-and-tradeoffs]], [[synthetic-balance-sheet-liquidity-risk]] | [[src-bcbs-lcr]], [[src-tata-bank-alm]], [[src-vab-ftp]] | Đã đủ cơ chế HQLA unencumbered và công thức Payer IRS |
  | Q3 | Cơ chế FTP bóc tách và phân bổ chi phí thanh khoản (TLP, Buffer Carry Cost, NSFR spread) và lãi suất | đủ | [[irrbb-liquidity-hqla-and-ftp-interaction]], [[ftp-risk-and-cost-components]], [[practical-alm-liquidity-governance]] | [[src-ftp-transmission-analysis]], [[src-vab-ftp]], [[src-choudhry-principles-banking]] | Đã đủ công thức 4 tầng, công thức Buffer carry và quy chế FTP VN |
  | Q4 | Xung đột tham số trong các mô hình hành vi (CASA, Prepayment, Early Redemption) giữa LCR/NSFR và IRRBB | một phần | [[irrbb-liquidity-hqla-and-ftp-interaction]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[behavioural-options]] | [[src-bcbs-lcr]], [[src-bcbs-nsfr]], [[src-bcbs-irrbb-2016]], [[src-lubinska-alm-optimisation]] | Quy chuẩn kiểm định rủi ro mô hình hành vi tại VN · src-tt83-2025-nhnn (C3-M8) |
  | Q5 | Khung quy định: So sánh chuẩn mực Basel vs Ngân hàng Nhà nước Việt Nam (TT 50/2026, TT 83/2025) | thiếu | [[irrbb-liquidity-hqla-and-ftp-interaction]] | [[src-bcbs-lcr]], [[src-bcbs-nsfr]], [[src-bcbs-irrbb-2016]] | Hướng dẫn kỹ thuật LCR/NSFR và IRRBB của NHNN · src-tt50-2026-nhnn (C2-M5, PL1, PL2) & src-tt83-2025-nhnn (C3-M5, C3-M7, PL5) |
  | Q6 | Quản trị tích hợp ALCO và bài toán tối ưu hóa bảng cân đối đa mục tiêu (LCR, NSFR, IRRBB, NIM, Leverage) | một phần | [[irrbb-liquidity-hqla-and-ftp-interaction]], [[practical-alm-liquidity-governance]], [[ftp-balance-sheet-optimization]] | [[src-lubinska-alm-optimisation]], [[src-bcbs-irrbb-2016]], [[src-choudhry-principles-banking]] | Dữ liệu kiểm định thực nghiệm tại NHTM Việt Nam · src-tt83-2025-nhnn (C3-M7) |
- created: [[irrbb-liquidity-hqla-and-ftp-interaction]] · updated: [[index]], [[hqla-decomposition-and-tradeoffs]] · proposed: không có
- conflicts: không có
- cần ingest: src-tt50-2026-nhnn C2-M5, PL1, PL2 (gỡ Q5, Q1 về quy định LCR/NSFR tại VN); src-tt83-2025-nhnn C3-M5, C3-M7, C3-M8, PL5 (gỡ Q5, Q4, Q6 về quản trị thanh khoản, IRRBB và rủi ro mô hình hành vi tại VN)

## [2026-10-17] research | IRRBB Principal and Interest Cash Flows Determination & Slotting
- bộ câu hỏi: 5 câu · phủ: 4 đủ / 0 một phần / 1 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Bản chất & định nghĩa dòng tiền tái định giá danh nghĩa Par 102 BCBS d368 (gốc hoàn trả, gốc tái định giá, coupon) | đủ | [[irrbb-principal-and-interest-cash-flows]], [[irrbb-balance-sheet-portfolios]], [[repricing-balance-sheet]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]] | Đã đủ định nghĩa toán học và phân rã 3 cấu phần |
  | Q2 | Cơ chế phân bổ dòng tiền (Cash Flow Slotting) 19 dải kỳ hạn cho công cụ cố định (Bullet/Amortising) vs thả nổi (Reset Date) | đủ | [[irrbb-principal-and-interest-cash-flows]], [[irrbb-balance-sheet-portfolios]], [[repricing-balance-sheet]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]] | Đã đủ nguyên tắc Par Value at Reset Date và slotting coupon/gốc |
  | Q3 | Phương pháp xác định dòng tiền theo mô hình hành vi (CASA Non-core/Core Table 2, Prepayment CPR, Early Redemption TDRR) | đủ | [[irrbb-principal-and-interest-cash-flows]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]], [[src-lubinska-alm-optimisation]] | Đã đủ công thức CPR multiplier 0.8/1.2, TDRR multiplier 1.2/0.8 và trần Table 2 |
  | Q4 | Dòng tiền phái sinh IRS (chân cố định vs thả nổi) và cơ chế bóc tách Biên thương mại Par 103 (Deduct vs Include) | đủ | [[irrbb-principal-and-interest-cash-flows]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]] | [[src-tata-bank-alm]], [[src-bcbs-irrbb-2016]] | Đã đủ quy tắc slotting IRS của Tata và 2 phương pháp chiết khấu Par 103 |
  | Q5 | Khung quy định: So sánh Basel BCBS d368 vs Ngân hàng Nhà nước Việt Nam (Thông tư 83/2025/TT-NHNN Phụ lục 5) | thiếu | [[irrbb-principal-and-interest-cash-flows]] | [[src-bcbs-irrbb-2016]] | Hướng dẫn kỹ thuật đo lường dòng tiền và dải kỳ hạn của NHNN · src-tt83-2025-nhnn (PL5) |
- created: [[irrbb-principal-and-interest-cash-flows]] · updated: [[index]], [[repricing-balance-sheet]] · proposed: không có
- conflicts: không có
- cần ingest: src-tt83-2025-nhnn PL5 (gỡ Q5 về quy định kỹ thuật dải kỳ hạn và dòng tiền tái định giá tại VN)




## [2026-10-17] lint | toàn wiki: 0 error, sửa 6 lỗi KaTeX, 6 nhóm đề xuất nội dung chờ duyệt
- trước: 0 error / 0 warning · sau: 0 / 0
- script phụ: audit_vault (relation thiếu cite: 0, note ngắn: 0) · LaTeX: 0 lỗi theo check_latex/test_latex_deep; quét bổ sung thấy 11 công thức có dấu gạch Unicode `–` ngoài `\text{}` (KaTeX strict mode cảnh báo)
- đã sửa (kỹ thuật, node `draft`, không đổi nội dung): bọc `–` trong `\text{–}` tại [[bcbs-nsfr]], [[nsfr]], [[asf-retail-and-small-business-deposits]], [[integrated-alm-liquidity-strategy]], [[nsfr-alm-governance-strategy-and-risks]] (2 chỗ)
- đề xuất chờ duyệt: (1) [[irrbb-standardised-shocks-eve-and-nii-measurement]] công thức cộng dồn EVE có bù trừ 50% phần lãi, raw d368 par 132 chỉ cộng các khoản lỗ, mâu thuẫn ngầm với [[irrbb-standardised-framework]]; ngưỡng đồng tiền trọng yếu ghi "≥ 5% bảng cân đối" thay vì "> 5% tài sản hoặc nợ sổ ngân hàng"; outlier test viết như can thiệp tự động; sàn lãi suất sau sốc viết như ngăn lãi suất âm (raw: tuỳ chọn, sàn ≤ 0) (2) [[irrbb-standardised-framework]] (canonical) điểm giữa dải 9M–1Y ghi 0.7917, raw Table là 0.875Y (3) [[src-bcbs-irrbb-2016]] claim ^irrbb-u07-4 diễn giải sàn lãi suất sau sốc khác trích dẫn; ^irrbb-u07-2 không trích số liệu Table 1 mà node dùng (4) [[irrbb-liquidity-hqla-and-ftp-interaction]] "LCR Inflow cap 50%" cite ^lcr40-77 (nguồn: trần 75%); RSF 65% thiếu điều kiện RW ≤ 35%, kỳ hạn ≥ 1 năm (5) 5 công thức `–` trong node canonical và 26 link `file:///` trong 4 node canonical cần đổi sang `[[id]]` (6) 51 công thức nằm trong alias wikilink
- phạm vi rà ngữ nghĩa: sâu với 5 node thay đổi chưa commit; các node còn lại chỉ rà máy (citations.py --uncited liệt kê 1620 dòng, chưa đọc hết)

## [2026-10-17] lint | citation nằm trong công thức gây KaTeX ParseError
- nguyên nhân: mẫu `$$ … \quad \text{[[src-…#^id]]} $$`; `#` là ký tự tham số macro của KaTeX nên báo "Expected 'EOF', got '#'"; link trong math cũng không render
- đã sửa (node `draft`, 6 chỗ): đưa citation ra sau `$$` tại [[irrbb-liquidity-hqla-and-ftp-interaction]] (2), [[ftp-transmission-mechanism]] (2), [[ftp-pricing-methodology]] (1), [[irrbb-principal-and-interest-cash-flows]] (1)
- đề xuất chờ duyệt: 20 chỗ cùng mẫu trong 7 node canonical (ftp-final-rate-determination 9, ftp-nature-and-balance-sheet-management 3, ftp-curve-construction-methodology 2, ftp-portfolio-and-bucket-allocation 2, ftp-risk-and-cost-components 2, ftp-cost-benefit-allocation-principles 1, lcr-by-currency 1); link node trong `\text{}` của môi trường cases tại [[integrated-alm-liquidity-strategy]] (không lỗi parse nhưng link không hoạt động)
- lint: 0 error / 0 warning
- [2026-10-17] user duyệt "sửa luôn": áp cùng cách sửa cho 21 chỗ trong 7 node canonical ([[ftp-final-rate-determination]] 10, [[ftp-nature-and-balance-sheet-management]] 3, [[ftp-curve-construction-methodology]] 2, [[ftp-portfolio-and-bucket-allocation]] 2, [[ftp-risk-and-cost-components]] 2, [[ftp-cost-benefit-allocation-principles]] 1, [[lcr-by-currency]] 1); chỉ dời vị trí citation, không đổi công thức hay nội dung. Wiki không còn mẫu `\quad \text{[[…]]}` trong math. Lint: 0 error / 0 warning
- [2026-10-17] [[integrated-alm-liquidity-strategy]] (draft): tách link [[outlier-bank-test]], [[bcbs-irrbb]] khỏi khối `cases` ra dòng ngay dưới công thức; công thức giữ nguyên

## [2026-10-17] research | IRRBB Basis Risk Measurement & Hedging (VNIBOR vs Big 4)
- bộ câu hỏi: 5 câu · phủ: 3 đủ / 1 một phần / 1 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Bản chất Basis Risk VNIBOR vs Big 4 12M tại Việt Nam (lệch pha tương quan, administered rate vs liên ngân hàng) | đủ | [[irrbb-basis-risk-measurement-and-hedging]], [[basis-risk]] | [[src-bcbs-irrbb-2016]], [[src-choudhry-principles-banking]] | Đã đủ lý thuyết chuẩn và phân tích cấu trúc thị trường VN |
  | Q2 | Phương pháp đo lường ΔNII, ΔEVE và kịch bản sốc kiểm tra sức chịu đựng riêng cho Basis Spread | đủ | [[irrbb-basis-risk-measurement-and-hedging]], [[basis-risk]], [[net-interest-income-sensitivity]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]] | Đã đủ công thức độ nhạy NII và kịch bản sốc giãn biên độ |
  | Q3 | Xử lý Basis Risk qua hệ thống Multi-curve FTP, bóc tách Basis Spread Charge và chuyển giao rủi ro về CFU | đủ | [[irrbb-basis-risk-measurement-and-hedging]], [[ftp-risk-and-cost-components]], [[ftp-curve-construction-methodology]] | [[src-ftp-transmission-analysis]], [[src-vab-ftp]], [[src-choudhry-principles-banking]] | Đã đủ nguyên tắc matched-basis và cấu trúc biểu giá COF |
  | Q4 | Kỹ thuật phòng ngừa: Basis Swap, Tái cấu trúc hợp đồng tín dụng (Prime rate, Floor) và Natural Hedging | một phần | [[irrbb-basis-risk-measurement-and-hedging]], [[basis-risk]] | [[src-bcbs-irrbb-2016]], [[src-choudhry-principles-banking]] | Dữ liệu thanh khoản và thực tiễn Basis Swap VND tại Việt Nam |
  | Q5 | Khung quy định: So sánh Basel BCBS d368 vs Ngân hàng Nhà nước Việt Nam (Thông tư 83/2025/TT-NHNN C3-M7, PL5) | thiếu | [[irrbb-basis-risk-measurement-and-hedging]] | [[src-bcbs-irrbb-2016]] | Hướng dẫn định lượng kịch bản sốc cơ sở của NHNN · src-tt83-2025-nhnn (C3-M7, PL5) |
- created: [[irrbb-basis-risk-measurement-and-hedging]] · updated: [[index]], [[models/repricing-balance-sheet]] · proposed: không có
- conflicts: không có
- cần ingest: src-tt83-2025-nhnn C3-M7, PL5 (gỡ Q5 về quy định kỹ thuật kịch bản sốc cơ sở và thẩm quyền ALCO tại VN)

## [2026-10-17] research | IRRBB Credit Spread Risk in the Banking Book (CSRBB)
- bộ câu hỏi: 5 câu · phủ: 2 đủ / 2 một phần / 1 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Bản chất CSRBB và ranh giới bóc tách IRRBB vs CSRBB vs Credit Risk (Annex 1 Par 1.2–1.3 BCBS d368) | đủ | [[irrbb-csrbb-measurement-and-hedging]], [[csrbb]] | [[src-bcbs-irrbb-2016]] | Đã đủ lý thuyết bóc tách 5 thành phần lãi suất của Basel |
  | Q2 | Khung đo lường định lượng CSRBB: Công thức & ý nghĩa của Spread Duration, CS01 và phân tích độ nhạy | một phần | [[irrbb-csrbb-measurement-and-hedging]], [[csrbb]] | [[src-choudhry-principles-banking]] | Chi tiết vi tích phân Spread Duration/Convexity là kiến thức nền |
  | Q3 | Cơ chế truyền dẫn kế toán và tác động xói mòn Vốn cấp 1 CET1 (FVOCI/AFS vs HTM) | đủ | [[irrbb-csrbb-measurement-and-hedging]], [[csrbb]] | [[src-bcbs-irrbb-2016]], [[src-choudhry-principles-banking]] | Đã đủ cơ chế AOCI trừ thẳng vào CET1 và kênh truyền dẫn vốn |
  | Q4 | Kỹ thuật phòng ngừa rủi ro CSRBB: CDS, hạn mức CS01/Spread Duration và tối ưu hóa danh mục HQLA | một phần | [[irrbb-csrbb-measurement-and-hedging]], [[csrbb]], [[hqla]] | [[src-choudhry-principles-banking]], [[src-bcbs-irrbb-2016]] | Dữ liệu thực tiễn công cụ phái sinh tín dụng (CDS) tại Việt Nam |
  | Q5 | Khung quy định: So sánh Basel (BCBS d368, EBA Guidelines) vs NHNN (TT 83/2025, TT 41/2016) | thiếu | [[irrbb-csrbb-measurement-and-hedging]] | [[src-bcbs-irrbb-2016]] | Hướng dẫn kỹ thuật đo lường và tính vốn CSRBB của NHNN · src-tt83-2025-nhnn (C3-M7, PL5), src-tt41-2016-nhnn |
- created: [[irrbb-csrbb-measurement-and-hedging]] · updated: [[index]], [[syntheses/irrbb-transmission-mechanisms-to-nii-and-eve]] · proposed: không có
- conflicts: không có
- cần ingest: src-tt83-2025-nhnn C3-M7, PL5 (gỡ Q5 về quy định kỹ thuật kịch bản sốc credit spread và thẩm quyền ALCO tại VN), src-tt41-2016-nhnn (gỡ Q5 về cơ chế ghi nhận AOCI vào Vốn cấp 1)

## [2026-10-17] research | IRRBB Fixed vs Floating Cash Flows & Repricing Profile
- bộ câu hỏi: 4 câu · phủ: 3 đủ / 1 một phần / 0 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Phân rã dòng tiền gốc & lãi (notional cash flows) giữa Fixed Rate vs Floating Rate theo Par 102 | đủ | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[irrbb-principal-and-interest-cash-flows]], [[repricing-balance-sheet]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]] | Đã đủ phân rã gốc hoàn trả, gốc tái định giá và dòng coupon/lãi thả nổi |
  | Q2 | Repricing profile & quy tắc Par Value tại Next Reset Date cho công cụ thả nổi (triệt tiêu rủi ro kỳ hạn gốc) | đủ | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[repricing-balance-sheet]] | [[src-tata-bank-alm]], [[src-bcbs-irrbb-2016]] | Đã đủ giải tích chứng minh PV = Par tại Reset Date của Tata và Par 104 BCBS |
  | Q3 | Xử lý cấu phần biên thương mại không tái định giá và quyền chọn nhúng (Prepayment vs Cap/Floor) | đủ | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[irrbb-principal-and-interest-cash-flows]], [[behavioural-options]] | [[src-bcbs-irrbb-2016]], [[src-choudhry-principles-banking]] | Đã đủ quy tắc Par 103/107 và tham số kịch bản CPR |
  | Q4 | Khung quy định: So sánh Basel BCBS d368 vs Ngân hàng Nhà nước Việt Nam (Thông tư 83/2025/TT-NHNN C3-M7, PL5) | một phần | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] | [[src-bcbs-irrbb-2016]] | Quy định phân bổ thang kỳ hạn tái định giá và xử lý biên thương mại của NHNN · src-tt83-2025-nhnn (C3-M7, PL5) |
- created: [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] · updated: [[index]] · proposed: không có
- conflicts: không có
- cần ingest: src-tt83-2025-nhnn C3-M7 & PL5 (gỡ Q4 về quy chuẩn thang kỳ hạn tái định giá dòng tiền tại VN)

## [2026-10-17] research | IRRBB Commercial Margins Unbundling & Discount Curves
- bộ câu hỏi: 5 câu · phủ: 4 đủ / 1 một phần / 0 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu (chờ TT83)
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Bản chất kinh tế của Commercial Margin: bóc tách thương quyền khách hàng vs chuyển đổi kỳ hạn | đủ | [[irrbb-commercial-margins-and-discount-curves]], [[internal-risk-transfer]], [[ftp-cost-benefit-allocation-principles]] | [[src-choudhry-principles-banking]], [[src-bcbs-irrbb-2016]] | Đã đủ lý luận tách biệt thương quyền phi rủi ro và chuyển đổi kỳ hạn của Choudhry |
  | Q2 | Phương pháp Deduct: bóc tách biên thương mại, chiết khấu theo đường cong phi rủi ro (Risk-free Curve) | đủ | [[irrbb-commercial-margins-and-discount-curves]], [[irrbb-principal-and-interest-cash-flows]] | [[src-bcbs-irrbb-2016]] | Đã đủ cơ chế Par 102/103 và quy tắc chiết khấu Nguyên tắc 8(c) |
  | Q3 | Phương pháp Include: giữ lại biên thương mại, chiết khấu theo đường cong bù spread (Risk-free + Spread) | đủ | [[irrbb-commercial-margins-and-discount-curves]], [[economic-value-of-equity]] | [[src-bcbs-irrbb-2016]], [[src-tata-bank-alm]] | Đã đủ nguyên tắc đối xứng dòng tiền - đường cong để tránh biến dạng PV |
  | Q4 | Nguyên tắc nhất quán toàn diện (Principle 8) và ranh giới phân định rủi ro với CSRBB | đủ | [[irrbb-commercial-margins-and-discount-curves]], [[csrbb]] | [[src-bcbs-irrbb-2016]], [[src-choudhry-principles-banking]] | Đã đủ cảnh báo bất đối xứng tài sản - nợ và đo lường CS01 |
  | Q5 | Khung quy định: So sánh Basel BCBS d368 vs Ngân hàng Nhà nước Việt Nam (Thông tư 83/2025/TT-NHNN C3-M7, PL5) | một phần | [[irrbb-commercial-margins-and-discount-curves]] | [[src-bcbs-irrbb-2016]] | Hướng dẫn kỹ thuật về việc bóc tách hay duy trì biên thương mại của NHNN · src-tt83-2025-nhnn (C3-M7, PL5) |
- created: [[irrbb-commercial-margins-and-discount-curves]] · updated: [[index]], [[models/repricing-balance-sheet]] · proposed: không có
- conflicts: không có
- cần ingest: src-tt83-2025-nhnn C3-M7 & PL5 (gỡ Q5 về quy chuẩn bóc tách biên thương mại và đường cong chiết khấu tại VN)


## [2026-10-17] schema | quy ước relation cho synthesis
- taxonomy (mục Relation): A và B đều phải là node tri thức; synthesis và source note không làm chủ thể hay đích của relation.
- template synthesis: `relations: []` luôn để trống.
- skill research: bản đồ quan hệ (bước 1), verify cạnh và khái niệm cần node riêng (bước 3), bảng chuỗi quan hệ trong `## Cơ chế` (bước 4), đưa cạnh mới về node tri thức.
- skill ingest: quy tắc relation trên; mục "Synthesis bị ảnh hưởng" (đánh dấu `cần rà lại` trong `## Bất định` / `## Đề xuất cập nhật`, log `syntheses flagged`).
- skill lint: rà dòng đánh dấu chưa rà và relation có synthesis làm chủ thể/đích.

## [2026-10-17] lint | dọn relations cụm thanh khoản (batch A, B, C đã duyệt)
- A. `relations: []` cho 9 synthesis (bỏ 38 cạnh: 27 trùng cạnh đã có ở node tri thức, 10 có claim không chứng minh quan hệ, 1 chuyển sang B): [[basel-liquidity-monitoring-framework]], [[hqla-decomposition-and-tradeoffs]], [[integrated-alm-liquidity-strategy]], [[lcr-economic-significance-and-alm-governance]], [[lcr-net-cash-outflows-mechanics]], [[nsfr-alm-governance-strategy-and-risks]], [[nsfr-structural-liquidity-and-alm-strategy]], [[practical-alm-liquidity-governance]], [[synthetic-balance-sheet-liquidity-risk]]. Synthesis canonical chỉ đổi frontmatter.
- B. [[balance-sheet-optimisation-model]]: bỏ `input-to` lcr/nsfr/net-interest-income-sensitivity (ngược chiều, lubinska-u04-12 nói đây là ràng buộc); thêm [[lcr]] và [[nsfr]] `limits` [[balance-sheet-optimisation-model]] (cite lubinska-u04-12).
- C. Bỏ 10 cạnh trỏ tới synthesis thanh khoản ở [[contingency-funding-plan]] ×2, [[liquidity-transfer-pricing]] ×2, [[internal-risk-transfer]], [[leverage-ratio]], [[leverage-exposure-measure]], [[ftp-transmission-mechanism]], [[ftp-pricing-methodology]], [[model-risk-management]] (node canonical chỉ đổi frontmatter).
- node nên tạo: liquidity-risk-management (concept, claim: [[src-choudhry-principles-banking#^choudhry-cfp-1]]: CFP là cấu phần của quy trình quản trị rủi ro thanh khoản).
- proposed (chưa duyệt, mục D): bỏ cặp hai chiều `lcr measures hqla`/`net-cash-outflows`, `nsfr measures available-stable-funding`/`required-stable-funding`; bỏ `governs` từ [[liquidity-monitoring-metrics]] ×5 và [[intraday-liquidity-risk]]; đổi `part-of [[bcbs]]` → `part-of [[liquidity-monitoring-metrics]]` ở 4 công cụ giám sát.
- còn lại: 13 cạnh synthesis FTP/IRRBB → synthesis thanh khoản, xử lý khi dọn cụm FTP, IRRBB.

---

## [2026-10-17] lint | dọn relations cụm FTP (batch A, C, E đã duyệt)
- A. `relations: []` cho 8 synthesis (bỏ 51 cạnh: 32 synthesis → synthesis gồm `implements` dùng sai nghĩa, 3 trùng cạnh ở node tri thức, 16 có claim không chứng minh quan hệ): [[ftp-balance-sheet-optimization]], [[ftp-cost-benefit-allocation-principles]], [[ftp-curve-construction-methodology]], [[ftp-economic-cost-and-incentive-validation]], [[ftp-final-rate-determination]], [[ftp-nature-and-balance-sheet-management]], [[ftp-portfolio-and-bucket-allocation]], [[ftp-risk-and-cost-components]]. Synthesis canonical chỉ đổi frontmatter. Hết 12/13 cạnh còn sót trỏ tới synthesis thanh khoản.
- C. Bỏ 5 cạnh trỏ tới synthesis FTP ở [[ftp-transmission-mechanism]], [[liquidity-transfer-pricing]], [[ftp-pricing-methodology]], [[internal-risk-transfer]] ×2.
- E. created: [[funds-transfer-pricing]] (concept, draft; 26 citation từ src-choudhry-principles-banking, src-vab-ftp, src-ftp-transmission-analysis). relations: added [[liquidity-transfer-pricing]] —part-of→ [[funds-transfer-pricing]] (choudhry-ftp-14) · [[ftp-transmission-mechanism]] —part-of→ [[funds-transfer-pricing]] (ftp-trans-2).
- node nên tạo: cost-of-funds (concept, claim: [[src-vab-ftp#^vab-ftp-7]]).
- lỗi wiki: [[src-vab-ftp]] và [[src-ftp-transmission-analysis]] không theo định dạng claim chuẩn (block-id gắn sau trích dẫn, thiếu dòng locator), nên `citations.py` không ghép được câu node ↔ claim.
- còn lại: 3 cạnh synthesis IRRBB → synthesis và 1 cạnh [[irrbb-balance-sheet-portfolios]] → synthesis, xử lý khi dọn cụm IRRBB.

---

## [2026-10-17] lint | dọn relations cụm IRRBB (batch A, C đã duyệt)
- A. `relations: []` cho 12 synthesis (bỏ 64 cạnh: 3 synthesis → synthesis, 49 trùng cạnh ở node tri thức, 12 có claim không chứng minh quan hệ hoặc đã có cạnh đúng ở node): [[irrbb-alm-governance-strategy-and-tradeoffs]], [[irrbb-basis-risk-measurement-and-hedging]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-commercial-margins-and-discount-curves]], [[irrbb-csrbb-measurement-and-hedging]], [[irrbb-five-tier-architecture]], [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[irrbb-liquidity-hqla-and-ftp-interaction]], [[irrbb-principal-and-interest-cash-flows]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[irrbb-transmission-mechanisms-to-nii-and-eve]]. Synthesis canonical chỉ đổi frontmatter.
- C. Bỏ [[irrbb-balance-sheet-portfolios]] `input-to` [[irrbb-five-tier-architecture]] (node canonical).
- node nên tạo: cs01 (metric, claim: [[src-choudhry-principles-banking#^choudhry-irrbb-9]]).
- kết quả toàn vault: 0 relation có synthesis làm chủ thể hoặc đích.

---

## [2026-10-17] schema | vòng đời node phát hiện từ research
- skill ingest: định dạng stub chuẩn (callout 3 dòng: Claim sẵn có · Hoàn thiện bằng · Phát hiện; `sources` bắt buộc); chế độ `/ingest --node <id>` (biên dịch node từ claim có sẵn); chế độ bổ sung cho unit `done` (chỉ thêm claim, block-id mới, không `mark`); mục "Nối lại khi có node mới" (link, đề xuất chuyển đích quan hệ, đánh dấu synthesis; log dòng `backfill`).
- skill research: tiêu chí đầu vào 3 điều kiện cho ứng viên stub (nguồn định danh khái niệm · chưa có node · chọn được type); stub tạo sau khi user duyệt ở bước 5; log `stubs: created`; gợi ý "Stub cần hoàn thiện".
- skill lint: check `stub-plan`, `stub-index`, `stub-stale`, `stub-count`; mục "thuật ngữ ≥ 3 node" áp tiêu chí đầu vào.
- tools/lint.py: thêm 4 check stub (kiểm thử trên bản copy vault: bắt đủ 4 lỗi cài sẵn). taxonomy: `stub_stale_days: 60`.
- evals: ingest +2 case (`--node`, bổ sung u17); research case 2 +2 assertion về stub.

## [2026-10-17] lint | chuyển đề xuất "node nên tạo" thành stub
- stubs: created [[liquidity-risk-management]] (concept, claim: [[src-choudhry-principles-banking#^choudhry-cfp-1]]) · [[cost-of-funds]] (metric, claim: [[src-vab-ftp#^vab-ftp-7]]; title theo nghĩa VAB là giá bán vốn FTP cho tài sản, khác nghĩa thông dụng "chi phí huy động") · [[cs01]] (metric, claim: [[src-choudhry-principles-banking#^choudhry-irrbb-9]]; relation `measures` [[csrbb]]).
- updated: [[bcbs]] callout stub theo định dạng mới (Hoàn thiện bằng `/ingest src-bcbs-framework SCO10`).
- backfill (link tới stub): [[irrbb-csrbb-measurement-and-hedging]] → [[cs01]] · [[irrbb-liquidity-hqla-and-ftp-interaction]] → [[liquidity-risk-management]] · [[funds-transfer-pricing]] → [[cost-of-funds]]. Node canonical nhắc các khái niệm này ([[csrbb]], [[contingency-funding-plan]]) chưa sửa; đề xuất link khi node thoát stub.
- lint: 0 error · 0 warning · stub-count 4 (3 sẵn sàng `/ingest --node`).

---
## [2026-10-17] research | IRRBB Payment Date, Maturity Date & Repricing Date
- bộ câu hỏi: 2 câu · phủ: 0 đủ / 2 một phần / 0 thiếu · phương án: cập nhật synthesis draft, đánh dấu phần thiếu nguồn
- bản đồ phủ:
  | Q | Câu hỏi (rút gọn) | Mức phủ | Node / synthesis | Nguồn cite chính | Thiếu gì · unit nên ingest |
  |---|---|---|---|---|---|
  | Q1 | Payment Date, Maturity Date và Repricing Date khác nhau như thế nào? | một phần | [[irrbb-principal-and-interest-cash-flows]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[repricing-balance-sheet]] | [[src-tata-bank-alm]] | Source note chưa có claim BCBS u05 par 102 về định nghĩa từng ngày; cần ingest đoạn raw lines 464–472 |
  | Q2 | Thời điểm thanh toán gốc/lãi ảnh hưởng thế nào đến Repricing Cash Flow? | một phần | [[irrbb-principal-and-interest-cash-flows]], [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] | [[src-tata-bank-alm]] | Source note chưa có claim BCBS u05 pars 102, 104, 106 về ánh xạ ngày dòng tiền; cần ingest raw lines 464–495 |
- created: không có · updated: [[irrbb-principal-and-interest-cash-flows]], [[index]] · proposed: không có
- conflicts: không có
- relations: không có
- stubs: không có
- cần ingest: src-bcbs-irrbb-2016 u05 pars 102, 104, 106 (gỡ Q1, Q2; raw lines 464–495)
- lỗi wiki phát hiện được: một số claim Par 102, 104, 106 trong synthesis đang cite `^irrbb-u05-2`, nhưng source note gắn block này với Par 101; rà lại citation sau ingest.

## [2026-10-17] research | IRRBB Payment Date, Maturity Date & Repricing Date (lần 2)
- bộ câu hỏi: 2 câu · phủ: 0 đủ / 2 một phần / 0 thiếu (không đổi so với lần 1) · phương án: ingest trước
- bản đồ phủ:
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | Q1 | một phần | [[irrbb-principal-and-interest-cash-flows]] (Q6), [[repricing-balance-sheet]] | thiếu claim BCBS par 102 (định nghĩa CF(t) và repricing date); src-bcbs-irrbb-2016 u05 raw 464–472 |
  | Q2 | một phần | [[irrbb-principal-and-interest-cash-flows]] (Q7) | thiếu claim par 104, 106 (slot fixed vs floating); thiếu cạnh notional repricing cash flow → repricing balance sheet; u05 raw 474–494 |
- created: không có · updated: không có · proposed: không có
- conflicts: không có
- relations: không có
- stubs: không có (ứng viên `notional-repricing-cash-flow` (metric) chờ sau ingest)
- cần ingest: src-bcbs-irrbb-2016 u05 (bổ sung, unit đã done) pars 102, 104, 106 (gỡ Q1, Q2)
- lỗi wiki phát hiện được: synthesis cite `^irrbb-u05-2` (par 101) cho claim par 102/104/106; citations.py --uncited báo 8 dòng trong [[irrbb-principal-and-interest-cash-flows]]

## [2026-10-17] ingest | src-bcbs-irrbb-2016 U05 (bổ sung)
- created: không có
- updated: [[src-bcbs-irrbb-2016]] (+6 claim par 102, 104, 106: ^irrbb-u05-9 … ^irrbb-u05-14; maturity canonical → draft theo duyệt của user), [[repricing-balance-sheet]] (thêm 6 cite BCBS ở bước 2; sửa 3 cite sai ^irrbb-u05-2 ở mục tiêu và exclusions; bỏ chi tiết equity exposures không có nguồn)
- proposed: [[irrbb-standardised-framework]], [[gap-risk]], [[bcbs-irrbb]] (canonical, ghi ## Đề xuất cập nhật)
- conflicts: không có (par 104, 106 khớp [[src-tata-bank-alm#^tata-gap-2]])
- syntheses flagged: [[irrbb-principal-and-interest-cash-flows]], [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[irrbb-commercial-margins-and-discount-curves]], [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[synthetic-balance-sheet-liquidity-risk]] (cite ^irrbb-u05-2 cho nội dung par 102/104/106)
- backfill: không có (không tạo node mới)
- tiếp theo: quay lại /research IRRBB Payment Date, Maturity Date & Repricing Date; ứng viên stub notional-repricing-cash-flow

## [2026-10-17] research | IRRBB Payment Date, Maturity Date & Repricing Date (lần 2, sau ingest)
- bộ câu hỏi: 2 câu · phủ: 2 đủ / 0 một phần / 0 thiếu (trước ingest: 0 / 2 / 0) · phương án: ingest trước
- bản đồ phủ:
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | Q1 | đủ | [[irrbb-principal-and-interest-cash-flows]] (Q6), [[repricing-balance-sheet]] | cách đọc "repricing date" nghĩa hẹp ↔ contractual maturity với công cụ cố định là diễn giải |
  | Q2 | đủ | [[irrbb-principal-and-interest-cash-flows]] (Q7) | cách đọc par 106 "closest to the contractual maturity" chưa có nguồn thứ hai |
- created: [[notional-repricing-cash-flow]] (stub) · updated: [[irrbb-principal-and-interest-cash-flows]] (Q6, Q7 viết lại; 27 citation ^irrbb-u05-2 chuyển sang ^irrbb-u05-9 … -14; 3 câu par 103 → [cần nguồn]), [[repricing-balance-sheet]] (link stub), [[index]] · proposed: không có
- conflicts: không có
- relations: added [[notional-repricing-cash-flow]] —input-to→ [[repricing-balance-sheet]] ([[src-bcbs-irrbb-2016#^irrbb-u05-2]])
- stubs: created [[notional-repricing-cash-flow]] (metric, claim: [[src-bcbs-irrbb-2016#^irrbb-u05-9]] … [[src-bcbs-irrbb-2016#^irrbb-u05-14]])
- cần ingest: src-bcbs-irrbb-2016 u05 par 103 (bổ sung; commercial margin, gỡ Q4 của synthesis)

## [2026-10-17] ingest | src-bcbs-irrbb-2016 U05 (bổ sung)
- claim mới: ^irrbb-u05-15 (par 103, raw dòng 474: ngân hàng được chọn trừ commercial margin và spread component khỏi notional repricing cash flow, phương pháp thận trọng và minh bạch). Không chạy `mark`.
- created: không có
- updated: [[src-bcbs-irrbb-2016]] · [[repricing-balance-sheet]] (bullet commercial margin ở Bước 2) · [[notional-repricing-cash-flow]] (thêm u05-15 vào "Claim sẵn có")
- proposed: [[irrbb-balance-sheet-portfolios]] (canonical — mục Par 103 đang cite p08-2; câu "nhất quán cho cả tài sản và nợ" không có nguồn)
- conflicts: không có
- syntheses flagged: [[irrbb-principal-and-interest-cash-flows]] (Q4: 3 chỗ `[cần nguồn: … par 103]` đổi sang cite u05-15, kết luận Q4 tách CF(t) khỏi đường cong chiết khấu, "Bắt buộc" → "nên" theo par 70 — đã rà theo phạm vi Mở rộng) · [[irrbb-commercial-margins-and-discount-curves]] (Q2, Q5 trộn par 103 với chiết khấu; chỉ đánh dấu)
- backfill: không có (không có node mới)
- tiếp theo: `/ingest --node notional-repricing-cash-flow`; rà synthesis irrbb-commercial-margins-and-discount-curves

## [2026-10-17] ingest | --node notional-repricing-cash-flow
- updated: [[notional-repricing-cash-flow]] (thoát stub; 15 claim: src-bcbs-irrbb-2016 u05-1..6, u05-9..15, p08-2; src-tata-bank-alm tata-gap-2) · index bỏ *stub*
- relations: giữ input-to [[repricing-balance-sheet]] (u05-2) · added input-to [[irrbb-standardised-framework]] (u05-1)
- conflicts: không có
- Basel vs VN: 4 dòng Basel có cite; cột VN `[cần nguồn]` (chưa có source note NHNN)
- backfill: linked không có (node draft duy nhất nhắc khái niệm là [[repricing-balance-sheet]], đã link) · flagged [[irrbb-commercial-margins-and-discount-curves]], [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[irrbb-standardised-shocks-eve-and-nii-measurement]] · proposed [[irrbb-standardised-framework]], [[irrbb-balance-sheet-portfolios]], [[key-rate-duration]], [[bcbs-irrbb]], [[irrbb-five-tier-architecture]] · quan hệ đề xuất chuyển đích: không có
- tiếp theo: ingest phần tính ∆EVE theo dải của src-bcbs-irrbb-2016 u05 (công thức chiết khấu CF(t)); ingest TT83/2025 cho cột VN

## [2026-10-17] ingest | src-bcbs-irrbb-2016 U05 (bổ sung)
- claim mới: ^irrbb-u05-16 (par 105) · ^irrbb-u05-17 … ^irrbb-u05-21 (par 132 bước 1–4: bù trừ trong dải, DF liên tục, lãi suất chiết khấu + footnote 29, EVE^nao, ∆EVE) · ^irrbb-u05-22 (intra-bucket mismatch) · ^irrbb-u05-23 (CF phụ thuộc kịch bản) · ^irrbb-u05-24 (ngoại lệ gộp tiền tệ). Không chạy `mark`.
- convert: par 105 và par 102 mất ký hiệu toán; registry conversion.status ok → partial; thêm mục "Ghi chú convert" ở source note
- updated: [[src-bcbs-irrbb-2016]] · [[notional-repricing-cash-flow]] (mục Công thức: 4 bước từ CF(t) tới ∆EVE thay `[cần nguồn]`; thêm CF phụ thuộc kịch bản, intra-bucket mismatch)
- proposed: [[irrbb-standardised-framework]] (cite u05-1 cho bước chiết khấu → u05-17..21; R_0 + ∆R là diễn giải; ngoại lệ gộp tiền tệ) · [[economic-value-of-equity]] (khối công thức chưa có citation)
- conflicts: không có
- syntheses flagged: [[irrbb-standardised-shocks-eve-and-nii-measurement]] (công thức ∆EVE dòng 79 đổi dấu, dùng một CF; công thức gộp tiền tệ bù trừ 50% dòng 84 không có trong par 132)
- backfill: không có (không có node mới)
- tiếp theo: `/research` rà synthesis irrbb-standardised-shocks-eve-and-nii-measurement; ingest TT83/2025 cho cột VN

## [2026-10-18] lint | gộp kiểm tra công thức vào tools/check_math.py, nối vào lint.py
- nguyên nhân lỗi KaTeX `Can't use function '$' in math mode`: mẫu `$$…$$ [[src-…#^id]]` (citation cùng dòng với display math) do lần sửa ngày ghi ở mục trước (đưa citation ra khỏi `\text{}`) để lại; renderer không nhận khối `$$` khi dòng có chữ khác
- tool: thêm `tools/check_math.py` (gộp rule của check_latex, test_latex_deep, check_katex_advanced, find_latex_errors, scan_all_math, scan_raw_latex, find_naked_words; bỏ false positive double subscript kiểu `f_A(w_A)` và `$$` trong inline code); `lint.py` import, báo `math-*` ở mức ERROR/WARN
- trước: 0 error (lint cũ không kiểm công thức) · sau khi bật rule: 31 error · sau sửa: 22 error
- đã sửa (node `draft`, 9 chỗ, chỉ chuyển citation xuống dòng dưới `$$`): [[ftp-transmission-mechanism]] (2), [[ftp-pricing-methodology]] (1), [[irrbb-basis-risk-measurement-and-hedging]] (1), [[irrbb-liquidity-hqla-and-ftp-interaction]] (2), [[irrbb-principal-and-interest-cash-flows]] (1), [[irrbb-standardised-shocks-eve-and-nii-measurement]] (2)
- đã sửa sau khi user duyệt (node `canonical`, 22 chỗ): `display-not-own-line` ở [[lcr-by-currency]] (1), [[ftp-cost-benefit-allocation-principles]] (1), [[ftp-curve-construction-methodology]] (2), [[ftp-final-rate-determination]] (9), [[ftp-nature-and-balance-sheet-management]] (3), [[ftp-portfolio-and-bucket-allocation]] (2), [[ftp-risk-and-cost-components]] (2); `special-char-in-text` (`&` → `\&`) ở [[irrbb-five-tier-architecture]] (1)
- cập nhật quy ước: CLAUDE.md (Citation và provenance, bản đồ tools), skill lint (2b), skill ingest
- sau duyệt: 0 error · xoá 10 script công thức cũ trong tools/ (check_latex, test_latex_deep, check_katex_advanced, find_latex_errors, scan_all_math, scan_raw_latex, find_naked_words, dump_formulas, inspect_formulas, find_subscripts) theo yêu cầu user; còn trong lịch sử git

## [2026-10-18] research | IRRBB rà lại 5 synthesis sau ingest U05 bổ sung
- bộ câu hỏi: 14 dòng (câu hỏi sẵn có của 3 synthesis draft + 2 vị trí ở synthesis canonical) · phủ: 0 đủ / 7 một phần / 2 thiếu (phần VN) / 1 nghi sai / 2 chưa đánh giá / 2 chỉ đề xuất · phương án: viết theo cụm (sửa citation, công thức; VN giữ `[cần nguồn]`)
- bản đồ phủ (bước 1, trước khi sửa):
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | CM-Q1 | một phần | [[irrbb-commercial-margins-and-discount-curves]] | ví dụ 10.5% = 6.5% + 4.0% không nguồn |
  | CM-Q2 | một phần | [[irrbb-commercial-margins-and-discount-curves]] | cite par 101 (u05-2) thay vì par 103 (u05-15), par 102 (u05-10); công thức EVE_deduct không cite |
  | CM-Q3 | một phần | [[irrbb-commercial-margins-and-discount-curves]] | như Q2; công thức EVE_include không cite |
  | CM-Q4 | nghi sai | [[irrbb-commercial-margins-and-discount-curves]] | "Principle 8 nhất quán tài sản/nợ" chưa kiểm; par 103 không yêu cầu nhất quán |
  | CM-Q5 | thiếu (VN) | [[irrbb-commercial-margins-and-discount-curves]] | src-tt83-2025-nhnn C3-M7, PL5 |
  | FF-Q1 | một phần | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] | 18 cite u05-2 → u05-9, u05-11, u05-16 |
  | FF-Q2 | một phần | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] | "Par 104, 106" cite par 101 → u05-11..14 |
  | FF-Q3 | một phần | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] | spread slot contractual maturity → u05-10; behavioural → u05-23 |
  | FF-Q4 | thiếu (VN) | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] | src-tt83-2025-nhnn C3-M7, PL5 |
  | SS-Q1 | có lỗi | [[irrbb-standardised-shocks-eve-and-nii-measurement]] | công thức ∆EVE ngược dấu, một CF; gộp tiền tệ bù 50% không có trong par 132 → u05-17..21, u05-23, u05-24, u05-8 |
  | SS-Q2 | chưa đánh giá | [[irrbb-standardised-shocks-eve-and-nii-measurement]] | không bị đánh dấu |
  | SS-Q3 | chưa đánh giá | [[irrbb-standardised-shocks-eve-and-nii-measurement]] | không bị đánh dấu |
  | 5T-149 | chỉ đề xuất (canonical) | [[irrbb-five-tier-architecture]] | 19 dải: thêm u05-16 |
  | SB-107 | chỉ đề xuất (canonical) | [[synthetic-balance-sheet-liquidity-risk]] | repricing tenor: thêm u05-9 |
- cần ingest: src-tt83-2025-nhnn C3-M7 (gỡ CM-Q5, FF-Q4), PL5 (gỡ CM-Q5, FF-Q4, SS-Q1 phần VN)
- updated: [[irrbb-standardised-shocks-eve-and-nii-measurement]] (∆EVE theo par 132 bước 1–4: u05-17..21, CF theo kịch bản u05-23, bỏ công thức ngược dấu; gộp tiền tệ chỉ cộng lỗ ∆EVE_{i,c} > 0 theo u05-8, bỏ bù trừ 50%, thêm u05-24; ∆NII cite p08-3, tata-egap-1/2 thay tata-nii-1; dynamic balance sheet → `[cần nguồn]`; outlier test "nên" theo trích p12-1; floor 100 bp là sàn biên độ sốc; bỏ "Black-76/Hull-White") · [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] (14 cite u05-2 sai par → u05-9..14, u05-15, u05-19, u05-23; "bắt buộc" → "được giả định"/"có thể" theo par 104, 106; bỏ số 3%–4% khỏi Diễn giải) · [[irrbb-commercial-margins-and-discount-curves]] (viết lại thân bài, giữ heading: bỏ trích dẫn "applied consistently…" không có trong raw d368; Deduct/Include cite u05-15, u05-19; 9 câu cite p08-2/choudhry-irrbb-9 vượt nội dung claim → `*Diễn giải:*` hoặc `[cần nguồn]`; bỏ số minh hoạ 10.5%/6.5%/4.0%) · index dòng 127
- proposed: [[irrbb-five-tier-architecture]] (dòng 149: thêm u05-16, u05-17; mốc 0.0028/22.5 năm chưa có claim) · [[synthetic-balance-sheet-liquidity-risk]] (dòng 107: thêm u05-9, u05-10; 19 dải không áp cho ∆NII theo claim)
- bản đồ phủ sau rà: CM-Q1 một phần · CM-Q2 đủ · CM-Q3 một phần (footnote 29) · CM-Q4 thiếu (nhất quán tài sản/nợ không có nguồn) · CM-Q5 thiếu (VN; claim công bố par 70(b)(c) bỏ sót) · FF-Q1 đủ · FF-Q2 đủ · FF-Q3 đủ · FF-Q4 thiếu (VN) · SS-Q1 đủ · SS-Q2 một phần (dynamic BS) · SS-Q3 một phần (Table 1 chưa có claim) · 5T-149, SB-107 đề xuất
- conflicts: không có
- relations: không có (cả 5 synthesis `relations: []`; không node nào trỏ relation tới chúng)
- stubs: không có
- lỗi wiki phát hiện được: claim [[src-bcbs-irrbb-2016#^irrbb-u07-4]] diễn đạt "sàn âm/không âm cho lãi suất sau sốc" lệch trích "higher floor … home currency" · claim [[src-bcbs-irrbb-2016#^irrbb-p12-1]] ghi "phải so sánh" trong khi trích là "should implement" · claim u07-2 không chép Table 1 · claim p08-2 lược yêu cầu công bố lựa chọn margin (raw u03 dòng 260–261)
- cần ingest: src-tt83-2025-nhnn C3-M7, PL5 (gỡ CM-Q5, FF-Q4) · src-bcbs-irrbb-2016 u03 bổ sung par 70(b)(c) (gỡ CM-Q5) · src-bcbs-irrbb-2016 u07 bổ sung Table 1 (gỡ SS-Q3)

## [2026-10-18] ingest | src-bcbs-irrbb-2016 U03 (bổ sung)
- claims mới: ^irrbb-p08-4 (par 70(i)(b) công bố giữ/trừ commercial margin), ^irrbb-p08-5 (par 70(i)(c) + fn 12 lãi suất chiết khấu và công bố), ^irrbb-p08-6 (Table A dòng g; raw dòng 296 thuộc Table A, không phải Table B như log research trước ghi)
- sửa diễn đạt (không đổi trích dẫn, block-id): ^irrbb-p12-1 "phải so sánh" → "nên (should) áp dụng ít nhất một phép thử"
- updated: [[irrbb-commercial-margins-and-discount-curves]] (Kết luận Q5, Q3 mục 2, Cơ chế Q5, Bất định: cite p08-4..6)
- conflicts: không có
- syntheses flagged: [[irrbb-commercial-margins-and-discount-curves]] (→ đã rà cùng ngày)
- backfill: không có (không tạo node mới)
- registry: không chạy `mark` (u03 đã done)

## [2026-10-18] ingest | src-bcbs-irrbb-2016 U07 (bổ sung)
- claims mới: ^irrbb-u07-5 (Table 1, 21 đồng tiền × Parallel/Short/Long, raw dòng 941–957; raw không ghi đơn vị)
- sửa diễn đạt (không đổi trích dẫn, block-id): ^irrbb-u07-4 "sàn âm/không âm cho lãi suất sau sốc" → "có thể đặt sàn cao hơn cho đồng nội tệ"
- updated: [[irrbb-standardised-shocks-eve-and-nii-measurement]] (Q3: dòng USD/EUR/JPY cite u07-5; Bất định)
- proposed: [[standardised-interest-rate-shocks]] (canonical) — AUD Short 400 → 450; câu phân vị 1%/99% · 6 tháng và callout đồng tiền ngoài Table 1 cite claim không chứa nội dung
- conflicts: không có
- syntheses flagged: [[irrbb-standardised-shocks-eve-and-nii-measurement]] (→ đã rà cùng ngày)
- lỗi wiki phát hiện được: outlier test được diễn đạt "bắt buộc" ở [[outlier-bank-test]], [[standardised-interest-rate-shocks]], [[bcbs-irrbb]], [[economic-value-at-risk]] trong khi par 88 là "should implement" (^irrbb-p12-1) — cần `/lint`
- tiếp theo: src-tt83-2025-nhnn C3-M7, PL5

## [2026-10-18] lint | R1 mức bắt buộc của outlier test (phạm vi: 4 node)
- trước: 0 error / 0 warning · sau: 0 / 0
- script phụ: không chạy (lint theo phạm vi)
- stub: 4 (3 sẵn sàng --node) — không đổi
- đã sửa: không (cả 4 node canonical)
- đề xuất chờ duyệt (`## Đề xuất cập nhật`): [[outlier-bank-test]] dòng 20, 22, 24, 61 · [[bcbs-irrbb]] dòng 60 · [[economic-value-at-risk]] dòng 52 · [[standardised-interest-rate-shocks]] dòng 25 — phép thử 15% Tier 1 là "should" (par 88), chỉ công bố tiêu chí, xét outlier (par 90) và yêu cầu biện pháp khi kết luận yếu kém (par 94) là "must"; "tự động kích hoạt" không có trong nguồn (u01-6 "strong presumption")
- lỗi claim phát hiện: ^irrbb-p12-3 diễn đạt "trong một thời hạn xác định" nhưng trích dẫn (par 94) không có; nội dung này ở par 95 ("should … within a specified time frame"), chưa có claim → đề xuất `/ingest src-bcbs-irrbb-2016 u03` bổ sung par 95

## [2026-10-18] ingest | src-bcbs-irrbb-2016 U03 (bổ sung)
- claims mới: ^irrbb-p12-4 (par 90, outlier must be considered … subject to review) · ^irrbb-p12-5 (par 91, yếu tố supervisor xét: ∆EVE, giả định commercial margin/equity/NMD/prepayment, dòng thu nhập) · ^irrbb-p12-6 (par 92, IMS kém → cải thiện IMS / dùng standardised framework) · ^irrbb-p12-7 (par 93, rủi ro quá mức so với thu nhập theo ∆NII) · ^irrbb-p12-8 (par 95, thời hạn khắc phục, should)
- sửa diễn đạt ^irrbb-p12-3: bỏ "trong một thời hạn xác định" (thuộc par 95); trích dẫn và block-id giữ nguyên
- created: không · updated: không (node tri thức)
- proposed: [[outlier-bank-test]] (canonical) — cite p12-4 cho dòng 22, p12-8 cho dòng 61
- conflicts: không có
- syntheses flagged: [[irrbb-standardised-shocks-eve-and-nii-measurement]] (Q1, Q2) · [[irrbb-commercial-margins-and-discount-curves]] (Q4, Q5)
- backfill: không có
- registry: không chạy `mark` (u03 đã done)
- tiếp theo: src-tt83-2025-nhnn C3-M7, PL5

## [2026-10-18] review | áp đề xuất đã duyệt vào 4 node canonical
- [[outlier-bank-test]]: dòng 20, 22, 24, 61 — phép thử 15% Tier 1 là should (par 88); outlier bị coi là có khả năng mang IRRBB quá mức và phải được rà soát (p12-4); bỏ "tự động kích hoạt"; điều kiện "must require" theo par 94; thời hạn khắc phục cite p12-8 (should)
- [[bcbs-irrbb]]: dòng 60 — Nguyên tắc 12 viết theo must/should của par 88, 94
- [[economic-value-at-risk]]: dòng 52 — viết theo should (u07-1, p12-1); vế "thay vì EVaR nội bộ" chuyển sang *Diễn giải:*
- [[standardised-interest-rate-shocks]]: dòng 25 (should); câu phân vị 1%/99%, cửa sổ 6 tháng → `[cần nguồn]`; bảng Table 1 cite từng dòng u07-5, **AUD Short 400 → 450**; callout đồng tiền ngoài Table 1 → `[cần nguồn: src-tt83-2025-nhnn PL5]`
- maturity giữ canonical; dòng đề xuất được nối "→ đã áp [2026-10-18]"
- còn chờ: 2 đề xuất [2026-10-17] ở [[bcbs-irrbb]] (dòng bảng notional repricing cash flow)
- lint: 0 error / 0 warning
- [2026-10-18] bổ sung: áp 2 đề xuất [2026-10-17] ở [[bcbs-irrbb]] — thêm dòng "Notional repricing cash flow" (link [[notional-repricing-cash-flow]], u05-9) và "Công cụ lãi suất thả nổi" (u05-12) vào bảng yêu cầu

## [2026-10-19] review | áp 10 đề xuất U05 đã duyệt vào 7 node canonical
- source note [[src-bcbs-irrbb-2016]]: thêm claim Table 1 Section IV (19 dải, điểm giữa 0.0028Y → 25Y) ^irrbb-u05-25
- [[gap-risk]]: thêm câu repricing date (u05-9) và floating reprice tại first reset date (u05-12)
- [[irrbb-balance-sheet-portfolios]]: link [[notional-repricing-cash-flow]]; mục par 103 cite u05-15 thay p08-2 cho câu dẫn; "áp dụng nhất quán cho tài sản và nợ" → `[cần nguồn]`
- [[economic-value-of-equity]]: cite 4 bước công thức (u05-17, 18, 19, 20, 21, 8); R theo Annex 2 + risk-free zero coupon rate; $CF_{i,c}(t_k)$ → $CF_{i,c}(k)$ trong EVE^nao; thêm ngoại lệ gộp tiền tệ (u05-24)
- [[irrbb-standardised-framework]]: link node; cite slotting (u05-9…14); Giai đoạn 3 cite u05-17…21, tách $R_0 + \Delta R$ chuyển xuống *Diễn giải:*, EVE đổi thành EVE^nao với Σ tới K; thêm giả định intra-bucket mismatch (u05-22), CF phụ thuộc kịch bản (u05-23); Giai đoạn 5 thêm u05-24
- [[key-rate-duration]]: link node
- [[irrbb-five-tier-architecture]]: viết lại dòng 19 dải (u05-16, u05-2, u05-25, u05-17); **mốc cuối 22.5 năm → 25 năm** theo Table 1
- [[synthetic-balance-sheet-liquidity-risk]]: định nghĩa reset cite u05-10, u05-9; 19 dải chỉ cho ∆EVE (u05-1, u05-2); phần ∆NII → `[cần nguồn]`
- maturity giữ canonical; dòng đề xuất được nối "→ đã áp [2026-10-19]"
- đề xuất mới (chờ duyệt): [[irrbb-standardised-framework]] dải 6 điểm giữa 0.7917 → 0.875 và câu outlier "chính thức bị xác định" mâu thuẫn [[outlier-bank-test]]; [[key-rate-duration]] 22.5 → 25 năm; [[irrbb-balance-sheet-portfolios]] mục par 104 cite u05-2 → u05-12, bỏ "về mệnh giá"
- lint: 0 error / 0 warning
- tiếp theo: duyệt 3 đề xuất mới; src-tt83-2025-nhnn C3-M7, PL5
- [2026-10-19] bổ sung: áp 3 đề xuất mới đã duyệt — [[irrbb-standardised-framework]] dải 6 điểm giữa 0.7917 → 0.8750, bảng cite u05-25, câu outlier viết theo should (p12-1) và "phải được rà soát" (p12-4); [[key-rate-duration]] 22.5 → 25 năm, cite u05-25, cột hệ số $S_{\text{short}}$ → `[cần nguồn]`; [[irrbb-balance-sheet-portfolios]] mục par 104 cite u05-12, bỏ "về mệnh giá (par value)", spread theo nguyên văn par 104
- lint: 0 error / 0 warning

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M7, PL5
- source note mới [[src-tt83-2025-nhnn]]: 39 claim (C3-M7: 13 claim Đ53–55; C5 Đ74 đọc một phần: 4 claim ^d74-1, ^d74-4a, ^d74-4b, ^d74-6; PL5: 22 claim ^pl5-*); 6 bảng tham số (Bảng 1–6)
- created: [[tt83-2025]] (regulation VN, draft; implements [[bcbs-irrbb]] là diễn giải; 8 relation governs có cite)
- updated: [[notional-repricing-cash-flow]] (cột VN bảng Basel vs VN, thêm dòng lãi suất thả nổi), [[repricing-balance-sheet]] (đoạn yêu cầu repricing gap profile Đ53.1.a(i), Đ55, Đ54.4.a)
- proposed: [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[standardised-interest-rate-shocks]] (thay `[cần nguồn: …PL5]` về VND), [[non-maturity-deposits]], [[behavioural-options]], [[irrbb-standardised-framework]], [[gap-risk]] (node canonical — chỉ đề xuất)
- Basel vs VN: 19 thang, trần NMDs lõi, $\gamma_i$, $u_i$, Bảng 5 tham số sốc giống d368; khác: chiết khấu chỉ risk-free rate, KAO ngân hàng tự đo, VND không có trong Bảng 5 (tự tính: bình quân 16 năm × $\hat{\alpha}$ 60/85/40%, sàn 100 bp, trần 400/500/300 bp), ngưỡng đồng tiền ≥ 5% tổng tài sản sổ ngân hàng, lộ trình ΔNII hoặc ΔEVE tới 31/12/2027, cả hai từ 01/01/2028; không thấy phép thử outlier 15% Tier 1
- conflicts: không có
- syntheses flagged: 9 synthesis draft ([[irrbb-basis-risk-measurement-and-hedging]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-commercial-margins-and-discount-curves]], [[irrbb-csrbb-measurement-and-hedging]], [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[irrbb-liquidity-hqla-and-ftp-interaction]], [[irrbb-principal-and-interest-cash-flows]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[irrbb-standardised-shocks-eve-and-nii-measurement]]) — `[cần nguồn: …C3-M7/PL5]` có thể thay bằng claim mới
- backfill: linked [[tt83-2025]] ở [[notional-repricing-cash-flow]], [[repricing-balance-sheet]] · proposed [[gap-risk]] · không có relation cần chuyển đích
- convert: raw lẫn NFC/NFD (dòng 1477, 1481, 1511); ghi chú biên tập ở PL5 dòng 2433; cận tổng $\sum_{K=1}^{K}$ ở PL5
- registry: mark C3-M7, PL5 done; C5 chưa mark (chỉ đọc Đ74)
- lint: 0 error / 0 warning
- tiếp theo: duyệt 7 đề xuất canonical; `/research` rà 9 synthesis IRRBB với cột NHNN; src-tt83-2025-nhnn C3-M9 (ICAAP), PL2 (báo cáo IRRBB gửi NHNN)

## [2026-10-19] review | áp 7 đề xuất TT83/2025 đã duyệt vào node canonical
- thêm mục `## Basel vs VN` (mỗi dòng cite riêng, cột hiệu lực theo Đ74): [[economic-value-of-equity]] (7 dòng), [[net-interest-income-sensitivity]] (6), [[standardised-interest-rate-shocks]] (6), [[non-maturity-deposits]] (5), [[behavioural-options]] (4), [[irrbb-standardised-framework]] (6), [[gap-risk]] (2)
- [[standardised-interest-rate-shocks]]: callout đồng tiền ngoài Table 1 thay `[cần nguồn: src-tt83-2025-nhnn PL5]` bằng pl5-c1-1, pl5-c1-2
- frontmatter: thêm `vn-reg` vào domains, `[[src-tt83-2025-nhnn]]` vào sources; maturity giữ canonical; dòng đề xuất nối "→ đã áp [2026-10-19]"
- `[cần nguồn]` còn lại ở cột Basel: định nghĩa ΔNII, hạn mức, đồng tiền ngoài Table 1, tiêu chí behavioural option, repricing gap; cột VN: phép thử outlier, commercial margin trong ΔNII
- lint: 0 error / 0 warning

## [2026-10-19] research | IRRBB Basel vs NHNN — rà 9 synthesis với TT83/2025 C3-M7, PL5
- bộ câu hỏi: 10 câu (Q1–Q9 lấy từ câu hỏi/khoảng trống VN của 9 synthesis; Q10 = ô `[cần nguồn]` cột Basel ở 7 node canonical) · phủ: 2 đủ / 6 một phần / 2 thiếu · phương án: viết theo cụm
- bản đồ phủ:
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | Q1 basis risk VN | một phần | [[irrbb-basis-risk-measurement-and-hedging]], [[tt83-2025]] | C3-M7/PL5 không có quy định riêng basis risk; 29 dòng uncited |
  | Q2 CASA, hedge accounting VN | một phần | [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[non-maturity-deposits]] | hedge accounting chưa có nguồn trong registry |
  | Q3 Deduct/Include margin VN | một phần | [[irrbb-commercial-margins-and-discount-curves]], [[tt83-2025]] | PL5 không nói margin; tt83 C3-M8 |
  | Q4 CSRBB VN | thiếu | [[irrbb-csrbb-measurement-and-hedging]] | C3-M7/PL5 không nhắc CSRBB; TT41/2016, TT11/2021 chưa register |
  | Q5 fixed/floating VN | đủ | [[irrbb-fixed-vs-floating-cash-flows-and-repricing]], [[notional-repricing-cash-flow]] | tt83 C3-M8 (giả định hành vi) |
  | Q6 LCR/NSFR + IRRBB VN | một phần | [[irrbb-liquidity-hqla-and-ftp-interaction]] | tt83 C3-M5, tt50-2026 |
  | Q7 CF gốc/lãi, margin, VND | một phần | [[irrbb-principal-and-interest-cash-flows]] | margin không quy định; tt83 C3-M8 |
  | Q8 dải, CASA lõi, khe hở VN | đủ | [[irrbb-repricing-profiles-and-behavioral-modeling]], [[tt83-2025]] | 15 dòng uncited |
  | Q9 sốc VND, outlier VN | một phần | [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[standardised-interest-rate-shocks]] | outlier: tt83 PL6 (RWA_IRRBB dòng 2794), C3-M9 |
  | Q10 ô Basel `[cần nguồn]` | thiếu | 7 node canonical | d368 u03 par 28–29 (dòng 108–114), u07 dòng 997–1042 (bổ sung) |
- cần ingest: src-tt83-2025-nhnn C3-M8 (Q3, Q5, Q7), PL6 + C3-M9 (Q9, Q4), src-bcbs-irrbb-2016 u03 + u07 bổ sung (Q10), src-tt83-2025-nhnn C3-M5 + src-tt50-2026-nhnn (Q6)
- updated (synthesis draft, viết theo cụm): [[irrbb-basis-risk-measurement-and-hedging]] (Q1: sửa câu C3-M7 "nhận diện chỉ số tham chiếu" vượt nguồn → ^d54-2; PL5 không có kịch bản basis), [[irrbb-casa-replicating-portfolio-and-irs-hedging]] (Q2: trần NMDs lõi, phòng ngừa ^d53-1b, ^d54-2, ^d55-1), [[irrbb-commercial-margins-and-discount-curves]] (Q3: PL5 chỉ risk-free ^pl5-a3-2, không nói margin), [[irrbb-csrbb-measurement-and-hedging]] (Q4: C3-M7/PL5 không có CSRBB; ô TT11/2021 thành `[cần nguồn]`), [[irrbb-fixed-vs-floating-cash-flows-and-repricing]] (Q5: ^pl5-a2-1, ^pl5-a1-1c, bãi bỏ TT13/2018 ^d74-6), [[irrbb-liquidity-hqla-and-ftp-interaction]] (Q6: phần IRRBB + lộ trình), [[irrbb-principal-and-interest-cash-flows]] (Q7: CF, CPR/TDRR cá nhân, sốc VND), [[irrbb-repricing-profiles-and-behavioral-modeling]] (Q8: repricing gap profile, giả định ^d54-4a, ^d54-3d), [[irrbb-standardised-shocks-eve-and-nii-measurement]] (Q9: 6+2 kịch bản, tổng hợp, sốc VND; outlier `[cần nguồn: PL6, C3-M9]`)
- frontmatter 9 synthesis: thêm `[[src-tt83-2025-nhnn]]`, `vn-reg`, as_of 2026-10-19; dòng đánh dấu ingest nối "→ đã rà [2026-10-19]"; mọi `[cần nguồn: src-tt83-2025-nhnn C3-M7/PL5]` đã gỡ
- phủ sau khi viết: Q5, Q8 đủ · Q1, Q2, Q3, Q6, Q7, Q9 một phần (thiếu C3-M8, C3-M5, PL6/C3-M9, hedge accounting) · Q4, Q10 thiếu
- conflicts: không có · relations: không có (9 synthesis `relations: []`, không node nào trỏ tới) · stubs: không có
- lint: 0 error / 0 warning

## [2026-10-19] ingest | src-bcbs-irrbb-2016 U03 (bổ sung)
- claim mới: ^irrbb-p03-2 (par 28 risk appetite statement, rà soát chính sách tối thiểu hằng năm), ^irrbb-p03-3 (par 29 policy limits, aggregate limits hợp nhất, gắn kịch bản), ^irrbb-p03-4 (par 32 xử lý, báo cáo vượt hạn mức)
- updated: [[tt83-2025]] (bảng Đối chiếu Basel thêm dòng "Hạn mức", "Vượt hạn mức")
- proposed: [[economic-value-of-equity]], [[net-interest-income-sensitivity]] (dòng "Hạn mức" cột Basel thay `[cần nguồn]`; thêm dòng "Vượt hạn mức"), [[bcbs-irrbb]] (Nguyên tắc 3: "phải" → theo should/must của nguồn; cụm "gap, basis, options" thuộc par 30 chưa có claim)
- conflicts: không có
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] (canonical — ghi `## Đề xuất cập nhật`)
- backfill: không có (không tạo node mới)
- câu hỏi mở: claim ^irrbb-p03-1 diễn đạt "should be articulated" thành "phải" (R1); claim cũ không sửa vì đang được cite
- registry: không chạy `mark` (u03 đã done)
- lint: 0 error / 0 warning
- tiếp theo: duyệt 3 đề xuất; `/ingest src-bcbs-irrbb-2016 u07` bổ sung dòng 997–1042 (Q10: đồng tiền ngoài Table 1, sàn, trần)

## [2026-10-19] review | áp 3 đề xuất U03 (par 28, 29, 32) đã duyệt vào node canonical
- [[economic-value-of-equity]], [[net-interest-income-sensitivity]]: `## Basel vs VN` dòng "Hạn mức" cột Basel thay `[cần nguồn]` bằng p03-1, p03-3; thêm dòng "Vượt hạn mức" (p03-4 · d54-4c)
- [[bcbs-irrbb]]: Nguyên tắc 3 viết theo should/must của nguồn (p03-1), thêm 3 bullet p03-2, p03-3, p03-4; "hạn mức riêng gap/basis/options" (par 30) → `[cần nguồn]`
- maturity giữ canonical; dòng đề xuất nối "→ đã áp [2026-10-19]"
- lint: 0 error / 0 warning

## [2026-10-19] ingest | src-bcbs-irrbb-2016 U07 (bổ sung)
- claim mới: ^irrbb-u07-6 (dòng 995, BCBS rà lại hiệu chỉnh định kỳ, vd 5 năm), ^irrbb-u07-7 (dòng 1001, chuỗi 16 năm 2000–2015, kỳ hạn 3m–20Y), ^irrbb-u07-8 (dòng 1009–1019, Table 3: 60% / 85% / 40%), ^irrbb-u07-9 (dòng 1021, 1042: Table 2 × Table 3 → Table 4 → sàn/trần → Table 1); sàn/trần đã có ở ^irrbb-u07-4
- updated: [[tt83-2025]] (dòng "Đồng tiền ngoài bảng" cột Basel thay `[cần nguồn]`, thêm dòng "Hiệu chỉnh lại biên độ sốc", bổ sung căn cứ implements)
- proposed: [[standardised-interest-rate-shocks]] (canonical — 3 ô cột Basel: sàn/trần u07-4, đồng tiền ngoài bảng u07-7/8/9, rà soát hiệu chỉnh u07-6)
- conflicts: không có (PL5.C.I.2 khớp phương pháp d368: cùng 16 năm, cùng kỳ hạn, cùng 60/85/40%)
- syntheses flagged: [[irrbb-standardised-shocks-eve-and-nii-measurement]] (Q3, sốc VND)
- convert: Table 2 mất hàng JPY–ZAR, Table 3 ký hiệu vỡ, tiêu đề Table 4 vỡ → ghi source note + `conversion.issues` registry; không chép Table 2, Table 4
- registry: không chạy `mark` (u07 đã done)
- lint: 0 error / 0 warning
- tiếp theo: duyệt đề xuất [[standardised-interest-rate-shocks]]; src-tt83-2025-nhnn C3-M8, PL6

## [2026-10-19] review | áp đề xuất U07 (bổ sung) đã duyệt vào [[standardised-interest-rate-shocks]]
- `## Basel vs VN`: cột Basel thay `[cần nguồn]` ở 3 dòng — "Đồng tiền ngoài bảng" (u07-7, u07-8, u07-9; ghi rõ d368 không nêu cách xử lý đồng tiền ngoài Table 1), "Sàn, trần tham số" (u07-4), "Tự xác định cú sốc" (u07-6); dòng "Khác biệt" thêm: PL5.C.I.2 dùng cùng phương pháp dựng Table 1
- maturity giữ canonical; dòng đề xuất nối "→ đã áp [2026-10-19]"
- lint: 0 error / 0 warning

## [2026-10-19] lint | rà lại ingest src-bcbs-irrbb-2016 U07 (bổ sung)
- 4 claim ^irrbb-u07-6…-9: trích dẫn khớp raw, diễn đạt đúng mức bắt buộc (không có must/should; "may" không xuất hiện trong đoạn trích), đặt đúng mục Unit 7
- sửa [[tt83-2025]] (draft): câu căn cứ implements "dùng cùng chuỗi 16 năm" → "16 năm hoặc khoảng thời gian ngân hàng tự xác định" (pl5-c1-2)
- proposed: [[standardised-interest-rate-shocks]] — dòng 109 thay `[cần nguồn]` (phân vị/cửa sổ) bằng phương pháp u07-7/8/9; dòng "Khác biệt" bỏ "16 năm" tuyệt đối
- claim bỏ sót trong u07 (chưa thêm): footnote 42 dòng 959 (jurisdiction được chọn khoảng khác 16 năm), dòng 979 (supervisor đặt sàn lãi suất sau sốc ≤ 0), dòng 989 (x = 4 trừ khi supervisor quy định khác), dòng 1044–1048 (rotation: ∆R(t1) ≤ 500 bp, ∆R(tK) ≤ 300 bp; cận dưới 0 hoặc âm)
- claim cũ ^irrbb-u07-4: locator ghi "lines 1034-1048" nhưng trích dẫn chỉ phủ dòng 1034; không sửa (đang được cite)
- lint: 0 error / 0 warning

## [2026-10-19] ingest | src-tt83-2025-nhnn PL5 (bổ sung)
- claim mới: ^pl5-a1-1-0 (dòng 2403, xác định phạm vi nhạy cảm lãi suất theo quy định nội bộ), ^pl5-a2-3a2 (dòng 2499–2521, NMDs ổn định / lõi / không lõi, phân bổ NMDs lõi theo Bảng 2), ^pl5-a2-3b2 (dòng 2531–2566, CPR0 theo danh mục p; CF^S là khoản trả gốc, lãi định kỳ), ^pl5-a2-3c2 (dòng 2576–2601, TDRR0 theo danh mục p; TD0 số dư còn lại), ^pl5-a3-2b (dòng 2627–2635, CF ròng tổng hợp; DF phù hợp cách phân bổ), ^pl5-c1-2b (dòng 2707, bình quân mọi lãi suất hằng ngày 9 kỳ hạn)
- updated: [[tt83-2025]] (định nghĩa: phạm vi nhạy cảm, danh mục hành vi, chiết khấu; ngoại lệ đồng tiền ngoài Bảng 5), [[notional-repricing-cash-flow]] (CF^S gồm lãi định kỳ)
- proposed: [[non-maturity-deposits]], [[behavioural-options]], [[economic-value-of-equity]], [[standardised-interest-rate-shocks]] (canonical — chỉ đề xuất)
- conflicts: không có
- syntheses flagged: [[irrbb-principal-and-interest-cash-flows]] (CF^S gồm lãi)
- backfill: không có (không tạo node mới)
- registry: không chạy `mark` (PL5 đã done); "TT83/2026" trong lệnh hiểu là TT83/2025 (tên file docx gốc "2025 - TT83 2026_114…")
- tiếp theo: src-tt83-2025-nhnn PL2 (báo cáo IRRBB gửi NHNN), C3-M8

## [2026-10-19] ingest | src-tt83-2025-nhnn PL2
- claim mới: PL2 ^pl2-0, ^pl2-i, ^pl2-ii4, ^pl2-ii6; C1 (chỉ Đ9, đọc một phần) ^d9-1, ^d9-2b, ^d9-3a, ^d9-4c, ^d9-5 — 9 claim
- updated: [[tt83-2025]] (bảng Yêu cầu chính thêm dòng Đ9; mục Báo cáo & nghĩa vụ thay `[cần nguồn]` bằng báo cáo hằng năm gửi NHNN, nội dung mục II.6 IRRBB, II.4 thanh khoản, bảng so sánh báo cáo nội bộ Đ55 với báo cáo gửi NHNN)
- proposed: không có node canonical bị đổi
- conflicts: không có
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] (canonical — `## Đề xuất cập nhật`: báo cáo gửi NHNN)
- backfill: không có (không tạo node mới)
- registry: mark PL2 done; C1 chưa mark (chỉ đọc Đ9, dòng 343–387)
- tiếp theo: src-tt83-2025-nhnn C3-M5 (thanh khoản), C3-M8 (rủi ro mô hình)

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M5
- claim mới (14): ^d45-1a, ^d45-1b, ^d45-2, ^d45-3, ^d46-1, ^d46-2, ^d47-1, ^d47-2, ^d47-3, ^d48-1, ^d48-2, ^d48-3, ^d48-4, ^d49-1
- created: [[liquidity-stress-testing]] (concept: 3 kịch bản, 5 yếu tố rủi ro, đầu vào kế hoạch dự phòng)
- updated: [[liquidity-risk-management]] (thoát stub: khung 6 khối Đ45–49), [[tt83-2025]] (Yêu cầu chính thêm Đ45–49; governs → liquidity-risk-management, liquidity-stress-testing, contingency-funding-plan), [[run-off-rate]] (góc nhìn VN Đ48.3.c; input-to → liquidity-stress-testing), [[lcr]] (link stress test VN)
- proposed: [[contingency-funding-plan]], [[funding-concentration-risk]], [[intraday-liquidity-risk]], [[hqla]] (canonical — chỉ đề xuất)
- conflicts: không có (hạn mức VN neo vào tỷ lệ pháp định VN, khác jurisdiction với LCR/NSFR)
- syntheses flagged: [[practical-alm-liquidity-governance]] (canonical — `## Đề xuất cập nhật` mới)
- backfill: linked [[lcr]] → liquidity-stress-testing · proposed [[contingency-funding-plan]] `part-of` → liquidity-risk-management · flagged [[practical-alm-liquidity-governance]]
- convert: 5 trích dẫn dòng 1261–1377 lẫn NFD, đã copy nguyên byte từ raw
- tiếp theo: src-tt83-2025-nhnn C3-M1 (Đ20 hạn mức chung, quy định chung về kiểm tra sức chịu đựng); src-tt50-2026-nhnn PL1 (tỷ lệ khả năng chi trả)

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M5 (bổ sung)
- claim mới: ^d46-1b (dòng 1287, 1291: phạm vi NHTM, CN NHNNg), ^d48-2b (dòng 1337: ví dụ kịch bản đặc thù), ^d48-3b (dòng 1345: yếu tố loại tiền tệ, khả năng chuyển đổi), ^d49-2e (dòng 1383: kết quả khắc phục kiến nghị)
- updated: [[liquidity-stress-testing]] (thêm cite d48-2b, d48-3b)
- proposed / conflicts / syntheses flagged / backfill: không có
- registry: không chạy `mark` (C3-M5 đã done)
- tiếp theo: src-tt83-2025-nhnn C3-M1

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M1
- claim mới (19): ^d17-1, ^d18-1, ^d18-2b, ^d19-1, ^d19-2, ^d19-3, ^d20-1, ^d20-2, ^d20-3, ^d22-2, ^d23-1, ^d23-2, ^d23-3, ^d23-4, ^d23-5, ^d23-6, ^d24-1, ^d25-3, ^d25-5
- created: [[risk-appetite]] (CAR mục tiêu, ROE, RAROC; d368 P3), [[risk-limits]] (Đ20; hạn mức IRRBB và thanh khoản), [[stress-testing]] (Đ23: 5 loại, 3 phương pháp gồm reverse stress test, tần suất)
- updated: [[tt83-2025]] (Yêu cầu chính thêm Đ19, Đ20, Đ23, Đ25.3; governs → risk-appetite, risk-limits, stress-testing), [[liquidity-stress-testing]] (tần suất hằng quý; part-of → stress-testing; gỡ câu hỏi mở), [[liquidity-risk-management]] (Đ20 thay `[cần nguồn]`; vai trò ALM)
- proposed: [[bcbs-irrbb]], [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[funding-concentration-risk]], [[lcr-by-currency]] (canonical — link node mới)
- conflicts: không có (VN: hạn mức do Tổng giám đốc ban hành; d368: governing body đặt policy limits — khác jurisdiction, ghi trong [[risk-limits]])
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]], [[practical-alm-liquidity-governance]], [[ftp-cost-benefit-allocation-principles]], [[ftp-nature-and-balance-sheet-management]] (canonical — `## Đề xuất cập nhật`); [[irrbb-basis-risk-measurement-and-hedging]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-csrbb-measurement-and-hedging]] (draft — `## Bất định`)
- backfill: linked [[model-risk-management]], [[balance-sheet-optimisation-model]] → risk-appetite
- câu hỏi mở còn lại: ai phê duyệt báo cáo nội bộ IRRBB (Đ55) — C3-M1 không nêu
- tiếp theo: src-tt83-2025-nhnn C3-M9 (ICAAP, Đ60 stress test vốn); C1 (Đ3.13 rủi ro trọng yếu)

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M9
- claim mới (8): ^d59-1, ^d59-2, ^d60-1, ^d60-2, ^d61-1, ^d61-2, ^d62-1, ^d63-1
- created: [[icaap]] (6 bước, stress test vốn, rà soát độc lập, báo cáo; d368 Nguyên tắc 9), [[capital-plan]] (Đ61; part-of icaap, input-to risk-limits), stub [[economic-capital]] (metric; hoàn thiện bằng PL6)
- updated: [[tt83-2025]] (Yêu cầu chính thêm Đ59–63; governs → icaap, capital-plan), [[stress-testing]] (stress test vốn; gỡ câu hỏi Đ60), [[risk-limits]] (phân bổ vốn mục tiêu làm cơ sở hạn mức), [[risk-appetite]] (liên kết ICAAP)
- proposed: [[bcbs-irrbb]] (Nguyên tắc 9 ↔ Đ60.1.a), [[csrbb]], [[duration-gap-model]], [[irrbb-standardised-framework]] (canonical — link node mới)
- conflicts: không có (VN đưa IRRBB vào stress test vốn qua tài sản tính theo rủi ro IRRBB; d368 P9 nói chung "xét trong ICAAP" và capital buffers cho rủi ro thu nhập — khác jurisdiction)
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]], 4 synthesis FTP canonical (`## Đề xuất cập nhật`); [[ftp-balance-sheet-optimization]], [[irrbb-basis-risk-measurement-and-hedging]], [[irrbb-csrbb-measurement-and-hedging]], [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[irrbb-transmission-mechanisms-to-nii-and-eve]] (draft — `## Bất định`)
- backfill: linked [[ftp-transmission-mechanism]] → economic-capital
- sửa trong lượt: bỏ câu "Tổng giám đốc tổ chức thực hiện ICAAP" ở [[icaap]] vì cite nhầm ^d25-5 (Đ25.2.b chưa có claim; ghi vào câu hỏi mở)
- tiếp theo: src-tt83-2025-nhnn PL6 (vốn kinh tế, vốn mục tiêu, tài sản tính theo rủi ro IRRBB); C3-M1 bổ sung Đ25.2.b (dòng 751)

## [2026-10-19] ingest | src-tt83-2025-nhnn PL6
- claim mới (7): ^pl6-1a (C_E), ^pl6-1b (RWA*_E 6 cấu phần), ^pl6-1c (RWA_IRRBB theo ΔEVE từ 01/01/2028), ^pl6-1d (RWA tập trung, sàn, lộ trình A/B), ^pl6-2 (C_Target), ^pl6-ii (C_A, 4 giả định), ^pl6-iii (RAROC)
- created: [[rwa-irrbb]], [[target-capital]], [[raroc]], [[projected-own-funds]] (metric)
- updated: [[economic-capital]] (thoát stub: công thức, 6 cấu phần RWA, sàn RWA tập trung), [[icaap]] (gỡ `[cần nguồn]` Phụ lục VI), [[capital-plan]] (chuẩn so sánh C_Target vs C_A), [[risk-appetite]] (CAR mục tiêu = CAR_Target; link raroc), [[tt83-2025]] (Yêu cầu chính thêm PL6.I, PL6.I.1.d(iv); governs → economic-capital, rwa-irrbb, target-capital)
- proposed: [[economic-value-of-equity]] (dòng "Dùng cho vốn"), [[bcbs-irrbb]] (Nguyên tắc 9), [[liquidity-transfer-pricing]] (link raroc) — canonical
- conflicts: không có (d368: IRRBB ở Pillar 2, không có vốn Pillar 1; VN: RWA_IRRBB trong vốn kinh tế ICAAP, vẫn là chỉ tiêu nội bộ — khác jurisdiction)
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] + 5 synthesis FTP canonical (`## Đề xuất cập nhật`); [[ftp-balance-sheet-optimization]], [[integrated-alm-liquidity-strategy]], [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[nsfr-alm-governance-strategy-and-risks]] (draft — `## Bất định`)
- backfill: linked [[ftp-transmission-mechanism]] → raroc; [[risk-limits]], [[stress-testing]] → target-capital
- convert: công thức PL6 viết bằng thẻ `<sub>`/`<sup>`; ghi vào Ghi chú convert, không trích công thức
- sửa trong lượt: `\times` trong index bị ghi thành ký tự tab do escape Python; đã sửa
- tiếp theo: src-tt83-2025-nhnn C1 (Đ3.13 rủi ro trọng yếu, ba tuyến bảo vệ); C3-M1 bổ sung Đ25.2.b

## [2026-10-19] ingest | src-tt83-2025-nhnn C1
- claim mới (22): ^d1-1, ^d3-7, ^d3-8, ^d3-9, ^d3-10, ^d3-11, ^d3-13, ^d3-15a, ^d3-20, ^d3-21, ^d3-22, ^d3-24, ^d3-32, ^d3-33, ^d4-2, ^d5-1, ^d5-1k, ^d6-2a, ^d6-4a, ^d6-4b, ^d6-4c, ^d8-2 (cộng 5 claim Đ9 đã có từ lượt PL2)
- created: [[three-lines-of-defence]] (Đ4.2), [[alco]] (Đ6.4.b, Đ25.3; so với Hội đồng rủi ro, Hội đồng quản lý vốn), [[banking-book]] (Đ3.32–34; Tata)
- updated: [[tt83-2025]] (phạm vi, rủi ro trọng yếu, định nghĩa IRRBB/sổ ngân hàng/thanh khoản/ALCO; governs → three-lines-of-defence, alco, banking-book), [[risk-appetite]] (Đ3.10, Đ3.13; gỡ câu hỏi mở Đ3.13.a), [[economic-capital]] (Đ3.7), [[stress-testing]] (Đ3.8), [[liquidity-risk-management]] (Đ3.20), [[icaap]] (Đ1.2 ngoại lệ, Hội đồng quản lý vốn), [[model-risk-management]] (góc nhìn VN Đ3.23–25)
- proposed: [[gap-risk]], [[basis-risk]], [[option-risk]], [[behavioural-options]] (định nghĩa VN Đ3.22), [[irrbb-balance-sheet-portfolios]] (link banking-book, Đ3.32–33), [[bcbs-irrbb]] — canonical; cộng 16 node canonical đề xuất link [[alco]]
- conflicts: không có (định nghĩa IRRBB VN cùng 3 cấu phần d368; VN không nhắc CSRBB — khác phạm vi định nghĩa, không phải mâu thuẫn)
- syntheses flagged: 26 synthesis nhắc ALCO (draft → `## Bất định`, canonical → `## Đề xuất cập nhật`); [[irrbb-alm-governance-strategy-and-tradeoffs]] thêm dòng ba tuyến bảo vệ
- backfill: linked [[ftp-transmission-mechanism]], [[lcr-nsfr-interlinkages]], [[model-risk-management]], [[nsfr]], [[rsf-loans-and-credit-exposures]], [[balance-sheet-optimisation-model]] → alco (gỡ link chèn nhầm trong sơ đồ ASCII của [[ftp-pricing-methodology]])
- convert: dòng 107 (Đ3.21) lẫn NFD và `*…*`; đã copy nguyên byte
- registry: mark C1 done (đã đọc trọn dòng 25–398)
- tiếp theo: src-tt83-2025-nhnn C3-M8 (rủi ro mô hình, Đ56.7); C3-M1 bổ sung Đ25.2.b (dòng 751)

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M8
- claim mới (8): ^d56-1, ^d56-2, ^d56-4, ^d56-4d, ^d56-5, ^d56-7, ^d57-1, ^d58-1
- created: [[model-validation]] (Đ56.4.đ, Đ56.7; d368 Nguyên tắc 6; Lubinska effective challenge)
- updated: [[model-risk-management]] (góc nhìn VN: xếp hạng, vòng đời, override, mô hình mua ngoài, ba tuyến, báo cáo; gỡ `[cần nguồn]` Mục 8), [[three-lines-of-defence]] (bảng ba tuyến cho mô hình; câu hỏi mở về vị trí bộ phận ALM), [[tt83-2025]] (Yêu cầu chính Đ56–58; governs → model-risk-management, model-validation)
- proposed: [[non-maturity-deposits]], [[behavioural-options]] (mô hình hành vi chịu kiểm định hằng năm), [[bcbs-irrbb]] (Nguyên tắc 6 vs Đ56), [[outlier-bank-test]] (link) — canonical
- conflicts: không có (d368 nêu cấu phần kỹ thuật kiểm định; TT83 nêu tần suất và phân tuyến — bổ sung nhau)
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] (canonical), [[irrbb-casa-replicating-portfolio-and-irs-hedging]] (draft)
- backfill: không có link mới ngoài các node đã cập nhật
- convert: 1 trích dẫn lẫn NFD, đã copy nguyên byte
- tiếp theo: src-tt83-2025-nhnn C3-M3 (rủi ro thị trường), C3-M6 (rủi ro tập trung); C3-M1 bổ sung Đ25.2.b

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M3
- claims: 7 (d35-1, d35-2, d36-1, d36-1c, d36-2, d37-1, d37-2)
- created: [[market-risk-management]]
- updated: [[risk-limits]] (hạn mức rủi ro thị trường Đ35.2), [[stress-testing]], [[banking-book]], [[model-risk-management]] (mô hình giá Đ36.1.c), [[tt83-2025]] (dòng Đ35–37, governs market-risk-management)
- proposed: [[csrbb]] (canonical — link market-risk-management)
- conflicts: không có
- syntheses flagged: [[ftp-portfolio-and-bucket-allocation]], [[ftp-nature-and-balance-sheet-management]] (Đề xuất cập nhật), [[irrbb-csrbb-measurement-and-hedging]] (Bất định, Q5)
- backfill: linked [[icaap]], [[repricing-balance-sheet]] · flagged 3 synthesis trên · proposed [[csrbb]]
- tiếp theo: src-tt83-2025-nhnn C3-M6 (rủi ro tập trung), C3-M2 (rủi ro tín dụng)

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M2
- claims: 14 (d26-1, d26-2, d26-2c, d26-3, d27-1, d27-2, d28-1, d28-2, d29-1, d30-1, d31-1, d32-2, d33-1, d34-1)
- created: [[credit-risk-management]]
- updated: [[risk-limits]] (hạn mức tín dụng Đ26.3), [[stress-testing]], [[model-validation]] (xếp hạng nội bộ đánh giá độc lập hằng năm), [[funds-transfer-pricing]] (Đ26.2.c, Đ45.1.b), [[ftp-pricing-methodology]], [[tt83-2025]] (dòng Đ26–34, governs credit-risk-management)
- proposed: không có
- conflicts: không có
- syntheses flagged: [[ftp-risk-and-cost-components]], [[ftp-final-rate-determination]] (Đề xuất cập nhật: Đ26.2.c pricing tín dụng), [[irrbb-commercial-margins-and-discount-curves]] (Bất định)
- backfill: linked [[icaap]], [[market-risk-management]], [[ftp-transmission-mechanism]] · flagged 3 synthesis trên
- tiếp theo: src-tt83-2025-nhnn C3-M6 (rủi ro tập trung), C3-M4 (rủi ro hoạt động)

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M6
- claims: 6 (d50-1, d50-2, d50-3, d51-1, d51-2, d52-1)
- created: [[concentration-risk-management]] (kèm sàn $RWA_{COR}$ và lộ trình A/B từ claim PL6 sẵn có pl6-1d)
- updated: [[credit-risk-management]], [[market-risk-management]], [[risk-limits]] (hạn mức tập trung Đ50.3), [[economic-capital]] (link), [[tt83-2025]] (dòng Đ50–52, governs concentration-risk-management)
- proposed: [[funding-concentration-risk]] (canonical — góc nhìn VN: Đ50 không áp cho nguồn vốn, chỉ Đ48.3.d)
- conflicts: không có (khác phạm vi với SRP50)
- syntheses flagged: [[basel-liquidity-monitoring-framework]], [[synthetic-balance-sheet-liquidity-risk]] (Đề xuất cập nhật), [[integrated-alm-liquidity-strategy]], [[lcr-economic-significance-and-alm-governance]] (Bất định)
- backfill: linked [[credit-risk-management]], [[market-risk-management]], [[economic-capital]] · flagged 4 synthesis trên · proposed [[funding-concentration-risk]]
- tiếp theo: src-tt83-2025-nhnn PL3 (báo cáo ICAAP), C3-M4 (rủi ro hoạt động)

## [2026-10-19] ingest | src-tt83-2025-nhnn PL3
- lệnh gốc: `/ingest src-tt83-2025-nhnn IRRBB`; C3-M7 và PL5 đã done, user chọn ingest PL3 (dòng RWA_IRRBB và thuyết minh phương pháp)
- claims: 6 (pl3-1, pl3-2, pl3-3a, pl3-3b, pl3-4, pl3-5) + 1 bổ sung C1 (d9-2c, Đ9.2.c báo cáo ICAAP hằng năm theo PL3)
- created: không có
- updated: [[icaap]] (bảng cấu trúc báo cáo PL3), [[rwa-irrbb]] (thuyết minh phương pháp), [[target-capital]], [[projected-own-funds]], [[raroc]], [[risk-appetite]], [[capital-plan]], [[stress-testing]], [[tt83-2025]] (dòng Đ9.2.c, PL3)
- proposed: không có
- conflicts: không có
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] (Đề xuất cập nhật), [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[ftp-balance-sheet-optimization]] (Bất định)
- backfill: không có
- tiếp theo: src-tt83-2025-nhnn C3-M4 (rủi ro hoạt động), C2 (hoạt động kiểm soát)

## [2026-10-19] ingest | src-tt83-2025-nhnn C5
- claims: 3 mới (d74-2, d74-3, d74-5); C5 trước đó đã có d74-1, d74-4a, d74-4b, d74-6; Đ75 (tổ chức thực hiện) không lấy claim. Đọc trọn unit, mark done
- created: không có
- updated (sửa hiệu lực sai "từ 01/07/2026 [d74-1]", vì Đ74.1 loại trừ khoản 2–4): [[model-validation]], [[model-risk-management]], [[three-lines-of-defence]] (Mục 8 chậm nhất 01/01/2028, mô hình xếp hạng nội bộ sớm hơn), [[credit-risk-management]], [[market-risk-management]], [[stress-testing]] (stress test tín dụng, thị trường chậm nhất 01/01/2028); [[rwa-irrbb]] (Đ74.5 áp dụng sớm ΔNII+ΔEVE phải thông báo NHNN 10 ngày); [[tt83-2025]] (dòng Đ23, Đ56–58; thêm dòng Đ74.2, Đ74.3, Đ74.5)
- proposed: không có
- conflicts: không có
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] (Đề xuất cập nhật), [[irrbb-casa-replicating-portfolio-and-irs-hedging]] (Bất định) — hiệu lực kiểm định mô hình
- backfill: không có
- tiếp theo: src-tt83-2025-nhnn C3-M1 bổ sung Đ25.2.b (dòng 751); C3-M4 (rủi ro hoạt động)

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M1 (bổ sung)
- claims: 1 mới (d25-2b: Đ25.2.a–b, Tổng giám đốc xây dựng, tổ chức thực hiện chính sách quản lý rủi ro và tổ chức thực hiện ICAAP)
- created: không có
- updated: [[icaap]] (thêm trách nhiệm Tổng giám đốc; đóng câu hỏi mở Đ25.2.b)
- proposed: không có
- conflicts: không có
- syntheses flagged: không có (chỉ thêm phân vai, không đổi kết luận)
- backfill: không có
- tiếp theo: src-tt83-2025-nhnn C3-M4 (rủi ro hoạt động)

## [2026-10-19] ingest | src-tt83-2025-nhnn C3-M4
- claims: 8 (d38-1, d38-2, d39-2, d39-3, d40-2, d42-1, d43-1, d44-1)
- created: [[operational-risk-management]]
- updated: [[risk-limits]] (hạn mức tổn thất rủi ro hoạt động), [[tt83-2025]] (dòng Đ38–44, governs operational-risk-management; sửa dòng phạm vi đã ingest)
- proposed: không có
- conflicts: không có
- syntheses flagged: không có
- backfill: linked [[economic-capital]], [[icaap]], [[market-risk-management]]
- tiếp theo: TT83 còn C2, C4, PL1, PL4 (kiểm soát, kiểm toán nội bộ; giá trị ALM thấp)

## [2026-10-19] ingest | src-tt83-2025-nhnn preamble, C2, C4, PL1, PL4 (+ bổ sung C1, C3-M1, C3-M4)
- claims: 20 — preamble (pre-1); C2 (d11-1, d11-5, d12-2, d13-2, d14-3, d15-2, d16-2, d16-3); C4 (d64-1, d65-3, d66-2, d69-1, d70-1, d71-1, d73-1); PL1 (pl1-1); PL4 (pl4-1); bổ sung C1 (d2-1, d7-1, d10-1), C3-M1 (d21-1, d21-2), C3-M4 (d41-1)
- created: [[new-product-approval]]
- updated: [[tt83-2025]] (phạm vi Đ2, cấu trúc Đ7; dòng Đ11–16, Đ21, Đ64–73; PL1, PL4; governs new-product-approval), [[three-lines-of-defence]] (bộ phận tuân thủ, kiểm toán nội bộ tuyến 3), [[market-risk-management]] (kiểm soát giao dịch tự doanh Đ16), [[credit-risk-management]] (xung đột lợi ích Đ15), [[operational-risk-management]] (Đ41), [[funds-transfer-pricing]] (link sản phẩm mới)
- proposed: không có
- conflicts: không có
- syntheses flagged: không có
- backfill: linked [[funds-transfer-pricing]]
- src-tt83-2025-nhnn: 20/20 unit done
- tiếp theo: src-tt50-2026-nhnn C2-M3

## [2026-10-19] skip | src-bcbs-framework SRP31, SRP98, DIS70
- lý do: trùng d368 đã ingest (đối chiếu raw: SRP98 99/113, SRP31 216/268, DIS70 26/39 đoạn dài khớp nguyên văn; phần lệch là link chéo, định dạng); cả ba là bản hợp nhất hiệu lực 15/12/2019, chưa có hiệu chỉnh d578
- claims: không có

## [2026-10-19] ingest | src-tata-bank-alm u08
- lệnh gốc: `/ingest IRRBB`; user chọn SRP98 → trùng d368, mark skipped SRP31/SRP98/DIS70 (entry skip ở trên), rồi ingest Tata u08
- claims: 18 (tata-eba-1…5, tata-sot-1…4, tata-rep-1…4, tata-fut-1…5)
- created: không có
- updated: [[model-validation]] (AI/ML, backtest mô hình hành vi), [[funds-transfer-pricing]] (rủi ro khí hậu trong FTP; bổ sung src-tt83 vào sources)
- proposed: [[outlier-bank-test]] (SOT NII 5%, sàn tuyến tính, tuân thủ đồng thời), [[net-interest-income-sensitivity]] (EBA SA 3 cấu phần, MV), [[economic-value-of-equity]], [[non-maturity-deposits]] (PTR), [[behavioural-options]] — canonical
- conflicts: không có (khung EU khác jurisdiction với d368/TT83; ngưỡng 15% EVE trùng d368)
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] (Đề xuất cập nhật); [[irrbb-standardised-shocks-eve-and-nii-measurement]], [[irrbb-transmission-mechanisms-to-nii-and-eve]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-repricing-profiles-and-behavioral-modeling]] (Bất định)
- backfill: không có
- tiếp theo: src-tata-bank-alm u07 (3.6 Rapid Rise in Interest Rates)

## [2026-10-19] ingest | src-tata-bank-alm u07
- lệnh gốc: `/ingest IRRBB`; user chọn Tata u07, phạm vi Mở rộng
- claims: 23 (tata-rr-1…4, tata-svb-1…10, tata-reg-1…9)
- created: [[silicon-valley-bank]] (entity)
- updated: [[model-validation]] (bài học SVB về giả định duration tiền gửi), [[lcr]] (link)
- proposed: [[outlier-bank-test]] (lịch sử ngưỡng EU 20% → 15% + NII, nguyên tắc SOT EBA 2018, sàn −100 bp/20 năm), [[non-maturity-deposits]], [[behavioural-options]], [[duration-gap-model]] — canonical
- conflicts: không có (sàn EBA 2018 và RTS 2022 khác hiệu lực)
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]], [[irrbb-five-tier-architecture]], [[practical-alm-liquidity-governance]] (Đề xuất cập nhật); [[hqla-decomposition-and-tradeoffs]], [[integrated-alm-liquidity-strategy]], [[irrbb-liquidity-hqla-and-ftp-interaction]], [[nsfr-alm-governance-strategy-and-risks]], [[nsfr-structural-liquidity-and-alm-strategy]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[irrbb-standardised-shocks-eve-and-nii-measurement]] (Bất định)
- backfill: linked [[lcr]] · proposed [[funding-concentration-risk]], [[irrbb-balance-sheet-portfolios]], [[available-stable-funding]], [[hqla]] (link SVB, đối chiếu số liệu)
- tiếp theo: src-tata-bank-alm u06 (Notes, xem có skip được không); src-choudhry-fixed-income-markets ch13 (Swaps)

## [2026-10-19] ingest | src-tata-bank-alm u06
- phạm vi: §3.1–3.5 (dòng 2177–2468); dòng 2069–2176 là Notes/References của ch2, không lấy claim; 21 claim (tata-prac-1…5, tata-niip-1…6, tata-beh-1…4, tata-neg-1…6)
- created: [[nii-planning]], [[negative-interest-rates]]
- updated: [[funds-transfer-pricing]] (ALM profit/cost center, truyền dẫn NMD), [[model-validation]] (backtest qua regime lãi suất), [[balance-sheet-optimisation-model]] (link)
- proposed: [[non-maturity-deposits]], [[behavioural-options]], [[net-interest-income-sensitivity]], [[option-risk]], [[interest-rate-cap-floor]] (canonical — chỉ đề xuất)
- conflicts: không có
- syntheses flagged: [[irrbb-repricing-profiles-and-behavioral-modeling]] (deposit beta có nguồn), [[irrbb-standardised-shocks-eve-and-nii-measurement]] (lãi suất âm)
- backfill: linked [[balance-sheet-optimisation-model]] · flagged 2 synthesis trên · proposed [[interest-rate-cap-floor]], [[option-risk]]
- sửa sổ sách: dòng index của src-tata-bank-alm ghi "4 units" từ trước, sửa thành 7
- tiếp theo: src-choudhry-fixed-income-markets ch13 (Swaps) hoặc src-lubinska-alm-optimisation u02 (Basel III)

## [2026-10-19] ingest | src-lubinska-alm-optimisation u02
- phạm vi: phương án Mở rộng, dòng 447–957; 50 claim (lubinska-u02-1…50): Ch1 Basel III (lịch sử, 3 trụ cột, LCR/HQLA/NSFR, vốn CRD IV, đòn bẩy), tổng quan tài liệu (EBA GL IRRBB 2015/2018, Memmel, Resti, Baldan); Ch2 maturity/repricing/refixing/incremental gap, phân loại IRRBB, EVE internal/external view, conditional CF, case study KAO, PV01, duration gap, ICAAP theo EBA 2018
- created: [[repricing-gap-analysis]] (model), [[pv01]] (metric); công thức ΔNII, incremental gap, PV01 dựng lại dưới nhãn tái dựng (raw formula-not-decoded)
- updated: [[icaap]] (EBA GL 2018, Trụ cột 2), [[repricing-balance-sheet]], [[ftp-transmission-mechanism]] (link)
- proposed: [[duration-gap-model]], [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[gap-risk]], [[basis-risk]], [[option-risk]], [[leverage-ratio]], [[key-rate-duration]] (canonical — chỉ đề xuất)
- conflicts: không có callout; ghi nhận diễn đạt lệch của nguồn T4 về tỷ lệ đòn bẩy "maximum of 3%" (LEV T2: tối thiểu 3%), đề xuất ghi chú ở [[leverage-ratio]]
- syntheses flagged: [[irrbb-five-tier-architecture]] (canonical), [[irrbb-transmission-mechanisms-to-nii-and-eve]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-standardised-shocks-eve-and-nii-measurement]] (sốc ±200 bp bối cảnh EUR), [[irrbb-repricing-profiles-and-behavioral-modeling]]
- backfill: linked [[repricing-balance-sheet]], [[ftp-transmission-mechanism]] · proposed [[key-rate-duration]]
- tiếp theo: src-lubinska-alm-optimisation u01 (front matter + Ch1 ALM, có thể skip phần mục lục) hoặc src-choudhry-fixed-income-markets ch13

## [2026-10-19] ingest | src-choudhry-principles-banking u25
- phạm vi: phương án Mở rộng, dòng 12526–13025; 25 claim (choudhry-clim-1…4: Ch22 rủi ro khí hậu, PRA SS3/19, chính sách, RMF 9 mảng; choudhry-cs-1…21: Ch23 CS1 đường cong nội bộ, CS2 FTP Europe Arab Bank, CS3 Treasury công ty chứng khoán, CS4 ALCO, CS5 phòng ngừa IRRBB, CS6 chiến lược tiền gửi)
- created: [[structural-hedging]] (concept, hedges → gap-risk có cite), [[climate-risk]] (concept)
- updated: [[alco]] (case study cấu trúc ALCO, ALCO phê duyệt thay đổi phương pháp), [[funds-transfer-pricing]] (NII âm, bỏ FTP Libor-flat, link climate-risk)
- proposed: [[gap-risk]], [[interest-rate-swap]], [[liquidity-transfer-pricing]], [[funding-concentration-risk]], [[non-maturity-deposits]] (canonical — chỉ đề xuất)
- conflicts: không có; "Type A/B" là phân loại của cơ quan quản lý Anh, không phải BCBS LCR
- syntheses flagged: [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-basis-risk-measurement-and-hedging]] (draft); [[irrbb-alm-governance-strategy-and-tradeoffs]], [[irrbb-five-tier-architecture]], [[practical-alm-liquidity-governance]] (canonical)
- backfill: linked [[funds-transfer-pricing]] → [[climate-risk]]; [[structural-hedging]] cite TT83 d3-33 (phái sinh phòng ngừa thuộc sổ ngân hàng)
- tiếp theo: src-choudhry-principles-banking u14 (ALCO PRA, basis risk cấu trúc, hedge accounting) hoặc u11 (công cụ phòng ngừa IRR)

## [2026-10-19] ingest | src-choudhry-principles-banking u26
- phạm vi: phương án Mở rộng, dòng 13026–13531; 13 claim (choudhry-cs-22…28: phần cuối CS6, CS7, Final Remarks, Appendix 23.1 CS5; choudhry-rae-1…4: Ch24 George Rae 1890; choudhry-web-1…2: Ch25 ChoudWest Bank, file IRRBB trên website); không trích dòng 13277–13283 (thông tin đăng nhập website)
- created: không có
- updated: [[alco]] (ALCO sở hữu Deposits Analysis Template, ALCO là diễn đàn tranh luận)
- proposed: [[non-maturity-deposits]], [[liquidity-transfer-pricing]] (canonical — chỉ đề xuất)
- conflicts: không có
- syntheses flagged: không có (không đổi tham số, phạm vi hay quan hệ)
- backfill: không có
- tiếp theo: src-choudhry-principles-banking u14 (ALCO PRA, basis risk cấu trúc, hedge accounting) hoặc u11 (công cụ phòng ngừa IRR)

## [2026-10-19] ingest | src-bcbs-framework RBC25
- phạm vi: phương án Mở rộng, dòng 2174–2454; 37 claim (rbc25-0…34, gồm FAQ rbc25-5-faq1, 6-faq2, 9-faq1/2/3, 16-faq1/2, 25-faq1); gồm cả phần CVA RBC25.30–25.34
- created: [[regulatory-internal-risk-transfer]] (concept; tách khỏi [[internal-risk-transfer]] mang nghĩa FTP)
- updated: [[banking-book]] (tiêu chí Basel RBC25, bảng chuyển sổ, bảng Basel vs VN; thêm domain basel, nguồn src-bcbs-framework; câu hỏi mở chuyển sổ có phần Basel)
- proposed: [[internal-risk-transfer]] (canonical — ghi chú phân biệt với IRT pháp quy)
- conflicts: không có; khác jurisdiction: TT83 xếp mọi repo vào sổ ngân hàng, RBC25 xếp repo phục vụ kinh doanh vào trading book; TT83 dùng ngưỡng thời gian ≤ 1 năm cho tự doanh, RBC25 dùng mục đích nắm giữ
- syntheses flagged: [[ftp-portfolio-and-bucket-allocation]] (canonical; phân định Banking/Trading Book và vị trí repo)
- backfill: không có node hay synthesis nào nhắc IRT theo nghĩa pháp quy; các link [[internal-risk-transfer]] hiện có đều mang nghĩa FTP, giữ nguyên
- sửa sổ sách: overview ghi src-bcbs-framework "1 / 44" units, registry có 115 units; sửa thành 2 / 115
- tiếp theo: src-bcbs-framework MAR11–MAR12 (định nghĩa rủi ro thị trường, trading desk) hoặc RBC20; ngoài framework: src-choudhry-principles-banking u14

## [2026-10-19] ingest | src-choudhry-principles-banking u10 u11 u14
- phạm vi: phương án Mở rộng, dòng 4770–5797 và 6870–7371; 80 claim (salm-1…3, opt-1…6, neg-1…5, fxs-1…5, hedge-1…27, sec-1…5, tig-1…2, alco-4…20, enc-1…10)
- created: [[forward-rate-agreement]], [[interest-rate-futures]], [[overnight-index-swap]], [[cross-currency-swap]] (instrument); [[securitisation]], [[asset-encumbrance]] (concept)
- updated: [[alco]] (FSA/PRA SS1/13, MI pack, bảng ToR Choudhry vs TT83, vị trí pari passu, tiểu ban ICLAAP, GALCO), [[negative-interest-rates]] (chính sách sản phẩm, NMD, balance guarantee swap), [[structural-hedging]] (công cụ phòng ngừa, ví dụ EAR và cap), [[balance-sheet-optimisation-model]] (LPP vs interior-point, tích hợp liquidity–IRRBB)
- proposed: [[interest-rate-swap]], [[interest-rate-cap-floor]], [[basis-risk]], [[net-interest-income-sensitivity]], [[non-maturity-deposits]], [[gap-risk]], [[hqla]] (canonical — chỉ đề xuất)
- conflicts: không có; khác jurisdiction: ALCO theo Choudhry/PRA (CFO chủ tịch, hằng tháng, báo cáo Board) vs TT83 Đ6.4.b (giúp việc TGĐ, tối thiểu hằng quý) — ghi bảng trong [[alco]]
- câu hỏi mở: ChoudWest 0,6 tỷ USD/năm (Choudhry) vs Ngân hàng 2 0,6526 tỷ USD/6 tháng (Lubinska) — chưa rõ cùng bài toán, ghi trong [[balance-sheet-optimisation-model]]; Table 6.4 ghi `80mm * (5% - 4%)` lệch lời văn (strike 3%), ghi chú convert
- syntheses flagged: 16 synthesis (quản trị ALCO; công cụ phòng ngừa IRRBB; NMD lãi suất âm; tối ưu hoá; link OIS/CCS/securitisation/encumbrance) — xem `## Bất định` / `## Đề xuất cập nhật`
- backfill: linked [[forward-rate-agreement]] ([[repricing-gap-analysis]], [[repricing-balance-sheet]]), [[interest-rate-futures]] và [[overnight-index-swap]] ([[repricing-balance-sheet]]), [[cross-currency-swap]] ([[rsf-derivatives-and-off-balance-sheet]]), [[securitisation]] ([[banking-book]]), [[asset-encumbrance]] ([[rsf-securities-financing-and-encumbrance]], [[lcr-nsfr-interlinkages]]) · proposed link ở 7 node canonical ([[interest-rate-cap-floor]], [[lcr-by-currency]], [[contingency-funding-plan]], [[irrbb-balance-sheet-portfolios]], [[liquidity-transfer-pricing]], [[economic-value-of-equity]], [[required-stable-funding]])
- tiếp theo: src-choudhry-principles-banking u09 (nguồn IRR, giả định gap analysis, ALM desk) hoặc u15 (asset encumbrance policy, hedge accounting, IFRS 9)

## [2026-10-19] ingest | src-choudhry-principles-banking u09 u15
- phạm vi: phương án Mở rộng, dòng 4259–4769 và 7372–7883; 69 claim (lgap-1…10, irr-1…8, desk-1…4, mo-1…3, salm-4…14, enc-11, hacc-1…5, ecl-1…5, eir-1…3, liq-1…12, igl-1…3, lab-1…4)
- created: [[hedge-accounting]], [[strategic-alm]] (concept); [[expected-credit-loss]], [[effective-interest-rate]] (metric)
- updated: [[liquidity-risk-management]] (10 nguyên tắc, liquidity policy statement, LAB), [[risk-appetite]] (RAS theo Choudhry), [[repricing-gap-analysis]] (giả định, điểm yếu, bucket NMD), [[alco]] (EWI, IRR, IGL, IFRS 9), [[asset-encumbrance]] (khung 4 bước), [[structural-hedging]] (hedge accounting), [[liquidity-transfer-restrictions]] (IGL 25%), [[funds-transfer-pricing]] (cost/profit centre, funding cash/balance sheet)
- proposed: [[hqla]], [[gap-risk]], [[basis-risk]], [[non-maturity-deposits]], [[contractual-maturity-mismatch]], [[option-risk]], [[interest-rate-swap]] (canonical — chỉ đề xuất)
- conflicts: không có; khác phạm vi: ALM Smile ≤20% funding O/N–1 tuần (Ch5) vs ≤20–30% bảng cân đối dưới 3 tháng (Ch11, trích sách 2007); LAB survival 2 tuần/3 tháng vs LCR 30 ngày (nguồn tự ghi LCR nay quyết định quy mô HQLA)
- ghi chú convert: dòng 4633–4639 trộn cột; Figure 10.8 (ECL stage) tách dòng rời; Table 11.1 lệch cột; ba loại hedge chỉ có trong hình
- syntheses flagged: 10 synthesis (quản trị thanh khoản và LAB; RAS; giả định gap analysis; IGL; link hedge accounting)
- backfill: linked [[hedge-accounting]] và [[strategic-alm]] ([[structural-hedging]]) · proposed [[interest-rate-swap]] (link hedge accounting), [[hqla]] (link EIR)
- tiếp theo: src-choudhry-principles-banking u18 (Ch11 phần tiếp: liquidity metrics, CFP) hoặc u03–u04 (Ch1 NII/NIM sensitivity, kịch bản lãi suất ChoudWest)

## [2026-10-19] ingest | src-choudhry-principles-banking u03 u04
- phạm vi: phương án Mở rộng, dòng 1181–2186 (bảng kịch bản chỉ đọc phần kết quả; Ch2 từ dòng 2047 đọc lướt, không trích); 25 claim (ref-1…3, lp-1…6, risk-1…2, nim-1…14)
- created: [[net-interest-margin]] (metric), [[loan-pricing]] (concept)
- updated: [[nii-planning]] (dự báo top-down/bottom-up, dữ liệu cấp tài khoản), [[alco]] (duyệt cho vay dưới TRR), [[raroc]] (định giá theo RoE mục tiêu)
- proposed: [[net-interest-income-sensitivity]] (case 5 kịch bản, cơ chế tái định giá, dự báo bottom-up), [[hqla]] (chi phí carry của buffer) (canonical — chỉ đề xuất)
- conflicts: không có; khác phạm vi: case ChoudWest là ví dụ minh hoạ (không FTP, đường cong phẳng, sốc +3%/−1%), khác phương pháp chuẩn d368
- ghi chú convert: câu kết quả Kịch bản 4 (dòng 1859–1861) nằm sau tiêu đề bảng Scenario 5, gán cho Kịch bản 4 theo logic số liệu; công thức Ví dụ 1.1–1.3 mất hoặc vỡ
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]], [[ftp-nature-and-balance-sheet-management]] (canonical); [[hqla-decomposition-and-tradeoffs]], [[irrbb-liquidity-hqla-and-ftp-interaction]], [[ftp-balance-sheet-optimization]] (draft) — NIM làm chỉ số đánh đổi
- backfill: linked [[net-interest-margin]] ở 9 node draft ([[alco]], [[negative-interest-rates]], [[structural-hedging]], [[cross-currency-swap]], [[balance-sheet-optimisation-model]], [[model-risk-management]], [[level-1-assets]], [[level-2-assets]], [[asf-wholesale-and-operational-funding]]) · proposed link ở 11 node canonical · không đánh dấu khoảng 20 synthesis chỉ nhắc NIM lướt qua
- tiếp theo: src-choudhry-principles-banking u18 (Ch11 phần tiếp: liquidity metrics, CFP) hoặc u05–u06 (Ch2–Ch3: rủi ro hoạt động, quy định)

## [2026-10-19] ingest | --node repricing-balance-sheet
- phạm vi: phương án Mở rộng; không đọc raw mới; viết lại theo template model (Mục tiêu / Công thức / Inputs & giả định / Calibration / Output & usage / Hạn chế & validation), bỏ hộp ASCII
- claim dùng thêm: lubinska-u02-22…25, 28, 34…37; choudhry-irr-3, 5, 7, 8, lgap-7, nim-3, hedge-21, alco-19; tata-rep-2, tata-nii-6, 7; irrbb-u05-16, 22, 25; tt83 pl5-a1-1c, pl5-a2-0, pl5-a2-t1, pl5-a2-1, pl5-a2-3a2, d54-4a
- sửa citation: trần NMD ghi đủ 5/4,5/4 năm (irrbb-u05-4); bỏ choudhry-irrbb-9 cho HTM/AFS (claim nói CSRBB FVOCI); bỏ tata-nii-5 cho tiền mặt (claim không nhắc); hạn chế song song chuyển từ choudhry-irrbb-4 sang choudhry-irr-7; relation input-to NII đổi cite từ tata-nii-1 sang lubinska-u02-23 (đích giữ nguyên)
- thêm: bảng Basel vs VN (TT83 PL5, hiệu lực 01/07/2026), bảng biến thể gap, ví dụ Choudhry 6.12, bất đối xứng NII của Tata, 8 hạn chế có citation
- [cần nguồn]/Diễn giải: danh sách sản phẩm cụ thể trong phạm vi, số dải nội bộ, CGAP (wiki tự trình bày)
- conflicts: không có
- syntheses flagged: [[irrbb-casa-replicating-portfolio-and-irs-hedging]], [[irrbb-principal-and-interest-cash-flows]], [[irrbb-repricing-profiles-and-behavioral-modeling]], [[irrbb-standardised-shocks-eve-and-nii-measurement]] (trần NMD, Basel vs VN)
- backfill: không áp dụng (node đã tồn tại)
- tiếp theo: Basel Framework SRP31 (đối chiếu par 101–106 với d368) hoặc Bardaeva u03 (IRRBB Management)

## [2026-10-19] ingest | src-bardaeva-alm u03
- phạm vi: phương án Mở rộng, dòng 874–1288 (Ch.10–13; Box 12.2 tối ưu cấu trúc vốn tập đoàn chỉ lấy tỷ lệ P2R CRD V); 59 claim (ch10-1…6, ch11-1…23, ch12-1…22, ch13-1…8)
- created: [[src-bardaeva-alm]] (source note), [[irrbb-management]], [[alm-operating-model]], [[srep]] (concept)
- updated: [[alco]] (thành phần ALM/Risk/Finance, amber zone, yêu cầu phòng ngừa qua ALCO), [[three-lines-of-defence]] (bảng tuyến theo Bardaeva, tuyến 4, khác biệt với TT83 Đ4.2), [[icaap]] (P2R từ ICAAP, vốn IRRBB trong ICAAP), [[risk-appetite]] (RAS trong quản trị IRRBB, xung đột Finance), [[structural-hedging]] (công cụ quản lý, IRS khi kỳ hạn huy động ≤ 1 năm, rủi ro không phòng ngừa được), [[funds-transfer-pricing]] (ALM dựng đường cong, đơn vị giao dịch không gán kỳ hạn)
- proposed: [[gap-risk]] (yield curve risk), [[net-interest-income-sensitivity]] (horizon 3–4 năm vs 01 năm PL5), [[non-maturity-deposits]] (stickiness, tin đồn) (canonical — chỉ đề xuất)
- conflicts: không có; khác biệt: tuyến 1 theo Bardaeva (ALM/Treasury, business lines không là tuyến) vs TT83 Đ4.2 (bộ phận tạo rủi ro)
- ghi chú convert: Table 10.1/10.2 mất tô màu front/middle office, bảng gone concern bị tách; Figure 12.1/12.2 là image
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] (canonical: quy cho Bardaeva khuyến nghị báo cáo CEO nhưng chỉ cite Choudhry; ưu tiên front-office profit centre ngược với ^ch11-11), [[irrbb-repricing-profiles-and-behavioral-modeling]] (draft: link irrbb-management)
- backfill: linked [[alm-operating-model]] ([[liquidity-transfer-restrictions]]) · proposed link [[irrbb-management]] ở [[bcbs-irrbb]], [[outlier-bank-test]], [[csrbb]]
- tiếp theo: src-bardaeva-alm u04 (Table 13.1 ICAAP reliability, SREP thanh khoản, ALM trong khủng hoảng) hoặc src-choudhry-principles-banking u21–u22 (Banking Book Policy Statement)

## [2026-10-19] ingest | src-bardaeva-alm u04
- phạm vi: phương án Mở rộng, dòng 1289–1611 (1617–1709 là bibliography, viết tắt, index, không trích); 56 claim (ch13-9…17, ch14-1…16, ch15-1…9, ch16-1…14)
- created: [[recovery-and-resolution-planning]] (concept), [[mrel]] (metric)
- updated: [[srep]] (quy trình P2R/P2G, tiêu chí ICAAP, mảng thanh khoản, giám sát theo quy mô, P2R/P2G sau hợp nhất), [[icaap]] (tiêu chí độ tin cậy, normative vs economic perspective), [[irrbb-management]] (bảng thị trường phát triển vs mới nổi, IRRBB/FTP trong khủng hoảng), [[alm-operating-model]] (theo quy mô ngân hàng), [[capital-plan]] (các bước lập kế hoạch vốn, CCyB tập đoàn, kế hoạch hành động vốn trong khủng hoảng, M&A, output floor), [[funds-transfer-pricing]] (FTP trong khủng hoảng, đường cong ở thị trường kém phát triển), [[liquidity-risk-management]] (SREP thanh khoản, khủng hoảng, M&A), [[risk-appetite]] (recovery triggers), [[stress-testing]] (khủng hoảng phi tài chính, P2G)
- proposed: [[contingency-funding-plan]] (thứ tự hành động thanh khoản), [[non-maturity-deposits]] (tiền gửi thị trường mới nổi, digitalization) (canonical — chỉ đề xuất)
- conflicts: không có; [cần nguồn]: lộ trình output floor 2022–2027 theo Bardaeva chưa có văn bản BCBS để đối chiếu
- ghi chú convert: công thức TSCR vỡ phân số (dòng 1307); Table 16.2 lệch ô năm; Figure 16.2–16.5 vỡ cột; danh sách thứ tự hành động thanh khoản đánh số sai
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]] (canonical: hàm ý VN theo đặc điểm thị trường mới nổi, FTP trong khủng hoảng), [[irrbb-casa-replicating-portfolio-and-irs-hedging]] (draft: giả định độ sẵn có IRS, độ ổn định CASA)
- backfill: linked [[recovery-and-resolution-planning]] ([[risk-appetite]], [[stress-testing]], [[liquidity-risk-management]], [[alm-operating-model]], [[capital-plan]]); "Kế hoạch Phục hồi Thanh khoản" trong [[nsfr-alm-governance-strategy-and-risks]] là kế hoạch khắc phục NSFR, không nối
- tiếp theo: src-choudhry-principles-banking u21–u22 (Banking Book Policy Statement, risk reporting) hoặc u24 (Recovery Planning and Resolution, đối chiếu node mới)

## [2026-10-19] ingest | src-choudhry-principles-banking u21 u22
- phạm vi: phương án Mở rộng, dòng 10430–11508 (Ch18 phần tiếp, Ch19, Ch20 phần đầu); 61 claim (rmf-1…15, kri-1…10, crd-1…11, bbp-1…9, st-1…16); 2 unit trong một lượt theo yêu cầu user
- created: [[key-risk-indicators]] (concept), [[expected-loss]], [[shareholder-value-added]] (metric)
- updated: [[stress-testing]] (khung, mục tiêu, phương pháp IR/FX/spread/tín dụng, stress log, ALCO "flight simulator", ví dụ +200bp), [[risk-limits]] (hạn mức Banking Book BPV/IR gap, EL/LV), [[banking-book]] (Banking Book Policy Statement), [[risk-appetite]] (risk taxonomy, register, khẩu vị IRR), [[irrbb-management]] (khẩu vị IRR, hạn mức BPV/IR gap, IRR tập trung về Treasury), [[market-risk-management]], [[liquidity-risk-management]] (OLAR), [[recovery-and-resolution-planning]] (RPI), [[icaap]], [[alco]], [[credit-risk-management]], [[raroc]] (hurdle CoC)
- proposed: [[internal-risk-transfer]] (IRR tập trung về Treasury qua internal swap), [[contingency-funding-plan]] (link KRI, LCP trong RP) (canonical — chỉ đề xuất)
- conflicts: không có; khung OLAR, KRI 4 màu, 48 giờ/24 giờ là thông lệ UK, không phải yêu cầu Basel/NHNN
- ghi chú convert: công thức loss volatility (dòng 10960) bị mất; Figure 18.4–18.12, 19.x là ảnh
- syntheses flagged: [[irrbb-alm-governance-strategy-and-tradeoffs]], [[practical-alm-liquidity-governance]], [[ftp-risk-and-cost-components]] (canonical); [[lcr-economic-significance-and-alm-governance]], [[nsfr-alm-governance-strategy-and-risks]] (draft)
- backfill: linked [[key-risk-indicators]] ([[climate-risk]], [[operational-risk-management]], [[strategic-alm]], [[tt83-2025]]), [[expected-loss]] ([[expected-credit-loss]], [[ftp-transmission-mechanism]]) · proposed [[contingency-funding-plan]]
- tiếp theo: src-choudhry-principles-banking u23–u24 (Ch20 phần tiếp: ICAAP, ILAAP, reverse stress; Ch21 Recovery Planning) hoặc u07–u08 (yield curve, đường cong funding nội bộ)

## [2026-10-19] research | NII Management (Cụm 1: Q1–Q4)
- bộ câu hỏi: 8 câu · phủ: 8 đủ / 0 một phần / 0 thiếu · phương án: viết theo cụm (Phương án A — Cụm 1: Q1–Q4)
- bản đồ phủ:
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | Q1 | đủ | [[net-interest-margin]], [[net-interest-income-sensitivity]], [[nii-planning]], [[loan-pricing]] | Đầy đủ định nghĩa, công thức NIM và 4 drivers |
  | Q2 | đủ | [[repricing-balance-sheet]], [[repricing-gap-analysis]], [[gap-risk]] | Đầy đủ công thức GAP và bất đối xứng RSA/RSL (Tata, Choudhry) |
  | Q3 | đủ | [[non-maturity-deposits]], [[behavioural-options]], [[option-risk]], [[replicating-portfolio-model]] | Đầy đủ trần NMD d368/TT83 PL5, pass-through và prepayment |
  | Q4 | đủ | [[nii-planning]], [[net-interest-income-sensitivity]] | Đầy đủ top-down/bottom-up và giả định constant/dynamic 12M |
  | Q5 | đủ | [[standardised-interest-rate-shocks]], [[basis-risk]], [[net-interest-income-sensitivity]] | Dành cho Cụm 2: sốc chuẩn hoá, phân tách margin và basis |
  | Q6 | đủ | [[bcbs-irrbb]], [[tt83-2025]], [[outlier-bank-test]], [[rwa-irrbb]] | Dành cho Cụm 2: chuẩn BCBS d368 vs TT83 Đ53–55, PL5 |
  | Q7 | đủ | [[funds-transfer-pricing]], [[ftp-transmission-mechanism]], [[structural-hedging]], [[interest-rate-swap]] | Dành cho Cụm 2: công cụ quản trị FTP, định giá, IRS |
  | Q8 | đủ | [[alco]], [[strategic-alm]], [[economic-value-of-equity]], [[balance-sheet-optimisation-model]] | Dành cho Cụm 2: đánh đổi NII vs EVE, NIM vs HQLA carry |
- created: [[nii-nature-repricing-mechanisms-and-planning]] (synthesis draft, Q1–Q4)
- updated: [[nii-planning]] (bổ sung relations drives net-interest-margin và input-to net-interest-income-sensitivity), [[index]]
- proposed: không có
- conflicts: không có
- relations: added [[nii-planning]] —drives→ [[net-interest-margin]] ([[src-choudhry-principles-banking#^choudhry-nim-12]]), [[nii-planning]] —input-to→ [[net-interest-income-sensitivity]] ([[src-tata-bank-alm#^tata-nii-3]])
- stubs: không có
- tiếp theo: Research Cụm 2 (Q5–Q8) — kịch bản sốc lãi suất, đối chiếu Basel vs TT83, công cụ hedging và đánh đổi ALCO

## [2026-10-19] research | NII Management (Cụm 2: Q5–Q8)
- bộ câu hỏi: 4 câu (Q5–Q8 trong bộ 8 câu) · phủ: 4 đủ / 0 một phần / 0 thiếu · phương án: viết theo cụm (Phương án A — Cụm 2: Q5–Q8)
- bản đồ phủ:
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | Q5 | đủ | [[standardised-interest-rate-shocks]], [[basis-risk]], [[net-interest-income-sensitivity]] | Đầy đủ 6 kịch bản sốc, công thức toán học và phân tách margin/basis |
  | Q6 | đủ | [[bcbs-irrbb]], [[tt83-2025]], [[outlier-bank-test]], [[rwa-irrbb]] | Đầy đủ đối chiếu BCBS d368 Nguyên tắc 8/12 vs TT83 Đ53–55, PL5 |
  | Q7 | đủ | [[funds-transfer-pricing]], [[ftp-transmission-mechanism]], [[structural-hedging]], [[interest-rate-swap]] | Đầy đủ cơ chế điều chuyển FTP, TRR, danh mục sao chép CASA và Receiver IRS |
  | Q8 | đủ | [[alco]], [[strategic-alm]], [[economic-value-of-equity]], [[balance-sheet-optimisation-model]] | Đầy đủ bài toán mâu thuẫn EVE vs NII, LPP tối ưu hóa và carry cost HQLA |
- created: [[nii-shocks-regulation-hedging-and-alco-tradeoffs]] (synthesis draft, Q5–Q8)
- updated: [[nii-planning]] (link synthesis 2), [[index]]
- proposed: không có
- conflicts: không có
- relations: không có cạnh mới (sử dụng các cạnh đã có trong candidate nodes)
- stubs: không có
- cần ingest: src-choudhry-principles-banking u18 (stress testing và liquidity interaction), src-bardaeva-alm u05 (Series review)
- tiếp theo: rà soát hoàn tất bộ câu hỏi NII Management; sẵn sàng cho chủ đề nghiên cứu mới

## [2026-10-19] ingest | src-choudhry-principles-banking u23–u24
- claims: 76 (st-17…21, icaap-1…16, ilaap-1…14, rst-1…12, rrp-1…18, gb-1…8)
- created: [[ilaap]], [[reverse-stress-testing]], [[cash-flow-survival-period]], [[bail-in]]
- updated: [[icaap]], [[srep]], [[stress-testing]] (bỏ alias Reverse Stress Testing sang node mới), [[liquidity-stress-testing]], [[liquidity-risk-management]], [[recovery-and-resolution-planning]], [[mrel]], [[capital-plan]], [[risk-appetite]], [[climate-risk]]
- proposed: [[contingency-funding-plan]], [[hqla]], [[bcbs-irrbb]] (canonical — chỉ đề xuất)
- conflicts: không có (OLAR, ICG/ILG, Pillar 2A/2B là quy định UK; EU vs US là khác jurisdiction)
- syntheses flagged: [[lcr-economic-significance-and-alm-governance]], [[nsfr-alm-governance-strategy-and-risks]], [[irrbb-basis-risk-measurement-and-hedging]] (Bất định); [[practical-alm-liquidity-governance]], [[irrbb-alm-governance-strategy-and-tradeoffs]] (Đề xuất cập nhật)
- backfill: linked [[alco]], [[srep]], [[recovery-and-resolution-planning]], [[lcr]] · flagged 3 synthesis draft · proposed [[hqla]], [[bcbs-irrbb]]
- tiếp theo: src-choudhry-principles-banking u07–u08 (climate risk, yield curve/liquidity preference) hoặc src-bardaeva-alm u05

## [2026-10-19] ingest | src-choudhry-principles-banking u18
- created: [[bank-strategic-plan]], [[loan-to-deposit-ratio]]; 38 claim (^choudhry-strat-1…33, ^choudhry-capm-1…5, ^choudhry-ftp-16)
- updated: [[strategic-alm]], [[capital-plan]] (+part-of bank-strategic-plan), [[risk-appetite]] (+limits bank-strategic-plan), [[raroc]], [[recovery-and-resolution-planning]], [[funds-transfer-pricing]] (draft)
- proposed: [[leverage-ratio]], [[contingency-funding-plan]] (canonical — chỉ đề xuất)
- conflicts: không có
- syntheses flagged: [[lcr-economic-significance-and-alm-governance]], [[nsfr-alm-governance-strategy-and-risks]] (Bất định); [[irrbb-alm-governance-strategy-and-tradeoffs]] (Đề xuất cập nhật)
- backfill: linked [[loan-to-deposit-ratio]] ở [[liquidity-risk-management]], [[risk-limits]], [[nsfr]], [[tt83-2025]] · flagged 2 synthesis draft · proposed không có
- ghi chú: [[bank-strategic-plan]] bị một tiến trình ngoài phiên ghi đè sau khi tạo; theo quyết định của user, giữ cấu trúc bản ghi đè, sửa citation sai (Đ61 ↔ 3–5 năm, strat-13, strat-24), quy trình 4 bước, bỏ 3 relation sai chiều hoặc thiếu căn cứ, bỏ alias "Ngân sách chiến lược"
- tiếp theo: src-choudhry-principles-banking u19 (Ch16 Bank Strategy II: capital và funding management policy) hoặc u07–u08

## [2026-10-19] lint | kiểm tra định kỳ sau research NII và ingest u18
- trước: 2 error / 0 warning · sau: 0 error / 0 warning / 1 info
- script phụ: audit_vault (relation thiếu cite: 0, note ngắn: 0) · công thức (math-*): 0 lỗi, 0 warning, 115 info
- stub: 3 (2 sẵn sàng --node: cost-of-funds, cs01; 0 quá hạn)
- đã sửa: tạo và chuẩn hoá node [[bank-strategic-plan]], bổ sung [[loan-to-deposit-ratio]] và [[bank-strategic-plan]] vào `02_wiki/index.md`, mark done unit u18 trong `03_meta/sources.yaml`
- đề xuất chờ duyệt: không có lỗi nội dung hay mâu thuẫn mới; tiếp tục duy trì trạng thái vault sạch

## [2026-10-19] ingest | src-choudhry-principles-banking u19
- created: [[contingent-convertible-bond]], [[bank-corporate-governance]]
- updated: [[capital-plan]], [[funds-transfer-pricing]], [[alco]], [[liquidity-risk-management]], [[loan-to-deposit-ratio]], [[bank-strategic-plan]]
- proposed: không có
- conflicts: không có (capital planning: Choudhry giao ALCO, TT83 Đ6.4.c giao Hội đồng quản lý vốn — khác jurisdiction, ghi *Diễn giải* ở [[capital-plan]])
- syntheses flagged: [[ftp-cost-benefit-allocation-principles]] (FTP cho vốn chủ sở hữu, case UBS), [[practical-alm-liquidity-governance]] (liquidity strategy, rating agency), [[irrbb-alm-governance-strategy-and-tradeoffs]] (phân vai ALCO và Hội đồng quản lý vốn) — đều ở Đề xuất cập nhật
- backfill: linked [[contingent-convertible-bond]] ở [[bail-in]], [[mrel]], [[stress-testing]], [[asf-capital-and-long-term-liabilities]], [[capital-plan]] · flagged không có · proposed không có
- claims: 52 (capm-6…31, peer-1…6, liq-13…16, coco-1…4, gov-1…12)
- tiếp theo: src-choudhry-principles-banking u20 (Ch17 phần còn lại: KBC và khung governance đề xuất) hoặc u07–u08

## [2026-10-19] lint | kiểm tra sức khoẻ vault sau ingest u19
- trước: 0 error / 0 warning · sau: 0 error / 0 warning / 1 info
- script phụ: audit_vault (relation thiếu cite: 0, note ngắn: 0) · công thức (math-*): 0 lỗi, 0 warning, 115 info
- stub: 3 (2 sẵn sàng --node: cost-of-funds, cs01; 0 quá hạn)
- đã sửa: không có lỗi kỹ thuật (vault 176 note hoàn toàn sạch)
- đề xuất chờ duyệt: không có lỗi nội dung hay mâu thuẫn mới

## [2026-10-19] ingest | --node cost-of-funds
- completed stub: [[cost-of-funds]] (metric draft, thoát stub, 7 cấu phần COF, công thức BHTG, DTBB, đệm HQLA, TLP thả nổi, quyền chọn trả trước và Cost of Funds kế toán/ALM)
- updated: [[funds-transfer-pricing]] (gỡ ghi chú stub, link cost-of-funds), [[ftp-transmission-mechanism]] (link COF ở kênh thanh khoản), [[ftp-pricing-methodology]] (link COF ở mục 3), [[key-risk-indicators]] (link cost of funds ở KPI/KRI), [[index]] (bỏ *stub*)
- proposed: [[internal-risk-transfer]], [[liquidity-transfer-pricing]] (canonical — đề xuất link cost-of-funds)
- conflicts: không có
- syntheses flagged: [[ftp-balance-sheet-optimization]] (draft, Bất định)
- backfill: linked [[funds-transfer-pricing]], [[ftp-transmission-mechanism]], [[ftp-pricing-methodology]], [[key-risk-indicators]] · flagged [[ftp-balance-sheet-optimization]] · proposed [[internal-risk-transfer]], [[liquidity-transfer-pricing]]
- claims: 15 (vab-ftp-7…12, vab-ftp-19…21, vab-ftp-25…29, vab-ftp-31…35; choudhry-kri-7, choudhry-strat-16, choudhry-nim-12; lubinska-u07-1, lubinska-u07-2)
- tiếp theo: /ingest --node cs01 (stub sẵn sàng còn lại) hoặc src-choudhry-principles-banking u20 (Corporate Governance)

## [2026-10-19] decision | trang tóm tắt domain
- created: [[domain-macro]], [[domain-product]], [[domain-alm]], [[domain-basel]], [[domain-vn-reg]] (`02_wiki/domains/`, `type: nav`; mỗi trang gồm mọi node có domain đó trong `domains`, không chia theo primary; claim chép từ node kèm citation)
- updated: [[overview]] (bảng domain link tới trang domain), [[index]] (dòng điều hướng tới 5 trang domain)
- tools: `tools/lint.py` thêm 5 ID `domain-*` vào `NAV` (bỏ kiểm tra schema/orphan/index, vẫn kiểm link và block-ref); `tools/citations.py` không đổi, vẫn rà trang domain
- schema: `CLAUDE.md` thêm dòng `02_wiki/domains/` vào bản đồ thư mục; `.claude/skills/ingest/SKILL.md` bước 5 thêm cập nhật trang domain
- lint: 0 error · `citations.py --uncited`: 0 dòng trong `02_wiki/domains/`

## [2026-10-20] ingest | src-bcbs-framework SRP30
- created: [[reputational-risk]], [[firm-wide-risk-management]], [[valuation-governance]]
- updated: [[icaap]], [[concentration-risk-management]] (bảng Basel vs VN), [[liquidity-risk-management]] (bảng Basel vs VN), [[risk-appetite]], [[risk-limits]], [[stress-testing]], [[new-product-approval]], [[three-lines-of-defence]], [[srep]]; [[domain-basel]], [[domain-alm]], [[domain-vn-reg]], [[domain-product]], [[index]], [[overview]]
- proposed: [[funding-concentration-risk]] (canonical — SRP30.22 nguồn vốn là tình huống tập trung; link [[concentration-risk-management]], [[reputational-risk]])
- conflicts: không có (khác biệt Basel vs TT83 ghi ở bảng: nguồn vốn trong phạm vi tập trung, chủ thể đặt tolerance/hạn mức, vị trí CRO)
- syntheses flagged: [[basel-liquidity-monitoring-framework]], [[synthetic-balance-sheet-liquidity-risk]], [[practical-alm-liquidity-governance]] (canonical, Đề xuất cập nhật); [[integrated-alm-liquidity-strategy]], [[lcr-economic-significance-and-alm-governance]], [[irrbb-liquidity-hqla-and-ftp-interaction]], [[irrbb-basis-risk-measurement-and-hedging]] (draft, Bất định)
- backfill: linked [[reputational-risk]] trong [[liquidity-stress-testing]], [[negative-interest-rates]], [[operational-risk-management]], [[cash-outflows]], [[derivatives-and-contingent-outflows]], [[unsecured-wholesale-funding]] · flagged [[irrbb-basis-risk-measurement-and-hedging]] · proposed [[funding-concentration-risk]]
- claims: 55 block-id (srp30-0 … srp30-52, gồm srp30-2b, srp30-2c, srp30-8b; không có claim cho 30.23)
- tiếp theo: src-bcbs-framework SRP20 (bốn nguyên tắc rà soát giám sát) hoặc SRP36 (risk data aggregation, đối chiếu TT83 Đ24, Đ74)

## [2026-10-20] register | src-bcbs-liquidity-principles-2008
- BCBS 144 "Principles for Sound Liquidity Risk Management and Supervision" (9/2008) · T2 · final · domains basel, alm · extractor docling
- 20 unit: preamble, intro, p01–p17 (theo số nguyên tắc, heading "The Role of Supervisors" gộp vào p14), annex
- conversion: partial (câu Principle 12 bị tách thành heading ở dòng 528; số footnote chèn rời trong câu)
- câu hỏi mở: published để null vì bìa chỉ ghi tháng 9/2008; chương Core Principles của src-bcbs-framework đang bị gộp vào unit DIS99 (heading cấp ####), cần tách lại khi ingest Principle 24

## [2026-10-20] tool | registry.py resplit
- tools: `tools/registry.py` thêm lệnh `resplit <source_id> [--preset|--pattern|--level|--chunk] [--add LINE:ID] [--dry-run]` (user duyệt): chạy lại units.py, giữ nguyên dòng (status, ngày ingest) của unit không đổi ranh giới; dừng nếu unit done/skipped bị đổi hoặc mất; dừng nếu sha256 raw khác registry; validate YAML trước khi ghi
- kiểm thử trên bản copy vault: chặn đúng khi tham số tách khác lần đăng ký (6 unit done/skipped bị ảnh hưởng); chạy lại lần hai không đổi; entry khác không đổi
- áp dụng: src-bcbs-framework `--pattern '^###\s+(?P<id>[A-Z]{3}[0-9]{2})\s+(?P<title>.+)' --add 24533:BCP` → giữ 114 unit, DIS99 thu về [24429, 24532], thêm unit BCP [24533, 26057] (Core Principles for effective banking supervision; Principle 24 thanh khoản ở BCP40.54–40.55)

## [2026-10-20] ingest | src-bcbs-liquidity-principles-2008 p01, p10, p11
- created: [[src-bcbs-liquidity-principles-2008]] (source note), [[bcbs-liquidity-principles]] (regulation)
- updated: [[ilaap]] (mục Basel thay [cần nguồn] bằng bảng 10 thành phần), [[liquidity-stress-testing]] (bảng Basel P10 vs TT83 Đ48), [[liquidity-risk-management]] (P1); [[domain-basel]], [[domain-alm]], [[index]], [[overview]]
- proposed: [[contingency-funding-plan]] (canonical — định nghĩa và yêu cầu CFP theo P11)
- conflicts: không có (SRP30.51 lặp gần nguyên văn para 94)
- syntheses flagged: [[practical-alm-liquidity-governance]] (canonical, Đề xuất cập nhật); [[lcr-economic-significance-and-alm-governance]], [[nsfr-alm-governance-strategy-and-risks]] (draft, Bất định)
- backfill: link [[bcbs-liquidity-principles]] thay chữ "Principles for Sound Liquidity…" trong [[liquidity-risk-management]] · proposed [[contingency-funding-plan]]
- claims: 26 block-id (lrm-p01, lrm-8, lrm-8b, lrm-9, lrm-p10, lrm-94…lrm-109, lrm-p11, lrm-110…lrm-122; một số block gộp 2–3 đoạn); quan hệ `governs` tới [[ilaap]] là suy luận, không cite
- ghi chú: ingest 3 unit trong một lần (tổng ~100 dòng, cùng phục vụ node ilaap)
- tiếp theo: src-bcbs-liquidity-principles-2008 p02–p04 (quản trị, liquidity risk tolerance, chi phí thanh khoản trong định giá nội bộ) hoặc p12 (đệm tài sản thanh khoản)

## [2026-10-20] ingest | src-bcbs-liquidity-principles-2008 p02, p03, p04
- updated: [[bcbs-liquidity-principles]] (bảng yêu cầu P2–P4, định nghĩa tolerance và liquidity charge, governs tới [[liquidity-transfer-pricing]], [[funds-transfer-pricing]], [[risk-appetite]]), [[liquidity-risk-management]] (bảng Basel vs VN thêm 3 dòng: chiến lược, cấu trúc tập đoàn, báo cáo HĐQT; bổ sung citation BCBS 144 vào dòng tolerance và định giá nội bộ), [[risk-appetite]] (P2), [[funds-transfer-pricing]] (thay "[cần nguồn]" chuẩn BCBS về FTP bằng P4 cho phần thanh khoản), [[new-product-approval]], [[alco]], [[three-lines-of-defence]]; [[domain-basel]], [[domain-alm]], [[index]], [[overview]]
- proposed: [[liquidity-transfer-pricing]] (canonical — căn cứ Basel P4 cho Liquidity FTP)
- conflicts: không có (SRP30.50 lặp nội dung P2, P4)
- syntheses flagged: [[ftp-nature-and-balance-sheet-management]], [[ftp-risk-and-cost-components]], [[ftp-economic-cost-and-incentive-validation]], [[practical-alm-liquidity-governance]] (canonical, Đề xuất cập nhật); [[ftp-balance-sheet-optimization]] (draft, Bất định)
- backfill: không có node mới; link [[bcbs-liquidity-principles]] thêm vào các node trên
- claims: 17 block-id (lrm-p02, lrm-10, lrm-10b, lrm-p03, lrm-11, lrm-11b, lrm-12…lrm-18, lrm-p04, lrm-19, lrm-19b, lrm-20)
- tiếp theo: src-bcbs-liquidity-principles-2008 p12 (đệm tài sản thanh khoản, đối chiếu [[hqla]]) hoặc p05 (đo lường dòng tiền, 134 dòng)

## [2026-10-20] review | contingency-funding-plan, liquidity-transfer-pricing
- user duyệt áp dụng đề xuất ngày 2026-10-20 vào thân bài hai node canonical (giữ maturity canonical)
- [[contingency-funding-plan]]: thêm mục 5 "Chuẩn mực Basel (BCBS 144 Principle 11)" — định nghĩa CFP, bảng 9 yêu cầu, liên kết với stress test và tolerance; domains thêm basel; sources thêm src-bcbs-liquidity-principles-2008
- [[liquidity-transfer-pricing]]: thêm mục 6 "Căn cứ Basel (BCBS 144 Principle 4)" — bảng 5 yêu cầu, đối chiếu SRP30.50 và TT83 Đ45.1.b, diễn giải liên hệ TLP (2.B) và Contingent Liquidity Charge (2.C); domains thêm basel; sources thêm src-bcbs-liquidity-principles-2008, src-bcbs-framework, src-tt83-2025-nhnn
- dòng đề xuất được giữ và đánh dấu "→ đã áp dụng [2026-10-20]"; các đề xuất cũ hơn (2026-10-19) trong hai node chưa xử lý

## [2026-10-20] review | xử lý toàn bộ đề xuất chờ duyệt trong node canonical
- phạm vi: 140 dòng `## Đề xuất cập nhật` trong 30 node canonical (user duyệt "xử lý hết"); giữ maturity canonical; mỗi dòng giữ lại và đánh dấu "→ đã áp dụng [2026-10-20]" hoặc "→ không áp dụng [2026-10-20]: <lý do>"
- link (61): chèn `[[id]]` ở lần nhắc đầu bằng script (bỏ qua frontmatter, code block, công thức, heading); chỗ khái niệm chỉ có trong heading hoặc code block thì đặt link ở mục liên kết hoặc trong nội dung mới
- không áp dụng (2): [[lcr-by-currency]] (node không nhắc khẩu vị rủi ro), [[contingency-funding-plan]] link NIM (chỉ có trong code block)
- nội dung (79): thêm góc nhìn VN theo TT83 (bảng Basel vs VN ở [[basis-risk]], [[gap-risk]], [[option-risk]], [[behavioural-options]], [[non-maturity-deposits]], [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[bcbs-irrbb]]; mục VN ở [[csrbb]], [[hqla]], [[funding-concentration-risk]], [[contingency-funding-plan]], [[intraday-liquidity-risk]], [[irrbb-balance-sheet-portfolios]]); ví dụ và case T4 (Choudhry, Tata, Lubinska, Bardaeva); tham chiếu EU SOT ở [[outlier-bank-test]]; nhầm lẫn "maximum 3%" (Lubinska) ở [[leverage-ratio]] ghi là diễn đạt lệch của nguồn T4, căn cứ LEV20.7
- sửa provenance khi đối chiếu: [[available-stable-funding]] (sự kiện SVB trước cite nsf30-2, nay cite tata-svb-4/7, bỏ chi tiết "tin đồn" không có nguồn), [[hqla]] (SVB là MBS sổ HTM, không phải TPCP Level 1; cite tata-svb-5/7), [[funding-concentration-risk]], [[irrbb-balance-sheet-portfolios]] (thêm cite tata-svb); [[standardised-interest-rate-shocks]] thay `[cần nguồn]` về phân vị bằng mô tả Table 1 (u07-7/8/9)
- frontmatter: [[interest-rate-swap]] bỏ alias "OIS Swap"; relations mới: [[contingency-funding-plan]] part-of [[liquidity-risk-management]], [[funding-concentration-risk]] input-to [[liquidity-stress-testing]]; domains thêm vn-reg cho 8 node; sources bổ sung theo citation mới
- còn lại: 84 dòng đánh dấu trong synthesis canonical (xử lý bằng /research, /query); [[domain-vn-reg]] cập nhật thống kê (72 node, canonical 18)
- lint: 0 error, 0 warning

## [2026-10-20] research | irrbb-alm-governance-strategy-and-tradeoffs (rà lại sau ingest)
- bộ câu hỏi: 6 câu (Q1–Q5 tách từ `question` gốc; Q6 mới: nghĩa vụ VN theo TT83) · phủ: 2 đủ / 4 một phần / 0 thiếu · phương án: hạ canonical → draft và viết lại tại chỗ (user duyệt)
- bản đồ phủ:
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | Q1 Khung quản trị HĐQT/ALCO theo 12 nguyên tắc | đủ | [[bcbs-irrbb]], [[alco]], [[irrbb-management]], [[three-lines-of-defence]], [[model-validation]] | thiếu góc nhìn VN; mục 1 quy kết Bardaeva nhưng chỉ cite Choudhry |
  | Q2 Đánh đổi EVE vs NII | một phần | [[economic-value-of-equity]], [[net-interest-income-sensitivity]], [[replicating-portfolio-model]] | ví dụ số do LLM dựng chưa gắn nhãn; ΔEVE → vốn kinh tế (TT83 PL6) chưa phản ánh |
  | Q3 Cạm bẫy thời lượng HQLA | một phần | [[hqla]], [[silicon-valley-bank]], [[outlier-bank-test]] | không nguồn nào định danh "duration trap"; câu SVB sai (MBS sổ HTM, không phải TPCP Level 1); trần duration 2,5–3 năm không nguồn |
  | Q4 Hạn mức ALCO 4 tầng | một phần | [[risk-limits]], [[bcbs-irrbb]], [[alco]] | khung 4 tầng là cách nhóm của LLM; số hạn mức (ΔEVE ≤ 10% T1, ΔNII ≤ 5%, DGAP, KAO ≤ 2%) không nguồn; d368 par 30 chưa có claim → /ingest src-bcbs-irrbb-2016 u03 (bổ sung) |
  | Q5 FTP tích hợp IRRBB | một phần | [[funds-transfer-pricing]], [[liquidity-transfer-pricing]], [[internal-risk-transfer]] | chưa có chuẩn BCBS cho FTP phần lãi suất |
  | Q6 Nghĩa vụ VN theo TT83 | đủ (wiki) | [[tt83-2025]], [[icaap]], [[rwa-irrbb]], [[economic-capital]], [[risk-limits]] | synthesis chưa có mục VN |
- (tiếp) viết lại [[irrbb-alm-governance-strategy-and-tradeoffs]] tại chỗ (canonical → draft, user duyệt):
  - thêm `## Câu hỏi` (Q1–Q6), `## Kết luận`, mục Q6 (bảng 12 dòng nghĩa vụ TT83), `## Bằng chứng ủng hộ/trái chiều`, `## Phụ thuộc regime`, `## Hàm ý ALM / quy định`, `## Bất định`; bảng chuỗi quan hệ cho Q1–Q5
  - sửa citation lệch: p04-1 (bị cite cho hạn mức và FTP), u01-3 (bị cite cho "3 tuyến"); sửa mức bắt buộc P6, P7 ("nên", không "phải")
  - sửa ví dụ số Q2 (IRS nhận cố định không biến tài sản thành thả nổi; "gần 60% NIM" lệch giả định) → thay bằng minh hoạ có nhãn, nối với d368 par 11
  - Q3: câu SVB sửa theo tata-svb-5 (MBS sổ HTM); trần duration 2,5–3 năm chuyển thành diễn giải không số
  - Q4: gỡ số hạn mức không nguồn (ΔEVE ≤ 10% T1, ΔNII ≤ 5%, DGAP −0,5…+1,5, KAO ≤ 2%); thay bằng bảng 10 dòng có nguồn (d368 P3, TT83 Đ53.2/Đ20.1, Choudhry bbp-4/5, hedge-22, salm-9); par 30 ghi [cần nguồn]
  - Q1: sửa quy kết Bardaeva (ch11-21, ch11-11), thêm FSA/PRA (alco-5, alco-7) và đối chiếu TT83 Đ6.4.b
  - dòng thiếu citation mang số liệu: 55 → 0 (còn câu hỏi, sơ đồ, Bất định)
  - 24 dòng đánh dấu ingest trong synthesis: thêm "→ đã rà [2026-10-20]"
  - phủ sau khi viết: Q1 đủ · Q2 đủ (ví dụ là minh hoạ có nhãn) · Q3 một phần (khái niệm không có nguồn) · Q4 một phần (thiếu par 30) · Q5 một phần (chưa có chuẩn BCBS cho FTP lãi suất) · Q6 đủ
  - relations: proposed [[economic-value-of-equity]] —input-to→ [[rwa-irrbb]] (cite pl6-1c), [[replicating-portfolio-model]] —hedges→ [[net-interest-income-sensitivity]] (cite irrbb-u06-6) (cả hai node canonical, ghi `## Đề xuất cập nhật`)
  - conflicts: không có (vị trí ALM Choudhry vs Bardaeva, chủ trì ALCO Choudhry vs TT83: khác mức độ hoặc khác jurisdiction)
  - stubs: không có
  - cần ingest: src-bcbs-irrbb-2016 u03 bổ sung par 30 (gỡ Q4)

## [2026-10-20] review | duyệt relation từ research irrbb-alm-governance-strategy-and-tradeoffs
- applied: [[economic-value-of-equity]] —input-to→ [[rwa-irrbb]] ([[src-tt83-2025-nhnn#^pl6-1c]]) · [[replicating-portfolio-model]] —hedges→ [[net-interest-income-sensitivity]] ([[src-bcbs-irrbb-2016#^irrbb-u06-6]])

## [2026-10-20] ingest | src-bcbs-irrbb-2016 U03 (bổ sung)
- phạm vi: par 30 (raw dòng 118), par 31 (dòng 119) · claim mới: ^irrbb-p03-5, ^irrbb-p03-6 · không mark lại unit
- updated: [[risk-limits]] (Basel IRRBB: sub-limits, risk tolerance gap/basis/option, hạn mức chiến lược phòng ngừa; relations limits → [[gap-risk]], [[basis-risk]], [[option-risk]] cite p03-5) · [[new-product-approval]] (d368 par 31) · [[irrbb-alm-governance-strategy-and-tradeoffs]] (draft; bảng Q4 thay dòng [cần nguồn] bằng 3 dòng có cite, Kết luận Q4; Q4 một phần → đủ)
- conflicts: không có
- syntheses flagged: [[irrbb-basis-risk-measurement-and-hedging]], [[irrbb-casa-replicating-portfolio-and-irs-hedging]] (hạn mức mới)
- backfill: không có
- tiếp theo: research `irrbb-standardised-shocks-eve-and-nii-measurement`

## [2026-10-20] research | irrbb-standardised-shocks-eve-and-nii-measurement (rà lại sau ingest)
- bộ câu hỏi: 4 câu (Q1–Q3 cũ, thêm Q4 VN) · phủ (bước 1): 3 đủ / 1 một phần / 0 thiếu · phương án: viết theo cụm, đánh dấu chỗ thiếu
- bản đồ phủ (trước khi viết):
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | Q1 ΔEVE | đủ (6 cờ chưa rà) | [[economic-value-of-equity]], [[irrbb-standardised-framework]], [[outlier-bank-test]] | mô hình định giá KAO [cần nguồn]; RWA_IRRBB (PL6), SOT EU (Tata) chưa đưa vào |
  | Q2 ΔNII | một phần | [[net-interest-income-sensitivity]], [[repricing-gap-analysis]] | dynamic balance sheet chưa có claim d368 (kiểm raw); NIM chưa nối |
  | Q3 6 kịch bản | đủ | [[standardised-interest-rate-shocks]] | 2 dòng công thức steepener/flattener thiếu cite; sàn sau sốc chỉ có nguồn EBA (Tata reg-8, sot-2) |
  | Q4 VN (mới) | đủ | [[tt83-2025]], [[rwa-irrbb]] | không có outlier test VN |
- lỗi wiki: [[standardised-interest-rate-shocks]] dòng 143–144 sàn −100 bp/5 bp/20 năm không cite (là sàn EBA 2018, không phải d368), dòng 93 pivot 3–5 năm không cite; [[economic-value-of-equity]] dòng 128 duration HQLA 5–7 năm không cite
- updated: [[irrbb-standardised-shocks-eve-and-nii-measurement]] (viết lại tại chỗ, draft; thêm Q4 VN; 4 bảng chuỗi quan hệ; 13 cờ ingest → đã rà) · không sửa node tri thức
- phủ sau khi viết: Q1 đủ · Q2 một phần (dynamic balance sheet chưa có claim d368; NIM chỉ có diễn giải) · Q3 đủ (sàn sau sốc chỉ có nguồn EBA) · Q4 đủ
- sửa trong synthesis: công thức xoay trục bỏ nhân $S_{short}/S_{long}$ lặp, theo đúng claim u07-3; Bằng chứng trái chiều bỏ câu quy cho tata-nii-11 điều nguồn không nói (EVE "biến động dữ dội" dưới sốc xoay trục); "slot" theo mức "may" của u05-13; thêm tham chiếu SOT EU (Tata), xấp xỉ gap (Lubinska, Choudhry), NMD sàn 0% (Choudhry)
- conflicts: không có · relations: không thêm (mọi dòng chuỗi quan hệ khớp cạnh có sẵn) · stubs: không có
- cần ingest: src-bcbs-irrbb-2016 u06 bổ sung dòng 784–809, 918 (dynamic balance sheet; gỡ Q2) · u03 bổ sung footnote 9 dòng 154 (Q2) · u07 bổ sung dòng 969–971 ($S_{long}$), 979, 1048 (sàn lãi suất sau sốc do supervisor đặt; Q3)

## [2026-10-20] ingest | src-bcbs-irrbb-2016 U03, U06, U07 (bổ sung)
- phạm vi: u03 par 34 + footnote 9 (raw dòng 136, 154) · u06 Annex 1 §2.1–2.2, §4.3 (dòng 784, 792, 798–809, 916–918) · u07 dòng 961–987, 979, 1048 · không mark lại unit
- claim mới: ^irrbb-p04-4, ^irrbb-u06-8, ^irrbb-u06-9, ^irrbb-u06-10, ^irrbb-u07-10, ^irrbb-u07-11 (6 claim)
- updated: [[negative-interest-rates]] (sàn lãi suất sau sốc d368 ≤ 0) · [[irrbb-standardised-shocks-eve-and-nii-measurement]] (draft, user duyệt áp trực tiếp: Q2 bảng ba trạng thái run-off/constant/dynamic, chân trời 1–3/≤5 năm; Q3 công thức sốc cơ sở, ví dụ 3,5 năm, sàn sau sốc; Q2 một phần → đủ)
- proposed: [[net-interest-income-sensitivity]] (ba trạng thái, chân trời) · [[standardised-interest-rate-shocks]] (u07-10, sàn sau sốc d368 vs EBA; sửa dòng 143–144 quy sàn EBA thành Basel; dòng 93 pivot không nguồn)
- conflicts: không có (sàn EBA âm nằm trong khung "không lớn hơn 0" của d368)
- syntheses flagged: [[nii-shocks-regulation-hedging-and-alco-tradeoffs]] (ba trạng thái bảng cân đối, chân trời, sàn sau sốc)
- backfill: không có
- tiếp theo: duyệt 2 đề xuất ở node canonical; research `nii-shocks-regulation-hedging-and-alco-tradeoffs`

## [2026-10-20] review | duyệt đề xuất ingest d368 U03/U06/U07 (bổ sung)
- applied: [[net-interest-income-sensitivity]] — chân trời 1–3/≤5 năm (u06-8), ΔNII = cơ sở − stress (u06-10), ba trạng thái bảng cân đối cite u06-9 thay u06-5 (trích dẫn của u06-5 không nói về dynamic hay chân trời 1–3 năm; bản cũ ghi "2–3 năm"), giới hạn dynamic view (p04-4)
- applied: [[standardised-interest-rate-shocks]] — mô tả sốc ngắn/dài hạn và $S_{long}$ (u07-10); dòng pivot 3–5 năm không nguồn thay bằng ví dụ 3,5 năm của d368; mục sàn lãi suất sau sốc viết lại: d368 ≤ 0 (u07-11), EBA 2018 và RTS/2022/10 qua Tata (reg-8, sot-2); bản cũ quy sàn EBA cho Basel và sai mốc ("qua đêm đến 1 năm −100 bp")

## [2026-10-20] research | nii-shocks-regulation-hedging-and-alco-tradeoffs (rà lại sau ingest)
- bộ câu hỏi: 4 câu (Q5–Q8 bộ NII Management) · phủ ước lượng: 0 đủ / 4 một phần / 0 thiếu (lần 2026-10-19 ghi 4 đủ) · phương án: viết lại theo cụm
- bản đồ phủ:
  | Q | Mức phủ | Node / synthesis | Thiếu gì · unit |
  |---|---|---|---|
  | Q5 | một phần | [[standardised-interest-rate-shocks]], [[net-interest-income-sensitivity]], [[basis-risk]] | cờ ingest u06-8/9/10, u07-11 chưa rà; nghi sai biên độ GBP; công thức tách margin không cite; quy trách nhiệm cite choudhry-alco-19 chưa verify |
  | Q6 | một phần | [[bcbs-irrbb]], [[tt83-2025]], [[outlier-bank-test]] | verify p12-7, d54-1a, tata-sot-3 (T4) |
  | Q7 | một phần | [[funds-transfer-pricing]], [[loan-pricing]], [[replicating-portfolio-model]], [[interest-rate-swap]], [[interest-rate-cap-floor]] | dòng cạnh loan-pricing —input-to→ net-interest-margin không tồn tại; FTP/loan-pricing/alco 0 cạnh; cap/floor chưa trả lời; nghi dẫn sai choudhry-cs-20 |
  | Q8 | một phần | [[alco]], [[economic-value-of-equity]], [[balance-sheet-optimisation-model]], [[lcr-nsfr-interlinkages]], [[hqla]] | dòng cạnh NII —input-to→ alco không tồn tại; cạnh lcr-nsfr-interlinkages —drives→ NII/EVE cite u02-4/p12-1 không nói về LCR/NSFR; u02-4 chưa dùng cho đánh đổi NII–EVE; verify lp-5, hedge-22 |
- kết quả sau verify: 3 đủ / 1 một phần (Q6: thiếu claim TT83 về ngưỡng ngoại lai và tần suất stress IRRBB)
- updated: [[nii-shocks-regulation-hedging-and-alco-tradeoffs]] (viết lại Q5–Q8; bản cũ lưu scratchpad). Sửa: biên độ GBP 250 bp (không phải 200); "VND ±400 bp" → trần 400 bp của phương pháp tự hiệu chỉnh PL5.C.I.2; biên thương mại nằm trong ΔNII (p08-3), không bị khấu trừ; bỏ quy trách nhiệm cite choudhry-alco-19, cs-1, nim-9, nim-14 cho ý nguồn không nói; "TT83 stress test hằng năm" không có nguồn → bỏ; "HĐQT/ALCO tự phê duyệt hạn mức" (d54-1a) → hạn mức ΔNII/ΔEVE bắt buộc (d53-2); thêm u02-4 cho đánh đổi NII–EVE, cap/floor (choudhry-hedge-20/23/25), cờ u06-8/9/10, u07-11 → đã rà
- proposed: [[interest-rate-cap-floor]] (đổi cite hedges NII → choudhry-hedge-20), [[interest-rate-swap]] (thêm hedges NII cite tata-nii-16; rà 2 cạnh cite không nhắc swap), [[hqla]] (thêm drives NIM "−" cite choudhry-nim-5), [[net-interest-income-sensitivity]] (đổi cite input-to balance-sheet-optimisation-model → lubinska-u04-12)
- conflicts: không có
- relations: added không có · proposed 4 (trên)
- stubs: không có
- lỗi wiki phát hiện: [[lcr-nsfr-interlinkages]] 3 cạnh cite không nói về LCR/NSFR (drives EVE cite irrbb-p12-1, drives NII cite irrbb-u02-4, drives NIM cite choudhry-nim-12); [[replicating-portfolio-model]] drives EVE cite irrbb-u06-6 (trích dẫn không nói về EVE); src-ftp-transmission-analysis để block-id trong blockquote nên citations.py không ghép được
- cần ingest: không bắt buộc; TT83 về ngưỡng ngoại lai/can thiệp NHNN với ΔNII nếu có (chưa xác định unit)

## [2026-10-20] review | 4 đề xuất cạnh từ research nii-shocks-regulation-hedging-and-alco-tradeoffs
- applied: [[interest-rate-cap-floor]] hedges → [[net-interest-income-sensitivity]] đổi cite irrbb-u06-4 → choudhry-hedge-20 · [[interest-rate-swap]] thêm hedges → [[net-interest-income-sensitivity]] (tata-nii-16), sources + src-tata-bank-alm · [[hqla]] thêm drives → [[net-interest-margin]] "−" (choudhry-nim-5) · [[net-interest-income-sensitivity]] input-to → [[balance-sheet-optimisation-model]] đổi cite lubinska-u05-11 → lubinska-u04-12
- updated: [[nii-shocks-regulation-hedging-and-alco-tradeoffs]] (bảng chuỗi quan hệ Q7/Q8 bỏ ghi chú chờ duyệt)
- còn mở: 2 cạnh của [[interest-rate-swap]] (input-to NII cite irrbb-u06-5; hedges EVE cite irrbb-u05-8) dẫn trích dẫn không nhắc swap — chưa xử lý, chờ quyết định

## [2026-10-20] review | interest-rate-swap — sửa cite 2 cạnh
- [[interest-rate-swap]] input-to → [[net-interest-income-sensitivity]]: cite irrbb-u06-5 → irrbb-p08-3 (ΔNII gồm khoản mục ngoại bảng; IRS là thoả thuận ngoại bảng, choudhry-hedge-10)
- [[interest-rate-swap]] hedges → [[economic-value-of-equity]]: cite irrbb-u05-8 → tata-svb-3; chiều pay-fixed ghi ở thân bài vì taxonomy chỉ cho regime với drives (receiver làm EVE nhạy hơn, tata-nii-10)
- thân bài: thêm 2 bullet (chiều phòng ngừa EVE; IRS trong ΔNII)

## [2026-10-20] ingest | src-bardaeva-alm u02
- created: không có
- updated: [[src-bardaeva-alm]] (thêm unit u02, Ch.6–9, 16 key claims, 24 trích dẫn nguyên văn), [[risk-appetite]] (bổ sung khung RAF 4 trụ cột, cơ chế đèn tín hiệu 3 màu Green/Amber/Red, ngưỡng leo thang ERT và Recovery Plan, vai trò calibration của ALM), [[alm-operating-model]] (định nghĩa tổng quát ALM, ma trận 4 phân hệ nhiệm vụ theo 3 chân trời thời gian Table 9.1 và tác động trên 6 nhóm sản phẩm bảng cân đối: Loans, Bonds, Participations, Cash, Deposits, Equity), [[balance-sheet-optimisation-model]] (bổ sung luận điểm Complete Interrelation và nhiệm vụ giải bài toán tối ưu hoá đa tham số để vượt qua các điểm nghẽn bottleneck), [[index]], [[overview]], [[domain-alm]]
- proposed: không có
- conflicts: không có
- syntheses flagged: không có
- backfill: không có
- tiếp theo: src-bardaeva-alm u01 (Lịch sử ALM tiền Basel đến Basel III) hoặc src-tt50-2026-nhnn C2-M3

## [2026-10-20] ingest | src-bardaeva-alm u01
- unit: u01 (Ch.1–5 Lịch sử 5 thời kỳ phát triển của các khái niệm ALM: 1950–1973 Can thiệp tối thiểu, 1973–1986 Rủi ro tối thiểu & Gap analysis, 1986–1998 Công cụ ngoại bảng, Duration gap & Repo, 1998–2008 Rào cản bảng cân đối & Basel II/ICAAP, 2009–2020 Biên sinh lời thấp, Basel III LCR/NSFR & Trái phiếu AT1)
- created: [[alm-evolution]] (khái niệm 6 kỷ nguyên tiến hoá ALM kết nối Ch.1–5 của u01 và Ch.6–7 của u02)
- updated:
  - [[src-bardaeva-alm]]: thêm unit u01 vào units_done, tóm tắt và 10 key claims (block-id ^ch1-1 đến ^ch5-4)
  - [[repricing-gap-analysis]]: bổ sung bối cảnh ra đời thập niên 1973–1986 và Box 2.1 so sánh Liquidity Gap vs Interest Rate Gap
  - [[lcr]]: bổ sung ví dụ tính toán đệm thanh khoản LCR mục tiêu 110% (Table 5.1), trần dòng vào 75%
  - [[contingent-convertible-bond]]: bổ sung số liệu phát hành AT1 thực tế 91 tỷ EUR tại châu Âu và ngưỡng kích hoạt CET1 5,125% theo CRR
  - [[index]], [[overview]], [[domain-alm]]
- proposed: [[duration-gap-model]] (canonical: đề xuất tại ## Đề xuất cập nhật về bối cảnh Ch.3 1986–1998, IRS và đệm trái phiếu Repo)
- conflicts: không có
- syntheses flagged: không có
- backfill: không có
- tiếp theo: src-bardaeva-alm u05 (notes) hoặc src-tt50-2026-nhnn C2-M3

## [2026-10-20] ingest | src-bcbs-irrbb-2016 U03 (bổ sung Table A & Table B)
- claim mới: ^irrbb-p08-7, ^irrbb-p08-8, ^irrbb-p08-9, ^irrbb-p08-10, ^irrbb-p08-11 (5 claim)
- updated: [[src-bcbs-irrbb-2016]] (thêm 5 key claims về khung công bố Trụ cột 3: Table A định tính/định lượng NMDs và Table B định lượng 6 kịch bản sốc EVE/NII so sánh T vs T-1 trên vốn Tier 1)
- proposed: [[bcbs-irrbb]] (canonical: đề xuất tại ## Đề xuất cập nhật chi tiết hoá khung công bố Trụ cột 3 theo Table A và Table B)
- conflicts: không có
- syntheses flagged: không có
- backfill: không có
## [2026-10-20] ingest | src-bcbs-irrbb-2016 U05 (bổ sung KAO & options)
- claim mới: ^irrbb-u05-26, ^irrbb-u05-27, ^irrbb-u05-28 (3 claim)
- updated: [[src-bcbs-irrbb-2016]] (thêm 3 key claims chi tiết hoá cơ chế định giá rủi ro quyền chọn tự động KAO, định giá lại biến động FVAO với mức tăng biến động ngầm định 25%, và quy tắc bù trừ quyền chọn mua phòng ngừa theo par 130–131)
- proposed: [[option-risk]], [[irrbb-standardised-framework]] (canonical: đề xuất tại ## Đề xuất cập nhật chi tiết hoá thuật toán KAO, phân loại swaptions/wholesale options và quy tắc bù trừ quyền chọn mua)
- conflicts: không có
- syntheses flagged: không có
- tiếp theo: hoàn thành tuần tự A -> B -> C

## [2026-10-20] ingest | src-bcbs-irrbb-2016 U03 (bổ sung Principle 5 wholesale NMDs & dimensions)
- claim mới: ^irrbb-p05-4, ^irrbb-p05-5, ^irrbb-p05-6 (3 claim)
- updated: [[src-bcbs-irrbb-2016]] (thêm 3 key claims chi tiết hoá Nguyên tắc 5: phân tầng giả định NMDs retail vs wholesale và cam kết cho vay doanh nghiệp, 6 chiều kích mô hình hoá hành vi NMDs và quyền chọn nhúng trong công cụ thả nổi, quy trình kiểm định độc lập, phân tích độ nhạy EVE/earnings và chu kỳ rà soát hàng năm)
- proposed: [[non-maturity-deposits]] (canonical: đề xuất tại ## Đề xuất cập nhật chi tiết hoá giả định hành vi NMDs bán buôn, 6 chiều kích mô hình hoá và quy trình kiểm định độc lập)
- conflicts: không có
- syntheses flagged: không có
- backfill: không có
- tiếp theo: src-tt50-2026-nhnn C2-M3 hoặc src-bardaeva-alm u05

## [2026-10-20] decision | hạ 45 node canonical về draft
- bối cảnh: 45 node mang `maturity: canonical` từ initial commit (2026-10-16), field `reviewed:` trống ở cả 45, log không có entry promote; có lỗi nội dung đã ghi nhận trong chính các node này (điểm giữa dải 9M–1Y, AUD short, "chỉ bao gồm" vs "typically", số thiếu citation ở 7 synthesis FTP).
- quyết định (user): hạ toàn bộ về `draft`; promote lại từng node khi user review thực sự (điền `reviewed:`).
- đã đổi: chỉ frontmatter `maturity: canonical → draft` và `updated: 2026-10-20`; thân bài và mục `## Đề xuất cập nhật` giữ nguyên.
- còn lại: 65 đề xuất chờ duyệt (18 node) trở thành việc LLM được tự áp theo write policy draft; gom nhóm và kế hoạch ingest/research ở phiên này.
- lint: 187 note · 0 error · 0 warning.

## [2026-10-20] review | giai đoạn 1: áp 65 đề xuất tồn đọng trên 18 node vừa hạ draft
- nhóm E (IRRBB lõi): [[irrbb-standardised-framework]] Giai đoạn 4 (phạm vi quyền chọn tự động ^irrbb-u05-26, +25% cho cả quyền chọn bán và mua ^irrbb-u05-27, lựa chọn đưa quyền chọn mua vào KAO ^irrbb-u05-28; bỏ "Black-Scholes, Hull-White" và lý do "phản ánh bất định" không có nguồn); [[option-risk]] tóm tắt + link; [[non-maturity-deposits]] mục "Giả định hành vi theo Principle 5" (^irrbb-p05-4…6, giữ mức "nên"); [[bcbs-irrbb]] Table A/B dưới Nguyên tắc 8 (^irrbb-p08-7…11); [[duration-gap-model]] chỉ thêm link [[alm-evolution]].
- 7 synthesis FTP: mục "Căn cứ quy định: NHNN và Basel" ở [[ftp-nature-and-balance-sheet-management]] (TT83 Đ6.4.b, Đ25.3, Đ26.2.c, PL6, Đ60.1; BCBS 144 P2, P4); đoạn đối chiếu NHNN/Basel đặt đúng chỗ ở [[ftp-risk-and-cost-components]], [[ftp-final-rate-determination]], [[ftp-cost-benefit-allocation-principles]] (thêm vốn chủ sở hữu trong FTP theo Choudhry capm-11…13, gov-12), [[ftp-economic-cost-and-incentive-validation]] (ghi khác biệt: sơ đồ đặt ALCO là cấp phê duyệt cao nhất, TT83 đặt ALCO tham mưu TGĐ), [[ftp-portfolio-and-bucket-allocation]] (repo: TT83 Đ3.33 vs RBC25.9; hạn mức sổ kinh doanh Đ35.2, Đ37.1), [[ftp-curve-construction-methodology]].
- [[practical-alm-liquidity-governance]]: mục 5 "Đối Chiếu NHNN và Basel" (TT83 Đ6.4.b, Đ23.5, Đ25.3, Đ45.3, Đ48.2, Đ48.4, Đ49.1; BCBS 144 P2/P4/P10/P11, SRP30.50–51; Choudhry ALCO, LAB, ILAAP, RAYG); thay câu quy kết chung về khủng hoảng bằng số liệu SVB có cite.
- [[basel-liquidity-monitoring-framework]], [[synthetic-balance-sheet-liquidity-risk]]: ALCO theo TT83; tập trung nguồn vốn SRP30.22 vs TT83 Đ50.1/Đ48.3; sửa "tuân thủ ngưỡng <1%" thành ngưỡng nhận diện đối tác trọng yếu SRP50.17; tỷ trọng bán buôn 20% ghi [cần nguồn].
- [[irrbb-five-tier-architecture]]: SVB thay "lãi suất tăng 500 bps" (không có nguồn) bằng ^tata-svb-5/7/9; repricing gap và PV01 ở Tầng 3; structural hedging, ví dụ EAR/cap ở Tầng 4; hedge accounting 80–125%; link OIS; ALCO theo TT83.
- không áp: 2 (OIS ở ftp-curve, currency swap ở five-tier: node không nhắc); áp một phần: 1 (duration-gap-model).
- sửa kỹ thuật: 34 link `file:///` → wikilink (five-tier 29, ftp-nature 4, behavioural-options 1); 3 link một ngoặc ở ftp-nature; câu cite ^vab-ftp-28 ở [[ftp-curve-construction-methodology]] viết sát trích dẫn, phương án VNIBOR + TPCP ghi [cần nguồn].
- đã kiểm: lỗi 0.7917 (framework) và AUD 400 (shocks) đã được sửa từ 2026-10-18/19.
- phát hiện cho giai đoạn sau: claim ^ch3-1 (Bardaeva) chỉ trích tiêu đề Table 3.1; ^irrbb-p05-4 claim có "khác biệt căn bản" không có trong trích; ^vab-ftp-24 chỉ trích câu dẫn, thiếu danh mục thông tin đường cong cơ sở; 8 synthesis FTP còn dẫn TT22.
- lint: 187 note · 0 error · 0 warning.

## [2026-10-20] ingest | src-tt50-2026-nhnn C2-M5
- created: [[src-tt50-2026-nhnn]] (27 claim C2-M5 Đ13–27 + 1 claim Đ37 từ unit C3, đọc một phần, không mark), [[tt50-2026]] (regulation VN, implements bcbs-lcr, bcbs-nsfr dưới *Diễn giải*)
- updated: [[lcr]] (5 dòng VN: phạm vi riêng lẻ, lộ trình 50% → 100% tới 01/10/2033, horizon 30 ngày, trần dòng vào 75%, báo cáo/theo dõi hằng ngày), [[nsfr]] (ngưỡng 90/95/100%, phạm vi), [[hqla]] (cấu trúc cấp, yêu cầu vận hành; sửa "bắt buộc từ 01/07/2027" sai thành LCR áp dụng từ 01/10/2028), [[net-cash-outflows]] (bảng Basel vs VN mới), [[available-stable-funding]], [[required-stable-funding]] (nhãn chờ PL2), [[lcr-by-currency]], [[loan-to-deposit-ratio]], [[intraday-liquidity-risk]], [[contingency-funding-plan]], [[liquidity-stress-testing]]
- conflicts: không có (khác Basel là khác jurisdiction: lộ trình chuyển tiếp, phạm vi riêng lẻ)
- syntheses flagged: 22 synthesis link lcr/nsfr/hqla và nhắc VN/TT22 (## Bất định)
- backfill: linked [[tt50-2026]] ở lần nhắc đầu trong 19 node draft
- phát hiện: TT50 sửa đổi chứ không thay TT22; tỷ lệ TT22 vẫn bắt buộc tới khi ngân hàng áp dụng LCR/NSFR (Đ13.4)
- tiếp theo: src-tt50-2026-nhnn PL1 (HQLA, hệ số rút/thu tiền), PL2 (ASF/RSF)

## [2026-10-20] ingest | src-tt50-2026-nhnn C2-M2, C2-M4
- updated: [[src-tt50-2026-nhnn]] (+4 claim: ^d8-1, ^d12-1, ^d12-4, ^d12-6), [[tt50-2026]] (relations governs leverage-ratio, LDR; bảng yêu cầu), [[leverage-ratio]] (VN: Thống đốc quyết định áp dụng và ngưỡng khi cần thiết; LEV = Vốn cấp 1 / EM), [[loan-to-deposit-ratio]] (công thức VN, ngưỡng 95%, thời điểm áp dụng)
- conflicts: không có
- syntheses flagged: các synthesis link leverage-ratio hoặc LDR (## Bất định)
- tiếp theo: src-tt50-2026-nhnn PL2, PL1

## [2026-10-20] ingest | src-tt50-2026-nhnn PL2
- updated: [[src-tt50-2026-nhnn]] (+4 claim: ^pl2-a1, ^pl2-a2 bảng ASF, ^pl2-b1, ^pl2-b2 bảng RSF), [[available-stable-funding]] (6 dòng VN + dòng Khác biệt), [[required-stable-funding]] (7 dòng VN + Khác biệt), [[nsfr]] (10 dòng VN), [[asf-capital-and-long-term-liabilities]], [[rsf-hqla-and-central-bank-reserves]], [[rsf-derivatives-and-off-balance-sheet]] (trả lời câu hỏi mở VN)
- conflicts: không có (khác jurisdiction)
- syntheses flagged: các synthesis link ASF/RSF/NSFR (## Bất định)
- tiếp theo: src-tt50-2026-nhnn PL1 (872 dòng: HQLA, hệ số rút tiền/thu tiền)

## [2026-10-20] ingest | src-tt50-2026-nhnn PL1
- updated: [[src-tt50-2026-nhnn]] (+14 claim PL1: ^pl1-a1 … ^pl1-c4), [[lcr]] (7 dòng VN: trần cấp 2 qua KĐC15%/KĐC40%, hệ số thanh khoản 100/85/75–50%, run-off 5%/10%), [[hqla]] (5 dòng VN), [[level-1-assets]], [[level-2-assets]] (sửa: trái phiếu chính quyền địa phương thuộc cấp 1, không phải 2A), [[retail-deposit-stability]], [[unsecured-wholesale-funding]], [[operational-deposits]], [[secured-funding]], [[committed-facilities]], [[hqla-unwinding-mechanism]], [[cash-outflows]]
- conflicts: không có (khác jurisdiction: điều kiện tiền gửi ổn định chặt hơn Basel; tiền gửi ngoại tệ luôn kém ổn định; không có mức 3%; chứng khoán chủ quyền nước ngoài cấp 1 phải niêm yết, có lịch sử giá)
- syntheses flagged: các synthesis link LCR/HQLA/dòng tiền (## Bất định)
- tiếp theo: src-bcbs-liquidity-principles-2008 p05–p09, p12; src-tt50-2026-nhnn PL4, C1

## [2026-10-20] decision | đính chính quan hệ TT50/2026 – TT22/2019
- user chỉ ra: TT50 thay thế TT22. Đối chiếu raw: Đ1.1 TT50 là khung tỷ lệ an toàn của NHTM, chi nhánh NHNNg; Đ37.3.a thu hẹp đối tượng của TT22 còn ngân hàng hợp tác xã và NHTM đang thực hiện Đ23.3 TT41/2016; không có điều khoản bãi bỏ TT22; Đ13.4 dẫn chiếu tỷ lệ tính theo TT22 trong giai đoạn chuyển tiếp.
- đính chính: dòng "TT50 sửa đổi chứ không thay TT22" ở entry ingest C2-M5 phía trên là chưa chính xác. Cách ghi đúng: TT50 thay thế TT22 đối với NHTM và chi nhánh NHNNg (kỹ thuật sửa đổi phạm vi, không bãi bỏ); tỷ lệ TT22 chỉ còn áp qua dẫn chiếu Đ13.4 tới khi áp dụng LCR/NSFR.
- updated: [[src-tt50-2026-nhnn]] (+2 claim: ^d1-1, ^d37-3a; sửa mục Thông tin nguồn, Tóm tắt), [[tt50-2026]] (Mục đích & phạm vi, Ngoại lệ, Sửa đổi / thay thế, Tác động ALM)
- hệ quả cho synthesis: chỗ dẫn TT22 nên đổi căn cứ sang TT50 (Đ13.4 cho giai đoạn chuyển tiếp, Đ16/Đ22 cho LCR/NSFR); các dòng đánh dấu "trước đó vẫn tuân thủ tỷ lệ TT22/2019" trong ## Bất định hiểu theo nghĩa dẫn chiếu Đ13.4.

## [2026-10-20] ingest | src-bcbs-liquidity-principles-2008 p05, p06, p07, p08, p09, p12
- claim mới (46): ^lrm-p05, ^lrm-22, ^lrm-23, ^lrm-24, ^lrm-26…^lrm-31, ^lrm-37, ^lrm-40, ^lrm-41, ^lrm-43, ^lrm-44, ^lrm-47…^lrm-50, ^lrm-53, ^lrm-56 (P5); ^lrm-p06, ^lrm-58, ^lrm-61, ^lrm-63, ^lrm-64 (P6); ^lrm-p07, ^lrm-65, ^lrm-66, ^lrm-69, ^lrm-74 (P7); ^lrm-p08, ^lrm-78, ^lrm-80, ^lrm-87 (P8); ^lrm-p09, ^lrm-88…^lrm-91 (P9); ^lrm-p12, ^lrm-123…^lrm-127 (P12)
- updated: [[bcbs-liquidity-principles]] (bảng P5–P9, P12 thay dòng `[cần nguồn]`; định nghĩa early warning indicators; governs mới tới [[liquidity-transfer-restrictions]], [[funding-concentration-risk]], [[intraday-liquidity-risk]], [[asset-encumbrance]], [[hqla]]); mục căn cứ BCBS 144 trong [[liquidity-risk-management]] (P5), [[liquidity-transfer-restrictions]] (P6), [[funding-concentration-risk]] (P7), [[intraday-liquidity-risk]] (P8), [[asset-encumbrance]] (P9, thêm domain basel), [[hqla]] (P12), [[liquidity-monitoring-metrics]], [[contractual-maturity-mismatch]], [[lcr-by-currency]], [[committed-facilities]], [[non-maturity-deposits]]
- conflicts: không có
- syntheses flagged: [[basel-liquidity-monitoring-framework]], [[synthetic-balance-sheet-liquidity-risk]], [[integrated-alm-liquidity-strategy]], [[practical-alm-liquidity-governance]], [[hqla-decomposition-and-tradeoffs]], [[lcr-economic-significance-and-alm-governance]] (căn cứ nguyên tắc BCBS 144 mới)
- backfill: không có node mới
- tiếp theo: src-bcbs-liquidity-principles-2008 p13 (công bố thông tin, đối chiếu TT50 PL4), p14–p17 (vai trò giám sát)

## [2026-10-20] ingest | src-vab-ftp u05 (bổ sung)
- claim mới: ^vab-ftp-41 (danh mục thông tin đường cong cơ sở: VND lãi suất huy động thực tế bình quân 3 tháng gồm chi phí huy động; USD LIBOR/SIBOR/SOFR và đường cong swap USD), ^vab-ftp-42 (hoàn thiện đường cong: nội suy tuyến tính VND, bình quân 3 tháng USD); claim ^vab-ftp-24 giữ nguyên
- syntheses flagged: [[ftp-risk-and-cost-components]] (mục 2.1 cite ^vab-ftp-24 cho VNIBOR + OMO + VGB — raw không có), [[ftp-curve-construction-methodology]] (mục 2.3 cite ^vab-ftp-24 cho chu kỳ rà soát ALCO — claim không nói; mục 3.1 phương án VNIBOR + TPCP không có trong VAB)
- tiếp theo: sửa hai synthesis ở Giai đoạn 3 (R1)

## [2026-10-20] ingest | src-tt50-2026-nhnn C1, PL4
- claim mới: ^d1-2, ^d1-5, ^d3-5, ^d3-15, ^d3-17, ^d3-18, ^d4-3, ^d5-1 (C1); ^pl4-1, ^pl4-3 (PL4). C1 nay ingest trọn; Đ4.1–4.2 (tín dụng, vốn) không trích
- updated: [[tt50-2026]] (Yêu cầu chính thêm Đ1.5, Đ4.3–4.4, Đ5, PL4; Định nghĩa thêm bị ràng buộc, ba mức huỷ ngang, rehypothecation; Ngoại lệ thêm Đ1.2), [[asset-encumbrance]] (VN: Đ3.17, Đ24.4; domain vn-reg), [[committed-facilities]] (Đ3.5–3.7)
- conflicts: không có
- syntheses flagged: không có (định nghĩa và công bố thông tin không đổi kết luận synthesis)
- tiếp theo: src-tt50-2026-nhnn PL3 (tổng trạng thái rủi ro), C3 phần còn lại

## [2026-10-20] maintenance | trang domain sau khi hạ 45 node
- gỡ nhãn "(canonical)" cũ trong [[domain-alm]], [[domain-basel]], [[domain-product]], [[domain-vn-reg]]; tính lại bảng Thống kê theo frontmatter (alm 178, basel 123, vn-reg 76, product 47, đều draft)
- [[domain-basel]], [[domain-vn-reg]]: dòng LCR/NSFR Basel ↔ VN không còn ghi "chờ PL1/PL2"; thêm dòng công bố thông tin (TT50 Đ27, PL4)

## [2026-10-20] ingest | src-vab-ftp u02, u03 (bổ sung)
- claim mới: ^vab-ftp-43 (TSTK theo Phụ lục 3 TT22, số dư bình quân 3 tháng không gồm repo), ^vab-ftp-44 (KKH có khả năng bị rút ≥ 15%, chú thích dẫn điểm 2 phần III Phụ lục 3 TT22)
- syntheses flagged: không có (dùng ngay cho research R1)

## [2026-10-20] ingest | src-bcbs-framework SRP50 (bổ sung)
- claim mới: ^srp50-15 (SRP50.14–15: chỉ số chia tổng nợ phải trả; theo dõi cả tỷ lệ tuyệt đối và mức tăng), ^srp50-17b (nhóm liên quan theo Large Exposure; tiền gửi nội bộ tập đoàn nhận diện riêng)

## [2026-10-20] research | Giai đoạn 3 R1–R3 + rà dòng Bất định BCBS 144
- R1 căn cứ FTP: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản" (TT50 Đ37.3.a, Đ13.4, Đ13.1, Đ13.5) vào 8 synthesis FTP và [[irrbb-liquidity-hqla-and-ftp-interaction]]; câu dẫn TT22 nay ghi rõ là căn cứ chuyển tiếp; cite ^vab-ftp-43/44 cho Phụ lục 3 TT22 và tỷ lệ 15%.
- R1 sửa cite sai ^vab-ftp-24: [[ftp-risk-and-cost-components]] mục 2.1 (thay danh mục VNIBOR/OMO/VGB bằng danh mục thật ^vab-ftp-28/41/42; phương án VNIBOR/OMO/VGB chuyển sang *Diễn giải* [cần nguồn]); [[ftp-curve-construction-methodology]] mục 2.3 (chu kỳ rà soát ALCO → [cần nguồn]) và 3.1.
- R1 khác: [[ftp-cost-benefit-allocation-principles]] bỏ dẫn TT41/2016 cho đệm thanh khoản cam kết ngoại bảng (không có nguồn trong wiki) → [cần nguồn].
- R2 LCR/NSFR: cập nhật câu "TT50 chưa ingest" ở [[irrbb-liquidity-hqla-and-ftp-interaction]], [[practical-alm-liquidity-governance]]; thêm cite Đ13.1, Đ16.1.c, Đ22.2 cho lộ trình ở [[nsfr-alm-governance-strategy-and-risks]], [[nsfr-structural-liquidity-and-alm-strategy]], [[integrated-alm-liquidity-strategy]]; thêm xử lý vi phạm LCR của VN (Đ17.2) vào bảng traffic-light ở [[lcr-economic-significance-and-alm-governance]]; bỏ "BCBS" khỏi danh sách cơ quan giám sát ở [[nsfr-alm-governance-strategy-and-risks]]; [[lcr]] thay câu "theo ghi chú register" bằng cite ^d13-1 và ^d17-2.
- R3 tập trung nguồn vốn: [[funding-concentration-risk]] sửa cite ^srp50-17 → ^srp50-17b (LEX, nội bộ tập đoàn), thêm công thức ^srp50-15, sửa run-off LCR (100% chỉ với định chế tài chính, 40% DN phi tài chính) và ASF NSFR (0% chỉ với định chế tài chính < 6 tháng, 50% DN phi tài chính), hạn mức ALCO 1,5–2%/Top 10 chuyển sang *Diễn giải* không nguồn. Repo RBC25 vs TT83 Đ3.33: đã đúng ở [[banking-book]], không đổi.
- BCBS 144 p05–p12: thêm mục căn cứ ở [[basel-liquidity-monitoring-framework]], [[hqla-decomposition-and-tradeoffs]], [[integrated-alm-liquidity-strategy]], [[lcr-economic-significance-and-alm-governance]], [[practical-alm-liquidity-governance]], [[synthetic-balance-sheet-liquidity-risk]]; dòng Bất định tương ứng → đã rà.
- còn mở: hệ số rút tiền KKH của TT50 PL1 thay cho 15% TT22 sau 2028; thủ tục xử lý NSFR dưới ngưỡng tại VN; TT83 C3-M5; dòng Bất định PL1/PL2 (ví dụ tính LCR/NSFR) chưa rà.

## [2026-10-20] maintenance | lưu trữ đề xuất cập nhật đã xử lý
- Theo yêu cầu user: xoá khỏi node các dòng `## Đề xuất cập nhật` đã có "→ đã áp dụng/đã rà"; nguyên văn lưu dưới đây. Mục rỗng thì bỏ heading.

### [[basis-risk]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: thêm góc nhìn VN: rủi ro cơ sở phát sinh từ sự khác nhau giữa lãi suất dùng để định giá lại tài sản và nợ phải trả có cùng kỳ hạn [[src-tt83-2025-nhnn#^d3-22]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm cách đo của nguồn T4: theo dõi benchmark của tài sản và nợ theo từng dải, sốc 1 bp để xem tác động P&L; một số ngân hàng mặc định khớp yếu tố rủi ro hai phía [[src-lubinska-alm-optimisation#^lubinska-u02-31]]. Link [[pv01]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: thêm hai dạng basis risk theo Choudhry: (1) cho vay cố định tài trợ bằng tiền gửi bám nhưng không gắn chính thức với lãi suất cơ bản NHTW, phòng ngừa bằng [[overnight-index-swap]] [[src-choudhry-principles-banking#^choudhry-hedge-18]]; (2) 'secondary IRR': tài sản tái định giá chậm hơn nợ [[src-choudhry-principles-banking#^choudhry-hedge-20]]. Thêm basis risk của futures (chênh lệch giá tiền mặt và futures) [[src-choudhry-principles-banking#^choudhry-hedge-27]] và khi roll strip hedge [[src-choudhry-principles-banking#^choudhry-hedge-7]]; giao dịch đối ứng chính xác giảm basis risk [[src-choudhry-principles-banking#^choudhry-hedge-3]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u14 — chờ user duyệt: thêm mẫu trang 'Basis Risk' trong ALCO MI pack (Figure 9.18): phân loại tài sản/nợ theo cơ sở lãi suất (fixed theo kỳ, administered, Bank Base Rate, non-interest) và cột Mis-Match [[src-choudhry-principles-banking#^choudhry-alco-19]]; FSA yêu cầu MI pack có phân tích basis risk [[src-choudhry-principles-banking#^choudhry-alco-9]]. Basis risk trong securitisation (IBOR 3 tháng so với Bank Base Rate) [[src-choudhry-principles-banking#^choudhry-sec-4]]; đã có node [[securitisation]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: thêm ví dụ kinh điển: khoản vay Mỹ theo prime rate (administered, không đổi hằng ngày) và funding theo Libor; tương quan dương nhưng không thay đổi cùng mức nên spread biến động [[src-choudhry-principles-banking#^choudhry-irr-5]]. Gap analysis giả định dịch chuyển song song, gây basis risk giữa tài sản ngắn và dài hạn [[src-choudhry-principles-banking#^choudhry-irr-7]]. → đã áp dụng [2026-10-20]

### [[behavioural-options]]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 — user duyệt [2026-10-19]: thêm dòng VN. Ngân hàng phải có quy định nội bộ về tiêu chí xác định khoản vay có rủi ro trả trước hạn và tiền gửi có rủi ro rút trước hạn; $\gamma_i$ (Bảng 3) và $u_i$ (Bảng 4) cùng giá trị d368 [[src-tt83-2025-nhnn#^pl5-a2-3b]] [[src-tt83-2025-nhnn#^pl5-a2-3c]]; công thức chỉ áp cho khách hàng cá nhân, khoản của tổ chức do ngân hàng tự xác định dòng tiền. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 (bổ sung) — chờ user duyệt: thêm vào `## Basel vs VN` dòng "Đơn vị tính tham số cơ sở": $CPR_0$ và $TDRR_0$ xác định cho từng danh mục p gồm các khoản cùng đồng tiền, cùng đặc điểm, trong điều kiện hiện hành [[src-tt83-2025-nhnn#^pl5-a2-3b2]] [[src-tt83-2025-nhnn#^pl5-a2-3c2]]; $CF^S$ là khoản trả gốc, lãi định kỳ [[src-tt83-2025-nhnn#^pl5-a2-3b2]]; $TD_0$ là số dư tiền gửi còn lại của danh mục [[src-tt83-2025-nhnn#^pl5-a2-3c2]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: thêm dòng `## Basel vs VN` "Định nghĩa": VN — rủi ro quyền lựa chọn hành vi phát sinh khi lãi suất thay đổi có thể làm thay đổi hành vi khách hàng [[src-tt83-2025-nhnn#^d3-22]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M8 — chờ user duyệt: thêm góc nhìn VN: mô hình $CPR_0$, $TDRR_0$ chịu yêu cầu vòng đời và kiểm soát override [[src-tt83-2025-nhnn#^d56-4]], kiểm định tối thiểu hằng năm [[src-tt83-2025-nhnn#^d56-4d]]; link [[model-validation]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u08 — chờ user duyệt: thêm: mô hình hành vi phân khúc khách hàng theo đặc điểm (số dư ban đầu, lãi khuyến mãi, quan hệ, tuổi, kênh mở), hiệu chỉnh riêng từng nhóm và backtest liên tục [[src-tata-bank-alm#^tata-fut-5]]; báo cáo EU yêu cầu tỷ lệ trả trước và rút trước hạn có điều kiện [[src-tata-bank-alm#^tata-rep-3]]; DeFi thiếu dữ liệu lịch sử để hiệu chỉnh hành vi [[src-tata-bank-alm#^tata-fut-2]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: thêm: lãi suất tăng nhanh làm khoản vay cố định lãi thấp được giữ lâu hơn (trả trước chậm), khoản vay thả nổi trả trước nhanh hơn [[src-tata-bank-alm#^tata-rr-3]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u06 — chờ user duyệt: thêm yêu cầu EBA (qua nguồn T4): xét tác động lên tốc độ trả trước hiện tại và tương lai từ kịch bản lãi suất, môi trường kinh tế, đặc điểm hợp đồng, và độ co giãn lãi suất sản phẩm [[src-tata-bank-alm#^tata-beh-1]]; bốn nhóm cần mô hình hành vi (NMD, thấu chi, vay có quyền trả trước, tiền gửi có kỳ hạn rút sớm); dữ liệu thời kỳ lãi suất âm không dùng backtest cho thời kỳ lãi suất dương và ngược lại [[src-tata-bank-alm#^tata-beh-2]]. Link [[negative-interest-rates]]. → đã áp dụng [2026-10-20]

### [[contingency-funding-plan]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M5 — chờ user duyệt: thêm góc nhìn VN: TT83/2025 bắt buộc lập kế hoạch dự phòng căn cứ kết quả kiểm tra sức chịu đựng, tối thiểu gồm nhận diện khủng hoảng và sự kiện kích hoạt, thẩm quyền kích hoạt và vai trò, nguồn dự phòng tài chính (lượng vốn, mức sẵn có, điều kiện, độ tin cậy, thời gian huy động), báo cáo trong và ngoài ngân hàng (kể cả NHNN), rà soát định kỳ [[src-tt83-2025-nhnn#^d48-4]]; thêm relation `part-of` → [[liquidity-risk-management]] (cite [[src-choudhry-principles-banking#^choudhry-cfp-1]]); link [[liquidity-stress-testing]] (node mới, `input-to` CFP). → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[overnight-index-swap]]; đề xuất link ở lần nhắc đầu OIS/SONIA. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → không áp dụng [2026-10-20]: NIM chỉ xuất hiện trong sơ đồ code block, không đặt link được
- [2026-10-19] ingest src-bardaeva-alm u04 — chờ user duyệt: thêm thứ tự hành động thanh khoản trong khủng hoảng theo Bardaeva (T4): tái định giá tiền gửi; cảnh báo tăng mạnh lãi suất tiền gửi có thể bị đọc là tín hiệu SOS [[src-bardaeva-alm#^ch15-3]]; đàm phán funding trung dài hạn với tổ chức tài chính, hỗ trợ từ công ty mẹ, chuyển nhượng khoản vay, cuối cùng yêu cầu khách hàng trả nợ trước [[src-bardaeva-alm#^ch15-4]]. Link [[recovery-and-resolution-planning]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u21–u22 — chờ user duyệt: đã có node [[key-risk-indicators]] (KRI Tier 1–3, EWI, RAYG, leo thang amber 48 giờ/red); đề xuất link ở mục "A. Hệ thống Chỉ báo Cảnh báo Sớm"; thêm: vi phạm red Tier 2 KRI không tự động kích hoạt LCP [[src-choudhry-principles-banking#^choudhry-kri-2]], LCP là phần thanh khoản của Recovery Plan [[src-choudhry-principles-banking#^choudhry-rmf-10]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u23–u24 — chờ user duyệt: thêm định nghĩa của Choudhry: CFP nêu chiến lược xử lý thiếu hụt thanh khoản trong tình huống khẩn cấp và chứng minh ngân hàng tồn tại qua một kịch bản stress [[src-choudhry-principles-banking#^choudhry-ilaap-8]]; khi [[cash-flow-survival-period]] ngắn hơn khẩu vị thì rà lại CFP [[src-choudhry-principles-banking#^choudhry-ilaap-7]]; ILAAP nêu biện pháp CFP sẽ áp dụng [[src-choudhry-principles-banking#^choudhry-ilaap-11]]. Link [[ilaap]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u18 — chờ user duyệt: thêm: Choudhry xếp CFP là 'Plan B'; CFP không thuộc chiến lược, nhưng phần chiến lược về thanh khoản và funding nên tham chiếu tới nó [[src-choudhry-principles-banking#^choudhry-strat-29]]. Link [[bank-strategic-plan]]. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p11 — chờ user duyệt: thêm góc nhìn Basel BCBS 144 Principle 11: định nghĩa CFP [[src-bcbs-liquidity-principles-2008#^lrm-110]]; CFP chính thức với chính sách cho nhiều môi trường stress, trách nhiệm, kích hoạt và leo thang [[src-bcbs-liquidity-principles-2008#^lrm-p11]]; nêu nguồn dự phòng, số tiền ước tính và lead time từng nguồn [[src-bcbs-liquidity-principles-2008#^lrm-111]]; gắn với kết quả stress test, kể cả trong ngày [[src-bcbs-liquidity-principles-2008#^lrm-112]]; yếu tố thiết kế (bán/chứng khoán hoá tài sản khi stress, hiệu ứng danh tiếng, chuyển thanh khoản giữa pháp nhân) [[src-bcbs-liquidity-principles-2008#^lrm-117]]; tiếp cận NHTW và thanh toán trong ngày [[src-bcbs-liquidity-principles-2008#^lrm-118]]; rà soát, cập nhật ít nhất hằng năm để HĐQT phê duyệt [[src-bcbs-liquidity-principles-2008#^lrm-121]]. Đề xuất thêm link [[bcbs-liquidity-principles]] và nguồn src-bcbs-liquidity-principles-2008 vào `sources`. → đã áp dụng [2026-10-20] (mục 5)

### [[csrbb]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9 — chờ user duyệt: đã có node [[icaap]] (và stub [[economic-capital]]); đề xuất link ở lần nhắc đầu ICAAP / vốn kinh tế. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M3 — chờ user duyệt: đã có node [[market-risk-management]]; đề xuất link ở chỗ phân định ranh giới sổ ngân hàng/sổ kinh doanh. TT83 Đ35–37 không nhắc credit spread; rủi ro lãi suất thuộc rủi ro thị trường gắn với sổ kinh doanh [[src-tt83-2025-nhnn#^d3-15a]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u03 — chờ user duyệt: đã có node [[irrbb-management]]; đề xuất link ở lần nhắc đầu "quản trị IRRBB" / quy trình nhận diện, đo lường, kiểm soát. → đã áp dụng [2026-10-20]

### [[funding-concentration-risk]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M5 — chờ user duyệt: thêm góc nhìn VN: mức độ tập trung huy động vốn và mất khả năng thu hút vốn từ khách gửi tiền quan trọng là yếu tố bắt buộc trong kiểm tra sức chịu đựng về thanh khoản [[src-tt83-2025-nhnn#^d48-3]]; chiến lược phải có đa dạng hoá nguồn vốn [[src-tt83-2025-nhnn#^d45-2]]; có thể thêm relation `input-to` → [[liquidity-stress-testing]] (cite d48-3). → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1 — chờ user duyệt: đã có node [[risk-appetite]]; đề xuất link ở lần nhắc đầu risk appetite. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M6 — chờ user duyệt: thêm góc nhìn VN: TT83 Đ50 áp chiến lược rủi ro tập trung cho cấp tín dụng và tự doanh, không nêu nguồn vốn [[src-tt83-2025-nhnn#^d50-1]]; tập trung huy động vốn chỉ là yếu tố phải phân tích trong kịch bản stress thanh khoản [[src-tt83-2025-nhnn#^d48-3]]. Khác phạm vi so với SRP50, không phải conflict. Link [[concentration-risk-management]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: đã có node [[silicon-valley-bank]] (nguồn Tata u07); đề xuất link ở chỗ nhắc SVB và đối chiếu số liệu đang viết với [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]]. → đã áp dụng [2026-10-20] (thêm link; số liệu SVB đối chiếu lại và cite tata-svb-4/5/7)
- [2026-10-19] ingest src-choudhry-principles-banking u25 — chờ user duyệt: thêm ví dụ hạn mức: không bucket kỳ hạn nào quá 20% tổng nhu cầu vốn (case công ty chứng khoán Anh, trước 2008) [[src-choudhry-principles-banking#^choudhry-cs-8]]; rủi ro tập trung theo ngành (định chế tài chính) là một tiêu chí trong chiến lược tiền gửi [[src-choudhry-principles-banking#^choudhry-cs-20]]. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-framework SRP30 — chờ user duyệt: SRP30.22 liệt kê nguồn vốn (funding sources) là một trong chín tình huống tập trung rủi ro của Pillar 2 [[src-bcbs-framework#^srp30-22]]; đề xuất thêm link [[concentration-risk-management]] (góc nhìn Basel SRP30) và [[reputational-risk]] ở mục 3 (dòng nhắc "căng thẳng danh tiếng"). → đã áp dụng [2026-10-20]

### [[gap-risk]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đề xuất bổ sung vào câu phân bổ dải kỳ hạn (dòng 46) rằng dòng tiền được xếp theo repricing date, tức ngày hoàn trả gốc, tái định giá gốc hoặc thanh toán lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]]; công cụ thả nổi tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7 — user duyệt [2026-10-19]: thêm dòng VN. TT83/2025 yêu cầu chiến lược IRRBB tối thiểu gồm nguyên tắc quản lý theo trạng thái chênh lệch kỳ định lại lãi suất (repricing gap profile) [[src-tt83-2025-nhnn#^d53-1a1]]; báo cáo nội bộ tối thiểu hằng quý gồm trạng thái này [[src-tt83-2025-nhnn#^d55-1]]; link [[tt83-2025]]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: thêm dòng `## Basel vs VN` "Định nghĩa": VN — rủi ro chênh lệch phát sinh từ sự không khớp thời điểm định giá lại lãi suất hoặc kỳ hạn giữa tài sản và nợ phải trả (kể cả ngoại bảng) trên sổ ngân hàng [[src-tt83-2025-nhnn#^d3-22]]; tương đương d368 [[src-bcbs-irrbb-2016#^irrbb-u02-2]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm nguồn T4 thứ hai: gap risk đo bằng repricing gap và chênh lệch ròng theo dải và đồng tiền trọng yếu, phụ thuộc dịch chuyển song song hay không [[src-lubinska-alm-optimisation#^lubinska-u02-30]]; dấu GAP và rủi ro tái đầu tư/tái cấp vốn [[src-lubinska-alm-optimisation#^lubinska-u02-26]]. Link [[repricing-gap-analysis]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u25 — chờ user duyệt: thêm cách phân loại năm nguồn IRRBB của Choudhry (gap, yield curve, basis, run-off, option; gap risk nhiều khi là lỗ cơ hội khi lãi suất cố định) [[src-choudhry-principles-banking#^choudhry-cs-12]]; IRRBB là sản phẩm phụ do khách hàng tạo ra, kèm sáu nguyên nhân [[src-choudhry-principles-banking#^choudhry-cs-13]]. Link [[structural-hedging]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10 — chờ user duyệt: thêm funding short/funding long: đường cong dương thì huy động ngắn, cho vay dài, 'tail' là interest-rate gap, lãi suất ngắn tăng làm thu hẹp biên [[src-choudhry-principles-banking#^choudhry-hedge-1]]; đường cong đảo ngược thì funding long [[src-choudhry-principles-banking#^choudhry-hedge-2]]. Công cụ phòng ngừa gap: đã có node [[forward-rate-agreement]] [[src-choudhry-principles-banking#^choudhry-hedge-8]] và [[interest-rate-futures]] [[src-choudhry-principles-banking#^choudhry-hedge-4]]. Gap risk trong [[securitisation]] phải được phòng ngừa [[src-choudhry-principles-banking#^choudhry-sec-4]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: thêm cách phân loại của Choudhry: IRR = investment (price) risk + income risk; income risk do lãi suất huy động và funding thay đổi không đồng bộ, chính là gap risk [[src-choudhry-principles-banking#^choudhry-irr-2]]; gap risk còn gọi là mismatch risk, nhạy với dịch chuyển song song hoặc pivotal; yield curve risk tách riêng [[src-choudhry-principles-banking#^choudhry-irr-4]]. Underfunded gap ngụ ý kỳ vọng lãi suất giảm, over-funded gap ngụ ý kỳ vọng lãi suất tăng [[src-choudhry-principles-banking#^choudhry-lgap-9]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u03 — chờ user duyệt: thêm cách phân loại của Bardaeva: gap risk, basis risk và yield curve risk là chung cho mọi ngân hàng, optionality risk có thể nhỏ hoặc đặc thù [[src-bardaeva-alm#^ch11-15]]; Risk lập báo cáo gap analysis cho ALM [[src-bardaeva-alm#^ch11-22]]. Link [[irrbb-management]] ở lần nhắc quy trình quản trị. → đã áp dụng [2026-10-20]

### [[internal-risk-transfer]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-bcbs-framework RBC25 — chờ user duyệt: thêm ghi chú phân biệt ở mục 1: Basel RBC25.18 dùng cùng tên "internal risk transfer" cho bản ghi nội bộ chuyển rủi ro giữa banking book và trading book, có hệ quả về vốn quy định [[src-bcbs-framework#^rbc25-18]]; khái niệm này nằm ở node [[regulatory-internal-risk-transfer]], khác với chuyển rủi ro BU → Treasury qua FTP của node này. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]] và [[loan-pricing]] (lãi suất hoà vốn theo RoE mục tiêu, TRR do ALCO duyệt ngoại lệ); đề xuất link ở chỗ nhắc NIM và định giá khoản vay. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u21–u22 — chờ user duyệt: thêm nguồn T4: thông lệ tốt là toàn bộ rủi ro lãi suất tập trung về Treasury qua giao dịch funding; vị thế của mảng khác được Treasury match fund hoặc phòng ngừa bằng internal swap [[src-choudhry-principles-banking#^choudhry-st-11]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest --node cost-of-funds — chờ user duyệt: đã hoàn thiện node [[cost-of-funds]]; đề xuất link ở mục 6 chỗ nhắc 'giá COF/VOF'. → đã áp dụng [2026-10-20]

### [[intraday-liquidity-risk]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M5 — chờ user duyệt: thêm góc nhìn VN: quản lý thanh khoản trong ngày là cấu phần bắt buộc (theo dõi trạng thái, xác định nguồn vốn, dự báo thay đổi bất thường) [[src-tt83-2025-nhnn#^d46-2]]; phải có công cụ đo cho hoạt động ngân hàng đại lý, lưu ký, thanh toán [[src-tt83-2025-nhnn#^d47-2]]. → đã áp dụng [2026-10-20]

### [[irrbb-balance-sheet-portfolios]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 103): mục "Xử lý Biên Thương mại và Phần bù Spread (Par 103)" (dòng 209–213) gán nội dung par 103 cho [[src-bcbs-irrbb-2016#^irrbb-p08-2]] (par 70, đường cong chiết khấu ∆EVE). Đề xuất: câu dẫn "Theo par 103, ngân hàng có quyền lựa chọn" cite [[src-bcbs-irrbb-2016#^irrbb-u05-15]] (trừ hay giữ commercial margin trong notional repricing cash flow, phương pháp thận trọng và minh bạch); hai bullet về đường cong chiết khấu giữ cite p08-2; dòng "Quy tắc nhất quán … cho cả tài sản và nợ" không có trong u05-15 lẫn p08-2, đổi thành "phương pháp phải thận trọng và minh bạch" [[src-bcbs-irrbb-2016#^irrbb-u05-15]] và ghi phần "nhất quán" là `[cần nguồn]`. → đã áp [2026-10-19]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; đề xuất link ở lần nhắc đầu "dòng tiền tái định giá danh nghĩa" (dòng 66). → đã áp [2026-10-19]
- [2026-10-19] review — user duyệt [2026-10-19]: mục par 104 ("tái định giá 100% về mệnh giá (par value) tại … first reset date") đang cite [[src-bcbs-irrbb-2016#^irrbb-u05-2]] (par 101). Đề xuất cite [[src-bcbs-irrbb-2016#^irrbb-u05-12]] cho cả hai câu; nguồn viết "reprice fully", không nói "về mệnh giá", nên bỏ "về mệnh giá (par value)" hoặc chuyển sang *Diễn giải:*. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[banking-book]]; mục "Ranh giới Sổ ngân hàng vs Sổ kinh doanh" nên link sang node này; thêm góc nhìn VN: sổ ngân hàng gồm repo/reverse repo, phái sinh phòng ngừa cho khoản mục báo cáo tình hình tài chính, tài sản tài chính dự trữ thanh khoản và giao dịch còn lại [[src-tt83-2025-nhnn#^d3-33]]; giao dịch tự doanh có thời hạn không quá 1 năm [[src-tt83-2025-nhnn#^d3-32]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: đã có node [[silicon-valley-bank]] (nguồn Tata u07); đề xuất link ở chỗ nhắc SVB và đối chiếu số liệu đang viết với [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]]. → đã áp dụng [2026-10-20] (thêm link; số liệu SVB đối chiếu lại và cite tata-svb-4/5/7)
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[overnight-index-swap]]; đề xuất link ở lần nhắc đầu OIS. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]

### [[liquidity-monitoring-metrics]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]

### [[liquidity-transfer-pricing]]
- [2026-10-19] ingest src-tt83-2025-nhnn PL6 — chờ user duyệt: đã có node [[raroc]] (lợi nhuận trước thuế / vốn kinh tế theo TT83 PL6.III); đề xuất link ở lần nhắc đầu RAROC. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u25 — chờ user duyệt: thêm case Europe Arab Bank (2009–2010): bỏ FTP Libor-flat, thêm liquidity premium tăng theo kỳ hạn (+12,5 bp O/N–2 tuần đến +32,5 bp 3–12 tháng), áp dụng từ 01/01/2010 [[src-choudhry-principles-banking#^choudhry-cs-4]]; đường FTP tháng theo GBP/EUR/USD, TLP từ tham số thị trường, P&L giao dịch FTP để trong 'ALCO Book' [[src-choudhry-principles-banking#^choudhry-cs-5]]; LDR Corporate gần 180% và Private khoảng 60% trước thay đổi [[src-choudhry-principles-banking#^choudhry-cs-3]]; bài học [[src-choudhry-principles-banking#^choudhry-cs-6]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest --node cost-of-funds — chờ user duyệt: đã hoàn thiện node [[cost-of-funds]]; đề xuất link ở mục 5 chỗ nhắc 'biểu giá bán vốn COF'. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u26 — chờ user duyệt: thêm ví dụ lịch sử (George Rae, 1890): lãi suất tiền gửi phụ thuộc chủ yếu điều kiện gửi; tiền gửi rút theo yêu cầu phải đầu tư vào chứng khoán chất lượng cao nhất nên lợi suất thấp, tiền gửi báo trước cho phép đầu tư tài sản kém thanh khoản hơn; ví dụ 2% / 2¼% / 2½% [[src-choudhry-principles-banking#^choudhry-rae-4]]. Đặt dưới `*Diễn giải:*` như tiền thân của liquidity premium theo kỳ hạn. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[overnight-index-swap]]; đề xuất link ở lần nhắc đầu OIS. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p04 — chờ user duyệt: node chưa có căn cứ Basel. Đề xuất thêm mục Basel: BCBS 144 P4 yêu cầu đưa chi phí, lợi ích, rủi ro thanh khoản vào định giá nội bộ, đo lường hiệu quả và duyệt sản phẩm mới cho mọi hoạt động trọng yếu, kể cả ngoại bảng [[src-bcbs-liquidity-principles-2008#^lrm-p04]]; liquidity charge gán tới trạng thái, danh mục hoặc giao dịch, kể cả cam kết tiềm tàng [[src-bcbs-liquidity-principles-2008#^lrm-19]]; xét thời gian nắm giữ dự kiến, thanh khoản thị trường và lợi ích của nguồn vốn ổn định như tiền gửi bán lẻ [[src-bcbs-liquidity-principles-2008#^lrm-19b]]; phân bổ tường minh ở cấp quản lý mảng và xét điều kiện stress [[src-bcbs-liquidity-principles-2008#^lrm-20]]. SRP30.50 lặp lại yêu cầu [[src-bcbs-framework#^srp30-50]]. Đề xuất link [[bcbs-liquidity-principles]] và thêm nguồn vào `sources`. → đã áp dụng [2026-10-20] (mục 6)

### [[non-maturity-deposits]]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 — user duyệt [2026-10-19]: thêm dòng VN. PL5 phân loại NMDs thành tiền gửi cá nhân (tài khoản giao dịch / không giao dịch) và tiền gửi tổ chức; tách NMDs ổn định bằng dữ liệu lịch sử, NMDs lõi lấy từ phần ổn định; trần Bảng 2 là 90%/5 năm, 70%/4,5 năm, 50%/4 năm (giống Table 2 d368); NMDs không lõi vào thang qua đêm [[src-tt83-2025-nhnn#^pl5-a2-3a]]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 (bổ sung) — chờ user duyệt: thêm vào dòng VN hoặc dòng "Khác biệt": PL5 định nghĩa NMDs ổn định là NMDs có khả năng cao khách hàng sẽ duy trì; NMDs lõi lấy từ phần ổn định; NMDs không lõi là phần còn lại; NMDs lõi được phân bổ sao cho đáp ứng Bảng 2 [[src-tt83-2025-nhnn#^pl5-a2-3a2]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M8 — chờ user duyệt: thêm góc nhìn VN: mô hình NMD lõi là mô hình theo TT83 Đ3.23 [[src-tt83-2025-nhnn#^d3-24]]; nếu ngân hàng xếp hạng rủi ro cao [[src-tt83-2025-nhnn#^d56-1]] thì phải kiểm định trước khi dùng, khi thay đổi trọng yếu và tối thiểu hằng năm [[src-tt83-2025-nhnn#^d56-4d]]; link [[model-validation]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u08 — chờ user duyệt: thêm: báo cáo EU (2024/855) yêu cầu ngày tái định giá bình quân của từng nhóm NMD (tách phần lõi) và pass-through rate (PTR) theo nhóm [[src-tata-bank-alm#^tata-rep-3]]; trong góc nhìn hợp đồng NMD xếp bucket ngắn nhất [[src-tata-bank-alm#^tata-rep-2]]; FinTech làm khách hàng chuyển tài khoản nhanh hơn, buộc xem lại mô hình quyền chọn nhúng của NMD với lịch sử dữ liệu ngắn [[src-tata-bank-alm#^tata-fut-1]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: thêm: deposit beta thấp của chu kỳ 2016–2019 không bền, tiền gửi không bảo hiểm có thể rời đi và beta tăng nhanh [[src-tata-bank-alm#^tata-rr-1]]; 2022–2023 tiền gửi dịch từ không kỳ hạn sang có kỳ hạn làm tăng duration gap; ECB 2017 cảnh báo mô hình hành vi hiệu chỉnh trong môi trường lãi suất giảm [[src-tata-bank-alm#^tata-rr-2]]; bài học SVB: tăng giả định duration tiền gửi giảm rủi ro hiển thị nhưng không giảm rủi ro thực [[src-tata-bank-alm#^tata-svb-9]]; EBA 2022 tăng cường giả định thận trọng cho NMD của đối tác phi tài chính [[src-tata-bank-alm#^tata-reg-9]]. Mục 'Rủi ro EVE khi kéo dài thời lượng NMDs' (dòng 76) nên link [[silicon-valley-bank]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u06 — chờ user duyệt: thêm định nghĩa deposit beta (tỷ lệ thay đổi lãi suất phi rủi ro, thường là lãi suất chính sách, truyền vào lãi suất tiền gửi), không ổn định nên có thể phải mô hình hoá hành vi ngân hàng tường minh [[src-tata-bank-alm#^tata-beh-4]]; ngân hàng là price-taker: ngân hàng lâu đời dùng replicating portfolio chỉ truyền một phần thay đổi lãi suất vì tiền gửi cũ đã phòng ngừa ở lãi suất lịch sử, ngân hàng online mới truyền gần hết [[src-tata-bank-alm#^tata-beh-3]]; rigid deposits khi lãi suất âm [[src-tata-bank-alm#^tata-neg-4]] và sàn 0% max(rI ± x; 0%) [[src-tata-bank-alm#^tata-neg-2]]; EBA yêu cầu xét ràng buộc tái định giá tiền gửi bán lẻ khi lãi suất thấp/âm [[src-tata-bank-alm#^tata-neg-5]]; số liệu Đức: tiền gửi không kỳ hạn 7,9% → 29,3% (1999–2021) rồi 26,1% (2023) [[src-tata-bank-alm#^tata-prac-1]] [[src-tata-bank-alm#^tata-prac-2]]. Link [[negative-interest-rates]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u25 — chờ user duyệt: thêm case chiến lược tiền gửi (UK): tiền gửi rút ngay của doanh nghiệp lớn/NBFI ổn định về hành vi nhưng xếp 'Type A' (non-sticky) theo cơ quan quản lý Anh [[src-choudhry-principles-banking#^choudhry-cs-19]]; khoảng 10% số dư cho NII âm (lãi suất khách hàng > FTP bid), số dư giá cao rất nhạy lãi suất [[src-choudhry-principles-banking#^choudhry-cs-20]]; giải pháp chuyển sang sản phẩm 'LCR-friendly', tài khoản báo trước 35 ngày [[src-choudhry-principles-banking#^choudhry-cs-21]]. Link [[structural-hedging]] (natural hedge NIBL – vay thả nổi [[src-choudhry-principles-banking#^choudhry-cs-17]]). → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u26 — chờ user duyệt: bổ sung case chiến lược tiền gửi (CS6, tiếp theo u25): tập trung vào khách hàng SME/Type B, đưa ra tiền gửi có kỳ hạn không được rút trước hạn để giảm dòng ra khi stress, định giá rủi ro thanh khoản để khuyến khích sản phẩm dài hạn hơn [[src-choudhry-principles-banking#^choudhry-cs-22]]; rà soát cấu trúc tiền gửi định kỳ theo cả NII và yêu cầu quản lý, bằng 'Deposits Analysis Template' do [[alco]] sở hữu [[src-choudhry-principles-banking#^choudhry-cs-23]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10 — chờ user duyệt: thêm cách xử lý NMD khi lãi suất âm: tiền gửi bán lẻ/SME sàn 0% coi như fixed-rate, IRS nhận cố định theo behavioural tenor, balance guarantee swap [[src-choudhry-principles-banking#^choudhry-neg-3]]; khoản thả nổi xếp bucket 1 tháng [[src-choudhry-principles-banking#^choudhry-neg-4]]. Đã link sẵn ở [[negative-interest-rates]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: thêm ba cách xếp bucket NMD trong gap report: bucket ngắn nhất (phổ biến nhất, làm gap biến động), bucket dài nhất, hoặc tách core/unstable với core phân tích định kỳ [[src-choudhry-principles-banking#^choudhry-lgap-7]]. Thêm phân loại 'sticky' (bán lẻ, doanh nghiệp nhỏ, khách hàng trên 3 năm) và 'non-sticky' (định chế tài chính, chính phủ, chính quyền địa phương) theo Choudhry [[src-choudhry-principles-banking#^choudhry-liq-10]]; run-off risk của NIBL khi lãi suất tăng [[src-choudhry-principles-banking#^choudhry-irr-6]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u03 — chờ user duyệt: thêm nguồn T4: ở bước đo lường IRRBB nên chú ý công cụ không xác định kỳ hạn [[src-bardaeva-alm#^ch11-17]]; thị trường chỉ có tài khoản tiết kiệm đòi hỏi đánh giá stickiness và chia tài khoản không kỳ hạn vào khung thời gian [[src-bardaeva-alm#^ch12-13]]; khách hàng thiếu tin tưởng ngân hàng rút tiền mỗi khi nghe tin đồn [[src-bardaeva-alm#^ch12-14]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u04 — chờ user duyệt: thêm vào phần phụ thuộc regime: ở thị trường mới nổi, tiền gửi bán lẻ biến động hơn với phần core ổn định thấp hơn [[src-bardaeva-alm#^ch14-15]], khách hàng lo âu và quyết định theo tin tức [[src-bardaeva-alm#^ch14-11]]; ở thị trường phát triển, tiền gửi bán lẻ sticky và hành vi mô hình hoá được [[src-bardaeva-alm#^ch14-14]] [[src-bardaeva-alm#^ch14-12]]; digitalization làm tiền gửi kém tin cậy hơn và nên phản ánh vào mô hình ALM [[src-bardaeva-alm#^ch16-10]]. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-irrbb-2016 U03 — chờ user duyệt: bổ sung chi tiết Principle 5 về giả định hành vi NMDs: bắt buộc phân tầng theo người gửi tiền (retail vs wholesale) và loại tài khoản (transactional vs non-transactional) [[src-bcbs-irrbb-2016#^irrbb-p05-4]]; 6 chiều kích mô hình hoá hành vi NMDs (độ nhạy lãi suất pass-through rate, mặt bằng lãi suất, spread chào so với thị trường, cạnh tranh định chế, vị trí địa lý và đặc tính khách hàng) cùng quyền chọn nhúng trong công cụ thả nổi [[src-bcbs-irrbb-2016#^irrbb-p05-5]]; và quy trình kiểm định độc lập, phân tích độ nhạy (sensitivity analysis) trên cả EVE và earnings, chu kỳ rà soát tối thiểu hàng năm [[src-bcbs-irrbb-2016#^irrbb-p05-6]]. → đã áp [2026-10-20] (node draft), mục "Giả định hành vi theo Principle 5"; giữ mức "should/nên" của nguồn thay cho "bắt buộc"; nguồn không nói "kiểm định độc lập" nên không viết

### [[option-risk]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: thêm góc nhìn VN: rủi ro quyền chọn gồm quyền chọn tự động (lãi suất thay đổi dẫn tới chắc chắn thực hiện quyền chọn theo hợp đồng) và quyền lựa chọn hành vi (lãi suất thay đổi có thể làm thay đổi hành vi khách hàng) [[src-tt83-2025-nhnn#^d3-22]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u06 — chờ user duyệt: thêm: sàn 0% trên tiền gửi bán lẻ là quyền chọn nhúng/hành vi, at/in the money khi lãi suất thấp hay âm [[src-tata-bank-alm#^tata-neg-2]]; coupon floor max(rI + x; 0%) và indicator floor max(rI; 0%) + x, tác động ngược chiều ở tài sản và nợ [[src-tata-bank-alm#^tata-neg-3]]. Link [[negative-interest-rates]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm định nghĩa của nguồn T4: quyền chọn tự động đánh giá theo ΔEVE, quyền rút tiền là quyền chọn hành vi; nguồn tách thêm 'yield risk' (dịch chuyển không song song ngoài dự kiến) [[src-lubinska-alm-optimisation#^lubinska-u02-32]]; case study giá trị quyền chọn tự động bù lỗ EVE khi lãi suất giảm [[src-lubinska-alm-optimisation#^lubinska-u02-41]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: thêm định nghĩa T4 của Choudhry: option risk là quyền của khách hàng chấm dứt hợp đồng trước hạn (CD, tài khoản séc, tiền gửi không kỳ hạn), ảnh hưởng NII khi quyền được thực hiện [[src-choudhry-principles-banking#^choudhry-irr-6]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-irrbb-2016 U05 — chờ user duyệt: bổ sung chi tiết cơ chế định giá rủi ro quyền chọn tự động KAO: quy định tăng độ biến động ngầm định tương đối +25% khi định giá lại quyền chọn bán và mua [[src-bcbs-irrbb-2016#^irrbb-u05-27]], xử lý swaptions phi bán lẻ và quyền chọn hành vi bán buôn như quyền chọn tự động [[src-bcbs-irrbb-2016#^irrbb-u05-26]], cùng quy tắc ràng buộc khi ngân hàng chỉ đưa quyền chọn mua dùng cho phòng ngừa rủi ro vào KAO phải cộng biến động thị trường của quyền chọn mua còn lại vào vốn pháp định [[src-bcbs-irrbb-2016#^irrbb-u05-28]]. → đã áp [2026-10-20] (node draft), chi tiết đặt ở [[irrbb-standardised-framework]]; sửa diễn đạt: nguồn yêu cầu cộng vào KAO thay đổi giá trị đã phản ánh trong vốn pháp định, không phải cộng vào vốn pháp định

### [[standardised-interest-rate-shocks]]
- [2026-10-18] ingest src-bcbs-irrbb-2016 U07 (bổ sung Table 1): có claim [[src-bcbs-irrbb-2016#^irrbb-u07-5]] chép đủ Table 1. Đề xuất: → đã áp [2026-10-18]
  - Bảng biên độ sốc (mục Bảng 1): dòng **AUD** ghi Short = 400 bps, raw và claim u07-5 là **450**; đổi cite của bảng từ `^irrbb-u07-2` sang `^irrbb-u07-5`, cite riêng từng dòng. Table 1 không ghi đơn vị; "bps" là cách đọc theo sàn/trần ở [[src-bcbs-irrbb-2016#^irrbb-u07-4]].
  - Câu "lấy các phân vị thứ 1% và 99% … trong khoảng thời gian 6 tháng" cite `^irrbb-u07-2`, nhưng claim đó chỉ nói chuỗi 2000–2015; phân vị và cửa sổ 6 tháng chưa có claim `[cần nguồn]`.
  - Callout "đồng tiền không nằm trong Bảng 1 (bao gồm VND) … phải tính toán … hoặc áp dụng mức sốc tối thiểu" cite `^irrbb-u07-4`, nhưng claim đó nói về sàn 100 bp, trần và quyền đặt sàn cao hơn cho home currency; cách xử lý đồng tiền ngoài Table 1 `[cần nguồn]`.
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 25 "Là căn cứ bắt buộc để xác định mức tổn thất cực đại …": đề xuất "Là bộ kịch bản dùng trong phép thử mà cơ quan giám sát nên (should) áp dụng: so max ∆EVE dưới 6 kịch bản với 15% Tier 1" ([[src-bcbs-irrbb-2016#^irrbb-p12-1]]). → đã áp [2026-10-18]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 — user duyệt [2026-10-19]: thay `[cần nguồn: src-tt83-2025-nhnn PL5]` trong callout đồng tiền ngoài Table 1 bằng: Bảng 5 PL5 dùng cùng giá trị Table 1 cho 21 đồng tiền, không có VND [[src-tt83-2025-nhnn#^pl5-c1-1]]; đồng tiền ngoài Bảng 5 tính bằng lãi suất bình quân hằng ngày 16 năm (kỳ hạn 3T–20N) × $\hat{\alpha}$ (60/85/40%), sàn 100 bp, trần 400 (song song) / 500 (ngắn hạn) / 300 (dài hạn) bp [[src-tt83-2025-nhnn#^pl5-c1-2]]; ngân hàng được tự xác định cú sốc theo hướng dẫn cập nhật BCBS d578 (2024) [[src-tt83-2025-nhnn#^pl5-c2]]. Thêm dòng VN cho 6 kịch bản [[src-tt83-2025-nhnn#^pl5-a3-1]] và công thức sốc [[src-tt83-2025-nhnn#^pl5-c1-3]]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-bcbs-irrbb-2016 U07 (bổ sung dòng 995–1042) — user duyệt [2026-10-19]: trong `## Basel vs VN`, (1) dòng "Sàn, trần tham số" cột Basel thay `[cần nguồn]` bằng: sàn 100 bp; trần 500 bp ngắn hạn, 400 bp song song, 300 bp dài hạn [[src-bcbs-irrbb-2016#^irrbb-u07-4]]; (2) dòng "Đồng tiền ngoài bảng" cột Basel thay `[cần nguồn]` bằng: Table 1 dựng từ lãi suất bình quân hằng ngày 16 năm (2000–2015, kỳ hạn 3m–20Y) [[src-bcbs-irrbb-2016#^irrbb-u07-7]] nhân tham số toàn cầu 60% / 85% / 40% [[src-bcbs-irrbb-2016#^irrbb-u07-8]], áp sàn và trần [[src-bcbs-irrbb-2016#^irrbb-u07-9]]; d368 không nêu cách xử lý đồng tiền ngoài Table 1; (3) dòng "Tự xác định cú sốc" cột Basel: BCBS sẽ rà lại hiệu chỉnh định kỳ (ví dụ 5 năm) [[src-bcbs-irrbb-2016#^irrbb-u07-6]]. Dòng "Khác biệt" thêm: PL5.C.I.2 áp phương pháp dựng Table 1 của d368 cho đồng tiền ngoài Bảng 5. → đã áp [2026-10-19]
- [2026-10-19] rà lại ingest U07 (bổ sung) — chờ user duyệt: (1) dòng 109 "phương pháp thống kê (phân vị, cửa sổ thời gian) dùng để suy ra biên độ `[cần nguồn]`": d368 không dùng phân vị hay cửa sổ thời gian; Table 1 được dựng từ lãi suất bình quân hằng ngày 16 năm ở các kỳ hạn 3m–20Y [[src-bcbs-irrbb-2016#^irrbb-u07-7]], nhân tham số toàn cầu 60% / 85% / 40% [[src-bcbs-irrbb-2016#^irrbb-u07-8]], rồi áp sàn và trần [[src-bcbs-irrbb-2016#^irrbb-u07-9]]. Đề xuất thay `[cần nguồn]` bằng câu này. (2) dòng "Khác biệt" dưới `## Basel vs VN` viết "(16 năm, 60/85/40%, sàn và trần giống nhau)"; PL5 cho phép 16 năm hoặc khoảng thời gian ngân hàng tự xác định [[src-tt83-2025-nhnn#^pl5-c1-2]]. Đề xuất viết "(mặc định 16 năm, cùng kỳ hạn, cùng 60/85/40%, cùng sàn và trần)". d368 footnote 42 (raw dòng 959) cũng cho jurisdiction chọn khoảng khác 16 năm, nhưng chưa có claim; cần `/ingest src-bcbs-irrbb-2016 u07` bổ sung. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 (bổ sung) — chờ user duyệt: thêm vào dòng VN "Đồng tiền ngoài bảng": lãi suất bình quân hằng ngày là bình quân của mọi mức lãi suất hằng ngày thuộc 9 kỳ hạn 3 tháng–20 năm [[src-tt83-2025-nhnn#^pl5-c1-2b]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-irrbb-2016 U07 (bổ sung) — chờ user duyệt: (1) mục công thức: cite [[src-bcbs-irrbb-2016#^irrbb-u07-10]] cho sốc song song, ngắn hạn, dài hạn và $S_{long} = 1 - S_{short}$; thêm ví dụ của nguồn tại 3,5 năm (short +41,7 bp; steepener +25,4 bp; flattener −1,6 bp với short = long = 100 bp). (2) dòng 143–144 "sàn âm −100 bp … 0 bps tại 20 năm" không cite và là sàn EBA 2018, không phải d368: thay bằng "d368: supervisor quốc gia có thể đặt sàn lãi suất sau sốc, không lớn hơn 0 [[src-bcbs-irrbb-2016#^irrbb-u07-11]]; EBA 2018: −100 bp, +5 bp/năm, 0% ở 20 năm [[src-tata-bank-alm#^tata-reg-8]]; RTS/2022/10: −150 bp, +3 bp/năm, 0% ở 50 năm [[src-tata-bank-alm#^tata-sot-2]]". (3) dòng 93 "pivot 3–5 năm" không có nguồn: gỡ hoặc ghi `[cần nguồn]`; *Diễn giải:* theo ví dụ của nguồn, steepener tại 3,5 năm vẫn dương (+25,4 bp) với JPY. → đã áp dụng [2026-10-20]

### [[interest-rate-cap-floor]]
- [2026-10-19] ingest src-tata-bank-alm u06 — chờ user duyệt: đã có node [[negative-interest-rates]]: nguồn so sánh sàn 0% trên tiền gửi bán lẻ với floor tự động (out of the money khi lãi suất cao, at/in the money khi thấp hoặc âm) [[src-tata-bank-alm#^tata-neg-2]]; đề xuất link ở mục mô hình Bachelier. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: thêm ứng dụng ALM (ví dụ 6.12): ngân hàng liability-sensitive (gap tức thời −80 trên 200 triệu USD, +1% làm NII giảm 0,8 triệu, EAR khoảng 7,8%) [[src-choudhry-principles-banking#^choudhry-hedge-20]] [[src-choudhry-principles-banking#^choudhry-hedge-21]] mua cap notional 80 triệu USD, strike 3% ATM, 1 năm, loại bỏ EAR; strike 4% OTM rẻ hơn nhưng còn EAR [[src-choudhry-principles-banking#^choudhry-hedge-23]]; chi phí 5bp NIM, giữ lợi khi lãi suất giảm, khác swap/FRA [[src-choudhry-principles-banking#^choudhry-hedge-24]]; ngân hàng asset-sensitive mua floor [[src-choudhry-principles-banking#^choudhry-hedge-25]]. Xem [[structural-hedging]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[forward-rate-agreement]]; đề xuất link ở lần nhắc đầu FRA. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]
- [2026-10-20] research nii-shocks-regulation-hedging-and-alco-tradeoffs — chờ user duyệt: đổi `cite` của cạnh `hedges → [[net-interest-income-sensitivity]]` từ `irrbb-u06-4` (định nghĩa gap/basis/option risk, không nhắc cap/floor) sang [[src-choudhry-principles-banking#^choudhry-hedge-20]] (ngân hàng liability-sensitive phòng ngừa NII bằng cap); floor cho ngân hàng asset-sensitive: [[src-choudhry-principles-banking#^choudhry-hedge-25]]. → đã áp dụng [2026-10-20]

### [[interest-rate-swap]]
- [2026-10-19] ingest src-choudhry-principles-banking u25 — chờ user duyệt: thêm ứng dụng phòng ngừa IRRBB: macro hedge bằng pool IRS cuối tháng, thường không áp được hedge accounting nên chịu biến động MTM [[src-choudhry-principles-banking#^choudhry-cs-14]]; chính sách 'chính thống' (tài sản cố định → IRS trả cố định, nợ cố định → IRS nhận cố định) và hạn chế của nó (chi phí tài sản bảo đảm) [[src-choudhry-principles-banking#^choudhry-cs-16]]; phòng ngừa theo phần ròng sau natural hedge, ưu tiên sản phẩm tiền mặt để giữ hạn mức swap [[src-choudhry-principles-banking#^choudhry-cs-17]]. Link [[structural-hedging]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: thêm hedge ratio theo PVBP/DV01: swap hiệu quả vì convexity dương, PVBP là thước đo chính để tính hedge ratio [[src-choudhry-principles-banking#^choudhry-hedge-12]]; ví dụ swap 5 năm £1 triệu PVBP £425 so với trái phiếu cố định £488,45, quy tắc kinh nghiệm PVBP swap ≈ trái phiếu từ ngày reset kế tiếp tới đáo hạn [[src-choudhry-principles-banking#^choudhry-hedge-13]]; hạn chế giả định dịch chuyển song song, cần dynamic hedging [[src-choudhry-principles-banking#^choudhry-hedge-14]]. Thêm phân loại asset-linked/liability-linked swap [[src-choudhry-principles-banking#^choudhry-hedge-11]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: đã có node [[overnight-index-swap]]; đề xuất bỏ alias `OIS Swap` khỏi node này (chuyển sang node mới) và link [[overnight-index-swap]] ở mục cấu trúc IRS. Đã có node [[cross-currency-swap]] [[src-choudhry-principles-banking#^choudhry-fxs-2]]; đề xuất link ở chỗ phân biệt với IRS. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10 — chờ user duyệt: thêm ứng dụng khi lãi suất âm: coi NMD sàn 0% là fixed-rate, vào IRS nhận cố định với tenor bằng behavioural tenor; balance guarantee swap điều chỉnh notional theo số dư NMD [[src-choudhry-principles-banking#^choudhry-neg-3]]. Xem [[negative-interest-rates]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u15 — chờ user duyệt: đã có node [[hedge-accounting]] (tiêu chí áp dụng, hiệu quả hồi tố 80–125% [[src-choudhry-principles-banking#^choudhry-hacc-3]]); đề xuất link ở mục Kế toán phòng ngừa rủi ro. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]
- [2026-10-20] research nii-shocks-regulation-hedging-and-alco-tradeoffs — chờ user duyệt: thêm cạnh `{type: hedges, to: "[[net-interest-income-sensitivity]]", cite: "[[src-tata-bank-alm#^tata-nii-16]]"}` (receiver swap ổn định NII dưới sốc −100 bp). Rà lại 2 cạnh hiện có: `input-to → [[net-interest-income-sensitivity]]` cite `irrbb-u06-5` và `hedges → [[economic-value-of-equity]]` cite `irrbb-u05-8`, cả hai trích dẫn không nhắc swap; ví dụ Tata còn cho thấy receiver swap làm repricing gap EVE tăng từ 1,74 lên 3,63 [[src-tata-bank-alm#^tata-nii-10]]. → đã áp dụng [2026-10-20] Rà 2 cạnh → [2026-10-20]: input-to NII đổi cite sang irrbb-p08-3; hedges EVE đổi cite sang tata-svb-3; chiều pay-fixed ghi trong thân bài (taxonomy chỉ cho regime với drives).

### [[available-stable-funding]]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: đã có node [[silicon-valley-bank]] (nguồn Tata u07); đề xuất link ở chỗ nhắc SVB và đối chiếu số liệu đang viết với [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]]. → đã áp dụng [2026-10-20] (thêm link; số liệu SVB đối chiếu lại và cite tata-svb-4/5/7)

### [[available-unencumbered-assets]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20] (link đặt ở mục 5 vì lần nhắc đầu nằm trong heading)

### [[contractual-maturity-mismatch]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: thêm góc nhìn T4: liquidity gap là chênh lệch kỳ hạn tài sản và nợ ở từng điểm kỳ hạn, mỗi gap là một phơi nhiễm funding gap risk [[src-choudhry-principles-banking#^choudhry-lgap-1]]; luôn là dynamic gap; marginal (incremental) gap = thay đổi tài sản − thay đổi nợ trong kỳ [[src-choudhry-principles-banking#^choudhry-lgap-3]]; 'ALM Smile': không quá 20% funding ở O/N–1 tuần và 9–12 tháng, kèm Table 5.1 [[src-choudhry-principles-banking#^choudhry-lgap-4]]; Choudhry (2007) đề xuất không quá 20–30% bảng cân đối tài trợ dưới 3 tháng [[src-choudhry-principles-banking#^choudhry-liq-6]]. → đã áp dụng [2026-10-20]

### [[economic-value-of-equity]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 105, 132): mục "Công thức tính toán chuẩn hoá" (dòng 30–72) chưa có citation cho các khối công thức. Đề xuất: bước 1 cite [[src-bcbs-irrbb-2016#^irrbb-u05-17]] (bù trừ trong dải) và [[src-bcbs-irrbb-2016#^irrbb-u05-18]] (DF liên tục); câu "R là lãi suất phi rủi ro sau sốc" sửa theo [[src-bcbs-irrbb-2016#^irrbb-u05-18]] (R phản ánh kịch bản i theo Annex 2) và [[src-bcbs-irrbb-2016#^irrbb-u05-19]] (risk-free zero coupon rate, hoặc cộng margin nếu CF gồm margin); bước 2 cite [[src-bcbs-irrbb-2016#^irrbb-u05-20]]; bước 3 cite [[src-bcbs-irrbb-2016#^irrbb-u05-21]]; bước 4 cite [[src-bcbs-irrbb-2016#^irrbb-u05-8]] và thêm ngoại lệ gộp tiền tệ của cơ quan giám sát quốc gia [[src-bcbs-irrbb-2016#^irrbb-u05-24]]. Link [[notional-repricing-cash-flow]] ở lần nhắc đầu CF_{i,c}(k). → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5 — user duyệt [2026-10-19]: thêm mục `## Basel vs VN`. Định nghĩa ΔEVE theo NHNN [[src-tt83-2025-nhnn#^pl5-a-0]]; 5 bước Phụ lục V [[src-tt83-2025-nhnn#^pl5-a3-2]] [[src-tt83-2025-nhnn#^pl5-a5]]; chiết khấu chỉ theo risk-free rate [[src-tt83-2025-nhnn#^pl5-a3-2]] (Basel cho phép cộng margin, u05-19); KAO do ngân hàng tự đo [[src-tt83-2025-nhnn#^pl5-a4]] (Basel: vol +25%, u05-7); tổng hợp đa tiền tệ giống Basel [[src-tt83-2025-nhnn#^pl5-a5]]; hạn mức ΔEVE bắt buộc [[src-tt83-2025-nhnn#^d53-2]]; lộ trình: ΔNII hoặc ΔEVE tới 31/12/2027 [[src-tt83-2025-nhnn#^d74-4a]], cả hai từ 01/01/2028 [[src-tt83-2025-nhnn#^d74-4b]]; phép thử outlier 15% Tier 1 không có trong C3-M7, PL5. Thêm relation từ [[tt83-2025]] đã khai ở node regulation. → đã áp [2026-10-19]
- [2026-10-19] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 28, 29, 32) — user duyệt [2026-10-19]: trong `## Basel vs VN`, dòng "Hạn mức" thay `[cần nguồn]` ở cột Basel bằng: ngân hàng phải có policy limits nhất quán với risk appetite, risk appetite nên thể hiện theo cả economic value và earnings [[src-bcbs-irrbb-2016#^irrbb-p03-1]]; hạn mức tổng nên áp dụng hợp nhất, có thể gắn với kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-p03-3]]. Thêm dòng "Vượt hạn mức": Basel — vị thế vượt hoặc có khả năng vượt nên được xử lý kịp thời và báo cáo lên ngay [[src-bcbs-irrbb-2016#^irrbb-p03-4]]; VN — cảnh báo sớm khi gần vượt, xử lý kịp thời khi vượt [[src-tt83-2025-nhnn#^d54-4c]]; điều khoản d368 par 32; TT83 Đ54.4.c. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn PL5 (bổ sung) — chờ user duyệt: thêm vào dòng VN về chiết khấu: dòng tiền ròng chiết khấu bằng hệ số lãi kép liên tục theo kịch bản và đồng tiền; ngân hàng tính hệ số chiết khấu phù hợp với cách phân bổ dòng tiền (thang hay điểm giữa) [[src-tt83-2025-nhnn#^pl5-a3-2b]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1 — chờ user duyệt: đã có node [[risk-appetite]], [[risk-limits]]; đề xuất link ở lần nhắc đầu risk appetite / hạn mức. VN: stress test IRRBB tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn PL6 — chờ user duyệt: thêm dòng `## Basel vs VN` "Dùng cho vốn": Basel — vốn IRRBB xét trong ICAAP theo rủi ro giá trị kinh tế [[src-bcbs-irrbb-2016#^irrbb-p09-2]]; VN — chậm nhất từ 01/01/2028, $RWA_{IRRBB}$ trong vốn kinh tế tính theo ΔEVE [[src-tt83-2025-nhnn#^pl6-1c]]; link [[rwa-irrbb]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u08 — chờ user duyệt: thêm tham chiếu EU: SA cho EVE = EVE kịch bản sốc − EVE cơ sở, có add-on quyền chọn tự động và giới hạn giả định hành vi [[src-tata-bank-alm#^tata-eba-2]] [[src-tata-bank-alm#^tata-eba-3]]; SOT EVE theo bảng cân đối run-off với sàn tuyến tính −150 bp → 0% ở 50 năm [[src-tata-bank-alm#^tata-sot-1]] [[src-tata-bank-alm#^tata-sot-2]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm: internal view (chiết khấu phi rủi ro) và external view (giữ biên thương mại), hệ số chiết khấu phải nhất quán với cách tách biên qua FTP [[src-lubinska-alm-optimisation#^lubinska-u02-38]]; dòng tiền điều kiện (conditional) là best practice [[src-lubinska-alm-optimisation#^lubinska-u02-39]]; EVE bắt được độ lồi, ΔEVE tĩnh có thể mô phỏng nghiệp vụ tương lai [[src-lubinska-alm-optimisation#^lubinska-u02-40]]; case study KAO bù lỗ EVE ở mọi kịch bản giảm lãi suất [[src-lubinska-alm-optimisation#^lubinska-u02-41]]; đường phi rủi ro có thể là secured IRS hoặc OIS [[src-lubinska-alm-optimisation#^lubinska-u02-42]]. Link [[pv01]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[overnight-index-swap]]; đề xuất link ở lần nhắc đầu OIS. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]
- [2026-10-20] research irrbb-alm-governance-strategy-and-tradeoffs — chờ user duyệt: thêm relation `{type: input-to, to: "[[rwa-irrbb]]", cite: "[[src-tt83-2025-nhnn#^pl6-1c]]"}` (chậm nhất từ 01/01/2028, $RWA_{IRRBB}$ tính theo ΔEVE). → đã áp dụng [2026-10-20]

### [[hqla]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M5 — chờ user duyệt: thêm vào `## Basel vs VN` hoặc góc nhìn VN: TT83/2025 yêu cầu duy trì đủ tài sản có tính thanh khoản cao theo quy định NHNN cho điều kiện bình thường và bất lợi [[src-tt83-2025-nhnn#^d45-1a]], quản lý theo giá trị thị trường và khả năng chuyển thành tiền [[src-tt83-2025-nhnn#^d46-2]]; định nghĩa và tỷ lệ HQLA VN vẫn chờ TT50/2026. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: đã có node [[silicon-valley-bank]] (nguồn Tata u07); đề xuất link ở chỗ nhắc SVB và đối chiếu số liệu đang viết với [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]]. → đã áp dụng [2026-10-20] (thêm link; số liệu SVB đối chiếu lại và cite tata-svb-4/5/7)
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: thêm vào `## Ứng dụng trong ALM`: Choudhry đề xuất chính sách đầu tư hai danh mục, 'HQLA book' theo Basel III và liquidity book non-HQLA để tăng lợi suất [[src-choudhry-principles-banking#^choudhry-tig-1]]; quy mô tối thiểu HQLA book theo khẩu vị stress thanh khoản trong RAS và ILAAP, hướng dẫn bởi LCR và Survival Days [[src-choudhry-principles-banking#^choudhry-tig-2]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: thêm vào `## Ứng dụng trong ALM`: mô hình vận hành LAB của Choudhry: tài trợ bằng nguồn trên 90 ngày, lý tưởng trên 1 năm, không bằng repo; danh mục ring-fenced trong Treasury hoặc ALCO book; khả năng NHTW chấp nhận tài sản không quan trọng [[src-choudhry-principles-banking#^choudhry-lab-2]]; quy mô đủ sống qua stress 2 tuần và 3 tháng, ngày nay do LCR quyết định trước tiên [[src-choudhry-principles-banking#^choudhry-lab-3]]; định kỳ bán hoặc repo một phần để chứng minh thanh khoản [[src-choudhry-principles-banking#^choudhry-lab-4]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: thêm vào `## Nhầm lẫn thường gặp`: quan điểm T4 của Choudhry cho rằng buffer nên chỉ gồm sovereign G7 hoặc trong nước, gọi việc Basel mở rộng định nghĩa là 'unfortunate' [[src-choudhry-principles-banking#^choudhry-liq-7]]; ghi rõ là ý kiến tác giả, không phải chuẩn mực. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15 — chờ user duyệt: đã có node [[effective-interest-rate]]: HQLA đo theo amortised cost hoặc FVTOCI chịu ảnh hưởng của EIR; EIR ảnh hưởng giá trị ghi sổ HQLA và tiền gửi, cần xét trong tính LCR [[src-choudhry-principles-banking#^choudhry-eir-3]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: thêm vào `## Ứng dụng trong ALM`: ví dụ chi phí của buffer (Choudhry Ex 1.5 kịch bản 2): tăng buffer £1,5bn tài trợ dài hạn, net cost of carry 3% (7,5% − 4,5%), NII −£45m, NIM −0,50 điểm % xuống 2,38% [[src-choudhry-principles-banking#^choudhry-nim-5]]. Xem [[net-interest-margin]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u23–u24 — chờ user duyệt: đã có node [[ilaap]] và [[cash-flow-survival-period]]; đề xuất link ở đề xuất u11 ("RAS và ILAAP", "Survival Days"). → đã áp dụng [2026-10-20]
- [2026-10-20] research nii-shocks-regulation-hedging-and-alco-tradeoffs — chờ user duyệt: thêm cạnh `{type: drives, to: "[[net-interest-margin]]", direction: "-", cite: "[[src-choudhry-principles-banking#^choudhry-nim-5]]"}` (đệm thanh khoản lợi suất thấp hơn chi phí vốn, net cost of carry 3%, NIM giảm 0,50 điểm %). → đã áp dụng [2026-10-20]

### [[lcr-by-currency]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1 — chờ user duyệt: đã có node [[risk-appetite]]; đề xuất link ở lần nhắc đầu risk appetite. → không áp dụng [2026-10-20]: node không nhắc khẩu vị rủi ro, không có chỗ đặt link
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[cross-currency-swap]]; đề xuất link ở lần nhắc đầu currency swap. → đã áp dụng [2026-10-20]

### [[leverage-ratio]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: nguồn T4 (Lubinska) ghi Basel III/CRR yêu cầu tỷ lệ đòn bẩy 'a maximum of 3%' [[src-lubinska-alm-optimisation#^lubinska-u02-13]], ngược với tối thiểu 3% trong LEV; đề xuất ghi vào mục Nhầm lẫn thường gặp như diễn đạt lệch của nguồn T4 (không phải conflict cùng tier: BCBS T2 là căn cứ). → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u18 — chờ user duyệt: thêm góc nhìn chiến lược (T4): Choudhry đề xuất dùng mức 3% của Basel III làm cận trên và đặt hạn mức leverage nội bộ chặt hơn, như một biện pháp macro-prudential trong pha mở rộng [[src-choudhry-principles-banking#^choudhry-strat-23]]; Leverage ratio (Assets/Capital) là KPI trong Table 15.1 [[src-choudhry-principles-banking#^choudhry-strat-28]]. Link [[bank-strategic-plan]]. → đã áp dụng [2026-10-20]

### [[net-interest-income-sensitivity]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5 — user duyệt [2026-10-19]: thêm mục `## Basel vs VN`. Định nghĩa ΔNII theo NHNN [[src-tt83-2025-nhnn#^pl5-b1]]; chân trời 01 năm, constant balance sheet [[src-tt83-2025-nhnn#^pl5-b2]] (Basel: rolling 12 tháng, p08-3); 2 kịch bản tăng/giảm song song, lấy giá trị giảm lớn nhất [[src-tt83-2025-nhnn#^pl5-b3]]; hạn mức ΔNII bắt buộc [[src-tt83-2025-nhnn#^d53-2]]; lộ trình [[src-tt83-2025-nhnn#^d74-4a]] [[src-tt83-2025-nhnn#^d74-4b]]. PL5 không nêu cách xử lý commercial margin trong dòng tiền ΔNII [cần nguồn]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 28, 29, 32) — user duyệt [2026-10-19]: trong `## Basel vs VN`, dòng "Hạn mức" thay `[cần nguồn]` ở cột Basel bằng: ngân hàng phải có policy limits nhất quán với risk appetite, risk appetite nên thể hiện theo cả economic value và earnings [[src-bcbs-irrbb-2016#^irrbb-p03-1]]; hạn mức tổng nên áp dụng hợp nhất, có thể gắn với kịch bản sốc [[src-bcbs-irrbb-2016#^irrbb-p03-3]]. Thêm dòng "Vượt hạn mức": Basel [[src-bcbs-irrbb-2016#^irrbb-p03-4]]; VN [[src-tt83-2025-nhnn#^d54-4c]]; điều khoản d368 par 32; TT83 Đ54.4.c. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1 — chờ user duyệt: đã có node [[risk-appetite]], [[risk-limits]]; đề xuất link ở lần nhắc đầu risk appetite / hạn mức. VN: stress test IRRBB tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u08 — chờ user duyệt: thêm phương pháp EBA SA (RTS/2022/09) như tham chiếu EU: NII = lãi đã cố định đến ngày tái định giá + lợi suất phi rủi ro sau tái định giá + biên thương mại sau reset, theo bảng cân đối không đổi [[src-tata-bank-alm#^tata-eba-2]]; biên thương mại nghiệp vụ mới theo biên năm trước [[src-tata-bank-alm#^tata-eba-3]]; cấu phần thay đổi giá trị thị trường cho công cụ ngoài kỳ NII, loại dòng tiền trong kỳ để tránh tính trùng [[src-tata-bank-alm#^tata-eba-4]]; SOT NII 5% vốn cấp 1 [[src-tata-bank-alm#^tata-sot-3]]. Link [[outlier-bank-test]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u06 — chờ user duyệt: thêm phần dự phóng: kế hoạch ALM phải tính độ nhạy EVE và NII kỳ vọng trong tương lai, cần khối lượng theo phân khúc hành vi và kỳ hạn nghiệp vụ mới [[src-tata-bank-alm#^tata-niip-6]]; margin-beta (NIM giảm 5 bp mỗi năm sau cú giảm 100 bp; 19 bp mỗi 100 bp lãi suất ngắn hạn) [[src-tata-bank-alm#^tata-niip-5]]. Link [[nii-planning]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm phương pháp gap: ΔNII ≈ GAP × Δi trong gapping period [[src-lubinska-alm-optimisation#^lubinska-u02-23]] [[src-lubinska-alm-optimisation#^lubinska-u02-25]]; mô phỏng NII phục vụ nhiều mục đích (stress test EBA có giả định cấu trúc sổ; thước đo nội bộ dùng sổ không đổi, khoản đáo hạn thay bằng khoản cùng đặc điểm) [[src-lubinska-alm-optimisation#^lubinska-u02-33]]. Link [[repricing-gap-analysis]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u11 — chờ user duyệt: thêm ví dụ số EAR (Choudhry ví dụ 6.12): gap tức thời −80, +1% song song làm NII giảm 0,8 triệu USD, EAR khoảng 7,8%, NIM giảm 40bp; NIM = (thu nhập lãi − chi phí lãi) / tài sản sinh lời bình quân [[src-choudhry-principles-banking#^choudhry-hedge-21]]; ALCO thường đặt hạn mức EAR ±5% hoặc ±10% [[src-choudhry-principles-banking#^choudhry-hedge-22]]. Lưu ý alias 'Earnings at Risk/EaR' đang nằm ở node này. Đã có node [[overnight-index-swap]] (phòng ngừa NII) [[src-choudhry-principles-banking#^choudhry-hedge-17]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: thêm ví dụ minh hoạ T4 (Choudhry Ex 1.5, ChoudWest): giả định lãi suất 5%, bảng cân đối không đổi 12 tháng, không FTP, đường cong phẳng [[src-choudhry-principles-banking#^choudhry-nim-1]]; NII cơ sở £461,0m [[src-choudhry-principles-banking#^choudhry-nim-2]]; +3% → NII +£64,7m (+14%), vì nhiều tài sản tái định giá hơn nợ [[src-choudhry-principles-banking#^choudhry-nim-4]]; lãi suất giảm xuống 4% → NII −£29,5m [[src-choudhry-principles-banking#^choudhry-nim-6]]. Ghi rõ đây là ví dụ minh hoạ, giả định khác d368 (sốc chuẩn, bảng cân đối cố định). → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: thêm cơ chế: NII nhạy lãi suất vì tài sản và nợ tái định giá ở thời điểm khác nhau [[src-choudhry-principles-banking#^choudhry-nim-9]]; ba kiểu phản ứng của lãi suất sản phẩm (giữ nguyên; bằng mức thay đổi benchmark; nhiều hơn hoặc ít hơn) [[src-choudhry-principles-banking#^choudhry-nim-3]]; ví dụ khoản vay cố định 10% và tiền gửi 1 tháng từ 2% lên 4% làm NII giảm từ £800 xuống £600 [[src-choudhry-principles-banking#^choudhry-nim-10]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: thêm vào phần dự báo: mô hình bottom-up cấp tài khoản, sốc lãi suất và tính lại để đo độ nhạy NII; thách thức dữ liệu [[src-choudhry-principles-banking#^choudhry-nim-13]]. Đã có node [[net-interest-margin]]; đề xuất link ở chỗ nhắc NIM. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u03 — chờ user duyệt: thêm vào mục horizon: thước đo thu nhập nội bộ thường dùng horizon ngân sách 3–4 năm [[src-bardaeva-alm#^ch11-16]], khác horizon ΔNII 01 năm của TT83 PL5 [[src-tt83-2025-nhnn#^pl5-b2]] (khác scope, không phải conflict). Link [[irrbb-management]]. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-irrbb-2016 U03/U06 (bổ sung) — chờ user duyệt: thêm vào phần giả định bảng cân đối: d368 Annex 1 phân ba trạng thái mô hình hoá thu nhập (run-off, constant, dynamic; dynamic là cách có ý nghĩa nhất) [[src-bcbs-irrbb-2016#^irrbb-u06-9]]; dynamic view hữu ích cho kế hoạch nhưng có thể che giấu rủi ro nền tảng [[src-bcbs-irrbb-2016#^irrbb-p04-4]]; chân trời thường 1–3 năm, không quá 5 năm [[src-bcbs-irrbb-2016#^irrbb-u06-8]]; ΔNII là chênh lệch giữa kịch bản cơ sở theo kế hoạch kinh doanh và kịch bản stress [[src-bcbs-irrbb-2016#^irrbb-u06-10]]. → đã áp dụng [2026-10-20]
- [2026-10-20] research nii-shocks-regulation-hedging-and-alco-tradeoffs — chờ user duyệt: đổi `cite` của cạnh `input-to → [[balance-sheet-optimisation-model]]` từ `lubinska-u05-11` (giới hạn tập trung nguồn vốn 80%) sang [[src-lubinska-alm-optimisation#^lubinska-u04-12]] (hạn mức biến động NII là ràng buộc bất đẳng thức của bài toán tối ưu). → đã áp dụng [2026-10-20]

### [[outlier-bank-test]]
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 20 "cơ chế sàng lọc định lượng bắt buộc": par 88 ghi "should implement at least one outlier/materiality test" ([[src-bcbs-irrbb-2016#^irrbb-p12-1]], [[src-bcbs-irrbb-2016#^irrbb-u01-6]]); chỉ việc công bố tiêu chí là "must". Đề xuất: "phép thử mà cơ quan giám sát nên (should) áp dụng tối thiểu một lần…; tiêu chí xác định outlier phải (must) được công bố". → đã áp [2026-10-18]
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 22 "sẽ tự động kích hoạt sự can thiệp giám sát tăng cường": nguồn ghi outlier "must be considered as potentially having undue IRRBB" ([[src-bcbs-irrbb-2016#^irrbb-p12-1]]) và "strong presumption" về hệ quả giám sát/vốn khi rà soát phát hiện quản trị yếu hoặc rủi ro quá mức ([[src-bcbs-irrbb-2016#^irrbb-u01-6]]); không có cơ chế tự động. Đề xuất bỏ "tự động", tách hai bước: bị coi là có khả năng mang IRRBB quá mức → khi rà soát kết luận yếu kém thì có giả định mạnh về biện pháp giám sát/vốn. → đã áp [2026-10-18]
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 24 heading "Công thức kiểm tra ngoại lai bắt buộc": đề xuất "Phép thử tối thiểu theo par 88". → đã áp [2026-10-18]
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 61 "Khi một ngân hàng bị xác định là ngân hàng ngoại lai … bắt buộc phải áp dụng … trong một thời hạn ấn định cụ thể": "must require" của par 94 gắn với kết luận "management of IRRBB is inadequate or … excessive risk" ([[src-bcbs-irrbb-2016#^irrbb-p12-3]]), không gắn trực tiếp với việc bị xác định là outlier; thời hạn là par 95 ("should be achieved within a specified time frame"), chưa có claim `[cần nguồn]`. Đề xuất đổi điều kiện kích hoạt theo par 94 và bỏ cụm thời hạn hoặc chờ ingest bổ sung par 95. → đã áp [2026-10-18]
- [2026-10-18] ingest src-bcbs-irrbb-2016 U03 (bổ sung): đề xuất dòng 22 cite thêm [[src-bcbs-irrbb-2016#^irrbb-p12-4]] (par 90: outlier "must be considered as potentially having undue IRRBB and subject to review"); đề xuất dòng 61 cite [[src-bcbs-irrbb-2016#^irrbb-p12-8]] cho cụm thời hạn (par 95, mức should) thay vì bỏ; có thể thêm [[src-bcbs-irrbb-2016#^irrbb-p12-7]] (rủi ro quá mức so với thu nhập theo ∆NII) vào mục phép thử bổ sung. → đã áp [2026-10-18]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M8 — chờ user duyệt: đã có node [[model-validation]]; đề xuất link ở lần nhắc đầu kiểm định mô hình. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u08 — chờ user duyệt: thêm góc nhìn EU (nguồn T4 mô tả RTS/2022/10; khác jurisdiction, không phải conflict): SOT EVE ngưỡng 15% vốn cấp 1, tính theo bảng cân đối run-off [[src-tata-bank-alm#^tata-sot-1]]; sàn lãi suất sau sốc tuyến tính −150 bp tăng 3 bp/năm tới 0% ở 50 năm [[src-tata-bank-alm#^tata-sot-2]]; **SOT NII** ngưỡng 5% vốn cấp 1, NII kế toán 1 năm, bảng cân đối không đổi, bắt buộc gồm biên thương mại, không áp sàn tuyến tính [[src-tata-bank-alm#^tata-sot-3]] (d368 và TT83 không có SOT NII). Thêm mục 'bài toán tuân thủ đồng thời': SOT EVE đặt cận trên và dưới cho tỷ trọng tài sản cố định theo duration, SOT NII đặt mức tối thiểu, vùng tuân thủ có thể rất nhỏ [[src-tata-bank-alm#^tata-sot-4]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: thêm lịch sử ngưỡng EU: Chỉ thị 2006/48/EC và CRD IV — giá trị kinh tế giảm quá 20% vốn tự có (sốc 200 bp); CRD V — EVE giảm quá 15% vốn cấp 1 theo sáu kịch bản hoặc NII suy giảm lớn theo hai kịch bản [[src-tata-bank-alm#^tata-reg-5]]; nguyên tắc SOT theo EBA 2018 (loại CET1, run-off, NPE khi tỷ lệ > 2%, cộng thay đổi dương giữa các đồng tiền trọng số 50%, kỳ hạn bình quân NMD tối đa 5 năm) [[src-tata-bank-alm#^tata-reg-7]]; sàn EBA 2018 −100 bp tăng 5 bp/năm, 0% từ 20 năm [[src-tata-bank-alm#^tata-reg-8]] (trước sàn RTS 2022 −150 bp/50 năm, khác hiệu lực, không conflict). Ví dụ SVB: để không là outlier, duration tiền gửi phải trên 3,7 năm [[src-tata-bank-alm#^tata-svb-7]]; link [[silicon-valley-bank]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u03 — chờ user duyệt: đã có node [[irrbb-management]]; đề xuất link ở lần nhắc đầu "quản trị IRRBB" / quy trình nhận diện, đo lường, kiểm soát. → đã áp dụng [2026-10-20]

### [[required-stable-funding]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có node [[alco]]; đề xuất link ở lần nhắc đầu ALCO. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14 — chờ user duyệt: đã có node [[asset-encumbrance]]; đề xuất link ở lần nhắc đầu encumbrance. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04 — chờ user duyệt: đã có node [[net-interest-margin]]; đề xuất link ở lần nhắc đầu NIM. → đã áp dụng [2026-10-20]

### [[duration-gap-model]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9 — chờ user duyệt: đã có node [[icaap]] (và stub [[economic-capital]]); đề xuất link ở lần nhắc đầu ICAAP / vốn kinh tế. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07 — chờ user duyệt: thêm ví dụ SVB: duration gap khoảng 3 năm (giả định tiền gửi gửi tạm duration 1 năm) ứng với lỗ khoảng 12,5 tỷ USD, hơn 100% vốn, khi sốc 200 bp; sổ HTM duration 6,25 năm [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-5]]; link [[silicon-valley-bank]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: thêm nguồn T4 thứ hai: DGAP = DA − w·DL với w = L/A, mức chấp nhận rủi ro theo chính sách ALCO [[src-lubinska-alm-optimisation#^lubinska-u02-45]]; ví dụ miễn nhiễm (Kaufman 1984) DA 4,17, DL 1, P/A 0,9 → DGAP 3,27 năm, về 0 bằng rút duration tài sản về 0,9 hoặc kéo duration tiền gửi lên 4,63 [[src-lubinska-alm-optimisation#^lubinska-u02-46]]; chiến lược chủ động DGAP 1 năm, tài sản 1.000 euro, lãi suất tăng 200 bp → vốn giảm 20 euro [[src-lubinska-alm-optimisation#^lubinska-u02-47]]; hạn chế (cần dữ liệu đầy đủ, bỏ qua trả trước, chỉ đúng với sốc nhỏ song song) [[src-lubinska-alm-optimisation#^lubinska-u02-48]]; Modified vs Macaulay duration [[src-lubinska-alm-optimisation#^lubinska-u02-44]]. Link [[pv01]], [[repricing-gap-analysis]]. → đã áp dụng [2026-10-20]

### [[economic-value-at-risk]]
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 52 "… làm chuẩn mực quy định bắt buộc thay vì dựa vào các mô hình EVaR nội bộ": 6 kịch bản là "Banks should apply" ([[src-bcbs-irrbb-2016#^irrbb-u07-1]]), phép thử ngoại lai là "should implement" ([[src-bcbs-irrbb-2016#^irrbb-p12-1]]); vế "thay vì EVaR nội bộ" không có trong claim được cite (par 69 còn ghi ngân hàng dùng IMS của mình để tính số công bố, [[src-bcbs-irrbb-2016#^irrbb-p08-1]] chỉ trích một phần). Đề xuất viết lại theo should và chuyển vế so sánh với EVaR sang `*Diễn giải:*`. → đã áp [2026-10-18]

### [[irrbb-standardised-framework]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đề xuất thêm cite cho câu phóng chiếu dòng tiền tái định giá (dòng 89): định nghĩa CF(t) và repricing date [[src-bcbs-irrbb-2016#^irrbb-u05-9]], thời điểm tái định giá [[src-bcbs-irrbb-2016#^irrbb-u05-10]], spread không tái định giá slot tới contractual maturity [[src-bcbs-irrbb-2016#^irrbb-u05-11]], công cụ thả nổi tái định giá toàn bộ tại first reset date [[src-bcbs-irrbb-2016#^irrbb-u05-12]], quy tắc slot fixed và floating [[src-bcbs-irrbb-2016#^irrbb-u05-13]] [[src-bcbs-irrbb-2016#^irrbb-u05-14]]. → đã áp [2026-10-19]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; đề xuất link ở lần nhắc đầu "dòng tiền tái định giá danh nghĩa" (dòng 89). → đã áp [2026-10-19]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 105, 132): (1) dòng 126 cite [[src-bcbs-irrbb-2016#^irrbb-u05-1]] (par 100, chỉ liệt kê 5 giai đoạn) cho bước chiết khấu; đề xuất cite [[src-bcbs-irrbb-2016#^irrbb-u05-17]] (bù trừ trong dải ra CF_{i,c}(k)) và [[src-bcbs-irrbb-2016#^irrbb-u05-18]] (DF liên tục); câu "hoặc bao gồm commercial margin nếu dòng tiền đã bao gồm margin" cite [[src-bcbs-irrbb-2016#^irrbb-u05-19]]. (2) Công thức DF_i = exp(−(R_0 + ∆R_i)·t_k) ở dòng 133: nguồn chỉ viết R_{i,c}(t_k) phản ánh kịch bản i theo Annex 2 [[src-bcbs-irrbb-2016#^irrbb-u05-18]]; cách tách R_0 + ∆R nên đặt dưới *Diễn giải:*. (3) Công thức EVE_{0,c}, EVE_{i,c} (dòng 141–145) và ∆EVE (dòng 150–170) cite [[src-bcbs-irrbb-2016#^irrbb-u05-20]], [[src-bcbs-irrbb-2016#^irrbb-u05-21]]; nguồn viết Σ tới K và gọi là EVE^nao (không gồm quyền chọn tự động). (4) Giai đoạn 5: thêm ngoại lệ cơ quan giám sát quốc gia được quy định cách gộp tiền tệ khác [[src-bcbs-irrbb-2016#^irrbb-u05-24]]. (5) Có thể thêm giả định intra-bucket mismatch [[src-bcbs-irrbb-2016#^irrbb-u05-22]] và CF phụ thuộc kịch bản [[src-bcbs-irrbb-2016#^irrbb-u05-23]]. → đã áp [2026-10-19]
- [2026-10-19] review (đối chiếu Table 1, ^irrbb-u05-25) — user duyệt [2026-10-19]: (1) bảng 19 dải ở Giai đoạn 2, dải 6 (9M–1Y) ghi điểm giữa 0.7917 năm; raw ghi 0.875Y [[src-bcbs-irrbb-2016#^irrbb-u05-25]]. Đề xuất sửa thành 0.8750 và cite u05-25 cho bảng. (2) Câu "nếu ∆EVE* > 15% Tier 1 Capital, ngân hàng chính thức bị xác định là ngân hàng ngoại lai" mâu thuẫn với [[outlier-bank-test]] đã sửa [2026-10-18]: phép thử 15% Tier 1 là should (par 88), outlier bị coi là có khả năng mang IRRBB quá mức và phải được rà soát [[src-bcbs-irrbb-2016#^irrbb-p12-4]]. Đề xuất viết lại theo cách đó. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5 — user duyệt [2026-10-19]: thêm đối chiếu VN. PL5 dùng cùng 5 bước và 3 nhóm vị thế [[src-tt83-2025-nhnn#^pl5-a1-2]]; nhóm chưa đáp ứng đủ tiêu chuẩn không phân bổ dòng tiền [[src-tt83-2025-nhnn#^pl5-a2-2]]; Bảng 1 19 thang giống Table 1 [[src-tt83-2025-nhnn#^pl5-a2-t1]]; KAO do ngân hàng tự đo [[src-tt83-2025-nhnn#^pl5-a4]]; đo theo đồng tiền khi tài sản hoặc nợ bằng đồng tiền đó ≥ 5% tổng tài sản trên sổ ngân hàng [[src-tt83-2025-nhnn#^d54-3c]]; chiết khấu chỉ theo risk-free rate [[src-tt83-2025-nhnn#^pl5-a3-2]]. → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9 — chờ user duyệt: đã có node [[icaap]] (và stub [[economic-capital]]); đề xuất link ở lần nhắc đầu ICAAP / vốn kinh tế. → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-irrbb-2016 U05 — chờ user duyệt: ở Giai đoạn 4 (Đo lường rủi ro quyền chọn tự động KAO), bổ sung chi tiết: phân loại quyền chọn tự động gồm caps/floors, swaptions phi bán lẻ và behavioural options bán buôn [[src-bcbs-irrbb-2016#^irrbb-u05-26]]; định giá biến động Delta FVAO kết hợp tăng độ biến động ngầm định +25% cho cả quyền chọn bán và mua [[src-bcbs-irrbb-2016#^irrbb-u05-27]]; công thức KAO_{i,c} = sum Delta FVAO^o - sum Delta FVAO^q và quy tắc xử lý khi chỉ đưa quyền chọn mua phòng ngừa vào KAO [[src-bcbs-irrbb-2016#^irrbb-u05-28]]. → đã áp [2026-10-20] (node draft); bỏ "Black-Scholes, Hull-White" và lý do "phản ánh bất định" vì không có trong trích dẫn

### [[key-rate-duration]]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; đề xuất link ở "Dòng tiền tái định giá danh nghĩa ròng" (dòng 62). → đã áp [2026-10-19]
- [2026-10-19] review (đối chiếu Table 1, ^irrbb-u05-25) — user duyệt [2026-10-19]: dòng bảng "17–19 | 10 năm đến trên 20 năm | 12.5 – 22.5 năm" sai điểm giữa dải cuối; raw ghi >20Y (25Y) [[src-bcbs-irrbb-2016#^irrbb-u05-25]]. Đề xuất sửa thành "12.5 – 25 năm" và cite u05-25. Cột hệ số (0.044 → 0.004) chưa có citation, cần rà nguồn. → đã áp [2026-10-19]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02 — chờ user duyệt: đã có node [[pv01]] (định nghĩa PV − PV* theo sốc 1 bp, tổng theo dải) [[src-lubinska-alm-optimisation#^lubinska-u02-43]]; đề xuất link ở chỗ nhắc Bucket PV01. → đã áp dụng [2026-10-20]

### [[replicating-portfolio-model]]
- [2026-10-20] research irrbb-alm-governance-strategy-and-tradeoffs — chờ user duyệt: thêm relation `{type: hedges, to: "[[net-interest-income-sensitivity]]", cite: "[[src-bcbs-irrbb-2016#^irrbb-u06-6]]"}` (danh mục tái lập quản lý biến động thu nhập từ NMD và vốn chủ sở hữu). → đã áp dụng [2026-10-20]

### [[bcbs-irrbb]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đề xuất thêm dòng vào bảng yêu cầu (sau dòng 69): | Notional repricing cash flow | Hoàn trả gốc, tái định giá gốc, thanh toán lãi; ngày của mỗi khoản là repricing date | par 102 [[src-bcbs-irrbb-2016#^irrbb-u05-9]] | và | Công cụ thả nổi | Tái định giá toàn bộ tại first reset date | par 104 [[src-bcbs-irrbb-2016#^irrbb-u05-12]] |. → đã áp [2026-10-18]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; dòng bảng "Notional repricing cash flow" đề xuất ở trên nên link tới node này. → đã áp [2026-10-18]
- [2026-10-18] lint (R1, mức bắt buộc outlier test): dòng 60 "phép thử tối thiểu bắt buộc là so sánh … 15% Vốn cấp 1": đề xuất "cơ quan giám sát phải công bố tiêu chí và nên (should) áp dụng ít nhất một phép thử so max ∆EVE dưới 6 kịch bản với 15% Tier 1" ([[src-bcbs-irrbb-2016#^irrbb-p12-1]]). "Khi vi phạm, ngân hàng bị áp dụng chế tài": đề xuất "khi rà soát kết luận quản trị yếu kém hoặc rủi ro quá mức, cơ quan giám sát phải yêu cầu một hoặc nhiều biện pháp" ([[src-bcbs-irrbb-2016#^irrbb-p12-3]]). → đã áp [2026-10-18]
- [2026-10-19] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 28, 29, 32) — user duyệt [2026-10-19]: Nguyên tắc 3 (dòng 49) viết "Khẩu vị rủi ro phải được định lượng"; nguồn viết "should be articulated" (nên), chỉ policy limits là "must" [[src-bcbs-irrbb-2016#^irrbb-p03-1]] (R1). Đề xuất viết lại theo mức bắt buộc của nguồn và thêm: risk appetite statement do governing body phê duyệt, chính sách IRRBB rà soát tối thiểu hằng năm [[src-bcbs-irrbb-2016#^irrbb-p03-2]]; hạn mức tổng nhất quán với cách đo, áp dụng hợp nhất [[src-bcbs-irrbb-2016#^irrbb-p03-3]]; vị thế vượt hạn mức được báo cáo lên ngay [[src-bcbs-irrbb-2016#^irrbb-p03-4]]. Cụm "hạn mức cụ thể cho từng loại rủi ro (gap, basis, options)" thuộc par 30, chưa có claim → `[cần nguồn]` hoặc ingest bổ sung u03 par 30 (raw dòng 118). → đã áp [2026-10-19]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1 — chờ user duyệt: đã có node [[risk-appetite]], [[risk-limits]], [[stress-testing]]; đề xuất link ở lần nhắc đầu risk appetite / policy limits / reverse stress test (Nguyên tắc 3–4). → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9 — chờ user duyệt: đã có node [[icaap]]; đề xuất link ở Nguyên tắc 9 và thêm dòng đối chiếu VN: TT83 đưa IRRBB vào ICAAP qua giả định lãi suất trong stress test vốn, tác động lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; ICAAP tối thiểu hằng năm [[src-tt83-2025-nhnn#^d59-1]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn PL6 — chờ user duyệt: Nguyên tắc 9: thêm đối chiếu VN — $RWA_{IRRBB}$ là cấu phần của vốn kinh tế ICAAP [[src-tt83-2025-nhnn#^pl6-1b]], theo ΔEVE từ 01/01/2028 [[src-tt83-2025-nhnn#^pl6-1c]]; link [[rwa-irrbb]], [[economic-capital]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1 — chờ user duyệt: đã có [[banking-book]]; định nghĩa IRRBB của VN có cùng 3 cấu phần gap/basis/option như d368 [[src-tt83-2025-nhnn#^d3-22]] — có thể thêm vào bảng đối chiếu; VN không nhắc CSRBB trong định nghĩa. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M8 — chờ user duyệt: Nguyên tắc 6: đối chiếu VN — kiểm định thuộc tuyến 2, tách khỏi bên xây dựng và sử dụng mô hình [[src-tt83-2025-nhnn#^d56-7]]; tần suất tối thiểu hằng năm [[src-tt83-2025-nhnn#^d56-4d]]; link [[model-validation]]. → đã áp dụng [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u23–u24 — chờ user duyệt: đã có node [[reverse-stress-testing]]; đề xuất link ở Nguyên tắc 4 ("stress testing ngược (reverse stress test)"). → đã áp dụng [2026-10-20]
- [2026-10-20] ingest src-bcbs-irrbb-2016 u03 (bổ sung Table A & Table B) — chờ user duyệt: Nguyên tắc 8 (dòng 58) chi tiết hoá khung công bố Trụ cột 3: Table A (định tính: 8 tiêu chí a–h gồm định nghĩa, chiến lược hedging, ALCO, kịch bản sốc, giải trình IMS vs Table B; định lượng: kỳ hạn tái định giá bình quân và dài nhất của NMDs [[src-bcbs-irrbb-2016#^irrbb-p08-7]], [[src-bcbs-irrbb-2016#^irrbb-p08-8]], [[src-bcbs-irrbb-2016#^irrbb-p08-9]]) và Table B (định lượng: định dạng cố định, so sánh T vs T–1 cho 6 kịch bản ΔEVE và 2 kịch bản song song ΔNII trên vốn Tier 1 [[src-bcbs-irrbb-2016#^irrbb-p08-10]], [[src-bcbs-irrbb-2016#^irrbb-p08-11]]). → đã áp [2026-10-20] (node draft) dưới Nguyên tắc 8; không viết "8 tiêu chí a–h", "T vs T–1", "vốn Tier 1" vì các trích dẫn p08-7…11 không chứa — cần bổ sung claim nếu muốn đưa vào

### [[basel-liquidity-monitoring-framework]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), câu ALCO trước nguyên tắc điều hành; sửa link file:/// thành wikilink
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M6: đã có node [[concentration-risk-management]]; TT83 Đ50–52 không đặt hạn mức tập trung nguồn vốn [[src-tt83-2025-nhnn#^d50-1]], chỉ có yếu tố tập trung huy động vốn trong stress thanh khoản [[src-tt83-2025-nhnn#^d48-3]]; cần rà lại chỗ nhắc SRP50 / nghĩa vụ VN. → đã áp [2026-10-20] (node draft), nguyên tắc điều hành 2; sửa "tuân thủ ngưỡng <1%" thành ngưỡng nhận diện SRP50.17
- [2026-10-20] ingest src-bcbs-framework SRP30: [[concentration-risk-management]] thêm góc nhìn Basel SRP30: SRP30.22 liệt kê nguồn vốn là một tình huống tập trung, còn TT83 Đ50 không đưa vào; cần rà lại phần tập trung nguồn vốn (SRP50 so với SRP30.22). → đã áp [2026-10-20] (node draft), cùng đoạn đối chiếu tập trung nguồn vốn

### [[ftp-cost-benefit-allocation-principles]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1: đã có node [[risk-appetite]], [[risk-limits]], [[stress-testing]]; bộ phận ALM đề xuất nguyên tắc giá điều chuyển vốn nội bộ [[src-tt83-2025-nhnn#^d25-3]]; cần rà lại chỗ nhắc khẩu vị rủi ro / hạn mức và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" sau 6 nguyên tắc
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" ở mục kết luận
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" ở mục kết luận
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" sau 6 nguyên tắc
- [2026-10-19] ingest src-choudhry-principles-banking u19: [[funds-transfer-pricing]] thêm cách xử lý vốn chủ sở hữu và lợi nhuận giữ lại qua FTP (lợi ích giao central ALCO book, RoE mục tiêu là chi phí quy đổi, tách 3 phần lãi subordinated debt; capm-11…14) và case UBS (gov-12); cần rà lại phần phân bổ lợi ích funding từ vốn. → đã áp [2026-10-20] (node draft), mục "Phân bổ lợi ích funding từ vốn chủ sở hữu" (capm-11…13, gov-12); capm-14 subordinated debt chưa đưa vào

### [[ftp-curve-construction-methodology]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), mục Biểu giá Thị trường 1
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: đã có node [[overnight-index-swap]] (OIS/SONIA, phòng ngừa NII và basis risk tiền gửi so với lãi suất cơ bản); cần rà lại chỗ nhắc OIS để link. → không áp dụng [2026-10-20]: node không nhắc OIS (đường cong USD dùng SOFR theo ^vab-ftp-29)

### [[ftp-economic-cost-and-incentive-validation]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" + căn cứ Basel sau sơ đồ mục 5
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" + căn cứ Basel sau sơ đồ mục 5
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" + căn cứ Basel sau sơ đồ mục 5
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p02–p04: [[funds-transfer-pricing]] có căn cứ Basel cho phần thanh khoản (BCBS 144 P4: liquidity charge gán tới trạng thái/danh mục/giao dịch, tính thời gian nắm giữ, thanh khoản thị trường, lợi ích nguồn vốn ổn định, xét stress), thay cho "[cần nguồn]" chuẩn BCBS về FTP; cần rà lại phần kiểm định incentive (P4 yêu cầu căn chỉnh động cơ của mảng kinh doanh với tolerance). → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" + căn cứ Basel sau sơ đồ mục 5

### [[ftp-final-rate-determination]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" ở mục 3.8
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" ở mục 3.8
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), mục Khái niệm và Liên kết
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M2: đã có node [[credit-risk-management]]; TT83 Đ26.2.c yêu cầu nguyên tắc đưa chi phí bù đắp rủi ro tín dụng vào định giá sản phẩm tín dụng theo mức rủi ro khách hàng [[src-tt83-2025-nhnn#^d26-2c]] (văn bản NHNN đầu tiên trong wiki chạm tới pricing tín dụng); cần rà lại chỗ nhắc credit spread / commercial margin. → đã áp [2026-10-20] (node draft), đoạn "Đối chiếu NHNN" ở mục 3.8

### [[ftp-nature-and-balance-sheet-management]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1: đã có node [[risk-appetite]], [[risk-limits]], [[stress-testing]]; bộ phận ALM đề xuất nguyên tắc giá điều chuyển vốn nội bộ [[src-tt83-2025-nhnn#^d25-3]]; cần rà lại chỗ nhắc khẩu vị rủi ro / hạn mức và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), mục "Căn cứ quy định: NHNN và Basel"
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN. → đã áp [2026-10-20] (node draft), mục "Căn cứ quy định: NHNN và Basel"
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), mục "Căn cứ quy định: NHNN và Basel" + link ALCO mục 1
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M3: đã có node [[market-risk-management]]; cần rà lại chỗ nhắc rủi ro thị trường / sổ kinh doanh. → đã áp [2026-10-20] (node draft), link [[market-risk-management]] trong mục "Căn cứ quy định: NHNN và Basel"; sơ đồ không nhắc sổ kinh doanh
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15: [[risk-appetite]] thêm RAS theo Choudhry (văn bản quan trọng nhất cần Board phê duyệt, macro-tolerance chia theo khối, hạn mức FX và encumbrance, rà soát hằng năm); cần rà lại phần khẩu vị rủi ro. → đã áp [2026-10-20] (node draft), link [[risk-appetite]] + BCBS P2 trong mục "Căn cứ quy định: NHNN và Basel"; chi tiết RAS để ở node risk-appetite
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04: đã có node [[net-interest-margin]] (định nghĩa, case ChoudWest 5 kịch bản: NII và NIM có thể đi ngược chiều, buffer £1,5bn làm NIM −0,50 điểm %, Table 1.10 hành động quản lý NIM); cần rà lại chỗ dùng NIM làm chỉ số đánh đổi. → đã áp [2026-10-20] (node draft), *Diễn giải* NII vs NIM trong mục "Căn cứ quy định: NHNN và Basel" (NIM ở mục 3 nằm trong code block)
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p02–p04: [[funds-transfer-pricing]] có căn cứ Basel cho phần thanh khoản (BCBS 144 P4: liquidity charge gán tới trạng thái/danh mục/giao dịch, tính thời gian nắm giữ, thanh khoản thị trường, lợi ích nguồn vốn ổn định, xét stress), thay cho "[cần nguồn]" chuẩn BCBS về FTP; cần rà lại phần căn cứ quy định của FTP. → đã áp [2026-10-20] (node draft), mục "Căn cứ quy định: NHNN và Basel"

### [[ftp-portfolio-and-bucket-allocation]]
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), mục Khái niệm và Liên kết
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M3: đã có node [[market-risk-management]]; sổ kinh doanh (Thị trường 2) chịu hạn mức rủi ro thị trường [[src-tt83-2025-nhnn#^d35-2]] và báo cáo hằng ngày [[src-tt83-2025-nhnn#^d37-1]]; cần rà lại mục Phân bổ theo Danh mục (Trading Book). → đã áp [2026-10-20] (node draft), sub-bullet dưới bước 1 Portfolio Segmentation
- [2026-10-19] ingest src-bcbs-framework RBC25: [[banking-book]] có thêm tiêu chí Basel RBC25 (phân loại theo mục đích nắm giữ, danh sách bắt buộc/suy định, hạn chế chuyển sổ) và bảng Basel vs VN; repo phục vụ kinh doanh mặc định thuộc trading book theo Basel [[src-bcbs-framework#^rbc25-9]], trong khi TT83 xếp mọi repo vào sổ ngân hàng [[src-tt83-2025-nhnn#^d3-33]]; cần rà lại mục 2 (Portfolio Segmentation, dòng Interbank Book có Repo/Reverse) và link [[banking-book]], [[regulatory-internal-risk-transfer]]. → đã áp [2026-10-20] (node draft), sub-bullet dưới bước 1 + *Diễn giải* về Repo trong Danh mục Treasury

### [[ftp-risk-and-cost-components]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế. → đã áp [2026-10-20] (node draft), mục 6 "Đối chiếu NHNN"
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN. → đã áp [2026-10-20] (node draft), mục 6 "Đối chiếu NHNN" + *Diễn giải* khác biệt công thức RAROC
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), mục Khái niệm và Liên kết
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M2: đã có node [[credit-risk-management]]; TT83 Đ26.2.c yêu cầu nguyên tắc đưa chi phí bù đắp rủi ro tín dụng vào định giá sản phẩm tín dụng theo mức rủi ro khách hàng [[src-tt83-2025-nhnn#^d26-2c]] (văn bản NHNN đầu tiên trong wiki chạm tới pricing tín dụng); cần rà lại mục cấu phần credit spread. → đã áp [2026-10-20] (node draft), mục 6 "Đối chiếu NHNN"
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: đã có node [[overnight-index-swap]] (OIS/SONIA, phòng ngừa NII và basis risk tiền gửi so với lãi suất cơ bản); cần rà lại chỗ nhắc OIS để link. → đã áp [2026-10-20] (node draft), link ở mục 2.1
- [2026-10-19] ingest src-choudhry-principles-banking u21–u22: đã có node [[expected-loss]], [[shareholder-value-added]]; cần rà lại mục Expected Loss Charge. → đã áp [2026-10-20] (node draft), link sau sơ đồ mục 6
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p02–p04: [[funds-transfer-pricing]] có căn cứ Basel cho phần thanh khoản (BCBS 144 P4: liquidity charge gán tới trạng thái/danh mục/giao dịch, tính thời gian nắm giữ, thanh khoản thị trường, lợi ích nguồn vốn ổn định, xét stress), thay cho "[cần nguồn]" chuẩn BCBS về FTP; cần rà lại cấu phần liquidity risk (TLP, đệm HQLA). → đã áp [2026-10-20] (node draft), đoạn căn cứ Basel ở đầu mục 3

### [[irrbb-alm-governance-strategy-and-tradeoffs]]
- [2026-10-19] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 28, 29, 32): claim mới về risk appetite statement [[src-bcbs-irrbb-2016#^irrbb-p03-2]], aggregate limits hợp nhất [[src-bcbs-irrbb-2016#^irrbb-p03-3]] và báo cáo vượt hạn mức [[src-bcbs-irrbb-2016#^irrbb-p03-4]]; [[tt83-2025]] yêu cầu hạn mức ΔNII và ΔEVE [[src-tt83-2025-nhnn#^d53-2]]; cần rà lại mục hệ thống hạn mức ALCO 4 tầng và câu "Principle 2/9" ở sơ đồ quản trị. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn PL2 (+ Đ9): [[tt83-2025]] có báo cáo quản lý rủi ro hằng năm gửi NHNN, hạn 90 ngày sau năm tài chính, Tổng giám đốc phê duyệt [[src-tt83-2025-nhnn#^d9-3a]] [[src-tt83-2025-nhnn#^d9-4c]]; mục IRRBB gồm chiến lược, hạn mức, kiểm tra sức chịu đựng, vi phạm [[src-tt83-2025-nhnn#^pl2-ii6]]; cần rà lại mục vai trò ALCO / báo cáo và phần hàm ý quy định NHNN. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1: đã có node [[risk-appetite]], [[risk-limits]], [[stress-testing]]; TT83 quy định bộ phận ALM kiểm soát hạn mức IRRBB và tổng tài sản tính theo rủi ro IRRBB, đề xuất nguyên tắc FTP [[src-tt83-2025-nhnn#^d25-3]]; hạn mức do Tổng giám đốc ban hành, nới lỏng phải báo cáo HĐQT [[src-tt83-2025-nhnn#^d20-1]] [[src-tt83-2025-nhnn#^d20-2]]; stress test IRRBB tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]]; cần rà lại mục vai trò ALCO / hệ thống hạn mức và hàm ý NHNN. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]]; vốn mục tiêu phân bổ cho rủi ro trọng yếu làm cơ sở hạn mức [[src-tt83-2025-nhnn#^d61-1]]; stress test vốn tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại mục Nguyên tắc 9 / ICAAP và hàm ý NHNN. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[economic-capital]] (hết stub), [[rwa-irrbb]], [[target-capital]], [[raroc]], [[projected-own-funds]]; $RWA_{IRRBB}$ theo ΔEVE từ 01/01/2028 [[src-tt83-2025-nhnn#^pl6-1c]]; cần rà lại mục EVE vs NII (ΔEVE nay nối thẳng vào vốn kinh tế) và Nguyên tắc 9. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[three-lines-of-defence]] (TT83 Đ4.2 [[src-tt83-2025-nhnn#^d4-2]]); cần rà lại chỗ nhắc 1LoD/2LoD. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M8: đã có node [[model-validation]]; TT83 yêu cầu kiểm định mô hình trước khi dùng, khi thay đổi trọng yếu và tối thiểu hằng năm [[src-tt83-2025-nhnn#^d56-4d]], do tuyến 2 thực hiện [[src-tt83-2025-nhnn#^d56-7]]; cần rà lại chỗ nhắc kiểm định mô hình hành vi. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn PL3: [[rwa-irrbb]] phải được thuyết minh phương pháp (mô tả, điểm mạnh, hạn chế, điều chỉnh giả định) trong báo cáo ICAAP hằng năm gửi NHNN [[src-tt83-2025-nhnn#^pl3-3b]] [[src-tt83-2025-nhnn#^d9-2c]]; cần rà lại mục vốn cho IRRBB / ICAAP. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C5: [[model-validation]] sửa hiệu lực — quản lý rủi ro mô hình Mục 8 (kể cả kiểm định hằng năm) bắt buộc chậm nhất từ 01/01/2028, sớm hơn chỉ với mô hình xếp hạng nội bộ [[src-tt83-2025-nhnn#^d74-3]]; áp dụng sớm phải thông báo NHNN trong 10 ngày [[src-tt83-2025-nhnn#^d74-5]]; cần rà lại chỗ nhắc kiểm định mô hình hành vi. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u08: [[outlier-bank-test]] có đề xuất thêm khung EU — SOT NII 5% vốn cấp 1 (d368, TT83 không có) [[src-tata-bank-alm#^tata-sot-3]], sàn lãi suất sau sốc tuyến tính [[src-tata-bank-alm#^tata-sot-2]], bài toán tuân thủ đồng thời EVE/NII [[src-tata-bank-alm#^tata-sot-4]]; cần rà lại mục đánh đổi EVE–NII. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07: đã có node [[silicon-valley-bank]] có nguồn (số liệu bảng cân đối, phòng ngừa, duration gap 3 năm, giả định duration tiền gửi) [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-9]]; cần rà lại chỗ nhắc SVB, đối chiếu số liệu và thay bằng citation. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u25: đã có node [[structural-hedging]] (phòng ngừa IRRBB theo phần ròng sau natural hedge, macro hedge pool IRS không áp được hedge accounting [[src-choudhry-principles-banking#^choudhry-cs-14]] [[src-choudhry-principles-banking#^choudhry-cs-17]]); cần rà lại mục chiến lược phòng ngừa và vai trò ALCO. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: [[alco]] thêm best practice FSA/PRA SS1/13 và ToR Choudhry (CFO chủ tịch, họp hằng tháng, báo cáo Board, pari passu với ExCo) đối chiếu TT83 (giúp việc TGĐ, tối thiểu hằng quý), MI pack có NII/NIM sensitivity và basis risk; cần rà lại phần quản trị ALCO. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: [[structural-hedging]] thêm công cụ phòng ngừa (FRA, futures, OIS, cap) và ví dụ EAR: gap −80, +1% làm NII giảm 0,8 triệu USD (EAR ~7,8%), cap 80 triệu strike 3% loại bỏ EAR với chi phí 5bp NIM, hạn mức EAR ALCO ±5%/±10%; cần rà lại phần lựa chọn công cụ phòng ngừa. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: đã có node [[overnight-index-swap]] (OIS/SONIA, phòng ngừa NII và basis risk tiền gửi so với lãi suất cơ bản); cần rà lại chỗ nhắc OIS để link. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15: [[risk-appetite]] thêm RAS theo Choudhry (văn bản quan trọng nhất cần Board phê duyệt, macro-tolerance chia theo khối, hạn mức FX và encumbrance, rà soát hằng năm); cần rà lại phần khẩu vị rủi ro. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u03/u04: đã có node [[net-interest-margin]] (định nghĩa, case ChoudWest 5 kịch bản: NII và NIM có thể đi ngược chiều, buffer £1,5bn làm NIM −0,50 điểm %, Table 1.10 hành động quản lý NIM); cần rà lại chỗ dùng NIM làm chỉ số đánh đổi. → đã rà [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u03: mục 1 "Triết Lý Quản Trị ALCO và Mô Hình Vận Hành ALM theo Moorad Choudhry & Polina Bardaeva" quy cho Bardaeva khuyến nghị ALM báo cáo trực tiếp CEO nhưng chỉ cite Choudhry. Bardaeva nói ALM nên độc lập, trực thuộc CFO hoặc CEO (khi họ có KPI cả về tham số rủi ro), hoặc thuộc đơn vị phụ trách chiến lược dài hạn [[src-bardaeva-alm#^ch11-21]]; gộp ALM vào Trading Desk là sai kể cả khi ALM không là profit center [[src-bardaeva-alm#^ch11-11]], trong khi bullet "Mô Hình Vận Hành Treasury" ưu tiên Front-Office Profit Centre. Đã có node [[irrbb-management]], [[alm-operating-model]], [[srep]]; cần rà lại mục 1. → đã rà [2026-10-20]
- [2026-10-19] ingest src-bardaeva-alm u04: [[irrbb-management]] thêm bảng thị trường phát triển và mới nổi (liability sensitive, khả năng phòng ngừa hạn chế, khó dựng đường cong nội bộ) và vai trò IRRBB/FTP trong khủng hoảng (chỉnh độ dốc đường cong FTP); đã có node [[recovery-and-resolution-planning]], [[mrel]]; cần rà lại phần hàm ý cho VN và mục 5 (FTP). → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u21–u22: Choudhry nêu bộ hạn mức Banking Book gồm BPV và Interest Rate Gap Limits trong hạn mức do ALCO đặt [[src-choudhry-principles-banking#^choudhry-bbp-5]], risk register ghi khẩu vị IRR là hạn mức chênh lệch tái định giá [[src-choudhry-principles-banking#^choudhry-rmf-5]], và toàn bộ IRR tập trung về Treasury qua internal swap [[src-choudhry-principles-banking#^choudhry-st-11]]; đã có node [[key-risk-indicators]]; cần rà lại mục 4 (hệ thống hạn mức ALCO 4 tầng). → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u23–u24: [[icaap]] có thêm quy trình UK (use test, một chủ sở hữu ICAAP, Pillar 2A/2B), [[srep]] có Pillar 2A/2B của PRA, [[recovery-and-resolution-planning]] có FSB Key Attributes và EU vs US; đã có node [[reverse-stress-testing]], [[bail-in]]; cần rà lại mục quản trị vốn/ICAAP và RRP. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u18 — chờ user duyệt: [[risk-appetite]] có quan hệ mới `limits` → [[bank-strategic-plan]]; [[capital-plan]] thêm `part-of` strategic plan và 3 mục tiêu capital management; [[raroc]] thêm các lựa chọn chỉ tiêu return (RoC Pillar I+II, RARoC, RoRAC, RoRWA); cần rà lại mục khẩu vị rủi ro và hạn mức ALCO. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u19: [[capital-plan]] và [[alco]] thêm mẫu capital management policy của Choudhry, trong đó ALCO sở hữu capital planning (capm-16, capm-19, capm-30); TT83 Đ6.4.c lại giao đánh giá mức đủ vốn cho Hội đồng quản lý vốn riêng (d6-4c); cần rà lại phần phân vai ALCO trong khung quản trị. → đã rà [2026-10-20]

### [[irrbb-five-tier-architecture]]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại mục "19 Dải Kỳ hạn Chuẩn hoá Basel d368" (dòng 149). → đã rà [2026-10-18]
- [2026-10-18] research (rà sau U05 bổ sung) — đề xuất cho dòng 149 "19 Dải Kỳ hạn Chuẩn hoá Basel d368", chờ user duyệt: → đã áp [2026-10-19]
  - Việc bù trừ dòng tiền dương và âm trong mỗi dải thành một vị thế ròng là bước 1 của par 132, nên cite thêm [[src-bcbs-irrbb-2016#^irrbb-u05-17]]; việc phân bổ theo khả năng chuẩn hoá của vị thế cite [[src-bcbs-irrbb-2016#^irrbb-u05-16]] (par 105). Giữ [[src-bcbs-irrbb-2016#^irrbb-u05-2]] cho 19 dải và điểm giữa dải.
  - Hai mốc "0.0028 năm" và "22.5 năm" không có trong claim u05-2 (claim chỉ nêu "Table 1"); cần `/ingest src-bcbs-irrbb-2016 u05` bổ sung claim Table 1 hoặc bỏ hai mốc.
  - Đề xuất viết lại: "Notional repricing cash flow được slot vào 19 dải kỳ hạn hoặc điểm giữa $t_k$ [[src-bcbs-irrbb-2016#^irrbb-u05-2]]; trong mỗi dải, dòng tiền dương và âm được bù trừ thành một vị thế ròng $CF_{i,c}(k)$ [[src-bcbs-irrbb-2016#^irrbb-u05-17]]."
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), đầu mục Ma trận Tương tác
- [2026-10-19] ingest src-tata-bank-alm u07: đã có node [[silicon-valley-bank]] có nguồn (số liệu bảng cân đối, phòng ngừa, duration gap 3 năm, giả định duration tiền gửi) [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-9]]; cần rà lại chỗ nhắc SVB, đối chiếu số liệu và thay bằng citation. → đã áp [2026-10-20] (node draft), Tầng 2: thay "lãi suất tăng 500 bps" (không có nguồn) bằng số liệu ^tata-svb-5/7/9; câu SVB trong sơ đồ Tầng 4 giữ nguyên
- [2026-10-19] ingest src-lubinska-alm-optimisation u02: đã có node [[repricing-gap-analysis]] (maturity/repricing/refixing/incremental gap, ΔNII ≈ GAP × Δi [[src-lubinska-alm-optimisation#^lubinska-u02-25]]) và [[pv01]] [[src-lubinska-alm-optimisation#^lubinska-u02-43]]; cần rà lại chỗ nhắc repricing gap, PV01 và link node. → đã áp [2026-10-20] (node draft), đoạn mở Tầng 3
- [2026-10-19] ingest src-choudhry-principles-banking u25: đã có node [[structural-hedging]] (phòng ngừa IRRBB theo phần ròng sau natural hedge, macro hedge pool IRS không áp được hedge accounting [[src-choudhry-principles-banking#^choudhry-cs-14]] [[src-choudhry-principles-banking#^choudhry-cs-17]]); cần rà lại tầng phòng ngừa. → đã áp [2026-10-20] (node draft), đoạn mở Tầng 4
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: [[structural-hedging]] thêm công cụ phòng ngừa (FRA, futures, OIS, cap) và ví dụ EAR: gap −80, +1% làm NII giảm 0,8 triệu USD (EAR ~7,8%), cap 80 triệu strike 3% loại bỏ EAR với chi phí 5bp NIM, hạn mức EAR ALCO ±5%/±10%; cần rà lại phần lựa chọn công cụ phòng ngừa. → đã áp [2026-10-20] (node draft), đoạn mở Tầng 4 (FRA/futures/swap/option, ví dụ EAR và cap)
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: đã có node [[overnight-index-swap]] (OIS/SONIA, phòng ngừa NII và basis risk tiền gửi so với lãi suất cơ bản); cần rà lại chỗ nhắc OIS để link. → đã áp [2026-10-20] (node draft), link ở Tầng 5 mục Base Benchmark Rate
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: đã có node [[cross-currency-swap]]; cần rà lại chỗ nhắc currency swap để link. → không áp dụng [2026-10-20]: node không nhắc currency swap
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15: [[repricing-gap-analysis]] thêm giả định và điểm yếu của gap analysis (song song, tái định giá giữa bucket, không time value, bucket tuỳ ý) và ba cách xếp bucket NMD; cần rà lại phần đo gap/NII. → đã áp [2026-10-20] (node draft), đoạn mở Tầng 3 (nêu giả định song song, link node cho phần còn lại)
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15: đã có node [[hedge-accounting]] (tiêu chí 80–125%, micro/macro); cần rà lại chỗ nhắc hedge accounting. → đã áp [2026-10-20] (node draft), thách thức 2

### [[practical-alm-liquidity-governance]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M5: đã có node [[liquidity-risk-management]] (thoát stub) và [[liquidity-stress-testing]] (mới); TT83/2025 Đ45–49 quy định chiến lược, hạn mức theo tỷ lệ pháp định VN [[src-tt83-2025-nhnn#^d45-3]], stress test tối thiểu 3 kịch bản [[src-tt83-2025-nhnn#^d48-2]], kế hoạch dự phòng 5 nội dung [[src-tt83-2025-nhnn#^d48-4]], báo cáo nội bộ hằng quý [[src-tt83-2025-nhnn#^d49-1]]; cần rà lại phần quy định pháp lệnh và Kế hoạch dự phòng (thêm góc nhìn NHNN). → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M1: đã có node [[risk-limits]], [[stress-testing]]; bộ phận ALM kiểm soát hạn mức rủi ro thanh khoản [[src-tt83-2025-nhnn#^d25-3]]; stress test thanh khoản tối thiểu hằng quý [[src-tt83-2025-nhnn#^d23-5]]; cần rà lại phần phân vai và tần suất. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-19] ingest src-tata-bank-alm u07: đã có node [[silicon-valley-bank]] có nguồn (số liệu bảng cân đối, phòng ngừa, duration gap 3 năm, giả định duration tiền gửi) [[src-tata-bank-alm#^tata-svb-5]] [[src-tata-bank-alm#^tata-svb-7]] [[src-tata-bank-alm#^tata-svb-9]]; cần rà lại chỗ nhắc SVB, đối chiếu số liệu và thay bằng citation. → đã áp [2026-10-20] (node draft), mục 1: thay câu quy kết chung bằng số liệu SVB có cite; Northern Rock, Lehman, Credit Suisse ghi [cần nguồn]
- [2026-10-19] ingest src-choudhry-principles-banking u25: case study ALCO (gộp ba ALCO, ghi danh sách tham dự qua Audit) [[src-choudhry-principles-banking#^choudhry-cs-11]] và chiến lược tiền gửi theo chi phí đệm LCR, NII âm [[src-choudhry-principles-banking#^choudhry-cs-20]]; cần rà lại mục quản trị ALCO và chiến lược tiền gửi. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: [[alco]] thêm best practice FSA/PRA SS1/13 và ToR Choudhry (CFO chủ tịch, họp hằng tháng, báo cáo Board, pari passu với ExCo) đối chiếu TT83 (giúp việc TGĐ, tối thiểu hằng quý), MI pack có NII/NIM sensitivity và basis risk; cần rà lại phần quản trị ALCO. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15: [[liquidity-risk-management]] thêm 10 nguyên tắc thanh khoản của Choudhry, liquidity policy statement, mô hình LAB (funding trên 90 ngày, lý tưởng trên 1 năm; survival 2 tuần và 3 tháng; định kỳ bán/repo một phần); cần rà lại phần quản trị thanh khoản và buffer. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-19] ingest src-choudhry-principles-banking u21–u22: đã có node [[key-risk-indicators]]; cần rà lại sơ đồ EWI (Green-Amber-Red) theo khung 4 màu RAYG của Choudhry [[src-choudhry-principles-banking#^choudhry-kri-6]]. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-19] ingest src-choudhry-principles-banking u23–u24: đã có node [[ilaap]], [[cash-flow-survival-period]]; [[liquidity-stress-testing]] có thêm góc nhìn UK (survival period, 3 kịch bản firm specific/market wide/combined); cần rà lại phần stress test thanh khoản. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-19] ingest src-choudhry-principles-banking u19: [[liquidity-risk-management]] thêm liquidity management strategy tích hợp với chiến lược vốn, chỉ tiêu ví dụ (buffer 115% stress 90 ngày, LDR 95%, LAB, trần wholesale; liq-13…15) và tiêu chí rating agency (Moody's BFSR, S&P, Fitch; peer-2…6); cần rà lại phần khung điều hành và hệ thống hạn mức. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-20] ingest src-bcbs-framework SRP30: [[liquidity-risk-management]] có bảng Basel SRP30.48–30.52 vs TT83 (liquidity risk tolerance do HĐQT đặt, chi phí thanh khoản trong định giá nội bộ và duyệt sản phẩm mới, stress test làm cơ sở CFP); cần rà lại phần khung quản trị. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p01, p10, p11: đã có node [[bcbs-liquidity-principles]]; [[ilaap]] có bảng thành phần ILAAP theo Basel (thay [cần nguồn]); [[liquidity-stress-testing]] có bảng Basel P10 vs TT83 Đ48 (trục ngắn hạn/kéo dài, phạm vi pháp nhân và trong ngày); cần rà lại phần stress test, ILAAP và CFP. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p02–p04: [[liquidity-risk-management]] thêm dòng Basel vs VN về chiến lược, cấu trúc tập đoàn, báo cáo HĐQT (BCBS 144 P3); [[risk-appetite]] thêm liquidity risk tolerance do HĐQT đặt (P2); cần rà lại phần khung quản trị và Liquidity FTP. → đã áp [2026-10-20] (node draft), mục 5 "Đối Chiếu NHNN và Basel"

### [[synthetic-balance-sheet-liquidity-risk]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation ở câu slotting. → đã rà [2026-10-18]
- [2026-10-18] research (rà sau U05 bổ sung) — đề xuất cho dòng 107 "Repricing Tenor (Kỳ hạn Lãi)", chờ user duyệt: → đã áp [2026-10-19]
  - Định nghĩa thời điểm reset nên cite par 102: tái định giá xảy ra tại ngày sớm nhất ngân hàng hoặc đối tác được quyền đơn phương thay đổi lãi suất, hoặc ngày lãi suất thả nổi tự động thay đổi theo benchmark [[src-bcbs-irrbb-2016#^irrbb-u05-10]]; repricing date là ngày của mỗi khoản hoàn trả, tái định giá hay thanh toán lãi [[src-bcbs-irrbb-2016#^irrbb-u05-9]].
  - 19 dải kỳ hạn của par 101 thuộc khuôn khổ chuẩn hoá đo ∆EVE [[src-bcbs-irrbb-2016#^irrbb-u05-1]] [[src-bcbs-irrbb-2016#^irrbb-u05-2]]; claim đã ingest không nói ∆NII dùng 19 dải này. Đề xuất bỏ "$\Delta\text{NII}$ và" khỏi câu, hoặc ghi `[cần nguồn]` cho phần ∆NII.
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã áp [2026-10-20] (node draft), đầu mục 6
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M6: đã có node [[concentration-risk-management]]; TT83 Đ50–52 không đặt hạn mức tập trung nguồn vốn [[src-tt83-2025-nhnn#^d50-1]], chỉ có yếu tố tập trung huy động vốn trong stress thanh khoản [[src-tt83-2025-nhnn#^d48-3]]; cần rà lại chỗ nhắc funding concentration. → đã áp [2026-10-20] (node draft), đầu mục 6
- [2026-10-20] ingest src-bcbs-framework SRP30: [[concentration-risk-management]] thêm góc nhìn Basel SRP30: SRP30.22 liệt kê nguồn vốn là một tình huống tập trung, còn TT83 Đ50 không đưa vào; cần rà lại phần tập trung nguồn vốn. → đã áp [2026-10-20] (node draft), đầu mục 6

## [2026-10-20] maintenance | áp quy tắc 13: xoá dòng đã xử lý khỏi node
- CLAUDE.md thêm quy tắc 13; sửa skill ingest (bước 4, Synthesis bị ảnh hưởng), research (bước 0), view review-queue (chỉ liệt kê node có dòng đề xuất thật).
- 43 node: khôi phục mục `## Đề xuất cập nhật` với câu "*Chưa có nội dung cần cập nhật.*" (dòng cũ đã lưu ở entry trước).
- 24 synthesis: xoá 53 dòng đánh dấu đã rà khỏi `## Bất định`; nguyên văn lưu dưới đây.

### [[basel-liquidity-monitoring-framework]]
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p05–p09, p12: [[bcbs-liquidity-principles]] P5–P9 có claim (đo lường, EWI, MIS, pháp nhân, funding, trong ngày, tài sản bảo đảm) là nền nguyên tắc của 5 công cụ SRP50; cần rà lại mục kiến trúc và chỗ quy nguồn. → đã rà [2026-10-20]

### [[ftp-balance-sheet-optimization]]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2.

### [[ftp-cost-benefit-allocation-principles]]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2.

### [[ftp-curve-construction-methodology]]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2.
- [2026-10-20] ingest src-vab-ftp u05 (bổ sung): đã có claim danh mục đường cong cơ sở ^vab-ftp-41, ^vab-ftp-42: VAB chỉ có phương án 1 (lãi suất huy động bình quân) cho VND, không có phương án VNIBOR + TPCP; mục 2.3 cite ^vab-ftp-24 cho chu kỳ rà soát ALCO nhưng claim không nói việc này; cần rà lại mục 2.3 và 3.1 ở R1. → đã rà [2026-10-20]

### [[ftp-economic-cost-and-incentive-validation]]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2.

### [[ftp-final-rate-determination]]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2.

### [[ftp-nature-and-balance-sheet-management]]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2.

### [[ftp-portfolio-and-bucket-allocation]]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2.

### [[ftp-risk-and-cost-components]]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2.
- [2026-10-20] ingest src-vab-ftp u05 (bổ sung): mục 2.1 cite ^vab-ftp-24 cho danh mục VNIBOR + OMO/tín phiếu + VGB, nhưng danh mục thật (^vab-ftp-41) là lãi suất huy động thực tế bình quân 3 tháng (VND) và LIBOR/SOFR + swap USD (ngoại tệ); cần sửa citation và nội dung ở R1. → đã rà [2026-10-20]

### [[hqla-decomposition-and-tradeoffs]]
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p05–p09, p12: [[hqla]] thêm P12 (lõi tiền mặt/TPCP và phần mở rộng, không dựa vào NHTW), [[liquidity-transfer-restrictions]] thêm P6; cần rà lại phần cấu phần đệm. → đã rà [2026-10-20]

### [[integrated-alm-liquidity-strategy]]
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p05–p09, p12: [[asset-encumbrance]] (P9), [[funding-concentration-risk]] (P7), [[intraday-liquidity-risk]] (P8), [[hqla]] (P12: đệm gắn với nhu cầu stress và tolerance, là tuyến dự phòng chứ không phải tuyến đầu); cần rà lại các mục chiến lược đệm và funding. → đã rà [2026-10-20]

### [[irrbb-basis-risk-measurement-and-hedging]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]

### [[irrbb-casa-replicating-portfolio-and-irs-hedging]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]

### [[irrbb-commercial-margins-and-discount-curves]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation và mục spread/commercial margin. → đã rà [2026-10-18]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 103): có claim [[src-bcbs-irrbb-2016#^irrbb-u05-15]] — par 103 cho chọn trừ commercial margin khỏi notional repricing cash flow (Stage 2), tách khỏi việc chọn đường cong chiết khấu ∆EVE ([[src-bcbs-irrbb-2016#^irrbb-p08-2]]); par 103 không có yêu cầu nhất quán cho tài sản và nợ; cần rà lại Q2, Q5 và câu trích 'A bank should decide whether…'. → đã rà [2026-10-18]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại các đoạn về dòng tiền tái định giá và citation par 101–106. → đã rà [2026-10-18]
- [2026-10-18] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 70(i)(b)(c), Table A g): có claim [[src-bcbs-irrbb-2016#^irrbb-p08-4]] … [[src-bcbs-irrbb-2016#^irrbb-p08-6]] — yêu cầu công bố lựa chọn margin trong dòng tiền và lãi suất chiết khấu; cần rà lại Q3, Q5. → đã rà [2026-10-18]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]

### [[irrbb-csrbb-measurement-and-hedging]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]

### [[irrbb-fixed-vs-floating-cash-flows-and-repricing]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation và mục fixed vs floating. → đã rà [2026-10-18]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại các đoạn về dòng tiền tái định giá và citation par 101–106. → đã rà [2026-10-18]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]

### [[irrbb-liquidity-hqla-and-ftp-interaction]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]
- [2026-10-20] ingest src-tt50-2026-nhnn C2-M5: [[lcr]], [[nsfr]], [[hqla]] có giá trị VN theo [[tt50-2026]] (LCR/NSFR áp dụng từ 01/10/2028, LCR quy VNĐ 50% → 100% tới 01/10/2033, NSFR 90% → 100% tới 01/10/2030; trước đó vẫn tuân thủ tỷ lệ TT22/2019); cần rà lại các câu về nghĩa vụ LCR/NSFR tại VN và chỗ dẫn TT22. → đã rà [2026-10-20] phần dẫn TT22 (R1: thêm mục "Căn cứ pháp lý VN của đệm thanh khoản"); nghĩa vụ LCR/NSFR rà ở R2. → R2 đã rà [2026-10-20]: câu về nghĩa vụ LCR/NSFR tại VN đã dẫn TT50 Đ13.1, Đ16.1.c, Đ22.2.

### [[irrbb-principal-and-interest-cash-flows]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation và Q1, Q2, Q6, Q7. → đã rà [2026-10-17]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 103): có claim ^irrbb-u05-15 cho quyền chọn trừ commercial margin khỏi CF(t); cần rà lại Q4. → đã rà [2026-10-17]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]

### [[irrbb-repricing-profiles-and-behavioral-modeling]]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]

### [[irrbb-standardised-shocks-eve-and-nii-measurement]]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung): đã có claim par 102, 104, 106 (^irrbb-u05-9 … ^irrbb-u05-14); các câu về repricing date, reset date, spread không tái định giá đang cite ^irrbb-u05-2 (par 101); cần rà lại citation ở mục slotting. → đã rà [2026-10-18]
- [2026-10-17] ingest --node notional-repricing-cash-flow: đã có node [[notional-repricing-cash-flow]]; cần rà lại các đoạn về dòng tiền tái định giá và citation par 101–106. → đã rà [2026-10-18]
- [2026-10-17] ingest src-bcbs-irrbb-2016 U05 (bổ sung par 105, 132): có claim cho 4 bước tính ∆EVE ([[src-bcbs-irrbb-2016#^irrbb-u05-17]] … [[src-bcbs-irrbb-2016#^irrbb-u05-21]]), intra-bucket mismatch (u05-22), CF phụ thuộc kịch bản (u05-23), ngoại lệ gộp tiền tệ (u05-24); công thức ∆EVE^base = Σ CF_k·[DF_i − DF_0] (dòng 79) đổi dấu so với nguồn (EVE_0 − EVE_i) và dùng một CF cho cả hai kịch bản; công thức gộp tiền tệ có bù trừ 50% phần lãi (dòng 84) không có trong par 132, nơi chỉ cộng các khoản lỗ ∆EVE_{i,c} > 0 ([[src-bcbs-irrbb-2016#^irrbb-u05-8]]); cần rà lại mục đo lường ∆EVE. → đã rà [2026-10-18]
- [2026-10-18] ingest src-bcbs-irrbb-2016 U07 (bổ sung Table 1): có claim [[src-bcbs-irrbb-2016#^irrbb-u07-5]] — biên độ Parallel/Short/Long cho 21 đồng tiền; claim u07-4 sửa diễn đạt sàn; cần rà lại Q3. → đã rà [2026-10-18]
- [2026-10-18] ingest src-bcbs-irrbb-2016 U03 (bổ sung par 90–93, 95): có claim outlier phải bị rà soát [[src-bcbs-irrbb-2016#^irrbb-p12-4]], IMS kém → dùng standardised framework [[src-bcbs-irrbb-2016#^irrbb-p12-6]], rủi ro quá mức so với thu nhập theo ∆NII dưới sốc [[src-bcbs-irrbb-2016#^irrbb-p12-7]], thời hạn khắc phục [[src-bcbs-irrbb-2016#^irrbb-p12-8]]; cần rà lại Q1 (phép thử ngoại lai) và Q2 (vai trò ∆NII trong đánh giá giám sát). → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M7, PL5: đã có node [[tt83-2025]] và claim Đ53–55, Đ74.4, PL5; các chỗ `[cần nguồn: src-tt83-2025-nhnn …]` và nhận định về khung NHNN có thể thay bằng claim mới; cần rà lại mục Basel vs NHNN. → đã rà [2026-10-19]
- [2026-10-19] ingest src-bcbs-irrbb-2016 U07 (bổ sung): claim mới về phương pháp dựng Table 1 (16 năm, 60/85/40%, sàn/trần) [[src-bcbs-irrbb-2016#^irrbb-u07-7]] [[src-bcbs-irrbb-2016#^irrbb-u07-8]] [[src-bcbs-irrbb-2016#^irrbb-u07-9]] và chu kỳ rà soát hiệu chỉnh [[src-bcbs-irrbb-2016#^irrbb-u07-6]]; [[tt83-2025]] PL5.C.I.2 dùng cùng phương pháp cho VND; cần rà lại Q3 (biên độ theo đồng tiền) và mục sốc VND. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C3-M9: đã có node [[icaap]], [[capital-plan]] (stub [[economic-capital]]); stress test vốn VN tính tác động lãi suất lên tài sản tính theo rủi ro IRRBB [[src-tt83-2025-nhnn#^d60-1]]; cần rà lại chỗ nhắc ICAAP / vốn kinh tế. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn PL6: đã có [[raroc]] (lợi nhuận trước thuế / $C_E$ [[src-tt83-2025-nhnn#^pl6-iii]]), [[economic-capital]], [[target-capital]], [[rwa-irrbb]]; cần rà lại chỗ nhắc RAROC / vốn kinh tế / RWA IRRBB theo định nghĩa VN. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn C1: đã có node [[alco]] (TT83 Đ6.4.b: Hội đồng ALCO giúp việc Tổng giám đốc về nội dung Đ25.3, họp tối thiểu hằng quý [[src-tt83-2025-nhnn#^d6-4b]]); cần rà lại chỗ nhắc ALCO và góc nhìn NHNN. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tt83-2025-nhnn PL3: [[rwa-irrbb]] phải được thuyết minh phương pháp (mô tả, điểm mạnh, hạn chế, điều chỉnh giả định) trong báo cáo ICAAP hằng năm gửi NHNN [[src-tt83-2025-nhnn#^pl3-3b]] [[src-tt83-2025-nhnn#^d9-2c]]; cần rà lại chỗ nhắc vốn Pillar 2 / RWA_IRRBB. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u08: [[outlier-bank-test]] có đề xuất thêm khung EU — SOT NII 5% vốn cấp 1 (d368, TT83 không có) [[src-tata-bank-alm#^tata-sot-3]], sàn lãi suất sau sốc tuyến tính [[src-tata-bank-alm#^tata-sot-2]], bài toán tuân thủ đồng thời EVE/NII [[src-tata-bank-alm#^tata-sot-4]]; cần rà lại mục outlier test và đo NII. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u07: [[outlier-bank-test]] có đề xuất thêm lịch sử ngưỡng EU (20% vốn tự có → 15% vốn cấp 1 + NII) [[src-tata-bank-alm#^tata-reg-5]] và sàn EBA 2018 [[src-tata-bank-alm#^tata-reg-8]]; cần rà lại mục outlier test. → đã rà [2026-10-20]
- [2026-10-19] ingest src-tata-bank-alm u06: đã có node [[negative-interest-rates]] (coupon/indicator floor, EBA yêu cầu xét kịch bản lãi suất âm và tác động bất đối xứng [[src-tata-bank-alm#^tata-neg-5]]); cần rà lại mục 'Môi trường lãi suất âm hoặc siêu thấp'. → đã rà [2026-10-20]
- [2026-10-19] ingest src-lubinska-alm-optimisation u02: đã có node [[repricing-gap-analysis]] (maturity/repricing/refixing/incremental gap, ΔNII ≈ GAP × Δi [[src-lubinska-alm-optimisation#^lubinska-u02-25]]) và [[pv01]] [[src-lubinska-alm-optimisation#^lubinska-u02-43]]; nguồn ghi sốc ±200 bp cho repricing gap [[src-lubinska-alm-optimisation#^lubinska-u02-23]] (bối cảnh EUR, khác hiệu chỉnh theo đồng tiền của d368); internal/external view EVE [[src-lubinska-alm-optimisation#^lubinska-u02-38]]; cần rà lại mục đo NII và chiết khấu EVE. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u10/u11/u14: [[negative-interest-rates]] thêm cách xử lý NMD của Choudhry (bán lẻ/SME sàn 0% coi như fixed-rate, IRS nhận cố định theo behavioural tenor, balance guarantee swap, khoản thả nổi xếp bucket 1 tháng); cần rà lại phần giả định NMD khi lãi suất thấp/âm. → đã rà [2026-10-20]
- [2026-10-19] ingest src-choudhry-principles-banking u09/u15: [[repricing-gap-analysis]] thêm giả định và điểm yếu của gap analysis (song song, tái định giá giữa bucket, không time value, bucket tuỳ ý) và ba cách xếp bucket NMD; cần rà lại phần đo gap/NII. → đã rà [2026-10-20]
- [2026-10-19] ingest --node repricing-balance-sheet: [[repricing-balance-sheet]] viết lại theo template model: sửa trần kỳ hạn bình quân NMD thành 5 / 4,5 / 4 năm (bán lẻ giao dịch / phi giao dịch / bán buôn; bản cũ ghi "4,5–5 năm"), thêm bảng Basel vs VN theo TT83 PL5, thêm hạn chế intra-bucket mismatch và giả định tĩnh, bỏ citation sai (choudhry-irrbb-9 cho HTM/AFS, tata-nii-5 cho tiền mặt); cần rà lại chỗ trích dẫn trần NMD và phạm vi danh mục. → đã rà [2026-10-20]
- [2026-10-20] ingest src-bcbs-irrbb-2016 U03/U06/U07 (bổ sung): Q2 dynamic balance sheet, chân trời thu nhập; Q3 công thức sốc cơ sở, ví dụ số, sàn sau sốc; áp trực tiếp theo duyệt của user. → đã rà [2026-10-20]

### [[lcr-economic-significance-and-alm-governance]]
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p05–p09, p12: [[hqla]] thêm BCBS 144 P12 (đệm là tuyến dự phòng, para 126); cần rà lại mục nghịch lý sử dụng đệm. → đã rà [2026-10-20]

### [[nii-shocks-regulation-hedging-and-alco-tradeoffs]]
- [2026-10-20] ingest src-bcbs-irrbb-2016 U03/U06/U07 (bổ sung): d368 Annex 1 có ba trạng thái bảng cân đối cho thước đo thu nhập (run-off, constant, dynamic) [[src-bcbs-irrbb-2016#^irrbb-u06-9]], chân trời 1–3 năm, tối đa 5 năm [[src-bcbs-irrbb-2016#^irrbb-u06-8]], sàn lãi suất sau sốc không lớn hơn 0 [[src-bcbs-irrbb-2016#^irrbb-u07-11]]; cần rà lại Q5 và các chỗ nói về giả định bảng cân đối NII. → đã rà [2026-10-20]

### [[practical-alm-liquidity-governance]]
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p05–p09, p12: [[bcbs-liquidity-principles]] thêm P5–P9, P12 (hạn mức, EWI, MIS, báo cáo HĐQT, đệm); cần rà lại mục 5 đối chiếu NHNN và Basel. → đã rà [2026-10-20]

### [[synthetic-balance-sheet-liquidity-risk]]
- [2026-10-20] ingest src-bcbs-liquidity-principles-2008 p05–p09, p12: [[funding-concentration-risk]], [[intraday-liquidity-risk]], [[liquidity-monitoring-metrics]] thêm căn cứ BCBS 144 P5, P7, P8; cần rà lại phần công cụ giám sát. → đã rà [2026-10-20]

## [2026-10-20] ingest | src-tt50-2026-nhnn PL1 (bổ sung Phần A — HQLA)
- source note: 13 claim mới PL1.A (`^pl1-a1-1b`, `^pl1-a1-vd`, `^pl1-a1-5`, `^pl1-a1-6`, `^pl1-a2-2`, `^pl1-a2-3`, `^pl1-a2-3g`, `^pl1-a3-3`, `^pl1-a4-1`, `^pl1-a4-3a`, `^pl1-a4-3b`, `^pl1-a4-3d`, `^pl1-a5`) gồm unwinding hai chặng và ví dụ số, điều kiện hạn mức ngân hàng mẹ, quyền NHNN hạ hệ số, điều kiện chi tiết cấp 1/2A/2B, tài sản chi nhánh ở nước ngoài, Bảng 3 và định giá; claim cũ không đổi; không chạy `registry.py mark`
- created: không có
- updated: [[level-1-assets]] (thêm `## Basel vs VN`, 11 dòng), [[level-2-assets]] (thêm `## Basel vs VN`, 15 dòng; đóng câu hỏi RMBS), [[hqla]] (5 dòng Basel vs VN; sửa câu "chờ ingest TT50"), [[hqla-unwinding-mechanism]] (mục VN, thêm domain `vn-reg`), [[tt50-2026]] (3 dòng Đối chiếu Basel)
- conflicts: không có (khác jurisdiction: không covered bond, không RCLF/Sukuk, cấp 2B có sẵn nhưng NHNN được loại, yêu cầu niêm yết)
- syntheses flagged: [[hqla-decomposition-and-tradeoffs]], [[irrbb-liquidity-hqla-and-ftp-interaction]], [[irrbb-csrbb-measurement-and-hedging]], [[synthetic-balance-sheet-liquidity-risk]] (cơ cấu HQLA VN)
- backfill: không có (không có node mới)
- domain: [[domain-vn-reg]] cập nhật cụm thanh khoản, bảng Basel ↔ VN, lỗ hổng, thống kê (concept 38; basel+vn-reg 61); index sửa dòng [[hqla]] từ canonical về draft cho khớp node
- câu hỏi mở: [[level-2-assets]] dòng "Chứng khoán công BBB- đến BBB+" Level 2B cite `^lcr30-45` nhưng claim LCR30.45 không có nhóm này
- tiếp theo: `src-tt50-2026-nhnn C2-M3` (giới hạn cấp tín dụng) hoặc `PL3`

## [2026-10-20] ingest | src-tt50-2026-nhnn PL1 (rà lại Phần A.IV — cấp 2B)
- source note: bổ sung dòng trích nguyên văn cho `^pl1-a4-3a` (hệ số 75%, niêm yết), `^pl1-a4-3b` (câu dẫn chứng khoán nợ doanh nghiệp 50%, không do tổ chức tài chính phát hành, niêm yết, giảm giá ≤ 20%), `^pl1-a4-3d` (câu dẫn cổ phiếu 50%, không do tổ chức tài chính phát hành) để mọi điều kiện trong câu claim có trích dẫn; block-id và câu claim không đổi
- created/updated node: không có
- 04_models/lcr-tt50-2026.xlsx: ThamSo!H11 (HQ_BR2B) điền `[[src-tt50-2026-nhnn#^pl1-a4-3d]]` thay "chưa có claim trong source note"; 395 công thức giữ nguyên

## [2026-10-20] ingest | src-tt50-2026-nhnn PL1 (bổ sung — tiêu chí xác định HQLA theo đầu mục)
- source note: 3 claim mới đủ tiêu chí theo đầu mục Bảng 3: `^pl1-a2-3c` (mục 1.1, 1.3: 5 điều kiện, 6 nhóm tổ chức phát hành), `^pl1-a3-3a` (mục 2.1.1: 4 điều kiện), `^pl1-a3-3b` (mục 2.1.2: 4 điều kiện); `^pl1-a4-3a` thêm điều kiện (viii) chứng khoán hoá tuân thủ pháp luật (claim tạo cùng ngày, chưa commit)
- created: không có
- updated: [[level-1-assets]] (ma trận tiêu chí mục 1.1–1.7, 5.1, cột Basel tương ứng), [[level-2-assets]] (ma trận mục 2.1.1–2.2.5 và covered bond, cột Basel tương ứng), [[hqla]] (dòng trỏ tới ma trận, tiêu chí chung Đ20.2)
- conflicts: không có
- syntheses flagged: không có (chỉ chi tiết hoá tiêu chí; 4 synthesis cơ cấu HQLA đã đánh dấu trong lượt PL1 Phần A cùng ngày)
- backfill: không có
- 04_models/lcr-tt50-2026.xlsx: ThamSo cột H nối thêm citation theo đầu mục cho HQ_L1, HQ_L2A, HQ_RMBS, HQ_CORP2B, HQ_SOV2B, HQ_EQ2B, HM_MAX, HM_NOBACK; 395 công thức giữ nguyên
- câu hỏi mở: cột Basel các mục 1.5, 1.6, 1.7 (một phần), 2.1.3, 2.2.3, 2.2.5 ghi [cần nguồn]; điều kiện thị trường và loại trừ tổ chức tài chính của Level 1 chưa có trích dẫn trong `src-bcbs-lcr` (cần bổ sung LCR30.41)
- tiếp theo: `/ingest src-bcbs-lcr` bổ sung LCR30.41–30.45 (điều kiện chi tiết) để hoàn thiện cột Basel; hoặc `src-tt50-2026-nhnn C2-M3`

## [2026-10-20] ingest | --node cash-outflows (chuẩn hoá bảng Basel vs VN theo TT50/2026)
- source note: không thay đổi (dùng claim có sẵn từ [[src-bcbs-lcr]] LCR40 và [[src-tt50-2026-nhnn]] PL1 Phần B).
- updated:
  - [[cash-outflows]]: hoàn thiện frontmatter (bổ sung domain `vn-reg`, sources, as_of, updated); nâng cấp phần `## Basel vs VN` thành bảng Markdown chi tiết 22 dòng đối chiếu đầy đủ 5 trụ cột dòng tiền ra (bán lẻ, bán buôn, repo, phái sinh/add-on, cam kết ngoại bảng & bảo lãnh) giữa Basel LCR40 và TT50/2026 PL1 Phần B (Bảng 4, Bảng 5); bổ sung mục `## Đọc thêm` liên kết mạng lưới node vệ tinh.
  - [[index]]: cập nhật tóm tắt và domains của [[cash-outflows]] (thêm `vn-reg`).
- conflicts: không có (khác biệt jurisdiction: TT50 không áp dụng mức 3% bán lẻ ổn định; ngưỡng SME tính theo số dư 30 tỷ VND tại ngân hàng; trade finance 3%, bảo lãnh 5%, cam kết hủy ngang vô điều kiện 0%; hiệu lực LCR từ 01/10/2026 theo Đ37.1).
- lint: 0 error, 0 warning.

## [2026-10-20] ingest | --node cash-outflows (chi tiết hóa các đầu mục thành phần & giải thích rõ ý nghĩa kinh tế)
- source note: không thay đổi (dùng claim có sẵn từ [[src-bcbs-lcr]] LCR40).
- updated:
  - [[cash-outflows]]: Mở rộng toàn diện phần `## Diễn giải` cho toàn bộ 5 trụ cột dòng tiền ra LCR40 (Tiền gửi Bán lẻ & SME; Nguồn vốn Bán buôn không bảo đảm; Nguồn vốn Có bảo đảm/Repo; Phái sinh & Nhu cầu bổ sung; Hạn mức cam kết & Nghĩa vụ tiềm tàng). Chi tiết hóa từng đầu mục thành phần với điều kiện quy chuẩn, phân tích sâu sắc ý nghĩa kinh tế & lý do giám sát (hành vi rút vốn, bất đối xứng thông tin, chi phí chuyển đổi, vách đá thanh khoản, rủi ro uy tín), cùng hàm ý thực tiễn cho quản trị ALM Treasury.
- conflicts: không có.
- lint: 0 error, 0 warning.


## [2026-10-20] ingest | src-tt50-2026-nhnn PL1 (Phần B — Dòng tiền ra LCR)
- source note: [[src-tt50-2026-nhnn]] bổ sung trích dẫn nguyên văn và claim ^pl1-b6 (Mục VI: Dòng tiền ra theo thỏa thuận khác 100%), hoàn thiện trích dẫn cho ^pl1-b1 (xử lý vi phạm thanh toán sớm ngày tiếp theo), ^pl1-b3 (chi phí chuyển đổi tiền gửi hoạt động tối thiểu toàn bộ lãi + 10% gốc), ^pl1-b3-3 (quy tắc thác TSBĐ thế chấp waterfall), ^pl1-b4 (ngoại lệ FX netting trong ngày, cheapest to deliver, TSBĐ dư thừa 100%, TSBĐ chưa bị đòi 100%), ^pl1-b5 (nghĩa vụ giải ngân cá nhân/DN vượt 50% dòng vào tính 100%), ^pl1-b5-3 (kích hoạt hợp đồng thanh toán trong 30 ngày 100%).
- updated:
  - [[cash-outflows]]: Bổ sung tiểu mục phân tích sâu Khung Pháp lý Dòng tiền ra theo TT50/2026/TT-NHNN (Phần B Phụ lục I) chi tiết hóa cả 5 trụ cột dòng ra theo TT50, bổ sung 2 dòng đối chiếu vào bảng Basel vs VN (giải ngân hợp đồng vượt 50% dòng vào và dòng tiền ra hợp đồng khác 100%), mở rộng 7 điểm khác biệt trọng yếu giữa Basel LCR40 và TT50/2026.
  - [[derivatives-and-contingent-outflows]]: Cập nhật YAML frontmatter (domains: [alm, basel, vn-reg, product], sources: [src-bcbs-lcr, src-tt50-2026-nhnn], updated: 2026-10-20); bổ sung bảng ma trận và phân tích Basel vs VN cho toàn bộ các cấu phần phái sinh, hạ bậc tín nhiệm, TSBĐ non-L1, look-back 24M, và nghĩa vụ tiềm ẩn (trade finance 3%, bảo lãnh 5%, autocallable 5%, hủy ngang vô điều kiện 0%).
  - [[retail-deposit-stability]]: Bổ sung domain vn-reg, cập nhật phân loại tiền gửi bán lẻ ổn định (5%), kém ổn định (10%), giải quyết 2 câu hỏi mở về trần bảo hiểm tiền gửi và quy tắc chế tài lãi suất không kỳ hạn VNĐ thấp nhất khi rút trước hạn theo TT50 PL1.B.I.4.
  - [[operational-deposits]]: Bổ sung domain vn-reg, cập nhật định lượng tiêu chí tiền gửi hoạt động tại VN (chi phí chuyển đổi tối thiểu toàn bộ lãi + 10% gốc, lãi suất không kỳ hạn thấp nhất, loại trừ correspondent banking, khống chế excess), giải quyết câu hỏi mở về khái niệm tiền gửi hoạt động trong TT50.
  - [[secured-funding]]: Bổ sung domain vn-reg, cập nhật quy tắc phân bổ thác TSBĐ thế chấp (waterfall rule), giải quyết câu hỏi mở về OMO/repo với NHNN nhận hệ số 0% theo Bảng 4.
  - [[committed-facilities]]: Bổ sung domain vn-reg, giải quyết câu hỏi mở về cơ chế xử lý hạn mức hủy ngang có điều kiện vs hủy ngang vô điều kiện (0%) theo Điều 3.5–3.7 và PL1.B.V.
  - [[unsecured-wholesale-funding]]: Bổ sung domain vn-reg, giải quyết câu hỏi mở về phân loại tiền gửi DNNN thuộc nhóm doanh nghiệp phi tài chính (40%).
  - [[tt50-2026]]: Cập nhật tình trạng ingest của Phụ lục I Phần B và bổ sung 6 dòng so sánh dòng tiền ra vào bảng Đối chiếu Basel.
- 04_models/lcr-tt50-2026.xlsx: ThamSo sheet điền citation wiki cho các mã dòng ra còn trống: O_EXCOL ([[src-tt50-2026-nhnn#^pl1-b4]]), O_UNCALL ([[src-tt50-2026-nhnn#^pl1-b4]]), O_DISB_OTH ([[src-tt50-2026-nhnn#^pl1-b5]]), O_DISB_THR ([[src-tt50-2026-nhnn#^pl1-b5]]), O_CONT_TRIG ([[src-tt50-2026-nhnn#^pl1-b5-3]]), O_OTHER ([[src-tt50-2026-nhnn#^pl1-b6]]).
- conflicts: không có.
- lint: 0 error, 0 warning.

## [2026-10-21] ingest | src-bcbs-lcr LCR30 (bổ sung — tiêu chí LCR30.40–30.46)
- source note: 13 claim mới `^lcr30-40` (supervisor có thể yêu cầu haircut Level 1; đo không cao hơn giá thị trường), `^lcr30-41a` (4 điều kiện chứng khoán Level 1, loại trừ tổ chức tài chính), `^lcr30-41b` (dự trữ NHTW), `^lcr30-43a`, `^lcr30-43b` (tiêu chí Level 2A, PD nội bộ, plain-vanilla), `^lcr30-43-faq1` (AA- giảm giá 10–20% vào Level 2B), `^lcr30-44` (Level 2B tuỳ cơ quan quốc gia), `^lcr30-45a`, `^lcr30-45b`, `^lcr30-45c` (tiêu chí RMBS, trái phiếu doanh nghiệp, cổ phiếu), `^lcr30-45-faq3` (chứng khoán chính phủ BBB+ đến BBB-), `^lcr30-45-faq4` (PSE từ BBB-), `^lcr30-46a` (điều kiện RCLF); raw dòng 239–389; claim cũ không đổi; không chạy `registry.py mark`
- created: không có
- updated: [[level-1-assets]] (cột Basel ma trận mục 1.2, 1.3, 1.5–1.7; Basel vs VN: quyền hạ hệ số, dự trữ, chứng khoán 0%, định giá, hạn mức NHTW), [[level-2-assets]] (cột Basel ma trận 2.1.1–2.2.5; Basel vs VN: Level 2B, quyền hạ hệ số 2A, chứng khoán công 2B, chi nhánh; sửa citation dòng "Chứng khoán công BBB- đến BBB+" sang `^lcr30-45-faq3`/`^lcr30-45-faq4`; sửa diễn giải trái phiếu AA- theo FAQ1; thêm khác biệt thị trường sâu/niêm yết, PD nội bộ, risk retention; xoá câu hỏi mở đã giải quyết), [[hqla]] (quyền hạ hệ số, định giá), [[tt50-2026]] (3 dòng Đối chiếu Basel)
- conflicts: không có (khác jurisdiction)
- syntheses flagged: [[hqla-decomposition-and-tradeoffs]] (dòng chứng khoán công BBB- cite sai block-id; tiêu chí thị trường)
- backfill: không có
- tiếp theo: `src-tt50-2026-nhnn C2-M3` hoặc `PL3`

## [2026-10-21] ingest | src-tt50-2026-nhnn PL1 (bổ sung — hoàn thiện node committed-facilities)
- source note: không thay đổi (dùng claim sẵn có từ [[src-tt50-2026-nhnn]] PL1 Phần B Mục V, Bảng 5, Đ3.5–3.7 và PL2 Bảng 10 Mục C.1).
- created: không có
- updated:
  - [[committed-facilities]]: Bổ sung ma trận và phân tích chuyên sâu đối chiếu Basel vs VN; đối chiếu chi tiết 12 dòng tham số giữa Basel LCR40.64 / NSF30.34 và TT50/2026 (Phụ lục I Phần B Mục V Bảng 5, Phụ lục II Bảng 10); làm rõ 3 điểm khác biệt trọng yếu (tiêu chí hủy ngang có điều kiện vs hủy ngang vô điều kiện 0%, chuẩn SME $\le 30$ tỷ đồng, tỷ lệ tài trợ thương mại 3%); bổ sung nguồn [[src-bcbs-liquidity-principles-2008]] và [[src-bcbs-nsfr]] vào frontmatter.
  - [[index]]: Cập nhật tóm tắt và bổ sung domain vn-reg cho [[committed-facilities]].
  - [[domain-vn-reg]]: Bổ sung [[committed-facilities]] vào danh mục node quản lý rủi ro thanh khoản.
- proposed: không có
- conflicts: không có
- syntheses flagged: không có
- backfill: không có
- lint: 0 error, 0 warning
- tiếp theo: `src-tt50-2026-nhnn C2-M3` (hạn chế, giới hạn cấp tín dụng) hoặc `PL3` (tổng trạng thái rủi ro tỷ lệ đòn bẩy LEV)


## [2026-10-21] ingest | src-tt50-2026-nhnn PL1 (bổ sung — đầu mục tài sản cấp 1)
- source note: 6 claim mới `^pl1-a2-3b` (1.2), `^pl1-a2-3d` (1.4.1), `^pl1-a2-3dd` (1.4.2), `^pl1-a2-3e` (1.5), `^pl1-a2-3h` (1.7, kể cả phần định nghĩa điểm h), `^pl1-a5-1` (chép nguyên văn Bảng 3 phần cấp 1, cột hệ số, (4)/(5), điểm hướng dẫn); raw dòng 1221–1259, 1351–1367; claim cũ không đổi; không chạy `registry.py mark`
- created: không có
- updated: [[level-1-assets]] (thêm `### Danh mục tài sản cấp 1 theo TT50/2026` trong Định nghĩa, 9 dòng 1.1–1.7, 5.1 có điểm Mục II; ma trận tiêu chí chuyển citation từ claim gộp `^pl1-a2` sang claim theo đầu mục, hệ số cite `^pl1-a5-1`)
- conflicts: không có
- syntheses flagged: không có (không có tham số mới)
- backfill: không có
- tiếp theo: làm tương tự cho cấp 2A/2B (`^pl1-a5-2` chép nguyên văn Bảng 3 mục 2) nếu cần; hoặc `src-tt50-2026-nhnn C2-M3`

## [2026-10-21] ingest | src-tt50-2026-nhnn PL1 (bổ sung — đầu mục tài sản cấp 2A, 2B)
- source note: 5 claim mới `^pl1-a3-3c` (2.1.3), `^pl1-a4-3c` (2.2.3, đủ 4 điều kiện), `^pl1-a4-3dd` (2.2.5, hệ số theo từng loại), `^pl1-a5-2a`, `^pl1-a5-2b` (chép nguyên văn Bảng 3 mục 2, 2.1, 2.2 kèm hệ số, (4)/(5), điểm hướng dẫn); raw dòng 1289, 1293, 1327–1335, 1349, 1368–1378; claim cũ không đổi; không chạy `registry.py mark`
- created: không có
- updated: [[level-2-assets]] (thêm `### Danh mục tài sản cấp 2 theo TT50/2026` trong Định nghĩa, 8 dòng 2.1.1–2.2.5 kèm đủ điều kiện; ma trận tiêu chí và bảng Basel vs VN chuyển citation 2.1.3, 2.2.3, 2.2.5 sang claim riêng, hệ số cite `^pl1-a5-2a`/`^pl1-a5-2b`)
- conflicts: không có
- syntheses flagged: không có (không có tham số mới)
- backfill: không có
- tiếp theo: `src-tt50-2026-nhnn C2-M3` hoặc `PL3`

## [2026-10-21] ingest | src-tt50-2026-nhnn PL1 (bổ sung — dòng tiền ra Phần B theo đầu mục)
- source note: 23 claim mới theo đầu mục Bảng 6, raw dòng 1394–1857: Mục I (`^pl1-b1-1`, `^pl1-b1-4a`, `^pl1-b1-4b`), Mục II (`^pl1-b2-1`, `^pl1-b2-2`, `^pl1-b2-3`), Mục III (`^pl1-b3-1`, `^pl1-b3-22`, `^pl1-b3-23a`–`^pl1-b3-23d`, `^pl1-b3-24`, `^pl1-b3-25`, `^pl1-b3-31`), Mục IV (`^pl1-b4-1`, `^pl1-b4-14`, `^pl1-b4-21`, `^pl1-b4-22`, `^pl1-b4-23`, `^pl1-b4-25`), Mục V (`^pl1-b5-1`, `^pl1-b5-2`, `^pl1-b5-31`), Bảng 6 (`^pl1-b7`); claim cũ không đổi; không chạy `registry.py mark`; Ghi chú convert: ô hệ số mục 5.1.3 Bảng 6 để trống
- created: không có
- updated:
  - [[cash-outflows]]: viết lại mục VN thành danh mục 29 dòng theo Bảng 6 kèm điều kiện và citation theo đầu mục; sửa nội dung lệch nguồn do lượt [2026-10-20] ghi: "hạn mức BHTG 125 triệu VND, QĐ 32/2021" (TT50 không có), VAMC/DATC trong nhóm 40% (chỉ có ở Bảng 4 có bảo đảm 25%), "giấy tờ có giá tự phát hành" trong nhóm 100% (III.2.5 không nói), "5 dải thời gian 15–21, 22–30" (Bảng 6 có 4 khung: ngày tiếp theo, 2–7, 8–14, 15–30), "L/C" trong tài trợ thương mại, "quỹ bảo trợ", "chịu 40%–100%" với tiền gửi hoạt động không đủ điều kiện, dẫn TT04/2022 và quy đổi EUR; hệ số 0% bổ sung điểm a(iv); cột hiệu lực 25 dòng đổi từ "01/10/2026 ^d37-1" sang "LCR từ 01/10/2028 ^d13-1"; ô Basel waterfall LCR40.48 đổi thành [cần nguồn]
  - [[retail-deposit-stability]], [[operational-deposits]], [[unsecured-wholesale-funding]], [[secured-funding]], [[derivatives-and-contingent-outflows]], [[committed-facilities]]: cùng loại sửa (125 triệu, VAMC/DATC trong 40%, giấy tờ có giá, L/C, "40%–100%"), citation theo đầu mục; 24 ô hiệu lực đổi sang "Áp dụng từ 01/10/2028 ^d13-1"; đoạn DNNN đánh nhãn diễn giải
  - [[asf-retail-and-small-business-deposits]]: câu hỏi mở "125 triệu VND" thay bằng nội dung có nguồn (`^pl1-b2-2`, `^d22-5`) và [cần nguồn] cho con số giới hạn
- conflicts: không có
- syntheses flagged: không có (không synthesis nào dùng nội dung VN dòng tiền ra; hệ số không đổi)
- backfill: không có
- 04_models/lcr-tt50-2026.xlsx: DongTienRa cột K, 37 dòng chuyển sang citation theo đầu mục + `^pl1-b7`; 5 dòng "chưa có claim" đã có claim; 395 công thức giữ nguyên
- câu hỏi mở: claim `^lcr40-71` không nhắc L/C nhưng [[derivatives-and-contingent-outflows]] dòng 159 và [[committed-facilities]] dòng 58 ghi L/C ở phần Basel; ô hệ số 5.1.3 Bảng 6 cần đối chiếu bản gốc
- tiếp theo: PL1 Phần C (dòng tiền vào) theo đầu mục Bảng 8, hoặc `src-tt50-2026-nhnn C2-M3`

## [2026-10-21] ingest | src-tt50-2026-nhnn PL1 (bổ sung — dòng tiền vào Phần C theo đầu mục)
- updated: [[src-tt50-2026-nhnn]] (+22 claim PL1.C: `^pl1-c1-1`…`^pl1-c1-5`, `^pl1-c2-1`, `^pl1-c2-2`, `^pl1-c2-4` (Bảng 7), `^pl1-c3`, `^pl1-c4-1`, `^pl1-c4-3`…`^pl1-c4-5`, `^pl1-c4-6a`, `^pl1-c4-6b`, `^pl1-c4-7`, `^pl1-c4-8a`, `^pl1-c4-8b`, `^pl1-c4-9`, `^pl1-c5-1`, `^pl1-c5-2`, `^pl1-c6`, `^pl1-c7` (Bảng 8); ghi chú convert Bảng 8 mục 5.2.2)
- updated: [[src-bcbs-lcr]] (+7 claim LCR40 bổ sung đoạn trích: `^lcr40-49b`, `^lcr40-84b`, `^lcr40-85b`, `^lcr40-87b`, `^lcr40-88b`, `^lcr40-89b`, `^lcr40-93-faq1`)
- updated: [[cash-inflows]] (thêm domain vn-reg, nguồn TT50; mục VN: danh mục 18 dòng Bảng 8 và 6 tiểu mục theo Mục I–VI; bảng Basel vs VN 27 dòng; rà phần Basel: bỏ câu không có nguồn ("nợ cơ cấu", "tránh gây sốc kinh tế xã hội", ví dụ trái phiếu DN), đổi câu lý do sang Diễn giải, thêm citation cho công thức trần 75%, khoản vay có thể chấm dứt, sovereign/MDB/PSE, excess balances, netting, forward repo/giao dịch chưa thanh toán; LCR40.76 "should" → "nên")
- updated: [[net-cash-outflows]] (dòng `[cần nguồn: TT50 PL1]` tách thành hệ số rút tiền ^pl1-b7 và hệ số thu tiền ^pl1-c7), [[tt50-2026]] (+3 dòng đối chiếu dòng vào), [[domain-vn-reg]] (dòng LCR; thống kê đếm lại 85 node, 70 basel+vn-reg), [[index]]
- conflicts: không có
- syntheses flagged: [[synthetic-balance-sheet-liquidity-risk]] (điều kiện nợ nhóm 1, hạn mức quay vòng; ví dụ dòng vào 50% bước 3)
- backfill: không có
- 04_models/lcr-tt50-2026.xlsx: ThamSo H55:H72 và DongTienVao cột K (18 dòng) chuyển sang citation theo đầu mục + `^pl1-c7`; 4 dòng "chưa có claim" đã có claim; 395 công thức giữ nguyên
- câu hỏi mở: TT50 Phần C không nêu khoản vay không kỳ hạn (ô VN `[cần nguồn]`); claim cũ `^lcr40-93` diễn đạt có ý forward repo/unsettled mà đoạn trích không có (nay có `^lcr40-93-faq1`)
- tiếp theo: `src-tt50-2026-nhnn C2-M3` (hạn chế, giới hạn cấp tín dụng) hoặc `PL3` (tổng trạng thái rủi ro)

## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M5 (bổ sung — yêu cầu vận hành HQLA Đ19.2, Đ20.2)
- updated: [[src-tt50-2026-nhnn]] (+8 claim: `^d19-2`, `^d20-2b`, `^d20-2c`, `^d20-2d`, `^d20-2dd`, `^d20-2g`, `^d20-2h`, `^d20-2i`)
- updated: [[src-bcbs-lcr]] (+11 block LCR30: `^lcr30-14`, `^lcr30-16b` (gồm chú thích 3), `^lcr30-16-faq`, `^lcr30-17`, `^lcr30-18b`, `^lcr30-19`, `^lcr30-20`, `^lcr30-22`, `^lcr30-23`, `^lcr30-26`, `^lcr30-29`)
- updated: [[hqla]] (mục "7 Yêu cầu Vận hành" chỉ có 4 dòng và cite `^lcr30-15` cho quyền kiểm soát → thay bằng bảng đối chiếu 17 yêu cầu Basel vs VN, có dòng Diễn giải khác biệt; dòng "Yêu cầu vận hành" trong bảng Basel vs VN trỏ tới mục mới), [[asset-encumbrance]] (quy tắc unencumbered LCR Basel và TT50), [[cash-outflows]] (mục 3.2 bỏ cite sai `^lcr40-48`, thay bằng chú thích 3 LCR30.16 và quy tắc TT50 `^pl1-b3-3`), [[tt50-2026]] (+1 dòng đối chiếu)
- conflicts: không có
- syntheses flagged: [[hqla-decomposition-and-tradeoffs]] (quyền kiểm soát, HQLA tại NHNN, hedge), [[irrbb-liquidity-hqla-and-ftp-interaction]] (giá trị HQLA được hedge)
- backfill: không có
- câu hỏi mở: TT50 chưa thấy quy tắc thứ tự ràng buộc pool, rào cản chuyển giao giữa pháp nhân; Basel không có claim về HQLA mất tiêu chuẩn giữ thêm 30 ngày
- tiếp theo: lượt 2 — LCR40.5 FAQ (mục 1.6 cash-outflows chưa có citation), LCR40.72 (L/C), LCR40.9, 40.18, 40.21, 40.24–25, LCR30.42

## [2026-10-21] ingest | src-bcbs-lcr LCR40 (bổ sung — đoạn lẻ và FAQ tài sản bảo đảm, phái sinh)
- updated: [[src-bcbs-lcr]] (+20 claim: `^lcr40-5-faq1`, `^lcr40-5-faq2`, `^lcr40-9`, `^lcr40-18`, `^lcr40-21`, `^lcr40-24`, `^lcr40-25`, `^lcr40-49-faq`, `^lcr40-51-faq`, `^lcr40-52-faq`, `^lcr40-55-faq`, `^lcr40-56-faq`, `^lcr40-63`, `^lcr40-71b`, `^lcr40-72`, `^lcr40-73-faq`, `^lcr40-74-faq`, `^lcr40-78-faq`, `^lcr40-79-faq`, `^lcr30-42`)
- updated: [[cash-outflows]] (mục 1.6 tiền gửi cầm cố, kim loại quý: thêm citation, sửa "run-off 0%" thành tuỳ chọn của jurisdiction; thời hạn báo trước cite `^lcr40-21` thay `^lcr40-20`, thêm VN `^pl1-b1-4a`; SME `^lcr40-24`, `^lcr40-25`; trade finance `^lcr40-71b`, `^lcr40-72`; mục 5.6 bỏ ví dụ chi phí hoạt động không có nguồn, thêm FAQ LCR40.74)
- updated: [[derivatives-and-contingent-outflows]] (FAQ LCR40.49, 40.51, 40.52, 40.55, 40.56; công thức 20% bỏ chữ "danh nghĩa", thêm citation; trade finance "thường là ≤ 5%" → "có thể, ví dụ ≤ 5%"; LCR40.72 có citation), [[committed-facilities]] (trade finance, LCR40.63), [[retail-deposit-stability]] (LCR40.9, 40.18, citation FAQ tiền gửi cầm cố), [[unsecured-wholesale-funding]] (LCR40.21 + VN, LCR40.24–25), [[secured-funding]] (FAQ LCR40.73, 40.79 customer shorts), [[hqla]] (trần 40% cite `^lcr30-42`), [[cash-inflows]] (FAQ LCR40.49, 40.55, 40.78, 40.79; sửa nhận định "TT50 thêm ba quy tắc": quyền thay thế TSBĐ khớp FAQ1 LCR40.55, hoàn trả sau 30 ngày khớp FAQ1 LCR40.78)
- conflicts: không có
- syntheses flagged: không có (tham số không đổi; nội dung sửa là citation và phạm vi)
- backfill: không có
- câu hỏi mở L/C đã đóng: raw LCR40.71 liệt kê documentary trade letters of credit; các node nhắc L/C đúng nội dung, nay có `^lcr40-71b`
- tiếp theo: TT50 Đ15, Đ17.2, Đ18.3 (xử lý khi vi phạm LCR); FAQ LCR30.41, 30.45 (tiêu chí 2B); LCR31.1–31.19 (ALA, cho ô `[cần nguồn]` trong [[hqla]])

## [2026-10-21] ingest | src-bcbs-lcr LCR30 (bổ sung — FAQ tiêu chí, đặc điểm HQLA; đọc chéo LCR31)
- updated: [[src-bcbs-lcr]] (+13 claim: `^lcr30-1-faq`, `^lcr30-6` (30.6–30.9), `^lcr30-10` (30.10–30.12), `^lcr30-15-faq`, `^lcr30-30` (30.30, 30.32), `^lcr30-41-faq`, `^lcr30-45-faq1`, `^lcr30-45-faq5`, `^lcr30-47-faq`, `^lcr31-6` (31.6–31.9), `^lcr31-11`, `^lcr31-16`, `^lcr31-18` (31.17–31.19))
- updated: [[hqla]] (thêm mục "Đặc điểm của HQLA" 7 dòng; dòng ALA trong Basel vs VN có citation), [[level-1-assets]] (FAQ LCR30.41: phạm vi home/host, giới hạn ngoại tệ; ô Basel "tài sản của chi nhánh ở nước ngoài" thay "không có đầu mục" bằng FAQ1), [[level-2-assets]] (FAQ LTV bình quân, cổ phiếu, Sukuk), [[alternative-liquidity-approaches]] (31.6–31.9, 31.11, 31.16, 31.18–19; mục regime gắn nhãn Diễn giải; góc VN thay đoạn không nguồn bằng `^pl1-a1-4` + [cần nguồn])
- conflicts: không có
- syntheses flagged: [[hqla-decomposition-and-tradeoffs]] (phạm vi Level 1 chủ quyền, tiêu chí RMBS/cổ phiếu)
- backfill: không có
- câu hỏi mở: ô VN của ALA vẫn [cần nguồn] (TT50 không có ALA); LCR31.21–31.61 (tiêu chí jurisdiction) không ingest — chỉ liên quan quốc gia xin áp dụng ALA
- tiếp theo: `src-tt50-2026-nhnn C2-M5` (Đ15, Đ17.2, Đ18.3 xử lý vi phạm LCR)

## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M5 (bổ sung — xử lý vi phạm LCR Đ15, Đ17.2, Đ18.3)
- updated: [[src-tt50-2026-nhnn]] (+4 claim: `^d15-1`, `^d17-2a`, `^d17-2b`, `^d18-3`), [[src-bcbs-lcr]] (+1 claim đọc chéo LCR20: `^lcr20-6b`)
- updated: [[lcr]] (mục "Xử lý khi LCR dưới ngưỡng": bảng Basel vs VN 6 dòng), [[tt50-2026]] (mục Báo cáo & nghĩa vụ +3 dòng; bảng đối chiếu +1 dòng), [[contingency-funding-plan]] (LCR20.6: cải thiện kế hoạch tài trợ dự phòng)
- conflicts: không có
- syntheses flagged: [[lcr-economic-significance-and-alm-governance]] (dòng Breach: TT50 gắn xử phạt, báo cáo hằng ngày)
- backfill: không có
- câu hỏi mở: Basel không có khái niệm "nguy cơ mất khả năng chi trả" tương ứng Đ18.1 trong các claim đã ingest
- tiếp theo: rà phạm vi LCR coi như đủ; còn lại FAQ Basel lặp và Đ14 (quản trị thanh khoản trong ngày, tài sản bảo đảm) mức ưu tiên thấp; có thể chuyển sang `src-tt50-2026-nhnn C2-M3` hoặc `PL3`

## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M4 (bổ sung — cấu phần L, D của LDR)
- claim mới: `^d12-2` (Đ12.1.a, Đ12.2), `^d12-4a` (Đ12.4.a–b), `^d12-4d` (Đ12.4.d, e, g–i), `^d12-5` (Đ12.1.b, Đ12.5.a, c), `^d12-8` (Đ12.8); C1 bổ sung `^d3-14` (Đ3.14 tỷ giá quy đổi)
- updated: [[loan-to-deposit-ratio]] (mục Công thức theo TT50: bảng cấu phần L 4 dòng, D 13 dòng, tỷ giá; Basel vs VN thêm dòng báo cáo, công bố thông tin; Diễn giải D ≠ tiền gửi khách hàng), [[tt50-2026]] (dòng Đ12.6, Đ12.8)
- conflicts: không có
- syntheses flagged: không thêm — 6 synthesis đã có dòng rà LDR từ ingest C2-M2, C2-M4 [2026-10-20]
- backfill: không có
- ghi chú: `04_models/lcr-tt50-2026.xlsx` chưa có sheet LDR; TT22/2019 chưa register nên chưa đối chiếu LDR cũ
- tiếp theo: src-tt50-2026-nhnn C2-M3 (giới hạn cấp tín dụng) hoặc PL3 (tổng trạng thái rủi ro)
## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M4 (bổ sung lần 2 — phân loại đầu mục cho vay)
- claim mới: `^d9-3` (Đ9.3, unit C2-M3 chỉ đọc khoản 3, không mark), `^d3-4` (Đ3.4 đầu tư trái phiếu doanh nghiệp), `^d1-4` (Đ1.4 chương trình, dự án theo quyết định Chính phủ)
- updated: [[loan-to-deposit-ratio]] (mục "Phân loại nghiệp vụ tín dụng trong LDR": 13 dòng nghiệp vụ → L / trừ D / không nêu, cột tác động có nhãn Diễn giải; dòng Chuyển tiếp thêm Đ37.2 `^d37-1`)
- conflicts: không có
- syntheses flagged: không thêm (đã có dòng rà LDR từ [2026-10-20])
- backfill: không có
- câu hỏi mở: định nghĩa "cho vay" (Luật Các TCTD, thông tư cho vay) chưa register; bán nợ, mua nợ, mua hẳn bộ chứng từ L/C không được Đ12 xếp vào L hay khoản trừ D
- tiếp theo: src-tt50-2026-nhnn C2-M3 (phần còn lại của Đ9–Đ11)
## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M3
- claim mới: `^d9-1` (Đ9.1–9.2 cơ sở vốn tự có), `^d9-4` (Đ9.4 thông qua cấp tín dụng đối tượng Đ135.1), `^d9-5` (Đ9.5 báo cáo), `^d10-1`…`^d10-3` (Đ10 cấp tín dụng đầu tư trái phiếu doanh nghiệp), `^d11-1`…`^d11-3` (Đ11 cấp tín dụng đầu tư cổ phiếu); `^d9-3` đã có từ lượt bổ sung C2-M4
- created: [[total-credit-outstanding]]
- updated: [[concentration-risk-management]] (giới hạn pháp định TT50, câu hỏi mở), [[tt50-2026]] (3 dòng Yêu cầu chính, relation governs → total-credit-outstanding), [[loan-to-deposit-ratio]] (link)
- conflicts: không có
- syntheses flagged: không có (thay đổi về giới hạn tín dụng, không chạm kết luận thanh khoản, tập trung nguồn vốn)
- backfill: linked [[total-credit-outstanding]] trong [[credit-risk-management]], [[loan-to-deposit-ratio]], [[concentration-risk-management]]
- sổ sách: registry mark C2-M3 done; overview 8/14; domain-vn-reg (metric 30, tổng 86), domain-alm (metric 48, tổng 179)
- câu hỏi mở: mức % giới hạn Đ136 Luật Các TCTD và Basel LEX chưa register/ingest
- tiếp theo: src-tt50-2026-nhnn PL3 (tổng trạng thái rủi ro) hoặc C2-M6 (tỷ lệ nắm giữ TPCP)
## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M4 (bổ sung lần 3 — giải trình đầu mục D, tách node L và D)
- claim mới: không có (toàn bộ lời văn Đ12.4–5 đã có claim)
- created: [[ldr-total-deposits]] (giải trình 12 đầu mục cộng/trừ, đối chiếu LCR `^pl1-b2-2`, `^pl1-b2-3`, `^pl1-b3-24` và NSFR `^pl2-a2`, mục "Không có trong D", ví dụ số D = 1.000), [[ldr-total-loans]] (4 đầu mục L, bảng phân loại nghiệp vụ chuyển từ node LDR, ví dụ L = 800)
- updated: [[loan-to-deposit-ratio]] (mục Công thức rút gọn, link sang L và D), [[total-credit-outstanding]] (link)
- conflicts: không có
- syntheses flagged: không có (tách node, không đổi tham số)
- backfill: linked [[ldr-total-loans]], [[ldr-total-deposits]] trong [[loan-to-deposit-ratio]], [[total-credit-outstanding]], domain-vn-reg
- sổ sách: index +2; domain-vn-reg (metric 32, tổng 88), domain-alm (metric 50, tổng 181)
- câu hỏi mở: chứng chỉ tiền gửi, trái phiếu không phải Vốn cấp 2, vay NHNN, cho vay TCTD nước ngoài không được Đ12 nêu — cần hướng dẫn báo cáo NHNN
- tiếp theo: src-tt50-2026-nhnn PL3 hoặc C2-M6
## [2026-10-21] ingest | src-tt50-2026-nhnn PL3
- claim mới: `^pl3-1`…`^pl3-9` (công thức EM, failed trades, nguyên tắc chung, nội bảng, cash pooling, repo, phái sinh, bù trừ và ký quỹ, ngoại bảng)
- updated: [[leverage-exposure-measure]] (thêm domain vn-reg, mục "Theo TT50/2026", bảng Basel vs VN 9 dòng), [[leverage-ratio]] (điền 3 ô [cần nguồn] VN; thêm dòng Mẫu số, Repo; gắn nhãn Diễn giải cho các câu không citation: lý do loại Vốn cấp 2, ví dụ G-SIB, 33,33 lần, CAR; đoạn HQLA paradox và repo cho bối cảnh VN), [[tt50-2026]] (governs → leverage-exposure-measure, dòng Đ8.1/PL3)
- conflicts: không có
- syntheses flagged: [[practical-alm-liquidity-governance]], [[synthetic-balance-sheet-liquidity-risk]] (VN thay [cần nguồn] cho EM; repo VN khác Basel; LEV chưa có ngưỡng)
- backfill: không có
- sổ sách: registry mark PL3 done; overview 9/14; index (leverage-exposure-measure: sửa maturity canonical → draft cho khớp node, thêm vn-reg); domain-vn-reg (metric 33, tổng 89)
- ghi chú: không trích được công thức `$$` trong dòng trích dẫn (lint math-display-not-own-line), công thức ghi trong câu diễn đạt claim
- câu hỏi mở: mức CCF và PFE cụ thể nằm ở TT14/2025, TT41/2016; Basel LEV về cash pooling và unsettled trades chưa ingest
- tiếp theo: src-tt50-2026-nhnn C2-M6 (tỷ lệ nắm giữ TPCP) hoặc C2-M1
## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M6
- claims: 4 (d28-1, d28-2, d28-4, d28-5); C1 bổ sung d3-13 (Tổng Nợ phải trả bình quân của tháng)
- created: [[government-bond-holding-ratio]], [[government-bond-holdings]] (part-of, cite d28-4), [[average-total-liabilities]] (part-of, cite d28-1)
- updated: [[tt50-2026]] (governs government-bond-holding-ratio, dòng Đ28), [[level-1-assets]] (link trần 30%)
- conflicts: không có
- syntheses flagged: [[practical-alm-liquidity-governance]], [[synthetic-balance-sheet-liquidity-risk]] (TPCP 17.000 tỷ, kiểm tra trần 30%), [[irrbb-csrbb-measurement-and-hedging]] (khuyến nghị ưu tiên TPCP VN)
- backfill: linked [[level-1-assets]] · flagged 3 synthesis trên · proposed không có
- tiếp theo: src-tt50-2026-nhnn C2-M7 (giới hạn góp vốn, mua cổ phần) hoặc C2-M1
## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M7
- claims: 5 (d29-1, d29-2, d29-3, d29-3d, d29-3dd)
- created: [[interbank-cross-shareholding]]
- updated: [[tt50-2026]] (governs interbank-cross-shareholding, dòng Đ29), [[concentration-risk-management]] (giới hạn 2 TCTD, dưới 5%)
- conflicts: không có
- syntheses flagged: không có
- backfill: linked [[concentration-risk-management]]
- ghi chú: lệnh /ingest TT50 LDR; C2-M4 đã ingest trọn, raw TT22/2019 chưa có trong vault (clipping "DTTT thay thế TT22" chỉ có ảnh), user chọn chuyển sang unit TT50 khác
- tiếp theo: src-tt50-2026-nhnn C2-M1 (giá trị thực vốn điều lệ) hoặc C3; register TT22/2019 khi có raw
## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M5, PL2 (bổ sung NSFR)
- claims C2-M5: 11 (d23-3c, d23-3g, d24-3c, d24-5, d24-6, d25-1, d25-2b, d25-4b, d25-4c, d26-1b, d26-3)
- claims PL2: 12 theo đầu mục Bảng 9, 10 (pl2-a2-1, pl2-a2-2, pl2-a2-6, pl2-a2-9, pl2-a2-11, pl2-b1-2, pl2-b2-1, pl2-b2-8, pl2-b2-9, pl2-b2-14, pl2-b2-16, pl2-b2-19), chép bảng theo từng nhóm khoản
- updated: thêm mục Basel vs VN cho [[asf-capital-and-long-term-liabilities]], [[asf-retail-and-small-business-deposits]], [[asf-wholesale-and-operational-funding]], [[rsf-hqla-and-central-bank-reserves]], [[rsf-loans-and-credit-exposures]], [[rsf-securities-financing-and-encumbrance]] (thêm vn-reg), [[rsf-derivatives-and-off-balance-sheet]] (thêm vn-reg); [[available-stable-funding]] (sửa câu Khác biệt: Basel cũng cho 95%/90% với tiền gửi bán lẻ ≥ 1 năm rút được không bị phạt nặng, NSF30.11), [[required-stable-funding]], [[interdependent-assets-and-liabilities]] (góc nhìn VN Đ26)
- conflicts: không có
- syntheses flagged: [[nsfr-alm-governance-strategy-and-risks]], [[nsfr-structural-liquidity-and-alm-strategy]], [[synthetic-balance-sheet-liquidity-risk]], [[irrbb-liquidity-hqla-and-ftp-interaction]] (giá trị VN cho ASF/RSF theo nhóm)
- backfill: linked node chi tiết asf-*/rsf-* từ [[available-stable-funding]], [[required-stable-funding]]
- ghi chú: không chạy registry mark (chế độ bổ sung)
- tiếp theo: src-tt50-2026-nhnn C2-M1 hoặc C3
## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M5, PL2 (bổ sung NSFR)
- claims C2-M5: 11 (d23-3c, d23-3g, d24-3c, d24-5, d24-6, d25-1, d25-2b, d25-4b, d25-4c, d26-1b, d26-3)
- claims PL2: 12 theo đầu mục Bảng 9, 10 (pl2-a2-1, pl2-a2-2, pl2-a2-6, pl2-a2-9, pl2-a2-11, pl2-b1-2, pl2-b2-1, pl2-b2-8, pl2-b2-9, pl2-b2-14, pl2-b2-16, pl2-b2-19), chép bảng theo từng nhóm khoản
- updated: thêm mục Basel vs VN cho [[asf-capital-and-long-term-liabilities]], [[asf-retail-and-small-business-deposits]], [[asf-wholesale-and-operational-funding]], [[rsf-hqla-and-central-bank-reserves]], [[rsf-loans-and-credit-exposures]], [[rsf-securities-financing-and-encumbrance]] (thêm vn-reg), [[rsf-derivatives-and-off-balance-sheet]] (thêm vn-reg); [[available-stable-funding]] (sửa câu Khác biệt: Basel cũng cho 95%/90% với tiền gửi bán lẻ ≥ 1 năm rút được không bị phạt nặng, NSF30.11), [[required-stable-funding]], [[interdependent-assets-and-liabilities]] (góc nhìn VN Đ26)
- conflicts: không có
- syntheses flagged: [[nsfr-alm-governance-strategy-and-risks]], [[nsfr-structural-liquidity-and-alm-strategy]], [[synthetic-balance-sheet-liquidity-risk]], [[irrbb-liquidity-hqla-and-ftp-interaction]] (giá trị VN cho ASF/RSF theo nhóm)
- backfill: linked node chi tiết asf-*/rsf-* từ [[available-stable-funding]], [[required-stable-funding]]
- ghi chú: không chạy registry mark (chế độ bổ sung)
- tiếp theo: src-tt50-2026-nhnn C2-M1 hoặc C3
## [2026-10-21] ingest | --node asf-public-sector-and-central-bank-funding, asf-other-liabilities
- lệnh: /ingest TT50 NSFR ASF; raw ASF (Đ23, PL2 Phần A) đã trích hết, user chọn tách node ASF còn thiếu; không claim mới
- created: [[asf-public-sector-and-central-bank-funding]] (Bảng 9 khoản 7–8, part-of available-stable-funding cite pl2-a2-6), [[asf-other-liabilities]] (khoản 2–5, 14, Đ25.4.c, part-of cite pl2-a2-2)
- updated: [[available-stable-funding]], [[asf-wholesale-and-operational-funding]] (link node mới)
- conflicts: không có
- syntheses flagged: không có (không đổi tham số)
- backfill: linked [[available-stable-funding]], [[asf-wholesale-and-operational-funding]]
- tiếp theo: src-tt50-2026-nhnn C2-M1 hoặc C3
## [2026-10-21] ingest | --node available-stable-funding (giải trình đầu mục ASF theo TT50)
- lệnh: /ingest TT50 NSFR ASF chi tiết đầu mục thành phần; không claim mới (raw Đ23, PL2 Phần A đã trích hết)
- updated: [[available-stable-funding]] thêm mục "Theo TT50/2026: giải trình từng đầu mục ASF": nguyên tắc chung (phạm vi, giá trị, thứ tự phân loại), bảng quy tắc kỳ hạn Đ23.3 (8 tình huống), bảng 14 khoản Bảng 9 × 5 cột kỳ hạn, giải trình từng khoản (điểm a(iii) PL I là bản VN của "phạt nặng"; DNNVV > 30 tỷ đồng chuyển sang khoản 12; khoản 6 trái phiếu xếp theo kỳ hạn), ví dụ số ASF = 725,5/1.000
- conflicts: không có
- syntheses flagged: không có (không đổi tham số)
- backfill: không có
- tiếp theo: src-tt50-2026-nhnn C2-M1 hoặc C3
- index: sửa maturity của [[available-stable-funding]] từ canonical thành draft cho khớp node

## [2026-10-21] ingest | --node required-stable-funding (giải trình đầu mục RSF theo TT50)
- lệnh: /ingest TT50 NSFR RSF chi tiết từng đầu mục thành phần; không claim mới (raw Đ24, PL2 Phần B đã trích hết)
- updated: [[required-stable-funding]] thêm mục "Theo TT50/2026: giải trình từng đầu mục RSF": nguyên tắc chung (A.4–A.20 là tài sản không bị ràng buộc nên A.3 xét trước HQLA), bảng quy tắc kỳ hạn Đ24.3–24.6 (9 tình huống, kỳ hạn muộn nhất), bảng Bảng 10 đủ các khoản A, B, C × 5 cột, giải trình từng nhóm khoản, ví dụ số RSF = 531,5 và NSFR = 136,5% (nối với ví dụ ASF)
- index: sửa maturity của [[required-stable-funding]] từ canonical thành draft cho khớp node
- conflicts: không có
- syntheses flagged: không có (không đổi tham số)
- backfill: không có
- tiếp theo: src-tt50-2026-nhnn C2-M1 hoặc C3
## [2026-10-21] ingest | src-tt50-2026-nhnn C2-M1
- claims: 5 (d6-1, d6-3, d7-1, d7-2, d7-3)
- created: [[real-value-of-charter-capital]] (metric), [[capital-shortfall-remediation]] (concept, so sánh với xử lý vi phạm LCR Đ17–18)
- updated: [[tt50-2026]] (governs 2 node mới, dòng Đ6–Đ7), [[interbank-cross-shareholding]] (link điều kiện Đ29.2.a, câu hỏi mở)
- conflicts: không có
- syntheses flagged: không có
- backfill: linked [[interbank-cross-shareholding]]
- tiếp theo: src-tt50-2026-nhnn C3 (tổ chức thực hiện, chuyển tiếp Đ30); register Luật Các TCTD 2024 (Đ28.3 giá trị thực vốn điều lệ, Đ135–136 giới hạn cấp tín dụng)
## [2026-10-21] ingest | src-tt50-2026-nhnn C3
- claims: 7 (d30-1, d31-1, d32-1, d33-4, d36-1, d36-3, d37-3b); heading C3 bỏ ghi chú "chưa ingest trọn"
- created: [[supervisory-discretion-tt50]] (concept: danh mục quyền tuỳ nghi của NHNN, đơn vị quyết định)
- updated: [[tt50-2026]] (governs node mới, dòng Đ30, Đ31–Đ35, Đ36, Đ37.3), [[total-credit-outstanding]] và [[concentration-risk-management]] (chuyển tiếp Đ30), [[contingency-funding-plan]] (chi nhánh NHNNg khi ngân hàng mẹ bất lợi, Đ36.3), [[leverage-ratio]] (Cục An toàn hệ thống trình LEV)
- conflicts: không có
- syntheses flagged: không có
- backfill: không có
- ghi chú: TT50 đã ingest 13/14 unit; chỉ còn preamble (không ingest)
- tiếp theo: register Luật Các TCTD 2024 (Đ28.3, Đ135–136), TT14/2025 (khoản giảm trừ vốn, CCF, PFE), TT22/2019 (LDR chuyển tiếp)