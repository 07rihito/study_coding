K = int(input())
A, B = map(int, input().split())

def to10(num, k):
    num_str = str(num)
    result = 0
    for i in range(len(num_str)):
        j = i + 1
#        print(f"{i=}, {j=},{pow(k, i)=}, {num_str[-j]=}")
        result += pow(k, i) * int(num_str[-j])
    return result

a_10 = to10(A, K)
b_10 = to10(B, K)
print(a_10 * b_10)