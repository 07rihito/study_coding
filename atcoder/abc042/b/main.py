#!/usr/bin/env python3

N, L = map(int, input().split())
S = [input() for _ in range(N)]
S = sorted(S, key=str.lower)

print("".join(S))
