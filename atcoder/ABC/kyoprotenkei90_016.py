N = int(input())
A, B, C = map(int, input().split())

ans = 10000
for i in range(10000):
    for j in range(10000 - i):
        if N < i * A + j * B:
            break
        elif ans < i + j:
            break
        if (N - (i * A) - (j * B)) % C == 0:
            k = (N - (i * A) - (j * B)) // C
            if ans < i + j + k:
                break
            else:
                ans = min(ans, i + j + k)
        else:
            continue
print(ans)