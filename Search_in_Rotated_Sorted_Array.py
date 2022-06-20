x=int(input())
a=list(map(int,input().split()))
y=int(input())
c=0
for i in range(0,x):
    if y==a[i]:
        print(i)
        c=1
        break
if c==0:
    print(-1)