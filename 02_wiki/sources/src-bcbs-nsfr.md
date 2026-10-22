---
title: "BCBS — Net Stable Funding Ratio (Basel Framework)"
aliases: []
type: source
source_id: src-bcbs-nsfr
domains: [basel, alm]
status: active
maturity: draft
tier: T2
doc_status: final
issuer: BCBS
published: 2025-12-17
effective: 2019-12-15
raw: 01_sources/alm/Basel/NSF/NSF.md
units_done: [preamble, NSF10, NSF20, NSF30, NSF99]
updated: 2026-10-16
---

## Thông tin nguồn
- Issuer: Basel Committee on Banking Supervision ([[bcbs]])
- Tier T2, `doc_status: final`. Bản consolidated do BIS website sinh ngày 17/12/2025.
- Version effective: NSF10, NSF20, NSF30 và NSF99 đều ghi *"Version effective as of 15 Dec 2019"*. NSF30 có FAQ bổ sung ngày 30/03/2023 và sửa đổi ngày 05/07/2024.
- Raw: `01_sources/alm/Basel/NSF/NSF.md` (423 dòng); meta: `NSF_meta.json`. Không có pdf gốc.
- Conversion: ok (xem `03_meta/sources.yaml`).
- Node regulation tương ứng: [[bcbs-nsfr]].

## Tóm tắt
Chuẩn mực NSFR yêu cầu ngân hàng duy trì cơ cấu nguồn vốn ổn định phù hợp với thành phần tài sản và các hoạt động ngoại bảng trong khoảng thời gian một năm.
- **NSF10** quy định các định nghĩa nền tảng (phản chiếu định nghĩa của chuẩn LCR và SRP50), định nghĩa định chế tài chính, phạm vi áp dụng hợp nhất cho các ngân hàng hoạt động quốc tế, nguyên tắc theo dõi rào cản chuyển giao thanh khoản cục bộ, và quyền quyết định quốc gia loại trừ các giao dịch phái sinh kỳ hạn $\le 6$ tháng với NHTW phục vụ điều hành tiền tệ.
- **NSF20** quy định mục tiêu hạn chế sự phụ thuộc quá mức vào nguồn vốn bán buôn ngắn hạn, định nghĩa công thức $\text{NSFR} = \frac{\text{ASF}}{\text{RSF}} \ge 100\%$ liên tục trên horizon 1 năm, và nghĩa vụ báo cáo tối thiểu hàng quý.
- **NSF30** quy định chi tiết phương pháp xác định và hiệu chuẩn các hệ số của hai cấu phần:
  - *Available Stable Funding (ASF)*: 5 tầng hệ số gồm 100% (vốn điều lệ CAP10, nợ $\ge 1$ năm), 95% (tiền gửi bán lẻ stable), 90% (tiền gửi bán lẻ less stable), 50% (nguồn vốn $< 1$ năm từ doanh nghiệp phi tài chính, operational deposits, nguồn vốn từ sovereign/PSEs, nguồn vốn 6M–1Y từ định chế tài chính/NHTW), và 0% (nguồn vốn $< 6$ tháng từ định chế tài chính/NHTW, nợ phái sinh ròng, nợ không kỳ hạn).
  - *Required Stable Funding (RSF)*: 8 tầng hệ số gồm 0% (tiền mặt, dự trữ NHTW), 5% (Level 1 unencumbered), 10% (cho vay liên ngân hàng $< 6$ tháng bảo đảm bằng Level 1 tái thế chấp được), 15% (Level 2A, cho vay liên ngân hàng $< 6$ tháng khác), 50% (Level 2B, HQLA cầm cố 6M–1Y, cho vay liên ngân hàng 6M–1Y, operational deposits tại nơi khác, các khoản cho vay khác $< 1$ năm), 65% (vay thế chấp nhà ở unencumbered $\ge 1$ năm RW $\le 35\%$), 85% (ký quỹ phái sinh initial margin, default fund CCP, cho vay $\ge 1$ năm RW $> 35\%$, cổ phiếu niêm yết, vàng), và 100% (tài sản cầm cố $\ge 1$ năm, tài sản phái sinh ròng, 5%–20% nợ phái sinh gộp, nợ xấu NPLs, tài sản cố định).
  - *Cam kết ngoại bảng*: RSF 5% đối với phần chưa rút của hạn mức tín dụng và thanh khoản cam kết.
  - *Tài sản và nợ phụ thuộc lẫn nhau (Interdependent)*: Cho phép áp đồng thời ASF 0% và RSF 0% nếu thỏa mãn 4 điều kiện nghiêm ngặt theo NSF30.35.
- **NSF99** cung cấp bảng tổng hợp toàn diện các hệ số ASF (Bảng 1), RSF (Bảng 2), cam kết ngoại bảng (Bảng 3) và hướng dẫn đối xử với các công cụ đặc thù (khoản vay bảo đảm một phần, tài sản tách biệt tài khoản ký quỹ khách hàng, và tiền gửi non-operational).

## Key claims

### Preamble

