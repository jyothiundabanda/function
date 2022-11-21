# def even(n):
#     if n%2==0 or n%2!=0:
#         s=0
#         while n>0:
#             c=n%10
#             s+=c
#             n//=10
#     return s
# num=int(input("no"))
# t=even(num)
# if t%2==0:
#     print("even")
# else:
#     print("odd")

def even(n):
    if n==0:
        return True
    elif n==1:
        return False
    else:
        return even(n%2)
num=int(input("no"))
if even(num):
    print(num,"even")
else:
    print(num,"odd")