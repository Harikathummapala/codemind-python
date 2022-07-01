m,n=map(int,input().split())
a=[]
e=0
o=0
for i in range(m):
    l=list(map(int,input().split()))
    if len(l)==n:
        a.append(l)
for i in range(m):
    for j in range(n):
        if i%2==0:
            e=e+a[i][j]
        else:
            o=o+a[i][j]
print(e,o)