arr = list(map(int, input().split()))

a = arr[0]
b = arr[1]
s=str(a)
num = a
while num != b:
    s+= ' '
    num+=2
    s+=str(num)
print(s)