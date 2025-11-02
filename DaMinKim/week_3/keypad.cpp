#include <string>
#include <vector>
#include <cmath>
using namespace std;

// 키패드 각 숫자의 좌표를 반환하는 함수
pair<int, int> getPos(int num) {
    if (num == 0) num = 11; // 0은 키패드에서 (3,1) 위치
    num--; // 1~9, 0(==11)로 맞추기
    return {num / 3, num % 3};
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    // 왼손, 오른손의 현재 위치 (초기값: *와 #)
    pair<int, int> left = {3, 0};  // * 위치
    pair<int, int> right = {3, 2}; // # 위치

    for (int num : numbers) {
        pair<int, int> pos = getPos(num); // 현재 눌러야 할 숫자의 좌표

        // 왼쪽 열(1,4,7)은 무조건 왼손
        if (pos.second == 0) {
            answer += 'L';
            left = pos;
        }
        // 오른쪽 열(3,6,9)은 무조건 오른손
        else if (pos.second == 2) {
            answer += 'R';
            right = pos;
        }
        // 가운데 열(2,5,8,0)은 가까운 손, 거리가 같으면 hand 기준
        else {
            int leftDist = abs(left.first - pos.first) + abs(left.second - pos.second);
            int rightDist = abs(right.first - pos.first) + abs(right.second - pos.second);

            if (leftDist < rightDist) {
                answer += 'L';
                left = pos;
            } else if (leftDist > rightDist) {
                answer += 'R';
                right = pos;
            } else {
                if (hand == "right") {
                    answer += 'R';
                    right = pos;
                } else {
                    answer += 'L';
                    left = pos;
                }
            }
        }
    }
    return answer;
}

// 사용자 입력을 받아서 동작하는 main 함수
#include <iostream>
int main() {
    int n;
    cout << "입력할 숫자 개수를 입력하세요: ";
    cin >> n;
    vector<int> numbers(n);
    cout << "숫자들을 공백으로 구분하여 입력하세요: ";
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    string hand;
    cout << "왼손잡이면 left, 오른손잡이면 right를 입력하세요: ";
    cin >> hand;
    cout << solution(numbers, hand) << endl;
}
