N = int(input())
H = list(map(int, input().split()))

ans = 0
i = 0
while True:
    j = i
    while j < (N - 1) and H[j + 1] <= H[j]:
        j += 1
#    print(f"{i=},{j=}")
    if not j < N:
        break
    ans = max(ans, j - i)
    i = j + 1
print(ans)