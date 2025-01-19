n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ht = [t - i * 0.006 for i in h]

ans = 0
abs_diff = 1000
for i in range(n):
    if abs(a - ht[i]) < abs_diff:
        abs_diff = abs(a - ht[i])
        ans = i + 1

print(ans)