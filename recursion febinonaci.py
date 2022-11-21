def fibonanci(a):
    if a<=1:
        return a
    else:
        return (fibonanci(a-1))+fibonanci(a-2)
n=int(input("no"))
if n>0:
    i=0
    while i<=n:
        print(fibonanci(i))
        i=i+1