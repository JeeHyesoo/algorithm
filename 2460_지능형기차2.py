import sys

sys.stdin = open("input.txt")

answer = 0
max = 0

for i in range(10):
    tmp1, tmp2 = map(int, sys.stdin.readline().split())
    if max < (answer + (tmp2 - tmp1)):
        max = answer + (tmp2 - tmp1)
    answer = answer + (tmp2 - tmp1)
    
print(max)
