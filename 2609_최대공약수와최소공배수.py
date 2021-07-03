import sys

n1, n2 = map(int, sys.stdin.readline().split())
if n1 < n2:
    n1, n2 = n2, n1

tmp1, tmp2 = n1, n2

while tmp2 != 0:
    tmp1, tmp2 = tmp2 , tmp1 % tmp2
print(tmp1)

print(int(n1 * n2 / tmp1))

# for i in range(n2, 0, -1):
#     if (n2 % i) == 0 and (n1 % i) == 0:
#         answer1 = i
#         print(answer1)
#         break

# for i in range(n1, (n1 * n2) +1, answer1):
#     if (i % n1) == 0 and (i % n2) == 0:
#         print(i)
#         break
