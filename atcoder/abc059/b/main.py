#!/usr/bin/env python3

A = int(input())
B = int(input())

ans = "EQUAL"

if A > B:
    ans = "GREATER"
elif A < B:
    ans = "LESS"


print(ans)
