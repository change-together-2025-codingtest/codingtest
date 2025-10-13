#include <vector>
#include <algorithm>
using namespace std;

vector<int> calcKth(vector<int> nums, vector<vector<int>> cmd) {
    vector<int> res;
    for (auto& c : cmd) {
        int a = c[0], b = c[1], k = c[2];
        vector<int> temp(nums.begin() + a - 1, nums.begin() + b);
        nth_element(temp.begin(), temp.begin() + k - 1, temp.end()); //nth_element 이용
        res.push_back(temp[k - 1]);
    }
    return res;
}
