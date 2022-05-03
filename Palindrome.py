x=int(input())
r=0
sum=0
a=x
while x>0:
    r=x%10
    sum=sum*10+r
    x=x//10
if sum==a:
    print("True")
else:
    print("False")
