dict={"first":"1","second": "2","third": "1","four": "5","five":"5","six":"9","seven":"7"}
a=[]
for i in dict.values():
    if i not in a:
        a.append(i)
print(a)

# dict={"first":"1","second": "2","third": "1","four": "5","five":"5","six":"9","seven":"7"}
# list=[]
# c=0
# for i in dict.values():
#     if i not in list:
#         list.append(i)
#     if c==1:
#         list.append(i)
# print(list)