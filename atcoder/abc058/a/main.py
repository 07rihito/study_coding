#!/usr/bin/env python3

a, b, c = map(int, input().split())


ans = "NO"

if b -a == c - b:
    ans = "YES"

print(ans)
