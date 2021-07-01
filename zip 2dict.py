keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
dict1=dict(zip(keys,values))
print(dict1)

keys=['red', 'green', 'blue']
values=['#FF0000','#008000', '#0000FF']
d={}
for i in range(len(keys)):
    d[keys[i]]=values[i]
print(d)

# set into dict
keys = {'Vlad Tepes', 'Alucard', 'Trevor', 'Isaac'}
values = {1, 2, 3, 4}
dictionary = dict(zip(keys,values))
print(dictionary)

d1={"a":100,"b":200,"c":100}
d2={"a":300,"b":200,"d":400}
d3=dict(d2)
d3.update(d1)
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=j+y
print(d3)