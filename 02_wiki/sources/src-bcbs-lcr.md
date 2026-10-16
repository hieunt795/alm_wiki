---
title: "BCBS — LCR Liquidity Coverage Ratio (Basel Framework)"
aliases: []
type: source
source_id: src-bcbs-lcr
domains: [basel, alm]
status: active
maturity: draft
tier: T2
doc_status: final
issuer: BCBS
published: 2025-12-17
effective: 2019-12-15
raw: 01_sources/alm/Basel/LCR/LCR.md
units_done: [preamble, LCR10, LCR20, LCR30, LCR31, LCR40, LCR90, LCR99]
updated: 2026-10-15
---

## Thông tin nguồn
- Issuer: Basel Committee on Banking Supervision ([[bcbs]])
- Tier T2, `doc_status: final`. Bản consolidated do BIS website sinh ngày 17/12/2025.
- Version effective: LCR10, LCR20, LCR30, LCR31, LCR40, LCR90 và LCR99 đều ghi *"Version effective as of 15 Dec 2019"*. LCR40 có FAQ bổ sung ngày 30/03/2023.
- Raw: `01_sources/alm/Basel/LCR/LCR.md` (1.421 dòng); meta: `LCR_meta.json`. Không có pdf gốc.
- Conversion: ok (xem `03_meta/sources.yaml`).
- Node regulation tương ứng: [[bcbs-lcr]].

## Tóm tắt
Chuẩn mực LCR yêu cầu ngân hàng giữ đủ HQLA không bị cầm cố để vượt qua kịch bản stress 30 ngày, kết hợp cú sốc riêng của ngân hàng (idiosyncratic) và cú sốc toàn thị trường.
- **LCR10** quy định phạm vi áp dụng trên cơ sở hợp nhất cho các ngân hàng hoạt động quốc tế; nguyên tắc xử lý khác biệt giữa Home và Host (tiền gửi bán lẻ/SME áp dụng theo Host); quy tắc loại trừ thặng dư HQLA không thể chuyển giao do rào cản pháp lý (ring-fencing); và yêu cầu quản lý thanh khoản theo từng đồng tiền trọng yếu.
- **LCR20** nêu mục tiêu, kịch bản stress, cấu trúc hai thành phần (HQLA / total net cash outflows), ngưỡng ≥ 100% và nghĩa vụ báo cáo.
- **LCR30** quy định về tài sản có tính thanh khoản cao (HQLA) — tử số của LCR: các đặc tính cốt lõi, yêu cầu vận hành (unencumbered, quyền kiểm soát của Treasury, periodic monetisation), phân loại Level 1 (không giới hạn, 0% haircut), Level 2A (haircut 15%), Level 2B (haircut 25–50%), cùng công thức trần 40% Level 2 và 15% Level 2B sau khi unwind giao dịch ngắn hạn ≤ 30 ngày.
- **LCR31** quy định các phương pháp thanh khoản thay thế (Alternative Liquidity Approaches - ALA) cho các quốc gia có sự thiếu hụt mang tính cơ cấu về tài sản Level 1 (hoặc cả Level 1 và 2) bằng đồng nội tệ so với nhu cầu của toàn hệ thống ngân hàng. Ba lựa chọn gồm: Option 1 (hạn mức cam kết thanh khoản có phí từ NHTW - CLF), Option 2 (HQLA bằng ngoại tệ bù đắp dòng tiền ra nội tệ kèm FX haircut tối thiểu 8%), Option 3 (sử dụng thêm tài sản Level 2A vượt trần 40% kèm haircut tối thiểu 20%). Áp dụng có trần tối đa (ví dụ 80%), yêu cầu đánh giá lại định kỳ tối đa 5 năm và chịu giám sát bình duyệt độc lập.
- **LCR40** quy định chi tiết cách tính dòng tiền ra và vào trong 30 ngày: run-off rate theo loại nguồn vốn (bán lẻ, SME, operational, wholesale, secured), tỷ lệ rút vốn của committed facilities, các nhu cầu thanh khoản phát sinh (derivatives, downgrade, collateral), tỷ lệ dòng vào theo đối tác, và mức trần dòng vào 75%.
- **LCR90** quy định lộ trình áp dụng chuẩn mực LCR 100% có hiệu lực từ 01/01/2019; cho phép ngoại lệ kéo dài lộ trình đối với các quốc gia đang thực hiện chương trình cải cách vĩ mô và cơ cấu kinh tế.
- **LCR99** bảng hướng dẫn ứng dụng tổng hợp toàn diện mọi hệ số HQLA, tỷ lệ dòng tiền ra, tỷ lệ dòng tiền vào và công thức xác định dòng tiền ra ròng kèm trần bù trừ 75%.

Nhiều tham số là **mức sàn tối thiểu**; jurisdiction được nâng cao hơn hoặc tự quyết định (national discretion). Đây là điểm mấu chốt khi đối chiếu với quy định VN.

## Key claims

### Preamble

- LCR mô tả chuẩn mực tỷ lệ đảm bảo khả năng thanh khoản nhằm thúc đẩy tính chống chịu ngắn hạn đối với hồ sơ rủi ro thanh khoản của ngân hàng.
  > "This standard describes the Liquidity Coverage Ratio, a measure which promotes the short-term resilience of a bank's liquidity risk profile."
  > — preamble ^lcr-preamble

### LCR10 — Definitions and application

#### Phạm vi áp dụng và các khoản đầu tư trọng yếu

- LCR và các công cụ giám sát thanh khoản áp dụng trên cơ sở hợp nhất cho tất cả các ngân hàng hoạt động quốc tế; cơ quan giám sát có thể mở rộng áp dụng cho các ngân hàng khác hoặc các phân nhóm thực thể để đảm bảo tính nhất quán và bình đẳng cạnh tranh.
  > "The LCR standard and monitoring tools should be applied to all internationally active banks on a consolidated basis, but may be used for other banks and on any subset of entities of internationally active banks as well to ensure greater consistency and a level playing field between domestic and cross-border banks."
  > — LCR10.1 ^lcr10-1

- Các khoản đầu tư không hợp nhất vào các thực thể ngân hàng, chứng khoán hoặc tài chính mà tập đoàn là bên cung ứng thanh khoản chính khi stress (hoặc hỗ trợ vì rủi ro uy tín) phải được xác định phương pháp lượng hóa dòng tiền rút tiềm tàng và xếp vào mục nghĩa vụ tài trợ tiềm tàng khác (LCR40.70).
  > "Normally, a non-controlling investment (eg a joint venture or minority-owned entity) can be regarded as significant if the banking group will be the main liquidity provider of such investment in times of stress"
  > "those arising from the need to support the investment in times of stress out of reputational concerns for the purpose of calculating the LCR. To the extent that such liquidity draws are not included elsewhere, they should be treated under "Other contingent funding obligations", as described in LCR40.70."
  > — LCR10.2 ^lcr10-2

- Dù phạm vi áp dụng LCR thế nào, ngân hàng phải chủ động giám sát và kiểm soát rủi ro thanh khoản ở cấp độ từng pháp nhân độc lập, chi nhánh nước ngoài, công ty con và toàn tập đoàn, có tính đến các rào cản chuyển giao thanh khoản.
  > "a bank should actively monitor and control liquidity risk exposures and funding needs at the level of individual legal entities, foreign branches and subsidiaries, and the group as a whole, taking into account legal, regulatory and operational limitations to the transferability of liquidity."
  > — LCR10.3 ^lcr10-3

#### Nguyên tắc Home vs Host

- Khi tính LCR hợp nhất, tập đoàn ngân hàng xuyên biên giới áp dụng các tham số thanh khoản của Home jurisdiction cho mọi thực thể hợp nhất, ngoại trừ tiền gửi bán lẻ / doanh nghiệp nhỏ (retail / small business deposits) thì phải tuân theo tham số của Host jurisdiction nơi thực thể (chi nhánh hoặc công ty con) hoạt động.
  > "When calculating the LCR on a consolidated basis, a cross-border banking group should apply the liquidity parameters adopted in the home jurisdiction to all legal entities being consolidated except for the treatment of retail / small business deposits that should follow the relevant parameters adopted in host jurisdictions in which the entities (branch or subsidiary) operate."
  > — LCR10.5 ^lcr10-5

- Tham số của Home jurisdiction vẫn được áp dụng cho tiền gửi bán lẻ/SME tại Host jurisdiction nếu: (1) Host không có quy định, (2) Host chưa triển khai LCR, hoặc (3) Home supervisor quyết định áp dụng tiêu chuẩn của Home khắt khe hơn Host.
  > "Home requirements for retail and small business deposits should apply to the relevant legal entities (including branches of those entities) operating in host jurisdictions if: … there are no host requirements for retail and small business deposits in the particular jurisdictions … those entities operate in host jurisdictions that have not implemented the LCR … the home supervisor decides that home requirements should be used that are stricter than the host requirements."
  > — LCR10.6 ^lcr10-6

#### Hạn chế chuyển giao thanh khoản (Ring-fencing)

- Nguyên tắc chung: không được ghi nhận thanh khoản thặng dư trong LCR hợp nhất nếu có nghi ngờ hợp lý về khả năng sẵn sàng chuyển giao (do ring-fencing, không chuyển đổi được đồng tiền, kiểm soát ngoại hối).
  > "as a general principle, no excess liquidity should be recognised by a cross-border banking group in its consolidated LCR if there is reasonable doubt about the availability of such liquidity."
  > "Liquidity transfer restrictions (eg ring-fencing measures, nonconvertibility of local currency, foreign exchange controls) in jurisdictions in which a banking group operates will affect the availability of liquidity by inhibiting the transfer of high-quality liquid assets (HQLA) and fund flows within the group."
  > "the eligible HQLA that are held by a legal entity being consolidated to meet its local LCR requirements (where applicable) can be included in the consolidated LCR to the extent that such HQLA are used to cover the total net cash outflows of that entity"
  > "If the HQLA held in excess of the total net cash outflows are not transferable, such surplus liquidity should be excluded from the LCR calculation."
  > — LCR10.7 ^lcr10-7

- Các hạn chế chuyển giao thanh khoản đưa vào LCR hợp nhất giới hạn ở các hạn chế hiện hành theo luật, quy định và yêu cầu giám sát; ngân hàng phải có quy trình theo dõi và đánh giá tác động thanh khoản toàn tập đoàn.
  > "the liquidity transfer restrictions to be accounted for in the consolidated ratio are confined to existing restrictions imposed under applicable laws, regulations and supervisory requirements"
  > — LCR10.8 ^lcr10-8

#### Quản lý theo đồng tiền

