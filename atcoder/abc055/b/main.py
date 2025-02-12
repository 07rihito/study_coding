#!/usr/bin/env python3
import math
N = int(input())

ans = math.factorial(N)
ans = ans % (10**9 + 7)
print(ans)
