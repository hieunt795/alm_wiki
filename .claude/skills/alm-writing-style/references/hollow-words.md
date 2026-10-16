# Từ sáo và từ hoa mỹ (rule T1, T4)

Mở file này khi nghi một từ đang lặp hoặc đang làm câu rỗng nghĩa. Danh sách không cố định: gặp từ sáo mới qua `/lint` hoặc `/alm-writing-style` thì bổ sung vào bảng phù hợp.

## Phạm vi đếm (T1)
- Đếm riêng từng node hoặc source note. Một lượt ingest tạo 10 node thì đếm 10 lần riêng biệt, không cộng dồn.
- Chỉ đếm trong văn do LLM viết (P1). Từ nằm trong trích nguyên văn `> "…"` không tính.
- Tối đa 3 lần mỗi từ. Từ thứ 4 trở đi phải thay bằng từ cụ thể hơn hoặc viết lại câu.

## Bảng 1 — Động từ và cụm sáo (giới hạn 3 lần/node)

| Từ sáo | Thay bằng |
|---|---|
| dẫn đến hệ quả là | do đó, vì vậy, nên |
| bộc lộ, thể hiện rõ nét | cho thấy, phản ánh; hoặc nêu thẳng số liệu |
| kích hoạt (nghĩa bóng) | làm tăng, gây ra |
| triệt tiêu, vô hiệu hoá | làm mất, loại bỏ, bù trừ |
| bào mòn | làm giảm (kèm mức giảm) |
| ép buộc | yêu cầu, buộc (kèm chủ thể theo C1) |
| thiết lập (nghĩa bóng) | đặt, quy định |
| đóng vai trò quan trọng / then chốt | nêu tác động bằng số (C3), hoặc xoá |
| tăng cường, nâng cao, củng cố | nêu đúng thay đổi: tăng tỷ lệ, bổ sung yêu cầu |
| toàn diện, mạnh mẽ, hiệu quả | xoá, hoặc nêu tiêu chí đo |

## Bảng 2 — Cụm hoa mỹ (thay ngay, không cần đếm)

| Cụm hoa mỹ | Thay bằng |
|---|---|
| đóng vai trò là, giữ vai trò là, được xem như là | là |
| nhằm mục đích, với mục tiêu | để |
| tiến hành thực hiện, thực hiện việc | làm, hoặc bỏ để dùng động từ chính |
| do việc, do bởi | vì, do |
| có thể có khả năng sẽ | có thể |
| cần lưu ý rằng, điều quan trọng là | xoá, viết thẳng nội dung |
| trong bối cảnh hiện nay | nêu mốc thời gian (R4), hoặc xoá |
| một cách đáng kể | kèm số (T3), hoặc xoá |

## Ngoại lệ
- Động từ có **nghĩa kỹ thuật chính xác** trong ALM/Basel không tính là từ sáo. Ví dụ "downgrade trigger được kích hoạt" hoặc "điều khoản collateral call được kích hoạt" là sự kiện hợp đồng, không phải nghĩa bóng.
- Cụm là **tên định danh** trong nguồn được giữ nguyên, ví dụ "significant stress", "effective deposit insurance scheme".
- "Thiết lập" khi nói về hạn mức nội bộ do ALCO đặt ("ALCO thiết lập hạn mức gap") vẫn được dùng, nhưng tính vào giới hạn đếm.
