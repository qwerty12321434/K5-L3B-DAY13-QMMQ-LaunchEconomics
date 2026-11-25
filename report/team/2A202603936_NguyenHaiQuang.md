# Báo cáo cá nhân · Nguyễn Hải Quang · 2A202603936

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hải Quang
- MSSV: 2A202603936
- Email: quangnh2004@gmail.com
- Vai trò: Người 2, kiểm chứng A–B và gắn nhãn bộ thứ nhất ở nhiệm vụ C.

## 2. Phần việc phụ trách

- Kiểm chứng A1, A2, B3 và B4 từ công thức và dữ liệu gốc.
- Gắn nhãn độc lập 20 ca. Khi cả hai bộ nhãn đã chốt, đối chiếu với người gắn nhãn thứ hai, tính tỷ lệ đồng thuận và lập bảng khắc phục 5 ca.

## 3. Đóng góp cụ thể

### Kiểm chứng A1, A2, B3 và B4

**A1.** Với xác suất thành công mỗi lần là 0,8, số lần chạy kỳ vọng khi giới hạn 2 lần là `1 + 0,2 = 1,20`. Khi chạy đến lúc thành công, kỳ vọng là `1 ÷ 0,8 = 1,25`. Hệ số chi phí mỗi việc thành công khi giới hạn 3 lần là `(1 + 0,2 + 0,2²) ÷ (1 − 0,2³) = 1,25`. Cả ba số khớp bảng nhóm.

**A2.** Tính trên 1.624 lượt chạy và 1.200 yêu cầu. Tử số cộng chi phí của mọi lượt chạy, kể cả lượt lỗi. Mẫu số là 978 yêu cầu có `ket_qua = thanh_cong`.

| Khoản | Phép tính | Chi phí |
| --- | --- | ---: |
| Token | `(5.771.712 × 26 + 734.774 × 130) ÷ 1.000` | 245.585,132 đ |
| Tool | `5.600 × 15` | 84.000 đ |
| Xem lại | `890 phút × 2.000` | 1.780.000 đ `simulated` |
| Làm lại | `1.132 phút × 2.000` | 2.264.000 đ `simulated` |
| Tổng | Cộng bốn khoản | 4.373.585,132 đ `simulated` |

Chi phí mỗi việc thành công là `4.373.585,132 ÷ 978 = 4.471,968… đ`, làm tròn thành **4.472 đ** `simulated`, khớp bảng nhóm.

**B3.** Với giới hạn `k`, giữ chi phí token và tool của các lượt `attempt ≤ k`. Với yêu cầu có `so_lan_chay > k`, tính là chuyển nhân viên và đặt phút xem lại, làm lại về 0 theo quy ước của lab. Chi phí toàn hệ thống bằng chi phí trợ lý cộng `12.000 đ × số yêu cầu không thành công`.

| Giới hạn | Thành công | Không thành công | Chi phí trợ lý `simulated` | Chi phí toàn hệ thống `simulated` | Chi phí trợ lý/việc thành công `simulated` |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 lần | 881 | 319 | 3.621.781 đ | 7.449.781 đ | 4.111 đ |
| 2 lần | 966 | 234 | 4.093.220 đ | 6.901.220 đ | 4.237 đ |
| 3 lần | 978 | 222 | 4.373.585 đ | 7.037.585 đ | 4.472 đ |

Kết quả khớp bảng nhóm. Giới hạn 2 lần có chi phí toàn hệ thống thấp nhất. Giới hạn 1 lần có chi phí trợ lý trên mỗi việc thành công thấp nhất và chuyển thêm 85 yêu cầu sang nhân viên so với giới hạn 2 lần.

**B4.** Lọc 982 yêu cầu thuộc `noi_dia` và `hang_nang`. Có 948 yêu cầu có ít nhất một lượt `ok`, 48 ca làm lại và 900 ca thành công. Chi phí token và tool là 224.513,274 đ. Chi phí mỗi việc thành công được tính bằng `(224.513,274 + 948 × 5 × 2.000 + 48 × phút làm lại × 2.000) ÷ 900`.

| Số phút làm lại mỗi ca | Chi phí/việc thành công `simulated` | So với 12.000 đ `simulated` | Số phút xem lại hòa vốn `simulated` |
| --- | ---: | ---: | ---: |
| 9 phút theo đề | 11.743 đ | 0,98× | 5,12 |
| 15,2973 phút, trung bình trên 74 ca `lam_lai` trong CSV `simulated` | 12.415 đ | 1,03× | 4,80 |

Kết quả khớp bảng nhóm. Giá trị 12.414,504… đ làm tròn đến đồng thành **12.415 đ** `simulated`. Dùng 15,3 phút cũng cho 12.414,793… đ và làm tròn thành 12.415 đ. Hướng dẫn ghi 12.414 đ, chênh 1 đ ở số hiển thị.

### Nhiệm vụ C

Bộ nhãn thứ nhất gồm 20 ca. Khi đối chiếu với bộ của Trần Duy Thành, hai bộ trùng 19/20 ca, đạt **95% đồng thuận trước thảo luận**. Hai người chốt **Ngữ cảnh** cho ca 6, ca duy nhất lệch nhãn. Bảng khắc phục gồm 5 ca đã trùng nhãn, mỗi loại lỗi một ca.

## 4. Bằng chứng

- Dữ liệu gốc gồm [CSV lượt chạy](../../src/logix_runs.csv) và [CSV yêu cầu](../../src/logix_requests.csv).
- Công thức và số liệu gốc trong [tài liệu dữ liệu](../../docs/du_lieu_va_cong_thuc.md). Kết quả đối chiếu nằm trong [bảng chi phí nhóm](bang_chi_phi.md).
- [Bảng lỗi chung](bang_loi.md) ghi hai bộ nhãn gốc, tỷ lệ đồng thuận, quy tắc phân biệt cho ca 6 và bảng khắc phục 5 ca.

## 5. Công cụ AI đã dùng

Codex hỗ trợ tính lại A1, A2, B3 và B4 bằng PowerShell từ dữ liệu gốc và trình bày kết quả. Phép kiểm dùng công thức của đề và đọc trực tiếp hai CSV. Sau khi tính, kết quả được đối chiếu với bảng nhóm ở cùng phạm vi, cùng giả định và cùng cách làm tròn.

Với nhiệm vụ C, Codex hỗ trợ nhập nguyên bộ nhãn đã cung cấp, đếm số ca trùng và soạn đề xuất phát hiện, khắc phục dựa trên mô tả trong đề.

## 6. Tự đánh giá

Phép kiểm B3 cho thấy giới hạn có chi phí trợ lý thấp nhất trên mỗi việc thành công có thể khác giới hạn tối ưu cho toàn hệ thống. Kết luận B4 nhạy với giả định thời gian làm lại. Ca 6 cho thấy cần phân biệt thao tác chọn sai của khách với một giả định của quy trình không phù hợp với hoàn cảnh.
