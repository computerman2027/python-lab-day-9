from mod2 import *

while(True):
    print("enter choice from 1 to 5 to select a function\nPress 6 to exit")
    ch=int(input())
    if(ch==1):
        x=int(input("Enter x :"))
        y=int(input("Enter y :"))
        print("f(x,y) =",f1(x,y))
    elif(ch==2):
        n=int(input("Enter n :"))
        r=int(input("Enter r :"))
        print("f(n,r) =",f2(n,r))
    elif(ch==3):
        n=int(input("Enter n :"))
        print("f(n) =",f3(n))
    elif(ch==4):
        m=int(input("Enter m :"))
        n=int(input("Enter n :"))
        print("f(n,r) =",f4(m,n))
    elif(ch==5):
        m=int(input("Enter m :"))
        x=int(input("Enter x :"))
        print("f(n,r) =",b(m,x))
    elif(ch==6):
        print("end")
        break
    else:
        print("Invalid input")
