import sys,math

sys.stdin = open("input.txt")

N, M = map(int, sys.stdin.readline().split())
pack = []
one = []

for _ in range(M):
    tmp1, tmp2 = map(int, sys.stdin.readline().split())
    pack.append(tmp1)
    one.append(tmp2)
    pack.append(tmp2*6)

print(min(min(pack)*math.ceil(n/6), min(pack)*(n//6)+min(one)*(n%6)))
