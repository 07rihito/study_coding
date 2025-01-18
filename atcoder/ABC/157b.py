a = []
for i in range(3):
    a.append(list(map(int, input().split())))

n = int(input())
b = []
for i in range(n):
    b.append(int(input()))

for i in b:
    for j in range(3):
        for k in range(3):
            if i == a[j][k]:
                a[j][k] = "-"

ans = "No"
for i in range(3):
    if a[i][0] == "-" and a[i][1] == "-" and a[i][2] == "-":
        ans = "Yes"
    if a[0][i] == "-" and a[1][i] == "-" and a[2][i] == "-":
        ans = "Yes"
if a[0][0] == "-" and a[1][1] == "-" and a[2][2] == "-":
    ans = "Yes"
if a[0][2] == "-" and a[1][1] == "-" and a[2][0] == "-":
    ans = "Yes"

print(ans)