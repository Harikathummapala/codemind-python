s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s3=s1.split()
s4=s2.split()
p=[]
for i in s4:
    if i in s3:
        p.append(i)
print(*p)