- NSFR yêu cầu ngân hàng duy trì cơ cấu nguồn vốn ổn định phù hợp với thành phần tài sản và các hoạt động ngoại bảng.
  > "The net stable funding ratio requires banks to maintain a stable funding profile in relation to the composition of their assets and off-balance-sheet activities."
  > — preamble ^nsf-preamble

### NSF10 — Definitions and applications

- Chuẩn mực NSFR bao gồm các định nghĩa và hiệu chuẩn đồng thuận quốc tế; các yếu tố thuộc quyết định quốc gia phải được quy định minh bạch và rõ ràng trong văn bản quy phạm của từng quốc gia.
  > "The net stable funding ratio (NSFR) consists primarily of internationally agreed-upon definitions and calibrations. Some elements, however, remain subject to national discretion to reflect jurisdiction-specific conditions. In these cases, national discretion should be explicit and clearly outlined in the regulations of each jurisdiction."
  > — NSF10.1 ^nsf10-1

- Trừ khi có quy định khác, các định nghĩa của NSFR phản chiếu chuẩn mực LCR và các chỉ số giám sát thanh khoản trong SRP50; các giám sát viên áp dụng định nghĩa chặt chẽ hơn trong LCR nội địa có quyền quyết định áp dụng định nghĩa chặt chẽ đó cho NSFR.
  > "Unless otherwise specified, the NSFR definitions mirror those in the liquidity coverage ratio (LCR) standard, set out in LCR, and the liquidity monitoring metrics, set out in SRP50. All references to LCR definitions in the NSFR refer to the definitions in the LCR standard published by the Basel Committee. Supervisors who have chosen to implement a more stringent definition in their domestic LCR rules than those set out in the Basel Committee LCR standard have discretion over whether to apply this stricter definition for the purposes of implementing the NSFR requirements in their jurisdiction."
  > — NSF10.2 ^nsf10-2

- Định chế tài chính trong chuẩn mực NSFR bao gồm ngân hàng, công ty chứng khoán, công ty bảo hiểm, fiduciaries và beneficiaries.
  > "banks, securities firms, insurance companies, fiduciaries … and beneficiaries … are considered as financial institutions for the application of the NSFR standard."
  > — NSF10.3 ^nsf10-3

- NSFR phải được áp dụng cho tất cả các ngân hàng hoạt động quốc tế trên cơ sở hợp nhất, và có thể mở rộng cho các ngân hàng khác để đảm bảo tính nhất quán và bình đẳng cạnh tranh.
  > "The NSFR must be applied to all internationally active banks on a consolidated basis, but may be used for other banks and on any subset of entities of internationally active banks as well to ensure greater consistency and a level playing field between domestic and cross-border banks."
  > — NSF10.4 ^nsf10-4

- Ngân hàng phải chủ động giám sát và kiểm soát rủi ro thanh khoản và nhu cầu tài trợ ở cấp độ từng pháp nhân độc lập, chi nhánh và công ty con, có tính đến các rào cản chuyển giao thanh khoản.
  > "a bank should actively monitor and control liquidity risk exposures and funding needs at the level of individual legal entities, foreign branches and subsidiaries, and the group as a whole, taking into account legal, regulatory and operational limitations to the transferability of liquidity."
  > — NSF10.5 ^nsf10-5

- Quyết định quốc gia có thể cho phép loại trừ các giao dịch phái sinh kỳ hạn ban đầu $\le 6$ tháng với NHTW phục vụ chính sách tiền tệ và thanh khoản ngắn hạn khỏi tính toán NSFR và bù trừ lãi/lỗ chưa thực hiện khỏi ASF.
  > "A limited national discretion allows derivative transactions with central banks arising from the latter's short-term monetary policy and liquidity operations to be excluded from the reporting bank's NSFR computation and to offset unrealised capital gains and losses related to these derivative transactions from available stable funding. These transactions include foreign exchange derivatives such as foreign exchange swaps, and must have a maturity of six months or less at inception."
  > — NSF10.6 ^nsf10-6

### NSF20 — Calculation and reporting

- NSFR yêu cầu duy trì cơ cấu tài trợ ổn định để giảm khả năng gián đoạn nguồn vốn làm xói mòn thanh khoản dẫn tới nguy cơ đổ vỡ ngân hàng và căng thẳng hệ thống; NSFR hạn chế sự phụ thuộc quá mức vào nguồn vốn bán buôn ngắn hạn.
  > "The net stable funding ratio (NSFR) requires banks to maintain a stable funding profile in relation to the composition of their assets and off-balance sheet activities. A sustainable funding structure is intended to reduce the likelihood that disruptions to a bank's regular sources of funding will erode its liquidity position in a way that would increase the risk of its failure and potentially lead to broader systemic stress. The NSFR limits overreliance on short-term wholesale funding, encourages better assessment of funding risk across all on- and off-balance sheet items, and promotes funding stability."
  > — NSF20.1 ^nsf20-1

