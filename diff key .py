dic={'1':['a','b'], '2':['c','d']}
dic1=dic.get("1")
dic2=dic.get("2")
i=0
while i<len(dic1):
    j=0
    while j<len(dic2):
        a=dic1[i]+dic2[j]
        print(a)
        j=j+1
    i=i+1

dict={'1':['a','b'], '2':['c','d']}
for x in dict["1"]:
    for y in dict["2"]:
        print(x+y)