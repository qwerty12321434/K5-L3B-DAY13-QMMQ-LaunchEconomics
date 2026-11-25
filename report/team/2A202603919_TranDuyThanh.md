# Báo cáo cá nhân — Trần Duy Thành · 2A202603919

## 1. Thông tin thành viên

- Họ tên: Trần Duy Thành
- MSSV: 2A202603919
- Email: djdjjdue2@gmail.com
- Vai trong nhóm: thiết kế thí nghiệm pilot (D) và gắn nhãn bộ thứ hai (C)

## 2. Phần việc phụ trách

- Tính D1, trả lời D2, chọn cách chia nhóm và viết kế hoạch pilot.
- Gắn độc lập 20 nhãn ở bộ thứ hai trước khi đối chiếu với bộ thứ nhất.

## 3. Đóng góp cụ thể

- Phần D1 trong `src/lab13.py` tính cỡ mẫu hai tỉ lệ, hệ số thiết kế, cỡ mẫu hiệu dụng và tỉ lệ mở lại từ CSV.
- `report/team/pilot_plan.yaml` ghi kết quả D1–D2, đánh đổi của cách chia theo nhân viên, lịch pilot, ba luật dừng và luồng rollback.
- Bộ nhãn thứ hai đã được điền cho 20 ca

## 4. Bằng chứng

- `src/lab13.py`: mục “Nhiệm vụ D1 · Cỡ mẫu và chia cụm”.
- `report/team/pilot_plan.yaml`: chú thích D1–D2 và nội dung kế hoạch.
- Cột “Nhãn người 2” trong `report/team/bang_loi.md` 

## 5. Công cụ AI đã dùng

- Codex hỗ trợ xem code D1, bản nháp kế hoạch pilot
- Codex đã chạy code để kiểm tra ba phép thử A1, kết quả D1 và tỉ lệ an toàn;

## 6. Tự đánh giá

- Đã hoàn thành phần tính cỡ mẫu D1, trả lời D2 và xây dựng kế hoạch pilot chia ngẫu nhiên theo nhân viên, gồm 20 người mỗi nhóm và 3 luật dừng.
- Điểm cần lưu ý của phương án là 40 nhân viên không đủ cỡ mẫu để phát hiện mức chênh 5 điểm phần trăm với power 0,80. Phương án chọn mức 6 điểm và cần tối thiểu 299 yêu cầu mỗi nhân viên; nếu tác động thật chỉ 5 điểm thì power khoảng 0,64.
- Nhãn hai bộ trùng 19/20 ca trước thảo luận nên cần thảo luận
