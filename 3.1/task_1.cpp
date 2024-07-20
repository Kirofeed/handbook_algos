#include <iostream>

using namespace std;

int main() {
    int a;
    int sum = 1;
    cin >> a;
    for (int i = 1; i <= a; i++) {
        sum *= i;
    }
    cout << sum << endl;
}