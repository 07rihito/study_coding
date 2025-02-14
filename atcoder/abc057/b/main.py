#!/usr/bin/env python3

N, M = map(int, input().split())
ab = []
for i in range(N):
    a, b = map(int, input().split())
    ab.append([a,b])

cd = []
for i in range(M):
    c, d = map(int, input().split())
    cd.append([c,d])

#print(f"{ab=}")
#print(f"{cd=}")
for i in range(N):
    a = ab[i][0]
    b = ab[i][1]
    ans = 1
    manhattan = 0
    min_manhattan = 10 ** 20
    for j in range(M):
        c = cd[j][0]
        d = cd[j][1]
        manhattan = abs(a - c) + abs(b - d)
#        print(f"{i=}, {j=}, {min_manhattan=}, {manhattan=}")
        if manhattan < min_manhattan:
            ans = j + 1
            min_manhattan = manhattan
        
    print(ans)