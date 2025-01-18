s = str(input())
t = str(input())

ans = len(s)
for start in range(len(s) - len(t) + 1):
    diff = 0
    for i in range(len(t)):
        if t[i] != s[start + i]:
            diff += 1
    ans = min(ans, diff)


print(ans)