- LCR hợp nhất được báo cáo bằng một đồng tiền chung, nhưng ngân hàng và cơ quan giám sát phải theo dõi nhu cầu thanh khoản theo từng đồng tiền trọng yếu; cơ cấu đồng tiền của HQLA phải tương thích với nhu cầu hoạt động; không được giả định các đồng tiền sẽ duy trì khả năng chuyển giao và chuyển đổi trong stress.
  > "while the LCR must be met on a consolidated basis and reported in a common currency, supervisors and banks should also be aware of the liquidity needs in each significant currency."
  > "the currencies of the stock of HQLA should be similar in composition to the operational needs of the bank. Banks and supervisors cannot assume that currencies will remain transferable and convertible in a stress period"
  > — LCR10.9 ^lcr10-9

### LCR20 — Calculation

- Mục tiêu của LCR: đủ HQLA để vượt qua stress đáng kể kéo dài 30 ngày.
  > "The Committee has developed the Liquidity Coverage Ratio (LCR) to promote the short-term resilience of the liquidity risk profile of banks by ensuring that they have sufficient high-quality liquid assets (HQLA) to survive a significant stress scenario lasting 30 calendar days."
  > — LCR20.1 ^lcr20-1

- Kịch bản stress kết hợp cú sốc idiosyncratic và market-wide, gồm 7 yếu tố: rút tiền gửi bán lẻ, mất một phần wholesale funding không đảm bảo, mất secured funding ngắn hạn, hạ bậc tín nhiệm tới 3 notch, biến động thị trường, rút hạn mức cam kết, mua lại nợ hoặc nghĩa vụ ngoài hợp đồng vì rủi ro uy tín.
  > "The scenario for this standard entails a combined idiosyncratic and market-wide shock that would result in:"
  > — LCR20.2 ^lcr20-2

- Stress test của LCR chỉ là yêu cầu tối thiểu; ngân hàng phải tự stress test với horizon dài hơn.
  > "This stress test should be viewed as a minimum supervisory requirement for banks."
  > — LCR20.3 ^lcr20-3

- LCR có hai thành phần: giá trị HQLA trong điều kiện stress và total net cash outflows.
  > "The LCR has two components: (1) value of the stock of HQLA in stressed conditions; and (2) total net cash outflows"
  > — LCR20.4 ^lcr20-4

- Ngưỡng ≥ 100% khi không có stress. Trong stress, ngân hàng được dùng HQLA và xuống dưới mức tối thiểu.
  > "the value of the ratio be no lower than 100% (ie the stock of HQLA should at least equal total net cash outflows) on an ongoing basis"
  > "During periods of stress, however, it would be entirely appropriate for banks to use their stock of HQLA, thereby falling below the minimum."
  > — LCR20.5 ^lcr20-5

- Supervisor phải phản ứng có phân biệt và tương xứng khi LCR < 100%.
  > "Supervisors should allow for differentiated responses to a reported LCR below 100%."
  > — LCR20.6 ^lcr20-6

- Báo cáo ít nhất hàng tháng, độ trễ lý tưởng không quá 2 tuần.
  > "The LCR must be reported to supervisors at least monthly, with the operational capacity to increase the frequency to weekly or even daily in stressed situations"
  > "ideally should not surpass two weeks"
  > — LCR20.7 ^lcr20-7

- Phải thông báo ngay cho supervisor khi LCR đã hoặc dự kiến xuống dưới 100%.
  > "Banks must also notify supervisors immediately if their LCR has fallen, or is expected to fall, below 100%."
  > — LCR20.8 ^lcr20-8

### LCR30 — High-quality liquid assets

#### Định nghĩa và nguyên tắc chung

- HQLA là tử số của LCR. Ngân hàng phải nắm giữ lượng HQLA không bị cầm cố để bù đắp tổng dòng tiền ra ròng trong 30 ngày stress.
  > "The numerator of the Liquidity Coverage Ratio (LCR) is the "stock of high-quality liquid assets (HQLA)"."
  > "banks must hold a stock of unencumbered HQLA to cover the total net cash outflows … over a 30-day period under the stress scenario prescribed in LCR20."
  > — LCR30.1 ^lcr30-1

- Tài sản được coi là HQLA nếu có thể chuyển đổi dễ dàng và ngay lập tức thành tiền mặt mà ít hoặc không bị mất giá. Năng lực tạo thanh khoản qua bán hoặc repo được giả định duy trì ngay cả trong stress nghiêm trọng.
  > "Assets are considered to be HQLA if they can be easily and immediately converted into cash at little or no loss of value."
  > "the test of whether liquid assets are of "high quality" is that, by way of sale or repo, their liquidity-generating capacity is assumed to remain intact even in periods of severe idiosyncratic and market stress."
  > — LCR30.2, LCR30.3 ^lcr30-2

- HQLA (trừ Level 2B) lý tưởng nên đủ điều kiện làm tài sản bảo đảm tại NHTW cho nhu cầu thanh khoản trong ngày và qua đêm; tuy nhiên điều này không tự nó quyết định tài sản là HQLA.
  > "HQLA (except Level 2B assets as defined below in LCR30.44 to LCR30.46) should ideally be eligible at central banks for intraday liquidity needs and overnight liquidity facilities."
  > "central bank eligibility does not by itself constitute the basis for the categorisation of an asset as HQLA."
  > — LCR30.4, LCR30.5 ^lcr30-4

#### Yêu cầu vận hành (Operational requirements)

- Ngân hàng phải định kỳ thanh khoản hóa (monetise) một tỷ lệ đại diện tài sản trong danh mục qua repo hoặc bán đứt để kiểm tra khả năng tiếp cận thị trường và giảm rủi ro phát tín hiệu tiêu cực khi stress.
  > "A bank must periodically monetise a representative proportion of the assets in the stock through repo or outright sale, in order to test its access to the market, the effectiveness of its processes for monetisation, the availability of the assets, and to minimise the risk of negative signalling during a period of actual stress."
  > — LCR30.15 ^lcr30-15

- Mọi tài sản HQLA phải "unencumbered" — không có hạn chế pháp lý, quy định hoặc hợp đồng đối với việc thanh lý, bán, chuyển nhượng. Không được cầm cố để bảo đảm giao dịch hoặc phục vụ chi phí hoạt động.
  > "All assets in the stock must be unencumbered. "Unencumbered" means free of legal, regulatory, contractual or other restrictions on the ability of the bank to liquidate, sell, transfer or assign the asset."
  > "An asset in the stock must not be pledged (either explicitly or implicitly) to secure, collateralise or credit-enhance any transaction, nor be designated to cover operational costs (such as rents and salaries)."
  > — LCR30.16 ^lcr30-16

- Danh mục HQLA phải chịu sự kiểm soát liên tục của bộ phận quản lý thanh khoản (ví dụ Treasurer) với đầy đủ thẩm quyền, năng lực pháp lý và vận hành để thanh khoản hóa bất kỳ tài sản nào tại bất kỳ thời điểm nào trong 30 ngày.
  > "The stock must be under the control of the function charged with managing the liquidity of the bank (eg the treasurer), meaning the function has the continuous authority, and legal and operational capability, to monetise any asset in the stock."
  > — LCR30.18 ^lcr30-18

- Tài sản nhận theo quyền tái thế chấp (rehypothecation) mà chủ sở hữu hưởng lợi có quyền rút trong 30 ngày stress không được tính vào HQLA. Tài sản nhận làm bảo đảm cho phái sinh không bị phong tỏa và được phép tái thế chấp hợp pháp có thể tính vào HQLA nếu ghi nhận dòng tiền ra tương ứng.
  > "Banks must not include in the stock of HQLA any assets, or liquidity generated from assets, they have received under right of rehypothecation, if the beneficial owner has the contractual right to withdraw those assets during the 30-day stress period."
  > "Assets received as collateral for derivatives transactions that are not segregated and are legally able to be rehypothecated may be included in the stock of HQLA provided that the bank records an appropriate outflow for the associated risks"
  > — LCR30.24, LCR30.25 ^lcr30-24

- Ngân hàng phải duy trì HQLA phù hợp với cơ cấu nhu cầu thanh khoản theo từng loại tiền tệ. Thặng dư HQLA tại pháp nhân con chỉ được tính vào mức hợp nhất nếu sẵn sàng chuyển giao cho công ty mẹ khi stress.
  > "banks should be able to meet their liquidity needs in each currency and maintain HQLA consistent with the distribution of their liquidity needs by currency."
  > "Any surplus of HQLA held at the legal entity can only be included in the consolidated stock if those assets would also be freely available to the consolidated (parent) entity in times of stress."
  > — LCR30.27, LCR30.21 ^lcr30-27

- Khi tài sản đủ điều kiện bị mất chuẩn (ví dụ bị hạ rating), ngân hàng được phép giữ tài sản đó trong danh mục thêm 30 ngày để kịp thời điều chỉnh hoặc thay thế (mitigate cliff effect).
  > "if an eligible liquid asset became ineligible (eg due to rating downgrade), a bank is permitted to keep such assets in its stock of liquid assets for an additional 30 calendar days."
  > — LCR30.28 ^lcr30-28

#### Cấu phần HQLA, Haircuts và Caps

- Danh mục gồm hai cấp tài sản: Level 1 được tính không giới hạn; Level 2 chỉ được chiếm tối đa 40% tổng danh mục HQLA (sau haircut). Level 2B (nếu được supervisor cho phép) tối đa 15% tổng HQLA (và nằm trong trần 40% của Level 2).
  > ""Level 1" assets can be included without limit, while "Level 2" assets can only comprise up to 40% of the stock."
  > "Supervisors may also choose to include within Level 2 an additional class of assets (Level 2B assets). If included, these assets must not comprise more than 15% of the total stock of HQLA. They must also be included within the overall 40% cap on Level 2 assets."
  > — LCR30.31, LCR30.33 ^lcr30-31

- Trần 40% Level 2 và 15% Level 2B được tính sau khi áp dụng haircut và sau khi tính đến việc unwind các giao dịch repo, cho vay chứng khoán và hoán đổi tài sản bảo đảm đáo hạn trong 30 ngày có trao đổi HQLA. Mức trần điều chỉnh Level 2 tối đa bằng 2/3 Level 1 điều chỉnh; trần Level 2B điều chỉnh bằng 15/85 tổng Level 1 và 2A điều chỉnh, hoặc tối đa 1/4 Level 1 điều chỉnh nếu trần 40% bị chạm.
  > "The 40% cap on Level 2 assets and the 15% cap on Level 2B assets must be determined after the application of required haircuts, and after taking into account the unwind of short-term securities financing transactions and collateral swap transactions maturing within 30 calendar days that involve the exchange of HQLA."
  > "The maximum amount of adjusted Level 2 assets is equal to two-thirds of the adjusted amount of Level 1 assets after haircuts have been applied."
  > "The maximum amount of adjusted Level 2B assets is equal to the ratio of 15/85 times the sum of the adjusted amounts of Level 1 and Level 2A assets, or, in cases where the 40% cap is binding, up to a maximum of 1/4 times the adjusted amount of Level 1 assets, both after haircuts have been applied."
  > — LCR30.34, LCR30.35, LCR30.36 ^lcr30-34