- NSFR là tỷ lệ giữa lượng nguồn vốn ổn định sẵn có (ASF) so với lượng nguồn vốn ổn định cần thiết (RSF), nên đạt tối thiểu 100% một cách liên tục; ASF là phần vốn và nợ dự kiến đáng tin cậy trong horizon 1 năm.
  > "The NSFR is defined as the amount of available stable funding relative to the amount of required stable funding. This ratio should be equal to at least 100% on an ongoing basis. "Available stable funding" is defined as the portion of capital and liabilities expected to be reliable over the one-year time horizon considered by the NSFR. The amount of stable funding required ("required stable funding") of an institution is a function of the liquidity characteristics and residual maturities of the various assets held by that institution as well as those of its off-balance sheet exposures."
  > — NSF20.2 ^nsf20-2

- NSFR phải được báo cáo tối thiểu hàng quý; độ trễ báo cáo không được vượt quá độ trễ cho phép của các chuẩn mực an toàn vốn Basel.
  > "The NSFR must be reported at least quarterly. The time lag in reporting should not surpass the allowable time lag under the Basel capital standards."
  > — NSF20.3 ^nsf20-3

### NSF30 — Available and required stable funding

#### Nguyên tắc và phương pháp luận hiệu chuẩn

- Lượng ASF và RSF được hiệu chuẩn để phản ánh mức độ ổn định giả định của nợ phải trả và tính thanh khoản của tài sản.
  > "The amounts of available stable funding (ASF) and required stable funding (RSF) specified in the standard are calibrated to reflect the presumed degree of stability of liabilities and liquidity of assets."
  > — NSF30.1 ^nsf30-1

- Hiệu chuẩn tính ổn định của nguồn nợ phản ánh qua hai chiều: kỳ hạn tài trợ (kỳ hạn dài hơn được giả định ổn định hơn kỳ hạn ngắn) và loại nguồn vốn/đối tác (tiền gửi bán lẻ và SME kỳ hạn $< 1$ năm ổn định hơn về mặt hành vi so với nguồn vốn bán buôn cùng kỳ hạn).
  > "The calibration reflects the stability of liabilities across two dimensions: (1) Funding tenor: the net stable funding ratio (NSFR) is generally calibrated such that longer-term liabilities are assumed to be more stable than short-term liabilities. (2) Funding type and counterparty: the NSFR is calibrated under the assumption that short-term (maturing in less than one year) deposits provided by retail customers and funding provided by small business customers are behaviourally more stable than wholesale funding of the same maturity from other counterparties."
  > — NSF30.2 ^nsf30-2

- Bốn tiêu chí xác định RSF của tài sản bao gồm: duy trì cấp tín dụng bền bỉ cho nền kinh tế thực, giả định ngân hàng tái cấp phần lớn các khoản vay đáo hạn để bảo vệ quan hệ khách hàng, kỳ hạn tài sản, và chất lượng tài sản/giá trị thanh khoản.
  > "In determining the appropriate amounts of required stable funding for various assets, the following criteria were taken into consideration, recognising the potential trade-offs between these criteria: (1) Resilient credit creation: the NSFR requires stable funding for some proportion of lending to the real economy in order to ensure the continuity of this type of intermediation. (2) Bank behaviour: the NSFR is calibrated under the assumption that banks may seek to roll over a significant proportion of maturing loans to preserve customer relationships. (3) Asset tenor: the NSFR assumes that some short-dated assets (maturing in less than one year) require a smaller proportion of stable funding because banks would be able to allow some proportion of those assets to mature instead of rolling them over. (4) Asset quality and liquidity value: the NSFR assumes that unencumbered, high-quality assets that can be securitised or traded, and thus can be readily used as collateral to secure additional funding or sold in the market, do not need to be wholly financed with stable funding."
  > — NSF30.3 ^nsf30-3

- Nguồn vốn ổn định bổ sung cũng được yêu cầu để hỗ trợ một phần các yêu cầu thanh khoản tiềm tàng phát sinh từ các cam kết ngoại bảng và nghĩa vụ tài trợ tiềm tàng.
  > "Additional stable funding sources are also required to support at least a small portion of the potential calls on liquidity arising from off-balance sheet commitments and contingent funding obligations."
  > — NSF30.4 ^nsf30-4

#### Cấu phần nguồn vốn ổn định sẵn có (ASF)

- Lượng ASF đo lường dựa trên các đặc tính về độ ổn định tương đối của các nguồn vốn, bao gồm kỳ hạn hợp đồng và xu hướng rút vốn của các nhà cung ứng vốn khác nhau.
  > "The amount of ASF is measured based on the broad characteristics of the relative stability of an institution's funding sources, including the contractual maturity of its liabilities and the differences in the propensity of different types of funding providers to withdraw their funding."
  > — NSF30.5 ^nsf30-5

- ASF được tính bằng cách gán giá trị ghi sổ của vốn và nợ vào 5 nhóm hệ số ASF; giá trị ghi sổ là giá trị trước khi áp dụng các khoản khấu trừ hoặc điều chỉnh theo quy định giám sát.
  > "The amount of ASF must be calculated by first assigning the carrying value of an institution's capital and liabilities to one of five categories as presented below. The amount assigned to each category is then multiplied by an ASF factor, and the total ASF is the sum of the weighted amounts. Carrying value represents the amount at which a liability or equity instrument is recorded before the application of any regulatory deductions, filters or other adjustments."
  > — NSF30.6 ^nsf30-6

