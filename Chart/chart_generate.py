import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu lấy từ kết quả benchmark của bạn
data = {
    "Dữ liệu": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Quicksort (PY)": [1509.31, 1635.73, 1995.60, 2003.08, 2190.98, 2064.52, 2142.78, 2122.11, 2097.31, 2130.63],
    "Heapsort (PY)": [2844.69, 2664.91, 3824.63, 3868.93, 3892.39, 4176.60, 3987.97, 3732.28, 3909.47, 4109.28],
    "Mergesort (PY)": [1466.12, 1471.13, 2106.51, 2142.58, 2096.00, 2171.93, 2280.10, 2089.01, 2106.15, 2331.02],
    "Sort (C++)": [34.74, 25.69, 102.79, 110.62, 131.47, 118.69, 118.35, 107.84, 108.25, 107.39],
    "Sort (NumPy)": [8.55, 8.14, 8.33, 7.31, 8.81, 12.23, 11.37, 12.13, 12.84, 11.57]
}

df = pd.DataFrame(data)

# ===== IN THỜI GIAN TRUNG BÌNH =====
print("=" * 60)
print("THỜI GIAN CHẠY TRUNG BÌNH CỦA CÁC THUẬT TOÁN")
print("=" * 60)
avg_times = df.mean(numeric_only=True)
for algo, avg_time in avg_times.items():
    print(f"{algo:20s}: {avg_time:8.2f} ms")
print("=" * 60 + "\n")

# ===== BIỂU ĐỒ 1: So sánh thời gian chạy (Line Chart) =====
plt.figure(figsize=(12, 6))
for col in df.columns:
    if col != "Dữ liệu":
        plt.plot(df["Dữ liệu"], df[col], marker='o', label=col, linewidth=2)

plt.xlabel("Số lần chạy", fontsize=12)
plt.ylabel("Thời gian (ms)", fontsize=12)
plt.title("So sánh Hiệu suất các Thuật toán Sắp xếp", fontsize=14, fontweight='bold')
plt.legend(loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('benchmark_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Đã lưu: benchmark_comparison.png")
# plt.show()

# ===== BIỂU ĐỒ 2: Biểu đồ cột - So sánh trung bình =====
plt.figure(figsize=(10, 6))
avg_times = df.mean(numeric_only=True)
colors = ['#FF6B6B', '#FF8C42', '#FFA500', '#00D4FF', '#4CAF50']
bars = plt.bar(avg_times.index, avg_times.values, color=colors, edgecolor='black', linewidth=1.5)

# Thêm giá trị trên các cột
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.ylabel("Thời gian trung bình (ms)", fontsize=12)
plt.title("Thời gian Trung bình của các Thuật toán", fontsize=14, fontweight='bold')
plt.xticks(rotation=15, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('benchmark_average.png', dpi=300, bbox_inches='tight')
print("✓ Đã lưu: benchmark_average.png")
# plt.show()

# ===== BIỂU ĐỒ 3: Box Plot - Phân bố dữ liệu =====
plt.figure(figsize=(10, 6))
boxplot_data = [df[col].values for col in df.columns if col != "Dữ liệu"]
labels = [col for col in df.columns if col != "Dữ liệu"]
bp = plt.boxplot(boxplot_data, labels=labels, patch_artist=True)

# Tô màu các box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.ylabel("Thời gian (ms)", fontsize=12)
plt.title("Phân bố Thời gian của các Thuật toán", fontsize=14, fontweight='bold')
plt.xticks(rotation=15, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('benchmark_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Đã lưu: benchmark_distribution.png")
# plt.show()

# ===== BIỂU ĐỒ 4: Biểu đồ cột - So sánh tất cả các lần chạy =====
plt.figure(figsize=(14, 6))
x = np.arange(len(df["Dữ liệu"]))
width = 0.15

for i, col in enumerate([c for c in df.columns if c != "Dữ liệu"]):
    plt.bar(x + i*width, df[col], width, label=col, color=colors[i])

plt.xlabel("Số lần chạy", fontsize=12)
plt.ylabel("Thời gian (ms)", fontsize=12)
plt.title("So sánh Thời gian theo từng Lần chạy", fontsize=14, fontweight='bold')
plt.xticks(x + width*2, df["Dữ liệu"].values)
plt.legend(loc='best')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('benchmark_detailed.png', dpi=300, bbox_inches='tight')
print("✓ Đã lưu: benchmark_detailed.png")
plt.show()

print("\n✓ Tất cả biểu đồ đã được tạo và lưu!")
