# Báo cáo cá nhân — Lương Đức Anh · 2A202603931

## 1. Thông tin thành viên

- Họ tên: Lương Đức Anh
- MSSV: 2A202603931
- Email: lda@ldlda.com
- Vai trong nhóm: Phụ trách chỉ số, hồ sơ launch, duyệt chéo và tổng hợp bài nộp (E).

## 2. Phần việc phụ trách

- Tính thử chỉ số chính, chỉ số dùng và chỉ số an toàn trên 1.200 yêu cầu.
- Đề xuất thêm chỉ số sử dụng và an toàn; đặc tả ít nhất 6 event có `trace_id`.
- Tổng hợp rủi ro kinh tế từ bảng độ nhạy, viết hồ sơ launch v0 và báo cáo nhóm.
- Duyệt chéo một nhóm khác khi được phân công; phần này đang chờ nhóm được chấm và bằng chứng của họ.

## 3. Đóng góp cụ thể

- Tính 5 chỉ số từ `src/logix_requests.csv`, định nghĩa 7 event và lập bảng nối event với chỉ số trong `chi_so.md`.
- Tổng hợp rủi ro làm lại (+51,8%) và xem lại (+40,7%) từ B1; đưa số liệu chi phí, chỉ số, lỗi và thiết kế pilot vào hồ sơ launch.
- Viết bản tổng hợp nhóm và ghi phần đóng góp, bằng chứng của các vai trong `TEAM.md`.

## 4. Bằng chứng

- [Đặc tả chỉ số, event và rủi ro](chi_so.md)
- [Hồ sơ launch v0](ho_so_launch_v0.md)
- [Báo cáo nhóm](group_report.md)
- [Phân công và đóng góp](../../TEAM.md)
- Các số chỉ số được đếm từ 1.200 dòng CSV bằng Python chuẩn; ví dụ chỉ số chính là 994/1.200 = 82,8%, bỏ qua gợi ý là 48/177 = 27,1%, mở lại là 51/1.200 = 4,25% (simulated).

## 5. Công cụ AI đã dùng

- Dùng ChatGPT/Codex để đọc yêu cầu và hồ sơ nhóm, tính/đối chiếu số từ CSV, soạn đặc tả event, rủi ro và bản nháp hồ sơ/báo cáo.
- Ban đầu môi trường thiếu `pandas`; sau đó đã cài `src/requirements.txt` trong `src/.venv`, chạy `python lab13.py` thành công (ba phép thử A1 đều đạt) và xác nhận `pilot_plan.yaml` đọc được bằng `yaml.safe_load`. Các chỉ số E cũng được đếm trực tiếp từ CSV bằng thư viện `csv` chuẩn để đối chiếu.

## 6. Tự đánh giá

Phần E đã có chỉ số, event, rủi ro và hồ sơ quyết định dựa trên kết quả A–D. Cần kiểm tra chéo các con số với nhóm trước khi chốt; phiếu chấm hội đồng sẽ được hoàn thành sau khi nhận phân công và hồ sơ của nhóm khác.
