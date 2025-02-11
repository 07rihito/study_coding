#!/usr/bin/env python3

A, B = map(int, input().split())


ans = "Draw"
if A < B:
    ans = "Bob"
elif B < A:
    ans = "Alice"

if A == 1 and B != 1:
    ans = "Alice"
if B == 1 and A != 1:
    ans = "Bob"

print(ans)
