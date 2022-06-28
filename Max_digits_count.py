x=int(input())
a=list(map(int,input().split()))
c=0
max=0
for i in range(x):
    if len(str(a[i]))>max:
        max=len(str(a[i]))
for i in range(x):
    if len(str(a[i]))==max:
        c=c+1
print(c)