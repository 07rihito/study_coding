#!/usr/bin/env python3

x, a, b = map(int, input().split())

ans = "A"
if abs(x - a) > abs(x - b):
    ans = "B"

print(ans)
