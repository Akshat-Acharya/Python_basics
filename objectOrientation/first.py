class Test :
    a=10
t1 = Test()
t2 = Test()
print(t1.a)
print(t2.a)
print(Test.a)
t1.a = 100
t2.a = 1000
Test.a = 500
print(t1.a)
print(t2.a)
print(Test.a)
t3 = Test()
print(t3.a)