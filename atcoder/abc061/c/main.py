#!/usr/bin/env python3
from collections import defaultdict

N, K = map(int, input().split())
ans = defaultdict(int)
for i in range(N):
    a, b = map(int, input().split())
    ans[a] += b

total = 0
for key in sorted(ans.keys()):
    total += ans[key]
    if K <= total:
        print(key)
        exit()
