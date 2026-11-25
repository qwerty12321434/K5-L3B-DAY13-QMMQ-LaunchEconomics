# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: QMMQ · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Phạm vi `noi_dia` + `hang_nang`: **4.599 đ/việc** gồm chi phí cố định ở 45.000 yêu cầu/tháng; **0,38×** mức nhân viên 12.000 đ [simulated] | Giả lập | Chủ chi phí (Người 1) |
| 2 · Ba yếu tố nhạy nhất | Làm lại **+51,8%**; xem lại **+40,7%**; lương **+23,1%** khi tăng theo kịch bản B1 [simulated] | Giả lập | Chủ chi phí (Người 1) |
| 3 · So với nhân viên tự làm | Giới hạn 2 lần có chi phí cả hệ thống thấp nhất: **6.901.220 đ/1.200 yêu cầu**, so với 14.400.000 đ nếu nhân viên tự xử lý cả 1.200 yêu cầu [simulated] | Giả lập | Chủ chi phí (Người 1) |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính **82,8%**; bỏ qua gợi ý **27,1%** trong 177 ca được xem lại; mở lại trong 7 ngày **4,25%**. Chạy thử không có đối chứng, không suy ra tác động nhân quả [simulated] | Giả lập | Chủ chỉ số (Người 4) |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận **19/20 = 95%**; có cách khắc phục cho 5 loại lỗi | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Phân nhóm ngẫu nhiên theo nhân viên **20/nhánh**; MDE **6 điểm %**, **859** yêu cầu hiệu dụng/nhánh; phạm vi `noi_dia` + `hang_nang`; quyết định **2027-01-05** | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100%: **11.743–12.415 đ/việc** tùy phút làm lại giả định; vượt mốc nhân viên ở 12.415 đ [simulated] | Giả lập | Chủ pilot |

Điều kiện: trước **2026-12-01**, Giám đốc vận hành chốt phân nhóm, event và ngưỡng đo; giữ pilot ở `noi_dia` + `hang_nang`; áp dụng luật dừng an toàn, chi phí (**>8.000 đ/việc trong 2 tuần**) và mức sửa/bỏ gợi ý (**>40% trong 1 tuần**) theo `pilot_plan.yaml`. Không mở rộng nếu thiếu mẫu hoặc chưa theo dõi đủ 7 ngày.

**Đề xuất: Go có điều kiện.**
