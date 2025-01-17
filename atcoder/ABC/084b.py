a, b = map(int, input().split())
s = str(input())

ans = "Yes"
if s[a] == "-":
    for i in range(len(s)):
        if i != a:
            if not s[i].isdecimal():
                ans = "No"
                break
else:
    ans = "No"

print(ans)