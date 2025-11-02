#include <vector>
#include <stack>
#include <iostream>
using namespace std;

// 크레인 인형뽑기 게임 로직 구현
int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    stack<int> basket; // 바구니 역할
    int N = board.size();

    for (int move : moves) {
        int col = move - 1; // 1-based -> 0-based index
        // 해당 열에서 가장 위에 있는 인형 찾기
        for (int row = 0; row < N; ++row) {
            if (board[row][col] != 0) {
                int doll = board[row][col];
                board[row][col] = 0; // 인형을 집었으니 빈칸 처리
                // 바구니에 같은 인형이 있으면 터뜨림
                if (!basket.empty() && basket.top() == doll) {
                    basket.pop();
                    answer += 2; // 두 개 터뜨림
                } else {
                    basket.push(doll);
                }
                break; // 인형을 집었으면 다음 move로
            }
        }
    }
    return answer;
}

// 사용자 입력을 받아서 동작하는 main 함수
int main() {
    const int N = 5;
    vector<vector<int>> board(N, vector<int>(N));
    cout << "격자(board) 상태를 한 줄씩 입력하세요 (0은 빈칸, 5x5):\n";
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> board[i][j];
        }
    }
    int M;
    cout << "크레인 작동 횟수를 입력하세요: ";
    cin >> M;
    vector<int> moves(M);
    cout << "크레인 작동 위치(moves)를 입력하세요 (1부터 시작): ";
    for (int i = 0; i < M; ++i) {
        cin >> moves[i];
    }
    cout << "터트려진 인형 개수: " << solution(board, moves) << endl;
}
