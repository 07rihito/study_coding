N, Q = map(int, input().split())
S = input()
a = [0] * (N + 1)
count = 0
for i in range(1, N):
    a[i + 1] = a[i] + (S[i - 1:i + 1] == "AC")
#print(f"{a=}")
for j in range(Q):
    l, r = map(int, input().split())
    print(a[r] - a[l])