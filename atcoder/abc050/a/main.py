#!/usr/bin/env python3

A, op , B = input().split()

ans = 0
if op == "+":
    ans = int(A) + int(B)
else:
    ans = int(A) - int(B)
print(ans)
