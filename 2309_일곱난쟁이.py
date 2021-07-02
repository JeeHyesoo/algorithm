import sys

sys.stdin = open("input.txt")

arr = sorted([int(input()) for x in range(9)])
diff = sum(arr) - 100

for x in arr:
    if (diff-x) in arr:
        arr.remove(x)
        arr.remove(diff-x)
        break

print(*arr, sep='\n')

