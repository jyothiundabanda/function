'''Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Uppercase characters : 3
No. of Lower case Characters : 12 '''

def list(l):
    i=0
    upper=0
    lower=0
    while i<len(l):
        d=l[i]
        if d.isupper():
            upper+=1
        if d.islower():
            lower+=1
        i=i+1
    print(upper)
    print(lower)
list('The quick Brow Fox')
