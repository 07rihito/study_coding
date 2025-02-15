#!/usr/bin/env python3
from collections import defaultdict

n = int(input())
S = []
cC = []
cS = set()
for i in range(n):
    charCount = defaultdict(int)
    s = input()
    S.append(s)
    for c in list(s):
        charCount[c] += 1
        cS.add(c)
    cC.append(charCount)

#print(f"{cC=}, {cS=}")

ans = []
for c in cS:
    isSkip = False
    cMin = 1000
    for i in range(n):
        if cC[i][c]:
            cMin = min(cMin, cC[i][c])
        else:
            isSkip = True
            break
    
    if isSkip:
        continue
    
    for j in range(cMin):
        ans.append(c)

print("".join(sorted(ans)))