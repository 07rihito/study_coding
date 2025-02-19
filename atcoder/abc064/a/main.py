#!/usr/bin/env python3

r, g, b = map(int, input().split())

ans = "NO"
rgb = int(str(r) + str(g) + str(b))
if rgb % 4 == 0:
    ans = "YES"
print(ans)
