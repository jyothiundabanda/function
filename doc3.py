'''Q3.Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Output : 20.'''

def list(l):
    i=0
    s=0
    while i<len(l):
        s=s+l[i]
        i=i+1
    return s
print(list((8, 2, 3, 0, 7)))
