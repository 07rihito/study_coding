#!/usr/bin/env python3

N = int(input())
a = []
for i in range(N):
    temp = int(input())
    a.append(temp)

ans = -1
light = a[0]
count = 1
old = set()
while True:
#    print(f"{light=}, {old=}, {count=}")
    if light == 2:
        ans = count
        break
    
    if light in old:
        break
    else:
        old.add(light)
    
    light = a[light - 1]
    count += 1
    

print(ans)
