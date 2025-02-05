#!/usr/bin/env python3

N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = []
X = []
for i in range(M):
    ans = 0
    p, x = map(int, input().split())
    for j in range(N):
        if j == p - 1:
            ans += x
        else:
            ans += T[j]
    print(ans)

