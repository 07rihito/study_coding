s = input()

i = 0
ans = ""
s_list = []
while i < len(s):
    j = i + 1
    while j < len(s) and s[i] == s[j]:
        j += 1
#    s_list.append(s[i:j])
    ans += str(s[i]) + str(len(s[i:j]))
    i = j

print(ans)