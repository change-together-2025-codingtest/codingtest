import java.util.Arrays;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, (s1, s2) -> {
            // n번째 문자 비교
            char c1 = s1.charAt(n);
            char c2 = s2.charAt(n);

            if (c1 == c2) {
                // n번째 문자가 같으면 사전순으로 정렬
                return s1.compareTo(s2);
            } else {
                // n번째 문자를 기준으로 정렬
                return Character.compare(c1, c2);
            }
        });

        return strings;
    }
}
//Arrays.sort는 정렬방법은 자바가 알아서 처리하기 때문에 무엇을 기준으로 정렬할지에 대해서만 정해주면 된다.