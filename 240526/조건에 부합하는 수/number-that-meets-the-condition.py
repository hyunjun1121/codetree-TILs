a = int(input())
s=''
for i in range(a):
    num = i+1
    if not((num%2==0) and (num%4 != 0)) and not((num//8)%2==0) and not((num%7)<4):
        s+=str(num)
        s+= ' '
print(s.strip())