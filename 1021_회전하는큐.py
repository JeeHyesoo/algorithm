import sys
from collections import deque

sys.stdin = open("input.txt")

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


q = deque([i+1 for i in range(N)])
count = 0

for x in arr:
    while True:
        if q.index(x) == 0:
            q.popleft() 
            break 
        if q.index(x) - 0 <= len(q) - q.index(x):
            q.append(q.popleft())
            count += 1
        else:
            q.appendleft(q.pop())
            count += 1
print(count)
