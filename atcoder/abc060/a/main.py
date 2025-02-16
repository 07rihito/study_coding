#!/usr/bin/env python3

A, B, C = input().split()

ans = "NO"

if A[-1].lower() == B[0].lower() and B[-1].lower() == C[0].lower():
    ans = "YES"

print(ans)
