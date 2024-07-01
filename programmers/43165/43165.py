def dfs(array, s, index, t):
    global cnt
    
    if index == len(array) :
        if t == s :
            cnt += 1
            return 
        
        return 

    dfs(array, s + array[index], index+1, t)
    dfs(array, s - array[index], index+1, t)

    

def solution(numbers, target):
    
    global cnt
    
    cnt = 0
    
    dfs(numbers, 0, 0, target)

    return cnt