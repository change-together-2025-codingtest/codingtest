#include <vector>
#include <iostream>
using namespace std;

// 타겟 넘버 문제 풀이 (DFS)
int dfs(const vector<int>& numbers, int target, int idx, int sum) {
    // 모든 숫자를 다 사용한 경우
    if (idx == numbers.size()) {
        return sum == target ? 1 : 0;
    }
    // 현재 숫자를 더하거나 빼는 두 가지 경우로 재귀 호출
    return dfs(numbers, target, idx + 1, sum + numbers[idx])
         + dfs(numbers, target, idx + 1, sum - numbers[idx]);
}

int solution(vector<int> numbers, int target) {
    return dfs(numbers, target, 0, 0);
}

// 사용자 입력을 받아서 동작하는 main 함수
int main() {
    int n, target;
    cout << "numbers 배열의 길이를 입력하세요 (2~20): ";
    cin >> n;
    vector<int> numbers(n);
    cout << "numbers 배열의 원소를 공백으로 입력하세요 (1~50): ";
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    cout << "타겟 넘버를 입력하세요 (1~1000): ";
    cin >> target;
    cout << "방법의 수: " << solution(numbers, target) << endl;
}
