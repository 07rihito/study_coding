#!/usr/bin/env python3
from collections import defaultdict

N, M = map(int, input().split())
cities = [0 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    cities[a - 1] += 1
    cities[b - 1] += 1

for city in cities:
    print(city)