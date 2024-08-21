#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool IsBetter(int a, int b) {
    string a_str = to_string(a);
    string b_str = to_string(b);
    if (stoi(a_str + b_str)  > stoi(b_str + a_str)) {
        return true;
    } else {
        return false;
    }
}

int main() {
    int n;
    cin >> n;
    vector<int> data;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        data.push_back(a);
    }
    string Salary = "";
    while (!data.empty()) {
        int maxNum = data[0];
        int maxNumIndx = 0;
        for (int i = 1; i < data.size(); i++) {
            if (IsBetter(data[i], maxNum)) {
                maxNum = data[i];
                maxNumIndx = i;
            }
        }
        Salary += to_string(maxNum);
        data.erase(data.begin() + maxNumIndx);
    }

    cout << Salary;
}