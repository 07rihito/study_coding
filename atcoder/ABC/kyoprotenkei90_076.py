N = int(input())
A = list(map(int, input().split()))
total = sum(A)
k = total // 10
A = A + A

ans = "No"
if total % 10 != 0:
    pass
else:
    left = 0
    A_sum = 0
    for right in range(len(A)):
        A_sum += A[right]
        if k < A_sum:
            A_sum -= A[left]
            left += 1
        if k == A_sum:
            ans = "Yes"
            break

print(ans)