N = int(input())
d = list(map(int, input().split()))
d_sorted = sorted(d)
cent= N // 2
#print(f"{N=}, {cent=}, {d=}, {d_sorted=}")
ans = 0
if N % 2 == 0:
    ans = d_sorted[cent] - d_sorted[cent - 1]

print(ans)