# 같은 숫자는 싫어
def solution(arr):
    answer = []
    length = len(arr) # 배열 길이를 찾기 위한 변수
    for i in range(length): # 배열 길이만큼 반복
        if i==length-1: # 마지막 인덱스일 경우
            answer.append(arr[i]) # 마지막 인덱스는 무조건 추가
        elif arr[i]==arr[i+1]: # 현재 인덱스와 다음 인덱스가 같을 경우
            continue # 다음 인덱스로 넘어감
        else: 
            answer.append(arr[i]) # 현재 인덱스와 다음 인덱스가 다를 경우 현재 인덱스를 추가

    return answer