- Khi xác định kỳ hạn nợ hoặc vốn có quyền chọn mua lại (call options), ngân hàng phải giả định nhà đầu tư thực hiện quyền chọn ở ngày sớm nhất có thể; nếu thị trường kỳ vọng nợ được mua lại trước hạn pháp lý thì ngân hàng phải tính theo hành vi đó.
  > "When determining the maturity of an equity or liability instrument, the bank must assume investors redeem call options at the earliest possible date."
  > "In particular, where the market expects certain liabilities to be redeemed before their legal final maturity date, banks and supervisors should assume such behaviour for the purpose of the NSFR and include these liabilities in the corresponding ASF category."
  > — NSF30.7 ^nsf30-7

- Nợ phái sinh được tính toán dựa trên chi phí thay thế (replacement cost) khi hợp đồng có giá trị âm; khi có thỏa thuận bù trừ song phương đủ điều kiện theo CRE52.7, chi phí thay thế là chi phí thay thế ròng.
  > "Derivative liabilities are calculated first based on the replacement cost for derivative contracts (obtained by marking to market) where the contract has a negative value. When an eligible bilateral netting contract is in place that meets the conditions as specified in CRE52.7, the replacement cost for the set of derivative exposures covered by the contract must be the net replacement cost."
  > — NSF30.8 ^nsf30-8

- Khi tính nợ phái sinh NSFR, tài sản bảo đảm đã đặt cọc dưới dạng variation margin liên quan đến hợp đồng phái sinh phải được khấu trừ khỏi giá trị chi phí thay thế âm.
  > "In calculating NSFR derivative liabilities, collateral posted in the form of variation margin in connection with derivative contracts, regardless of the asset type, must be deducted from the negative replacement cost amount."
  > — NSF30.9 ^nsf30-9

- Các khoản nợ và công cụ vốn nhận hệ số ASF 100% bao gồm: vốn điều lệ quy định CAP10 (loại trừ phần công cụ Tier 2 có kỳ hạn còn lại $< 1$ năm); các công cụ vốn khác có kỳ hạn còn lại $\ge 1$ năm (loại trừ công cụ có quyền chọn rút ngắn kỳ hạn $< 1$ năm); các khoản vay và nợ có kỳ hạn còn lại $\ge 1$ năm (dòng tiền đáo hạn $< 1$ năm không được nhận 100%); và tiền gửi bán lẻ có kỳ hạn $\ge 1$ năm có điều khoản phạt nặng nếu rút sớm.
  > "Liabilities and capital instruments receiving a 100% ASF factor comprise: (1) the total amount of regulatory capital, before the application of capital deductions, as defined in CAP10, excluding the proportion of Tier 2 instruments with residual maturity of less than one year; (2) the total amount of any capital instrument not included in NSF30.10(1) that has an effective residual maturity of one year or more, but excluding any instruments with explicit or embedded options that, if exercised, would reduce the expected maturity to less than one year; (3) the total amount of secured and unsecured borrowings and liabilities (including term deposits) with effective residual maturities of one year or more. Cash flows falling below the one-year horizon but arising from liabilities with a final maturity greater than one year do not qualify for the 100% ASF factor; and (4) retail term deposits maturing over one year that cannot be withdrawn early without significant penalty."
  > — NSF30.10 ^nsf30-10

- Nợ nhận hệ số ASF 95% bao gồm tiền gửi không kỳ hạn và có kỳ hạn $< 1$ năm (hoặc $> 1$ năm rút được không bị phạt nặng) thuộc nhóm "stable" của khách hàng bán lẻ và doanh nghiệp nhỏ.
  > "Liabilities receiving a 95% ASF factor comprise "stable" (as defined in LCR40.7 to LCR40.12) non-maturity (demand) deposits and/or term deposits with residual maturities of less than one year,and/or term deposits with residual maturities greater than one year that can be withdrawn early without a significant penalty, provided by retail and small business customers."
  > — NSF30.11 ^nsf30-11

- Nợ nhận hệ số ASF 90% bao gồm tiền gửi không kỳ hạn và có kỳ hạn $< 1$ năm (hoặc $> 1$ năm rút được không bị phạt nặng) thuộc nhóm "less stable" của khách hàng bán lẻ và doanh nghiệp nhỏ.
  > "Liabilities receiving a 90% ASF factor comprise "less stable" (as defined in LCR40.13 to LCR40.15) non-maturity (demand) deposits and/or term deposits with residual maturities of less than one year, and/or term deposits with residual maturities greater than one year that can be withdrawn early without a significant penalty, provided by retail and small business customers."
  > — NSF30.12 ^nsf30-12

- Nợ nhận hệ số ASF 50% bao gồm: nguồn vốn kỳ hạn $< 1$ năm từ khách hàng doanh nghiệp phi tài chính; tiền gửi vận hành (operational deposits theo LCR40.26–36); nguồn vốn kỳ hạn $< 1$ năm từ chính phủ, PSE, MDB và ngân hàng phát triển quốc gia; và nguồn vốn kỳ hạn từ 6 tháng đến dưới 1 năm từ NHTW và định chế tài chính.
  > "Liabilities receiving a 50% ASF factor comprise: (1) funding (secured and unsecured) with a residual maturity of less than one year provided by non-financial corporate customers; (2) operational deposits (as defined in LCR40.26 to LCR40.36); (3) funding with residual maturity of less than one year from sovereigns, public sector entities (PSEs), and multilateral and national development banks; and (4) other funding (secured and unsecured) not included in the categories above with residual maturity between six months to less than one year, including funding from central banks and financial institutions."
  > — NSF30.13 ^nsf30-13

