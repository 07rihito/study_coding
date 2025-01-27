
def convertNto10(n, num):
    num_str = str(num)
    result = 0
    for i in range(len(num_str)):
        j = i + 1
        result += pow(n, i) * int(num_str[-j])
    return result

def convert10toN(num, n):
    amari_list = []
    sho_old = -1
    while True:
        amari = num % n
        sho = num // n
        num = num // n
        if sho == sho_old:
            break
        amari_list.insert(0, str(amari))
        sho_old = sho
    amari_list.insert(0, str(sho))
    return int("".join(amari_list))

N, K = map(int, input().split())
for i in range(K):
    N_10 = convertNto10(8, N)
    N_9 = convert10toN(N_10, 9)
    N = int(str(N_9).replace("8", "5"))

print(N)