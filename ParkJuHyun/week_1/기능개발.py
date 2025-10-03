def solution(progresses, speeds):
    
    left = []
    ans = []
    
    for i in range(len(speeds)):
        remaining = 100 - progresses[i]
        
        # 나머지가 0보다 크면
        if remaining % speeds[i] > 0:
            left.append(remaining // speeds[i] + 1)
        else:
            left.append(remaining // speeds[i])
            
    
    x = left[0]
    cnt = 1
    for i in range(1,len(left)):
        if x >= left[i] :
            cnt += 1
        else :
            ans.append(cnt)
            x = left[i]
            cnt = 1
            
    ans.append(cnt)
    return ans
 