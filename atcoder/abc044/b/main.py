#!/usr/bin/env python3

w = input()
w_set = set(w)
#print(f"{w=},{w_set=},{w_set.count('a')=}")
ans = "Yes"
for word in w_set:
    if w.count(word) % 2 != 0:
        ans = "No"

print(ans)
