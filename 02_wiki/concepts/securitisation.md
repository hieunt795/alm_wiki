---
title: "Securitisation"
aliases: [Securitisation, Securitization, Chứng khoán hoá, ABS, Asset-backed securities]
type: concept
domains: [product, alm]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-choudhry-principles-banking]]"]
relations:
  - {type: exposed-to, to: "[[gap-risk]]", cite: "[[src-choudhry-principles-banking#^choudhry-sec-4]]"}
  - {type: exposed-to, to: "[[basis-risk]]", cite: "[[src-choudhry-principles-banking#^choudhry-sec-4]]"}
tags: [securitisation, abs, spv, funding, balance-sheet-capacity, credit-risk-transfer]
updated: 2026-10-19
reviewed:
---

## Ý chính
Securitisation là kỹ thuật chuyển một số loại tài sản có dòng tiền dự đoán được thành chứng khoán giao dịch được. Ngân hàng tạo chứng khoán đảm bảo bằng pool tài sản rồi bán cho nhà đầu tư tổ chức, thường thông qua một special purpose vehicle (SPV) [[src-choudhry-principles-banking#^choudhry-sec-1]].

Với ALM, securitisation là công cụ cho dung lượng bảng cân đối và chuyển giao rủi ro tín dụng, kèm giảm vốn yêu cầu nếu có [[src-choudhry-principles-banking#^choudhry-sec-2]].

## Cơ chế & drivers
**Lý do ngân hàng securitise** [[src-choudhry-principles-banking#^choudhry-sec-2]]:
- huy động vốn dài hạn từ thị trường vốn, qua đó đa dạng hoá nguồn funding;
- giải phóng dung lượng bảng cân đối bằng cách bán khoản vay cho SPV; nếu có chuyển giao rủi ro tín dụng được công nhận thì có thể giảm vốn yêu cầu.

**Cấu trúc phát hành** [[src-choudhry-principles-banking#^choudhry-sec-3]]:

| Cấu trúc | Đặc điểm | Nguồn |
|---|---|---|
| Static pool / pass-through | Pool tài sản cố định, không thay thế | [[src-choudhry-principles-banking#^choudhry-sec-3]] |
| Revolving pool / master trust | Tài sản mới đủ điều kiện có thể chuyển vào trust để thay tài sản đã trả hoặc để phát hành mới | [[src-choudhry-principles-banking#^choudhry-sec-3]] |

**Subordination.** Tranche thấp hạng (junior) bảo vệ tranche cao hạng (senior) khỏi tổn thất gốc và lãi. Theo luật EU, originator phải giữ lại 5% ABS đã phát hành [[src-choudhry-principles-banking#^choudhry-sec-5]].

## Phụ thuộc regime
[cần nguồn]

## Góc nhìn theo domain
- **ALM (rủi ro lãi suất trong cấu trúc)**: securitisation thả nổi thường được tài trợ bằng notes theo spread trên IBOR 3 tháng. Nếu tài sản gắn chỉ số khác (5 năm cố định, Bank Base Rate, Standard Variable Mortgage Rate), cấu trúc có rủi ro lãi suất cần quản lý [[src-choudhry-principles-banking#^choudhry-sec-4]]:
  - gap risk phải được phòng ngừa;
  - basis risk (ví dụ IBOR 3 tháng trên notes so với Bank Base Rate trên tài sản thế chấp) bị tổ chức xếp hạng đánh giá tiêu cực nếu không giảm thiểu bằng swap [[src-choudhry-principles-banking#^choudhry-sec-4]].

  Xem [[gap-risk]], [[basis-risk]].
- **Liquidity**: tài sản đưa vào ABS hoặc covered bond trở thành tài sản bị encumber [[src-choudhry-principles-banking#^choudhry-enc-2]]. Xem [[asset-encumbrance]].
- **Basel/VN**: [cần nguồn]

## Bằng chứng thực nghiệm
[cần nguồn]

## Câu hỏi mở
- Basel securitisation framework (CRE40–CRE45) chưa ingest [cần nguồn].
