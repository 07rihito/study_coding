H, W = map(int, input().split())

ans = 0
if H == 1 or W == 1:
    ans = max(H, W)
else:
    for h in range(H):
        for w in range(W):
            if h % 2 == 0 and w % 2 == 0:
                ans += 1

print(ans)
