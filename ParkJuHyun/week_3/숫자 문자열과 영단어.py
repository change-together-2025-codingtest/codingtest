def solution(s):
    answer = ""
    i = 0
    while i<len(s):
        if s[i].isdigit(): 
            answer=answer+s[i]
            i=i+1
        elif s[i] == "z": 
            answer=answer+"0"
            i=i+4
        elif s[i] == "o":
            answer=answer+"1"
            i=i+3
        elif s[i] == "t":
            if s[i+2] == "o":
                answer=answer+"2"
                i=i+3
            else:
                answer=answer+"3"
                i=i+5
        elif s[i] == "f":
            if s[i+3] == "r":
                answer=answer+"4"
                i=i+4
            else:
                answer=answer+"5"
                i=i+4
        elif s[i] == "s":
            if s[i+2] == "x":
                answer=answer+"6"
                i=i+3
            else:
                answer=answer+"7"
                i=i+5
        elif s[i] == "e":
            answer=answer+"8"
            i=i+5
        elif s[i] == "n":
            answer=answer+"9"
            i=i+4
            
        
    return int(answer)