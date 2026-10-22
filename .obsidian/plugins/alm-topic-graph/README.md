# ALM Neural Link Graph

Graph cục bộ cho các node trong `02_wiki/`, bố trí dạng mạng liên kết. Kích thước node tăng theo tổng số liên kết đi vào và đi ra; node domain đang chọn luôn lớn nhất. Bấm node để đọc nội dung trong khung bên cạnh, nhấp đúp để mở ghi chú.

## Mở và thao tác

- Chọn biểu tượng mạng ở ribbon hoặc chạy **Open ALM Neural Link Graph** từ command palette.
- Lọc theo domain, tìm node, kéo node để sắp xếp; kéo vùng trống để pan và cuộn để zoom.
- Chọn node để xem nội dung Markdown trong khung đọc. Khung tự cập nhật khi ghi chú thay đổi.
- Quan hệ khai báo trong frontmatter được vẽ bằng cạnh liền có hướng; wikilink trong nội dung là cạnh chấm.
- Đường kính node ghi chú chạy từ 3 đến 18 px theo bậc liên kết; node domain có đường kính tối thiểu 26 px. Liên kết phân loại domain không cộng vào bậc node ghi chú.

## Dữ liệu

- Node: ghi chú có `type` trong `02_wiki/`, loại trừ `source` và `nav`.
- Domain và loại node: frontmatter của ghi chú.
- Quan hệ: frontmatter `relations` và wikilink trong nội dung node.

Plugin không sửa nội dung ghi chú và không thay thế Graph View gốc của Obsidian.
