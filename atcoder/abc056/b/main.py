#!/usr/bin/env python3

W, a, b = map(int, input().split())

ans = 0
if a + W < b:
    ans = b - (a + W)
elif a <= b <= a + W:
    ans = 0
elif b + W < a:
    ans = a - (b + W)
    
print(ans)