- Số dư điều chỉnh (adjusted amount) của Level 1, Level 2A và Level 2B là giá trị có được sau khi hoàn trả (unwind) các giao dịch tài trợ có bảo đảm, cho vay có bảo đảm và hoán đổi tài sản bảo đảm ngắn hạn (đáo hạn ≤ 30 ngày). Trường hợp tài sản bảo đảm nhận được từ cho vay/swap bị đem tái thế chấp (rehypothecated) trong một giao dịch tài trợ ngắn hạn khác, cả hai giao dịch đều phải được unwind đồng thời. Tổng HQLA = Level 1 + Level 2A + Level 2B − Adjustment 15% − Adjustment 40%.
  > "The adjusted amount of Level 1 assets is defined as the amount of Level 1 assets that would result after unwinding those short-term secured funding, secured lending and collateral swap transactions involving the exchange of any HQLA for any Level 1 assets (including cash) that meet, or would meet if held unencumbered, the operational requirements for HQLA"
  > "In cases where collateral received in a short-term secured lending or collateral swap transaction would meet the operational requirements if held unencumbered, but has been rehypothecated in a short-term secured funding or collateral swap transaction, both transactions must be unwound for the purpose of calculating the adjusted HQLA amounts."
  > "The formula for the calculation of the stock of HQLA is as follows:"
  > "Adjustment for 15% cap = max"
  > "Adjustment for 40% cap = max"
  > — LCR30.37, LCR30.38, LCR30.39 ^lcr30-37


- Level 1 không bị haircut và gồm: tiền mặt, dự trữ NHTW rút được khi stress (gồm tiền gửi qua đêm và tiền gửi kỳ hạn có điều khoản rút theo thông báo), chứng khoán khả nhượng có rủi ro 0% phát hành/bảo lãnh bởi chính phủ/NHTW/PSE/MDB. Nếu chính phủ có hệ số rủi ro khác 0%, trái phiếu chính phủ/NHTW phát hành bằng đồng nội tệ vẫn được tính vào Level 1; nếu bằng ngoại tệ thì giới hạn bằng net outflow của ngoại tệ đó.
  > "Level 1 assets can comprise an unlimited share of the pool and are not subject to a haircut under the LCR."
  > "coins and banknotes"
  > "central bank reserves … to the extent that the central bank policies allow them to be drawn down in times of stress"
  > "In this context, central bank reserves would include banks' overnight deposits with the central bank, and term deposits with the central bank: (i) that are explicitly and contractually repayable on notice from the depositing bank; or (ii) that constitute a loan against which the bank can borrow on a term basis or on an overnight but automatically renewable basis"
  > "where the sovereign has a non-0% risk weight, sovereign or central bank debt securities issued in domestic currencies by the sovereign or central bank in the country in which the liquidity risk is being taken or in the bank's home country"
  > "where the sovereign has a non-0% risk weight, domestic sovereign or central bank debt securities issued in foreign currencies are eligible up to the amount of the bank's stressed net cash outflows in that specific foreign currency"
  > — LCR30.40, LCR30.41 ^lcr30-41

- Level 2A áp dụng haircut 15%, gồm: chứng khoán chính phủ/NHTW/PSE/MDB hệ số rủi ro 20%; trái phiếu doanh nghiệp (không do định chế tài chính phát hành) và covered bond (không do chính ngân hàng phát hành) có rating tối thiểu AA- (hoặc PD nội bộ tương đương). Tiêu chuẩn biến động giá thị trường: sụt giá tối đa không quá 10% trong thời kỳ 30 ngày stress.
  > "A 15% haircut is applied to the current market value of each Level 2A asset held in the stock of HQLA."
  > "Marketable securities representing claims on or guaranteed by sovereigns, central banks, PSEs or multilateral development banks that satisfy all of the following conditions: … assigned a 20% risk weight under CRE20"
  > "Corporate debt securities (including commercial paper) … and covered bonds … that satisfy all the following conditions: … have a long-term credit rating from a recognised external credit assessment institution (ECAI) of at least AA-"
  > "maximum decline of price not exceeding 10% or increase in haircut not exceeding 10 percentage points over a 30-day period during a relevant period of significant liquidity stress"
  > — LCR30.43 ^lcr30-43

- Level 2B áp dụng haircut lớn hơn (25% đến 50%), gồm: RMBS rating tối thiểu AA, LTV bình quân ≤ 80% khi phát hành, sụt giá stress ≤ 20% (haircut 25%); trái phiếu doanh nghiệp rating BBB- đến A+, sụt giá stress ≤ 20% (haircut 50%); cổ phiếu thuộc chỉ số chính nội địa bằng đồng nội tệ, sụt giá stress ≤ 40% (haircut 50%).
  > "A larger haircut is applied to the current market value of each Level 2B asset held in the stock of HQLA."
  > "Residential mortgage backed securities (RMBS) that satisfy all of the following conditions may be included in Level 2B, subject to a 25% haircut: … the underlying mortgages are "full recourse" loans … and have a maximum loan-to-value ratio (LTV) of 80% on average at issuance"
  > "Corporate debt securities (including commercial paper) … that satisfy all of the following conditions may be included in Level 2B, subject to a 50% haircut: … have a long-term credit rating from a recognised ECAI of at least BBB-"
  > "maximum decline of price not exceeding 20% or increase in haircut over a 30-day period not exceeding 20 percentage points during a relevant period of significant liquidity stress"
  > "Common equity shares that satisfy all of the following conditions may be included in Level 2B, subject to a 50% haircut: … a constituent of major stock index (or indices) of the home jurisdiction where the liquidity risk is taken"
  > "maximum decline of price not exceeding 40% or increase in haircut over a 30-day period not exceeding 40 percentage points during a relevant period of significant liquidity stress"
  > — LCR30.45 ^lcr30-45

- Hạn mức thanh khoản cam kết có hạn chế (RCLF) từ NHTW được tính vào Level 2B nếu chịu phí cam kết tối thiểu bằng mức lớn hơn giữa 75 bps/năm hoặc 25 bps cao hơn chênh lệch lợi suất tài sản thế chấp và HQLA đại diện; có tài sản thế chấp unencumbered hỗ trợ và kỳ hạn vượt quá 30 ngày.
  > "supervisors may choose to include within Level 2B assets the undrawn value of any contractual committed liquidity facility (CLF) provided by a central bank"
  > "The facility (termed a restricted-use committed liquidity facility, or RCLF) must, in normal times, be subject to a commitment fee on the total (drawn and undrawn) facility amount that is at least the greater of: … 75 basis points per annum; or … at least 25 basis points per annum above the difference in yield on the assets used to secure the RCLF and the yield on a representative portfolio of HQLA after adjusting for any material differences in credit risk."
  > — LCR30.46 ^lcr30-46

- Supervisor có thẩm quyền quy định các sản phẩm tài chính Shari'ah (như Sukuk) là HQLA thay thế cho ngân hàng Hồi giáo với các điều kiện và haircut phù hợp.
  > "national supervisors in jurisdictions in which Shari'ah compliant banks operate have the discretion to define Shari'ah compliant financial products (such as Sukuk) as alternative HQLA applicable to such banks only, subject to such conditions or haircuts that the supervisors may require."
  > — LCR30.47 ^lcr30-47

### LCR31 — Alternative liquidity approaches

#### Điều kiện và phạm vi áp dụng

- Một số quốc gia có thể thiếu hụt nguồn cung HQLA Level 1 (hoặc cả Level 1 và Level 2) bằng đồng nội tệ để đáp ứng tổng nhu cầu của các ngân hàng. Basel phát triển cơ chế thanh khoản thay thế (ALA), chỉ áp dụng cho một số ít quốc gia và đồng tiền đủ điều kiện. Sự thiếu hụt riêng Level 2 không đủ điều kiện áp dụng ALA.
  > "Some jurisdictions may have an insufficient supply of Level 1 high-quality liquid assets (HQLA), or both Level 1 and Level 2 HQLA,[^p27-0] in their domestic currency[^p27-1] to meet the aggregate demand of banks with significant exposures in this currency. To address this situation, the Basel Committee has developed alternative treatments for holdings in the stock of HQLA, which are expected to apply to a limited number of currencies and jurisdictions."
  > — LCR31.1 ^lcr31-1

- Có 3 lựa chọn thay thế (ALA): (1) Hạn mức thanh khoản cam kết theo hợp đồng từ NHTW có thu phí (Option 1); (2) Sử dụng HQLA bằng ngoại tệ để bù đắp nhu cầu thanh khoản nội tệ (Option 2); (3) Sử dụng bổ sung tài sản Level 2 với mức haircut cao hơn (Option 3).
  > "There are three alternative treatments available: (1) contractual committed liquidity facilities from the relevant central bank, for a fee (Option 1); (2) foreign currency HQLA to cover domestic liquidity needs (Option 2); and (3) additional use of Level 2 assets with a higher haircut (Option 3)."
  > — LCR31.3 ^lcr31-3

- Quốc gia không bị giới hạn ở 1 lựa chọn, nhưng việc sử dụng phải bị khống chế bởi một hạn mức tổng thể do supervisor quy định (tính bằng % tổng HQLA yêu cầu bằng đồng tiền đó). Ví dụ nếu trần là 80%, ngân hàng phải đáp ứng ít nhất 20% yêu cầu HQLA bằng tài sản Level 1 nội tệ.
  > "the usage of any of the above options must be constrained by a limit specified by supervisors in jurisdictions whose currency is eligible for the alternative treatment. The limit should be expressed in terms of the maximum amount of HQLA associated with the use of the options (whether individually or in combination) that a bank is allowed to include in its Liquidity Coverage Ratio (LCR), as a percentage of the total amount of HQLA the bank is required to hold in the currency concerned."
  > "If, for example, the maximum level of usage of the options is set at 80%, it means that a bank adopting the options, either individually or in combination, would only be allowed to include HQLA associated with the options (after applying any relevant haircut) up to 80% of the required amount of HQLA in the relevant currency. … Thus, at least 20% of the HQLA requirement would need to be met by Level 1 assets in the relevant currency."
  > — LCR31.4, LCR31.5 ^lcr31-4

