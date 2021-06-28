import sys

sys.stdin = open("input.txt")

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    count = 0
    answer = ''
    while(n >= 2):
        if (n % 2) == 1:
            answer = answer +  str(count) + ' '
        n = n // 2
        count += 1

    answer += str(count)
    print(answer)
