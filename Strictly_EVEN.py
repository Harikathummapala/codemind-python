n=int(input())
c=0
c2=0
a=list(map(int,input().split()))
for i in range(0,n):
    if i%2!=0 and a[i]%2==0:
        c2=c2+1
if c2>0:
    print(False)
else:
    print(True)