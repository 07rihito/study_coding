#!/usr/bin/env python3
N = int(input())
a = list(map(int, input().split()))

highRate = 0
count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for rate in a:
    if rate < 400:
        count[0] = 1
    elif rate < 800:
        count[1] = 1
    elif rate < 1200:
        count[2] = 1
    elif rate < 1600:
        count[3] = 1
    elif rate < 2000:
        count[4] = 1
    elif rate < 2400:
        count[5] = 1
    elif rate < 2800:
        count[6] = 1
    elif rate < 3200:
        count[7] = 1
    else:
        count[8] += 1

color_max = sum(count)
if count[8] == 0:
    color_min = sum(count)
else:
    color_min = sum(count[:7]) + 1
    
print(color_min, color_max)