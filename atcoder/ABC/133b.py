n, d = map(int, input().split())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
ans = 0
for x_index in range(n):
    for y_index in range(x_index + 1, n):
        distance = 0
        temp_dis = 0
        for d_index in range(d):
            dis_2point = x[x_index][d_index] - x[y_index][d_index]
            temp_dis  += dis_2point ** 2
        distance = pow(temp_dis, 0.5)
        if distance.is_integer():
            ans += 1

print(ans)