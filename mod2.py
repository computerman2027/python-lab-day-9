def f1(x,y):
    if(y<=x):
        return f1(x-y,y)+1
    return 1

def f2(n,r):
    if(n>0 and r>0):
       return f2(n-1,r)+f2(n-1,r-1)
    return n+r

def f3(n):
    if n>1:
        return f3(n/2)+1
    return 0
def f4(m,n):
    if m==0 or (m>=n and n>=1):
        return 1
    else:
        return f4(m-1,n)+f4(m-1,n-1)

def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

def b(m,x):
    if(x==0):
        return 1
    elif(m>x):
        return fact(m)/(fact(x)*fact(m-x))
    else:
        return b(m,x-1)*((m-x+1)/x)
