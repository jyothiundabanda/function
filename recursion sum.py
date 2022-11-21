def my_function(n):
    if n==0:
        return 0
    return my_function(n-1)+n
n=int(input("no"))
print(my_function(n))