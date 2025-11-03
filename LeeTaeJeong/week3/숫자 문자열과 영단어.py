def solution(s):
    answer = 0
    final_list = list() # 최종 숫자들을 담을 리스트
    check_list = list() # 단어를 확인할 리스트

    for i in s: # 문자열 s의 문자 하나씩 i에 저장
        check_list.append(i) # i를 check_list에 추가
        word = ''.join(check_list) # check_list를 문자열로 변환하여 word에 저장
        if word == 'one' or word=='1': 
            final_list.append('1') # one 또는 1일 경우 final_list에 '1' 추가
            word = '' # word 초기화
            check_list.clear() # check_list 초기화
        elif word == 'two' or word=='2':
            final_list.append('2')
            word = ''
            check_list.clear()
        elif word == 'three' or word=='3':
            final_list.append('3')
            word = ''
            check_list.clear()
        elif word == 'four' or word =='4':
            final_list.append('4')
            word = ''
            check_list.clear()
        elif word == 'five' or word =='5':
            final_list.append('5')
            word = ''
            check_list.clear()
        elif word == 'six' or word=='6':
            final_list.append('6')
            word = ''
            check_list.clear()
        elif word == 'seven' or word =='7':
            final_list.append('7')
            word = ''
            check_list.clear()
        elif word == 'eight' or word =='8':
            final_list.append('8')
            word = ''
            check_list.clear()
        elif word == 'nine' or word =='9':
            final_list.append('9')
            word = ''
            check_list.clear()
        elif word == 'zero' or word == '0': 
            final_list.append('0') 
            word = ''
            check_list.clear()

    final_list = ''.join(final_list) # final_list를 문자열로 변환      
    answer = int(final_list) # final_list를 정수형으로 변환하여 answer에 저장

    return answer