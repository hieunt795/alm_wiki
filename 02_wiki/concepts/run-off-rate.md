---
title: Run-off rate
aliases: [Run-off rate, Run-off factor, Tỷ lệ rút vốn, Hệ số dòng tiền ra]
type: concept
domains: [alm, basel]
status: active
maturity: draft
valid_from:
valid_to:
as_of:
sources: ["[[src-bcbs-lcr]]", "[[src-tt83-2025-nhnn]]"]
relations:
  - {type: part-of, to: "[[cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: input-to, to: "[[net-cash-outflows]]", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: drives, to: "[[lcr]]", direction: "-", cite: "[[src-bcbs-lcr#^lcr40-1]]"}
  - {type: input-to, to: "[[liquidity-stress-testing]]", cite: "[[src-tt83-2025-nhnn#^d48-3]]"}
tags: [liquidity, deposit-behaviour, stress-test]
updated: 2026-10-19
reviewed:
---

## Ý chính
Run-off rate là tỷ lệ số dư một loại nợ được giả định bị rút hoặc không được tái tục trong kịch bản stress 30 ngày của [[lcr]]. Dòng ra kỳ vọng = số dư × run-off rate [[src-bcbs-lcr#^lcr40-1]]. Với cam kết ngoại bảng, tham số tương đương là drawdown rate ([[committed-facilities]]).

## Cơ chế & drivers
Basel phân biệt run-off theo bốn yếu tố:
- **Loại đối tác**: thể nhân, SME, doanh nghiệp phi tài chính, tổ chức tài chính [[src-bcbs-lcr#^lcr40-5]] [[src-bcbs-lcr#^lcr40-19]].
- **Mức bảo hiểm tiền gửi và quan hệ khách hàng**: stable hay less stable ([[retail-deposit-stability]]).
- **Mục đích nắm giữ**: operational hay non-operational ([[operational-deposits]]).
- **Tài sản bảo đảm**: với [[secured-funding]].

Bảng tham số tối thiểu:

| Nguồn vốn | Run-off | Nguồn |
|---|---|---|
| Stable retail / SME | 5% (jurisdiction có thể 3%) | [[src-bcbs-lcr#^lcr40-7]] [[src-bcbs-lcr#^lcr40-11]] |
| Less stable retail / SME | ≥ 10% | [[src-bcbs-lcr#^lcr40-13]] |
| Operational deposits | 25% | [[src-bcbs-lcr#^lcr40-26]] |
| DN phi tài chính, chính phủ, NHTW, MDB, PSE | 40% (20% nếu bảo hiểm toàn bộ) | [[src-bcbs-lcr#^lcr40-40]] [[src-bcbs-lcr#^lcr40-41]] |
| Tổ chức tài chính, pháp nhân khác | 100% | [[src-bcbs-lcr#^lcr40-42]] |
| Trái phiếu ngân hàng tự phát hành (trừ bán riêng cho bán lẻ) | 100% | [[src-bcbs-lcr#^lcr40-43]] |
| Dòng ra phái sinh ròng (có master netting) | 100% | [[src-bcbs-lcr#^lcr40-49]] |
| Kích hoạt hạ 3 bậc tín nhiệm (*Downgrade triggers*) | 100% tài sản bảo đảm / dòng tiền phát sinh | [[src-bcbs-lcr#^lcr40-51]] |
| Biến động định giá thị trường phái sinh | Dòng ký quỹ ròng 30 ngày lớn nhất trong 24 tháng | [[src-bcbs-lcr#^lcr40-56]] |

Đối trọng của run-off rate ở vế dòng tiền vào là **inflow rate** (xem chi tiết tại [[cash-inflows]]), bị khống chế bởi trần bù trừ 75% [[src-bcbs-lcr#^lcr40-77]].

## Phụ thuộc regime
Basel đặt run-off là **mức sàn**. Jurisdiction nâng lên để phản ánh hành vi người gửi tiền trong stress tại nước mình [[src-bcbs-lcr#^lcr40-6]]. Muốn áp mức 3% thì jurisdiction phải chứng minh run-off thực tế dưới 3% trong các đợt stress [[src-bcbs-lcr#^lcr40-12]]. Phải giả định mua lại trước hạn nếu thị trường kỳ vọng ngân hàng thực hiện quyền chọn call option [[src-bcbs-lcr#^lcr40-20]].

## Góc nhìn theo domain
- **Basel**: tham số chuẩn hoá để so sánh được giữa các ngân hàng. Một số tham số để national discretion và phải công bố [[src-bcbs-lcr#^lcr40-2]].
- **ALM**: *Diễn giải* — run-off rate theo LCR là giả định giám sát, khác với giả định hành vi (behavioural) dùng trong mô hình NMD nội bộ. Hai bộ giả định cần được đối chiếu nhưng không thay thế nhau. Node NMD chưa có.
- **VN**: TT83/2025 bắt buộc xét tỷ lệ rút trước hạn (run-off rate) thực tế của nợ phải trả trong thời kỳ căng thẳng gia tăng khi kiểm tra sức chịu đựng về thanh khoản [[src-tt83-2025-nhnn#^d48-3]]; Đ48 không ấn định giá trị. Xem [[liquidity-stress-testing]]. Tham số LCR theo [[tt50-2026|TT50/2026]] PL1 (Phần B. Dòng tiền ra) chưa ingest [cần nguồn].

## Câu hỏi mở
- Run-off thực tế của tiền gửi bán lẻ VN trong các giai đoạn stress (ví dụ năm 2022) so với mức sàn Basel? Cần nguồn dữ liệu.
- TT50/2026 có áp mức 3% cho stable deposits không, và Bảo hiểm tiền gửi Việt Nam có đáp ứng tiêu chí "effective deposit insurance scheme" [[src-bcbs-lcr#^lcr40-8]] không?
