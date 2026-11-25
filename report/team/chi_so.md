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
| `refund_request_received` | Hệ thống tiếp nhận | `request_id`, `trace_id`, `depot`, `staff_id`, `loai`, `arm` (pilot/đối chứng; lấy từ nhánh đã gán trước cho nhân viên) | Khi nhận yêu cầu, sau khi xác định nhân viên/nhánh và trước khi xử lý |
| `agent_run_completed` | Agent | `request_id`, `trace_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Sau mỗi lần chạy |
| `suggestion_shown` | Giao diện CSKH | `request_id`, `trace_id`, `staff_id`, `suggestion_id`, `loai` | Khi gợi ý được hiển thị cho nhân viên |
| `staff_decision_recorded` | Giao diện CSKH | `request_id`, `trace_id`, `staff_id`, `suggestion_id`, `decision` (giu/sua/bo/khong_xem), `reviewed`, `review_minutes` | Ghi một quyết định cuối cho mỗi gợi ý. Đo thời gian nhân viên thực sự xem gợi ý, trừ thời gian gián đoạn. Ghi 0 khi xác nhận không xem và để trống khi thiếu phép đo. |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `trace_id`, `refund_obligation_id` (mã khoản hoàn đã duyệt, giữ nguyên qua các yêu cầu gửi lại), `idempotency_key`, `ledger_transaction_id`, `amount_vnd`, `status` (posted/failed/duplicate_blocked) | Sau mỗi nỗ lực ghi sổ, kể cả lỗi và lượt bị chặn. Lượt ghi thành công có mã giao dịch sổ cái. |
| `refund_case_closed` | Hệ thống nghiệp vụ | `request_id`, `trace_id`, `closed_at`, `hours_to_close`, `within_24h` | Khi yêu cầu được đóng |
| `refund_case_reopened` | Hệ thống nghiệp vụ | `request_id`, `trace_id`, `reopened_at`, `within_7_days`, `reason` | Khi yêu cầu mở lại; phát trong vòng 7 ngày sau đóng |
| `refund_rework_required` | Giao diện CSKH | `request_id`, `trace_id`, `rework_id`, `reason`, `extra_minutes`, `caused_by_agent` | Khi nhân viên hoàn tất việc làm lại. Ghi thời gian thực làm lại, loại trừ thời gian đã ghi ở bước xem gợi ý. |
| `refund_case_outcome_finalized` | Hệ thống nghiệp vụ | `request_id`, `trace_id`, `outcome` (thanh_cong/lam_lai/chuyen_nhan_vien), `closed_at`, `finalized_at` | Chốt kết quả theo định nghĩa A2 sau khi theo dõi đủ 7 ngày kể từ lúc đóng và xác minh số tiền hoàn. |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: đếm yêu cầu có `refund_case_closed.within_24h` và không có `refund_case_reopened.within_7_days`, nối theo `request_id`. Mẫu số lấy từ `refund_request_received` theo nhánh và đợt nhận yêu cầu. Chỉ chốt khi đủ thời gian theo dõi các yêu cầu có thể đóng trong 24 giờ.
- Tỉ lệ bỏ qua gợi ý: số yêu cầu có quyết định `sua` hoặc `bo` / số yêu cầu đã xem lại có quyết định `giu/sua/bo`. Nếu một yêu cầu có nhiều gợi ý, dùng quyết định cuối trên gợi ý đã xem gần nhất. Tỉ lệ xem lại: số yêu cầu có `reviewed = true` / số yêu cầu đủ điều kiện trong nhánh can thiệp từ `refund_request_received`.
- Tỉ lệ mở lại: đếm `request_id` có `refund_case_reopened.within_7_days`, chia cho số yêu cầu đã có đủ thời gian theo dõi trong cùng nhánh và đợt nhận yêu cầu.
- Tỉ lệ làm lại: số yêu cầu có kết quả cuối `lam_lai` / tổng số yêu cầu trong cùng đợt đã đủ thời gian theo dõi. Dùng `refund_rework_required` để đo số phút làm lại và truy nguyên từng ca.

### Dữ liệu kiểm tra luật dừng

- **Hoàn trùng.** Với mỗi `refund_obligation_id`, đếm các `ledger_transaction_id` khác nhau ở trạng thái `posted`. Hai giao dịch đã ghi cho cùng khoản hoàn kích hoạt luật dừng ngay. Event gửi lặp có cùng mã giao dịch chỉ được tính một lần. Lượt `duplicate_blocked` được lưu để đối soát.
- **Chi phí.** Tính theo tuần nhận yêu cầu trong phạm vi pilot và chỉ đánh giá khi đợt yêu cầu đã đủ thời gian theo dõi. Cộng chi phí token và tool từ mọi lượt chạy, kể cả lượt lỗi, với chi phí nhân viên bằng `2.000 đ × (tổng review_minutes + tổng extra_minutes)`. Khử trùng lượt chạy theo `request_id` và `attempt`, thời gian xem theo `request_id` và `suggestion_id`, thời gian làm lại theo `request_id` và `rework_id`. Chia cho số yêu cầu có kết quả cuối `thanh_cong`. Dữ liệu thiếu số phút hoặc tuần chưa có ca thành công được ghi là chưa đủ để đánh giá ngưỡng.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | Nếu tiền làm lại gấp đôi, chi phí mỗi việc thành công tăng **51,8%** (từ 4.472 lên 6.787 đ/việc; simulated) | Chi phí phút làm lại trên mỗi yêu cầu và tỉ lệ `ket_qua = lam_lai`, theo tuần và loại yêu cầu | Thu hẹp phạm vi ở loại có tỉ lệ làm lại cao; chuyển ca làm lại cho nhân viên và rà soát nguyên nhân trước khi mở rộng | Chủ pilot (Người 3) |
| Nhân viên phải xem lại nhiều hơn | Nếu tiền xem lại gấp đôi, chi phí mỗi việc thành công tăng **40,7%** (từ 4.472 lên 6.292 đ/việc; simulated) | Tỉ lệ `duoc_xem_lai = 1`, tỉ lệ sửa/bỏ gợi ý, theo tuần và loại yêu cầu | Tạm dừng mở rộng; kiểm tra chất lượng gợi ý và điều chỉnh luồng trước khi tiếp tục | Vận hành CSKH (quản lý pilot) |
