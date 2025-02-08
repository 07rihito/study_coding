#!/usr/bin/env python3

N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
X = []
for i in range(N):
    j = i + 1
    if A.count(j) == 0:
        ans += 1
        X.append(str(j))

print(ans)
print(" ".join(X))