s = input()
t = input()

s_sorted = sorted(s)
t_sorted = sorted(t, reverse=True)
#print(f"{s_sorted=},{t_sorted=},{s_sorted < t_sorted=}")
if s_sorted < t_sorted:
    print("Yes")
else:
    print("No")