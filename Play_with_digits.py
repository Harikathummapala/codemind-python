x=int(input())
a=list(map(int,input().split()))
sum=0
z=[]
for i in range(x):
    p=a[i]
    while(p):
        r=p%10
        p=p//10
        sum=sum+r
print(sum)