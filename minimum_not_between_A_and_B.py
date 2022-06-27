x=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
min=999
c=0
for i in range(x):
    if arr[i]<a or arr[i]>b:
        c=c+1
        if arr[i]<min:
            min=arr[i]
if c==0:
    print(-1)
else:
    print(min)