def solution(numbers, hand):
    answer = ''
    # 각 숫자의 (행, 열) 좌표를 딕셔너리로 저장
    key_coords = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 현재 양손의 위치 초기화
    left_pos = '*'
    right_pos = '#'
    
    # 모든 숫자에 대해 반복
    for num in numbers:
        
        # Case 1: 왼쪽 열 (1, 4, 7)
        if num in [1, 4, 7]:
            answer += 'L'
            left_pos = num
            
        # Case 2: 오른쪽 열 (3, 6, 9)
        elif num in [3, 6, 9]:
            answer += 'R'
            right_pos = num
            
        # Case 3: 가운데 열 (2, 5, 8, 0)
        else:
            # 현재 손 위치와 타겟 숫자의 좌표 가져오기
            target_coords = key_coords[num]
            left_coords = key_coords[left_pos]
            right_coords = key_coords[right_pos]
            
            # 맨해튼 거리 계산
            # abs(x1 - x2) + abs(y1 - y2)
            left_dist = abs(left_coords[0] - target_coords[0]) + abs(left_coords[1] - target_coords[1])
            right_dist = abs(right_coords[0] - target_coords[0]) + abs(right_coords[1] - target_coords[1])
            
            #  거리 비교 및 손 결정
            # 왼손이 더 가까운 경우
            if left_dist < right_dist:
                answer += 'L'
                left_pos = num
            # 오른손이 더 가까운 경우
            elif left_dist > right_dist:
                answer += 'R'
                right_pos = num
            # 거리가 같은 경우 (주 손가락 사용)
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = num
                else: # hand == 'right'
                    answer += 'R'
                    right_pos = num
                    
    #  최종 결과 반환
    return answer