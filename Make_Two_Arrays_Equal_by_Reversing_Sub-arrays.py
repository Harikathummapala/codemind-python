n=int(input())
l=list(map(int,input().split()))
m=int(input())
li=list(map(int,input().split()))
l=sorted(l)
li=sorted(li)
if m==n:
    c=0
    for i in range(n):
        if l[i]!=li[i]:
            c=1
            break
    if c==1:
        print("False")
    else:
        print("True")
else:
    print("False")