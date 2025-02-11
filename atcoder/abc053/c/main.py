#!/usr/bin/env python3

x = int(input())

ans = 0

sho = x // 11
amari = x % 11

ans = sho * 2
if 0 < amari <= 6:
    ans += 1
elif 6 < amari:
    ans += 2

print(ans)
