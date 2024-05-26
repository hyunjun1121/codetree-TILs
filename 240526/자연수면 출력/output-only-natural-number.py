arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]

if a>=1:
    s = ''
    for i in range(b):
        s+=str(a)
    print(s)
else:
    print(0)