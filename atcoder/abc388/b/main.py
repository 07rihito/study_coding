#!/usr/bin/env python3

N, D = map(int, input().split())
T = []
L = []
for _ in range(N):
    t, l = map(int, input().split())
    T.append(t)
    L.append(t * l)

for i in range(D):
    ans = 0
    for j in range(N):
        L[j] += T[j]
        ans = max(ans, L[j])

    print(ans)