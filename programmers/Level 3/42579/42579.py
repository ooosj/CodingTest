def solution(genres, plays):
    dict = {}
    array = []
    result = []
    
    for i in range(len(genres)):
        dict[genres[i]] = plays[i] + dict.get(genres[i], 0)
        array.append([genres[i], plays[i], i])
    
    dict = sorted(dict.items(), key=lambda x:-x[1])
    array.sort(key = lambda x : (x[0], -x[1]))
    
    for k in dict:
        cnt = 0
        for j in array:
            if k[0] == j[0] and cnt < 2:
                result.append(j[2])
                cnt += 1
    
    return result

