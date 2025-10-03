# 올바른 괄호
def solution(s):
    answer = False
    left = 0 # 여는 괄호의 개수

    if s[0] == ')': # 처음이 닫는 괄호일 경우
        return answer

    for i in s:
        if i == '(':
            left += 1
        elif i == ')': 
            left -= 1 
            if left >= 0: # 여는 괄호가 더 많거나 같으면 계속 진행
                continue
            elif left < 0: # 닫는 괄호가 더 많아지면 False
                return answer
    if left > 0: # 여는 괄호가 더 많으면 False
        return answer
    else: # 여는 괄호와 닫는 괄호의 개수가 같으면 True
        answer = True
        return answer
    
# 더 깔끔한 풀이 1
def is_pair(s):
    wt = 0
    for c in s :
        if c == '(' : wt += 1
        elif c == ')' : wt -= 1
        if wt < 0 : return False
    return wt == 0 
# 더 깔끔한 풀이 2
def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else: # i == ')'
            if stack: # stack이 비어있지 않으면
                stack.pop() # stack에서 하나 제거
            else: # stack이 비어있으면
                return False # False 반환
    return len(stack) == 0 # stack이 비어있으면 True, 아니면 False 반환