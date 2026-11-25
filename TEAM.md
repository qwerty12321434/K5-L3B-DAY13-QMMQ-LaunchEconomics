# Team

## Thông tin nhóm

- Tên nhóm: QMMQ
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-QMMQ-LaunchEconomics`
- URL repo: [Repo nhóm trên GitHub](https://github.com/qwerty12321434/K5-L3B-DAY13-QMMQ-LaunchEconomics)
- Nhánh nộp: `main`.
- Commit đã kiểm tra: `477be2e` (sau khi merge PR #3).
- Commit nộp cuối: Chờ kết quả duyệt chéo.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |    Trần Quang Minh    |  2A202603929    |  tqminhnh04@gmail.com     |        | Chi phí và độ nhạy (A–B) |
|   2 |     Nguyễn Hải Quang   |  2A202603936    |    quangnh2004@gmail.com   | qwerty12321434 | Phân tích lỗi, gắn nhãn bộ 1 và kiểm số (C) |
|   3 |    Trần Duy Thành    |   2A202603919   |       |        | Thiết kế pilot và gắn nhãn bộ 2 (D) |
|   4 |    Lương Đức Anh    |  2A202603931   |      lda@ldlda.com |  ldlda      | Chỉ số, hồ sơ launch, duyệt chéo và nộp bài (E) |

## Phân công

| Người | Việc phụ trách | File phụ trách |
| --- | --- | --- |
| **1 · Chi phí và độ nhạy** | Viết mô hình chi phí, chạy 3 phép thử A1, tính theo 4 loại yêu cầu và cộng chi phí cố định. Chạy các kịch bản độ nhạy, so giới hạn chạy lại và tính trường hợp xem lại 100%. | [`src/lab13.py`](src/lab13.py) (A–B), [`bang_chi_phi.md`](report/team/bang_chi_phi.md) |
| **2 · Lỗi và kiểm chứng** | Gắn nhãn độc lập 20 ca (bộ 1). Tính độ đồng thuận, viết quy tắc cho ca bất đồng và lập bảng khắc phục 5 ca. Tự tính và đối chiếu các kết quả A1, A2, B3 và B4. | [`bang_loi.md`](report/team/bang_loi.md) |
| **3 · Thiết kế pilot** | Gắn nhãn độc lập 20 ca (bộ 2). Tính cỡ mẫu và hiệu ứng chia cụm, trả lời D1–D2, chọn cách chia nhóm, chốt thời lượng, viết ít nhất 3 luật dừng và kiểm tra YAML. | [`src/lab13.py`](src/lab13.py) (D1), [`pilot_plan.yaml`](report/team/pilot_plan.yaml) |
| **4 · Chỉ số và quyết định** | Tính chỉ số, đặc tả ít nhất 6 event, tổng hợp rủi ro kinh tế và hồ sơ launch v0. Ghi phiếu chấm nhóm khác, tổng hợp báo cáo nhóm và kiểm tra bản nộp. | [`chi_so.md`](report/team/chi_so.md), [`ho_so_launch_v0.md`](report/team/ho_so_launch_v0.md), [`phieu_cham.md`](report/team/phieu_cham.md), [`group_report.md`](report/team/group_report.md), [`TEAM.md`](TEAM.md) |

## Thứ tự và mốc bàn giao

1. **Bắt đầu song song.** Người 1 chạy A1 rồi tính A2–A4. Người 2 chuẩn bị bảng lỗi và tự tính số để kiểm chứng từ CSV. Người 3 tính cỡ mẫu và dựng khung YAML. Người 4 tính chỉ số, thiết kế event và dựng khung hồ sơ 7 mục.
2. **Bàn giao A–B theo từng phần.** Người 1 gửi A1–A2 cho người 2 đối chiếu ngay khi có. Khi xong B, người 1 gửi B3–B4 cho người 2 kiểm số, gửi kết quả độ nhạy cho người 3 chốt phạm vi và ngưỡng chi phí của pilot, và cho người 4 viết mục rủi ro kinh tế.
3. **Đối chiếu nhãn ở CP3.** Người 2 và 3 chốt riêng đủ 20 nhãn mỗi người trước khi trao đổi. Người 2 tính tỷ lệ đồng thuận trên hai bộ nhãn đã chốt, cùng người 3 thống nhất quy tắc cho các ca bất đồng, rồi gửi tỷ lệ đồng thuận và bảng khắc phục 5 ca cho người 4.
4. **Chốt hồ sơ trước 17:00 theo lịch lớp mẫu.** Người 3 gửi kế hoạch pilot đã kiểm tra YAML. Người 4 ghép kết quả A–D với phần E. Cả nhóm đối chiếu bằng chứng và chốt một đề xuất Go, Go có điều kiện hoặc No-go trước khi duyệt chéo.

Sau giờ giải lao, người 3 tiếp nhận lượt viết code cho D1. Người 1 phụ trách phần A–B, còn người 2 tự tính chi phí để kiểm chứng. Người 1 và 3 trao đổi trước khi ghép các phần vào `src/lab13.py`.

## Cá nhân

Mỗi thành viên tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Mỗi người ghi phần việc và cập nhật đóng góp, bằng chứng sau khi hoàn thành. Bằng chứng có thể là file, commit hoặc kết quả kiểm chứng do mình thực hiện.

### Đóng góp của các thành viên

| Họ tên | MSSV | Phần việc phụ trách | Đóng góp cụ thể | Bằng chứng |
| --- | --- | --- | --- | --- |
| Trần Quang Minh | 2A202603929 | A1–A4 và B1–B4, mô hình chi phí và phân tích độ nhạy | Dùng Codex hỗ trợ triển khai mô hình chi phí theo loại yêu cầu, tính chi phí cố định, phân tích giới hạn chạy lại và xem lại 100%. Tạo bảng từ CSV, ghi nhãn `simulated` và chạy lại code trên máy cá nhân. Ba phép thử A1 đều đạt. | [Code A–B](src/lab13.py), [bảng chi phí](report/team/bang_chi_phi.md), [báo cáo cá nhân](report/team/2A202603929_TranQuangMinh.md) |
| Nguyễn Hải Quang | 2A202603936 | Phân tích lỗi C, bộ nhãn 1 và kiểm chứng A–B | Gắn nhãn 20 ca, đối chiếu hai bộ đạt 19/20 ca trước thảo luận, lập bảng khắc phục 5 ca và kiểm chứng A1, A2, B3, B4. | [Bảng lỗi](report/team/bang_loi.md), [báo cáo cá nhân](report/team/2A202603936_NguyenHaiQuang.md) |
| Trần Duy Thành | 2A202603919 | Thiết kế pilot D và bộ nhãn 2 | Tính D1, chọn thiết kế ngẫu nhiên theo nhân viên, viết kế hoạch pilot với 3 luật dừng và gắn nhãn độc lập bộ thứ hai. | [Kế hoạch pilot](report/team/pilot_plan.yaml), [code D1](src/lab13.py), [bảng lỗi](report/team/bang_loi.md), [báo cáo cá nhân](report/team/2A202603919_TranDuyThanh.md) |
| Lương Đức Anh | 2A202603931 | Chỉ số E, hồ sơ launch, duyệt chéo và tổng hợp bài nộp | Tính thử 5 chỉ số từ 1.200 yêu cầu, đặc tả 7 event ban đầu và cách tính, tổng hợp 2 rủi ro kinh tế, hoàn thiện hồ sơ launch và báo cáo nhóm. Phiếu chấm đang chờ giảng viên phân nhóm. | [Chỉ số](report/team/chi_so.md), [hồ sơ launch](report/team/ho_so_launch_v0.md), [báo cáo nhóm](report/team/group_report.md), [báo cáo cá nhân](report/team/2A202603931_LuongDucAnh.md) |
