list=[('yellow', 1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
a=[]
b={}
for i in list:
    if i[0] not in a:
        a.append(i[0])
    for k in a:
        c=[]
        for j in list:
            if j[0]==k:
                c.append(j[1])
        b[k]=c
print(b)

# a=[]
# b={}
# for i in list:
#     if i[0] not in a:
#         a.append(i[0])
#     for k in a:
#         c=[]
#         for j in list:
#             if j[0]==k:
#                 c.append(j[1])
#         b[k]=c
# print(b)