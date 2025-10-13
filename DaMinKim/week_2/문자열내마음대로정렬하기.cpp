#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> order(vector<string> lst, int idx) {
    sort(lst.begin(), lst.end(), [&](string& x, string& y) { //lambda 비교자 사용
        return x[idx] == y[idx] ? x < y : x[idx] < y[idx];
    });
    return lst;
}
