n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    s=s+a[i]
m=s//n
for i in range(n):
    if a[i]==m:
        print("True")
        break
else:
    print("False")