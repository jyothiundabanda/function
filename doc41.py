'''Q40. Write a function For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1.


Q41. Write a Python program to find the list with maximum and minimum length.
Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])'''

def func(l):
    i=0
    max=l[i]
    min=l[i]
    while i<len(l):
        if l[i]>max:
            max=l[i]
        if l[i]<min:
            min=l[i]
        i=i+1
    print([len(max),max])
    print([len(min),min])
func([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
