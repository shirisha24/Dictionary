dict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
b=set()
for i in dict:
    for keys,values in i.items():
        b.add(values)
print(b)