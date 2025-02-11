#!/usr/bin/env python3

N, M = map(int, input().split())
A = []
B = []

for i in range(N):
    a = input()
    A.append(a)

for i in range(M):
    b = input()
    B.append(b)

ans = "No"
def check_in():
    for mi in range(M):
        for mj in range(M):
            if A[i + mi][j + mj] != B[mi][mj]:
                return False
            
        
    return True

result = False
for i in range(N - M + 1):
    for j in range(N - M + 1):
        if A[i][j] == B[0][0]:
            result = check_in()
        
        if result:
            print("Yes")
            exit()

print(ans)