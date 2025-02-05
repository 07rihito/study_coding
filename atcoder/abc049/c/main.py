#!/usr/bin/env python3

words = ("dream" "dreamer" "erase" "eraser")
S = input()
ans = "YES"
while True:
    L = len(S)
    if L < 1:
        break
    
    if L < 5:
        ans = "NO"
        break
    
    j = 0
    if S[-1] == "r":
        if S[-3] == "s":
            j = -6
        else:
            j = -7
    elif S[-1] == "m":
        j = -5
    elif S[-1] == "e":
        j = -5
    else:
        ans = "NO"
        break
    
    word = S[j:]
    S = S[:j]
#    print(f"{j=}, {word=}, {S=}")
    if not word in words:
        ans = "NO"
        break

print(ans)
