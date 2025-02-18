#!/usr/bin/env python3

N = int(input())
s = []
total = 0
for i in range(N):
    temp = int(input())
    s.append(temp)
    total += temp

s = sorted(s)
while True:
    
    if len(s) == 0:
        print(0)
        exit()
    
    if total % 10 != 0:
        print(total)
        exit()
    
    m = s.pop(0)
    if m % 10 != 0:
        total -= m