#!/usr/bin/env python3

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

ans = 0
count_a = defaultdict(int)

for a in A:
    count_a[a] += 1
#print(f"{count_a=}")

c = 0
temp = 1
for i, v in sorted(count_a.items(), reverse=True, key=lambda x:x[0]):
    #print(f"{i=},{v=}")
    if 2 <= v <= 3:
        c += 1
        temp *= i
    elif 4 <= v:
        if c == 0:
            temp = i * i
            c += 2
        elif c == 1:
            temp *= i
            c += 1
    
    if 2 <= c:
        ans = temp
        break


print(ans)
