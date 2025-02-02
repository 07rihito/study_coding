#!/usr/bin/env python3

N = int(input())
a = list(map(int, input().split()))

ans = pow(10, 10)
for i in range(101):
    pra_diff = 0
    mai_diff = 0
    for A in a:
        pra_diff += pow(A - i, 2)
        mai_diff += pow(A + i, 2)
    ans = min(ans, pra_diff, mai_diff)
print(ans)
