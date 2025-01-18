p = list(map(int, input().split()))

s = [chr(64 + i) for i in p]
print("".join(s).lower())