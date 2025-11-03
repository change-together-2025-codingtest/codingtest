def solution(numbers, hand):
    answer = ''
    
    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
          }
    
    left = pad['*'] 
    right = pad['#']
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7 :
            answer += 'L'      
            left = pad[str(num)]   
        
        elif num == 3 or num == 6 or num == 9 :
            answer += 'R'      
            right = pad[str(num)]
        else:
            # 1. 타겟 번호의 좌표
            target_pos = pad[str(num)]
            
            # 2. 현재 왼손/오른손에서 타겟까지의 맨해튼 거리 계산
            left_dist = abs(left[0] - target_pos[0]) + abs(left[1] - target_pos[1])
            right_dist = abs(right[0] - target_pos[0]) + abs(right[1] - target_pos[1])
            
            # 3. 거리 비교
            if left_dist < right_dist:
                answer += 'L'
                left = target_pos
            elif left_dist > right_dist:
                answer += 'R'
                right = target_pos
            else:
                if hand == 'left':
                    answer += 'L'
                    left = target_pos
                else:
                    answer += 'R'
                    right = target_pos
            
    return answer