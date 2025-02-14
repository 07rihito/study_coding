H, W = map(int, input().split())

if H == 1 or W == 1:
    print(max(H, W))
    exit()

ans = 0
for w in range(W):
    for h in range(H):
        if w % 2 == 0 and h % 2 == 0:
            ans += 1

print(ans)
