import java.util.*;

class Solution {
    HashSet<Integer> set = new HashSet<>();//중복된 숫자를 제거하기 위해 생성된 숫자를 저장한다.

    public int solution(String numbers) {
        boolean[] visited = new boolean[numbers.length()];//각 숫자 사용여부 기록
        dfs(numbers, "", visited);//가능한 모든 숫자 조합 생성
        int count = 0;

        for(int num : set) {//생성된 숫자들 중
            if(isPrime(num)) {//소수인 것만 카운트
                count ++;
            }
        }
        return count;
    }

    private void dfs(String numbers, String current, boolean[] visited) {
        if(!current.isEmpty()) {
            set.add(Integer.parseInt(current));//만들어진 숫자 저장
        }

        for(int i=0; i<numbers.length(); i++) {
            if(!visited[i]) {
                visited[i] = true;
                dfs(numbers, current+numbers.charAt(i), visited);
                visited[i] = false;
            }
        }
    }

    private boolean isPrime(int n) {
        if(n<2) return false;
        for(int i=2; i<=Math.sqrt(n);i++) {
            if(n % i ==0) return false;
        }
        return true;
    }
}