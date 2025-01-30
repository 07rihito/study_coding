N = int(input())
h = list(map(int, input().split()))

ans = 0
while any(h):
    water_flag = False
#    print(f"{h=}")
    ans += 1
    for j in range(len(h)):
        if h[j] != 0:
            water_flag = True
        else:
            if water_flag:
                water_flag = False
                break
        
        if water_flag:
            h[j] -= 1
        

print(ans)