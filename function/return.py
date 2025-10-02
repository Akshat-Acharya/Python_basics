def add(a,b) : 
    return a+b

def add(*a):    
#creates a tupple 
    sum=0
    for i in a :
        sum = sum+ i

    return sum

def show(**x) :
    print(x,type(x))


def xyz(c,d,a,b) :
    print(a,b,c,c,d)

print(add((int)(input("Enter first value : ")),(int)(input("Enter second value : "))))
print(add(1,23,5,67,674,24,2))
show(a=10,b=30,c=20,d=40)
xyz(a=20,b=10,c=30,d=90)