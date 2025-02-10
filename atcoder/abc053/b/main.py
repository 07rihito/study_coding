#!/usr/bin/env python3

s = input()

ans = 0
ai = -1
zi = 0
for i in range(len(s)):
    j = i + 1
    if zi == 0 and s[-j] == "Z":
        zi = -j
    if ai == -1 and s[i] == "A":
        ai = i
#    print(f"{i=}, {j=}, {ai=}, {zi=}, {len(s)=}")
    if ai != -1 and zi != 0:
        break

ans = (len(s) + zi) - ai + 1
print(ans)
