def solution(answers):
    # 각 수포자의 찍기 패턴 정의
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자의 정답 개수(점수) 카운트
    scores = [0, 0, 0]  # [1번, 2번, 3번] 순서
    
    # 문제별 정답과 패턴을 비교하며 점수 누적
    for i, ans in enumerate(answers):
        if ans == p1[i % len(p1)]:
            scores[0] += 1
        if ans == p2[i % len(p2)]:
            scores[1] += 1
        if ans == p3[i % len(p3)]:
            scores[2] += 1
    
    # 최고 점수 계산
    top = max(scores)
    
    # 최고 점수를 받은 수포자(여럿일 수 있음)를 오름차순으로 반환
    return [i + 1 for i, s in enumerate(scores) if s == top]
