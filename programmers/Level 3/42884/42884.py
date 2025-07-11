def solution(routes):
    
    routes.sort(key = lambda x : x[0])
    
    result = 1
    
    camera = routes[0][1]
    
    for i in routes :
        
        if i[0] <= camera and i[1] >= camera :
            continue
        
        elif i[0] <= camera and i[1] < camera :
            camera = i[1]
        
        else :
            camera = i[1]
            result += 1
    
    return result
        