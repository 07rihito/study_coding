S = input()

ans = False
if S[0] == "A":
    if S[2:-1].count("C") == 1:
        S = S.replace("A", "")
        S = S.replace("C", "")
        if S.islower():
            ans = True

if ans:
    print("AC")
else:
    print("WA")