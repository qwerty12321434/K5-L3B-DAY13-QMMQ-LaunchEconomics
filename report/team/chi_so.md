# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h` = 1 và `mo_lai_trong_7_ngay` = 0 / tổng số yêu cầu | **994/1.200 = 82,8% (simulated)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số yêu cầu được xem lại có `quyet_dinh_xem_lai` là `sua` hoặc `bo` / số yêu cầu được xem lại | **48/177 = 27,1% (simulated)** |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu có `mo_lai_trong_7_ngay` = 1 / tổng số yêu cầu | **51/1.200 = 4,25% (simulated)** |
| Dùng | Tỉ lệ yêu cầu được nhân viên xem lại | Số yêu cầu có `duoc_xem_lai` = 1 / tổng số yêu cầu | **177/1.200 = 14,8% (simulated)** |
| An toàn | Tỉ lệ yêu cầu phải làm lại | Số yêu cầu có `ket_qua` = `lam_lai` / tổng số yêu cầu | **74/1.200 = 6,2% (simulated)** |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_received` | Hệ thống tiếp nhận | `request_id`, `trace_id`, `depot`, `staff_id`, `loai`, `arm` (pilot/đối chứng) | Khi nhận yêu cầu, trước khi phân nhóm |
| `agent_run_completed` | Agent | `request_id`, `trace_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Sau mỗi lần chạy |
| `suggestion_shown` | Giao diện CSKH | `request_id`, `trace_id`, `staff_id`, `suggestion_id`, `loai` | Khi gợi ý được hiển thị cho nhân viên |
| `staff_decision_recorded` | Nhân viên CSKH | `request_id`, `trace_id`, `staff_id`, `decision` (giu/sua/bo), `reviewed` | Khi nhân viên giữ, sửa hoặc bỏ gợi ý; ghi cả trường hợp không xem lại |
| `refund_case_closed` | Hệ thống nghiệp vụ | `request_id`, `trace_id`, `closed_at`, `hours_to_close`, `within_24h` | Khi yêu cầu được đóng |
| `refund_case_reopened` | Hệ thống nghiệp vụ | `request_id`, `trace_id`, `reopened_at`, `within_7_days`, `reason` | Khi yêu cầu mở lại; phát trong vòng 7 ngày sau đóng |
| `refund_rework_required` | Nhân viên CSKH | `request_id`, `trace_id`, `reason`, `extra_minutes`, `caused_by_agent` | Khi nhân viên phải sửa hoặc làm lại câu trả lời |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_case_closed` (`within_24h`) + `refund_case_reopened` (`within_7_days`), nối theo `request_id`/`trace_id`; mẫu số lấy từ `refund_request_received`.
- Tỉ lệ bỏ qua gợi ý và tỉ lệ xem lại: `suggestion_shown` + `staff_decision_recorded`; mẫu số là số yêu cầu có gợi ý hiển thị hoặc được xem lại tương ứng.
- Tỉ lệ mở lại: `refund_case_reopened` / `refund_request_received`.
- Tỉ lệ làm lại: `refund_rework_required` / `refund_request_received`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | Nếu tiền làm lại gấp đôi, chi phí mỗi việc thành công tăng **51,8%** (từ 4.472 lên 6.787 đ/việc; simulated) | Chi phí phút làm lại trên mỗi yêu cầu và tỉ lệ `ket_qua = lam_lai`, theo tuần và loại yêu cầu | Thu hẹp phạm vi ở loại có tỉ lệ làm lại cao; chuyển ca làm lại cho nhân viên và rà soát nguyên nhân trước khi mở rộng | Chủ pilot (Người 3) |
| Nhân viên phải xem lại nhiều hơn | Nếu tiền xem lại gấp đôi, chi phí mỗi việc thành công tăng **40,7%** (từ 4.472 lên 6.292 đ/việc; simulated) | Tỉ lệ `duoc_xem_lai = 1`, tỉ lệ sửa/bỏ gợi ý, theo tuần và loại yêu cầu | Tạm dừng mở rộng; kiểm tra chất lượng gợi ý và điều chỉnh luồng trước khi tiếp tục | Vận hành CSKH (quản lý pilot) |
