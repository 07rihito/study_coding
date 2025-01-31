import itertools

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
choices = itertools.combinations(A, 5)
for a,b,c,d,e in choices:
    wari = a % P * b % P * c % P * d % P * e % P
    if wari == Q:
        ans += 1
print(ans)