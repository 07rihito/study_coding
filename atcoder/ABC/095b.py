n, x = map(int, input().split())
m = [int(input()) for i in range(n)]

ans = 0
for i in range(n):
    if x - m[i] < 0:
        break
    x -= m[i]
    ans += 1

print(x // min(m) + ans)