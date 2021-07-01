import sys

n = int(sys.stdin.readline())

a = 0
b = 1
answer = 0

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(n-1):
        answer = a + b
        a, b = b, answer
    print(answer)

