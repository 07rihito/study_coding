K, N = map(int, input().split())
l = list(map(int, input().split()))

l_sorted = sorted(l, reverse=True)
ans = 0
for i in range(N):
    ans += l_sorted[i]

print(ans)