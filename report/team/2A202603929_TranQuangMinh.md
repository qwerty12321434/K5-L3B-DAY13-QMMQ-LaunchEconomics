# Báo cáo cá nhân — TranQuangMinh — 2A202603929

## 1. Thông tin thành viên

- Họ tên: TranQuangMinh
- MSSV: 2A202603929
- Email: tqminhhn04@gmail.com
- GitHub: [MinhTrannnnn](https://github.com/MinhTrannnnn)
- Vai trong nhóm: Người viết code, phụ trách mô hình chi phí và phân tích độ nhạy (nhiệm vụ A–B).

## 2. Phần việc phụ trách

- A1: Các hàm tính số lần chạy kỳ vọng, xác suất thành công và hệ số chi phí mỗi việc thành công.
- A2–A3: Mô hình chi phí từ trace và phân tích theo bốn loại yêu cầu.
- A4: Phân bổ chi phí cố định 40 triệu đồng/tháng cho phạm vi `noi_dia` + `hang_nang`.
- B1–B2: Chín kịch bản độ nhạy, kịch bản thay đổi hai yếu tố và xếp hạng tác động.
- B3–B4: So sánh giới hạn chạy lại theo chi phí toàn hệ thống; đánh giá phương án xem lại 100%.

## 3. Đóng góp cụ thể

Phụ trách phần A–B của nhóm, sử dụng Codex hỗ trợ triển khai `src/lab13.py` và tạo `bang_chi_phi.md` từ kết quả chạy trên hai CSV của lab. Code lọc trace theo `request_id`, cộng chi phí mọi lần chạy kể cả lỗi và chỉ đếm yêu cầu có `ket_qua == 'thanh_cong'` ở mẫu số.

Phần độ nhạy dùng lại `mo_hinh` với tham số giá và hệ số thay đổi. Khi giới hạn số lần chạy, các yêu cầu vượt giới hạn được chuyển sang nhân viên và đặt phút xem lại/làm lại bằng 0 theo hướng dẫn lab; chi phí toàn hệ thống cộng thêm 12.000 đồng cho mỗi yêu cầu không thành công.

Báo cáo phân biệt chi phí mỗi việc thành công với chi phí toàn hệ thống trên mỗi yêu cầu; ghi nhãn `simulated` cho các số sử dụng phút giả lập. Phần B4 trình bày cả giả định 9 phút làm lại/ca và trung bình tính từ CSV để thể hiện rủi ro chi phí nhân viên.

## 4. Bằng chứng

- Code: [src/lab13.py](../../src/lab13.py), gồm các hàm A1, `mo_hinh` và `bao_cao_ab`.
- Bảng kết quả và giải thích: [bang_chi_phi.md](bang_chi_phi.md), các mục A1–A4 và B1–B4.
- Ba phép thử A1: **1,20 · 1,25 · 1,25**, đều đạt.
- A2: Tổng chi phí **4.373.585 đồng**, **978 việc thành công**, chi phí **4.472 đồng/việc thành công**, gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu [simulated].
- B2: Ba yếu tố ảnh hưởng mạnh nhất theo các kịch bản đã thử là **làm lại (+51,8%)**, **xem lại (+40,7%)**, **lương (+23,1%)** [simulated].
- B3: Giới hạn **2 lần chạy** có chi phí hệ thống thấp nhất, **6.901.220 đồng**; giới hạn **1 lần** có chi phí mỗi việc thành công thấp nhất, **4.111 đồng**, nhưng chuyển thêm **85 yêu cầu** sang nhân viên so với giới hạn 2 lần [simulated].
- B4: Xem lại 100% trong phạm vi `noi_dia` + `hang_nang` cho chi phí **11.743 đồng/việc thành công** với giả định 9 phút làm lại; dùng trung bình CSV **15,2973 phút/ca** thì chi phí lên **12.415 đồng/việc thành công** [simulated].

## 5. Công cụ AI đã dùng

- **Công cụ:** ChatGPT/Codex trong phiên làm việc với repo lab.
- **Mục đích:** Đọc yêu cầu, giải thích công thức, hỗ trợ viết code A–B, sinh bảng báo cáo và chạy kiểm tra. Code và bản báo cáo ban đầu do Codex hỗ trợ soạn; các con số được tính bằng code từ CSV, không lấy từ suy đoán của AI.
- **Kiểm tra đã chạy trong phiên với Codex:** Chạy `lab13.py` bằng Python 3.12; xác nhận cả ba phép thử A1 đạt; tính lại tổng chi phí bằng thư viện `csv` và số học Python để đối chiếu mô hình pandas cho giới hạn 1, 2, 3 lần và không giới hạn.
- **Kiểm tra bổ sung đã chạy:** Xác nhận quan hệ tuyến tính giữa kịch bản gấp đôi/giảm nửa và kịch bản thay đổi một cặp; tổng bốn loại yêu cầu khớp toàn mẫu; nội dung báo cáo khớp output; hai CSV và `lab13_starter.py` không thay đổi.
- **Cá nhân đã chạy lại:** Chạy `python lab13.py` trong môi trường `.venv` trên máy cá nhân và cung cấp output terminal; cả ba phép thử A1 đạt, chương trình in đủ bảng A–B và kết thúc không lỗi. Các kiểm tra bổ sung ở trên do Codex thực hiện; cá nhân vẫn cần đọc và giải thích được công thức trước khi bảo vệ.

Chạy trong thư mục `src/` sau khi đã cài môi trường:

```bash
source .venv/bin/activate
python lab13.py
```

## 6. Tự đánh giá

Phần A–B đã có code chạy từ đầu đến cuối và báo cáo sinh trực tiếp từ kết quả tính; các kiểm tra trong phiên đều đạt. Kết luận kinh tế cần giữ đúng phạm vi và nhãn `simulated`, vì thời gian xem lại/làm lại chưa phải số đo thực tế.

Cần tự kiểm tra lại khả năng giải thích hai điểm trước khi bảo vệ: vì sao tử số tính mọi lần chạy còn mẫu số chỉ tính việc thành công; vì sao giới hạn **2 lần chạy** tối ưu chi phí toàn hệ thống dù giới hạn **1 lần** có chi phí mỗi việc thành công thấp hơn [simulated].

Phần cỡ mẫu D1 chờ người phụ trách D bổ sung; kết quả A–B được bàn giao cho người phụ trách chỉ số và hồ sơ cuối. Báo cáo này chỉ ghi nhận phạm vi A–B, chưa xác nhận kết quả duyệt chéo hoặc đóng góp của các thành viên khác.
