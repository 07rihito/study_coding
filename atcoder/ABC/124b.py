n = int(input())
h_list = list(map(int, input().split()))

ans = 1
for x in range(1, n):
    is_count = True
    for y in range(0, x):
        if h_list[x] < h_list[y]:
            is_count = False
            break
    if is_count:
        ans += 1

print(ans)