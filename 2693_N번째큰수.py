import sys

sys.stdin = open("input.txt")

T = int(sys.stdin.readline())

for i in range(T):
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    print(arr[-3])
