dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20} 
max1=0
max2=0
max3=0
a=[]
for i in dict:
    for j in dict:
        if dict[j]>max1:
            max1=dict[j]
            max1_key=j
        elif max1>dict[j] and max2<dict[j]:
            max2=dict[j]
            max2_key=j
        elif max2>dict[j] and max3<dict[j]:
            max3=dict[j]
            max3_key=j
a.append(max1_key)
a.append(max2_key)
a.append(max3_key)
print(a)