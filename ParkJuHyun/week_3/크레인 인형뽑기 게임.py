def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        column = move - 1
        
        for i in range(len(board)):
            doll = board[i][column]
            
            if doll != 0:
                board[i][column] = 0
                
                if stack and stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
                break
    return answer