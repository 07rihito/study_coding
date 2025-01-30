from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
bc = defaultdict(int)

for a in A:
    bc[a] += 1

bc_v_sort = sorted(bc.items(), key=lambda x:x[1], reverse=True)
#print(bc_v_sort)
ans = 0
for i in range(K, len(bc_v_sort)):
#    print(f"{i=},{bc_v_sort[i]=},{bc_v_sort[i][1]=}")
    ans += bc_v_sort[i][1]
    
print(ans)