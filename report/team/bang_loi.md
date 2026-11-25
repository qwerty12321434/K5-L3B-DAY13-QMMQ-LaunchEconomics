# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Hải Quang · Người gắn nhãn 2: Trần Duy Thành

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Ngữ cảnh | Do người dùng | Không | Ngữ cảnh |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận trước thảo luận:** 19 ca trùng ÷ 20 ca = **95%**, đạt ngưỡng 80%.

## Quy tắc phân biệt cho các ca không trùng

- **Ca 6 — Ngữ cảnh.** Khi mô tả đã nêu rõ hàng bị vỡ nhưng trợ lý chỉ dùng mục giao trễ để quyết định, nhóm xếp lỗi vào **Ngữ cảnh**. Nếu thông tin khách cung cấp sai và phần còn lại không đủ để xác định tình huống thật, nhóm xếp vào **Do người dùng**.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các event và ngưỡng dưới đây là đề xuất cho pilot. Ghi `trace_id` cùng các event để truy vết theo yêu cầu.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Ghi `refund_input_validation_failed` khi số tài khoản thiếu chữ số theo quy tắc của ngân hàng đã chọn. Chặn mỗi lần kiểm tra thất bại. | Giữ yêu cầu ở trạng thái chờ bổ sung. Chỉ tạo lệnh hoàn sau khi khách sửa số tài khoản và kiểm tra lại thành công. | Kỹ sư phụ trách biểu mẫu hoàn phí |
| 7 | Hệ thống | Cảnh báo ngay khi cùng một `trace_id` có thông báo hoàn thành công mà `refund_ledger_write` chưa xác nhận ghi thành công. | Chỉ báo hoàn thành công sau khi sổ cái xác nhận. Khi hết lượt thử, chuyển ca sang nhân viên với trạng thái chờ xác minh. | Kỹ sư phụ trách tích hợp sổ cái |
| 18 | Ngữ cảnh | Hằng ngày, đếm các event `ticket_reopened` có lý do hoàn thiếu và đối chiếu với số tiền đã hoàn. Rà từng ca mở lại dù tiền hoàn khớp công thức. | Tin nhắn ghi rõ phí ban đầu, tỷ lệ hoàn và số tiền thực nhận để khách kiểm tra được cách tính. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Ghi `handoff_to_staff` với lý do `outside_retention_window` cho mỗi yêu cầu có đơn quá 12 tháng. | Nói rõ giới hạn tra cứu và chuyển mã đơn, thời điểm giao cùng tóm tắt yêu cầu sang luồng xử lý thủ công. | Trưởng nhóm vận hành hoàn phí |
| 17 | Ngầm | Mỗi ngày, đối chiếu các khoản hoàn cho đơn dưới 2 kg với bảng giá có hiệu lực tại thời điểm tính phí. Cảnh báo khi có ít nhất một ca lệch tiền. | Làm mới bộ nhớ đệm khi bảng giá đổi, lưu phiên bản bảng giá vào trace, tính lại và đối soát các giao dịch bị ảnh hưởng. | Kỹ sư phụ trách dịch vụ bảng giá |
