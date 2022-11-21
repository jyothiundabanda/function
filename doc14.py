'''Q14.Write a function to check if a number is prime or not.'''
def prime(a):
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count=count+1
        i+=1
    if count==2:
        print("prime number")
    else:
        print("not")
    # return count
num=int(input("no"))
prime(num)




    