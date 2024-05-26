arr = list(map(int,input().split()))
new_list = []
num = arr[0]
for i in range(arr[1]-arr[0]+1):
    if num %6==0 and num%8 !=0:
        new_list.append(num)
    num+=1
print(sum(new_list))