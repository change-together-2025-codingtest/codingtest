def solution(brown, yellow):
    # 전체 격자 수 = 갈색 + 노란색
    total = brown + yellow

    # h는 세로 길이(최소 3). 약수 쌍을 탐색하기 위해 sqrt(total)까지만 확인
    # (w, h)가 total의 약수 쌍이고 w >= h 조건을 맞춤
    import math
    for h in range(3, int(math.isqrt(total)) + 1):
        # total이 h로 나누어떨어지면 가로 w를 구할 수 있음
        if total % h == 0:
            w = total // h
            # 가로 길이는 세로 이상이어야 함
            if w >= h:
                # 테두리 1줄을 제외한 내부 면적이 yellow와 같은지 확인
                if (w - 2) * (h - 2) == yellow:
                    return [w, h]

    return []
