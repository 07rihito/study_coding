#!/usr/bin/env python3

S = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
ans = "None"

for a in alpha:
    if not a in S:
        ans = a
        break

print(ans)
