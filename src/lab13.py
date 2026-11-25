"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Phần A–B đã hoàn thiện; TODO CP4 dành cho người phụ trách D.
Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# Ba hàm A1 được kiểm tra trước khi tính trên dữ liệu.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải thuộc (0, 1].')
    if k is not None and (isinstance(k, bool) or not isinstance(k, int) or k < 1):
        raise ValueError('k phải là số nguyên dương hoặc None.')
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    so_lan_chay_ky_vong(p, k)  # Kiểm tra miền giá trị giống hàm trên.
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP2 gọi lại mo_hinh với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        if isinstance(max_lan_chay, bool) or not isinstance(max_lan_chay, int) or max_lan_chay < 1:
            raise ValueError('max_lan_chay phải là số nguyên dương hoặc None.')
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = float(tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai)
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())
    return dict(
        token=float(tien_token.sum()), tool=float(tien_tool.sum()),
        chay_lai=float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
        xem_lai=float(xem_lai), lam_lai=float(lam_lai), tong=tong,
        thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else math.inf,
        hoa_don_moi_yc=float((tien_token.sum() + tien_tool.sum()) / len(reqs)) if len(reqs) else math.inf,
    )


def bao_cao_ab(runs, reqs):
    """Sinh bảng A–B trực tiếp từ dữ liệu; không chép số từ đáp án mẫu."""
    def so(x, le=0):
        return f'{x:,.{le}f}'.replace(',', '_').replace('.', ',').replace('_', '.')

    def bang(tieu_de, cot, dong):
        return '\n'.join([tieu_de, '', '| ' + ' | '.join(cot) + ' |',
                          '| ' + ' | '.join(['---'] * len(cot)) + ' |']
                         + ['| ' + ' | '.join(map(str, row)) + ' |' for row in dong])

    goc = mo_hinh(runs, reqs)
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    trong_pham_vi = mo_hinh(runs, pham_vi)
    phan = [
        '# Bảng chi phí · Nhiệm vụ A và B',
        'Nguồn số: chạy `src/lab13.py` trên hai CSV được phát; toàn bộ dữ liệu lab là giả lập. '
        'Mọi tổng, tỉ lệ hoặc kết luận có sử dụng phút `_simulated` được ghi nhãn **simulated**. '
        'Các bảng A2–B3 chưa cộng chi phí cố định, trừ A4.',
        bang('## A1 · Ba phép thử đáp án biết trước', ['Phép thử (p = 0,8)', 'Kết quả của nhóm'], [
            ['Số lần chạy trung bình, tối đa 2 lần', so(so_lan_chay_ky_vong(0.8, 2), 2)],
            ['Số lần chạy trung bình, chạy đến khi đúng', so(so_lan_chay_ky_vong(0.8), 2)],
            ['Hệ số chi phí mỗi việc thành công, tối đa 3 lần', so(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 2)],
        ]),
        'Giả định mỗi lần chạy đúng độc lập với xác suất p: E = (1 − (1 − p)^k)/p; '
        'P(thành công) = 1 − (1 − p)^k; E/P = 1/p = 1,25 với p = 0,8. '
        'Khi chạy đến khi đúng, E = 1/p và P = 1.',
    ]
    dong_a2 = []
    for nhan, key, nguon, loai in [
        ('Token', 'token', 'tokens_in / 1.000 × 26 + tokens_out / 1.000 × 130', 'đo từ trace'),
        ('Tool', 'tool', 'tool_calls × 15', 'đo từ trace'),
        ('Trong đó, phần của lần chạy thứ 2 và 3', 'chay_lai', 'token + tool của attempt > 1; đã nằm trong hai dòng trên', 'đo từ trace'),
        ('Xem lại', 'xem_lai', 'phut_xem_lai_simulated × 2.000', 'simulated'),
        ('Làm lại', 'lam_lai', 'phut_lam_lai_simulated × 2.000', 'simulated'),
        ('Tổng chi phí', 'tong', 'token + tool + xem lại + làm lại', 'simulated'),
        ('Số việc thành công (việc)', 'thanh_cong', "ket_qua == 'thanh_cong'", 'đếm từ dữ liệu'),
        ('Chi phí mỗi việc thành công', 'cps', 'tổng / số việc thành công', 'simulated'),
        ('Hoá đơn token và tool chia cho số yêu cầu', 'hoa_don_moi_yc', 'hoá đơn / số yêu cầu', 'đo từ trace'),
    ]:
        dong_a2.append([nhan, so(goc[key], 1 if key == 'hoa_don_moi_yc' else 0), nguon, loai])
    phan.append(bang('## A2 · Mô hình chi phí từ trace', ['Khoản', 'Giá trị (đ, trừ số việc)', 'Cách tính', 'Nhãn'], dong_a2))
    phan.append(f'- Tử số tính mọi lần chạy kể cả lỗi vì vẫn phát sinh tiền; mẫu số chỉ đếm {goc["thanh_cong"]} việc thành công. Chi phí mỗi việc thành công gấp **{so(goc["cps"] / goc["hoa_don_moi_yc"], 1)} lần** hoá đơn chia số yêu cầu [simulated].\n'
                f'- Khoản lớn nhất là làm lại: **{so(goc["lam_lai"] / goc["tong"] * 100, 1)}%**; tổng tiền nhân viên chiếm **{so((goc["xem_lai"] + goc["lam_lai"]) / goc["tong"] * 100, 1)}%** [simulated].')
    he_thong = goc['tong'] + (len(reqs) - goc['thanh_cong']) * BASELINE
    phan.append(f'So sánh cùng khối lượng: ({so(goc["tong"])} + {len(reqs) - goc["thanh_cong"]} × 12.000) / {len(reqs)} = '
                f'**{so(he_thong / len(reqs))} đ/yêu cầu**, bằng {so(he_thong / len(reqs) / BASELINE, 2)}× nhân viên tự làm [simulated]; áp dụng quy ước B3 cho mọi yêu cầu không thành công.')

    dong_a3 = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        nhom = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, nhom)
        so_run = runs['request_id'].isin(nhom['request_id']).sum()
        dong_a3.append([loai, len(nhom), so(kq['thanh_cong'] / len(nhom) * 100, 1) + '%',
                        so(so_run / len(nhom), 2), so(kq['cps']), so(kq['cps'] / BASELINE, 2) + '×'])
    phan.append(bang('## A3 · Tách theo loại yêu cầu', ['Loại', 'Số yêu cầu', 'Tỉ lệ thành công', 'Số lần chạy mỗi yêu cầu', 'Chi phí mỗi việc thành công [simulated]', 'So với 12.000 đ [simulated]'], dong_a3))
    quoc_te = reqs[reqs['loai'] == 'quoc_te']
    run_qt = runs[runs['request_id'].isin(quoc_te['request_id'])]
    ok_qt = run_qt.assign(ok=run_qt['status'].eq('ok')).groupby('attempt')['ok'].mean()
    kq_qt = mo_hinh(runs, quoc_te)
    phan.append(f'- Quốc tế không đáng đưa vào pilot: {so(kq_qt["cps"])} đ/việc thành công = {so(kq_qt["cps"] / BASELINE, 2)}× mốc 12.000 đ [simulated].\n'
                f'- Tỉ lệ run `ok` ở lần 1/2/3 của quốc tế là {" / ".join(so(ok_qt.get(k, 0) * 100, 1) + "%" for k in (1, 2, 3))}; chạy lại không khắc phục tốt lỗi lặp. Đây là tỉ lệ theo run, khác thành công cuối của yêu cầu.\n'
                '- Đề xuất phạm vi noi_dia + hang_nang; doi_tac cần đánh giá riêng điều khoản, dù chi phí mỗi việc thành công còn dưới 12.000 đ [simulated].')

    dong_a4 = []
    for khoi_luong in (45000, 22500):
        thanh_cong_thang = khoi_luong * trong_pham_vi['thanh_cong'] / len(reqs)
        co_dinh = 40000000 / thanh_cong_thang
        cps = trong_pham_vi['cps'] + co_dinh
        dong_a4.append([so(khoi_luong) + ' yêu cầu/tháng', so(thanh_cong_thang), so(co_dinh), so(cps), so(cps / BASELINE, 2) + '×'])
    phan.append(bang('## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)', ['Khối lượng toàn công ty', 'Việc thành công trong phạm vi/tháng', 'Cố định mỗi việc (đ)', 'Chi phí mỗi việc thành công + cố định (đ) [simulated]', 'So với 12.000 đ [simulated]'], dong_a4))
    nguong_luong = 40000000 / (BASELINE - trong_pham_vi['cps']) * len(reqs) / trong_pham_vi['thanh_cong']
    phan.append(f'- Giữ cơ cấu mẫu: việc thành công trong phạm vi/tháng = khối lượng toàn công ty × {trong_pham_vi["thanh_cong"]}/{len(reqs)}; chi phí biến đổi = {so(trong_pham_vi["tong"])} / {trong_pham_vi["thanh_cong"]} = {so(trong_pham_vi["cps"])} đ [simulated].\n'
                f'- Cố định 40.000.000 đ/tháng chưa đảo kết luận ở 45.000 hoặc 22.500 yêu cầu/tháng; điểm hoà vốn theo chi phí/việc thành công khoảng {so(nguong_luong)} yêu cầu toàn công ty/tháng [simulated].\n'
                '- Cột so với 12.000 đ chỉ so chi phí/việc thành công; khi đánh giá tiết kiệm toàn công ty phải cộng phần nhân viên xử lý như B3.')

    kich_ban = [
        ('Giá token gấp đôi', '52 đ vào; 260 đ ra / 1.000 token; tool giữ nguyên', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', '13 đ vào; 65 đ ra / 1.000 token', dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại gấp đôi', 'Tiền xem lại × 2', dict(he_so_xem_lai=2)),
        ('Tỉ lệ xem lại giảm một nửa', 'Tiền xem lại ÷ 2', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', 'Tiền làm lại × 2', dict(he_so_lam_lai=2)),
        ('Số ca làm lại giảm một nửa', 'Tiền làm lại ÷ 2', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', '2.500 đ/phút', dict(luong_phut=2500)),
        ('Chỉ cho chạy tối đa 2 lần', 'Bỏ attempt > 2; yêu cầu vượt giới hạn chuyển nhân viên, phút simulated = 0', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần', 'Bỏ attempt > 1; yêu cầu vượt giới hạn chuyển nhân viên, phút simulated = 0', dict(max_lan_chay=1)),
    ]
    dong_b1 = []
    for ten, cach, tham_so in kich_ban:
        kq = mo_hinh(runs, reqs, **tham_so)
        dong_b1.append([ten, cach, so(kq['cps']), f'{(kq["cps"] / goc["cps"] - 1) * 100:+.1f}%'.replace('.', ',')])
    phan.append(bang('## B1 · Đổi từng yếu tố', ['Kịch bản', 'Cách tính', 'Chi phí mỗi việc thành công (đ) [simulated]', 'Thay đổi [simulated]'], dong_b1))
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    phan.append('## B2 · Đổi một cặp và xếp hạng\n\n'
                f'- Token và xem lại cùng gấp đôi: **{so(cap["cps"])} đ**, tăng **{so((cap["cps"] / goc["cps"] - 1) * 100, 1)}%** [simulated]; bằng tổng hai tác động riêng vì số việc thành công giữ nguyên và mô hình cộng tuyến tính.\n'
                f'- Theo các mức biến động B1: **1. Làm lại (+{so(goc["lam_lai"] / goc["tong"] * 100, 1)}%) · 2. Xem lại (+{so(goc["xem_lai"] / goc["tong"] * 100, 1)}%) · 3. Lương (+{so((goc["xem_lai"] + goc["lam_lai"]) * 0.25 / goc["tong"] * 100, 1)}%)** [simulated].')

    dong_b3, ket_qua_gioi_han = [], {}
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        ca_he_thong = kq['tong'] + BASELINE * khong_thanh_cong
        ket_qua_gioi_han[k] = (kq, ca_he_thong)
        dong_b3.append([f'{k} lần', so(kq['tong']), khong_thanh_cong, so(ca_he_thong), so(kq['cps'])])
    phan.append(bang('## B3 · Giới hạn chạy lại có thật sự rẻ hơn', ['Giới hạn', 'Tổng chi phí trợ lý (đ) [simulated]', 'Số yêu cầu không thành công', 'Chi phí cả hệ thống (đ) [simulated]', 'Chi phí mỗi việc thành công (đ) [simulated]'], dong_b3))
    re_nhat = min(ket_qua_gioi_han, key=lambda k: ket_qua_gioi_han[k][1])
    cps_thap = min(ket_qua_gioi_han, key=lambda k: ket_qua_gioi_han[k][0]['cps'])
    chenh_viec = ket_qua_gioi_han[re_nhat][0]['thanh_cong'] - ket_qua_gioi_han[cps_thap][0]['thanh_cong']
    phan.append(f'- Cả hệ thống = tổng trợ lý + (số yêu cầu − số thành công) × 12.000 đ, theo quy ước B3.\n'
                f'- **{re_nhat} lần** rẻ nhất cho công ty ({so(ket_qua_gioi_han[re_nhat][1])} đ); **{cps_thap} lần** có chi phí/việc thành công thấp nhất nhưng đẩy thêm {chenh_viec} yêu cầu sang nhân viên [simulated].')

    run_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_dau_ra = run_pv.loc[run_pv['status'].eq('ok'), 'request_id'].nunique()
    so_lam_lai = int(pham_vi['ket_qua'].eq('lam_lai').sum())
    phut_thuc_nghiem = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].mean()
    phut_trung_vi = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated'].median()
    hoa_don_pv = trong_pham_vi['token'] + trong_pham_vi['tool']
    dong_b4 = []
    for nhan, phut in [('Giả định đề bài: 9 phút/ca', 9),
                       ('Theo trung bình CSV chính xác', phut_thuc_nghiem),
                       ('Trung bình làm tròn 1 chữ số (đối chiếu hướng dẫn)', round(phut_thuc_nghiem, 1))]:
        tong = hoa_don_pv + co_dau_ra * 5 * LUONG_PHUT + so_lam_lai * phut * LUONG_PHUT
        cps = tong / trong_pham_vi['thanh_cong']
        hoa_von = (BASELINE * trong_pham_vi['thanh_cong'] - hoa_don_pv - so_lam_lai * phut * LUONG_PHUT) / (co_dau_ra * LUONG_PHUT)
        dong_b4.append([nhan, so(phut, 4), so(tong), so(cps), so(cps / BASELINE, 2) + '×', so(hoa_von, 2)])
    phan.append(bang('## B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang)', ['Kịch bản', 'Phút làm lại/ca [simulated]', 'Tổng chi phí (đ) [simulated]', 'Chi phí/việc thành công (đ) [simulated]', 'So với 12.000 đ [simulated]', 'Phút xem lại tối đa để hoà vốn [simulated]'], dong_b4))
    phan.append(f'- Phạm vi {len(pham_vi)} yêu cầu, {trong_pham_vi["thanh_cong"]} thành công; {co_dau_ra} yêu cầu có ≥1 run `ok`, mỗi yêu cầu xem lại 5 phút; {so_lam_lai} ca làm lại; token + tool = {so(hoa_don_pv)} đ.\n'
                f'- Công thức: (token + tool + {co_dau_ra} × 5 × 2.000 + {so_lam_lai} × phút làm lại × 2.000) / {trong_pham_vi["thanh_cong"]}; phút trung bình/trung vị của toàn bộ ca làm lại = {so(phut_thuc_nghiem, 4)}/{so(phut_trung_vi, 1)} [simulated].\n'
                '- Xem lại 100% gần hoặc vượt mốc 12.000 đ/việc thành công [simulated]; pilot cần đo thời gian thực và mức xem lại có thể giảm an toàn. B4 chưa cộng cố định và phần nhân viên làm thay.')
    phan.append('## Nguồn phương pháp và bàn giao\n\n'
                '- Công thức, quy tắc cắt lần chạy và giả định B4: `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (A–B).\n'
                '- Người phụ trách chỉ số và hồ sơ cuối lấy kết quả từ các bảng trên, giữ nguyên nhãn simulated và phạm vi.\n'
                '- Phần tính cỡ mẫu D1 do người phụ trách D bổ sung vào `src/lab13.py`.')
    return '\n\n'.join(phan) + '\n'


# ---------- Nhiệm vụ D1 · Cỡ mẫu và chia cụm ----------
def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhánh khi so hai tỉ lệ độc lập, trước hiệu ứng chia cụm."""
    if not (0 < p1 < 1 and 0 < p2 < 1 and p1 != p2):
        raise ValueError('Hai tỉ lệ phải khác nhau và thuộc (0, 1).')
    if not (0 < alpha < 1 and 0 < power < 1):
        raise ValueError('alpha và power phải thuộc (0, 1).')
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_beta = NormalDist().inv_cdf(power)
    p_trung_binh = (p1 + p2) / 2
    tu = (z_alpha * math.sqrt(2 * p_trung_binh * (1 - p_trung_binh))
          + z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(tu / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=0.02):
    """Hệ số thiết kế cho m yêu cầu trong mỗi cụm."""
    if m < 1 or not 0 <= icc < 1:
        raise ValueError('m phải dương và ICC phải thuộc [0, 1).')
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(so_cum, m, icc=0.02):
    return so_cum * m / he_so_thiet_ke(m, icc)


def power_hai_ti_le(p1, p2, n_moi_nhom, alpha=0.05):
    """Xấp xỉ power hai phía theo phân phối chuẩn cho n hiệu dụng mỗi nhánh."""
    p_trung_binh = (p1 + p2) / 2
    do_lech_chuan_h0 = math.sqrt(2 * p_trung_binh * (1 - p_trung_binh) / n_moi_nhom)
    do_lech_chuan_h1 = math.sqrt((p1 * (1 - p1) + p2 * (1 - p2)) / n_moi_nhom)
    nguong = NormalDist().inv_cdf(1 - alpha / 2) * do_lech_chuan_h0
    phan_phoi = NormalDist(mu=p2 - p1, sigma=do_lech_chuan_h1)
    return phan_phoi.cdf(-nguong) + 1 - phan_phoi.cdf(nguong)


def bao_cao_d1(reqs):
    """Tính năm câu D1 và tỉ lệ an toàn để chốt luật dừng pilot."""
    n5 = co_mau_hai_ti_le(0.70, 0.75)
    n6 = co_mau_hai_ti_le(0.70, 0.76)
    de75 = he_so_thiet_ke(75)
    so_yeu_cau_nhan_vien = math.ceil(n5 * de75)
    so_nhan_vien_nhom = math.ceil(so_yeu_cau_nhan_vien / 75)
    m6 = 1
    while co_mau_hieu_dung(20, m6) < n6:
        m6 += 1
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    an_toan_chung = reqs['mo_lai_trong_7_ngay'].eq(1).mean()
    an_toan_pham_vi = pham_vi['mo_lai_trong_7_ngay'].eq(1).mean()
    return ('\n## D1 · Cỡ mẫu và chỉ số an toàn\n'
            f'a) Chia theo yêu cầu, 0,70 → 0,75: {n5:,} yêu cầu/nhóm.\n'
            f'b) Theo nhân viên, m=75: DE={de75:.2f}; cần {so_yeu_cau_nhan_vien:,} '
            f'yêu cầu và {so_nhan_vien_nhom} nhân viên/nhóm, tổng {2 * so_nhan_vien_nhom} > 40.\n'
            f'c) 20 nhân viên/nhóm: c/ICC=20/0,02={20 / 0.02:,.0f} '
            f'< {n5:,}; không đủ cho chênh 5 điểm.\n'
            f'd) 6 depot/nhóm: c/ICC=6/0,02={6 / 0.02:,.0f} '
            f'< {n5:,}; chỉ có 6 cụm/nhóm.\n'
            f'e) Chênh 6 điểm: n={n6:,}/nhóm; 20 nhân viên/nhóm cần '
            f'm={m6} yêu cầu/người, DE={he_so_thiet_ke(m6):.2f}, '
            f'n hiệu dụng={co_mau_hieu_dung(20, m6):.1f}/nhóm.\n'
            f'Đánh đổi: nếu tác động chỉ 5 điểm, power tại n hiệu dụng {n6:,} '
            f'xấp xỉ {power_hai_ti_le(0.70, 0.75, n6):.2f}, dưới 0,80.\n'
            f'An toàn: mở lại 7 ngày toàn mẫu {an_toan_chung:.2%} '
            f'({reqs["mo_lai_trong_7_ngay"].eq(1).sum()}/{len(reqs)}); '
            f'phạm vi noi_dia + hang_nang {an_toan_pham_vi:.2%} '
            f'({pham_vi["mo_lai_trong_7_ngay"].eq(1).sum()}/{len(pham_vi)}).')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print(bao_cao_ab(runs, reqs))
    print(bao_cao_d1(reqs))