- Ngân hàng phải chứng minh đã nỗ lực tối đa sử dụng tài sản Level 1, Level 2 và giảm thiểu rủi ro thanh khoản (giảm net cash outflows) trước khi xin áp dụng ALA. Không được coi ALA là công cụ tối đa hoá lợi nhuận dựa trên chênh lệch lợi suất; tính thanh khoản quan trọng hơn lợi suất ròng.
  > "A bank must demonstrate that it has taken reasonable steps to use Level 1 and Level 2 assets and reduce the amount of liquidity risk (as measured by reducing net cash outflows in the LCR) to improve its LCR, before applying an alternative treatment."
  > "Banks should not treat the use of the options simply as an economic choice that maximises the profits of the bank through the selection of alternative HQLA based primarily on yield considerations. The liquidity characteristics of an alternative HQLA portfolio should be considered to be more important than its net yield."
  > — LCR31.10 ^lcr31-10

#### Chi tiết 3 lựa chọn (Option 1, Option 2, Option 3)

- **Option 1 (Committed Liquidity Facility - CLF):** Hạn mức thanh khoản cam kết từ NHTW phải là thỏa thuận hợp đồng riêng biệt với cơ chế thường trực (standing facilities); kỳ hạn tối thiểu vượt ngoài cửa sổ 30 ngày của LCR; không thể hủy ngang trước hạn; không đòi hỏi quyết định tín dụng ex-post của NHTW khi rút vốn; và phải chịu phí cam kết thu trên toàn bộ hạn mức bất kể có rút hay không. Mức phí phải triệt tiêu động cơ tìm kiếm lợi suất (lợi suất ròng của tài sản thế chấp sau khi trừ phí không được cao hơn lợi suất danh mục Level 1/Level 2 tương ứng).
  > "Under Option 1, banks may access contractual committed liquidity facilities provided by the relevant central bank (ie relevant given the currency in question) for a fee."
  > "these facilities must be established contractual arrangements between the central bank and the commercial bank with a maturity date which, at a minimum, falls outside the 30-day LCR window. Further, the contract must be irrevocable prior to maturity and must not involve an ex post credit decision by the central bank. Such facilities must also incur a fee for the facility which is charged regardless of the amount, if any, drawn down against that facility; and the fee must be set so that both banks that claim the facility to meet the LCR and banks that do not have similar financial incentives to reduce their exposure to liquidity risk. That is, the fee should be set so that the net yield on the assets used to secure the facility should not be higher than the net yield on a representative portfolio of Level 1 and Level 2 assets, after adjusting for any material differences in credit risk."
  > — LCR31.12 ^lcr31-12

- **Option 2 (HQLA bằng ngoại tệ bù đắp thanh khoản nội tệ):** Cho phép ngân hàng thiếu hụt HQLA nội tệ nắm giữ HQLA bằng ngoại tệ có khả năng chuyển đổi tự do và đáng tin cậy. Vị thế bất cân xứng kỳ hạn đồng tiền (currency mismatch) phải được kiểm soát trong hạn mức của supervisor.
  > "Under Option 2, supervisors may permit banks that evidence a shortfall of HQLA in the domestic currency (ie insufficient domestic currency HQLA relative to domestic currency liquidity risk) to hold HQLA in a currency that does not match the currency of the associated liquidity risk. However, the resulting currency mismatch positions must be justifiable and controlled within limits agreed by their supervisors."
  > — LCR31.13 ^lcr31-13

- HQLA ngoại tệ trong Option 2 phải chịu haircut tối thiểu 8% đối với các đồng tiền chủ chốt (turnover toàn cầu ≥ 10%). Các đồng tiền khác áp dụng haircut cao hơn dựa trên biến động tỷ giá lịch sử. Trường hợp đồng tiền được neo tỷ giá chính thức hiệu quả (peg mechanism), haircut có thể hạ thấp tương ứng. Haircut áp dụng cho phần HQLA ngoại tệ vượt ngưỡng do supervisor quy định (ngưỡng tối đa 25% tổng net cash outflows nội tệ).
  > "such liquid assets must be subject to a minimum haircut of 8% for major currencies that are active in global foreign exchange markets."
  > "If the domestic currency is formally pegged to another currency under an effective mechanism, the haircut for the pegged currency may be lowered to a level that reflects the limited exchange rate risk under the peg arrangement."
  > "Hence under a threshold of 25%, a bank using Option 2 must apply the haircut to that portion of foreign currency HQLA in excess of 25% that are used to cover liquidity needs in the domestic currency."
  > — LCR31.14, LCR31.15 ^lcr31-14

- **Option 3 (Sử dụng thêm tài sản Level 2A vượt trần):** Cho phép bổ sung Level 2A vào HQLA khi thiếu hụt Level 1 nhưng có đủ Level 2A. Toàn bộ phần Level 2A vượt trần 40% phải chịu haircut tối thiểu 20% (cao hơn 5% so với mức chuẩn 15%). Level 2B vẫn tuyệt đối tuân thủ trần 15%. Ngân hàng phải chịu được kiểm tra sức chịu tải giá trị danh mục khi stress thị trường.
  > "This option addresses currencies for which there are insufficient Level 1 assets, as determined by reference to the qualifying principles and criteria, but where there are sufficient Level 2A assets. Under this option, supervisors may permit banks that evidence a shortfall of HQLA in the domestic currency (ie relative to domestic currency liquidity risk) to hold additional Level 2A assets in the stock of HQLA. These additional Level 2A assets must be subject to a minimum haircut of 20%, ie 5% higher than the 15% haircut applicable to Level 2A assets that are included in the 40% cap."
  > "Any Level 2B assets held by the bank must remain subject to the cap of 15%, regardless of the amount of other Level 2 assets held."
  > — LCR31.17 ^lcr31-17

#### Nguyên tắc đánh giá điều kiện đủ (Qualifying Principles)

- Để đủ điều kiện áp dụng ALA, quốc gia phải thỏa mãn cả 3 nguyên tắc: (Principle 1) Chứng minh sự thiếu hụt HQLA nội tệ mang tính cơ cấu trong trung hạn (3–5 năm) không thể khắc phục ngay; (Principle 2) Có năng lực hạn chế và quản trị rủi ro không thực hiện được của các lựa chọn (năng lực tài chính bảo trợ CLF, quản lý rủi ro FX, tiêu chuẩn khắt khe cho Level 2A bổ sung); (Principle 3) Cam kết nghĩa vụ giám sát, công bố minh bạch và đánh giá định kỳ.
  > "All of the following principles must be satisfied in order for a jurisdiction to qualify for alternative treatment. (1) To use the alternative treatment under the LCR, a jurisdiction must demonstrate and justify that insufficient HQLA denominated in the domestic currency exists, taking into account all relevant factors affecting the supply of, and demand for, such HQLA (Principle 1). … (2) A jurisdiction that intends to adopt one or more of the options for alternative treatment must be capable of limiting the uncertainty of performance, or mitigating the risks of non-performance, of the option(s) concerned (Principle 2). … (3) A jurisdiction that intends to adopt one or more of the options for alternative treatment must be committed to observing all of the obligations set out below (Principle 3)."
  > — LCR31.20 ^lcr31-20

- Quốc gia áp dụng ALA phải thực hiện tự đánh giá lại điều kiện đủ định kỳ tối đa 5 năm một lần, công bố công khai kết quả và chấp nhận quy trình bình duyệt độc lập (independent peer review) của Ủy ban Basel. Nếu sự thiếu hụt không còn, phải lập lộ trình chuyển đổi về chuẩn mực LCR thông thường.
  > "The jurisdiction should perform a review of its eligibility for alternative treatment every five years after it has adopted the options. The primary purpose of this review is to determine that there remains insufficient HQLA in the jurisdiction. The review should be in the form of a self-assessment of the jurisdiction's compliance with each of the Principles set out in this chapter."
  > — LCR31.58 ^lcr31-58

### LCR40 — Cash inflows and outflows

#### Định nghĩa và nguyên tắc chung

- Total net cash outflows = tổng dòng ra kỳ vọng − tổng dòng vào kỳ vọng trong 30 ngày stress. Dòng ra = số dư × run-off/drawdown rate; dòng vào = số dư phải thu × inflow rate, có trần 75% dòng ra.
  > "The term total net cash outflows … is defined as the total expected cash outflows minus total expected cash inflows in the specified stress scenario for the subsequent 30 calendar days."
  > "Total expected cash inflows are calculated by multiplying the outstanding balances of various categories of contractual receivables by the rates at which they are expected to flow in under the scenario up to an aggregate cap of 75% of total expected cash outflows."
  > — LCR40.1 ^lcr40-1

- Phần lớn tham số được hài hoà giữa các jurisdiction; một số tham số do supervisor quốc gia quyết định và phải công bố.
  > "a few parameters are to be determined by supervisory authorities at the national level. Where this is the case, the parameters should be transparent and made publicly available."
  > — LCR40.2 ^lcr40-2

- Không đếm trùng: tài sản đã tính vào HQLA (tử số) thì dòng vào của nó không được tính vào mẫu số.
  > "if an asset is included as part of the stock of high-quality liquid assets (HQLA) (ie the numerator), the associated cash inflows cannot also be counted as cash inflows (ie part of the denominator)."
  > — LCR40.4 ^lcr40-4

#### Dòng ra — tiền gửi bán lẻ

- Tiền gửi bán lẻ là tiền gửi của thể nhân. Tiền gửi của pháp nhân, doanh nghiệp tư nhân, hợp danh thuộc nhóm wholesale.
  > "Retail deposits are defined as deposits placed with a bank by a natural person. Deposits from legal entities, sole proprietorships or partnerships are captured in wholesale deposit categories."
  > — LCR40.5 ^lcr40-5

- Tiền gửi bán lẻ chia thành "stable" và "less stable". Run-off rate là **mức sàn**, jurisdiction có thể đặt cao hơn.
  > "The run-off rates for retail deposits are minimum floors, with higher run-off rates established by individual jurisdictions as appropriate to capture depositor behaviour in a period of stress in each jurisdiction."
  > — LCR40.6 ^lcr40-6

- Stable deposits thường chịu run-off 5%. Điều kiện: được bảo hiểm toàn bộ bởi một quỹ bảo hiểm tiền gửi hiệu quả, VÀ người gửi có quan hệ khác với ngân hàng hoặc là tài khoản giao dịch (ví dụ tài khoản nhận lương).
  > "Stable deposits, which usually receive a run-off factor of 5%, are the amount of the deposits that are fully insured … by an effective deposit insurance scheme or by a public guarantee that provides equivalent protection and where:"
  > — LCR40.7 ^lcr40-7

