#!/usr/bin/env python3

Q = int(input())
snake_list = [0]
left = 0
right = 0
for i in range(1, Q + 1):
    q = list(map(int, input().split()))
    if q[0] == 1:
        snake_list.append(snake_list[-1] + q[1])
#        print(f"{snake_list=}")
    elif q[0] == 2:
        left += 1
    elif q[0] == 3:
        print(snake_list[left + q[1] - 1] - snake_list[left])
#    print(f"{snake_list=}")
