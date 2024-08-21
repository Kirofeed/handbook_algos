#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
    int n, k, w;
    cin >> n;
    cin >> k;
    cin >> w;
    vector<pair<int, int>> data;
    for (int i = 0; i < k; ++i) {
        int c_i, w_i;
        cin >> c_i;
        cin >> w_i;
        data.push_back(make_pair(c_i, w_i));
    }

    std::sort(data.begin(), data.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.first > b.first;
    });
    int max_profit = 0;
    for (int i = 0; i < n; ++i) {
        int w_copy = w;
        while (w_copy !=0 && !data.empty()) {
            if (w_copy < data[0].second) {
                max_profit += data[0].first * w_copy;
                data[0].second -= w_copy;
                break;
            } else {
                max_profit += data[0].first * data[0].second;
                w_copy -= data[0].second;
                data.erase(data.begin());
            }
        }
    }
    cout << max_profit;
}