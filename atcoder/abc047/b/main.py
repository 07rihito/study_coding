#!/usr/bin/env python3

W, H, N = map(int, input().split())

Xmin = 0
Xmax = W
Ymin = 0
Ymax = H
ans = 0
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
#        Xmin = Xmin + (x - Xmin)
        Xmin = max(Xmin ,x)
    elif a == 2:
        Xmax = min(Xmax, x)
    elif a == 3:
        Ymin = max(Ymin, y)
    elif a == 4:
        Ymax = min(Ymax, y)
    
ans = max(0, (Xmax - Xmin)) * max(0, (Ymax - Ymin))
print(int(ans))
