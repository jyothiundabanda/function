'''Q49. Write a flowchart which takes an input N. Then input N numbers. Then for each of the N numbers, print “even” if the number is even or and “odd” if the number is odd.
Sample input:
7
1
4
23
95
1203
403
84
Sample output:
Odd
Even
Odd
Odd
Odd'''

def fun(a):
    i=0
    while i<=n:
        if i%2==0:
            print("even")
        else:
            print("odd")
        i=i+1
n=int(input("no"))
fun(n)