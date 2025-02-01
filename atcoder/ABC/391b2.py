def find_subgrid(S, T, N, M):
    for a in range(N - M + 1):
        for b in range(N - M + 1):
            match = True
            for i in range(M):
                for j in range(M):
                    if S[a + i][b + j] != T[i][j]:
                        match = False
                        break
                if not match:
                    break
            if match:
                print(a + 1, b + 1)  # 1-based index

# 入力例
N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(M)]

find_subgrid(S, T, N, M)
