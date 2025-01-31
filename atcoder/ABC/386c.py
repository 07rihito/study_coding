import sys
K = int(input())
S = input()
T = input()

k = 0
i = 0
ans = "No"
if S == T:
    print("Yes")
    sys.exit()

while k < K:
    j = i
    while j < min(len(S),len(T)) and S[j] == T[j]:
        j += 1
    if len(S) == len(T):
        #長さが同じでS中の任意の一文字を変更する
        s = list(S)
        s[j] = T[j]
        S = "".join(s)
    elif len(T) < len(S):
        #S中の文字を1つ選び、削除する
        S = S[:j] + S[j + 1:]
    elif len(S) < len(T):
        #S中の(先頭や末尾を含む)任意の位置に、任意の文字を1つ挿入する
        s = list(S)
        s.insert(j, T[j])
        S = "".join(s)
    else:
        pass
    
    k += 1
    if S == T:
        ans = "Yes"
        break

print(ans)

