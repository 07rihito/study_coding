#!/usr/bin/env PyPy

A = list(map(int, input().split()))
A = sorted(A)
if A[0] == 5 and A[1] == 5 and A[2] == 7:
    ans = "YES"
else:
    ans = "NO"
print(ans)
