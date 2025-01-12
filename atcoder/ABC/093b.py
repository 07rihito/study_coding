a, b, k = map(int, input().split())

a_list = [i for i in range(a, a + k) if a <= i <= b]
b_list = [i for i in range(b - k + 1, b + 1) if a <= i <= b]
ab_set = set(a_list + b_list)
ab_list = sorted(ab_set)
[print(i) for i in ab_list]
