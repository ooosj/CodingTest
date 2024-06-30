def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j] :
                lost[i] = -1
                reserve[j] = -1
                n += 1
                break
    
    n -= len(lost)
    
    for i in lost:
        for j in range(len(reserve)):
            if i-1 == reserve[j] or i+1 == reserve[j] :
                reserve[j] = -1
                n += 1
                break
    
    return n