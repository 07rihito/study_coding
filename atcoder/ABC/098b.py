N = int(input())
S = str(input())

ans = 0
for i in range(1, N):
    count = 0
    X = S[:i]
    Y = S[i:]
    x = set(X)
    y = set(Y)
    for j in x:
        if j in y:
            count += 1
    ans = max(ans,count)
    #print(f"{X=},{Y=},{x=},{y=},{ans=},{count=}")
print(ans)