dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
l={}
for i in dic1:
    if i in dic2:
        dic2[i]+=dic1[i]
l={**dic1,**dic2,**dic3}
print(l)
# antoer model
dic1={1:10, 2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic={}
for i in dic1:
    for j in dic2:
        dic={**dic1,**dic2,**dic3}
print(dic)
    