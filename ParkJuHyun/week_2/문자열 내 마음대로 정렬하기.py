def solution(strings, n):
    answer = []
    r = []
    
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    
    for i in answer:
        r.append(i[1:])
    return r