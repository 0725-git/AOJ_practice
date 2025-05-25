a = list(map(int,input().split()))
if a[0] >= a[2]+a[4] and a[1] >= a[3]+a[4] and a[2] >= a[4] and a[3] >= a[4]:
    print("Yes")
else :
    print("No")