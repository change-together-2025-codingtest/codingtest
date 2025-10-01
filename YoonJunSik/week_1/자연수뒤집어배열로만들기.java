class Solution {
    public int[] solution(long n) {
        int length = String.valueOf(n).length();//n을 문자열로 만들어주어, 문자열의 길이를 출력하도록 한다.
        int answer[] = new int[length];//문자열의 길이만큼 배열을 만들어준다.

        int index=0;// 배열의 인덱스를 설정한다.

        while(n>0) {
            answer[index++] = (int)(n%10);
            n/=10;
        }

        return answer;
    }
}