- Nợ nhận hệ số ASF 0% bao gồm: nguồn vốn kỳ hạn $< 6$ tháng từ NHTW và định chế tài chính; nợ không kỳ hạn xác định (vị thế bán khống short positions, trừ thuế hoãn lại và lợi ích cổ đông thiểu số); chênh lệch ròng nợ phái sinh NSFR lớn hơn tài sản phái sinh NSFR; và các khoản phải trả ngày giao dịch (trade date payables).
  > "Liabilities receiving a 0% ASF factor comprise: (1) all other liabilities and equity categories not included in the above categories, including other funding with residual maturity of less than six months from central banks and financial institutions; (2) other liabilities without a stated maturity. This category must include short positions and open maturity positions that are not otherwise captured under NSF30.10 to NSF30.13."
  > "(3) NSFR derivative liabilities as calculated according to NSF30.8 and NSF30.9 net of NSFR derivative assets as calculated according to NSF30.23 and NSF30.24, if NSFR derivative liabilities are greater than NSFR derivative assets"
  > "(4) "trade date" payables arising from purchases of financial instruments, foreign currencies and commodities"
  > — NSF30.14 ^nsf30-14

#### Cấu phần nguồn vốn ổn định cần thiết (RSF)

- Lượng RSF đo lường hồ sơ rủi ro thanh khoản của tài sản và ngoại bảng, tính bằng giá trị ghi sổ của tài sản nhân hệ số RSF tương ứng cộng với các cam kết ngoại bảng nhân hệ số RSF; sử dụng trọng số rủi ro của phương pháp Chuẩn hóa (CRE20).
  > "The amount of RSF is measured based on the broad characteristics of the liquidity risk profile of an institution's assets and off-balance-sheet exposures. The amount of RSF is calculated by first assigning the carrying value of an institution's assets to the categories listed below. The carrying value of an asset item should generally be recorded by following its accounting value, ie net of specific provisions, in line with CRE20.1 and the requirements for on-balance sheet, non-derivative assets in LEV30. The amount assigned to each category is then multiplied by its associated RSF factor, and the total RSF is the sum of the weighted amounts added to the amount of off-balance-sheet activity (or potential liquidity exposure) multiplied by its associated RSF factor."
  > "Regardless of whether a bank uses the internal ratings-based (IRB) approach, the standardised approach risk weights in CRE20 must be used to determine the NSFR treatment."
  > — NSF30.15 ^nsf30-15

- Đối với tài sản có quyền chọn gia hạn kỳ hạn, ngân hàng phải giả định nhà đầu tư thực hiện quyền chọn gia hạn.
  > "When determining the maturity of an instrument, the bank must assume investors exercise any option to extend maturity."
  > — NSF30.17 ^nsf30-17

- Tài sản bị cầm cố (encumbered assets) trong thời gian từ 1 năm trở lên phải chịu hệ số RSF 100%; tài sản HQLA bị cầm cố từ 6 tháng đến dưới 1 năm chịu hệ số RSF 50%; tài sản cầm cố dưới 6 tháng chịu hệ số RSF như tài sản unencumbered.
  > "Assets on the balance sheet that are encumbered … for one year or more must receive a 100% RSF factor. Assets encumbered for a period of between six months and less than one year that would, if unencumbered, receive an RSF factor lower than or equal to 50% must receive a 50% RSF factor."
  > — NSF30.20 ^nsf30-20

- Đối với các thỏa thuận tài trợ có bảo đảm (repo, reverse repo), ngân hàng loại khỏi tài sản các chứng khoán đi vay không có quyền sở hữu hưởng lợi (beneficial ownership); các chứng khoán cho vay mà ngân hàng giữ quyền sở hữu hưởng lợi vẫn phải nằm trên bảng cân đối và chịu hệ số RSF tương ứng.
  > "For secured funding arrangements, use of balance sheet and accounting treatments should generally result in banks excluding, from their assets, securities which they have borrowed in securities financing transactions (such as reverse repos and collateral swaps) where they do not have beneficial ownership. In contrast, banks must include securities they have lent in securities financing transactions where they retain beneficial ownership."
  > — NSF30.21 ^nsf30-21

- Các khoản phải thu và phải trả từ giao dịch tài trợ chứng khoán phải được báo cáo trên cơ sở gộp (gross basis), chỉ được bù trừ ròng với cùng một đối tác nếu thỏa mãn điều kiện netting theo LEV30.
  > "Amounts receivable and payable under these securities financing transactions should generally be reported on a gross basis, meaning that the gross amount of such receivables and payables should be reported on the RSF side and ASF side, respectively. The only exception is that securities financing transactions with a single counterparty may be measured on a net basis when calculating the NSFR, provided that the netting conditions for securities financing transactions set out in LEV30 are met."
  > — NSF30.22 ^nsf30-22

