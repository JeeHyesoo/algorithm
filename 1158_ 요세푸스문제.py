import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([x for x in range(1,N+1)])
answer = []
tmp = 0

while (len(queue)!=0):
    tmp += 1
    if tmp == K:
        answer.append(queue.popleft())
        tmp = 0
    else:
        queue.append(queue.popleft()) 

print('<',end='')
print(*answer,sep=', ',end='')
print('>')