str="SHIRisha"
b=" "
i=0
while i<len(str):
    if str[i]>="A" and str[i]<="Z":
        b=b+str[i].lower()
    else:
        b=b+str[i].upper()
    i=i+1
print(b)



