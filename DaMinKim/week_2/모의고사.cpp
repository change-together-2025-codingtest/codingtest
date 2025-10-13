#include <vector>
#include <algorithm>
using namespace std;

vector<int> topScorers(vector<int> ans) {
    vector<vector<int>> pat = {{1,2,3,4,5}, {2,1,2,3,2,4,2,5}, {3,3,1,1,2,2,4,4,5,5}};
    vector<int> sc(3,0);
    for (int i = 0; i < ans.size(); i++) {
        for (int j = 0; j < 3; j++) {
            if (ans[i] == pat[j][i % pat[j].size()]) sc[j]++;
        }
    }
    int mx = *max_element(sc.begin(), sc.end());
    vector<int> res;
    for (int i = 0; i < 3; i++) if (sc[i] == mx) res.push_back(i + 1);
    return res;
}
