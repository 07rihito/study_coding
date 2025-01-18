n = int(input())

ans = "No"
for x in range(1, 10):
    if n % x == 0:
        if (n // x) < 10:
            ans = "Yes"

print(ans)