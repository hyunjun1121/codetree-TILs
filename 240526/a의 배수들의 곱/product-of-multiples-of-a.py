arr = list(map(int,input().split()))
a = arr[0]
b = arr[1]
new_list=[]
for i in range(b):
    if (i+1)%a ==0:
        new_list.append(i+1)
number = 1
for j in new_list:
    number *= j
print(number)