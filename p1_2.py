# Write a program in Python using function (recursive and non recursive) which will calculate factorial of a number using function. The number is being passed as argument.

x = int(input("Enter number: "))
product = 1 
def fact(x):
    pro = 1
    for i in range(1, x+1):
        pro *= i
    return pro
def factrec(x):
    product = 1
    if x == 1:
        return 1
    product = product * x * factrec(x - 1)
    return product
product = factrec(x)
print("factorial =",product)