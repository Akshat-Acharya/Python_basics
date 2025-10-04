class Test :
    def show(self) :
        print("Hello from show")
    def __init__(self) :
        print("Hello from constructor")
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        print(f"Name is {self.name} and age is {self.age}")

# Can only use one constructor at a time 
# There is a errorr in this code until u comment one of the constructor and object



t1 = Test()
t1.show()
print(t1)
t2 = Test('akshat',18)
