A = list(map(int, input().split()))
A_sorted = sorted(A)
B = []

ans = "No"
count = 0
for i in range(len(A)):
    if A[i] != A_sorted[i]:
        count += 1
        B.append(i)

if count == 2:
    if B[0] + 1 == B[1] or B[0] - 1 == B[1]:
        ans = "Yes"

print(ans)