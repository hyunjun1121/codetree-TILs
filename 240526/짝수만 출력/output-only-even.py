arr=list(map(int,input().split()))
a= arr[0]
b=arr[1]
num = a
s = str(a)
while b != num:
    s += ' '
    num +=2
    s += str(num)
print(s)