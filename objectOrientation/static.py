class Test :
    @classmethod
    def show(self,a,b) : 
        print(a,b)
    @staticmethod
    def display(a,b,c) :
        print(a,b,c)

Test.display(10,20,30)
t1 = Test()
t1.show(10,20)
t1.display(10,20,30)
