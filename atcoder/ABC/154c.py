from collections import defaultdict

N = int(input())
A = defaultdict(int)
ans = "YES"
for i in input().split():
    if 0 < A[i]:
        ans = "NO"
        break
    A[i] += 1

print(ans)