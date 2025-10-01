h=(int)(input("Enter marks of Hindi : "))
e=(int)(input("Enter marks of English : "))
m=(int)(input("Enter marks of Maths : "))
s=(int)(input("Enter marks of Science : "))
t=h+s+e+m
a=t/4;
print("Total marks are",t,"and average marks are",a)
if a>90 and a<=100 : 
    print("Excellent")
elif(80<a<=90) :
    print("Very good")
elif 70<a<=80 :
    print("good")
elif 60<a<=70 : 
    print("average")
else :
    print("Try again")