

---

# BÁO CÁO THỬ NGHIỆM HIỆU NĂNG THUẬT TOÁN SẮP XẾP

Dự án này tập trung vào việc đo lường, phân tích và so sánh hiệu năng của các thuật toán sắp xếp phổ biến trên tập dữ liệu lớn ( phần tử).

## 👨‍💻 Thông Tin Sinh Viên

* **Họ và tên:** Phan Đình Minh Huấn
* **Mã số sinh viên:** 25520616
* **Lớp:** TTNT2025
* **Đơn vị:** Đại học Công nghệ Thông tin - ĐHQG TP.HCM (UIT)

## 💻 Cấu Hình Thử Nghiệm (Hardware)

Toàn bộ các thử nghiệm Benchmark được thực hiện trên cấu hình máy cá nhân để đảm bảo tính nhất quán:

* **CPU:** Intel Core i5-12600K (10 nhân, 16 luồng)
* **RAM:** 16GB DDR4
* **GPU:** NVIDIA GeForce RTX 5060 Ti 16GB

---

## 📊 Mô Tả Dữ Liệu (Dataset)

Dữ liệu thử nghiệm được lưu trữ trong file CSV gồm **10 cột**, mỗi cột chứa **1,000,000** giá trị được sinh ngẫu nhiên:

| Nhóm dữ liệu | Số lượng cột | Kiểu dữ liệu | Trình trạng dữ liệu |
| --- | --- | --- | --- |
| **Double** | 5 Cột | `Double` | Cột 1: Đã sắp xếp tăng dần |
|  |  |  | Cột 2: Đã sắp xếp giảm dần |
|  |  |  | Cột 3-5: Ngẫu nhiên |
| **Integer** | 5 Cột | `Integer` | Ngẫu nhiên hoàn toàn |

---

## 🛠 Thuật Toán Triển Khai

Dự án so sánh hiệu năng giữa các kỹ thuật sắp xếp kinh điển và các hàm thư viện tối ưu hóa:

### 1. Thuật toán tự triển khai (Manual Implementation)

* **Heap Sort:** Tận dụng cấu trúc dữ liệu Heap để sắp xếp.
* **Merge Sort:** Thuật toán chia để trị với độ phức tạp ổn định .
* **Quick Sort:** Thuật toán sắp xếp nhanh (có tối ưu chọn Pivot).

### 2. Hàm sắp xếp hệ thống (Library Sort)

* **C++ std::sort:** Hàm sắp xếp gốc của ngôn ngữ C++.
* **NumPy Sort:** Giải thuật sắp xếp tối ưu hóa cho mảng lớn trong Python.

---

## 📁 Cấu Trúc Repository

```text
├── Dataset/
│   ├── dataset_generate.py       # Mã nguồn tạo dữ liệu ngẫu nhiên
│   └── dataset_sorting_1M.zip    # File nén chứa 10 triệu bản ghi
├── SORT AND BENCHMARK/
│   ├── sort_cpp.cpp              # Triển khai thuật toán bằng C++
│   └── sort_py.py                # Triển khai thuật toán bằng Python
├── Chart/
│   ├── chart_generate.py         # Script vẽ biểu đồ từ kết quả test
│   └── benchmark_comparison.png  # Biểu đồ so sánh trực quan
└── README.md                     # Tài liệu hướng dẫn

```

---

## 📚 Nguồn Tham Khảo

Dự án được hoàn thành với sự tham khảo từ các nguồn uy tín:

* **Lý thuyết & Thuật toán:** GeeksforGeeks, 28tech.
* **Kỹ thuật lập trình:** Các kênh YouTube chuyên ngành IT.
* **Hỗ trợ logic & Debug:** Gemini AI và các mô hình ngôn ngữ lớn.

---

### Hướng dẫn chạy thử nghiệm

1. Giải nén file dữ liệu trong thư mục `Dataset/`.
2. Chạy file `sort_cpp.cpp` để đo thời gian thực thi của C++.
3. Chạy file `sort_py.py` để so sánh với Python và NumPy.
4. Sử dụng `chart_generate.py` để trích xuất biểu đồ so sánh.

---

*Bản quyền thuộc về Phan Đình Minh Huấn - UIT 2026.*

---

**Cách sử dụng:**

1. Bạn tạo một file mới tên là `README.md` (nhớ xóa đuôi `.txt` nếu có).
2. Copy toàn bộ đoạn mã trên và dán vào.
3. Commit và Push lên GitHub bằng lệnh:
```powershell
git add README.md
git commit -m "Add professional README"
git push origin main

```



Bạn có muốn mình giúp viết thêm phần **Kết quả thực nghiệm (Experimental Results)** để điền các thông số thời gian chạy thực tế trên máy i5-12600K của bạn vào bảng không?