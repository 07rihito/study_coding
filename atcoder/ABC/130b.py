n, x = map(int, input().split())
l = list(map(int, input().split()))

ans = 1
d = 0
for i in range(2, n + 2):
    d = d + l[i - 2]
    if x < d:
        break
    ans += 1

print(ans)