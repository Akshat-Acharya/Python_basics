class Test :
    def addAll(self,*a) :
        sum = 0
        print(type(a))
        for i in a :
            sum = sum + i
        return sum
    def add(self,a=0,b=0,c=0,d=0) :
        return a+b+c+d

t1 = Test()
print(t1.add(1,2,3))
print(t1.add(1,2,3,4))
print(t1.addAll(1,2,3,45,6,7,89,9))