- Bốn tiêu chí của "effective deposit insurance scheme": chi trả nhanh, phạm vi rõ ràng, công chúng biết rộng rãi, tổ chức bảo hiểm có quyền pháp lý và độc lập.
  > "(1) that guarantees that it has the ability to make prompt payouts; (2) for which the coverage is clearly defined; (3) of which public awareness is high; and (4) in which the deposit insurer has formal legal powers to fulfil its mandate and is operationally independent, transparent and accountable."
  > — LCR40.8 ^lcr40-8

- Có bảo hiểm tiền gửi thôi chưa đủ để coi là "stable".
  > "The presence of deposit insurance alone is not sufficient to consider a deposit "stable"."
  > — LCR40.10 ^lcr40-10

- Jurisdiction có thể áp run-off 3% cho stable deposits nếu quỹ bảo hiểm có prefunding, có nguồn vốn dự phòng và chi trả nhanh.
  > "Jurisdictions may choose to apply a run-off rate of 3% to stable deposits in their jurisdiction, if they meet the above stable deposit criteria and the following additional criteria for deposit insurance schemes:"
  > — LCR40.11 ^lcr40-11

- Áp mức 3% thì phải chứng minh được run-off thực tế của stable deposits dưới 3% trong các giai đoạn stress.
  > "should be able to provide evidence of run-off rates for stable deposits within the banking system below 3% during any periods of stress"
  > — LCR40.12 ^lcr40-12

- Less stable deposits có run-off tối thiểu 10%. Supervisor lập thêm bucket cao hơn, ví dụ: tiền gửi không được bảo hiểm toàn bộ, giá trị lớn, khách hàng HNW, internet deposits, ngoại tệ.
  > "with a minimum run-off rate of 10%"
  > "Buckets of less stable deposits may include deposits that are not fully covered by an effective deposit insurance scheme or sovereign deposit guarantee, high-value deposits, deposits from sophisticated or high net worth individuals, deposits that can be withdrawn quickly (eg internet deposits) and foreign currency deposits, as determined by each jurisdiction."
  > — LCR40.13 ^lcr40-13

- Không xác định được tiền gửi nào đủ điều kiện "stable" thì phải xếp toàn bộ vào less stable.
  > "it must place the full amount in the "less stable" buckets as established by its supervisor."
  > — LCR40.14 ^lcr40-14

- Run-off của tiền gửi ngoại tệ do supervisor quyết định. Tiền gửi ngoại tệ biến động hơn nội tệ thì phải coi là less stable.
  > "Supervisors will determine the run-off factor that banks in their jurisdiction should use for foreign currency deposits."
  > — LCR40.15 ^lcr40-15

- Tiền gửi có kỳ hạn còn lại > 30 ngày được loại khỏi dòng ra nếu người gửi không có quyền rút trong 30 ngày, hoặc rút trước hạn bị phạt đáng kể (lớn hơn rõ rệt so với mất lãi).
  > "Cash outflows related to retail term deposits with a residual maturity or withdrawal notice period greater than 30 days may be excluded from total expected cash outflows if the depositor has no legal right to withdraw deposits within the 30-day horizon of the LCR, or if early withdrawal results in a significant penalty that is materially greater than the loss of interest."
  > — LCR40.16 ^lcr40-16

- Ngân hàng cho rút mà không phạt thì **toàn bộ nhóm** tiền gửi đó bị coi là không kỳ hạn.
  > "the entire category of these funds must be treated as demand deposits"
  > — LCR40.17 ^lcr40-17

#### Dòng ra — wholesale funding không đảm bảo

- Unsecured wholesale funding là nợ huy động từ pháp nhân, không có tài sản bảo đảm, không gồm nghĩa vụ phái sinh.
  > ""unsecured wholesale funding" is defined as those liabilities and general obligations that are raised from non-natural persons (ie legal entities, including sole proprietorships and partnerships) and are not collateralised by legal rights to specifically designated assets owned by the borrowing institution"
  > — LCR40.19 ^lcr40-19

- Chỉ tính phần đáo hạn hoặc có thể bị rút trong 30 ngày, kể cả phần có quyền chọn của nhà đầu tư. Kỳ vọng thị trường về việc mua lại sớm cũng phải được giả định.
  > "The wholesale funding included in the LCR is defined as all funding that is callable within the LCR's horizon of 30 days or that has its earliest possible contractual maturity date situated within this horizon"
  > — LCR40.20 ^lcr40-20

- Vốn từ khách hàng SME được xử lý như tiền gửi bán lẻ (cùng bucket và run-off).
  > "Unsecured wholesale funding provided by small business customers is treated the same way as retail deposits for the purposes of this standard"
  > — LCR40.22 ^lcr40-22

- Ngưỡng SME: tổng vốn huy động từ một khách hàng < 1 triệu EUR (hợp nhất).
  > "provided the total aggregated funding … raised from one small business customer is less than €1 million (on a consolidated basis where applicable)."
  > — LCR40.23 ^lcr40-23

- Operational deposits (clearing, custody, cash management) được run-off 25% nếu khách hàng phụ thuộc thực chất vào ngân hàng; cần supervisor chấp thuận.
  > "These funds may receive a 25% run-off factor only if the customer has a substantive dependency with the bank and the deposit is required for such activities."
  > — LCR40.26 ^lcr40-26

- Điều kiện của dịch vụ: khách phụ thuộc vào ngân hàng như bên trung gian thứ ba độc lập, có hợp đồng ràng buộc, chấm dứt phải báo trước ≥ 30 ngày hoặc chịu chi phí chuyển đổi đáng kể.
  > "The termination of such agreements must be subject either to a notice period of at least 30 days or significant switching costs"
  > — LCR40.27 ^lcr40-27

- Operational deposit phải là sản phẩm phụ của dịch vụ, nằm trong tài khoản chuyên biệt, và không được định giá theo cách khuyến khích khách để dư. Khi lãi suất gần 0, tài khoản nên không trả lãi. Trong giai đoạn lãi suất thấp kéo dài, excess balance có thể rất lớn.
  > "In the case that interest rates in a jurisdiction are close to zero, such accounts should be non-interest bearing. Banks should be particularly aware that during prolonged periods of low interest rates, excess balances (as defined below) could be significant."
  > — LCR40.28 ^lcr40-28

- Số dư vượt nhu cầu vận hành (excess balance) không được hưởng 25%. Không xác định được excess thì toàn bộ là non-operational.
  > "Any excess balances that could be withdrawn and would still leave enough funds to fulfil these clearing, custody and cash management activities do not qualify for the 25% factor."
  > "If banks are unable to determine the amount of the excess balance, then the entire deposit must be assumed to be excess to requirements and, therefore, considered non-operational."
  > — LCR40.29 ^lcr40-29

- Ngân hàng phải xây dựng phương pháp luận xác định số dư vượt mức (excess deposits) ở cấp độ đủ chi tiết để đánh giá rủi ro rút vốn trong stress riêng lẻ, tính đến các chỉ báo như tỷ lệ số dư tài khoản trên khối lượng thanh toán/quyết toán hoặc tài sản lưu ký.
  > "Banks must determine the methodology for identifying excess deposits that are excluded from this treatment. This assessment should be conducted at a sufficiently granular level to adequately assess the risk of withdrawal in an idiosyncratic stress. The methodology should take into account relevant factors such as the likelihood that wholesale customers have above average balances in advance of specific payment needs, and consider appropriate indicators (eg ratios of account balances to payment or settlement volumes or to assets under custody) to identify those customers that are not actively managing account balances efficiently."
  > — LCR40.30 ^lcr40-30

- Bên gửi operational deposit phải tính inflow 0%.
  > "Operational deposits must receive a 0% inflow assumption for the depositing bank"
  > — LCR40.31 ^lcr40-31

- Correspondent banking và prime brokerage không được coi là hoạt động operational.
  > "if the deposit under consideration arises out of correspondent banking or from the provision of prime brokerage services, it must be treated as if there were no operational activity for the purpose of determining run-off factors."
  > — LCR40.32 ^lcr40-32

- Dịch vụ bù trừ (clearing) giới hạn ở các thỏa thuận cho phép khách hàng chuyển vốn hoặc chứng khoán gián tiếp qua các thành viên trực tiếp trong hệ thống thanh toán bù trừ, bao gồm truyền nhận lệnh thanh toán, thấu chi trong ngày và quản lý số dư sau quyết toán.
  > "A clearing relationship, in this context, refers to a service arrangement that enables customers to transfer funds (or securities) indirectly through direct participants in domestic settlement systems to final recipients."
  > — LCR40.33 ^lcr40-33

- Dịch vụ lưu ký (custody) bao gồm quản lý an toàn, báo cáo và xử lý tài sản tài chính thay mặt khách hàng, bao gồm quyết toán giao dịch chứng khoán, xử lý tài sản bảo đảm, nhận cổ tức/thu nhập và các dịch vụ quản lý tiền mặt liên quan đến lưu ký.
  > "A custody relationship, in this context, refers to the provision of safekeeping, reporting, processing of assets or the facilitation of the operational and administrative elements of related activities on behalf of customers in the process of their transacting and retaining financial assets."
  > — LCR40.34 ^lcr40-34

- Dịch vụ quản lý tiền mặt (cash management) cung cấp các sản phẩm và dịch vụ để khách hàng quản lý dòng tiền, tài sản nợ/có và thực hiện các giao dịch thanh toán cần thiết cho hoạt động kinh doanh liên tục, như kiều hối, thu/chi hộ và quản lý chi trả lương.
  > "A cash management relationship, in this context, refers to the provision of cash management and related services to customers. Cash management services, in this context, refers to those products and services provided to a customer to manage its cash flows, assets and liabilities, and conduct financial transactions necessary to the customer's ongoing operations."
  > — LCR40.35 ^lcr40-35

- Phần operational deposit được bảo hiểm toàn bộ có thể xử lý như stable retail.
  > "The portion of the operational deposits generated by clearing, custody and cash management activities that is fully covered by deposit insurance may receive the same treatment as "stable" retail deposits."
  > — LCR40.36 ^lcr40-36

