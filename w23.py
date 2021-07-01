data=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d={}
for a in data:
    if a['item'] not in d:
        d[a['item']]=a['amount']
    else:
        d[a['item']]+=a['amount']
print(d)

dic={}
for i in range(2):
    name=input("enter str")
    age=int(input("enter num"))
    marks=int(input("enter num"))
dic["name"]=name
dic["age"]=age
dic["marks"]=marks
print(dic)