dict={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
b=[]
for i in dict.values():
    b.append(i)
b1=[]
i=0
while i<4:
    j=0
    d={}
    for k in dict:
        d[k]=b[j][i]
        j=j+1
    b1.append(d)
    i=i+1
print(b1)
        
        