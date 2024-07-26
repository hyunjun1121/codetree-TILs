n = int(input())

n_list = list(map(int, input().split()))
n

def middle(a):
    
    return n_list[int(a/2)]
    

for i in range(n):
    if i%2==0: #홀수 일 때
        print(middle(i), end= ' ')