#!/usr/bin/env python3
import itertools

S = input()
temp = [i for i in range(1, len(S))]
#print(f"{temp=}")

ans = int(S)
for i in range(1, len(S)):
    combs = itertools.combinations(temp, i)
    for comb in combs:
#        print(f"{comb=}")
        temp_index = 0
        for index in comb:
            index = int(index)
            ans += int(S[temp_index:index])
#            print(f"{S[temp_index:index]=}")
            temp_index = index
        ans += int(S[temp_index:])
        


print(ans)
