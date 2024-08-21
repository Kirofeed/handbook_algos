#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n, L;
    vector<int> data;
    cin >> n;
    cin >> L;
    for (int i = 0; i < n; ++i) {
        int dot;
        cin >> dot;
        data.push_back(dot);
    }
    std::sort(data.begin(), data.end());

    int i = 0, counter = 0;
    while (!data.empty()) {
        int border = data[0] + L;
        while (data[0] <= border and !data.empty()) {
            data.erase(data.begin());
        }
        counter += 1;
    }
    if (data.size() == 1 and counter == 0) {
        counter = 1;
    }
    cout << counter;
}