- Tài sản phái sinh tính theo chi phí thay thế dương; khi có thỏa thuận bù trừ song phương đủ điều kiện, chi phí thay thế là chi phí thay thế ròng.
  > "Derivative assets are calculated first based on the replacement cost for derivative contracts (obtained by marking to market) where the contract has a positive value. When an eligible bilateral netting contract is in place that meets the conditions as specified in CRE52.7, the replacement cost for the set of derivative exposures covered by the contract must be the net replacement cost."
  > — NSF30.23 ^nsf30-23

- Tài sản bảo đảm nhận về liên quan đến hợp đồng phái sinh không được bù trừ chi phí thay thế dương, trừ khi nhận dưới dạng variation margin bằng tiền mặt thỏa mãn điều kiện LEV30; phần variation margin nhận về không đủ tiêu chuẩn hoặc initial margin nhận về được gán hệ số ASF 0%.
  > "In calculating NSFR derivative assets, collateral received in connection with derivative contracts must not offset the positive replacement cost amount, regardless of whether or not netting is permitted under the bank's operative accounting or risk-based framework, unless it is received in the form of cash variation margin and meets the conditions as specified in LEV30 for the cash portion of variation margin exchanged between counterparties to be viewed as a form of pre-settlement payment."
  > — NSF30.24 ^nsf30-24

- Tài sản nhận hệ số RSF 0% bao gồm: tiền mặt, tiền xu immediately available; toàn bộ dự trữ tại NHTW (cả bắt buộc và vượt mức); các khoản khiếu nại đối với NHTW có kỳ hạn còn lại $< 6$ tháng; và các khoản phải thu ngày giao dịch (trade date receivables).
  > "Assets assigned a 0% RSF factor comprise … coins and banknotes immediately available to meet obligations"
  > — NSF30.25 ^nsf30-25

- Tài sản nhận hệ số RSF 5% bao gồm tài sản Level 1 unencumbered theo định nghĩa LCR30.41 (trừ tài sản nhận 0% RSF), gồm chứng khoán thị trường 0% RW của sovereign, central bank, PSEs, BIS, IMF, ECB, EC, MDBs và nợ công phát hành bằng ngoại tệ.
  > "Assets assigned a 5% RSF factor comprise unencumbered Level 1 assets as defined in LCR30.41, excluding assets receiving a 0% RSF as specified above, and including: (1) marketable securities representing claims on or guaranteed by sovereigns, central banks, PSEs, the Bank for International Settlements, the International Monetary Fund, the European Central Bank and the European Community, or multilateral development banks that are assigned a 0% risk weight under CRE20; and (2) certain non-0% risk-weighted sovereign or central bank debt securities"
  > — NSF30.26 ^nsf30-26

- Tài sản nhận hệ số RSF 10% bao gồm các khoản cho vay unencumbered đối với định chế tài chính có kỳ hạn còn lại $< 6$ tháng được bảo đảm bằng tài sản Level 1 mà ngân hàng có quyền tự do tái thế chấp.
  > "Assets assigned a 10% RSF factor comprise unencumbered loans to financial institutions with residual maturities of less than six months, where the loan is secured against Level 1 assets as defined in LCR30.41, and where the bank has the ability to freely rehypothecate the received collateral for the life of the loan."
  > — NSF30.27 ^nsf30-27

- Tài sản nhận hệ số RSF 15% bao gồm tài sản Level 2A unencumbered (chứng khoán 20% RW và trái phiếu doanh nghiệp/covered bond AA- trở lên); và tất cả các khoản cho vay unencumbered khác đối với định chế tài chính có kỳ hạn còn lại $< 6$ tháng.
  > "Assets assigned a 15% RSF factor comprise: (1) unencumbered Level 2A assets as defined in LCR30.43, including: (a) marketable securities representing claims on or guaranteed by sovereigns, central banks, PSEs or multilateral development banks that are assigned a 20% risk weight under CRE20; and (b) corporate debt securities (including commercial paper) and covered bonds with a credit rating equal or equivalent to at least AA–; (2) all other unencumbered loans to financial institutions with residual maturities of less than six months not included in NSF30.27."
  > — NSF30.28 ^nsf30-28

- Tài sản nhận hệ số RSF 50% bao gồm: tài sản Level 2B unencumbered (RMBS AA, trái phiếu DN A+ đến BBB-, cổ phiếu lớn không do định chế tài chính phát hành); HQLA bị cầm cố từ 6 tháng đến dưới 1 năm; cho vay định chế tài chính và NHTW kỳ hạn 6 tháng đến dưới 1 năm; tiền gửi operational gửi tại định chế tài chính khác; và các tài sản non-HQLA khác có kỳ hạn $< 1$ năm (cho vay doanh nghiệp, bán lẻ, SME, sovereign).
  > "Assets assigned a 50% RSF factor comprise: (1) unencumbered Level 2B assets as defined and subject to the conditions set forth in LCR30.45, including: (a) residential mortgage-backed securities with a credit rating of at least AA; (b) corporate debt securities (including commercial paper) with a credit rating of between A+ and BBB–; and (c) exchange-traded common equity shares not issued by financial institutions or their affiliates; (2) any HQLA as defined in the LCR that are encumbered for a period of between six months and less than one year; (3) all loans to financial institutions and central banks with residual maturity of between six months and less than one year; (4) deposits held at other financial institutions for operational purposes, as outlined in LCR40.26 to LCR40.36, that are subject to the 50% ASF factor in NSF30.13(2); and (5) all other non-HQLA not included in the above categories that have a residual maturity of less than one year, for example, loans to non-financial corporate clients, loans to retail customers (ie natural persons) and small business customers, and loans to sovereigns, national development banks and PSEs."
  > — NSF30.29 ^nsf30-29

