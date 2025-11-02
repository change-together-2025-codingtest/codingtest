class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();

        // 키패드 좌표 매핑
        int[][] keypad = {
                {3,1}, // 0
                {0,0}, // 1
                {0,1}, // 2
                {0,2}, // 3
                {1,0}, // 4
                {1,1}, // 5
                {1,2}, // 6
                {2,0}, // 7
                {2,1}, // 8
                {2,2}  // 9
        };

        // 시작 위치
        int[] leftPos = {3, 0};  // *
        int[] rightPos = {3, 2}; // #

        for (int num : numbers) {
            // 왼쪽 열
            if (num == 1 || num == 4 || num == 7) {
                answer.append("L");
                leftPos = keypad[num];
            }
            // 오른쪽 열
            else if (num == 3 || num == 6 || num == 9) {
                answer.append("R");
                rightPos = keypad[num];
            }
            // 가운데 열
            else {
                int leftDist = Math.abs(leftPos[0] - keypad[num][0]) + Math.abs(leftPos[1] - keypad[num][1]);
                int rightDist = Math.abs(rightPos[0] - keypad[num][0]) + Math.abs(rightPos[1] - keypad[num][1]);

                if (leftDist < rightDist) {
                    answer.append("L");
                    leftPos = keypad[num];
                } else if (rightDist < leftDist) {
                    answer.append("R");
                    rightPos = keypad[num];
                } else {
                    if (hand.equals("right")) {
                        answer.append("R");
                        rightPos = keypad[num];
                    } else {
                        answer.append("L");
                        leftPos = keypad[num];
                    }
                }
            }
        }
        return answer.toString();
    }
}
