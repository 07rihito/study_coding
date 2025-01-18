s, t = map(int, input().split())

ans = 0
for a in range(100 + 1):
    for b in range(100 + 1):
        for c in range(100 + 1):
            if a + b + c <= s and a * b * c <= t:
                ans += 1

print(ans)