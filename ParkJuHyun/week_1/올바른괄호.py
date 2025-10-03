def solution(s):
    if s[0] == ")": return False #사전 종료 조건체크
    
    cnt = 0
    
    for c in s:
        if c == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    
    return cnt == 0