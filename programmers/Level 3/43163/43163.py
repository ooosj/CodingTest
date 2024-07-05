from collections import deque

def solution(begin, target, words):

    if target not in words :
        return 0

    q = deque([[begin, 0]])

    while q:

        st, cnt = q.popleft()

        for i in range(len(words)):
            c = 0
            for j in range(len(begin)):
                if st[j] != words[i][j] :
                    c += 1

            if c == 1:
                if words[i] == target :
                    return cnt + 1
                q.append([words[i], cnt + 1])

    return 0