a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for a_index in range(a + 1):
    for b_index in range(b + 1):
        for c_index in range(c + 1):
            total = 500 * a_index + 100 * b_index + 50 * c_index
            if total == x:
                ans += 1

print(ans)