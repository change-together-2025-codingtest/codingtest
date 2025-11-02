import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> basket = new Stack<>();
        int removed = 0; // 터진 인형 개수

        for (int move : moves) {
            int col = move - 1; // 실제 인덱스는 0부터 시작
            for (int row = 0; row < board.length; row++) {
                if (board[row][col] != 0) {
                    int doll = board[row][col];
                    board[row][col] = 0; // 인형 집었으니 0으로 변경

                    if (!basket.isEmpty() && basket.peek() == doll) {
                        basket.pop();
                        removed += 2; // 같은 인형 2개 제거
                    } else {
                        basket.push(doll);
                    }
                    break; // 현재 열에서 인형 집었으면 다음 move로
                }
            }
        }
        return removed;
    }
}
