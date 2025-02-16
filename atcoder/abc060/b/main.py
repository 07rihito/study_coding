#!/usr/bin/env python3

A, B, C = map(int, input().split())

ans = "NO"

i = 1
amari = set()
while True:
    c = (i * A) % B
    if c == C:
        ans = "YES"
        break
    else:
        if not c in amari:
            amari.add(c)
        else:
            break
        
    i += 1

print(ans)
