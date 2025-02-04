#!/usr/bin/env python3

N = int(input())
T = []
A = []
ans = 0
old_t, old_a = 0, 0
for i in range(N):
    t, a = map(int, input().split())
    if i == 0:
        diff_t = 1
        diff_a = 1
    else:
        diff_t = old_t // t + 1 if old_t % t != 0 else old_t // t
        diff_a = old_a // a + 1 if old_a % a != 0 else old_a // a
    diff = max(diff_t, diff_a)
    old_t = diff * t
    old_a = diff * a
    ans = old_t + old_a
#    print(f"{t=}, {a=}, {diff=}, {old_t=}, {old_a=}, {ans=}")

print(ans)
