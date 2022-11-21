'''Q6.Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8].'''

def list(l):
    i=0
    b=[]
    while i<len(l):
        if l[i]%2==0:
            b.append(l[i])
        i=i+1
    return b
print(list([1, 2, 3, 4, 5, 6, 7, 8, 9]))