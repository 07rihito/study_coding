S = str(input())
N = len(S)

i = 0
words = []
while i < N:
    j = i + 1
#    print(f"{i=},{j=},{S[j]=}")
    while j < N and S[j].islower():
        j += 1
    words.append(S[i:j + 1])
    
    i = j + 1

print("".join(sorted(words, key=str.lower)))