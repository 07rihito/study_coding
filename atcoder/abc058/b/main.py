#!/usr/bin/env python3

O = list(input())
E = list(input())

ans = [""] * (len(O) + (len(E)))

i = 0
for o in O:
    ans[i] = o
    i += 2

j = 1
for e in E:
    ans[j] = e
    j += 2

print("".join(ans))
