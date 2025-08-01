b=int(input("Enter a number: "))
def fact(b):

    fact=1
    for i in range(1,b+1):
        fact*=i
    return fact


print("Factorial of",b,"is: ",fact(5))

