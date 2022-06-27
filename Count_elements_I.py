n,m= map(int,input().split())
a1=set(map(int,input().split()))
a2=set(map(int,input().split()))
p=[]
c=list(a1)+list(a2)
for i in range(len(c)):
    if i  not in p and c.count(i)>1:
        p.append(i)
print(len(p))