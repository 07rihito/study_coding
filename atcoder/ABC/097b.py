X = int(input())

ans = 0
for x in range(1, 1001):
    for y in range(2, 11):
        temp = x ** y
        if X < temp:
            break
        ans = max(ans, temp)
        #print(f"{x=},{y=},{ans=}")

print(ans)