#!/usr/bin/env python3

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

ans = 0
if K < N:
    ans = K * X + (N - K) * Y
else:
    ans = N * X
print(ans)
