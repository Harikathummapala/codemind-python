x=int(input())
sum=0
sum1=0
a=list(map(int,input().split()))
for i in range(0,x):
    if i%2==0:
        sum+=a[i]
    else:
        sum1+=a[i]
if(sum-sum1)%4==0:
    print('X')
else:
    print('Y')
