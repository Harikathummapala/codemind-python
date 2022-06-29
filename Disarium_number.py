a=int(input())
sum=0
b=1

for i in str(a):
    sum=sum+int(i)**b
    b=b+1
if(a==sum):
    print("True")
else:
    print("False")