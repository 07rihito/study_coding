N, Q = map(int, input().split())
su = [1 for _ in range(N)]
hato = [ i for i in range(N)]

ans = 0
for i in range(Q):
    query = input().split()
    if query[0] == "2":
        print(ans)
    else:
        P = int(query[1]) - 1
        H = int(query[2]) - 1
        old_su = hato[P]
        su[old_su] -= 1
        su[H] += 1
        hato[P] = H
        if su[H] == 2:
            ans += 1
        if su[old_su] == 1:
            ans -= 1
