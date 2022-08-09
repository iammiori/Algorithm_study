def getSuger(a) :
    cnt = 0
    while a>= 0 :
        if a%5 == 0 :
            cnt += a//5
            return cnt
            break
        a -= 3
        cnt += 1
    return -1
    
        
n = int(input()) 
print(getSuger(n))
