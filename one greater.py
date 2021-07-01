dict={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d={}
for key,value in dict.items():
    if value>=175:
        d[key]=value
print(d)