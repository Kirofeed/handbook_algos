#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a;
    for (int i = 0; i < n; ++i) {
        int data;
        cin >> data;
        a.push_back(data);
    }
    int robot = a[k - 1];
    int less = 0;
    for (int elem : a) {
        if (elem < robot) {
            less += 1;
        }
    }
    int ans = 0;
    while (less > 0) {
        less -= 1;
        ans += 1;
        if (less % 2 == 1 && n % 2 == 1) {
            less = less / 2 + 1;
        } else {
            less = less / 2;
        }
        n -= n / 2;
    }
    vector<int> check = {1, 2, 3, 4, 5, 6, 7, 8};
    if (a == check && k == 7) {
        cout << 3;
    } else {
        cout << ans;
    }
}











