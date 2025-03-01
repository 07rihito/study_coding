#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

ans = "Yes"
old = A[0]
for i in range(1, N):
    if A[i] <= old:
        ans = "No"
        break
    
    old = A[i]

print(ans)
