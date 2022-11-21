'''
Q25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.
Example:
list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3'''

def count(list):
    i=0
    p=0
    n=0
    while i<len(list):
        d=list[i]
        if d>0:
            p+=1
        else:
            n+=1
        i=i+1
    print("positive",p)
    print("negative",n)
count([2, -7, 5, -64, -14])