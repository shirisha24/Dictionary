dict=[{'id' : 1, 'subject' : 'math', 'V' : 70,'VI' : 82},{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
# dict1={}
for i in dict:
    n=i.pop('V')
    n1=i.pop('VI')
    i['V+VI']=n+n1/2
print(dict)

 
