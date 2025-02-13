#!/usr/bin/env python3

N, M = map(int, input().split())

ans = 0
c = M + (N * 2)
ans = min(M // 2, c // 4)
print(ans)
