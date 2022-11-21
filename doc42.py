'''Q42. Find the sum of number digits in List.
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
The original list is : [15, 81, 11, 234]'''

def func(a):
    i=0
    b=[]
    while i<len(a):
        sum=0
        while a[i]>0:
            d=a[i]%10
            sum=sum+d
            a[i]=a[i]//10
        b.append(sum)
        i=i+1
    return b
print(func([12, 67, 98, 34]))
print(func([15, 81, 11, 234]))