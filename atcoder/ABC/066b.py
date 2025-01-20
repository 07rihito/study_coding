s = str(input())

ans = s[:-1]
while True:
    ans_len = len(ans)
    if ans_len % 2 == 0:
        if ans[:ans_len // 2] == ans[ans_len // 2:]:
            break
    ans = ans[:-1]
    if ans_len <= 1:
        break

print(ans_len)