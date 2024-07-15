n,m = map(int, input().split())
n_list = list(map(int, input().split()))
m_list=[]
for i in range(m):
    a,b = map(int, input().split())
    c= 0
    for j in range(b-a+1):
        c += n_list[j+a-1]
    print(c)