N, Y = map(int, input().split())

ans = "-1 -1 -1"
skip_flag = False
for x in range(N + 1):
    for y in range(N - x + 1):
        total = x * 10000 + y * 5000 + (N - x - y) * 1000
        if total == Y:
            ans = f"{x} {y} {N - x - y}"
            skip_flag = True
        if skip_flag:
            break
    if skip_flag:
        break
        
print(ans)