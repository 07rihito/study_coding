a, b = map(int, input().split())

a_str = str(a) * b
b_str = str(b) * a
#print(f"{a_str=},{b_str=}")
print(min(a_str, b_str))