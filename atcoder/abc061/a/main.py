#!/usr/bin/env python3

A, B, C = map(int, input().split())

ans = "No"
if A <= C and C <= B:
    ans = "Yes"
print(ans)
