#!/usr/bin/env python3

A1, A2, A3 = map(int, input().split())

ans = "No"
if A1 * A2 == A3:
    ans = "Yes"
elif A1 * A3 == A2:
    ans = "Yes"
elif A2 * A3 == A1:
    ans = "Yes"

print(ans)
