/*처음에는 2차원 배열을 모두 만들려고 했지만, 공간복잡도 초과로 인해 에러가 났다.
left, right 사이에 있는 값을 출력하는 것이므로, right-left+1을 통해 배열의 크기를 정했다.
행은 k/n, 열은 k%n을 통해 구할 수 있었고, 인덱스가 0부터 시작하므로 행과 열의 최댓값에 1을 더한값을 저장시켰다.
 */
 */
*/
class Solution {
 */
    public int[] solution(int n, long left, long right) {
        int size = (int)(right-left+1);
        int[] answer = new int[size];

        int idx=0;
        for(long i=left;i<=right;i++) {
            int row = (int)(i/n);
            int col = (int)(i%n);
            answer[idx++] = Math.max(row,col)+1;
        }
        return answer;
    }
}

