'''Q1.Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
list=['abc', 'xyz', 'aba', '1221']
result= 2.'''

def result(l):
    i=0
    s=0
    while i<len(l):
        d=l[i]
        k=d[::-1]
        if d==k:
            s=s+1
        i=i+1
    return s
print(result(['abc', 'xyz', 'aba', '1221']))
            


