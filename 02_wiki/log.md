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
