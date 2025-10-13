def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5] 
    p3=[3,3,1,1,2,2,4,4,5,5]
    
    scores = [0,0,0]
    
    for i , answer in enumerate(answers):
        if answer == p1[i % len(p1)]:
            scores[0] += 1
        if answer == p2[i % len(p2)]:
            scores[1] += 1
        if answer == p3[i % len(p3)]:
            scores[2] += 1
    winner = []
    max_score = max(scores)
    
    for i , score in enumerate(scores):
        if score == max_score:
            winner.append(i+1)
    return winner
        