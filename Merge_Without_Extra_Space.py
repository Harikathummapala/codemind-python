x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    c=arr+brr
    c=sorted(c)
    print(*c)
        