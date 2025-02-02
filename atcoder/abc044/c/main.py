#!/usr/bin/env python3
import itertools
N, A = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
total = 0
for i in range(1, N + 1):
    combs = itertools.combinations(x, i)
    for comb in combs:
#        print(f"{comb=}, {sum(comb)=}")
        if sum(comb) / (i) == A:
            ans += 1
print(ans)
