# def sum(a):
#     if a==0:
#         return 0
#     else:
#         return (a%10+sum(a//10))
# print(sum(123))

# a=[2,4,[4,3],[8,1]]
# def sum(a):
#     i=0
#     for b in a:
#         if type(b)==list:
#             i=i+sum(b)
#         else:
#             i=i+b
#     return i
# print(sum(a))


# a=[2,4,[4,3],[8,1]]
# def fun(a):
#     i=0
#     b=[]
#     while i<len(a):
#         if type (a[i]) is list:
#             j=0
#             while j<len(a[i]):
#                 c=a[i][j]
#                 b.append(c)
#                 j=j+1
#         else:
#             s=a[i]
#             b.append(a[i])
#         i=i+1  
#     return  sum(b)
# print(fun([2,4,[4,3],[8,1]]))



# a=[2,4,[4,3],[8,1]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i]) == list:
#         j=0
#         c=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#     i=i+1  
# print(sum(b))


