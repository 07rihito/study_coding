from collections import defaultdict

N, M = map(int, input().split())
K = []
A = []
q = defaultdict(int)
for _ in range(N):
    temp = list(map(int, input().split()))
    K.append(temp[0])
    A.append(temp[1:])
    for i in range(temp[0]):
        q[temp[i + 1]] += 1
#print(f"{N=},{M=},{K=},{A=}")
#print(f"{q=}")

ans = 0
for key in q.keys():
    if q[key] == N:
        ans += 1

print(ans)