#!/usr/bin/env python3

H, W = map(int, input().split())

print("#" * (W + 2))
for i in range(H):
    temp = input()
    print("#" + temp + "#")
print("#" * (W + 2))
