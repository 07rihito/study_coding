N, Q = map(int, input().split())
hato = [i for i in range(N)]
su = [1 for _ in range(N)]

ans = 0
for i in range(Q):
    q = input().split()
    if int(q[0]) == 2:
        print(ans)
    else:
        P = int(q[1]) - 1
        H = int(q[2]) - 1
        old_su = hato[P]
        su[old_su] -= 1
        hato[P] = H
        su[H] += 1
        if su[old_su] == 1:
            ans -= 1
        if su[H] == 2:
            ans += 1
        