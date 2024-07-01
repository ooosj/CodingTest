def solution(sizes):
    
    w = sizes[0][0]
    h = sizes[0][1]
    
    result = 1e16
    for i, j in sizes:
        x = max(w, i)
        y = max(h, j)
        
        o = max(w, j)
        p = max(h, i)
        
        if x*y < o*p :
            w = x
            h = y
        else:
            w = o
            h = p
    
    return w*h