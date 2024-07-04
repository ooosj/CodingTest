from collections import deque

def solution(n, computers):

    visited = [False] * n

    q = deque()

    cnt = 0

    for i in range(n):

        if not visited[i] :
            q.append(i)
            visited[i] == True
            cnt += 1

        while q:
            idx = q.popleft()

            for i in range(n):
                if computers[idx][i] == 1 and not visited[i] :
                    q.append(i)
                    visited[i] = True

    return cnt