a , b = map(int,input().split())
if a>b:
    c = a
    a = b
    b = c
a+=10
b = b*2
print(a,b)