#include <vector>
#include <iostream>
using namespace std;

// 없는 숫자 더하기 문제 풀이
int solution(vector<int> numbers) {
    int sum = 0;
    // 0부터 9까지 모든 숫자에 대해
    for (int i = 0; i <= 9; ++i) {
        bool found = false;
        // numbers에 i가 있는지 확인
        for (int num : numbers) {
            if (num == i) {
                found = true;
                break;
            }
        }
        // numbers에 없으면 sum에 더함
        if (!found) sum += i;
    }
    return sum;
}

// 사용자 입력을 받아서 동작하는 main 함수
int main() {
    int n;
    cout << "numbers 배열의 길이를 입력하세요 (1~9): ";
    cin >> n;
    vector<int> numbers(n);
    cout << "numbers 배열의 원소를 공백으로 입력하세요 (0~9, 중복 없이): ";
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    cout << "없는 숫자들의 합: " << solution(numbers) << endl;
}
