x={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}
for k in x:
    if k in y:
        if x[k]==y[k]:
            print("1 is present in both x,y")
        