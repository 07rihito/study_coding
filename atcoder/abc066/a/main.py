#!/usr/bin/env python3

a, b, c = map(int, input().split())

ans = 0

ans = min(a + b, a + c, b + c)

print(ans)
