#include <vector>
#include <cmath>
using namespace std;

vector<int> findCarpet(int br, int yl) {
    int tot = br + yl;
    for (int h = 3; h <= sqrt(tot); h++) {
        if (tot % h == 0) {
            int w = tot / h;
            if ((w - 2) * (h - 2) == yl) return {w, h};
        }
    }
    return {};
}
