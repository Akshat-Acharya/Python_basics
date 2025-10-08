d1 = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
print(d1,type(d1))
print()
print(d1.keys())
print()
print(d1.values())
print()
#key
print(d1[0]) 
print(d1.get(0))
print()
d1[1] = "first"
d1.update(2:"second")
print(d1)