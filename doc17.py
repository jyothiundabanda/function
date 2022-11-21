'''Q17. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )'''
def vote(age):
    if age>=18:
        return "eligible for vote"
    else:
        return "not"
b=int(input("no"))
print(vote(b))

