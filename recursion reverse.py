def reverse(a):
    if len(a)==1:
        return a
    else:
        return reverse(a[1:])+a[0]
a=input("no")
print(reverse(a))

