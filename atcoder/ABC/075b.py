h, w = map(int, input().split())
s = list()
for i in range(0, h + 2):
    if i == 0 or i == h + 1:
        s.append(list("-" * (w + 2)))
    else:
        temp = input()
        s.append(list("-" + temp + "-"))

ans = []
for x in range(1, len(s) - 1):
    ans_temp = ""
    for y in range(1, len(s[x]) - 1):
        count = 0
        if s[x][y] == "#":
            count = "#"
        else:
            if s[x - 1][y - 1] == "#":
                count += 1
            if s[x - 1][y] == "#":
                count += 1
            if s[x - 1][y + 1] == "#":
                count += 1

            if s[x][y - 1] == "#":
                count += 1
            if s[x][y + 1] == "#":
                count += 1

            if s[x + 1][y - 1] == "#":
                count += 1
            if s[x + 1][y] == "#":
                count += 1
            if s[x + 1][y + 1] == "#":
                count += 1
        ans_temp += str(count)
    ans.append(ans_temp)

for a in ans:
    print(a)