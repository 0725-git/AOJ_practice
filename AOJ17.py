while True:
    a,b = map(int,input().split())
    for i in range(a):
        for j in range(b):
            print("#",end="")
        print()
    print()
    if a == 0 and b == 0:
        break