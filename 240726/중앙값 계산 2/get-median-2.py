n = int(input())

n_list = list(map(int, input().split()))

def middle(i): 
    m_list= []
    for j in range(i+1):
        m_list.append(n_list[j])
    m_list.sort()
    
    return m_list[int(i/2)]    

for i in range(n):
    if i%2==0: #홀수 일 때
        print(middle(i), end= ' ')