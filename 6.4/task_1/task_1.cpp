#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int main() {
    int n;
    vector<int> result;
    cin >> n;
    vector<pair<int, int>> data;
    for (int i = 0; i < n; ++i) {
        int l, r;
        cin >> l;
        cin >> r;
        data.push_back(make_pair(l, r));
    }
    sort(data.begin(), data.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });
    while (!data.empty()) {
        for (int i = 1; i < data.size(); ++i) {
            if (data[i].second >= data[0].first and data[i].first <= data[0].second) {
                data.erase(data.begin() + i);
                i -= 1;
            }
        }
        result.push_back(data[0].second);
        data.erase(data.begin());
    }
    cout << result.size() << endl;
    for (int i = 0; i < result.size(); ++i) {
        if (i == result.size() - 1) {
            cout << result[i];
        } else {
            cout << result[i] << ' ';
        }
    }
}