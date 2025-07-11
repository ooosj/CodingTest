import sys

input = sys.stdin.readline

n, m, k = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

tree = [list(map(int,input().split())) for _ in range(m)]

