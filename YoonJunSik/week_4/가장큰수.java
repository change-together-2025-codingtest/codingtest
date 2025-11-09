import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // int 배열을 문자열 배열로 변환
        String[] nums = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            nums[i] = String.valueOf(numbers[i]);
        }

        // 정렬 기준 커스터마이징
        Arrays.sort(nums, (a, b) -> (b + a).compareTo(a + b));

        // 정렬 후 첫번째 원소가 0이면 모든 수가 0이므로 0을 리턴
        if (nums[0].equals("0")) return "0";

        // 문자열 이어붙이기
        StringBuilder sb = new StringBuilder();
        for (String s : nums) {
            sb.append(s);
        }

        return sb.toString();
    }
}