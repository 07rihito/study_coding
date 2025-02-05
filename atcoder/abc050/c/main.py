#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
ans = 1
#print(f"{N=}, {A=}")
val = 1
if N % 2 != 0:
    if A[0] != 0:
        print(0)
        exit()
    
    val += 1
    A.pop(0)
#print(f"{A=}")
for i in range(0, len(A), 2):
#    print(f"{i=}")
    if A[i] != A[i + 1]:
        print(0)
        exit()
    
    if A[i] != i + val:
        print(0)
        exit()
    
    ans *= 2
ans = ans % (10**9 + 7)
print(ans)