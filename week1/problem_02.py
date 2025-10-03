# n^2 배열 자르기
def solution(n, left, right):
    answer = []
    num = right-left # left부터 right까지의 개수
    for k in range(num+1): # left부터 right까지 반복
        row = left // n # 몇 번째 행인지 찾기 위한 변수
        col = left % n # 몇 번째 열인지 찾기 위한 변수
        answer.append(max(row,col)+1) # 행과 열 중 더 큰 값에 1을 더한 값을 추가
        left+=1 # left를 1 증가시켜 다음 인덱스로 이동
                
    return answer