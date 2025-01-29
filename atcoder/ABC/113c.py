N, M = map(int, input().split())
A = [[] for _ in range(N)]
#print(f"{A=}")
for i in range(M):
    p, y = map(int, input().split())
    A[p - 1].append((y, i))
#print(f"{A=}")

ans = [0] * M
for i in range(N):
    elm = A[i]
    elm_sorted = sorted(A[i])
#    print(f"{A=}")
#    print(f"{elm=}, {elm_sorted=}")
    for j, k in enumerate(elm_sorted):
#        print(f"{j=},{k=}")
        ans[k[1]] = f"{i + 1:06}{j + 1:06}"

print(*ans)
