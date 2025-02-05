#!/usr/bin/env python3

vowel = ("a", "e", "i", "o", "u")
c = input()

ans = "consonant"

if c in vowel:
    ans = "vowel"
print(ans)
