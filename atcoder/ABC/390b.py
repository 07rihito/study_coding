N = int(input())
A = list(map(int, input().split()))

ans = "Yes"
diff = A[1] / A[0]
temp = A[0]
for i in range(1, N):
    temp = temp * diff
    if A[i] != temp:
        ans = "No"

print(ans)