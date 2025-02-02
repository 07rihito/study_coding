#!/usr/bin/env python3

N, K = map(int, input().split())
D = list(map(int, input().split()))

for n in range(N, 100000000):
    match = True
    for i in list(str(n)):
        if int(i) in D:
            match = False
            break
    
    if match:
        print(n)
        exit()