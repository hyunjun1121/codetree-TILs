y,m,d = map(int, input().split())

def decide():
    if (y%4 ==0 and not (y%100==0)) or (y%4 ==0 and (y%100==0) and y%400==0):
        return 100
    else:
        return 0 
    


def weather(m):
    if 3<=m<=5:
        print('Spring')
    if 6<=m<=8:
        print('Summer')
    if 9<=m<=11:
        print('Fall')
    if m ==1 or m==2 or m==12:
        print('Winter')

a = 0
if m in [1, 3, 5, 7, 8, 10, 12]:
    if d >31:
        a+=1
        
elif m in [4, 6, 9, 11]:
    if d>30:
        a+=1
else:
    if decide() == 100:
        if d>29:
            a+=1
    else:
        if d>28:
            a+=1
if a >0:
    print(-1)