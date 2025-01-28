N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

As, Bs = zip(*sorted(zip(A, B)))
ans = 0
for i in range(N):
    if  Bs[i] <= M:
        ans += As[i] * Bs[i]
        M = M - Bs[i]
    else:
        ans += As[i] * (M % Bs[i])
        M = M - (M % Bs[i])
    if M == 0:
        break

print(ans)