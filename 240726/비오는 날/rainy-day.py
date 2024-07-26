n = int(input())

for i in range(n):
    a = input().split()
    if a[2] == 'Rain':
        print(a[0]+' '+ a[1]+' '+a[2])
        break