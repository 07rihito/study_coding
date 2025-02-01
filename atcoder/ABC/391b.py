N, M = map(int, input().split())
S = []
T = []

for _ in range(N):
    S.append(list(str(input())))

for _ in range(M):
    T.append(list(str(input())))

count = 0
for i in range(N - M + 1):
    for j in range(N - M + 1):
        match = True
        for x in range(M):
            for y in range(M):
                if S[i + x][j + y] != T[x][y]:
                    match = False
                    break
            if not match:
                break
        if match:
            print(i + 1, j + 1)
            exit()