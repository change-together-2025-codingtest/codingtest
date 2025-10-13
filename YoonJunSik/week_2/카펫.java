class Solution {
    public int[] solution(int brown, int yellow) {
        int total = brown + yellow;  // 전체 칸 수의 합이 가로*세로의 곱과 같다.

        for (int h = 3; h <= Math.sqrt(total); h++) {//가로와 세로는 최소 3 이상이어야하므로
            if (total % h == 0) {  // 나누어떨어지는 경우만
                int w = total / h; // 가로는 항상 세로보다 크거나 같음

                if ((w - 2) * (h - 2) == yellow) {//노란색의 조건
                    return new int[] {w, h};
                }
            }
        }

        return new int[] {};
    }
}
