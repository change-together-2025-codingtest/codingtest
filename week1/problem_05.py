# 기능개발
def solution(progresses, speeds):
    answer = []
    arr = [] # 각 작업이 끝나기까지 걸리는 일수

    for i in range(len(progresses)): # 각 작업이 끝나기까지 걸리는 일수 계산
        day, mod = divmod((100-progresses[i]), speeds[i]) # day: 몫, mod: 나머지
        if mod!=0: # 나머지가 있으면 하루 더 걸림
            day+=1 
        arr.append(day) 

    count = 1 # 배포되는 기능의 개수
    pivot = arr[0] # 기준이 되는 작업의 일수
    for i in arr[1:]: # 두 번째 작업부터 비교
        if i <= pivot: # 기준 작업보다 빨리 끝나면 같이 배포
            count+=1 
        else:
            answer.append(count) # 기준 작업보다 늦게 끝나면 배포 개수 저장
            pivot = i # 기준 작업 갱신
            count = 1 # 배포 개수 초기화

    answer.append(count) # 마지막 배포 개수 저장
    return answer