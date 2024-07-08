n,m = map(int,input().split())

n_num = []
m_num=[]

for i in range(m):
    n_num.append(n*(i+1))
for i in range(n):
    m_num.append(m*(i+1))

for num in n_num:
    if num in m_num:
        print(num)
        break