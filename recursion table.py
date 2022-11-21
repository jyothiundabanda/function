def table(n,x):
    if n==1:
        return x
    return x+table(n-1,x)
n=int(input("no"))
x=int(input("no"))
print(table(n,x))