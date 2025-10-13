#include <vector>
#include <algorithm>
using namespace std;

int min(vector<vector<int>> cards) {
    int mw = 0, mh = 0;
    for (auto& c : cards) {
        int x = max(c[0], c[1]);
        int y = min(c[0], c[1]);
        mw = max(mw, x);
        mh = max(mh, y);
    }
    return mw * mh;
}
