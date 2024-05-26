n=int(input())
a =''
num=1
for i in range(n):
    a+=str(num)
    a+= ' '
    num+=1
a.strip()
print(a)