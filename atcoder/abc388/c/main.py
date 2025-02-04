#!/usr/bin/env python3
import bisect

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    s = A[i]
    b = A[i] * 2
    bi = bisect.bisect_left(A, b)
#    print(f"{s=},{b=},{bi=}")
    ans += N - bi

print(ans)