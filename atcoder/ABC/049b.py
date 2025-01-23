H, W = map(int, input().split())
C = []
for i in range(H):
    C.append(list(str(input())))

for h in range(2 * H):
    temp = ""
    for w in range(W):
        i = (h + 2) // 2 - 1
        j = w
        #print(f"{i=},{j=}")
        #print(C[i][j])
        temp += C[i][j]
    print(temp)