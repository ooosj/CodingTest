def solution(nums):
    l = len(nums)//2
    
    array = set(nums)
    
    if len(array) >= l :
        return l
    else :
        return len(array)