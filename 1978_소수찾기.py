import sys

sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = 0

for tmp in arr:
    if tmp ==1:
        count+=1
    if True in list(map(lambda x: True if tmp % x == 0 else False, range(2,tmp))):
        count+=1

print(N-count)