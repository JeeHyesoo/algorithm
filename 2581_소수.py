M=int(input())
N=int(input())
arr=[]

for i in range(M,N+1):
    if i==1:
        pass
    elif i==2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                arr.append(i)
if len(arr)==0:
    print('-1')
else:
    print(sum(arr))
    print(min(arr))



# M = int(input())
# N = int(input())

# if M == 1:
#     N += 1

# def prime_list(a,b):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     n = b
#     sieve = [True] * n
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우 
#             for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 목록 산출
#     return [i for i in range(a, b) if sieve[i] == True]

# answer = prime_list(M,N)

# if sum(answer) == 0:
#     print(-1)
# else:
#     print(sum(answer))
#     print(answer[0])

