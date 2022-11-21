'''Q40. Write a function For example, if we give 9119  the function should return
  811181, as the  square of 9 is 81 and square of 1  is 1.'''

def func(n):
    i=0
    while n>0:
        r=n%10
        i=i*10+r
        n=n//10
    k=i
    while k>0:
      m=k%10
      v=m**2
      k=k//10
      print(v,end="")
n=int(input("no"))
func(n)