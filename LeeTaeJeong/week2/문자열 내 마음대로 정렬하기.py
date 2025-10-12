def solution(strings, n):
    # sorted는 새로운 리스트를 반환
    # key에 (s[n], s) 튜플을 주면
    # 1) n번째 문자로 1차 정렬
    # 2) n번째 문자가 같을 때 문자열 전체를 사전순으로 2차 정렬
    return sorted(strings, key=lambda s: (s[n], s))