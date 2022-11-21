'''Q50. Make a split function 
Input :-[“i am anjali”]
Output :- [‘i’,’am’,’anjali’]'''

# def func(a):
#     i=0
#     b=[]
#     while i<len(a):
#         d=a.split()
#         # b.append(d)
#         i=i+1
#     return d
# print(func(["i am anjali"]))

# a="i am anjali"
# b=a.split()
# print(b)

# def fun(a):
#     print(a)
# def fun2(b):
#     fun(b)
# fun2(6)

# def fun(a):
#     def fun1(b):
#         return a*b
#     return fun1
# x=fun(10)
# print(x(5))

# def fun(x):
#     def func(y):
#         if symbol=="+":
#             return x + y
#         if symbol=="-":
#             return x-y
#         if symbol=="*":
#             return x*y
#     return func
# x=int(input("enter: "))
# y=int(input("enter :"))
# symbol=input("enter the symbol here:")
# a = fun(x)
# print(a(y))

# def fun(x):
#     def func(y):
#         return x+y
#     return func
# x=int(input("enter:"))
# y=int(input("enter:"))
# a=fun(x)
# print(a(y))

# def fun(x):
#     def func(y):
#         if symbol=="+":
#             return x + y
#         if symbol=="-":
#             return x-y
#         if symbol=="*":
#             return x*y
#     return func
# x=int(input("enter: "))
# y=int(input("enter :"))
# symbol=input("enter the symbol here:")
# a = fun(x)
# print(a(y))

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def floor(a,b):
    return a//b
def sub(a,b):
    return a-b
def div(a,b):
    return a%b
a=int(input("number1:"))
b=int(input("number2:"))
print("addition form:",add(a,b))
print("multiplication form:",multiply(a,b))
print("floor division form:",floor(a,b))
print("subtraction form:",sub(a,b))
print("division form:",div(a,b))