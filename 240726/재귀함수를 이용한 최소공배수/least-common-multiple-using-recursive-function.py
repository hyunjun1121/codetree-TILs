n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()


def gcd(a,b):
    while a!= 0:
        b,a = a,b%a
    return b

def lcm(a,b):
    return (a*b)/gcd(a,b)






a = n_list[0]
for i in range(n-1):
    b= n_list[i+1]
    a = lcm(a,b)
print(int(a))