- Tiền gửi trong mạng lưới các ngân hàng hợp tác xã (institutional networks of cooperative banks) có cơ chế bảo vệ tương hỗ chống mất khả năng thanh khoản/thanh toán được áp run-off 25% đối với khoản gửi tại định chế trung ương do yêu cầu tiền gửi tối thiểu theo luật định hoặc phân công nhiệm vụ chung.
  > "So long as both the bank that has received the monies and the bank that has deposited participate in the same institutional network's mutual protection scheme against illiquidity and insolvency of its members, a 25% run-off rate may be given to the amount of deposits of member institutions with the central institution or specialised central service providers that are placed: (1) due to statutory minimum deposit requirements, which are registered at regulators; or (2) in the context of common task sharing and legal, statutory or contractual arrangements."
  > — LCR40.37 ^lcr40-37

- Bên gửi tiền trong mạng lưới ngân hàng hợp tác xã phải tính inflow 0% đối với khoản tiền gửi này.
  > "As with other operational deposits, these deposits must receive a 0% inflow assumption for the depositing bank, as these funds are considered to remain with the centralised institution."
  > — LCR40.38 ^lcr40-38

- Việc áp dụng tỷ lệ đối với mạng lưới ngân hàng hợp tác xã phải có sự chấp thuận của supervisor; hoạt động correspondent banking bị loại trừ và phải chịu dòng ra 100%.
  > "Supervisory approval should be given to ensure that banks utilising this treatment actually are the central institution or a central service provider of such a cooperative (or otherwise named) network. Correspondent banking activities must not be included in this treatment and must receive a 100% outflow treatment"
  > — LCR40.39 ^lcr40-39

- Doanh nghiệp phi tài chính, chính phủ, NHTW, MDB, PSE (không có quan hệ operational): run-off 40%.
  > "The run-off factor for these funds must be 40%, unless the criteria in LCR40.41 are met."
  > — LCR40.40 ^lcr40-40

- Mức 20% nếu toàn bộ khoản tiền gửi được bảo hiểm.
  > "may receive a 20% run-off factor if the entire amount of the deposit is fully covered by an effective deposit insurance scheme or by a public guarantee that provides equivalent protection."
  > — LCR40.41 ^lcr40-41

- Tổ chức tài chính và pháp nhân khác (ngân hàng, công ty chứng khoán, bảo hiểm, fiduciary, SPV, công ty liên kết): run-off 100%.
  > "The run-off factor for these funds must be 100%."
  > — LCR40.42 ^lcr40-42

- Trái phiếu và giấy tờ nợ do ngân hàng phát hành thuộc nhóm 100%, trừ khi chỉ bán cho và chỉ được nắm giữ bởi khách bán lẻ/SME.
  > "All notes, bonds and other debt securities issued by the bank must be included in this category regardless of the holder, unless the bond is sold exclusively in the retail market and held in retail accounts"
  > — LCR40.43 ^lcr40-43

- Số dư tiền mặt của khách hàng từ dịch vụ prime brokerage phải được tách biệt khỏi các khoản phong tỏa theo luật bảo vệ tài sản khách hàng, không được bù trừ với các phơi nhiễm khác, bị loại khỏi HQLA và được ghi nhận là dòng vào theo LCR40.87.
  > "Customer cash balances arising from the provision of prime brokerage services, including but not limited to the cash arising from prime brokerage services as identified in LCR40.32, must be considered separate from any required segregated balances related to client protection regimes imposed by national regulations, and must not be netted against other customer exposures included in this standard. These offsetting balances held in segregated accounts are treated as inflows in LCR40.87 and must be excluded from the stock of HQLA."
  > — LCR40.44 ^lcr40-44

#### Dòng ra — secured funding

- Secured funding là nợ có bảo đảm bằng quyền pháp lý trên tài sản cụ thể. Không gồm giao dịch bảo đảm bằng tài sản không giao dịch được, trừ khi đối tác là NHTW.
  > ""secured funding" is defined as those liabilities and general obligations that are collateralised by legal rights to specifically designated assets owned by the borrowing institution in the case of bankruptcy, insolvency, liquidation or resolution."
  > — LCR40.45 ^lcr40-45

- Khi stress, khả năng tiếp tục thực hiện repo, reverse repo và tài trợ chứng khoán bị thu hẹp; hoán đổi tài sản bảo đảm (collateral swaps) được xử lý như repo/reverse repo; tài sản cho khách hàng vay để bán khống (customer short positions) được đối xử như một hình thức secured funding và tính dòng ra dựa trên số vốn huy động được.
  > "Loss of secured funding on short-term financing transactions: In this scenario, the ability to continue to transact repurchase, reverse repurchase and other securities financing transactions is limited to transactions backed by HQLA or with the bank's domestic sovereign, PSE or central bank. Collateral swaps must be treated as repurchase or reverse repurchase agreements, as must any other transaction with a similar form. Additionally, collateral lent to the bank's customers to effect short positions must be treated as a form of secured funding. … The amount of outflow must be calculated based on the amount of funds raised through the transaction, and not the value of the underlying collateral."
  > — LCR40.46 ^lcr40-46

- Giao dịch bảo đảm bằng Level 1 hoặc với NHTW trong nước: không giảm khả năng huy động. Level 2: giảm bằng haircut. Với chính phủ, MDB, PSE trong nước (RW ≤ 20%) bảo đảm bằng tài sản khác L1/L2A: 25%.
  > "Due to the high quality of Level 1 assets, no reduction in funding availability against these assets is assumed to occur."
  > "A reduction in funding availability must be assigned to maturing transactions backed by Level 2 assets equivalent to the required haircuts."
  > — LCR40.47 ^lcr40-47

- Các giao dịch khác đáo hạn: run-off 100%. Bảng tóm tắt theo loại tài sản bảo đảm (giao dịch đáo hạn trong 30 ngày):
  > "For all other maturing transactions the run-off factor is 100%"
  > "The table below summarises the outflow applicable to transactions maturing within 30 days."
  > — LCR40.48 ^lcr40-48

  | Tài sản bảo đảm / đối tác | Dòng ra |
  |---|---|
  | Level 1 hoặc với NHTW | 0% |
  | Level 2A | 15% |
  | Với chính phủ, PSE (RW ≤ 20%), MDB trong nước, không bảo đảm bằng L1/L2A | 25% |
  | RMBS đủ điều kiện Level 2B | 25% |
  | Level 2B khác | 50% |
  | Còn lại | 100% |

#### Dòng ra — các yêu cầu bổ sung

- Dòng ra phái sinh ròng: hệ số 100%. Chỉ được netting theo đối tác khi có master netting agreement. Quyền chọn "in the money" được giả định thực hiện.
  > "The sum of all net derivative cash outflows must receive a 100% factor."
  > "Options that can be exercised within the next 30 days, including options that expire in greater than 30 days (eg an Americanstyle option), must be assumed to be exercised when they are "in the money" to the option buyer."
  > — LCR40.49 ^lcr40-49

- Trường hợp thanh toán phái sinh được bảo đảm bằng HQLA, dòng tiền ra được tính ròng với dòng tiền hoặc tài sản nhận về theo hợp đồng nếu ngân hàng có quyền pháp lý và năng lực vận hành tái sử dụng tài sản đó (chống đếm trùng).
  > "Where derivative payments are collateralised by HQLA, cash outflows should be calculated net of any corresponding cash or collateral inflows that would result, all other things being equal, from contractual obligations for cash or collateral to be provided to the bank, if the bank is legally entitled and operationally capable to re-use the collateral in new cash raising transactions once the collateral is received. This is in line with the principle that banks should not double count liquidity inflows and outflows."
  > — LCR40.50 ^lcr40-50

- Downgrade trigger: 100% tài sản bảo đảm hoặc dòng tiền phát sinh khi bị hạ tới 3 notch.
  > "the bank assumes that 100% of this additional collateral or cash outflow must be posted for any downgrade up to and including a 3-notch downgrade of the bank's long-term credit rating."
  > — LCR40.51 ^lcr40-51

- Tài sản bảo đảm không phải Level 1 đã đặt cọc: cộng thêm 20% giá trị vào HQLA yêu cầu.
  > "20% of the value of all such posted collateral, net of collateral received on a counterparty basis … must be added to the stock of required HQLA by the bank posting such collateral."
  > — LCR40.52 ^lcr40-52

- Nhu cầu thanh khoản phát sinh từ tài sản bảo đảm không tách biệt vượt mức (excess non-segregated collateral) mà đối tác có quyền rút theo hợp đồng bất kỳ lúc nào: tính 100% dòng ra.
  > "Increased liquidity needs related to excess non-segregated collateral held by the bank that could contractually be called at any time by the counterparty: 100% of the non-segregated collateral (ie where the collateral is unencumbered and included in the stock of HQLA or where a recall of collateral by the counterparty would need to use additional funding) that could contractually be recalled by the counterparty because the collateral is in excess of the counterparty's current collateral requirements."
  > — LCR40.53 ^lcr40-53

- Nhu cầu thanh khoản phát sinh từ tài sản bảo đảm đến hạn theo hợp đồng mà đối tác chưa yêu cầu nộp: tính 100% dòng ra.
  > "Increased liquidity needs related to contractually required collateral on transactions for which the counterparty has not yet demanded the collateral be posted: 100% of the collateral that is contractually due but where the counterparty has not yet demanded the posting of such collateral."
  > — LCR40.54 ^lcr40-54

- Nhu cầu thanh khoản từ hợp đồng cho phép đối tác thay thế tài sản bảo đảm sang non-HQLA mà không cần ngân hàng đồng ý: tính 100% dòng ra đối với phần HQLA không tách biệt có thể bị thay thế; nếu thay thế sang HQLA bậc thấp hơn thì dòng ra bằng chênh lệch haircut.
  > "Increased liquidity needs related to contracts that allow collateral substitution without the bank's consent to non-HQLA assets: 100% of the amount of non-segregated HQLA collateral that can be substituted with non-HQLA. For substitution of HQLA with other HQLA of a lower liquidity value, the outflow should be measured based on the difference between the LCR haircuts of the collateral currently held and the potential substitute collateral."
  > — LCR40.55 ^lcr40-55

- Biến động định giá: dùng dòng collateral ròng tuyệt đối lớn nhất trong 30 ngày, xét trong 24 tháng trước (look-back approach).
  > "Any outflow generated by increased needs related to market valuation changes must be included in the LCR calculated by identifying the largest absolute net 30-day collateral flow realised during the preceding 24 months."
  > — LCR40.56 ^lcr40-56

- ABS, covered bond và công cụ tài trợ cấu trúc do ngân hàng tự phát hành, đáo hạn trong 30 ngày: dòng ra 100%.
  > "100% outflow of funding transactions maturing within the 30-day period, when these instruments are issued by the bank itself"
  > — LCR40.57 ^lcr40-57

