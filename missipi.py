# a="my name is siri"
n=input("enter string....")
d={}
for c in n:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)