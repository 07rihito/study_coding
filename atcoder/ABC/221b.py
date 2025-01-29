S = input()
T = input()


ans = "No"
if S == T:
    ans = "Yes"
else:
    count = 0
    for i in range(len(S) - 1):
        if S[i] != T[i]:
            temp = S[:i] + S[i + 1] + S[i] + S[i + 2:]
            if temp == T:
                ans = "Yes"
                break

print(ans)