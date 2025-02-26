#!/usr/bin/env python3

N = int(input())
ans = 1
max = 0
for i in range(1, N + 1):
    count = 0
    num = i
    while num % 2 == 0:
        
        count += 1
        num = num // 2
    
    
    if count > max:
        max = count
        ans = i
#        print(f"{max=}, {count=}, {ans=}")

print(ans)
