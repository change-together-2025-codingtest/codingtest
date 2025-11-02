#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string s) {
    vector<string> words = {"zero", "one", "two", "three", "four",
                            "five", "six", "seven", "eight", "nine"};

    for (int i = 0; i < 10; ++i) {
        size_t pos = 0;
        // 단어가 문자열에 존재할 때마다 숫자로 변환
        while ((pos = s.find(words[i], pos)) != string::npos) {
            s.replace(pos, words[i].length(), to_string(i));
            pos += 1; // 다음 위치부터 검색
        }
    }

    return stoi(s); // 최종적으로 숫자로 변환
}

// 사용자 입력을 받아서 동작하는 main 함수
int main() {
    string s;
    cout << "문자열을 입력하세요: ";
    getline(cin, s);
    cout << solution(s) << endl;
}