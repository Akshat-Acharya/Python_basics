name="Ram"
age=25
s1="My name is",name,"and my age is",age
s2="My name is"+name+"and my age is"+(str)(age)
s3="My name is {} and age is {}"
print(s3.format(name,age))
s4="My name is {1} and age is {0}"
print(s4.format(age,name))
s5="My name is {name} and age is {age} and city is {city}"
print(s5.format(name="Shyam",age=35,city="Indore"))
s6=f"My name is {name} and age is {age}"
print(s6)