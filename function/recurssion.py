def fact(n) :
    if n == 1 :
        return 1
    return fact(n-1)*n

sqr = lambda a: a*a
add = lambda a,b : a+b
a = (int)(input("Enter the value for factorial : "))
print("factorial of",a,"is",fact(a))
print(sqr(a))
print(add(a,10))
