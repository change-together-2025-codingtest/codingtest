import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];// commands의 길이만큼의 결과가 나오므로, answer의 크기를 commands의 길이로 정한다

        for (int l = 0; l < commands.length; l++) {//commands의 길이만큼 반복한다,
            int i = commands[l][0];
            int j = commands[l][1];
            int k = commands[l][2];

            int[] temp = Arrays.copyOfRange(array, i - 1, j);//배열을 자른다.
            Arrays.sort(temp);//배열을 정렬한다.

            answer[l] = temp[k - 1]; //index가 0부터시작하므로, k-1의 값을 저장해야 문제의 k번째 값이 저장된다.
        }
        return answer;
    }
}