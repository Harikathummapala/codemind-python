n,m= map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
p=[]
for i in a1:
    if i in a2 and i not in p:
        p.append(i)
print(*p)