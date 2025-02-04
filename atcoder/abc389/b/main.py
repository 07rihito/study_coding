#!/usr/bin/env python3

X = int(input())
ans = 1
i = 1
while True:
    ans *= i
    if ans == X:
        break
    i += 1

print(i)
