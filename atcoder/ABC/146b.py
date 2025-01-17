n = int(input())
s = str(input())

def get_diff_char(a: str, b: int):
    result = ""
    temp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i, val in enumerate(temp):
        if val == a:
            ii = (i + b) % 26
            result = temp[ii]
            break
    return result

ans = ""
for i in list(s):
    ans += get_diff_char(i, n)

print(ans)