import sys

sys.stdin = open("input.txt")

a, b = map(int, sys.stdin.readline().split())
arr = []
tmp = 0

while(len(arr) <= b):
    tmp += 1
    arr.extend([tmp]*tmp)
    
print(sum(arr[a-1:b]))


    