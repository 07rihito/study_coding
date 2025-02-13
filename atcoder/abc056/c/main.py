#!/usr/bin/env python3

X = int(input())

x = 0
for i in range(1, 1000000000):
    x += i
#    print(f"{i=}, {x=}")
    if X <= x:
        print(i)
        exit()
