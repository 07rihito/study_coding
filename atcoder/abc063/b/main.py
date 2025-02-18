#!/usr/bin/env python3

S = input()
s = set(S.lower())

if len(S) == len(s):
    print("yes")
else:
    print("no")