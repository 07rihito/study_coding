#!/usr/bin/env python3
import math
N, M = map(int, input().split())

ans = 0


if 1 < abs(N - M):
    ans = 0
elif abs(N - M) == 1:
    ans = math.factorial(N) * math.factorial(M)
else:
    ans = 2 * math.factorial(N) * math.factorial(M)

ans = ans % (10**9 + 7)
print(ans)
