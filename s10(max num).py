my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
a=[]
for i in my_dict:
    a.append(i) 
a=[50,58,56,40,100,20]
b=len(a)
c=[]
i=0
while i<b:
    j=0
    while j<b:
        if a[j]>a[i]:
            if a[j] not in c:
                c.append(a[j])
        j=j+1
    break
    i=i+1
print(c)

