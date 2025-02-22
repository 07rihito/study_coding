#!/usr/bin/env python3

S = list(input())
for i in range(len(S) - 1, 0, -1):
#    print(f"{S[i-1]=}, {S[i]=}, {i=}")
    if S[i - 1] == "W" and S[i] == "A":
        S[i - 1] = "A"
        S[i] = "C"

print("".join(S))