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
    print("pf =",product)
    return product
print("p =",product)
product2 = factrec(x)
print("p =",product)
print(product2)
