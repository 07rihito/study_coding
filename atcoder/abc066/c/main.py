#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    
    a_str = str(a[i])
    if i % 2 != 0:
        if n % 2 == 0:
            ans.insert(0, a_str)
        else:
            ans.append(a_str)
    else:
        if n % 2 == 0:
            ans.append(a_str)
        else:
            ans.insert(0, a_str)
    
#    print(f"{ans=}")
print(" ".join(ans))
