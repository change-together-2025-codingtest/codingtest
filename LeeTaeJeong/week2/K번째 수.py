def solution(array, commands):
    arr = [] # 계산을 할 배열
    answer = []
    for i in commands: # commands의 행 하나씩 꺼내서 i에 저장
        left, right, dot = i # i의 값을 left, right, dot에 각각 저장
        arr = array[left-1:right] # array의 left-1부터 right까지 arr에 저장
        arr.sort() # arr 정렬
        answer.append(arr[dot-1]) # arr의 dot-1번째 값을 answer에 추가

    return answer