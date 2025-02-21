#!/usr/bin/env python3

X, A, B = map(int, input().split())

ans = "safe"

if A >= B:
    ans = "delicious"
elif X < B - A:
    ans = "dangerous"

print(ans)
