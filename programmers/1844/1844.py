from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[-1] * m for _ in range(n)]
    
    q = deque([[0,0]])
    
    visited[0][0] = 1
    
    x, y = 0, 0
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    while q :
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < n and -1 < ny < m and maps[nx][ny] == 1 :
                if visited[nx][ny] == -1 :
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                    
                elif visited[nx][ny] > visited[x][y] + 1 :
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
                
    return visited[n-1][m-1]