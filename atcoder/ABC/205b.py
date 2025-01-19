n = int(input())
a = list(map(int, input().split()))

a_sorted = sorted(a)
ans = "Yes"
for i in range(1, n + 1):
    if i != a_sorted[i - 1]:
        ans = "No"
        break

print(ans)