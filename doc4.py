'''Q4.Write a Python program to reverse a string.
Sample String : "1234abcd"
Output : "dcba4321".'''

def string(l):
    i=len(l)
    b=""
    while i>0:
        b=b+l[i-1]
        i=i-1
    return b
print(string("1234abcd"))