s = str(input())
t = str(input())

ans = "No"
for i in range(len(s)):
    if s == t:
        ans = "Yes"
        break
    s = s[-1] + s[:-1]

print(ans) 