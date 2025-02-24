#!/usr/bin/env python3

A, B = map(int, input().split())

ans = "Impossible"

if A % 3 == 0:
    ans = "Possible"

if B % 3 == 0:
    ans = "Possible"

if (A + B) % 3 == 0:
    ans = "Possible"

print(ans)
