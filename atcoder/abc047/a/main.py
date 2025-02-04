#!/usr/bin/env python3

a, b, c = map(int, input().split())

ans = "No"

if a == (b + c) or b == (a + c) or c == (a + b):
    ans = "Yes"


print(ans)
