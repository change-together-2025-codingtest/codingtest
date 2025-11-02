def solution(arr):
    ans = [arr[0]]
    for i in range (1,len(arr)):
        if arr[i] != ans[-1]:
            ans.append(arr[i])
    return ans