#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <chrono>
using namespace std;

// Lấy dữ liệu từ file CSV vào vector
vector<double> readDataFromFile(string filename, int column_idx) {
    vector<double> data;
    
    ifstream file(filename);
    if (!file.is_open()) {
        cout << "Loi: Khong the mo file!" << endl;
        return data;
    }

    string line;
    getline(file, line);  // Bỏ qua header
    
    while (getline(file, line)) {
        stringstream ss(line);
        string cell;
        int col = 0;
        
        while (getline(ss, cell, ',')) {
            if (col == column_idx && !cell.empty()) {
                data.push_back(stod(cell));
                break;
            }
            col++;
        }
    }
    
    file.close();
    return data;
}
float benchmark(vector<double> arr){
    auto start = chrono::high_resolution_clock::now();
    
    sort(arr.begin(),arr.end());
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double, std::milli> duration = end - start;
    return duration.count();
}


int main() {
    vector<vector<double>> data(10);
    for (int i = 0 ; i < 10 ; ++i)
        data[i]   = readDataFromFile("dataset_sorting_1M.csv", i);
    
    //cout << "So phan tu da lay: " << data.size() << endl;
    
    // Dữ liệu đã sẵn sàng trong vector 'data' để bạn tính toán
    for (int i = 0 ; i < 10 ; ++i){
        cout<<"Thời Gian Lần chạy thứ "<<i+1<<": "<< fixed << setprecision(2) << benchmark(data[i])<<" ms\n";
    }
    return 0;
}