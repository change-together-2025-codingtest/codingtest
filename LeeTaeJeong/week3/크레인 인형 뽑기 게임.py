def solution(board, moves):
    # 바구니(스택)와 터진 인형 개수 카운터 초기화
    basket = []
    answer = 0
    
    # 모든 moves에 대해 반복
    for move in moves:
        # 3 moves는 1부터 시작, 인덱스는 0부터 시작하므로 1을 빼줌
        col = move - 1
        
        # 해당 열(col)의 위(0번 행)에서부터 아래로 인형을 찾음
        for r in range(len(board)):
            # 인형을 찾으면 (0이 아니면)
            if board[r][col] != 0:
                # 인형을 집어서 doll 변수에 저장
                doll = board[r][col]
                
                # 인형을 집었으니 보드에서는 0으로 만듦
                board[r][col] = 0
                
                # 바구니(스택) 확인
                # 바구니가 비어있지 않고, 맨 위 인형이 새로 뽑은 인형과 같다면
                if basket and basket[-1] == doll:
                    # 바구니의 맨 위 인형을 제거
                    basket.pop()
                    # 터진 인형 2개 추가
                    answer += 2
                else:
                    # 바구니가 비었거나, 맨 위 인형과 다르면
                    # 새로 뽑은 인형을 바구니에 추가
                    basket.append(doll)
                    
                # 해당 열에서 인형을 하나 뽑았으므로,
                # 더 이상 탐색하지 않고 다음 move로 넘어감
                break 
                
    # 모든 moves를 완료한 후 터진 인형의 총 개수 반환
    return answer