- Tài sản nhận hệ số RSF 65% bao gồm: cho vay thế chấp nhà ở unencumbered có kỳ hạn còn lại $\ge 1$ năm có RW $\le 35\%$; và các khoản cho vay unencumbered khác $\ge 1$ năm có RW $\le 35\%$ (ngoại trừ cho vay định chế tài chính).
  > "Assets assigned a 65% RSF factor comprise: (1) unencumbered residential mortgages with a residual maturity of one year or more that would qualify for a 35% or lower risk weight under CRE20; and (2) other unencumbered loans, including loans to sovereigns, multilateral development banks, PSEs and national development banks, not included in the above categories, excluding loans to financial institutions, with a residual maturity of one year or more that would qualify for a 35% or lower risk weight under CRE20."
  > — NSF30.30 ^nsf30-30

- Tài sản nhận hệ số RSF 85% bao gồm: tiền mặt hoặc tài sản ký quỹ ban đầu (initial margin) cho hợp đồng phái sinh và đóng góp vào quỹ dự phòng vỡ nợ của CCP; các khoản cho vay unencumbered $\ge 1$ năm có RW $> 35\%$ (trừ định chế tài chính); chứng khoán không phải HQLA $\ge 1$ năm và cổ phiếu niêm yết sàn giao dịch; hàng hóa giao dịch thực thể gồm vàng.
  > "Assets assigned an 85% RSF factor comprise: (1) cash, securities or other assets posted as initial margin for derivative contracts and cash or other assets provided to contribute to the default fund of a central counterparty (CCP), in both cases regardless of whether recorded on or off the balance sheet."
  > "(2) other unencumbered performing loans that do not qualify for the 35% or lower risk weight under CRE20 and have residual maturities of one year or more, excluding loans to financial institutions; (3) unencumbered securities with a remaining maturity of one year or more and exchange-traded equities, that are not in default and do not qualify as HQLA according to the LCR standard; and (4) physical traded commodities, including gold."
  > — NSF30.31 ^nsf30-31

- Tài sản nhận hệ số RSF 100% bao gồm: toàn bộ tài sản bị cầm cố $\ge 1$ năm; chênh lệch ròng tài sản phái sinh NSFR lớn hơn nợ phái sinh NSFR; tài sản không có kỳ hạn xác định; nợ xấu (NPLs); cho vay định chế tài chính kỳ hạn $\ge 1$ năm; cổ phiếu chưa niêm yết; tài sản cố định; và từ 5% đến 20% (theo quyết định quốc gia) tổng nợ phái sinh gộp (trước khi trừ variation margin đặt cọc).
  > "Assets assigned a 100% RSF factor comprise: (1) all assets that are encumbered for a period of one year or more; (2) NSFR derivative assets as calculated according to NSF30.23 and NSF30.24 net of NSFR derivative liabilities as calculated according to NSF30.8 and NSF30.9, if NSFR derivative assets are greater than NSFR derivative liabilities; (3) assets without a stated maturity not included in NSF30.32(1) and NSF30.32(2) (including non-maturity reverse repos unless banks can demonstrate to supervisors that the non-maturity reverse repo would effectively mature in less than one year); (4) all other assets not included in the above categories, including non-performing loans, loans to financial institutions with a residual maturity of one year or more, non-exchange-traded equities, fixed assets, items deducted from regulatory capital, retained interest, insurance assets, subsidiary interests and defaulted securities; and (5) 5% to 20% (depending on national discretion) of all derivative liabilities (ie negative replacement cost amounts) as calculated according to NSF30.8 to NSF30.9 (before deducting variation margin posted)."
  > — NSF30.32 ^nsf30-32

- Đối với ngoại bảng, hạn mức cam kết tín dụng và thanh khoản không thể hủy ngang hoặc chỉ có thể hủy ngang có điều kiện (irrevocable / conditionally revocable credit and liquidity facilities) chịu hệ số RSF 5% trên phần hạn mức chưa rút.
  > "Irrevocable and conditionally revocable credit and liquidity facilities to any client"
  > "5% of the currently undrawn portion"
  > — NSF30.34 ^nsf30-34

