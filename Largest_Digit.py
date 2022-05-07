x=int(input())
d=0
while x>0:
    r=x%10
    if r>d:
        d=r
    x=x//10
print(d)
        