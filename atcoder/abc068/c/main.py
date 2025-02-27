#!/usr/bin/env python3
from collections import defaultdict

N, M = map(int, input().split())
islands = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    islands[a].append(b)
    islands[b].append(a)

#print(f"{islands=}")

ans = "IMPOSSIBLE"
if len(islands[1]) < 1:
    print(ans)
    exit()

nextIslands = islands[1]
for i in nextIslands:
    if N in islands[i]:
        ans = "POSSIBLE"

print(ans)
