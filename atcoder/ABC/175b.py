n = int(input())
l = list(map(int, input().split()))

ans = 0
#a < b + c
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if i == j or i == k or j == k:
                continue
            
            if l[i] == l[j] or l[i] == l[k] or l[j] == l[k]:
                continue
            
            if l[i] < l[j] + l[k] and l[j] < l[i] + l[k] and l[k] < l[i] + l[j]:
                ans += 1
            
print(ans)