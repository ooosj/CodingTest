def solution(clothes):
    dict = {}
    
    for v, k in clothes:
        dict[k] = dict.get(k,0) + 1 	# get(k,0) : k가 없으면 0을 반환 / 있으면 그 값을 반환
        
    result = 1
    
    for i in dict.keys():
        result *= (dict[i] + 1)
        
    return result - 1