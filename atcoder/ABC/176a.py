N, X, T = map(int, input().split())

takoset = N // X
if N % X != 0:
    takoset += 1
print( takoset * T)