- Mất nguồn vốn tài trợ từ ABCP, conduit, công cụ đầu tư cấu trúc (SIV): tính 100% nợ ngắn hạn đáo hạn và 100% tài sản có thể bị trả lại qua quyền chọn bán thanh khoản (liquidity puts).
  > "Loss of funding on asset-backed commercial paper, conduits, securities investment vehicles and other such financing facilities: 100% of maturing amount and 100% of returnable assets. Banks having structured financing facilities that include the issuance of short-term debt instruments, such as asset-backed commercial paper, must fully consider the potential liquidity risk arising from these structures."
  > — LCR40.58 ^lcr40-58

- Committed facilities gồm hạn mức không huỷ ngang hoặc huỷ ngang có điều kiện. Phần được giả định rút thì coi là dư nợ không được trả lại, bất kể kỳ hạn.
  > "These facilities only include contractually irrevocable (committed) or conditionally revocable agreements to extend funds in the future."
  > "all facilities that are assumed to be drawn (as outlined in the paragraphs below) must be assumed to remain outstanding without repayment, regardless of maturity."
  > — LCR40.59 ^lcr40-59

- Phần hạn mức cam kết chưa giải ngân được tính ròng với HQLA hợp lệ đã đặt cọc hoặc cam kết đặt cọc khi rút vốn (ví dụ cơ cấu repo), nếu ngân hàng có quyền pháp lý và năng lực vận hành tái sử dụng tài sản đó và không có tương quan bất lợi giữa xác suất rút vốn và giá trị tài sản bảo đảm.
  > "The currently undrawn portion of these facilities may be calculated net of any HQLA eligible for the stock of HQLA, if the HQLA have already been posted as collateral by the counterparty to secure the facilities or that are contractually obliged to be posted when the counterparty will draw down the facility (eg a liquidity facility structured as a repo facility), if the bank is legally entitled and operationally capable to re-use the collateral in new cash raising transactions once the facility is drawn, and there is no undue correlation between the probability of drawing the facility and the market value of the collateral."
  > — LCR40.60 ^lcr40-60

- Định nghĩa liquidity facility: là hạn mức cam kết chưa rút được dùng để tái tài trợ nghĩa vụ nợ của khách hàng khi khách hàng không rollover được trên thị trường tài chính (ví dụ chương trình commercial paper). Phần hạn mức vượt quy mô nợ đáo hạn trong 30 ngày được xếp vào credit facility. Hạn mức vốn lưu động thông thường xếp vào credit facility.
  > "A liquidity facility is defined as any committed, undrawn backup facility that would be utilised to refinance the debt obligations of a customer in situations where such a customer is unable to rollover that debt in financial markets (eg pursuant to a commercial paper programme, secured financing transactions, obligations to redeem units). The amount of the commitment that must be treated as a liquidity facility is the amount of the currently outstanding debt issued by the customer … maturing within a 30-day period that is backstopped by the facility."
  > "General working capital facilities for corporate entities (eg revolving credit facilities in place for general corporate or working capital purposes) must not be classified as liquidity facilities, but as credit facilities."
  > — LCR40.61 ^lcr40-61

- Mọi hạn mức cung cấp cho quỹ đầu cơ (hedge funds), quỹ thị trường tiền tệ (MMFs), SPE, conduit phải được phân loại toàn bộ là liquidity facility cấp cho pháp nhân khác (drawdown 100%).
  > "any facilities provided to hedge funds, money market funds and special purpose funding vehicles, for example SPEs (as defined in LCR40.58) or conduits, or other vehicles used to finance the banks' own assets, must be captured in their entirety as a liquidity facility to other legal entities."
  > — LCR40.62 ^lcr40-62

- Tỷ lệ rút (drawdown) trên phần chưa giải ngân: bán lẻ/SME 5%; credit facility cho DN phi tài chính, chính phủ, NHTW, PSE, MDB 10%; liquidity facility cho nhóm này 30%; cho ngân hàng chịu giám sát 40%; credit facility cho định chế tài chính khác 40%; liquidity facility cho định chế tài chính khác 100%; pháp nhân khác (SPE, conduit) 100%.
  > "(1) Committed credit and liquidity facilities to retail and small business customers: banks must assume a 5% drawdown of the undrawn portion of these facilities."
  > "(2) Committed credit facilities to non-financial corporates, sovereigns and central banks, PSEs and multilateral development banks: banks must assume a 10% drawdown of the undrawn portion of these credit facilities."
  > "(3) Committed liquidity facilities to non-financial corporates, sovereigns and central banks, PSEs and multilateral development banks: banks must assume a 30% drawdown of the undrawn portion of these liquidity facilities."
  > "(4) Committed credit and liquidity facilities extended to banks subject to prudential supervision: banks must assume a 40% drawdown of the undrawn portion of these facilities."
  > — LCR40.64 ^lcr40-64

- Nghĩa vụ theo hợp đồng cấp vốn trong vòng 30 ngày cho các tổ chức tài chính và NHTW chưa được ghi nhận ở phần khác phải tính dòng ra 100%.
  > "Contractual obligations to extend funds within a 30-day period: Any contractual lending obligations to financial institutions, including central banks, not captured elsewhere in this standard must be captured here at a 100% outflow rate."
  > — LCR40.65 ^lcr40-65

- Nghĩa vụ cấp vốn theo hợp đồng cho khách bán lẻ và wholesale phi tài chính: phần vượt 50% dòng vào hợp đồng từ chính nhóm khách đó tính là dòng ra 100%.
  > "exceeds 50% of the total contractual inflows due in the next 30 calendar days from these clients, the difference must be reported as a 100% outflow."
  > — LCR40.66 ^lcr40-66

- Các nghĩa vụ tài trợ tiềm tàng khác: run-off do supervisor quốc gia quyết định và phải công bố.
  > "Other contingent funding obligations: (run-off rates at national discretion)."
  > — LCR40.67 ^lcr40-67

- Nghĩa vụ tài trợ tiềm tàng có thể mang tính hợp đồng hoặc phi hợp đồng (non-contractual) bắt nguồn từ rủi ro uy tín, các sản phẩm ngân hàng bảo trợ hoặc kỳ vọng thanh khoản của khách hàng.
  > "These contingent funding obligations may be either contractual or non-contractual and are not lending commitments. Non-contractual contingent funding obligations include associations with, or sponsorship of, products sold or services provided that may require the support or extension of funds in the future under stressed conditions. Non-contractual obligations may be embedded in financial products and instruments sold, sponsored, or originated by the institution that can give rise to unplanned balance sheet growth arising from support given for reputational risk considerations."
  > — LCR40.68 ^lcr40-68

- Một số nghĩa vụ tiềm tàng phụ thuộc vào các sự kiện tín dụng hoặc thị trường (ví dụ công cụ nợ autocallable note phát hành có trigger thị trường), ngân hàng và supervisor phải phân tích thận trọng các kịch bản kích hoạt.
  > "Some of these contingent funding obligations are explicitly contingent upon a credit or other event that is not always related to the liquidity events simulated in the stress scenario, but may nevertheless have the potential to cause significant liquidity drains in times of stress."
  > — LCR40.69 ^lcr40-69

- Nghĩa vụ tài trợ tiềm tàng phi hợp đồng liên quan đến việc cấp thanh khoản cho các liên doanh hoặc khoản đầu tư thiểu số không hợp nhất (theo LCR10.2) phải được ghi nhận khi ngân hàng là bên cung ứng thanh khoản chính.
  > "Non-contractual contingent funding obligations related to potential liquidity draws from joint ventures or minority investments in entities, which are not consolidated per LCR10.1, should be captured where there is the expectation that the bank will be the main liquidity provider when the entity is in need of liquidity."
  > — LCR40.70 ^lcr40-70

- Trade finance: cơ quan quốc gia có thể áp run-off thấp (ví dụ ≤ 5%).
  > "In the case of contingent funding obligations stemming from trade finance instruments, national authorities may apply a relatively low run-off rate (eg 5% or less)."
  > — LCR40.71 ^lcr40-71

- Danh mục các nghĩa vụ tài trợ tiềm tàng khác bao gồm: hạn mức tín dụng có thể hủy ngang vô điều kiện (uncommitted), bảo lãnh và thư tín dụng không liên quan thương mại, mua lại nợ trước hạn, quỹ ổn định giá trị, và vị thế bán khống của khách hàng bù trừ nội bộ bằng tài sản khách hàng khác (run-off tối thiểu 50%).
  > "National authorities must determine the run-off rates for the other contingent funding obligations listed below in accordance with LCR40.67."
  > "a minimum 50% run-off factor of the contingent obligations must be applied where banks have internally matched client assets against other clients' short positions where the collateral does not qualify as Level 1 or Level 2, and the bank may be obligated to find additional sources of funding for these positions in the event of client withdrawals."
  > — LCR40.73 ^lcr40-73

- Dòng ra hợp đồng khác: 100%. Không gồm chi phí hoạt động.
  > "Other contractual cash outflows: 100%."
  > "Outflows related to operating costs, however, are not included in this standard."
  > — LCR40.74 ^lcr40-74

#### Dòng vào

- Chỉ tính dòng vào theo hợp đồng từ khoản phải thu đang performing. Không tính dòng vào tiềm tàng, kể cả hạn mức từ NHTW.
  > "the bank must only include contractual inflows (including interest payments) from outstanding exposures that are fully performing and for which the bank has no reason to expect a default within the 30-day time horizon. Contingent inflows, including facilities obtained from a central bank or other party, must not be included in total net cash inflows."
  > — LCR40.75 ^lcr40-75

- Ngân hàng và supervisor phải giám sát mức độ tập trung của dòng vào kỳ vọng giữa các đối tác bán buôn để tránh phụ thuộc quá mức vào dòng tiền từ một số ít đối tác.
  > "Banks and supervisors should monitor the concentration of expected inflows across wholesale counterparties in the context of banks' liquidity management in order to ensure that their liquidity position is not overly dependent on the arrival of expected inflows from one or a limited number of wholesale counterparties."
  > — LCR40.76 ^lcr40-76

- Trần dòng vào là 75% tổng dòng ra, nên HQLA tối thiểu bằng 25% tổng dòng ra.
  > "the amount of inflows that can offset outflows must be capped at 75% of total expected cash outflows as calculated in the standard. This requires that a bank must maintain a minimum amount of stock of HQLA equal to 25% of the total cash outflows."
  > — LCR40.77 ^lcr40-77

