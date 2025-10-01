a=(int)(input("Enter a year : "))
print("leap year") if(a%4==0 and a%100 != 0 or a%400==0) else print("non leap year")