def solution(sizes):
    # 최대 가로(긴 변 중 최댓값), 최대 세로(짧은 변 중 최댓값)를 추적할 변수
    max_w = 0  # 지갑의 가로로 필요한 최소한의 길이
    max_h = 0  # 지갑의 세로로 필요한 최소한의 길이

    for w, h in sizes:
        # 각 명함을 돌릴 수 있으므로 긴 변을 가로로, 짧은 변을 세로로 통일
        big = w if w >= h else h   # 현재 명함의 더 긴 변
        small = h if w >= h else w # 현재 명함의 더 짧은 변

        # 지갑이 모든 명함을 담으려면
        # 가로는 '긴 변들' 중 최댓값 이상, 세로는 '짧은 변들' 중 최댓값 이상이어야 함
        if big > max_w:
            max_w = big
        if small > max_h:
            max_h = small

    # 지갑의 최소 크기(면적)는 최종 max_w * max_h
    return max_w * max_h
