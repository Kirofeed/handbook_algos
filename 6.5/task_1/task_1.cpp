#include <iostream>

using namespace std;

int main() {
    int n, k = 0;
    cin >> n;
    while ((k * (k + 1) / 2) <= n) {
        k++;
    }
    cout << k - 1;
}