n=int(input("enter num"))
i=1
a=[]
b={}
while i<=n:
    j=1
    c=[]
    while j<=10:
        d=i*j
        c.append(d)
        j=j+1
    b[i]=c
    i=i+1
print(b)