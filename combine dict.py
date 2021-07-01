dict1={"a":100,"b":200,"c":300}
dict2={"a":300,"b":200,"d":400}
d3=dict(dict1)
d3.update(dict2)
for i,j in dict1.items():
    for x,y in dict2.items():
        if i==x:
            d3[i]=(j+y)
print(d3)