N = int(input())
S = input()

i = 0
ans = 0
j = 0
while j < N:
    j = i
#    print(f"{i=},{j=},{S[i]=},{S[j]=}")
    while S[i] == S[j] and j < N:
        j += 1
        if N <= j:
            break

    ans += 1
    i = j

print(ans)