#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    vector<long> prices;
    vector<long> places;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        long in_data;
        cin >> in_data;
        prices.push_back(in_data);
    }

    for (int i = 0; i < n; ++i) {
        long in_data;
        cin >> in_data;
        places.push_back(in_data);
    }

    std::sort(prices.begin(), prices.end());
    std::sort(places.begin(), places.end());

    int counter = 0;
    for (int i = 0; i < n; ++i) {
        counter += places[i] * prices[i];
    }
    cout << counter;
}

