#!/usr/bin/env python3

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
ans = ["" for i in range(N)]

for i in range(N):
    hitoi = Q[i]
    target_index = P[i]
    temp_ans = Q[target_index - 1]
    ans[hitoi - 1] = str(temp_ans)
#    print(f"{hitoi=}, {target_index=}, {temp_ans=}, {ans=}")
    
print(" ".join(ans))
