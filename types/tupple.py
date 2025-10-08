t1 = (10,20,30,40,50)
print(t1)
# to update we gotta convert it into list and then update 
l1 = (list)(t1)
l1.append(60)
t1 = (tuple)(l1)
print(t1)
#
t1 = ("Mango", "apple","banana","orange")
a,*b,c = t1
print(a)
print(b)
print(c)
