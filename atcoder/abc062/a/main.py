#!/usr/bin/env python3

g1 = (1,3,5,7,8,10,12)
g2 = (4,6,9,11)
g3 = (2,)

x, y = map(int, input().split())

ans = "No"

if x in g1 and y in g1:
    ans = "Yes"
elif x in g2 and y in g2:
    ans = "Yes"
elif x in g3 and y in g3:
    ans = "Yes"

print(ans)
