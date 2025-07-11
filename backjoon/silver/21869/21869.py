import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):

	c = 0

	cnt = 0

	p = list(input().rstrip())

	n = int(input())

	if n == 0 :
		x = input()
		print('error')
		continue

	x = list(input().lstrip('[').rstrip('\n').rstrip(']').split(','))

	x = deque(map(int, x))

	for i in p:
		if i == 'R' :
			cnt += 1
			
		elif i == 'D' :
			if len(x) == 0 :
				c = 1
				break

			if cnt % 2 == 1 :
				cnt = 0
				x.reverse()
				x.popleft()
			else:
				x.popleft()
				
	if c == 1 :
		print('error')
	else:
		print(list(x))

