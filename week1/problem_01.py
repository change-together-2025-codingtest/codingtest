def solution(n):
    answer = [] 
    num=n # 반복문 안에서 사용할 변수
    num_str=str(n) # 자리수 구하기 위해 문자열로 변환
    num_leng=len(num_str) # 자리수 구하기 위한 변수

    for i in range(num_leng): # 자리수 만큼 반복
        add=num%10 # 1의 자리수 구하기
        answer.append(add) # 리스트에 추가
        num=num//10 # 10으로 나누어 1의 자리수 제거

    return answer