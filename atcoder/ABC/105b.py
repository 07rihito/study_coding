n = int(input())

ans = "No"
total = 0
for x in range(100):
    for y in range(100):
        total = x * 4 + y * 7
        if total == n:
            ans = "Yes"
            break
    

print(ans)