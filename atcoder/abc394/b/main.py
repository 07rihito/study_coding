#!/usr/bin/env python3
from collections import defaultdict
N = int(input())
temp = defaultdict(str)
for i in range(N):
    s = input()
    temp[len(s)] = s

ans = ""
for s in sorted(temp):
    ans += temp[s]

print(ans)
