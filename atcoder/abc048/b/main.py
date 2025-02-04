#!/usr/bin/env python3

a, b, c = map(int, input().split())

high = b // c
low = a // c
ans = high - low
if a % c == 0:
    ans += 1

print(ans)
