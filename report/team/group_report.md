# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: QMMQ
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm xây hồ sơ Gate 2a cho trợ lý hoàn phí LogiX-VN từ 1.200 yêu cầu giả lập và 1.624 lần chạy. Mục tiêu là đánh giá chi phí, chất lượng và cách thiết kế một pilot có đối chứng; dữ liệu chạy thử không đủ để kết luận tác động nhân quả.

## 3. Giải pháp

Nhóm chia bốn phần: A–B mô hình chi phí và độ nhạy (`bang_chi_phi.md`); C gắn nhãn lỗi và cách khắc phục (`bang_loi.md`); D thiết kế pilot (`pilot_plan.yaml`); E chỉ số, event, rủi ro và hồ sơ quyết định (`chi_so.md`, `ho_so_launch_v0.md`).

## 4. Kết quả

Chi phí mỗi việc thành công trong phạm vi `noi_dia` + `hang_nang` là **4.599 đ** khi phân bổ chi phí cố định ở 45.000 yêu cầu/tháng [simulated]. Làm lại và xem lại là hai yếu tố nhạy nhất, lần lượt **+51,8%** và **+40,7%** khi gấp đôi [simulated]. Chạy thử có chỉ số chính **82,8%**, tỉ lệ bỏ qua gợi ý **27,1%** trong các yêu cầu được xem lại và tỉ lệ mở lại **4,25%** [simulated]. Hai bộ nhãn đồng thuận **19/20 ca (95%)**. Pilot đề xuất chia ngẫu nhiên theo nhân viên, 20 người mỗi nhánh, MDE 6 điểm phần trăm và quyết định ngày **2027-01-05**. Đề xuất cuối: **Go có điều kiện**, theo các điều kiện tại `ho_so_launch_v0.md`.

Đặc tả pilot có 9 event có `trace_id`, gồm giao dịch sổ cái để phát hiện hoàn trùng, thời gian xem lại và làm lại thực tế, và kết quả cuối để tính chi phí mỗi việc thành công.

Duyệt chéo **đang chờ giảng viên phân nhóm**. Phiếu chấm và phản hồi hội đồng sẽ được cập nhật sau buổi duyệt.

## 5. Khó khăn và cách xử lý

Phiên hỗ trợ ban đầu thiếu `pandas`; đã cài các thư viện trong `src/.venv` và chạy `python lab13.py` thành công, ba phép thử A1 đều đạt. Tệp `pilot_plan.yaml` cũng đọc được bằng `yaml.safe_load`. Trước khi nộp, một thành viên khác cần chạy lại theo checklist trên máy của nhóm và đối chiếu output với các bảng A–D.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Số phút xem lại/làm lại là simulated; mức chi phí thật có thể khác, đặc biệt khi xem lại 100% thì chi phí là **11.743–12.415 đ/việc** [simulated]. Thời gian pilot và cỡ mẫu dựa trên giả định; cách chia theo nhân viên có nguy cơ lan truyền gợi ý giữa đồng nghiệp. Chỉ số chạy thử không có nhóm đối chứng nên không chứng minh trợ lý làm tăng hiệu quả.

## 8. Tài liệu tham khảo

`docs/du_lieu_va_cong_thuc.md`; `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; tài liệu Google PAIR về lỗi và thất bại an toàn (được dẫn trong đề bài).
