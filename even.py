dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for k in dict:
    a=dict[k]
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)
    dict[k]=b
print(dict)
