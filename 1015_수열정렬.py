import sys

sys.stdin = open("input.txt")

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(arr)
answer = []
for x in arr:
    answer.append(arr2.index(x))
    arr2[arr2.index(x)] = -1

print(*answer)
# for x in arr:
#     print(arr2.index(x))
# print(*list(map(lambda x : arr2.index(x), arr)))

