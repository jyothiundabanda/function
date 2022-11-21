'''Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):
"4",  "5" --> "9"
"34", "5" --> "39"
Notes:
If either input is an empty string, consider it as zero.'''

def string(a,b):
    i=0
    while i<len(a):
        d=int(a)+int(b)
        i=i+1
    return d
print(string("34", "5" ))
