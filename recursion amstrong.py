def amrs(n):
    a=n
    s=0
    len=len(str(n))
    while n>0:
        r=n%10
        b=r**len
        s=s+b
        n=n//10
    if s==a:
        print("amstrong number")
    else:
        print("not")
amrs(153)

