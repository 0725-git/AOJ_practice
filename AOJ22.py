count = [[[0 for i in range (10)]for j in range (3)]for k in range(4)]
n = int(input())
for _ in range(n) :
    b,f,r,v = map(int,input().split())
    count[b-1][f-1][r-1] += v
    
for k in range (4):
    for j in range (3):
        print(" ".join(str(count[k][j][i])for i in range(10)))
    if k != 3:
        print("#"*20)