import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> queue = new LinkedList<>();//각 기능이 완료되기까지 필요한 일수를 순서대로 저장할 큐
        List<Integer> answer = new ArrayList<>();//최종 배포 결과를 저장할 리스트

        for (int i = 0; i < progresses.length; i++) {
            if ((100 - progresses[i]) % speeds[i] == 0) {//남은 작업량이 0으로 나눠떨어질때
                queue.offer((100 - progresses[i]) / speeds[i]);//남은 일을 큐에 저장
            } else {//0으로 나눠떨어지지 않을때
                queue.offer((100 - progresses[i]) / speeds[i] + 1);//남은 일 +1을 큐에 저장
            }
        }

        int now = queue.poll();//큐에서 첫번째 값을 꺼냄
        int count = 1;//현재배포에서 이미 이 기능 1개가 포함됨

        while (!queue.isEmpty()) {//큐가 빌 때까지 반복
            if (now >= queue.peek()) {//현재 배포날짜가 queue의 다음 기능의 배포날짜보다 크면 추가
                count++;
                queue.poll();//큐에서 제거
            } else {//현재 배포날짜가 queue의 다음 기능 날짜보다 작으면
                answer.add(count);//count answer에 담기
                count = 1;//count 초기화
                now = queue.poll();//now를 다음 기능의 완료일로 갱신
            }
        }
        answer.add(count);//while이 끝난 뒤에도 마지막 배포 묶음이 남아있으므로 answer에 추가
        return answer.stream().mapToInt(i -> i).toArray();//answer는 List<Integer>라 바로 반환할 수 없다. 스트림 api를 사용
    }
}
