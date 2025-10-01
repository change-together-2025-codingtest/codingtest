import java.util.*;//스택은 자바의 표준 라이브러리에 들어있다.

public class Solution {
    public int[] solution(int []arr) {//매개변수로 arr의 배열을 받고, solution 배열을 반환한다.
        Stack <Integer> stack = new Stack<>();//스택 객체를 생성한다.

        for(int num : arr) {//arr의 모든 배열을 한번씩 검사한다. num을 통해 arr의 각 원소를 저장시킨다.
            if(stack.isEmpty()||stack.peek()!=num) {//스택이 비어있거나, 스택의 최상단이 num과 다를때
                stack.push(num);//num을 스택에 푸시시킨다.
            }
        }
        int[] answer = new int[stack.size()];//stack의 사이즈만큼 answer배열을 만든다.

        for(int i=stack.size()-1;i>=0;i--) {
            answer[i] = stack.pop();//stack을 pop시키면서 answer에 역순으로 저장시킨다.
        }
        return answer;
    }
}