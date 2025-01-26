N, M, Q = map(int, input().split())
side = [ [] for i in range(N) ]
for i in range(M):
    u, v = map(int, input().split())
    side[u - 1].append(v - 1)
    side[v - 1].append(u - 1)
c = list(map(int, input().split()))
s = []
for i in range(Q):
    s.append(list(map(int, input().split())))


for i in range(Q):
    mode = s[i][0]
    x = s[i][1]
    if mode == 1:
        print(c[x - 1])
        for j in side[x - 1]:
            c[j] = c[x - 1]
    else:
        print(c[x - 1])
        c[x - 1] = s[i][2]