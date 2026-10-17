---
title: Basel Committee on Banking Supervision (BCBS)
aliases: [BCBS, Basel Committee, Ủy ban Basel về Giám sát Ngân hàng]
type: entity
domains: [basel]
status: active
maturity: draft
sources: ["[[src-bcbs-lcr]]"]
relations: []
tags: [standard-setter]
updated: 2026-10-17
reviewed:
---

## Vai trò
Cơ quan ban hành chuẩn mực LCR trong Basel Framework [[src-bcbs-lcr]]. Bản hợp nhất trong corpus được sinh từ dữ liệu Basel Framework trên website BIS.

> [!note] Node stub
> Claim sẵn có: chưa có
> Hoàn thiện bằng: `/ingest src-bcbs-framework SCO10`
> Phát hiện: ingest src-bcbs-lcr, dùng làm điểm liên kết; mô tả vai trò và lịch sử cần nguồn chính thức (phần SCO của `src-bcbs-framework`, chưa ingest)

## Công cụ / chính sách
Các standard đã có trong wiki:
- [[bcbs-lcr]] — Liquidity Coverage Ratio

Đã register nhưng chưa ingest: NSFR (`src-bcbs-nsfr`), Leverage ratio (`src-bcbs-lev`), IRRBB 2016 (`src-bcbs-irrbb-2016`), Basel Framework đầy đủ (`src-bcbs-framework`).

## Timeline
[cần nguồn]

## Liên quan ALM
Chuẩn mực BCBS (LCR, NSFR, IRRBB) là chuẩn tham chiếu cho quy định ALM của NHNN. Mức độ nội luật hoá cụ thể cần ghi theo từng regulation VN, qua relation `implements`.
