dict={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for x,y in dict.items():
    b=x.split()
    c=b[0]+b[1]
    d.update({c:y})
print(d)