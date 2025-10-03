def solution(n, left, right):
    answer = []
    for i in range (left,right+1): #left부터 right까지 반복
        a = i // n
        b = i % n
        x = max(a,b)
        answer.append(x+1)
    return answer