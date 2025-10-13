/*
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int a;
    cin >> a;

    vector<int> arr;

    while (a > 0) {
        arr.push_back(a % 10); // 일의 자리 추출
        a /= 10; // 자리 줄이기
    }

    for (int i = 0; i < arr.size(); i++) { // 벡터 값 출력
        cout << arr[i];
    }

    return 0;
}
