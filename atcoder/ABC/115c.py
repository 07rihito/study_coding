N, K = map(int, input().split())
h = []
for _ in range(N):
    h.append(int(input()))
h_sorted = sorted(h)
#print(f"{N=}, {K=}, {h=}, {h_sorted=}")
ans = 10 ** 9
for i in range(N - K + 1):
    ans = min(ans, h_sorted[i + K - 1] - h_sorted[i])
print(ans)