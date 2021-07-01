dict = {'a' : 'siri', 'b' : 'shirish', 'c': 'chinni'}
keys = []
values = []
items=dict.items()
for item in items:
    keys.append(item[0])
    values.append(item[1])
print ("keys :",(keys))
print ("values :",(values))