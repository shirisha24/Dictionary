# dict={0: 10, 1: 20}
# print(dict)
# dict.update({2:30})
# print(dict)

# dict={0:10,1:20}
# dict[2]=30
# print(dict)


# a=[1,2,3,4,5,6]
# b=["one","two","three","four","five"]
# i=0
# dict={}
# while i<len(b):
#     dict[a[i]]=b[i]
#     i=i+1
# dict.update({6:"six"})
# print(dict)


# a=[1,2,3,4,5,6]
# b=["one","two","three","four","five"]
# b.append("six")
# d=zip(a,b)
# print(dict(d))

a=[1,2,3,4,5,6]
b=["one","two","three","four","five"]
n=int(input("enter num"))
n1=input("enter num")
i=0
while i<len(a):
    a.append(n)
    b.append(n1)
    i=i+1
    c=dict(zip(a,b))
    break
print(c)


    