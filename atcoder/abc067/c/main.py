#!/usr/bin/env python3

N = int(input())
a = list(map(int,input().split()))

sunuke_sum = a[0]
arai_sum = sum(a[1:])
ans = abs(sunuke_sum - arai_sum)
for i in range(1, N - 1):
    sunuke_sum += a[i]
    arai_sum -= a[i]
    ans = min(ans, abs(sunuke_sum - arai_sum))

print(ans)
