while True:
    H,W = map(int,input().split())
    for i in range (H):
        for j in range (W):
            if (i+j) % 2 == 0:
                print("#", end="")
            else :
                print(".", end="")
        print()
    print()
    if H == 0 and W == 0:
        break