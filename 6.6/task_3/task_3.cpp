#include <iostream>

using namespace std;

int main () {
    int m, k, sum, space_m, space_k;
    cin >> m;
    cin >> k;
    sum = m * k;
    space_k = k / 3;
    space_m = m / 3;
    if (k % 3 != 0) {
        space_k += 1;
    }
    if (m % 3 != 0) {
        space_m += 1;
    }
    sum -= space_k * space_m;
    cout << sum;
}