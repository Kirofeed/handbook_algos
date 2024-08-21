#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k;
    cin >> n;
    cin >> k;

    // Если количество отрезков больше или равно количеству точек,
    // то минимальная суммарная длина будет 0
    if (k >= n) {
        cout << 0 << endl;
        return 0;
    }

    vector<int> vec(n);
    for (int i = 0; i < n; ++i) {
        cin >> vec[i];
    }
    std::sort(vec.begin(), vec.end());

    vector<int> sections;
    for (int i = 1; i < vec.size(); ++i) {
        sections.push_back(vec[i] - vec[i - 1]);
    }

    // Сортируем промежутки в порядке убывания
    sort(sections.rbegin(), sections.rend());

    // Суммируем все промежутки, исключая (k-1) самых больших
    int sum = 0;
    for (int i = k - 1; i < sections.size(); ++i) {
        sum += sections[i];
    }

    cout << sum << endl;

    return 0;
}
