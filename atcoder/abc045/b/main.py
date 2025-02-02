#!/usr/bin/env python3

A = input()
B = input()
C = input()

def cgame(player: list):
    if len(player) == 0:
        return 0, list()
    pcard = player[0]
    player = player[1:]
    return pcard, player

next = "a"
pairs = dict()
pairs["a"] = A
pairs["b"] = B
pairs["c"] = C
ans = ""
while True:
    old_card = next
    next, pairs[old_card] = cgame(pairs[next])
    if next == 0:
        ans = old_card.upper()
        break

print(ans)
