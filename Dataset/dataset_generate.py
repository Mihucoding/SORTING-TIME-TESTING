import numpy as np
import pandas as pd

# Cấu hình số lượng dòng
num_rows = 1_000_000

print(f"Đang tạo dataset với {num_rows} dòng...")

# 1. TẠO DỮ LIỆU SỐ THỰC (FLOATS)
# Tạo mảng ngẫu nhiên từ -100,000 đến 100,000
# np.random.uniform rất nhanh vì nó được viết bằng C ở bên dưới
floats = np.random.uniform(-10000000, 10000000, size=num_rows)
floats_2 = np.random.uniform(-1000000, 10000000, size=num_rows)

# Tạo các cột đặc biệt
col_float_asc = np.sort(floats)        # Sắp xếp tăng dần
col_float_desc = np.sort(floats_2)[::-1] # Sắp xếp giảm dần (đảo ngược mảng)

# Tạo 3 cột random còn lại
floats_random = np.random.uniform(-10000000, 10000000, size=(3, num_rows))

# 2. TẠO DỮ LIỆU SỐ NGUYÊN (INTEGERS)
# Tạo 5 cột số nguyên ngẫu nhiên
ints_random = np.random.randint(-10000000, 10000000, size=(5, num_rows))

# 3. ĐÓNG GÓI VÀO DATAFRAME
df = pd.DataFrame({
    'float_asc': col_float_asc,
    'float_desc': col_float_desc,
    'float_rand_1': floats_random[0],
    'float_rand_2': floats_random[1],
    'float_rand_3': floats_random[2],
    'int_rand_1': ints_random[0],
    'int_rand_2': ints_random[1],
    'int_rand_3': ints_random[2],
    'int_rand_4': ints_random[3],
    'int_rand_5': ints_random[4]
})

# 4. XUẤT FILE CSV
df.to_csv('dataset_sorting_1M.csv', index=False)
print("Đã tạo xong file!")