- Reverse repo / securities borrowing: bảo đảm bằng Level 1 thì giả định được roll-over (inflow 0%); bằng Level 2 thì inflow bằng haircut; bằng tài sản không phải HQLA thì nhận lại 100% tiền. Khoản cho vay ký quỹ (margin loans) bảo đảm bằng non-HQLA tính tối đa 50% dòng vào.
  > "A bank must assume that maturing reverse repurchase or securities borrowing agreements secured by Level 1 assets will be rolled-over and will not give rise to any cash inflows (0%). Maturing reverse repurchase or securities lending agreements secured by Level 2 HQLA must lead to cash inflows equivalent to the relevant haircut for the specific assets. A bank is assumed not to roll over maturing reverse repurchase or securities borrowing agreements secured by non-HQLA assets, and may assume to receive back 100% of the cash related to those agreements. Collateralised loans extended to customers for the purpose of taking leveraged trading positions ("margin loans") must also be considered as a form of secured lending; however, for this scenario banks must not recognise more than 50% of contractual inflows from maturing margin loans made against non-HQLA collateral."
  > — LCR40.78 ^lcr40-78

- Ngoại lệ đối với reverse repo và vay chứng khoán: nếu tài sản bảo đảm nhận về được tái sử dụng để bù đắp các vị thế bán khống (short positions) có thể kéo dài vượt quá 30 ngày thì giả định phải tiếp tục rollover và tính inflow 0%.
  > "As an exception to LCR40.78, if the collateral obtained through reverse repo, securities borrowing, or collateral swaps, which matures within the 30-day horizon, is re-used (ie rehypothecated) and is used to cover short positions that could be extended beyond 30 days, a bank must assume that such reverse repo or securities borrowing arrangements will be rolled-over and not give rise to any cash inflows, reflecting its need to continue to cover the short position or to repurchase the relevant securities. In these cases, the short position should be treated symmetrically and not give rise to any outflows."
  > — LCR40.79 ^lcr40-79

- Vị thế bán khống của ngân hàng: nếu bù đắp bằng việc vay chứng khoán không bảo đảm thì giả định bị rút toàn bộ, dẫn đến dòng ra 100% (theo LCR40.74); nếu bù đắp bằng giao dịch tài trợ chứng khoán có bảo đảm thì duy trì trong 30 ngày và dòng ra 0%.
  > "In the case of a bank's short positions, if the short position is being covered by an unsecured security borrowing, the bank should assume the unsecured security borrowing of collateral from financial market participants would run-off in full, leading to a 100% outflow of either cash or HQLA to secure the borrowing, or cash to close out the short position by buying back the security. This must be recorded as a 100% other contractual outflow according to LCR40.74. If, however, the bank's short position is being covered by a collateralised securities financing transaction, the bank must assume the short position will be maintained throughout the 30-day period and receive a 0% outflow."
  > — LCR40.80 ^lcr40-80

- Dù có các giả định rollover, ngân hàng phải quản trị tài sản bảo đảm sao cho sẵn sàng hoàn trả khi đối tác quyết định không rollover reverse repo hoặc cho vay chứng khoán (đặc biệt đối với non-HQLA).
  > "Despite the rollover assumptions in LCR40.78 and LCR40.79, a bank should manage its collateral such that it is able to fulfil obligations to return collateral whenever the counterparty decides not to roll-over any reverse repo or securities lending transaction. This is especially the case for non-HQLA collateral, since such outflows are not captured in the LCR framework."
  > — LCR40.81 ^lcr40-81

- Hạn mức ngân hàng được cấp từ tổ chức khác: inflow 0%.
  > "Such facilities must receive a 0% inflow rate, meaning that this scenario does not consider inflows from committed credit or liquidity facilities."
  > — LCR40.82 ^lcr40-82

- Nguyên tắc xác định dòng vào theo đối tác: phản ánh nhu cầu tiếp tục cấp tín dụng hoặc gia hạn khoản vay (franchise preservation) đối với các phân khúc khách hàng, trong khi các khoản phải thu từ tổ chức tài chính được giả định thu hồi toàn bộ (trừ tiền gửi operational).
  > "For all other types of transactions, either secured or unsecured, the inflow rate must be determined by counterparty. In order to reflect the need for a bank to conduct ongoing loan origination/roll-over with different types of counterparties, even during a time of stress, a set of limits on contractual inflows by counterparty type must be applied. Regarding financial institutions, the bank may generally assume a complete return of liquidity from such institutions, provided the funds are not supporting operational activities as described in LCR40.89."
  > — LCR40.83 ^lcr40-83

- Chỉ tính khoản vay performing, và lấy ngày trả muộn nhất mà đối tác có quyền theo hợp đồng.
  > "inflows must only be taken at the latest possible date, based on the contractual rights available to counterparties."
  > — LCR40.84 ^lcr40-84

- Khoản vay không có kỳ hạn xác định bị loại khỏi dòng vào, trừ khoản thanh toán tối thiểu đến hạn trong 30 ngày.
  > "Inflows from loans that have no specific maturity (ie have non-defined or open maturity) must be excluded"
  > — LCR40.85 ^lcr40-85

- Khách bán lẻ/SME: ngân hàng được giả định tiếp tục cho vay 50%, nên inflow tính 50%.
  > "banks must assume to continue to extend loans to retail and small business customers, at a rate of 50% of contractual inflows. This results in an inflow of 50% of the contractual amount."
  > — LCR40.86 ^lcr40-86

- Wholesale: inflow 100% với tổ chức tài chính và NHTW, 50% với đối tác phi tài chính.
  > "Banks must assume to continue to extend loans to wholesale clients, at a rate of 0% of inflows for financial institutions and central banks, and 50% for all others"
  > "(1) 100% for financial institution and central bank counterparties; and (2) 50% for non-financial wholesale counterparties."
  > — LCR40.87 ^lcr40-87

- Chứng khoán đáo hạn trong 30 ngày không nằm trong HQLA: inflow 100%. Tài sản Level 1/2 đáo hạn thì tính trong HQLA, không tính là dòng vào.
  > "Inflows from securities maturing within 30 days not included in the stock of HQLA may be treated in the same category as inflows from financial institutions (ie 100% inflow)."
  > — LCR40.88 ^lcr40-88

- Tiền gửi operational ngân hàng đặt ở định chế khác: inflow 0%.
  > "they must receive a 0% inflow rate"
  > — LCR40.89 ^lcr40-89

- Tiền gửi giữ tại tổ chức trung ương của mạng lưới ngân hàng hợp tác xã: bên gửi không được tính dòng vào (inflow 0%).
  > "The same treatment applies for deposits held at the centralised institution in a cooperative banking network, that are assumed to stay at the centralised institution, as outlined in LCR40.37 to LCR40.39; in other words, the depositing bank must not count any inflow for these funds – ie they must receive a 0% inflow rate."
  > — LCR40.90 ^lcr40-90

- Dòng vào phái sinh ròng theo hợp đồng: hệ số 100% (tính theo phương pháp bù trừ song phương tại LCR40.49).
  > "The sum of all net derivative cash inflows must receive a 100% inflow factor. The amounts of derivatives cash inflows and outflows must be calculated in accordance with the methodology described in LCR40.49."
  > — LCR40.91 ^lcr40-91

- Phái sinh bảo đảm bằng HQLA: dòng vào tính ròng với các nghĩa vụ cung cấp tài sản bảo đảm theo hợp đồng (chống đếm trùng).
  > "Where derivatives are collateralised by HQLA, cash inflows must be calculated net of any corresponding cash or contractual collateral outflows that would result, all other things being equal, from contractual obligations for cash or collateral to be posted by the bank, given these contractual obligations would reduce the stock of HQLA."
  > — LCR40.92 ^lcr40-92

- Dòng vào theo hợp đồng khác do quốc gia quyết định (national discretion); loại trừ dòng vào từ doanh thu phi tài chính; các giao dịch forward repo/swaps và các giao dịch mua bán non-HQLA chưa thanh toán (unsettled) được xử lý đồng bộ.
  > "Other contractual cash inflows may be included at national discretion. Inflow percentages may be determined as appropriate for each type of inflow by supervisors in each jurisdiction. Cash inflows related to non-financial revenues are not taken into account in the calculation of the net cash outflows for the purposes of this standard."
  > — LCR40.93 ^lcr40-93

### LCR90 — Transition

- Ngưỡng tối thiểu LCR 100% có hiệu lực từ ngày 01/01/2019.
  > "The minimum Liquidity Coverage Ratio requirement of 100% is effective from 1 January 2019."
  > — LCR90.1 ^lcr90-1

- Các quốc gia đang nhận hỗ trợ tài chính cho cải cách kinh tế vĩ mô và cơ cấu có thể chọn lộ trình áp dụng riêng phù hợp với chương trình tái cấu trúc kinh tế.
  > "individual countries that are receiving financial support for macroeconomic and structural reform purposes may choose a different implementation schedule for their national banking systems, consistent with the design of their broader economic restructuring programme."
  > — LCR90.2 ^lcr90-2

### LCR99 — Application guidance

- Bảng tổng hợp các hệ số áp dụng trong LCR: Level 1 (100%), Level 2A (85%), Level 2B (RMBS 75%, khác 50%); trần 40% Level 2 và 15% Level 2B; các tỷ lệ run-off và inflow; công thức tính LCR = HQLA / Total net cash outflows, với Total net cash outflows = Total cash outflows − min [total cash inflows, 75% of gross outflows].
  > "The table below summarises the Liquidity Coverage Ratio (LCR; percentages are factors to be multiplied by the total amount of each item)."
  > "Total net cash outflows = Total cash outflows minus min [total cash inflows, 75% of gross outflows]"
  > "LCR = Stock of HQLA / Total net cash outflows"
  > — LCR99.1 ^lcr99-1

## Node bị ảnh hưởng
- Metric: [[lcr]], [[net-cash-outflows]]
- Concept: [[run-off-rate]], [[retail-deposit-stability]], [[unsecured-wholesale-funding]], [[operational-deposits]], [[secured-funding]], [[committed-facilities]], [[hqla]], [[level-1-assets]], [[level-2-assets]], [[liquidity-transfer-restrictions]], [[alternative-liquidity-approaches]]
- Regulation: [[bcbs-lcr]] · Entity: [[bcbs]]

## Mâu thuẫn ghi nhận
Không có mâu thuẫn trong phạm vi LCR20 và LCR40. Khi ingest TT50/2026 (Mục 5, PL1), cần đối chiếu run-off rate và inflow rate theo jurisdiction (xem bảng Basel vs VN trong [[lcr]]).

## Ghi chú convert
- Nhiều đoạn chứa link BIS dạng `[LCR40.16](https://…)`. Khi trích dẫn, giữ phần chữ và bỏ URL.
- Một số footnote bị cắt ngang dòng (ví dụ footnote của LCR40.7), không ảnh hưởng claim.
