import numpy as np
import time
import random
import sys
import pandas as pd
sys.setrecursionlimit(10**6) # Tăng giới hạn recursion của Python

#HEAPPP
def heapify(arr, n , i):
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest] , arr[i]
        heapify(arr,n,largest)
def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
#QUICKSORT
def swap_pos(arr,i,j):
    arr[i] , arr[j] = arr[j] , arr[i]

def partition(arr,low,high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    pivot = arr[high]
    i = low - 1
    for j in range (low,high,1):
        if arr[j] < pivot:
            i += 1
            swap_pos(arr,i,j) 
    swap_pos(arr,high,i+1)
    return i + 1
def quick_sort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quick_sort(arr,pivot + 1 ,high)
        quick_sort(arr,low, pivot - 1)
#MERGE_SORT
def merge(arr,l,m,r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i , j = 0,0
    while ( i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            arr[l] = left[i]
            i += 1
            l += 1
        else:
            arr[l] = right[j]
            j += 1
            l += 1  
    while (i < len(left)):
        arr[l] = left[i]
        i += 1
        l += 1
    while (j < len(right)):
        arr[l] = right[j]
        j += 1
        l += 1

def merge_sort(arr,l,r):
    if l >= r:
        return
    m = (l + r) // 2  
    merge_sort(arr,l,m)
    merge_sort(arr,m+1,r)
    merge(arr,l,m,r)



def run_benchmark(name, data):
    arr = list(data) 
    np_arr = np.array(arr)
    
    
    if name == "Quick Sort":
        start_time = time.perf_counter()
        quick_sort(arr,0,len(arr) - 1)
    elif name == "Python Sort":
        start_time = time.perf_counter()
        np_arr.sort() 
    elif name == "Heap Sort":
        start_time = time.perf_counter()
        heap_sort(arr)
    elif name == "Merge Sort":
        start_time = time.perf_counter()
        merge_sort(arr, 0, len(arr) - 1)
        
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000 # Đổi ra ms

def main():
    filename = 'dataset_sorting_1M.csv'
    
    
    
    print(f"--- Đang đọc dữ liệu từ {filename} ---")
    try:
        df = pd.read_csv(filename)  # Hãy đưa ra đường dẫn của bạn nếu code không chạy
        #df = pd.read_csv(r"đường dẫn đến file lưu dataset\dataset_sorting_1M.csv")
        print(f"Đã đọc file thành công! Kích thước gốc: {df.shape}")
    except FileNotFoundError:
        print("Không tìm thấy file csv. Hãy chạy code tạo file ở bước trước.")
        return

    # Lấy danh sách các cột cần test
    columns = df.columns
    results = {}

    print(f"\n--- Bắt đầu Benchmark (Test trên {1000000} phần tử đầu tiên mỗi cột) ---")
    print(f"{'Column Name':<20} | {'Python Sort':<12} | {'Quick Sort':<12} | {'Merge Sort':<12} | {'Heap Sort':<12}")
    print("-" * 80)

    for col in columns:
        
        data_subset = df[col].values[0:].tolist()
        
        # Đo thời gian từng thuật toán ( Tham khảo Gemini)
        t_py = run_benchmark("Python Sort", data_subset)
        t_qs = run_benchmark("Quick Sort", data_subset)
        t_ms = run_benchmark("Merge Sort", data_subset)
        t_hs = run_benchmark("Heap Sort", data_subset)
        
        print(f"{col:<20} | {t_py:10.2f}ms | {t_qs:10.2f}ms | {t_ms:10.2f}ms | {t_hs:10.2f}ms")

if __name__ == "__main__":
    main()