- Cơ chế xử lý tài sản và nợ phụ thuộc lẫn nhau (interdependent assets and liabilities): giám sát viên có quyền quyết định áp dụng hệ số ASF 0% và RSF 0% nếu thỏa mãn đồng thời 4 điều kiện: xác định rõ ràng cặp tài sản nợ, kỳ hạn và giá trị gốc khớp nhau, ngân hàng đóng vai trò đơn thuần là đơn vị chuyển giao vốn (pass-through unit), và đối tác hai bên không phải là một.
  > "National supervisors have discretion in limited circumstances to determine whether certain asset and liability items, on the basis of contractual arrangements, are interdependent such that the liability cannot fall due while the asset remains on the balance sheet, the principal payment flows from the asset cannot be used for something other than repaying the liability, and the liability cannot be used to fund other assets. For interdependent items, supervisors may adjust RSF and ASF factors so that they are both 0%, subject to the following criteria: (1) The individual interdependent asset and liability items must be clearly identifiable. (2) The maturity and principal amount of both the liability and its interdependent asset must be the same. (3) The bank is acting solely as a pass-through unit to channel the funding received (the interdependent liability) into the corresponding interdependent asset. (4) The counterparties for each pair of interdependent liabilities and assets must not be the same."
  > — NSF30.35 ^nsf30-35

- Trước khi quyết định cho phép áp dụng cơ chế interdependent, cơ quan giám sát nên cân nhắc liệu có tạo ra các khuyến khích lệch lạc hoặc hệ quả ngoài ý muốn hay không.
  > "Before exercising this discretion, supervisors should consider whether perverse incentives or unintended consequences are being created."
  > — NSF30.36 ^nsf30-36

- Các trường hợp thực hiện quyền quyết định áp dụng cơ chế interdependent phải minh bạch, cụ thể và được công bố rõ ràng trong quy định của từng quốc gia.
  > "The instances where supervisors will exercise the discretion to apply this exceptional treatment should be transparent, explicit and clearly outlined in the regulations of each jurisdiction, to provide clarity both within the jurisdiction and internationally."
  > — NSF30.37 ^nsf30-37

### NSF99 — Definitions and applications / Summary tables

- Bảng tổng hợp các hệ số ASF: 100%, 95%, 90%, 50%, 0%.
  > "Table 1 below summarises the components of each of the available stable funding (ASF) categories and the associated maximum ASF factor to be applied in calculating an institution's total amount of available stable funding under the standard."
  > — NSF99.1 ^nsf99-1

- Bảng tổng hợp các hệ số RSF: 0%, 5%, 10%, 15%, 50%, 65%, 85%, 100%.
  > "Table 2 summarises the specific types of assets to be assigned to each asset category and their associated required stable funding (RSF) factor."
  > — NSF99.2 ^nsf99-2

- Bảng tổng hợp các hệ số ngoại bảng: RSF 5% cho hạn mức tín dụng/thanh khoản cam kết.
  > "Table 3 identifies the specific types of off-balance sheet exposures to be assigned to each off-balance sheet category and their associated RSF factor."
  > — NSF99.3 ^nsf99-3

- Khoản vay có bảo đảm một phần phải được tách thành phần có bảo đảm và không bảo đảm để áp hệ số RSF tương ứng; nếu không thể phân tách thì phải áp hệ số RSF cao hơn cho toàn bộ khoản vay.
  > "Some loans are only partially secured and are therefore separated into secured and unsecured portions with different risk weights under the Basel capital framework. The specific characteristics of these portions of loans should be taken into account for the calculation of the NSFR: the secured and unsecured portions of a loan should each be treated according to its characteristics and assigned the corresponding RSF factor. If it is not possible to draw the distinction between the secured and unsecured part of the loan, the higher RSF factor must be applied to the whole loan."
  > — NSF99.4 ^nsf99-4

- Tài sản tách biệt để bảo vệ vốn khách hàng trong tài khoản giao dịch ký quỹ phải được báo cáo theo tài sản cơ sở và xét theo thời gian bị cầm cố.
  > "Assets that are owned by banks, but segregated to satisfy statutory requirements for the protection of customer equity in margined trading accounts, must be reported in accordance with the underlying exposure, whether or not the segregation requirement is separately classified on a bank's balance sheet. However, those assets must also be treated according to NSF30.20. That is, they may be subject to a higher RSF depending on (the term of) encumbrance."
  > — NSF99.5 ^nsf99-5

- Tiền gửi non-operational tại các tổ chức tài chính khác phải được đối xử tương đương như cho vay tổ chức tài chính có tính đến kỳ hạn của tiền gửi.
  > "Non-operational deposits held at other financial institutions must be treated equivalently to loans to financial institutions, taking into account the term of the deposit."
  > — NSF99.6 ^nsf99-6

## Node bị ảnh hưởng
- [[nsfr]]
- [[available-stable-funding]]
- [[required-stable-funding]]
- [[interdependent-assets-and-liabilities]]
- [[asf-capital-and-long-term-liabilities]]
- [[asf-retail-and-small-business-deposits]]
- [[asf-wholesale-and-operational-funding]]
- [[rsf-hqla-and-central-bank-reserves]]
- [[rsf-loans-and-credit-exposures]]
- [[rsf-securities-financing-and-encumbrance]]
- [[rsf-derivatives-and-off-balance-sheet]]
- [[bcbs-nsfr]]
- [[lcr]]
- [[hqla]]

## Mâu thuẫn ghi nhận
- Không có

## Ghi chú convert
- Conversion ok, không phát hiện lỗi bảng hoặc công thức.
