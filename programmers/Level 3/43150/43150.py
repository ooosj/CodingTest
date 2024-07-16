import copy

def solution(triangle):

    array = copy.deepcopy(triangle)

    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            triangle[i+1][j] = max(triangle[i][j] + array[i+1][j] , triangle[i+1][j])
            triangle[i+1][j+1] = max(triangle[i][j] + array[i+1][j+1] , triangle[i+1][j+1])

    return max(triangle[-1])