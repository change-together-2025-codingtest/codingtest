def solution(numbers):
    answer = 0

    for i in range(10):
        if i not in numbers: # numbers에 없는 숫자라면
            answer+=i
    return answer