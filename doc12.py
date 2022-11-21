'''Q12.Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105'''

def list(l):
    a=str(l)
    i=0
    while i<len(a):
        d=a[i]
        k=d%10
        i=i+1
    return k
print(list([1450,960000,1050]))