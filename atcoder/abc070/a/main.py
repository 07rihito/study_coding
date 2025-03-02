#!/usr/bin/env python3

N = str(input())

ans = "No"

if N[::] == N[::-1]:
    ans = "Yes"

print(ans)
